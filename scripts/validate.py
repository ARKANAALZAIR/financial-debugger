from pathlib import Path
import re,json,sys
ROOT=Path(__file__).resolve().parents[1]
EXPECTED='2.1.2'
errors=[]
for x in ['SKILL.md','README.md','LICENSE','CHANGELOG.md','CONTRIBUTING.md','QUALITY-GATES.md','VERSION','manifest.json','RELEASE-MANIFEST.json','references/audit-integrity.md','references/full-audit-contract.md','templates/full-debug.md','scripts/validate.py']:
    if not (ROOT/x).is_file(): errors.append('missing '+x)
if (ROOT/'VERSION').read_text().strip()!=EXPECTED: errors.append('VERSION mismatch')
m=json.loads((ROOT/'manifest.json').read_text());
if m.get('version')!=EXPECTED: errors.append('manifest version mismatch')
rm=json.loads((ROOT/'RELEASE-MANIFEST.json').read_text());
if rm.get('version')!=EXPECTED: errors.append('release manifest version mismatch')
sk=(ROOT/'SKILL.md').read_text(encoding='utf-8')
front=re.search(r'^version:\s*([0-9.]+)$', sk, re.M)
if not front or front.group(1)!=EXPECTED: errors.append('SKILL version mismatch')
for q in ['Non-negotiable rendering contract','Primary Module:','Related Modules:','Decision Link:','Materiality: DECISION-CHANGING | HIGH | MEDIUM | LOW','Use only `HIGH`, `MODERATE`, or `LOW`','Audit Integrity Check']:
    if q not in sk: errors.append('SKILL missing '+q)
seq=['ID: FD-NNN','Severity: CRITICAL | HIGH | MEDIUM | LOW','Materiality: DECISION-CHANGING | HIGH | MEDIUM | LOW','Type: <machine-readable category>','Primary Module: M##','Related Modules: [optional]','Decision-Changing: YES | NO | UNKNOWN','Decision Link: <specific decision variable/condition or N/A>','Location: <where in the reasoning chain>','Problem: <specific defect, gap, or uncertainty>','Evidence: <what supports the finding; distinguish user input, verified evidence, and missing evidence>','Reasoning: <why the evidence supports the diagnosis without overclaiming>','Impact: <what thesis/decision/portfolio outcome could change>','Recommended Action: <smallest high-information next step>','Verification Needed: <text or NONE>']
fb=sk[sk.find('### Mandatory Finding Schema'):]; pos=-1
for q in seq:
 z=fb.find(q)
 if z<0: errors.append('finding field missing '+q)
 elif z<pos: errors.append('finding field out of order '+q)
 pos=z
ft=(ROOT/'templates/full-debug.md').read_text(encoding='utf-8')
# exact top-level integrity and module order
if ft.count('## AUDIT INTEGRITY CHECK')!=1: errors.append('integrity heading count != 1')
mods=re.findall(r'^\| (M\d{2}) \|',ft,re.M)
if mods[:20]!=[f'M{i:02d}' for i in range(1,21)]: errors.append('template module order mismatch')
if 'Class | Status | Coverage' not in ft: errors.append('template class/status headers missing')
if 'Overall: PASS | FAIL' not in ft: errors.append('template overall integrity missing')
if 'Severity Count Reconciled' in ft and 'Materiality Count Reconciled' in ft: pass
else: errors.append('separate severity/materiality reconciliation missing')
if f'### v{EXPECTED}' not in (ROOT/'README.md').read_text(encoding='utf-8'): errors.append('README current version missing')
if not (ROOT/'CHANGELOG.md').read_text().startswith(f'# Changelog\n\n## {EXPECTED} '): errors.append('CHANGELOG current version missing')
for bad in ROOT.rglob('*'):
 if bad.is_file() and (bad.suffix in {'.pyc', '.pyo'} or '__pycache__' in bad.parts): errors.append(f'build artifact present: {bad.relative_to(ROOT)}')
if errors:
 print('FAIL'); print('\n'.join(errors)); raise SystemExit(1)
print('PASS'); print('version',EXPECTED); print('render_contract PASS'); print('finding_contract PASS'); print('status_contract PASS'); print('integrity_contract PASS')
