# R1 Stage 6D — Original data-lineage authentication and manuscript evidence

**Date:** 2026-10-17. **Status:** evidence-source investigation and publication text **prepared for author review**; authentication of original experimental runs **NOT ESTABLISHED**. Historical 43-pair labels and Reviewer A selections remain unchanged.

## Newly source-corroborated KCNK9/TASK3 findings

- Archived original PubChem full/concise assay result CSVs **24/24 SHA-256 verified**. Stage 6B original source download: [Actions run 38987545673](https://github.com/kiran978/AssayProvenance-Audit/actions/runs/38987545673).
- PubChem AIDs [540322](https://pubchem.ncbi.nlm.nih.gov/bioassay/540322) and [652211](https://pubchem.ncbi.nlm.nih.gov/bioassay/652211) share **88 exact substance IDs**. Of these, **84/88** have all **20** matched dose-ratio and SD columns within **±0.0005001** (post-hoc descriptive tolerance); **1681/1760** cells near-matched across the full 88-SID table. **51/54** paired nonblank deposited IC50 values are identical.
- In the **84** near-matched SID profiles, **1494/1680** values in AID 540322 equal the corresponding AID 652211 values after the former are rounded to three decimal places. This supports a possible representation/transformation link but **cannot establish transfer direction or original run identity**.
- SID-shuffling (fixed seed **6162026**, **10,000 permutations**) yielded mean **0.9744**, maximum **6** complete profiles aligned by chance under this constructed analytic shuffle, compared with **84** at true SID pairing. **0/7656** off-diagonal pairs of distinct SIDs meet the 20-field tolerance. This is **only a substance-alignment check**, not an experimental provenance negative control, classifier test or physical dependence probability.
- Four SID result profiles diverge: **104221960, 104221966, 104221970, 113635250**.
- **New published anchoring for a divergent row:** NIH's original [ML365 report](https://www.ncbi.nlm.nih.gov/books/NBK179826/) identifies SID **104221970** / CID **46785920** as the ML365 molecule, includes AID **652211** in the TASK3 selectivity assay, and describes ML365 TASK3 IC50 **0.26 ± 0.02 µM (n=4)**. Current AID 652211 lists **0.26 µM** for this SID, whereas AID 540322 lists **2.72 µM**. This corroborates the biological provenance *context* for that exceptional deposited row; it does not authenticate the 84 other shared profiles.
- [ML308 report](https://www.ncbi.nlm.nih.gov/books/NBK133427/) associates AID 540322 with a separate named probe project. Original depositor source IDs differ (`KCNK9_Inh_SAR_CRC_2` vs `TASK1_Inh_SAR_TASK3_CRC`), while the records share a Johns Hopkins Ion Channel Center affiliation and grant. Archived source dates **2012-06-21** and **2013-11-04** are **not authenticated experiment acquisition dates**. AID 652211's public deposit date is **2013-03-28** and modify date **2013-11-04**; see [PubChem date semantics](https://pubchem.ncbi.nlm.nih.gov/docs/record-dates).

## Verification boundary

**Original instrument raw files, original plate/run identity, transfer/version logs and depositor confirmation have NOT been recovered.** No laboratory has been contacted by this stage. Do not classify this pair as a gold-standard duplicate run or prove data reuse from the close processed values alone. Reviewer A's **UNRESOLVED** selections for data reuse, execution, program lineage, and **HOLD_UNRESOLVED** benchmark disposition remain untouched.

Frozen/current selected CID intersection differences (**1003→1011**, **55→88**, **34→39**) remain unreconciled without the historical exact CID sets and original selection code; the KCNK9 frozen 55 coincides with the current both-active count but cannot authenticate the original filter.

No second independent human reviewer is being sought, per project choice. The owner reports personal human scientific verification with AI used for original drafting/compilation; the original first-person declaration, source-locator approvals and endpoint exception approvals remain pending. A revised journal manuscript must acknowledge missing authenticated controls, post-review rule changes, the selected-cohort limitations and outstanding upstream ChEMBL/BindingDB sensitivity/attrition reconstruction.

## Prepared reproducible deliverables

A local Stage 6D package includes **10-sheet Excel evidence workbook**, 88-SID screen, 1760-cell comparator, four divergent SIDs, 24-file SHA-256 check, 10k SID-shuffle test with fixed random seed, original public PubChem result and description ZIPs, a standard-library reproduction script, original evidence report, manuscript-ready Methods/Results/Discussion/Limitations language, and a **draft-only, unsent** scientific inquiry to the original data custodian.

**Final status:** empirical evidence finalized for human author review; direct measurement-lineage authentication is still open and must not be claimed as achieved.
