#!/usr/bin/env python3
"""Apply regrades.tsv (one decision per M-graded code of leaf 188, GAPS3 2 Oct 2026) to key.tsv and conflicts.tsv.

Usage: python3 scripts/apply_regrades.py [--regrades regrades.tsv] [--key key.tsv] [--conflicts conflicts.tsv] [--check]

Per row: key.tsv's grade becomes grade_after, its value becomes value_after, and its note gains one tag
"GAPS3 2 Oct 2026: <decision>" (once; idempotent). conflicts.tsv gains a `decision` column carrying the same
sentence for every code it lists (merge_leaf.py preserves the column). --check applies nothing and exits 1 if
key.tsv or conflicts.tsv differ from what applying regrades.tsv would give (rule 7: the committed key matches
its own evidence file). Disk only.
"""
import argparse, csv, sys
from collections import OrderedDict
TAG = "GAPS3 2 Oct 2026: "

def load(p): return list(csv.DictReader(open(p, newline='', encoding='utf-8'), delimiter='\t'))

def apply(regrades, key_rows, conf_rows):
    key = OrderedDict((r['code'], r) for r in key_rows)
    conf = OrderedDict((r['code'], r) for r in conf_rows)
    for c in conf.values():
        c.setdefault('decision', '')
    missing = [r['code'] for r in regrades if r['code'] not in key]
    if missing:
        sys.exit(f"regrades.tsv names codes absent from key.tsv: {missing}")
    for r in regrades:
        k = key[r['code']]
        if k['grade'] != r['grade_before'] and TAG not in k['note']:
            sys.exit(f"code {r['code']}: key.tsv grade {k['grade']} != grade_before {r['grade_before']}")
        k['grade'] = r['grade_after']
        k['value'] = r['value_after']
        if TAG not in k['note']:
            k['note'] = (k['note'] + '; ' if k['note'] else '') + TAG + r['decision']
        if r['code'] in conf:
            conf[r['code']]['decision'] = TAG + r['decision']
    return list(key.values()), list(conf.values())

def write(path, rows, fields):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
        w.writeheader()
        for r in rows: w.writerow({k: r.get(k, '') for k in fields})

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--regrades', default='regrades.tsv'); ap.add_argument('--key', default='key.tsv')
    ap.add_argument('--conflicts', default='conflicts.tsv'); ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    regrades, key_rows, conf_rows = load(a.regrades), load(a.key), load(a.conflicts)
    KF, CF = ['code', 'value', 'n', 'pages', 'grade', 'note'], ['code', 'variants', 'decision']
    before_key = [{k: r.get(k, '') for k in KF} for r in key_rows]
    before_conf = [{k: r.get(k, '') for k in CF} for r in conf_rows]
    new_key, new_conf = apply(regrades, [dict(r) for r in key_rows], [dict(r) for r in conf_rows])
    new_key = [{k: r.get(k, '') for k in KF} for r in new_key]
    new_conf = [{k: r.get(k, '') for k in CF} for r in new_conf]
    changed = sum(1 for b, n in zip(before_key, new_key) if b != n)
    if a.check:
        if new_key != before_key or new_conf != before_conf:
            print(f"STALE: {changed} key.tsv row(s) and/or conflicts.tsv differ from regrades.tsv"); sys.exit(1)
        print(f"ok: key.tsv and conflicts.tsv match regrades.tsv ({len(regrades)} decisions)"); return
    write(a.key, new_key, KF); write(a.conflicts, new_conf, CF)
    g = {}
    for r in regrades: g[(r['grade_before'], r['grade_after'])] = g.get((r['grade_before'], r['grade_after']), 0) + 1
    print(f"applied {len(regrades)} decisions, {changed} key rows changed; by grade: " + ', '.join(f"{a}->{b} {n}" for (a, b), n in sorted(g.items())))

if __name__ == '__main__':
    main()
