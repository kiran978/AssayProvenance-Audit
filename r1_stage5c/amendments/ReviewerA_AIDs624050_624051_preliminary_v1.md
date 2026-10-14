# R1 Stage 5C — Reviewer A, Pair 6: OX2R / HCRTR2

**Recorded:** 2026-10-14  
**Reviewer sequence:** Pair 6/43  
**Frozen pair ID:** `PUBCHEM::NP_001517::IC50::624050::624051`  
**Status:** AI-assisted author-coordinated preliminary human assessment; not external/blinded independent validation, no final reconciled expert consensus. Reviewer qualifications, conflicts, independence statement and signature have not been checked in this audit.

## Reviewer A's submitted decisions, preserved as submitted

```text
PAIR_NUMBER: 6/43
PAIR_ID: PUBCHEM::NP_001517::IC50::624050::624051

TARGET: OX2R / HCRTR2
TARGET_ACCESSION: NP_001517.2
SHARED_EXACT_CIDS_REPORTED: 213

PRIMARY_RECORDS_EXAMINED: YES
DOCUMENTARY_EVIDENCE: VERIFIED

DATA_REUSE: UNRESOLVED
EXPERIMENTAL_EXECUTION: UNRESOLVED
DISCOVERY_PROGRAM: SHARED_PROGRAM

PROGRAM_LINEAGE_EVIDENCE:
Both assay records explicitly trace compound
selection to the same broader OX1R antagonist
discovery workflow.

AID 624050:
Primary AID 434989; confirmation AID 492963.

AID 624051:
Primary AID 485270; confirmation AID 492964.

Both reference the common OX1R assay cascade.

MEASUREMENT_REUSE_EVIDENCE:
Different assay readouts documented.
Numerical copying not established.
Raw measurement independence not verified.

PHYSICAL_EXECUTION_EVIDENCE:
Distinct experimental procedures documented.
Run-level independence remains unverified.

ENDPOINT_COMPATIBILITY: SENSITIVITY_ONLY

STRICT_BENCHMARK_DECISION:
CONFIRMED_NOT_INDEPENDENT

ELIGIBILITY_RECOMMENDATION:
EXCLUDE_PAIR_FROM_STRICT_INDEPENDENT_BENCHMARK

RETAIN_FOR:
Within-program orthogonal assay comparison
and OX2R selectivity sensitivity analysis.

HUMAN_VALIDATION_STATUS: PENDING
```

## Independent documentary QA — machine-supported original-source verification, **not** a second human review

Original depositor PubChem AID description JSONs, fetched during R1 source recovery and checked using SHA-256:

- [AID 624050](https://pubchem.ncbi.nlm.nih.gov/bioassay/624050) JSON SHA-256 `45d23c7798e8093619dd1ca3801b6e947746a100c949d2bfa9f065d7ffea0088`
- [AID 624051](https://pubchem.ncbi.nlm.nih.gov/bioassay/624051) JSON SHA-256 `0199a2e9680cba5cfd1b4cb2b79a3de904d74a12b70764036d551ff154d12a5c`

Exact source anchors:

1. Both `target[0].mol_id.protein_accession`: `NP_001517.2`, human orexin receptor type 2.
2. Both `description[0]`: The Scripps Research Institute Molecular Screening Center; `description[2]`: assay provider Patricia McDonald; `description[4]`: grant `R01 DA023915-02`; `description[5]`: grant PI Patricia McDonald.
3. AID 624050 `protocol[2]` identifies upstream OX1R primary fluorescence-screen `AID 434989` and fluorescence confirmation `AID 492963`; `protocol[4]` describes CHO/OX2R Calcium5 fluorescence for antagonist selectivity.
4. AID 624051 `protocol[2]` identifies upstream OX1R primary IP-One / FRET-screen `AID 485270` and IP-One HTRF confirmation `AID 492964`; `protocol[4]` describes CHO/OX2R cells, IP1 competition and HTRF-based antagonist selectivity.
5. Both deposited `xref[]` lists reference OX1R summary `AID 435008`, upstream screening / confirmation records, and downstream OX1R AIDs `504699` / `504701`. **Neither AID has a direct xref to the other member (624050 ↔ 624051)**. The common assay cascade, not direct pairwise xref, grounds the shared-program assertion.
6. Frozen Stage 4 pair registry reports **213 shared exact CIDs**, a previously assigned compatibility category `SENSITIVITY_ONLY`, and historical label `NONINDEPENDENT_SAME_DISCOVERY_PROGRAM`. These are preserved unchanged and are not claimed to have been recomputed from experimental tables during Stage 5C.

## Assessment and decision-rule scope

- **Recorded shared program — supported.** Documentary source language establishes common OX1R antagonist screening, shared center, researcher and grant, even though the counterscreens read out OX2R.
- **Data reuse — unresolved.** Two technologies are described, but there is no verified row-level / replicate / raw-signal trace demonstrating identical or distinct experimental values.
- **Physical execution — unresolved.** Detailed protocols differ; source records do not establish executed plates, batches, dates, or run identifiers.
- **Compatibility — `SENSITIVITY_ONLY`.** This reproduces the frozen compatibility judgment. Orthogonal OX2R readouts should not be pooled as exchangeable IC50 estimates absent harmonization / sensitivity analysis.
- **Strict program-disjoint independence — `CONFIRMED_NOT_INDEPENDENT`.** As defined in Stage 5C's *post-rejection* review rubric, affirmatively demonstrated shared discovery-program membership excludes this pair from an independent-program benchmark. **It is not a conclusion that raw measurements were duplicated or that the physical experiments were identical.**
- **Eligibility — excluded from strict independent-program benchmark.** Preserve both assay records for within-program orthogonal comparisons and OX2R selectivity sensitivity analysis. Exclusion is at the **pair** level, not deletion of either AID or its source evidence.

## Pending validation / scientific sign-off

1. Examine original SID/CID results, dose points and individual biological readouts; seek run-level provenance, plate/date identifiers and replicate-level metadata if raw-data independence is to be claimed.
2. Obtain reviewer qualifications, conflict disclosure and documented AI exposure; obtain a second qualified human assessment blinded to the first.
3. Resolve disagreements according to the Stage 5C rubric, maintain unresolved measurement-level categories, and save any new consensus only as a separately versioned dataset. Do **not** rewrite frozen cohort classifications or report independent validation as complete.

**Audit state:** Reviewer A preliminary selection preserved and supported within its explicitly stated program-disjoint scope; `HUMAN_VALIDATION_STATUS: PENDING`.
