#!/usr/bin/env python3
"""N2R-5 step 0: per entry, decoded content words (brackets removed) that already stand as the same plain word in the transcription / decoded content words."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); import decode
FUNC = set("the a an of to and in is are was were be been for on at by with that this it as or not but from have has had will would shall should you your i we he his her him them they their there then than so if do does did can could may might must".split())
k = decode.load_key(HERE/"key-no2.md")
for h, l in decode.load_ciphertext(HERE/"ms18"/"n2r5_entries.txt"):
    text = decode.entry_text(l); r, _ = decode.decode_entry(text, k)
    tr = set(re.findall(r"[a-z]+", re.sub(r"\s*=\s*", "", text.lower())))
    dec = [w for w in re.findall(r"[a-z]+", re.sub(r"[\[\]{}]", " ", re.sub(r"\s*=\s*", "", r.lower()))) if w not in FUNC and len(w) > 1]
    print(h.split("|")[0].strip(), sum(1 for w in dec if w in tr), len(dec))
