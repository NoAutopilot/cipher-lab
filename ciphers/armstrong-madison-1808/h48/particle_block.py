#!/usr/bin/env python3
"""H48: does a period table put English function words in a 1-99 block (the target's design family C: a particle
block 1-99 and a book >= 100, ARM-DESIGN)? For each table: the share of its valued codes below 100 whose value is a
function word, the same share at >= 100, and their difference; null = the table's values permuted over its codes
(2,000 draws), so the difference is tested against the same table's own mix of values. Tables: the Madrid legation
cipher (tools/data/uscodes-1800/key_legation_madrid_1807.tsv, all glossed values and the grade-C subset), WE028 and
THE972 (Department tables, the same directory) as references.
usage: python3 ciphers/armstrong-madison-1808/h48/particle_block.py"""
import csv, os, random, re
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
D = os.path.join(ROOT, "tools", "data", "uscodes-1800")
FW = set("""a an the of to in on at by for from with into upon unto as and or but nor not no if so than that this these
those there then thus which who whom whose what when where while it its he him his she her they them their we us our
i me my you your be is are was were been am being have has had do does did shall will would should could may might must
can all any each some such very more most other one same also only yet till until after before about against between
through during without within under over up out""".split())
def load(path, code_col="code", value_col="value", grade=None):
    rows = csv.DictReader((l for l in open(path, encoding="utf-8") if not l.startswith("#")), delimiter="\t")
    out = []
    for r in rows:
        c = re.sub(r"\D", "", r.get(code_col) or ""); v = (r.get(value_col) or "").strip().lower().split("|")[0]
        if not c or not v or v in ("-", "?", "null"): continue
        if grade and r.get("grade") != grade: continue
        out.append((int(c), v))
    return out
def stat(pairs):
    lo = [v in FW for c, v in pairs if c < 100]; hi = [v in FW for c, v in pairs if c >= 100]
    return (sum(lo) / len(lo) if lo else 0.0), (sum(hi) / len(hi) if hi else 0.0), len(lo), len(hi)
def test(name, pairs, draws=2000, seed=48):
    a, b, nlo, nhi = stat(pairs); d = a - b
    rnd = random.Random(seed); vals = [v for _, v in pairs]; codes = [c for c, _ in pairs]; null = []
    for _ in range(draws):
        rnd.shuffle(vals); x, y, _, _ = stat(list(zip(codes, vals))); null.append(x - y)
    null.sort(); p = sum(n >= d for n in null) / draws
    print(f"{name}\tcodes<100 {nlo}\tFW share {a:.3f}\tcodes>=100 {nhi}\tFW share {b:.3f}\tdiff {d:+.3f}\tnull p95 {null[int(.95*draws)]:+.3f}\tp {p:.4f}")
def header_cols(path):
    for l in open(path, encoding="utf-8"):
        if not l.startswith("#"): return l.rstrip("\n").split("\t")
leg = os.path.join(D, "key_legation_madrid_1807.tsv")
test("legation (all glossed)", load(leg))
test("legation (grade C)", load(leg, grade="C"))
for t in ["WE028.tsv", "THE972_bourdeau.tsv"]:  # these name the code column 'value' and the word 'plaintext'
    test(t, load(os.path.join(D, t), "value", "plaintext"))
# positive control (power at the legation table's own n): the same glossed values, with the codes reassigned so that
# function words fill the 39 codes below 100 first (a table built with a particle block); must clear its null
pairs = load(leg); codes = sorted(c for c, _ in pairs); nlo = sum(c < 100 for c in codes)
rnd = random.Random(7); fw = [v for _, v in pairs if v in FW]; other = [v for _, v in pairs if v not in FW]
rnd.shuffle(fw); rnd.shuffle(other); vals = fw[:nlo] + other + fw[nlo:]
lo_vals, hi_vals = vals[:nlo], vals[nlo:]; rnd.shuffle(hi_vals)
test("control: legation values with a built 1-99 particle block", list(zip(codes, lo_vals + hi_vals)))
# weaker control: only half of the sub-100 codes are function words (a mixed particle block)
half = nlo // 2; vals2 = fw[:half] + other[:nlo - half]; rest = fw[half:] + other[nlo - half:]; rnd.shuffle(rest)
test("control: half-particle 1-99 block", list(zip(codes, vals2 + rest)))
