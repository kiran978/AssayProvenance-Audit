# R1 Stage 5C — Reviewer A, Pair 5: ASK1 / MAP3K5

**Recorded:** 2026-10-14. **Sequence:** Pair 5/43. **Frozen pair key:** `PUBCHEM::NP_005914::IC50::1159604::1159605`.

**Governance:** Author-coordinated and AI-assisted preliminary human assessment; not independent blinded external validation or a final reconciled consensus. Reviewer qualification/conflict declaration and a second qualified human assessment remain pending.

## Reviewer A — submitted selections (preserved verbatim)

```text
PAIR_NUMBER: 5/43
PAIR_ID: PUBCHEM::NP_005914::IC50::1159604::1159605

PRIMARY_RECORDS_EXAMINED: YES
TARGET_ACCESSION: NP_005914.1
SHARED_EXACT_CIDS_REPORTED: 215

DATA_REUSE: UNRESOLVED
EXPERIMENTAL_EXECUTION: UNRESOLVED
DISCOVERY_PROGRAM: SHARED_PROGRAM

PROGRAM_LINEAGE_EVIDENCE:
Both records explicitly identify primary AID 1159602.

MEASUREMENT_REUSE_EVIDENCE:
No affirmative evidence of copying or proven
independent raw measurement generation.

PHYSICAL_EXECUTION_EVIDENCE:
Different documented reaction procedures;
actual run-level independence unverified.

ENDPOINT_COMPATIBILITY: INCOMPATIBLE

STRICT_BENCHMARK_DECISION:
CONFIRMED_NOT_INDEPENDENT

ELIGIBILITY_RECOMMENDATION:
EXCLUDE_PAIR_FROM_INDEPENDENT_POTENCY_BENCHMARK

RETAIN_AID_1159604_AS: ARTIFACT_COUNTERSCREEN
RETAIN_AID_1159605_AS: ASK1_POTENCY_ASSAY

HUMAN_VALIDATION_STATUS: PENDING
```

## Documentary QA against the original PubChem depositor JSON (assistant; not independent expert adjudication)

Original records recovered by the successful R1 GitHub Actions Run #1 and checked by SHA-256:

- [AID 1159604](https://pubchem.ncbi.nlm.nih.gov/bioassay/1159604): `115f320eea374220afbcd5fe5e6b08bf3a0f7713d3bbbadb9e6120ad51e2ad7f`.
- [AID 1159605](https://pubchem.ncbi.nlm.nih.gov/bioassay/1159605): `db80be8da7fedd233bc7c448dc89f609cd78426c3781dfb2494773c625472698`.

**Exact source anchors:**

1. Both records `target[0].mol_id.protein_accession` = `NP_005914.1` (ASK1/MAP3K5). This target annotation on the TruHits counterscreen does *not* make its interference signal a direct ASK1 enzymatic potency measurement.
2. Both `description[0]`, `description[2]`, `description[4]`, `description[5]` name the Scripps screening center, assay provider/PI Derek Duckett and grant `1 R01 GM103957-01`.
3. Both `xref[0].xref.aid` explicitly identify **primary AID 1159602** as the upstream ASK1 inhibitor screen. This and shared center/provider/grant substantiate **SHARED_PROGRAM**. No evidence was found in the inspected descriptions proving that AIDs 1159604 and 1159605 copied one another's measurements.
4. AID **1159604**, `description[8]`, `protocol[2]`, `protocol[5]` describes the **AlphaScreen TruHits bead optical-interference counterscreen**, not the specific inhibition of ASK1 catalytic function.
5. AID **1159605**, `description[8]`, `protocol[2]`, `protocol[5]` describes the **ASK1 kinase assay** using ASK1 enzyme, MKK6, ATP, and AlphaScreen phospho-MKK6 detection.
6. Both `comment[0]` caution that experiments **may** have been split into screening campaigns and data are normalized per plate. This does **not** demonstrate either common or separate physical runs.
7. Frozen 43-pair Stage 4 registry lists **215 shared exact CIDs**, historical compatibility `INCOMPATIBLE_FOR_INTENDED_ESTIMAND`, and original provenance label `NONINDEPENDENT_SAME_DISCOVERY_PROGRAM`; the historical records are read-only, and compound overlap is not evidence of raw-data reuse.

## Reasoned eligibility decision — two distinct exclusion grounds

- **Provenance criterion:** Under the prospectively *Stage 5C-defined* strict **program-disjoint benchmark**, the affirmative shared program evidence supports the reviewer's `CONFIRMED_NOT_INDEPENDENT` *at the discovery-program lineage level*. It **does not** establish duplicated raw data, the same assay execution or nonindependence at the measurement level. The respective subdimensions remain `UNRESOLVED`.
- **Endpoint criterion:** TruHits optical-interference IC50 is not ASK1 catalytic inhibition IC50. For a direct ASK1 potency pairwise benchmark, the endpoints are incompatible regardless of their experimental provenance. Therefore `EXCLUDE_PAIR_FROM_INDEPENDENT_POTENCY_BENCHMARK` is independently justified.
- **Preservation:** AID 1159604 remains useful as an **artifact-interference counterscreen**; AID 1159605 is the **ASK1 potency assay**. Neither is discarded from the wider research record.

## Open requirements before formal validation

1. If a measurement-level claim is needed, inspect SID/CID table content, replicate and concentration-response source records, plate/run identifiers and laboratory source files where available.
2. Document reviewer qualification, conflicts, independence from authors and whether prior AI interpretations were seen; no falsely-blinded or independent-review claim.
3. Obtain another genuine human reviewer decision and resolve discrepancies by a documented procedure. Keep any final benchmark label and cohort changes in a *separately versioned adjudicated* output, never by rewriting the frozen cohort.
4. **Current status:** Reviewer A preliminary assessment documented; `HUMAN_VALIDATION_STATUS: PENDING`; final reconciled program label **not issued**.

**QA disposition:** The reviewer selections are mutually consistent **under the stated strict program-disjoint rule** and the ASK1-potency intended estimand. No hidden changes to the submitted decisions.
