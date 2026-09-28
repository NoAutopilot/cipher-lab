#!/usr/bin/env python3
"""F61-FAMILY-5 (28 Sept 2026): place the letters of word-span gloss passes onto the signs of each segment (the letter-aligned
recipe, second form). Input: passes/<OUT>_words<P>_<chunk>.tsv (segment, pos, kind, word, tick_from, tick_to, conf, note) from two
blind passes A and B, sheets/<OUT>_segments.json (classes and v3 sets per tick). Per segment and pass, a dynamic programme
assigns every letter of every gloss word (in order) to one sign, monotonically: a sign takes at most one letter (OTHER, the
word-code sign of this hand, takes any number), a letter inside its word's tick span [from, to] costs 0, one tick outside
costs 1, further 3; a letter that falls in the sign's v3 set scores +1 (a hidden or uncovered position has no set and scores 0
for any letter, so the control positions are placed by the neighbours and the span alone); a letter left unplaced costs 2.
Dashes and struck words place nothing. Output passes/<OUT>_placed_<chunk>.tsv: segment, pos, class, letter_A, letter_B,
agree (A == B), set, hidden; and the control figures: at the hidden positions (v3-covered, shown as ?), the share of placed
letters inside the true set, per pass and where A and B agree; the same at the shown positions; word agreement A vs B.
  python3 place_letters.py OUT CHUNK [--control]"""
import csv, json, os, re, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"
out, chunk = sys.argv[1], sys.argv[2]
J = json.load(open(f"{HERE}/sheets/{out}_segments.json")); by = {s["file"].replace(".jpg", ""): s for s in J["segments"]}
FOLD = {"v": "u", "j": "i"}
def norm(w): return "".join(FOLD.get(c, c) for c in re.sub(r"\[.*?\]", lambda m: m.group(0)[1:-1], w.lower()) if c.isalpha() or c == "?")
def sets_for(seg, control):
    """per tick: the letter set the DP may score with (None where hidden/uncovered), and the true set for scoring"""
    k = len(seg["positions"]); shown = {i: v for i, v in seg["shown"]}; hid = {h[0]: h[2] for h in seg["hidden"]}
    dp = [None] * (k + 1); truth = [None] * (k + 1)
    for i in range(1, k + 1):
        v = shown.get(i, "?")
        if v != "?": dp[i] = set(v.split("/")); truth[i] = dp[i]
        elif i in hid: truth[i] = set(hid[i].split("/"))
    return dp, truth
def place(words, seg, control):
    k = len(seg["positions"]); cls = seg["classes"]; dp, truth = sets_for(seg, control)
    letters = []   # (char, from, to)
    for w in words:
        if w["kind"].strip().lower() in ("dash", "struck") or w["word"].strip() in ("-", ""): continue
        try: f, t = int(w["tick_from"]), int(w["tick_to"])
        except ValueError: f, t = 1, k
        for c in norm(w["word"]): letters.append((c, min(f, t), max(f, t)))
    n = len(letters); NEG = -1e9
    # state: after i letters, last sign used j (0 = none). value = best score; each sign used at most once unless OTHER
    best = [[NEG] * (k + 1) for _ in range(n + 1)]; back = [[None] * (k + 1) for _ in range(n + 1)]; best[0][0] = 0
    for i in range(1, n + 1):
        c, f, t = letters[i - 1]
        for j in range(0, k + 1):
            # skip this letter (unplaced)
            if best[i - 1][j] - 2 > best[i][j]: best[i][j] = best[i - 1][j] - 2; back[i][j] = (j, None)
        for jprev in range(0, k + 1):
            if best[i - 1][jprev] == NEG: continue
            for j in range(max(1, jprev), k + 1):
                if j == jprev and cls[j - 1] != "OTHER": continue
                d = 0 if f <= j <= t else (1 if (j == f - 1 or j == t + 1) else 3)
                s = (1 if (dp[j] and c in dp[j]) else 0) - d
                if best[i - 1][jprev] + s > best[i][j]: best[i][j] = best[i - 1][jprev] + s; back[i][j] = (jprev, j)
    j = max(range(k + 1), key=lambda j: best[n][j]); placed = defaultdict(str); i = n
    while i > 0:
        jprev, jj = back[i][j]
        if jj is not None: placed[jj] = letters[i - 1][0] + placed[jj]
        j = jprev; i -= 1
    return placed, truth
def load(p):
    d = defaultdict(list)
    for r in csv.DictReader(open(f"{P}/{out}_words{p}_{chunk}.tsv"), delimiter="\t"): d[r["segment"].strip()].append(r)
    return d
A, B = load("A"), load("B"); control = "--control" in sys.argv
rows = []; stat = defaultdict(lambda: [0, 0]); wa = wt = 0
for stem in sorted(set(A) | set(B)):
    seg = by.get(stem)
    if not seg: continue
    pa, truth = place(A.get(stem, []), seg, control); pb, _ = place(B.get(stem, []), seg, control)
    hid = {h[0] for h in seg["hidden"]}
    for i, (pos, c) in enumerate(zip(seg["positions"], seg["classes"]), 1):
        la, lb = pa.get(i, "-"), pb.get(i, "-"); ag = la == lb; tr = truth[i]
        kind = "hidden" if i in hid else ("shown" if tr else "free")
        rows.append((stem, pos, c, la, lb, "y" if ag else "n", "/".join(sorted(tr)) if tr else "-", kind))
        if tr:
            for tag, l in (("A", la), ("B", lb)):
                stat[(kind, tag)][1] += 1; stat[(kind, tag)][0] += (l != "-" and l[0] in tr)
            if ag: stat[(kind, "agreed")][1] += 1; stat[(kind, "agreed")][0] += (la != "-" and la[0] in tr)
    import difflib
    a = [norm(w["word"]) for w in A.get(stem, []) if w["kind"] != "dash"]; b = [norm(w["word"]) for w in B.get(stem, []) if w["kind"] != "dash"]
    wa += sum(bl.size for bl in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks()); wt += max(len(a), len(b))
with open(f"{P}/{out}_placed_{chunk}.tsv", "w") as f:
    f.write("segment\tpos\tclass\tletter_A\tletter_B\tagree\tset\tkind\n" + "".join("\t".join(map(str, r)) + "\n" for r in rows))
print(f"word agreement A vs B: {wa}/{wt} = {wa/wt if wt else 0:.3f}")
for kind in ("hidden", "shown"):
    print(kind + ": " + "; ".join(f"{tag} {v[0]}/{v[1]} = {v[0]/v[1]:.3f}" if v[1] else f"{tag} n/a" for tag, v in ((t, stat[(kind, t)]) for t in ("A", "B", "agreed"))))
ag = sum(1 for r in rows if r[5] == "y" and r[3] != "-"); print(f"positions where A and B place the same letter: {ag}/{len(rows)}")
