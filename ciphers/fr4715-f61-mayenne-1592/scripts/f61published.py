#!/usr/bin/env python3
"""Campaign step H44 (28 Sept 2026, runner session_01J8hunWPcE7QYcpCx59CUHV): PUBLISHED-CHECK of the five sign classes
of f.61r that no period gloss covers (CA, LOOPBAR, ZHOOK, CROSS, LL; family/KEY.md) against the one PUBLISHED source on
disk, S. Tomokiyo's reconstruction of the Mayenne cipher (keys/key_mayenne_1592.tsv, transcribed from mayenne.png) and
his own interlinear markup of f.61 (scripts/tomokiyo_spans.tsv, from BnFfr4715f61.png). Script-only, no calls.

For each class, three published facts are gathered and written to family/key_published_rare.tsv (key source
`published`, credit Tomokiyo; NEVER merged into family/key_period_*):
  (a) which of his 16 table drawings the F61-CAL reader matched the class to (read_call_A.tsv 'symbol' column, the
      on-disk shape-to-drawing matching; '?' = the reader matched no drawing), and the letters that cell carries;
  (b) the letters Tomokiyo himself writes over the class's signs on f.61 (class_diag.tsv, and re-derived here by the
      F61-CAL DP with the published pairs in the key so the aligner can place them);
  (c) the runner's own reading of the two shape descriptions (the atlas row vs the table row), stated as such.

Test (rule 3, pre-registered before the numbers were seen): key_period_v3.tsv under test_period_key.py's own filter
(--collapse-ebr --min 2 --frac 0.1; the filter is re-implemented here line for line and the baseline must reproduce
family/test_period_key_result_v3_frac0.1_min2.txt exactly, else STALE) plus the published pairs, scored on (1) the 55
known letters and (2) f.108r's 84 overlay letters, each against 20 keys with the letter sets permuted across the classes
(seed 1). The 55-letter figure is CIRCULAR for any pair read from Tomokiyo's own f.61 markup (the reference and the
source are the same letters) and is reported, not gated; the gate is f.108r: the published pairs must raise 66/84 and
the result must stay above every permuted key. A pair that lowers either leaf is recorded as a conflict, not used.

  python3 scripts/f61published.py [--check]     (from the target folder; --check exits 1 if the result file is stale)
Writes scripts/f61published_result.txt and family/key_published_rare.tsv.
"""
import csv, os, random, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
FAM = os.path.abspath(f"{HERE}/../family")
from f61crib import align, load_read, load_spans, classify
from f61crib4 import split_lines
from f61joint import f108_lines

RARE = ["CA", "LOOPBAR", "ZHOOK", "CROSS", "LL"]
INV = {"S01": "a", "S02": "n", "S03": "b/o", "S04": "c/p", "S05": "d/q", "S06": "e", "S07": "r", "S08": "f/s",
       "S09": "g/t", "S10": "h/u", "S11": "i/x", "S12": "l/y", "S13": "m/z", "S14": "que", "S15": "qui", "S16": "pour"}
# (c) the runner's reading of keys/key_mayenne_1592.tsv's 'sign' descriptions against scripts/f61_atlas.tsv, written
# before any score was looked at. Only one atlas row has a table drawing of the same construction.
RUNNER_MATCH = {
    "CROSS": ("a", "table row a: 'cross/plus shape with a short diagonal stroke rising from the crossing point toward the upper right' = atlas CROSS 'a plain plus or cross, possibly with a stroke rising to the upper right'; the table's a/n column draws TWO symbols (a: this cross; n: a heavier, blockier cross), so the cell is a alone or a/n"),
    "ZHOOK": (None, "no table drawing of a 7/Z hook over crossed stems; the i/x drawing is 'a small knot above a long horizontal bar crossed by a short vertical stroke' (grade ? in the key file)"),
    "CA": (None, "no table drawing is a cursive a"),
    "LOOPBAR": (None, "no table drawing is a loop on a stem with a bar at the foot (que = converging strokes into a loop; pour = a hook into one long diagonal)"),
    "LL": (None, "no table drawing is an ll"),
}
# published pairs used in the test, per class, with their source (written before the numbers were seen)
PUBLISHED = {
    "ZHOOK": [("i", "Tomokiyo f.61 markup (BnFfr4715f61.png): i at L07/11 and L11/11, j at L07/3 -- his own reading of this leaf, self-labelled incomplete"),
              ("x", "the i/x cell partner of keys/key_mayenne_1592.tsv (table column i/x); no attestation")],
    "CROSS": [("a", "table row a (mayenne.png), matched by the F61-CAL reader (S01) and by the runner's reading of the two descriptions; Tomokiyo's own f.61 markup sets a DASH over both CROSS signs (L01/1, L07/10)"),
              ("n", "the a/n column partner; the table draws n as a separate, heavier cross, so this is the cell reading, not the drawing's")],
}
NULL_PUBLISHED = {"CA": "dashes at every CA position of the five spans (class_diag.tsv, by eye; H4's DP dash-share rule: CA under dashes too)", "LOOPBAR": "dashes at every LOOPBAR position by eye (class_diag.tsv); H4's DP dash-share rule put 2 of 3 under dashes, the third takes a neighbour's letter in the DP (an aligner artefact of an uncovered class, see the result file)", "LL": "dash at L05/16",
                  "CROSS": "dashes at L01/1 and L07/10 (conflicts with the table drawing, recorded, not resolved)"}

def load_v3():
    """test_period_key.py load_key() with --collapse-ebr --min 2 --frac 0.1, re-implemented line for line."""
    MIN, FRAC, COLLAPSE = 2, 0.1, {"EBR_A": "EBR", "EBR_B": "EBR"}
    rows = [r for r in csv.DictReader((l for l in open(f"{FAM}/key_period_v3.tsv") if not l.startswith("#")), delimiter="\t")]
    tot = Counter(); key = {}
    for r in rows:
        if r["letter"] not in ("-", ""): tot[(r["class"], r["leaf"])] += int(r["n"])
    for r in rows:
        if r["letter"] in ("-", "") or r["class"] in ("PLAIN", "OTHER", "DASH") or int(r["n"]) < MIN: continue
        if int(r["n"]) < FRAC * tot[(r["class"], r["leaf"])]: continue
        key.setdefault(COLLAPSE.get(r["class"], r["class"]), set()).add(r["letter"])
    return {c: tuple(sorted(v)) for c, v in key.items()}

def score(key, lines, spans):
    mat = tot = 0
    for s, line, markup in spans:
        mt, _ = align(markup, lines[line], key); mat += mt; tot += sum(1 for c in markup if c != "-")
    return mat, tot

def placed(key, lines, spans, classes):
    """letters of the markup that the DP places on signs of the given classes (line, pos, class, char)."""
    out = []
    for s, line, markup in spans:
        _, pairs = align(markup, lines[line], key)
        for i, j in pairs:
            if lines[line][j] in classes: out.append((line, j + 1, lines[line][j], markup[i]))
    return out

def run(key, lines, spans61, spans108, label, rng_seed=1):
    rng = random.Random(rng_seed); labs = sorted(key); vals = [key[l] for l in labs]
    perms = []
    for _ in range(20):
        v = list(vals); rng.shuffle(v); perms.append(dict(zip(labs, v)))
    out = []; res = {}
    for tag, spans in (("f.61 known (55)", spans61), ("f.108r overlay (84)", spans108)):
        mt, tot = score(key, lines, spans); cs = [score(p, lines, spans)[0] for p in perms]
        used = [l for _, l, _ in spans]; cls = Counter(c for l in used for c in lines[l])
        cov = sum(n for c, n in cls.items() if c in key) / max(1, sum(cls.values()))
        miss = sorted(c for c in cls if c not in key)
        out.append(f"  {tag}: {mt}/{tot} = {mt/tot:.3f}; 20 permuted keys mean {sum(cs)/20/tot:.3f} max {max(cs)/tot:.3f}; covered {cov:.2f} (uncovered: {' '.join(miss) or 'none'})")
        res[tag] = (mt, tot, max(cs))
    return [label] + out, res

def main():
    read = load_read(); lines = split_lines(read); lines.update(f108_lines())
    spans61 = load_spans()
    spans108 = [(s, "F108_" + ("L02" if s == "T1" else "L03"), m) for s, _, m, _ in
                (l.rstrip("\n").split("\t") for l in open(f"{HERE}/tomokiyo_spans_3983.tsv") if l[0] == "T")]
    out = ["H44 PUBLISHED-CHECK of the rare classes (script-only; sources: keys/key_mayenne_1592.tsv, read_call_A.tsv, tomokiyo_spans.tsv, class_diag.tsv)", ""]
    # (a) reader's S-labels per rare class, from read_call_A.tsv (the F61-CAL shape-to-drawing matching on disk)
    slab = defaultdict(Counter); marks = defaultdict(Counter); pos = defaultdict(list)
    for r in csv.DictReader(open(f"{HERE}/read_call_A.tsv"), delimiter="\t"):
        c = classify(r["marks"])
        if c in RARE: slab[c][r["symbol"]] += 1; marks[c][r["marks"].split(";")[0]] += 1; pos[c].append(f"{r['line']}/{r['pos']}")
    out.append("(a) F61-CAL reader's table-drawing labels per rare class (read_call_A.tsv symbol column; '?' = matched no drawing):")
    for c in RARE:
        lab = ", ".join(f"{s}{'=' + INV[s] if s in INV else ''} x{n}" for s, n in slab[c].most_common())
        out.append(f"  {c}: {sum(slab[c].values())} signs on the span lines ({' '.join(pos[c])}); labels {lab}; marks {dict(marks[c])}")
    # (b) Tomokiyo's letters on those positions: class_diag.tsv (by eye) and the DP with the published pairs in the key
    v3 = load_v3()
    pub = {c: tuple(l for l, _ in v) for c, v in PUBLISHED.items()}
    out.append(""); out.append("(b) Tomokiyo's own markup over the rare positions (class_diag.tsv: ZHOOK i:2 j:1; CA, LOOPBAR, LL, CROSS, C6 dashes only). DP placement with v3 + published pairs in the key:")
    kp = dict(v3); kp.update(pub)
    for line, p, c, ch in placed(kp, lines, spans61, set(RARE)): out.append(f"  {line}/{p} {c}: '{ch}'")
    out.append("  (a position missing from this list took a gap in the DP: no markup character over it)")
    out.append(""); out.append("(c) runner's reading of the two shape descriptions:")
    for c in RARE: out.append(f"  {c}: {RUNNER_MATCH[c][1]}")
    # tests
    out.append(""); out.append("TESTS (20 permuted keys, seed 1, test_period_key.py filter re-implemented: --collapse-ebr --min 2 --frac 0.1):")
    o, base = run(v3, lines, spans61, spans108, "K0 = key_period_v3.tsv baseline (must equal family/test_period_key_result_v3_frac0.1_min2.txt: 43/55 mean 0.372 max 0.618; 66/84 mean 0.344 max 0.512)")
    out += o
    assert base["f.61 known (55)"][0] == 43 and base["f.108r overlay (84)"][0] == 66, "baseline does not reproduce test_period_key.py -- STALE filter"
    variants = [("K1 = v3 + ZHOOK i/x (published: Tomokiyo's f.61 markup + the table cell partner)", {"ZHOOK": ("i", "x")}),
                ("K2 = K1 + CROSS a/n (the table's a/n column, drawing matched)", {"ZHOOK": ("i", "x"), "CROSS": ("a", "n")}),
                ("K3 = K1 + CROSS a (the drawing's own letter only)", {"ZHOOK": ("i", "x"), "CROSS": ("a",)})]
    results = {}
    for label, extra in variants:
        k = dict(v3); k.update(extra); o, r = run(k, lines, spans61, spans108, label); out += o; results[label[:2]] = r
        # circularity: letters the DP puts on ZHOOK/CROSS positions of the 55 (these are the reference itself)
        pl = [x for x in placed(k, lines, spans61, set(extra)) if x[3] != "-"]; hit = sum(1 for _, _, c, ch in pl if ch in k[c])
        out.append(f"    of the 55, letters matched AT the added classes' positions (circular for ZHOOK): {hit} of {len(pl)} letters placed there; 55-letter score without them {r['f.61 known (55)'][0]-hit}/{55-hit}")
    # gate on f.108r
    m0 = base["f.108r overlay (84)"][0]; m1, _, mx1 = results["K1"]["f.108r overlay (84)"]
    out.append("")
    out.append(f"GATE (pre-registered, f.108r only, non-circular): K1 reads more than K0 ({m1} vs {m0}) and beats every permuted key (max {mx1}/84 = {mx1/84:.3f}): {'PASS' if m1 > m0 and m1 > mx1 else 'FAIL'}")
    zl = [(l, p, ch) for l, p, c, ch in placed(dict(v3, ZHOOK=("i", "x")), lines, spans108, {"ZHOOK"})]
    out.append(f"  f.108r overlay letters the DP places on its 7 ZHOOK signs under K1 (Tomokiyo's reprint of the leaf's period gloss): {' '.join(f'{l[5:]}/{p}:{ch}' for l, p, ch in zl)}")
    for kk in ("K2", "K3"):
        r = results[kk]; a, b = r["f.61 known (55)"][0], r["f.108r overlay (84)"][0]
        out.append(f"  {kk} vs K1: f.61 {a} vs {results['K1']['f.61 known (55)'][0]}, f.108r {b} vs {m1} (CROSS absent from f.108r's two lines; on f.61 Tomokiyo's dashes make CROSS = a a conflict with his markup: recorded, not used)")
    txt = "\n".join(out) + "\n"
    # the published key file (rule 4 grade: published pairs, credit Tomokiyo; never merged into key_period_*)
    tsv = ["# key_published_rare.tsv -- campaign step H44 (28 Sept 2026, runner session_01J8hunWPcE7QYcpCx59CUHV), regenerated by scripts/f61published.py.",
           "# Key source: published (CLAUDE.md rule 10 vocabulary) -- S. Tomokiyo, 'Duke of Mayenne's Ciphers' (mayenne.htm, table mayenne.png,",
           "# transcribed in keys/key_mayenne_1592.tsv) and his interlinear markup of BnF fr.4715 f.61 (bnf4715.htm#no38, BnFfr4715f61.png,",
           "# self-labelled 'Solution Incomplete'; scripts/tomokiyo_spans.tsv). One row per (class, letter). These rows are NOT period readings",
           "# and are never merged into family/key_period_*.tsv; a decode that uses them has key source 'mixed' (period + published) for these",
           "# classes, which the verifier records. 'null' = Tomokiyo leaves the sign unread (a dash) at every one of its f.61 positions.",
           "class\tletter\tn_f61_positions\tsource\tevidence"]
    for c in RARE:
        if c in PUBLISHED:
            for l, ev in PUBLISHED[c]:
                n = sum(1 for _, _, cc, ch in placed(kp, lines, spans61, {c}) if cc == c and ch == l)
                tsv.append(f"{c}\t{l}\t{n} of {len(pos[c])} ({'j folded to i' if c == 'ZHOOK' and l == 'i' else 'markup letters at the class positions'})\tpublished (Tomokiyo)\t{ev}")
        if c in NULL_PUBLISHED:
            tsv.append(f"{c}\tnull\t{len(pos[c])} of {len(pos[c])} (dashes by eye, class_diag.tsv)\tpublished (Tomokiyo f.61 markup)\t{NULL_PUBLISHED[c]}; table drawing match: {RUNNER_MATCH[c][1]}")
    tsvtxt = "\n".join(tsv) + "\n"
    rp, kp_path = f"{HERE}/f61published_result.txt", f"{FAM}/key_published_rare.tsv"
    if "--check" in sys.argv:
        ok = os.path.exists(rp) and open(rp).read() == txt and os.path.exists(kp_path) and open(kp_path).read() == tsvtxt
        print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(rp, "w").write(txt); open(kp_path, "w").write(tsvtxt); print(txt, end=""); print("--- family/key_published_rare.tsv ---"); print(tsvtxt, end="")
if __name__ == "__main__":
    main()
