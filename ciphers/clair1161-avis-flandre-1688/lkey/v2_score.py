#!/usr/bin/env python3
"""C1161-V2 score + rule-3 control (lkey/PREREG-C1161-V2.md). Usage: python3 v2_score.py [--draws 300] [--seed 1]
Scores baseline (key.tsv on ciphertext.tsv), V1 (key_lasry.tsv), V2 and V2b (ciphertext_v2.tsv under key_v2/key_v2b) by the spec
judge's fr16 4-gram model; nulls permute Lasry's ten nomenclature values among his ten codes (V2b also the five post-hoc letter signs);
known-answer cover of his f163r excerpt on c186R; per-face longest covered run. Writes lkey/v2_score.tsv."""
import sys, csv, json, random, argparse, collections, difflib
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
import judge_plaintext as J
T = Path(__file__).resolve().parents[1]
ap = argparse.ArgumentParser(); ap.add_argument('--draws', type=int, default=300); ap.add_argument('--seed', type=int, default=1)
a = ap.parse_args()
spec = json.load(open(T.parents[1] / 'specs' / 'clair1161-avis-flandre-1688.json'))
M = J.NgramModel([J.read_corpus(T.parents[1] / p) for p in spec['judge']['corpora']])
NOM = ['77', '62', '55', '52', '48', '76', '37', '30', '60', '44']
POST = ['8', 'rc', 'tz', 'c', 'L']
EXC = J.fold("""Ce Seigneur a par deulx fois escript et mande a ceste royne quelle laissast passer en silence et dissimulation beaucoup
de choses quant au faict de la religion en ce royaume afin de regaigner sa noblesse et peuple et que son filz et elle y puissent regner et
commander en plus grand repos""")
def key(p): return {r['sign']: r['value'] for r in csv.DictReader(open(p), delimiter='\t')}
def ct(p): return list(csv.DictReader(open(p), delimiter='\t'))
C1, C2 = ct(T / 'ciphertext.tsv'), ct(T / 'lkey' / 'ciphertext_v2.tsv')
def decode(c, k):
    f = collections.defaultdict(str)
    for r in c: f[r['line'].split('_')[0]] += k.get(r['sign'], '')
    return f
def known(f):
    s = J.fold(f['c186R']); m = difflib.SequenceMatcher(None, EXC, s, autojunk=False)
    return sum(b.size for b in m.get_matching_blocks() if b.size >= 4) / len(EXC)
def score(c, k):
    f = decode(c, k); t = ''.join(f[x] for x in sorted(f)); return M.score(t), known(f), f
def longest_run(s):
    s = J.fold(s); i = run = best = 0
    while i < len(s):
        L = next((L for L in range(min(M.maxw, len(s) - i), 2, -1) if s[i:i+L] in M.words), 0)
        if L: run += L; i += L; best = max(best, run)
        else: run = 0; i += 1
    return best
kb, k1, k2, k2b = (key(T / p) for p in ('key.tsv', 'lkey/key_lasry.tsv', 'lkey/key_v2.tsv', 'lkey/key_v2b.tsv'))
B, V1, V2, V2b = score(C1, kb), score(C1, k1), score(C2, k2), score(C2, k2b)
rnd = random.Random(a.seed)
def null(k, letters):
    out = []
    for _ in range(a.draws):
        kk = dict(k); v = [k['n' + c] for c in NOM]; rnd.shuffle(v); kk.update(('n' + c, x) for c, x in zip(NOM, v))
        if letters:
            v = [k[s] for s in letters]; rnd.shuffle(v); kk.update(zip(letters, v))
        out.append(score(C2, kk)[:2])
    return sorted(x[0] for x in out), sorted(x[1] for x in out)
n2, kn2 = null(k2, []); n2b, kn2b = null(k2b, POST)
p = J.pct
print(f"baseline key.tsv  score {B[0]:.4f}  known-answer c186R {B[1]:.3f}")
print(f"V1 key_lasry      score {V1[0]:.4f}  known {V1[1]:.3f}")
print(f"V2 units          score {V2[0]:.4f}  known {V2[1]:.3f}")
print(f"  null({a.draws}) score median {p(n2,.5):.4f} p99 {p(n2,.99):.4f} max {n2[-1]:.4f}; known p99 {p(kn2,.99):.3f}")
print(f"  GATE V2 > p99: {'PASS' if V2[0] > p(n2,.99) else 'FAIL'}; V2 - baseline {V2[0]-B[0]:+.4f}; V2 - V1 {V2[0]-V1[0]:+.4f}")
print(f"  known-answer: V2 > baseline {V2[1] > B[1]}, V2 > null p99 {V2[1] > p(kn2,.99)}")
print(f"V2b units+5 post-hoc score {V2b[0]:.4f}  known {V2b[1]:.3f}")
print(f"  null({a.draws}) score median {p(n2b,.5):.4f} p99 {p(n2b,.99):.4f} max {n2b[-1]:.4f}; known p99 {p(kn2b,.99):.3f}")
print(f"  gate V2b > p99: {'PASS' if V2b[0] > p(n2b,.99) else 'FAIL'} (post-hoc selection: M at best); V2b - baseline {V2b[0]-B[0]:+.4f}")
gate = V2[0] > p(n2, .99)
with open(T / 'lkey' / 'v2_score.tsv', 'w') as fh:
    fh.write('face\tbaseline_longest_run\tv2_longest_run\tv2b_longest_run\tlicensed_gain(gate PASS and v2>=20 and +5)\n')
    for x in sorted(B[2]):
        o, n, nb = longest_run(B[2][x]), longest_run(V2[2][x]), longest_run(V2b[2][x])
        g = gate and n >= 20 and n - o >= 5
        fh.write(f"{x}\t{o}\t{n}\t{nb}\t{'yes' if g else 'no'}\n"); print(x, o, n, nb, 'LICENSED GAIN' if g else '-')
