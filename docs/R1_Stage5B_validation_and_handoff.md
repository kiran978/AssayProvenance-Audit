# R1 Stage 5B — 43-pair preliminary scientific assessment

**Status:** Complete as a documentary pre-adjudication research work package; **not** final expert adjudication.
**Study:** Former JCIM ci-2026-03304f.
**Date:** 14 October 2026.

## Source evidence and reproducibility

- [GitHub Actions Run #1 for Stage 5B](https://github.com/kiran978/AssayProvenance-Audit/actions/runs/38530398913): completed successfully.
- [Download the Stage 5B generated evidence artifact](https://github.com/kiran978/AssayProvenance-Audit/actions/runs/38530398913/artifacts/11877886775).
- [Stage 5B code](../r1_stage5b/build_documentary_adjudication.py) and [43-case documentary interpretation table](../r1_stage5b/data/43pair_documentary_interpretations.csv) are versioned.
- Workflow regenerates all outputs using 71 source-verified original PubChem assay-description JSON files downloaded in R1 Run 1.
- The retrieved artifact was checked after download: ZIP CRC intact, 43 pair rows, 71 AIDs, 86 verifiable source excerpts, 43 cases with shared recorded grant identifiers after normalization, 14 AID-xref pairs, **zero qualified independent reviewer decisions and zero new final provenance labels**.

The first-stage input is a **diagnostic cohort**, not a PubChem prevalence sample. Metadata or a grant link do not establish physical experiment reuse, independent experiment execution, or a unique source program. AID cross-references may demonstrate sequential experiments, selectivity screening or re-testing and must not be conflated with copied measurements.

## Critical cases for primary investigator review

- **KCNK9/TASK1**: AIDs 540322/652211 and 623898/652211 involve differently named research branches and different readout technologies. Shared organizational grants do not establish a single discovery program. Do not presume dependence without qualifying evidence.
- **p97**: 504649 denotes cell-based reporter and 504650 a biochemical ATPase test in the deposited PubChem records. Verify the reported discrepancy with the NIH summary-table entry and obtain specific run-level proof.
- **Late-stage powder retests and Set 2/Set 4**: Treat sequential screening stages and compound selection separately from physical experimental independence.
- **MITF/Orexin/SUMO**: Orthogonal technologies/counterscreens can differ in endpoints and compatibility; resolve compatibility separately from provenance.

## Requirement before updating the JCIM manuscript

Obtain two **genuine qualified human expert** reviews of the same 43 cases, blinded to frozen verdicts. Record source URLs, precise experimental relationship, reviewer credentials and review dates, disagreements and reconciliation outcomes. Keep the unresolved category when evidence is insufficient. Quantify class-wise agreement and chance-corrected agreement only when estimable.

**The original historical label `NONINDEPENDENT_SAME_DISCOVERY_PROGRAM` for 43 cases is stored for audit, not independently verified.** The source-descriptions alone do not justify a replacement 0/43 scientific conclusion. Do not recalculate provenance-filtered networks or claim benchmark leakage from these documentary observations alone.

GitHub Actions artifacts expire after 30 days; the downloaded primary-source and Stage 5B evidence ZIPs should be archived permanently in a suitable repository release/archive where redistribution terms permit.
