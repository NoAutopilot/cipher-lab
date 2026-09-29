#!/usr/bin/env python3
"""VERIFY-F61-V5 (29 Sept 2026): f.61r meter and known-span score under key v4 plus the values this audit endorses.
Endorsed changes (AUDIT.md VERIFY-F61-V5): VBAR_A s/t -> g/t; EBR (all f.61 brackets are form B, H22 4/4) -> l/y; SBS b/e/o -> b/o;
ZHOOK (unread) -> i/x, graded S on f.61 (cross-hand link by letter agreement, not by glyph). C6 stays unread/null (VERIFY-F61-V4).
Meter bands from family/f61_decode_period_v4_frac0.1_sbs.tsv: firm = one letter (C/C+), two-way = two letters, wider = 3+, unread/null.
Known spans: test_period_key's DP, 2000 permuted keys (seed 20260929) on f.61; f.108r scored with EBR left at v4 (its brackets are
mostly form A, H22). Writes meter_v5_result.txt; --check."""
import csv, os, random, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); F = os.path.abspath(f"{HERE}/../family"); S = os.path.abspath(f"{HERE}/../scripts")
CHECK = "--check" in sys.argv
sys.argv = [sys.argv[0], "--key", f"{F}/key_period_v4.tsv", "--collapse-ebr", "--min", "2", "--frac", "0.1", "--sbs"]
sys.path.insert(0, F); sys.path.insert(0, S)
import test_period_key as T
from f61crib import align, load_read, load_spans
from f61crib4 import split_lines
from f61joint import f108_lines
from sbs_relabel import relabel
NEW = {"VBAR_A": "g/t", "EBR": "l/y", "SBS": "b/o", "ZHOOK": "i/x"}
def band(letters, cls):
    if cls == "C6" or letters in ("-", ""): return "unread/null"
    n = len(letters.split("/")); return "firm" if n == 1 else ("two-way" if n == 2 else "wider")
def main():
    d = list(csv.DictReader(open(f"{F}/f61_decode_period_v4_frac0.1_sbs.tsv"), delimiter="\t")); out = []
    for tag, f in (("v4 (C6 regraded, VERIFY-F61-V4)", lambda r: r["period_letters"]), ("v4 + endorsed (this audit)", lambda r: NEW.get(r["class"], r["period_letters"]))):
        c = Counter(band(f(r), r["class"]) for r in d)
        out.append(f"{tag}: {len(d)} signs: firm {c['firm']} / two-way {c['two-way']} / wider {c['wider']} / unread-or-null {c['unread/null']}")
    ch = Counter((r["class"], r["period_letters"], NEW[r["class"]]) for r in d if r["class"] in NEW)
    out.append("tokens changed: " + "; ".join(f"{k[0]} {k[1]} -> {k[2]} x{v}" for k, v in sorted(ch.items())))
    wid = Counter(r["class"] + "=" + NEW.get(r["class"], r["period_letters"]) for r in d if band(NEW.get(r["class"], r["period_letters"]), r["class"]) == "wider")
    out.append("still wider than two: " + " ".join(f"{k}:{v}" for k, v in sorted(wid.items())))
    key4 = T.load_key(); key5 = dict(key4); key5.update({"VBAR_A": ("g", "t"), "EBR": ("i", "l"), "SBS": ("b", "o"), "ZHOOK": ("i", "x")})
    key5r = dict(key5); key5r["EBR"] = key4["EBR"]
    lines = split_lines(load_read()); lines.update(f108_lines()); relabel(lines)
    s61 = load_spans(); s108 = [(s, "F108_" + ("L02" if s == "T1" else "L03"), m) for s, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{S}/tomokiyo_spans_3983.tsv") if l[0] == "T")]
    def sc(key, spans):
        mt = tot = 0
        for s, l, m in spans:
            mm = m.translate(str.maketrans("jvy", "iui")); mt += align(mm, lines[l], key)[0]; tot += sum(1 for c in mm if c != "-")
        return mt, tot
    for tag, spans, keys in (("f.61 five spans", s61, (("v4", key4), ("v4+endorsed", key5))), ("f.108r overlay", s108, (("v4", key4), ("v4+endorsed (EBR at v4)", key5r)))):
        for kt, k in keys:
            mt, tot = sc(k, spans); labs = sorted(k); vals = [k[x] for x in labs]; rng = random.Random(20260929); cs = []
            for _ in range(2000):
                v = list(vals); rng.shuffle(v); cs.append(sc(dict(zip(labs, v)), spans)[0])
            cs.sort(); out.append(f"{tag} (j=i, v=u, y=i folded): {kt} {mt}/{tot} = {mt/tot:.3f}; 2000 permuted mean {sum(cs)/2000/tot:.3f} p95 {cs[1899]/tot:.3f} max {cs[-1]/tot:.3f}; >= key {sum(x >= mt for x in cs)}/2000")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/meter_v5_result.txt"
    if CHECK: sys.exit(0 if open(p).read() == txt else "STALE")
    open(p, "w").write(txt); print(txt)
if __name__ == "__main__": main()
