# R1 Stage 6C — Measurement-lineage investigation and historical CID reconciliation

**17 October 2026.** Stage 6C *deposited-result concordance and original-count checks* COMPLETE; original laboratory data-transfer/run authentication still OPEN. No original frozen data, signed reviewer findings or empirical evidence labels are overwritten.

## Source and verified quantitative result

- Stage 6B original 24 full/concise PubChem result CSVs: **24/24 SHA-256 verified** against the prior manifest; source run [38987545673](https://github.com/kiran978/AssayProvenance-Audit/actions/runs/38987545673).
- KCNK9/TASK3 AIDs [540322](https://pubchem.ncbi.nlm.nih.gov/bioassay/540322) and [652211](https://pubchem.ncbi.nlm.nih.gov/bioassay/652211): **88 shared SIDs**, each having ten comparable `Ratio at...` and ten `SD at...` fields.
- **84/88** SIDs have *all twenty* paired deposited values within absolute ±0.0005001; **840/880** dose-ratio pairs and **841/880** SD pairs within that post-hoc rounding tolerance.
- All 84 near-matching SID profiles have identical reported `N`, `IC50` string representations (including blanks) and activity outcomes. Across the 88 shared SIDs, **51/54 jointly nonblank IC50s are identical**.
- Divergent SIDs: `104221960` (CID 31520618), `104221966` (CID 49852192), `104221970` (CID 46785920), and `113635250` (CID 50919319). Their response profiles should not be erased or treated as duplicates.
- Example: SID 103059764, at 30 μM ratio **0.265625 vs 0.266**, SD **0.0121976 vs 0.012**, both reported IC50 1.84 μM and N=8. This supports a hypothesis of reformatting or reuse of *deposited values*; **direction, original physical experiment and transfer mechanism are not established**.

## External original documents

- [ML308 KCNK9 probe report](https://www.ncbi.nlm.nih.gov/books/NBK133427/) explicitly includes AID **540322** among KCNK9 SAR assays.
- [ML365 TASK1 report](https://www.ncbi.nlm.nih.gov/books/NBK179826/) and [assay inventory](https://www.ncbi.nlm.nih.gov/books/NBK179826/table/ml365.t2/) explicitly list AID **652211** as a TASK3 selectivity screen.
- Named project differences neither demonstrate independent experimental runs nor confirm reuse of raw detector signals. Neither report contains an authenticated cross-deposition transfer ledger for this pair.

## Frozen versus currently deposited CID intersections

| Stage 5C review pair | AIDs | Frozen selected shared CIDs | Current shared CIDs | Difference | Current both-active CIDs |
|---|---|---:|---:|---:|---:|
| 1 | 851 / 856 | 81 | 81 | 0 | 51 |
| 2 | 624326 / 624327 | 1003 | 1011 | +8 | 947 |
| 4 | 504699 / 504701 | 247 | 247 | 0 | 155 |
| 9 | 602166 / 602234 | 73 | 73 | 0 | 42 |
| 11 | 540322 / 652211 | 55 | 88 | +33 | 55 |
| 18 | 652164 / 652165 | 34 | 39 | +5 | 31 |

The frozen KCNK9 55 equals the currently shared *both-active* CIDs, but this is **not proof that both-active inclusion was the historical selection rule**. The exact original included CID lists and source-version/eligibility code remain unrecovered; the two other differing pairs do not fit this same simplistic active-only explanation. No re-labelling or alteration to frozen counts.

## Governance and validation limits

- The KCNK9 case is a **high-priority candidate to authenticate a source-data transfer/reuse pathway**, not an independently verified positive-control example.
- **Zero authenticated positive/negative experimental-provenance gold standards**, so no sensitivity, specificity, AUROC, F1 or false-positive estimates are justified.
- Preserve Reviewer A measurement reuse **UNRESOLVED**, execution **UNRESOLVED**, program lineage **UNRESOLVED**, strict benchmark **HOLD_UNRESOLVED** until actual source origin is checked and changes explicitly signed.
- One human reviewer with reported personal scientific verification; AI used to draft/compile. Signed declaration, ten proposed source-locator patches and four endpoint exception approvals remain pending. Project decision is not to recruit a second reviewer; avoid consensus/agreement claims.
- Existing Stage 5C rule was formalized after original JCIM reviewer criticism; do not misrepresent as original prospective preregistration.

## Reproducibility

A complete downloadable Stage 6C archive was prepared for the project owner with a **nine-sheet workbook**, 88-SID decision-transparent matrix, 1,760 cell-level comparisons, four-SID divergent record, six-pair frozen-vs-current counts, 24-file hash manifest, original input ZIP/frozen CSV and two reproduction scripts. The numerical analysis uses only Python standard libraries. All original source files and original labels are retained.

**Next stage 6D:** Seek original data-deposition transfer records, SID-level primary measurement files, normalization/data processing metadata and laboratory run/plate identifiers for AIDs 540322/652211, or report a conservative documented near-identity case study without authenticated ground truth.
