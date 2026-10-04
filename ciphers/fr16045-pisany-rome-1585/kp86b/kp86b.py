#!/usr/bin/env python3
"""Pre-registered test kp86b (kp86b/PREREG_kp86b.md): key86 on fr.16045 f.244v + f.245r (17 Sept 1586) against the
Colbert 16 pt II clear copy p.51 l.13 - p.52 (kp86b/colbert_p51_52.txt). Same statistic, nulls and positive control as
kp86/kp86.py (imported, unchanged); two arms: A = key86.tsv as published, B = key86 with the label-level remap from unit (a)
(kp86b/cellcheck_a.md: T31->o, T45->u, T47->f, T57->n). Each arm gets its own nulls and its own control.
    python3 kp86b/kp86b.py --err E [--tokens tx86b/ciphertext_f244v_f245r.tsv] [--extra tx86b/passA.tsv tx86b/passB.tsv]
Writes kp86b/kp86b_result.json. Folio sub-scores (f244v / f245r lines alone) are descriptive, not gating."""
import argparse, json, os, random, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(T, 'kp86')); sys.path.insert(0, os.path.join(T, '../../tools'))
from kp86 import norm, load_key, dec, p99, test
from stream_align import nw_score
REMAP_B = {'T31': 'o', 'T45': 'u', 'T47': 'f', 'T57': 'n'}


def load_tokens(path, prefix=None):
    toks, dropped = [], 0
    for ln in open(os.path.join(T, path)):
        if not ln.strip():
            continue
        lab, body = ln.rstrip('\n').split('\t', 1)
        if prefix and not lab.startswith(prefix):
            continue
        for t in body.split():
            t = t.rstrip('?')
            if t.startswith('T') and t[1:].isdigit():
                toks.append(t)
            elif t != '/':
                dropped += 1
    return toks, dropped


def control(key, ctext, clear, err, seeds=5):
    cells = {}
    for lab, v in key.items():
        if len(v) == 1:
            cells.setdefault(v, []).append(lab)
    labs = list(key); out = []
    for sd in range(seeds):
        r2 = random.Random(500 + sd)
        ct = [r2.choice(cells[c]) for c in ctext if c in cells]
        ct = [r2.choice([x for x in labs if x != t]) if r2.random() < err else t for t in ct]
        s, ks, os_ = test(ct, key, clear, 200, 200, r2)
        out.append({"seed": sd, "N": len(ct), "score": round(s, 4), "keyshuffle_p99": round(p99(ks), 4),
                    "order_p99": round(p99(os_), 4), "pass": bool(s > p99(ks) and s > p99(os_))})
    n = sum(x["pass"] for x in out)
    return {"seeds": out, "passed": n, "pass": n >= 4}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--err', type=float, required=True)
    ap.add_argument('--tokens', default='tx86b/ciphertext_f244v_f245r.tsv')
    ap.add_argument('--extra', nargs='*', default=['tx86b/passA.tsv', 'tx86b/passB.tsv'])
    a = ap.parse_args()
    ctext = norm(open(os.path.join(HERE, 'colbert_p51_52.txt')).read())
    clear = np.array([ord(c) - 97 for c in ctext], dtype=np.int64)
    keyA = load_key(); keyB = dict(keyA); keyB.update(REMAP_B)
    out = {"clear_letters": len(clear), "err": a.err, "remap_B": REMAP_B}
    for arm, key in (('A', keyA), ('B', keyB)):
        rnd = random.Random(20261004)
        res = {}
        for name in [a.tokens] + a.extra:
            toks, dr = load_tokens(name)
            s, ks, os_ = test(toks, key, clear, 1000, 1000, rnd)
            res[name] = {"tokens": len(toks), "dropped": dr, "decoded_letters": int(len(dec(toks, key))),
                         "score": round(s, 4), "keyshuffle_p99": round(p99(ks), 4), "keyshuffle_mean": round(float(np.mean(ks)), 4),
                         "order_p99": round(p99(os_), 4), "order_mean": round(float(np.mean(os_)), 4),
                         "above_both": bool(s > p99(ks) and s > p99(os_))}
            print(arm, name, res[name])
        for pre in ('f244v', 'f245r'):
            toks, _ = load_tokens(a.tokens, pre)
            if toks:
                res['descriptive_' + pre] = {"tokens": len(toks), "score": round(nw_score(dec(toks, key), clear), 4)}
        res['positive_control'] = control(key, ctext, clear, a.err)
        print(arm, 'control', res['positive_control']['passed'], '/5')
        t = res[a.tokens]
        res['verdict'] = ('NON-TEST (positive control fails)' if not res['positive_control']['pass'] else
                          'PASS' if t['above_both'] else
                          'FAIL' if a.err <= 0.10 else 'FAIL at err > 0.10 with the control passing at this e')
        print(arm, 'VERDICT', res['verdict'])
        out['arm_' + arm] = res
    json.dump(out, open(os.path.join(HERE, 'kp86b_result.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()
