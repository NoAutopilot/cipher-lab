#!/usr/bin/env python3
"""F61-FAMILY-10 (29 Sept 2026): key v6 = key v5 plus what VERIFY-F61-V7 endorsed and the part of VERIFY-F61-V6 it endorsed
(AUDIT.md sections VERIFY-F61-V6 and VERIFY-F61-V7; verify_v6/, verify_v7/).

Pooled key (every leaf), from V7 -- the hash family keyed by shape, not by pass code:
    HASH4 (the 4-head hash) = CELL d/q, grade C on f.101r / f.188r / f.274r (period decipherments). f.188r's HASH4 i 10 / x 3 rows
        (by blind shape 10 of 12 are the 2#) leave the HASH4 row and are written under H24; f.101r's HASH4 i 4 stays as stray support.
    H24 (the 2# sign) = CELL i/x (j/y are period spellings of i, folded), taking those two f.188r rows.
    HASHLOOP (the looped hash, most of f.106r's and f.108r's "HASH4") = a separate row, UNREAD, never pooled into HASH4.
f.61 reading only, from V6 (the bowl rule; NOT a pooled cell):
    4TRI c/p (t dropped) and f.61's single 4STEM token (L11) a/n, grade S (period value from fr.3984 f.176r / fol. 177r, linked by the
    blind bowl attribute). Written as F61READ rows, read only by load_key_v6(f61=True). f.61's one HASH4 (L01) reads d/q through the
    pooled cell, grade S on f.61 (linked by blind shape, V7).
Not merged (await VERIFY-F61-V8): ZHOOK = 2# (H235) and the 4PI split (H233-H240). ZHOOK and 4PI must load exactly as in v5.

Output family/key_period_v6.tsv (key_period_v5.tsv is never edited): every v5 line verbatim, except the two f.188r HASH4 i/x rows, kept
as '#moved-to-H24-v5' comment lines; then the moved H24 rows, the CELL rows, the HASHLOOP row and the F61READ rows.

Reproduction (from key_period_v6.tsv through load_key_v6): f.61 five known spans 53/55 (f.61 reading key) and f.108r overlay 74/84
(pooled key, EBR at the form-A set), 2000 permuted keys each (seed 20260929); the f.61 meter firm 12 / two-way 58 / wider 4 /
unread-or-null 25 of 99 (V7's "v5 + V6 + V7", from f61_decode_period_v4_frac0.1_sbs.tsv, C6 unread/null). load_key_v6 is also
checked to return exactly v5's sets (build_key_v5.load_key_v5) for every class this merge does not change.
Writes key_period_v6.tsv and build_key_v6_result.txt; exits non-zero on any mismatch.
  python3 build_key_v6.py [--check]   (--check: regenerate both in memory, fail if either committed file is stale)"""
import csv, os, random, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); S = os.path.abspath(f"{HERE}/../scripts")
sys.path.insert(0, HERE); sys.path.insert(0, S)
CHECK = "--check" in sys.argv
V5, V6 = f"{HERE}/key_period_v5.tsv", f"{HERE}/key_period_v6.tsv"
RES = f"{HERE}/build_key_v6_result.txt"
MIN, FRAC = 2, 0.1
FOLD = str.maketrans("jvy", "iui")
F188 = "fr.3984 f.188r/f.184r"
PERIOD_LEAVES = ("fr.3982 f.101r", F188, "fr.3984 f.274r")
V7 = "VERIFY-F61-V7 (setD 2# i/x 38/42, 4-head d/q 37/45, within-leaf p 5e-05; each leaf clears alone)"
V6A = "VERIFY-F61-V6 (f.176r bowl yes c/p 18/3, no 10/39, p 4e-7; f.61 shape = code at 14/14 positions)"
UNCHANGED = ("ZHOOK", "4PI", "4STEM", "4TRI", "C43")   # pooled sets that must equal v5's (4TRI/4STEM change on f.61 only)
def build():
    lines = open(V5).read().rstrip("\n").split("\n")
    hdr = next(l for l in lines if l.startswith("class\t")).split("\t")
    body, moved, hashcnt, h24cnt = [], [], Counter(), Counter()
    for l in lines:
        r = dict(zip(hdr, l.split("\t")))
        if not l.startswith("#") and l != "\t".join(hdr):
            if r["class"] == "HASH4" and r["leaf"] == F188 and r["letter"] in ("i", "x"):
                moved.append(r); body.append("#moved-to-H24-v5\t" + l); continue
            if r["class"] == "HASH4" and r["letter"] in ("d", "q"): hashcnt[(r["leaf"], r["letter"])] += int(r["n"])
            if r["class"] == "H24" and r["letter"] in ("i", "x"): h24cnt[(r["leaf"], r["letter"])] += int(r["n"])
        body.append(l)
    assert sorted((m["letter"], m["n"]) for m in moved) == [("i", "10"), ("x", "3")], moved
    head = ["# key_period_v6.tsv -- F61-FAMILY-10 (key v6), 29 Sept 2026: key_period_v5.tsv plus VERIFY-F61-V7 (endorse) and the endorsed part "
            "of VERIFY-F61-V6 (AUDIT.md). Built by build_key_v6.py; do not hand-edit.",
            "# Changed (pooled): HASH4 d/i/q -> CELL d/q (the 4-head); f.188r HASH4 i 10 / x 3 moved to H24 (the 2#); H24 -> CELL i/x; "
            "HASHLOOP (the looped hash) a separate UNREAD row, never pooled into HASH4.",
            "# Changed (f.61 reading only, F61READ rows, load_key_v6(f61=True)): 4TRI c/p, 4STEM a/n (L11), grade S. No pooled 4STEM a/n cell.",
            "# Not merged (await VERIFY-F61-V8): ZHOOK = 2# (H235), the 4PI split (H233-H240).",
            "# Key source: period (fr.3982 f.101r, fr.3984 f.188r, fr.3984 f.274r decipherments) for the hash cells; period (fr.3984 f.176r / fol. 177r) "
            "for the F61READ rows. v5 header follows:"]
    add = []
    for m in moved:
        add.append(f"H24\t{m['letter']}\t{m['n']}\t{F188}\tMOVED from HASH4 by shape, {V7}; f.188r HASH4-coded i/x rows are the 2# in 10 of 12 tiles; v5 bands {m['bands']}")
        h24cnt[(F188, m["letter"])] += int(m["n"])
    for L in "dq":
        for lf in PERIOD_LEAVES:
            if hashcnt[(lf, L)]: add.append(f"HASH4\t{L}\t{hashcnt[(lf, L)]}\t{lf}\tCELL d/q {V7}; the 4-head hash; grade C on this leaf")
    for L in "ix":
        for lf in PERIOD_LEAVES:
            if h24cnt[(lf, L)]: add.append(f"H24\t{L}\t{h24cnt[(lf, L)]}\t{lf}\tCELL i/x {V7}; the 2# sign (j/y = i, period spelling); grade C on this leaf")
    add.append("HASHLOOP\t-\t0\tfr.3984 f.106r; fr.3984 f.108r\tUNREAD: the looped hash (f.106r HASH4 looped 5/5 in V7 setD; most of f.108r's HASH4); "
               "no period value; a separate class, never pooled into HASH4's counts (VERIFY-F61-V7 caveat 3)")
    add.append(f"4TRI\tc\t5\tfr.4715 f.61r\tF61READ c/p {V6A}; bowl sign = 4TRI at all 5 f.61 positions, Tomokiyo c/p 5/5; grade S; f.61 reading only")
    add.append(f"4TRI\tp\t0\tfr.4715 f.61r\tF61READ c/p (cell partner; the 5 in the c row counts f.61 4TRI tokens Tomokiyo reads c or p)")
    add.append(f"4STEM\ta\t1\tfr.4715 f.61r\tF61READ a/n {V6A}; f.61's single 4STEM token (L11), no bowl; grade S; f.61 reading only, NOT a pooled cell "
               "(f.108v's 4STEM is the c/p sign by sequence: a code conflict between leaves, rule 4)")
    add.append(f"4STEM\tn\t0\tfr.4715 f.61r\tF61READ a/n (cell partner)")
    return "\n".join(head + body + add) + "\n"
def load_key_v6(path=V6, ebr="B", fold=True, f61=False):
    """Class -> sorted letter tuple, as build_key_v5.load_key_v5 (CELL rows give the set outright; other rows --min 2 --frac 0.1 per
    leaf; EBR form B for f.61, form A for f.108r). HASHLOOP ('-' only) never loads: unread. F61READ rows are skipped unless f61=True,
    when they replace the class's set for the f.61 reading (4TRI c/p, 4STEM a/n)."""
    rows = [r for r in csv.DictReader((l for l in open(path) if not l.startswith("#")), delimiter="\t")]
    tot = Counter(); key = defaultdict(set); cellset = defaultdict(set); f61set = defaultdict(set)
    for r in rows:
        if r["bands"].startswith("F61READ"): continue
        if r["letter"] not in ("-", ""): tot[(r["class"], r["leaf"])] += int(r["n"])
    for r in rows:
        if r["bands"].startswith("F61READ"): f61set[r["class"]].add(r["letter"]); continue
        if r["bands"].startswith("CELL"): cellset[r["class"]].add(r["letter"]); continue
        if r["letter"] in ("-", "") or r["class"] in ("PLAIN", "OTHER", "DASH") or int(r["n"]) < MIN: continue
        if int(r["n"]) < FRAC * tot[(r["class"], r["leaf"])]: continue
        key[r["class"]].add(r["letter"])
    for c, v in cellset.items(): key[c] = set(v)
    if f61:
        for c, v in f61set.items(): key[c] = set(v); cellset[c] = set(v)
    ebrB, ebrA = key.pop("EBR_B", set()), key.pop("EBR_A", set()) | key.pop("EBR", set())
    key["EBR"] = ebrB if ebr == "B" else ebrA
    cellc = set(cellset) | ({"EBR"} if ebr == "B" and "EBR_B" in cellset else set())
    f = (lambda c, s: s.translate(FOLD) if fold and c in cellc else s)
    return {c: tuple(sorted({f(c, x) for x in v})) for c, v in key.items() if v}
def repro(tsv):
    import tempfile
    tmp = tempfile.NamedTemporaryFile("w", suffix=".tsv", delete=False); tmp.write(tsv); tmp.close()
    from build_key_v5 import load_key_v5
    from f61crib import align, load_read, load_spans
    from f61crib4 import split_lines
    from f61joint import f108_lines
    from sbs_relabel import relabel
    out, bad = [], []
    k5, k5A, k5raw = load_key_v5(), load_key_v5(ebr="A"), load_key_v5(fold=False)
    k6, k6A, k6raw = load_key_v6(tmp.name), load_key_v6(tmp.name, ebr="A"), load_key_v6(tmp.name, fold=False)
    k6f, k6fraw = load_key_v6(tmp.name, f61=True), load_key_v6(tmp.name, f61=True, fold=False)
    os.unlink(tmp.name)
    out.append(f"v5 classes (build_key_v5.load_key_v5): {len(k5)}; v6 pooled classes: {len(k6)}; HASHLOOP loaded: {'HASHLOOP' in k6} (must be False: unread)")
    if set(k6) != set(k5) or "HASHLOOP" in k6: bad.append(f"class sets differ: {sorted(set(k5) ^ set(k6))}")
    ch = sorted(c for c in k6 if k5.get(c) != k6[c]); chA = sorted(c for c in k6A if k5A.get(c) != k6A[c])
    out.append("changed in v6 pooled (EBR form B): " + "; ".join(f"{c} {'/'.join(k5raw[c])} -> {'/'.join(k6raw[c])}" for c in ch))
    if ch != ["H24", "HASH4"] or chA != ["H24", "HASH4"]: bad.append(f"pooled changes {ch} / form A {chA} != [H24, HASH4]")
    if k6["HASH4"] != ("d", "q") or k6["H24"] != ("i", "x"): bad.append(f"HASH4 {k6['HASH4']} H24 {k6['H24']}")
    for c in UNCHANGED:
        if k5.get(c) != k6.get(c) or k5A.get(c) != k6A.get(c): bad.append(f"{c} moved in pooled key ({k5.get(c)} -> {k6.get(c)})")
    out.append("unchanged from v5 (checked, pooled): " + " ".join(f"{c}={'/'.join(k6[c])}" for c in UNCHANGED) + "; EBR form A = " + "/".join(k6A["EBR"]))
    chf = sorted(c for c in k6f if k6.get(c) != k6f[c])
    out.append("f.61 reading key over the pooled key: " + "; ".join(f"{c} {'/'.join(k6raw[c])} -> {'/'.join(k6fraw[c])}" for c in chf))
    if chf != ["4STEM", "4TRI"] or k6f["4TRI"] != ("c", "p") or k6f["4STEM"] != ("a", "n"): bad.append(f"f.61 reading changes {chf}")
    # meter (bands as meter_v5.py / meter_v7.py)
    def band(letters, cls):
        if cls == "C6" or letters in ("-", ""): return "unread/null"
        n = len(letters.split("/")); return "firm" if n == 1 else ("two-way" if n == 2 else "wider")
    NEW = {c: "/".join(k6fraw[c]) for c in set(chf) | set(ch) | {"VBAR_A", "EBR", "SBS", "ZHOOK"}}
    d = list(csv.DictReader(open(f"{HERE}/f61_decode_period_v4_frac0.1_sbs.tsv"), delimiter="\t"))
    c = Counter(band(NEW.get(r["class"], r["period_letters"]), r["class"]) for r in d)
    meter = (c["firm"], c["two-way"], c["wider"], c["unread/null"], len(d))
    out.append(f"f.61 meter under v6 (f.61 reading key): {len(d)} signs: firm {meter[0]} / two-way {meter[1]} / wider {meter[2]} / unread-or-null {meter[3]}")
    if meter != (12, 58, 4, 25, 99): bad.append(f"meter {meter} != (12, 58, 4, 25, 99)")
    wid = Counter(r["class"] + "=" + NEW.get(r["class"], r["period_letters"]) for r in d if band(NEW.get(r["class"], r["period_letters"]), r["class"]) == "wider")
    out.append("  still wider: " + " ".join(f"{k}:{v}" for k, v in sorted(wid.items())))
    tc = Counter((r["class"], r["period_letters"], NEW[r["class"]]) for r in d if r["class"] in NEW and r["period_letters"] != NEW[r["class"]])
    out.append("  tokens changed from the v4 decode: " + "; ".join(f"{k[0]} {k[1]} -> {k[2]} x{v}" for k, v in sorted(tc.items())))
    # known spans
    lines = split_lines(load_read()); lines.update(f108_lines()); relabel(lines)
    s61 = load_spans(); s108 = [(s, "F108_" + ("L02" if s == "T1" else "L03"), m) for s, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{S}/tomokiyo_spans_3983.tsv") if l[0] == "T")]
    def sc(key, spans):
        mt = tot = 0
        for s, l, m in spans:
            mm = m.translate(FOLD); mt += align(mm, lines[l], key)[0]; tot += sum(1 for ch_ in mm if ch_ != "-")
        return mt, tot
    for tag, spans, k, want in (("f.61 five spans, f.61 reading key", s61, k6f, (53, 55)), ("f.61 five spans, pooled key (info)", s61, k6, None),
                                ("f.108r overlay, pooled key (EBR form A)", s108, k6A, (74, 84))):
        mt, tot = sc(k, spans); labs = sorted(k); vals = [k[x] for x in labs]; rng = random.Random(20260929); cs = []
        for _ in range(2000):
            v = list(vals); rng.shuffle(v); cs.append(sc(dict(zip(labs, v)), spans)[0])
        cs.sort(); ge = sum(x >= mt for x in cs)
        out.append(f"{tag} (j=i, v=u, y=i folded): v6 {mt}/{tot} = {mt/tot:.3f}; 2000 permuted mean {sum(cs)/2000/tot:.3f} p95 {cs[1899]/tot:.3f} max {cs[-1]/tot:.3f}; >= key {ge}/2000")
        if want and (mt, tot) != want: bad.append(f"{tag} {mt}/{tot} != {want[0]}/{want[1]}")
    out.append("REPRODUCED: " + ("yes" if not bad else "NO -- " + "; ".join(bad)))
    return "\n".join(out) + "\n", bad
def main():
    tsv = build()
    if CHECK:
        if not os.path.exists(V6) or open(V6).read() != tsv: sys.exit("STALE key_period_v6.tsv")
    txt, bad = repro(tsv)
    if CHECK:
        if open(RES).read() != txt: sys.exit("STALE build_key_v6_result.txt")
        print("check OK")
    else:
        open(V6, "w").write(tsv); open(RES, "w").write(txt); print(txt, end="")
    if bad: sys.exit(1)
if __name__ == "__main__": main()
