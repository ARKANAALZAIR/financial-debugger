#!/usr/bin/env python3
"""Static repository validator for Financial Debugger."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

required_files = [
    "SKILL.md", "README.md", "LICENSE", "CHANGELOG.md",
    "CONTRIBUTING.md", "QUALITY-GATES.md", "tests/test-cases.md",
    "templates/quick-debug.md", "templates/deep-debug.md",
    "templates/valuation-debug.md", "templates/portfolio-debug.md",
    "templates/postmortem.md", "templates/full-debug.md",
    "references/full-audit-contract.md",
]
required_dirs = ["examples", "references", "templates", "tests", "scripts"]

for d in required_dirs:
    if not (ROOT / d).is_dir():
        errors.append(f"missing directory: {d}/")
for f in required_files:
    if not (ROOT / f).is_file():
        errors.append(f"missing file: {f}")

skill = ROOT / "SKILL.md"
if skill.is_file():
    text = skill.read_text(encoding="utf-8")
    if not re.search(r"^name:\s*financial-debugger\s*$", text, re.M):
        errors.append("SKILL.md: missing/invalid name")
    m = re.search(r"^version:\s*([^\s]+)\s*$", text, re.M)
    if not m:
        errors.append("SKILL.md: missing version")
    elif m.group(1) != "1.9.0":
        errors.append(f"SKILL.md: expected version 1.9.0, found {m.group(1)}")
    if not re.search(r"^description:\s*\S+", text, re.M):
        errors.append("SKILL.md: missing description")

    for term in ["ID: FD-", "Severity:", "Type:", "Location:", "Problem:", "Evidence:", "Reasoning:", "Impact:", "Recommended Action:", "FULL FINANCIAL DEBUG", "M01", "M20", "ERROR NOT FOUND", "NOT ASSESSABLE", "Primary Module", "Related Modules", "Audit Integrity Check"]:
        if term.lower() not in text.lower():
            errors.append(f"SKILL.md: missing mandatory finding schema field: {term}")

readme = ROOT / "README.md"
if readme.is_file():
    text = readme.read_text(encoding="utf-8")
    if "# Financial Debugger" not in text:
        errors.append("README.md: missing title")
    for term in ["evidence sufficiency", "assumption registry", "expectations audit", "risk vs uncertainty", "decision-changing", "next best action", "mandatory finding", "Recommended Action", "full financial debug", "audit this", "20 canonical", "error not found"]:
        if term.lower() not in text.lower():
            errors.append(f"README.md: missing required concept: {term}")
    for item in ["CHANGELOG.md", "CONTRIBUTING.md", "LICENSE", "QUALITY-GATES.md", "scripts/validate.py"]:
        if item not in text and not (item == "scripts/validate.py" and "scripts/" in text and "validate.py" in text):
            errors.append(f"README.md: missing repository structure reference: {item}")

tests = ROOT / "tests/test-cases.md"
if tests.is_file():
    cases = re.findall(r"^##\s+\d+\s+", tests.read_text(encoding="utf-8"), re.M)
    if len(cases) < 56:
        errors.append(f"tests/test-cases.md: expected at least 56 numbered cases, found {len(cases)}")

if errors:
    print("FAIL")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("PASS — Financial Debugger v1.9.0 repository integrity checks passed.")
