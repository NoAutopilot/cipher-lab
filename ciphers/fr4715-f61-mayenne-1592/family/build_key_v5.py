#!/usr/bin/env python3
"""F61-FAMILY-9 (29 Sept 2026): key v5 = key v4 plus the four cells VERIFY-F61-V5 endorsed (AUDIT.md section VERIFY-F61-V5,
verify_v5/), taken from key_period_f176.tsv (H177, runner 6; fr.3984 f.176r / fol. 177r, Desportes's hand):
    VBAR_A g/t   EBR_B l/y (form-B brackets only)   SBS b/o   ZHOOK i/x (grade S on f.61)
Not merged (the verifier's "may not take"): 4STEM p/c, HASH4 d/q, BETA m/z, DBL o, 4PI p/c, CROSS s.
The runner's reader code DBL on f.176r is the side-by-side b/o glyph, i.e. key v4's SBS: its o/b rows are written under SBS, and no
f.176r row is ever written under DBL (v4's DBL, the stacked loops e/r/u, is untouched).
f.176r's EBR class is all form-B brackets (H180, 11/11), so its rows go under EBR_B; EBR_A and v4's unsplit EBR rows stay as they are.

Output family/key_period_v5.tsv (key_period_v4.tsv is never edited):
  * every v4 row of a class not changed here, verbatim;
  * v4's rows for VBAR_A, EBR_B, SBS, ZHOOK kept as '#superseded-v4' comment lines (provenance, ignored by every loader);
  * the endorsed cell rows: the f.176r counts of the two cell letters, bands 'CELL x/y VERIFY-F61-V5; f.176r code C; ...'.
    The fol. 177r clear is folded (h170_gate.fold: j->i, v->u, y->i), so EBR_B's y row carries the folded i/y count (n 10).
Cell rows ARE the class's letter set: they are exempt from the n >= 0.1 x leaf-total rule, which would cut a polyphonic cell's
partner letter (g 10 of 110, x 3 of 31, b 6 of 64) -- read the file with load_key_v5() here, not test_period_key.load_key.

Reproduction (VERIFY-F61-V5's numbers, from key_period_v5.tsv through load_key_v5): f.61 five known spans 53/55 and f.108r overlay
74/84 (EBR at the form-A set there), 2000 permuted keys each (seed 20260929); the f.61 meter firm 12 / two-way 50 / wider 12 /
unread-or-null 25 of 99 (from f61_decode_period_v4_frac0.1_sbs.tsv, C6 unread/null). load_key_v5 is also checked to return exactly
v4's sets (test_period_key.load_key, --collapse-ebr --min 2 --frac 0.1) for every class this merge does not change.
Writes key_period_v5.tsv and build_key_v5_result.txt; exits non-zero on any mismatch.
  python3 build_key_v5.py [--check]   (--check: regenerate both in memory, fail if either committed file is stale)"""
import csv, os, random, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); S = os.path.abspath(f"{HERE}/../scripts")
CHECK = "--check" in sys.argv
V4, F176, V5 = f"{HERE}/key_period_v4.tsv", f"{HERE}/key_period_f176.tsv", f"{HERE}/key_period_v5.tsv"
RES = f"{HERE}/build_key_v5_result.txt"
MIN, FRAC = 2, 0.1
FOLD = str.maketrans("jvy", "iui")
# target class in v5 -> (f.176r reader codes pooled into it, cell letters, f.176r letter for each cell letter, note)
ENDORSED = {
    "VBAR_A": (("VBAR_A",), "gt", {"g": "g", "t": "t"}, "cell 0.55 vs wrong text 0.20; f.108r t5 g2 7/7 p 0.005"),
    "EBR_B": (("EBR",), "ly", {"l": "l", "y": "i"}, "f.176r brackets form B (H180 11/11); y = folded i/y of the clear; cell 0.67 vs 0.18"),
    "SBS": (("SBS", "DBL"), "bo", {"b": "b", "o": "o"}, "reader code DBL on f.176r is v4's SBS glyph; cell 0.62 (SBS), 0.68 (DBL code)"),
    "ZHOOK": (("ZHOOK",), "ix", {"i": "i", "x": "x"}, "graded S on f.61 (letter agreement + f.108v gain, no glyph link); cell 0.53 vs 0.23"),
}
FORBIDDEN = ("4STEM", "HASH4", "BETA", "DBL", "4PI", "CROSS")   # verifier's "may not take": rows must equal v4's
def rows_of(path):
    head, rows = [], []
    for l in open(path):
        (head if l.startswith("#") else rows).append(l.rstrip("\n"))
    hdr = rows[0].split("\t"); return head, hdr, [dict(zip(hdr, r.split("\t"))) for r in rows[1:] if r]
def build():
    h4, hdr, v4 = rows_of(V4); _, _, f176 = rows_of(F176)
    cnt = defaultdict(Counter)
    for r in f176: cnt[r["class"]][r["letter"]] += int(r["n"])
    out = ["# key_period_v5.tsv -- F61-FAMILY-9 (key v5), 29 Sept 2026: key_period_v4.tsv plus the four cells VERIFY-F61-V5 endorsed "
           "(AUDIT.md), from key_period_f176.tsv (fr.3984 f.176r / fol. 177r). Built by build_key_v5.py; do not hand-edit.",
           "# Changed: VBAR_A s/t -> g/t; EBR_B -> l/y (form-B brackets only; EBR_A and unsplit EBR untouched); SBS b/e/o -> b/o "
           "(f.176r reader code DBL written as SBS, nothing merged into DBL); ZHOOK (unread) -> i/x (grade S on f.61).",
           "# Not merged: 4STEM p/c (conflict with f.108r), HASH4 d/q (leaf's own i share), BETA m/z (n too small), DBL o (reader code), 4PI p/c, CROSS s.",
           "# CELL rows are the class's whole letter set (exempt from the 0.1 x leaf-total rule); read with build_key_v5.load_key_v5.",
           "# Key source: period (fr.3984 f.176r/fol. 177r) for the CELL rows; v4's own sources for the rest. v4 header follows:"]
    out += h4 + ["\t".join(hdr)]
    sup, cells = [], []
    for r in v4:
        line = "\t".join(r[k] for k in hdr)
        (sup.append("#superseded-v4\t" + line) if r["class"] in ENDORSED else out.append(line))
    for tgt, (codes, cell, src, note) in ENDORSED.items():
        assert tgt != "DBL"
        for L in cell:
            for code in codes:
                n = cnt[code][src[L]]
                if n: cells.append(f"{tgt}\t{L}\t{n}\tfr.3984 f.176r/f.177r\tCELL {cell[0]}/{cell[1]} VERIFY-F61-V5; f.176r code {code}"
                                   f"{' (letter ' + src[L] + ' in the folded clear)' if src[L] != L else ''}; {note}")
    return "\n".join(out + sup + cells) + "\n"
def load_key_v5(path=V5, ebr="B", fold=True):
    """Class -> sorted letter tuple, as test_period_key.load_key with --collapse-ebr --min 2 --frac 0.1, except CELL rows give the set
    outright. ebr='B': f.61's unsplit EBR (all form B) = EBR_B's cell; ebr='A': EBR = EBR_A + unsplit EBR rows (form-A brackets,
    f.108r). fold: j->i, v->u, y->i on the CELL letters, as the known-span scoring folds Tomokiyo's letters (v4's sets as v4 has them)."""
    rows = [r for r in csv.DictReader((l for l in open(path) if not l.startswith("#")), delimiter="\t")]
    tot = Counter(); key = defaultdict(set); cellset = defaultdict(set)
    for r in rows:
        if r["letter"] not in ("-", ""): tot[(r["class"], r["leaf"])] += int(r["n"])
    for r in rows:
        if r["bands"].startswith("CELL"): cellset[r["class"]].add(r["letter"]); continue
        if r["letter"] in ("-", "") or r["class"] in ("PLAIN", "OTHER", "DASH") or int(r["n"]) < MIN: continue
        if int(r["n"]) < FRAC * tot[(r["class"], r["leaf"])]: continue
        key[r["class"]].add(r["letter"])
    for c, v in cellset.items(): key[c] = set(v)
    ebrB, ebrA = key.pop("EBR_B", set()), key.pop("EBR_A", set()) | key.pop("EBR", set())
    key["EBR"] = ebrB if ebr == "B" else ebrA
    cellc = set(cellset) | ({"EBR"} if ebr == "B" and "EBR_B" in cellset else set())
    f = (lambda c, s: s.translate(FOLD) if fold and c in cellc else s)   # fold the cell letters only (l/y -> i/l), as VERIFY-F61-V5 did
    return {c: tuple(sorted({f(c, x) for x in v})) for c, v in key.items() if v}
def repro():
    sys.argv = [sys.argv[0], "--key", V4, "--collapse-ebr", "--min", "2", "--frac", "0.1", "--sbs"]
    sys.path.insert(0, HERE); sys.path.insert(0, S)
    import test_period_key as T
    from f61crib import align, load_read, load_spans
    from f61crib4 import split_lines
    from f61joint import f108_lines
    from sbs_relabel import relabel
    out, bad = [], []
    key4 = T.load_key(); k5 = load_key_v5(); k5A = load_key_v5(ebr="A"); k5raw = load_key_v5(fold=False)
    if set(k5) != set(key4) | {"ZHOOK"}: bad.append(f"class sets differ beyond ZHOOK: {sorted(set(key4) ^ set(k5))}")
    changed = sorted(c for c in k5 if key4.get(c) != k5[c])
    same_A = sorted(c for c in k5A if c != "EBR" and key4.get(c) != k5A[c]) + ([] if key4["EBR"] == k5A["EBR"] else ["EBR(form A)"])
    out.append("v4 classes (test_period_key.load_key, --collapse-ebr --min 2 --frac 0.1): " + str(len(key4)) + "; v5 classes: " + str(len(k5)))
    out.append("changed in v5 (f.61, EBR form B): " + "; ".join(f"{c} {'/'.join(key4.get(c, ('unread',)))} -> {'/'.join(k5raw[c])}" for c in changed))
    if changed != ["EBR", "SBS", "VBAR_A", "ZHOOK"]: bad.append(f"changed classes {changed} != the four endorsed")
    if same_A != ["SBS", "VBAR_A", "ZHOOK"]: bad.append(f"form-A load differs from v4 outside the three non-EBR cells: {same_A}")
    for c in FORBIDDEN:
        if key4.get(c) != k5.get(c): bad.append(f"{c} moved ({key4.get(c)} -> {k5.get(c)})")
    out.append("unchanged from v4 (checked): " + " ".join(f"{c}={'/'.join(key4[c])}" for c in FORBIDDEN if c in key4) + "; EBR on form A (f.108r) = " + "/".join(k5A["EBR"]))
    # meter
    NEW = {c: "/".join(k5raw[c]) for c in changed}
    def band(letters, cls):
        if cls == "C6" or letters in ("-", ""): return "unread/null"
        n = len(letters.split("/")); return "firm" if n == 1 else ("two-way" if n == 2 else "wider")
    d = list(csv.DictReader(open(f"{HERE}/f61_decode_period_v4_frac0.1_sbs.tsv"), delimiter="\t"))
    c = Counter(band(NEW.get(r["class"], r["period_letters"]), r["class"]) for r in d)
    meter = (c["firm"], c["two-way"], c["wider"], c["unread/null"], len(d))
    out.append(f"f.61 meter under v5: {len(d)} signs: firm {meter[0]} / two-way {meter[1]} / wider {meter[2]} / unread-or-null {meter[3]}")
    if meter != (12, 50, 12, 25, 99): bad.append(f"meter {meter} != (12, 50, 12, 25, 99)")
    ch = Counter((r["class"], r["period_letters"], NEW[r["class"]]) for r in d if r["class"] in NEW)
    out.append("tokens changed: " + "; ".join(f"{k[0]} {k[1]} -> {k[2]} x{v}" for k, v in sorted(ch.items())))
    # known spans
    lines = split_lines(load_read()); lines.update(f108_lines()); relabel(lines)
    s61 = load_spans(); s108 = [(s, "F108_" + ("L02" if s == "T1" else "L03"), m) for s, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{S}/tomokiyo_spans_3983.tsv") if l[0] == "T")]
    def sc(key, spans):
        mt = tot = 0
        for s, l, m in spans:
            mm = m.translate(FOLD); mt += align(mm, lines[l], key)[0]; tot += sum(1 for ch_ in mm if ch_ != "-")
        return mt, tot
    for tag, spans, k, want in (("f.61 five spans", s61, k5, (53, 55)), ("f.108r overlay (EBR form A)", s108, k5A, (74, 84))):
        mt, tot = sc(k, spans); labs = sorted(k); vals = [k[x] for x in labs]; rng = random.Random(20260929); cs = []
        for _ in range(2000):
            v = list(vals); rng.shuffle(v); cs.append(sc(dict(zip(labs, v)), spans)[0])
        cs.sort(); ge = sum(x >= mt for x in cs)
        out.append(f"{tag} (j=i, v=u, y=i folded): v5 {mt}/{tot} = {mt/tot:.3f}; 2000 permuted mean {sum(cs)/2000/tot:.3f} p95 {cs[1899]/tot:.3f} max {cs[-1]/tot:.3f}; >= key {ge}/2000")
        if (mt, tot) != want: bad.append(f"{tag} {mt}/{tot} != {want[0]}/{want[1]}")
    out.append("REPRODUCED: " + ("yes" if not bad else "NO -- " + "; ".join(bad)))
    return "\n".join(out) + "\n", bad
def main():
    tsv = build()
    if CHECK:
        if open(V5).read() != tsv: sys.exit("STALE key_period_v5.tsv")
    else: open(V5, "w").write(tsv)
    txt, bad = repro()
    if CHECK:
        if open(RES).read() != txt: sys.exit("STALE build_key_v5_result.txt")
    else: open(RES, "w").write(txt); print(txt, end="")
    if bad: sys.exit(1)
if __name__ == "__main__": main()
