#!/usr/bin/env python3
"""passnorm.py -- mechanical notation normaliser for blind Sonnet passes (RUN1-ES132, 4 Oct 2026).

Glyph-shape spellings only, applied identically to every pass and decided before any test 1 score was computed:
 'e' or 'ι' written as a vowel sign -> ρ / ⊣ (the looped ρ sign reads as an 'e'; the u-hook as 'ι': revised 4 Oct
 2026 after the first scoring run from ι -> σ, by comparing the glyph with test 0's reconciled 2⊣ on f.119v; both
 blind-pass numbers in NOTES.md are from the revised map);
 a trailing '6' on a token whose stem is a Cp.30 base 1-37 and whose whole number is >= 38 (e.g. 236, 66, 326) -> σ
 (the σ hook reads as a '6'; test 0's passes wrote 256/316 for 25σ/31σ); tokens carrying @c are left as codes;
 vowel signs written after an above-mark are moved before it (22@nρ -> 22ρ@n); a repeated vowel sign is kept once;
 '35_6' -> 35_σ; 'ω' -> '10' (shape of the '10' ligature); brace words and everything else unchanged.
Usage: passnorm.py PASS.tsv  (prints the normalised lines)
"""
import re, sys
VOWELS = '+.σρ⊣'

def norm_tok(t):
    if t.startswith('{') or t in ('/', '#'): return t
    q = '?' if t.endswith('?') else ''
    t = t.rstrip('?').replace('ω', '10')
    m = re.match(r'^(\d+|[A-Za-z])(_?)(.*)$', t)
    if not m: return t + q
    base, und, rest = m.groups()
    rest = rest.replace('e', 'ρ').replace('ι', '⊣')
    if und and rest[:1] == '6': rest = 'σ' + rest[1:]  # 35_6 -> 35_σ
    marks = re.findall(r'@(?:\d|[a-z])', rest)
    vows = [c for c in re.sub(r'@(?:\d|[a-z])', '', rest) if c in VOWELS]
    if base.isdigit() and len(base) >= 2 and base.endswith('6') and int(base) >= 38 and 1 <= int(base[:-1]) <= 37 \
            and '@c' not in marks:
        base = base[:-1]; vows = ['σ'] + vows
    v = vows[0] if vows else ''
    return base + und + v + ''.join(marks) + q

def norm_line(s):
    return ' '.join(norm_tok(t) for t in s.split())

if __name__ == '__main__':
    for l in open(sys.argv[1], encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        a, b = l.rstrip('\n').split('\t', 1)
        print(a + '\t' + norm_line(b))
