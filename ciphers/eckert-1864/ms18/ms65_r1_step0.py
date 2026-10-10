#!/usr/bin/env python3
"""MS65-R1 step 0 (Wave 3 'Step-0 ruling', 10 Oct 2026): per entry, (a) ordered overlap = LCS of content words between the decoded body (No. 2 key, bracketed
meanings included, {time}/{tail} annotations dropped) and the holder transcription of the entry's lines, / decoded content words; (b) control = same LCS against the
transcription words shuffled within the entry, 20 draws, p95; (c) decoded content words NOT in the transcription at all. Numbers are spelled as words on both sides.
Disk only. Usage: n2r6_step0.py"""
import re, random, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); import decode
FUNC = set("the a an of to and in is are was were be been for on at by with that this it as or not but from have has had will would shall should you your i we he his her him them they their there then than so if do does did can could may might must".split())
ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = {20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}
def num(n):
    n = int(n)
    if n < 20: return [ONES[n]]
    if n < 100: return [TENS[n//10*10]] + ([ONES[n%10]] if n%10 else [])
    if n < 1000: return [ONES[n//100], "hundred"] + (num(n%100) if n%100 else [])
    return [str(n)]
def words(t):
    out = []
    for w in re.findall(r"\d+|[a-z]+", t.lower()):
        out += num(w) if w.isdigit() else [w]
    return [w for w in out if w not in FUNC and len(w) > 1]
def lcs(a, b):
    m = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(len(a)):
        for j in range(len(b)):
            m[i+1][j+1] = m[i][j]+1 if a[i]==b[j] else max(m[i][j+1], m[i+1][j])
    return m[-1][-1]
k = decode.load_key(HERE/"key.md")
rnd = random.Random(11)
for h, l in decode.load_ciphertext(HERE/"ms18"/"ms65_r1_entries.txt"):
    text = decode.entry_text(l); r, _ = decode.decode_entry(text, k)
    r0 = r; r = re.sub(r"\{[^}]*\}", " ", r)
    if not words(r): r = re.sub(r"\{(time|tail):", " ", r0).replace("}", " ")  # Y9: the decoder put the whole body in {tail:}; keep it (note in NOTES)
    dec = words(re.sub(r"[\[\]]", " ", r)); tr = words(re.sub(r"\s*=\s*", "", text))
    a = lcs(dec, tr)/len(dec); ctl = []
    for _ in range(20):
        s = tr[:]; rnd.shuffle(s); ctl.append(lcs(dec, s)/len(dec))
    ctl.sort(); p95 = ctl[18]
    miss = sorted(set(w for w in dec if w not in set(tr)))
    print(f"{h.split('|')[0].strip()[:3]} a={a:.3f} ({lcs(dec,tr)}/{len(dec)}) b_p95={p95:.3f} hit={'YES' if a>=0.5 and a>p95 else 'no'} (c)={len(miss)}: {' '.join(miss)}")
