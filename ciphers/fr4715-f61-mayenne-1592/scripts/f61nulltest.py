#!/usr/bin/env python3
"""Campaign step H49 (28 Sept 2026, runner session_01J8hunWPcE7QYcpCx59CUHV): F61-NULLTEST. Do the uncovered classes (CA,
LOOPBAR, LL, CROSS, ZHOOK) behave in the family's period alignments (family/key_period_v3.tsv: one row per class, letter,
leaf with its count; '-' = the aligner gave the sign no letter) like NULLS -- as Tomokiyo's dashes on f.61 say (H44) -- or
like polyphonic CELLS (two letters carrying most tokens, as every covered class does)?

Statistics per class, on its lettered tokens: top-2 share (the two commonest letters' share) and the normalised entropy;
plus the dash share on all tokens. Controls, subsampled to the rare class's OWN lettered token count n (rule 3, the
ARM3-ADJ lesson: a class separates at N=1000 says nothing about N=9): (a) every covered class with 30+ lettered tokens,
2000 multinomial draws of n tokens from its own letter distribution -- the CELL band; (b) a NULL model, 2000 draws of n
tokens from the pooled letter distribution of all lettered tokens of the covered classes (what a sign that takes a
random neighbour's letter looks like under this aligner). Pre-registered verdict, per class with n >= 7: 'null-like' if
its top-2 share is below the 5th percentile of EVERY cell control's draws AND at or above the 5th percentile of the null
model's draws; 'cell-like' if above the null model's 95th percentile and inside every cell control's 5-95 band;
'untestable at this n' otherwise or when n < 7. Nothing here writes a key row: a 'null-like' verdict licenses only the
statement that the period alignments do not contradict Tomokiyo's dashes, at the stated n.

  python3 scripts/f61nulltest.py [--check]     (from the target folder)
"""
import csv, math, os, random, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); FAM = os.path.abspath(f"{HERE}/../family")
RARE = ["CA", "LOOPBAR", "LL", "CROSS", "ZHOOK"]; DRAWS = 2000; MINCTRL = 30
def stats(cnt):
    n = sum(cnt.values()); top2 = sum(k for _, k in cnt.most_common(2)) / n
    H = -sum(k / n * math.log(k / n) for k in cnt.values()); Hn = H / math.log(n) if n > 1 else 0.0
    return top2, Hn
def draw(rng, dist, n):
    letters, w = zip(*dist.items()); return Counter(rng.choices(letters, weights=w, k=n))
def main():
    rows = [r for r in csv.DictReader((l for l in open(f"{FAM}/key_period_v3.tsv") if not l.startswith("#")), delimiter="\t")]
    tot = defaultdict(Counter)
    for r in rows: tot[r["class"]][r["letter"]] += int(r["n"])
    lettered = {c: Counter({l: k for l, k in cnt.items() if l not in ("-", "") and len(l) == 1}) for c, cnt in tot.items()}
    covered = sorted(c for c in lettered if c not in RARE and c not in ("OTHER", "PLAIN", "DASH", "RSIGN") and sum(lettered[c].values()) >= MINCTRL)
    pooled = Counter()
    for c in covered: pooled.update(lettered[c])
    out = [f"H49 null test on family/key_period_v3.tsv: cell controls = {len(covered)} covered classes with >= {MINCTRL} lettered tokens ({' '.join(covered)}); null model = pooled letters of those classes; {DRAWS} draws each, seed 1"]
    out.append("covered classes at full N (top-2 share / normalised entropy / dash share): " + "; ".join(f"{c} {stats(lettered[c])[0]:.2f}/{stats(lettered[c])[1]:.2f}/{tot[c]['-']/sum(tot[c].values()):.2f}" for c in covered))
    rng = random.Random(1)
    for c in RARE:
        cnt = lettered.get(c, Counter()); n = sum(cnt.values()); N = sum(tot.get(c, Counter()).values()); dash = tot.get(c, Counter())["-"]
        line = f"{c}: N={N} (dash {dash}), lettered n={n}: " + " ".join(f"{l}:{k}" for l, k in cnt.most_common())
        if n < 7: out.append(line + " -> untestable at this n (< 7)"); continue
        t2, Hn = stats(cnt)
        null = sorted(stats(draw(rng, pooled, n))[0] for _ in range(DRAWS)); q = lambda a, p: a[int(p * (len(a) - 1))]
        cells = {cc: sorted(stats(draw(rng, lettered[cc], n))[0] for _ in range(DRAWS)) for cc in covered}
        below_all = all(t2 < q(cells[cc], 0.05) for cc in covered); inside_all = all(q(cells[cc], 0.05) <= t2 <= q(cells[cc], 0.95) for cc in covered)
        null_p = sum(1 for v in null if v >= t2) / DRAWS
        verdict = "null-like" if (below_all and t2 >= q(null, 0.05)) else ("cell-like" if (t2 > q(null, 0.95) and inside_all) else "untestable at this n")
        out.append(line + f"; top-2 share {t2:.2f}, entropy {Hn:.2f}, dash share {dash/N:.2f}")
        out.append(f"  null model at n={n}: top-2 p05 {q(null,0.05):.2f} median {q(null,0.5):.2f} p95 {q(null,0.95):.2f}; P(null >= {t2:.2f}) = {null_p:.3f}")
        out.append("  cell controls at n=%d (p05 / median): " % n + "; ".join(f"{cc} {q(cells[cc],0.05):.2f}/{q(cells[cc],0.5):.2f}" for cc in covered))
        out.append(f"  below every cell control's p05: {below_all}; inside every cell band: {inside_all} -> VERDICT {verdict}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/f61nulltest_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    main()
