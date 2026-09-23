#!/usr/bin/env python3
"""Derive symbol values from the interlinear gloss of Dupuy 468 f.28 (step 3 of the brief).

For every gloss item word@i-j in ciphertext.txt, take the cipher tokens under it (plain tokens dropped) and the
gloss word normalised (lower case, j->i, v->u, ae/oe->e, letters only; '_' joins a two-word gloss). If the
number of letter tokens equals the number of gloss letters, each token gets the aligned letter (one vote).
A span of a single word-sign token (K, F, O, PW, o, ...) under a whole word gets that word as a word-sign vote.
Spans whose lengths differ are listed as 'unaligned' and give no vote. Writes key_from_gloss.tsv (every vote,
with line and position) and prints the per-symbol tally, flagging any symbol with conflicting votes.
Written 23 Sept 2026. Usage: python3 key_from_gloss.py
"""
import os
import re
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
WORDSIGNS = {"K", "F", "O", "PW", "o", "g", "HHH", "SX", "Y~", "ß"}


def norm(w):
    w = w.lower().replace("j", "i").replace("v", "u").replace("ae", "e").replace("oe", "e")
    return re.sub(r"[^a-z_]", "", w)


def main():
    votes, unaligned = [], []
    items = []  # (line, gloss item, word, [(pos, token)])
    for l in open(os.path.join(HERE, "ciphertext.txt"), encoding="utf-8"):
        if l.startswith("#") or not l.strip():
            continue
        p = l.rstrip("\n").split("\t") + ["", ""]
        ln, toks, gl = p[0], p[1].split(), p[2]
        for g in gl.split():
            w, _, span = g.rpartition("@")
            a, _, b = span.partition("-")
            a, b = int(a), int(b or a)
            pt = [(ln, i, toks[i - 1]) for i in range(a, b + 1)
                  if i <= len(toks) and not toks[i - 1].startswith("[PLAIN")]
            items.append((ln, g, w, pt))
    # a word split over a line end is glossed twice (end of line n, start of line n+1): join the two spans
    merged, k = [], 0
    while k < len(items):
        ln, g, w, pt = items[k]
        if k + 1 < len(items) and items[k + 1][2] == w and items[k + 1][0] != ln and pt and items[k + 1][3]:
            merged.append((ln + "+" + items[k + 1][0], g + "+" + items[k + 1][1], w, pt + items[k + 1][3]))
            k += 2
            continue
        merged.append((ln, g, w, pt))
        k += 1
    for ln, g, w, pt in merged:
        cip = [t for _, _, t in pt]
        word = norm(w).replace("_", "")
        if not cip or "?" in w:
            unaligned.append((ln, g, " ".join(cip), "illegible or over clear words"))
            continue
        if len(cip) == 1 and cip[0] in WORDSIGNS:
            votes.append((pt[0][0], pt[0][1], cip[0], "=" + word, w))
        elif len(cip) == len(word):
            for (l2, i, t), c in zip(pt, word):
                votes.append((l2, i, t, c, w))
        else:
            unaligned.append((ln, g, " ".join(cip), f"{len(cip)} tokens vs {len(word)} letters"))
    with open(os.path.join(HERE, "key_from_gloss.tsv"), "w", encoding="utf-8") as f:
        f.write("# one row per glossed cipher token whose gloss word aligns letter for letter (or a word sign)\n")
        f.write("line\tpos\ttoken\tvalue\tgloss\n")
        for v in votes:
            f.write("\t".join(map(str, v)) + "\n")
        f.write("# unaligned gloss items (no vote)\n")
        for u in unaligned:
            f.write("# " + "\t".join(u) + "\n")
    tally = defaultdict(Counter)
    for _, _, t, c, _ in votes:
        tally[t][c] += 1
    print(f"{len(votes)} votes from aligned glosses; {len(unaligned)} gloss items unaligned")
    for t in sorted(tally, key=lambda k: -sum(tally[k].values())):
        c = tally[t]
        flag = ""
        if len(c) > 1 and not all(v.startswith("=") for v in c):
            top = c.most_common(1)[0][0]
            flag = "   <-- minority: " + "; ".join(f"{l}:{i} {v} ({w})" for l, i, tt, v, w in votes
                                                 if tt == t and v != top)
        print(f"{t:6s} {dict(c.most_common())}{flag}")
    for u in unaligned:
        print("unaligned:", *u)


if __name__ == "__main__":
    main()
