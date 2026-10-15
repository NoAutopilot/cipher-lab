#!/usr/bin/env python3
"""SUR-2061 (15 Oct 2026): slide each word of den Heijer 2012 p.362's Dutch legend gloss over the 2061 battery decode
(reading_2061_battery_nieuw_tokens.tsv) and score under PREREG-SUR-2061.md rule 2: a MATCH is a contiguous span with
>= 2 U/M tokens covered, zero H/C/S conflicts, every M token's value set containing the crib letter. Strict letters, with
an optional y~ij / i~j / z~s / c~k orthographic table reported separately (--ortho). Usage: python3 align_heijer_p362.py CRIB.txt"""
import csv, re, sys, os, itertools
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(H, '..', 'reading_2061_battery_nieuw_tokens.tsv')
ortho = '--ortho' in sys.argv
EQ = {('y','i'),('i','y'),('i','j'),('j','i'),('y','j'),('j','y'),('z','s'),('s','z'),('c','k'),('k','c'),('c','s'),('s','c')}
rows = [r for r in csv.DictReader(open(T), delimiter='\t')]
lines = {}
for r in rows: lines.setdefault(r['line'], []).append(r)
def letters(r):
    v = r['value']
    if v == '?' : return None              # U: any letter
    if '|' in v: return set(v.split('|'))
    return {v}
def single(r): return len(r['value']) == 1 or '|' in r['value'] or r['value'] == '?'
crib = open(sys.argv[1]).read().lower()
crib = crib.replace('ij', 'y') if '--ij2y' in sys.argv else crib
words = sorted(set(w for w in re.findall(r'[a-zëéè]+', crib) if len(w) >= 4))
out = []
for ln, toks in lines.items():
    for w in words:
        w2 = w.replace('ë','e').replace('é','e')
        for s in range(len(toks) - len(w2) + 1):
            span = toks[s:s+len(w2)]
            if not all(single(t) for t in span): continue
            agree = conf = um = 0; detail = []
            for t, c in zip(span, w2):
                L = letters(t); g = t['grade']
                ok = L is None or c in L or (ortho and any((c, x) in EQ for x in L))
                if g in 'HCS':
                    if ok: agree += 1
                    else: conf += 1
                else:
                    if ok: um += 1
                    else: conf += 1
                detail.append(f"{t['pos']}:{t['value']}{g}")
            if conf == 0 and um >= 2:
                out.append((ln, w2, span[0]['pos'], agree, um, ' '.join(detail)))
print('line\tcrib_word\tstart_pos\tHC_agree\tUM_covered\ttokens')
for o in sorted(out): print('\t'.join(map(str, o)))
