#!/usr/bin/env python3
"""W11008-KP: does WVO 5194 (24 June 1572, "George Certain" to "Lambert Certain") use the 1572 Orange-Nassau table?

  python3 w5194_gate.py            write w5194_gate.tsv
  python3 w5194_gate.py --check    exit 1 if the committed w5194_gate.tsv is stale (rule 7)

Gate pre-registered in PREREG-W11008KP.md before this score was computed. Input: w5194_ciphertext.tsv (page 1,
manuscript lines 3-8, two blind passes reconciled), runs bounded by clear words that Groen III pp.448-449 also prints;
the Groen span between the same anchors is fixed below, copied from Groen's printed words only (R2 corrected 8 Oct 2026 per AUDIT 3 item 4) (letters only; j->i, v->u, accents stripped).
Statistic: LCS between the run decoded with ../orange-nassau-1572/key_nepveu.tsv (letter codes only; every other
number dropped as null) and the Groen span. Null: 1000 seeded permutations of the 24 letter values among the 24 letter
codes. PASS per run if real > shuffle p95.
"""
import csv, os, random, sys, unicodedata
H = os.path.dirname(os.path.abspath(__file__))
KEY = {}
for r in csv.DictReader(open(os.path.join(H, '..', 'orange-nassau-1572', 'key_nepveu.tsv')), delimiter='\t'):
    KEY[int(r['group'])] = r['value'].split('/')[0]
GROEN = {  # Groen III p.448, between the clear anchors on the leaf
    'R1': ('que', 'suis', 'comme je'),
    'R2': ('suis', 'toujours', "resolu en campagne je me trouve"),
}
def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if c.isalpha() and ord(c) < 128)
    return s.replace('j', 'i').replace('v', 'u')
runs = {}
for r in csv.DictReader(open(os.path.join(H, 'w5194_ciphertext.tsv')), delimiter='\t'):
    if r['run'] and r['token'].isdigit():
        runs.setdefault(r['run'], []).append(int(r['token']))
def dec(k, codes): return norm(''.join(k[c] for c in codes if c in k))
def lcs(a, b):
    p = [0] * (len(b) + 1)
    for x in a:
        q = [0]
        for j, y in enumerate(b):
            q.append(p[j] + 1 if x == y else max(p[j + 1], q[j]))
        p = q
    return p[-1]
def main():
    codes = sorted(KEY); vals = [KEY[c] for c in codes]
    rng = random.Random(5194)
    shuf = []
    for _ in range(1000):
        v = vals[:]; rng.shuffle(v); shuf.append(dict(zip(codes, v)))
    out = ['run\tanchors\tn_codes\tn_letter_codes\tdecode\tgroen\treal_lcs\tshuf_mean\tshuf_p95\tge_real\tverdict']
    for run, (a, b, g) in GROEN.items():
        c = runs[run]; G = norm(g); dd = dec(KEY, c); real = lcs(dd, G)
        s = sorted(lcs(dec(k, c), G) for k in shuf)
        p95 = s[949]; ge = sum(x >= real for x in s)
        out.append(f'{run}\t{a}..{b}\t{len(c)}\t{sum(x in KEY for x in c)}\t{dd}\t{G}\t{real}\t{sum(s)/1000:.2f}\t{p95}\t{ge}\t'
                   + ('PASS' if real > p95 else 'MISS'))
    txt = '\n'.join(out) + '\n'
    path = os.path.join(H, 'w5194_gate.tsv')
    if '--check' in sys.argv:
        ok = os.path.exists(path) and open(path).read() == txt
        print('w5194_gate.tsv', 'current' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(path, 'w').write(txt); print(txt)
main()
