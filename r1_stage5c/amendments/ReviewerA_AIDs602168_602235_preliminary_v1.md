# R1 Stage 5C — Reviewer A, Pair 8: SRC1 / NCOA1

**Review sequence:** Pair 8 of 43 (frozen cohort row 7).  
**Pair ID:** `PUBCHEM::NP_003734::IC50::602168::602235`  
**Date recorded:** 2026-10-15  
**Status:** Reviewer A preliminary human assessment, AI-assisted verification. **Not** a blinded independent external expert assessment or two-reviewer consensus. Reviewer qualifications, conflict declaration, and second human review remain pending.

## Reviewer A's original selections — preserved as submitted

```text
PAIR_NUMBER: 8/43
PAIR_ID: PUBCHEM::NP_003734::IC50::602168::602235

TARGET: SRC1 / NCOA1
ACCESSION: NP_003734.3
SHARED_EXACT_CIDS_REPORTED: 73

PRIMARY_RECORDS_EXAMINED: YES
SOURCE_INTEGRITY: VERIFIED

DATA_REUSE: UNRESOLVED
EXPERIMENTAL_EXECUTION: UNRESOLVED
DISCOVERY_PROGRAM: SHARED_PROGRAM
ENDPOINT_COMPATIBILITY: COMPATIBLE

PROGRAM_LINEAGE_EVIDENCE:
Both assays are components of a coordinated
SRC-family inhibitor discovery program,
with different SRC3 and SRC1 selection
branches.

MEASUREMENT_REUSE_EVIDENCE:
Identical reporter assay principles and
near-identical experimental procedures.
Numerical reuse not established.

PHYSICAL_EXECUTION_EVIDENCE:
Distinct depositor assay IDs.
Actual plate/run independence unverified.

STRICT_BENCHMARK_DECISION:
CONFIRMED_NOT_INDEPENDENT

ELIGIBILITY_RECOMMENDATION:
EXCLUDE_FROM_STRICT_PROGRAM-DISJOINT_BENCHMARK

RETAIN_FOR:
Within-program SRC1 reporter comparisons
and assessment of compound-selection effects.

REMAINING_UNCERTAINTY:
Matched IC50 values, replicate measurements,
plate IDs, run dates and source data files.

HUMAN_VALIDATION_STATUS: PENDING
```

## Assistant source audit — separate from human independent validation

Original depositor PubChem BioAssay `description/JSON` files from R1 recovered 71-AID artifact, independently read and hashed:

| Record | Original source | Archived raw JSON SHA-256 | Depositor source ID |
|---|---|---|---|
| 602168 | https://pubchem.ncbi.nlm.nih.gov/bioassay/602168 | `df8121289034462b0991ea27d0ba3fff566985d085cfd12fb7c29da6a931dd36` | `SRC1_INH_LUMI_1536_3XIC50 DCSRUN for SRC3` |
| 602235 | https://pubchem.ncbi.nlm.nih.gov/bioassay/602235 | `5df1fcf02e91a906a2d1a6c587651c834826f045f2de56976d5815f2cc5795f2` | `SRC1_INH_LUMI_1536_4XIC50 DRUN` |

Exact archived JSON field locations (zero-indexed):

- Both `target[0].mol_id.protein_accession`: `NP_003734.3`; name refers to NCOA1.
- Both `description[0]`: Scripps Research Institute Molecular Screening Center; `description[2]`: assay provider Bert O'Malley; `description[4]`: grant `5U19DK062434-09`; `description[5]`: grant PI Bert O'Malley.
- Both `description[6]`: different named depositor source IDs; `description[8]`: explicit SRC1 reporter measurement while AID 602168 is a *selectivity counterscreen for SRC3 inhibitor selection*.
- AID **602168** `protocol[2]`: SRC3 top 250 from primary AID 588352, SRC3 confirmation AID 588792 and VP16 counterscreen AID 588794 are evaluated for off-target SRC1 inhibitory effects.
- AID **602235** `protocol[2]`: SRC1-confirmed compounds from AID 588820, filtered against SRC1 VP16 counterscreen AID 588824, progress to SRC1 dose-response evaluation.
- Both `protocol[4]` (identical text): HEK293 GAL4 reporter / pBIND-SRC1 luciferase assay, quadruplicate, 10-point 1:3 dilution starting at 36 uM nominal concentration.
- Both `protocol[10]`: 1536-well reporter cell assay, ONE-Glo luciferase and ViewLux fluorescence/luminescence instrumentation; full methods substantially matched, but not every letter is identical.
- Both `protocol[20-24]`: 4-parameter sigmoidal curve fitting (the relevant subsection appears in `protocol[22]` for 602168, `protocol[20]` for 602235); these are method descriptions, *not* raw IC50-data lineage.
- Of 43 paired protocol text entries, **34 are exactly identical**, reflecting a shared written protocol template. This does **not** prove identical measurements.
- Both `comment[0]` mention that the assays *may* have been run in separate screening campaigns and normalized on a per-plate basis. This possibility is not evidence of actual execution or cross-AID data reuse.
- Both `xref` lists refer to their respective upstream SRC3 or SRC1 screening branches; **neither original AID record directly references the other**. Their shared-program designation is an inference from documented common SRC-family program, provider, grant, and complementary selection pathways—not a claimed reciprocal AID xref.
- The historical frozen cohort (row 7) records **73 shared exact CIDs**, assay compatibility `COMPATIBLE`, historical `NONINDEPENDENT_SAME_DISCOVERY_PROGRAM`. The overlap has **not** been newly recalculated from raw PubChem result tables in this Stage 5C review. The frozen data is not changed.

## Scientific evidence interpretation and audit outcome

1. **DATA_REUSE UNRESOLVED:** same technology, common protocol and shared compounds are not affirmative evidence of copied raw signals, fitted IC50s or distinct remeasurement.
2. **EXPERIMENTAL_EXECUTION UNRESOLVED:** neither separate source IDs nor a common written protocol establish separate plates, actual runs, dates or batch independence.
3. **DISCOVERY_PROGRAM SHARED_PROGRAM:** overlapping SRC-family research, center, grant, principal investigator and coordinated selectivity-study design support shared broader program despite different initial SRC3- versus SRC1-selected compound sets. Do not describe the distinct branches as a single identical experiment.
4. **ENDPOINT_COMPATIBILITY COMPATIBLE:** both record SRC1-driven HEK293 GAL4/luciferase IC50 under matching dilution/readout methods. Compound-selection mechanisms differ; compatibility does not imply unbiased interchangeability or independent evidence.
5. **STRICT_BENCHMARK_DECISION CONFIRMED_NOT_INDEPENDENT:** Reviewer A's classification is supported *as a discovery-program-disjoint decision* under the R1 Stage 5C rubric adopted after the original manuscript review. **Do not interpret this as confirmed measurement-level dependence or duplicate observations.**
6. **ELIGIBILITY:** `EXCLUDE_FROM_STRICT_PROGRAM-DISJOINT_BENCHMARK` provisionally; retain for explicitly labeled within-program SRC1 assay comparisons and compound-selection bias checks.

**Acceptance status:** Preliminary Reviewer A selections are internally consistent and source-supported at the scope stated above. Formal validation is still `PENDING`: missing reviewer qualification/conflict/independence documentation, second independent qualified human assessment, result-table comparison, run-level data and reconciliation.

## Required next evidence

Compare original result rows for overlapping CIDs/SIDs, dose-point values, raw/reported IC50s, curve-fit outputs and replicates; seek plate layouts, run IDs and laboratory dates from provider/source study; then review possible data copying separately from shared study lineage. Never silently relabel the historical frozen cohort or report the existing 0/43 count as newly independently validated.
