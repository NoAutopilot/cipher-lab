#!/usr/bin/env python3
"""Build tools/keys/key60.tsv (Court symbol cipher no.60, BnF fr.3995 ff.108-111) from Daniel Bourdeau's
decode60.py (github.com/dbourdeau/cyphersolver, nevers1593/, MIT code / CC BY 4.0 text).

  python3 tools/keys/key60_from_bourdeau.py PATH/TO/cyphersolver [--check]

Reads decode60.py's KEY, ROMAN and NULLS dictionaries without executing the file (ast.literal_eval of the three
assignments), and writes one row per sign: sign, value, grade, source, note. Source 'table' is the deciphering
table ff.110v-111 / enciphering sheet f.109; 'crib-f151' marks the cursive values Bourdeau read off the interlined
crib fr.3986 f.151 (key60.txt, 'CURSIVE VALUES CONFIRMED'); those, and rows whose value Bourdeau left with '?',
are graded M. --check exits 1 if the committed TSV differs from a regeneration (rule 7).
"""
import ast, subprocess, sys, os

CRIB = {'ꝺo', 'do', 'ꝑ', 'λ', '⊥', '1', '∝', 'ur', 'pi', 'X++', 'ꝺ'}   # forms first read on the f.151 crib
AMBIG = {'2+': 'p|i', '6': 'di|s', 'y': 's|ve', 'x': 'a|d'}                      # key60.txt gives two values from the crib

def load(src):
    tree = ast.parse(open(src, encoding='utf-8').read())
    d = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and node.targets[0].id in ('KEY', 'ROMAN', 'NULLS'):
            d[node.targets[0].id] = ast.literal_eval(node.value)
    return d

def build(repo):
    src = os.path.join(repo, 'nevers1593', 'decode60.py')
    h = subprocess.run(['git', '-C', repo, 'log', '-1', '--format=%H'], capture_output=True, text=True).stdout.strip()
    d = load(src)
    out = ['# Cipher no.60, the Court symbol cipher ("Chiffre baille a Monsieur de Nevers, Montereau, aoust 1593"),',
           '# BnF fr.3995 ff.108-111 (Gallica btv1b525085665 canvases 208-213). Reconstruction and numbering: Satoshi',
           '# Tomokiyo, Cryptiana (cryptiana.web.fc2.com, nevers.htm and henryiv2.htm). Transcription of the tables and',
           '# glyph tags: Daniel Bourdeau, github.com/dbourdeau/cyphersolver nevers1593/key60.txt + decode60.py',
           f'# (commit {h}; code MIT, text CC BY 4.0). Converted by tools/keys/key60_from_bourdeau.py, 24 Sept 2026.',
           '# Tags are Bourdeau\'s descriptive stand-ins (see his key60.txt for the shapes). grade M = crib-read cursive',
           '# form or value marked uncertain by him; Tomokiyo\'s own table is an image on henryiv2.htm, not compared here.',
           'sign\tvalue\tgrade\tsource\tnote']
    for s, v in d['KEY'].items():
        src_ = 'crib-f151' if s in CRIB else 'table'
        g = 'M' if (s in CRIB or '?' in v or s in AMBIG) else 'H'
        val = AMBIG.get(s, v)
        note = 'Bourdeau decode60.py value ' + v if s in AMBIG else ''
        out.append(f'{s}\t{val}\t{g}\t{src_}\t{note}')
    for s, v in d['ROMAN'].items():
        if s in d['KEY']: continue   # 'x': alphabet a (sheet) vs roman x = d (col.1); kept once as a|d, grade M
        out.append(f'{s}\t{v}\tH\ttable\troman numeral, col.1')
    for s in sorted(d['NULLS']):
        out.append(f'{s}\tNULL\tH\ttable\tnull (enciphering sheet)')
    return '\n'.join(out) + '\n'

if __name__ == '__main__':
    repo = sys.argv[1]
    tsv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'key60.tsv')
    new = build(repo)
    if '--check' in sys.argv:
        sys.exit(0 if open(tsv, encoding='utf-8').read() == new else 1)
    open(tsv, 'w', encoding='utf-8').write(new)
    print(tsv, new.count('\n') - 8, 'rows')
