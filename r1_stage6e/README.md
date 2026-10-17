# R1 Stage 6E — Pre-submission cross-source validation audit

**Prepared 2026-10-17. Status: PARTIAL CLOSURE; NOT final manuscript/submission-ready validation.** This stage precedes manuscript reconstruction and audits the original peer-review concerns about ChEMBL/BindingDB attrition, overlap cutoffs, reviewer signoff and limitations. The original frozen 43 PubChem cases and source-dimension selections are unchanged.

## Verified calculations from the frozen selected PubChem set
| Exact CID cutoff | selected pair count | target count | shared-program labels | program-unresolved |
|---:|---:|---:|---:|---:|
| 10 | 43 | 29 | 41 | 2 |
| 20 | 43 | 29 | 41 | 2 |
| 30 | 30 | 24 | 29 | 1 |
| 40 | 22 | 19 | 21 | 1 |
| 50 | 17 | 14 | 16 | 1 |
| 100 | 10 | 8 | 10 | 0 |
| 200 | 8 | 6 | 8 | 0 |

**Left truncation:** GE10 means re-filtering an original GE20-selected 43-pair cohort, not rediscovering the omitted GE10–19 pairs. These results do **not** test source-wide ChEMBL or BindingDB cutoff robustness. No confirmed independent raw-measurement or execution provenance is inferred.

## Original ChEMBL 37 funnel, evidence and unit boundary
- **304** S0 GE20 pairs / 102 targets, **240** same-document pairs, **64** cross-document pairs.
- **36** pre-manual cross-document candidate pairs / 22 targets. Therefore **28** of 64 were removed before manual review (arithmetic only); case-level reasons unavailable.
- Original manuscript reports **one independent target/source-family group**. This is **not a pair count**. Do not present '36→1' as pair-level attrition or relabel the other 35 pairs without original manual ledger.
- Historical S1/S2/S3 pair/target counts **588/225**, **889/296**, **1036/287** are GE20 filter-relaxation results, not GE10/GE30 re-discoveries.
- 304 original pair IDs and 36 manual source-family decisions and official ChEMBL 37 SQLite have not been recovered for this stage; full GE10/20/30 is **NOT RUN**.

## Original BindingDB 202609 funnel and source gate
- Reported **46 cross-document GE20 candidates** over **eight raw candidate target identifiers**.
- A breadth gate requiring **at least eight adequately supported independent eligible targets** cannot be satisfied solely from eight raw candidate targets. Original 46 pair/source-family ledger and exact exclusion outcomes absent, so the failure mechanism remains **reported, not independently verified**.
- Official frozen [BindingDB 202609 archive listing](https://bdb8.ucsd.edu/rwd/bind/chemsearch/marvin/Download.jsp) located, but actual release TSV/mapping and original source-family selections were not downloaded. Do not swap 202610 for 202609.

## Human reviewer approval & methodology
- 21 explicit approval records tracked: ten locator patches, four endpoint changes (Pairs 14,18,26,33), three rule-derived exclusions (Pairs 1–3), Pair 4 HOLD reconciliation, signed first-person reviewer attestation, Pair 9 numerical units and Pair 11 deposited-value concordance caveat.
- User reports human scientific verification and AI drafting/compilation; no signed first-person record supplied. No second reviewer will be sought. Do not claim double blind or inter-rater agreement.
- No authenticated provenance positive/negative experimental controls; no classifier sensitivity/specificity/AUROC. Shared programs do not mean identical assay measurements. Source-specific analytic units must remain distinct.
- Prior-art novelty (Kalliokoski 2013; Landrum/Riniker 2024), selection biases, original protocol dates and end-to-end cross-source reproducibility remain high-risk reviewer concerns.

A reproducible ZIP containing **nine-sheet audit workbook**, 43 individual pair thresholds, reviewer correction queue, methodological limitations, data-source register, strict ChEMBL37 SQLite extraction helper, BindingDB202609 explicit-mapping normalizer and generic GE10/20/30 discovery sweep has been prepared in the conversation workspace. These helper scripts passed **synthetic smoke tests**, but their absent real source inputs prevent a claim of original cross-source replay.

**Recommended next acquisition:** original 304 ChEMBL pair table + 36 manual decisions + 46 BindingDB candidate/source-family table, plus original source configuration/DB release checksums. If unavailable, constrain journal manuscript to a selected PubChem evidence case-study rather than claiming a validated cross-source negative-feasibility result.