#!/usr/bin/env python3
"""BNF-G60D: instrument that keeps each no.60 tag's full value (letters, syllables, words), Viterbi-resolves ambiguous
tags under the fr16 4-gram, scores (a) 4-gram per char, (b) word cover; null = value strings permuted within class.
Registered in .claude/briefs/runs/2026-10-08-ytbiz-bnf-g60d.md. Scripts only. Usage: g60d_instrument.py ERR [N] [SEEDS] [SHUF]
Gate statistic named before running: (b) word cover."""
import sys, random, math, statistics
from pathlib import Path
R = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(R / "tools"))
import judge_plaintext as J

KEYF = R / "ciphers/fr3986-nevers-revol-1593/key.tsv"

def load_key(path=KEYF):
    rows = [l.rstrip("\n").split("\t") for l in Path(path).read_text().splitlines()
            if l and not l.startswith("#") and not l.startswith("sign\t")]
    key = {}
    for r in rows:
        alts = [a for a in (J.fold(x) for x in r[1].split("|")) if a]
        if alts: key[r[0]] = alts
    return key

def cls(alts):
    n = len(alts[0]); return "L" if n == 1 else ("S" if n <= 3 else "W")

def make_null(key, rnd):
    by = {}
    for s, a in key.items(): by.setdefault(cls(a), []).append(s)
    out = {}
    for c, tg in by.items():
        vals = [key[s] for s in tg]; rnd.shuffle(vals); out.update(zip(tg, vals))
    return out

class Inst:
    def __init__(self):
        self.model = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA["fr"]])
        m = self.model; self.cache = {}
        self.lg = lambda g: math.log10((m.c.get(g, 0) + m.k) / (m.ctx.get(g[:-1], 0) + m.V * m.k))
    def lp(self, ctx, ch):
        k = ctx + ch; v = self.cache.get(k)
        if v is None: v = self.cache[k] = self.lg(k) if len(ctx) == 3 else -1.2
        return v
    def viterbi(self, seq, key, beam=200):
        st = {"": (0.0, "")}  # last-3 context -> (score, text)
        for s in seq:
            alts = key.get(s)
            if not alts: continue
            nst = {}
            for ctx, (sc, tx) in st.items():
                for a in alts:
                    c2, s2 = ctx, sc
                    for ch in a:
                        s2 += self.lp(c2, ch); c2 = (c2 + ch)[-3:]
                    cur = nst.get(c2)
                    if cur is None or s2 > cur[0]: nst[c2] = (s2, tx + a)
            if len(nst) > beam: nst = dict(sorted(nst.items(), key=lambda kv: -kv[1][0])[:beam])
            st = nst
        return max(st.values())[1]
    def stats(self, seq, key):
        t = self.viterbi(seq, key); return self.model.score(t), self.model.cover(t)

def synth(inst, key, rnd, N):
    """fr16 window enciphered with key: greedy longest word/syllable/letter match, uniform homophone; N tags."""
    by = {}
    for s, alts in key.items():
        for a in alts: by.setdefault(a, []).append(s)
    maxl = max(map(len, by)); raw = inst.model.raw
    j = rnd.randrange(0, len(raw) - 40 * N); w = raw[j:j + 40 * N]; i = 0; seq = []
    while len(seq) < N and i < len(w):
        for L in range(min(maxl, len(w) - i), 0, -1):
            if w[i:i + L] in by:
                seq.append(rnd.choice(by[w[i:i + L]])); i += L; break
        else: i += 1
    return seq

def main():
    err = float(sys.argv[1]); N = int(sys.argv[2]) if len(sys.argv) > 2 else 190
    seeds = int(sys.argv[3]) if len(sys.argv) > 3 else 10; shuf = int(sys.argv[4]) if len(sys.argv) > 4 else 200
    key = load_key(); tags = sorted(key); inst = Inst()
    print(f"tags {len(key)} classes", {c: sum(cls(a) == c for a in key.values()) for c in "LSW"})
    pa = pb = 0
    for seed in range(seeds):
        rnd = random.Random(2000 + seed)
        seq = synth(inst, key, rnd, N)
        seq = [rnd.choice(tags) if rnd.random() < err else s for s in seq]
        ra, rb = inst.stats(seq, key)
        nul = [inst.stats(seq, make_null(key, rnd)) for _ in range(shuf)]
        na = sorted(x[0] for x in nul); nb = sorted(x[1] for x in nul)
        qa, qb = J.pct(na, .99), J.pct(nb, .99)
        pa += ra > qa; pb += rb > qb
        print(f"seed {seed}: (a) real {ra:.3f} p99 {qa:.3f} {'P' if ra>qa else 'F'} | (b) real {rb:.3f} p99 {qb:.3f} mean {statistics.mean(nb):.3f} {'P' if rb>qb else 'F'}", flush=True)
    print(f"ERR={err} N={N}: (a) {pa}/{seeds}  (b) {pb}/{seeds}")
if __name__ == "__main__": main()
