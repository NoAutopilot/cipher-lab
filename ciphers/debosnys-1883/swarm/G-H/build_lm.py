"""Quadgram tables for the language screen, from corpora already in tools/data (sources in each dir's README/MANIFEST).
For each language writes lm/<lang>.sp.bin (27 symbols, a-z + space) and lm/<lang>.ns.bin (spaces removed):
float32 log P(d | a b c) for all 27^4 contexts, recursive Dirichlet backoff (beta 2), after folding (umlauts/accents -> base,
ß -> ss). Also lm/<lang>.held.txt: 20,000 held-out characters (last 5% of the corpus) for calibration."""
import gzip, os, re, struct, unicodedata, math, glob, sys
DATA = '../../../../tools/data'
LANGS = {'de': ['de19'], 'de16': ['de16'], 'en': ['en'], 'fr': ['fr19'], 'la': ['la18'], 'it': ['it16'], 'es': ['es17'],
         'pt': ['pt18'], 'nl': ['nl20'], 'da': ['da19'], 'pl': ['pl19'], 'lt': ['lt'], 'fr18': ['fr18']}
def read(p):
    op = gzip.open if p.endswith('.gz') else open
    with op(p, 'rt', encoding='utf-8', errors='ignore') as f: return f.read()
def fold(s):
    s = s.lower().replace('ß', 'ss').replace('æ', 'ae').replace('œ', 'oe').replace('ø', 'o').replace('ł', 'l')
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r'[^a-z]+', ' ', s)
    return re.sub(r' +', ' ', s)
def table(text, alpha, beta=2.0):
    """recursive Dirichlet backoff: P(d|abc) = (c(abcd) + beta*P(d|bc)) / (c(abc) + beta), down to a smoothed unigram"""
    idx = {c: i for i, c in enumerate(alpha)}; A = 27
    t = [idx[c] for c in text if c in idx]
    c1 = [0.0]*A; c2 = [0.0]*A**2; c3 = [0.0]*A**3; c4 = [0.0]*A**4
    for i in range(len(t)):
        d = t[i]; c1[d] += 1
        if i >= 1: c2[t[i-1]*A+d] += 1
        if i >= 2: c3[(t[i-2]*A+t[i-1])*A+d] += 1
        if i >= 3: c4[((t[i-3]*A+t[i-2])*A+t[i-1])*A+d] += 1
    tot = sum(c1); p1 = [(x + 0.5) / (tot + 0.5*A) for x in c1]
    def ctxsum(c, m): 
        s = [0.0]*(len(c)//A)
        for j, x in enumerate(c): s[j//A] += x
        return s
    s2, s3, s4 = ctxsum(c2, A), ctxsum(c3, A), ctxsum(c4, A)
    p2 = [(c2[j] + beta*p1[j % A]) / (s2[j//A] + beta) for j in range(A**2)]
    p3 = [(c3[j] + beta*p2[j % A**2]) / (s3[j//A] + beta) for j in range(A**3)]
    return [math.log((c4[j] + beta*p3[j % A**3]) / (s4[j//A] + beta)) for j in range(A**4)]
os.makedirs('lm', exist_ok=True)
alpha_sp = 'abcdefghijklmnopqrstuvwxyz '
for lang, dirs in LANGS.items():
    if len(sys.argv) > 1 and lang not in sys.argv[1:]: continue
    files = []
    for d in dirs: files += sorted(glob.glob(f'{DATA}/{d}/*.txt*'))
    files = [f for f in files if 'LICENSE' not in f and 'README' not in f]
    text = fold(' '.join(read(f) for f in files))
    text = text[:3_000_000] if len(text) > 3_000_000 else text
    cut = int(len(text) * 0.95)
    train, held = text[:cut], text[cut:cut + 20000]
    open(f'lm/{lang}.held.txt', 'w').write(held)
    for tag, tx in (('sp', train), ('ns', train.replace(' ', ''))):
        tb = table(tx, alpha_sp)
        with open(f'lm/{lang}.{tag}.bin', 'wb') as f: f.write(struct.pack(f'{len(tb)}f', *tb))
    print(lang, len(files), 'files', len(train), 'chars')
