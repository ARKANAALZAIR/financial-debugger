from pathlib import Path
import re,sys

def main():
    p=Path(sys.argv[1]) if len(sys.argv)>1 else None
    if not p or not p.is_file():
        print('usage: python scripts/validate_report.py REPORT.md')
        return 2
    t=p.read_text(encoding='utf-8')
    errs=[]
    ids=re.findall(r'^\| (M\d{2}) \|',t,re.M)
    if ids[:20] != [f'M{i:02d}' for i in range(1,21)]:
        errs.append('M01-M20 module matrix order/count failed')
    if t.count('## AUDIT INTEGRITY CHECK')!=1:
        errs.append('integrity section count != 1')
    for fld in ['Primary Module:','Related Modules:','Decision Link:','Impact:','Recommended Action:','Verification Needed:']:
        if fld not in t:
            errs.append('missing canonical finding field '+fld)
    if 'Severity Count Reconciled:' not in t or 'Materiality Count Reconciled:' not in t:
        errs.append('separate severity/materiality reconciliation missing')
    if errs:
        print('FAIL'); print('\n'.join(errs)); return 1
    print('PASS'); return 0

if __name__=='__main__': raise SystemExit(main())
