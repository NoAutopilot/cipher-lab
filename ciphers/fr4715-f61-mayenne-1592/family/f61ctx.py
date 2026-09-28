#!/usr/bin/env python3
"""F61-FAMILY-3, campaign step H33 (28 Sept 2026): resolve the grade-M pair tokens of the period-key skeleton of f.61r by
context -- one blind Opus TEXT call in the H16 shape (scripts/f61judge.py), the key withheld, with the same 20-permutation
control, the positive control on the known span lines FIRST. Pre-registered before any call.

`build TAG` writes the candidate sets a judge sees and the withheld key:
  passes/f61ctx_<TAG>_sets.txt   21 sets in a shuffled order (seed 7): set 0 = the period key (family/key_period_v3.tsv,
                                 pairs n >= 2 and n >= 0.1 x the leaf class total, EBR_A/EBR_B folded into EBR -- exactly
                                 decode_period.py's rule), each sign written as its period letter set [e/r/o] (one letter
                                 when the class has one); a class with no period pair is written ? (an unread sign, any
                                 letter); sets 1-20 = the same letter sets permuted across the covered classes (seed 1).
  passes/f61ctx_<TAG>_key.json   the map behind each label -- never shown to the judge.
  TAG known: the six span lines of scripts/passA_classes.tsv (the H16 positive control lines; Tomokiyo's readings withheld).
  TAG full:  every line of f.61r the decode uses (passA_classes.tsv + passU2_classes.tsv L02/L04/L10).
`score TAG` reads the judge's TSV passes/f61ctx_<TAG>_verdict.tsv (label, score_0_10, reading) and reports the target's
rank among 21 (ties against the target). Gate: rank 1 of 21 (p = 1/21 = 0.048 under the null that the judge cannot tell).
The known control must PASS before the full set is built and judged; a full-set PASS makes the judge's reading of the
target set the context decode, written by `decode` to family/f61_decode_period_v3_ctx.txt with per-token grades: C/C+ as
in decode_period.py (the period key gives one letter), M-ctx (a period pair resolved by the judge, with the pair shown),
? (no period pair: the judge's letter is a guess, grade I). Still not a reading of the letter (rule 10): a skeleton whose
pair choices a verifier can check against the sets file.
  python3 f61ctx.py build known|full
  python3 f61ctx.py score known|full
  python3 f61ctx.py decode          (from the family folder)
"""
import csv, json, os, random, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); S = os.path.abspath(f"{HERE}/../scripts"); P = f"{HERE}/passes"
KEYFILE = f"{HERE}/key_period_v3.tsv"; FRAC = 0.1
# H57 (28 Sept 2026, runner session_01J8hunWPcE7QYcpCx59CUHV, the parent's row): --h26-split relabels f.61's signs by H26's blind
# sort (scripts/f61qo2.py: group-G2 signs and every f.61 DBL -> SBS) and gives SBS the cell b/o (H26/H51: 6/6 and 7/7 under
# Tomokiyo's b/o letters, a controlled fit) while PHI on this leaf becomes e/r (its period 'o' counts are the side-by-side glyph
# the family readers folded into PHI, KEY.md); --published-zhook adds ZHOOK = i/x from key_published_rare.tsv (Tomokiyo,
# labelled published, never a period pair). Tags gain the suffix '2' (known2, full2). Without the options every H33 output is
# reproduced byte for byte. Pre-registered before the H57 calls.
SPLIT = "--h26-split" in sys.argv; PUBZ = "--published-zhook" in sys.argv
def load_key():
    rows = [r for r in csv.DictReader((l for l in open(KEYFILE) if not l.startswith("#")), delimiter="\t")]
    tot = defaultdict(int); key = defaultdict(dict); leaves = defaultdict(lambda: defaultdict(set))
    for r in rows:
        if r["letter"] != "-": tot[(r["class"], r["leaf"])] += int(r["n"])
    for r in rows:
        cl = {"EBR_A": "EBR", "EBR_B": "EBR"}.get(r["class"], r["class"])
        if r["letter"] != "-" and int(r["n"]) >= 2 and int(r["n"]) >= FRAC * tot[(r["class"], r["leaf"])]:
            key[cl][r["letter"]] = key[cl].get(r["letter"], 0) + int(r["n"]); leaves[cl][r["letter"]].add(r["leaf"])
    out = {c: "/".join(sorted(v, key=lambda k: -v[k])) for c, v in key.items()}
    if SPLIT:
        out["SBS"] = "b/o"; leaves["SBS"]["b"].add("H26/H51 fit"); leaves["SBS"]["o"].add("H26/H51 fit")
        if "PHI" in out: out["PHI"] = "/".join(l for l in out["PHI"].split("/") if l != "o")
    if PUBZ:
        out["ZHOOK"] = "i/x"; leaves["ZHOOK"]["i"].add("published (Tomokiyo)"); leaves["ZHOOK"]["x"].add("published (Tomokiyo)")
    return out, leaves
def read_lines(tag):
    lines = defaultdict(list)
    for path in ([f"{S}/passA_classes.tsv"] if tag == "known" else [f"{S}/passA_classes.tsv", f"{S}/passU2_classes.tsv"]):
        for r in csv.DictReader((l for l in open(path) if not l.startswith("#")), delimiter="\t"):
            lines[r["line"]].append(r["sign"])
    if SPLIT:
        sys.path.insert(0, S); import f61qo2
        for line, seq in lines.items():
            for j, c in enumerate(seq):
                if c in ("PHI", "DBL") and (f61qo2.G.get((line, j + 1)) == "G2" or c == "DBL"): seq[j] = "SBS"
    return dict(sorted(lines.items()))
def maps(base):
    labs = sorted(base); rng = random.Random(1); out = [dict(base)]
    for _ in range(20):
        v = [base[l] for l in labs]; rng.shuffle(v); out.append(dict(zip(labs, v)))
    return out
def render(lines, cmap):
    return {line: " ".join((f"[{cmap[c]}]" if "/" in cmap[c] else cmap[c]) if c in cmap else "?" for c in seq) for line, seq in lines.items()}
def build(tag):
    base, _ = load_key(); lines = read_lines(tag); ms = maps(base)
    if SPLIT or PUBZ: tag = tag + "2"
    order = list(range(21)); random.Random(7).shuffle(order); key = {}; txt = []
    for k, mi in enumerate(order):
        lab = f"SET-{k+1:02d}"; key[lab] = {"map_index": mi, "target": mi == 0, "map": ms[mi]}
        txt.append(f"== {lab}"); txt += [f"{line}: {s}" for line, s in render(lines, ms[mi]).items()]
    open(f"{P}/f61ctx_{tag}_sets.txt", "w").write("\n".join(txt) + "\n"); json.dump(key, open(f"{P}/f61ctx_{tag}_key.json", "w"), indent=1)
    print(tag, "sets written;", len(lines), "lines;", sum(len(v) for v in lines.values()), "signs; target is", [l for l, v in key.items() if v["target"]][0], "(withheld)")
def score(tag):
    key = json.load(open(f"{P}/f61ctx_{tag}_key.json")); rows = [r for r in csv.DictReader(open(f"{P}/f61ctx_{tag}_verdict.tsv"), delimiter="\t")]
    sc = {r["label"]: float(r["score_0_10"]) for r in rows}; tl = [l for l, v in key.items() if v["target"]][0]
    rank = 1 + sum(1 for l, s in sc.items() if l != tl and s >= sc[tl])
    out = [f"{tag}: target {tl} scored {sc[tl]}; rank {rank} of 21 (ties against the target)",
           "all scores: " + " ".join(f"{l}:{sc[l]:g}" for l in sorted(sc, key=lambda l: -sc[l])),
           "target reading as given by the judge: " + next(r["reading"] for r in rows if r["label"] == tl),
           f"GATE H33 ({tag}): rank {rank} of 21 -> {'PASS' if rank == 1 else 'FAIL'}"]
    open(f"{P}/f61ctx_{tag}_result.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
def decode():
    base, leaves = load_key(); lines = read_lines("full"); key = json.load(open(f"{P}/f61ctx_full_key.json"))
    tl = [l for l, v in key.items() if v["target"]][0]; rows = [r for r in csv.DictReader(open(f"{P}/f61ctx_full_verdict.tsv"), delimiter="\t")]
    reading = next(r["reading"] for r in rows if r["label"] == tl).split("|"); reading = [x.strip() for x in reading]
    assert len(reading) == len(lines), (len(reading), len(lines))
    tot = defaultdict(int); text = []; tsv = ["line\tpos\tclass\tperiod_letters\tjudge_letter\tgrade"]
    for (line, seq), rd in zip(lines.items(), reading):
        rd = rd.replace(" ", ""); out = []
        if len(rd) != len(seq): print(f"WARNING {line}: judge gave {len(rd)} letters for {len(seq)} signs"); rd = (rd + "?" * len(seq))[:len(seq)]
        for i, (c, ch) in enumerate(zip(seq, rd), 1):
            ls = base.get(c, "")
            if not ls: g = "I"
            elif "/" in ls: g = "M-ctx" if ch in ls.split("/") else "M-ctx!"
            else: g = "C+" if len(leaves[c][ls]) >= 2 else "C"
            tot[g] += 1; tsv.append(f"{line}\t{i}\t{c}\t{ls or '-'}\t{ch}\t{g}")
            out.append(ch if g in ("C", "C+") else (f"{ch}[{ls}]" if g.startswith("M") else f"{ch}?"))
        text.append(f"{line}: " + " ".join(out))
    hdr = (f"# f.61r under key_period_v3.tsv with the grade-M pairs resolved by context by a blind Opus text judge (H33, F61-FAMILY-3, 28 Sept 2026; "
           f"sets in passes/f61ctx_full_sets.txt, verdict passes/f61ctx_full_verdict.tsv, control passes/f61ctx_known_result.txt): "
           f"{sum(tot.values())} signs, " + ", ".join(f"{g} {n}" for g, n in sorted(tot.items())) + ". x[e/r] = the judge's choice within the period pair; x? = no period pair, the judge's guess (grade I). Not a reading of the letter (rule 10).\n")
    open(f"{HERE}/f61_decode_period_v3_ctx.txt", "w").write(hdr + "\n".join(text) + "\n"); open(f"{HERE}/f61_decode_period_v3_ctx.tsv", "w").write("\n".join(tsv) + "\n")
    print(hdr + "\n".join(text))
if __name__ == "__main__":
    {"build": lambda: build(sys.argv[2]), "score": lambda: score(sys.argv[2]), "decode": decode}[sys.argv[1]]()
