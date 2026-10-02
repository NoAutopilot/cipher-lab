#!/usr/bin/env python3
"""ce36_dict.py -- GAPS13 (2 Oct 2026): is code 36 c or e? Word-level dictionary test, disk only (CLAUDE.md rule 3).
Word list: every word of tools/data/es18 (1690-1725) + tools/data/es17c (Memorial historico, 1640s) seen >= --minf times,
normalized by one orthographic fold applied identically to the list and to both candidate readings: lower case, accents
folded, h dropped, y->i, v->u, b->u, z->c, ç->c, j->x, doubled letters collapsed (period spelling: zyrcunstanzyas ~
circunstancias, ybyere ~ hubiere). Body words: the key-regenerated body (reading_tokens.tsv L01-L14, NULL dropped) cut at
the word boundaries in SEG below (segmentation written once, before the test, and identical under c and e).
Statistic per position: form the word with the letter as c and as e; 'c-only' / 'e-only' if exactly one is in the list.
Target score: number of the 4 code-36 occurrences that are c-only (c = the predicted, committed M value).
Controls (each can vary on the score):
 (a) label shuffle, --seeds seeds: the predicted letter at each occurrence drawn c/e at random (a pure permutation of an
     all-c prediction cannot change the score -- rule 3's orthogonal-control case -- so labels are redrawn, not permuted);
     score = occurrences exclusive AND matching the drawn label.
 (b) position shuffle, --seeds seeds: the same c-vs-e word test at 4 random C-graded body positions (any letter, not 36);
     score = c-only count there -- the word list's bare bias toward c.
 (c) known answer: every C-graded body c or e (not 36), word with the true letter vs the other; accuracy = true-only /
     (true-only + wrong-only), per class.
Pre-registered gate (written before the run): S for c only if target score > max of (b) AND >= p95 of (a) AND known-answer
accuracy >= 0.8 with at least half the known-answer positions decisive and no class wrong-only majority. Else 36 stays M.
Usage: python3 body/ce36_dict.py [--seeds 20] [--minf 2] [--corpora es18,es17c]
"""
import argparse, csv, glob, gzip, os, random, re, sys, unicodedata
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(T))
ap = argparse.ArgumentParser(); ap.add_argument('--seeds', type=int, default=20); ap.add_argument('--minf', type=int, default=2)
ap.add_argument('--corpora', default='es18,es17c'); a = ap.parse_args()
SEG = ("no abyendo nobedad en estas partes que la de aber mudado este gouyerno con las zyrcunstanzyas que ay se sabran "
       "mexores pero con ansya las que ybyere del norte y de ytalya pues esauan de ocasyonar las que puedan ocuryr z para "
       "yas seguradad de la lorespondenzya se pondra solamente yn sobrescryto en esta")
def fold(w):
    w = unicodedata.normalize('NFD', w.lower()); w = ''.join(ch for ch in w if not unicodedata.combining(ch))
    w = w.replace('h', '')
    for x, y in (('y', 'i'), ('v', 'u'), ('b', 'u'), ('z', 'c'), ('j', 'x')): w = w.replace(x, y)
    return re.sub(r'(.)\1+', r'\1', w)
cnt = Counter()
for c in a.corpora.split(','):
    fs = sorted(glob.glob(os.path.join(ROOT, 'tools', 'data', c, '*.txt.gz')))
    for f in fs:
        for w in re.findall(r'[a-zA-ZáéíóúüñçÁÉÍÓÚÜÑÇ]+', gzip.open(f, 'rt', encoding='utf-8', errors='ignore').read()):
            cnt[fold(w)] += 1
    print('corpus %s: %d files' % (c, len(fs)))
LEX = {w for w, n in cnt.items() if n >= a.minf and len(w) >= 2}
print('word list: %d folded types at freq >= %d' % (len(LEX), a.minf))
BODY = ['L%02d' % i for i in range(1, 15)]
toks = [r for r in csv.DictReader(open(os.path.join(T, 'reading_tokens.tsv'), encoding='utf-8'), delimiter='\t')
        if r['line'] in BODY and r['value'] not in ('[?]', 'NULL')]
text = [r['value'] for r in toks]; assert ''.join(text) == SEG.replace(' ', ''), 'SEG does not match the body'
wid = []; k = 0
for wi, w in enumerate(SEG.split()):
    for _ in w: wid.append((wi, k)); k += 1
words = SEG.split(); starts = {}
for i, (wi, _) in enumerate(wid): starts.setdefault(wi, i)
def forms(i):
    wi = wid[i][0]; w = list(words[wi]); j = i - starts[wi]; out = {}
    for L in 'ce': w[j] = L; out[L] = ''.join(w)
    return out
def verdict(i):
    f = forms(i); ic, ie = fold(f['c']) in LEX, fold(f['e']) in LEX
    return f, ('c' if ic and not ie else 'e' if ie and not ic else 'both' if ic else 'neither')
pos36 = [i for i, r in enumerate(toks) if r['sign'] == '36']
tv = []
for i in pos36:
    f, v = verdict(i); tv.append(v)
    print('  %s pos%s  c:%s (%d)  e:%s (%d)  -> %s' % (toks[i]['line'], toks[i]['pos'], f['c'], cnt[fold(f['c'])], f['e'], cnt[fold(f['e'])], v))
TS = sum(v == 'c' for v in tv); print('TARGET: %d of %d occurrences c-only (e-only %d, both %d, neither %d)' % (TS, len(tv), tv.count('e'), tv.count('both'), tv.count('neither')))
sa = []
for sd in range(1, a.seeds + 1):
    rng = random.Random(sd); lab = [rng.choice('ce') for _ in pos36]; sa.append(sum(v == l for v, l in zip(tv, lab)))
sa_s = sorted(sa); p95 = sa_s[int(0.95 * (len(sa_s) - 1))]
print('CONTROL (a) label shuffle, %d seeds: score min %d max %d mean %.2f p95 %d; %d of %d at or above target' % (a.seeds, min(sa), max(sa), sum(sa) / len(sa), p95, sum(s >= TS for s in sa), a.seeds))
cand = [i for i, r in enumerate(toks) if r['grade'] == 'C' and r['sign'] != '36']; sb = []
for sd in range(1, a.seeds + 1):
    rng = random.Random(sd); sb.append(sum(verdict(i)[1] == 'c' for i in rng.sample(cand, len(pos36))))
print('CONTROL (b) position shuffle, %d seeds: c-only count min %d max %d mean %.2f; %d of %d at or above target' % (a.seeds, min(sb), max(sb), sum(sb) / len(sb), sum(s >= TS for s in sb), a.seeds))
ka = [i for i in cand if text[i] in 'ce']; res = {'c': Counter(), 'e': Counter()}
for i in ka:
    v = verdict(i)[1]; tr = text[i]; res[tr]['right' if v == tr else 'wrong' if v in 'ce' else v] += 1
R = sum(res[x]['right'] for x in 'ce'); W = sum(res[x]['wrong'] for x in 'ce'); N = len(ka); dec = R + W
acc = R / dec if dec else 0.0
print('CONTROL (c) known answer: %d positions, decisive %d, right %d wrong %d, accuracy %.3f; true c %s; true e %s'
      % (N, dec, R, W, acc, dict(res['c']), dict(res['e'])))
cls_ok = all(res[x]['wrong'] <= res[x]['right'] for x in 'ce')
ok = TS > max(sb) and TS >= p95 and acc >= 0.8 and dec >= N / 2 and cls_ok
print('VERDICT: %s' % ('clears all three controls -- licenses S for c' if ok else 'does not clear the pre-registered gate -- code 36 stays M'))
