#!/usr/bin/env python3
"""V-BRANDT (verifier, 9 Oct 2026): re-runs BRANDT-GATE test 1/test 2 and BRANDT-UP's LCS gate at fresh seeds, and the
blind-input sensitivities: test 2 on each blind pass alone (passA49_u / passB49_u, no worker settlement, no gloss override) and
the LCS gate on each blind margin-gloss pass (glossA20u / glossB20u) and with 0021's worker-split 'eine' removed.
Writes nothing but stdout; `--check` compares stdout with v_brandt.out and exits 1 if stale. Seeds 777 and 31337, n 2000."""
import csv, random, re, sys, os, io, contextlib
H = os.path.dirname(os.path.abspath(__file__)); os.chdir(H)
sys.path.insert(0, os.path.join(H, '../../../tools'))
FOLD = str.maketrans({'ä': 'a', 'ö': 'o', 'ü': 'u', 'j': 'i', 'v': 'u', 'y': 'i'})
def fold(s): return s.strip().lower().translate(FOLD)
def rows(fn): return list(csv.DictReader((l for l in open(fn) if not l.startswith('#')), delimiter='\t'))
N = 2000
def pstats(real, c):
    c = sorted(c); return 'real %d; control mean %.2f, p99 %d, max %d, n %d; p = %.4f' % (
        real, sum(c) / len(c), c[int(.99 * len(c))], c[-1], len(c), (1 + sum(x >= real for x in c)) / (len(c) + 1)), c[int(.99 * len(c))], c[-1]
def main(out):
    # test 1, fresh seed
    import interlinear_align as ia
    pairs = ia.load_pairs('pairs_0020.tsv')
    kw = dict(floor=150, clear_consumes=True, prior=None, code_prefix=None, null_cost=-3.0, wildcard=None, max_chunk=8, seg_bonus=1.0, len_prior=0.0)
    def agrees(ps):
        prep, res, counts, shown = ia.run_align(ps, **kw)
        return sum(1 for r in ia.token_rows(prep, res, counts, shown) if r[-1] == 'agrees')
    real = agrees(pairs); rng = random.Random(777); idx = list(range(len(pairs))); d = []
    for _ in range(N):
        while True:
            p = idx[:]; rng.shuffle(p)
            if all(a != b for a, b in zip(idx, p)): break
        d.append(agrees([dict(q, plain_raw=pairs[k]['plain_raw']) for q, k in zip(pairs, p)]))
    s, p99, mx = pstats(real, d); print('T1 agrees seed 777:', s, 'gate', 'PASS' if real > mx else 'FAIL', file=out)
    # test 2
    key = {r['value']: fold(r['meaning']) for r in rows('key_0020.tsv') if len(fold(r['meaning'])) == 1}
    vals = sorted(key); lets = [key[v] for v in vals]
    def t2(data, tag, seed):
        sc = lambda k: sum(1 for v, g in data if k[v] == g)
        rng = random.Random(seed); c = []
        for _ in range(N):
            p = lets[:]; rng.shuffle(p); c.append(sc(dict(zip(vals, p))))
        s, p99, mx = pstats(sc(key), c)
        print('T2 %s seed %d: scorable %d; %s; gate %s' % (tag, seed, len(data), s, 'PASS' if sc(key) > p99 else 'FAIL'), file=out)
    rec = [(r['value'], fold(r['gloss'])) for r in rows('ciphertext_0049.tsv')]
    ok = lambda v, g: v.isdigit() and len(g) == 1 and g.isalpha() and v in key
    t2([(v, g) for v, g in rec if ok(v, g)], 'reconciled', 777)
    # undo the 46 a->d override on f49_L01 pos 1
    und = [(r['value'], 'a' if (r['line'], r['pos']) == ('f49_L01', '1') else fold(r['gloss'])) for r in rows('ciphertext_0049.tsv')]
    t2([(v, g) for v, g in und if ok(v, g)], 'reconciled, 46 override undone', 31337)
    for fn in ('passA49_u.tsv', 'passB49_u.tsv'):
        data = []
        for r in rows(fn):
            if '=' not in r['token']: continue
            v, g = r['token'].split('=', 1); g = fold(g)
            if ok(v, g): data.append((v, g))
        t2(data, 'blind %s alone' % fn, 31337)
    # BRANDT-UP LCS
    def norm(s):
        s = s.lower().replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss'); s = re.sub(r'\[\?\]', '', s)
        return re.sub(r'[^a-z]', '', s)
    C = {r['value']: r['letter'] for r in rows('values_gate.tsv') if r['grade'] == 'C'}
    grp = lambda fn: [r['token'] for r in rows(fn) if re.fullmatch(r'\d+', r['token'])]
    g20, g21 = grp('ciphertext_0020u.tsv'), grp('ciphertext_0021.tsv')
    gtxt = lambda fn: norm(''.join(l for l in open(fn) if not l.startswith('#')))
    gl21 = norm(''.join(r['gloss'] for r in rows('ciphertext_0021.tsv') if r['gloss'] not in ('', '^')))
    gl21_noeine = norm(''.join(r['gloss'] for r in rows('ciphertext_0021.tsv') if r['gloss'] not in ('', '^') and len(r['gloss']) > 1))
    def lcs(a, b):
        prev = [0] * (len(b) + 1)
        for x in a:
            cur = [0]
            for j, y in enumerate(b): cur.append(prev[j] + 1 if x == y else max(prev[j + 1], cur[j]))
            prev = cur
        return prev[-1]
    cv, cl = sorted(C), [C[v] for v in sorted(C)]
    def up(gl20, gl21, tag, seed):
        st = lambda k: lcs([k[v] for v in g20 if v in k], gl20) + lcs([k[v] for v in g21 if v in k], gl21)
        rng = random.Random(seed); c = []
        for _ in range(N):
            p = cl[:]; rng.shuffle(p); c.append(st(dict(zip(cv, p))))
        r = st(C); s, p99, mx = pstats(r, c)
        print('UP %s seed %d: %s; gate %s' % (tag, seed, s, 'PASS' if r > p99 else 'FAIL'), file=out)
    up(gtxt('gloss_0020u.txt'), gl21, 'worker gloss', 777)
    up(gtxt('gloss_0020u.txt'), gl21_noeine, 'worker gloss, 0021 without split eine', 31337)
    up(gtxt('glossA20u.txt'), gl21_noeine, 'blind glossA20u, 0021 without split eine', 31337)
    up(gtxt('glossB20u.txt'), gl21_noeine, 'blind glossB20u, 0021 without split eine', 31337)
    # head line 1 decoded by C values alone (no gloss involved)
    print('UP 0020u decoded by C values:', ''.join(C.get(v, '.') for v in g20), file=out)
buf = io.StringIO(); main(buf); txt = buf.getvalue()
if '--check' in sys.argv:
    old = open('v_brandt.out').read() if os.path.exists('v_brandt.out') else ''
    print('v_brandt --check:', 'OK' if old == txt else 'STALE'); sys.exit(0 if old == txt else 1)
sys.stdout.write(txt)
