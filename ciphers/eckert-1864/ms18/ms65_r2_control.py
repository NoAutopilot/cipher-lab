#!/usr/bin/env python3
"""MS65-R2 (10 Oct 2026): matched control for the rows guessed Cipher No. 2 (same statistic as ls3_r18_control.py, rule 3).
Per entry: (a) does the decoded time word equal the time the ledger writes in the entry's own header/tail (a plain "5 PM", "1230 Pm", "12 M")?
(b) does a decoded day numeral equal the day the header writes ("Oct 22nd")? Under book 1, 2, 9, and under 200 meaning-shuffled copies of each book
(meanings permuted among rows of the same kind, seeds 1000+i). H counts tie with the shuffles by construction (a shuffle keeps which words are in
the key), so they are NOT the test. Usage: ms18_n2g_control.py"""
import random, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); import decode
BOOKS = {"1": "key.md", "2": "key-no2.md", "9": "key-no9.md"}
SEEDS = 200
def norm_time(s):
    m = re.search(r"(\d{1,2})[.:]?(\d\d)?\s*([AaPp])\.?\s*[Mm]\b", s)
    if m: return f"{int(m.group(1))}.{m.group(2) or '00'} {m.group(3).upper()}M"
    m = re.fullmatch(r"\s*(12)\s*(M|m)?\s*", s)
    return "12.00 PM" if m else None
def shuffled(key, seed):
    rng = random.Random(seed); by = {}
    for w, (m, g, k) in key.items(): by.setdefault(k, []).append(w)
    out = {}
    for k, ws in by.items():
        if k == "numeral": ws = [w for w in ws if key[w][0].split()[0].isdigit()]
        vals = [key[w] for w in ws]; rng.shuffle(vals)
        for w, v in zip(ws, vals): out[w] = v
    return out
def hdr_facts(lines):
    lines = [l for l in lines if not re.match(r"^\(?\s*No\.? ?\d", l)]  # header remnants of the next entry (image-read, p9874/p9913): "( No 1 ) 1230 Pm", "No 1  5 PM"
    txt = " ".join(lines)
    t = None
    for m in re.finditer(r"(?<![\w.])(\d{1,2}[.:]?\d{0,2}\s*[AaPp][Mm]\b|\b12\s*M\b)", txt):
        t = norm_time(m.group(1)); break
    md = re.search(r"\b(?:Jan|Feb|Mar|Apr|May|June?|July?|Aug|Sept?|Oct|Nov|Dec)\w*\.?\s+(\d{1,2})", lines[0] if len(lines[0]) > 8 else txt)
    return t, (md.group(1) if md else None)
def check(text, key, ht, hd):
    r, _ = decode.decode_entry(text, key)
    tt = re.findall(r"\{time: ([^}]*)\}", r); dd = re.findall(r"\[(\d{1,2})\]", r) + re.findall(r"\{date: [A-Za-z]+ (\d+)\}", r)
    return (None if ht is None else bool(tt) and norm_time(tt[0]) == ht), (None if hd is None else hd in dd)
keys = {b: decode.load_key(HERE/f) for b, f in BOOKS.items()}
print("row | header time / day | time agrees (book 1/2/9) | day agrees (1/2/9) | shuffled book 2: time / day agree of %d | shuffled book 1: time / day" % SEEDS)
for header, lines in decode.load_ciphertext(HERE/"ms18"/"ms65_r2_entries.txt"):
    text = decode.entry_text(lines); ht, hd = hdr_facts(lines)
    real = {b: check(text, keys[b], ht, hd) for b in keys}
    f = lambda x: "NT" if x is None else ("Y" if x else "n")
    s = {}
    for b in ("2", "1"):
        tc = dc = 0
        for i in range(SEEDS):
            a, c = check(text, shuffled(keys[b], 1000+i), ht, hd); tc += bool(a); dc += bool(c)
        s[b] = (tc, dc)
    print(f"{header.split(' |')[0]} {header.split('(')[-1].rstrip(')')} | {ht} / {hd} | " + "/".join(f(real[b][0]) for b in "129") + " | " + "/".join(f(real[b][1]) for b in "129") + f" | {s['2'][0]} / {s['2'][1]} | {s['1'][0]} / {s['1'][1]}")
