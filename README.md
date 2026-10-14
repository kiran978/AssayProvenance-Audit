# AssayProvenance-Audit

Evidence recovery and provenance adjudication for **JCIM manuscript ci-2026-03304f**.

**Status:** R1 source-recovery stage, *not* validated expert adjudication.

The original frozen PubChem cohort contained 43 assay pairs, 71 distinct PubChem AIDs, and 29 targets. The archive recorded 23 COMPATIBLE, 10 SENSITIVITY_ONLY, and 10 INCOMPATIBLE_FOR_INTENDED_ESTIMAND pairs; the previous 43 NONINDEPENDENT_SAME_DISCOVERY_PROGRAM labels are historical **unvalidated** findings. **No independent human reviewer decisions have been obtained.**

The repository's `data/R1_43pair_stage4_source_registry.csv` preserves the historical labels in explicitly marked columns, while keeping new decisions `NOT_ADJUDICATED`. The source-recovery workflow downloads **assay descriptions only** from official PubChem PUG REST; it does **not** claim pair independence/dependence and does **not** publish compound-level data.

For the original frozen P1_10D CSV, consult the separately retained frozen source archive (SHA-256 `85a182baf53024067f0707d0e7cdab992b48e5446d4887d19723182ddb146c66`). This repository's lightweight source-recovery task currently validates the 43-pair registry and 71-AID manifest but does **not** replace a full byte-for-byte archive rerun.

To start or re-run recovery: **Actions → R1 PubChem source recovery → Run workflow**. On completion, download the `R1-PubChem-primary-source-retrieval` artifact for original JSON and SHA-256 retrieval log. Artifacts expire after 30 days. Partial failures may occur; check `retrieval_log.csv` for every AID.

Publication or interpretation of provenance classifications requires direct source inspection, a formal independence definition, and blinded independent human review. See the original R1 work package for the full researcher-facing workbook and the review protocol.
