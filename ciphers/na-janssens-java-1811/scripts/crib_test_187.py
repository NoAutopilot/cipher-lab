#!/usr/bin/env python3
"""Crib test: is leaf 187R (plain 'Extrait', Batavia 20 Juin 1811) the plaintext of leaf 188 ('Numero Un')?

Compares the ordered sequence of leaf 188's keyed token values (reading_tokens.tsv, U dropped) with the word
sequence of a candidate plain text, by (S1) longest common subsequence, against a shuffled-order null of the
same candidate (rule 3: order is the axis LCS varies on), and (S2) bag-of-words coverage of leaf 188's keyed
word types, which a shuffle cannot vary, so its controls are two other Janssens texts of the same bundle
(the No.5 plain copy, the No.2 gloss). Positive control (ceiling): the No.2 cipher codes (keysource_passA.tsv,
leaves 190-192) decoded with key.tsv against the No.2 gloss words -- the key was built from that gloss, so this
is what a true cipher/plain pair scores by construction, not an independent result.
Run from the target folder: python3 scripts/crib_test_187.py [--shuffles 2000]
"""
import csv, re, random, sys, unicodedata, statistics as st
random.seed(7)
NSH = int(sys.argv[sys.argv.index('--shuffles')+1]) if '--shuffles' in sys.argv else 2000

def norm(s):
    s = unicodedata.normalize('NFKD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace("'", " ").replace("’", " ")
    return [w for w in re.findall(r"[a-z]+", s)]

def text_words(path):
    return norm(" ".join(l for l in open(path, encoding='utf-8') if not l.startswith('#')))

# leaf 188 keyed sequence
seq188 = []
for r in csv.DictReader(open('reading_tokens.tsv'), delimiter='\t'):
    if r['grade'] in ('C', 'M', 'H', 'S') and r['value'] not in ('?', ''):
        seq188 += norm(r['value'])

# No.2 gloss (leaves 190-192) codes and words; decode the codes with key.tsv
key = {}
for r in csv.DictReader(open('key.tsv'), delimiter='\t'):
    key[r['code']] = r['value']
ks = [r for r in csv.DictReader(open('keysource_passA.tsv'), delimiter='\t') if r['leaf'] in ('190', '191', '192')]
no2_gloss = []
no2_decoded = []
for r in ks:
    no2_gloss += norm(r['gloss'])
    v = key.get(r['code'].strip())
    if v and v != '?':
        no2_decoded += norm(v)

cands = {
    'leaf187R (target crib)': text_words('leaf187_text.txt'),
    'No.5 plain copy (control, other letter)': text_words('no5_plaintext.txt'),
    'No.2 gloss (control, other letter)': no2_gloss,
}
# GAPS7 (2 Oct 2026): extra candidates from the command line, e.g. --text print/opkomst13_LII_16juin1811.txt
for i, a in enumerate(sys.argv):
    if a == '--text':
        cands[f'{sys.argv[i+1]} (candidate)'] = text_words(sys.argv[i+1])

def lcs(a, b):
    prev = [0] * (len(b) + 1)
    for x in a:
        cur = [0]
        for j, y in enumerate(b):
            cur.append(prev[j] + 1 if x == y else max(prev[j + 1], cur[j]))
        prev = cur
    return prev[-1]

def run(name, q, cand):
    t = lcs(q, cand)
    null = []
    c = list(cand)
    for _ in range(NSH):
        random.shuffle(c)
        null.append(lcs(q, c))
    null.sort()
    mu, sd = st.mean(null), st.pstdev(null)
    p95, p99 = null[int(0.95 * NSH) - 1], null[int(0.99 * NSH) - 1]
    z = (t - mu) / sd if sd else float('nan')
    rank = sum(1 for n in null if n >= t)
    print(f"S1 LCS  {name}: query {len(q)} tokens, candidate {len(cand)} words: LCS {t} ({t/len(q):.3f} of query); "
          f"shuffled-order null mean {mu:.1f} sd {sd:.1f} p95 {p95} p99 {p99} max {null[-1]}; z {z:+.2f}; "
          f"null >= target: {rank}/{NSH}")
    return t, mu, p95, p99

print(f"leaf 188 keyed sequence: {len(seq188)} tokens (from reading_tokens.tsv, grades C/M, U dropped)")
for name, cand in cands.items():
    run(name + ' vs leaf 188', seq188, cand)
print(f"positive control (ceiling, by construction): No.2 codes decoded by key.tsv ({len(no2_decoded)} tokens) vs No.2 gloss ({len(no2_gloss)} words)")
run('No.2 decoded vs No.2 gloss', no2_decoded, no2_gloss)

# S2 bag of words
types188 = sorted(set(w for w in seq188 if len(w) >= 3))
content188 = sorted(w for w in types188 if len(w) >= 5)
print(f"\nS2 coverage: leaf 188 keyed word types len>=3: {len(types188)}; len>=5: {len(content188)} {content188}")
for name, cand in cands.items():
    voc = set(cand)
    hit = [w for w in types188 if w in voc]
    hitc = [w for w in content188 if w in voc]
    print(f"  {name}: vocab {len(voc)} types; covers {len(hit)}/{len(types188)} types ({len(hit)/len(types188):.2f}), "
          f"content {len(hitc)}/{len(content188)} {hitc}")
named = ['deux', 'vaisseaux', 'arrive', 'ennemie', 'debarquer', 'troupes', 'ancien', 'gouverneur', 'recu', 'seules']
print("\nVerdict's named C-grade words present in each candidate:")
for name, cand in cands.items():
    voc = set(cand)
    print(f"  {name}: {[w for w in named if w in voc]}")
