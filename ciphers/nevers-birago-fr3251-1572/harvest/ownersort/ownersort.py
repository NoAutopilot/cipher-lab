#!/usr/bin/env python3
"""BIR-OWNERSORT (4 Oct 2026): the owner's complete sign sort folded in as a third reader, per PREREG.md beside this file.
Run from the repo root: python3 ciphers/nevers-birago-fr3251-1572/harvest/ownersort/ownersort.py [--check]
Steps: (1) three_reader.tsv + agreement_by_sign.tsv; (2) power control, then the split test per new pile -> splits.tsv, power.tsv;
(3) owner changes vs base with the BIR-OWNER random-change control -> changes.tsv, score.json, and, on leaves that pass,
exceptions_ownersort_<leaf>.tsv + decode_ownersort.json; (4) recut.tsv (aside / bad-cut tiles). Disk only.
Tile -> position mapping is BIR-OWNER's rule (harvest/tx_decode/eye/open/sorter/score_owner.py), copied, not changed."""
import csv, json, os, random, sys, difflib
from collections import defaultdict, Counter
from multiprocessing import Pool
sys.path.insert(0, 'tools')
import judge_plaintext as jp
H = os.path.dirname(os.path.abspath(__file__))
N = 'ciphers/nevers-birago-fr3251-1572'; E = N + '/harvest/tx_decode/eye'; S3252 = 'ciphers/birago-fr3252-1571-72'
SEED = 20261004; NCTL = 200; NPOW = 50; KS = (1, 2, 3, 5)
def tsv(p): return list(csv.DictReader(open(p), delimiter='\t'))
key = {r['sign']: r['value'] for r in tsv(N + '/harvest/key_1572_sheet.tsv')}
VALUES = sorted(set(key.values()))
LEAF = {'f117': dict(tx=E + '/verify/ciphertext_f117_top1.tsv', tok=E + '/apply/reading_f117_apply_tokens.tsv', spec='specs/birago-fr3252-f117.json',
                     exc=E + '/apply/exceptions_apply_f117.tsv', pa=S3252 + '/harvest/f117/passA.tsv', pb=S3252 + '/harvest/f117/passB.tsv'),
        'f168': dict(tx=E + '/verify/ciphertext_f168_top1.tsv', tok=E + '/apply/reading_f168_apply_tokens.tsv', spec='specs/nevers-birago-fr3251-1572.json',
                     exc=E + '/apply/exceptions_apply_f168.tsv', pa=N + '/harvest/f168/passA.tsv', pb=N + '/harvest/f168/passB.tsv'),
        'f144r': dict(tx=N + '/harvest/ciphertext_f144r.tsv', tok=E + '/open/reading_f144r_open_tokens.tsv', spec='specs/nevers-birago-fr3251-1572.json',
                      exc=E + '/open/exceptions_open144.tsv', pa=N + '/harvest/f144r/passA.tsv', pb=N + '/harvest/f144r/passB.tsv')}
COMMITTED = {'f117': E + '/apply/reading_f117_apply_tokens.tsv', 'f168': E + '/apply/reading_f168_apply_tokens.tsv',
             'f144r': E + '/open/sorter/reading_f144r_owner_tokens.tsv'}
settled = {r['sid']: r for r in tsv(N + '/sorter/owner-sort-2026-10-04/settled_labels.tsv')}
def fam(p): return p.rsplit('-', 1)[0] if p and '-' in p and len(p.rsplit('-', 1)[1]) == 1 else p

def align(a, b):
    """indices i of a -> j of b: identity when equal length, else difflib (BIR-OWNER rule)."""
    if len(a) == len(b): return {k: k for k in range(len(a))}
    m = {}
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag == 'equal' or tag == 'replace':
            for k in range(min(i2 - i1, j2 - j1)): m[i1 + k] = j1 + k
    return m

# ---- tile -> position (BIR-OWNER rule) and reader A/B per position
tiles = defaultdict(list)
for sid in settled:
    ln, i = sid.rsplit('_', 1); tiles[ln].append((int(i), sid))
sid2pos = {}; reader = {}
for leaf, c in LEAF.items():
    tx = defaultdict(list)
    for r in tsv(c['tx']): tx[r['line']].append((int(r['pos']), r['sign']))
    for which in ('pa', 'pb'):
        pp = defaultdict(list)
        for r in tsv(c[which]): pp[leaf + '_' + r['passage']].append((int(r['pos']), r['sign_id']))
        for ln, t in tx.items():
            t.sort(); p = sorted(pp.get(ln, []))
            for i, j in align([s for _, s in p], [s for _, s in t]).items():
                reader[(leaf, ln.split('_', 1)[1], t[j][0], which)] = p[i][1]
    for ln, t in tx.items():
        t.sort(); l = sorted(tiles.get(ln, []))
        for i, j in align([settled[s]['old_sign'] for _, s in l], [s for _, s in t]).items():
            sid2pos[l[i][1]] = (leaf, ln.split('_', 1)[1], t[j][0])

base = {lf: {(r['line'], int(r['pos'])): r for r in tsv(c['tok'])} for lf, c in LEAF.items()}
ORDER = {lf: sorted(base[lf]) for lf in LEAF}
ORDER = {lf: sorted(base[lf], key=lambda k: (k[0], k[1])) for lf in LEAF}
models = {}
for lf, c in LEAF.items():
    j = json.load(open(c['spec']))['judge']; jp._ALPHA = None
    models[lf] = jp.NgramModel([jp.read_corpus(p) for p in (j.get('corpora') or jp.LANG_CORPORA[j['language']])])
def letters(vals): return ''.join(v for v in vals if v not in ('?', 'NULL', '')).lower()
def text(lf, over): return letters(over.get(k, base[lf][k]['value']) for k in ORDER[lf])
def tot(lf, over):
    t = text(lf, over); return models[lf].score(t) * len(t)

def step1():
    rows = []
    for sid, s in sorted(settled.items()):
        p = sid2pos.get(sid)
        if not p: rows.append(dict(sid=sid, leaf='', line='', pos='', tx_sign='', A='', B='', owner_start=s['old_sign'], owner_pile=s['new_sign'],
                                   owner_family=fam(s['new_sign']), status=s['status'])); continue
        lf, ln, pos = p
        rows.append(dict(sid=sid, leaf=lf, line=ln, pos=pos, tx_sign=base[lf][(ln, pos)]['sign'], A=reader.get((lf, ln, pos, 'pa'), ''),
                         B=reader.get((lf, ln, pos, 'pb'), ''), owner_start=s['old_sign'], owner_pile=s['new_sign'],
                         owner_family=fam(s['new_sign']) if s['status'] in ('kept', 'moved') else '', status=s['status']))
    cols = list(rows[0])
    with open(H + '/three_reader.tsv', 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows: f.write('\t'.join(str(r[c]) for c in cols) + '\n')
    agg = defaultdict(Counter)
    for r in rows:
        if not r['leaf'] or not r['owner_family']: continue
        g = agg[r['tx_sign']]; g['n'] += 1; o = r['owner_family']
        g['A=B'] += r['A'] == r['B']; g['A=O'] += r['A'] == o; g['B=O'] += r['B'] == o; g['all3'] += r['A'] == r['B'] == o
        g['O=tx'] += o == r['tx_sign']
    with open(H + '/agreement_by_sign.tsv', 'w') as f:
        f.write('tx_sign\tn\tA=B\tA=owner\tB=owner\tall_three\towner=tx\n')
        T = Counter()
        for sg in sorted(agg, key=lambda x: -agg[x]['n']):
            g = agg[sg]; T.update(g)
            f.write(f"{sg}\t{g['n']}\t{g['A=B']}\t{g['A=O']}\t{g['B=O']}\t{g['all3']}\t{g['O=tx']}\n")
        f.write(f"ALL\t{T['n']}\t{T['A=B']}\t{T['A=O']}\t{T['B=O']}\t{T['all3']}\t{T['O=tx']}\n")
    return rows, T

def G(P, xval, fixed):
    """best gain from one free value on positions P (list of (leaf,(line,pos))) vs xval; fixed = base overrides."""
    by = defaultdict(list)
    for lf, k in P: by[lf].append(k)
    def S(v):
        o = {lf: dict(fixed.get(lf, {})) for lf in by}
        for lf, ks in by.items():
            for k in ks: o[lf][k] = v
        return sum(tot(lf, o[lf]) for lf in by)
    s0 = S(xval); best = max(VALUES, key=S)
    return S(best) - s0, best

def ctl_job(args):
    union, k, xval, fixed, seed = args
    rnd = random.Random(seed); return [G(rnd.sample(union, k), xval, fixed)[0] for _ in range(NCTL)]

def test_one(P, union, xval, fixed, seed):
    g, best = G(P, xval, fixed); c = sorted(ctl_job((union, len(P), xval, fixed, seed)))
    return g, best, jp.pct(c, 0.95), bool(g > jp.pct(c, 0.95) and g > 0)

def pos_of(sids): return [(sid2pos[s][0], sid2pos[s][1:]) for s in sids if s in sid2pos]

def power_job(args):
    k, i, Y, Z, TY, TZ = args
    rnd = random.Random(SEED * 100 + k * 1000 + i)
    P = rnd.sample(TZ, k); fixed = defaultdict(dict)
    for lf, kk in TY + TZ: fixed[lf][kk] = key[Y]
    return test_one(P, TY + TZ, key[Y], fixed, SEED + k * 7919 + i)[3]

def step2():
    final = defaultdict(list)
    for sid, s in settled.items():
        if s['status'] in ('kept', 'moved') and sid in sid2pos: final[s['new_sign']].append(sid)
    # power control first
    sheet = [p for p in final if p in key and len(final[p]) >= 3]
    pairs = [(y, z) for y in sheet for z in sheet if y != z and key[y] != key[z] and len(z) >= 1]
    rnd = random.Random(SEED); jobs = []
    for k in KS:
        ok = [(y, z) for y, z in pairs if len(final[z]) > k]
        for i in range(NPOW):
            y, z = rnd.choice(ok); jobs.append((k, i, y, z, pos_of(final[y]), pos_of(final[z])))
    with Pool(4) as pool: res = pool.map(power_job, jobs)
    power = {k: sum(r for (kk, *_), r in zip(jobs, res) if kk == k) / NPOW for k in KS}
    with open(H + '/power.tsv', 'w') as f:
        f.write('k\tpasses_of_50\tpower\n')
        for k in KS: f.write(f'{k}\t{round(power[k] * NPOW)}\t{power[k]:.2f}\n')
    def pw(n): return power[max([k for k in KS if k <= n] or [1])]
    out = []; args = []
    for P in sorted(final):
        X = fam(P)
        if P == X: continue
        n = len(final[P]); srcs = Counter(settled[s]['old_sign'] for s in final[P])
        leaves = Counter(sid2pos[s][0] for s in final[P] if s in sid2pos)
        row = dict(pile=P, family=X, n=n, from_piles=' '.join(f'{a}:{b}' for a, b in srcs.most_common()),
                   leaves=' '.join(f'{a}:{b}' for a, b in leaves.most_common()), G='', best_value='', ctl_p95='', power=f'{pw(n):.2f}', verdict='')
        if X not in key or not final.get(X):
            row['verdict'] = 'owner-only (off-sheet family, untestable by the key)' if X not in key else 'owner-only (no tiles left in parent pile)'
            out.append(row); continue
        args.append((row, pos_of(final[P]), pos_of(final[P]) + pos_of(final[X]), key[X]))
        out.append(row)
    with Pool(4) as pool:
        res = pool.starmap(test_one, [(p, u, xv, {}, SEED + i) for i, (_, p, u, xv) in enumerate(args)])
    for (row, *_), (g, best, p95, ok) in zip(args, res):
        row.update(G=f'{g:.3f}', best_value=best, ctl_p95=f'{p95:.3f}')
        row['verdict'] = ('SUPPORTED (distinct; tiles U, best value a proposal only)' if ok else
                          ('merge supported (not distinct; takes key[family])' if float(row['power']) >= 0.5 else
                           'untestable at this N (owner-only distinction, flagged; takes key[family] at M)'))
    cols = list(out[0])
    with open(H + '/splits.tsv', 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for r in out: f.write('\t'.join(str(r[c]) for c in cols) + '\n')
    return out, power

def step3(splits):
    verdict = {r['pile']: r['verdict'] for r in splits}
    inst = defaultdict(dict)  # blind instruments, as BIR-OWNER
    va = {}
    for lf in LEAF:
        for r in tsv(E + f'/verify/vanswers_{lf}.tsv'): va[r['qid']] = r['answer']
    for r in tsv(E + '/verify/vpositions.tsv'):
        a = va.get(r['qid'])
        if a in ('A', 'B'): inst[(r['leaf'], r['passage'], int(r['pos']))]['VERIFY'] = r[a]
    oa = {}
    for p in ('f117a', 'f117b', 'f168', 'f144r'):
        for r in tsv(E + f'/open/oanswers_{p}.tsv'): oa[r['qid']] = r['answer']
    for f, name in ((E + '/open/opositions.tsv', 'OPEN'), (E + '/open/opositions_f144r.tsv', 'OPEN144')):
        for r in tsv(f):
            if oa.get(r['qid']): inst[(r['leaf'], r['passage'], int(r['pos']))][name] = oa[r['qid']]
    changes = defaultdict(list); rows = []
    for sid, s in sorted(settled.items()):
        if s['status'] != 'moved' or sid not in sid2pos: continue  # PREREG: kept / aside / bad-cut = no change
        lf, ln, pos = sid2pos[sid]; b = base[lf][(ln, pos)]; P = s['new_sign']; X = fam(P)
        if P != X and verdict.get(P, '').startswith('SUPPORTED'): v = '?'
        else: v = key.get(X, '?')
        if v == b['value']: continue
        ins = inst.get((lf, ln, pos), {})
        agree = any(ins.get(k) == X for k in ('VERIFY', 'OPEN', 'OPEN144'))
        g = 'U' if v == '?' else ('S' if agree else 'M')
        r = dict(sid=sid, leaf=lf, line=ln, pos=pos, tx_sign=b['sign'], base_value=b['value'], status=s['status'], owner_pile=P, owner_value=v,
                 grade=g, blind=' '.join(f'{k}={x}' for k, x in sorted(ins.items())))
        rows.append(r); changes[lf].append(r)
    topk = {}
    for lf in LEAF:
        d = defaultdict(list)
        for r in tsv(E + f'/open/olat_{lf}_topk.tsv'): d[(r['line'], int(r['pos']))].append(r['cand'])
        topk[lf] = d
    rnd = random.Random(SEED); out = {}; pa = pb = 0.0; na = nb = 0; pc = [0.0] * NCTL
    for lf in LEAF:
        m = models[lf]; ch = changes[lf]
        ta = text(lf, {}); tb = text(lf, {(r['line'], r['pos']): r['owner_value'] for r in ch})
        sa, sb = m.score(ta), m.score(tb)
        nv = sum(r['owner_value'] != '?' for r in ch); nu = len(ch) - nv
        cand = [k for k, cs in topk[lf].items() if k in base[lf] and any(key.get(x, '?') != base[lf][k]['value'] for x in cs if x != base[lf][k]['sign'])]
        allk = [k for k in base[lf] if base[lf][k]['value'] not in ('?', '')]
        cs_ = []
        for d in range(NCTL):
            over = {}
            for k in rnd.sample(cand, min(nv, len(cand))):
                alts = [x for x in topk[lf][k] if x != base[lf][k]['sign'] and key.get(x, '?') != base[lf][k]['value']]
                over[k] = key.get(rnd.choice(alts), '?')
            rest = [k for k in allk if k not in over]
            for k in rnd.sample(rest, min(nu, len(rest))): over[k] = '?'
            t = text(lf, over); sc = m.score(t); cs_.append(sc); pc[d] += sc * len(t)
        srt = sorted(cs_); p95 = jp.pct(srt, 0.95)
        real, null, _ = m.controls(max(len(tb), 20))
        out[lf] = dict(changes=len(ch), value_changes=nv, u=nu, S=sum(r['grade'] == 'S' for r in ch), M=sum(r['grade'] == 'M' for r in ch),
                       a=round(sa, 4), b=round(sb, 4), c_p95=round(p95, 4), c_median=round(jp.pct(srt, 0.5), 4), b_rank=sum(x >= sb for x in cs_) + 1,
                       N_a=len(ta), N_b=len(tb), real_p05=round(jp.pct(real, 0.05), 3), null_p99=round(jp.pct(null, 0.99), 3), PASS=bool(sb > sa and sb > p95))
        pa += sa * len(ta); na += len(ta); pb += sb * len(tb); nb += len(tb)
        open(H + f'/text_a_{lf}.txt', 'w').write(ta + '\n'); open(H + f'/text_b_{lf}.txt', 'w').write(tb + '\n')
    pcs = sorted(x / nb for x in pc)
    out['pooled'] = dict(a=round(pa / na, 4), b=round(pb / nb, 4), c_p95=round(jp.pct(pcs, 0.95), 4), PASS=bool(pb / nb > pa / na and pb / nb > jp.pct(pcs, 0.95)))
    cols = list(rows[0])
    with open(H + '/changes.tsv', 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows: f.write('\t'.join(str(r[c]) for c in cols) + '\n')
    return out, changes

RECUT = {'f117': 'tools/iiif_lines.py --ark ark:/12148/btv1b9060232m --canvas 118 --region 4380,1400,3150,1300',
         'f144r': 'tools/iiif_lines.py --ark ark:/12148/btv1b9060248g --canvas 146 --region 4350,800,3650,760',
         'f168R': 'tools/iiif_lines.py --ark ark:/12148/btv1b9060248g --canvas 171 --region <R-line band, as sorter/pages>',
         'f168V': 'tools/iiif_lines.py --ark ark:/12148/btv1b9060248g --canvas 172 --region <V-line band, as sorter/pages>'}
def step4():
    with open(H + '/recut.tsv', 'w') as f:
        f.write('sid\tstatus\tleaf\tline\tpos\ttx_sign\tA\tB\tcommand\n')
        for sid, s in sorted(settled.items()):
            if s['status'] not in ('aside', 'bad-cut'): continue
            lf, ln, pos = sid2pos.get(sid, ('', '', ''))
            tsg = base[lf][(ln, pos)]['sign'] if lf else ''
            f.write(f"{sid}\t{s['status']}\t{lf}\t{ln}\t{pos}\t{tsg}\t{reader.get((lf, ln, pos, 'pa'), '')}\t{reader.get((lf, ln, pos, 'pb'), '')}\t"
                    f"{RECUT.get(lf if lf != 'f168' else lf + ln[0], '')} --out <scratch> --debug (native recut; line {ln} pos {pos})\n")

if __name__ == '__main__':
    rows, T = step1(); print('step1', dict(T))
    splits, power = step2(); print('power', power)
    print('verdicts', Counter(r['verdict'].split(' (')[0] for r in splits))
    score, changes = step3(splits); print(json.dumps(score, indent=1))
    step4()
    json.dump(dict(agreement=dict(T), power=power, verdicts=dict(Counter(r['verdict'].split(' (')[0] for r in splits)), score=score),
              open(H + '/score.json', 'w'), indent=1)
