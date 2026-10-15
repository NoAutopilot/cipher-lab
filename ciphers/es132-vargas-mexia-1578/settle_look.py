#!/usr/bin/env python3
"""settle_look.py -- applies PREREG-ES132-F89.md (ES132-F89, LANE DEFAULT-A4-0235-15 account 4, 15 Oct 2026): the two-crop look at the 40
f.89 duplicate candidates left `keep:` by settle_dup.py. Reads look_f89/items.tsv (52 items: 40 candidates + 12 decoys, kind hidden from the
look) and look_f89/look_batch{1,2,3}.tsv (the three Sonnet look verdicts), plus look_f89/held.tsv (items the worker's own reconcile read held
back; never adds). Gate: decoys rejected (no/unclear) >= 10 of 12. If it passes, a candidate with verdict yes is applied to
ciphertext_f89r/f89v/f90r/f91r.tsv (token := proposal, unflagged; position-checked against the old token), old tokens kept in
look_f89/look_settled.tsv; summary look_f89/look_result.json. --check: exit 1 if any output is stale or a ciphertext file lacks a settled token.
"""
import sys, json
from pathlib import Path
HERE = Path(__file__).resolve().parent
D = HERE / 'look_f89'
HDR = '# SETTLED (ES132-F89, 15 Oct 2026): f.89 \'?\' tokens settled by a two-crop look against the f.93-95 duplicate per PREREG-ES132-F89.md; old tokens in look_f89/look_settled.tsv.'


def tsv(p):
    rows = [l.rstrip('\n').split('\t') for l in open(p, encoding='utf-8') if l.strip() and not l.startswith('#')]
    return [dict(zip(rows[0], r)) for r in rows[1:]]


def main():
    items = tsv(D / 'items.tsv')
    look = {}
    for b in (1, 2, 3):
        for r in tsv(D / f'look_batch{b}.tsv'): look[r['id'].strip()] = r['verdict'].strip().lower()
    held = {r['id'] for r in tsv(D / 'held.tsv')} if (D / 'held.tsv').exists() else set()
    dec = [it for it in items if it['kind'] == 'decoy']; cand = [it for it in items if it['kind'] == 'cand']
    rej = sum(look[it['id']] in ('no', 'unclear') for it in dec)
    gate = rej >= 10
    by = {}
    for it in cand:
        k = (it['act'], look[it['id']]); by[f'{k[0]}:{k[1]}'] = by.get(f'{k[0]}:{k[1]}', 0) + 1
    apply = {}
    rows = []
    for it in cand:
        v = look[it['id']]
        if not gate: d = 'not-applied:gate-failed'
        elif v != 'yes': d = f'keep:look-{v}'
        elif it['id'] in held: d = 'keep:held-by-reconcile'
        else: d = 'applied'
        new = it['P'] if d == 'applied' else it['x']
        rows.append([it['id'], it['f89'], it['x'], it['P'], it['dup'], it['act'], v, d, new])
        if d == 'applied':
            pg, ln, i = it['f89'].split(':'); apply[(pg, ln, int(i))] = (it['x'], new)
    outs = {}
    for pg in ('f89r', 'f89v', 'f90r', 'f91r'):
        f = HERE / f'ciphertext_{pg}.tsv'
        lines = f.read_text(encoding='utf-8').split('\n'); new = []
        for l in lines:
            if l.startswith('#') or '\t' not in l: new.append(l); continue
            ln, b = l.split('\t', 1); toks = b.split()
            for i in range(len(toks)):
                if (pg, ln, i + 1) in apply:
                    old, nw = apply[(pg, ln, i + 1)]
                    if toks[i] == old: toks[i] = nw
                    elif toks[i] != nw: raise SystemExit(f'position mismatch {pg} {ln} {i+1}: {toks[i]} vs {old}')
            new.append(ln + '\t' + ' '.join(toks))
        if any(k[0] == pg for k in apply) and HDR not in new:
            new.insert(max(k for k, l in enumerate(new) if l.startswith('#')) + 1, HDR)
        outs[f.name] = '\n'.join(new)
    res = dict(prereg='PREREG-ES132-F89.md', items=len(items), candidates=len(cand), decoys=len(dec),
               decoys_rejected=rej, gate_pass=gate, candidate_verdicts=by, held_by_reconcile=sorted(held),
               applied=sum(r[7] == 'applied' for r in rows),
               decoy_verdicts={it['id']: look[it['id']] for it in dec})
    outs['look_f89/look_settled.tsv'] = ('# settle_look.py (ES132-F89): id f89_pos f89_tok_old proposal dup_pos action verdict decision f89_tok_new\n'
                                         + '\n'.join('\t'.join(r) for r in rows) + '\n')
    outs['look_f89/look_result.json'] = json.dumps(res, indent=1, ensure_ascii=False) + '\n'
    if '--check' in sys.argv:
        stale = [k for k, v in outs.items() if not (HERE / k).exists() or (HERE / k).read_text(encoding='utf-8') != v]
        print('STALE ' + ' '.join(stale) if stale else 'OK: committed outputs match'); sys.exit(1 if stale else 0)
    for k, v in outs.items(): (HERE / k).write_text(v, encoding='utf-8')
    print(json.dumps(res, ensure_ascii=False))


if __name__ == '__main__':
    main()
