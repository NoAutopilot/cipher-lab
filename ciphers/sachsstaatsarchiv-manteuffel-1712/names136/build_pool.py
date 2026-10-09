#!/usr/bin/env python3
"""MANT-NAMES136 (9 Oct 2026): build the candidate lists BEFORE scoring, and the crib_list_fit.py inputs.
Lists (first column = folded lowercase form):
  pool_names.tsv  capitalised words from on-disk sources only: the folder's key.tsv (values + notes = Krauske's table
                  names), frame_inventory.tsv, mant0609/seen_before.tsv, HYPOTHESES.md, AUDIT.md (edition quotes:
                  Heinsius XIV, Acta Borussica), and the era corpus tools/data/fr18 (Torcy and others; capitalised
                  words seen >= 2 times). Every word, attested spelling only.
  pool_names_var.tsv  pool_names plus ONE uniform period-orthography variant rule applied to every word alike
                  (umlaut dropped already by folding; ff->f, f->v, ff->v, w->v, k->c, c->k, tz->z, th->t, y->i, oe->o).
                  DISCLOSED: the f->v variant was chosen after the target decode 'lolhovel' was seen (MANT-0136, 04:17).
  pool_fr.tsv     every lowercase 1-3 word n-gram (spaces removed) of length 7-11 letters seen >= 2 times in fr18,
                  for r09 (a phrase window, not necessarily a name).
Inputs for the tool: codes.tsv (line, position, sign: 0136 + 0103 + f468 g13), key_cl.tsv (code, letter, grade: a
key.tsv value that is one letter keeps it, anything else '_').
  python3 ciphers/sachsstaatsarchiv-manteuffel-1712/names136/build_pool.py [--check]
"""
import csv, glob, gzip, hashlib, os, re, sys, unicodedata
from collections import Counter
D = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(D); ROOT = os.path.dirname(os.path.dirname(T))

def fold(w):
    w = unicodedata.normalize('NFKD', w.lower()); w = ''.join(c for c in w if not unicodedata.combining(c))
    return re.sub('[^a-z]', '', w.replace('ß', 'ss'))

CAP = re.compile(r"\b([A-ZÄÖÜÉ][a-zäöüéèêàâôûç]{2,13})\b")
def names():
    c = Counter()
    for f in ['key.tsv', 'frame_inventory.tsv', 'mant0609/seen_before.tsv', 'HYPOTHESES.md', 'AUDIT.md']:
        for m in CAP.findall(open(os.path.join(T, f), encoding='utf-8', errors='replace').read()):
            c[fold(m)] += 2
    for f in sorted(glob.glob(os.path.join(ROOT, 'tools/data/fr18/*.txt.gz'))):
        for m in CAP.findall(gzip.open(f, 'rt', encoding='utf-8', errors='replace').read()):
            c[fold(m)] += 1
    return sorted(w for w, n in c.items() if n >= 2 and 3 <= len(w) <= 14)

RULES = [('ff', 'f'), ('f', 'v'), ('ff', 'v'), ('w', 'v'), ('k', 'c'), ('c', 'k'), ('tz', 'z'), ('th', 't'), ('y', 'i'), ('oe', 'o')]
def variants(w):
    out = {w}
    for a, b in RULES:
        out |= {x.replace(a, b) for x in list(out)}
    return out

def phrases():
    c = Counter()
    for f in sorted(glob.glob(os.path.join(ROOT, 'tools/data/fr18/*.txt.gz'))):
        ws = [fold(x) for x in gzip.open(f, 'rt', encoding='utf-8', errors='replace').read().split()]
        ws = [x for x in ws if x]
        for n in (1, 2, 3):
            for i in range(len(ws) - n + 1):
                p = ''.join(ws[i:i + n])
                if 7 <= len(p) <= 11: c[p] += 1
    return sorted(p for p, n in c.items() if n >= 2)

def codes():
    rows = []
    for f in ['f0136_09/ciphertext.tsv', 'f0103_09/ciphertext.tsv']:
        for r in csv.DictReader((l for l in open(os.path.join(T, f)) if not l.startswith('#')), delimiter='\t'):
            rows.append((r['line'], r['pos'], r['sign']))
    for i, s in enumerate('3.35.44.12.34.21.7'.split('.'), 1):   # f468/passes.tsv g13, gloss 'Welling' (control)
        rows.append(('f468_g13', str(i), s))
    return rows

def keycl():
    out = []
    for r in csv.DictReader(open(os.path.join(T, 'key.tsv')), delimiter='\t'):
        v = r['value'].strip().lower()
        out.append((r['code'], v if re.fullmatch('[a-z]', v) else '_', r['grade']))
    return out

def render():
    n = names(); nv = sorted({v for w in n for v in variants(w)})
    return {'pool_names.tsv': n, 'pool_names_var.tsv': nv, 'pool_fr.tsv': phrases(),
            'codes.tsv': ['line\tposition\tsign'] + ['\t'.join(r) for r in codes()],
            'key_cl.tsv': ['code\tletter\tgrade'] + ['\t'.join(r) for r in keycl()]}

if __name__ == '__main__':
    bad = 0
    for f, lines in render().items():
        txt = '\n'.join(lines) + '\n'; p = os.path.join(D, f)
        if '--check' in sys.argv:
            if open(p).read() != txt: print('STALE', f); bad = 1
        else:
            open(p, 'w').write(txt)
        print(f, len(lines), hashlib.sha256(txt.encode()).hexdigest()[:16])
    sys.exit(bad)
