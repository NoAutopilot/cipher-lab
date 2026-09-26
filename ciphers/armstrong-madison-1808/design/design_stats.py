#!/usr/bin/env python3
"""ARM-DESIGN (26 Sept 2026, LANE ARM, Fable): what kind of code is the 20 Feb 1808 letter in?

Plaintext-free statistics computed first on siblings of KNOWN design (controls), then on the target.
Designs simulated by encoding en18 text (tools/data/en18) under a code table:
  onepart    WE028's own 1600-entry vocabulary, one alphabetical run 1..1600 (a one-part code)
  twopart    the same vocabulary, values randomly permuted (a two-part / sequential-numbered code)
  blockwise  WE028 as published (letter blocks of 40-100 entries at scrambled positions, alphabetical inside)
  the972     THE=972 as far as published (Bourdeau's 580 entries; heavy syllable spelling) -- a partial table
  hdec       H-DEC: 180 roots at 100,110,...,1890, units digit = inflection (0 base,1 -s,2 -ed,3 -ing,4 -ly,5 -er,...),
             block 1-99 = 26 letters + 73 particles (spelling of out-of-vocabulary words by letters)
  hhom       H-HOM: 180 words at the same decades, units digit = a homophone chosen with a lazy-writer preference
             w_d ~ 1/(d+1)  (hhom_flat: uniform choice), block 1-99 as hdec
Real usage controls: THE=972 in Armstrong's own four other 1808 letters (tools/data/uscodes-1800/stats.py).
Every statistic is one that CAN differ between the designs for the manipulation compared (CLAUDE.md rule 3).
Offline; stdlib only.  python3 design_stats.py [--sims 60] [--seed 1] [--out DIR]
"""
import argparse, gzip, math, random, re, sys, importlib.util
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
US = REPO / "tools/data/uscodes-1800"
EN18 = REPO / "tools/data/en18"
TARGET = HERE.parent / "ciphertext.txt"
SUFFIXES = ["s", "ed", "ing", "ly", "er", "es", "d", "est", "ment"]  # digits 1..9 under H-DEC


def load_table(path):
    t = {}
    for line in open(path, encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        if len(p) < 2 or p[0] == "value":
            continue
        try:
            v = int(p[0])
        except ValueError:
            continue
        w = p[1].strip().lower()
        if w:
            t[v] = w
    return t


def target_tokens():
    toks = []
    for line in open(TARGET, encoding="utf-8"):
        if line.startswith("#"):
            continue
        for tk in line.split():
            if tk.isdigit():
                toks.append(int(tk))
    return toks


def usage_instances():
    spec = importlib.util.spec_from_file_location("ustats", US / "stats.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return {k: [int(x) for x in v.split()] for k, v in m.THE972_USAGE.items()}


def en18_words():
    words = []
    for p in sorted(EN18.glob("*.txt.gz")):
        t = gzip.open(p, "rt", encoding="utf-8", errors="replace").read().lower()
        ws = re.findall(r"[a-z]+", t)
        n = len(ws)
        words.append(ws[int(n * 0.1):int(n * 0.9)])  # drop front/back matter
    return words


# ---------------- encoders ----------------
class TableCode:
    """Encode words under a value->unit table: whole word if present, else greedy longest-prefix spelling
    with the table's own syllables/letters; a word that cannot be spelled is skipped."""
    def __init__(self, table):
        self.enc = defaultdict(list)
        for v, w in table.items():
            self.enc[re.sub(r"[^a-z]", "", w)].append(v)
        self.enc.pop("", None)
        self.maxlen = max(len(k) for k in self.enc)

    def encode(self, words, rng, homophone_pref=None):
        out = []
        for w in words:
            if w in self.enc:
                out.append(self.pick(self.enc[w], rng)); continue
            if getattr(self, "enc_only", False):
                self.drops += 1; continue
            i, seq, ok = 0, [], True
            while i < len(w):
                for L in range(min(self.maxlen, len(w) - i), 0, -1):
                    if w[i:i + L] in self.enc:
                        seq.append(self.pick(self.enc[w[i:i + L]], rng)); i += L; break
                else:
                    ok = False; break
            if ok:
                out.extend(seq)
        return out

    @staticmethod
    def pick(vals, rng):
        return vals[0] if len(vals) == 1 else rng.choice(vals)


class DecadeCode:
    """Block 1-99 = the 99 commonest function words; decades 100..1890 = 180 roots (lemmas). A word the code
    does not hold is DROPPED (modelling the letter's graphic-symbol passages as its out-of-vocabulary route),
    not letter-spelled; the drop count per letter is reported (target: 35 short passages + 2 lines)."""
    def __init__(self, roots, particles, mode, rng, extra=None):
        self.mode = mode
        self.low = {p: i + 1 for i, p in enumerate(particles[:99])}
        self.root = {r: 100 + 10 * i for i, r in enumerate(roots[:180])}
        self.drops = 0
        if mode == "hinsert":  # gapped numbering: later additions fill units 1,2,3.. of a random decade
            fill = defaultdict(int)
            for w in extra:
                d = rng.randrange(180)
                if fill[d] < 9:
                    fill[d] += 1; self.root[w] = 100 + 10 * d + fill[d]

    def encode(self, words, rng, **kw):
        out = []
        for w in words:
            if w in self.low:
                out.append(self.low[w]); continue
            if self.mode in ("hdec", "hinsert"):
                hit = None
                if w in self.root:
                    hit = self.root[w]
                else:
                    for d, suf in enumerate(SUFFIXES, 1):
                        if w.endswith(suf) and len(w) > len(suf) + 1:
                            st = w[:-len(suf)]
                            if st in self.root:
                                hit = self.root[st] + d; break
                            if st + "e" in self.root:
                                hit = self.root[st + "e"] + d; break
                if hit is not None:
                    out.append(hit); continue
                if self.mode == "hinsert" and w in self.root:
                    out.append(self.root[w]); continue
            else:
                if w in self.root:
                    if self.mode == "hhom_flat":
                        d = rng.randrange(10)
                    else:
                        d = rng.choices(range(10), weights=[1 / (k + 1) for k in range(10)])[0]
                    out.append(self.root[w] + d); continue
            self.drops += 1
        return out


# ---------------- statistics ----------------
def entropy(counts):
    n = sum(counts)
    return -sum(c / n * math.log2(c / n) for c in counts if c)


def jsd(p, q):
    def kl(a, b):
        return sum(x * math.log2(x / y) for x, y in zip(a, b) if x > 0 and y > 0)
    m = [(x + y) / 2 for x, y in zip(p, q)]
    return 0.5 * kl(p, m) + 0.5 * kl(q, m)


def stats(toks, rng, vmax=None):
    N = len(toks); D = len(set(toks)); vmax = vmax or max(toks)
    hi = [v for v in toks if v >= 100]; lo = [v for v in toks if v < 100]
    s = {"N": N, "D": D, "D/N": D / N, "low_share": len(lo) / N, "low_distinct": len(set(lo)),
         "hi_distinct": len(set(hi))}
    # units digit among values >= 100 (tokens): concentration and entropy
    dc = Counter(v % 10 for v in hi)
    prof = sorted(dc.values(), reverse=True) + [0] * 10
    s["units_top1"] = prof[0] / max(1, len(hi)); s["units_top2"] = (prof[0] + prof[1]) / max(1, len(hi))
    s["units_H"] = entropy(list(dc.values()))
    s["units_digit0_share"] = dc[0] / max(1, len(hi))
    # decade variants among distinct values >= 100
    dec = defaultdict(set)
    for v in set(hi):
        dec[v // 10].add(v)
    s["decades_occupied"] = len(dec)
    s["decade_multi_frac"] = sum(1 for d in dec.values() if len(d) >= 2) / max(1, len(dec))
    s["variants_per_decade"] = len(set(hi)) / max(1, len(dec))
    # decade x units dependence (H-DEC: word-specific digit; H-HOM: digit independent of decade)
    # statistic: mean modal-digit share over decades with >= 3 tokens, minus its permutation null (digits shuffled among hi tokens)
    def modal(hv):
        by = defaultdict(list)
        for v in hv:
            by[v // 10].append(v % 10)
        rows = [max(Counter(ds).values()) / len(ds) for ds in by.values() if len(ds) >= 3]
        return (sum(rows) / len(rows), len(rows)) if rows else (float("nan"), 0)
    real, nrows = modal(hi)
    null = []
    digs = [v % 10 for v in hi]; decs = [v // 10 for v in hi]
    for _ in range(200):
        rng.shuffle(digs)
        null.append(modal([10 * a + b for a, b in zip(decs, digs)])[0])
    null = [x for x in null if x == x]
    mu = sum(null) / len(null) if null else float("nan")
    sd = (sum((x - mu) ** 2 for x in null) / len(null)) ** 0.5 if null else float("nan")
    s["decade_units_modal"] = real; s["decade_units_null"] = mu
    s["decade_units_z"] = (real - mu) / sd if sd and sd == sd and sd > 0 else float("nan")
    s["decade_units_rows"] = nrows
    # hundred-block trough (tokens), blocks from 100 to the block holding vmax
    bc = Counter(v // 100 for v in hi)
    blocks = [bc.get(b, 0) for b in range(1, vmax // 100 + 1)]
    med = sorted(blocks)[len(blocks) // 2]
    s["block_min"] = min(blocks); s["block_median"] = med
    s["block_trough"] = min(blocks) / med if med else float("nan")
    # pair-of-adjacent-blocks minimum (the target's 900-1099 shape)
    s["block_pair_min"] = min(a + b for a, b in zip(blocks, blocks[1:])) if len(blocks) > 1 else min(blocks)
    # frequency-position divergence: token-weighted vs distinct-weighted 19-bin histogram over 1..vmax
    nb = 19
    def hist(vals):
        h = [0] * nb
        for v in vals:
            h[min(nb - 1, (v - 1) * nb // vmax)] += 1
        n = sum(h); return [x / n for x in h]
    s["freqpos_jsd"] = jsd(hist(toks), hist(set(toks)))
    # top-frequency mass concentration: share of tokens carried by the top-10 values
    top = Counter(toks).most_common(10)
    s["top10_share"] = sum(c for _, c in top) / N
    # top-10 values' spread: their positions (0..1) in the range -- one-part puts them in the t/o/a/i slices
    pos = sorted(v / vmax for v, _ in top)
    s["top10_pos_sd"] = (sum((p - sum(pos) / len(pos)) ** 2 for p in pos) / len(pos)) ** 0.5
    # one-part signature: the k-th most frequent token should sit at the alphabetical position of the k-th most
    # frequent word of the language (en18 top-8: the of to and in a that be -> t o t a i a t b); mean |pos - alpha|
    alpha = [0.80, 0.58, 0.80, 0.02, 0.36, 0.02, 0.80, 0.06]
    top8 = [v for v, _ in Counter(toks).most_common(8)]
    s["onepart_dist"] = sum(abs(v / vmax - a) for v, a in zip(top8, alpha)) / len(top8)
    # units digits 1..9 (values >= 100): are they used in order (1 > 2 > 3 ..., insertion numbering) or as fixed
    # slots with arbitrary popularity (an inflection/homophone map)? Spearman rho of digit vs its count
    d19 = [dc.get(d, 0) for d in range(1, 10)]
    rk = {d: r for r, d in enumerate(sorted(range(9), key=lambda i: -d19[i]))}
    n9 = 9; s["digit_order_rho"] = 1 - 6 * sum((i - rk[i]) ** 2 for i in range(9)) / (n9 * (n9 * n9 - 1))
    # digits 2,3 vs 4,6,7 (the target's own shape): share of non-zero-digit tokens on digits 2+3
    nz = sum(d19); s["digits23_share"] = (d19[1] + d19[2]) / nz if nz else float("nan")
    # successive value gap (order-dependent): median |delta| real vs shuffled-order
    gaps = sorted(abs(a - b) for a, b in zip(toks, toks[1:]))
    sh = toks[:]; rng.shuffle(sh)
    gsh = sorted(abs(a - b) for a, b in zip(sh, sh[1:]))
    s["gap_median"] = gaps[len(gaps) // 2]; s["gap_median_shuffled"] = gsh[len(gsh) // 2]
    s["gap_small_frac"] = sum(1 for g in gaps if g <= 10) / len(gaps)
    s["gap_small_frac_shuffled"] = sum(1 for g in gsh if g <= 10) / len(gsh)
    return s


KEYS = ["N", "D", "D/N", "low_share", "low_distinct", "hi_distinct", "units_top1", "units_top2", "units_H",
        "units_digit0_share", "decades_occupied", "decade_multi_frac", "variants_per_decade",
        "decade_units_modal", "decade_units_null", "decade_units_z", "block_trough", "block_pair_min",
        "freqpos_jsd", "onepart_dist", "digit_order_rho", "digits23_share", "top10_share", "top10_pos_sd", "gap_median", "gap_median_shuffled", "gap_small_frac",
        "gap_small_frac_shuffled"]


def fmt(x):
    return f"{x:.3f}" if isinstance(x, float) else str(x)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sims", type=int, default=60)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--n", type=int, default=369)
    ap.add_argument("--out", default=str(HERE))
    a = ap.parse_args()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    rng = random.Random(a.seed)

    we028 = load_table(US / "WE028.tsv"); the972 = load_table(US / "THE972_bourdeau.tsv")
    # --- table layout (needs plaintext; controls only) ---
    lay = open(out / "table_layout.txt", "w", encoding="utf-8")
    for name, t in [("WE028", we028), ("THE972_bourdeau", the972)]:
        vals = sorted(t); runs = [[vals[0]]]
        for x, y in zip(vals, vals[1:]):
            (runs[-1].append(y) if t[y] >= t[x] else runs.append([y]))
        L = sorted((len(r) for r in runs), reverse=True)
        print(f"{name}: {len(vals)} entries, {len(runs)} maximal ascending runs, longest {L[:8]}, "
              f"median {L[len(L)//2]}, runs>=20: {sum(1 for x in L if x >= 20)} covering "
              f"{sum(x for x in L if x >= 20)} entries", file=lay)
        for b in range(0, max(vals) + 1, 100):
            print(f"  {b:5d}: " + "".join(t[v][0] for v in vals if b <= v < b + 100), file=lay)
    lay.close()

    corp = en18_words()
    allw = Counter(w for f in corp for w in f)
    particles = [w for w, _ in allw.most_common(400)][:99]
    stopset = set(particles)
    top3k = {w for w, _ in allw.most_common(4000)}
    def lemma(w):
        for suf in SUFFIXES:
            if w.endswith(suf) and len(w) > len(suf) + 2:
                st = w[:-len(suf)]
                if st in top3k: return st
                if st + "e" in top3k: return st + "e"
        return w
    lem = Counter()
    for w, n in allw.most_common(6000):
        if w not in stopset and len(w) > 2:
            lem[lemma(w)] += n
    roots = [w for w, _ in lem.most_common(180)]
    extra = [w for w, _ in lem.most_common(800) if w not in roots][:450]

    def sample_words(r, n_words):
        f = r.choice(corp); i = r.randrange(0, len(f) - n_words)
        return f[i:i + n_words]

    designs = {}
    vocab_vals = sorted(we028); vocab_words = [we028[v] for v in vocab_vals]
    designs["blockwise_WE028"] = lambda r: TableCode(we028)
    designs["onepart"] = lambda r: TableCode(dict(zip(vocab_vals, sorted(vocab_words))))
    def twopart(r):
        vv = vocab_vals[:]; r.shuffle(vv); return TableCode(dict(zip(vv, vocab_words)))
    designs["twopart"] = twopart
    designs["the972_partial"] = lambda r: TableCode(the972)
    designs["hdec"] = lambda r: DecadeCode(roots, particles, "hdec", r)
    designs["hhom_lazy"] = lambda r: DecadeCode(roots, particles, "hhom", r)
    designs["hhom_flat"] = lambda r: DecadeCode(roots, particles, "hhom_flat", r)
    designs["hinsert"] = lambda r: DecadeCode(roots, particles, "hinsert", r, extra=extra)
    # H-SEQ: particle block 1-99 + the 1800 commonest content forms numbered 100..1899 in random order
    content = [w for w, _ in allw.most_common(3000) if w not in stopset][:1800]
    def seq_pblock(r):
        vv = list(range(100, 1900)); r.shuffle(vv)
        t = {i + 1: p for i, p in enumerate(particles[:99])}; t.update(dict(zip(vv, content)))
        c = TableCode(t); c.drops = 0; c.enc_only = True; return c
    designs["seq_pblock"] = seq_pblock
    drops = defaultdict(list)

    rows = []  # (dataset, kind, stats)
    tgt = target_tokens()
    rows.append(("TARGET armstrong-madison-1808", "target", stats(tgt, random.Random(7), 1900)))
    for k, v in usage_instances().items():
        rows.append((f"REAL THE972 usage {k}", "real", stats(v, random.Random(7), 1600)))
    pooled = [x for v in usage_instances().values() for x in v]
    rows.append(("REAL THE972 usage pooled", "real", stats(pooled, random.Random(7), 1600)))
    sims = defaultdict(list)
    for name, mk in designs.items():
        for i in range(a.sims):
            r = random.Random(a.seed * 1000 + i)
            code = mk(r)
            toks = []
            while len(toks) < a.n:
                if hasattr(code, "drops"): code.drops = 0
                toks = code.encode(sample_words(r, a.n * 2), r)[:a.n]
            if hasattr(code, "drops"):
                drops[name].append(code.drops)
            vmax = 1900 if name in ("hdec", "hhom_lazy", "hhom_flat") else 1600
            sims[name].append(stats(toks, random.Random(i), vmax))
    with open(out / "sim_tokens_example.tsv", "w") as f:
        for name, mk in designs.items():
            r = random.Random(a.seed * 1000); code = mk(r)
            f.write(name + "\t" + " ".join(map(str, code.encode(sample_words(r, 300), r)[:120])) + "\n")

    # --- write tables ---
    with open(out / "stats_real.tsv", "w") as f:
        f.write("dataset\t" + "\t".join(KEYS) + "\n")
        for name, _, s in rows:
            f.write(name + "\t" + "\t".join(fmt(s[k]) for k in KEYS) + "\n")
    with open(out / "stats_sim.tsv", "w") as f:
        f.write("design\tstat\tmean\tsd\tp05\tp50\tp95\ttarget\ttarget_percentile\n")
        T = rows[0][2]
        for name, lst in sims.items():
            for k in KEYS:
                xs = sorted(s[k] for s in lst if s[k] == s[k])
                if not xs:
                    continue
                mu = sum(xs) / len(xs); sd = (sum((x - mu) ** 2 for x in xs) / len(xs)) ** 0.5
                q = lambda p: xs[min(len(xs) - 1, int(p * len(xs)))]
                tv = T[k]
                pct = 100 * sum(1 for x in xs if x < tv) / len(xs) + 50 * sum(1 for x in xs if x == tv) / len(xs)
                f.write(f"{name}\t{k}\t{mu:.3f}\t{sd:.3f}\t{fmt(q(.05))}\t{fmt(q(.5))}\t{fmt(q(.95))}\t{fmt(tv)}\t{pct:.0f}\n")
    # console summary
    print("design/dataset".ljust(30), " ".join(k[:11].rjust(11) for k in KEYS[2:]))
    for name, _, s in rows:
        print(name[:30].ljust(30), " ".join(fmt(s[k])[:11].rjust(11) for k in KEYS[2:]))
    for name, lst in sims.items():
        mu = {k: sum(s[k] for s in lst if s[k] == s[k]) / max(1, sum(1 for s in lst if s[k] == s[k])) for k in KEYS}
        print(("SIM " + name)[:30].ljust(30), " ".join(fmt(mu[k])[:11].rjust(11) for k in KEYS[2:]))
    for name, ds in drops.items():
        print(f"OOV drops per {a.n}-token letter under {name}: mean {sum(ds)/len(ds):.1f} (target: 35 short + 2 line passages)")
    # Zipf K estimate: K such that E[D] matches, for tokens drawn Zipf(s) over K entries
    def expD(K, N, sexp):
        p = [1 / (k ** sexp) for k in range(1, K + 1)]; z = sum(p)
        return sum(1 - (1 - x / z) ** N for x in p)
    T = rows[0][2]
    for label, N, D in [("all", T["N"], T["D"]), ("hi>=100", 237, 168), ("low<100", 132, 48)]:
        for sexp in (1.0, 1.2):
            K, best = None, None
            for k in range(20, 5000, 5):
                e = expD(k, N, sexp)
                if best is None or abs(e - D) < best: best, K = abs(e - D), k
            print(f"Zipf K estimate {label}: N={N} D={D} s={sexp}: K~{K} (E[D]={expD(K, N, sexp):.1f})")
    # K from vocabulary coverage: the target codes 237 tokens >= 100 and writes ~37 passages in shorthand, so its
    # above-100 vocabulary covers about 237/(237+37) = 86.5% of content tokens (if every passage is one OOV word;
    # the two full lines make the true share lower). Coverage of en18 content tokens by the top-K lemmas / forms:
    ctoks = [w for f in corp for w in f if w not in stopset]
    ctot = len(ctoks); lemc = Counter(lemma(w) for w in ctoks); formc = Counter(ctoks)
    print("content-token coverage of en18 by top-K entries (lemmas | inflected forms):")
    for K in (180, 300, 500, 800, 1000, 1200, 1500, 1800, 2500):
        cl = sum(n for _, n in lemc.most_common(K)) / ctot; cf = sum(n for _, n in formc.most_common(K)) / ctot
        print(f"  K={K:5d}: lemmas {cl:.3f}  forms {cf:.3f}")
    # distinct content words in 237 en18 content tokens (what a full-vocabulary code would show above 100)
    rr = random.Random(5); ds = []
    for _ in range(200):
        i = rr.randrange(len(ctoks) - 237); ds.append(len(set(ctoks[i:i + 237])))
    ds.sort(); print(f"en18: distinct content words in 237 content tokens: mean {sum(ds)/len(ds):.1f}, p05 {ds[10]}, p95 {ds[189]} (target hi: 168 distinct in 237)")
    print("vocab sizes: WE028", len(we028), "THE972", len(the972), "roots", len(roots), "particles", len(particles),
          "en18 words", sum(allw.values()))


if __name__ == "__main__":
    main()
