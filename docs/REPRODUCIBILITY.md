# Reproducing the deposited research results

## Requirements and quick run

- Python 3.10+ with **standard library only** for the committed primary count-validation script.
- Data are checked **within their original source-specific denominators**.

```bash
git clone https://github.com/kiran978/AssayProvenance-Audit.git
cd AssayProvenance-Audit
python scripts/verify_public_evidence.py
```

Expected successful exit: all `PASS` checks, including ChEMBL **304/240/64/28/36**, 201 GE30 pairs, PubChem **43/41/2** and KCNK9 **88/84/1,681 of 1,760**. The [automatic verification workflow](../.github/workflows/verify-and-deposit-evidence.yml) successfully ran on GitHub; it also deposited 24 intact PubChem exports from the Stage 6B original workflow run.

## Primary source snapshots and file integrity

The original PubChem result files downloaded in the original pilot run on **2026-10-17 UTC** are now committed in [data/pubchem/original_result_tables_2026-10-17](../data/pubchem/original_result_tables_2026-10-17/) as 12 full and 12 concise CSVs. All 24 match the SHA-256 values in [the retriever's original manifest](../r1_stage6b/generated/retrieval_manifest.csv). **Do not re-fetch current PubChem exports and silently overwrite these frozen data**; create a new dated snapshot to evaluate drift.

For re-retrieval and initial exploratory comparisons, run:
```bash
python r1_stage6b/pilot_pubchem_result_audit.py
```
This script **contacts live PubChem PUG REST**, so numerical values or counts can change, and outputs should be versioned separately. GitHub Actions workflow [stage6b](../.github/workflows/r1-stage6b-empirical-audit.yml) retains historical retrieval code and logs. PUG REST is a public source; its availability is not guaranteed.

The earlier ChEMBL original author-supplied archive's **40-file SHA-256 audit** is preserved in [the integrity manifest](../provenance/original_recovered_bundle_40file_sha256_manifest.csv). The 304, 64, 36 and 78 case-level **derived snapshots** are committed, but the *source archive and original ChEMBL37 SQLite have not been fully deposited*, so the complete raw-database extraction cannot be independently replayed from this repository alone.

## Reproduction boundaries

1. ChEMBL cutoff **>=20** can be re-filtered within the 304 original pairs. **GE10=360** is a historical *summary-only* result because the additional 56 pair rows are unavailable. Do not claim a GE10 source/family adjudication.
2. Bibliographic title duplicate-review flags do not prove raw measurement duplication. The ChEMBL final 36 manual case dispositions were missing; independent target/source-family group count **1** is a *historical unverified summary*, not a verified 36-to-1 pair attrition.
3. BindingDB release **202609** 46 candidate pairs/eight candidate targets is **summary only**, and the original pair ledger is missing. It has not been replayed at 10,20,30 thresholds.
4. Single-reviewer decisions contain unresolved original measurement and execution identities; 21 targeted first-person approvals remain pending. Absence of a second qualified reviewer should be acknowledged, not converted into agreement statistics.
5. KCNK9 numerical equality is a deposited processed result comparison. Its **0.0005001 post-hoc threshold** is not proof of copied raw instrument signals, assay plate identity or data transfer direction.
6. No proven raw-reuse positive/negative controls or predictive-model benchmarking were available.

## Manuscript-data alignment

- **ChEMBL figure:** use `strict_s0_ge20_atlas_304.csv` and `cross_document_64_triage.csv`; report raw count units.
- **Program vs execution:** use `stage5e_43pair_provisional_scientific_decision_dimensions.csv`; the unapproved exceptions and human sign-off are preserved as status.
- **KCNK9 concordance:** join all 1,760 difference rows to 88 SID summaries; preserve four divergent SIDs.
- **Frozen/current CID counts:** `stage6c_six_pair_frozen_vs_current_overlap.csv`; never overwrite the historical frozen shared CID counts.
