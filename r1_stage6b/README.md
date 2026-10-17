# R1 Stage 6B — Empirical PubChem result-level pilot

**2026-10-17, GitHub Actions Run [38987545673](https://github.com/kiran978/AssayProvenance-Audit/actions/runs/38987545673).** Successfully fetched original *currently accessible deposited* concise and full PubChem assay-result CSVs for all 12 AIDs in six pilot pairs (**24/24 HTTP 200**). All 24 download SHA-256 hashes match the retrieval manifest. Frozen 43-pair analysis, original 71-AID descriptions, and Reviewer A selections unchanged.

**Artifacts:** [PUG REST download/replay script](./pilot_pubchem_result_audit.py), [GitHub Actions workflow](../.github/workflows/r1-stage6b-empirical-audit.yml), [per-pair quantitative result audit](./generated/pair_result_audit.csv), [file hashes and source columns](./generated/retrieval_manifest.csv), [run summary](./generated/run_summary.json). Raw complete CSVs are in the GitHub Actions artifact `R1-Stage6B-Original-PubChem-Result-Pilot` (retention 90 days) and separately packaged with the project owner's Stage 6B workbook.

## Pilot comparisons

| Pair | AIDs | Frozen shared CIDs | Current concise shared CIDs | Shared SIDs | Major caution |
|---|---|---:|---:|---:|---|
| 1 | 851 / 856 | 81 | 81 | 82 | Different S1P2 receptor assay vs optical-interference control |
| 2 | 624326 / 624327 | 1003 | 1011 | 1011 | Kinetic vs endpoint FAS-TE |
| 4 | 504699 / 504701 | 247 | 247 | 247 | Fluorescence vs HTRF; Reviewer A HOLD retained |
| 9 | 602166 / 602234 | 73 | 73 | 73 | SRC3 LogIC50 descriptive unit conflict |
| 11 | 540322 / 652211 | 55 | 88 | 88 | Strong near-identity of current deposited dose results |
| 18 | 652164 / 652165 | 34 | 39 | 39 | FAS-TE formats; endpoint exception still pending |

Frozen shared CID counts are not recomputed historical truths: count differences (+8/+33/+5) may reflect upstream filters or source snapshots and need direct reconciliation. Do not silently update frozen values.

## Crucial empirical findings from full result tables

- **Pair 11 KCNK9 (540322 / 652211):** 88 shared SIDs, each with 10 same-named dose-response ratio fields; **840/880** paired values agree to ±0.0005001, **84/88** SID ten-point profiles agree at all ten points within this descriptive rounding threshold, and **51/54** paired nonblank full-table IC50 are exactly identical. Four SID profiles diverge markedly. This warrants focused original measurement transfer/run provenance investigation, but **does not independently prove the same physical experiment or actual copied raw signals**. Reviewer dimensions remain UNRESOLVED.
- **Pair 9 SRC3:** All 229/229 (AID 602166) and 240/240 (AID 602234) evaluable full-source `LogIC50` values follow `log10(IC50[μM] × 10^-6)` within 0.02; none follows `log10(IC50[μM])`. The text metadata for 602234 erroneously refers to micromolar LogIC50 even though numerical values follow molar convention. Original values retained; reviewer normalization approval pending.
- **Pair 2 FAS-TE:** 19,965 paired nonblank same-named dose readings; only two are within 0.0005001; none of the 1,011 SID multi-dose profiles is wholly identical. Different current deposited response vectors are **not** proof of physically separate assay runs.

Full PubChem source CSVs have five nonmeasurement metadata rows; exclude them when counting original measurement entries. Matching SID/CID, fitted potency or outcome does not prove identical raw laboratory observations. In particular, SID represents *substance identity*, not assay plate/run identity.

## Scientific validation state

**Empirical result-row audit pilot COMPLETE. Provenance gold-standard control validation NOT ESTABLISHED.**

No independently authenticated positive control (documented reuse/transfer of the same physical source measurement) or negative control (documented separate origin/run; separate program if applicable) is available. Stage 6B case selection is hypothesis-driven, not blind independent external validation. No sensitivity, specificity, F1, AUROC, or definitive duplicated-experiment prevalence can be estimated.

Reviewer A's formal first-person declaration, prior Stage 5D source patch and four endpoint approvals, case 4 HOLD-rule reconciliation and raw plate/run evidence remain open. One human reviewer is the project policy; AI support was used for initial drafting and compilation and must be disclosed separately. No second reviewer will be pursued.

**Next gate:** Independent original measurement/plate provenance recovery for 540322/652211; reconcile frozen/current CID differences; if authenticated control examples remain unavailable, report this as a *source-value screening audit* with limitations, not a validated provenance classifier.
