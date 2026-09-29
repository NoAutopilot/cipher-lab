#!/usr/bin/env python3
"""F61-FAMILY-11 (29 Sept 2026): key v7 = key v6 plus exactly what VERIFY-F61-V8 endorsed (AUDIT.md section VERIFY-F61-V8, its "Meter"
and "What should merge" lists; verify_v8/).

1. ZHOOK: value unchanged (CELL i/x); its note now records the glyph link "the 2# sign = H24 cell, glyph link VERIFY-F61-V8", grade S,
   replacing v5/v6's "no glyph link".
2. 4PI (the 4-head) = CELL d/q, grade C on f.101r / f.188r (period decipherments); f.108r's 4PI reads d/q through it.
3. f.61's 4-over-Pi is a SEPARATE class, 4PIPI, f.61 reading only (F61TOK rows, per token): L11 9 reads a/n at grade M from
   Tomokiyo S5's n alone; L01 12 stays unread (outside the published spans, no source).
4. The pooled 4PI row is split before any further pooling: f.188r's 4-with-r-tail rows (a 5, n 1, e 1, h 1, r 1; V8 "Finding for the
   key") leave 4PI and are written as class 4PIR with a HELD note, never loaded (no value endorsed; "might be C43 miscoded", untested).
Not merged: H240 as proposed (both f.61 4PI a/n) -- not endorsed by V8 (L01 12 has no source). Nothing else changes.

Output family/key_period_v7.tsv (key_period_v6.tsv is never edited): every v6 line verbatim, except the ZHOOK rows and the f.188r
4PI r-tail rows, kept as '#replaced-v6' / '#moved-to-4PIR-v6' comment lines; then the new ZHOOK, 4PI CELL, 4PIR and 4PIPI rows.

Reproduction (from key_period_v7.tsv through load_key_v7): f.61 five known spans 53/55 (f.61 reading key, f.61's 4PI tokens relabelled
by f61_relabel) and f.108r overlay 74/84 (pooled key, EBR form A), 2000 permuted keys each (seed 20260929); V8's meter
(verify_v8/meter_v8.py bands, from f61_decode_period_v4_frac0.1_sbs.tsv): "both cells as endorsed" (f.61's two 4PI held unread)
firm 12 / two-way 58 / wider 2 / unread-or-null 27 of 99, and key v7 as merged (L11 9 a/n grade M, L01 12 unread) 12 / 59 / 2 / 26
(V8's variant added after scoring). load_key_v7 is also checked to return exactly v6's sets for every class this merge does not change.
Writes key_period_v7.tsv and build_key_v7_result.txt; exits non-zero on any mismatch.
  python3 build_key_v7.py [--check]   (--check: regenerate both in memory, fail if either committed file is stale)"""
import csv, os, random, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); S = os.path.abspath(f"{HERE}/../scripts")
sys.path.insert(0, HERE); sys.path.insert(0, S)
CHECK = "--check" in sys.argv
V6, V7 = f"{HERE}/key_period_v6.tsv", f"{HERE}/key_period_v7.tsv"
RES = f"{HERE}/build_key_v7_result.txt"
MIN, FRAC = 2, 0.1
FOLD = str.maketrans("jvy", "iui")
F188, F101 = "fr.3984 f.188r/f.184r", "fr.3982 f.101r"
RTAIL = ("a", "n", "e", "h", "r")       # f.188r 4PI rows of the 4-with-r-tail form (V8: a 5, n 1, and the e/h/r strays)
V8 = "VERIFY-F61-V8"
V8Z = f"{V8} (setF and setG: ZHOOK -> 2# 10/10, f.61 3/3, f.108r 7/7; in-hand distractors 0/27; within-leaf p 5e-05; gate 20/21 each)"
V8P = f"{V8} (setF and setG: period 4PI rows lettered d/q -> 4-head 12/12; f.108r 4PI 9/9)"
F61TOK = {("L11", 9): ("a", "n"), ("L01", 12): ()}   # f.61's 4-over-Pi tokens: value per token (empty = unread)
UNCHANGED = ("ZHOOK", "HASH4", "H24", "4STEM", "4TRI", "C43", "EBR", "SBS", "VBAR_A")   # pooled sets that must equal v6's
def build():
    lines = open(V6).read().rstrip("\n").split("\n")
    hdr = next(l for l in lines if l.startswith("class\t")).split("\t")
    body, zh, rt, picnt = [], [], [], Counter()
    for l in lines:
        r = dict(zip(hdr, l.split("\t")))
        if not l.startswith("#") and l != "\t".join(hdr):
            if r["class"] == "ZHOOK":
                zh.append(r); body.append("#replaced-v6\t" + l); continue
            if r["class"] == "4PI" and r["leaf"] == F188 and r["letter"] in RTAIL:
                rt.append(r); body.append("#moved-to-4PIR-v6\t" + l); continue
            if r["class"] == "4PI" and r["letter"] in ("d", "q"): picnt[(r["leaf"], r["letter"])] += int(r["n"])
        body.append(l)
    assert sorted((z["letter"], z["n"]) for z in zh) == [("i", "28"), ("x", "3")], zh
    assert sorted((m["letter"], m["n"]) for m in rt) == [("a", "5"), ("e", "1"), ("h", "1"), ("n", "1"), ("r", "1")], rt
    assert dict(picnt) == {(F101, "d"): 5, (F101, "q"): 2, (F188, "d"): 9, (F188, "q"): 2}, picnt
    head = ["# key_period_v7.tsv -- F61-FAMILY-11 (key v7), 29 Sept 2026: key_period_v6.tsv plus what VERIFY-F61-V8 endorsed (AUDIT.md, "
            "'What should merge' 1-4). Built by build_key_v7.py; do not hand-edit.",
            "# Changed (pooled): ZHOOK note only (value i/x unchanged; glyph link to the 2#/H24 cell, grade S); 4PI a/d/n/q -> CELL d/q "
            "(the 4-head); f.188r 4PI r-tail rows (a 5, n 1, e, h, r) split off as 4PIR, HELD, never loaded.",
            "# Changed (f.61 reading only, F61TOK rows, per token): f.61's 4-over-Pi is its own class 4PIPI: L11 9 a/n grade M "
            "(Tomokiyo S5 alone), L01 12 unread.",
            "# Not merged: H240 as proposed (both f.61 4PI a/n), not endorsed by VERIFY-F61-V8.",
            "# Key source: period (fr.3982 f.101r, fr.3984 f.188r decipherments) for 4PI d/q; period (H24 cell, f.101r/f.188r/f.274r) linked "
            "by blind shape for ZHOOK; published (Tomokiyo S5, credited) for 4PIPI L11 9. v6 header follows:"]
    add = []
    for z in zh:
        add.append(f"ZHOOK\t{z['letter']}\t{z['n']}\t{z['leaf']}\tCELL i/x (value unchanged from v5/v6); f.176r code ZHOOK; the 2# sign = H24 cell, "
                   f"glyph link {V8Z}; grade S on f.61 (period value from other hands, linked by blind shape); replaces 'no glyph link'")
    for L in "dq":
        for lf in (F101, F188):
            add.append(f"4PI\t{L}\t{picnt[(lf, L)]}\t{lf}\tCELL d/q {V8P}; the 4-head; grade C on this leaf; f.108r's 4PI reads d/q through this cell")
    for m in rt:
        add.append(f"4PIR\t{m['letter']}\t{m['n']}\t{F188}\tHELD: the 4-with-r-tail form (V8 'Finding for the key'; setF 'E 4r-like', setG 'N 4 + r-like tail'), "
                   f"split from 4PI before any further pooling; no value endorsed, may be C43 miscoded (untested); never loaded; v6 bands {m['bands']}")
    add.append(f"4PIPI\ta\t0\tfr.4715 f.61r\tF61TOK L11 9 a/n grade M: f.61's 4-over-Pi (a separate sign from the 4-head, {V8} P2: setF/setG E,E "
               "'4 over Pi'); value from Tomokiyo S5's n alone, no period glyph (V8 E<->a/n read-out failed); f.61 reading only")
    add.append("4PIPI\tn\t1\tfr.4715 f.61r\tF61TOK L11 9 a/n (cell partner; the 1 is Tomokiyo S5's n at L11 9)")
    add.append("4PIPI\t-\t0\tfr.4715 f.61r\tF61TOK L01 12 UNREAD: outside the published spans, no source (H240's a/n here is not endorsed)")
    return "\n".join(head + body + add) + "\n"
def load_key_v7(path=V7, ebr="B", fold=True, f61=False):
    """Class -> sorted letter tuple, as build_key_v6.load_key_v6 (CELL rows give the set outright; other rows --min 2 --frac 0.1 per
    leaf; EBR form B for f.61, form A for f.108r; F61READ rows only with f61=True). HASHLOOP and 4PIR (HELD) never load. F61TOK rows
    (4PIPI) load only with f61=True, as class 4PIPI = the L11 9 value; use f61_relabel on the f.61 lines so that only L11 9 carries
    the 4PIPI label and L01 12 carries 4PIPI_UNREAD (no key entry)."""
    rows = [r for r in csv.DictReader((l for l in open(path) if not l.startswith("#")), delimiter="\t")]
    tot = Counter(); key = defaultdict(set); cellset = defaultdict(set); f61set = defaultdict(set)
    skip = lambda r: r["bands"].startswith(("F61READ", "F61TOK", "HELD"))
    for r in rows:
        if skip(r): continue
        if r["letter"] not in ("-", ""): tot[(r["class"], r["leaf"])] += int(r["n"])
    for r in rows:
        if r["bands"].startswith("HELD"): continue
        if r["bands"].startswith(("F61READ", "F61TOK")):
            if r["letter"] not in ("-", ""): f61set[r["class"]].add(r["letter"])
            continue
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
def f61_relabel(lines):
    """f.61's two 4PI tokens are the 4-over-Pi (V8 P2), not the 4-head: L11 9 -> 4PIPI (read a/n, grade M), L01 12 -> 4PIPI_UNREAD."""
    for (l, p), v in F61TOK.items():
        assert lines[l][p - 1] == "4PI", (l, p, lines[l][p - 1])
        lines[l][p - 1] = "4PIPI" if v else "4PIPI_UNREAD"
    assert not any(c == "4PI" for k, v in lines.items() if not k.startswith("F108_") for c in v)
    return lines
def repro(tsv):
    import tempfile
    tmp = tempfile.NamedTemporaryFile("w", suffix=".tsv", delete=False); tmp.write(tsv); tmp.close()
    from build_key_v6 import load_key_v6
    from f61crib import align, load_read, load_spans
    from f61crib4 import split_lines
    from f61joint import f108_lines
    from sbs_relabel import relabel
    out, bad = [], []
    k6, k6A, k6raw, k6f = load_key_v6(), load_key_v6(ebr="A"), load_key_v6(fold=False), load_key_v6(f61=True)
    k7, k7A, k7raw = load_key_v7(tmp.name), load_key_v7(tmp.name, ebr="A"), load_key_v7(tmp.name, fold=False)
    k7f, k7fraw = load_key_v7(tmp.name, f61=True), load_key_v7(tmp.name, f61=True, fold=False)
    os.unlink(tmp.name)
    out.append(f"v6 pooled classes (build_key_v6.load_key_v6): {len(k6)}; v7 pooled classes: {len(k7)}; loaded 4PIR/HASHLOOP/4PIPI: "
               f"{sorted(c for c in ('4PIR', 'HASHLOOP', '4PIPI') if c in k7)} (must be none)")
    if set(k7) != set(k6): bad.append(f"class sets differ: {sorted(set(k6) ^ set(k7))}")
    ch = sorted(c for c in k7 if k6.get(c) != k7[c]); chA = sorted(c for c in k7A if k6A.get(c) != k7A[c])
    out.append("changed in v7 pooled (EBR form B): " + "; ".join(f"{c} {'/'.join(k6raw[c])} -> {'/'.join(k7raw[c])}" for c in ch))
    if ch != ["4PI"] or chA != ["4PI"] or k7["4PI"] != ("d", "q"): bad.append(f"pooled changes {ch} / form A {chA} != [4PI], 4PI {k7.get('4PI')}")
    for c in UNCHANGED:
        if k6.get(c) != k7.get(c) or k6A.get(c) != k7A.get(c): bad.append(f"{c} moved in pooled key ({k6.get(c)} -> {k7.get(c)})")
    out.append("unchanged from v6 (checked, pooled): " + " ".join(f"{c}={'/'.join(k7[c])}" for c in UNCHANGED) + "; EBR form A = " + "/".join(k7A["EBR"]))
    zn = [l for l in tsv.split("\n") if l.startswith("ZHOOK\t")]
    if len(zn) != 2 or not all("glyph link VERIFY-F61-V8" in l and "no glyph link" not in l.split("replaces")[0] for l in zn): bad.append("ZHOOK note")
    out.append(f"ZHOOK rows: {len(zn)}, value {'/'.join(k7['ZHOOK'])} (unchanged), note 'the 2# sign = H24 cell, glyph link VERIFY-F61-V8', grade S")
    chf = sorted(c for c in k7f if k7.get(c) != k7f[c])
    out.append("f.61 reading key over the pooled key: " + "; ".join(f"{c} {'/'.join(k7raw.get(c, ('unread',)))} -> {'/'.join(k7fraw[c])}" for c in chf)
               + "; 4PIPI applies at L11 9 only (L01 12 relabelled 4PIPI_UNREAD, no entry)")
    if chf != ["4PIPI", "4STEM", "4TRI"] or k7f["4PIPI"] != ("a", "n") or any(k6f[c] != k7f[c] for c in ("4STEM", "4TRI", "HASH4", "ZHOOK")):
        bad.append(f"f.61 reading changes {chf}")
    # meter (bands as verify_v8/meter_v8.py)
    def band(letters, cls):
        if cls == "C6" or letters in ("-", ""): return "unread/null"
        n = len(letters.split("/")); return "firm" if n == 1 else ("two-way" if n == 2 else "wider")
    NEW = {c: "/".join(k7fraw[c]) for c in {"4STEM", "4TRI", "HASH4", "ZHOOK", "VBAR_A", "EBR", "SBS"}}
    d = list(csv.DictReader(open(f"{HERE}/f61_decode_period_v4_frac0.1_sbs.tsv"), delimiter="\t"))
    def v7(r, pi):
        if r["class"] == "4PI": return pi((r["line"], int(r["pos"])))
        return NEW.get(r["class"], r["period_letters"])
    for tag, pi, want in (("V8 'both cells as endorsed' (f.61's two 4PI held unread)", lambda t: "-", (12, 58, 2, 27, 99)),
                          ("key v7 as merged (L11 9 a/n grade M, L01 12 unread)", lambda t: "/".join(F61TOK[t]) or "-", (12, 59, 2, 26, 99))):
        c = Counter(band(v7(r, pi), r["class"]) for r in d)
        meter = (c["firm"], c["two-way"], c["wider"], c["unread/null"], len(d))
        wid = Counter(r["class"] + "=" + v7(r, pi) for r in d if band(v7(r, pi), r["class"]) == "wider")
        out.append(f"f.61 meter, {tag}: {len(d)} signs: firm {meter[0]} / two-way {meter[1]} / wider {meter[2]} / unread-or-null {meter[3]}; "
                   "still wider: " + " ".join(f"{k}:{v}" for k, v in sorted(wid.items())))
        if meter != want: bad.append(f"meter {tag} {meter} != {want}")
    # known spans
    lines = split_lines(load_read()); lines.update(f108_lines()); relabel(lines)
    lines61 = f61_relabel({k: list(v) for k, v in lines.items()})
    s61 = load_spans(); s108 = [(s, "F108_" + ("L02" if s == "T1" else "L03"), m) for s, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{S}/tomokiyo_spans_3983.tsv") if l[0] == "T")]
    def sc(key, spans, ll):
        mt = tot = 0
        for s, l, m in spans:
            mm = m.translate(FOLD); mt += align(mm, ll[l], key)[0]; tot += sum(1 for ch_ in mm if ch_ != "-")
        return mt, tot
    for tag, spans, k, ll, want in (("f.61 five spans, f.61 reading key", s61, k7f, lines61, (53, 55)),
                                    ("f.61 five spans, pooled key, 4PI unrelabelled (info)", s61, k7, lines, None),
                                    ("f.108r overlay, pooled key (EBR form A)", s108, k7A, lines, (74, 84))):
        mt, tot = sc(k, spans, ll); labs = sorted(k); vals = [k[x] for x in labs]; rng = random.Random(20260929); cs = []
        for _ in range(2000):
            v = list(vals); rng.shuffle(v); cs.append(sc(dict(zip(labs, v)), spans, ll)[0])
        cs.sort(); ge = sum(x >= mt for x in cs)
        out.append(f"{tag} (j=i, v=u, y=i folded): v7 {mt}/{tot} = {mt/tot:.3f}; 2000 permuted mean {sum(cs)/2000/tot:.3f} p95 {cs[1899]/tot:.3f} max {cs[-1]/tot:.3f}; >= key {ge}/2000")
        if want and (mt, tot) != want: bad.append(f"{tag} {mt}/{tot} != {want[0]}/{want[1]}")
    out.append("REPRODUCED: " + ("yes" if not bad else "NO -- " + "; ".join(bad)))
    return "\n".join(out) + "\n", bad
def main():
    tsv = build()
    if CHECK:
        if not os.path.exists(V7) or open(V7).read() != tsv: sys.exit("STALE key_period_v7.tsv")
    txt, bad = repro(tsv)
    if CHECK:
        if open(RES).read() != txt: sys.exit("STALE build_key_v7_result.txt")
        print("check OK")
    else:
        open(V7, "w").write(tsv); open(RES, "w").write(txt); print(txt, end="")
    if bad: sys.exit(1)
if __name__ == "__main__": main()
