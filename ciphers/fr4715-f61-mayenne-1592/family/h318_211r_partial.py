#!/usr/bin/env python3
"""H318 + H320 (runner 12 session_012eShPsWwW3quuzzUNV7nW5, 29 Sept 2026), script-only, written before running.
H320: for the 18 signs of fr.3983 f.211r's cipher run (H315: family/passes/f211r_rec/ciphertext_draft.tsv, x from f211r_passA/B.tsv averaged),
which classes key v7 (family/key_period_v7.tsv via build_key_v7.load_key_v7, pooled) gives a cell. Atlas EBR_A is read with v7's EBR form A
(a/l/s), EBR_B with form B (i/l) -- an assumption stated here; VBAR_A/VBAR_B, SBS, DBL, HASH4, 4STEM map by name; OTHER has no cell.
H318: under each gloss slot both H316 readers placed (forb- 470-975, comm- 1320-1700, elle 2105-2350, v-l 2590-2800; agreed letters only: f o r b /
c o m m / e l l e / v l, v folded to u), the signs whose x falls inside the slot; score = the largest number of the slot's letters that can be matched
one-to-one to distinct signs whose cell holds the letter (order-free, bipartite), summed over slots. Control: 1000 keys with v7's cells permuted
across the classes (each class keeps a cell of some other class; seed 318), the same signs and letters. Pre-stated: descriptive at this N;
'consistent with key v7' iff real > the shuffled p95; below it 'no signal at this N'. Grade: the gloss letters are M (two model reads, H316 FAIL), so
nothing here is C and nothing is a reading; ASKS 93 stays open.  python3 h318_211r_partial.py [--check]"""
import csv, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.argv, _argv = sys.argv[:1], sys.argv
import build_key_v7 as b
sys.argv = _argv
KB, KA = b.load_key_v7(ebr="B"), b.load_key_v7(ebr="A")
def cell(c):
    if c == "EBR_A": return set(KA["EBR"])
    if c == "EBR_B": return set(KB["EBR"])
    return set(KB.get(c, ()))
rd = lambda f: list(csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t"))
dr = rd(f"{HERE}/passes/f211r_rec/ciphertext_draft.tsv"); xa = rd(f"{HERE}/passes/f211r_passA.tsv"); xb = rd(f"{HERE}/passes/f211r_passB.tsv")
signs = [(int((int(a["x_sheet"]) + int(bb["x_sheet"])) / 2), r["sign"], r["alt"]) for r, a, bb in zip(dr, xa, xb)]
out = ["H320 cell coverage (key v7 pooled): " + " ".join(f"{s}{'/' + a if a else ''}={''.join(sorted(cell(s))) or '-'}" for _, s, a in signs)]
unread = [s for _, s, _ in signs if not cell(s)]
out.append(f"signs with a v7 cell {len(signs) - len(unread)}/{len(signs)}; no cell: {' '.join(unread) or 'none'}")
SLOTS = [("forb-", 470, 975, "forb"), ("comm-", 1320, 1700, "comm"), ("elle", 2105, 2350, "elle"), ("v-l", 2590, 2800, "ul")]
def match(letters, cells):
    m = {}
    def aug(i, seen):
        for j, c in enumerate(cells):
            if letters[i] in c and j not in seen:
                seen.add(j)
                if j not in m or aug(m[j], seen): m[j] = i; return True
        return False
    return sum(aug(i, set()) for i in range(len(letters)))
def score(cf):
    tot = 0; per = []
    for name, x0, x1, let in SLOTS:
        cs = [cf(s) for x, s, _ in signs if x0 <= x <= x1]; k = match(list(let), cs); tot += k; per.append(f"{name}: {k}/{len(let)} over {len(cs)} signs")
    return tot, per
real, per = score(cell)
classes = sorted({s for _, s, _ in signs if cell(s)}); pool = [frozenset(cell(c)) for c in classes]
rng = random.Random(318); null = []
for _ in range(1000):
    p = pool[:]; rng.shuffle(p); mp = dict(zip(classes, p)); null.append(score(lambda s: set(mp.get(s, ())))[0])
null.sort(); p95 = null[949]; mean = sum(null) / len(null)
out += ["H318 slots: " + "; ".join(per), f"real {real} of {sum(len(l) for *_, l in SLOTS)} letters; shuffled mean {mean:.2f}, p95 {p95}, max {null[-1]}; >= real {sum(n >= real for n in null)}/1000",
        "read-out: " + ("consistent with key v7 (real > shuffled p95), descriptive at this N" if real > p95 else "no signal at this N (real <= shuffled p95)")]
txt = "\n".join(out) + "\n"; res = f"{HERE}/h318_211r_partial_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
