# R1 Stage 5C — Reviewer A, Pair 10: p97 / VCP

**Review sequence:** 10 of 43. **Recorded:** 2026-10-15. **Frozen dataset row:** 9 (0-indexed row 8).  
**Frozen pair ID:** `PUBCHEM::AAI21795::IC50::504649::504650`  
**Governance:** Author-coordinated AI-assisted preliminary human assessment. Not an independent blinded external expert review, not two-reviewer consensus. Reviewer identity/credentials, potential conflicts and independent signed verification remain to be documented.

## Reviewer A's submitted assessment — preserved verbatim

```text
PAIR_NUMBER: 10/43
PAIR_ID: PUBCHEM::AAI21795::IC50::504649::504650

TARGET: p97 / VCP
TARGET_ACCESSION: AAI21795.1
SHARED_EXACT_CIDS_REPORTED: 64

PRIMARY_RECORDS_EXAMINED: YES
SOURCE_INTEGRITY: VERIFIED

AID_504649: CELLULAR_REPORTER
SOURCE_ID_504649: KUA10008

AID_504650: BIOCHEMICAL_ATPASE
SOURCE_ID_504650: KUA10007

DATA_REUSE: UNRESOLVED
EXPERIMENTAL_EXECUTION: UNRESOLVED
DISCOVERY_PROGRAM: SHARED_PROGRAM
ENDPOINT_COMPATIBILITY:
INCOMPATIBLE_FOR_INTENDED_ESTIMAND

ASSAY_IDENTITY_RECONCILIATION:
NIH report Table 1 reverses the AID labels.
Original PubChem records and NIH detailed
methods support the corrected mapping.

PROGRAM_LINEAGE_EVIDENCE:
Both assays belong to the same p97 inhibitor
optimization program, linked to AID 1794.

UPSTREAM_REFERENCE:
KUA10001 / AID 463184, not AID 504650.

MEASUREMENT_REUSE_EVIDENCE:
Distinct assay technologies and outcomes.
Raw measurement non-reuse is not established.

PHYSICAL_EXECUTION_EVIDENCE:
Different documented procedures.
Run-level independence is unverified.

STRICT_BENCHMARK_DECISION:
CONFIRMED_NOT_INDEPENDENT

ELIGIBILITY_RECOMMENDATION:
EXCLUDE_FROM_STRICT_INDEPENDENT_BENCHMARK

RETAIN_FOR:
BIOCHEMICAL_TO_CELLULAR_ACTIVITY_COMPARISON

REMAINING_UNCERTAINTY:
Raw-data provenance, plate/run identifiers,
and numerical measurement reuse.

HUMAN_VALIDATION_STATUS: PENDING
```

## Verification sources and deposited source integrity

- [PubChem AID 504649](https://pubchem.ncbi.nlm.nih.gov/bioassay/504649), original depositor JSON SHA-256 `15f0e18cbfb1eadad08613328586e981a0cfb8ac5c6d68d247b8d9bc40e8d618`.
  - `descr.name`: `Inhibition of proteasomal turnover of a p97-dependent reporter substrate in human cells - Hit Optimization Round 3`.
  - `descr.aid_source.db.source_id.str`: `KUA10008`.
  - `descr.description[6]`: purpose of testing effects of p97 inhibitors on proteasome reporter turnover in cells, referring to upstream `KUA10001`.
  - `descr.protocol[0]`: UbG76V-GFP/HeLa cellular protocol; `protocol[5]`: normalized GFP decay-rate constant from repeated fluorescence intensity measurements.
  - `descr.xref`: `AID 1794` (summary) and **AID 463184**, expressly commented `KUA10001`.
- [PubChem AID 504650](https://pubchem.ncbi.nlm.nih.gov/bioassay/504650), original depositor JSON SHA-256 `8281c9d866324162e981aa1d11fb9e0651945fdcdf5d4ec3dd4b93f47ea63f80`.
  - `descr.name`: `p97 ATPase dose response - Hit Optimization Round 3`.
  - `descr.aid_source.db.source_id.str`: `KUA10007`.
  - `descr.description[6]`: `Determine inhibition of purified p97 by small molecules for SAR study.`
  - `descr.protocol[0]`: p97 enzyme/ATP reaction and luminescence-based biochemical assay.
  - `descr.xref`: `AID 1794` (common probe-development summary).
- Both `descr.target[0].mol_id.protein_accession` = `AAI21795.1`; `descr.description[0:4]` records assay provider Raymond Deshaies, performer Tsui-Fen Chou and grant `1 R03 MH085687-01`.

The original frozen 43-pair registry records **64 shared exact CIDs**, compatibility `INCOMPATIBLE_FOR_INTENDED_ESTIMAND`, historical provenance label `NONINDEPENDENT_SAME_DISCOVERY_PROGRAM`. This is archival information; overlap has not been recalculated from raw result rows and historical labels have not been modified.

## Independently checked NIH project-report inconsistency

Primary cited report: [Chou and colleagues, *Selective, reversible inhibitors of the AAA ATPase p97*](https://www.ncbi.nlm.nih.gov/books/NBK133422/), NIH Probe Reports, updated 2013.

- **Section 2.1, Table 1** assigns the hit-optimization-round-3 biochemical ATPase assay to `AID 504649`, and the cellular reporter assay to `AID 504650`. These table labels are **inverted** relative to the archived PubChem assay descriptions.
- **Section 2.1 detailed protocols** assign biochemical ATPase assays to `AID 463184`, `488828`, `504650`; and cellular UbG76V-GFP assays to `AID 463185`, `488830`, `504649`.
- The report's **Probe Structure & Characteristics** table is also consistent with the deposited AID identities: p97 ATPase IC50 for `AID 504650`, cellular UbG76V-GFP IC50 for `AID 504649`.

**Audit interpretation:** A published summary-table label error is documented and reconciled using depositor records plus the same report's detailed methods. Do not silently edit, conceal or rely on the erroneous Table 1 mapping. This review does not assert a formally issued publisher erratum.

The upstream source ID `KUA10001` maps to original p97 ATPase [AID 463184](https://pubchem.ncbi.nlm.nih.gov/bioassay/463184), **not** to later `AID 504650` (KUA10007).

## Evaluation and decision-rule boundaries

- `DATA_REUSE=UNRESOLVED`, `EXPERIMENTAL_EXECUTION=UNRESOLVED`: biochemical versus cellular systems and different protocols distinguish assay functions, but do not establish the identity/provenance of each raw measurement, fitted IC50 or laboratory run.
- `DISCOVERY_PROGRAM=SHARED_PROGRAM`: directly substantiated by the same p97 inhibitor optimization effort, summary AID 1794, shared provider/performer and grant, and common report.
- `ENDPOINT_COMPATIBILITY=INCOMPATIBLE_FOR_INTENDED_ESTIMAND`: purified p97 ATPase inhibition and cellular reporter-turnover inhibition are mechanistically different response variables. They may be used as **separately labeled biochemical-to-cellular translations**, not exchangeable p97 enzyme potency measurements.
- `CONFIRMED_NOT_INDEPENDENT` is **only a program-disjoint benchmark classification** under the specifically defined strict criterion adopted after original JCIM review. **Do not treat this as evidence of duplicated assays or physical measurement reuse.**
- `EXCLUDE_FROM_STRICT_INDEPENDENT_BENCHMARK` is recorded as the reviewer's *provisional* eligibility recommendation; preserve both original AIDs for cross-context response analysis.
- `HUMAN_VALIDATION_STATUS=PENDING`: reviewer qualification/conflict documentation, second qualified human assessment, source-level execution confirmation and formal consensus remain outstanding. The historical frozen cohort and original 0/43 claim remain unchanged and not newly validated.

## Unresolved work

Compare both original PubChem SID/CID result tables including curve-fitting outputs and raw measurements where available; inspect original plate/run IDs, experiment dates, replicates, raw ATPase luminescence, GFP kinetic curves and lineage logs; obtain human-source-review independent confirmation. Store new evidence as separately versioned amendments only.
