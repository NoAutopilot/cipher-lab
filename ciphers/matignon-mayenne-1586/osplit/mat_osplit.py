#!/usr/bin/env python3
"""MAT-OSPLIT (15 Oct 2026): o shape split (A plain round / B round with right stem) scored by MAT-KA's block-held-out gloss
instrument, per osplit/PREREG-MAT-OSPLIT.md (ee2c00674; addendum 1 e1e49a3f5), both pushed before the sort and any score.

Reads osplit/sort_tokens.tsv + osplit/sort_answers.tsv (blind Sonnet sort), relabels each sorted o token oA / oB (X stays o),
aligns every f.91 block alone with o masked (f91/mat_ka.py align(masked_h='o')), then
 1. split test: pooled LOBO hits of oA + oB vs 1000 random A/B relabelings at the same per-block counts (gate: > p95);
 2. per shape: MAT-KA's verdict rule (200-draw label-shuffle null, power code at the shape's n, 20 seeds).
Gating run = MAT-KA's reader unchanged (block E from both drafts); secondary run = block E from f91e only (addendum 1).
Writes osplit/mat_osplit_result.tsv. Usage: python3 mat_osplit.py [--check]
MAT-O3X (PREREG addendum 2): --answers FILE (default sort_answers.tsv) reads another sort; its result goes to
mat_osplit_result_<FILE stem minus 'sort_answers'>.tsv, e.g. --answers sort_answers_o3x.tsv -> mat_osplit_result_o3x.tsv.
"""
import collections, csv, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'f91'))
import mat_ka as KA  # noqa: E402
B = KA.BLOCKS
CAND = {'oA': 'i', 'oB': 'a'}
SPLITS = 1000

shape = {}
ANS = sys.argv[sys.argv.index('--answers') + 1] if '--answers' in sys.argv else 'sort_answers.tsv'
SUF = os.path.splitext(os.path.basename(ANS))[0].replace('sort_answers', '')
ans = {r['id']: r['shape'].strip().upper() for r in csv.DictReader(open(os.path.join(HERE, ANS)), delimiter='\t')}
for r in csv.DictReader(open(os.path.join(HERE, 'sort_tokens.tsv')), delimiter='\t'):
    s = ans.get(r['id'], 'X')
    if s in ('A', 'B'): shape[(r['draft'], r['line'], int(r['position']))] = 'o' + s

def build_signs(e_only):
    sg = collections.defaultdict(list)
    for i in KA.INS:
        for r in csv.DictReader(open(os.path.join(KA.HERE, f'ciphertext_draft_{i}.tsv')), delimiter='\t'):
            b = r['line'][0]
            if b not in B or (e_only and b == 'E' and i != 'f91e'): continue
            s = r['sign'] if r['confidence'] == 'H' else '?'
            sg[b].append(shape.get((i, r['line'], int(r['position'])), s))
    return sg

def power(al, val, n):
    cnt = {c: sum(1 for b in B for s, x in al[b] if s == c and x) for c in KA.HKEY if c != 'o'}
    same = [c for c in cnt if KA.HKEY[c] == val and cnt[c] >= n]
    if same: return max(same, key=lambda c: (cnt[c], c))
    ge = [c for c in cnt if cnt[c] >= n]
    return min(ge, key=lambda c: (cnt[c], c))

def run(e_only):
    KA.signs = build_signs(e_only)
    al = KA.align(masked_h='o')
    rows = []
    pa, pb = KA.label_pos(al, 'oA'), KA.label_pos(al, 'oB')
    ha, na, _, _ = KA.lobo(pa); hb, nb, _, _ = KA.lobo(pb)
    stat = ha + hb
    # unsplit o (all sorted A/B plus X), for reference
    po = {b: pa[b] + pb[b] + [x for s, x in al[b] if s == 'o' and x] for b in B}
    ho, no, _, majo = KA.lobo(po)
    # split control: per block, shuffle the A/B labels among the scored A/B positions
    accs = []
    for d in range(1, SPLITS + 1):
        rnd = random.Random(d); qa, qb = {}, {}
        for b in B:
            pool = pa[b] + pb[b]; rnd.shuffle(pool); qa[b], qb[b] = pool[:len(pa[b])], pool[len(pa[b]):]
        accs.append(KA.lobo(qa)[0] + KA.lobo(qb)[0])
    accs.sort(); p95 = accs[int(0.95 * SPLITS) - 1]
    split_pass = stat > p95
    tag = 'E-f91e-only(secondary)' if e_only else 'MAT-KA-reader(gating)'
    rows.append((tag, 'split', f'{stat}/{na + nb}={stat / max(1, na + nb):.3f}',
                 f'{sum(accs) / SPLITS:.1f}/{p95}/{accs[-1]}', f'unsplit o LOBO {ho}/{no}={ho / max(1, no):.3f} maj {majo}',
                 '', 'PASS' if split_pass else 'FAIL', 'split-PASS' if split_pass else 'split-FAIL'))
    for lab in ('oA', 'oB'):
        pos = KA.label_pos(al, lab); counts = {b: len(pos[b]) for b in B}
        h, n, folds, maj = KA.lobo(pos); acc = h / n if n else 0.0
        mean, p95l, mx = KA.null(al, counts)
        if n == 0:
            rows.append((tag, lab, '0/0', '', '', '', '', 'no-scored-positions')); continue
        pc = power(al, CAND[lab], n)
        pal = KA.align(masked_h=pc); ppos = KA.label_pos(pal, pc)
        flat = [(b, x) for b in B for x in ppos[b]]; beat = fit = 0
        for s in range(1, KA.SUBS + 1):
            rnd = random.Random(s); sub = flat if len(flat) <= n else rnd.sample(flat, n)
            sp = collections.defaultdict(list)
            for b, x in sub: sp[b].append(x)
            ph, pn, _, pm = KA.lobo(sp); _, pp95, _ = KA.null(pal, {b: len(sp[b]) for b in B}, seed0=s)
            beat += (ph / pn if pn else 0) > pp95; fit += pm == KA.HKEY[pc]
        pw = beat >= 11 and fit >= 11
        if not pw: v = 'too-short'
        elif acc > p95l and maj == CAND[lab]: v = 'candidate-S'
        elif acc > p95l: v = f'candidate-S-at-{maj}(flag)'
        else: v = 'fails-held-out'
        if not split_pass: v += ';grade-M(split-FAIL)'
        fs = ' '.join(f'{b}:{t}{fh}/{fn}' for b, (t, fh, fn) in folds.items())
        rows.append((tag, lab, f'{h}/{n}={acc:.3f}', f'{mean:.3f}/{p95l:.3f}/{mx:.3f}', f'majority {maj}; folds {fs}',
                     f'{pc}={KA.HKEY[pc]} n{min(len(flat), n)} beat{beat}/20 fit{fit}/20', 'PASS' if pw else 'FAIL', v))
    return rows

def main():
    rows = run(False) + run(True)
    res = 'run\tlabel\tstatistic\tnull_mean/p95/max\tdetail\tpower\tgate\tverdict\n' + ''.join('\t'.join(map(str, r)) + '\n' for r in rows)
    rp = os.path.join(HERE, f'mat_osplit_result{SUF}.tsv')
    if '--check' in sys.argv:
        st = not os.path.exists(rp) or open(rp).read() != res
        print('STALE' if st else 'OK'); sys.exit(1 if st else 0)
    open(rp, 'w').write(res); print(res)

if __name__ == '__main__':
    main()
