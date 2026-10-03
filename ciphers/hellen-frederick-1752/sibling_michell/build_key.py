#!/usr/bin/env python3
"""Build key_sibling.tsv from DECODE's transcriptions of the period interlinear decipherments of
Michell (Prussian envoy, London) to Frederick II, KHA PWV inv. 198 -- DECODE R1050 (28 Aug/8 Sept 1752, 2 pp.)
and R1051 (1/12 Nov 1751, 1 p.), transcriber "XZ", March 2020 (files DOC_R1050_D1938_1938.txt, DOC_R1051_D1940_1940.txt,
fetched 3 Oct 2026). Each <PLAINTEXT> line is the period decipherer's interlinear gloss over the code line below it.
A line is paired word-for-code only when its word count equals its code count; other lines are skipped and counted.
Values are the PERIOD gloss of Michell's code: for the Hellen target they are a sibling key (grade S at best, rule 4).
Usage: python3 build_key.py [--check]   (--check exits 1 if key_sibling.tsv is stale)"""
import re, sys, collections, os
HERE = os.path.dirname(os.path.abspath(__file__))
FILES = [('R1050', 'DOC_R1050_D1938_1938.txt'), ('R1051', 'DOC_R1051_D1940_1940.txt')]

def codes(line):
    line = line.replace('1/2', '½')
    out = []
    for tok in re.split(r',\s*|\s{2,}|\.\s*$', line.strip()):
        tok = re.sub(r'[\s_]', '', tok)
        if tok:
            out.append(tok)
    return out

def build():
    pairs, skipped, used = collections.defaultdict(collections.Counter), [], 0
    for rec, fn in FILES:
        lines = open(os.path.join(HERE, fn), encoding='utf-8').read().splitlines()
        for i, l in enumerate(lines):
            m = re.match(r'<PLAINTEXT FR (.*)>\s*$', l)
            if not m or i + 1 >= len(lines):
                continue
            words = m.group(1).split()
            cs = codes(lines[i + 1])
            if len(words) != len(cs):
                skipped.append((rec, i + 1, len(words), len(cs)))
                continue
            used += 1
            for w, c in zip(words, cs):
                pairs[c][(w, rec)] += 1
    return pairs, skipped, used

def render(pairs):
    rows = ['code\tvalue\tgrade\tsource\tnote']
    def k(c):
        d = re.sub(r'\D', '', c) or '0'
        return (int(d), c)
    for c in sorted(pairs, key=k):
        vals = collections.Counter()
        recs = collections.defaultdict(set)
        for (w, rec), n in pairs[c].items():
            vals[w] += n; recs[w].add(rec)
        if not re.fullmatch(r'\d+½?', c):
            continue  # uncertain transcription ('3?', '2863l', '0/3?')
        if len(vals) == 1:
            w, n = vals.most_common(1)[0]
            v, note = w, f'n={n}'
        else:
            v = '|'.join(w for w, _ in vals.most_common())
            note = 'conflict ' + ','.join(f'{w}:{n}' for w, n in vals.most_common())
        src = 'Michell sibling, DECODE ' + '+'.join(sorted(set().union(*recs.values())))
        rows.append(f'{c}\t{v}\tS\t{src}\t{note}')
    return '\n'.join(rows) + '\n'

if __name__ == '__main__':
    pairs, skipped, used = build()
    out = render(pairs)
    path = os.path.join(HERE, 'key_sibling.tsv')
    if '--check' in sys.argv:
        sys.exit(0 if open(path).read() == out else 1)
    open(path, 'w').write(out)
    print(f'lines paired {used}, skipped {len(skipped)} (word/code count mismatch): {skipped}')
    print(f'codes {out.count(chr(10)) - 1}')
