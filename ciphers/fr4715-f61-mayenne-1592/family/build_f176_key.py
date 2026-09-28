#!/usr/bin/env python3
"""H177 (runner 6, 28 Sept 2026): period key rows for fr.3984 f.176r from its separate-sheet decipherment fol. 177r (H175 PASS).
f.176r has no clear anchors, so align_separate.py's anchor split does not apply. Design, fixed before the stage-1 passes were read:
 1. Signs: for each row, blind passes A and B are aligned by difflib on their sign sequences; a column where A == B keeps the sign,
    any other column becomes '?' (never matches, never yields a key row). PLAIN dropped.
 2. Clear: the blind reads of fol. 177r (passes/f177r_clearA_*.tsv, in line order; L01's salutation up to the first '/' dropped),
    folded as h170_gate.py folds; trimmed to N = floor(0.8 x signs) so the DP (global on the letters) cannot run past the cipher.
 3. Alignment: F61-CAL's DP (scripts/f61crib.align) with key v4's letter SETS (h170_gate.load_key) as the only match criterion:
    v4 decides WHERE signs and letters line up, never WHICH letter of a set, and a class outside v4 (the rare classes) takes the
    letter the DP puts opposite it on a diagonal step.
 4. Rows: every diagonal pair (consensus sign, letter) -> counts per (class, letter); key_period_f176.tsv (class, letter, n, leaf,
    bands) with leaf 'fr.3984 f.176r/f.177r' and bands = 'DP stage <rows>'.
 5. Control (the same pipeline, wrong clear): fr.3984 f.184r's clear from word 0, same N. Reported per class beside the true run:
    a class's letters under the wrong text show what the alignment forces by itself (v4-set letters for covered classes, noise for
    rare ones); a rare-class letter is reported only where the true run's top letter has n >= 3 and exceeds the wrong run's count
    for that letter.
Grade C for pairs whose letter is in the class's v4 set (period decipherment, set-anchored); rare-class letters are C- candidates for a
verifier, never merged here.  python3 build_f176_key.py ROWS [--check]   (ROWS e.g. L01-L12; reads passes/f176r_signs{A,B}_*.tsv)"""
import difflib, glob, os, re, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.abspath(f"{HERE}/../scripts"))
import h170_gate as g
from f61crib import align
P = f"{HERE}/passes"; LEAF = "fr.3984 f.176r/f.177r"; RARE = ("CA", "CROSS", "LL", "LOOPBAR", "ZHOOK")
def pass_rows(tag):
    rows = defaultdict(list)
    for f in sorted(glob.glob(f"{P}/f176r_signs{tag}_*.tsv")):
        for r in g.rd(f):
            s = {"EBR_A": "EBR", "EBR_B": "EBR"}.get(r["sign"].strip(), r["sign"].strip())
            if s != "PLAIN": rows[r["line"]].append(s)
    return rows
def consensus(a, b):
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == "equal": out += a[i1:i2]
        elif op == "replace" and i2 - i1 == j2 - j1: out += [f"?{x}|{y}" for x, y in zip(a[i1:i2], b[j1:j2])]   # H178: 1:1 disputes keep their pair
        else: out += ["?"] * max(i2 - i1, j2 - j1)
    return out
def clear_text():
    files = sorted(glob.glob(f"{P}/f177r_clearA_*.tsv")); lines = {}
    for f in files:
        for r in g.rd(f): lines.setdefault(r["line"], r["text"])
    order = sorted(lines, key=lambda l: int(l[1:])); t = ""
    for l in order:
        x = lines[l]
        if l == "L01": x = x.split("/", 1)[1] if "/" in x else x
        t += g.fold(x)
    return t, order
DISP = {"true": defaultdict(Counter), "wrong": defaultdict(Counter)}
def run(seq, text, key, tag):
    _, pairs = align(text, seq, key); c = defaultdict(Counter); m = 0
    for i, j in pairs:
        s = seq[j]
        if s.startswith("?"):
            if s != "?": DISP[tag][tuple(sorted(s[1:].split("|")))][text[i]] += 1
            continue
        c[s][text[i]] += 1; m += text[i] in key.get(s, ())
    return c, m / len(text)
def main():
    lo, hi = [int(x) for x in re.findall(r"\d+", sys.argv[1])]; want = [f"L{k:02d}" for k in range(lo, hi + 1)]
    A, B = pass_rows("A"), pass_rows("B"); missing = [l for l in want if l not in A or l not in B]
    if missing: sys.exit(f"missing rows in the passes: {missing}")
    seq = [s for l in want for s in consensus(A[l], B[l])]; key = g.load_key()
    text, order = clear_text(); N = min(len(text), int(0.8 * len(seq)))
    w184 = g.fold(" ".join(r["word"] for r in g.rd(f"{P}/f184r_clear_rec.tsv")))[:N]
    ct, ft = run(seq, text[:N], key, "true"); cw, fw = run(seq, w184, key, "wrong")
    out = [f"rows {want[0]}-{want[-1]}: {len(seq)} signs, consensus {sum(not s.startswith('?') for s in seq)} ({sum(not s.startswith('?') for s in seq)/len(seq):.2f}); "
           f"clear lines {order[0]}-{order[-1]}, {len(text)} letters, N {N}",
           f"whole-stretch match: fol. 177r {ft:.3f} vs wrong f.184r {fw:.3f} (margin {ft - fw:+.3f})", "",
           "class\tv4 set\ttrue: letters (n)\twrong: letters (n)\tin-set share true / wrong"]
    for c in sorted(set(ct) | set(cw), key=lambda c: -sum(ct[c].values())):
        vs = key.get(c, ()); nt = sum(ct[c].values()); nw = sum(cw[c].values())
        st = sum(ct[c][x] for x in vs) / nt if nt else 0; sw = sum(cw[c][x] for x in vs) / nw if nw else 0
        fmt = lambda C: " ".join(f"{x}{n}" for x, n in C.most_common(6))
        out.append(f"{c}\t{'/'.join(vs) or '-'}\t{fmt(ct[c])} ({nt})\t{fmt(cw[c])} ({nw})\t{st:.2f} / {sw:.2f}")
    out.append("")
    for c in RARE:
        if ct[c]:
            x, n = ct[c].most_common(1)[0]; ok = n >= 3 and n > cw[c][x]
            out.append(f"rare {c}: true top {x} {n} of {sum(ct[c].values())}, wrong-text count of {x} {cw[c][x]} -> {'candidate' if ok else 'not reported'}")
    out.append(""); out.append("H178: letters opposite 1:1 disputed columns (A code | B code), true / wrong, pairs with n >= 3 under the true text")
    for pr, C in sorted(DISP["true"].items(), key=lambda x: -sum(x[1].values())):
        if sum(C.values()) >= 3:
            W = DISP["wrong"][pr]; fmt = lambda C: " ".join(f"{x}{n}" for x, n in C.most_common(6))
            out.append(f"{pr[0]}|{pr[1]}\t{fmt(C)} ({sum(C.values())})\t{fmt(W)} ({sum(W.values())})")
    rows = [f"{c}\t{x}\t{n}\t{LEAF}\tDP stage {want[0]}-{want[-1]}" for c in sorted(ct) for x, n in ct[c].most_common()]
    tsv = ("# key_period_f176.tsv -- H177 (runner 6), build_f176_key.py " + sys.argv[1] + ": set-anchored DP pairs, consensus signs only; "
           "key source period; NOT merged into v4 (a verifier's)\nclass\tletter\tn\tleaf\tbands\n" + "\n".join(rows) + "\n")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/build_f176_key_result.txt"; kf = f"{HERE}/key_period_f176.tsv"
    if "--check" in sys.argv:
        ok = open(res).read() == txt and open(kf).read() == tsv; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); open(kf, "w").write(tsv); print(txt, end="")
if __name__ == "__main__": main()
