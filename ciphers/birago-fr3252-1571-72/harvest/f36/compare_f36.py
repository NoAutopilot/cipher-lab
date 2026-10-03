#!/usr/bin/env python3
"""F36-READ (3 Oct 2026): reconcile two blind passes of fr.3252 f.36-37 (sign id + the clerk's interlinear gloss letter),
decode the reconciled signs under the printed Ceppo-Nevers key, and compare them with the period gloss token by token.

  python3 compare_f36.py            # writes recon.tsv, passD.tsv (for decode_control.py), compare.tsv, reading_*.txt
  python3 compare_f36.py --check    # exit 1 if the committed outputs are stale (rule 7)

Inputs: passA_{r36,v36}.tsv, passB_{r36,v36}.tsv (columns passage pos sign_id alt conf gloss gconf note),
../../../ceppo-nevers-fr3251-1570s/harvest/sign_id_map.json (S## -> printed value; the readers never saw it), plus
X_THETA2=r (HARVEST-D, f.36v period gloss). Runs split by prose (r36_L05.1/.2) are joined per line before alignment.
Per sign: the two passes' sign ids are aligned (difflib on the id strings); agree -> that id; one '?' -> the other;
disagree -> '?' (unsettled; both kept in recon.tsv). Gloss: agree -> that letter; one '?'/'-' -> the other (gconf M);
disagree -> '?'.
Grades per decoded token (CLAUDE.md rule 4): C = printed value equals the agreed period gloss; M = everything else
(gloss disagrees, gloss absent, or sign unsettled). S would need key + control reading beyond the gloss; the gloss
covers the cipher, so S is used only where the gloss is absent and the key value fits a word the gloss already gives.
"""
import csv, difflib, json, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAP = HERE.parents[2] / "ceppo-nevers-fr3251-1570s/harvest/sign_id_map.json"
EXTRA = {"X_THETA2": "r"}


def load(p):
    rows = {}
    for r in csv.DictReader(open(p), delimiter="\t"):
        line = r["passage"].split(".")[0].strip()
        rows.setdefault(line, []).append(r)
    return rows


def norm_g(g):
    g = (g or "").strip().lower()
    return g if g else "-"


def main(check=False):
    m = {e["id"]: e["value"] for e in json.load(open(MAP))}
    m.update(EXTRA)
    A, B = {}, {}
    for pg in ("r36", "v36"):
        A.update(load(HERE / f"passA_{pg}.tsv")); B.update(load(HERE / f"passB_{pg}.tsv"))
    out = {}
    recon = ["line\tpos\tA\tB\tsign\tgA\tgB\tgloss\tprinted\tgrade"]
    passd = ["passage\tpos\tsign_id"]
    stats = Counter()
    order = sorted(set(A) | set(B), key=lambda k: (k.split("_")[0] != "r36", k))
    order = [k for k in order if k.startswith("r36")] + [k for k in order if k.startswith("v36top")] + \
        [k for k in order if k.startswith("v36mid")] + [k for k in order if k.startswith("r37")]
    gl_lines, dec_lines, cmp_lines = [], [], []
    for line in order:
        a, b = A.get(line, []), B.get(line, []); ia = [r["sign_id"].strip() for r in a]; ib = [r["sign_id"].strip() for r in b]
        sm = difflib.SequenceMatcher(None, ia, ib, autojunk=False)
        pairs = []
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == "equal" or (op == "replace" and i2 - i1 == j2 - j1):
                pairs += [(a[i], b[j]) for i, j in zip(range(i1, i2), range(j1, j2))]
            else:
                n = max(i2 - i1, j2 - j1)
                for k in range(n):
                    pairs.append((a[i1 + k] if i1 + k < i2 else None, b[j1 + k] if j1 + k < j2 else None))
        pos = 0; gtxt = dtxt = ""
        for ra, rb in pairs:
            pos += 1
            sa = ra["sign_id"].strip() if ra else ""; sb = rb["sign_id"].strip() if rb else ""
            ga = norm_g(ra["gloss"]) if ra else ""; gb = norm_g(rb["gloss"]) if rb else ""
            if sa == sb: s = sa; stats["sign_agree"] += 1
            elif sa in ("", "?"): s = sb or "?"; stats["sign_one"] += 1
            elif sb in ("", "?"): s = sa; stats["sign_one"] += 1
            else: s = "?"; stats["sign_split"] += 1
            if ga == gb: g = ga; stats["gloss_agree"] += 1
            elif ga in ("", "?", "-"): g = gb or "?"; stats["gloss_one"] += 1
            elif gb in ("", "?", "-"): g = ga; stats["gloss_one"] += 1
            else: g = "?"; stats["gloss_split"] += 1
            v = m.get(s, "?") if s not in ("?", "") else "?"
            if v == "null":
                grade = "null"
            elif v != "?" and g not in ("?", "-", "") and v == g:
                grade = "C"
            else:
                grade = "M"
            stats["grade_" + grade] += 1
            if v not in ("?", "null") and g not in ("?", "-", ""):
                stats["cmp_n"] += 1; stats["cmp_match"] += (v == g)
            recon.append(f"{line}\t{pos}\t{sa}\t{sb}\t{s}\t{ga}\t{gb}\t{g}\t{v}\t{grade}")
            passd.append(f"{line}\t{pos}\t{s}")
            gtxt += g if g not in ("-", "") else "."
            dtxt += "" if v == "null" else (v if v != "?" else "_")
        gl_lines.append(f"{line}\t{gtxt}"); dec_lines.append(f"{line}\t{dtxt}")
    files = {"recon.tsv": "\n".join(recon) + "\n", "passD.tsv": "\n".join(passd) + "\n",
             "reading_gloss.txt": "\n".join(gl_lines) + "\n", "reading_key.txt": "\n".join(dec_lines) + "\n"}
    stale = [f for f, t in files.items() if not (HERE / f).exists() or (HERE / f).read_text() != t]
    if check:
        print("stale:" if stale else "OK, not stale", " ".join(stale)); sys.exit(1 if stale else 0)
    for f, t in files.items():
        (HERE / f).write_text(t)
    for k in sorted(stats): print(f"{k}\t{stats[k]}")
    if stats["cmp_n"]:
        print(f"printed key vs agreed gloss: {stats['cmp_match']}/{stats['cmp_n']} = {stats['cmp_match']/stats['cmp_n']:.3f}")
    tot = stats["sign_agree"] + stats["sign_one"] + stats["sign_split"]
    print(f"two-reader sign disagreement: {stats['sign_split']}/{tot} = {stats['sign_split']/tot:.3f} "
          f"(one-sided {stats['sign_one']})")


if __name__ == "__main__":
    main("--check" in sys.argv)
