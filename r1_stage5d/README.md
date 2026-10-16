# R1 Stage 5D — Validation QC and independent-review readiness

**Prepared:** 2026-10-16. **Status:** SOURCE-CORRECTION WORKING COPY PRODUCED; REVIEWER SIGN-OFF AND INDEPENDENT VALIDATION PENDING.

The second submitted Reviewer A workbook for pairs 12–43 was audited against the original archived PubChem AID description JSONs and frozen 43-pair registry. The original workbook and frozen cohort remain unchanged.

## Verified integrity

- All 32 pair assignments match the 43-pair registry.
- All 53 original assay descriptions needed for these 32 pairs have verified SHA-256 hashes.
- Original reviewer scientific selections for measurement reuse, experimental execution, program lineage, endpoint compatibility, benchmark criteria, eligibility and confidence remain unchanged in the corrected working copy.
- Six pair rows contained invalid zero-indexed PubChem source locations. After checking the actual source text, ten individual AID locator replacements remove 22 out-of-range referenced positions. They remain **proposals awaiting Reviewer A confirmation**.

| Review pair | AID(s) requiring source reference repair | Original locator | Checked corrected locator |
|---|---|---|---|
| 13 | 504497, 588600 | `protocol[8–14]` | `protocol[8–13]` |
| 15 | 504488, 588599 | `protocol[10–14]` | `protocol[10–13]` |
| 16 | 623898 | `description[11–17]` | `description[1]` |
| 19 | 488904, 504497 | `protocol[8–14]` | `protocol[8–13]` |
| 20 | 504492, 588598 | `protocol[9–16]` | `protocol[9–15]` |
| 25 | 623898 | `description[11–17]` | `description[1]` |

## Scientific compatibility exceptions: original frozen vs Reviewer A submitted

| Pair | AID pair | Historical frozen | Reviewer A submission |
|---|---|---|---|
| 14 | 624343 / 624347 | `INCOMPATIBLE_FOR_INTENDED_ESTIMAND` | `SENSITIVITY_ONLY` |
| 18 | 652164 / 652165 | `COMPATIBLE` | `SENSITIVITY_ONLY` |
| 26 | 652286 / 652287 | `COMPATIBLE` | `SENSITIVITY_ONLY` |
| 33 | 1692 / 2332 | `COMPATIBLE` | `SENSITIVITY_ONLY` |

These are **not** silently reverted. They require an explicitly defined intended estimand, documentary rationale and reviewer approval. Source checks show PAF versus TNF-alpha IL-8 stimulation (Pair 14), endpoint versus kinetic FAS-TE fluorescence (Pairs 18 and 26), and different S1P4 reporter test formats with powder-based late-stage testing (Pair 33). Numeric pooling remains on hold for the disputed categories.

## Accuracy of the human-review claim

The project owner states that Reviewer A personally examined AI-drafted assessments. The earlier workbook declaration incorrectly suggested no AI assistance and a signed/blinded assessment. A truthful **first-person** signed statement remains necessary, documenting: qualifications, exactly which cases/records were verified, AI assistance, access to prior labels, conflicts, review dates, and personal approval of source and endpoint corrections. The manuscript may describe this as **AI-assisted human documentary verification** after genuine attestation. Do not claim an AI-free, fully blinded or independently consensus-reviewed process without it.

A distinct second qualified human's full 43-pair source-only review is not yet available. Agreement statistics, consensus labels, and any revised independent-program prevalence remain **NOT_ADJUDICATED**. Do not claim experimental measurement reuse just because assay records belong to the same program.

## Next acceptance gate — Stage 5E

1. Reviewer A confirms ten source-locator patches, resolves four endpoint categories or explicitly keeps them on HOLD, and signs an accurate first-person declaration.
2. A genuinely separate expert independently assesses the 43 source-only pairs, blinded to Reviewer A selections wherever feasible and reporting actual AI exposure.
3. Only then perform formal disagreement reconciliation and issue a separately versioned consensus benchmark. Never edit the original frozen 43-pair results.

**Full Stage 5D working workbook, correction manifest and integrity report** were prepared as local review artifacts. This GitHub record intentionally omits reviewer identity/signature details; secure personal attestations should not be committed to the repository.
