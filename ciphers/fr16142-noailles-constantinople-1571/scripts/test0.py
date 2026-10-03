#!/usr/bin/env python3
"""Test 0 (FT-D, 3 Oct 2026): Tomokiyo's published key against a glossed leaf.

Input: ciphertext.tsv (line, tokens) where each token is a glyph id in Tomokiyo's table terms:
  <letter><n>  the n-th homophone of that letter in his column (a1, a2, e3 ...);  N<k> a null;  D<k> a doubler;
  W:<word> a nomenclator code read as its table word;  ? an unread sign.
and gloss.tsv (line, text): the period marginal/interlinear decipherment of the same lines, as transcribed.
Decoding is the letter part of each id (the key is what makes 'e3' mean e). The statistic is the
letter-level similarity (difflib ratio, letters only, lower case, u=v, i=j) between the decode and the gloss.
Null: 200 keys made by permuting the letter values among the letter glyph ids (seeded) -- the shuffle changes
which letter each glyph yields, so it can change the statistic (rule 3 orthogonality check).
Prints real, shuffle mean, p95, max, rank, N. --check exits non-zero if results.json is stale.
"""
import sys, json, random, re, difflib, argparse, os
D = os.path.dirname(os.path.abspath(__file__)) + '/..'

def norm(s):
    s = s.lower().replace('v', 'u').replace('j', 'i').replace('y', 'i')
    s = re.sub(r'[éèêë]', 'e', s)
    return re.sub(r'[^a-z]', '', s)

def load(fn):
    out = {}
    for ln in open(fn):
        if ln.startswith('#') or not ln.strip(): continue
        parts = ln.rstrip('\n').split('\t')
        out[parts[0]] = parts[1] if len(parts) > 1 else ''
    return out

def decode(toks, key):
    s = []
    for t in toks:
        if t.startswith('W:'): s.append(t[2:])
        elif t in key: s.append(key[t])
    return ''.join(s)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--check', action='store_true')
    ap.add_argument('--shuffles', type=int, default=200); a = ap.parse_args()
    ct = load(f'{D}/ciphertext.tsv'); gl = load(f'{D}/gloss.tsv')
    lines = [l for l in ct if l in gl and gl[l].strip()]
    toks = {l: ct[l].split() for l in lines}
    ids = sorted({t for l in lines for t in toks[l] if re.fullmatch(r'[a-z]\d+', t)})
    key = {t: t[0] for t in ids}
    gold = norm(''.join(gl[l] for l in lines))
    def score(k):
        return difflib.SequenceMatcher(None, norm(''.join(decode(toks[l], k) for l in lines)), gold, autojunk=False).ratio()
    real = score(key)
    rng = random.Random(16142); vals = [key[t] for t in ids]; sh = []
    for _ in range(a.shuffles):
        v = vals[:]; rng.shuffle(v); sh.append(score(dict(zip(ids, v))))
    sh.sort()
    res = {'lines': len(lines), 'cipher_tokens': sum(len(toks[l]) for l in lines), 'letter_glyph_ids': len(ids),
           'gloss_letters': len(gold), 'real': round(real, 4), 'shuffle_mean': round(sum(sh)/len(sh), 4),
           'shuffle_p95': round(sh[int(0.95*len(sh))-1], 4), 'shuffle_max': round(sh[-1], 4),
           'rank': 1 + sum(s >= real for s in sh), 'of': len(sh) + 1,
           'decode': {l: decode(toks[l], key) for l in lines}}
    fn = f'{D}/results.json'
    if a.check:
        old = json.load(open(fn)); 
        if old != res: print('STALE'); sys.exit(1)
        print('OK'); return
    json.dump(res, open(fn, 'w'), indent=1, ensure_ascii=False)
    print(json.dumps({k: v for k, v in res.items() if k != 'decode'}))

main()
