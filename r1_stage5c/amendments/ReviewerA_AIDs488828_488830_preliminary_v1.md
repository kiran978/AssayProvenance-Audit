# R1 Stage 5C — Reviewer A, Pair 7: p97 / VCP, AID 488828 vs 488830

**Review sequence:** 7 of 43. **Recorded:** 2026-10-14. **Pair key:** `PUBCHEM::AAI21795::IC50::488828::488830`.

**Validation scope:** Author-coordinated, AI-assisted preliminary human review. Not blinded independent external expert adjudication; no second human review or consensus. Reviewer credentials, independence, conflicts, AI exposure and signature remain to be documented separately.

## Reviewer A original selections — unchanged

```text
PAIR_NUMBER: 7/43
PAIR_ID: PUBCHEM::AAI21795::IC50::488828::488830

TARGET: p97 / VCP
ACCESSION: AAI21795.1
SHARED_EXACT_CIDS_REPORTED: 84

PRIMARY_RECORDS_EXAMINED: YES
SOURCE_INTEGRITY: VERIFIED

DATA_REUSE: UNRESOLVED
EXPERIMENTAL_EXECUTION: UNRESOLVED
DISCOVERY_PROGRAM: SHARED_PROGRAM

PROGRAM_LINEAGE_EVIDENCE:
Both assays belong to the same p97 inhibitor
hit-optimization program and are explicitly
listed in the NIH probe-development report.

AID 488828 SOURCE_ID: KUA10003
AID 488830 SOURCE_ID: KUA10004

UPSTREAM REFERENCE:
KUA10001, not automatically AID 488828.

MEASUREMENT_REUSE_EVIDENCE:
Different readout modalities and biological
endpoints are documented.
Raw measurement non-reuse is not verified.

PHYSICAL_EXECUTION_EVIDENCE:
Distinct experimental systems are described.
Run-level independence is not established.

ENDPOINT_COMPATIBILITY:
INCOMPATIBLE_FOR_DIRECT_POTENCY_COMPARISON

STRICT_BENCHMARK_DECISION:
CONFIRMED_NOT_INDEPENDENT

ELIGIBILITY_RECOMMENDATION:
EXCLUDE_PAIR_FROM_STRICT_INDEPENDENT_BENCHMARK

RETAIN_FOR:
Within-program biochemical-versus-cellular
response comparisons.

REMAINING_UNCERTAINTY:
Raw data provenance, actual execution
identity, and KUA10001 cross-reference
reconciliation.

HUMAN_VALIDATION_STATUS: PENDING
```

## Assistant documentary QA (not a second human review)

Official PubChem `description/JSON` downloaded by the original R1 recovery job, integrity checked:

- [AID 488828](https://pubchem.ncbi.nlm.nih.gov/bioassay/488828), source ID `KUA10003`, JSON SHA256 `7c4d6ef3c162fdb035813fbac97efd98f7230bbb08bfc89d25e982c979cfe49f`.
- [AID 488830](https://pubchem.ncbi.nlm.nih.gov/bioassay/488830), source ID `KUA10004`, JSON SHA256 `3f3ffd2a8a4eb6331b7d895f5c4b18712dfdf342d13df1d1cd5eaa4cca62c4f3`.

Specific depositor-source locations:

- Both `target[0].mol_id.protein_accession`: `AAI21795.1`. Both `description[0]`: assay provider Raymond Deshaies; `description[1]`: performer Tsui-Fen Chou; `description[3]`: `1 R03 MH085687-01`; same original source center (University of Kansas Specialized Chemistry Center).
- AID 488828 `description[6]`: SAR inhibition of purified p97; `protocol[0]`: purified-enzyme p97 ATPase assay, ATP, Kinase-Glo Plus reagent and luminescence reading.
- AID 488830 `description[6]`: cellular p97-dependent reporter turnover following inhibitor selection from `KUA10001`; `protocol[0]`: UbG76V-GFP/HeLa cell imaging at sequential timepoints with GFP measurement. `protocol[5]`: degradation rate constant computed from the GFP-intensity time series.
- AID 488830 `xref[]` includes an `aid: 6505` entry commented `KUA10001`. However, the original PubChem assay record [AID 463184](https://pubchem.ncbi.nlm.nih.gov/bioassay/463184) explicitly identifies external source ID `KUA10001`. The AID-6505 versus 463184 xref needs reconciliation, and `KUA10001` must not be misassigned to AID 488828 (`KUA10003`).
- [NIH Molecular Libraries report, *Selective, reversible inhibitors of the AAA ATPase p97*, Table 1](https://www.ncbi.nlm.nih.gov/books/NBK133422/) explicitly lists AID 463184 (earlier p97 ATPase assay), AID 488828 (round-2 biochemical ATPase), and AID 488830 (round-2 cellular reporter) as activities within the same probe-development project.
- Frozen P1_10D/Stage 4 selected-pair registry reports **84 shared exact CIDs** and historical compatibility `INCOMPATIBLE_FOR_INTENDED_ESTIMAND`; original provenance label was `NONINDEPENDENT_SAME_DISCOVERY_PROGRAM`. These historical values were not revised.

## Evidence-based interpretation, limitations, and reviewer disposition

- **DATA_REUSE UNRESOLVED / EXPERIMENTAL_EXECUTION UNRESOLVED**: The assays describe different biological systems and raw observable signals, but original measurement tables and lab/plate/run identities have not been compared conclusively. No affirmative proof of copied data or of independent execution.
- **DISCOVERY_PROGRAM SHARED_PROGRAM**: Same grant, provider, compound-optimization effort and joint project listing support common program membership.
- **Endpoint compatibility**: Biochemical ATP hydrolysis and cellular reporter proteasomal turnover quantify different biological responses. Treat `INCOMPATIBLE_FOR_DIRECT_POTENCY_COMPARISON` as incompatible for a pooled **single biochemical potency estimand**; both data types may nevertheless inform a multilevel mechanistic response analysis if separately labeled.
- **Program-disjoint rule**: The reviewer's `CONFIRMED_NOT_INDEPENDENT` and `EXCLUDE_PAIR_FROM_STRICT_INDEPENDENT_BENCHMARK` follow the documented shared program under the Stage 5C **post-rejection prospectively fixed** program-disjoint definition; **do not translate this into confirmed duplication of experimental measurements**.
- **Retain** both assays for explicitly labeled within-program biochemical-versus-cellular concordance analyses (endpoint-specific, not interchangeable IC50s).
- **Human validation:** `PENDING`. The reviewer decision is preliminary, not consensus or blinded external validation; missing reviewer qualification/conflict declaration and second qualified assessment. Preserve every original frozen row and every reviewer selection unchanged.

## Next possible primary-evidence work

Inspect original PubChem SID/CID result tables, concentration-response point and replicate metadata, source-laboratory record IDs and execution dates for AIDs 463184, 488828, 488830, and ambiguous cross-reference AID 6505 if accessible. Capture data lineage/provenance separately for each original signal and IC50 fit. Record any new evidence as an append-only amendment and obtain independent human review before releasing final updated benchmark results.
