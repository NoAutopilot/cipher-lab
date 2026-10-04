#!/usr/bin/env python3
"""RUN2-PAG (4 Oct 2026): per-occurrence table for the 7 codes where tools/gibbs_align.py (RUN1-PAG, gibbs_codes.tsv) and
tools/interlinear_align.py (align_all.tsv / key.tsv) disagree: 31, 45, 48, 97, 148, 176, 204.
For every occurrence: pair, page, both tools' chunk for this token, the whole pair's segmentation under each tool, the gloss.
Gibbs chunks are the per-letter seed-0 run (the run that passed PREREG_seg2.md held-out) and a pooled seed-0 run.
Disk only, deterministic. Writes settle7.tsv and settle7_rulings.tsv (S where the token's own Gibbs chunk equals the held-out-passed code value and
the gloss word admits it with firm neighbours, else M; DEMOTE lists the eye-read context demotions). --check exits 1 if either
is stale or an S ruling is missing from ../exceptions.tsv.
    python3 settle7.py [--check]
N4-PAG65 (4 Oct 2026) extends the same table and rule to code 65 (hard-EM 'ab' over "Labbe", single attestation) and code 116
(key.tsv 'g', grade C, against 'ge' in "genie"/"Visage"/"agee"/"Mariage"). Neither is in gibbs_codes.tsv (not held in both
letters): their value is the per-letter seed-0 Gibbs run's own chunk (the same run that passed PREREG_seg2.md held-out),
65 = b (1/1, L1), 116 = ge (4/4, all L2). Same S/M rule; DEMOTE lists the three 116 tokens whose neighbours do not pin it.
"""
import collections, csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import gibbs_align as ga
import interlinear_align as ia

CODES = ['31', '45', '48', '97', '148', '176', '204', '65', '116']
GIBBS = {'31': 'b', '45': 'r', '48': 'u', '97': 'en', '148': 'lo', '176': 'ni', '204': 'que',  # gibbs_codes.tsv
         '65': 'b', '116': 'ge'}  # N4-PAG65: per-letter Gibbs run's own chunk, not held in both letters
# Context demotions read by eye from both segmentations (RUN2-PAG): the token's own Gibbs chunk equals the code value but the
# gloss word with its firm (H/C/S) neighbours does not pin it there.
DEMOTE = {
    ('P17', 4): 'gloss "en secret": 221 se, 32 c, 212 re, 47 t (all S) pin "secret"; en lies on 222/191/46/221/97 and Gibbs '
                'makes four of them null to put it on 97 -- not pinned',
    ('P33', 1): 'gloss "en 2e Nopces": en could sit on 220 (unsettled, key sa) with 97 null, or on 97 -- not pinned',
    # ('P53', 13), 176 in "genie", was demoted here by RUN2-PAG for the 116 = g conflict; N4-PAG65 settles 116 = ge at P53 12
    # (87 de H on the left, 176 ni on the right), so the demotion is lifted.
    ('P23', 24): 'gloss "Visage": 245 fa (M, single), 220 sa (M), 214 nde (M) on both sides; "ge" vs "g" + an e on 214 not pinned',
    ('P37', 1): 'gloss "agee": 30 a (M) and 34 de (M) on both sides, 87 de (H) one further; "ge"+"e" vs "g"+"ee" not pinned',
    ('P42', 5): 'gloss "Mariage" ends the pair, but 30 a (M) on the left and 213 ma (C) reads against the gloss ("ri" by Gibbs); '
                'the e is not pinned to 116',
}
L1 = {'f60R', 'f61L', 'f61R', 'f65L'}


def gibbs_tokens(pairs, seed=0):
    prep, keep = ga.sample(pairs, seed=seed)
    m = {}
    for k, t, c, ch, sh in ga.token_modes(prep, keep):
        m[(pairs[k]['cipher_line'], t)] = (ch, sh)
    return m


def main():
    pairs = ia.load_pairs(os.path.join(HERE, 'pairs.tsv'))
    l1 = [p for p in pairs if p['page'] in L1]
    l2 = [p for p in pairs if p['page'] not in L1]
    per = {**gibbs_tokens(l1), **gibbs_tokens(l2)}
    pool = gibbs_tokens(pairs)
    hard = {}
    for r in csv.DictReader(open(os.path.join(HERE, 'align_all.tsv')), delimiter='\t'):
        hard[(r['cipher_line'], int(r['idx']))] = (r['plain_chunk'], r['status'])
    rows = ['code\tpair\tpage\tidx\thardEM_chunk\thardEM_status\tgibbs_letter_chunk\tgibbs_letter_share\tgibbs_pool_chunk\t'
            'gloss\tcipher\thardEM_seg\tgibbs_letter_seg']
    for c in CODES:
        for p in pairs:
            toks = p['cipher_raw'].split()
            for j, t in enumerate(toks):
                if str(ia.classify_token(t)[1]) != c or ia.classify_token(t)[0] not in ('num', 'code'):
                    continue
                L = p['cipher_line']
                hs = ' '.join('%s=%s' % (x, hard.get((L, i), ('?',))[0] or '0') for i, x in enumerate(toks))
                gs = ' '.join('%s=%s' % (x, per.get((L, i), ('-',))[0] or '0') for i, x in enumerate(toks))
                h = hard.get((L, j), ('', 'none'))
                g = per.get((L, j), ('', 0.0))
                rows.append('\t'.join([c, L, p['page'], str(j), h[0], h[1], g[0], '%.2f' % g[1],
                                       pool.get((L, j), ('',))[0], p['plain_raw'], p['cipher_raw'], hs, gs]))
    pos = {p['cipher_line']: p['positions'].split(',') for p in pairs}
    rul = ['code\tvalue\tpair\tline\tposition\tgibbs_chunk\thardEM_chunk\tgloss\truling\twhy']
    for r in rows[1:]:
        f = r.split('\t')
        c, L, page, j, hch, gch, gloss = f[0], f[1], f[2], int(f[3]), f[4], f[6], f[9]
        if gch != GIBBS[c]:
            g, why = 'M', 'own Gibbs chunk %r is not the code value' % gch
        elif (L, j) in DEMOTE:
            g, why = 'M', DEMOTE[(L, j)]
        else:
            g, why = 'S', 'own Gibbs chunk = code value; gloss word admits it with firm neighbours'
        rul.append('\t'.join([c, GIBBS[c], L, page, pos[L][j], gch, hch, gloss, g, why]))
    txt = '\n'.join(rows) + '\n'
    rtxt = '\n'.join(rul) + '\n'
    rpath = os.path.join(HERE, 'settle7_rulings.tsv')
    exc = os.path.join(HERE, '..', 'exceptions.tsv')
    need = {(x.split('\t')[3], x.split('\t')[4], x.split('\t')[1]) for x in rul[1:] if x.split('\t')[8] == 'S'}
    have = {(e[0], e[1], e[2]) for e in (l.rstrip('\n').split('\t') for l in open(exc)) if len(e) > 3 and e[3] == 'S'}
    path = os.path.join(HERE, 'settle7.tsv')
    if '--check' in sys.argv:
        ok = os.path.exists(path) and open(path).read() == txt and open(rpath).read() == rtxt and need <= have
        print('settle7 up to date (%d S rulings in exceptions.tsv)' % len(need) if ok else 'settle7 STALE')
        sys.exit(0 if ok else 1)
    open(path, 'w').write(txt)
    open(rpath, 'w').write(rtxt)
    print(rtxt)
    print('S rulings missing from exceptions.tsv: %d' % len(need - have))


if __name__ == '__main__':
    main()
