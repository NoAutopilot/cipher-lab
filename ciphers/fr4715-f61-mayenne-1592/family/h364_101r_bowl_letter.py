#!/usr/bin/env python3
"""H364 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), script-only, written before running: does the bowl answer track the period letter
on fr.3982 f.101r, whose own interlinear gloss built v7's 4TRI cell? H362's answers (passes/h362_reply.tsv, gate 17/20 PASS) for its 50 4TRI and 20 C43
tokens are joined to the period alignment passes/f101r_align.tsv (plain_chunk = the gloss letter the alignment pairs with the code): per line, the
alignment's code sequence (raw '@CODE') is matched to the reconciled draft's sign sequence by difflib, and a token takes the letter of its matched
alignment row (rows whose status is 'null-or-unaligned' or whose letter is empty give none). Cross-tab: bowl answer (yes/no) x letter class (c/p/t,
a/n, other). Pre-stated: 'the bowl tracks the letter on f.101r' iff among tokens with a c/p/t or a/n letter, yes<->c/p/t and no<->a/n agree on >= 0.75
of them (n >= 15); if agreement < 0.6 with n >= 15, 'the bowl does not track the letter on f.101r' (H362's no-share there is shape, not a/n); else
'unclear at this N'. Descriptive; no key change.   python3 h364_101r_bowl_letter.py [--check]"""
import csv, difflib, os, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; ARGS = sys.argv[1:]
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
al = defaultdict(list)
for r in rd(f"{P}/f101r_align.tsv"):
    if r["kind"] == "code": al[r["cipher_line"]].append(r)
dr = defaultdict(list)
for r in rd(f"{P}/recf101r/ciphertext_draft.tsv"): dr[r["line"]].append(r)
letter = {}
for line, rows in dr.items():
    a = al.get(line, []); sa = [x["value"] for x in a]; sd = [x["sign"] for x in rows]
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, sd, sa, autojunk=False).get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                ar = a[j1 + k]; L = ar["plain_chunk"].strip()
                if L and not ar["status"].startswith("null"): letter[(line, rows[i1 + k]["position"])] = L
ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h362_reply.tsv")}
cls = lambda L: "c/p/t" if L in ("c", "p", "t") else "a/n" if L in ("a", "n") else "other"
tab = defaultdict(Counter); out = []
for r in rd(f"{HERE}/h362_items.tsv"):
    L = letter.get((r["line"], r["pos"])); a = ans.get(r["item"], "missing")
    tab[(r["code"], a)][cls(L) if L else "none"] += 1
for k in sorted(tab): out.append(f"{k[0]} bowl={k[1]}: " + " ".join(f"{c} {v}" for c, v in sorted(tab[k].items())))
agree = tab[("4TRI", "yes")]["c/p/t"] + tab[("4TRI", "no")]["a/n"] + tab[("C43", "yes")]["c/p/t"] + tab[("C43", "no")]["a/n"]
n = sum(tab[(c, a)][x] for c in ("4TRI", "C43") for a in ("yes", "no") for x in ("c/p/t", "a/n"))
sh = agree / n if n else 0
ro = ("the bowl tracks the letter on f.101r" if sh >= 0.75 else "the bowl does not track the letter on f.101r" if sh < 0.6 else "unclear at this N") if n >= 15 else "unclear at this N"
out.append(f"tokens with a c/p/t or a/n letter: {n}; bowl-letter agreement {agree}/{n} = {sh:.2f} -> {ro}")
txt = "\n".join(out) + "\n"; rs = f"{HERE}/h364_101r_bowl_letter_result.txt"
if "--check" in ARGS:
    ok = os.path.exists(rs) and open(rs).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(rs, "w").write(txt); print(txt, end="")
