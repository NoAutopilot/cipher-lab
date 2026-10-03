#!/usr/bin/env python3
"""GAPS27-riksarkivet-r4282-1628 (3 Oct 2026): does the letter table of DECODE key record 4275 (Chifferklaver II:108,
heading read "Zu Meynz gefundene feindl. Ziffern Ao 1634 in Julio", cover "Mainz 1634 ... Hofmeister ... Aschaffenburg";
all reading M) fit R4282 on the signs the two share?  The table (IMG_R4275_I25666_P, read by eye at 200 dpi, grade M)
gives each plain letter one graphic sign and one 2-digit number.  STRICT: the four key signs whose shape matches an
R4282 sign class in Bourdeau's notation without doubt.  WIDE: STRICT plus three ambiguous pairings (R4282 L=lambda vs
the key's c-sign, an inverted V; R4282 E=epsilon vs the key's r-sign, a reversed epsilon; R4282 u vs the key's
e-sign, a U/upsilon shape).  Same statistic and controls as key4327_overlap.py (rule 3): mean la18 Latin unigram
log-probability of the letters the key gives R4282's tokens of those signs, vs (a) the same values permuted among the
signs and (b) distinct random Latin letters, 2000 draws each.  --check re-derives and compares with the committed
key4275_overlap.json."""
import collections, json, random, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from key4327_overlap import latin_unigrams, tokens, score, HERE
STRICT = {'T': 'u', 'B': 'h', '8': 'y', 'o': 'd'}   # key v-sign is a Delta; v -> u in la18's alphabet
WIDE = dict(STRICT, L='c', E='r', u='e')

def test(key, seed):
    lp = latin_unigrams(); toks = tokens(); rng = random.Random(seed)
    real = score(key, toks, lp)
    signs, vals = list(key), list(key.values())
    perm, rand = [], []
    for _ in range(2000):
        rng.shuffle(vals); perm.append(score(dict(zip(signs, vals)), toks, lp))
        rand.append(score(dict(zip(signs, rng.sample(sorted(lp), len(signs)))), toks, lp))
    pct = lambda xs: round(sum(x >= real for x in xs) / len(xs), 4)
    p95 = lambda xs: round(sorted(xs)[int(0.95 * len(xs))], 4)
    return {'tokens': len(toks), 'covered': sum(t in key for t in toks), 'signs': len(key),
            'real_mean_logp': round(real, 4),
            'perm_mean': round(sum(perm) / len(perm), 4), 'perm_p95': p95(perm), 'perm_frac_ge_real': pct(perm),
            'rand_mean': round(sum(rand) / len(rand), 4), 'rand_p95': p95(rand), 'rand_frac_ge_real': pct(rand),
            'mapped_letter_counts': dict(collections.Counter(key[t] for t in toks if t in key))}

def run():
    return {'strict': test(STRICT, 4275), 'wide': test(WIDE, 42751)}

if __name__ == '__main__':
    out = run(); j = HERE / 'key4275_overlap.json'
    if '--check' in sys.argv:
        ok = json.loads(j.read_text()) == out; print('OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    j.write_text(json.dumps(out, indent=1) + '\n'); print(json.dumps(out, indent=1))
