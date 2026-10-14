# R1 Stage 5C — Reviewer A, Pair 3: CHT AID 504840 vs 588401

**Recorded:** 2026-10-14  
**Reviewer sequence:** 3 of 43  
**Frozen cohort pair key:** `PUBCHEM::NP_068587::IC50::504840::588401`  
**Review governance:** Author-coordinated, AI-assisted, non-blinded preliminary human assessment, **not** independent external adjudication. Credentials, conflicts, contemporaneous reviewer declaration, and a second independent human review remain pending.

## Reviewer A's submitted decision — unchanged

| Dimension | Selected classification |
|---|---|
| Measurement reuse | `UNRESOLVED` |
| Physical experimental execution | `UNRESOLVED` |
| Discovery-program lineage | `SHARED_PROGRAM` |

**Reviewer rationale submitted:** CHT project summary [PubChem AID 1053196](https://pubchem.ncbi.nlm.nih.gov/bioassay/1053196), Section 1, explicitly lists the five-point CRC AID 504840 and ten-point CRC AID 588401 as steps in the same inhibitor hit-validation program. The source reports a final 256 compounds categorized active based on combined confirmation/counterscreen evidence, *not* by this pair alone. The two AIDs describe different concentration-series designs but do not provide conclusive plate/run or raw-measurement reuse records. Reviewer A reports live PubChem page access barriers; this audit separately checked the previously archived official JSON records and the web-indexed project summary.

## Assistant documentary QA (not a replacement for Reviewer A)

Original PubChem JSON files in the archived `R1-PubChem-primary-source-retrieval.zip`:

- AID [504840](https://pubchem.ncbi.nlm.nih.gov/bioassay/504840): SHA-256 `4fbd3e7dfc60f39966a2bb1389f276d0be44c840889c75aa3db285d93ed1a68c`.
- AID [588401](https://pubchem.ncbi.nlm.nih.gov/bioassay/588401): SHA-256 `74009a4b1aa733defe12226f1f399e24e213904956b5d95bb8e16676471da0b2`.
- Both `description[9]`: grant `1R03DA028852-01`, Johns Hopkins Ion Channel Center; both `description[7]`: assay provider Alicia Ruggiero; both `description[6]`: screening center PI Min Li.
- Both `protocol[0]`: 5-point vs 10-point CRC, otherwise nearly identical introductory assay objective.
- **Source nuance:** 42 of 43 entries in the two archived `protocol[]` arrays are byte-for-byte text-equal. Only `protocol[0]` differs (5-point vs 10-point CRC). This demonstrates protocol-description reuse/common experimental design, **not** identical measurement data or the same physical run.
- Both `xref[]` lists point to shared upstream AIDs 488997, 488975, 493221 and 493222; neither archived description explicitly xrefs the other member of the pair. Their interrelationship is **affirmatively documented** by AID 1053196.
- The historical frozen 43-pair registry lists **274 shared exact CIDs**, historical potency-compatibility label `COMPATIBLE`, and the original unverified provenance label `NONINDEPENDENT_SAME_DISCOVERY_PROGRAM`. These historical labels remain unchanged, and CID overlap does not imply raw measurement reuse.
- PubChem AID [1053196](https://pubchem.ncbi.nlm.nih.gov/bioassay/1053196) was deposited on **2014-07-24**, later than the first 2011 source assay. It is a depositor-provided retrospective summary of how data from multiple assays were combined; it is **not** an experimental plate/run log.

## Evaluated evidentiary support

- **Measurement reuse — UNRESOLVED.** No affirmative result-level comparison/plate provenance in the assessed sources demonstrates either same or distinct raw measurements. Duplicate protocols alone are not duplicate data.
- **Execution — UNRESOLVED.** CRC series with different point counts do not prove or refute distinct physical experimental runs.
- **Discovery-program lineage — SHARED_PROGRAM.** Affiliated grant, provider, assaying center, shared source AID references and especially the explicit project summary support this classification.

## Outstanding evidence / sign-off

(1) Compare PubChem source assay tables at exact SID/CID, concentration-response and raw/summary signal fields; (2) search for original experiment/plate identifiers and dates, replicate mappings and lab records; (3) obtain Reviewer A's signed conflict/qualification declaration; (4) obtain separate qualified reviewer evaluation; (5) reconcile actual human disagreements. If no more evidence becomes available, preserve UNRESOLVED rather than inventing certainty.

**Review-state:** Preliminary Reviewer A classifications recorded as selected; **not** final consensus; **no historical-label mutation**. Manuscript benchmark labels and counts must not be updated on this basis.
