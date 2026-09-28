#!/usr/bin/env python3
"""H43: the Madrid legation cipher (Erving to Madison, 1806-1807, "Cypher of the Legation") as a value -> gloss table,
from the period interlinear decodes read blind in H32/H33/H38 (h32/legation_groups.tsv, 1,050 groups), H42
(h42/reads/f373L.tsv, 129 groups) and H47 (h47/reads/f28*.tsv, frames 284-286, 564 groups after the duplicate guard). The H26 letter (corr/erving1807_groups.tsv, the LOC copy) carries no glosses; its NARA original is the H47 source.
Per value: the majority gloss (case-folded), its count, the number of glossed occurrences, the runner-up.
Grade (CLAUDE.md rule 4; H43's row: C where two or more readings agree): C where the majority gloss is attested two or
more times AND more than twice the runner-up gloss (a two-thirds share was tried first and rejected: the reader's phrase
alignment scatters 13 of 31 glosses of 133 over neighbouring words, so 'of' 18 vs 'the' 4 would read M); M otherwise. Every digit string is single-reader (M) -- see the note column.
Writes tools/data/uscodes-1800/key_legation_madrid_1807.tsv (header comment lines read by tools/key_crossmatch.py's
EXTRA_KEY_GLOBS; home: none, so no self-pair with the Armstrong target, whose code this is NOT: H38 MISS at n=1,030).
usage: python3 ciphers/armstrong-madison-1808/h43/build_key.py [--check]"""
import csv, os, re, sys
from collections import Counter, defaultdict
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H); ROOT = os.path.dirname(os.path.dirname(T))
OUT = os.path.join(ROOT, "tools", "data", "uscodes-1800", "key_legation_madrid_1807.tsv")
occ = defaultdict(Counter); seen = Counter(); frames = defaultdict(set)
def add(src, frame, g, gl):
    g = re.sub(r"\D", "", g or "")
    if not g: return
    seen[g] += 1; frames[g].add(frame)
    gl = (gl or "").strip().lower()
    if gl and gl != "-": occ[g][gl] += 1
for r in csv.DictReader(open(os.path.join(T, "h32", "legation_groups.tsv")), delimiter="\t"):
    add("h32", r["frame"], r["group"], r["gloss"])
for r in csv.DictReader(open(os.path.join(T, "h42", "reads", "f373L.tsv")), delimiter="\t"):
    if (r["group"] or "").upper() != "NONE": add("h42", "f373L", r["group"], r["gloss"])
# H47 (28 Sept 2026): the NARA original of Erving No 21, 24 Mar 1807 (frames 284-286), with the same duplicate-band
# guard as h47/check.py (a crop repeating the previous crop's group sequence is the same physical line, dropped)
import difflib
for fr in ["f284L", "f284R", "f285L", "f285R", "f286L", "f286R"]:
    crops = {}
    for r in csv.DictReader(open(os.path.join(T, "h47", "reads", fr + ".tsv")), delimiter="\t"):
        if re.sub(r"\D", "", r.get("group") or ""):
            crops.setdefault(int(re.sub(r"\D", "", r["crop"]) or 0), []).append(r)
    prev = None
    for c in sorted(crops):
        seq = [re.sub(r"\D", "", r["group"]) for r in crops[c]]
        if prev and len(seq) >= 2 and difflib.SequenceMatcher(None, seq, prev).ratio() >= 0.6: continue
        for r in crops[c]: add("h47", fr, r["group"], r["gloss"])
        prev = seq
lines = ["# Madrid legation cipher ('Cypher of the Legation'), George W. Erving to James Madison, 1806-1807, NARA RG 59 M31 reel 12.",
         "# Value -> majority period interlinear gloss, rebuilt from blind single-reader reads of the decoded despatches (frames 389-390,",
         "# 403-409, 426-428, 373, 284-286). Built by ciphers/armstrong-madison-1808/h43/build_key.py (do not edit by hand). Partial: only the",
         "# values used in those letters; glosses of a phrase spread over several groups are the reader's alignment. NOT the key of the",
         "# Armstrong 20 Feb 1808 letter (corr/screen.py MISS at n=1,030, H38).",
         "# office: US legation at Madrid (George W. Erving, secretary/charge d'affaires) -> James Madison, Secretary of State",
         "# years: 1806-1807", "# language: en", "# home: none",
         "# note: grade C = majority gloss attested >=2 times and more than twice the runner-up; M otherwise; digits single-reader",
         "code\tvalue\tgrade\tn_glossed\tn_seen\trunner_up\tframes"]
nC = nM = 0
for g in sorted(occ, key=int):
    c = occ[g]; (v, k), tot = c.most_common(1)[0], sum(c.values())
    second = c.most_common(2)[1][1] if len(c) > 1 else 0
    grade = "C" if k >= 2 and k > 2 * second else "M"
    nC += grade == "C"; nM += grade == "M"
    ru = ";".join(f"{w}:{n}" for w, n in c.most_common()[1:3])
    lines.append(f"{g}\t{v}\t{grade}\t{tot}\t{seen[g]}\t{ru}\t{','.join(sorted(frames[g]))}")
text = "\n".join(lines) + "\n"
if "--check" in sys.argv:
    ok = os.path.exists(OUT) and open(OUT).read() == text
    print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
open(OUT, "w").write(text)
print(f"values seen {len(seen)}, glossed values {len(occ)} (C {nC}, M {nM}), glossed occurrences {sum(sum(c.values()) for c in occ.values())}")
