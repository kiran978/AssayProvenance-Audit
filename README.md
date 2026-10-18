# Provenance-aware audit of public bioactivity data

**Research data and reproducible analysis for:** *Numerical Assay Overlap versus Independent Evidence: A Provenance-Aware Audit of Public Bioactivity Data* (working manuscript). **Proposed journal:** *Clinica Chimica Acta* (Elsevier); **not yet submitted or accepted as of 2026-10-18**.

> **Status: research-stage evidence archive; not a certified experimental-run duplication dataset.** The original public chemical database and frozen program screens, derived analyses, and signed human review are separate evidence levels. This repo presently contains **provisional single-reviewer scientific decisions**; the first-person approval of corrections is pending. No second independent reviewer was recruited. AI was used for drafting/compilation, with human verification reported by the project owner; signed approval remains outstanding.

## Quick start

```bash
git clone https://github.com/kiran978/AssayProvenance-Audit.git
cd AssayProvenance-Audit
python3 scripts/verify_public_evidence.py
```

The check uses only Python standard libraries. See [reproducibility instructions](docs/REPRODUCIBILITY.md), [data dictionary](docs/DATA_DICTIONARY.md), [evidence maturity](docs/EVIDENCE_STATUS.md), and [source terms](docs/DATA_RIGHTS_AND_ATTRIBUTION.md).

## Citable derived evidence in this repository

| Data unit | File or folder | Status |
|---|---|---|
| **ChEMBL 37, S0**: 304 GE20 candidate pairs/102 targets | [304-case atlas](data/chembl/strict_s0_ge20_atlas_304.csv) | Case-level frozen derived audit, source database not deposited |
| **ChEMBL**: 64 different-document cases; 28 bibliographic flags, 36 for manual review | [64-case triage](data/chembl/cross_document_64_triage.csv), [36 queue](data/chembl/pre_manual_candidates_36.csv) | Automated documentary triage; final manual decisions absent |
| **ChEMBL**: 78 additional S1/S2/S3 sensitivity review cases | [sensitivity queue](data/chembl/s1_s2_s3_pending_candidates_78.csv) | Unadjudicated |
| **ChEMBL** overlap threshold re-filters | [threshold table](data/chembl/thresholds_ge1_to_ge200_with_coverage.csv) | GE20+ case-derived; GE10 summary-only |
| **BindingDB 202609** | [limitations and missing inputs](docs/EVIDENCE_STATUS.md) | Historical 46 candidates/8 targets cannot be case-level reproduced |
| **PubChem** original frozen 43 pairs/71 AIDs/29 target strata | [original registry](data/R1_43pair_stage4_source_registry.csv) | Frozen history unchanged |
| **PubChem** 43 provisional multidimensional decisions | [43-case scientific dimensions](data/pubchem/stage5e_43pair_provisional_scientific_decision_dimensions.csv) | Reported single-reviewer verification; first-person sign-off **pending** |
| **PubChem** six-pair result-level pilot | [Stage 6B pair audit](r1_stage6b/generated/pair_result_audit.csv) | 12 concise and 12 full result CSVs recovered |
| **PubChem** original measured-result exports, dated 2026-10-17 | [24 immutable SHA-verified exports](data/pubchem/original_result_tables_2026-10-17/) | **24/24 retrieved files** SHA-256 verified against original manifest; no laboratory plate/run provenance |
| **KCNK9/TASK3** AIDs 540322/652211 | [88-SID comparison](data/pubchem/stage6c_kcnk9_sid88_concordance.csv), [1,760 comparisons](data/pubchem/stage6c_kcnk9_1760_dose_sd_comparisons.csv), [four divergent SIDs](data/pubchem/stage6c_kcnk9_four_divergent_sids.csv) | Original deposited-value near-concordance **84/88**; physical data reuse unknown |
| Source integrity | [ChEMBL source archive manifest](provenance/original_recovered_bundle_40file_sha256_manifest.csv), [PubChem 24 source checksums](r1_stage6b/generated/retrieval_manifest.csv) | Original ChEMBL bundle contents not fully re-deposited; hashes previously checked |

### Results we can reproduce — and cannot conclude

- ChEMBL GE20: **304 pairs / 102 targets**, **240 same-document IDs**, **64 cross-document IDs**, **28 bibliographic review flags**, **36 awaiting original manual source-family judgments**. GE30: **201 pairs / 66 targets**, **24 cross-document pairs**, **6 pre-manual candidates**. Historical group of one accepted target/source family is **not independently validated** by the missing manual ledger.
- PubChem frozen endpoint suitability: **23 compatible / 10 sensitivity-only / 10 incompatible**. Later documentary assessment: **41 shared discovery-program labels / 2 unresolved**; measurement reuse **43/43 unresolved** and physical-run execution **43/43 unresolved**.
- KCNK9/TASK3: **88 shared SIDs**, **84 near-matching 20-field profiles**, **1,681/1,760** paired fields matching within the post-hoc 0.0005001 criterion, **51/54** jointly nonblank IC50s identical. This raises a **processed-result lineage question**, **not verified laboratory experimental duplication**.
- No verified positive/negative original experimental reuse controls; no accuracy, AUROC, sensitivity, specificity, cross-database prevalence, clinical diagnostic inference, or proven model leakage is claimed.
- The 43-pair PubChem sample was intentionally selected; the original ChEMBL/BindingDB eligibility sets have different units and selection processes and must not be pooled.

## Reproducible analytical figures

Eight evidence-derived analytical figures (each in **PNG and editable SVG**) are versioned under [figures/reproducible](figures/reproducible/). They are generated deterministically from the deposited tabular data by [scripts/regenerate_evidence_figures.py](scripts/regenerate_evidence_figures.py); see [figure dependencies](requirements-figures.txt) and the passing [figure-build workflow](.github/workflows/build-reproducible-figures.yml).

```bash
python -m pip install -r requirements-figures.txt
python scripts/regenerate_evidence_figures.py
```

**These are reproduced analytical plot versions, not a claim that the embedded figures in an earlier Word manuscript use identical rendering or typography.** Check the journal manuscript's individual figure numbers and captions against this generated set before substitution. Figure 8 illustrates **counterfactual eligibility**, not experimentally verified independent datasets.

## Provenance, reusability, and publication

The [original project stages](r1_stage5e/README.md) remain for reproducibility and historically frozen labels are preserved; the newer `data/chembl` and `data/pubchem` tables are versioned derived outputs, **not silently substituted for the original records**. We provide algorithmic verification with [GitHub Actions](.github/workflows/verify-and-deposit-evidence.yml) and the script above.

No Zenodo DOI is claimed by this repository. Before any public release, obtain contributor confirmation, check [third-party rights and attribution](docs/DATA_RIGHTS_AND_ATTRIBUTION.md), select a suitable license, and verify the human scientific review correction approvals. **Current repository visibility is private.** A private URL does not satisfy a manuscript's claim that data are publicly available.

**Data citation:** See [CITATION.cff](CITATION.cff). Draft [Data Availability Statement](docs/SUBMISSION_DATA_STATEMENT.md) requires updating when public access and final release are actually confirmed.
