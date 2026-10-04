#!/usr/bin/env python3
"""A3V3-SAVT table recovery (PREREG amendment 2): hard-EM on c380 lines 6-14 against the Charriere print, held-out on 15-22.
Then the same EM on all of lines 6-22 for the proposed table with per-pile evidence. Writes savt/recovery.json and
savt/table_proposed.tsv. Usage: python3 savt/recover.py"""
import json, random, collections, os
from align import load_G, seed_values, load_tokens, decode, semiglobal, HERE

def em(toks_fit, seed, G, iters=10, minocc=3):
    vals = dict(seed); hist = []
    for it in range(iters):
        dec = decode(toks_fit, vals); D = ''.join(c for c, _ in dec)
        mt, mp, pairs = semiglobal(D, G); hist.append(round(mt / mp, 4))
        ev = collections.defaultdict(collections.Counter)
        for iD, jG in pairs: ev[toks_fit[dec[iD][1]][2]][G[jG]] += 1
        new = dict(vals)
        for p, c in ev.items():
            if p in seed and (len(seed[p]) > 1 or seed[p] == 'DOUBLE'): continue
            if sum(c.values()) >= minocc: new[p] = c.most_common(1)[0][0]
        if new == vals: break
        vals = new
    return vals, ev, hist

def Ssemi(toks, vals, G):
    D = ''.join(c for c, _ in decode(toks, vals)); mt, mp, _ = semiglobal(D, G); return mt / mp if mp else 0.0

def main():
    G = load_G(); seed = seed_values(); toks = load_tokens()
    fit = [t for t in toks if 6 <= t[0] <= 14]; test = [t for t in toks if t[0] >= 15]
    rec, _, hist = em(fit, seed, G)
    out = {'fit_hist': hist, 'heldout_recovered': Ssemi(test, rec, G), 'heldout_seed': Ssemi(test, seed, G)}
    piles = sorted(rec); vl = [rec[p] for p in piles]; n1 = []
    for s in range(1, 201):
        r = random.Random(s); sh = vl[:]; r.shuffle(sh); n1.append(Ssemi(test, dict(zip(piles, sh)), G))
    n1.sort(); out['heldout_N1'] = {'mean': round(sum(n1) / 200, 4), 'p95': round(n1[189], 4), 'max': round(n1[-1], 4)}
    out['heldout_pass'] = bool(out['heldout_recovered'] > n1[-1] and out['heldout_recovered'] > out['heldout_seed'])
    # full recovery on lines 6-22
    late = [t for t in toks if t[0] >= 6]
    full, ev, hist2 = em(late, seed, G); out['full_hist'] = hist2
    # seed-alignment evidence (iteration 0 of the EM on lines 6-22): how often each pile's seed value meets the same gloss letter
    _, ev0, _ = em(late, seed, G, iters=1)
    cnt = collections.Counter(t[2] for t in toks)
    rows = []
    for p in sorted(set(cnt) | set(full)):
        c = ev.get(p, collections.Counter()); n = sum(c.values()); top = c.most_common(3)
        agree = (top[0][1] / n) if n else 0.0
        emv = full.get(p, '?'); sd = seed.get(p, '-')
        c0 = ev0.get(p, collections.Counter()); n0 = sum(c0.values())
        conf = c0.get(sd[:1], 0) if sd not in ('-', 'DOUBLE') else 0
        # proposed = seed when the held-out failed (EM table not licensed), else the EM value
        val = emv if out['heldout_pass'] else (sd if sd != '-' else '?')
        grade = 'C' if (out['heldout_pass'] and n >= 5 and agree >= 0.60 and val == top[0][0]) else 'M'
        if val == '?': grade = '-'
        rows.append((p, cnt[p], sd, val, n0, conf, round(conf / n0, 3) if n0 else 0.0, ' '.join(f'{a}:{b}' for a, b in c0.most_common(3)), emv, n, round(agree, 3), grade))
    with open(os.path.join(HERE, 'table_proposed.tsv'), 'w') as f:
        f.write('# A3V3-SAVT proposed pile -> letter table (c380, fr.16144 f.187r), hard-EM vs Charriere IV p.638 print of the 23 Dec 1587 letter.\n')
        f.write('# grade C: >=5 aligned gloss letters, plurality >=60%, held-out passed; else M. HELD-OUT FAILED (recovery.json): proposed = seed value, all M.\n# seedaln_* = evidence from the seed-table alignment of lines 6-22 (alignment chosen to maximise matches: confirm counts are optimistic).\n')
        f.write('# Piles are SV-SORT over-split clusters, not a settled alphabet: proposals for the owner sort, not labels.\n')
        f.write('pile\tn_tokens_c380\tseed_value\tproposed\tseedaln_n\tseedaln_confirm\tseedaln_confirm_share\tseedaln_top3\tem_value(heldout_failed)\tem_aligned_n\tem_plurality_share\tgrade\n')
        for r in rows: f.write('\t'.join(map(str, r)) + '\n')
    out['grades'] = dict(collections.Counter(r[11] for r in rows))
    out['changed_from_seed'] = sorted(p for p in full if full[p] != seed.get(p))
    json.dump(out, open(os.path.join(HERE, 'recovery.json'), 'w'), indent=1); print(json.dumps(out, indent=1))

if __name__ == '__main__':
    main()
