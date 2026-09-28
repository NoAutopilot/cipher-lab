#!/usr/bin/env python3
"""H47: the NARA original of Erving to Madison No 21, 24 Mar 1807 (M31 reel 12 frames 284-286, 'In the Cipher of the
Legation', period interlinear decode), read blind on band crops (h47/reads/f28{4,5,6}{L,R}.tsv, three Sonnet calls).
Two checks:
 (1) glosses vs the legation table's majority glosses, recomputed here from H43's own inputs (h32 pool + h42 frame
     373), never from the committed table, which H47 later rebuilds with these reads: a glossed group agrees when the table's majority gloss equals the read gloss or
     one of its words; null = the frame's own glosses shuffled over its testable groups, 2,000 draws, p95.
 (2) digits vs an independent witness of the same letter: corr/erving1807_groups.tsv (ARM-CORR's eye transcription of
     the LOC 'Duplicate', pages 2-3). difflib matching blocks between the two group streams, against a null of the
     NARA stream shuffled (200 draws): real matched-in-order groups vs null p95.
usage: python3 h47/check.py"""
import csv, difflib, os, random, re
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H); ROOT = os.path.dirname(os.path.dirname(T))
ORDER = ["f284L", "f284R", "f285L", "f285R", "f286L", "f286R"]
# the table's majority glosses from H43's own inputs only (h32 pool + h42 frame 373), so a later rebuild of the table
# that includes these reads cannot leak them back into this check
occ = {}
def _add(g, gl):
    g = re.sub(r"\D", "", g or ""); gl = (gl or "").strip().lower()
    if g and gl and gl != "-": occ.setdefault(g, Counter())[gl] += 1
for r in csv.DictReader(open(os.path.join(T, "h32", "legation_groups.tsv")), delimiter="\t"): _add(r["group"], r["gloss"])
for r in csv.DictReader(open(os.path.join(T, "h42", "reads", "f373L.tsv")), delimiter="\t"): _add(r["group"], r["gloss"])
key = {g: c.most_common(1)[0][0] for g, c in occ.items()}
reads = []; dropped = []
for fr in ORDER:
    f = os.path.join(H, "reads", fr + ".tsv")
    if not os.path.exists(f): print("missing", fr); continue
    crops = {}
    for r in csv.DictReader(open(f), delimiter="\t"):
        g = re.sub(r"\D", "", r.get("group") or "")
        if g: crops.setdefault(int(re.sub(r"\D", "", r["crop"]) or 0), []).append((fr, g, (r.get("gloss") or "").strip().lower()))
    prev = None
    for c in sorted(crops):  # duplicate-band guard (h29/check_we028.py, h32/merge_screen.py): a crop repeating the
        seq = [g for _, g, _ in crops[c]]  # previous crop's group sequence (the same physical line) is dropped
        if prev and len(seq) >= 2 and difflib.SequenceMatcher(None, seq, prev).ratio() >= 0.6:
            dropped.append((fr, c)); continue
        reads.extend(crops[c]); prev = seq
def words(s): return set(re.findall(r"[a-z]+", s))
def match(g, gl): return key.get(g) is not None and gl not in ("", "-") and (key[g] == gl or key[g] in words(gl))
glossed = [(g, gl) for _, g, gl in reads if gl not in ("", "-")]
test = [(g, gl) for g, gl in glossed if g in key]
hits = sum(match(g, gl) for g, gl in test)
rnd = random.Random(47); gls = [gl for _, gl in test]; null = []
for _ in range(2000):
    rnd.shuffle(gls); null.append(sum(match(g, gl) for (g, _), gl in zip(test, gls)))
null.sort()
print(f"groups read {len(reads)} (distinct {len(set(g for _,g,_ in reads))}), glossed {len(glossed)}; per region " +
      ", ".join(f"{fr} {sum(1 for x in reads if x[0]==fr)}" for fr in ORDER))
print(f"duplicate bands dropped: {dropped}")
print(f"(1) glossed groups whose value is in the legation table: {len(test)}; agree with its majority gloss: {hits}; "
      f"gloss-shuffle null mean {sum(null)/len(null):.2f}, p95 {null[int(.95*len(null))]}")
loc = []
for l in open(os.path.join(T, "corr", "erving1807_groups.tsv")):
    if l.startswith("#") or not l.strip(): continue
    loc += re.findall(r"\d+", l.split("\t", 1)[1] if "\t" in l else l)
nara = [g for _, g, _ in reads]
def matched(a, b): return sum(m.size for m in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks())
real = matched(nara, loc); nl = []
for _ in range(200):
    s = nara[:]; rnd.shuffle(s); nl.append(matched(s, loc))
nl.sort()
print(f"(2) LOC copy stream {len(loc)} groups; groups matched in order with the NARA read: {real} "
      f"(shuffled-NARA null mean {sum(nl)/len(nl):.1f}, p95 {nl[int(.95*len(nl))]})")
new = sorted({(g, gl) for g, gl in glossed if g not in key}, key=lambda x: int(x[0]))
print(f"glossed values not in the table ({len(new)}): " + ", ".join(f"{g}={gl}" for g, gl in new[:60]))
# digit-level disagreement between the two witnesses on the stretches difflib pairs one-for-one (an upper bound on
# the NARA read's digit error there, since the LOC copy is itself one eye transcription at grade S)
eq = rep = unp_n = unp_l = 0
for op, a1, a2, b1, b2 in difflib.SequenceMatcher(None, nara, loc, autojunk=False).get_opcodes():
    if op == "equal": eq += a2 - a1
    elif op == "replace" and a2 - a1 == b2 - b1: rep += a2 - a1
    else: unp_n += a2 - a1; unp_l += b2 - b1
print(f"(2b) one-for-one aligned groups {eq + rep}: identical {eq}, differing {rep} ({100 * rep / max(1, eq + rep):.1f} pct); "
      f"unpaired NARA {unp_n} (the NARA pages outside the LOC copy's pages 2-3 among them), unpaired LOC {unp_l}")
