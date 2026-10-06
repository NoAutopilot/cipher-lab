"""R10-BAL103E: fr17 test of '9 = s everywhere' on f.50 against two nulls (r10e/PREREG.md). --check exits 1 if result.tsv is stale."""
import csv, os, random, sys, json
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H); R = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, os.path.join(R, 'tools'))
import judge_plaintext as jp
spec = json.load(open(os.path.join(R, 'specs', 'baluze103-letellier-marca-1644.json')))
m = jp.NgramModel([jp.read_corpus(p) for p in jp.LANG_CORPORA[spec['judge']['language']]])
toks, nine = [], []
for r in csv.DictReader(open(os.path.join(T, 'reading_tokens.tsv')), delimiter='\t'):
    if r['grade'] == 'U' or r['value'] in ('', '?'): continue
    for k, ch in enumerate(jp.fold(r['value'].split('|')[0])):
        toks.append(ch)
        if sorted(r['value'].split('|')) == ['i', 'r', 's']: nine.append(len(toks) - 1)
S0 = m.score(''.join(toks)); n9 = set(nine)
other = [i for i in range(len(toks)) if i not in n9]
freq = [toks[i] for i in other]
def pctl(x, xs): return sum(v < x for v in xs) / len(xs)
def p95(xs): return sorted(xs)[int(0.95 * len(xs))]
out = [f"letters\t{len(toks)}\nnine_positions\t{len(nine)}\nS_committed\t{S0:.4f}"]
res = {}
for v in 'sir':
    ch = [i for i in nine if toks[i] != v]
    t = toks[:]
    for i in ch: t[i] = v
    D = m.score(''.join(t)) - S0
    rn = random.Random(1644); pool = [i for i in other if toks[i] != v]
    n1, n2 = [], []
    for _ in range(2000):
        t = toks[:]
        for i in rn.sample(pool, len(ch)): t[i] = v
        n1.append(m.score(''.join(t)) - S0)
        t = toks[:]
        for i in ch: t[i] = rn.choice(freq)
        n2.append(m.score(''.join(t)) - S0)
    res[v] = (D, n1, n2)
    out.append(f"all_{v}\tm={len(ch)}\tD={D:.4f}\tnull1_p95={p95(n1):.4f}\tnull1_median={sorted(n1)[1000]:.4f}\tpctl1={pctl(D, n1):.3f}"
               f"\tnull2_p95={p95(n2):.4f}\tnull2_median={sorted(n2)[1000]:.4f}\tpctl2={pctl(D, n2):.3f}")
D, n1, n2 = res['s']
g = [D >= 0, D > p95(n1), D > p95(n2)]
out.append(f"G1\t{'pass' if g[0] else 'fail'}\nG2\t{'pass' if g[1] else 'fail'}\nG3\t{'pass' if g[2] else 'fail'}\ngate\t{'PASS' if all(g) else 'FAIL'}")
txt = '\n'.join(out) + '\n'; f = os.path.join(H, 'result.tsv')
if '--check' in sys.argv:
    ok = os.path.exists(f) and open(f).read() == txt; print('r10e up to date' if ok else 'stale: result.tsv'); sys.exit(0 if ok else 1)
open(f, 'w').write(txt); print(txt)
