# R1 Stage 6 — Methodological validation and sensitivity analysis

**Prepared:** 2026-10-16. **Status:** operational-rule sensitivity and source-integrity checks COMPLETE; empirical provenance-control validation NOT ESTABLISHED.

Source: previously consolidated **43 selected PubChem assay pairs**, 29 target strata, 71 unique PubChem AIDs. All 71 archived original AID description JSONs were SHA-256-verified against the recorded source index; frozen pair keys, endpoint classifications, shared-CID counts and historic provenance labels were unchanged.

## Three separate meanings of independence
1. **Measurement reuse:** 43/43 `UNRESOLVED` — no affirmative proof of copied or distinct raw measurements.
2. **Physical experimental execution:** 43/43 `UNRESOLVED` — plate/run identity unverified.
3. **Discovery-program lineage:** 41 `SHARED_PROGRAM`, 2 `UNRESOLVED` — the unresolved pair records (Pairs 11 and 25) belong to the same KCNK9/TASK3 target.

Neither shared compounds nor shared program prove copied raw measurements. Failure to demonstrate independence is not evidence of dependence.

## Reproducibly calculated rule sensitivity

| Scenario | Operational condition | Excluded | HOLD | Hypothetical candidate pairs | Candidate targets | Confirmed independent |
|---|---|---:|---:|---:|---:|---:|
| S0 | Preserve Reviewer A submission, with 3 rule-derived exclusions flagged | 40 | 3 | 0 | 0 | 0 |
| S1 | Mechanical exclude all 41 SHARED_PROGRAM cases | 41 | 2 | 0 | 0 | 0 |
| S2 | Optimistically suppose unresolved program lineage is distinct | 41 | 0 | 2 | 1 | 0 |
| S3 | Require affirmative distinct measurements and executed runs | 0 | 43 | 0 | 0 | 0 |
| S4 | Counterfactually treat all 43 assays as physically independent; frozen COMPATIBLE only | 20 | 0 | 23 | 19 | 0 |
| S5 | Same unsupported assumption; frozen COMPATIBLE + SENSITIVITY_ONLY | 10 | 0 | 33 | 23 | 0 |
| S6 | Same unsupported assumption; explicit Reviewer A COMPATIBLE only | 25 | 0 | 18 | 16 | 0 |
| S7 | Same unsupported assumption; explicit Reviewer A COMPATIBLE + SENSITIVITY_ONLY | 12 | 0 | 31 | 23 | 0 |

S4–S7 exclusions are **endpoint filters under counterfactual universal physical independence**, not documented reuse and not real independent admissions. S1 is not an approved modification to Pair 4's explicit Reviewer A HOLD; S2 is unverified and does not meet the original eight-target criterion.

Historic endpoint strata: **23 COMPATIBLE, 10 SENSITIVITY_ONLY, 10 INCOMPATIBLE**; explicit Reviewer A strata for 39/43: **18 COMPATIBLE, 13 SENSITIVITY_ONLY, 8 INCOMPATIBLE**; four earlier assessments lack a separately submitted endpoint verdict. Pairs 14, 18, 26 and 33 changed compatibility labels in the human-reviewed draft but await first-person approval.

Within the *already selected 43 pairs*, a tightened historical shared-CID threshold of **≥100** leaves **10 raw pairs / 8 raw targets** and **≥200** leaves **8 raw pairs / 6 raw targets**, not confirmed independent target breadth. Original ChEMBL/BindingDB upstream selection and S1–S3 sensitivity queues were **not** rerun.

Graph of AIDs connected by original selected pairs: 33 components, 11 AIDs repeated between pairs, indicating a risk of reusing the same source assay in naive pair-level resampling. Graph components are not necessarily discovery programs.

## Validation gates

- No independently confirmed positive (proven copied/reused raw data) or negative (affirmatively distinct data, execution, and, where required, program) provenance-control pairs were present. These cannot be backfilled from the same original reviewed cases without circular evaluation.
- Classification sensitivity, specificity, F1, AUROC, chance-corrected human agreement and calibration cannot be estimated. No second independent human review will be pursued per project choice; disclose that limitation.
- First-person reviewer declaration, 10 source-locator approvals, four endpoint exceptions, Pair 4 HOLD rule reconciliation and initial three derived exclusions are pending; numeric dose-response and source run-level evidence still need recovery.
- The project owner reports human scientific verification and use of AI for initial drafting/compilation; this is disclosed separately from human scientific judgment. Do not claim AI-free, fully blinded, externally verified expert consensus.
- Rule protocol is documented **after the original JCIM rejection** and should **not** be described as the original study's preregistration.

**Reproducible artifacts:** Stage 6 Excel workbook with eleven sheets, eight-scenario CSV, 43-pair matrix, threshold grid, source-digest manifest, program/endpoint control candidates (**not gold standards**), and executable Python reconstruction script have been prepared as a downloadable archive by the project owner.

**Next gate (6B):** obtain independently evidenced original SID/CID measurement and experiment-run records and external known-truth positive/negative provenance controls if feasible; otherwise publish the operational sensitivity results with their explicit evidentiary limits. Address JCIM's outstanding ChEMBL/BindingDB source-family and modeling-method novelty criticisms separately.