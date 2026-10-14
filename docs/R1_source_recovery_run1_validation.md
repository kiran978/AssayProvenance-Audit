# R1 primary-source recovery — GitHub Actions Run #1

**Study:** JCIM ci-2026-03304f  
**Repository:** kiran978/AssayProvenance-Audit (private)  
**Run:** https://github.com/kiran978/AssayProvenance-Audit/actions/runs/38526148731  
**Commit that triggered the workflow:** `1b49a57ae5340beb6628e9f2d19a02e6a8b187e7`  
**Run status:** COMPLETED / SUCCESS (integrity and recover jobs)  
**Date:** 2026-10-14 UTC

## Source-recovery results

| Check | Observed |
|---|---:|
| Historical assay pairs in working registry | 43 |
| PubChem AIDs in frozen scope | 71 |
| Distinct targets | 29 |
| Official AID description JSON records fetched | 71 |
| Failed requests | 0 |
| Records in retrieval_log.csv | 71 |
| SHA-256 checks against retrieved JSON files | 71 passed; 0 mismatches |
| Invalid JSON responses | 0 |
| Independent human provenance reviews completed | 0 |

Source recovery used `https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/{aid}/description/JSON` and retained the raw response bytes together with timestamped source URLs, byte counts, and SHA-256 hashes.

## Evidence artifact

GitHub Actions artifact: [R1-PubChem-primary-source-retrieval](https://github.com/kiran978/AssayProvenance-Audit/actions/runs/38526148731/artifacts/11875648081)

- Artifact ID: `11875648081`
- ZIP archive size: 507,094 bytes
- ZIP SHA-256: `b9494267e7ea364ba9a2ae82c1622de705f997fd1994401da1883a8cd6724255`
- Contents: 71 `AID_*.description.json` files and `retrieval_log.csv` (72 entries total)
- GitHub Actions retention configured at 30 days; **download and archive the artifact before expiration**.

## Scientific interpretation

**A successful source download does NOT validate the historical 43 same-discovery-program classifications.** Shared depositor, shared grant, and shared discovery program can coexist with distinct assay experiments. Missing proof of independent programs does not itself prove dependence. The new 43-pair registry remains `NOT_ADJUDICATED`.

**Next requirement:** Manually examine both AID descriptions for all 43 pairs; verify record reuse, experiment execution and program lineage as separate dimensions; add documentary citations and reviewer notes; obtain genuine blinded independent human decisions; reconcile disagreements. Preserve the original archived frozen data and all original results unchanged until a separately versioned adjudicated release is authorized.

**Audit scope note:** This repository currently contains the 43-pair Stage 4 working registry and 71-AID manifest. The original frozen `P1_10D_FINAL_FROZEN_all43_pubchem_adjudicated.csv` is retained separately with SHA-256 `85a182baf53024067f0707d0e7cdab992b48e5446d4887d19723182ddb146c66`, not yet byte-for-byte replicated to GitHub.
