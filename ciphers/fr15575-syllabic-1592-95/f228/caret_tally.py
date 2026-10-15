#!/usr/bin/env python3
"""SYL-CARET: the no.54 legend mark ^ against the f.228 L01-L04 period gloss (PREREG-SYL-CARET.md).

  python3 caret_tally.py [--seeds 200] [--out caret_tally.tsv] [--check]

Decode stream per line: 2-digit syllable codes -> key_syllabary.tsv value; H-graded header letter signs of
../key_no54.tsv (n=e, :=r, y=r, 9=y, 7=o, x=n, ...) -> their letter; every other token '_' (unkeyed).
Each ^ token gets a candidate value v (a letter, or empty = NULL). The line's decoded letters are LCS-aligned
(tools/decode_witness.lcs_align) to the normalised gloss (gloss_v2.tsv, NV05C normaliser, imported).
T(v) = number of the ^ tokens whose letter v is in the LCS matching.
Null A (primary): ^ tokens set to '_'; v is placed instead at k positions (k = number of ^ tokens) drawn without
replacement from the positions of H-read single-letter signs on L01-L04 (their own value replaced by v), seeds
1..S; statistic = matched count at the drawn positions. Null B (secondary): k extra v tokens inserted at random
token gaps across L01-L04, ^ tokens '_'. Calibration: H single-letter signs at their true values (match share).
--check exits 1 if the committed --out differs from a regeneration (rule 7).
"""
import argparse, csv, os, random, re, string, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "tools"))
sys.path.insert(0, os.path.join(HERE, "..", "control_fr3641"))
from decode_witness import lcs_align  # noqa: E402
from score_control import norm  # noqa: E402

CANDS = ["s", "l"]  # key_no54_legend.tsv rows 2 (s, H) and 9 (l, M)


def load():
    syl = {}
    with open(os.path.join(HERE, "key_syllabary.tsv"), encoding="utf-8") as f:
        for r in csv.reader((l for l in f if not l.startswith("#")), delimiter="\t"):
            if len(r) >= 2 and re.fullmatch(r"\d\d", r[0]):
                syl[r[0]] = norm(r[1])
    let = {}
    with open(os.path.join(HERE, "..", "key_no54.tsv"), encoding="utf-8") as f:
        for r in csv.reader((l for l in f if not l.startswith("#")), delimiter="\t"):
            if len(r) >= 4 and r[2].startswith("letter sign") and r[3] == "H":
                let[r[0]] = norm(r[1])
    lines = {}
    with open(os.path.join(HERE, "ciphertext.tsv"), encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            lines.setdefault(r["line"], []).append((r["sign"].rstrip("?"), r["conf"]))
    with open(os.path.join(HERE, "gloss_v2.tsv"), encoding="utf-8") as f:
        gloss = {r["line"]: norm(r["text"]) for r in csv.DictReader(f, delimiter="\t")}
    return syl, let, lines, gloss


def matched_at(vals, g, watch):
    """vals: list of per-token value strings ('' or '_' allowed). Return count of watch indices whose letters all match."""
    dec, owner = [], []
    for i, v in enumerate(vals):
        for ch in (v or ""):
            dec.append(ch); owner.append(i)
    _, pairs = lcs_align(dec, list(g))
    m = {d for d, _ in pairs}
    ok = {}
    for d, o in enumerate(owner):
        if o in watch:
            ok[o] = ok.get(o, True) and d in m
    return sum(1 for o in watch if ok.get(o))


def base_vals(toks, syl, let):
    return [syl.get(s) or let.get(s) or "_" for s, _ in toks]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--seeds", type=int, default=200)
    ap.add_argument("--out", default=os.path.join(HERE, "caret_tally.tsv"))
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    syl, let, lines, gloss = load()
    L = [ln for ln in sorted(lines) if ln in gloss]
    carets = {ln: [i for i, (s, _) in enumerate(lines[ln]) if s == "^"] for ln in L}
    k = sum(len(v) for v in carets.values())
    single = [(ln, i) for ln in L for i, (s, c) in enumerate(lines[ln]) if s in let and c == "H"]
    out = ["# SYL-CARET (PREREG-SYL-CARET.md): ^ tokens of f.228 L01-L04 vs gloss_v2.tsv; regenerate with caret_tally.py",
           "metric\tvalue", f"caret_tokens\t{k}", f"single_letter_H_positions\t{len(single)}"]
    # calibration: true single-letter values
    cal = 0
    for ln in L:
        vals = base_vals(lines[ln], syl, let)
        vals = ["_" if lines[ln][i][0] == "^" else v for i, v in enumerate(vals)]
        cal += matched_at(vals, gloss[ln], {i for (l2, i) in single if l2 == ln})
    out.append(f"calibration_true_single_letter_matched\t{cal}/{len(single)}")
    # per-position detail for s and l, and T(v) for every letter + NULL
    T = {}
    detail = []
    for v in list(string.ascii_lowercase):
        t = 0
        for ln in L:
            vals = base_vals(lines[ln], syl, let)
            vals = [v if lines[ln][i][0] == "^" else x for i, x in enumerate(vals)]
            for i in carets[ln]:
                hit = matched_at(vals, gloss[ln], {i})
                t += hit
                if v in CANDS:
                    detail.append(f"pos_{ln}_{i + 1}_{v}\t{hit}")
        T[v] = t
    for v in CANDS:
        out.append(f"T_{v}\t{T[v]}")
    # nulls
    for v in CANDS:
        rng = random.Random(1)
        A = []
        for sd in range(1, a.seeds + 1):
            rng = random.Random(sd)
            pick = set(rng.sample(single, k))
            tot = 0
            for ln in L:
                vals = base_vals(lines[ln], syl, let)
                vals = ["_" if lines[ln][i][0] == "^" else x for i, x in enumerate(vals)]
                w = {i for (l2, i) in pick if l2 == ln}
                for i in w:
                    vals[i] = v
                tot += matched_at(vals, gloss[ln], w) if w else 0
            A.append(tot)
        B = []
        for sd in range(1, a.seeds + 1):
            rng = random.Random(10000 + sd)
            gaps = [(ln, j) for ln in L for j in range(len(lines[ln]) + 1)]
            pick = rng.sample(gaps, k)
            tot = 0
            for ln in L:
                vals = base_vals(lines[ln], syl, let)
                vals = ["_" if lines[ln][i][0] == "^" else x for i, x in enumerate(vals)]
                ins = sorted([j for (l2, j) in pick if l2 == ln], reverse=True)
                for j in ins:
                    vals.insert(j, "\x00")
                w = {i for i, x in enumerate(vals) if x == "\x00"}
                vals = [v if x == "\x00" else x for x in vals]
                tot += matched_at(vals, gloss[ln], w) if w else 0
            B.append(tot)
        for nm, arr in (("A", A), ("B", B)):
            s_ = sorted(arr)
            p95 = s_[int(0.95 * len(s_)) - 1]
            out += [f"null{nm}_{v}_mean\t{sum(arr) / len(arr):.3f}", f"null{nm}_{v}_p95\t{p95}",
                    f"null{nm}_{v}_ge_T\t{sum(1 for x in arr if x >= T[v])}"]
        p95A = sorted(A)[int(0.95 * len(A)) - 1]
        out.append(f"gate_beats_nullA_p95_{v}\t{'yes' if T[v] > p95A else 'no'}")
    others = sorted(((T[v], v) for v in string.ascii_lowercase), reverse=True)
    out.append("T_all_letters\t" + " ".join(f"{v}={t}" for t, v in others))
    out += detail
    text = "\n".join(out) + "\n"
    if a.check:
        old = open(a.out, encoding="utf-8").read() if os.path.exists(a.out) else ""
        print("caret_tally.tsv up to date" if old == text else "caret_tally.tsv is stale")
        sys.exit(0 if old == text else 1)
    open(a.out, "w", encoding="utf-8").write(text)
    print(text, end="")


if __name__ == "__main__":
    main()
