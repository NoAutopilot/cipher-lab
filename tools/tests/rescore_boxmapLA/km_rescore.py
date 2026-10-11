#!/usr/bin/env python3
"""BOXMAP-RESCORE (others), 11 Oct 2026, account 3: MQS-SHEETS G3 "KM" (tools/tests/km_birago_map.py) re-run with only the box map
changed. km_birago_map.py goes through tools/decipher_sheet.py, which needs Python >= 3.12 (nested f-string quotes), and this
container's 3.12 has no numpy/opencv; this file is the same statistic without the decipher_sheet import: the held-out no.87
tokens (f178v L13-L23, f179r L01-L03; harvest/ciphertext_<fol>.tsv, one record per row whose sign is a T-code or X_ code, as
decipher_sheet's graded() yields kind 'sign'), each joined to its box(es) exactly as decipher_sheet.Boxes.token_box does
(map rows by (line, pos), op from the map; one 1:1 row -> counted, anything else -> apart), the same held-out classify call,
the same null (box ids permuted within each line, random.Random(20261009), 20 draws) and the same gate (>= 0.55 and > p95).
With the old map it reproduces km_birago_map.py's committed line (381 / 231 / 0.606 / neighbour 75 / null 0.066, 0.085, 0.094 /
apart 2:1 13, 1:2 4, no box 4), checked 11 Oct 2026.

  python3 tools/tests/rescore_boxmapLA/km_rescore.py [--map MAP] [--json OUT]
"""
import collections, csv, json, os, random, subprocess, sys, tempfile
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
BIR = os.path.join(ROOT, 'ciphers', 'nevers-birago-fr3251-1572'); A = os.path.join(BIR, 'atlas')
GATE, DRAWS = 0.55, 20
rd = lambda p: list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))


def main():
    mp = sys.argv[sys.argv.index('--map') + 1] if '--map' in sys.argv else os.path.join(A, 'no87_box_token.tsv')
    tsv = os.path.join(tempfile.mkdtemp(), 'ho.tsv')
    ho = []
    for i in range(13, 24):
        ho += ['--holdout', f'f178v_{i}_']
    for i in ('01', '02', '03'):
        ho += ['--holdout', f'f179r_{i}_']
    subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'glyph_atlas.py'), 'classify', '--out', A, '--labels',
                    os.path.join(A, 'labels.json'), '--page', 'all', '--tsv', tsv, '--topk', '3'] + ho, check=True,
                   stdout=subprocess.DEVNULL)
    code = {r['box']: r['code'] for r in rd(tsv)}
    by_tok = collections.defaultdict(list)
    for r in rd(mp):
        by_tok[(r['line'], int(r['pos']))].append((r['sid'], r.get('op', '1:1')))
    lines, other = collections.defaultdict(list), collections.Counter()
    for fol, rng_ in (('f178v', range(13, 24)), ('f179r', range(1, 4))):
        keep = {f'{fol}_L{i:02d}' for i in rng_}
        for t in rd(os.path.join(BIR, 'harvest', f'ciphertext_{fol}.tsv')):
            if t['line'] not in keep or not t['sign']:
                continue
            b = by_tok.get((t['line'], int(t['pos'])))
            if not b:
                other['no box'] += 1; continue
            if len(b) != 1 or b[0][1] != '1:1':
                other[b[0][1] if len(b) == 1 else '2:1'] += 1; continue
            lines[t['line']].append((int(t['pos']), t['sign'], b[0][0]))
    toks = [(lab, p, s, sid) for lab, v in lines.items() for p, s, sid in sorted(v)]
    n = len(toks)
    agree = sum(code.get(sid) == s for lab, p, s, sid in toks)
    neigh = 0
    for lab, v in lines.items():
        v = sorted(v)
        for k, (p, s, sid) in enumerate(v):
            c = code.get(sid)
            if c != s and any(c == v[j][1] for j in (k - 1, k + 1) if 0 <= j < len(v)):
                neigh += 1
    rng = random.Random(20261009)
    nulls = []
    for _ in range(DRAWS):
        hit = 0
        for lab, v in lines.items():
            v = sorted(v); sids = [x[2] for x in v]; rng.shuffle(sids)
            hit += sum(code.get(sid) == s for (p, s, _), sid in zip(v, sids))
        nulls.append(hit / n)
    p95 = float(np.percentile(nulls, 95)); rate = agree / n; ok = rate >= GATE and rate > p95
    print(f'KM: held-out 1:1 tokens {n}; classify top-1 = own sign label {agree} ({rate:.3f}); neighbour label (not own) {neigh}; '
          f'null (box ids permuted within line, {DRAWS} draws) mean {np.mean(nulls):.3f} p95 {p95:.3f} max {max(nulls):.3f}; '
          f'apart (not in gate): {dict(other)}; gate >= {GATE} and > p95: ' + ('PASS' if ok else 'FAIL'))
    if '--json' in sys.argv:
        json.dump(dict(map=os.path.relpath(os.path.abspath(mp), ROOT), n=n, agree=agree, rate=round(rate, 3), neighbour=neigh,
                       null_mean=round(float(np.mean(nulls)), 3), null_p95=round(p95, 3), null_max=round(max(nulls), 3),
                       apart=dict(other), gate='PASS' if ok else 'FAIL'),
                  open(sys.argv[sys.argv.index('--json') + 1], 'w'), indent=1)
    return 0 if ok else 3


if __name__ == '__main__':
    sys.exit(main())
