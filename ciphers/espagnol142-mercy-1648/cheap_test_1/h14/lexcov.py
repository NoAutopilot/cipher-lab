#!/usr/bin/env python3
"""Campaign step H14 (28 Sept 2026): lexicon coverage as an instrument independent of the n-gram judge.
Coverage = share of word tokens found in the Cartas vocabulary (tools/data/es17c7, words with >= MINC occurrences).
  reading: the cipher words of reading.txt (upper-case stretches; '_' = boxed 101, skipped) segmented as written.
  controls: the H1 exact-profile control decodes (cheap_test_1/exactprof_k38_oos_cartas13_seed*.json, Cartas t.13
  windows, and exactprof_k38_seed*.json, Don Quijote windows) segmented at their TRUE word boundaries (regenerated
  from the raw text); the 5%/10% corrupted decodes (noisy/); 20 letter shuffles of the reading re-segmented at the
  same word lengths (order destroyed, lengths kept); the letter's own clear words (m2/clear_words_only.txt).
  python3 ciphers/espagnol142-mercy-1648/cheap_test_1/h14/lexcov.py
"""
import glob, gzip, json, os, random, re, sys, unicodedata
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(H, '..', '..'); R = os.path.join(T, '..', '..')
sys.path.insert(0, os.path.join(R, 'tools')); import homophonic_anneal as ha
S = '/tmp/claude-0/-home-user-cipher-lab/47290f4d-8269-54b1-b458-60a79602e50f/scratchpad'
MINC = 3
def words_of(text): return [w for w in (ha.fold(x) for x in text.split()) if w]
vocab = Counter()
for f in sorted(glob.glob(os.path.join(R, 'tools/data/es17c7/*.txt.gz'))):
    vocab.update(words_of(gzip.open(f, 'rt', encoding='utf-8').read()))
V = {w for w, c in vocab.items() if c >= MINC}
print(f'vocabulary: {len(V)} words with >= {MINC} occurrences ({sum(vocab.values())} tokens)')
def cov(words, label):
    ws = [w for w in words if w and w != '_']
    hit = sum(1 for w in ws if w in V); lh = sum(len(w) for w in ws if w in V); L = sum(len(w) for w in ws)
    print(f'  {label}: words {len(ws)}, in-vocab {hit} ({hit/len(ws):.1%}), letter-weighted {lh/L:.1%}')
    return hit / len(ws)
# reading
rd = open(os.path.join(T, 'reading.txt'), encoding='utf-8').read()
cipher_words = [ha.fold(w) for w in re.findall(r'\b[A-Z_]{1,}\b', rd) if w.strip('_')]
lens = [len(w) for w in cipher_words]
print('== reading'); r_cov = cov(cipher_words, 'reading.txt cipher words')
clear = words_of(open(os.path.join(T, 'm2/clear_words_only.txt'), encoding='utf-8').read())
cov(clear, 'the letter\'s own clear words (m2/clear_words_only.txt)')
# shuffles
letters = list(''.join(cipher_words)); rng = random.Random(1); sh = []
for s in range(20):
    rng.shuffle(letters); i = 0; ws = []
    for n in lens: ws.append(''.join(letters[i:i + n])); i += n
    ws_ = [w for w in ws if w]; sh.append(sum(1 for w in ws_ if w in V) / len(ws_))
print(f'== 20 shuffles of the reading letters at the same word lengths: mean {sum(sh)/len(sh):.1%}, max {max(sh):.1%}')
# controls: true word boundaries of a window = cumulative folded word lengths of the raw text
def window_words(raw, start, N, dec):
    ws = words_of(raw); bounds = []; pos = 0
    for w in ws:
        bounds.append((pos, pos + len(w))); pos += len(w)
    out = []
    for a, b in bounds:
        if b <= start or a >= start + N: continue
        out.append(dec[max(a, start) - start:min(b, start + N) - start])
    return out
raws = {'cartas13': open(S + '/memorialhistri13realuoft.txt', encoding='utf-8').read(), 'dq': open(S + '/donquijote.txt', encoding='utf-8').read()}
print('== exact-profile control decodes at their true word boundaries')
for tag, pat in (('cartas13', 'exactprof_k38_oos_cartas13_seed?.json'), ('dq', 'exactprof_k38_seed?.json')):
    for f in sorted(glob.glob(os.path.join(T, 'cheap_test_1', pat))):
        o = json.load(open(f)); ws = window_words(raws[tag], o['window_start'], o['N'], o['decoded'])
        cov(ws, f'{os.path.basename(f)} (share {o["share"]})')
        cov(window_words(raws[tag], o['window_start'], o['N'], o['plain']), '   its true plaintext') if f.endswith('seed1.json') else None
print('== corrupted controls (5%, 10%)')
for f in sorted(glob.glob(os.path.join(T, 'cheap_test_1/noisy/*.json'))):
    o = json.load(open(f)); tag = 'cartas13' if 'cartas13' in f else 'dq'
    seed = int(re.search(r'seed(\d)', f).group(1)); prof = ha.load_profile(os.path.join(T, 'cipher_codes.tsv'), {'NONE'})
    _seq, p, _truth, start = ha.make_profile_control(raws[tag], prof, seed)
    ws = window_words(raws[tag], start, len(p), o['decoded']); ok = sum(1 for a, b in zip(o['decoded'], p) if a == b) / len(p)
    cov(ws, f'{os.path.basename(f)} (letters right {ok:.1%})')
