#!/usr/bin/env python3
"""TXE4-5 PAIR-BANK, unit 2 (12 Oct 2026, account 3): machine-only joins and pools (PREREG benchmark-tx/PREREG-txeng4-5.md R4a).

Read-free: no truth file, no owner file, no secure list, no labels.json is opened. Inputs are the atlas (signs.tsv, bitmaps.npz),
the sibling leaves' passC_agreement.tsv (the two blind passes), no.87's passA/passB benchmark outputs, and the bases being
corrected. Steps:
 1. agree/: sibling line reads (pass A's own sequence from the agreement file) and agreed positions; passage -> atlas line by
    ordinal (Lnn -> line nn; R/V -> the recto/verso page), kept only when the atlas line's box count is within [0.75, 1.5] x the
    read's token count (pairing.tsv); f139v (atlas strips span two passages), f162r (sub-lines) and f174vB's R01/V0x drop out.
    no.87's own agreement: passA vs passB per line, LCS alignment on sign equality, agreed = matched-equal positions of pass A.
 2. maps/sib_r1.tsv: box_token_align --lam 0 (width-only seed).
 3. knn/: a cosine kNN (k 7; 16x16 downsampled ink + rh rw dy) trained on sibling tiles labelled by the round-1 join at agreed
    positions (pages f152r, f178r, f178v, f179r never in training); top-3 for every atlas tile, leave-one-out on its own tiles.
 4. maps/sib_r2.tsv: box_token_align --topk knn --loo --check-labels knn top-1 --check-bound (steered -> leave-one-out check);
    FAIL lines dropped and re-checked once. maps/sib_pool.tsv: positions identical in rounds 1 and 2, op 1:1, on PASS lines.
 5. maps/no87_passA.tsv, no87_labels.tsv, f152r_passA.tsv, f152r_passZ.tsv: the same recipe with --read the base.
 6. maps/SHIFT-CHECKS.md: every join's rows and verdict, to paste into the PREREG addendum and RESULTS.
Usage (repo root): python3 benchmark-tx/txeng4/5/build_maps.py
"""
import csv, json, os, subprocess, sys, collections
import numpy as np

R = os.getcwd()
C = 'ciphers/nevers-birago-fr3251-1572'; H = f'{C}/harvest'; AT = f'{C}/atlas'
O = 'benchmark-tx/txeng4/5'
for d in ('agree', 'maps', 'knn'):
    os.makedirs(f'{O}/{d}', exist_ok=True)
BTA = [sys.executable, 'tools/box_token_align.py', '--signs', f'{AT}/signs.tsv']
NO87 = {'f178r', 'f178v', 'f179r'}; NEVER_TRAIN = NO87 | {'f152r'}
SIB = ['f139v', 'f144r', 'f162r', 'f168', 'f174r', 'f174v', 'f174vB', 'f175v', 'f184r']
# R4a drop-and-recheck-once: lines whose steered (leave-one-out) join check FAILed B1 on the first build (01:37 UTC, sidecars of
# that run kept as maps/first_build/): f139v_L03 (atlas f139v lines are strips of two passages), every f174vB_L (the harvest
# f174vB passages do not sit on atlas f174vB's lines by ordinal; probe/ tests the +1 offset), f184r_L09 (22 tokens vs 32 boxes).
DROP_LINES = {'f139v_L03', 'f184r_L09'} | {f'f174vB_L{n:02d}' for n in range(1, 12)}
F174VB_OFFSET = int(os.environ.get('F174VB_OFFSET', '0'))   # set to 1 if probe/f174vB_shift1 PASSes (declared in the addendum)


def rd(p):
    return list(csv.DictReader(open(p), delimiter='\t'))


def wr(p, cols, rows):
    with open(p, 'w') as f:
        f.write('\t'.join(cols) + '\n' + ''.join('\t'.join(str(r[c]) for c in cols) + '\n' for r in rows))


# ---- 1. agreement -> reads
atlas = rd(f'{AT}/signs.tsv')
nbox = collections.Counter((r['page'], int(r['line'])) for r in atlas)
pairing, sib_read, sib_agree = [], [], []
for leaf in SIB:
    rows = rd(f'{H}/{leaf}/passC_agreement.tsv')
    byp = collections.defaultdict(list)
    for r in rows:
        if r['posA']:
            byp[r['passage']].append(r)
    for pas, rs in byp.items():
        m = pas[0]; rest = pas[1:]
        if not rest.isdigit():
            pairing.append(dict(leaf=leaf, passage=pas, page='', line='', tokens=len(rs), boxes='', kept='no:sub-line')); continue
        n = int(rest)
        page = {'L': leaf, 'R': leaf + 'r', 'V': leaf + 'v'}[m] if m in 'RV' else leaf
        if m == 'L' and (leaf.endswith('r') or leaf.endswith('v') or leaf.endswith('B')):
            page = leaf
        elif m == 'L':
            pairing.append(dict(leaf=leaf, passage=pas, page='', line='', tokens=len(rs), boxes='', kept='no:no-page')); continue
        b = nbox.get((page, n), 0)
        ok = b and 0.75 * len(rs) <= b <= 1.5 * len(rs)
        pairing.append(dict(leaf=leaf, passage=pas, page=page, line=n, tokens=len(rs), boxes=b, kept='yes' if ok else 'no:count'))
        if not ok:
            continue
        ln = f'{page}_L{n:02d}'
        if ln in DROP_LINES and not (leaf == 'f174vB' and F174VB_OFFSET):
            pairing[-1]['kept'] = 'no:steered-check-FAIL'; continue
        if leaf == 'f174vB' and F174VB_OFFSET:
            ln = f'{page}_L{n + F174VB_OFFSET:02d}'; pairing[-1]['line'] = n + F174VB_OFFSET
        rs = sorted(rs, key=lambda r: int(r['posA']))
        for i, r in enumerate(rs, 1):
            sib_read.append(dict(line=ln, pos=i, sign=r['idA']))
            if r['status'] == 'agree' and r['idA'] == r['idB']:
                sib_agree.append(dict(line=ln, pos=i, sign=r['idA']))
wr(f'{O}/agree/pairing.tsv', ['leaf', 'passage', 'page', 'line', 'tokens', 'boxes', 'kept'], pairing)
wr(f'{O}/agree/sib_read.tsv', ['line', 'pos', 'sign'], sib_read)
wr(f'{O}/agree/sib_agree.tsv', ['line', 'pos', 'sign'], sib_agree)
print(f'sibling lines kept {sum(1 for p in pairing if p["kept"] == "yes")} of {len(pairing)}; tokens {len(sib_read)}, agreed {len(sib_agree)}')


def lcs_agree(a, b):
    n, m = len(a), len(b)
    S = np.zeros((n + 1, m + 1), int)
    for i in range(n):
        for j in range(m):
            S[i + 1, j + 1] = max(S[i, j] + (a[i] == b[j]), S[i, j + 1], S[i + 1, j])
    out, i, j = [], n, m
    while i and j:
        if a[i - 1] == b[j - 1] and S[i, j] == S[i - 1, j - 1] + 1:
            out.append(i); i -= 1; j -= 1
        elif S[i - 1, j] >= S[i, j - 1]:
            i -= 1
        else:
            j -= 1
    return set(out)


def load_lines(p):
    d = collections.defaultdict(list)
    for r in rd(p):
        d[r['line']].append(r['sign'])
    return d


A87, B87 = load_lines('benchmark-tx/outputs/birago1572-no87/passA.tsv'), load_lines('benchmark-tx/outputs/birago1572-no87/passB.tsv')
no87_agree = []
for ln, a in A87.items():
    ag = lcs_agree(a, B87.get(ln, []))
    for i, s in enumerate(a, 1):
        if i in ag:
            no87_agree.append(dict(line=ln, pos=i, sign=s))
wr(f'{O}/agree/no87_agree.tsv', ['line', 'pos', 'sign'], no87_agree)
print(f'no.87 pass A tokens {sum(len(v) for v in A87.values())}, A/B-agreed {len(no87_agree)}')


# ---- 2. round 1
def bta(read, out, extra=(), signs=None):
    cmd = list(BTA); cmd[3] = signs or cmd[3]
    r = subprocess.run(cmd + ['--read', read, '--out', out] + list(extra), capture_output=True, text=True)
    sys.stdout.write(r.stdout[-3000:])
    if r.returncode not in (0, 2, 3):
        sys.exit(r.stderr)
    return r.returncode


bta(f'{O}/agree/sib_read.tsv', f'{O}/maps/sib_r1.tsv', ['--lam', '0', '--no-loo'])
r1 = {(r['line'], r['pos']): r['sid'] for r in rd(f'{O}/maps/sib_r1.tsv') if r['op'] == '1:1'}

# ---- 3. kNN
idx = {r['sid']: i for i, r in enumerate(atlas)}
bm = np.load(f'{AT}/bitmaps.npz')['signs']
def feat(i):
    s = (bm[i] > 64).astype(np.float32).reshape(16, 3, 16, 3).mean(axis=(1, 3)).ravel()
    r = atlas[i]
    return np.concatenate([s, [float(r['rh']), float(r['rw']), float(r['dy'])]])
F = np.stack([feat(i) for i in range(len(atlas))]); F /= (np.linalg.norm(F, axis=1, keepdims=True) + 1e-9)
train = [(idx[r1[(r['line'], str(r['pos']))]], r['sign']) for r in sib_agree if (r['line'], str(r['pos'])) in r1
         and atlas[idx[r1[(r['line'], str(r['pos']))]]]['page'] not in NEVER_TRAIN]
ti = np.array([t[0] for t in train]); tl = np.array([t[1] for t in train])
print(f'kNN training tiles {len(ti)} on pages {sorted(set(atlas[i]["page"] for i in ti))}')
S = F @ F[ti].T
topk, top1 = [], []
K = 7
for i in range(len(atlas)):
    s = S[i].copy()
    s[ti == i] = -9  # leave-one-out
    nb = np.argsort(-s)[:K]
    votes = collections.Counter()
    for j in nb:
        votes[tl[j]] += 1 + s[j]
    best = [c for c, _ in votes.most_common(3)]
    sid = atlas[i]['sid']
    topk.append(dict(box=sid, k1=best[0], k2=best[1] if len(best) > 1 else '_', k3=best[2] if len(best) > 2 else '_'))
    top1.append(dict(sid=sid, label=best[0]))
wr(f'{O}/knn/knn_topk.tsv', ['box', 'k1', 'k2', 'k3'], topk)
wr(f'{O}/knn/knn_top1.tsv', ['sid', 'label'], top1)
loo_acc = np.mean([top1[i]['label'] == l for i, l in zip(ti, tl)])
print(f'kNN leave-one-out top-1 agreement with its own training labels {loo_acc:.3f} (n {len(ti)})')

# ---- 4. round 2 and pools; 5. the base maps
checks = ['# Shift checks (tools/join_check.py via box_token_align.py --check-bound; steered -> leave-one-out row)\n']
def r2(read, out, extra=(), signs=None):
    rc = bta(read, out, ['--topk', f'{O}/knn/knn_topk.tsv', '--check-labels', f'{O}/knn/knn_top1.tsv', '--check-bound'] + list(extra), signs)
    # the check labels steered the map (same kNN as --topk), so the honest row is leave-one-out: rewrite the sidecar --steered
    r = subprocess.run([sys.executable, 'tools/join_check.py', '--map', out, '--check-labels', f'{O}/knn/knn_top1.tsv', '--read', read, '--steered'], capture_output=True, text=True)
    sys.stdout.write('\n'.join(l for l in r.stdout.split('\n') if not l.startswith('  '))[-600:] + '\n')
    sc = json.load(open(out + '.joincheck.json'))
    v = sc['verdict']
    checks.append(f'\n## {out}: {v} (n {sc["n"]}, share0 {sc["share0"]:.3f}, share+-1 {sc["sharepm1"]:.3f}, null p95_0 {sc["p95_0"]:.3f}, p95_pm1 {sc["p95_pm1"]:.3f})\n')
    bad = []
    for ln, d in sorted(sc['lines'].items()):
        c = d['counts']
        checks.append(f'  {ln}: placed {d["placed"]} 0/-1/+1/none {c.get("0",0)}/{c.get("-1",0)}/{c.get("1",c.get("+1",0))}/{c.get("none",0)} {d["verdict"]}\n')
        if d['verdict'] == 'fail':
            bad.append(ln)
    return v, bad, rc

def r2_with_drop(read, out, extra=(), signs=None):
    v, bad, rc = r2(read, out, extra, signs)
    if v == 'FAIL' and bad:
        rows = [r for r in rd(read) if r['line'] not in bad]
        read2 = out.replace('.tsv', '_read_dropped.tsv'); wr(read2, ['line', 'pos', 'sign'], rows)
        checks.append(f'  -> dropped FAIL lines {bad}; re-check once\n')
        v, bad2, rc = r2(read2, out, extra, signs)
        bad = bad + bad2
    return v, bad

v, bad = r2_with_drop(f'{O}/agree/sib_read.tsv', f'{O}/maps/sib_r2.tsv')
r2m = {(r['line'], r['pos']): r['sid'] for r in rd(f'{O}/maps/sib_r2.tsv') if r['op'] == '1:1'}
pool = []
if v == 'PASS':
    for r in rd(f'{O}/agree/sib_agree.tsv'):
        k = (r['line'], r['pos'])
        if r['line'] not in bad and r1.get(k) and r1.get(k) == r2m.get(k):
            pool.append(dict(sid=r1[k], page=atlas[idx[r1[k]]]['page'], line=r['line'], pos=r['pos'], op='1:1', sign=r['sign']))
wr(f'{O}/maps/sib_pool_map.tsv', ['sid', 'page', 'line', 'pos', 'op', 'sign'], pool)
wr(f'{O}/agree/sib_pool_agree.tsv', ['line', 'pos', 'sign'], pool)
print(f'sibling round-2 verdict {v}; stable agreed pool tiles {len(pool)} of {len(sib_agree)} agreed')
# the pool map carries the sidecar of sib_r2 verbatim is not valid (different sha); re-check the stable subset itself
rows = [r for r in rd(f'{O}/agree/sib_read.tsv') if r['line'] in {p['line'] for p in pool}]
wr(f'{O}/agree/sib_pool_read.tsv', ['line', 'pos', 'sign'], rows)
v3, bad3, rc = r2(f'{O}/agree/sib_pool_read.tsv', f'{O}/maps/sib_pool_map.tsv')
# NB: the --lines rerun regenerates the map for the pool lines; stable filter re-applied below
m3 = {(r['line'], r['pos']): r['sid'] for r in rd(f'{O}/maps/sib_pool_map.tsv') if r['op'] == '1:1'}
pool = [p for p in pool if m3.get((p['line'], str(p['pos']))) == p['sid']]
sc = json.load(open(f'{O}/maps/sib_pool_map.tsv.joincheck.json'))
checks.append(f'\n## maps/sib_pool_map.tsv (pool lines only): {sc["verdict"]} (n {sc["n"]}, share0 {sc["share0"]:.3f})\n')
wr(f'{O}/agree/sib_pool_agree.tsv', ['line', 'pos', 'sign'], pool)
print(f'pool tiles after the pool-map re-check {len(pool)}')

for name, read in [('no87_passA', 'benchmark-tx/outputs/birago1572-no87/passA.tsv'), ('no87_labels', 'benchmark-tx/outputs/birago1572-no87/labels.tsv')]:
    v, bad = r2_with_drop(read, f'{O}/maps/{name}.tsv')
    print(f'{name}: {v}, failed lines {bad}')
# f152r: benchmark-tx/txeng3/7/map_f152r.py (the SCRIPT, not its forbidden map file) records that atlas page f152r lines 2-5 are the
# letter lines L01-L04 and that prose boxes outside the cipher run are cut by x: L01 keeps cx > 2520, L04 keeps cx < 2460. Scratch
# signs.tsv with those boxes removed and lines 2-5 renumbered 1-4, so the read's line names resolve; geometry only, no label.
XB = {2: lambda cx: cx > 2520, 5: lambda cx: cx < 2460}
srows = []
for r in atlas:
    if r['page'] != 'f152r':
        srows.append(dict(r)); continue
    li = int(r['line'])
    if li < 2 or not XB.get(li, lambda cx: True)(int(r['x']) + int(r['w']) / 2):
        continue
    q = dict(r); q['line'] = str(li - 1); srows.append(q)
wr(f'{O}/maps/signs_f152r_run.tsv', list(atlas[0].keys()), srows)
checks.append('\n## f152r: scratch signs (atlas lines 2-5 -> L01-L04, prose boxes outside the run removed by x, per txeng3/7/map_f152r.py)\n')
for name, read in [('f152r_passA', 'benchmark-tx/outputs/birago1572-f152r/passA.tsv'), ('f152r_passZ', 'benchmark-tx/outputs/birago1572-f152r/passZ_pipeline.tsv')]:
    v, bad = r2_with_drop(read, f'{O}/maps/{name}.tsv', signs=f'{O}/maps/signs_f152r_run.tsv')
    print(f'{name}: {v}, failed lines {bad}')
open(f'{O}/maps/SHIFT-CHECKS.md', 'w').write(''.join(checks))
print('wrote', f'{O}/maps/SHIFT-CHECKS.md')
