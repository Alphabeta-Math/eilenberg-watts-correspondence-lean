#!/usr/bin/env python3
"""Build local sources in import order, retaining complete diagnostics."""
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "evidence/extraction-manifest.json").read_text())
modules = {entry["module"]: entry for entry in manifest["sourceFiles"]}
order, done, active = [], set(), set()
def visit(name):
    if name not in modules or name in done:
        return
    if name in active:
        raise RuntimeError(f"Import cycle: {name}")
    active.add(name)
    for dep in modules[name]["imports"]:
        visit(dep)
    active.remove(name)
    done.add(name)
    order.append(name)
for name in modules:
    visit(name)
with (ROOT / "evidence/standalone-build.log").open("w") as log:
    for index, name in enumerate(order, 1):
        print(f"[{index}/{len(order)}] {name}", flush=True)
        subprocess.run(["lake", "build", f"+{name}:leanArts"], cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, check=True)
    subprocess.run(["lake", "build"], cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, check=True)
print("Complete standalone library build passed.", flush=True)
