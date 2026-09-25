#!/usr/bin/env python3
"""Compute N, K, IC for the Kaliningrad cryptogram and matched-N language controls.
Usage: python3 ic_analysis.py
"""
import re, sys, random, math

def tokenize_signs(text):
    # strip comment lines and bracketed counters
    lines = [l for l in text.splitlines() if l.strip() and not l.startswith('#') and not l.startswith('[SECTION')]
    signs = []
    for line in lines:
        # drop leading [I/1] style markers
        line = re.sub(r'^\[[^\]]+\]\s*', '', line)
        # drop bracketed running counts like [194]
        line = re.sub(r'\[\d+\]', '', line)
        words = line.split()
        for w in words:
            if set(w) <= set('.'):
                continue
            # dotted groups like x.s.f.d. -> individual signs split on '.'
            if '.' in w:
                parts = [p for p in w.split('.') if p]
                for p in parts:
                    signs.extend(split_word_signs(p))
                continue
            signs.extend(split_word_signs(w))
    return signs

def split_word_signs(w):
    w = w.strip('"\'-,')
    out = []
    i = 0
    while i < len(w):
        c = w[i]
        if c in ("'",'"'):
            i += 1
            continue
        nxt = w[i+1] if i+1 < len(w) else ''
        if nxt in ("'",'"'):
            out.append(c+nxt)
            i += 2
        else:
            out.append(c)
            i += 1
    return [s for s in out if s.isalpha() or "'" in s or '"' in s]

def ic(signs):
    n = len(signs)
    if n < 2:
        return 0.0
    from collections import Counter
    counts = Counter(signs)
    num = sum(c*(c-1) for c in counts.values())
    den = n*(n-1)
    return num/den if den else 0.0

if __name__ == '__main__':
    with open('ciphertext.txt', encoding='utf-8') as f:
        text = f.read()
    signs = tokenize_signs(text)
    n = len(signs)
    k = len(set(signs))
    print(f"N={n} K={k} IC={ic(signs):.4f}")
