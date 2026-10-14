#!/usr/bin/env python3
"""Validate Stage 4 source-recovery inputs; never assert expert adjudication."""
import collections
import csv
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]

def read(relative_path):
    with (ROOT / relative_path).open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))

def main():
    registry = read("data/R1_43pair_stage4_source_registry.csv")
    manifest = read("data/R1_71_aid_retrieval_manifest.csv")
    assert len(registry) == 43, f"Expected 43 pairs; found {len(registry)}"
    assert len(manifest) == 71, f"Expected 71 AIDs; found {len(manifest)}"
    assert len({row["pair_key"] for row in registry}) == 43, "Duplicate pair ID"
    aids = {str(int(aid)) for row in registry for aid in (row["aid_a"], row["aid_b"])}
    manifest_aids = {str(int(row["aid"])) for row in manifest}
    assert aids == manifest_aids, "Manifest differs from 43-pair registry AIDs"
    assert len(aids) == 71, "Wrong AID count"
    assert len({row["target"] for row in registry}) == 29, "Wrong target count"
    assert collections.Counter(row["historical_compatibility_label_FROZEN"]
                               for row in registry) == {
                                   "COMPATIBLE": 23,
                                   "SENSITIVITY_ONLY": 10,
                                   "INCOMPATIBLE_FOR_INTENDED_ESTIMAND": 10
                               }
    assert all(row["historical_provenance_label_FROZEN_DO_NOT_OVERRIDE"]
               == "NONINDEPENDENT_SAME_DISCOVERY_PROGRAM" for row in registry)
    assert all(row["final_independence_status"] == "NOT_ADJUDICATED"
               for row in registry)
    assert all(not row["reviewer_1_decision"] and not row["reviewer_2_decision"]
               for row in registry)
    print("PASS: 43 historical pairs, 71 AIDs, 29 targets, 23/10/10 compatibility; "
          "0 independent human decisions; no historical labels modified.")

if __name__ == "__main__":
    main()
