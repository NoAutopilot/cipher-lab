"""Build the Copiale known-answer token file from two public line datasets.
cipher: learnable-typewriter/copiale annotation.json (HF), keys 'NN_k.png' / 'NNB_k.png'
plain : leitro/Decipher-from-Pixels-Copiale copiale_gt/*.gt (MIT), keys 'page-line'
page map (checked by decoding): NN -> page 2NN-2, NNB -> 2NN-1, line k -> k+1.
Gold per token = the published key (Knight, Megyesi & Schaefer 2011, Fig. 6) applied to the transcription.
Writes data/copiale_tokens.tsv (page line pos token gold) and prints key-decode vs leitro agreement."""
import json, re, difflib, sys
from copiale_key import KEY, SPACE, LOGO, decode
d = json.load(open('data/copiale_cipher_lines_learnable-typewriter.json'))
gt = {}
for f in ['train', 'valid', 'test']:
    for l in open(f'data/{f}.gt', encoding='utf-8'):
        k, v = l.rstrip('\n').split('\t', 1); gt[k] = v
def pid(k):
    m = re.match(r'(\d+)(B?)_(\d+)\.png$', k)
    if not m: return None
    n, b, li = int(m.group(1)), m.group(2), int(m.group(3))
    return (2*n - 2 + (1 if b else 0), li + 1)
rows = []; agree = []; 
for k, v in d.items():
    p = pid(k)
    if not p: continue
    toks = v['label'].split()
    rows.append((p, toks))
rows.sort()
def norm(s):
    s = s.lower().replace('ä','a').replace('ö','o').replace('ü','u').replace('ß','ss')
    s = re.sub(r'\*[^*]*\*', ' ', s)
    return re.sub(r'[^a-z]+', '', s)
out = open('data/copiale_tokens.tsv', 'w')
out.write('page\tline\tpos\ttoken\tgold\n')
for (pg, li), toks in rows:
    prev = ''
    for i, t in enumerate(toks):
        if t in SPACE: g = '_'
        elif t in LOGO: g = '#'
        elif t == ':': g = prev[-1:] or '?'
        else: g = KEY.get(t, '?')
        if g not in ('_', '#', '?'): prev = g
        g = g.replace('ä','a').replace('ö','o').replace('ü','u')
        out.write(f'{pg}\t{li}\t{i}\t{t}\t{g}\n')
    ref = gt.get(f'{pg}-{li}')
    if ref is not None:
        a, b = norm(decode(toks)), norm(ref)
        agree.append(difflib.SequenceMatcher(None, a, b, autojunk=False).ratio())
out.close()
print('lines', len(rows), 'with plaintext', len(agree), 'mean key-decode/plaintext letter similarity %.3f' % (sum(agree)/len(agree)))
print('lines >=0.9:', sum(a >= 0.9 for a in agree), ' <0.7:', sum(a < 0.7 for a in agree))
