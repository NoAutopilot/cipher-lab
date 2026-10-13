#!/usr/bin/env python3
"""BNF-K60 (13 Oct 2026): order-sensitive local-anchor test of key no.60 on f.91 L02-L05, registered in
../PREREG-K60.md before any score was computed.

Shape ported from D. Bourdeau's cyphersolver targets/nevers1593/f88/shuffle_control.py (MIT, c60e6dd, 12 Oct 2026;
issue #32 by R. Weglarek): decode the cipher tokens with key no.60, take the longest lexicon word spelled inside a
contiguous decoded run, compare with random permutations of the same tokens. Not a copy: our lexicon (fr16), our key
(ciphers/fr3986-nevers-revol-1593/key.tsv, synced to his c60e6dd), every table alternative of an M tag allowed, and a
word may start or end inside a token's value (substring of the run, not token-aligned).

Usage:
  k60_order_test.py target [--shuf 5000]
  k60_order_test.py control ERR [--texts 200] [--shuf 5000]      positive control at sign-substitution rate ERR
  k60_order_test.py negative [--texts 200] [--shuf 5000]          random tag strings, f.91 tag frequencies
"""
import sys, re, gzip, random, argparse
from collections import Counter
from pathlib import Path
from multiprocessing import Pool

R = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(R / "tools"))
import judge_plaintext as J

KEYF = R / "ciphers/fr3986-nevers-revol-1593/key.tsv"
CT = Path(__file__).resolve().parents[1] / "ciphertext.tsv"
FR16 = R / "tools/data/fr16"
F_ALL = ["lettresdecatheri01cathuoft_djvu.txt.gz", "lettresdecatheri02cathuoft_djvu.txt.gz",
         "lettresindites00marg_djvu.txt.gz"]
F_WINDOW = "lettresdecatheri02cathuoft_djvu.txt.gz"      # control windows; held out of the control lexicon
MINLEN, MINCOUNT, N_CTRL, UNK_SHARE = 4, 2, 135, 0.18
UNK = "<U>"


def load_key():
    key = {}
    for l in KEYF.read_text().splitlines():
        if not l or l.startswith("#") or l.startswith("sign\t"):
            continue
        r = l.split("\t")
        alts = sorted({a for a in (J.fold(x) for x in r[1].split("|")) if a})
        if alts:
            key[r[0]] = alts
    return key


def words(files):
    c = Counter()
    for f in files:
        txt = gzip.open(FR16 / f, "rt", encoding="utf-8", errors="ignore").read()
        c.update(J.fold(w) for w in re.findall(r"[^\W\d_]+", txt))
    return {w for w, n in c.items() if len(w) >= MINLEN and n >= MINCOUNT}


def trie(lex):
    root = {}
    for w in lex:
        n = root
        for ch in w:
            n = n.setdefault(ch, {})
        n["$"] = 1
    return root


def target_tokens():
    toks = []
    for l in CT.read_text().splitlines():
        lid, body = l.split("\t", 1)
        if lid in ("f91_L02", "f91_L03", "f91_L04", "f91_L05"):
            toks += [t.rstrip("?") for t in body.split() if not t.startswith("w:")]
    return toks


class Stat:
    """S = length of the longest lexicon word spelled inside any contiguous run of keyed tokens."""
    def __init__(self, key, root):
        self.key, self.root = key, root

    def __call__(self, seq):
        vals = [self.key.get(t) for t in seq]
        best, where = 0, None
        n = len(vals)
        for i in range(n):
            if not vals[i]:
                continue
            for a in vals[i]:
                for k in range(len(a)):
                    # DFS: (node, token index, offset in current alt string, alt string, depth)
                    stack = [(self.root, i, a, k, 0)]
                    while stack:
                        node, j, s, o, d = stack.pop()
                        while o < len(s):
                            node = node.get(s[o])
                            if node is None:
                                break
                            o += 1; d += 1
                            if "$" in node and d > best:
                                best, where = d, (i, j)
                        else:
                            if j + 1 < n and vals[j + 1]:
                                for b in vals[j + 1]:
                                    stack.append((node, j + 1, b, 0, d))
        return best, where


def decode_span(key, seq, i, j):
    return " ".join("|".join(key[t]) for t in seq[i:j + 1])


def pval(stat, seq, nshuf, seed):
    rnd = random.Random(seed)
    s0, _ = stat(seq)
    ge = 0
    t = list(seq)
    for _ in range(nshuf):
        rnd.shuffle(t)
        if stat(t)[0] >= s0:
            ge += 1
    return s0, ge


def synth(key, raw, rnd, N):
    """fr16 window enciphered with key: greedy longest word/syllable/letter value, uniform homophone (as G60D)."""
    by = {}
    for s, alts in key.items():
        for a in alts:
            by.setdefault(a, []).append(s)
    maxl = max(map(len, by))
    j = rnd.randrange(0, len(raw) - 40 * N)
    w = raw[j:j + 40 * N]; i = 0; seq = []
    while len(seq) < N and i < len(w):
        for L in range(min(maxl, len(w) - i), 0, -1):
            if w[i:i + L] in by:
                seq.append(rnd.choice(by[w[i:i + L]])); i += L; break
        else:
            i += 1
    return seq


G = {}


def _init(lexfiles):
    G["key"] = load_key()
    G["stat"] = Stat(G["key"], trie(words(lexfiles)))


def _ctrl(args):
    idx, err, nshuf, mode = args
    key, stat = G["key"], G["stat"]
    rnd = random.Random(60000 + idx)
    tags = sorted(key)
    if mode == "neg":
        tf = G["tf"]
        seq = rnd.choices(list(tf), weights=list(tf.values()), k=N_CTRL)
    else:
        seq = synth(key, G["raw"], rnd, N_CTRL)
        seq = [rnd.choice(tags) if rnd.random() < err else s for s in seq]   # sign substitution
        pos = rnd.sample(range(len(seq)), round(UNK_SHARE * len(seq)))      # unkeyed share, as f.91
        for p in pos:
            seq[p] = UNK
    s0, ge = pval(stat, seq, nshuf, 70000 + idx)
    return s0, ge


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["target", "control", "negative"])
    ap.add_argument("err", nargs="?", type=float, default=0.0)
    ap.add_argument("--texts", type=int, default=200)
    ap.add_argument("--shuf", type=int, default=None)
    a = ap.parse_args()
    if a.mode == "target":
        nshuf = a.shuf or 5000
        key = load_key(); lex = words(F_ALL); stat = Stat(key, trie(lex))
        seq = target_tokens()
        unk = [t for t in seq if t not in key]
        print(f"lexicon fr16 (3 files, len>={MINLEN}, count>={MINCOUNT}): {len(lex)} words")
        print(f"tokens {len(seq)}, keyed {len(seq) - len(unk)}, unkeyed {len(unk)}: {dict(Counter(unk))}")
        s0, where = stat(seq)
        i, j = where
        print(f"S = {s0}; run tokens {i}-{j}: {' '.join(seq[i:j + 1])}")
        print(f"decoded values there: {decode_span(key, seq, i, j)}")
        s0b, ge = pval(stat, seq, nshuf, 91)
        print(f"shuffles >= S: {ge}/{nshuf}; p = {ge / nshuf:.5f}; (ge+1)/(n+1) = {(ge + 1) / (nshuf + 1):.5f}")
        return
    nshuf = a.shuf or 5000
    if a.mode == "control":
        lexfiles = [f for f in F_ALL if f != F_WINDOW]
        mode = "pos"
    else:
        lexfiles = F_ALL
        mode = "neg"
    raw = J.fold(gzip.open(FR16 / F_WINDOW, "rt", encoding="utf-8", errors="ignore").read())
    tf = Counter(target_tokens())

    def init():
        _init(lexfiles); G["raw"] = raw; G["tf"] = tf
    with Pool(4, initializer=init) as pool:
        res = pool.map(_ctrl, [(k, a.err, nshuf, mode) for k in range(a.texts)], chunksize=1)
    hits = sum(ge / nshuf <= 0.01 for _, ge in res)
    Ss = sorted(s for s, _ in res)
    print(f"{a.mode} err={a.err} texts={a.texts} shuf={nshuf}: power(p<=0.01) = {hits}/{a.texts} = {hits / a.texts:.3f}; "
          f"S median {Ss[len(Ss) // 2]}, min {Ss[0]}, max {Ss[-1]}")


if __name__ == "__main__":
    main()
