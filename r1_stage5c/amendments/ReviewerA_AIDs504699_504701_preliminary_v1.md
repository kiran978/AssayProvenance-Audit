# R1 Stage 5C — Reviewer A, Pair 4: OX1R 504699 vs 504701

**Recorded:** 2026-10-14  
**Review sequence:** Pair 4/43 (not the frozen source CSV row number).  
**Pair:** `PUBCHEM::NP_001516::IC50::504699::504701`.  
**Governance:** Author-coordinated AI-assisted preliminary human review; not blinded external validation, not adjudicated consensus. Relevant credentials, conflicts, and independently signed review remain to be verified.

## Reviewer A's submitted assessments — verbatim key/value selections

```text
PAIR: 4/43
PAIR_ID: PUBCHEM::NP_001516::IC50::504699::504701
TARGET_IDENTITY: SUPPORTED
COMMON_PROGRAM_LINEAGE: SUPPORTED
COMPOUND_OVERLAP: SUPPORTED
DIFFERENT_ASSAY_MODALITIES: SUPPORTED
MEASUREMENT_REUSE: UNRESOLVED
PHYSICAL_EXECUTION_INDEPENDENCE: UNRESOLVED
RAW_DATA_INDEPENDENCE: UNRESOLVED
IC50_FITTING_INDEPENDENCE: UNRESOLVED
INDEPENDENT_DATASET_ELIGIBILITY: HOLD
REVIEWER_DECISION: HOLD
```

No reviewer selection has been modified.

## Independent source-integrity / scientific quality check (assistant, not expert adjudication)

Archived, official PubChem depositor `description/JSON` files originally retrieved in R1 GitHub Actions Run #1; SHA-256:

- AID [504699](https://pubchem.ncbi.nlm.nih.gov/bioassay/504699): `281791e5acb36876deb57bb41e7a36ccb5ce6a64b0d1f8462f3cb41561a45202`.
- AID [504701](https://pubchem.ncbi.nlm.nih.gov/bioassay/504701): `f6b0d83c642f3e9d77f43ac82622c171bf4309cfcd205c587356ae37a9a8fed3`.

Both original descriptions:

- `target[0].mol_id.protein_accession` = human OX1R `NP_001516.2`.
- `description[0]` records Scripps Research Institute Molecular Screening Center; `description[2]` lists assay provider Patricia McDonald, `description[4]` the common grant `R01 DA023915-02`, and `description[5]` same grant PI.
- `protocol[2]` records assay-specific source and confirmation AIDs. AID 504699: primary 434989, confirmation 492963, counterscreen 492965. AID 504701: primary 485270, confirmation 492964, counterscreen 493232. The `xref` arrays refer to the same wider OX1R program, including summary AID 435008; neither directly references the opposing AID in this pair.
- AID 504699 `protocol[4]` and `protocol[10]`: CHO/OX1R cells, Fluo-8 calcium fluorescence, FLIPR Tetra kinetic readout. `protocol[14]` ratio I_Max/I_Min; `protocol[31]` four-parameter IC50 fitting; assay start concentration 49.8 uM.
- AID 504701 `protocol[4]` and `protocol[10]`: CHO/OX1R cells, IP-One competitive immunoassay, IP1 HTRF with acceptor/donor emission at 671/618 nm; `protocol[14]` ratio I671/I618; `protocol[31]` four-parameter IC50 fitting; assay upper concentration 66.2 uM.
- Both `comment[0]` state a campaign **may** have been repeated and data were normalized per plate. This is a general assay caveat, **not direct proof** of any shared or independent physical run between these AIDs.
- Frozen P1_10D selected-pair registry lists **247 shared exact CIDs**, compatibility `SENSITIVITY_ONLY`, and historical `NONINDEPENDENT_SAME_DISCOVERY_PROGRAM`; all are unchanged. CID overlap was **not re-estimated from raw result tables in Stage 5C**.

## Evidence-based evaluation

- Target identity, shared recorded program, compound overlap, and distinct assay modalities: supported at the documentary level.
- Measurement reuse, physical execution independence, raw signal independence, and IC50-fit input independence: unresolved; differing biological readout and identical fitting-software descriptions do not prove independent or reused source data.
- `REVIEWER_DECISION: HOLD` and `INDEPENDENT_DATASET_ELIGIBILITY: HOLD` are **preserved**, and mean the case is **not to be admitted as confirmed independent data** at this stage.
- **Decision-rule reconciliation needed:** The Stage 5C strict *program-disjoint* definition classifies an explicitly shared discovery program as **not program-independent**, irrespective of unresolved measurement reuse. If the reviewer meant `HOLD` solely for the evidence about measurement identity/execution, that is appropriate. If `HOLD` is meant as the final classification of strict program independence, the intended label needs an explicit reviewer clarification rather than silent relabeling. Neither `SHARED_PROGRAM` nor `NOT_PROGRAM_DISJOINT` means duplicated measurements.
- No new accepted final program-independence or network eligibility label has been entered; leave final consensus blank until proper validation.

## Further evidence required

Compare source result rows by SID/CID and dose concentration; ascertain experimental plate and run IDs, campaign dates, replicate structure, raw kinetic calcium traces, HTRF 671/618 signals, curve-fit inputs and any data-transfer records. Request original laboratory evidence where accessible. Record positive/negative control performance for method validation, reviewer expertise and potential conflicts, second reviewer assessment and actual signed reconciliation.

**Audit conclusion:** Reviewer A's `HOLD` is a conservative workflow disposition pending stronger evidence and rule clarification. It is **not** proof of data duplication or experimental independence.
