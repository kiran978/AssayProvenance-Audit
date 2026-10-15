# R1 Stage 5C — Reviewer A, Pair 11: TASK3 / KCNK9 across ML308 and ML365 branches

**Review sequence:** 11/43. **Date recorded:** 2026-10-15.  
**Pair ID:** `PUBCHEM::NP_057685::IC50::540322::652211`  
**Governance:** Author-coordinated, AI-assisted preliminary human assessment. **Not** a blinded independent external review, not a second human assessment and not a final consensus. Reviewer qualification/conflict declaration/signature remain pending.

## Submitted Reviewer A decisions — retained verbatim

```text
PAIR_NUMBER: 11/43
PAIR_ID: PUBCHEM::NP_057685::IC50::540322::652211

TARGET: KCNK9 / TASK3
TARGET_ACCESSION: NP_057685.1
SHARED_EXACT_CIDS_REPORTED: 55

PRIMARY_DESCRIPTION_RECORDS_EXAMINED: YES
SOURCE_INTEGRITY: VERIFIED

DATA_REUSE: UNRESOLVED
EXPERIMENTAL_EXECUTION: UNRESOLVED
DISCOVERY_PROGRAM: UNRESOLVED
ENDPOINT_COMPATIBILITY: COMPATIBLE

DOCUMENTED_BRANCH_A:
AID 540322, KCNK9_Inh_SAR_CRC_2
TASK3 inhibitor development
Primary AID 488922
Summary AID 488964
Associated probe: ML308

DOCUMENTED_BRANCH_B:
AID 652211, TASK1_Inh_SAR_TASK3_CRC
TASK3 selectivity for TASK1 inhibitors
Primary AID 602410
Summary AID 602490
Associated probe: ML365

PROGRAM_LINEAGE_EVIDENCE:
Separate primary screens, project summaries,
probe objectives and assay providers.
Shared center, grant and research personnel.
No direct documentary link proving that
the branches constitute one discovery program.
Distinct-program independence also unproven.

MEASUREMENT_REUSE_EVIDENCE:
Near-identical TASK3 fluorescence protocols.
55 exact-CID overlap reported.
Raw signal and potency-value reuse unverified.

PHYSICAL_EXECUTION_EVIDENCE:
Separate deposited assay records.
Original experiment/plate independence unknown.

STRICT_BENCHMARK_DECISION:
HOLD_UNRESOLVED

ELIGIBILITY_RECOMMENDATION:
HOLD_PENDING_PRIMARY_EVIDENCE

RETAIN_FOR:
TASK3 functional inhibition comparison,
subject to provenance and assay QC.

REQUIRED_NEXT_ACTION:
1. Compare 55 shared CIDs at SID/result level.
2. Compare IC50 and concentration-response values.
3. Recover experiment dates and plate/run IDs.
4. Establish compound-selection provenance.
5. Resolve relationship between ML308 and
   ML365 screening programs.
6. Reconcile anomalous AID cross-reference.

HUMAN_VALIDATION_STATUS: PENDING
```

## Original-source archive: SHA-256-verified PubChem description JSON

- [AID 540322](https://pubchem.ncbi.nlm.nih.gov/bioassay/540322): `d13901cd671d1014017dd6442602db198281363472eb549451b755202851c222`.
- [AID 652211](https://pubchem.ncbi.nlm.nih.gov/bioassay/652211): `893fc10ab0c1c16e5f7bcc7912393b0da829e4451866a565fa52561a80d5acc0`.
- Both target `NP_057685.1` in `target[0].mol_id.protein_accession`.
- Both describe a KCNK9/TASK3 FluxOR thallium-flux assay, with IC50 in micromolar (`results[22]`). Assay descriptions `description[15]` (540322) and `description[14]` (652211) state the different objectives.
- AID 540322: source `KCNK9_Inh_SAR_CRC_2`, grant `R03 MH090849-01` (`description[7]`), provider Meng Wu (`description[5]`), `xref[0]` summary **488964**, `xref[1]` primary **488922**.
- AID 652211: source `TASK1_Inh_SAR_TASK3_CRC`, grant `R03 MH090849-01` (`description[5]`), provider Min Li (`description[3]`), `xref[0]` summary **602490**, `xref[1]` primary **602410**; `description[14]` calls this a TASK3 selectivity assay for TASK1 inhibitory candidates.
- **Neither archived JSON record directly cross-references the other pair member.** Both report overlapping research personnel, not unique proof of a single scientific discovery program or of independent program lineages.
- Both use 23 similarly labeled `results[]` fields, including concentration-specific ratios/SDs, replicate number, Hill constant and `IC50`; 17 corresponding `protocol[]` entries are exactly identical (arrays have 40 and 39 entries), demonstrating shared written assay procedures, *not* reused numeric outcomes.
- Frozen Stage 4 registry reported **55 shared exact CIDs**, historical endpoint compatibility `COMPATIBLE` and the historical `NONINDEPENDENT_SAME_DISCOVERY_PROGRAM` label. Those prior entries are **not altered** and the 55 CIDs have not yet been independently reconstructed from raw SID/CID values in this review.

## Independent NIH report checks

1. [KCNK9/ML308 NIH probe-development report](https://www.ncbi.nlm.nih.gov/books/NBK133427/): summary AID **488964**, HTS primary AID **488922**, SAR including **540322** and probe **ML308**.
2. [TASK1/ML365 NIH probe-development report](https://www.ncbi.nlm.nih.gov/books/NBK179826/): summary AID **602490**, primary **602410**, TASK3 counterscreen **652211**, probe **ML365**.
3. Different lead probes, project summaries, and compound-selection paths are documented. Both reports nonetheless identify the same assay grant and Johns Hopkins center, and their investigators overlap. **Do not collapse these into SHARED_PROGRAM or DISTINCT_PROGRAMS without affirmatively establishing the intended meaning and linkage of a discovery program.** The reviewer-selected `UNRESOLVED` is appropriate.

## New specific QC findings (not edits to Reviewer A's choices)

**AID cross-reference defect:**

- AID 540322's archived `xref[2]` has `aid: 92992`, accompanied by a comment identifying a *KCNK9 confirmatory screen*.
- Actual [AID 92992](https://pubchem.ncbi.nlm.nih.gov/bioassay/92992) is an unrelated ChEMBL assay concerning ADP-induced platelet aggregation.
- [AID 492992](https://pubchem.ncbi.nlm.nih.gov/bioassay/492992) is the corresponding KCNK9 confirmatory assay, and the ML308 report identifies AID 492992 in this screening cascade.
- This supports **POSSIBLE_XREF_TYPO_92992_VS_492992**, with high documentary confidence, but **does not** authorize silently editing the original PubChem xref, and AID 492992 should remain a *proposed* corrected referent until depositor/source confirmation. Do not treat the incorrect AID 92992 as experimental lineage evidence.

**Concentration-schema differences:**

- Both assay records use result labels `Ratio at 41.1nM` and `Ratio at 13.7nM`, but `results[12].tc.concentration` is **0.0410 uM (540322)** versus **0.0411 uM (652211)**, and `results[14].tc.concentration` is **0.0130 uM (540322)** versus **0.0137 uM (652211)**.
- This is **RESULT_TC_CONCENTRATION_METADATA_DIFFERENCE**. It may represent rounding/depositor metadata, not proof of erroneous measured concentrations. Compare actual original result rows and source run conditions before applying any concentration normalization or declaring data incompatible.
- `ENDPOINT_COMPATIBILITY=COMPATIBLE` remains the reviewer selection at the *biological method* level; numeric concentration metadata need a separate QC flag.

## Scientific evaluation and disposition

- `DATA_REUSE=UNRESOLVED`: matching methods and overlapping compounds are insufficient to establish either copied results or independent biological measurements.
- `EXPERIMENTAL_EXECUTION=UNRESOLVED`: separate AID records and metadata dates do not prove separate plates, dates or physical runs.
- `DISCOVERY_PROGRAM=UNRESOLVED`: separate TASK3 vs TASK1 lead objectives with shared grant/investigators do not, on their own, satisfy affirmative SHARED_PROGRAM or DISTINCT_PROGRAMS under the prospective Stage 5C rule.
- `STRICT_BENCHMARK_DECISION=HOLD_UNRESOLVED`; `ELIGIBILITY_RECOMMENDATION=HOLD_PENDING_PRIMARY_EVIDENCE`: preserve Reviewer A choices and do not include as confirmed independent or confirmed nonindependent at this review stage.
- Retain both original assays for **within-target TASK3 functional comparisons conditional on harmonization**, not as independent benchmarks.
- `HUMAN_VALIDATION_STATUS=PENDING`: Reviewer A preliminary submission is not blinded human consensus; no second qualified human assessment, agreement or adjudicated label exists. No frozen historical labels were overwritten.

## Focused next steps

1. Obtain official PubChem AID 540322 and 652211 full result tables, compare all 55 frozen-overlap CIDs at original SID/CID level and original concentration-series values (especially 41.1 / 13.7 nM slots).
2. Compare raw replicates and fitted IC50 with censoring/qualifiers; distinguish exact data copying from methodological template reuse.
3. Seek plate/run identifiers, dates and batch provenance from original primary data/assay center where available.
4. Trace whether ML308 and ML365 compounds were selected from common or distinct reagent libraries/optimization cycles; distinguish administratively shared grant from direct project-execution lineage.
5. Source-check and annotate AID 92992/492992 mismatch without mutating depositor evidence.
6. Obtain qualified, conflict-disclosed independent human review and reconcile genuine disagreements before any benchmark-label release.
