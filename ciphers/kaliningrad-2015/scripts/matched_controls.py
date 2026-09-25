#!/usr/bin/env python3
"""Matched-N IC controls for the Kaliningrad cryptogram: transliterated Russian and German
at the same letter count N as the target. 20 random windows each, mean and range reported.
"""
import random, re
from collections import Counter

RU_MAP = {
 'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'e','ж':'zh','з':'z','и':'i','й':'i',
 'к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f',
 'х':'h','ц':'c','ч':'ch','ш':'sh','щ':'shch',"ъ":"'",'ы':'y',"ь":"'",'э':'e','ю':'yu','я':'ya',
}

def transliterate_ru(text):
    out = []
    for ch in text.lower():
        if ch in RU_MAP:
            out.append(RU_MAP[ch])
    return ''.join(out)

def clean_de(text):
    out = []
    for ch in text.lower():
        if ch.isalpha() and ch.isascii() or ch in 'äöüß':
            out.append(ch)
    return ''.join(out)

def ic(s):
    n = len(s)
    if n < 2:
        return 0.0
    counts = Counter(s)
    num = sum(c*(c-1) for c in counts.values())
    den = n*(n-1)
    return num/den if den else 0.0

def windows(letters, n, trials, seed):
    rng = random.Random(seed)
    out = []
    if len(letters) <= n:
        return [letters]
    for _ in range(trials):
        start = rng.randint(0, len(letters)-n-1)
        out.append(letters[start:start+n])
    return out

if __name__ == '__main__':
    N = 978  # from ic_analysis.py on ciphertext.txt (sign count incl. apostrophe-merged units)
    with open('scripts/ru_gutenberg_30774.txt', encoding='utf-8') as f:
        ru_raw = f.read()
    ru_letters = transliterate_ru(ru_raw)
    with open('../../tools/data/de16/composed_enhg.txt', encoding='utf-8', errors='ignore') as f:
        de_raw = f.read()
    de_letters = clean_de(de_raw)

    for name, letters in [('ru (transliterated, 30774)', ru_letters), ('de (composed_enhg)', de_letters)]:
        ws = windows(letters, N, 20, 42)
        ics = [ic(w) for w in ws]
        print(f"{name}: n_letters_total={len(letters)} windows={len(ws)} IC mean={sum(ics)/len(ics):.4f} range=({min(ics):.4f}-{max(ics):.4f})")
