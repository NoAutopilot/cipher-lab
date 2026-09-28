#!/usr/bin/env python3
"""H75 (28 Sept 2026): regenerate every number the r16-r17 Burgsdorf crib candidate stands on, from committed files,
into candidates/crib_evidence.tsv; --check exits 1 if the committed TSV is stale (CLAUDE.md rule 7 shape). A crib
candidate's evidence, not a reading: reading.txt, key.tsv and every grade are unchanged.
Numbers: H41 (402 Urkunden Bd. 4-5 names), H53 (wildcard variants), H61 (599 / 883 names, only 72 wild), H62 (72 split as
7 2), H63 (r16 ink gaps, needs Pillow and images/f22r_canvas58.jpg), H71 (best list fit on read, name-free windows),
H72 (synthetic-name null), H74 (independent onomasticon).
  python3 ciphers/espagnol142-mercy-1648/candidates/crib_evidence.py [--check] [--skip-image]"""
import os, sys, subprocess
D = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(D); ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, os.path.join(ROOT, 'tools')); import crib_list_fit as clf
os.chdir(T)
C, K = 'cipher_codes_522.tsv', 'key.tsv'
def words(f): return [l.split('\t')[0] for l in open(f) if l.strip()]
def run(label, codes, wordfile, fixed=('S',), wild=()):
    toks = clf.load_window(codes, K, 'r16:2', 'r18:21', fixed, wild)
    res = clf.rank(words(wordfile), toks); v = clf.verdict(res)
    b = next(r for r in res if r[4] == 'burgsdorf')
    return [(f'{label}.best', v['best']), (f'{label}.burgsdorf', f'{b[0]} ({b[1]}/{b[2]}) at {b[3]}'),
            (f'{label}.P', f"{v['P']:.3f}"), (f'{label}.candidate', str(v['candidate']))]
out = []
out += run('H41', C, 'h41/namelist.tsv')
out += run('H53a_nomen_only', C, 'h41/namelist.tsv', ('S', 'M'), ('48', '52', '65', '72'))
out += run('H53b_72_only', C, 'h41/namelist.tsv', ('S', 'M'), ('72',))
toks_c = clf.load_window(C, K, 'r16:2', 'r18:21', ('S', 'M'), ())
out.append(('H53c_none.burgsdorf', '%s (%s/%s)' % clf.fit('burgsdorf', toks_c)[:3]))
out += run('H61_599', C, 'h61/names_bd1236.tsv', ('S', 'M'), ('72',))
out += run('H61_883', C, 'h61/names_bd1to6.tsv', ('S', 'M'), ('72',))
out += run('H62_split', 'h62/cipher_codes_split72.tsv', 'h41/namelist.tsv', ('S', 'M'), ())
if '--skip-image' not in sys.argv:
    g = subprocess.run([sys.executable, 'h63/gaps.py'], capture_output=True, text=True).stdout
    gl = [l for l in g.split('\n') if l.startswith('span 32')]
    out.append(('H63.r16_21_gap_px', gl[0].split('gap to next')[1].strip() if gl else 'n/a'))
r71 = subprocess.run([sys.executable, 'h71/fp.py'], capture_output=True, text=True).stdout.strip().split('\n')
out.append(('H71', r71[0])); out.append(('H71.top_scores', r71[1].split(':', 1)[1].strip()))
r72 = subprocess.run([sys.executable, 'h72/synth.py'], capture_output=True, text=True).stdout.strip().split('\n')[0]
out.append(('H72', r72))
toks = clf.load_window(C, K, 'r16:2', 'r17:21')   # unread tokens only (r18 is read: "...cartas de cr...")
res = clf.rank(words('h74/onomasticon.tsv'), toks)
out.append(('H74.best_on_unread_r16_2_r17_21', '%s %s (%s/%s)' % (res[0][4], res[0][0], res[0][1], res[0][2])))
text = 'item\tvalue\n' + ''.join(f'{k}\t{v}\n' for k, v in out)
path = os.path.join(D, 'crib_evidence.tsv')
if '--check' in sys.argv:
    ok = os.path.exists(path) and open(path).read() == text
    print('crib_evidence.tsv', 'current' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(path, 'w').write(text); print(text)
