#!/usr/bin/env python3
"""SIG-4612D crib placement on 4612 v3, attempt 2 (9 Oct 2026, account 1, for LANE SIG-4). Pre-registration: PREREG.md beside this
file (pushed f60d73d1c before this file existed). Same steps 1-3 as ../sig4612c/crib_place.py (imported, not copied), plus step 3a:
a consistent reassignment is admitted only with (i) >= 2 kept placements implying it, or (ii) one placement and a whole-stream per-code
check (>= 3 outside occurrences, coverage gain >= 0.20 with c -> L applied alone).

  python3 crib_place2.py control     # (a) calibrate f, 10 known-answer seeds; writes control.json
  python3 crib_place2.py target      # refuses unless control.json passed; 4612 topical + (b) + (c); writes target.json
  python3 crib_place2.py selftest    # offline synthetic check
"""
import json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(T, 'sig4612c'))
import crib_place as C

MARGIN = 0.20
MIN_OUT = 3


def covered(seg, key, words):
    """Per-position coverage of one segment by the word_share rule (null letters break)."""
    letters = [key.get(c) for c in seg]; hit = [False] * len(seg); i0 = 0
    while i0 < len(seg):
        if letters[i0] is None: i0 += 1; continue
        j0 = i0
        while j0 < len(seg) and letters[j0] is not None: j0 += 1
        s = letters[i0:j0]; n = len(s)
        for i in range(n):
            for j in range(i + 3, n + 1):
                if ''.join(s[i:j]) in words:
                    for k in range(i, j): hit[i0 + k] = True
        i0 = j0
    return hit


def place2(segs, key, cribs, words):
    """Steps 1-3 (as attempt 1) then 3a. Returns kept, admitted {c: L}, report rows for every consistent reassignment."""
    kept, cons, _ = C.place(segs, key, cribs)
    support, wins = {}, {}
    for k, (si, i, w) in enumerate(kept):
        for j, c in enumerate(segs[si][i:i + len(w)]):
            if key.get(c) != w[j]: support.setdefault((c, w[j]), []).append(k)
    adm, rep = {}, []
    for c, L in sorted(cons.items()):
        ks = support[(c, L)]
        if len(ks) >= 2:
            adm[c] = L; rep.append(dict(code=c, letter=L, route='i', placements=len(ks))); continue
        si0, i0, w0 = kept[ks[0]]; win = set(range(i0, i0 + len(w0)))
        k2 = dict(key); k2[c] = L; n = old = new = 0
        for si, s in enumerate(segs):
            if c not in s: continue
            h0, h1 = covered(s, key, words), covered(s, k2, words)
            for p, x in enumerate(s):
                if x == c and not (si == si0 and p in win):
                    n += 1; old += h0[p]; new += h1[p]
        d = (new - old) / n if n else 0.0
        ok = n >= MIN_OUT and d >= MARGIN
        if ok: adm[c] = L
        rep.append(dict(code=c, letter=L, route='ii' if ok else 'rejected', placements=1, outside=n, cov_gain=round(d, 3)))
    return kept, adm, rep


def gain2(segs, key, cribs, words):
    kept, adm, rep = place2(segs, key, cribs, words)
    k2 = dict(key); k2.update(adm); b = C.share(segs, key, words)
    return C.share(segs, k2, words) - b, kept, adm, rep, b


def control():
    key, nulls = C.load_key(); words = C.lexicon(); alpha = sorted(set(key.values()))
    base_t = C.share(C.load_segments(os.path.join(T, 'ciphertext_4612_v3.tsv'), nulls), key, words)
    segs = C.load_segments(os.path.join(T, 'ciphertext_5811.tsv'), nulls, C.N_CUT)
    codes = sorted({c for s in segs for c in s if c in key})
    calib = {}
    for f in C.F_GRID:
        v = [C.share(segs, C.perturb(key, codes, f, random.Random(9000 + s), alpha)[0], words) for s in range(20)]
        calib[f] = sum(v) / len(v)
    f = min(C.F_GRID, key=lambda x: (abs(calib[x] - base_t), x))
    print(f'4612 baseline {base_t:.4f}; calibrated f={f} (mean share {calib[f]:.4f})', flush=True)
    pool = [w for w in C.fold_words(os.path.join(T, 'groen', 'groen_IV_CDLXXXIII.txt'), [162, 174]) if len(w) >= 6]
    lens = [len(w) for w in C.TOPICAL]; rows = []
    for s in range(10):
        pk, pert = C.perturb(key, codes, f, random.Random(s), alpha)
        cribs = C.draw(pool, lens, random.Random(1000 + s))
        g, kept, adm, rep, b = gain2(segs, pk, cribs, words)
        rec = sum(1 for c, l in adm.items() if c in pert and l == key[c]); false = len(adm) - rec
        rows.append(dict(seed=s, kept=len(kept), consistent=len(rep), admitted=len(adm),
                         via_i=sum(r['route'] == 'i' for r in rep), via_ii=sum(r['route'] == 'ii' for r in rep),
                         recovered=rec, false=false, recoverable=len(C.recoverable(segs, key, cribs, pert)),
                         base=round(b, 4), G=round(g, 4),
                         false_codes=[(c, l, key[c], c in pert) for c, l in adm.items() if not (c in pert and l == key[c])]))
        print('  seed', rows[-1], flush=True)
    R = sum(r['recovered'] for r in rows); RV = sum(r['recoverable'] for r in rows)
    recall = R / RV if RV else 0.0; mf = sum(r['false'] for r in rows) / 10; mg = sum(r['G'] for r in rows) / 10
    ok = RV > 0 and recall >= 0.30 and mf <= 2.0 and mg > 0
    json.dump(dict(f=f, calib=calib, base_4612=base_t, rows=rows, pooled_recall=recall, mean_false=mf, mean_G=mg, PASS=ok),
              open(os.path.join(HERE, 'control.json'), 'w'), indent=1)
    print(f'CONTROL (a): f={f} recall {R}/{RV}={recall:.3f} (>=0.30), mean false {mf:.1f} (<=2.0), mean G {mg:+.4f} (>0) -> '
          f'{"PASS" if ok else "FAIL (CONTROL BELOW GATE)"}')


def target():
    c = json.load(open(os.path.join(HERE, 'control.json')))
    if not c['PASS']: print('CONTROL BELOW GATE: control.json did not pass; target not scored'); sys.exit(3)
    key, nulls = C.load_key(); words = C.lexicon()
    segs = C.load_segments(os.path.join(T, 'ciphertext_4612_v3.tsv'), nulls)
    g, kept, adm, rep, b = gain2(segs, key, C.TOPICAL, words)
    print(f'TARGET topical: base {b:.4f} G {g:+.4f} kept {len(kept)} consistent {len(rep)} admitted {len(adm)}', flush=True)
    excl = set(C.fold_words(os.path.join(T, 'decipherment_7208.txt'))) | set(C.TOPICAL)
    pool = [w for p in ('decipherment_7205.txt', 'decipherment_4614.txt') for w in C.fold_words(os.path.join(T, p))
            if len(w) >= 6 and w not in excl]
    lens = [len(w) for w in C.TOPICAL]
    gb = [gain2(segs, key, C.draw(pool, lens, random.Random(46120 + d)), words)[0] for d in range(200)]
    print(f'(b) off-topic: mean {sum(gb)/200:+.4f} p95 {C.p95(gb):+.4f} max {max(gb):+.4f}', flush=True)
    flat = [x for s in segs for x in s]; gc = []
    for k in range(200):
        r = random.Random(46220 + k); f2 = flat[:]; r.shuffle(f2); ss = []; p = 0
        for s in segs: ss.append(f2[p:p + len(s)]); p += len(s)
        gc.append(gain2(ss, key, C.TOPICAL, words)[0])
    print(f'(c) shuffled: mean {sum(gc)/200:+.4f} p95 {C.p95(gc):+.4f} max {max(gc):+.4f}', flush=True)
    ok = g > C.p95(gb) and g > C.p95(gc)
    json.dump(dict(base=b, G=g, kept=[(si, i, w, ''.join(key.get(x, '?') for x in segs[si][i:i + len(w)])) for si, i, w in kept],
                   admitted={str(k): v for k, v in sorted(adm.items())}, report=rep,
                   b=dict(mean=sum(gb) / 200, p95=C.p95(gb), max=max(gb)), c=dict(mean=sum(gc) / 200, p95=C.p95(gc), max=max(gc)),
                   PASS=ok), open(os.path.join(HERE, 'target.json'), 'w'), indent=1)
    print(f'GATE: G {g:+.4f} > (b) p95 {C.p95(gb):+.4f} and > (c) p95 {C.p95(gc):+.4f} -> {"PASS" if ok else "FAIL"}')


def selftest():
    key = {i + 1: ch for i, ch in enumerate('ABCDEFGHIKLMNOPQRSTVXYZ')}; enc = {v: k for k, v in key.items()}
    words = {'MASTRICHT', 'SOT', 'ROT', 'RAT'}
    bad = dict(key); bad[enc['S']] = 'X'; bad[enc['R']] = 'Y'
    # one placement; S occurs 3 more times outside in "SOT", R only in the crib -> S admitted via (ii), R rejected
    segs = [[enc[ch] for ch in 'ZZQQMASTRICHTQQ'], [enc[ch] for ch in 'QSOTQ'], [enc[ch] for ch in 'QSOTQ'], [enc[ch] for ch in 'QSOTQ']]
    kept, adm, rep = place2(segs, bad, ['MASTRICHT'], words)
    assert adm == {enc['S']: 'S'}, (adm, rep)
    # two placements imply R -> admitted via (i)
    segs2 = segs + [[enc[ch] for ch in 'ZMASTRICHTZ']]
    _, adm2, rep2 = place2(segs2, bad, ['MASTRICHT', 'MASTRICHT'], words)
    assert adm2.get(enc['R']) == 'R' and any(r['route'] == 'i' for r in rep2), rep2
    print('selftest OK')


if __name__ == '__main__':
    {'control': control, 'target': target, 'selftest': selftest}[sys.argv[1]]()
