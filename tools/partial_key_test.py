#!/usr/bin/env python3
"""partial_key_test.py: does a PARTIAL key (a few codes -> letters, e.g. one implied by a crib placement) carry
letter-ORDER structure beyond the unigram statistic it was selected by? (H31, 28 Sept 2026, spinelli-beinecke-c1515.)

Statistics over the whole sign-coded text under the key (unmapped codes are gaps; a pair or triple counts only when
every position in it is mapped):
  bigram  = mean log P(b | a) over adjacent mapped pairs under the corpus letter bigram model (add-0.5)
  trigram = mean log P(c | a b) over adjacent mapped triples
  kl      = KL(mapped-letter distribution || corpus letter distribution), in nats (0 = Italian-shaped)
Controls (CLAUDE.md rule 3): (1) --shuffles N shuffled KEYS: the same letters permuted over the same codes, so the
unigram total is unchanged and only the assignment of letters to codes varies -- the bigram/trigram statistics can
differ, kl can differ (the counts land on other letters); (2) --order-shuffles M with --crib and the crib_pattern
options: for each of M shuffled-ORDER copies of the text, the best crib placement chosen exactly as the real one
was (tools/crib_pattern.run) and its implied key scored the same way, so the real placement is compared with
placements selected the same way on text with no order structure. Reported: the real values, each control's
mean / p95 / max and the real value's rank. A real bigram or trigram above the shuffled-key p95 says the key's
letter order is not what a random assignment of those letters gives; it never says the key is right (a candidate
anchor at most, rule 10). The tool never writes the words solved, new or first.

  python3 tools/partial_key_test.py --codes ciphers/<t>/passes/letter_codes_v4.tsv --group-col page \\
      --key SEVEN=a NINE=n ... [--corpus F ...] [--lang it] [--shuffles 200] [--seed 1] \\
      [--order-shuffles 50 --crib "..." --wild HOOK --skip A B --max-skip 6 --homophones]
Test: python3 tools/tests/test_partial_key_test.py (offline: a true key on a real Italian window scores above the
shuffled-key p95 on bigrams; a random key does not)."""
import argparse, math, os, random, sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import homophonic_anneal as ha  # noqa: E402
import crib_pattern as cp  # noqa: E402


class LM:
    def __init__(self, corpora, k=0.5):
        s = "".join(ha.fold(t) for t in corpora)
        self.uni = Counter(s); self.bi = Counter(s[i:i + 2] for i in range(len(s) - 1))
        self.tri = Counter(s[i:i + 3] for i in range(len(s) - 2))
        self.tot = sum(self.uni.values()); self.k = k; self.V = len(ha.ALPHA)
        self.freq = {a: (self.uni[a] + 0.5) / (self.tot + 0.5 * self.V) for a in ha.ALPHA}

    def lp_bi(self, a, b):
        return math.log((self.bi[a + b] + self.k) / (self.uni[a] + self.k * self.V))

    def lp_tri(self, a, b, c):
        return math.log((self.tri[a + b + c] + self.k) / (self.bi[a + b] + self.k * self.V))


def stats(groups, key, lm):
    bis, tris, cnt = [], [], Counter()
    for g in groups:
        m = [key.get(c) for c in g]
        for i, a in enumerate(m):
            if a:
                cnt[a] += 1
            if i >= 1 and m[i - 1] and a:
                bis.append(lm.lp_bi(m[i - 1], a))
            if i >= 2 and m[i - 2] and m[i - 1] and a:
                tris.append(lm.lp_tri(m[i - 2], m[i - 1], a))
    n = sum(cnt.values())
    kl = sum(c / n * math.log((c / n) / lm.freq[a]) for a, c in cnt.items()) if n else float("nan")
    return (sum(bis) / len(bis) if bis else float("nan"), len(bis),
            sum(tris) / len(tris) if tris else float("nan"), len(tris), kl, n)


def shuffled_keys(key, n, seed):
    rng = random.Random(seed)
    codes, letters = list(key), [key[c] for c in key]
    for _ in range(n):
        l2 = list(letters); rng.shuffle(l2)
        yield dict(zip(codes, l2))


def rank(real, vals, higher_better=True):
    if higher_better:
        return sum(1 for v in vals if v >= real)
    return sum(1 for v in vals if v <= real)


def summ(vals, pct):
    """mean, the pct quantile, and the extreme on the same side (max for a p95, min for a p05)."""
    vals = sorted(vals)
    return sum(vals) / len(vals), vals[min(len(vals) - 1, int(round(pct * (len(vals) - 1))))], (vals[-1] if pct >= 0.5 else vals[0])


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--codes", required=True); ap.add_argument("--group-col", default=None)
    ap.add_argument("--key", nargs="+", required=True, help="CODE=letter pairs")
    ap.add_argument("--corpus", nargs="*", default=None); ap.add_argument("--lang", default="it")
    ap.add_argument("--shuffles", type=int, default=200); ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--order-shuffles", type=int, default=0)
    ap.add_argument("--crib", default=None); ap.add_argument("--wild", nargs="*", default=[])
    ap.add_argument("--skip", nargs="*", default=[]); ap.add_argument("--max-skip", type=int, default=6)
    ap.add_argument("--homophones", action="store_true"); ap.add_argument("--max-err", type=int, default=0)
    a = ap.parse_args()
    import judge_plaintext as jp
    paths = a.corpus or [str(p) for p in jp.LANG_CORPORA[a.lang]]
    texts = [jp.read_corpus(p) for p in paths]
    lm = LM(texts)
    groups = cp.read_codes(a.codes, a.group_col)
    key = {}
    for kv in a.key:
        c, l = kv.split("="); key[c] = ha.fold(l)
    rb, nb, rt, nt, rkl, n = stats(groups, key, lm)
    print(f"REAL key ({len(key)} codes, {n} mapped tokens of {sum(len(g) for g in groups)}): "
          f"bigram {rb:.3f} over {nb} pairs, trigram {rt:.3f} over {nt} triples, KL from {a.lang} {rkl:.3f}")
    sb, st, skl = [], [], []
    for k2 in shuffled_keys(key, a.shuffles, a.seed):
        b, _, t, _, kl, _ = stats(groups, k2, lm); sb.append(b); st.append(t); skl.append(kl)
    for name, real, vals, hb in (("bigram", rb, sb, True), ("trigram", rt, st, True), ("KL", rkl, skl, False)):
        m, p, x = summ(vals, 0.95 if hb else 0.05)
        print(f"SHUFFLED-KEY control ({a.shuffles}): {name} mean {m:.3f} {'p95' if hb else 'p05'} {p:.3f} "
              f"{'max' if hb else 'min'} {x:.3f}; real {real:.3f} -- {rank(real, vals, hb)}/{a.shuffles} shuffles "
              f"{'at or above' if hb else 'at or below'}")
    if a.order_shuffles and a.crib:
        uni = cp.unigram(texts); crib = ha.fold(a.crib); rng = random.Random(a.seed + 77)
        ob, ot, okl, found = [], [], [], 0
        for _ in range(a.order_shuffles):
            sh = cp.shuffle_groups(groups, rng)
            res, _ = cp.run(sh, crib, set(a.wild), set(a.skip), a.max_skip, a.homophones, uni, a.max_err)
            if not res:
                continue
            found += 1
            b, _, t, _, kl, _ = stats(sh, res[0][3], lm); ob.append(b); ot.append(t); okl.append(kl)
        print(f"SHUFFLED-ORDER placements: {found}/{a.order_shuffles} copies had a placement; their best placement's key "
              f"scored on its own (shuffled) text:")
        if found:
            for name, real, vals, hb in (("bigram", rb, ob, True), ("trigram", rt, ot, True), ("KL", rkl, okl, False)):
                m, p, x = summ(vals, 0.95 if hb else 0.05)
                print(f"  {name} mean {m:.3f} {'p95' if hb else 'p05'} {p:.3f} {'max' if hb else 'min'} {x:.3f}; "
                      f"real {real:.3f} -- {rank(real, vals, hb)}/{found} {'at or above' if hb else 'at or below'}")


if __name__ == "__main__":
    main()
