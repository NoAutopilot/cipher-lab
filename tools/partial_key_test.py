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
shuffled-key p95 on bigrams; a random key does not).
POLYPHONIC ORDER MODE (--cells, H354, fr4715-f61-mayenne-1592 runner 13, 29 Sept 2026): does a polyphonic key (each sign class
-> a small letter SET) carry letter-order structure on a sign draft? Runs of >= --min-run consecutive keyed signs per line
(any unkeyed sign breaks a run) are resolved by a 4-gram beam (tools/judge_plaintext.NgramModel, --lang, --width); the
statistic is the ORDER GAIN = beam log10/letter in real order minus its mean over --within within-run shuffles (each run's
signs permuted in place, so run cuts and each run's multiset are fixed and letter frequency cannot score). Control: the
same gain under --keys binned-permuted keys (cells permuted within bins of 3 classes adjacent in the draft's token rank).
--shuffle-target S repeats the whole test on S whole-draft sign shuffles (rule 3's ARM-C1 control: a real signal must
vanish there). Lesson recorded with it: a plain beam score against within-bin permuted keys is NOT an order control --
it passed on shuffled drafts in 4 of 7 leaves (H341). Report only; never a reading.
  python3 tools/partial_key_test.py --cells cells.tsv --draft ciphertext_draft.tsv [--lang fr] [--keys 100] [--within 10]
      [--width 400] [--min-run 4] [--seed 342] [--key-seed 3420] [--shuffle-target 0]
  cells.tsv: 'class<TAB>letters' with letters as a/b/c; draft: TSV with line, position (or pos) and sign columns.
Test: python3 tools/tests/test_partial_key_test_cells.py (offline: a true pair-cell key on a French text shows an order
gain above the binned p95; the same text shuffled does not)."""
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



# ---- polyphonic order mode (--cells), H354 ----
def _cells_load(path):
    out = {}
    for line in open(path):
        if not line.strip() or line.startswith("#") or line.startswith("class\t"): continue
        c, l = line.rstrip("\n").split("\t")[:2]; out[c] = frozenset(x for x in l.split("/") if x)
    return out
def _draft_load(path):
    import csv as _csv
    rows = [r for r in _csv.DictReader((l for l in open(path) if not l.startswith("#")), delimiter="\t")]
    return [(r["line"], r["sign"]) for r in rows]
def order_runs(draft, cells, min_run=4):
    runs, cur, last = [], [], None
    for line, s in draft:
        if line != last or s not in cells:
            if len(cur) >= min_run: runs.append(cur)
            cur = []
        if s in cells: cur.append(s)
        last = line
    if len(cur) >= min_run: runs.append(cur)
    return runs
def make_lp(lang):
    import judge_plaintext as jp
    M = jp.NgramModel([jp.read_corpus(p) for p in jp.LANG_CORPORA[lang]])
    return lambda g: math.log10((M.c.get(g, 0) + M.k) / (M.ctx.get(g[:-1], 0) + 26 * M.k))
def beam_best(sets, lp, width=400):
    beam = [("", 0.0)]
    for st in sets:
        nb = {}
        for s, v in beam:
            for ch in st:
                t_ = s + ch; w = v + (lp(t_[-4:]) if len(t_) >= 4 else 0.0)
                if t_[-3:] not in nb or nb[t_[-3:]][1] < w: nb[t_[-3:]] = (t_, w)
        beam = sorted(nb.values(), key=lambda x: -x[1])[:width]
    return beam[0][1]
def order_score(runs, cf, lp, width=400):
    tot = n = 0.0
    for run in runs:
        sets = [tuple(sorted(cf(c))) for c in run]
        if any(not s for s in sets): continue
        tot += beam_best(sets, lp, width); n += len(run) - 3
    return tot / n if n else float("nan")
def order_gain_test(draft, cells, lp, keys=100, within=10, width=400, min_run=4, seed=342, key_seed=3420):
    runs = order_runs(draft, cells, min_run)
    cnt = Counter(s for _, s in draft)
    classes = sorted({s for _, s in draft if s in cells}, key=lambda c: (-cnt[c], c))
    rng = random.Random(seed); shuf = []
    for _ in range(within):
        s = []
        for r in runs: r2 = r[:]; rng.shuffle(r2); s.append(r2)
        shuf.append(s)
    def gain(cf):
        real = order_score(runs, cf, lp, width)
        return real - sum(order_score(s, cf, lp, width) for s in shuf) / len(shuf)
    cf0 = lambda c: cells.get(c, ())
    gv = gain(cf0); bins = [classes[i:i + 3] for i in range(0, len(classes), 3)]; rk = random.Random(key_seed); null = []
    for _ in range(keys):
        mp = {}
        for bn in bins:
            cs = [cells[c] for c in bn]; rk.shuffle(cs); mp.update(zip(bn, cs))
        null.append(gain(lambda c, mp=mp: mp.get(c, ())))
    null.sort(); p95 = null[max(0, int(round(0.95 * keys)) - 1)]
    return {"runs": len(runs), "signs": sum(len(r) for r in runs), "gain": gv, "p95": p95, "mean": sum(null) / len(null),
            "ge": sum(x >= gv for x in null), "keys": keys, "signal": gv > p95}
def cells_main(argv):
    ap = argparse.ArgumentParser(description="partial_key_test.py polyphonic order mode (see the module docstring)")
    ap.add_argument("--cells", required=True); ap.add_argument("--draft", required=True); ap.add_argument("--lang", default="fr")
    ap.add_argument("--keys", type=int, default=100); ap.add_argument("--within", type=int, default=10)
    ap.add_argument("--width", type=int, default=400); ap.add_argument("--min-run", type=int, default=4)
    ap.add_argument("--seed", type=int, default=342); ap.add_argument("--key-seed", type=int, default=3420)
    ap.add_argument("--shuffle-target", type=int, default=0)
    a = ap.parse_args(argv)
    cells, draft, lp = _cells_load(a.cells), _draft_load(a.draft), make_lp(a.lang)
    kw = dict(keys=a.keys, within=a.within, width=a.width, min_run=a.min_run, seed=a.seed, key_seed=a.key_seed)
    r = order_gain_test(draft, cells, lp, **kw)
    print(f"real draft: runs {r['runs']}, signs {r['signs']}; order gain {r['gain']:.4f}; binned keys mean {r['mean']:.4f} p95 {r['p95']:.4f}, >= real {r['ge']}/{r['keys']} -> {'order signal' if r['signal'] else 'no order signal'}")
    hits = 0
    for k in range(a.shuffle_target):
        sg = [s for _, s in draft]; random.Random(a.seed * 1000 + k).shuffle(sg)
        rs = order_gain_test([(l, s) for (l, _), s in zip(draft, sg)], cells, lp, **kw); hits += rs["signal"]
        print(f"shuffled target {k + 1}: order gain {rs['gain']:.4f} vs p95 {rs['p95']:.4f} -> {'order signal' if rs['signal'] else 'no order signal'}")
    if a.shuffle_target:
        print(f"ARM-C1: order signal on {hits}/{a.shuffle_target} shuffled targets -> {'the real-draft result is VOID' if hits else 'control clean'}")

if __name__ == "__main__":
    if "--cells" in sys.argv: cells_main(sys.argv[1:]); sys.exit(0)
    main()
