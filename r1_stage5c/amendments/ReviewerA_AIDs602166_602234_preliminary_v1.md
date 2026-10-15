# R1 Stage 5C — Reviewer A, Pair 9: SRC3 / NCOA3

**Review sequence:** 9 of 43. **Recorded:** 2026-10-15.  
**Frozen pair key:** `PUBCHEM::NP_858045::IC50::602166::602234`.

**Governance:** Author-coordinated, AI-assisted preliminary human review; not blinded independent external validation and not a reconciled consensus. Reviewer qualifications, potential conflicts, independent second review, and any signed verification remain pending.

## Original reviewer selections — reproduced without changes

```text
PAIR_NUMBER: 9/43
PAIR_ID: PUBCHEM::NP_858045::IC50::602166::602234

TARGET: SRC3 / NCOA3
TARGET_ACCESSION: NP_858045.1
SHARED_EXACT_CIDS_REPORTED: 73

PRIMARY_RECORDS_EXAMINED: YES
SOURCE_INTEGRITY: VERIFIED

DATA_REUSE: UNRESOLVED
EXPERIMENTAL_EXECUTION: UNRESOLVED
DISCOVERY_PROGRAM: SHARED_PROGRAM
ENDPOINT_COMPATIBILITY: COMPATIBLE

PROGRAM_LINEAGE_EVIDENCE:
AID 602166 follows the SRC3 inhibitor
discovery and confirmation workflow.

AID 602234 follows the SRC1 inhibitor
discovery workflow, with SRC3 assessed
as a selectivity counterscreen.

Both belong to the documented coordinated
SRC-family screening research program.

MEASUREMENT_REUSE_EVIDENCE:
Identical reporter systems and procedures;
73 shared CIDs reported.
Numerical measurement reuse not proven.

PHYSICAL_EXECUTION_EVIDENCE:
Distinct deposited assay identifiers.
Plate/run identity remains unresolved.

ADDITIONAL_QC_CONCERN:
LogIC50 descriptions differ in stated
concentration units.

STRICT_BENCHMARK_DECISION:
CONFIRMED_NOT_INDEPENDENT

ELIGIBILITY_RECOMMENDATION:
EXCLUDE_FROM_STRICT_PROGRAM_DISJOINT_BENCHMARK

RETAIN_FOR:
Within-program SRC3 functional inhibition
comparisons and selectivity analyses.

REMAINING_UNCERTAINTY:
Matched CID/SID potency data, raw
replicate responses, run dates, plate IDs,
curve-fitting provenance and LogIC50 units.

HUMAN_VALIDATION_STATUS: PENDING
```

## Source-integrity and documentary QA (assistant verification, not human consensus)

Official original depositor PubChem BioAssay descriptions downloaded in R1 GitHub Run 1, verified locally:

| AID | Original source | Depositor source ID | Archived JSON SHA-256 |
|---|---|---|---|
| 602166 | https://pubchem.ncbi.nlm.nih.gov/bioassay/602166 | `SRC3_INH_LUMI_1536_3XIC50 DRUN` | `bf5fe7809c1bada6b927068d4bbb5ae52eca0ca81edbc9b2aca3af096366947a` |
| 602234 | https://pubchem.ncbi.nlm.nih.gov/bioassay/602234 | `SRC3_INH_LUMI_1536_4XIC50 DCSRUN for SRC1` | `35dbd00ac38082cf741b61e00bc73eaf146cf9f8d6a956be5973efe47cdf6e58` |

**Source locations (zero-based JSON arrays):**

- Both `target[0].mol_id.protein_accession` = `NP_858045.1`.
- Both `description[0]`, `description[2]`, `description[4]`, `description[5]`: Scripps Molecular Screening Center, assay provider Bert O'Malley, grant `5U19DK062434-09`, same grant PI.
- AID 602166 `protocol[2]` describes SRC3 top 250 from primary AID 588352, follow-up confirmation AID 588792, and VP16 counterscreen AID 588794.
- AID 602234 `protocol[2]` describes SRC1-confirmed compounds from AID 588820, counterscreened against VP16 AID 588824, then evaluated for off-target SRC3 inhibition.
- Both `protocol[4]` and `protocol[10]`: transfected HEK293 GAL4-SRC3 / pBIND-SRC3 reporter, luciferase readout, ten-point 1:3 dilution series starting nominally at 36 µM, quadruplicate, ONE-Glo and ViewLux.
- Both `protocol[]` arrays contain 43 entries; **37 of the paired text entries are exactly identical**, consistent with reused written procedures, not proof of reused measurements.
- Both original `xref[]` arrays refer to their respective SRC1 or SRC3 screening pathways; neither directly xrefs the opposite pair-member AID.
- Historical frozen cohort records **73 shared exact CIDs**, historical compatibility `COMPATIBLE`, and unvalidated old label `NONINDEPENDENT_SAME_DISCOVERY_PROGRAM`. Frozen records remain read-only. CID overlap was not recalculated from source result rows during this review.

## Substantive QC exception — LogIC50 unit descriptions

In each original JSON, the **`results[2].name` is `LogIC50`**, but `results[2].description[0]` differs:

- AID 602166: `Log10 of the qualified IC50 (IC50) from the inhibitor assay in M concentration`.
- AID 602234: `Log10 of the qualified IC50 (IC50) from the inhibitor assay in uM concentration`.

By contrast, both `results[1]` IC50 descriptions label the regular IC50 concentration in micromolar (`unit: 5`). The `LogIC50` fields have `unit: 254` (unspecified).

**Consequences:** If the deposited log values follow these definitions, `log10(IC50[M]) = log10(IC50[µM]) - 6`. The source descriptions disagree by a six-unit offset, but this review has **not** tested the actual values to establish whether the deposited data are shifted, already normalized or mislabeled. Mark `LOGIC50_UNIT_HARMONIZATION_HOLD`. Never automatically apply a +6/-6 transformation without checking matched original numeric IC50 / LogIC50 result pairs and assay deposition conventions, including censored `>` values.

**Additional schema-joining caution:** The `results[]` field ordering differs beyond the first three entries (AID 602166 `results[3]` is Maximal Response, whereas AID 602234 `results[3]` is Hill Slope). Join result attributes by semantic name and schema/TID per *each* AID, not by a shared array ordinal alone.

## Scientific interpretation / provisional benchmark disposition

1. `DATA_REUSE=UNRESOLVED`: shared procedure templates and shared CIDs do not prove raw or fitted result reuse.
2. `EXPERIMENTAL_EXECUTION=UNRESOLVED`: distinctive source IDs and workflow positions do not establish actual separate plates/runs.
3. `DISCOVERY_PROGRAM=SHARED_PROGRAM`: coordinated SRC-family discovery project, provider, grant and complementary selection pathways provide affirmative program-lineage evidence.
4. `ENDPOINT_COMPATIBILITY=COMPATIBLE`: the SRC3 luciferase IC50 readout and measured target are comparable at the biological-method level. **Numeric LogIC50 harmonization is separately ON HOLD** until source result rows are verified.
5. `STRICT_BENCHMARK_DECISION=CONFIRMED_NOT_INDEPENDENT`: this is justified under the *post-rejection Stage 5C strict program-disjoint criterion only*; it does **not** signify duplicated raw measurements.
6. `ELIGIBILITY_RECOMMENDATION=EXCLUDE_FROM_STRICT_PROGRAM_DISJOINT_BENCHMARK`: reviewer recommendation preserved; assays retained for within-program SRC3 functional inhibition and selectivity studies. No final consensus or updated frozen cohort created.

## Follow-up required

- Retrieve both official PubChem assay result tables and compare, by SID/CID, `IC50`, `LogIC50`, fitting qualifiers, censoring and curve parameters. Check whether `LogIC50` reflects M or µM and whether the discrepancy is metadata-only; log every original vs normalized value and formula if normalization is justified.
- Inspect raw replicate, plate, experimental date and run identifiers, when obtainable, for actual independence or reuse.
- Obtain independent signed human review (qualifications/conflicts/AI exposure documented), resolve disagreement, preserve original review and frozen row unchanged.

**Audit status:** preliminary reviewer decisions supported with a **separate unresolved LogIC50 metadata QC exception**. `HUMAN_VALIDATION_STATUS=PENDING`.
