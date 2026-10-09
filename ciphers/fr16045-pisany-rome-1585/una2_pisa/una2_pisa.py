#!/usr/bin/env python3
"""UNA2-PISA (9 Oct 2026; una2_pisa/PREREG-UNA2-PISA.md): T57 -> T32 relabel re-score of the 11 tokens una_pisa/result.tsv marks
SETTLED-T32 on f.301v/f.302v. pis1key.py (run_files, identical's alignment), kp86d.control imported unchanged; key86.tsv unchanged.
    python3 una2_pisa/una2_pisa.py          -> una2_pisa/tx87c/*, una2_pisa/result.json, una2_pisa/per_token.tsv
Paths relative to the target folder."""
import itertools, json, os, random, sys
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, os.path.join(T, 'pis1key'))
import pis1key as P
from pis1key import nw_score, dec, load_tokens, norm, control

PAGES = [('f301v', 'tx87', 'kp87a/colbert_p338_339.txt', 0.192),
         ('f302v', 'tx87b', 'kp87b/colbert_p341_342.txt', 0.335)]
pos = {}
for ln in open(os.path.join(T, 'una_pisa/tokens_pos.tsv')).read().splitlines()[1:]:
    f = ln.split('\t'); pos[(f[0], f[1], int(f[3]))] = (int(f[2]), f[4])
verdict = {}
for ln in open(os.path.join(T, 'una_pisa/result.tsv')).read().splitlines()[1:]:
    f = ln.split('\t')
    if len(f) > 8 and f[3] == 'test':
        pg, l, p = f[2].split('_'); verdict[(pg, l, int(p[1:]))] = f[8]
# verdict ids carry `pos`; convert to ord
SETTLED = {}
for (pg, l, o), (p, lab) in pos.items():
    v = verdict.get((pg, l, p))
    if v:
        SETTLED[(pg, l, o)] = v


def read(path):
    return [(ln.rstrip('\n').split('\t', 1) if ln.strip() else None) for ln in open(os.path.join(T, path))]


def relabel(lines, pg, picks):
    """picks: set of (line, ord) with ord 1-based over non-'/' tokens. Asserts T57 and that pos matches."""
    out = []
    for x in lines:
        if x is None:
            out.append(None); continue
        lab, body = x; t = body.split(); j = 0
        for n, w in enumerate(t):
            if w == '/':
                continue
            j += 1
            if (lab, j) in picks:
                assert w.strip('?') == 'T57', (pg, lab, j, w)
                if (pg, lab, j) in pos:
                    assert pos[(pg, lab, j)][0] == n + 1, (pg, lab, j, n + 1)
                t[n] = w.replace('T57', 'T32')
        out.append([lab, ' '.join(t)])
    return out


def write(lines, dst):
    p = os.path.join(T, dst); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w').write(''.join('\n' if x is None else f'{x[0]}\t{x[1]}\n' for x in lines))
    return dst


def per_token(ctf, clf, key, targets):
    """pis1key.identical's band_dp alignment, reported per (line, ord) for the target tokens."""
    from stream_align import band_dp, A
    toks, where = [], []
    for x in read(ctf):
        if x:
            j = 0
            for t in x[1].split():
                if t != '/':
                    j += 1; toks.append(t.rstrip('?')); where.append((x[0], j))
    clear = np.array([ord(c) - 97 for c in norm(open(os.path.join(T, clf)).read())])
    letters, owner = [], []
    for i, t in enumerate(toks):
        for c in key.get(t, ''):
            letters.append(ord(c) - 97); owner.append(i)
    d = np.array(letters); N, M = len(d), len(clear)
    E = np.full((A + 1, A), -1.0); E[np.arange(A), np.arange(A)] = 2.0
    ref = np.linspace(0, min(M, N), N + 1) if M >= N else np.arange(N + 1) * (M / N)
    path, _, _ = band_dp(d, clear, E, ref, max(200, abs(M - N) + 200), 1.0, 1.0, free_start=True)
    ok = {i for i, j in path if d[i] == clear[j]}; on = dict(path)
    res = {}
    for i, w in enumerate(where):
        if w in targets:
            idx = [n for n, o in enumerate(owner) if o == i]
            copy = ''.join(chr(clear[on[n]] + 97) if n in on and on[n] is not None and on[n] >= 0 else '-' for n in idx)
            res[w] = {"label": toks[i], "decoded": key.get(toks[i], ''), "copy": copy,
                      "identical": bool(idx) and all(n in ok for n in idx)}
    return res


def main():
    key = P.load_key(); out = {}; rows = []
    for pg, d, cl, err in PAGES:
        clear, ptext = P.clear_of(cl)
        rec = f'{d}/ciphertext_{pg}_preT32.tsv'; lines = read(rec)  # pre-edit bytes (committed file now carries the relabel)
        picks = {(l, o) for (p, l, o), v in SETTLED.items() if p == pg and v == 'SETTLED-T32'}
        newf = write(relabel(lines, pg, picks), f'una2_pisa/tx87c/ciphertext_{pg}.tsv')
        allT57 = {(x[0], j + 1) for x in lines if x for j, w in enumerate([w for w in x[1].split() if w != '/'])
                  if w.strip('?') == 'T57'}
        allf = write(relabel(lines, pg, allT57), f'una2_pisa/tx87c/_all_{pg}.tsv')
        r = {"err": err, "picks": sorted(f'{l} o{o}' for l, o in picks), "n_T57": len(allT57),
             "old": P.run_files(key, [rec, f'{d}/passA.tsv', f'{d}/passB.tsv'], clear), "new": P.run_files(key, [newf], clear)}
        r["all_T57_relabel"] = P.run_files(key, [allf], clear)[allf]
        os.remove(os.path.join(T, allf))
        r["positive_control"] = control(key, ptext, clear, err, r["new"][newf]["decoded_letters"])
        print(pg, 'control', r["positive_control"]["passed"], '/5', flush=True)
        o, n = r["old"][rec], r["new"][newf]
        r["G1"] = bool(n["score"] > o["score"] and n["above_both"]); r["G2"] = bool(r["positive_control"]["passed"] >= 4)
        # descriptive null
        cand = sorted(allT57); k = len(picks)
        combos = list(itertools.combinations(cand, k))
        draws_sets = combos if len(combos) <= 200 else random.Random(20261009).sample(combos, 200)
        draws = []
        for s in draws_sets:
            tmp = write(relabel(lines, pg, set(s)), f'una2_pisa/tx87c/_tmp_{pg}.tsv')
            tk, _ = load_tokens(tmp); draws.append(float(nw_score(dec(tk, key), clear)))
        os.remove(os.path.join(T, f'una2_pisa/tx87c/_tmp_{pg}.tsv')); draws.sort()
        r["random_relabel_null"] = {"n": len(draws), "mean": round(sum(draws) / len(draws), 4), "max": round(draws[-1], 4),
                                    "p95": round(draws[int(0.95 * (len(draws) - 1))], 4),
                                    "share_ge_ours": round(sum(x >= n["score"] - 1e-9 for x in draws) / len(draws), 3)}
        tgt = {(l, o2) for (p, l, o2) in SETTLED if p == pg}
        pt_old = per_token(rec, cl, key, tgt); pt_new = per_token(newf, cl, key, tgt)
        for w in sorted(tgt, key=lambda z: (z[0], z[1])):
            rows.append([pg, w[0], str(w[1]), SETTLED[(pg,) + w], pt_old[w]["label"], pt_old[w]["copy"],
                         str(pt_old[w]["identical"]), pt_new[w]["label"], pt_new[w]["copy"], str(pt_new[w]["identical"])])
        out[pg] = r
    rel = [x for x in rows if x[3] == 'SETTLED-T32']
    g3_new = sum(x[9] == 'True' for x in rel); g3_old = sum(x[6] == 'True' for x in rel)
    out["G3"] = {"relabelled": len(rel), "identical_new_n": g3_new, "identical_old_la": g3_old,
                 "pass": bool(g3_new >= 6 and g3_new > g3_old)}
    out["PASS"] = bool(all(out[p]["G1"] and out[p]["G2"] for p, *_ in PAGES) and out["G3"]["pass"])
    json.dump(out, open(os.path.join(H, 'result.json'), 'w'), indent=1)
    open(os.path.join(H, 'per_token.tsv'), 'w').write(
        'page\tline\tord\tuna_pisa\told_label\told_copy\told_identical\tnew_label\tnew_copy\tnew_identical\n'
        + ''.join('\t'.join(x) + '\n' for x in rows))
    print(json.dumps({p: {"G1": out[p]["G1"], "G2": out[p]["G2"]} for p, *_ in PAGES}), out["G3"], 'PASS', out["PASS"])


if __name__ == '__main__':
    main()
