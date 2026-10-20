"""SHERWOOD-REREAD (20 Oct 2026): align blind passes A/B to ciphertext.tsv per line and score the known-answer gate and the
33 targets (PREREG-SHERWOOD-REREAD.md). Token alignment is edit-distance DP with a per-pair cost from digit similarity."""
import csv, os, sys
H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def load_tx():
    d = {}
    for l in open(os.path.join(H, 'ciphertext.tsv')):
        if l.startswith('#') or l.startswith('line\t'): continue
        a, b = l.rstrip('\n').split('\t'); d[a] = b.split()
    return d
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
def nums(toks):
    """Flatten a line to its sequence of numbers (chained groups such as 246-35-364 split on '-'); words dropped.
    Returns the numbers and, per token, the index range of its numbers."""
    out, spans = [], []
    for t in toks:
        if t.startswith('g:'): t = t.split('@', 1)[1]
        if t.startswith(('w:', 'x:')): spans.append((len(out), len(out))); continue
        ps = [p for p in norm(t).split('-') if p]; spans.append((len(out), len(out) + len(ps))); out += ps
    return out, spans
def lookup(line, group, k):
    ref = tx[line]; group = norm(group); idx = [i for i, t in enumerate(ref) if norm(t.split('@')[-1]) == group][k]
    rn, sp = nums(ref); a, b = sp[idx]; res = []
    for p in 'AB':
        if line not in P[p]: res.append(None); continue
        hn, _ = nums(P[p][line]); al = align(rn, hn)[a:b]
        res.append(None if any(x is None for x in al) else '-'.join(al))
    return res
def score(fn, out):
    rows = list(csv.DictReader(open(os.path.join(H, 'tx2', fn)), delimiter='\t')); seen = {}; res = []
    for r in rows:
        k = seen.get((r['line'], r['group']), 0); seen[(r['line'], r['group'])] = k + 1
        a, b = lookup(r['line'], r['group'], k)
        na, nb = (norm(a) if a else ''), (norm(b) if b else '')
        g0 = norm(r['group']); res.append((r['line'], r['group'], a or '-', b or '-', int(na != g0), int(nb != g0),
                    int(na == nb and na != g0 and na != '')))
    with open(os.path.join(H, 'tx2', out), 'w') as f:
        f.write('line\tgroup\tpassA\tpassB\tA_diff\tB_diff\tagree_change\n')
        for x in res: f.write('\t'.join(map(str, x)) + '\n')
    n = len(res); return n, sum(x[4] for x in res), sum(x[5] for x in res), sum(x[6] for x in res)
for fn, out in [('known_answer.tsv', 'ka_scored.tsv'), ('targets.tsv', 'targets_scored.tsv')]:
    n, ea, eb, ch = score(fn, out)
    print('%s: n=%d passA_diff=%d (%.1f%%) passB_diff=%d (%.1f%%) A=B!=tx %d (%.1f%%)' % (fn, n, ea, 100*ea/n, eb, 100*eb/n, ch, 100*ch/n))
