# Case-level data dictionary

## ChEMBL records

- `strict_s0_ge20_atlas_304.csv`: original strict-S0 GE20 **derived** assay-pair atlas from ChEMBL 37. One row = target, endpoint, assay A/B source-document combination with `n_shared` **parent-compound count**. `same_document=1` means shared document ID, **not identical laboratory measurements**. `status` has no final manually adjudicated outcome.
- `cross_document_64_triage.csv`: 64 unique different-document assay-pair records. `bibliographic_duplicate_review=1` means **review flag based on documentary comparison**, not source-verified copying. `pre_manual_candidate=1` marks 36 cases awaiting manual review. `manual_independence_status=NOT_RECORDED` is a truthful missing result.
- `pre_manual_candidates_36.csv`: strict-S0 cross-document review subset of the preceding 64, **not** independent cases. Target breadth is 22.
- `s1_s2_s3_pending_candidates_78.csv`: further candidate records from *assay-eligibility sensitivity cohorts*, not GE cutoff sensitivity. `manual_decision=NOT_RECORDED` must not be recoded as dependent or independent.
- `thresholds_ge1_to_ge200_with_coverage.csv`: `atlas_pairs_recomputed` and `atlas_targets_recomputed` are valid from 304-case source at >=20 only. `raw_pairs_reported_any_ge` rows below GE20 are archived summaries, not reproduced pair-level source data.

## PubChem records

- `R1_43pair_stage4_source_registry.csv`: immutable historical diagnostic selection of 43 pairs (29 target strata, 71 distinct AIDs). Historic single `NONINDEPENDENT_SAME_DISCOVERY_PROGRAM` label was **not a proof of physical duplication**.
- `stage5e_43pair_provisional_scientific_decision_dimensions.csv`: one row per historical pair; `ReviewerA_measurement_reuse` and `ReviewerA_physical_execution` are **UNRESOLVED** across all 43. `ReviewerA_discovery_program` is a separately documented program-association axis (**41 shared, 2 unresolved**), not an experimental copying label. `RULE_DERIVED*` columns contain retrospective sensitivity decisions and are **not necessarily explicit reviewer submissions**; 21 sign-offs remain pending.
- `original_result_tables_2026-10-17/*.csv`: original 12 full and 12 concise PubChem PUG REST export snapshots for the six-pair pilot, checksum-matched to the Stage6B manifest. AID is an *assay record*, CID is a *compound identity*, and SID is a *substance record*: **none is a physical plate/run ID**.
- `stage6c_kcnk9_sid88_concordance.csv`: one row per shared source SID for AIDs 540322 and 652211. `ALL20_Dose_and_SD_near_match=YES` means 10 dose-ratio and 10 SD fields matched *to ±0.0005001*, **not proven original raw measurement reuse**. Four SIDs were divergent.
- `stage6c_kcnk9_1760_dose_sd_comparisons.csv`: one row per shared SID × comparable field. `abs_difference` and `difference_within_0.0005001` describe deposited **processed output** agreement, not calibration or experimental matching.
- `stage6c_six_pair_frozen_vs_current_overlap.csv`: count comparisons between historical selected overlap and later complete PubChem retrieval. Changes do not independently identify why historical filters differed.
- `stage6c_source24_sha256_manifest.csv`: second-pass verification of the 24 source result CSVs.

## Integrity / missingness

Original author-uploaded ChEMBL archive bytes are not yet available in this GitHub deposit; `provenance/original_recovered_bundle_40file_sha256_manifest.csv` records the previously verified integrity audit, not substitute files. Explicit unresolved and missing values are scientifically meaningful and should **not** be filled, imputed or reclassified solely from shared compound overlap.
