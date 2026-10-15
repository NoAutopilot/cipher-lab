#!/usr/bin/env python3
"""MAT-F91C (15 Oct 2026): align_f91.py (MAT-F91) unchanged except the block list (C, F) and the input/output file names, per PREREG-MAT-F91C.md.

Builds one pair per block (whole normalised gloss vs whole reconciled cipher block), runs tools/interlinear_align.py align
with --prior ../key.tsv, scores R (PREREG-MAT-F91.md) on H single-letter codes, then 200 within-block word-shuffle
controls. Unsettled columns (pass A != pass B) enter as '@?' and are excluded. Writes align_f91c_result.tsv and
align_f91c_codes.tsv. Usage: python3 align_f91.py [--draws 200]
"""
import csv, os, random, subprocess, sys, tempfile, collections, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
TOOL = os.path.join(ROOT, 'tools', 'interlinear_align.py'); KEY = os.path.join(HERE, '..', 'key.tsv')
BLOCKS = ['C', 'F']
DRAWS = int(sys.argv[sys.argv.index('--draws') + 1]) if '--draws' in sys.argv else 200
FOLD = str.maketrans('vj', 'ui')

def fold(s):
    s = unicodedata.normalize('NFKD', s.lower()); return ''.join(c for c in s if 'a' <= c <= 'z').translate(FOLD)

key = {}
for r in csv.DictReader(open(KEY), delimiter='\t'):
    key[r['code']] = (r['value'], r['grade'])
toks = collections.defaultdict(list)
for r in csv.DictReader(open(os.path.join(HERE, 'ciphertext_draft_f91c.tsv')), delimiter='\t'):
    b = r['line'][0]
    if b not in BLOCKS: continue
    s = r['sign'] if r['confidence'] == 'H' else '?'
    toks[b].append(('%' + s) if s.isdigit() and int(s) >= 10 else '@' + s)
gloss = collections.defaultdict(list)
for r in csv.DictReader(open(os.path.join(HERE, 'gloss_f91c.tsv')), delimiter='\t'):
    if r['block'] in BLOCKS: gloss[r['block']] += r['normalised'].split()
prior = tempfile.NamedTemporaryFile('w', suffix='.tsv', delete=False)
prior.write('code\tvalue\n')
for c, (v, g) in key.items():
    if g == 'H' and len(v) == 1: prior.write(f'{c}\t{v}\n')
prior.close()

def run(glosses):
    d = tempfile.mkdtemp(); pp = os.path.join(d, 'pairs.tsv')
    with open(pp, 'w') as f:
        f.write('plain_line\tplain_raw\tcipher_line\tcipher_raw\n')
        for b in BLOCKS: f.write(f'{b}\t{" ".join(glosses[b])}\t{b}\t{" ".join(toks[b])}\n')
    out = os.path.join(d, 'align.tsv')
    subprocess.run([sys.executable, TOOL, 'align', pp, out, os.path.join(d, 'key.tsv'), '--code-prefix', '@',
                    '--word-code-prefix', '%', '--prior', prior.name, '--keep-fs', '--max-chunk', '12'],
                   check=True, capture_output=True)
    return list(csv.DictReader(open(out), delimiter='\t'))

def score(rows):
    per = collections.defaultdict(list); hit = n = 0; blk = collections.Counter(); blkn = collections.Counter()
    for r in rows:
        c = r['raw'].lstrip('@%'); ch = fold(r['plain_chunk'] or '')
        if c == '?' or not ch: continue
        per[c].append(ch)
        if c in key and key[c][1] == 'H' and len(key[c][0]) == 1:
            n += 1; blkn[r['cipher_line']] += 1
            if ch == fold(key[c][0]): hit += 1; blk[r['cipher_line']] += 1
    return (hit / n if n else 0.0), hit, n, per, {b: (blk[b], blkn[b]) for b in BLOCKS}

R, hit, n, per, byblk = score(run(gloss))
ctrl = []
for s in range(1, DRAWS + 1):
    rnd = random.Random(s); g = {b: rnd.sample(gloss[b], len(gloss[b])) for b in BLOCKS}
    ctrl.append(score(run(g))[0])
ctrl.sort(); mx = ctrl[-1]; p95 = ctrl[int(0.95 * len(ctrl)) - 1]; mean = sum(ctrl) / len(ctrl)
gate = R > mx and R >= 0.60
with open(os.path.join(HERE, 'align_f91c_result.tsv'), 'w') as f:
    f.write('stat\tvalue\n')
    for k, v in [('R', f'{R:.3f}'), ('hits', hit), ('aligned_H_letter_tokens', n), ('ctrl_mean', f'{mean:.3f}'),
                 ('ctrl_p95', f'{p95:.3f}'), ('ctrl_max', f'{mx:.3f}'), ('draws', DRAWS), ('gate', 'PASS' if gate else 'FAIL')]:
        f.write(f'{k}\t{v}\n')
    for b, (h, m) in byblk.items(): f.write(f'R_block_{b}\t{h}/{m}\n')
with open(os.path.join(HERE, 'align_f91c_codes.tsv'), 'w') as f:
    f.write('code\tkey_value\tkey_grade\tn_aligned\ttop_chunk\ttop_share\tclass\n')
    for c, chs in sorted(per.items(), key=lambda kv: -len(kv[1])):
        top, k = collections.Counter(chs).most_common(1)[0]; share = k / len(chs)
        kv, kg = key.get(c, ('', 'absent'))
        alts = {fold(a) for a in kv.split('|')} if kv else set()
        if len(chs) < 2 or share < 0.6: cls = 'undecided'
        elif kg in ('U', 'absent') or kv in ('+', '*'): cls = 'candidate-M'
        elif top in alts: cls = 'confirmed' if kg == 'H' else 'picks-alternative'
        else: cls = 'conflict'
        f.write(f'{c}\t{kv}\t{kg}\t{len(chs)}\t{top}\t{share:.2f}\t{cls}\n')
print(f'R {R:.3f} ({hit}/{n}); control mean {mean:.3f} p95 {p95:.3f} max {mx:.3f} over {DRAWS}; gate {"PASS" if gate else "FAIL"}; by block {byblk}')
