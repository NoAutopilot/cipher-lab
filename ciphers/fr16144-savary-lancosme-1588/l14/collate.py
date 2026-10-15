#!/usr/bin/env python3
"""SAV-L14 collation (PREREG-SAV-L14.md): word-level LCS recall of a gloss reading against a printed text, PX-BRODEC-normalised.
Usage: collate.py GLOSS.tsv PRINT.txt [--control CTRL.txt] [--shuffles 20]. Offline, deterministic (seed 0)."""
import sys, re, random, unicodedata, argparse
ABBR = [(r"\bamb\w*'?", 'ambassadeur'), (r"\bseig\w*'?", 'seigneur'), (r'\bg\.\s*s\.', 'grand seigneur'),
        (r'\bv\.\s*m\.', 'vostre maieste'), (r'\bs\.\s*m\.', 'sa maieste'), (r'\bvre\s+mate\b', 'vostre maieste'), ('&', ' et ')]
def norm(t):
    t = t.lower()
    for a, b in ABBR: t = re.sub(a, b, t)
    t = unicodedata.normalize('NFD', t); t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    t = t.replace('v', 'u').replace('j', 'i').replace('y', 'i')
    return [w for w in re.split(r"[^a-z]+", t) if len(w) > 1]
def gloss_words(path):
    out = []
    for ln in open(path, encoding='utf-8'):
        if ln.startswith('#') or ln.startswith('page\t'): continue
        p = ln.rstrip('\n').split('\t')
        if len(p) < 3: continue
        out += [w for w in p[2].split() if '?' not in w and '[' not in w]   # only words the reader did not mark uncertain
    return norm(' '.join(out))
def text_words(path):
    return norm(' '.join(l for l in open(path, encoding='utf-8') if not l.startswith('#')))
def lcs(a, b):
    prev = [0] * (len(b) + 1)
    for x in a:
        cur = [0]
        for j, y in enumerate(b): cur.append(prev[j] + 1 if x == y else max(prev[j + 1], cur[j]))
        prev = cur
    return prev[-1]
ap = argparse.ArgumentParser(); ap.add_argument('gloss'); ap.add_argument('print_'); ap.add_argument('--control'); ap.add_argument('--shuffles', type=int, default=20)
a = ap.parse_args(); g = gloss_words(a.gloss); p = text_words(a.print_)
r = lcs(g, p) / max(1, len(g)); print(f'gloss_words={len(g)} print_words={len(p)} recall_print={r:.3f}')
if a.control:
    c = text_words(a.control)[:len(p)]; print(f'control_words={len(c)} recall_control={lcs(g, c) / max(1, len(g)):.3f}')
rng = random.Random(0); s = []
for _ in range(a.shuffles):
    h = g[:]; rng.shuffle(h); s.append(lcs(h, p) / max(1, len(h)))
print(f'shuffle_mean={sum(s) / len(s):.3f}')
print('gloss words found in print (set):', sorted(set(g) & set(p)))
