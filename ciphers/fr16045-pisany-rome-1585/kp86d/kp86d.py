#!/usr/bin/env python3
"""Pre-registered test kp86d (kp86d/PREREG_kp86d.md, RUN4-PIS2): key86 on fr.16045 f.275r (4 Nov 1586 letter) against
the Colbert 16 pt II clear copy pp.121-123 (kp86d/colbert_p121_123.txt). Statistic, nulls and decode rule from
kp86/kp86.py (imported, unchanged). Arms: A = key86.tsv as published; B = key86 + RUN4-PIS1's f.244r remap
(T31->o, T45->u, T47->f, T57->n), fitted elsewhere, f.275r held out. Positive control: the first n_dec letters of the
copy span with the in-clear phrase removed (CLEAR_IN_MS), enciphered with the arm's key at noise e, scored against the
same full copy text; 5 seeds, 200/200 nulls, pass at >= 4/5.
    python3 kp86d/kp86d.py --err E [--tokens tx86d/ciphertext_f275r.tsv] [--extra tx86d/passA.tsv tx86d/passB.tsv]
Writes kp86d/kp86d_result.json."""
import argparse, json, os, random, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(T, 'kp86')); sys.path.insert(0, os.path.join(T, '../../tools'))
from kp86 import norm, load_key, dec, p99, test
REMAP_B = {'T31': 'o', 'T45': 'u', 'T47': 'f', 'T57': 'n'}
CLEAR_IN_MS = 'Mais croyant que Monsieur de Luxembourg'   # written in clear on f.275r between the two cipher blocks


def load_tokens(path):
    toks, dropped = [], 0
    for ln in open(os.path.join(T, path)):
        if not ln.strip():
            continue
        for t in ln.rstrip('\n').split('\t', 1)[1].split():
            t = t.rstrip('?')
            if t.startswith('T') and t[1:].isdigit():
                toks.append(t)
            elif t != '/':
                dropped += 1
    return toks, dropped


def control(key, ptext, clear, err, n):
    cells = {}
    for lab, v in key.items():
        if len(v) == 1:
            cells.setdefault(v, []).append(lab)
    labs = list(key); out = []
    src = [c for c in ptext if c in cells][:n]
    for sd in range(5):
        r2 = random.Random(500 + sd)
        ct = [r2.choice(cells[c]) for c in src]
        ct = [r2.choice([x for x in labs if x != t]) if r2.random() < err else t for t in ct]
        s, ks, os_ = test(ct, key, clear, 200, 200, r2)
        out.append({"seed": sd, "N": len(ct), "score": round(s, 4), "keyshuffle_p99": round(p99(ks), 4),
                    "order_p99": round(p99(os_), 4), "pass": bool(s > p99(ks) and s > p99(os_))})
    k = sum(x["pass"] for x in out)
    return {"seeds": out, "passed": k, "pass": k >= 4}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--err', type=float, required=True)
    ap.add_argument('--tokens', default='tx86d/ciphertext_f275r.tsv')
    ap.add_argument('--extra', nargs='*', default=['tx86d/passA.tsv', 'tx86d/passB.tsv'])
    a = ap.parse_args()
    raw = open(os.path.join(HERE, 'colbert_p121_123.txt')).read()
    ctext = norm(raw); clear = np.array([ord(c) - 97 for c in ctext], dtype=np.int64)
    ptext = norm(raw.replace(CLEAR_IN_MS, ''))
    keyA = load_key(); keyB = dict(keyA); keyB.update(REMAP_B)
    out = {"clear_letters": len(clear), "err": a.err, "remap_B": REMAP_B}
    for arm, key in (('A', keyA), ('B', keyB)):
        rnd = random.Random(20261004); res = {}
        for name in [a.tokens] + a.extra:
            toks, dr = load_tokens(name)
            s, ks, os_ = test(toks, key, clear, 1000, 1000, rnd)
            res[name] = {"tokens": len(toks), "dropped": dr, "decoded_letters": int(len(dec(toks, key))),
                         "score": round(s, 4), "keyshuffle_p99": round(p99(ks), 4), "keyshuffle_mean": round(float(np.mean(ks)), 4),
                         "order_p99": round(p99(os_), 4), "order_mean": round(float(np.mean(os_)), 4),
                         "above_both": bool(s > p99(ks) and s > p99(os_))}
            print(arm, name, res[name])
        n = res[a.tokens]["decoded_letters"]
        res['positive_control'] = control(key, ptext, clear, a.err, n)
        print(arm, 'control', res['positive_control']['passed'], '/5', res['positive_control']['seeds'])
        t = res[a.tokens]
        res['verdict'] = ('NON-TEST (positive control fails)' if not res['positive_control']['pass'] else
                          'PASS' if t['above_both'] else
                          ('FAIL' if a.err <= 0.10 else 'FAIL at err > 0.10 with the control passing at this e'))
        print(arm, 'VERDICT', res['verdict']); out['arm_' + arm] = res
    json.dump(out, open(os.path.join(HERE, 'kp86d_result.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()
