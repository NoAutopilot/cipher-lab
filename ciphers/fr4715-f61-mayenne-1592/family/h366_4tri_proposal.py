#!/usr/bin/env python3
"""H366 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), script-only: writes family/PROPOSAL_v8_4tri.md -- the f.101r period-letter tally of
the readers' 4TRI code split by the bowl answers of H362/H365 (gated calls), with the top letters per group, as a PROPOSAL for a separate verifier
(rule 4: witnesses named, nothing loaded into a key). Letters come from passes/f101r_align.tsv via H364's join; answers as H365 merges them.
python3 h366_4tri_proposal.py [--check]"""
import csv, os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; ARGS = sys.argv[1:]
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
h364 = open(f"{HERE}/h364_101r_bowl_letter.py").read(); h364 = h364[:h364.index("ans = {r")]
g = {"__file__": f"{HERE}/h364_101r_bowl_letter.py", "__name__": "h366"}; exec(compile(h364, "h364_prefix", "exec"), g); letter = g["letter"]
ans = {}
a362 = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h362_reply.tsv")}
for r in rd(f"{HERE}/h362_items.tsv"):
    if r["code"] == "4TRI": ans[(r["line"], r["pos"])] = a362.get(r["item"], "missing")
for c in ("c1", "c2", "c3", "c4"):
    a = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h365_reply_{c}.tsv")}
    for r in rd(f"{HERE}/h365_items.tsv"):
        if r["chunk"] == c: ans[(r["line"], r["pos"])] = a.get(r["item"], "missing")
tal = {"yes": Counter(), "no": Counter(), "n": Counter()}
for k, v in ans.items():
    L = letter.get(k)
    if L and v in tal: tal[v][L] += 1
fmt = lambda c: ", ".join(f"{l} {n}" for l, n in c.most_common())
md = f"""# PROPOSAL_v8_4tri.md -- runner 13, 29 Sept 2026 (H366; a proposal for a separate verifier, not a key change)

**What:** the readers' 4TRI code on fr.3982 f.101r carries two signs, told apart by a stem-foot bowl (H193's attribute; gated forced-choice calls
H362 + H365, gates 17-19/20 on H193's f.176v anchors). f.101r's own period alignment (`passes/f101r_align.tsv`, grade C per pair) gives, per bowl
answer, these letters for the {sum(len(list(c.elements())) for c in tal.values())} answered 4TRI tokens that carry a letter:

| bowl answer | tokens with a letter | letters (count) |
|---|---|---|
| yes (bowl: the c/p sign of H193) | {sum(tal['yes'].values())} | {fmt(tal['yes'])} |
| no (no bowl) | {sum(tal['no'].values())} | {fmt(tal['no'])} |
| n (unclear) | {sum(tal['n'].values())} | {fmt(tal['n'])} |

**Proposed for verification (not applied):** read the no-bowl "4TRI" as the a/n sign (C43's period cell a/n), and keep 4TRI's c/p/t for the bowl sign
only. Witnesses: f.101r's period alignment (above); f.124r's order gain and held-gloss count both rise with the same split (H360 0.034 -> 0.071;
H361 148 -> 156); f.101r's own order gain rises (H365 0.082 -> 0.102); H218/H231 found the 4TRI code mixing the two signs on f.176r and f.106r.
**Against / open:** the bowl sign still pairs with a/n in {tal['yes']['a'] + tal['yes']['n']} of {sum(tal['yes'].values())} (readers' shape answers are
not perfect, and the alignment has its own errors, `conflict` rows 1522 of 3077 on f.101r); the bowl gate is on Desportes's hand (f.176v), checked
here against period letters on f.101r's; f.61's own 4TRI tokens have not been bowl-read. A verifier decides whether v8 splits 4TRI; any f.61 token
graded from 4TRI would change grade accordingly (rule 4: record the witnesses, do not settle by majority).
"""
out = f"{HERE}/PROPOSAL_v8_4tri.md"
if "--check" in ARGS:
    ok = os.path.exists(out) and open(out).read() == md; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(out, "w").write(md); print(md)
