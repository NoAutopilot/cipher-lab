#!/usr/bin/env python3
"""GAPS-riksarkivet-r4282-1628 (3 Oct 2026): does DECODE key record 4327 (Chifferklaver II:154, Oxenstierna-Sadler,
1620s) fit R4282 on the signs the two share?  Key 4327 gives each letter a-z two 2-digit numbers and one sign; seven
of those signs (read by eye, grade M, from IMG_R4327_I25950_P at 300 dpi) also occur in Bourdeau's R4282 transcription.
Statistic: mean Latin unigram log-probability (la18 corpus) of the letters the real key assigns to R4282's tokens of
those signs.  Controls (rule 3, both can vary on this statistic): (a) the same seven letters permuted among the seven
signs; (b) seven distinct letters drawn at random from the Latin alphabet.  --check re-derives and compares
with the committed key4327_overlap.json."""
import collections, gzip, json, math, random, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
REPO = HERE.parent.parent
KEY = {'E': 'a', 'L': 'd', 'x': 'h', 'A': 'k', 'M': 'l', 'T': 'm', 'o': 'y'}  # R4282 sign -> key-4327 letter (M)

def latin_unigrams():
    c = collections.Counter()
    for f in sorted((REPO / 'tools/data/la18').glob('*.txt.gz')):
        for ch in gzip.open(f, 'rt', errors='ignore').read().lower():
            if 'a' <= ch <= 'z':
                c[ch.replace('j', 'i').replace('v', 'u')] += 1
    tot = sum(c.values())
    alpha = 'abcdefghiklmnopqrstuxyz'
    return {a: math.log((c[a] + 1) / (tot + 26)) for a in alpha}

def tokens():
    t = (HERE / 'r4282_transcription_bourdeau.txt').read_text()
    s = ' '.join(l for l in t.splitlines() if not l.startswith('#'))
    s = re.sub(r'\[[^\]]*\]', ' ', s)
    return [ch for ch in s if not ch.isspace()]

def score(key, toks, lp):
    v = [lp[key[t]] for t in toks if t in key]
    return sum(v) / len(v)

def run():
    lp = latin_unigrams(); toks = tokens(); rng = random.Random(4327)
    real = score(KEY, toks, lp)
    signs, vals = list(KEY), list(KEY.values())
    perm, rand = [], []
    for _ in range(2000):
        rng.shuffle(vals); perm.append(score(dict(zip(signs, vals)), toks, lp))
        rand.append(score(dict(zip(signs, rng.sample(sorted(lp), len(signs)))), toks, lp))
    cov = sum(t in KEY for t in toks)
    pct = lambda xs: round(sum(x >= real for x in xs) / len(xs), 4)
    p95 = lambda xs: round(sorted(xs)[int(0.95 * len(xs))], 4)
    return {'tokens': len(toks), 'covered': cov, 'real_mean_logp': round(real, 4),
            'perm_mean': round(sum(perm) / len(perm), 4), 'perm_p95': p95(perm), 'perm_frac_ge_real': pct(perm),
            'rand_mean': round(sum(rand) / len(rand), 4), 'rand_p95': p95(rand), 'rand_frac_ge_real': pct(rand),
            'mapped_letter_counts': dict(collections.Counter(KEY[t] for t in toks if t in KEY))}

if __name__ == '__main__':
    out = run(); j = HERE / 'key4327_overlap.json'
    if '--check' in sys.argv:
        ok = json.loads(j.read_text()) == out; print('OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    j.write_text(json.dumps(out, indent=1) + '\n'); print(json.dumps(out, indent=1))
