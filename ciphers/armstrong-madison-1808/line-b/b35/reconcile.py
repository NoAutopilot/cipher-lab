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
        for line in open(HERE / n, encoding="utf-8"):
            p = line.rstrip("\n").split("\t")
            if len(p) < 3 or not p[0].strip().isdigit(): continue
            rows[int(p[0])] = p[2].split()
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
