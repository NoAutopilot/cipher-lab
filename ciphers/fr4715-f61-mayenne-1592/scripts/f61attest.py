#!/usr/bin/env python3
"""F61-SKEL-GRADE (campaign step H76, 28 Sept 2026, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only, for the verifier
page (CAMPAIGN.md H66): the f.61r skeleton of scripts/f61_skeleton.txt (H58, read as committed, not regenerated) with
every lettered or paired position tagged by what its cell rests on. NOT a reading; no letter chosen.

Tags (the strongest that applies):
  {P}  both letters of the cell period-attested by a blind tile sort against the period gloss of the family leaves:
       SBS b/o (H65 o, H67 b, H89 o on f.274), 4TRI c/p (H69)
  {P1:x} one letter of the cell so attested: VBAR_A t, VBAR_B s (H70 f.101r, thin; H89 f.274, 13/13)
  {pub} published key value (ZHOOK i/x, Tomokiyo's table: family/key_published_rare.tsv, H44)
  {K}  period key (family/key_period_v3.tsv) has both cell letters among the class's top 3 on at least one leaf with n >= 5
  {K1} period key has one of the two cell letters in that top 3
  {F}  our f.61 fit only (scripts/f61joint_h51_map.tsv, grade M) -- no period support found
Nulls '-' and unread '?' are untagged. Counts per tag overall and for L10 (the unmarked run).
  python3 scripts/f61attest.py [--check]   -> scripts/f61_skeleton_attest.txt
"""
import csv, os, re, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); FAM = f"{HERE}/../family"
P = {"SBS": "P", "4TRI": "P"}; P1 = {"VBAR_A": "t", "VBAR_B": "s"}; PUB = {"ZHOOK"}
cnt = defaultdict(lambda: defaultdict(Counter))
for r in csv.DictReader((l for l in open(f"{FAM}/key_period_v3.tsv") if not l.startswith("#")), delimiter="\t"):
    cnt[r["class"]][r["leaf"]][r["letter"]] += int(r["n"])
def ktag(cls, cell):
    a = set(cell.split("/")); best = 0
    for leaf, c in cnt.get(cls, {}).items():
        if sum(c.values()) < 5: continue
        best = max(best, len(a & {l for l, _ in c.most_common(3)}))
    return {2: "K", 1: "K1"}.get(best, "F")
sk = open(f"{HERE}/f61_skeleton.txt").read().splitlines()
cells = dict(x.split("=") for x in next(l for l in sk if l.startswith("# cells used:")).split(":", 1)[1].split())
out = ["# f.61r skeleton with attestation tags -- campaign H76, 28 Sept 2026, scripts/f61attest.py from scripts/f61_skeleton.txt (H58). NOT a reading: no letter chosen within any pair.",
       "# tags: {P} both cell letters period-attested by a blind tile sort (SBS b/o H65/H67/H89, 4TRI c/p H69); {P1:x} one letter so attested (VBAR_A t, VBAR_B s, H70 f.101r + H89 f.274, two hands); {pub} published key (ZHOOK); {K} both letters in the period key's top 3 for the class on a leaf with n>=5; {K1} one letter; {F} our f.61 fit only."]
tot, l10 = Counter(), Counter(); lines = {}
for l in sk:
    m = re.match(r"(L\d\d) \(\d+ signs\): (.*)", l)
    if m: lines[m.group(1)] = [m.group(2).split(), None]
    m = re.match(r"(L\d\d) classes: (.*)", l)
    if m: lines[m.group(1)][1] = m.group(2).split()
for line, (toks, classes) in lines.items():
    outt = []
    for t, c in zip(toks, classes):
        if t in ("-", "?"): outt.append(t); continue
        cell = cells.get(c, "")
        tag = P.get(c) or (f"P1:{P1[c]}" if c in P1 else None) or ("pub" if c in PUB else None) or (ktag(c, cell) if cell else "F")
        outt.append(f"{t}{{{tag}}}"); tot[tag.split(':')[0]] += 1
        if line == "L10": l10[tag.split(':')[0]] += 1
    out.append(f"{line}: " + " ".join(outt))
fmt = lambda c: ", ".join(f"{k} {c[k]}" for k in ("P", "P1", "pub", "K", "K1", "F") if c[k])
out.insert(2, f"# counts over lettered/paired positions: {fmt(tot)} (of {sum(tot.values())}); L10: {fmt(l10)} (of {sum(l10.values())})")
txt = "\n".join(out) + "\n"; res = f"{HERE}/f61_skeleton_attest.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
