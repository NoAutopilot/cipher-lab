"""Exit non-zero if a cited edition page file is missing or lacks the quoted OCR string (rule 7 style staleness check).
python3 check_evidence.py   (run from ciphers/thurloe-printed/dutch1653)"""
import csv, os, re, html, sys
bad = 0
for r in csv.DictReader(open('edition_evidence.tsv'), delimiter='\t'):
    p = r['file']
    if not os.path.exists(p):
        print('MISSING', p); bad += 1; continue
    t = html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', open(p, errors='replace').read())))
    if r['must_contain'] not in t:
        print('STALE', p, repr(r['must_contain'])); bad += 1
print('ok' if not bad else f'{bad} problem(s)')
sys.exit(1 if bad else 0)
