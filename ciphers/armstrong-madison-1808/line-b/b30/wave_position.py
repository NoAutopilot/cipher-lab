"""Line B step B30 -- are the wave strokes (Tomokiyo 20/22/23) fillers or separators? For each type: share of its
tokens at a run edge (first or last of a fragment with >= 2 glyphs) and share immediately adjacent to another token
of the same family, against a within-run permutation null (glyph order shuffled inside each fragment, 10,000
draws). Comparison set: the next commonest types 36, 65, 35, 33."""
import random, sys
from collections import Counter
from pathlib import Path
HERE = Path(__file__).resolve().parent; REPO = HERE.parents[3]
frags = [l.strip().split(';') for l in open(REPO / "ciphers/armstrong-madison-1808/codex-2026-09-27b/glyphs.txt") if l.strip()]
WAVE = {'20', '22', '23'}
def stats(fr, fam):
    edge = tot = adj = 0
    for f in fr:
        if len(f) < 2: continue
        for i, g in enumerate(f):
            if g in fam:
                tot += 1; edge += (i == 0 or i == len(f) - 1)
                adj += any(f[j] in fam for j in (i-1, i+1) if 0 <= j < len(f))
    return (edge / tot if tot else 0, adj / tot if tot else 0, tot)
rng = random.Random(2)
def null(fam, draws=10000):
    e = []; a = []
    for _ in range(draws):
        fr = []
        for f in frags:
            g = f[:]; rng.shuffle(g); fr.append(g)
        s = stats(fr, fam); e.append(s[0]); a.append(s[1])
    e.sort(); a.sort(); return e, a
print(f"{'family':12s}{'n':>5s}{'edge share':>12s}{'null p05':>9s}{'p95':>7s}{'pct':>6s}{'same-family adj':>17s}{'null p05':>9s}{'p95':>7s}{'pct':>6s}")
for name, fam in (("waves 20/22/23", WAVE), ("20 alone", {'20'}), ("36", {'36'}), ("65", {'65'}), ("35", {'35'}), ("33", {'33'})):
    s = stats(frags, fam); e, a = null(fam, 3000)
    pe = 100*sum(1 for x in e if x < s[0])/len(e); pa = 100*sum(1 for x in a if x < s[1])/len(a)
    print(f"{name:12s}{s[2]:5d}{s[0]:12.3f}{e[int(.05*len(e))]:9.3f}{e[int(.95*len(e))]:7.3f}{pe:6.0f}{s[1]:17.3f}{a[int(.05*len(a))]:9.3f}{a[int(.95*len(a))]:7.3f}{pa:6.0f}")
# run-start and run-end types
print("run-initial types:", Counter(f[0] for f in frags).most_common(6))
print("run-final types:  ", Counter(f[-1] for f in frags).most_common(6))

# B30b: if 20 (or the wave family) is a word space, the glyph groups between waves are words: compare their
# length distribution with en18 word lengths (band of 60 samples of the same count of words).
import gzip, re
def segments(fr, sep):
    out = []
    for f in fr:
        cur = 0
        for g in f:
            if g in sep:
                if cur: out.append(cur); cur = 0
            else: cur += 1
        if cur: out.append(cur)
    return out
texts = []
for p in sorted((REPO / "tools/data/en18").glob("*.txt.gz")):
    t = gzip.open(p, "rt", encoding="utf-8", errors="replace").read(); n = len(t); texts.append(t[int(n*0.1):int(n*0.9)])
def band(nw, draws=60):
    rng2 = random.Random(5); rows = []
    for _ in range(draws):
        t = rng2.choice(texts); s = rng2.randint(0, len(t) - 20000); ws = re.findall(r"[A-Za-z]+", t[s:s+20000])[:nw]
        L = [len(w) for w in ws]; rows.append((sum(L)/len(L), sum(1 for x in L if x <= 2)/len(L), sum(1 for x in L if x >= 8)/len(L), max(L)))
    return rows
for label, sep in (("20 = space", {'20'}), ("20/22/23 = space", WAVE)):
    seg = segments(frags, sep); tv = (sum(seg)/len(seg), sum(1 for x in seg if x <= 2)/len(seg), sum(1 for x in seg if x >= 8)/len(seg), max(seg))
    rows = band(len(seg))
    print(f"\n{label}: {len(seg)} segments, lengths {sorted(seg)}")
    for k, name in enumerate(("mean length", "share <= 2", "share >= 8", "max")):
        arr = sorted(r[k] for r in rows)
        print(f"  {name:12s} target {tv[k]:6.2f}  en18 words band p05 {arr[3]:6.2f} p50 {arr[30]:6.2f} p95 {arr[57]:6.2f}  pct {100*sum(1 for x in arr if x < tv[k])/60:4.0f}")
