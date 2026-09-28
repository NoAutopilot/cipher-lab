#!/usr/bin/env python3
"""H42: is M31 reel 12 frame 373 (Erving, spring 1807, left page) a key sheet or usage of the Madrid legation cipher?
Reads h42/reads/f373L.tsv (one blind Sonnet pass: crop, pos, group, gloss, conf, note) and checks every glossed
group against the majority period gloss of the same value in the pool (h32/legation_groups.tsv, H32-H38, 1,050 groups).
Match rule: the pool's majority gloss equals the read gloss or one of its words (glosses like "to his" span two groups).
Null: the frame's own glosses shuffled among its glossed groups, 2,000 draws, same rule; reports p95.
Also: value overlap with the pool vs the target (ciphertext groups, corr/screen.py input) for the record.
usage: python3 h42/check.py"""
import csv, os, random, re
from collections import Counter, defaultdict
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
pool = defaultdict(Counter)
for r in csv.DictReader(open(os.path.join(T, "h32", "legation_groups.tsv")), delimiter="\t"):
    gl = r["gloss"].strip().lower()
    if gl and gl != "-": pool[r["group"].strip()][gl] += 1
maj = {k: v.most_common(1)[0][0] for k, v in pool.items()}
reads = []
for r in csv.DictReader(open(os.path.join(H, "reads", "f373L.tsv")), delimiter="\t"):
    g = re.sub(r"[^0-9a-zA-Z]", "", r["group"] or "")
    if not g or g.upper() == "NONE": continue
    reads.append((g, (r["gloss"] or "").strip().lower(), r.get("conf", "")))
def words(s): return set(re.findall(r"[a-z]+", s))
def match(g, gl): return g in maj and gl not in ("", "-") and (maj[g] == gl or maj[g] in words(gl))
glossed = [(g, gl) for g, gl, _ in reads if gl not in ("", "-")]
testable = [(g, gl) for g, gl in glossed if g in maj]
hits = sum(match(g, gl) for g, gl in testable)
rnd = random.Random(42); gls = [gl for _, gl in testable]; null = []
for _ in range(2000):
    rnd.shuffle(gls); null.append(sum(match(g, gl) for (g, _), gl in zip(testable, gls)))
null.sort()
print(f"groups read {len(reads)}, distinct {len(set(g for g,_,_ in reads))}, glossed {len(glossed)}")
print(f"values also in the pool {len(set(g for g,_,_ in reads) & set(pool))} of {len(set(g for g,_,_ in reads))} distinct")
print(f"glossed groups whose value has a pool gloss: {len(testable)}; agree with pool majority: {hits}; "
      f"gloss-shuffle null mean {sum(null)/len(null):.2f}, p95 {null[int(0.95*len(null))]}")
print("per group (value, frame gloss, pool majority, agree):")
for g, gl in testable: print(f"  {g}\t{gl}\t{maj[g]} ({sum(pool[g].values())})\t{'Y' if match(g, gl) else '-'}")
new = [(g, gl) for g, gl in glossed if g not in maj]
print(f"glossed values with no pool gloss ({len(new)}): " + ", ".join(f"{g}={gl}" for g, gl in new))
