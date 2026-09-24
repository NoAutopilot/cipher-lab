#!/usr/bin/env python3
"""J7 (24 Sept 2026): matched control for the 5549 body (rule 3).
Plaintext: Groen IV CDXLIV (WVO 5797, Lodewijk/Jan to Willem, Oct 1573), held out of corpus_T.txt.
Design: 82 letter signs (homophones by corpus letter frequency), 20 syllable signs, 14 common-word signs and 18
name/noun signs (the 5549 body: 82 distinct values below 100, 52 above; 24% of tokens above 99), one null at 1%.
Run pattern: j7/body_5549.txt (61 runs, same lengths; clear frames of the same letter length; in-run fragments)."""
import json, os, re, sys
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..', '..', '..', 'tools'))
import german_ngram as g
t = open(os.path.join(H, 'src_cdxliv.txt'), encoding='utf-8').read()
t = re.sub(r'\b(margenoot|voetnoot|pagina|Over|Octobre)\b\S*', ' ', t)
t = re.sub(r'\[p\. [^\]]*\]', ' ', t)
z = '#'.join(g.select(t))
z = re.sub(r'#(p|s)#', '#', z)
open(os.path.join(H, 'control_plain.txt'), 'w').write('#' + z + '#\n')
freq = Counter(open(os.path.join(H, 'corpus_T.txt')).read().replace('#', '').replace('\n', ''))
tot = sum(freq[c] for c in g.ALPHA)
hom = {c: max(1, round(80 * freq[c] / tot)) for c in g.ALPHA}
while sum(hom.values()) > 82:
    c = max(hom, key=lambda c: hom[c] - 80 * freq[c] / tot); hom[c] -= 1
while sum(hom.values()) < 82:
    c = max(hom, key=lambda c: 80 * freq[c] / tot - hom[c]); hom[c] += 1
for c in g.ALPHA:
    if hom[c] == 0:
        hom[c] = 1; hom[max(hom, key=hom.get)] -= 1
design = dict(letters=g.ALPHA, homophones=hom,
              syllables=["en", "er", "ch", "ge", "ei", "ie", "un", "in", "st", "an", "de", "te", "ben", "den", "sch",
                         "uer", "ten", "ich", "ung", "gen"],
              words=["und", "der", "die", "das", "zu", "uon", "nicht", "mit", "den", "in", "auch", "ist", "wir", "sich",
                     "gott", "alba", "almechtige", "herzog", "konig", "dateno", "delfft", "seras", "franckreich",
                     "keiser", "reichstag", "kolln", "sachsen", "speir", "franckfurt", "churfurst", "graueneinigung",
                     "almechtigen"],
              nulls=1, null_rate=0.01, syl_rate=0.8)
json.dump(design, open(os.path.join(H, 'control_design.json'), 'w'), indent=1)
print(sum(hom.values()), hom, len(z.replace('#', '')), 'letters of plaintext')
