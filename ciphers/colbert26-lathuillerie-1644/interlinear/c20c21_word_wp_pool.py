"""COL26-11B (account 2, 13 Oct 2026; PREREG-COL26-11B.md): build the pass-1 x pass-2 exact-agreement pooled pairing file and run the
UNCHANGED interlinear/c20c21_word_wp.py (sha256 checked) on it, or on pass 2 alone, in a scratch tree.
Usage: python3 interlinear/c20c21_word_wp_pool.py pool|p2|agree
"""
import csv, hashlib, os, re, shutil, subprocess, sys, tempfile
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
SHA = '473d985208891a0d6de22f5a649a59b2ef1b4dd4218c555f07358dfdbe3906d3'
def norm(s): return re.sub(r'[^a-z]', '', re.sub(r'\[[^\]]*\]', '', s.lower())).replace('v', 'u').replace('j', 'i')
def rows(f): return list(csv.DictReader(open(f), delimiter='\t'))
F = ['unit', 'word', 'first', 'last', 'conf', 'note']
def pool():
    p1, p2 = rows(f'{H}/c20c21_word_pairs.tsv'), rows(f'{H}/c20c21_word_pairs_p2.tsv')
    k2 = {(r['unit'], norm(r['word']), r['first'], r['last']) for r in p2}
    out = [r for r in p1 if (r['unit'], norm(r['word']), r['first'], r['last']) in k2]
    with open(f'{H}/c20c21_word_pairs_pool.tsv', 'w', newline='') as fh:
        w = csv.DictWriter(fh, F, delimiter='\t', extrasaction='ignore'); w.writeheader(); w.writerows(out)
    return len(p1), len(p2), len(out)
def agree():
    p1, p2 = rows(f'{H}/c20c21_word_pairs.tsv'), rows(f'{H}/c20c21_word_pairs_p2.tsv')
    d1 = {}; d2 = {}
    for d, rr in ((d1, p1), (d2, p2)):
        seen = {}
        for r in rr:
            k = (r['unit'], norm(r['word'])); seen[k] = seen.get(k, 0) + 1
            d[k + (seen[k],)] = (int(r['first']), int(r['last']))
    both = set(d1) & set(d2)
    ex = sum(d1[k] == d2[k] for k in both)
    near = sum(abs(d1[k][0] - d2[k][0]) <= 1 and abs(d1[k][1] - d2[k][1]) <= 1 for k in both)
    print(f'AGREEMENT words paired by both {len(both)} (p1 {len(d1)}, p2 {len(d2)}): exact {ex} ({ex/max(1,len(both)):.3f}), '
          f'within 1 group each end {near} ({near/max(1,len(both)):.3f})')
def run(pairs):
    src = f'{H}/c20c21_word_wp.py'
    assert hashlib.sha256(open(src, 'rb').read()).hexdigest() == SHA, 'instrument changed'
    d = tempfile.mkdtemp(); os.makedirs(f'{d}/interlinear')
    shutil.copy(src, f'{d}/interlinear/'); shutil.copy(f'{H}/c20c21_reconciled.tsv', f'{d}/interlinear/')
    shutil.copy(f'{T}/key_period.tsv', d); shutil.copy(pairs, f'{d}/interlinear/c20c21_word_pairs.tsv')
    subprocess.run([sys.executable, '-I', f'{d}/interlinear/c20c21_word_wp.py', '--stage', '1'], check=True)
mode = sys.argv[1] if len(sys.argv) > 1 else 'pool'
if mode == 'agree': agree()
elif mode == 'p2': run(f'{H}/c20c21_word_pairs_p2.tsv')
else:
    n1, n2, n = pool(); print(f'POOL pass1 rows {n1}, pass2 rows {n2}, exact-agreement rows kept {n}'); run(f'{H}/c20c21_word_pairs_pool.tsv')
