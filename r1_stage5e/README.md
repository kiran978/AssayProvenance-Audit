# R1 Stage 5E — Consolidated 43-pair documentary review

**Assembled 2026-10-16.** Stage 5E **consolidation complete**; formal first-person reviewer sign-off and explicit case-level correction approvals **pending**. Original frozen 43-pair cohort and labels remain unchanged.

## Source inputs and traceability
- 43 original frozen PubChem assay pairs / 29 target strata / 71 distinct AIDs.
- 11 initial Reviewer A decisions recorded under [Stage 5C amendments](../r1_stage5c/amendments/); the amendment to AIDs 851/856 supersedes initial distinct/independent claims.
- 32 Reviewer A assessments transcribed from the returned Stage 5D workbook, `02_Review_32` (pairs 12–43).
- 71/71 original PubChem description JSON files match Stage 5B SHA-256 digests. Historical CID overlap remains archived, not independently recomputed from source result tables at this stage.

## Preliminary consolidated classifications
- Measurement reuse **UNRESOLVED 43/43**; physical experimental execution **UNRESOLVED 43/43**.
- Program lineage **SHARED_PROGRAM 41/43**; **UNRESOLVED 2/43**.
- Explicit reviewer strict-program selections: **CONFIRMED_NOT_INDEPENDENT 37**, **HOLD_UNRESOLVED 2**, **HOLD 1**, **not separately selected 3** (pairs 1–3). Pair 4 submitted HOLD is preserved even though its `COMMON_PROGRAM_LINEAGE: SUPPORTED` was normalized to `SHARED_PROGRAM` for rubric alignment.
- Applying the *strict program-disjoint rule*, and marking derivations explicitly: **37 explicitly provisionally excluded**, **3 rule-derived exclusions pending explicit reviewer confirmation**, **3 HOLD** (pairs 4, 11, 25). **Zero pairs are admitted as confirmed independent.**
- The 43 source-evidence pairs are consolidated; no final consensus-labelled benchmark has been released.
- **No pair is proven to share copied raw measurements** by the documentary evidence. `CONFIRMED_NOT_INDEPENDENT` denotes *non-disjoint discovery programs under the adopted rule*, not raw-plate duplication.

## Remaining QC and reviewer approval
1. Reviewers have not personally signed off on the ten technically repaired source locators spanning six cases (13,15,16,19,20,25).
2. Endpoint-compatibility exceptions at pairs 14,18,26,33 retain their submitted `SENSITIVITY_ONLY` classifications without silently replacing frozen labels; intended-estimand-based human acceptance is pending.
3. Case 4 `SHARED_PROGRAM` and explicit reviewer `HOLD` must be reconciled at the decision-rule level; pair 9 LogIC50 units and pair 11 source xref/concentration metadata still need original-result verification.
4. The project owner reports one human reviewer personally checked scientific assessments, with AI used in initial drafting and compilation. The workbook's **first-person declaration remains unsigned** and credentials, review dates and competing interests not established. Do **not** characterize as AI-free, fully blinded, externally validated or two-reviewer consensus.
5. The project elected **not to pursue a second independent human review**. This is a transparent deviation from the earlier [two-reviewer Stage 5C protocol](../r1_stage5c/protocol_v1.md); avoid inter-rater reliability statistics or claims.

**Stage 6 recommendation:** Empirical positive/negative provenance controls, selected SID/CID result-level audit, strict-vs-relaxed program-lineage sensitivity analysis and uncertainty-aware reanalysis before manuscript revision.

The complete Stage 5E Excel, CSV, source archive and reproducibility package were prepared for project-owner download, not committed here to avoid inadvertently publishing reviewer details.
