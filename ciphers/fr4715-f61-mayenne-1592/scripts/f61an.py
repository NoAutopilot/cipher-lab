#!/usr/bin/env python3
"""F61-AN (campaign step H24, 28 Sept 2026, runner session_01J8hunWPcE7QYcpCx59CUHV): the table draws a and n as two distinct
symbols (keys/key_mayenne_1592.tsv rows 1-2: a lighter cross with a rising diagonal, n a heavier, blockier one) while the
readers' 4-shaped classes (C43, 4STEM, C6, LOOPBAR on f.61; C43/4STEM on f.108) all carry a AND n (H23: C43 a:8 n:6, no
split at the class level). Is the a/n cell two glyphs the atlas merges, as the V signs (H13-H15), the brackets (H22) and
the loops (H26) were?

Pre-registered before the call (prompt in scripts/PROMPTS.md, H24). Same design as scripts/f61qo.py: expected positions and
labels from disk -- every C43/4STEM/C6/LOOPBAR sign of the six span lines (passA_classes.tsv), of L10 (read_call_U.tsv)
and of f.108r bands L02/L03 (the reconciled draft); the letter under each sign is Tomokiyo's by the joint cell map's DP;
label a or n; anything else listed, never scored. Pairing per sheet in reading order; a sheet whose listed count differs
is dropped. Statistic: best group-to-letter match (groups -> {a, n}); null: exact over all label arrangements when
C(n, k) <= 200000, else 2000 permutations (seed 1), plus the 200-permutation p95. Gate (H24): observed above the
permutation p95 with p < 0.05. Reported whatever the gate: the group of every sign, so a pass names which shape is a and
which is n.

  python3 scripts/f61an.py expected
  python3 scripts/f61an.py score read_call_AN.tsv [--check]
"""
import csv, itertools, math, os, random, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from f61crib import load_read, load_spans, fit, align
from f61crib3 import load_cells, cell_map, values, OPTS
from f61crib4 import split_lines
from f61joint import f108_lines
SHEETS = ["f61sheetB_L01", "f61sheetB_L03", "f61sheetB_L05", "f61sheetB_L07", "f61sheetB_L08", "f61sheetB_L11", "f61sheetB_L10", "f108sheetB_L02", "f108sheetB_L03"]
CLS = ("C43", "4STEM", "C6", "LOOPBAR"); CELLS = ("a", "n")
def expected():
    lines = split_lines(load_read()); lines.update(f108_lines())
    u = {}
    for r in csv.DictReader((l for l in open(f"{HERE}/read_call_U.tsv") if not l.startswith("#")), delimiter="\t"):
        u.setdefault(r["line"], []).append(r["sign"])
    lines["L10"] = u["L10"]
    spans = load_spans() + [(s, "F108_" + ("L02" if s == "T1" else "L03"), m) for s, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{HERE}/tomokiyo_spans_3983.tsv") if l[0] == "T")]
    cm = values(cell_map(fit(spans, lines, "an", OPTS, keep_dashes=True), load_cells()))
    letter = {}
    for s, line, markup in spans:
        _, pairs = align(markup, lines[line], cm)
        for mi, sj in pairs:
            if markup[mi] != "-": letter[(line, sj)] = markup[mi]
    out = []
    for sheet in SHEETS:
        line = ("F108_" if sheet.startswith("f108") else "") + sheet.split("_")[1]
        for j, c in enumerate(lines.get(line, [])):
            if c in CLS:
                L = letter.get((line, j), "-"); lab = ("a" if L == "a" else ("n" if L == "n" else "-")) if c in ("C43", "4STEM") else "-"   # C6/LOOPBAR listed (the reader must count them) but never scored: their a/n counts are the DP's, not Tomokiyo's (class_diag: dashes)
                out.append((sheet, j + 1, c, L, lab))
    return out
def stat(groups, labels):
    gs = sorted(set(groups)); best = 0
    for lets in itertools.product(CELLS, repeat=len(gs)):
        m = dict(zip(gs, lets)); best = max(best, sum(1 for g, l in zip(groups, labels) if m[g] == l))
    return best
def score(path):
    exp = expected(); by_sheet = defaultdict(list)
    for e in exp: by_sheet[e[0]].append(e)
    rows = list(csv.DictReader((l for l in open(f"{HERE}/{path}") if not l.startswith("#")), delimiter="\t"))
    got = defaultdict(list)
    for r in rows: got[r["sheet"].replace(".jpg", "")].append(r)
    out = [f"{path}: {len(rows)} loop signs listed; expected {len(exp)} ({sum(1 for e in exp if e[4] != '-')} labelled)"]
    groups, labels = [], []; qo = []
    for sheet in SHEETS:
        g = sorted(got.get(sheet, []), key=lambda r: (int(r["segment"]), float(r["x_px"]))); e = by_sheet.get(sheet, [])
        if len(g) != len(e):
            out.append(f"  {sheet}: expected {len(e)}, listed {len(g)} -> NOT reconciled, dropped"); continue
        for r, ex in zip(g, e):
            out.append(f"  {sheet}/{ex[1]} {ex[2]}: group {r['group']} ({r.get('arrangement', '')}), letter {ex[3]} ({ex[4]})")
            if ex[4] != "-": groups.append(r["group"]); labels.append(ex[4])
    n = len(labels)
    if n < 5: out.append(f"scored {n} < 5: NON-TEST")
    else:
        obs = stat(groups, labels); k = labels.count("n")
        if math.comb(n, k) <= 200000:
            exact = [stat(groups, ["n" if i in c else "a" for i in range(n)]) for c in itertools.combinations(range(n), k)]
            p = sum(1 for e in exact if e >= obs) / len(exact); pnote = f"exact P(>=obs) = {p:.4f} over {len(exact)} arrangements"
        else:
            rng = random.Random(1); cnt = 0
            for _ in range(2000):
                l2 = list(labels); rng.shuffle(l2); cnt += stat(groups, l2) >= obs
            p = cnt / 2000; pnote = f"permutation P(>=obs) = {p:.4f} over 2000 (seed 1)"
        rng = random.Random(1); perm = []
        for _ in range(200):
            l2 = list(labels); rng.shuffle(l2); perm.append(stat(groups, l2))
        perm.sort(); p95 = perm[int(0.95 * 200) - 1]
        out.append(f"scored {n} (a {n - k}, n {k}); groups {len(set(groups))}; observed {obs}/{n}; {pnote}; permutation p95 {p95}/{n}")
        out.append(f"GATE H24: {'PASS' if obs > p95 and p < 0.05 else 'FAIL'}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/f61an_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    if sys.argv[1] == "expected":
        for e in expected(): print("\t".join(map(str, e)))
    else: score(sys.argv[2])
