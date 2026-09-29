#!/usr/bin/env python3
"""DEB-SWARM-0 (29 Sept 2026): build swarm/corpora/ from Project Gutenberg bodies (fetched once to a scratch dir)
and the repo's existing tools/data corpora. Writes <lang>.txt.gz (folded a-z plus spaces) and MANIFEST.tsv.
Usage: build_corpora.py --gut DIR   (DIR holds pg<id>.txt as fetched from gutenberg.org/cache/epub/<id>/pg<id>.txt)"""
import argparse, gzip, hashlib, os, re, unicodedata, pathlib
HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parents[2] / 'tools' / 'data'
SOURCES = {  # lang: [(kind, id/path, author, title, year)]
 'fr': [('repo', 'fr19/pg14155_Madame_Bovary.txt.gz', 'Flaubert', 'Madame Bovary', 1857),
        ('repo', 'fr19/pg11131_Pierre_et_Jean.txt.gz', 'Maupassant', 'Pierre et Jean', 1888),
        ('repo', 'fr19v/pg6099_Les_Fleurs_du_Mal.txt.gz', 'Baudelaire', 'Les Fleurs du Mal (verse)', 1857)],
 # verse used for the controls' plaintexts (Hugo, Tennyson, Camoes) is kept OUT of these corpora on purpose
 'en': [('repo', 'en/pg76_huckfinn.txt', 'Twain', 'Adventures of Huckleberry Finn', 1884),
        ('gut', 98, 'Dickens', 'A Tale of Two Cities', 1859)],
 'pt': [('gut', 16425, 'Castelo Branco', "Amor de Perdicao", 1862),
        ('gut', 21406, 'Castelo Branco', 'Novelas do Minho', 1875)],
 'es': [('gut', 17223, 'Valera', 'Pepita Jimenez', 1874),
        ('gut', 29506, 'Alarcon', 'El sombrero de tres picos', 1874)],
 'la': [('repo', 'la18/zaluski_epistolae_t1.txt.gz', 'Zaluski', 'Epistolae historico-familiares t.1 (1680-1740 chancery Latin; no 1850-1900 Latin prose corpus on disk)', 1709)],
}
def fold(s):
    s = unicodedata.normalize('NFKD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('ß', 'ss').replace('æ', 'ae').replace('œ', 'oe')
    return re.sub(r'[^a-z]+', ' ', s).strip()
def body(t):
    a = re.search(r'\*\*\* ?START OF[^\n]*\n', t); b = re.search(r'\*\*\* ?END OF', t)
    return t[a.end() if a else 0: b.start() if b else len(t)]
def read(p):
    return (gzip.open(p, 'rt', encoding='utf-8', errors='replace') if str(p).endswith('.gz') else open(p, encoding='utf-8', errors='replace')).read()
if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--gut', required=True); a = ap.parse_args()
    rows = ['lang\tsource\tauthor\ttitle\tyear\tsha1_raw\tletters']
    for lang, srcs in SOURCES.items():
        parts = []
        for kind, ref, au, ti, yr in srcs:
            p = DATA / ref if kind == 'repo' else pathlib.Path(a.gut) / f'pg{ref}.txt'
            raw = read(p); t = fold(body(raw)); parts.append(t)
            src = f'tools/data/{ref}' if kind == 'repo' else f'https://www.gutenberg.org/cache/epub/{ref}/pg{ref}.txt'
            rows.append(f'{lang}\t{src}\t{au}\t{ti}\t{yr}\t{hashlib.sha1(raw.encode()).hexdigest()}\t{len(t.replace(" ", ""))}')
        with gzip.open(HERE / 'corpora' / f'{lang}.txt.gz', 'wt', compresslevel=9) as f:
            f.write('\n'.join(parts))
    (HERE / 'corpora' / 'MANIFEST.tsv').write_text('\n'.join(rows) + '\n')
    print('\n'.join(rows))
