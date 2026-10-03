#!/usr/bin/env python3
"""GAPS3-riksarkivet-r4282-1628 (3 Oct 2026): does the letter table on DECODE key record 4307's fourth page
(IMG_R4307_I25838_P, Chifferklaver II:134, "Dis verkehrte Alphabet kann auch nach aller notdurft gebraucht werden",
Hartmann Drach catalogue) fit R4282 on the signs the two share?  The table gives each plain letter one cipher
letter-shape; read by eye at 200 dpi, grade M throughout (German hand, row alignment itself M).  Only cipher shapes
with a single plain value in that read and present in R4282 are used.  Same statistic and controls as
key4327_overlap.py (rule 3): mean la18 Latin unigram log-probability of the letters the key gives R4282's tokens of
those signs, vs (a) the same values permuted among the signs and (b) distinct random Latin letters, 2000 draws each.
--check re-derives and compares with the committed key4307p4_overlap.json."""
import collections, json, random, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from key4327_overlap import latin_unigrams, tokens, score, HERE
# R4282 sign (Bourdeau notation) -> key-4307 p.4 plain letter (all M)
KEY = {'q': 'a', 'e': 'b', 'x': 'd', 'c': 'f', 'A': 'f', 'f': 'g', 'g': 'i', 'h': 'm', 'i': 'n', 'r': 'o',
       'k': 'p', 't': 'q', 'u': 'r', '3': 's', 'n': 'x', 'D': 'z'}

def run():
    lp = latin_unigrams(); toks = tokens(); rng = random.Random(4307)
    real = score(KEY, toks, lp)
    signs, vals = list(KEY), list(KEY.values())
    perm, rand = [], []
    for _ in range(2000):
        rng.shuffle(vals); perm.append(score(dict(zip(signs, vals)), toks, lp))
        rand.append(score(dict(zip(signs, rng.sample(sorted(lp), len(signs)))), toks, lp))
    cov = sum(t in KEY for t in toks)
    pct = lambda xs: round(sum(x >= real for x in xs) / len(xs), 4)
    p95 = lambda xs: round(sorted(xs)[int(0.95 * len(xs))], 4)
    return {'tokens': len(toks), 'covered': cov, 'signs': len(KEY), 'real_mean_logp': round(real, 4),
            'perm_mean': round(sum(perm) / len(perm), 4), 'perm_p95': p95(perm), 'perm_frac_ge_real': pct(perm),
            'rand_mean': round(sum(rand) / len(rand), 4), 'rand_p95': p95(rand), 'rand_frac_ge_real': pct(rand),
            'mapped_letter_counts': dict(collections.Counter(KEY[t] for t in toks if t in KEY))}

if __name__ == '__main__':
    out = run(); j = HERE / 'key4307p4_overlap.json'
    if '--check' in sys.argv:
        ok = json.loads(j.read_text()) == out; print('OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    j.write_text(json.dumps(out, indent=1) + '\n'); print(json.dumps(out, indent=1))
