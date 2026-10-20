"""SHERWOOD-REREAD (20 Oct 2026): align blind passes A/B to ciphertext.tsv per line and score the known-answer gate and the
33 targets (PREREG-SHERWOOD-REREAD.md). Token alignment is edit-distance DP with a per-pair cost from digit similarity."""
import csv, os, sys
H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def load_tx():
    d = {}
    for l in open(os.path.join(H, 'ciphertext.tsv')):
        if l.startswith('#') or l.startswith('line\t'): continue
        a, b = l.rstrip('\n').split('\t'); d[a] = b.split()
    d['p347_L05'] = d['p347_L05b']; return d
def load_pass(p):
    d = {}
    for f in sorted(os.listdir(os.path.join(H, 'tx2'))):
        if f.startswith('pass%s_' % p) and f.endswith('.tsv'):
            for l in open(os.path.join(H, 'tx2', f)):
                if '\t' in l: a, b = l.rstrip('\n').split('\t', 1); d[a.strip()] = b.split()
    return d
norm = lambda t: t.rstrip('?')
def cost(a, b):
    a, b = norm(a), norm(b)
    if a == b: return 0
    if a.startswith(('w:', 'x:', 'g:')) or b.startswith(('w:', 'x:', 'g:')): return 2
    import difflib
    return 2 * (1 - difflib.SequenceMatcher(None, a, b).ratio())
def align(ref, hyp):
    n, m = len(ref), len(hyp); D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): D[i][0] = i
    for j in range(m + 1): D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + cost(ref[i-1], hyp[j-1]))
    i, j, out = n, m, [None] * n
    while i > 0 and j > 0:
        if D[i][j] == D[i-1][j-1] + cost(ref[i-1], hyp[j-1]): out[i-1] = hyp[j-1]; i -= 1; j -= 1
        elif D[i][j] == D[i-1][j] + 1: i -= 1
        else: j -= 1
    return out
tx = load_tx(); P = {p: load_pass(p) for p in 'AB'}
def lookup(line, group, k):
    ref = tx[line]; idx = [i for i, t in enumerate(ref) if norm(t) == group][k]
    return [(align(ref, P[p].get(line, [])) or [None] * len(ref))[idx] if line in P[p] else None for p in 'AB']
def score(fn, out):
    rows = list(csv.DictReader(open(os.path.join(H, 'tx2', fn)), delimiter='\t')); seen = {}; res = []
    for r in rows:
        k = seen.get((r['line'], r['group']), 0); seen[(r['line'], r['group'])] = k + 1
        a, b = lookup(r['line'], r['group'], k)
        na, nb = (norm(a) if a else ''), (norm(b) if b else '')
        res.append((r['line'], r['group'], a or '-', b or '-', int(na != r['group']), int(nb != r['group']),
                    int(na == nb and na != r['group'] and na != '')))
    with open(os.path.join(H, 'tx2', out), 'w') as f:
        f.write('line\tgroup\tpassA\tpassB\tA_diff\tB_diff\tagree_change\n')
        for x in res: f.write('\t'.join(map(str, x)) + '\n')
    n = len(res); return n, sum(x[4] for x in res), sum(x[5] for x in res), sum(x[6] for x in res)
for fn, out in [('known_answer.tsv', 'ka_scored.tsv'), ('targets.tsv', 'targets_scored.tsv')]:
    n, ea, eb, ch = score(fn, out)
    print('%s: n=%d passA_diff=%d (%.1f%%) passB_diff=%d (%.1f%%) A=B!=tx %d (%.1f%%)' % (fn, n, ea, 100*ea/n, eb, 100*eb/n, ch, 100*ch/n))
