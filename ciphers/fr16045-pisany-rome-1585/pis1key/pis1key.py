#!/usr/bin/env python3
"""PIS1-KEY wrapper (pis1key/PREREG_pis1key.md). Reuses kp86/kp86.py (test, norm, dec, p99, load_key) and kp86d/kp86d.py
(load_tokens, control) unchanged by import.
    python3 pis1key/pis1key.py relabel   -> pis1key/tx_relabel/*, pis1key/relabel_result.json
    python3 pis1key/pis1key.py remap     -> pis1key/remap_result.json, pis1key/key86_proposals.tsv
Paths relative to the target folder."""
import json, os, random, re, sys
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, os.path.join(T, 'kp86')); sys.path.insert(0, os.path.join(T, 'kp86d'))
sys.path.insert(0, os.path.join(T, '../../tools'))
from kp86 import norm, load_key, dec, p99, test
from kp86d import load_tokens, control
from stream_align import nw_score


def clear_of(path, drop=''):
    raw = open(os.path.join(T, path)).read()
    return np.array([ord(c) - 97 for c in norm(raw)], dtype=np.int64), norm(raw.replace(drop, '') if drop else raw)


def run_files(key, files, clear):
    rnd = random.Random(20261004); res = {}
    for name in files:
        toks, dr = load_tokens(name)
        s, ks, os_ = test(toks, key, clear, 1000, 1000, rnd)
        res[name] = {"tokens": len(toks), "dropped": dr, "decoded_letters": int(len(dec(toks, key))), "score": round(s, 4),
                     "keyshuffle_p99": round(p99(ks), 4), "order_p99": round(p99(os_), 4),
                     "above_both": bool(s > p99(ks) and s > p99(os_))}
        print(name, res[name], flush=True)
    return res


def relabel_file(src, dst, rule):
    out = []
    for ln in open(os.path.join(T, src)):
        if not ln.strip():
            out.append(ln); continue
        lab, body = ln.rstrip('\n').split('\t', 1)
        out.append(lab + '\t' + rule(body) + '\n')
    p = os.path.join(T, dst); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w').write(''.join(out))
    return dst


def sub_all(new):
    return lambda body: ' '.join(re.sub(r'^T31(\??)$', new + r'\1', t) for t in body.split())


def merge_cut(body):
    t = body.split(); o = []; i = 0
    while i < len(t):
        if t[i].rstrip('?') == 'T31' and i + 1 < len(t) and t[i + 1].rstrip('?') == 'T30':
            o.append('T36'); i += 2
        else:
            o.append(re.sub(r'^T31(\??)$', r'T36\1', t[i])); i += 1
    return ' '.join(o)


def relabel():
    key = load_key(); out = {}
    pages = [('f244r', 'tx86', ['ciphertext_f244r.tsv', 'passA.tsv', 'passB.tsv'], 'kp86/colbert_p49_50.txt', '', 0.284,
              sub_all('T45')),
             ('f275r', 'tx86e', ['ciphertext_f275r.tsv', 'passA.tsv', 'passB.tsv'], 'kp86d/colbert_p121_123.txt',
              'Mais croyant que Monsieur de Luxembourg', 0.215, sub_all('T36'))]
    for pg, d, fs, cl, drop, err, rule in pages:
        clear, ptext = clear_of(cl, drop)
        old = [f'{d}/{f}' for f in fs]
        new = [relabel_file(f'{d}/{f}', f'pis1key/tx_relabel/{d}_{f}', rule) for f in fs]
        r = {"err": err, "old": run_files(key, old, clear), "new": run_files(key, new, clear)}
        if pg == 'f275r':
            v = relabel_file(old[0], 'pis1key/tx_relabel/tx86e_ciphertext_f275r_mergecut.tsv', merge_cut)
            r["descriptive_mergecut"] = run_files(key, [v], clear)
        if pg == 'f244r':   # kp86.py's control: copy text enciphered, not truncated
            r["positive_control"] = ctrl86(key, ptext, clear, err)
        else:
            r["positive_control"] = control(key, ptext, clear, err, r["new"][new[0]]["decoded_letters"])
        print(pg, 'control', r["positive_control"]["passed"], '/5', flush=True)
        r["supported"] = bool(r["new"][new[0]]["score"] > r["old"][old[0]]["score"] and r["new"][new[0]]["above_both"])
        r["would_be_identical"] = identical(new[0], cl, key, {'T31': 'T45' if pg == 'f244r' else 'T36'})
        out[pg] = r
    json.dump(out, open(os.path.join(H, 'relabel_result.json'), 'w'), indent=1)


def ctrl86(key, ctext, clear, err):   # kp86/kp86.py main()'s positive-control block, verbatim logic
    cells = {}
    for lab, v in key.items():
        if len(v) == 1:
            cells.setdefault(v, []).append(lab)
    labs = list(key); seeds = []
    for sd in range(5):
        r2 = random.Random(500 + sd)
        ct = [r2.choice(cells[c]) for c in ctext if c in cells]
        ct = [r2.choice([x for x in labs if x != t]) if r2.random() < err else t for t in ct]
        s, ks, os_ = test(ct, key, clear, 200, 200, r2)
        seeds.append({"seed": sd, "N": len(ct), "score": round(s, 4), "keyshuffle_p99": round(p99(ks), 4),
                      "order_p99": round(p99(os_), 4), "pass": bool(s > p99(ks) and s > p99(os_))})
    n = sum(x["pass"] for x in seeds)
    return {"seeds": seeds, "passed": n, "pass": n >= 4}


def identical(ctf, clf, key, newlab):
    """Descriptive: of the relabelled tokens, how many decode to a letter that the band_dp alignment (as kp86b/cgrades.py)
    places on the identical copy letter."""
    from stream_align import band_dp, A
    toks, orig = [], []
    for ln in open(os.path.join(T, ctf)):
        if ln.strip():
            for t in ln.rstrip('\n').split('\t', 1)[1].split():
                if t != '/':
                    toks.append(t.rstrip('?'))
    clear = np.array([ord(c) - 97 for c in norm(open(os.path.join(T, clf)).read())])
    letters, owner = [], []
    for i, t in enumerate(toks):
        for c in key.get(t, ''):
            letters.append(ord(c) - 97); owner.append(i)
    d = np.array(letters); N, M = len(d), len(clear)
    E = np.full((A + 1, A), -1.0); E[np.arange(A), np.arange(A)] = 2.0
    ref = np.linspace(0, min(M, N), N + 1) if M >= N else np.arange(N + 1) * (M / N)
    path, _, _ = band_dp(d, clear, E, ref, max(200, abs(M - N) + 200), 1.0, 1.0, free_start=True)
    ok = {i for i, j in path if d[i] == clear[j]}
    target = set(newlab.values()); hit = tot = 0
    # relabelled tokens are those whose label is now the new label but was T31 in the source; count all new-label tokens
    for i, t in enumerate(toks):
        if t in target:
            idx = [n for n, o in enumerate(owner) if o == i]
            tot += 1; hit += bool(idx) and all(n in ok for n in idx)
    return {"tokens_with_new_label": tot, "identical": hit, "note": "counts all tokens now carrying the new label, incl. ones that already had it"}


FIT = [('tx86/ciphertext_f244r.tsv', 'kp86/colbert_p49_50.txt'), ('tx86c/ciphertext_f244v_f245r.tsv', 'kp86b/colbert_p51_52.txt')]
HELD = [('f275r', 'tx86e/ciphertext_f275r.tsv', 'kp86d/colbert_p121_123.txt', 'Mais croyant que Monsieur de Luxembourg', 0.215),
        ('f301v', 'tx87/ciphertext_f301v.tsv', 'kp87a/colbert_p338_339.txt', '', 0.192)]
CELLS = ['T45', 'T47', 'T49', 'T57']
CAND = list('abcdefghilmnopqrstuxy')


def score(key, ctf, clf):
    toks, _ = load_tokens(ctf); return float(nw_score(dec(toks, key), clear_of(clf)[0]))


def remap():
    A = load_key(); key = dict(A)
    F = lambda k: sum(score(k, c, l) for c, l in FIT)
    best = F(key); log = [{"start": "key86", "F": round(best, 4)}]
    for rnd_ in range(5):
        changed = False
        for c in CELLS:
            for v in CAND + [A[c]]:
                if v == key[c]:
                    continue
                k2 = dict(key); k2[c] = v; f = F(k2)
                if f > best + 1e-12:
                    best, key, changed = f, k2, True
            log.append({"round": rnd_, "cell": c, "value": key[c], "F": round(best, 4)})
        if not changed:
            break
    fitted = {c: key[c] for c in CELLS if key[c] != A[c]}
    print('fitted remap', fitted, 'F', best, flush=True)
    deg = {c: 'e' for c in CELLS}
    oldB = {'T45': 'u', 'T47': 'f', 'T57': 'n'}
    out = {"fit_log": log, "fitted_remap": fitted, "fit_F_armA": log[0]["F"], "fit_F_fitted": round(best, 4),
           "degenerate_remap": deg, "held": {}}
    KA = A; KF = dict(A); KF.update(fitted); KD = dict(A); KD.update(deg); KB = dict(A); KB.update(oldB)
    rr = random.Random(7)
    rand = [{c: rr.choice(CAND) for c in CELLS} for _ in range(200)]
    for pg, ctf, clf, drop, err in HELD:
        clear, ptext = clear_of(clf, drop)
        sA = score(KA, ctf, clf)
        r = {"armA": round(sA, 4), "degenerate": round(score(KD, ctf, clf), 4), "old_armB_noT31": round(score(KB, ctf, clf), 4)}
        r["single_cell"] = {c: round(score({**A, c: v}, ctf, clf), 4) for c, v in fitted.items()}
        g = []
        for rm in rand:
            g.append(score({**A, **rm}, ctf, clf) - sA)
        r["random_remap_gain"] = {"mean": round(float(np.mean(g)), 4), "p95": round(float(np.percentile(g, 95)), 4),
                                  "max": round(float(np.max(g)), 4)}
        if fitted:
            r["fitted"] = run_files(KF, [ctf], clear)[ctf]
            r["control"] = control(KF, ptext, clear, err, r["fitted"]["decoded_letters"])
            f = r["fitted"]["score"]
            r["G1"] = bool(f > round(sA, 4)); r["G2"] = r["fitted"]["above_both"]
            r["G3"] = bool(f > r["degenerate"] and fitted != deg and not (r["degenerate"] > round(sA, 4)))
            r["G4"] = r["control"]["pass"]
        print(pg, {k: v for k, v in r.items() if k != 'control'}, flush=True)
        out["held"][pg] = r
    if fitted:
        hs = out["held"].values()
        out["gate_joint"] = all(h["G1"] and h["G2"] and h["G3"] and h["G4"] for h in hs)
        out["cell_pass"] = {c: bool(out["gate_joint"] and all(h["single_cell"][c] > h["armA"] for h in hs)) for c in fitted}
    else:
        out["gate_joint"] = False; out["cell_pass"] = {}
    json.dump(out, open(os.path.join(H, 'remap_result.json'), 'w'), indent=1)
    with open(os.path.join(H, 'key86_proposals.tsv'), 'w') as f:
        f.write('cell\tkey86\tfitted\tfit_F_A\tfit_F_fitted\theld\tarmA\tsingle_cell\tjoint\tdegenerate\tgate_joint\tcell_pass\n')
        for c in CELLS:
            for pg, h in out["held"].items():
                f.write(f'{c}\t{A[c]}\t{fitted.get(c, A[c])}\t{out["fit_F_armA"]}\t{out["fit_F_fitted"]}\t{pg}\t{h["armA"]}\t'
                        f'{h["single_cell"].get(c, "")}\t{h.get("fitted", {}).get("score", "")}\t{h["degenerate"]}\t'
                        f'{out["gate_joint"]}\t{out["cell_pass"].get(c, False)}\n')
    print('gate_joint', out["gate_joint"], 'cell_pass', out["cell_pass"])


if __name__ == '__main__':
    {'relabel': relabel, 'remap': remap}[sys.argv[1]]()
