#!/usr/bin/env python3
"""Turn a confirm/correct pass (line pos code marks action conf note) into tools/reconcile_passes.py long format.
Deleted rows and plain ('_') boxes are dropped; a sign with marks is CODE^m1^m2; --base drops the marks.
  python3 pass2_long.py passA2.tsv OUT.tsv [--base]"""
import csv, sys
src, dst = sys.argv[1], sys.argv[2]
base = '--base' in sys.argv
rows = list(csv.DictReader(open(src), delimiter='\t'))
with open(dst, 'w') as f:
    f.write('line\tpos\ttoken\tconf\n')
    n = 0
    for r in rows:
        if r['action'].strip() == 'delete' or r['code'].strip() in ('_', ''):
            continue
        m = [x for x in r['marks'].split('|') if x.strip()] if r['marks'] else []
        tok = r['code'].strip() + ('' if base or not m else '^' + '^'.join(sorted(m)))
        f.write(f"f54r_L{int(r['line']):02d}\t{r['pos']}\t{tok}\t{r['conf']}\n")
        n += 1
print(f'{src}: {len(rows)} rows -> {n} signs')
