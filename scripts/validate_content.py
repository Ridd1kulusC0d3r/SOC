#!/usr/bin/env python3
"""Validate curated SOC content; Python standard library only."""
import json
import re
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"id", "type", "level", "status", "review_cycle_days"}
PREFIXES = {"track": "tracks/", "sop": "sop/", "playbook": "playbooks/", "runbook": "runbooks/", "mssp": "mssp/"}

def fail(msg):
    print("ERROR:", msg, file=sys.stderr)
    raise SystemExit(1)

def main():
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    if catalog.get("schema_version") != "1.0.0": fail("unsupported schema")
    paths = catalog.get("paths", [])
    if not paths or len(paths) != len(set(paths)): fail("empty catalog or duplicate paths")
    ids = set()
    for path in paths:
        if path.startswith("/") or ".." in Path(path).parts: fail("unsafe path: " + path)
        file = ROOT / path
        if not file.is_file(): fail("missing: " + path)
        content = file.read_text(encoding="utf-8")
        if not content.startswith("---\n"): fail("no frontmatter: " + path)
        pieces = content.split("---\n", 2)
        if len(pieces) < 3: fail("malformed frontmatter: " + path)
        metadata = {}
        for line in pieces[1].splitlines():
            if ":" not in line: fail("malformed metadata: " + path)
            key, value = line.split(":", 1)
            metadata[key.strip()] = value.strip().strip(chr(34)).strip(chr(39))
        if not REQUIRED.issubset(metadata) or any(not metadata[x] for x in REQUIRED):
            fail("missing metadata: " + path)
        if metadata["id"] in ids: fail("duplicate ID: " + metadata["id"])
        ids.add(metadata["id"])
        if metadata["type"] not in PREFIXES or not path.startswith(PREFIXES[metadata["type"]]):
            fail("incorrect path/type: " + path)
        if not metadata["review_cycle_days"].isdigit(): fail("invalid review cycle: " + path)
        if len(content.splitlines()) < 15: fail("document too short: " + path)
    print(f"OK: {len(paths)} curated documents, unique IDs and valid frontmatter")

if __name__ == "__main__":
    main()
