"""D07-NOX510 (LANE DEFAULT-account-1-20261007-0042 worker, account 1, 7 Oct 2026). Pre-registered in PREREG-D07NOX510.md (same folder).
Part 1: the 14 split-pile c262 tiles bounded (bridge re-run under every whole-group and 200 random placements).
Part 2: c510-516 owner-pile stream decoded through D07-NOXT's 19-pile bridge, scored vs Dupuy 221R-226R (set-aware exact LCS ratio) with
key-permuted and order-shuffled nulls.
    python3 nox510.py score   -> results/d07nox510_summary.json, results/d07nox510_decode.tsv
    python3 nox510.py check   rule 7: recompute and compare with the committed files
"""
import collections, json, os, random, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'results')
OS = os.path.dirname(HERE)
T = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, HERE)
import bridge_ownerpiles as B  # noqa: E402
import keytie  # noqa: E402

CHILD = {'k006': ['k006-b', 'k006-c', 'k087-d'], 'k072': ['k072-b'], 'k087': ['k087-b', 'k087-c', 'k087-d']}
N = 200


def norm(s):  # scripts/test0.py's norm
    import re
    s = s.lower().replace('v', 'u').replace('j', 'i').replace('y', 'i')
    s = re.sub(r'[éèêë]', 'e', s)
    return re.sub(r'[^a-z]', '', s)


def lcs_len(a, b):
    """bit-parallel exact LCS; a: reference string, b: list of letter sets."""
    if not a or not b:
        return 0
    m = {}
    for i, c in enumerate(a):
        m[c] = m.get(c, 0) | (1 << i)
    full = (1 << len(a)) - 1; v = full
    for s in b:
        mk = 0
        for c in s:
            mk |= m.get(c, 0)
        u = v & mk
        v = ((v + u) | (v - u)) & full
    return len(a) - bin(v).count('1')


def R(dec, ref):
    return 2 * lcs_len(ref, dec) / (len(dec) + len(ref))


# ---------------- Part 1
def part1():
    tiles, rec = B.load()
    lines = sorted(rec)
    merges = json.load(open(os.path.join(OS, 'summary.json')))['merges']
    raw = {L: [t['cluster'] for t in tiles[L]] for L in lines}
    own = {L: [merges.get(c, c) for c in raw[L]] for L in lines}
    K = json.load(open(os.path.join(HERE, 'results', 'basin_keys.json')))
    Lk = [K[f'alt{i:02d}'] for i in keytie.L_IDX]
    idx = [(L, i) for L in lines for i, c in enumerate(raw[L]) if c in CHILD]

    def run(place):  # place: {(L,i): pile}
        cl = {L: list(own[L]) for L in lines}
        for (L, i), p in place.items():
            cl[L][i] = p
        b = B.bridged(B.prov_rows(B.em(tiles, rec, cl)[0]), Lk)
        return json.dumps({p: ''.join(sorted(chr(97 + x) for x in s)) for p, s in sorted(b.items())}, sort_keys=True)

    variants = collections.Counter(); runs = []
    base = run({})
    variants[base] += 1; runs.append(('all-parent', base))
    for par, kids in CHILD.items():
        for k in kids:
            pl = {(L, i): k for (L, i) in idx if raw[L][i] == par}
            v = run(pl); variants[v] += 1; runs.append((f'{par}->{k}', v))
    rng = random.Random(510)
    for _ in range(N):
        pl = {(L, i): rng.choice([raw[L][i]] + CHILD[raw[L][i]]) for (L, i) in idx}
        variants[run(pl)] += 1
    names = {v: f'V{j}' for j, v in enumerate(sorted(variants, key=lambda v: (v != base, -variants[v])))}
    return dict(n_tiles=len(idx), by_parent=dict(collections.Counter(raw[L][i] for L, i in idx)),
                base_is_d07noxt=json.loads(base) == json.load(open(os.path.join(OUT, 'd07noxt_summary.json')))['bridged_after'],
                variants={names[v]: dict(count=variants[v], bridge=json.loads(v)) for v in variants},
                whole_group=[(a, names[v]) for a, v in runs])


# ---------------- Part 2
def stream():
    lab = {}
    for r in B.tsv(os.path.join(OS, 'settled_labels.tsv')):
        if r['status'] != 'bad-cut':
            lab[r['sid']] = r['new_sign']
    out = []
    for r in B.tsv(os.path.join(T, 'run2', 'nxatl', 'sequences.tsv')):
        if r['leaf'] != 'c262' and r['tile'] in lab:
            out.append((r['tile'], lab[r['tile']]))
    return out


def reference():
    txt = ''.join(norm(ln.split('\t', 1)[1]) for ln in open(os.path.join(T, 'run2', 'nxdup', 'dupuy221_226_norm.txt'))
                  if not ln.startswith('#') and '\t' in ln)
    k = txt.index('icelleque') + len('icelleque')
    return txt[k:]


def sets_of(bridge):
    return {p: frozenset(norm(v) or v for v in vs) for p, vs in bridge.items()}


def dec_of(st, bs):
    return [(t, p, bs[p]) for t, p in st if p in bs]


def path(ref, dec):
    """LCS DP with traceback; returns list of (dec index, ref index) matches."""
    n, m = len(dec), len(ref)
    ra = np.frombuffer(ref.encode(), dtype=np.uint8)
    rows = np.zeros((n + 1, m + 1), dtype=np.int16)
    for i, s in enumerate(dec):
        mt = np.zeros(m, dtype=bool)
        for c in s:
            mt |= ra == ord(c)
        prev = rows[i]
        cur = np.maximum(prev[1:], prev[:-1] + mt)
        rows[i + 1, 1:] = np.maximum.accumulate(cur)
    i, j, out = n, m, []
    while i and j:
        if ref[j - 1] in dec[i - 1] and rows[i, j] == rows[i - 1, j - 1] + 1:
            out.append((i - 1, j - 1)); i -= 1; j -= 1
        elif rows[i - 1, j] >= rows[i, j - 1]:
            i -= 1
        else:
            j -= 1
    assert len(out) == rows[n, m]
    return out[::-1]


def runs4(pth):
    tok, cur = set(), [pth[0]] if pth else []
    for a, b in pth[1:] + [(None, None)]:
        if a is not None and a == cur[-1][0] + 1 and b == cur[-1][1] + 1:
            cur.append((a, b)); continue
        if len(cur) >= 4:
            tok |= {x for x, _ in cur}
        cur = [(a, b)]
    return tok


def score(bridge, ref, st, with_path):
    bs = sets_of(bridge)
    d = dec_of(st, bs); dec = [s for _, _, s in d]
    r = R(dec, ref)
    rng = random.Random(16142)
    ps = sorted(bs); vals = [bs[p] for p in ps]
    nk, no, nrun = [], [], []
    for _ in range(N):
        v = vals[:]; rng.shuffle(v); kb = dict(zip(ps, v))
        nk.append(R([kb[p] for _, p, _ in d], ref))
    for _ in range(N):
        s2 = dec[:]; rng.shuffle(s2); no.append(R(s2, ref))
        if with_path:
            nrun.append(len(runs4(path(ref, s2))))
    res = dict(stream_tiles=len(st), decoded_tokens=len(dec), ref_letters=len(ref), R=round(r, 5),
               k_perm=dict(mean=round(float(np.mean(nk)), 5), p99=round(float(np.percentile(nk, 99)), 5), max=round(max(nk), 5)),
               o_shuf=dict(mean=round(float(np.mean(no)), 5), p99=round(float(np.percentile(no, 99)), 5), max=round(max(no), 5)))
    res['gate'] = 'PASS' if r > max(nk) and r > max(no) else 'FAIL'
    pth = None
    if with_path:
        pth = path(ref, dec); rt = runs4(pth)
        res['lcs'] = len(pth)
        res['run4_tokens'] = len(rt)
        res['run4_o_shuf'] = dict(mean=round(float(np.mean(nrun)), 2), p99=float(np.percentile(nrun, 99)), max=max(nrun))
        res['S_licensed'] = res['gate'] == 'PASS' and len(rt) > res['run4_o_shuf']['p99']
    return res, d, pth


def compute():
    p1 = part1()
    st = stream(); ref = reference()
    base = json.load(open(os.path.join(OUT, 'd07noxt_summary.json')))['bridged_after']
    prim, d, pth = score(base, ref, st, True)
    var = {k: score(v['bridge'], ref, st, False)[0] for k, v in p1['variants'].items() if v['bridge'] != base}
    rt = runs4(pth); mp = dict(pth)
    rows = []
    for i, (t, p, s) in enumerate(d):
        j = mp.get(i)
        rows.append((t, p, ''.join(sorted(s)), ref[j] if j is not None else '-', j + 1 if j is not None else '-',
                     'S' if prim['S_licensed'] and i in rt else 'M'))
    prim['grades'] = dict(H=0, C=0, S=sum(r[5] == 'S' for r in rows), M=sum(r[5] == 'M' for r in rows), I=0)
    return dict(part1=p1, part2_primary=prim, part2_variants=var), rows


def write(res, rows):
    json.dump(res, open(os.path.join(OUT, 'd07nox510_summary.json'), 'w'), indent=1)
    with open(os.path.join(OUT, 'd07nox510_decode.tsv'), 'w') as f:
        f.write('# D07-NOX510: c510-516 tiles in bridged owner piles, letter set from key.tsv via the 19-pile bridge; ref = Dupuy letter on the\n'
                '# LCS path (scoring alignment only, not a reading). Grades per PREREG-D07NOX510.md.\n')
        f.write('tile\tpile\tletters\tdupuy_lcs\tref_pos\tgrade\n')
        for r in rows:
            f.write('\t'.join(map(str, r)) + '\n')


def main(a):
    if a[:1] == ['score']:
        res, rows = compute(); write(res, rows)
        print(json.dumps({k: v for k, v in res.items()}, indent=1)[:6000])
    elif a[:1] == ['check']:
        res, rows = compute()
        if json.loads(json.dumps(res)) != json.load(open(os.path.join(OUT, 'd07nox510_summary.json'))):
            sys.exit('d07nox510_summary.json stale')
        print('d07nox510_summary.json up to date')
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
