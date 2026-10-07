#!/usr/bin/env python3
"""Step 6 of SFZ-1 (7 Oct 2026): does Amidani's 1447 key (key.tsv, built from italien 1584 ff.366/367 + copies) also read
his 4 May 1446 letter, BnF italien 1583 f.70 (Bourdeau's draft transcription, ciphers/sforza-maino-1446/ciphertext_f70.txt)?

A TEST, not a reading: Bourdeau's codes are mapped to our labels by his written descriptions only (MAP below; codes with
no counterpart decode to nothing and are dropped), the f.70 signs are decoded with the pooled key, and two statistics are
compared with 200 shuffled keys (the key's sign -> value map permuted among mapped signs, same seed each run):
  lm   mean log10 4-gram probability per letter under tools/judge_plaintext.py's NgramModel on the it16dip corpus
       (16th-c. Italian diplomatic letters: an era mismatch for 1446, flagged)
  q4   fraction of the decode's 4-grams found in the two clear copies' text (ff.365, 368)
PASS (pre-registered in the brief) = both statistics above the shuffle p95. No reading file is written unless it passes.

    python3 ciphers/sforza-italien1584-1447/amidani/f70_test.py
"""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..', '..', '..')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import judge_plaintext as jp  # noqa: E402

# Bourdeau code (signs.tsv description) -> our label (labels.md); None = no counterpart found by description
MAP = {
    'p': 'q',     # "p as written": our q (p/q-like sign with a stroke through the descender)
    'F': 'F',     # double-barred stroke
    'B': 'P',     # barred b: our P (b with a bar)
    '+': '+',
    'E': 'B',     # f.70 E "b with double bar": nearest is our B (b with hooked tail) -- weak
    '8': '8',
    'Q': 'Q',     # phi
    'J': 'J',     # barred yogh
    'c': 'c',
    'S': 'f',     # long s: our f (single long s with crossbar)
    'H': 'H',     # looped h
    'd': 'd',     # d with apostrophe
    'z': 'z',
    '>': '>',
    'r': 'R',     # "r as written": our R (or-like sign) -- weak
    'Y': 'Y',     # slashed v: our Y (gamma-like) -- weak
    'V': 'V',     # cross-circle: our V (circle with bar), 1 occurrence in training
    'g': 'g',
    'D': 'D',     # divide sign
    'n': 'n',
    'X': 'x',     # X: our x
    'W': None,    # ab-ligature: no counterpart
    '4': '4',
    'O': None,    # reversed c: no counterpart
    '6': 'b',     # 6: our b (6-like b)
    'e': 'e',
    '3': '3',
    'b': 'b',
    'K': None,    # hatched sign: no counterpart
    'P': None,    # barred p: no counterpart
    's': 'S',     # s: our S (curl + long s) -- weak
}
SEED = 70
NSHUF = 200


def main():
    key = {}
    for l in open(os.path.join(HERE, 'key.tsv')).read().split('\n')[1:]:
        if l:
            a = l.split('\t')
            key[a[0]] = a[1]
    codes = []
    for l in open(os.path.join(ROOT, 'ciphers', 'sforza-maino-1446', 'ciphertext_f70.txt')):
        if l.startswith('#'):
            continue
        for t in l.split():
            if t.startswith('{') or t == '.':
                continue
            codes.append(t)
    labs = [MAP.get(c) for c in codes]
    nomap = sorted({c for c, l in zip(codes, labs) if l is None or l not in key})
    covered = [l for l in labs if l is not None and l in key]
    signs = sorted(set(covered))
    vals = [key[s] for s in signs]
    lm = jp.NgramModel([jp.read_corpus(p) for p in jp.LANG_CORPORA['it16dip']])
    clear = ''.join(jp.fold(' '.join(x for x in open(os.path.join(HERE, f)) if not x.startswith('#')))
                    for f in ('clear_f365.txt', 'clear_f368.txt'))
    g4 = {clear[i:i + 4] for i in range(len(clear) - 3)}

    def stats(m):
        s = ''.join(m[x] for x in covered)
        q = [s[i:i + 4] in g4 for i in range(len(s) - 3)]
        return s, lm.score(s), float(np.mean(q))
    real_s, real_lm, real_q = stats(dict(zip(signs, vals)))
    rng = np.random.default_rng(SEED)
    sl, sq = [], []
    for _ in range(NSHUF):
        _, a, b = stats(dict(zip(signs, rng.permutation(vals))))
        sl.append(a); sq.append(b)
    p95l, p95q = np.quantile(sl, 0.95), np.quantile(sq, 0.95)
    ok = real_lm > p95l and real_q > p95q
    print(f'f.70 codes {len(codes)}; decoded {len(covered)}; codes with no counterpart or untrained: {" ".join(nomap)}')
    print(f'lm(it16dip)\treal {real_lm:.3f}\tshuffle mean {np.mean(sl):.3f}\tp95 {p95l:.3f}')
    print(f'q4(copies)\treal {real_q:.3f}\tshuffle mean {np.mean(sq):.3f}\tp95 {p95q:.3f}')
    print(f'verdict: {"PASS" if ok else "FAIL"} (both above shuffle p95 required)')
    print('decode (TEST ONLY, not a reading, every token M at best):', real_s[:200])
    return 0


if __name__ == '__main__':
    sys.exit(main())
