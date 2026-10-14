#!/usr/bin/env python3
"""Rebuild Stage 5 machine evidence from Stage 4 registry and 71 PubChem descriptions.
No human scientific adjudications, no inferred provenance independence.
"""
import csv, hashlib, json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"data/R1_43pair_stage4_source_registry.csv"
RAW=ROOT/"raw_pubchem"
OUT=ROOT/"stage5_out"
OUT.mkdir(parents=True,exist_ok=True)
def csvrows(p):
    with p.open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
def save(name,rows):
    with (OUT/name).open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def grants(d):
    found=list(d.get("grant_number",[]) or [])
    for line in d.get("description",[]):
        m=re.search(r"Grant (?:Proposal )?Number\s*:\s*(.+)",str(line),re.I)
        if m:found.append(m.group(1).strip())
    return set(re.sub(r"[^A-Z0-9]","",str(x).upper()) for x in found if x)
def xrefs(d):
    return set(int(x["xref"]["aid"]) for x in d.get("xref",[])
               if isinstance(x.get("xref"),dict) and str(x["xref"].get("aid","")).isdigit())
def mentions(d,aid):
    pattern=r"(?<!\d)"+str(aid)+r"(?!\d)"
    return [f"{k}[{i}]" for k in ("description","protocol","comment")
            for i,line in enumerate(d.get(k,[])) if re.search(pattern,str(line))]
data={}; metadata=[]
source_log={r["aid"]:r for r in csvrows(RAW/"retrieval_log.csv")}
for p in sorted(RAW.glob("AID_*.description.json")):
    aid=int(p.name.split("_")[1].split(".")[0]);raw=p.read_bytes()
    sha=hashlib.sha256(raw).hexdigest()
    assert source_log[str(aid)]["sha256"]==sha, "SHA256 mismatch for "+str(aid)
    d=json.loads(raw)["PC_AssayContainer"][0]["assay"]["descr"]
    assert int(d["aid"]["id"])==aid
    data[aid]=(d,sha)
    center=d.get("aid_source",{}).get("db",{})
    metadata.append(dict(aid=aid,source_url=f"https://pubchem.ncbi.nlm.nih.gov/bioassay/{aid}",
        raw_sha256=sha,assay_name=d.get("name",""),depositor=center.get("name",""),
        source_identifier=center.get("source_id",{}).get("str",""),
        grants=";".join(sorted(grants(d))),source_aids=";".join(map(str,sorted(xrefs(d)))),
        human_verified="NO"))
source=csvrows(SRC)
assert len(source)==43 and len(data)==71
result=[];blind=[]
for s in source:
    a,b=int(s["aid_a"]),int(s["aid_b"]);dA,shaA=data[a];dB,shaB=data[b]
    cA=dA.get("aid_source",{}).get("db",{});cB=dB.get("aid_source",{}).get("db",{})
    common=sorted(grants(dA)&grants(dB));xA=b in xrefs(dA);xB=a in xrefs(dB)
    mA=mentions(dA,b);mB=mentions(dB,a)
    result.append(dict(pair_key=s["pair_key"],aid_a=a,aid_b=b,target=s["target"],
        recorded_depositor_match=str(cA.get("name")==cB.get("name")),
        recorded_common_grants=";".join(common),
        source_id_a=cA.get("source_id",{}).get("str",""),
        source_id_b=cB.get("source_id",{}).get("str",""),
        a_xref_b=str(xA),b_xref_a=str(xB),
        a_text_mentions_b=";".join(mA[:8]),b_text_mentions_a=";".join(mB[:8]),
        source_url_a=f"https://pubchem.ncbi.nlm.nih.gov/bioassay/{a}",
        source_url_b=f"https://pubchem.ncbi.nlm.nih.gov/bioassay/{b}",
        source_sha256_a=shaA,source_sha256_b=shaB,
        historical_label_UNVALIDATED=s["historical_provenance_label_FROZEN_DO_NOT_OVERRIDE"],
        historical_compatibility=s["historical_compatibility_label_FROZEN"],
        measurement_reuse="NOT_ASSESSED",independent_execution="NOT_ASSESSED",
        independent_programs="NOT_ASSESSED",human_reviewer1="",
        human_reviewer2="",independent_expert_consensus="",
        stage5_status="PENDING_EXPERT_ADJUDICATION"))
    blind.append(dict(pair_key=s["pair_key"],aid_a=a,aid_b=b,target=s["target"],
        source_url_a=f"https://pubchem.ncbi.nlm.nih.gov/bioassay/{a}",
        source_url_b=f"https://pubchem.ncbi.nlm.nih.gov/bioassay/{b}",
        source_sha256_a=shaA,source_sha256_b=shaB,
        reviewer_id="",copied_measurements="",separate_execution="",
        independent_programs="",final_classification="",evidence_location="",
        rationale="",review_date=""))
assert len({r["target"] for r in result})==29
assert sum(bool(r["recorded_common_grants"]) for r in result)==43
assert sum(r["a_xref_b"]=="True" or r["b_xref_a"]=="True" for r in result)==14
assert all(r["stage5_status"]=="PENDING_EXPERT_ADJUDICATION" for r in result)
save("R1_Stage5_43pair_machine_evidence.csv",result)
save("R1_Stage5_71aid_metadata.csv",metadata)
save("R1_Stage5_BLINDED_expert_form.csv",blind)
summary=dict(n_pairs=len(result),n_aids=len(data),n_targets=29,
    shared_grants=43,direct_aid_xrefs=14,hashes_verified=71,
    independent_expert_adjudications=0)
(OUT/"summary.json").write_text(json.dumps(summary,indent=2)+"\n")
print("Stage 5 integrity PASS:",summary)
