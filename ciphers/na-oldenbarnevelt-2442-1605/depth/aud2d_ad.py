#!/usr/bin/env python3
"""AUD2D-OLD2442 (8 Oct 2026): authentication distance (AD) for the vowel-digit design of NA 3.01.14 inv. 2442.

R = redundancy per digit token = log2(5) - H(vowel | consonant frame), the frame being the word's skeleton with every
vowel position masked (in this design every vowel, and v, is a digit; consonants are clear). H(vowel | frame) is a
held-out cross-entropy: skeleton->vowel-string counts from six es1600 volumes, scored on the seventh (XCVI, a non-Osuna
volume), add-alpha backoff to the vowel-unigram model for unseen skeletons. A plug-in (train=test) figure is printed too;
it overstates redundancy and is not used.
H(K) design level = log2(5!) for the digit->vowel map over the five digits used (2,3,4,7,8), plus liberties (counted
from reading_tokens.tsv / overrides.tsv in aud2d_runs.py). A sensitivity row uses log2(23P5) (digits free over the whole
alphabet, VX-CT03's own solver setting). Unicity U = H(K)/R digit tokens; AD = 1.5 U.
Usage: python3 aud2d_ad.py            (reads tools/data/es1600/*.txt.gz)
"""
import gzip, math, re, sys, unicodedata
from collections import Counter, defaultdict
from pathlib import Path
DATA = Path(__file__).resolve().parents[3] / "tools" / "data" / "es1600"
VOLS = ["42", "43", "44", "45", "46", "47", "96"]
VOW = set("aeiou")

def fold(w):
    w = unicodedata.normalize("NFD", w.lower())
    w = "".join(c for c in w if not unicodedata.combining(c))
    return w.replace("v", "u")

def words(vol):
    t = gzip.open(DATA / f"coleccindedocu{vol}madruoft.txt.gz", "rt", encoding="utf-8").read()
    for w in re.findall(r"[^\W\d_]+", t):
        w = fold(w)
        if w == "y":
            w = "i"
        if any(c in VOW for c in w):
            yield w

def split(w):
    return "".join("_" if c in VOW else c for c in w), "".join(c for c in w if c in VOW)

def train(vols):
    sk = defaultdict(Counter); uni = Counter()
    for v in vols:
        for w in words(v):
            s, vs = split(w); sk[s][vs] += 1; uni.update(vs)
    return sk, uni

def xent(sk, uni, vols, alpha=1.0):
    tot = sum(uni.values()); pu = {c: uni[c] / tot for c in "aeiou"}
    bits = 0.0; nv = 0
    for v in vols:
        for w in words(v):
            s, vs = split(w)
            pb = math.prod(pu[c] for c in vs)
            c = sk.get(s); n = sum(c.values()) if c else 0
            p = ((c[vs] if c else 0) + alpha * pb) / (n + alpha)
            bits += -math.log2(p); nv += len(vs)
    return bits / nv, nv, pu

if __name__ == "__main__":
    sk, uni = train(VOLS[:-1])
    h, nv, pu = xent(sk, uni, VOLS[-1:])
    hu = -sum(p * math.log2(p) for p in pu.values())
    skall, uall = train(VOLS)
    hp, _, _ = xent(skall, uall, VOLS[-1:], alpha=1e-9)
    R = math.log2(5) - h
    print(f"vowel unigram H = {hu:.3f} bits; held-out H(V|skeleton) = {h:.3f} bits/vowel over {nv} vowels (test XCVI)")
    print(f"plug-in (train=test, not used) H(V|skeleton) = {hp:.3f}")
    print(f"R = log2(5) - H = {math.log2(5):.3f} - {h:.3f} = {R:.3f} bits per digit token")
    for name, hk in (("vowel map 5! (brief's design level)", math.log2(120)),
                     ("free over 23 letters 23P5 (sensitivity)", math.log2(23 * 22 * 21 * 20 * 19))):
        print(f"{name}: H(K0) = {hk:.2f} bits; unicity(no liberties) = {hk / R:.1f} digits; AD = {1.5 * hk / R:.1f} digits")
