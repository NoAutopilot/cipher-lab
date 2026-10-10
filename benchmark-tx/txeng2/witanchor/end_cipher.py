#!/usr/bin/env python3
"""END-CIPHER (PREREG-txeng2-21; TX-RED pass 14 F69): the cipher side of the f.103r end anchor, read-free.

WIT-GROEN showed the clerk text's last ~520 letters are the dispatch's closing passage (Groen IV pp.90*-91*, another manuscript copy).
Untested there: that f.103r's LAST cipher lines encode that passage. Here the folder's committed reading of f.103r L36-L37
(ciphers/fr16104-vivonne-spain-1572/tx/f103r_rec.tsv -- the folder's own reading, never the truth) is decoded with the published key's
C-grade rows (build_vivonne_confirm2.rd_key's `force`; unkeyed tokens and marks skipped) into a letter string, then aligned by
wit_anchor's routine (SequenceMatcher ratio, best window, step 10 then 1) to (a) Groen's normalised passage and (b) dec_norm's last
800 letters; selection-fair null = 200 letter-shuffled copies of the decoded string, each at its own best window over the same target.
Gate (declared in PREREG-21): ANCHORED if the best window in Groen's passage lies in its last 200 letters AND ratio - null max >= 0.03.
Reads tx/f103r_rec.tsv, key.tsv, key_tomokiyo.tsv, dec_norm.txt and the on-disk OCR. No truth file, no output file, no crop.
Run from the repo root: python3 benchmark-tx/txeng2/witanchor/end_cipher.py
"""
import difflib, gzip, json, os, random, re, sys, unicodedata
ROOT = os.getcwd()
sys.path.insert(0, os.path.join(ROOT, 'benchmark-tx'))
sys.argv = [sys.argv[0]]  # keep the build module's own argv parsing quiet
import build_vivonne_confirm2 as bv  # noqa: E402  (imports only; build() is never called)
HERE = os.path.dirname(os.path.abspath(__file__))

def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if c.isascii() and c.isalpha())
    return s.translate(str.maketrans('vjyk', 'uiic'))

# Groen passage exactly as wit_groen.py
ocr = gzip.open('sources/ia-fulltext/print-check/archivesoucorre03housgoog_djvu.txt.gz', 'rt', encoding='utf-8', errors='replace').read()
m1 = re.search(r"L.Empereur\s+fait\s+asseur", ocr); assert m1
m2 = re.search(r"rem[ée]dier\s+ses\s+af\S*aires", ocr[m1.start():]); assert m2
groen = norm(ocr[m1.start():m1.start() + m2.end()])
dec = norm(open('ciphers/fr16104-vivonne-spain-1572/tx/dec_norm.txt', encoding='utf-8').read())
dec_tail = dec[-800:]

pub, force, grade = bv.rd_key()
lines = dict(bv.raw_tokens(os.path.join(bv.TX, 'f103r_rec.tsv')))
LINES = ['L36', 'L37']
toks = [t for L in LINES for t in lines[L]]
decoded = ''.join(force[t] for t in toks if t in force)
decoded = norm(decoded)
n_keyed = sum(1 for t in toks if t in force)

def best(seq, tgt, step=10):
    L = len(seq); br, bo = -1.0, 0
    rng_ = range(0, max(1, len(tgt) - L + 1), step)
    for o in rng_:
        r = difflib.SequenceMatcher(None, seq, tgt[o:o + L], autojunk=False).ratio()
        if r > br: br, bo = r, o
    for o in range(max(0, bo - step), min(len(tgt) - L, bo + step) + 1):
        r = difflib.SequenceMatcher(None, seq, tgt[o:o + L], autojunk=False).ratio()
        if r > br: br, bo = r, o
    return br, bo

def run(tgt, name, n_null=200):
    r, o = best(decoded, tgt)
    rng = random.Random(20261010)
    nulls = []
    s = list(decoded)
    for _ in range(n_null):
        rng.shuffle(s)
        nulls.append(best(''.join(s), tgt)[0])
    nulls.sort()
    return dict(target=name, target_len=len(tgt), ratio=round(r, 4), offset=o, end=o + len(decoded),
                end_gap_to_target_end=len(tgt) - (o + len(decoded)), null_max=round(nulls[-1], 4),
                null_p95=round(nulls[int(0.95 * n_null) - 1], 4), margin_vs_max=round(r - nulls[-1], 4), null_n=n_null)

res = dict(lines=LINES, tokens=len(toks), keyed_tokens=n_keyed, decoded_letters=len(decoded), decoded_head=decoded[:40],
           groen_letters=len(groen), results=[run(groen, 'groen_passage'), run(dec_tail, 'dec_norm_last_800')])
g = res['results'][0]
res['verdict'] = 'ANCHORED' if (g['end_gap_to_target_end'] <= 200 and g['margin_vs_max'] >= 0.03) else 'NOT ANCHORED'
json.dump(res, open(os.path.join(HERE, 'result_end.json'), 'w'), indent=1)
for k in ('lines', 'tokens', 'keyed_tokens', 'decoded_letters', 'groen_letters', 'verdict'):
    print(k, res[k])
for r in res['results']:
    print(r)
