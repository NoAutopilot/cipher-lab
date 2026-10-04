#!/usr/bin/env python3
"""Pre-registered test kp87a (kp87a/PREREG_kp87a.md, RUN5-PIS87): key86 (arm A only, as published) on one cipher page of
the 24 Mar 1587 letter (fr.16045 f.297-303) against its Colbert 16 pt II clear copy (pp.324 ff.). Statistic, nulls and
decode rule from kp86/kp86.py (imported, unchanged); positive control and gate exactly kp86d/kp86d.py's control()
(imported, unchanged): the first n_dec letters of the copy span with any in-clear phrases removed, enciphered with key86 at
noise e, scored against the full copy text; 5 seeds, 200/200 nulls, pass at >= 4/5.
    python3 kp87a/kp87a.py --err E --clear kp87a/colbert_<pp>.txt --tokens tx87/ciphertext_<page>.tsv \
        [--extra tx87/passA.tsv tx87/passB.tsv] [--inms "phrase" ...] [--out kp87a/kp87a_result.json]
Run from anywhere; paths are relative to the target folder."""
import argparse, json, os, random, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(T, 'kp86')); sys.path.insert(0, os.path.join(T, 'kp86d'))
sys.path.insert(0, os.path.join(T, '../../tools'))
from kp86 import norm, load_key, dec, p99, test
from kp86d import load_tokens, control


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--err', type=float, required=True)
    ap.add_argument('--clear', required=True)
    ap.add_argument('--tokens', required=True)
    ap.add_argument('--extra', nargs='*', default=[])
    ap.add_argument('--inms', nargs='*', default=[], help='phrases written in clear inside the cipher block')
    ap.add_argument('--out', default='kp87a/kp87a_result.json')
    a = ap.parse_args()
    raw = open(os.path.join(T, a.clear)).read()
    clear = np.array([ord(c) - 97 for c in norm(raw)], dtype=np.int64)
    pt = raw
    for ph in a.inms:
        pt = pt.replace(ph, '')
    ptext = norm(pt)
    key = load_key()
    out = {"clear_letters": len(clear), "err": a.err, "arm": "A (key86.tsv as published)"}
    rnd = random.Random(20261004); res = {}
    for name in [a.tokens] + a.extra:
        toks, dr = load_tokens(name)
        s, ks, os_ = test(toks, key, clear, 1000, 1000, rnd)
        res[name] = {"tokens": len(toks), "dropped": dr, "decoded_letters": int(len(dec(toks, key))),
                     "score": round(s, 4), "keyshuffle_p99": round(p99(ks), 4), "keyshuffle_mean": round(float(np.mean(ks)), 4),
                     "order_p99": round(p99(os_), 4), "order_mean": round(float(np.mean(os_)), 4),
                     "above_both": bool(s > p99(ks) and s > p99(os_))}
        print(name, res[name], flush=True)
    n = res[a.tokens]["decoded_letters"]
    res['positive_control'] = control(key, ptext, clear, a.err, n)
    print('control', res['positive_control']['passed'], '/5', res['positive_control']['seeds'], flush=True)
    t = res[a.tokens]
    res['verdict'] = ('NON-TEST (positive control fails)' if not res['positive_control']['pass'] else
                      'PASS' if t['above_both'] else
                      ('FAIL' if a.err <= 0.10 else 'FAIL at err > 0.10 with the control passing at this e'))
    print('VERDICT', res['verdict']); out['arm_A'] = res
    json.dump(out, open(os.path.join(T, a.out), 'w'), indent=1)


if __name__ == '__main__':
    main()
