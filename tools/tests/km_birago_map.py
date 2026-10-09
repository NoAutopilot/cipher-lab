#!/usr/bin/env python3
"""KM, the box-to-token map test (PREREG-MQS-SHEETS G3; MQS-SHEETS unit 4, 9 Oct 2026). Run through
`python3 tools/tests/test_decipher_sheet.py --km` or directly. Compares glyph_atlas classify's top-1 code for the box the map
assigns each held-out 1:1 token (found through decipher_sheet.Boxes.token_box, this tool's own cut path) with the token's own
sign label; the held-out lines (f.178v L13-L23, f.179r L01-L03) never vote. Null: box ids permuted within each line (20 draws);
the image moves with the permutation and the label does not. Gate: agreement >= 0.55 and above the null's p95. The 26 2:1 and
8 1:2 rows are counted apart and never in the gate. It prints codes and counts only (no letter values)."""
import collections, os, random, subprocess, sys, tempfile, types
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
os.chdir(ROOT)
import numpy as np
import decipher_sheet as ds, decode_key

BIR = os.path.join(ROOT, 'ciphers', 'nevers-birago-fr3251-1572')
A = os.path.join(BIR, 'atlas')
GATE = 0.55
DRAWS = 20


def heldout(label):
    f, l = label.split('_L') if '_L' in label else (None, None)
    return bool(f) and ((f == 'f178v' and int(l) >= 13) or (f == 'f179r' and int(l) <= 3))


def main():
    tsv = os.path.join(tempfile.mkdtemp(), 'ho.tsv')
    ho = []
    for i in range(13, 24):
        ho += ['--holdout', f'f178v_{i}_']
    for i in ('01', '02', '03'):
        ho += ['--holdout', f'f179r_{i}_']
    subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'glyph_atlas.py'), 'classify', '--out', A, '--labels', os.path.join(A, 'labels.json'),
                    '--page', 'all', '--tsv', tsv, '--topk', '3'] + ho, check=True, stdout=subprocess.DEVNULL)
    code = {r['box']: r['code'] for r in ds.load_tsv(tsv)}
    bx = ds.Boxes(A, os.path.join(A, 'no87_box_token.tsv'))
    lines = collections.defaultdict(list)       # line label -> [(pos, sign, sid)] 1:1 held-out tokens, in position order
    other = collections.Counter()
    for fol in ('f178v', 'f179r'):
        ns = types.SimpleNamespace(config=None, ciphertext=None, key=None, exceptions=None, style=None, reading=None, tokens=None)
        job = ds.select_job(decode_key.load_config(BIR, ns), fol)
        recs, key, ct = ds.graded(BIR, job)
        for r in recs:
            if r['kind'] != 'sign':
                continue
            lab = f"{r['folio']}_{r['line']}"
            if not heldout(lab):
                continue
            b = bx.token_box(r)
            if not b:
                other['no box'] += 1; continue
            if len(b) != 1 or b[0][1] != '1:1':
                other[b[0][1] if len(b) == 1 else '2:1'] += 1; continue
            lines[lab].append((r['pos'], r['sign'], b[0][0]))
    toks = [(lab, p, s, sid) for lab, v in lines.items() for p, s, sid in sorted(v)]
    n = len(toks)
    agree = sum(code.get(sid) == s for lab, p, s, sid in toks)
    own = agree; neigh = 0
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
    p95 = float(np.percentile(nulls, 95))
    rate = agree / n
    ok = rate >= GATE and rate > p95
    print(f'KM: held-out 1:1 tokens {n}; classify top-1 = own sign label {agree} ({rate:.3f}); neighbour label (not own) {neigh}; '
          f'null (box ids permuted within line, {DRAWS} draws) mean {np.mean(nulls):.3f} p95 {p95:.3f} max {max(nulls):.3f}; '
          f'apart (not in gate): {dict(other)}; gate >= {GATE} and > p95: ' + ('PASS' if ok else 'FAIL'))
    return 0 if ok else 3


if __name__ == '__main__':
    sys.exit(main())
