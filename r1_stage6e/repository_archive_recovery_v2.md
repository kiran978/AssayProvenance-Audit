# R1 Stage 6E v2 — Original uploaded repository-bundle recovery

**Prepared:** 2026-10-17. **Status:** CHemBL strict-S0 numerical and automated triage recovery **PASS**; final manual source-family decisions, BindingDB and reviewer sign-off **PENDING**. This record supersedes the evidence-availability assumptions (not the frozen scientific outputs) from the earlier Stage 6E README.

**User-provided input:** `JCIM_Data_Code_Repository_Bundle.zip`; SHA-256 `6bb718fd4cd3dda7084648ec8553cf76d0f452fcc1be3d3b83e7e36874f7ee2a`. The ZIP has 41 entries including a 40-item SHA256 manifest; **all 40 manifest hashes and sizes verified**. The bundled derived tables are source evidence, not replacement for raw ChEMBL37/BindingDB202609 releases.

## ChEMBL recovered source ledger

- Strict S0 GE20 atlas: **304 assay pairs across 102 target IDs** (original `phase3c4_S0_pair_overlap_atlas_GE20.csv`).
- Same-document IDs: **240 pairs**; cross-document IDs **64**. The original 64-case ledger documents **28 bibliographic-duplicate-review flagged** cases (same normalized source document title, not verified copied assay data), leaving **36 pre-manual candidates across 22 targets**.
- Every `manual_independence_status` in the 64-case queue is **blank**. Thus the downstream claim of **one accepted target/source-family group** cannot be derived from manual case decisions in this archive. One group is not one pair; do not report 36-to-1 pair attrition.
- Original S1/S2/S3 GE20 context-relaxation summaries report **588/225**, **889/296**, **1036/287** pair/target counts. The uploaded sensitivity manual queue contains **12 + 32 + 34 = 78** new pre-manual cases with blank adjudication fields.

## GE10/20/30 source-threshold analysis

| Cutoff | Pairs | Target IDs | Same-document | Cross-document | Pre-manual candidates |
|---|---:|---:|---:|---:|---:|
| GE10 | **360 (original summary only)** | n/a | n/a | n/a | n/a |
| GE20 | 304 | 102 | 240 | 64 | 36 |
| GE25 | 229 | 78 | 198 | 31 | 10 |
| GE30 | **201** | **66** | **177** | **24** | **6** |
| GE40 | 164 | 51 | 147 | 17 | 4 |
| GE50 | 147 | 39 | 135 | 12 | 4 |
| GE100 | 50 | 12 | 45 | 5 | 2 |
| GE200 | 5 | 5 | 3 | 2 | 0 |

GE20 and stricter are exact re-filters of the original supplied 304 rows; not new database ingestion. GE10=360 is archived in `phase3c4_S0_overlap_atlas_summary.json`; the other **56 GE10–19 pair rows and target IDs are not included** in the GE20 table, so a fully comparable GE10 provenance-funnel result is **not** supported. No original ChEMBL37 SQLite source database has been supplied.

**Material threshold-sensitive finding:** The original S1–S3 summary identifies the historic one independent target group as **CHEMBL244**. The original 304 atlas contains 79 CHEMBL244 pairs, **67 within-document** and **12 cross-document pre-manual**; each of the latter has `n_shared=23`. **At GE30, no CHEMBL244 cross-document candidates survive.** The remaining within-document CHEMBL244 overlap cannot substitute for that distinct-source group. Other GE30 final human classifications remain unknown.

## Still not resolved

- **BindingDB 202609:** no original 46-case pair ledger, source-family decisions, frozen TSVs or assay/entry mapping; the 46-pair/8-target figures are historical reported counts, not independently replayed.
- ChEMBL 36 original manually adjudicated verdicts, their grouping rules, and source-family evidence for the reported accepted group.
- Reviewer A's 21 first-person corrections/attestations still pending, no second reviewer (per user decision), and no authenticated laboratory-reuse positive/negative controls.
- The reviewer’s cross-source GE10/20/30 source-wide validation request is **only partially closed**. Do not claim cross-source attrition finality, independent provenance classification accuracy, or complete manuscript submission readiness.

**Reproducible workbook and complete ZIP** are prepared in the conversation workspace with original unchanged bundle, source linked 304/64/36/78 cases, hashes, full CSV audit, and standard-library rerun code. No personal reviewer files or old frozen labels were modified on GitHub.
