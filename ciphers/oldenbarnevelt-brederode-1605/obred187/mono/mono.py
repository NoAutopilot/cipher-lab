#!/usr/bin/env python3
"""OBRED-MONO (15 Oct 2026), PREREG obred187/PREREG-OBREDMONO.md.

Joint band-monotonicity check of OBRED-SEG's 20 word leads for no. 92 + the scan-187 postscript: under an alphabetical homophonic
list, code order implies letter order, so D = discordant slot pairs ((c1 < c2, l1 > l2) or one code with two letters) is near 0 for
right leads. Null: letters permuted among the slots of each pool gap (1,000 draws, seed 4562). Synthetic known-answer control (OBRED-SEG's
generator, e = 0.5 and 0.75, 40 sims each, seed 1600, 200 null draws per sim) must pass before any target number counts.
Writes mono_gate.json and mono_leads.tsv beside this script; --check exits 1 if a regeneration differs. Grade M unless the PREREG's
S condition holds. Disk/CPU only.
Run: python3 ciphers/oldenbarnevelt-brederode-1605/obred187/mono/mono.py [--check]
"""
import bisect, json, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.normpath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(T, 'obred187', 'seg'))
sys.path.insert(0, os.path.join(T, 'obred187', 'band'))
sys.path.insert(0, os.path.join(T, 'obred187', 'try'))
import seg as S  # OBRED-SEG decoder, lexicon, sub-runs, unchanged
import band as B
from run_try import pairs556, ALPHA

NA = len(ALPHA)


def gap_key(c, pcodes):
    return ('at', c) if c in pcodes else ('gap', bisect.bisect_left(pcodes, c))


def discord(slots):
    """slots: list of (code, letter_idx, lead). Returns D and the list of discordant (i, j)."""
    out = []
    for i in range(len(slots)):
        c1, l1, _ = slots[i]
        for j in range(i + 1, len(slots)):
            c2, l2, _ = slots[j]
            if (c1 == c2 and l1 != l2) or (c1 < c2 and l1 > l2) or (c2 < c1 and l2 > l1):
                out.append((i, j))
    return len(out), out


def null_D(slots, pcodes, draws, rng):
    groups = {}
    for k, (c, _, _) in enumerate(slots):
        groups.setdefault(gap_key(c, pcodes), []).append(k)
    res = []
    for _ in range(draws):
        s = list(slots)
        for idx in groups.values():
            lets = [slots[k][1] for k in idx]; rng.shuffle(lets)
            for k, l in zip(idx, lets):
                s[k] = (slots[k][0], l, slots[k][2])
        res.append(discord(s)[0])
    return res


def flags(slots, pcodes, pairs):
    leads = sorted({s[2] for s in slots})
    keyed = {}
    for k, (c, _, L) in enumerate(slots):
        keyed.setdefault(gap_key(c, pcodes), []).append(k)
    testable = set()
    for idx in keyed.values():
        for a in idx:
            for b in idx:
                if a != b and (slots[a][0] != slots[b][0] or slots[a][2] != slots[b][2]):
                    testable.add(slots[a][2])
    bad = {}
    for i, j in pairs:
        for L in {slots[i][2], slots[j][2]}:
            bad[L] = bad.get(L, 0) + 1
    return {L: ('contradicted' if bad.get(L) else 'clean') if L in testable else 'untestable' for L in leads}, bad


def anchor_discord(slots, pool):
    n = {}
    for c, l, L in slots:
        for pc, pl in pool:
            if (c == pc and l != pl) or (c < pc and l > pl) or (pc < c and pl > l):
                n[L] = n.get(L, 0) + 1
    return n


def leads_from_paths(paths, subs, ivs):
    """returns list of (lead_id, subrun_no, i, j, word) and slots."""
    leads, slots = [], []
    for n, ((_, _, codes), p) in enumerate(zip(subs, paths), 1):
        for i, j, w, ne in p:
            if w and len(w) >= S.MINW:
                L = len(leads); leads.append((L, n, i, j, w))
                for k in range(i, j):
                    slots.append((codes[k], ALPHA.index(w[k - i]), L))
    return leads, slots


def control(lens, sims=40, nd=200, seed=1600):
    trie = S.lexicon([f for f in S.FILES if f != S.HELD])
    held = S.words_of(S.HELD)
    seq = [ALPHA.index(c) for w in held for c in w]
    out = {}
    for e in (0.5, 0.75):
        rng = random.Random(seed)
        jp = 0; nlead = ntest = 0; rt = rc = wt = wc = 0; hit = ntok = 0
        for _ in range(sims):
            bands = B.synth_list(seq, rng)
            enc = lambda g: rng.choice(bands[g])
            pool = []
            for _ in range(41):
                g = rng.choice(seq); c = enc(g)
                if rng.random() < e:
                    g = max(0, min(NA - 1, g + rng.choice((-1, 1))))
                pool.append((c, g))
            pool.sort()
            subs, truth = [], []
            for L in lens:
                k = rng.randrange(0, len(held) - 200); ws = []
                while sum(map(len, ws)) < L:
                    ws.append(held[k]); k += 1
                codes = [enc(ALPHA.index(ch)) for w in ws for ch in w]
                subs.append(('s', 0, codes)); truth.append(ws)
            ivs = S.to_ivs(pool, subs)
            for s_iv, ws in zip(ivs, truth):
                for (lo, hi), ch in zip(s_iv, ''.join(ws)):
                    hit += lo <= ALPHA.index(ch) <= hi; ntok += 1
            paths = [S.decode(iv, trie) for iv in ivs]
            leads, slots = leads_from_paths(paths, subs, ivs)
            right = {}
            for L, n, i, j, w in leads:
                spans, k = {}, 0
                for tw in truth[n - 1]:
                    spans[(k, k + len(tw))] = tw; k += len(tw)
                right[L] = spans.get((i, j)) == w
            pcodes = sorted({c for c, _ in pool})
            D, pairs = discord(slots)
            nul = null_D(slots, pcodes, nd, rng)
            jp += (sum(x <= D for x in nul) / nd) <= 0.05
            fl, _ = flags(slots, pcodes, pairs)
            for L, f in fl.items():
                nlead += 1
                if f == 'untestable':
                    continue
                ntest += 1
                if right[L]:
                    rt += 1; rc += f == 'clean'
                else:
                    wt += 1; wc += f == 'clean'
        pt = rt / max(1, rt + wt); pcl = rc / max(1, rc + wc)
        out[f'e{e}'] = dict(sims=sims, null_draws=nd, interval_hit=hit / max(1, ntok), leads=nlead, testable=ntest,
                            right_testable=rt, right_clean_rate=rc / max(1, rt), wrong_testable=wt,
                            wrong_clean_rate=wc / max(1, wt), precision_testable=pt, precision_clean=pcl,
                            joint_p05_share=jp / sims,
                            gate=jp / sims >= 0.70 and rc / max(1, rt) >= 0.60 and pcl >= pt + 0.10)
    out['gate'] = 'PASS' if out['e0.5']['gate'] and out['e0.75']['gate'] else 'BELOW GATE'
    return out


def target_leads():
    subs = S.target_subruns()
    P = pairs556(); pool = sorted(B.leaf_pairs(P, '555') + B.leaf_pairs(P, '556'))
    rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(T, 'obred187', 'seg', 'seg_92_187.tsv'))][1:]
    leads, slots = [], []
    for r in rows:
        n = int(r[2]); i, j = (int(x) for x in r[3].split('-')); i -= 1
        codes = [int(x) for x in r[4].split()]; w = r[6]
        assert codes == subs[n - 1][2][i:j] and len(w) == len(codes), r
        L = len(leads); leads.append((L, n, i, j, w))
        for c, ch in zip(codes, w):
            slots.append((c, ALPHA.index(ch), L))
    # the leads are OBRED-SEG's own decode of the same intervals
    trie = S.lexicon(S.FILES)
    chk, _ = leads_from_paths([S.decode(iv, trie) for iv in S.to_ivs(pool, subs)], subs, None)
    assert [x[1:] for x in chk] == [x[1:] for x in leads]
    return subs, pool, leads, slots


def build():
    subs, pool, leads, slots = target_leads()
    ctrl = control([len(c) for _, _, c in subs])
    pcodes = sorted({c for c, _ in pool})
    D, pairs = discord(slots)
    nul = null_D(slots, pcodes, 1000, random.Random(4562))
    p = sum(x <= D for x in nul) / len(nul)
    fl, bad = flags(slots, pcodes, pairs)
    anc = anchor_discord(slots, pool)
    tgt = dict(slots=len(slots), D=D, null_mean=sum(nul) / len(nul), null_p05=sorted(nul)[int(0.05 * len(nul))],
               null_min=min(nul), p=p, draws=len(nul), passes=p <= 0.05,
               clean=sum(f == 'clean' for f in fl.values()), contradicted=sum(f == 'contradicted' for f in fl.values()),
               untestable=sum(f == 'untestable' for f in fl.values()))
    s_ok = ctrl['gate'] == 'PASS' and tgt['passes'] and ctrl['e0.75']['precision_clean'] >= 0.80
    rows = ['subrun\tspan\tcodes\tword\tflag\tdiscordant_pairs\twith\tanchor_discord\tgrade']
    for L, n, i, j, w in leads:
        partners = sorted({(leads[slots[b][2]][4] if slots[a][2] == L else leads[slots[a][2]][4]) + ':' +
                           (f'{slots[a][0]}{ALPHA[slots[a][1]]}/{slots[b][0]}{ALPHA[slots[b][1]]}')
                           for a, b in pairs if L in (slots[a][2], slots[b][2])})
        g = 'S' if (s_ok and fl[L] == 'clean' and len(w) >= 5) else 'M'
        rows.append(f'{n}\t{i + 1}-{j}\t{" ".join(str(s[0]) for s in slots if s[2] == L)}\t{w}\t{fl[L]}\t{bad.get(L, 0)}\t'
                    f'{" ".join(partners) or "-"}\t{anc.get(L, 0)}\t{g}')
    res = dict(control=ctrl, target=tgt, S_condition=s_ok, prereg='obred187/PREREG-OBREDMONO.md (9a6abd583)')
    res = json.loads(json.dumps(res), parse_float=lambda x: round(float(x), 4))
    return json.dumps(res, indent=1, sort_keys=True) + '\n', '\n'.join(rows) + '\n'


def main():
    gate, rows = build()
    gp, rp = os.path.join(HERE, 'mono_gate.json'), os.path.join(HERE, 'mono_leads.tsv')
    if '--check' in sys.argv:
        bad = any((open(f).read() != s) if os.path.exists(f) else True for f, s in ((gp, gate), (rp, rows)))
        print('stale' if bad else 'up to date'); sys.exit(1 if bad else 0)
    open(gp, 'w').write(gate); open(rp, 'w').write(rows)
    print(gate); print(rows)


if __name__ == '__main__':
    main()
