#!/usr/bin/env python3
"""Rule-3 controls for key_153 (WVO-153-KEY-2, 10 Oct 2026). Prints both numbers side by side; --check exits 1 if the
committed controls_153.txt is stale.

(a) Shuffle-consistency (the bSZL statistic): share of valued tokens whose witness value equals their class's majority
    value, against the same share after the values are shuffled across tokens (10000 draws, seed 153). The shuffle
    moves values between classes, so the control can differ from the real figure (CLAUDE.md rule 3, orthogonality).
(b) Concordance: for each class of key_153 that maps to a class of an earlier key, does the value agree? Map to key_98
    by shape name (key_98's own readers wrote Sb as '6', Z as '2', Or as '+'/theta, N as 'v', NOTES.md:758; the other
    names are this worker's eye from key_98's legend names, not an image comparison: logged as such). key_74 and key_53
    are mapped by digit identity only (their letter-like signs carry other names). Null: key_153's values permuted among
    its mapped classes, 10000 draws, p95 of matches. A shared key is a test result: matched/total and p95 side by side.
"""
import collections, csv, random, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOP = HERE.parent
OUT = HERE / "controls_153.txt"
N = 10000

MAP98 = {"0": "0", "1": "1", "3": "3", "4": "4", "5": "5", "8": "8", "9": "9", "6": "Sb", "2": "Z", "TH": "Or",
         "v": "N", "L": "L", "Lm": "Lf", "dT": "D", "d": "D", "dD": "Td", "q": "Pf", "g": "Qg", "phi": "Dp", "vb": "Pb",
         "V": "V", "st": "Ma", "S": "S", "Zb": "Yz", "M": "M", "K": "K", "B": "B"}


def rows(p):
    with open(p, encoding="utf-8") as f:
        return [r for r in csv.DictReader((l for l in f if not l.startswith("#")), delimiter="\t")]


def norm(v):
    return v.lower().replace("v", "u") if len(v) == 1 else v.lower()


def run():
    out = []
    rng = random.Random(153)
    ct = [r for r in rows(TOP / "ciphertext_153.tsv") if r["value"] not in ("-", "") and r["sign"] != "."]
    cls = [r["sign"] for r in ct]
    vals = [r["value"] for r in ct]

    def consistency(vs):
        by = collections.defaultdict(collections.Counter)
        for c, v in zip(cls, vs):
            by[c][v] += 1
        return sum(cnt.most_common(1)[0][1] for cnt in by.values()) / len(vs)

    real = consistency(vals)
    sh = []
    for _ in range(N):
        v2 = vals[:]; rng.shuffle(v2); sh.append(consistency(v2))
    sh.sort()
    out.append(f"(a) shuffle-consistency, all valued tokens N={len(vals)}: real {real:.3f} | shuffled mean "
               f"{sum(sh)/N:.3f} p95 {sh[int(.95*N)]:.3f} max {sh[-1]:.3f} -> {'PASS' if real > sh[int(.95*N)] else 'FAIL'}")
    allsig = [r for r in rows(TOP / "ciphertext_153.tsv") if r["sign"] not in (".", "Zh", "Me", "e", "C16")]
    withheld = len(allsig) - len(vals)
    out.append(f"    withheld tokens (value '-', cipher spelling differs from the witnesses) counted as misses: real "
               f"{real * len(vals) / len(allsig):.3f} over N={len(allsig)} ({withheld} withheld) | same shuffled p95 {sh[int(.95*N)]:.3f}")
    cg = [(c, v) for r, c, v in zip(ct, cls, vals) if r["grade"] == "C"]
    cls_c, vals_c = [c for c, _ in cg], [v for _, v in cg]
    cls_bak = cls[:]
    cls[:] = cls_c
    real_c = consistency(vals_c)
    shc = []
    for _ in range(N):
        v2 = vals_c[:]; rng.shuffle(v2); shc.append(consistency(v2))
    shc.sort()
    cls[:] = cls_bak
    out.append(f"    C-graded tokens only N={len(vals_c)}: real {real_c:.3f} | shuffled mean {sum(shc)/N:.3f} "
               f"p95 {shc[int(.95*N)]:.3f}")

    k153 = {r["sign"]: r["value"] for r in rows(TOP / "key_153.tsv") if r["grade"] == "C"}
    pre = {k: MAP98[k] for k in ("0", "1", "3", "4", "5", "8", "9", "6", "2", "TH", "v")}
    for name, mapping in (("key_98", MAP98), ("key_98 [pre-fixed map: digits + 98's own reader labels only]", pre),
                          ("key_74", None), ("key_53", None)):
        other = {r["sign"]: r["value"] for r in rows(TOP / f"{name.split()[0]}.tsv")}
        pairs = []
        for s, v in k153.items():
            o = (mapping or {}).get(s) if mapping else (s if s.isdigit() else None)
            if o and o in other:
                pairs.append((s, v, other[o]))
        if not pairs:
            out.append(f"(b) {name}: no mapped classes"); continue
        ours = [norm(v) for _, v, _ in pairs]
        theirs = [{norm(x) for x in t.split("|")} for _, _, t in pairs]
        match = sum(a in b for a, b in zip(ours, theirs))
        null = []
        for _ in range(N):
            p = ours[:]; rng.shuffle(p); null.append(sum(a in b for a, b in zip(p, theirs)))
        null.sort()
        p95 = null[int(.95 * N)]
        miss = [f"{s}={v}/{t}" for s, v, t in pairs if norm(v) not in {norm(x) for x in t.split('|')}]
        out.append(f"(b) key_153 vs {name}: {match}/{len(pairs)} classes same value | permuted p95 {p95} "
                   f"-> {'PASS' if match > p95 else 'FAIL'}; differ: {', '.join(miss) or 'none'}")
    return "\n".join(out) + "\n"


def main():
    s = run()
    if "--check" in sys.argv:
        if not OUT.exists() or OUT.read_text() != s:
            print("STALE: controls_153.txt"); sys.exit(1)
        print("check OK"); print(s, end=""); return
    OUT.write_text(s); print(s, end="")


if __name__ == "__main__":
    main()
