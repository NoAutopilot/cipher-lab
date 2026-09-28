"""B35 reconciliation: pass A vs pass B per crop (glyph tokens only, Levenshtein distance / longer length), and
each pass's concatenated glyph stream vs Tomokiyo's tokenisation (codex glyphs.txt) by global sequence alignment
(difflib ratio on label lists). Numerals are anchors, not scored. Page-2 caveat: ARM-TR2 found the crops_0031L
line index off by one for page-2 crops other than L02/L06, so crop-to-line identity on page 2 is by content."""
import difflib, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; REPO = HERE.parents[3]
def load(*names):
    rows = {}
    for n in names:
        if not (HERE / n).exists(): print(f"missing {n}", file=sys.stderr); continue
        for line in open(HERE / n, encoding="utf-8"):
            p = line.rstrip("\n").split("\t")
            if len(p) < 3 or not p[0].strip().isdigit(): continue
            rows[int(p[0])] = " ".join(p[2:]).split()  # pass A files are tab-separated per token, pass B space-separated
    return rows
A = load("passA_1-15.tsv", "passA_16-29.tsv"); B = load("passB_1-15.tsv", "passB_16-29.tsv")
def glyphs(toks): return [t[1:] for t in toks if t.startswith("T")]
def lev(a, b):
    d = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        prev, d[0] = d[0], i
        for j, y in enumerate(b, 1):
            cur = d[j]; d[j] = min(d[j] + 1, d[j-1] + 1, prev + (x != y)); prev = cur
    return d[len(b)]
tot_d = tot_n = 0; print("crop  nA  nB  lev  disagreement")
for k in sorted(set(A) | set(B)):
    ga, gb = glyphs(A.get(k, [])), glyphs(B.get(k, [])); n = max(len(ga), len(gb), 1); d = lev(ga, gb)
    tot_d += d; tot_n += n; print(f"{k:4d} {len(ga):3d} {len(gb):3d} {d:4d}  {d/n:.2f}")
print(f"pass A vs pass B, glyph tokens: {sum(len(glyphs(v)) for v in A.values())} vs {sum(len(glyphs(v)) for v in B.values())}; summed Levenshtein / summed max length = {tot_d}/{tot_n} = {tot_d/tot_n:.3f}")
tom = [g for l in open(REPO / "ciphers/armstrong-madison-1808/codex-2026-09-27b/glyphs.txt") if l.strip() for g in l.strip().split(";")]
for name, P in (("A", A), ("B", B)):
    stream = [g for k in sorted(P) for g in glyphs(P[k])]
    sm = difflib.SequenceMatcher(None, stream, tom, autojunk=False)
    print(f"pass {name} stream ({len(stream)}) vs Tomokiyo ({len(tom)}): ratio {sm.ratio():.3f}, matching tokens {sum(b.size for b in sm.get_matching_blocks())}")
sa = [g for k in sorted(A) for g in glyphs(A[k])]; sb = [g for k in sorted(B) for g in glyphs(B[k])]
sm = difflib.SequenceMatcher(None, sa, sb, autojunk=False); print(f"pass A stream vs pass B stream: ratio {sm.ratio():.3f}")
from collections import Counter
print("type counts A:", sorted(Counter(sa).items(), key=lambda kv: -kv[1])[:12]); print("type counts B:", sorted(Counter(sb).items(), key=lambda kv: -kv[1])[:12]); print("type counts Tomokiyo:", sorted(Counter(tom).items(), key=lambda kv: -kv[1])[:12])

# --- count-level agreement and positional confusion (crops where both readers found the same number of glyphs)
eq = [k for k in sorted(set(A) & set(B)) if len(glyphs(A[k])) == len(glyphs(B[k]))]
print(f"crops with equal glyph counts: {len(eq)}/{len(set(A) & set(B))}; count agreement within 1: "
      f"{sum(abs(len(glyphs(A[k])) - len(glyphs(B[k]))) <= 1 for k in set(A) & set(B))}")
conf = Counter(); same = tot = 0
for k in eq:
    for x, y in zip(glyphs(A[k]), glyphs(B[k])):
        tot += 1
        if x == y: same += 1
        else: conf[tuple(sorted((x, y)))] += 1
print(f"positional label agreement on equal-count crops: {same}/{tot} = {same/max(tot,1):.3f}")
print("top confusions (unordered label pairs):", conf.most_common(15))
# how concentrated are the confusions? a systematic near-duplicate pair shows as a few pairs carrying most mass
m = sum(conf.values()); print(f"top 5 pairs carry {sum(c for _, c in conf.most_common(5))}/{m} of the disagreements")
# per-crop glyph counts against Tomokiyo's 28 fragments (crops.tsv has 29 lines; identity by order, page 2 shifted by ARM-TR2)
frag = [len(l.strip().split(";")) for l in open(REPO / "ciphers/armstrong-madison-1808/codex-2026-09-27b/glyphs.txt") if l.strip()]
print("Tomokiyo fragment glyph counts:", frag)
print("pass A per-crop counts:        ", [len(glyphs(A[k])) for k in sorted(A)])
print("pass B per-crop counts:        ", [len(glyphs(B[k])) for k in sorted(B)])
