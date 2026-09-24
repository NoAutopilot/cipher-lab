#!/usr/bin/env python3
"""Cheap test 1 (24 Sept 2026): index of coincidence and unigram shape of the five Koehler cryptograms (Kahn,
Cryptologia 5(2), April 1981; transcription as printed on Cipherbrain, sources/schmeh/posts/47b-koehler-update-2021.txt).
Question: transposition (IC of the plaintext language survives) or substitution/one-time (IC flattened)?
Controls, same lengths: (a) German plaintext (tools/data/de16/composed_enhg.txt, Early New High German, the only
German corpus on disk), (b) English plaintext (tools/data/pg1661_holmes.txt), (c) uniform random letters.
Reports both target and control numbers (CLAUDE.md rule 3)."""
import random, re, sys
from collections import Counter
from pathlib import Path
random.seed(1)
ROOT = Path(__file__).resolve().parents[2]
txt = (ROOT / "sources/schmeh/posts/47b-koehler-update-2021.txt").read_text(encoding="utf-8")
lines = txt.splitlines()
msgs, cur, key = {}, None, None
for ln in lines:
    s = ln.strip().lower()
    if re.fullmatch(r"(237|178|137|140|229)", s):
        key = s; cur = []; msgs[key] = cur; continue
    if key and cur is not None:
        if re.fullmatch(r"([a-z]{1,5} ?)+\.?", s) and s:
            cur.extend(re.findall(r"[a-z]+", s))
            if s.endswith("."): key = None
        elif s: key = None
def ic(s):
    c = Counter(s); n = len(s)
    return sum(v*(v-1) for v in c.values()) / (n*(n-1)) if n > 1 else 0
def corpus(p):
    t = re.sub(r"[^a-z]", "", (ROOT / p).read_text(encoding="utf-8", errors="replace").lower().replace("ä","ae").replace("ö","oe").replace("ü","ue").replace("ß","ss"))
    return t
de = corpus("tools/data/de16/composed_enhg.txt"); en = corpus("tools/data/pg1661_holmes.txt")
print("msg\tlen\tdistinct\tIC\tIC_de_ctrl\tIC_en_ctrl\tIC_random")
allc = ""
for k, ws in msgs.items():
    s = "".join(ws); allc += s
    n = len(s)
    ics = lambda t: sum(ic(t[i:i+n]) for i in (random.randrange(len(t)-n) for _ in range(50)))/50
    print(f"{k}\t{n}\t{len(set(s))}\t{ic(s):.4f}\t{ics(de):.4f}\t{ics(en):.4f}\t{sum(ic(''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(n)))for _ in range(50))/50:.4f}")
n = len(allc)
print(f"pooled\t{n}\t{len(set(allc))}\t{ic(allc):.4f}\t(German plain ~0.076, English ~0.066, uniform 0.0385)")
cnt = Counter(allc)
print("pooled unigram, most common:", cnt.most_common(8))
print("pooled unigram, least common:", cnt.most_common()[-6:])
# chi-square vs uniform over 26 letters
exp = n/26
chi = sum((cnt.get(ch,0)-exp)**2/exp for ch in "abcdefghijklmnopqrstuvwxyz")
print(f"chi-square vs uniform (25 df; 37.7 at p=0.05, 44.3 at p=0.01): {chi:.1f}")
if len(msgs) != 5 or any(len("".join(v)) != int(k) for k, v in msgs.items()):
    print("WARNING: parsed lengths differ from Kahn's headers:", {k: len(''.join(v)) for k, v in msgs.items()}); sys.exit(1)
