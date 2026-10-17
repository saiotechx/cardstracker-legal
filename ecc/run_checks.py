#!/usr/bin/env python3
"""Run declared baseline checks. Fail closed on missing/invalid checks.
Passing means only these checks passed; task-specific acceptance is separate.
"""
import json, pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
cfg = json.loads((ROOT / "ecc" / "verification.json").read_text())
checks = cfg.get("required_checks")
if not isinstance(checks, list) or not checks:
    sys.exit("ECC BLOCKED: no project checks configured")
for item in checks:
    ident = item["id"]
    if "files" in item:
        for relative in item["files"]:
            target = (ROOT / relative).resolve()
            if not target.is_relative_to(ROOT) or not target.is_file() or target.stat().st_size < 10:
                sys.exit(f"ECC FAILED: {ident}: file missing or too short: {relative}")
        print(f"ECC PASS: {ident}: structural files present (not semantic content review)", flush=True)
    else:
        argv = item.get("argv")
        if not isinstance(argv, list) or not argv or not all(isinstance(x,str) and x for x in argv):
            sys.exit(f"ECC BLOCKED: invalid command for {ident}")
        try:
            result = subprocess.run(argv,cwd=ROOT,timeout=1200,check=False)
        except (OSError,subprocess.TimeoutExpired) as error:
            sys.exit(f"ECC FAILED: {ident}: {error}")
        if result.returncode:
            sys.exit(f"ECC FAILED: {ident}: exit {result.returncode}")
        print(f"ECC PASS: {ident}: command succeeded", flush=True)
print("ECC PREFLIGHT PASS (not release authorization)", flush=True)
