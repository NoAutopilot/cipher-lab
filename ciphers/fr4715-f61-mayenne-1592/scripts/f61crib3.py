#!/usr/bin/env python3
"""F61-CRIB3 (campaign step H12, 27 Sept 2026): the class map fitted through the Mayenne table's own pairing.

Same 19 shape classes, folds, scoring DP and shuffle count as scripts/f61crib.py; same null-aware alignment as
scripts/f61crib2.py (tools/interlinear_align.py --code-prefix @ --wildcard - --null-cost -1). The difference: a class
does not take a free top-2 letter set but ONE table cell of keys/key_mayenne_1592.tsv (a/n, b/o, c/p, d/q, e/r, f/s,
g/t, h/u, i/x, l/y, m/z), the cell whose two letters its aligned markup letters fall in most often (ties: the
alphabetically first cell, reported); a class with no aligned letter is a null. The withheld span is scored with the
cell's pair, so the pair's second letter comes from the key (grade H source), not from 1-2 occurrences in 55 letters.

Controls: 20 maps per fold with the fitted cells permuted across the classes (seed 1), pooled like the target.
Gate (H12, CAMPAIGN.md): (a) pooled held-out above every one of the 20 pooled controls AND (b) the cell of PHI, C43,
4TRI, VBAR, DBL and INF identical in all five folds. The V s/t conflict (one class, cells f/s and g/t) is reported per
fold, not settled.

  python3 scripts/f61crib3.py [--check]   (from the target folder)
Writes scripts/f61crib3_result.txt and scripts/f61crib3_map.tsv (cells fitted on all five spans).
"""
import os, random, sys
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from f61crib import HERE, FOLDS, load_read, load_spans, fit, score, align

OPTS = ("--wildcard", "-", "--null-cost", "-1")
STABLE = ["PHI", "C43", "4TRI", "VBAR", "DBL", "INF"]

def load_cells():
    """the table's letter pairs from keys/key_mayenne_1592.tsv: column order a..m over n..z."""
    rows = [l.rstrip("\n").split("\t") for l in open(f"{HERE}/../keys/key_mayenne_1592.tsv") if not l.startswith("#")]
    letters = [r[1] for r in rows[1:] if r[2] == "letter"]
    top = "abcdefghilm"; bot = "nopqrstuxyz"
    cells = [a + "/" + b for a, b in zip(top, bot)]
    assert set(letters) == set(top + bot), sorted(letters)
    return cells
def cell_map(counts, cells):
    """class -> (cell, cell counts) by top-1 cell; a class with no letters -> None."""
    out = {}
    for c, cnt in counts.items():
        cc = Counter()
        for l, n in cnt.items():
            for cell in cells:
                if l in cell.split("/"): cc[cell] += n
        if cc:
            best = sorted(cc.items(), key=lambda kv: (-kv[1], kv[0]))
            out[c] = (best[0][0], cc, len(best) > 1 and best[1][1] == best[0][1])
    return out
def values(cm):
    return {c: tuple(v[0].split("/")) for c, v in cm.items()}

def main():
    lines, spans, cells = load_read(), load_spans(), load_cells()
    by = {s: (s, l, m) for s, l, m in spans}
    out = ["reader file: read_call_A.tsv (marks column only); fit: tools/interlinear_align.py " + " ".join(("--code-prefix", "@") + OPTS)
           + " -> top-1 table cell per class; score: f61cal.py DP with the cell pair"]
    rng = random.Random(1); NC = 20
    pooled = tot_all = 0; ctrl = [0] * NC; folds_cells = {c: set() for c in STABLE}; vconf = []
    for held in FOLDS:
        train = [by[s] for s in by if s not in held]; test = [by[s] for s in held]
        cm = cell_map(fit(train, lines, "c3_" + "".join(held), OPTS, keep_dashes=True), cells)
        kmap = values(cm)
        mt, tot = score(kmap, lines, test); pooled += mt; tot_all += tot
        for c in STABLE: folds_cells[c].add(cm[c][0] if c in cm else "null")
        vb = cm.get("VBAR"); vconf.append(f"{'+'.join(held)}: " + (" ".join(f"{k}:{n}" for k, n in vb[1].most_common()) if vb else "none"))
        labs = sorted(kmap); vals = [kmap[l] for l in labs]; cs = []
        for k in range(NC):
            v = list(vals); rng.shuffle(v)
            cmk, _ = score(dict(zip(labs, v)), lines, test); ctrl[k] += cmk; cs.append(cmk)
        ties = [c for c in cm if cm[c][2]]
        out.append(f"held-out {'+'.join(held)}\tmatched {mt}/{tot}\tshuffled max {max(cs)}/{tot} mean {sum(cs)/NC:.2f}\tcells "
                   + " ".join(f"{l}={cm[l][0]}" for l in labs) + (f"\tties: {' '.join(ties)}" if ties else ""))
    pc = [c / tot_all for c in ctrl]
    out.append(f"POOLED held-out\t{pooled}/{tot_all} = {pooled/tot_all:.3f}  (H11 free sets 36/55 = 0.655; H1 24/55 = 0.436; F61-CAL level 0.85)")
    out.append("controls (20 cell-permuted maps pooled across folds, seed 1): " + " ".join(f"{c:.3f}" for c in pc))
    out.append(f"control mean {sum(pc)/NC:.3f} max {max(pc):.3f}")
    stab = {c: sorted(v) for c, v in folds_cells.items()}
    stable = all(len(v) == 1 for v in stab.values())
    out.append("cell per fold: " + " ".join(f"{c}={'|'.join(v)}" for c, v in stab.items()))
    out.append("VBAR cell counts per fold (the s/t conflict): " + "; ".join(vconf))
    a = pooled / tot_all > max(pc)
    out.append(f"GATE H12 (a) pooled above every control: {'PASS' if a else 'FAIL'}; (b) six classes cell-stable: {'PASS' if stable else 'FAIL'}; H12 {'PASS' if a and stable else 'FAIL'}")
    # all-span map for H4, plus which of the 55 letters the all-span map misses on its own spans (in-sample, non-gating)
    full = cell_map(fit(spans, lines, "c3_all", OPTS, keep_dashes=True), cells)
    kfull = values(full)
    classes = Counter(c for l in lines.values() for c in l)
    with open(f"{HERE}/f61crib3_map.tsv", "w") as f:
        f.write("# F61-CRIB3 map fitted on all five Tomokiyo spans: class -> Mayenne table cell (top-1 cell by aligned-letter count), 27 Sept 2026.\n"
                "# Grade M: cells chosen from Tomokiyo's own 'Solution Incomplete' markup; the pair itself is the key's (grade H source). 'null' = no letter aligned.\n"
                "class\tn_signs\tcell\tcell_counts\ttie\n")
        for c, n in classes.most_common():
            v = full.get(c)
            f.write(f"{c}\t{n}\t{v[0] if v else 'null'}\t{' '.join(f'{k}:{m}' for k, m in v[1].most_common()) if v else ''}\t{'yes' if v and v[2] else ''}\n")
    miss = Counter()
    for s, line, markup in spans:
        _, pairs = align(markup, lines[line], kfull)
        seq = lines[line]
        for mi, sj in pairs:
            c = markup[mi]
            if c != "-" and c not in kfull.get(seq[sj], ()): miss[f"{c}@{seq[sj]}"] += 1
    ins, _ = score(kfull, lines, spans)
    out.append(f"all-span map (scripts/f61crib3_map.tsv), in-sample, non-gating: {ins}/55 matched; misses " + " ".join(f"{k}:{n}" for k, n in miss.most_common()))
    # sensitivity, non-gating, added after the gated run above was read: the key has no v and no j (u=v, i=j in the
    # period hand; class_diag already noted 'u=v'), so the markup's v and j are folded to u and i before fit and score
    # (CLAUDE.md rule 3, PX-BRODEC: one transcription convention on both sides). The gate above stays as pre-registered.
    nspans = [(s_, l_, m_.replace("v", "u").replace("j", "i")) for s_, l_, m_ in spans]
    nby = {s_: (s_, l_, m_) for s_, l_, m_ in nspans}
    rng2 = random.Random(1); p2 = 0; c2 = [0] * NC; fc2 = {c: set() for c in STABLE}
    for held in FOLDS:
        train = [nby[s_] for s_ in nby if s_ not in held]; test = [nby[s_] for s_ in held]
        cm = cell_map(fit(train, lines, "c3uv_" + "".join(held), OPTS, keep_dashes=True), cells); kmap = values(cm)
        p2 += score(kmap, lines, test)[0]
        for c in STABLE: fc2[c].add(cm[c][0] if c in cm else "null")
        labs = sorted(kmap); vals = [kmap[l] for l in labs]
        for k in range(NC):
            v = list(vals); rng2.shuffle(v); c2[k] += score(dict(zip(labs, v)), lines, test)[0]
    pc2 = [c / tot_all for c in c2]
    out.append(f"sensitivity (non-gating), v->u and j->i folded in the markup: pooled held-out {p2}/{tot_all} = {p2/tot_all:.3f}; controls mean {sum(pc2)/NC:.3f} max {max(pc2):.3f}; cell per fold: "
               + " ".join(f"{c}={'|'.join(sorted(v))}" for c, v in fc2.items()))
    txt = "\n".join(out) + "\n"
    res = f"{HERE}/f61crib3_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt
        print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")

if __name__ == "__main__":
    main()
