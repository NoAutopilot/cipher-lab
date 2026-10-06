#!/usr/bin/env python3
"""R8-BAL103: f.50 transcription-vs-table test, as registered in r8/PREREG.md (pushed 3f73102cc before any score was computed).
Decodes pass A and pass B separately with key_decode.tsv (first value, U dropped, word codes -> word), scores each page and line with the
fr17 4-gram model of tools/judge_plaintext.py, runs the permutation null and the matched synthetic (fr17 enciphered with this table,
sign noise r = 0.15 / 0.30), the per-line break rule, the Spearman test and the descriptive per-sign gain.
Writes r8/lines.tsv, r8/result.tsv, r8/sign_gain.tsv, r8/decodes.txt; --check exits 1 if any committed output is stale."""
import sys, os, random, gzip
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H); R = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, os.path.join(R, 'tools'))
import judge_plaintext as J

def readkey():
    k = {}
    for ln in open(os.path.join(T, 'key_decode.tsv')):
        if ln.startswith('#') or ln.startswith('code\t'): continue
        c, v = ln.rstrip('\n').split('\t')[:2]; k[c] = v.split('|')[0]
    return k
KEY = readkey()
LETSIGNS = [s for s, v in KEY.items() if len(v) == 1]

def readpass(p):
    lines = {}
    for i, ln in enumerate(open(os.path.join(T, p))):
        if i == 0: continue
        f = ln.rstrip('\n').split('\t')
        lines.setdefault(f[0], []).append(f[2])
    return lines
PASSES = {'A': {}, 'B': {}}
for pg, a, b in (('r', 'tx/f50r_passA_long.tsv', 'tx/r7b/f50r_passB_long.tsv'), ('v', 'tx/f50v_passA_long.tsv', 'tx/f50v_passB_long.tsv')):
    PASSES['A'].update(readpass(a)); PASSES['B'].update(readpass(b))
AGR = {}
for p in ('tx/r7b/rec_r/agreement.tsv', 'tx/r7b/rec_v/agreement.tsv'):
    for i, ln in enumerate(open(os.path.join(T, p))):
        if i: f = ln.rstrip('\n').split('\t'); AGR[f[0]] = float(f[5])
LINES = sorted(AGR)

def dec(signs, key=KEY):
    return ''.join(key[s] for s in signs if s in key and key[s] not in ('', '?')).lower()

M = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA['fr17']])
sc = M.score

def synth(n, r, rnd, start=None):
    """fr17 window -> signs (random homophone; que/qui -> =11/=12; letters without a sign dropped) -> noise at rate r -> decode."""
    inv = {}
    for s in LETSIGNS: inv.setdefault(KEY[s], []).append(s)
    raw = M.raw
    j = rnd.randrange(0, len(raw) - 3 * n) if start is None else start
    txt = raw[j:j + 3 * n].replace('j', 'i').replace('v', 'u').replace('w', 'u').replace('k', 'c')
    out, i = [], 0
    while i < len(txt) and len(out) < n:
        if txt.startswith('que', i): out.append('=11'); i += 3; continue
        if txt.startswith('qui', i): out.append('=12'); i += 3; continue
        c = txt[i]; i += 1
        if c in inv: out.append(rnd.choice(inv[c]))
    out = [rnd.choice([s for s in LETSIGNS if s != x]) if rnd.random() < r else x for x in out]
    return out

def pct(xs, q): xs = sorted(xs); return xs[min(len(xs) - 1, int(q * (len(xs) - 1)))]

def ranks(x):
    o = sorted(range(len(x)), key=lambda i: x[i]); r = [0.0] * len(x); i = 0
    while i < len(o):
        j = i
        while j + 1 < len(o) and x[o[j + 1]] == x[o[i]]: j += 1
        for k in range(i, j + 1): r[o[k]] = (i + j) / 2
        i = j + 1
    return r
def spear(a, b):
    ra, rb = ranks(a), ranks(b); n = len(a); ma, mb = sum(ra) / n, sum(rb) / n
    num = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    den = (sum((x - ma) ** 2 for x in ra) * sum((y - mb) ** 2 for y in rb)) ** .5
    return num / den if den else 0.0

def run():
    rnd = random.Random(1644); res = []; out_dec = []
    page = {p: [s for L in LINES for s in PASSES[p][L]] for p in 'AB'}
    S = {p: sc(dec(page[p])) for p in 'AB'}
    nlet = {p: len(dec(page[p])) for p in 'AB'}
    # T1 permutation null
    vals = [KEY[s] for s in LETSIGNS]; perm = {'A': [], 'B': []}
    for _ in range(200):
        v = vals[:]; rnd.shuffle(v); k2 = dict(KEY); k2.update(zip(LETSIGNS, v))
        for p in 'AB': perm[p].append(sc(dec(page[p], k2)))
    # T1 synthetic
    syn = {}
    for r in (0.15, 0.30):
        syn[r] = [sc(dec(synth(nlet['A'], r, rnd))) for _ in range(20)]
    for p in 'AB':
        res += [('T1', f'S_pass{p}', f'{S[p]:.3f}'), ('T1', f'letters_pass{p}', nlet[p]),
                ('T1', f'perm_mean_pass{p}', f'{sum(perm[p]) / 200:.3f}'), ('T1', f'perm_p99_pass{p}', f'{pct(perm[p], .99):.3f}'),
                ('T1', f'table_reads_pass{p}', S[p] > pct(perm[p], .99))]
    for r in syn:
        res += [('T1', f'synth_r{r}_mean', f'{sum(syn[r]) / 20:.3f}'), ('T1', f'synth_r{r}_p05', f'{pct(syn[r], .05):.3f}'),
                ('T1', f'synth_r{r}_p95', f'{pct(syn[r], .95):.3f}')]
    # T2 per-line reference: r=0.15 synthetic windows at each line length
    ref = {}
    rows = []
    for L in LINES:
        dA, dB = dec(PASSES['A'][L]), dec(PASSES['B'][L])
        sA, sB = sc(dA), sc(dB)
        br = {}
        for p, d, s in (('A', dA, sA), ('B', dB, sB)):
            n = len(d)
            if n not in ref:
                ref[n] = pct([sc(dec(synth(n + 4, 0.15, rnd))[:n]) for _ in range(200)], .05)
            br[p] = s < ref[n]
        rows.append((L, AGR[L], len(dA), len(dB), sA, sB, ref[len(dA)], ref[len(dB)], br['A'], br['B'], br['A'] and br['B'], dA, dB))
        out_dec.append(f'{L}\tagr={AGR[L]:.3f}\n  A: {dA}\n  B: {dB}')
    agr = [r[1] for r in rows]; mean = [(r[4] + r[5]) / 2 for r in rows]
    rho = spear(agr, mean); ge = 0
    for _ in range(10000):
        m2 = mean[:]; rnd.shuffle(m2)
        if spear(agr, m2) >= rho: ge += 1
    p_rho = (ge + 1) / 10001
    HI = [r for r in rows if r[1] >= 0.90]; LO = [r for r in rows if r[1] < 0.80]
    fHI = sum(r[10] for r in HI) / len(HI) if HI else float('nan'); fLO = sum(r[10] for r in LO) / len(LO) if LO else float('nan')
    t1 = all(S[p] > pct(perm[p], .99) for p in 'AB')
    if not t1 or (fHI >= 0.5 and p_rho >= 0.05): verdict = 'table suspect'
    elif fHI < 0.5 and (p_rho < 0.05 or fLO > fHI): verdict = 'transcription suspect'
    else: verdict = 'undecided'
    res += [('T2', 'break_lines', sum(r[10] for r in rows)), ('T2', 'lines', len(rows)),
            ('T2', 'HI_lines', len(HI)), ('T2', 'HI_break_frac', f'{fHI:.3f}'), ('T2', 'LO_lines', len(LO)), ('T2', 'LO_break_frac', f'{fLO:.3f}'),
            ('T2', 'spearman_rho_agr_vs_score', f'{rho:.3f}'), ('T2', 'rho_perm_p_one_sided', f'{p_rho:.4f}'), ('RULE', 'verdict', verdict)]
    # descriptive per-sign gain on ciphertext.tsv (current settled text), n counted on agreed rows
    ct = [l.rstrip('\n').split('\t') for l in open(os.path.join(T, 'ciphertext.tsv'))][1:]
    seq = [f[2] for f in ct]; nag = {}
    for f in ct:
        if f[5] == 'agree': nag[f[2]] = nag.get(f[2], 0) + 1
    base = sc(dec(seq)); gains = []
    for s in LETSIGNS:
        if nag.get(s, 0) < 5: continue
        best = max(((sc(dec(seq, dict(KEY, **{s: c}))) - base, c) for c in 'abcdefghilmnoprstuxyz' if c != KEY[s]))
        gains.append((s, KEY[s], nag[s], best[1], best[0]))
    sg = []
    for _ in range(20):
        sy = synth(len(seq), 0.15, rnd); b0 = sc(dec(sy)); mx = 0
        cnt = {}
        for x in sy: cnt[x] = cnt.get(x, 0) + 1
        for s in LETSIGNS:
            if cnt.get(s, 0) < 5: continue
            mx = max(mx, max(sc(dec(sy, dict(KEY, **{s: c}))) - b0 for c in 'abcdefghilmnoprstuxyz' if c != KEY[s]))
        sg.append(mx)
    p95 = pct(sg, .95)
    res += [('DESC', 'synth_max_sign_gain_p95', f'{p95:.4f}'), ('DESC', 'settled_text_S', f'{base:.3f}')]
    return res, rows, sorted(gains, key=lambda g: -g[4]), p95, out_dec

def render():
    res, rows, gains, p95, out_dec = run()
    o = {}
    o['result.tsv'] = 'test\tstat\tvalue\n' + ''.join(f'{a}\t{b}\t{c}\n' for a, b, c in res)
    o['lines.tsv'] = 'line\tagr\tnA\tnB\tsA\tsB\trefA_p05\trefB_p05\tbreakA\tbreakB\tbreak_line\tdecA\tdecB\n' + ''.join(
        f'{r[0]}\t{r[1]:.3f}\t{r[2]}\t{r[3]}\t{r[4]:.3f}\t{r[5]:.3f}\t{r[6]:.3f}\t{r[7]:.3f}\t{int(r[8])}\t{int(r[9])}\t{int(r[10])}\t{r[11]}\t{r[12]}\n' for r in rows)
    o['sign_gain.tsv'] = 'sign\tvalue\tn_agreed\tbest_alt\tgain\tover_synth_p95\n' + ''.join(
        f'{g[0]}\t{g[1]}\t{g[2]}\t{g[3]}\t{g[4]:.4f}\t{int(g[4] > p95)}\n' for g in gains)
    o['decodes.txt'] = '\n'.join(out_dec) + '\n'
    return o

if __name__ == '__main__':
    o = render(); stale = False
    for fn, txt in o.items():
        p = os.path.join(H, fn)
        if '--check' in sys.argv:
            if not os.path.exists(p) or open(p).read() != txt: print('STALE', fn); stale = True
        else: open(p, 'w').write(txt)
    if '--check' in sys.argv:
        print('stale' if stale else 'up to date'); sys.exit(1 if stale else 0)
    print(o['result.tsv'])
