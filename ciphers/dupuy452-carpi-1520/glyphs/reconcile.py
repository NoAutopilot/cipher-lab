#!/usr/bin/env python3
"""Align the two blind passes (passA.tsv, passB.tsv) to the segmented, classified signs
(classified.tsv) and reconcile.

Unit of alignment: one crop file x one of its text lines (line_no). The crop's band (y) picks the
physical line of the page, the crop's box (x) picks the window of segmented signs, so the 700 px
overlap between the _s1 and _s2 segments of a band is handled by aligning each segment to its own
window (a sign in the overlap can collect a reading from each). Alignment is global on the pass
side and free-ended on the segmented side (a reader may stop short of the crop edge), with
substitution score log P(code | type) re-estimated from the previous round's alignments
(ROUNDS rounds, add-one smoothing, seeded by SEED_A / SEED_B, the legend's own descriptions).

Writes glyphs/alignment.tsv (one row per segmented sign: its type and the codes each pass gave,
'-' where the pass covered the sign but gave nothing, '.' where no crop of that pass covers it)
and glyphs/pass_extra.tsv (pass tokens aligned to no segmented sign), and the confusion tables
glyphs/confusion_A.tsv, glyphs/confusion_B.tsv (pass code x type counts).
"""
import csv
import json
import math
import os
import re
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.dirname(HERE)
PAGES = ["f28r", "f28v", "f29r", "f29v"]
ROUNDS = 4
GAP = -2.5          # score of a gap on either side (a sign seen by one and not the other)

NON_SIGN = re.compile(r'PLAIN|^\(see |blank|spillover|dash|^\(\.|^\.$|^\($|^28$|^29$|NOTE|cipher|French|begins|'
                      r'transition|plain|here|same|block|line|mid-band|point|ends|Madame|scet|pere|mon\[|aus\[')

# pass A composite tokens: the reader flagged these as possibly two or three signs read as one
EXPAND_A = {"TO": ["T", "o"], "TA": ["T", "a"], "ov": ["o", "v"], "zv": ["z", "v"], "to": ["T", "o"],
            "on": ["o", "n"], "oRk": ["o", "Rk"], "ox": ["o", "x"], "oo": ["o", "o"], "Tz": ["T", "z"],
            "oI": ["o", "I"], "oso": ["o", "s", "o"], "ma": ["m", "a"], "v-o": ["v", "-o"], "T-o": ["T", "-o"],
            "T-v": ["T", "v"], "T-i": ["T", "I"], "zv-o": ["z", "v", "-o"], "ov6": ["o", "v", "6"],
            "box7": ["box", "7"], "boxx7": ["boxx", "7"], "Z-lam": ["z", "lam"], "omg-lam": ["omg", "lam"],
            "Um(loop)m": ["Um", "m"], "Z(curl)S": ["Z(curl)", "S"], "Uheart]m": ["Um", "m"]}
EXPAND_B = {"fo": ["f", "o"]}

SEED_A = {"phi": "arr", "lam": "lam", "rho": "rho", "v": "v", "dag": "db", "f": "f", "I": "I", "z": "z", "o": "o",
          "box": "box", "n": "n", "T": "T", "x": "X", "eps": "E", "7": "7", "S": "S", "Rk": "R", "theta": "th",
          "omg": "w", "A": "A", "Delta": "Del", "star": "X", "H": "H", "psi": "psi", "s": "S", "m": "m", "6": "six",
          "C6": "six", "heart": "heart", "hash": "hash", "-o": "dash_o", "del": "Del"}
SEED_B = {"C04": "l", "C10": "lam", "v": "v", "C11": "db", "o": "o", "f": "f", "C01": "rho", "C13": "psi",
          "I": "I", "ρ": "q", "z": "z", "ψ": "psi", "C09": "box", "A": "arr", "x": "X", "T": "T", "n": "n",
          "7": "7", "E": "E", "C06": "q", "s": "S", "C19": "th", "R": "R", "C07": "Del", "C14": "w", "H": "H",
          "S": "S", "m": "m", "C18": "z", "6": "six", "C08": "X", "C22": "plus", "K": "K", "3": "three",
          "C21": "oplus", "C20": "box3", "C17": "heart", "C12": "six", "L": "L", "C12 ": "six"}


def load_signs():
    rows = list(csv.DictReader(open(os.path.join(HERE, "classified.tsv")), delimiter="\t"))
    lines = {(r["page"], int(r["line"])): float(r["y_centre"])
             for r in csv.DictReader(open(os.path.join(HERE, "lines.tsv")), delimiter="\t")}
    by_line = defaultdict(list)
    for r in rows:
        r["xc"] = int(r["x"]) + int(r["w"]) / 2
        by_line[(r["page"], int(r["line"]))].append(r)
    return rows, lines, by_line


def norm_code(tok, pas):
    t = tok.strip().strip('"')
    if not t or NON_SIGN.search(t):
        return []
    if t.startswith("[") and t.endswith("]"):
        t = t[1:-1]
    t = t.strip()
    if t in ("", "(.", "."):
        return []
    exp = (EXPAND_A if pas == "A" else EXPAND_B).get(t)
    return exp if exp else [t]


def load_pass(pas):
    fn = os.path.join(TARGET, f"pass{pas}.tsv")
    seqs = defaultdict(list)
    for line in open(fn, encoding="utf-8"):
        if line.startswith("#") or line.startswith("crop_file"):
            continue
        f = line.rstrip("\n").split("\t")
        if len(f) < 4 or not f[0][:4] in PAGES:
            continue
        for c in norm_code(f[3], pas):
            seqs[(f[0], int(f[1]))].append((c, f"{f[0]}:{f[1]}:{f[2]}"))
    return seqs


def crop_boxes():
    man = json.load(open(os.path.join(TARGET, "images", "crops", "manifest.json")))["crops"]
    return {c["crop"]: c["box"] for c in man if c["crop"][:4] in PAGES}


def window(crop, line_no, box, lines, by_line):
    page = crop[:4]
    inband = sorted([(y, li) for (p, li), y in lines.items() if p == page and box[1] <= y < box[3]])
    if line_no > len(inband):
        return None, []
    li = inband[line_no - 1][1]
    sig = [r for r in by_line.get((page, li), []) if box[0] <= r["xc"] < box[2]]
    return li, sig


def align(codes, sigs, score):
    """Global on codes, free end gaps on sigs. Returns list of (code_index|None, sig_index|None)."""
    n, m = len(codes), len(sigs)
    NEG = -1e9
    D = [[NEG] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    for j in range(m + 1):
        D[0][j] = 0.0
    for i in range(1, n + 1):
        D[i][0] = D[i - 1][0] + GAP
        B[i][0] = "u"
    for i in range(1, n + 1):
        ci = codes[i - 1][0]
        for j in range(1, m + 1):
            s = score(ci, sigs[j - 1]["type"])
            best, b = D[i - 1][j - 1] + s, "d"
            if D[i - 1][j] + GAP > best:
                best, b = D[i - 1][j] + GAP, "u"
            if D[i][j - 1] + GAP > best:
                best, b = D[i][j - 1] + GAP, "l"
            D[i][j], B[i][j] = best, b
    j = max(range(m + 1), key=lambda k: D[n][k])
    i, out = n, []
    tail = [(None, k) for k in range(m - 1, j - 1, -1)]
    while i > 0 or j > 0:
        if i == 0:
            out.append((None, j - 1)); j -= 1; continue
        b = B[i][j]
        if b == "d":
            out.append((i - 1, j - 1)); i -= 1; j -= 1
        elif b == "u":
            out.append((i - 1, None)); i -= 1
        else:
            out.append((None, j - 1)); j -= 1
    return list(reversed(out)) + list(reversed(tail))


def make_score(conf, types, seed):
    if conf is None:
        return lambda c, t: 3.0 if seed.get(c) == t else -1.5
    tot_c = {c: sum(v.values()) for c, v in conf.items()}
    nt = len(types)

    def score(c, t):
        v = conf.get(c)
        if not v:
            return 3.0 if seed.get(c) == t else -1.5
        p = (v.get(t, 0) + 0.2) / (tot_c[c] + 0.2 * nt)
        return math.log(p * nt)          # log-odds against a uniform guess
    return score


def run_pass(pas, seqs, boxes, lines, by_line, types, seed):
    conf = None
    for _ in range(ROUNDS):
        score = make_score(conf, types, seed)
        newconf = defaultdict(Counter)
        results = []
        for (crop, ln), codes in sorted(seqs.items()):
            if crop not in boxes:
                continue
            li, sigs = window(crop, ln, boxes[crop], lines, by_line)
            if li is None or not sigs:
                results.append((crop, ln, li, codes, sigs, [(k, None) for k in range(len(codes))]))
                continue
            al = align(codes, sigs, score)
            results.append((crop, ln, li, codes, sigs, al))
            for a, b in al:
                if a is not None and b is not None:
                    newconf[codes[a][0]][sigs[b]["type"]] += 1
        conf = newconf
    return results, conf


def main():
    rows, lines, by_line = load_signs()
    types = sorted({r["type"] for r in rows})
    boxes = crop_boxes()
    reads = {"A": defaultdict(list), "B": defaultdict(list)}
    covered = {"A": set(), "B": set()}
    extra = []
    confs = {}
    for pas, seed in (("A", SEED_A), ("B", SEED_B)):
        seqs = load_pass(pas)
        results, conf = run_pass(pas, seqs, boxes, lines, by_line, types, seed)
        confs[pas] = conf
        for crop, ln, li, codes, sigs, al in results:
            # coverage: the span of segmented signs between the first and last aligned sign
            idx = [b for a, b in al if a is not None and b is not None]
            if idx:
                for k in range(min(idx), max(idx) + 1):
                    covered[pas].add(sigs[k]["n"])
            for a, b in al:
                if a is not None and b is not None:
                    reads[pas][sigs[b]["n"]].append(codes[a][0])
                elif a is not None:
                    prev = next((sigs[bb]["n"] for aa, bb in reversed(al[:al.index((a, b))]) if bb is not None), "")
                    extra.append((pas, crop, ln, codes[a][1], codes[a][0], li if li is not None else "", prev))
        with open(os.path.join(HERE, f"confusion_{pas}.tsv"), "w") as f:
            f.write("code\ttotal\t" + "\t".join(types) + "\n")
            for c in sorted(conf, key=lambda c: -sum(conf[c].values())):
                f.write(f"{c}\t{sum(conf[c].values())}\t" + "\t".join(str(conf[c].get(t, 0)) for t in types) + "\n")
    with open(os.path.join(HERE, "alignment.tsv"), "w") as f:
        f.write("n\tpage\tline\tx\ttype\td1\tpassA\tpassB\n")
        for r in rows:
            out = []
            for pas in "AB":
                if reads[pas].get(r["n"]):
                    out.append("|".join(reads[pas][r["n"]]))
                elif r["n"] in covered[pas]:
                    out.append("-")
                else:
                    out.append(".")
            f.write(f"{r['n']}\t{r['page']}\t{r['line']}\t{r['x']}\t{r['type']}\t{r['d1']}\t{out[0]}\t{out[1]}\n")
    with open(os.path.join(HERE, "pass_extra.tsv"), "w") as f:
        f.write("pass\tcrop\tline_no\tpass_row\tcode\tpage_line\tafter_sign_n\n")
        for e in extra:
            f.write("\t".join(str(v) for v in e) + "\n")
    print(json.dumps({p: {c: dict(confs[p][c].most_common(3)) for c in sorted(confs[p], key=lambda c: -sum(confs[p][c].values()))[:45]} for p in "AB"}, ensure_ascii=False)[:6000])


if __name__ == "__main__":
    main()
