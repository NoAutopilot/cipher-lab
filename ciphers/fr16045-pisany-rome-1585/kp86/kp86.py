#!/usr/bin/env python3
"""Known-answer test kp86 (PREREG_kp86.md): Tomokiyo's 1586-87 table (key86.tsv) on fr.16045 f.244r against the
Colbert 16 pt II clear copy (kp86/colbert_p49_50.txt). Statistic tools/stream_align.nw_score; nulls key-shuffle (1000)
and order-shuffle (1000); positive control at the measured err_2reader (5 seeds, 200/200 nulls).
    python3 kp86/kp86.py --err E [--tokens tx86/ciphertext_f244r.tsv] [--extra tx86/passA.tsv tx86/passB.tsv]
Writes kp86/kp86_result.json. Run from the target folder or anywhere (paths are relative to the target folder)."""
import argparse, json, os, random, sys, unicodedata
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(T, '../../tools'))
from stream_align import nw_score


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if 'a' <= c <= 'z')
    return s.replace('j', 'i').replace('v', 'u')


def load_key():
    key = {}
    for ln in open(os.path.join(T, 'key86.tsv')).read().splitlines()[1:]:
        f = ln.split('\t'); key[f[0]] = '' if f[1] == '<null>' else norm(f[1])
    return key


def load_tokens(path):
    toks, dropped = [], 0
    for ln in open(os.path.join(T, path)):
        if not ln.strip():
            continue
        for t in ln.rstrip('\n').split('\t', 1)[1].split():
            t = t.rstrip('?')
            if t.startswith('T') and t[1:].isdigit():
                toks.append(t)
            else:
                dropped += 1
    return toks, dropped


def dec(toks, key):
    return np.array([ord(c) - 97 for c in ''.join(key.get(t, '') for t in toks)], dtype=np.int64)


def p99(x):
    return float(np.percentile(x, 99))


def test(toks, key, clear, nk, no, rnd):
    s = nw_score(dec(toks, key), clear)
    labs, vals = list(key), list(key.values())
    ks = []
    for _ in range(nk):
        v = vals[:]; rnd.shuffle(v); ks.append(nw_score(dec(toks, dict(zip(labs, v))), clear))
    os_ = []
    for _ in range(no):
        t = toks[:]; rnd.shuffle(t); os_.append(nw_score(dec(t, key), clear))
    return s, ks, os_


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--err', type=float, required=True)
    ap.add_argument('--tokens', default='tx86/ciphertext_f244r.tsv')
    ap.add_argument('--extra', nargs='*', default=['tx86/passA.tsv', 'tx86/passB.tsv'])
    a = ap.parse_args()
    key = load_key()
    ctext = norm(open(os.path.join(HERE, 'colbert_p49_50.txt')).read())
    clear = np.array([ord(c) - 97 for c in ctext], dtype=np.int64)
    rnd = random.Random(20261004)
    out = {"clear_letters": len(clear), "err": a.err}
    for name in [a.tokens] + a.extra:
        toks, dr = load_tokens(name)
        s, ks, os_ = test(toks, key, clear, 1000, 1000, rnd)
        out[name] = {"tokens": len(toks), "dropped": dr, "decoded_letters": int(len(dec(toks, key))),
                     "score": round(s, 4), "keyshuffle_p99": round(p99(ks), 4), "keyshuffle_mean": round(float(np.mean(ks)), 4),
                     "order_p99": round(p99(os_), 4), "order_mean": round(float(np.mean(os_)), 4),
                     "above_both": bool(s > p99(ks) and s > p99(os_))}
        print(name, out[name])
    # positive control
    cells = {}
    for lab, v in key.items():
        if len(v) == 1:
            cells.setdefault(v, []).append(lab)
    labs = list(key); seeds = []
    for sd in range(5):
        r2 = random.Random(500 + sd)
        ct = [r2.choice(cells[c]) for c in ctext if c in cells]
        ct = [r2.choice([x for x in labs if x != t]) if r2.random() < a.err else t for t in ct]
        s, ks, os_ = test(ct, key, clear, 200, 200, r2)
        seeds.append({"seed": sd, "N": len(ct), "score": round(s, 4), "keyshuffle_p99": round(p99(ks), 4),
                      "order_p99": round(p99(os_), 4), "pass": bool(s > p99(ks) and s > p99(os_))})
    npass = sum(x["pass"] for x in seeds)
    out["positive_control"] = {"seeds": seeds, "passed": npass, "pass": npass >= 4}
    print("control", npass, "/5", seeds)
    tgt = out[a.tokens]
    if not out["positive_control"]["pass"]:
        v = "NON-TEST (positive control fails)"
    elif tgt["above_both"]:
        v = "PASS"
    else:
        v = "FAIL" if a.err <= 0.10 else "FAIL at err > 0.10 with the control passing at this e (read per PREREG)"
    out["verdict"] = v; print("VERDICT", v)
    json.dump(out, open(os.path.join(HERE, 'kp86_result.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()
