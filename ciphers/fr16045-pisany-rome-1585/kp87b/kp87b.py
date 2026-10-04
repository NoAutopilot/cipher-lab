#!/usr/bin/env python3
"""Pre-registered test kp87b (kp87b/PREREG_kp87b.md, PIS1-302): kp87a/kp87a.py run UNCHANGED (statistic, nulls, seeds,
positive control, gate) on f.302v of the 24 Mar 1587 letter against its Colbert 16 pt II clear copy, twice:
  arm A = key86.tsv as published (kp87a.load_key untouched);
  arm B = key86 + kp86d.REMAP_B (the PIS1 remap, reported beside A; nothing enters key86.tsv from this test).
kp87a.main() writes its result under the key 'arm_A' of the --out file; for arm B this wrapper only swaps kp87a's
imported load_key for one that applies REMAP_B and renames the key afterwards. Then the margin-gloss witness (not gating):
  W1 = nw_score(gloss letters, copy letters) vs an order-shuffle of the gloss letters (1000, p99), both texts through
       kp86.norm (one convention: lower case, letters only, j->i, v->u, accents stripped; the gloss's abbreviations are
       expanded in gloss_f302v_expanded.txt before norm, per CLAUDE.md rule 3 PX-BRODEC);
  W2 = kp86.test(reconciled tokens, key86, gloss letters) with the same key-shuffle / order nulls (1000/1000).
    python3 kp87b/kp87b.py --err E      (tokens tx87b/ciphertext_f302v.tsv, extra tx87b/passA.tsv tx87b/passB.tsv)
Writes kp87b/kp87b_result.json."""
import argparse, json, os, random, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
for d in ('kp86', 'kp86d', 'kp87a'):
    sys.path.insert(0, os.path.join(T, d))
sys.path.insert(0, os.path.join(T, '../../tools'))
import kp86, kp86d, kp87a
from stream_align import nw_score

CLEAR = 'kp87b/colbert_p341_342.txt'
TOKS = 'tx87b/ciphertext_f302v.tsv'
EXTRA = ['tx87b/passA.tsv', 'tx87b/passB.tsv']
GLOSS = 'kp87b/gloss_f302v_expanded.txt'


def run_arm(err, inms, out_name, key_fn):
    orig = kp87a.load_key
    kp87a.load_key = key_fn
    try:
        sys.argv = ['kp87a.py', '--err', str(err), '--clear', CLEAR, '--tokens', TOKS, '--extra', *EXTRA,
                    '--out', out_name] + (['--inms', *inms] if inms else [])
        kp87a.main()
    finally:
        kp87a.load_key = orig
    p = os.path.join(T, out_name); r = json.load(open(p)); os.remove(p)
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--err', type=float, required=True)
    ap.add_argument('--inms', nargs='*', default=[])
    a = ap.parse_args()
    out = {}
    rA = run_arm(a.err, a.inms, 'kp87b/_armA.json', kp86.load_key)
    out.update({k: v for k, v in rA.items() if k != 'arm_A'}); out['arm_A'] = rA['arm_A']
    keyB = lambda: {**kp86.load_key(), **kp86d.REMAP_B}
    rB = run_arm(a.err, a.inms, 'kp87b/_armB.json', keyB)
    out['arm_B'] = rB['arm_A']; out['remap_B'] = kp86d.REMAP_B
    # margin-gloss witness (not gating)
    clear = np.array([ord(c) - 97 for c in kp86.norm(open(os.path.join(T, CLEAR)).read())], dtype=np.int64)
    gl = np.array([ord(c) - 97 for c in kp86.norm(open(os.path.join(T, GLOSS)).read())], dtype=np.int64)
    rnd = random.Random(20261004)
    w1 = nw_score(gl, clear); nul = []
    for _ in range(1000):
        g = gl.copy(); rnd.shuffle(g); nul.append(nw_score(g, clear))
    out['W1_gloss_vs_copy'] = {"gloss_letters": int(len(gl)), "score": round(w1, 4), "order_p99": round(kp86.p99(nul), 4),
                               "order_mean": round(float(np.mean(nul)), 4), "above": bool(w1 > kp86.p99(nul))}
    toks, _ = kp86d.load_tokens(TOKS)
    s, ks, os_ = kp86.test(toks, kp86.load_key(), gl, 1000, 1000, rnd)
    out['W2_decode_vs_gloss'] = {"score": round(s, 4), "keyshuffle_p99": round(kp86.p99(ks), 4),
                                 "order_p99": round(kp86.p99(os_), 4),
                                 "above_both": bool(s > kp86.p99(ks) and s > kp86.p99(os_))}
    print('W1', out['W1_gloss_vs_copy']); print('W2', out['W2_decode_vs_gloss'])
    json.dump(out, open(os.path.join(HERE, 'kp87b_result.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()
