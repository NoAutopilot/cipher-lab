#!/usr/bin/env python3
"""C1161-LKEY score + rule-3 control (lkey/PREREG-C1161-LKEY.md). Usage: python3 lkey_score.py [--draws 200] [--seed 1]
Scores our key.tsv decode (baseline), the key_lasry.tsv decode (V1) and V1 with the changed signs' values permuted among
themselves (200 draws), by the spec judge's fr16 4-gram model; per-face longest covered run. Writes lkey/score.tsv."""
import sys, csv, json, random, argparse, collections
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
import judge_plaintext as J
T = Path(__file__).resolve().parents[1]
ap = argparse.ArgumentParser(); ap.add_argument('--draws', type=int, default=200); ap.add_argument('--seed', type=int, default=1)
a = ap.parse_args()
spec = json.load(open(T.parents[1] / 'specs' / 'clair1161-avis-flandre-1688.json'))
M = J.NgramModel([J.read_corpus(T.parents[1] / p) for p in spec['judge']['corpora']])
def key(p): return {r['sign']: r['value'] for r in csv.DictReader(open(p), delimiter='\t')}
ct = list(csv.DictReader(open(T / 'ciphertext.tsv'), delimiter='\t'))
def decode(k):
    faces = collections.defaultdict(str)
    for r in ct: faces[r['line'].split('_')[0]] += k.get(r['sign'], '')
    return faces
def longest_run(s):
    s = J.fold(s); i = run = best = 0
    while i < len(s):
        L = next((L for L in range(min(M.maxw, len(s) - i), 2, -1) if s[i:i+L] in M.words), 0)
        if L: run += L; i += L; best = max(best, run)
        else: run = 0; i += 1
    return best
def score(k):
    f = decode(k); t = ''.join(f[x] for x in sorted(f)); return M.score(t), M.cover(t), f
ours, las = key(T / 'key.tsv'), key(T / 'lkey' / 'key_lasry.tsv')
changed = sorted(s for s in las if las[s] != ours.get(s))
b, v = score(ours), score(las)
rnd = random.Random(a.seed); null = []
for _ in range(a.draws):
    vals = [las[s] for s in changed]; rnd.shuffle(vals); k = dict(las); k.update(zip(changed, vals)); null.append(score(k)[0])
null.sort(); p99 = J.pct(null, 0.99)
print(f"changed signs {len(changed)}: {' '.join(s+':'+ours.get(s,'-')+'>'+las[s] for s in changed)}")
print(f"baseline key.tsv score {b[0]:.4f} cover {b[1]:.3f}")
print(f"V1 key_lasry.tsv score {v[0]:.4f} cover {v[1]:.3f}")
print(f"permuted-changed null ({a.draws}): median {J.pct(null,.5):.4f} p99 {p99:.4f} max {null[-1]:.4f}")
print(f"gate V1 > p99: {'PASS' if v[0] > p99 else 'FAIL'}; V1 - baseline {v[0]-b[0]:+.4f}")
with open(T / 'lkey' / 'score.tsv', 'w') as fh:
    fh.write('face\tletters\tours_longest_run\tv1_longest_run\tgain_stretch(>=20 and +5)\n')
    for x in sorted(b[2]):
        o, n = longest_run(b[2][x]), longest_run(v[2][x])
        g = n >= 20 and n - o >= 5
        fh.write(f"{x}\t{len(J.fold(v[2][x]))}\t{o}\t{n}\t{'yes' if g else 'no'}\n"); print(x, o, n, 'GAIN' if g else '-')
