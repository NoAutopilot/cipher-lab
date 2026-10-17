#!/usr/bin/env python3
"""LOPE-KEYAPP known-answer gate (PREREG-LOPE-KEYAPP.md): Bourdeau's clear-copy code values vs Kolosova 2024 cifra 7.
Usage: python3 gate.py [--check]   (writes gate.tsv; --check exits 1 if gate.tsv is stale)."""
import csv, random, sys, unicodedata, re, os, io
HERE = os.path.dirname(os.path.abspath(__file__))
K7 = os.path.join(HERE, '..', 'kolosova2024_cifra7.tsv')
MAP = {'z': '3', 'ɣ': 'y', 'ʃ': 's', 'ɡ': 'g', 'ᵹ': 'i'}

def tok(code):
    """Bourdeau group -> Kolosova notation, or None if not a code token (prefix + 1-3 Latin letters)."""
    s = ''.join(MAP.get(c, c) for c in code)
    return s if re.fullmatch(r'[3yxtsr][a-z]{1,3}', s) else None

def norm(w):
    w = re.sub(r'\(.*?\)', '', w).strip().lower().replace('ç', 'z').replace('j', 'g')
    w = ''.join(c for c in unicodedata.normalize('NFD', w) if unicodedata.category(c) != 'Mn')
    return {'sa': 'su santidad'}.get(w, w)

def load_k7():
    rows = [r for r in csv.reader(io.open(K7, encoding='utf-8'), delimiter='\t') if r and not r[0].startswith('#')][1:]
    return [(norm(r[0]), r[1].strip(), r[2].strip()) for r in rows]

# (Bourdeau group, his value, his grade, witness) -- from key_codes.tsv and read_r9649.md at HEAD 044576987
KA = [
 ('ton','que','confirmed','R9644'),('tab','nunca','confirmed','R9644'),('xud','hombre','confirmed','R9644'),
 ('xul','lo','confirmed','R9644'),('ɣm','fue','confirmed','R9644'),('xon','mas','confirmed','R9644'),
 ('tu','no','confirmed','R9644'),('top','por','confirmed','R9644'),('xu','hara','probable','R9644'),
 ('ɣmᵹ','arcobispo','probable','R9644'),('xett','gastar','probable','R9644'),('sub','si','confirmed','R9644'),
 ('ɣaf','es','confirmed','R9644'),('zun','da','confirmed','R9644'),('zar','de','confirmed','R9644'),
 ('ʃid','Sa (Su Santidad)','confirmed','R9644'),('ta','no','confirmed','R9644'),('xil','le (+s = les)','confirmed','R9644'),
 ('xur','na','confirmed','R9644'),('xuɡ','la','confirmed','R9644'),('tod','otro (+s = otros)','confirmed','R9644'),
 ('tad','obligado','probable','R9644'),('ʃuf','tanta','probable','R9644'),('ɣᵹb','duque','confirmed','R9644'),
 ('tel','pues','confirmed','R9644'),('ɣed','embaxador','probable','R9644'),
 ('ɣub','el','confirmed','R9648'),('taf','papa','confirmed','R9648'),('ɣof','esta','confirmed','R9648'),
 ('ɣuc','en','confirmed','R9648'),('ɣon','Francia','confirmed','R9648'),('zed','arçobispo','confirmed','R9648'),
 ('tef','paz','confirmed','R9648'),('ʃu','se','confirmed','R9648'),('zil','con','confirmed','R9648'),
 ('rab','vuestra magestad','confirmed','R9648'),
 ('zuf','cardenal','confirmed','R9649'),('yan','fortaleza','confirmed','R9649'),('tun','querria','confirmed','R9649'),
 ('ti','ni','probable','R9649'),
]

def score(k7, items):
    d = {}
    for w, c, _ in k7:
        d.setdefault(c, set()).add(w)
    out = []
    for g, v, gr, wit in items:
        k = tok(g)
        if k not in d:
            out.append((g, k, v, gr, wit, '', 'absent'))
        else:
            out.append((g, k, v, gr, wit, '/'.join(sorted(d[k])), 'agree' if norm(v) in d[k] else 'disagree'))
    return out

def counts(res):
    a = sum(r[6] == 'agree' for r in res); dz = sum(r[6] == 'disagree' for r in res)
    return a, dz, sum(r[6] == 'absent' for r in res)

def main():
    k7 = load_k7()
    assert all(tok(g) for g, *_ in KA), [g for g, *_ in KA if not tok(g)]
    lines = []
    for name, items in (('primary', KA), ('strict', [x for x in KA if x[3] != 'R9648'])):
        res = score(k7, items)
        a, dz, ab = counts(res)
        rng = random.Random(1522); words = [w for w, _, _ in k7]; null = []
        for _ in range(200):
            rng.shuffle(words)
            null.append(counts(score([(w, c, t) for w, (_, c, t) in zip(words, k7)], items))[0])
        null.sort(); p99 = null[int(0.99 * 200) - 1]; mean = sum(null) / 200
        ok = a / (a + dz) >= 0.80 and a > p99
        lines.append(f'# {name}: n={len(items)} agree={a} disagree={dz} absent={ab} share={a/(a+dz):.3f} '
                     f'shuffle_mean={mean:.2f} shuffle_p99={p99} shuffle_max={null[-1]} gate={"PASS" if ok else "FAIL"}')
        if name == 'primary':
            body = ['bourdeau\tkolosova_notation\tbourdeau_value\tbourdeau_grade\twitness\tkolosova_words\tverdict'] + \
                   ['\t'.join(r) for r in res]
    text = '\n'.join(lines + body) + '\n'
    fn = os.path.join(HERE, 'gate.tsv')
    if '--check' in sys.argv:
        sys.exit(0 if io.open(fn, encoding='utf-8').read() == text else 1)
    io.open(fn, 'w', encoding='utf-8').write(text)
    print('\n'.join(lines))

if __name__ == '__main__':
    main()
