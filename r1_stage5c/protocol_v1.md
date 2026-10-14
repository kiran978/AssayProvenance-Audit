# R1 Stage 5C — prospectively locked human validation rubric

**Prepared:** 2026-10-14. **Former JCIM manuscript:** ci-2026-03304f. **Status:** no human reviews yet.

This rubric was fixed for the independent validation stage **after the previous JCIM editorial decision**. It is not a claim that these rules were preregistered before the original study.

## Dataset and raters

Forty-three selected PubChem assay pairs (29 targets, 71 AIDs) require **two distinct, qualified human expert reviews**. Previous machine-generated / AI-assisted classifications must be hidden from both. Reviewers must not inspect each other's reports before both are locked. Do not grant external reviewers access to the internal repository containing prior labels: distribute separate neutral evidence packets outside GitHub. The principal investigator should record reviewer qualifications, roles, competing interests, independence statements, signature and review date.

## Three evidence dimensions

Each expert must give an evidence-supported category separately for:

1. **Data reuse:** CONFIRMED_REUSE / CONFIRMED_DISTINCT / UNRESOLVED.
2. **Experimental execution:** SAME_EXECUTION / DISTINCT_EXECUTION / UNRESOLVED.
3. **Discovery-program lineage:** SHARED_PROGRAM / DISTINCT_PROGRAMS / UNRESOLVED.

Same depositor or funding grant, orthogonal assay readouts, and numerical agreement do not alone establish physical data reuse, independent experiment execution, or common program membership. Source descriptions can document linked stages, but often cannot establish experimental run identity.

## Strict program-disjoint benchmark decision

- CONFIRMED_NOT_INDEPENDENT: affirmative evidence of reused measurements, same execution, **or** an explicitly shared discovery program.
- CONFIRMED_INDEPENDENT: affirmative evidence of distinct original measurements **and** distinct experimental execution **and** independent discovery programs.
- HOLD_UNRESOLVED: insufficient affirmative evidence to establish either conclusion.

**Program-level nonindependence does not assert copied measurements.** For each case, both PubChem source records must be inspected, primary paper/run or patent evidence sought where needed, and exact source URLs, quoted locations, rationales and limitations recorded. A missing independent-lineage proof is not proof of dependence.

## Reliability and final scientific sign-off

No reviewers have yet been recruited and no independent reviews have yet been submitted. Keep original machine labels frozen as historical outcomes; do not recalculate the 0/43 or network results from preliminary documentation alone.

Upon **two actual human reviews of all 43 pairs**, validate forms, then report raw 3-category agreement, 3x3 pairwise-agreement table, class-specific agreement, and Cohen's kappa only when estimable. κ is not validly estimable for a fully degenerate one-category table. Agreement is not correctness.

Disagreements or jointly unresolved cases require primary-document review and a documented consensus/third-person decision with conflict resolution notes. Independently verified **positive and negative control pairs** are additionally required to assess class discrimination; control evidence and verified labels have not yet been obtained.

**Do not store signed reviewer personal information or private reviewer verdicts in a public repository.** Retain only consented versions in a controlled research archive. Original historical frozen files remain read-only. All GitHub workflow checks of templates are software tests, not human-validation results.
