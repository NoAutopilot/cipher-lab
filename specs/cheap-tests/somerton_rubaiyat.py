#!/usr/bin/env python3
"""Cheap test 3 (24 Sept 2026): host-text-as-key for the Somerton Man code (Tamam Shud, 1948). The five letter lines
were written inside the back cover of a copy of FitzGerald's Rubaiyat; Abbott's group (2009-14) argues the letters are
word initials. Question: is any line, or any substring of 5+ letters, the initial-letter sequence of consecutive words
in FitzGerald's text (first and fifth editions, Project Gutenberg #246, tools/data/pg246_rubaiyat.txt)?
Control: 1000 random strings of the same lengths drawn from the initial-letter distribution of English prose
(tools/data/pg1661_holmes.txt), searched the same way. Reports both numbers (CLAUDE.md rule 3)."""
import random, re
from collections import Counter
from pathlib import Path
random.seed(1)
ROOT = Path(__file__).resolve().parents[2]
t = (ROOT / "tools/data/pg246_rubaiyat.txt").read_text(encoding="utf-8", errors="replace")
a, b = t.find("*** START OF"), t.find("*** END OF")
t = t[t.find("\n", a)+1:b]
words = re.findall(r"[A-Za-z]+", t)
host = "".join(w[0].upper() for w in words)
# code lines: Wikipedia/Schmeh transcription; first letters M/W ambiguous on lines 1 and 3
lines = {"L1": ["MRGOABABD", "WRGOABABD"], "L2": ["MLIAOI"], "L3": ["MTBIMPANETP", "WTBIMPANETP"],
         "L4": ["MLIABOAIAQC"], "L5": ["ITTMTSAMSTGAB"]}
def hits(s, minlen=5):
    out = set()
    for L in range(len(s), minlen-1, -1):
        for i in range(len(s)-L+1):
            sub = s[i:i+L]
            if sub in host: out.add(sub)
    return sorted(out, key=len, reverse=True)
print(f"host: {len(words)} words in Gutenberg #246 (both editions + notes); initial string length {len(host)}")
best_target = 0
for k, vs in lines.items():
    for v in vs:
        h = hits(v)
        top = h[:3]
        best_target = max(best_target, len(h[0]) if h else 0)
        print(f"{k} {v}: longest match {len(h[0]) if h else '<5'} {top}")
en = (ROOT / "tools/data/pg1661_holmes.txt").read_text(encoding="utf-8", errors="replace")
dist = Counter(w[0].upper() for w in re.findall(r"[A-Za-z]+", en))
letters, weights = zip(*dist.items())
lens = [9, 6, 11, 11, 13]
N = 1000
longest = Counter()
for _ in range(N):
    m = 0
    for L in lens:
        s = "".join(random.choices(letters, weights, k=L))
        h = hits(s); m = max(m, len(h[0]) if h else 0)
    longest[m] += 1
print(f"control: {N} random 5-line sets from English initial-letter distribution; longest match per set:",
      dict(sorted(longest.items())))
p = sum(v for k, v in longest.items() if k >= best_target) / N if best_target else 1.0
print(f"target longest match {best_target}; fraction of control sets reaching >= that: {p:.3f}")
