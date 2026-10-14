#!/usr/bin/env python3
"""Retrieve official PubChem BioAssay descriptions, without provenance adjudication.
Python >=3.10, standard library. Save original response bytes and SHA256.
"""
import argparse
import csv
import datetime
import hashlib
import json
import pathlib
import random
import time
from urllib import request, error

BASE = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/{aid}/description/JSON"

def download(aid, timeout=45, retries=5):
    url = BASE.format(aid=aid)
    headers = {"User-Agent": "AssayProvenance-Audit/0.4 (academic bioassay curation)",
               "Accept": "application/json"}
    for attempt in range(retries):
        try:
            req = request.Request(url, headers=headers)
            with request.urlopen(req, timeout=timeout) as resp:
                raw = resp.read()
            document = json.loads(raw.decode("utf-8"))
            if not isinstance(document, dict):
                raise ValueError("PubChem response is not a JSON object")
            return raw, url, ""
        except (error.HTTPError, error.URLError, TimeoutError,
                ValueError, UnicodeDecodeError) as exc:
            message = str(exc)
            if isinstance(exc, error.HTTPError) and exc.code in (400, 401, 403, 404):
                return None, url, message
            if attempt == retries - 1:
                return None, url, message
            time.sleep(min(12, 2 ** attempt + random.random()))
    return None, url, "retry_exhausted"

def run(manifest, output, delay, overwrite=False):
    output.mkdir(parents=True, exist_ok=True)
    with manifest.open(newline="", encoding="utf-8-sig") as stream:
        records = list(csv.DictReader(stream))
    if len(records) != 71 or len({r["aid"] for r in records}) != 71:
        raise ValueError("Manifest must contain exactly 71 unique AIDs")
    log = []
    for position, item in enumerate(records, 1):
        aid = str(int(item["aid"]))
        destination = output / ("AID_" + aid + ".description.json")
        if destination.exists() and not overwrite:
            raw = destination.read_bytes()
            status, err = "REUSED_EXISTING", ""
        else:
            raw, _, err = download(aid)
            if raw is None:
                status = "FAILED"
            else:
                destination.write_bytes(raw)
                status = "DOWNLOADED"
        log.append({
            "aid": aid,
            "timestamp_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "state": status,
            "source_url": BASE.format(aid=aid),
            "sha256": hashlib.sha256(raw).hexdigest() if raw else "",
            "bytes": len(raw) if raw else 0,
            "error": err if status == "FAILED" else "",
        })
        print(f"[{position}/{len(records)}] AID {aid}: {status}", flush=True)
        if position < len(records):
            time.sleep(max(0.0, delay))
    with (output / "retrieval_log.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(log[0]))
        writer.writeheader()
        writer.writerows(log)
    failures = sum(row["state"] == "FAILED" for row in log)
    print(f"PubChem source retrieval: {len(log) - failures} succeeded, {failures} failed.", flush=True)
    return failures

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=pathlib.Path,
        default=pathlib.Path("data/R1_71_aid_retrieval_manifest.csv"))
    parser.add_argument("--output", type=pathlib.Path,
        default=pathlib.Path("raw_pubchem"))
    parser.add_argument("--delay", type=float, default=0.5)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    raise SystemExit(int(run(args.manifest, args.output, args.delay, args.overwrite) > 0))
