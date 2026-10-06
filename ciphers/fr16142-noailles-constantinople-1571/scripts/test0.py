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
--stat lcs (R9-NOX, 6 Oct 2026, PREREG-R9NOX-LCS.md) swaps the statistic for the exact LCS ratio 2*LCS/(|a|+|b|) in the real
score and both nulls; difflib's ratio is greedy and swung 0.23 on a two-letter gloss change (R7A-NOX262). Default stays difflib.
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

def lcs_len(a, b):
    # bit-parallel exact LCS length (Allison-Dix / Hyyro)
    if not a or not b: return 0
    m = {}
    for i, c in enumerate(a): m[c] = m.get(c, 0) | (1 << i)
    full = (1 << len(a)) - 1; v = full
    for c in b:
        u = v & m.get(c, 0)
        v = ((v + u) | (v - u)) & full
    return len(a) - bin(v).count('1')

def ratio(a, b, stat):
    if stat == 'lcs': return 2 * lcs_len(a, b) / (len(a) + len(b)) if (a or b) else 1.0
    return difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()

def decode(toks, key):
    s = []
    for t in toks:
        if t.startswith('W:'): s.append(t[2:])
        elif t in key: s.append(key[t])
    return ''.join(s)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--check', action='store_true')
    ap.add_argument('--shuffles', type=int, default=200)
    ap.add_argument('--ct', default='ciphertext.tsv'); ap.add_argument('--gloss', default='gloss.tsv')
    ap.add_argument('--hash', choices=['e', 'o'], default='e', help="resolve an unsettled o1/e2 '#' glyph as e2 or o1")
    ap.add_argument('--stat', choices=['difflib', 'lcs'], default='difflib')
    ap.add_argument('--out', default='results.json'); a = ap.parse_args()
    ct = load(f'{D}/{a.ct}'); gl = load(f'{D}/{a.gloss}')
    # block comparison: the passes found 11 sloping lines where the margin gloss has 13, so lines are not paired 1:1
    lines = sorted(ct)
    def tok(t):
        t = t.rstrip('?')
        if t == 'o1/e2': t = 'e2' if a.hash == 'e' else 'o1'
        return t
    toks = {l: [tok(t) for t in ct[l].split()] for l in lines}
    ids = sorted({t for l in lines for t in toks[l] if re.fullmatch(r'[a-z]\d+', t)})
    key = {t: t[0] for t in ids}
    gold = norm(''.join(gl[l] for l in sorted(gl)))
    def score(k):
        return ratio(norm(''.join(decode(toks[l], k) for l in lines)), gold, a.stat)
    real = score(key)
    rng = random.Random(16142); vals = [key[t] for t in ids]; sh = []
    for _ in range(a.shuffles):
        v = vals[:]; rng.shuffle(v); sh.append(score(dict(zip(ids, v))))
    sh.sort()
    # second null: decode fixed, gloss word order shuffled (keeps the gloss's letter frequencies, destroys its sequence)
    dec = norm(''.join(decode(toks[l], key) for l in lines))
    words = ' '.join(gl[l] for l in sorted(gl)).split(); gsh = []
    for _ in range(a.shuffles):
        w = words[:]; rng.shuffle(w)
        gsh.append(ratio(dec, norm(''.join(w)), a.stat))
    gsh.sort()
    res = ({'stat': 'lcs'} if a.stat == 'lcs' else {}) | {'lines': len(lines), 'cipher_tokens': sum(len(toks[l]) for l in lines), 'letter_glyph_ids': len(ids),
           'gloss_letters': len(gold), 'real': round(real, 4), 'shuffle_mean': round(sum(sh)/len(sh), 4),
           'shuffle_p95': round(sh[int(0.95*len(sh))-1], 4), 'shuffle_max': round(sh[-1], 4),
           'rank': 1 + sum(s >= real for s in sh), 'of': len(sh) + 1,
           'gloss_order_null_mean': round(sum(gsh)/len(gsh), 4), 'gloss_order_null_p95': round(gsh[int(0.95*len(gsh))-1], 4),
           'gloss_order_null_max': round(gsh[-1], 4), 'gloss_order_rank': 1 + sum(s >= real for s in gsh),
           'decode': {l: decode(toks[l], key) for l in lines}}
    fn = f'{D}/{a.out}'
    if a.check:
        old = json.load(open(fn)); 
        if old != res: print('STALE'); sys.exit(1)
        print('OK'); return
    json.dump(res, open(fn, 'w'), indent=1, ensure_ascii=False)
    print(json.dumps({k: v for k, v in res.items() if k != 'decode'}))

main()
