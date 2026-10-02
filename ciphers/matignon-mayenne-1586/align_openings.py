#!/usr/bin/env python3
"""GAPS-matignon-mayenne-1586 (2 Oct 2026, account-4): align Tomokiyo's published openings of
ff. 110 ("f.111"), 143 and 154 (and, as a reproduction of the gap-3 scratch number, f. 150) against
our straight-substitution decode of the first cipher line(s) of each leaf, with a within-line shuffle
control, and tabulate which plaintext letter every unkeyed label (U, BOX, T, z, 4, w ...) and every
disagreeing H code falls on.

The openings are S. Tomokiyo's modern readings (cryptiana.web.fc2.com/code/henryiii.htm, "Mayenne-
Forget's Cipher-1", on disk at sources/cryptiana/web/henryiii.htm lines 628-631), so anything read
off the alignment is grade M at most (CLAUDE.md rule 4: a modern published reading, credited); this
script commits no value to key.tsv and changes no reading.

Method (same shape as align_crib.py, bMAT1D): global monotonic DP over (cipher tokens of the first L
lines of the leaf) x (plaintext items of the opening). A token consumes 0 letters (a null, NULL_GAP) or
1 letter; a token whose key value is a known word (12=il, 14=que, 25=nous ...) consumes exactly that
word; a code that Tomokiyo left as a number (49, 76) is a plaintext item of its own that only the same
cipher token can consume. Score: H single-letter token +4 match / -5 mismatch; M (set) token +2 if the
letter is in its set / -4 if not; U token 0 (unscored, it only consumes a letter); a null -2; a plaintext
item skipped by no token -4 (so one mismatch, -5, beats a null plus a skip, -6, and disagreements show); both ends free (the opening may be shorter or longer than the lines taken).
Because U tokens carry no score, the letter under a U label is read off a path driven entirely by the
keyed tokens around it -- the same licence align_crib.py relies on.

Control (rule 3): the tokens of each line are shuffled within the line (seeded, --shuffles draws) and
the DP re-run; the statistic (best path score) depends on token order relative to the fixed plaintext,
so the control can differ from the target (CLAUDE.md rule 3's "can the control vary on this axis" check:
yes). Reported per leaf: real score, shuffle max / p95 / median, and for every U label with >= 2
aligned occurrences the top letter and its share, real vs the mean top-letter share over the shuffles.

Usage:  python3 ciphers/matignon-mayenne-1586/align_openings.py [--shuffles 200] [--seed 1] [--out DIR]
Writes DIR/openings_alignment.tsv (one row per token on the real path), DIR/openings_summary.json and
prints the tabulation. Exit 0 always (it is a report, not a gate); --check exits 1 if the committed
openings_summary.json differs from a fresh run (rule 7).
"""
import argparse
import csv
import json
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
MATCH_H, MISMATCH_H = 4, -5
MATCH_M, MISMATCH_M = 2, -4
MATCH_CODE = 8          # a numbered code (49, 76) matched to Tomokiyo's own number
NULL_GAP = -2           # token consumes nothing
PT_SKIP = -4            # plaintext item consumed by no token; null + skip (-6) is worse than one mismatch (-5),
                        # so a keyed token that contradicts Tomokiyo is shown as DISAGREE, not hidden as a gap pair
NEUTRAL = 0             # U token consumes a letter, unscored

# Tomokiyo's openings, verbatim from henryiii.htm (snapshot sources/cryptiana/web/henryiii.htm, lines
# 628-631; the live page read 2 Oct 2026 01:58 UTC is identical in this section). "f.111" is Bourdeau's
# "probably a slip for f. 110" (his NOTES.md, HEAD 2 Oct 2026) and the gap-2 note's own observation.
OPENINGS = {
    "f110": ("Monsieur de Villeroi vous verres bien par la lettre que je fais au roi dueiemes", 2),
    "f143r": ("s'estant laisse entendre 49 il se voulloit de partir du 76 duquel je scai quil est tres "
              "malcontant et ayant considere que je lai tousjours ou y tenir pour le meilleur", 5),
    "f150": ("il estoit me besoins car je tourvai quil auoit", 2),
    "f154": ("en quelle peine [nous] estion", 1),
}
# (text, number of cipher lines of the leaf taken, sized so the tokens cover the opening with slack)

FOLD = str.maketrans("vjàâäéèêëîïôöùûüç", "uiaaaeeeeiioouuuc")


def norm_plain(s):
    """Tomokiyo's text -> list of items: single folded letters, or ('#', code) for a bare number."""
    s = s.lower().replace("'", "").replace("[", "").replace("]", "").translate(FOLD)
    items = []
    for tok in re.findall(r"[0-9]+|[a-z]+", s):
        if tok.isdigit():
            items.append("#" + tok)
        else:
            items.extend(tok)
    return items


def load_key():
    key = {}
    with open(HERE / "key.tsv", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            key[r["code"]] = (r["value"], r["grade"])
    return key


def load_lines():
    lines = {}
    order = []
    with open(HERE / "ciphertext.txt", encoding="utf-8") as f:
        for ln in f:
            if not ln.strip() or ln.startswith("#"):
                continue
            lid, toks = ln.rstrip("\n").split("\t")[:2]
            lines[lid] = toks.split()
            order.append(lid)
    return lines, order


def classify(tok, key):
    """-> (kind, payload): ('H', letter) | ('M', set) | ('W', word) | ('N', code) | ('U', None)"""
    if tok not in key:
        return ("U", None)
    val, grade = key[tok]
    if val in ("+", "", "?"):
        return ("U", None)
    if val == "*":
        return ("N", tok)
    if "|" in val:
        alts = val.split("|")
        if all(len(a) == 1 for a in alts):
            return ("M", set(alts))
        return ("M", set(a[0] for a in alts))  # yy = ss|s, T= = m|mm: first letter of each alternative
    if len(val) > 1:
        return ("W", val)
    return ("H", val)


def align(tokens, plain, key):
    """Returns (best score, path) with path = list of (token index, plain start, plain end) per token
    (start == end for a null); plaintext items skipped appear as (None, j, j+1)."""
    n, m = len(tokens), len(plain)
    kinds = [classify(t, key) for t in tokens]
    NEG = -10 ** 9
    S = [[NEG] * (m + 1) for _ in range(n + 1)]
    back = [[None] * (m + 1) for _ in range(n + 1)]
    S[0][0] = 0
    for j in range(1, m + 1):   # leading plaintext skips
        S[0][j] = S[0][j - 1] + PT_SKIP
        back[0][j] = ("skip", 0, j - 1)
    for i in range(1, n + 1):
        kind, pay = kinds[i - 1]
        for j in range(0, m + 1):
            best, bk = NEG, None
            # null: token consumes nothing
            v = S[i - 1][j] + NULL_GAP
            if v > best:
                best, bk = v, ("null", i - 1, j)
            # plaintext skip
            if j > 0:
                v = S[i][j - 1] + PT_SKIP
                if v > best:
                    best, bk = v, ("skip", i, j - 1)
            if j > 0:
                item = plain[j - 1]
                if kind == "W":
                    L = len(pay)
                    if j >= L and "".join(x for x in plain[j - L:j]) == pay:
                        v = S[i - 1][j - L] + MATCH_H * L
                        if v > best:
                            best, bk = v, ("word", i - 1, j - L)
                elif kind == "N":
                    if item == "#" + pay:
                        v = S[i - 1][j - 1] + MATCH_CODE
                        if v > best:
                            best, bk = v, ("code", i - 1, j - 1)
                elif kind == "U":
                    if item == "#" + tokens[i - 1]:
                        v = S[i - 1][j - 1] + MATCH_CODE
                        if v > best:
                            best, bk = v, ("code", i - 1, j - 1)
                    elif not item.startswith("#"):
                        v = S[i - 1][j - 1] + NEUTRAL
                        if v > best:
                            best, bk = v, ("letter", i - 1, j - 1)
                elif not item.startswith("#"):
                    if kind == "H":
                        sc = MATCH_H if item == pay else MISMATCH_H
                    else:
                        sc = MATCH_M if item in pay else MISMATCH_M
                    v = S[i - 1][j - 1] + sc
                    if v > best:
                        best, bk = v, ("letter", i - 1, j - 1)
            S[i][j] = best
            back[i][j] = bk
    # free ends: all tokens consumed with plaintext left over, or all plaintext consumed with tokens left
    end, score = None, NEG
    for j in range(m + 1):
        if S[n][j] > score:
            score, end = S[n][j], (n, j)
    for i in range(n + 1):
        if S[i][m] > score:
            score, end = S[i][m], (i, m)
    path = []
    i, j = end
    while (i, j) != (0, 0):
        op, pi, pj = back[i][j]
        if op == "null":
            path.append((i - 1, j, j))
        elif op == "skip":
            path.append((None, j - 1, j))
        elif op == "word":
            path.append((i - 1, pj, j))
        else:
            path.append((i - 1, j - 1, j))
        i, j = pi, pj
    path.reverse()
    return score, path


def run_leaf(leaf, text, nlines, lines, order, key, shuffles, seed):
    lids = [l for l in order if l.split("-")[0] == leaf][:nlines]
    toks, where = [], []
    for lid in lids:
        for p, t in enumerate(lines[lid], 1):
            toks.append(t)
            where.append((lid, p))
    plain = norm_plain(text)
    score, path = align(toks, plain, key)
    rows = []
    hits = Counter()
    for ti, a, b in path:
        if ti is None:
            rows.append({"line": "", "pos": "", "sign": "", "grade": "", "key": "", "plain": plain[a], "op": "skipped-plain"})
            continue
        kind, pay = classify(toks[ti], key)
        val = key.get(toks[ti], ("?", "U"))[0]
        grade = key.get(toks[ti], ("?", "U"))[1]
        under = "".join(plain[a:b]) if b > a else "-"
        if kind == "H":
            op = "agree" if under == pay else ("null" if under == "-" else "DISAGREE")
        elif kind == "M":
            op = "in-set" if under in pay else ("null" if under == "-" else "OUT-OF-SET")
        elif kind == "W":
            op = "word" if under == pay else "null"
        elif kind == "N":
            op = "code" if under.startswith("#") else "null"
        else:
            op = "U-on-letter" if under not in ("-",) and not under.startswith("#") else ("U-code" if under.startswith("#") else "null")
        hits[op] += 1
        rows.append({"line": where[ti][0], "pos": where[ti][1], "sign": toks[ti], "grade": grade, "key": val,
                     "plain": under, "op": op})
    # control: shuffle within each line
    rng = random.Random(seed)
    ctrl = []
    ctrl_top = defaultdict(list)
    for _ in range(shuffles):
        stoks = []
        for lid in lids:
            l = list(lines[lid])
            rng.shuffle(l)
            stoks.extend(l)
        sc, sp = align(stoks, plain, key)
        ctrl.append(sc)
        per = defaultdict(Counter)
        for ti, a, b in sp:
            if ti is None or b == a:
                continue
            k, _ = classify(stoks[ti], key)
            if k == "U" and not plain[a].startswith("#"):
                per[stoks[ti]][plain[a]] += 1
        for lab, c in per.items():
            ctrl_top[lab].append(c.most_common(1)[0][1] / sum(c.values()))
    ctrl.sort()
    return {
        "leaf": leaf, "lines": lids, "tokens": len(toks), "plain_items": len(plain), "score": score,
        "ops": dict(hits), "ctrl_max": ctrl[-1], "ctrl_p95": ctrl[int(0.95 * (len(ctrl) - 1))],
        "ctrl_median": ctrl[len(ctrl) // 2], "ctrl_min": ctrl[0], "shuffles": shuffles,
        "ctrl_top_share": {k: round(sum(v) / len(v), 3) for k, v in ctrl_top.items()},
    }, rows


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--shuffles", type=int, default=200)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--out", default=str(HERE / "openings"))
    ap.add_argument("--check", action="store_true", help="exit 1 if openings_summary.json on disk differs")
    a = ap.parse_args()
    key = load_key()
    lines, order = load_lines()
    out = Path(a.out)
    out.mkdir(exist_ok=True)
    summaries, allrows = [], []
    for leaf, (text, nl) in OPENINGS.items():
        s, rows = run_leaf(leaf, text, nl, lines, order, key, a.shuffles, a.seed)
        summaries.append(s)
        for r in rows:
            r["leaf"] = leaf
        allrows.extend(rows)
    # tabulation: U labels and disagreeing H codes, pooled over the leaves whose real score beats the control max
    good = {s["leaf"] for s in summaries if s["score"] > s["ctrl_max"]}
    u_tab = defaultdict(Counter)
    h_dis = defaultdict(Counter)
    h_agree = Counter()
    for r in allrows:
        if r["leaf"] not in good or not r["sign"]:
            continue
        if r["grade"] == "U" and r["op"] == "U-on-letter":
            u_tab[r["sign"]][r["plain"]] += 1
        elif r["grade"] == "H" and r["op"] == "DISAGREE":
            h_dis[(r["sign"], r["key"])][r["plain"]] += 1
        elif r["grade"] == "H" and r["op"] == "agree":
            h_agree[r["sign"]] += 1
    tab = {"leaves_above_control_max": sorted(good),
           "U_labels": {k: dict(v.most_common()) for k, v in sorted(u_tab.items(), key=lambda kv: -sum(kv[1].values()))},
           "H_disagreements": {f"{k[0]}={k[1]}": dict(v.most_common()) for k, v in sorted(h_dis.items(), key=lambda kv: -sum(kv[1].values()))},
           "H_agree_counts": dict(h_agree)}
    result = {"leaves": summaries, "tabulation": tab, "params": {"shuffles": a.shuffles, "seed": a.seed,
              "MATCH_H": MATCH_H, "MISMATCH_H": MISMATCH_H, "MATCH_M": MATCH_M, "MISMATCH_M": MISMATCH_M,
              "NULL_GAP": NULL_GAP, "PT_SKIP": PT_SKIP, "MATCH_CODE": MATCH_CODE}}
    sj = out / "openings_summary.json"
    if a.check:
        old = json.loads(sj.read_text()) if sj.exists() else None
        if old != result:
            print("STALE: openings_summary.json differs from a fresh run", file=sys.stderr)
            sys.exit(1)
        print("openings_summary.json is current")
        return
    with open(out / "openings_alignment.tsv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["leaf", "line", "pos", "sign", "grade", "key", "plain", "op"], delimiter="\t")
        w.writeheader()
        w.writerows(allrows)
    sj.write_text(json.dumps(result, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    for s in summaries:
        print(f"{s['leaf']}: lines {','.join(s['lines'])} ({s['tokens']} tokens vs {s['plain_items']} plaintext items) "
              f"score {s['score']} | within-line shuffle x{s['shuffles']}: max {s['ctrl_max']} p95 {s['ctrl_p95']} "
              f"median {s['ctrl_median']} | ops {s['ops']}")
    print("leaves above control max:", tab["leaves_above_control_max"])
    print("U labels -> plaintext letters (pooled over those leaves; shuffle mean top-share in brackets):")
    for lab, c in tab["U_labels"].items():
        n = sum(c.values())
        top = max(c.items(), key=lambda kv: kv[1])
        ctrl_share = [s["ctrl_top_share"].get(lab) for s in summaries if s["leaf"] in good and lab in s["ctrl_top_share"]]
        cs = f"{sum(ctrl_share) / len(ctrl_share):.2f}" if ctrl_share else "n/a"
        print(f"  {lab:5s} n={n:2d} top {top[0]} {top[1]}/{n} ({top[1] / n:.2f}) [{cs}]  all {c}")
    print("H codes disagreeing with Tomokiyo (pooled):")
    for k, c in tab["H_disagreements"].items():
        sign = k.split("=")[0]
        print(f"  {k:8s} agree {h_agree.get(sign, 0):2d} disagree {sum(c.values()):2d} -> {dict(c)}")


if __name__ == "__main__":
    main()
