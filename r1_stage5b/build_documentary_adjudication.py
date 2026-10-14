#!/usr/bin/env python3
"""R1 5B documentary pair-review report from archived PubChem JSON.
No independent reviewer decisions; descriptions do not prove execution identity.
"""
from pathlib import Path
import csv, json, hashlib, re
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"/"R1_43pair_stage4_source_registry.csv"
NOTES=ROOT/"r1_stage5b/data/43pair_documentary_interpretations.csv"
RAW=ROOT/"raw_pubchem"
OUT=ROOT/"r1_stage5b/generated"
OUT.mkdir(parents=True,exist_ok=True)
def load(path):
    with path.open(newline="",encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))
def save(path,rows):
    with path.open("w",newline="",encoding="utf-8") as fh:
        writer=csv.DictWriter(fh,fieldnames=list(rows[0]))
        writer.writeheader();writer.writerows(rows)
def find_grants(d):
    sources=list(d.get("grant_number",[]) or [])
    for line in d.get("description",[]) or []:
        m=re.search(r"Grant (?:Proposal )?Number\s*:\s*(.+)",str(line),re.I)
        if m:sources.append(m.group(1))
    vals={re.sub("[^A-Z0-9]","",str(x).upper()) for x in sources if str(x).strip()}
    return vals|{x[1:] for x in vals if x.startswith("1R")}
def excerpt(d):
    for field in ("protocol","description"):
        for i,text in enumerate(d.get(field,[])):
            for match in re.finditer(r"purpose of this assay|objective of the current|powder samples|set 2|late stage|purpose of this biochemical",str(text),re.I):
                start=max(0,match.start()-35);end=min(len(text),match.start()+260)
                if end-start>65:return f"{field}[{i}]@{start}:{end}",text[start:end]
    for field in ("description","protocol"):
        for i,text in enumerate(d.get(field,[])):
            if len(str(text))>75:return f"{field}[{i}]@0:{min(260,len(text))}",text[:260]
    return "name",d.get("name","")
def crossref(d,aid):
    return any(item.get("xref",{}).get("aid")==aid for item in d.get("xref",[]))
pairs=load(DATA);notes=load(NOTES);log=load(RAW/"retrieval_log.csv")
assert len(pairs)==len(notes)==43 and len(log)==71
assert len({x["pair_key"] for x in pairs})==43
sha={int(x["aid"]):x["sha256"] for x in log}
doc={}
for aid,digest in sha.items():
    by=(RAW/f"AID_{aid}.description.json").read_bytes()
    assert hashlib.sha256(by).hexdigest()==digest,(aid,"SHA256 mismatch")
    desc=json.loads(by)["PC_AssayContainer"][0]["assay"]["descr"]
    assert int(desc["aid"]["id"])==aid
    doc[aid]=desc
assert len(doc)==71
evidence=[];excerpts=[];blind=[]
for index,(pair,note) in enumerate(zip(pairs,notes),1):
    a,b=map(int,[pair["aid_a"],pair["aid_b"]])
    assert a==int(note["aid_a"]) and b==int(note["aid_b"]), ("Pair order drift",index)
    da,db=doc[a],doc[b];ka,qa=excerpt(da);kb,qb=excerpt(db)
    for aid,d,k,q in [(a,da,ka,qa),(b,db,kb,qb)]:
        if k!="name":
            m=re.fullmatch(r"(protocol|description)\[(\d+)\]@(\d+):(\d+)",k)
            assert m,(aid,k)
            f,i,x,y=m.group(1),*map(int,m.groups()[1:])
            assert d[f][i][x:y]==q
        else:assert d["name"]==q
        excerpts.append(dict(pair_key=pair["pair_key"],aid=aid,source_url=f"https://pubchem.ncbi.nlm.nih.gov/bioassay/{aid}",
            raw_sha256=sha[aid],json_text_location=k,source_verbatim=q))
    ca=da.get("aid_source",{}).get("db",{});cb=db.get("aid_source",{}).get("db",{})
    comment=note["preliminary_documented_distinction"]
    evidence.append(dict(pair_key=pair["pair_key"],aid_a=a,aid_b=b,target=pair["target"],
        source_url_a=f"https://pubchem.ncbi.nlm.nih.gov/bioassay/{a}",
        source_url_b=f"https://pubchem.ncbi.nlm.nih.gov/bioassay/{b}",
        sha256_a=sha[a],sha256_b=sha[b],
        title_a=da.get("name",""),title_b=db.get("name",""),
        source_id_a=ca.get("source_id",{}).get("str",""),
        source_id_b=cb.get("source_id",{}).get("str",""),
        recorded_same_depositor=str(ca.get("name")==cb.get("name")),
        recorded_shared_grant=str(bool(find_grants(da)&find_grants(db))),
        direct_xref_a_to_b=str(crossref(da,b)),direct_xref_b_to_a=str(crossref(db,a)),
        excerpt_locator_a=ka,excerpt_locator_b=kb,
        preliminary_relation=note["relationship_type"],preliminary_source_comment=comment,
        frozen_historical_compatibility=pair["historical_compatibility_label_FROZEN"],
        frozen_historical_provenance_UNVALIDATED=pair["historical_provenance_label_FROZEN_DO_NOT_OVERRIDE"],
        measurement_copy="NOT_ESTABLISHED_FROM_DESCRIPTIONS",
        independent_execution="NOT_ESTABLISHED_FROM_DESCRIPTIONS",
        independent_program_lineage="NOT_ESTABLISHED_FROM_DESCRIPTIONS",
        provisional_state="HOLD_PENDING_PRIMARY_SOURCE_AND_EXPERT_ADJUDICATION",
        qualified_expert_1="",qualified_expert_2="",final_reconciled_label=""))
    blind.append(dict(pair_key=pair["pair_key"],aid_a=a,aid_b=b,
        source_url_a=f"https://pubchem.ncbi.nlm.nih.gov/bioassay/{a}",
        source_url_b=f"https://pubchem.ncbi.nlm.nih.gov/bioassay/{b}",
        excerpt_locator_a=ka,excerpt_locator_b=kb,
        human_reviewer_id="",copied_measurements="",distinct_assay_execution="",
        independent_programs="",verdict="",source_rationale="",source_document_citation="",date=""))
assert len(evidence)==43 and len(excerpts)==86
assert len({x["target"] for x in evidence})==29
assert sum(x["recorded_shared_grant"]=="True" for x in evidence)==43
assert sum(x["direct_xref_a_to_b"]=="True" or x["direct_xref_b_to_a"]=="True" for x in evidence)==14
assert all(x["final_reconciled_label"]=="" for x in evidence)
save(OUT/"R1_Stage5B_43pair_documentary_evidence.csv",evidence)
save(OUT/"R1_Stage5B_86_verbatim_source_excerpts.csv",excerpts)
save(OUT/"R1_Stage5B_blinded_human_reviewer_form.csv",blind)
summary=dict(pairs=43,aids=71,targets=29,source_excerpts=86,
   shared_grant_pairs=43,direct_AID_xref_pairs=14,
   independent_human_reviews=0,final_independence_labels=0,
   status="DOCUMENTARY_SOURCE_TRIAGE_COMPLETE_HUMAN_ADJUDICATION_PENDING")
(OUT/"summary.json").write_text(json.dumps(summary,indent=2)+"\n")
print(json.dumps(summary,indent=2))
