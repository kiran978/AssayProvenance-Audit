# Evidence maturity and unresolved validation gates

_Last reviewed 2026-10-18; proposed journal: Clinica Chimica Acta, not submitted._

| Component | Reproducible? | Boundary |
|---|---|---|
| ChEMBL S0 GE20 304/102; same-document 240; cross-document 64 | YES, derived frozen case-level files | Original ChEMBL37 SQLite not deposited |
| ChEMBL 28 source-title duplicate review flags → 36 candidates | YES, automated triage records | No 28 raw-duplicate proof; 36 final human judgments missing |
| ChEMBL GE30 201/66, 24 cross-document and six candidates | YES, within original GE20 atlas | Cannot infer finalized independent GE30 targets |
| ChEMBL GE10 360 pairs | HISTORICAL SUMMARY ONLY | 56 GE10–19 pair rows unavailable |
| ChEMBL S1/S2/S3 78 additional review cases | YES, source queue | Human case decisions missing |
| BindingDB 202609 46 cross-document candidates/eight targets | HISTORICAL SUMMARY ONLY | Exact 46-case source/candidate ledger and original 202609 source mapping missing |
| PubChem frozen 43 cases, 29 target strata, 71 AIDs | YES, fixed cohort | Purposively selected subset, not random prevalence sample |
| PubChem source program categories 41 shared, two unresolved | YES, provisional case-level entries | Human first-person approval pending; does not prove duplicated experiments |
| PubChem original 24 result CSVs | YES, original archival SHA-256 source snapshot | No original plate/run/depositor-transfer ledger |
| KCNK9/TASK3 84/88 20-field profile near-matches | YES, 88 SID and 1,760 field rows | Processed-result concordance; raw reuse/run identity unknown |
| Verified empirical positive/negative reuse controls | NO | Cannot calculate classifier metrics |
| Second independent human adjudication | NOT PERFORMED | No between-reviewer kappa or consensus claims |
| Reviewer A 21 item first-person corrections | PENDING | No fabricated signed or backdated approval |
| Public availability/DOI | NOT YET | GitHub remains private; no verified Zenodo DOI or public research release |

## Nonnegotiable interpretation rules

- Distinguish **same source program**, **same document**, **copied processed values** and **same laboratory measurement/run**. None logically entails the other without the appropriate provenance evidence.
- 43 apparent pair-network edges -> 0 *program-disjoint confirmed* edges is a deterministic rule-based eligibility result, **not** a measured false-positive rate, classifier accuracy or proof all 43 share copied raw values.
- ChEMBL/BindingDB/PubChem discovery cohorts use different units and sampling funnels; avoid pooled independence rate or naive numerical attrition across units.
- The post-JCIM review Stage5C strict program-disjoint rule was documented retrospectively. Do not call it prospective preregistration.
- Before public release, verify rights in original-source representations, author/co-author consent and human review status; do not upload unapproved signed forms or personal email threads.

Full original project-stage records remain in `r1_stage5*` and `r1_stage6*` directories to preserve provenance.
