#!/usr/bin/env python3
"""Stage 6B public PubChem result-row pilot. Python stdlib only.
Never equate overlapping CID or matching potency with identical raw measurements.
"""
import csv, hashlib, io, json, math, os, statistics, time, urllib.request, urllib.error
from collections import defaultdict, Counter
from datetime import datetime, timezone
from pathlib import Path

PAIRS=[
 ("P01","851","856","S1P2 functional assay vs CRE-BLA interference counterscreen"),
 ("P02","624326","624327","FAS-TE kinetic vs endpoint fluorescence"),
 ("P04","504699","504701","OX1R calcium vs HTRF functional readout"),
 ("P09","602166","602234","SRC3 project branches; LogIC50 unit warning"),
 ("P11","540322","652211","KCNK9/TASK3 potentially separate programs"),
 ("P18","652164","652165","FAS-TE endpoint vs kinetic assay"),
]
BASE="https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/{}/{}"
OUT=Path("r1_stage6b/generated")
RAW=OUT/"raw";RAW.mkdir(parents=True,exist_ok=True)
MANIFEST=[]; DATA={}; STATS=[]
def retrieve(aid,mode):
 url=BASE.format(aid, "concise/CSV" if mode=="concise" else "CSV")
 dest=RAW/f"AID_{aid}.{mode}.csv"
 last=""
 for attempt in range(3):
  try:
   req=urllib.request.Request(url,headers={"User-Agent":"AssayProvenanceAudit/1.0 (academic research; PubChem PUG REST)","Accept":"text/csv"})
   with urllib.request.urlopen(req,timeout=100) as response:
    http=response.status; payload=response.read(60*1024*1024+1)
    if len(payload)>60*1024*1024: raise ValueError("MAX_60MB_EXCEEDED")
    ct=response.headers.get("Content-Type","")
   txt=payload.decode("utf-8-sig")
   rows=list(csv.DictReader(io.StringIO(txt)))
   headers=list(rows[0]) if rows else (next(csv.reader(io.StringIO(txt)),[]) if txt.strip() else [])
   if not rows or not headers: raise ValueError("NO_DATA_ROWS_OR_HEADERS")
   if not any("sid" in h.lower() for h in headers): raise ValueError("NO_SID_COLUMN")
   dest.write_bytes(payload)
   return {"aid":aid,"mode":mode,"status":"OK","url":url,"http_status":http,"sha256":hashlib.sha256(payload).hexdigest(),
     "bytes":len(payload),"rows":len(rows),"headers":" | ".join(headers),"error":""},rows
  except Exception as exc:
   last=(type(exc).__name__+": "+str(exc))[:280]
   if attempt<2:time.sleep(2*(attempt+1))
 return {"aid":aid,"mode":mode,"status":"ERROR","url":url,"http_status":"",
    "sha256":"","bytes":0,"rows":0,"headers":"","error":last},[]
def col(row, candidates):
 l={str(k).strip().lower().replace("_"," ").replace("  "," "):v for k,v in row.items()}
 for name in candidates:
  key=name.lower().replace("_"," ")
  if key in l:return str(l[key] or "").strip()
 return ""
def indexed(rows):
 cid=defaultdict(list);sid=defaultdict(list); outcome=Counter(); col_meta=Counter()
 for r in rows:
  c=col(r,["CID","PUBCHEM_CID"]); s=col(r,["SID","PUBCHEM_SID"])
  if c and c not in ("0","-1"):cid[c].append(r)
  if s:sid[s].append(r)
  x=col(r,["Activity Outcome","PUBCHEM_ACTIVITY_OUTCOME"])
  if x:outcome[x]+=1
  unit=col(r,["Activity Name"])
  if unit:col_meta[unit]+=1
 return cid,sid,outcome,col_meta
def median_value(records):
 vals=[]
 for r in records:
  v=col(r,["Activity Value [uM]","Activity Value (uM)"])
  try:
   x=float(v)
   if math.isfinite(x) and x>0:vals.append(x)
  except:pass
 return statistics.median(vals) if vals else None
def pair_summary(pair):
 pid,a,b,context=pair
 ra=DATA.get((a,"concise"),[]);rb=DATA.get((b,"concise"),[])
 ca,sa,oa,na=indexed(ra);cb,sb,ob,nb=indexed(rb)
 shared=sorted(set(ca)&set(cb),key=lambda z:int(z) if z.isdigit() else z)
 sharedsid=set(sa)&set(sb)
 vals=[]
 outcomes=[]
 for c in shared:
  x=median_value(ca[c]);y=median_value(cb[c])
  if x is not None and y is not None: vals.append((x,y))
  aa={col(r,["Activity Outcome","PUBCHEM_ACTIVITY_OUTCOME"]) for r in ca[c]}
  bb={col(r,["Activity Outcome","PUBCHEM_ACTIVITY_OUTCOME"]) for r in cb[c]}
  if len(aa)==1 and len(bb)==1 and "" not in aa and "" not in bb:outcomes.append(next(iter(aa))==next(iter(bb)))
 exact_values=sum(1 for x,y in vals if abs(x-y)<=max(1e-12,1e-8*max(x,y)))
 logd=[abs(math.log10(x/y)) for x,y in vals]
 complete=bool(ra and rb)
 return {
 "pair":pid,"aid_a":a,"aid_b":b,"context":context,
 "concise_a_status":next((r["status"] for r in MANIFEST if r["aid"]==a and r["mode"]=="concise"),"MISSING"),
 "concise_b_status":next((r["status"] for r in MANIFEST if r["aid"]==b and r["mode"]=="concise"),"MISSING"),
 "result_row_a":len(ra),"result_row_b":len(rb),
 "unique_cid_a":len(ca),"unique_cid_b":len(cb),"shared_cids_from_results":len(shared) if complete else "",
 "shared_sids_from_results":len(sharedsid) if complete else "",
 "cid_level_outcome_comparable_count":len(outcomes),
 "cid_level_outcome_agreement_count":sum(outcomes),
 "matched_positive_uM_values_count":len(vals),
 "matched_exact_uM_values_count":exact_values,
 "median_abs_log10_potency_difference":round(statistics.median(logd),6) if logd else "",
 "activity_names_a":";".join(na.keys())[:400],"activity_names_b":";".join(nb.keys())[:400],
 "outcomes_a":json.dumps(oa,sort_keys=True),"outcomes_b":json.dumps(ob,sort_keys=True),
 "source_url_a":BASE.format(a,"concise/CSV"),"source_url_b":BASE.format(b,"concise/CSV"),
 "source_status":"RESULT_ROWS_RECOVERED" if complete else "INCOMPLETE",
 "raw_measurement_reuse":"UNRESOLVED","execution_identity":"UNRESOLVED",
 "provenance_gold_standard":"NO__NOT_ESTABLISHED",
 "interpretation_guardrail":"CID/SID overlap, matched outcomes or potency do not prove reused laboratory measurements; use full raw readout, dates, plates and fit inputs to determine reuse."
 }
def write_csv(path,rows,cols=None):
 if not rows and not cols:return
 with open(path,"w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=cols or list(rows[0].keys()),extrasaction="ignore")
  w.writeheader();w.writerows(rows)
def main():
 ids=list(dict.fromkeys(x for p in PAIRS for x in p[1:3]))
 for aid in ids:
  for mode in ("concise","full"):
   rec,rows=retrieve(aid,mode);MANIFEST.append(rec);DATA[(aid,mode)]=rows
   print("RESULT",aid,mode,rec["status"],rec["rows"],rec["error"],flush=True)
   time.sleep(0.75)
 summary=[pair_summary(p) for p in PAIRS]
 write_csv(OUT/"retrieval_manifest.csv",MANIFEST)
 write_csv(OUT/"pair_result_audit.csv",summary)
 timestamp=datetime.now(timezone.utc).isoformat()
 totals={"retrieval_timestamp_utc":timestamp,"pilot_pairs":len(PAIRS),"unique_aids":len(ids),
 "concise_success":sum(r["status"]=="OK" and r["mode"]=="concise" for r in MANIFEST),
 "full_success":sum(r["status"]=="OK" and r["mode"]=="full" for r in MANIFEST),
 "pairs_both_concise_recovered":sum(r["source_status"]=="RESULT_ROWS_RECOVERED" for r in summary),
 "provenance_confirmed_reuse_pairs":0,"provenance_confirmed_distinct_pairs":0,
 "interpretation":"Quantitative result-row comparisons only. No external provenance gold standards, verified raw measurement reuse, or plate/run identities."
 }
 (OUT/"run_summary.json").write_text(json.dumps(totals,indent=2),encoding="utf-8")
 (OUT/"results.README.md").write_text("# Stage 6B primary result-row retrieval pilot\n\n"
 "Original PubChem PUG REST result CSVs in raw/; hashes and HTTP errors in retrieval_manifest.csv.\n"
 "Overlap metrics in pair_result_audit.csv are descriptive. Matching outcomes or numerical results cannot be used alone as labels for experimental data reuse.\n"
 "Inspect full result rows to identify potency fields and deposit-specific unit metadata. Confirm plate/run identities separately.\n\n"
 +json.dumps(totals,indent=2)+"\n",encoding="utf-8")
 if totals["pairs_both_concise_recovered"]==0:print("WARNING: NO_COMPLETE_PAIR_RESULTS; ANALYSIS_MUST_NOT_CLAIM_SUCCESS",flush=True)
if __name__=="__main__":main()
