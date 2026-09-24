#!/usr/bin/env python3
"""Period French character n-gram model (Witten-Bell interpolated) and word list, for scoring cipher readings.

Corpus: tools/data/fr16/*_djvu.txt(.gz) -- Internet Archive OCR of 16th-century French letters (see
tools/data/fr16/MANIFEST.tsv). Folding matches the cipher tables: upper case, accents stripped, J->I, U->V,
W->VV, K kept, everything that is not a letter dropped. Words are kept separately for a segmentation bonus.

  from french16_ngram import load
  m = load()                      # cached in tools/data/fr16/model_o5.pkl.gz after the first build
  m.logp('ILESTIMPOSSIBLE')       # log2 probability of a continuous letter string (no BOS context)
  m.words                         # Counter of folded words
  m.bits_per_char                 # mean -log2 p per char on a held-out 5% of the corpus
"""
import os, re, gzip, glob, math, pickle, unicodedata, collections, random
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'fr16')
ORDER = 5

def fold(s):
    s = unicodedata.normalize('NFD', s)
    s = ''.join(ch for ch in s if unicodedata.category(ch) != 'Mn').upper()
    s = s.replace('J', 'I').replace('U', 'V').replace('W', 'VV').replace('Œ', 'OE').replace('Æ', 'AE')
    return s

def corpus_words():
    for fn in sorted(glob.glob(os.path.join(D, '*_djvu.txt*'))):
        op = gzip.open if fn.endswith('.gz') else open
        with op(fn, 'rt', encoding='utf-8', errors='replace') as f:
            txt = f.read()
        txt = re.sub(r'-\s*\n\s*', '', txt)          # rejoin hyphenated line ends
        for w in re.findall(r"[^\W\d_]+", txt):
            w = fold(w)
            w = re.sub('[^A-Z]', '', w)
            if w: yield w

class Model:
    def __init__(self, words, order=ORDER):
        self.order = order
        self.words = collections.Counter(words)
        text = ''.join(words)
        cut = int(len(text) * 0.95)
        train, self._held = text[:cut], text[cut:cut + 200000]
        self.alpha = sorted(set(train))
        cnt = [collections.defaultdict(collections.Counter) for _ in range(order)]
        for k in range(order):              # k = context length
            for i in range(k, len(train)):
                cnt[k][train[i - k:i]][train[i]] += 1
        self.c = [{h: (dict(v), sum(v.values()), len(v)) for h, v in ck.items()} for ck in cnt]
        self.bits_per_char = -self.logp(self._held) / len(self._held)
    def p(self, h, ch):
        pr = 1.0 / (len(self.alpha) + 1)
        for k in range(0, min(len(h), self.order - 1) + 1):
            e = self.c[k].get(h[len(h) - k:] if k else '')
            if not e: break
            d, n, t = e
            pr = (d.get(ch, 0) + t * pr) / (n + t)
        return pr
    def logp(self, s):
        return sum(math.log2(self.p(s[max(0, i - self.order + 1):i], s[i])) for i in range(len(s)))

def load(rebuild=False):
    fn = os.path.join(D, f'model_o{ORDER}.pkl.gz')
    if os.path.exists(fn) and not rebuild:
        with gzip.open(fn, 'rb') as f: return pickle.load(f)
    m = Model(list(corpus_words()))
    with gzip.open(fn, 'wb') as f: pickle.dump(m, f)
    return m

if __name__ == '__main__':
    import french16_ngram; m = french16_ngram.load(rebuild=True)
    print(f'words {sum(m.words.values())}, distinct {len(m.words)}, alphabet {"".join(m.alpha)}, '
          f'held-out {m.bits_per_char:.3f} bits/char')
    for s in ('ILESTIMPOSSIBLE', 'ILEXTIMPOSSIBLE', 'VOVSSAVRIEZ', 'SERVICE', 'SQRVICE'):
        print(s, round(m.logp(s), 1))
