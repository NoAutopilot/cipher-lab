#!/usr/bin/env python3
"""H335 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), script-only, written before running: a gloss-free held-leaf check of key v7 in the
secretary's hand. fr.3983 f.106r rows 1-12, pooled reconciled sign draft (passes/recf106rall/ciphertext_draft.tsv, every draft row, H332). Each
line is split into runs of consecutive signs whose class has a v7 cell (build_key_v7.load_key_v7, EBR_A -> form A, EBR_B -> form B, H325's cell());
any other sign (PLAIN, DASH, OTHER, unkeyed class) breaks a run; runs under 4 signs are dropped. Each run is resolved by the fr16 4-gram beam of
scripts/f61beam_margin.py (width 400, lp from scripts/f61hash4_108r); the score is the summed 4-gram log10 over all runs divided by the letters
scored. Controls on the same runs: (b) 200 binned-permuted keys (v7's cells permuted within bins of 3 classes adjacent in f.106r token rank, seed
3350; H329's design) and (c) the frequency-only key (top-k fr16 letters, k = the class's v7 cell size). Pre-stated as H329: 'consistent with key v7
on a held leaf in f.61's hand' iff real > (b) p95 AND real > (c); else 'no signal beyond frequency'. Limits: the beam chooses within cells, so larger
cells score higher (the binned control carries the cell sizes along); sign-pass agreement is 0.85 / 0.76 (rows 1-6 / 7-12). No reading, no merge.
python3 h335_106r_v7_beam.py [--check]"""
import csv, gzip, glob, os, random, sys, unicodedata
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{HERE}/../../.."); P = f"{HERE}/passes"
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
sys.path.insert(0, HERE); sys.path.insert(0, f"{HERE}/../scripts")
import build_key_v7 as b
import f61hash4_108r as H
lp = H.lp
KB, KA = b.load_key_v7(ebr="B"), b.load_key_v7(ebr="A")
def cell(c): return set(KA["EBR"]) if c == "EBR_A" else set(KB["EBR"]) if c == "EBR_B" else set(KB.get(c, ()))
rd = lambda f: list(csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t"))
rows = rd(f"{P}/recf106rall/ciphertext_draft.tsv")
cnt = Counter(r["sign"] for r in rows)
classes = sorted({r["sign"] for r in rows if cell(r["sign"])}, key=lambda c: (-cnt[c], c))
runs = []; cur = []; last = None
for r in rows:
    if r["line"] != last or not cell(r["sign"]):
        if len(cur) >= 4: runs.append(cur)
        cur = []
    if cell(r["sign"]): cur.append(r["sign"])
    last = r["line"]
if len(cur) >= 4: runs.append(cur)
def best(sets):
    beam = [("", 0.0)]
    for st in sets:
        nb = {}
        for s, v in beam:
            for ch in st:
                t = s + ch; w = v + (lp(t[-4:]) if len(t) >= 4 else 0.0)
                if t[-3:] not in nb or nb[t[-3:]][1] < w: nb[t[-3:]] = (t, w)
        beam = sorted(nb.values(), key=lambda x: -x[1])[:400]
    return beam[0][1]
def score(cf):
    tot = n = 0.0
    for run in runs:
        sets = [tuple(sorted(cf(c))) for c in run]
        if any(not s for s in sets): continue
        tot += best(sets); n += len(run) - 3
    return tot / n
real = score(cell)
rng = random.Random(3350); bins = [classes[i:i + 3] for i in range(0, len(classes), 3)]; null = []
for _ in range(200):
    mp = {}
    for bn in bins:
        cs = [frozenset(cell(c)) for c in bn]; rng.shuffle(cs); mp.update(zip(bn, cs))
    null.append(score(lambda c: set(mp.get(c, ()))))
null.sort(); p95 = null[189]
fold = lambda w: unicodedata.normalize("NFKD", w).encode("ascii", "ignore").decode().lower().translate(str.maketrans("jvy", "iui"))
lf = Counter()
for f in glob.glob(f"{ROOT}/tools/data/fr16/*.txt.gz") + glob.glob(f"{ROOT}/tools/data/fr16/*.txt"):
    t = (gzip.open(f, "rt", errors="ignore") if f.endswith(".gz") else open(f, errors="ignore")).read(); lf.update(ch for ch in fold(t) if "a" <= ch <= "z")
order = [c for c, _ in lf.most_common()]; fsc = score(lambda c: set(order[:len(cell(c))]))
nsig = sum(len(r) for r in runs)
out = [f"draft rows {len(rows)}; keyed classes {len(classes)}: {' '.join(classes)}; runs >= 4 signs {len(runs)}, signs in them {nsig}",
       f"real (v7) {real:.4f} log10/letter; (b) binned mean {sum(null) / 200:.4f} p95 {p95:.4f} max {null[-1]:.4f}, >= real {sum(x >= real for x in null)}/200; (c) frequency key {fsc:.4f}",
       "read-out: " + ("consistent with key v7 on a held leaf in f.61's hand" if real > p95 and real > fsc else "no signal beyond frequency")]
txt = "\n".join(out) + "\n"; res = f"{HERE}/h335_106r_v7_beam_result.txt"
if "--check" in ARGS:
    ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
