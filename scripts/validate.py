#!/usr/bin/env python3
"""Static repository validator for Financial Debugger v1.9.2."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
required_files = [
    "SKILL.md", "README.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md", "QUALITY-GATES.md", "tests/test-cases.md",
    "templates/quick-debug.md", "templates/deep-debug.md", "templates/valuation-debug.md", "templates/portfolio-debug.md",
    "templates/postmortem.md", "templates/full-debug.md", "references/full-audit-contract.md", "references/audit-integrity.md"
]
required_dirs = ["examples", "references", "templates", "tests", "scripts"]
for d in required_dirs:
    if not (ROOT / d).is_dir(): errors.append(f"missing directory: {d}/")
for f in required_files:
    if not (ROOT / f).is_file(): errors.append(f"missing file: {f}")

skill = ROOT / "SKILL.md"
if skill.is_file():
    text = skill.read_text(encoding="utf-8")
    if not re.search(r"^name:\s*financial-debugger\s*$", text, re.M): errors.append("SKILL.md: invalid name")
    m = re.search(r"^version:\s*([^\s]+)\s*$", text, re.M)
    if not m or m.group(1) != "1.9.2": errors.append("SKILL.md: expected version 1.9.2")
    for term in ["FULL FINANCIAL DEBUG","M01","M20","ERROR NOT FOUND","NOT ASSESSABLE","NOT APPLICABLE","COMPLETED","Primary Module","Related Modules","Audit Integrity Check","DECISION-CHANGING","UNREPRODUCIBLE","USER INPUT / UNVERIFIED","VERIFIED SOURCE / DATE","PARTIALLY VERIFIED","Assessment confidence"]:
        if term.lower() not in text.lower(): errors.append(f"SKILL.md: missing hardening term: {term}")

readme = ROOT / "README.md"
if readme.is_file():
    text = readme.read_text(encoding="utf-8")
    if "# Financial Debugger" not in text: errors.append("README.md: missing title")
    for term in ["evidence sufficiency","assumption registry","expectations audit","risk vs uncertainty","decision-changing","next best action","mandatory finding","full financial debug","audit this","20 canonical","not assessable","audit integrity"]:
        if term.lower() not in text.lower(): errors.append(f"README.md: missing concept: {term}")

tests = ROOT / "tests/test-cases.md"
if tests.is_file():
    cases = re.findall(r"^##\s+\d+\s+", tests.read_text(encoding="utf-8"), re.M)
    if len(cases) < 70: errors.append(f"tests/test-cases.md: expected at least 70 numbered cases, found {len(cases)}")

contract = ROOT / "references/full-audit-contract.md"
if contract.is_file():
    c = contract.read_text(encoding="utf-8")
    for term in ["ERROR NOT FOUND","NOT ASSESSABLE","NOT APPLICABLE","COMPLETED","Primary Module","Related Modules","Reconciliation requirements","DECISION-CHANGING"]:
        if term not in c: errors.append(f"full-audit-contract.md: missing {term}")

if errors:
    print("FAIL")
    for e in errors: print("-", e)
    sys.exit(1)
print("PASS — Financial Debugger v1.9.2 repository integrity checks passed.")
print("files", sum(1 for p in ROOT.rglob('*') if p.is_file()))
print("test_cases", len(re.findall(r"^##\s+\d+\s+", tests.read_text(encoding="utf-8"), re.M)))
