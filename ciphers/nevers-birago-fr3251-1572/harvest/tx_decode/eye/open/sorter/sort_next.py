#!/usr/bin/env python3
"""BIR-OWNER: rank the positions the owner has not settled (taken-out, aside, bad-cut, or untouched at grade M/U) by how much the
best single lattice top-k alternative would move the leaf's judge score. A pointer for what to sort next, not a reading.
Run from the repo root after score_owner.py; writes sort_next.tsv beside this file."""
import csv, json, sys, os
sys.path.insert(0, 'tools'); import judge_plaintext as jp
H = os.path.dirname(os.path.abspath(__file__)); N = 'ciphers/nevers-birago-fr3251-1572'; E = N + '/harvest/tx_decode/eye'
tsv = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
key = {r['sign']: r['value'] for r in tsv(N + '/harvest/key_1572_sheet.tsv')}
spec = {'f117': 'specs/birago-fr3252-f117.json', 'f168': 'specs/nevers-birago-fr3251-1572.json', 'f144r': 'specs/nevers-birago-fr3251-1572.json'}
tok = {'f117': E + '/apply/reading_f117_apply_tokens.tsv', 'f168': E + '/apply/reading_f168_apply_tokens.tsv', 'f144r': H + '/reading_f144r_owner_tokens.tsv'}
pos = tsv(H + '/owner_positions.tsv'); out = []
for lf in spec:
    j = json.load(open(spec[lf]))['judge']; m = jp.NgramModel([jp.read_corpus(p) for p in (j.get('corpora') or jp.LANG_CORPORA[j['language']])])
    base = {(r['line'], int(r['pos'])): r for r in tsv(tok[lf])}
    order = sorted(base)
    txt = lambda over: ''.join(over.get(k, base[k]['value']) for k in order if over.get(k, base[k]['value']) not in ('?', 'NULL', '')).lower()
    s0 = m.score(txt({}))
    topk = {}
    for r in tsv(E + f'/open/olat_{lf}_topk.tsv'): topk.setdefault((r['line'], int(r['pos'])), []).append(r['cand'])
    for p in pos:
        if p['leaf'] != lf: continue
        k = (p['line'], int(p['pos']))
        if p['status'] == 'moved' or (p['status'] == 'kept' and base[k]['grade'] not in ('M', 'U')): continue
        best = (0.0, '')
        for c in topk.get(k, []):
            v = key.get(c)
            if not v or v == base[k]['value']: continue
            d = m.score(txt({k: v})) - s0
            if d > best[0]: best = (d, c)
        if best[1]: out.append((lf, p['sid'], p['line'], p['pos'], p['status'], base[k]['sign'], base[k]['value'], best[1], key[best[1]], round(best[0], 4)))
out.sort(key=lambda r: -r[-1])
with open(H + '/sort_next.tsv', 'w') as f:
    f.write('leaf\tsid\tline\tpos\towner_status\tsign_now\tvalue_now\tbest_alt\talt_value\tscore_gain\n')
    for r in out: f.write('\t'.join(map(str, r)) + '\n')
for lf in spec: print(lf, [r[1:2] + r[4:] for r in out if r[0] == lf][:6])
