#!/usr/bin/env python3
"""CL571-9429: score glossed (unit, number) pairs from DECODE R9429 (Clair 417 f.236) against key 9431 and the published Clair 421
table, with a permutation control (PREREG-CL571-9429.md). Usage: score_9429.py [--check]  (--check: exit 1 if score_9429.txt is stale)."""
import csv, random, re, sys, unicodedata
from pathlib import Path
H = Path(__file__).resolve().parent
KEYS = {'9431': H.parent / '9431_key.tsv', 'clair421': H.parent / 'clair421_published.tsv'}

def norm(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r"[^a-z]", '', s)

def load_key(p):
    rows = []
    for r in csv.DictReader((l for l in open(p, encoding='utf-8') if not l.startswith('#')), delimiter='\t'):
        m = re.match(r'(\d+)', r['code'] or '')
        if m and r.get('plaintext'):
            rows.append((int(m.group(1)), norm(r['plaintext'])))
    return rows

def load_pairs():
    ps = {}
    for r in csv.DictReader((l for l in open(H / 'pairs.tsv', encoding='utf-8') if not l.startswith('#')), delimiter='\t'):
        units = tuple(norm(u) for u in r['unit'].split('|'))
        ps[(units, int(r['number']))] = r['set']
    return list(ps)

def hits(pairs, rows):
    by = {}
    for n, pt in rows:
        by.setdefault(pt, set()).add(n)
    return sum(1 for units, n in pairs if any(n in by.get(u, ()) for u in units))

def main():
    pairs = load_pairs()
    out = [f'CL571-9429 score: {len(pairs)} unique (unit, number) pairs from pairs.tsv']
    for name, p in KEYS.items():
        rows = load_key(p)
        pts = {pt for _, pt in rows}
        cov = sum(1 for units, _ in pairs if any(u in pts for u in units))
        h = hits(pairs, rows)
        rng = random.Random(9429)
        nums = [n for n, _ in rows]
        null = []
        for _ in range(2000):
            rng.shuffle(nums)
            null.append(hits(pairs, list(zip(nums, [pt for _, pt in rows]))))
        null.sort()
        mean, p95 = sum(null) / len(null), null[int(0.95 * len(null))]
        fit = 'fits' if (h > p95 and h >= 0.6 * cov) else ('does not fit' if h <= p95 else 'undecided')
        out.append(f'{name}: rows {len(rows)}, units covered {cov}/{len(pairs)}, hits {h}, null mean {mean:.2f} p95 {p95} -> {fit}')
    txt = '\n'.join(out) + '\n'
    f = H / 'score_9429.txt'
    if '--check' in sys.argv:
        ok = f.exists() and f.read_text() == txt
        print('OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    f.write_text(txt); print(txt, end='')

if __name__ == '__main__':
    main()
