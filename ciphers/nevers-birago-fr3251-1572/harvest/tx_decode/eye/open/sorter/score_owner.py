#!/usr/bin/env python3
"""BIR-OWNER (3 Oct 2026): score the owner's partial sorter picks against the base readings, per PREREG-OWNER.md.
Run from the repo root: python3 ciphers/nevers-birago-fr3251-1572/harvest/tx_decode/eye/open/sorter/score_owner.py
Writes owner_positions.tsv and owner_score.json beside this file."""
import csv, json, os, random, sys, difflib
from collections import defaultdict
sys.path.insert(0, 'tools')
import judge_plaintext as jp
H = os.path.dirname(os.path.abspath(__file__))
N = 'ciphers/nevers-birago-fr3251-1572'; E = N + '/harvest/tx_decode/eye'
def tsv(p): return list(csv.DictReader(open(p), delimiter='\t'))
key = {r['sign']: r['value'] for r in tsv(N + '/harvest/key_1572_sheet.tsv')}
LEAF = {'f117': dict(tx=E + '/verify/ciphertext_f117_top1.tsv', tok=E + '/apply/reading_f117_apply_tokens.tsv', spec='specs/birago-fr3252-f117.json'),
        'f168': dict(tx=E + '/verify/ciphertext_f168_top1.tsv', tok=E + '/apply/reading_f168_apply_tokens.tsv', spec='specs/nevers-birago-fr3251-1572.json'),
        'f144r': dict(tx=N + '/harvest/ciphertext_f144r.tsv', tok=E + '/open/reading_f144r_open_tokens.tsv', spec='specs/nevers-birago-fr3251-1572.json')}
settled = {r['sid']: r for r in tsv(H + '/owner_settled.tsv')}
# tile -> (leaf, line, pos)
tiles = defaultdict(list)
for sid in settled:
    ln, i = sid.rsplit('_', 1); tiles[ln].append((int(i), sid))
sid2pos = {}
for leaf, c in LEAF.items():
    tx = defaultdict(list)
    for r in tsv(c['tx']): tx[r['line']].append((int(r['pos']), r['sign']))
    for ln, t in tx.items():
        t.sort(); l = sorted(tiles.get(ln, []))
        a = [settled[s]['old_sign'] for _, s in l]; b = [s for _, s in t]
        if len(a) == len(b):  # equal counts: tile i is position i (labels may differ where the transcription changed)
            for k in range(len(a)): sid2pos[l[k][1]] = (leaf, ln.split('_', 1)[1], t[k][0])
            continue
        for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
            if tag == 'equal' or (tag == 'replace' and i2 - i1 == j2 - j1):
                for k in range(i2 - i1):
                    sid2pos[l[i1 + k][1]] = (leaf, ln.split('_', 1)[1], t[j1 + k][0])
            elif tag == 'replace':  # unequal block: map in order as far as it goes
                for k in range(min(i2 - i1, j2 - j1)):
                    sid2pos[l[i1 + k][1]] = (leaf, ln.split('_', 1)[1], t[j1 + k][0])
# blind instruments: (leaf, line, pos) -> {instrument: sign}
inst = defaultdict(dict)
va = {}
for lf in LEAF:
    for r in tsv(E + f'/verify/vanswers_{lf}.tsv'): va[r['qid']] = r['answer']
for r in tsv(E + '/verify/vpositions.tsv'):
    a = va.get(r['qid'])
    if a in ('A', 'B'): inst[(r['leaf'], r['passage'], int(r['pos']))]['VERIFY'] = r[a]
ea = {}
for lf in LEAF:
    for r in tsv(E + f'/answers_{lf}.tsv'): ea[r['qid']] = r['answer']
for r in tsv(E + '/positions.tsv'):
    a = ea.get(r['qid'])
    if a in ('A', 'B'): inst[(r['leaf'], r['passage'], int(r['pos']))]['EYE'] = r[a]
oa = {}
for p in ('f117a', 'f117b', 'f168', 'f144r'):
    for r in tsv(E + f'/open/oanswers_{p}.tsv'): oa[r['qid']] = r['answer']
for f, name in ((E + '/open/opositions.tsv', 'OPEN'), (E + '/open/opositions_f144r.tsv', 'OPEN144')):
    for r in tsv(f):
        if oa.get(r['qid']): inst[(r['leaf'], r['passage'], int(r['pos']))][name] = oa[r['qid']]
GRADE_INST = ('VERIFY', 'OPEN', 'OPEN144')
# base tokens
base = {lf: {(r['line'], int(r['pos'])): r for r in tsv(c['tok'])} for lf, c in LEAF.items()}
rows = []; changes = defaultdict(list)
for sid, s in settled.items():
    if sid not in sid2pos: continue
    lf, ln, pos = sid2pos[sid]; b = base[lf][(ln, pos)]
    st, new = s['status'], s['new_sign']
    ins = inst.get((lf, ln, pos), {})
    row = dict(sid=sid, leaf=lf, line=ln, pos=pos, tx_sign=b['sign'], base_value=b['value'], base_grade=b['grade'], status=st, owner_sign=new,
               owner_value='', change='', grade='', **{k: ins.get(k, '') for k in ('VERIFY', 'OPEN', 'OPEN144', 'EYE')})
    if st == 'moved':
        v = key.get(new, '?') if '-' not in new else '?'
        row['owner_value'] = v
        if v != b['value']:
            row['change'] = 'U' if v == '?' else 'value'
            agree = any(ins.get(k) == new for k in GRADE_INST)
            row['grade'] = 'U' if v == '?' else ('S' if agree else 'M')
            changes[lf].append(row)
    rows.append(row)
cols = list(rows[0])
with open(H + '/owner_positions.tsv', 'w') as f:
    f.write('\t'.join(cols) + '\n')
    for r in sorted(rows, key=lambda r: (r['leaf'], r['line'], r['pos'])): f.write('\t'.join(str(r[c]) for c in cols) + '\n')
def letters(vals):
    return ''.join(v for v in vals if v not in ('?', 'NULL', '')).lower()
def text(lf, over):
    return letters(over.get(k, r['value']) for k, r in sorted(base[lf].items(), key=lambda kv: (kv[0][0], kv[0][1])))
topk = {}
for lf in LEAF:
    d = defaultdict(list)
    for r in tsv(E + f'/open/olat_{lf}_topk.tsv'): d[(r['line'], int(r['pos']))].append(r['cand'])
    topk[lf] = d
rnd = random.Random(20261003); out = {}
pool = {k: [0.0, 0, 0.0, 0, [0.0] * 200, 0.0, 0] for k in ()}
pa = pb = pbs = 0.0; pna = pnb = pnbs = 0; pc = [0.0] * 200
for lf, c in LEAF.items():
    spec = json.load(open(c['spec'])); jp._ALPHA = None
    j = spec['judge']; m = jp.NgramModel([jp.read_corpus(p) for p in (j.get('corpora') or jp.LANG_CORPORA[j['language']])])
    ch = changes[lf]
    ta = text(lf, {}); tb = text(lf, {(r['line'], r['pos']): r['owner_value'] for r in ch})
    tbs = text(lf, {(r['line'], r['pos']): r['owner_value'] for r in ch if r['grade'] in ('S', 'U')})
    sa, sb, sbs = m.score(ta), m.score(tb), m.score(tbs)
    nv = sum(r['change'] == 'value' for r in ch); nu = sum(r['change'] == 'U' for r in ch)
    cand = [k for k, cs in topk[lf].items() if any(key.get(x, '?') != base[lf][k]['value'] for x in cs if x != base[lf][k]['sign']) and k in base[lf]]
    allk = [k for k in base[lf] if base[lf][k]['value'] not in ('?', '')]
    cs_ = []
    for d in range(200):
        pk = rnd.sample(cand, min(nv, len(cand))); over = {}
        for k in pk:
            alts = [x for x in topk[lf][k] if x != base[lf][k]['sign'] and key.get(x, '?') != base[lf][k]['value']]
            over[k] = key.get(rnd.choice(alts), '?')
        rest = [k for k in allk if k not in over]
        for k in rnd.sample(rest, min(nu, len(rest))): over[k] = '?'
        t = text(lf, over); sc = m.score(t); cs_.append(sc); pc[d] += sc * len(t)
    srt = sorted(cs_); p95 = jp.pct(srt, 0.95)
    real, null, _ = m.controls(max(len(ta), 20))
    out[lf] = dict(n_changes=len(ch), value_changes=nv, u_removals=nu, S=sum(r['grade'] == 'S' for r in ch), M=sum(r['grade'] == 'M' for r in ch),
                   a=round(sa, 4), b=round(sb, 4), bS=round(sbs, 4), c_p95=round(p95, 4), c_median=round(jp.pct(srt, 0.5), 4),
                   b_rank_in_c=sum(x >= sb for x in cs_) + 1, N_a=len(ta), N_b=len(tb), real_p05=round(jp.pct(real, 0.05), 3), null_p99=round(jp.pct(null, 0.99), 3),
                   PASS=bool(sb > sa and sb > p95))
    pa += sa * len(ta); pna += len(ta); pb += sb * len(tb); pnb += len(tb); pbs += sbs * len(tbs); pnbs += len(tbs)
    open(H + f'/owner_b_{lf}.txt', 'w').write(tb + '\n'); open(H + f'/owner_a_{lf}.txt', 'w').write(ta + '\n')
pcs = sorted(x / pnb for x in pc)
out['pooled'] = dict(a=round(pa / pna, 4), b=round(pb / pnb, 4), bS=round(pbs / pnbs, 4), c_p95=round(jp.pct(pcs, 0.95), 4), PASS=bool(pb / pnb > pa / pna and pb / pnb > jp.pct(pcs, 0.95)))
json.dump(out, open(H + '/owner_score.json', 'w'), indent=1); print(json.dumps(out, indent=1))
