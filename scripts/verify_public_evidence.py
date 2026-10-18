#!/usr/bin/env python3
"""Check deposited case-level evidence against reproducible reported counts.
Python 3.10+ standard library only. Deliberately does not infer raw-run reuse.
Run: python scripts/verify_public_evidence.py
"""
from __future__ import annotations
import csv, json, hashlib
from pathlib import Path
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
def read(rel):
    with (ROOT/rel).open(encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f))
def check(name,got,want):
    if got!=want:
        raise AssertionError(f"{name}: expected {want!r}; got {got!r}")
    print(f"PASS {name}: {got}")
    return got

a=read("data/chembl/strict_s0_ge20_atlas_304.csv")
cross=read("data/chembl/cross_document_64_triage.csv")
manual=read("data/chembl/pre_manual_candidates_36.csv")
sens=read("data/chembl/s1_s2_s3_pending_candidates_78.csv")
pub=read("data/pubchem/stage5e_43pair_provisional_scientific_decision_dimensions.csv")
sid=read("data/pubchem/stage6c_kcnk9_sid88_concordance.csv")
dose=read("data/pubchem/stage6c_kcnk9_1760_dose_sd_comparisons.csv")
pilot=read("data/pubchem/stage6c_six_pair_frozen_vs_current_overlap.csv")
check("ChEMBL S0 GE20 pairs",len(a),304)
check("ChEMBL S0 GE20 targets",len({x["target"] for x in a}),102)
check("Same document IDs",sum(x["same_document"]=="1" for x in a),240)
check("Different document IDs",sum(x["same_document"]=="0" for x in a),64)
check("Cross-document queue",len(cross),64)
check("Bibliographic duplicate flags (NOT proven raw reuse)",sum(x["bibliographic_duplicate_review"]=="1" for x in cross),28)
check("Pre-manual candidate flags",sum(x["pre_manual_candidate"]=="1" for x in cross),36)
check("Pre-manual rows",len(manual),36)
check("Pre-manual targets",len({x["target"] for x in manual}),22)
check("Unrecorded ChEMBL manual decisions",sum(x["manual_independence_status"] in ("","NOT_RECORDED") for x in cross),64)
check("Sensitivity review candidates",len(sens),78)
check("Sensitivity S1 / S2 / S3",sorted(Counter(x["cohort"].split("_")[0] for x in sens).values()),[12,32,34])

thresholds=[]
for n in [20,25,30,40,50,100,200]:
    subset=[x for x in a if int(x["n_shared"])>=n]
    doc_cross=[x for x in subset if x["same_document"]=="0"]
    m=[x for x in manual if int(x["n_shared"])>=n]
    thresholds.append({"threshold":n,"pairs":len(subset),"targets":len({x["target"] for x in subset}),
         "cross_document":len(doc_cross),"pre_manual":len(m)})
check("GE30 pairs/targets/cross-document/pre-manual",
      [thresholds[2][k] for k in ("pairs","targets","cross_document","pre_manual")],[201,66,24,6])
check("CHEMBL244 GE30 pre-manual candidates",
      sum(x["target"]=="CHEMBL244" and int(x["n_shared"])>=30 for x in manual),0)

check("PubChem pairs",len(pub),43)
check("PubChem source-program labels",dict(Counter(x["ReviewerA_discovery_program"] for x in pub)),
      {"SHARED_PROGRAM":41,"UNRESOLVED":2})
check("PubChem physical execution unresolved",
      sum(x["ReviewerA_physical_execution"]=="UNRESOLVED" for x in pub),43)
check("PubChem measurement reuse unresolved",
      sum(x["ReviewerA_measurement_reuse"]=="UNRESOLVED" for x in pub),43)
check("PubChem frozen endpoint categories",
      dict(Counter(x["Frozen_endpoint_compatibility"] for x in pub)),
      {"COMPATIBLE":23,"SENSITIVITY_ONLY":10,"INCOMPATIBLE_FOR_INTENDED_ESTIMAND":10})
check("KCNK9 shared SIDs",len(sid),88)
check("KCNK9 near-matching 20-field profiles",
      sum(x["ALL20_Dose_and_SD_near_match"]=="YES" for x in sid),84)
check("KCNK9 paired raw result fields",len(dose),1760)
check("KCNK9 near-matching cells",
      sum(x["difference_within_0.0005001"]=="YES" for x in dose),1681)
check("KCNK9 paired nonblank IC50 observations",
      sum(bool(x["IC50_A_uM"]) and bool(x["IC50_B_uM"]) for x in sid),54)
check("KCNK9 exactly matching nonblank IC50",
      sum(bool(x["IC50_A_uM"]) and bool(x["IC50_B_uM"]) and
          x["IC50_exact_string_equal"]=="YES" for x in sid),51)
check("Six pilot comparisons",len(pilot),6)

summary={"status":"SOURCE-DERIVED_COUNTS_REPRODUCED_NO_LAB_PROVENANCE_GOLD_STANDARDS",
  "chembl_thresholds":thresholds,"chEMBL_final_36_manual_verdicts":"MISSING",
  "bindingdb_202609_46case_ledger":"MISSING",
  "human_first_person_signoff":"PENDING",
  "authentic_original_measurement_provenance_controls":"NOT_AVAILABLE"}
print(json.dumps(summary,indent=2))
