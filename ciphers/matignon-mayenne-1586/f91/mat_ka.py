#!/usr/bin/env python3
"""MAT-KA (15 Oct 2026): block-held-out known-answer test of the unkeyed labels U, T, D2, BOX2, + on f.91r-92r blocks A-F,
per PREREG-MAT-KA.md (pushed 17451d305 before any score).

Each block is aligned alone with tools/interlinear_align.py run_align (settings as align_f91e.py); every code that is not an H
single-letter key code is renamed to a unique singleton, so its chunk comes from H-code anchoring only. For a label, the fit is its
majority gloss letter in the other five blocks; pooled leave-one-block-out (LOBO) accuracy is scored against 200 label-shuffle draws
(same per-block counts, pool = all scored code positions) and a power check (a known H code, masked the same way, subsampled to the
label's count, 20 seeds). Writes mat_ka_result.tsv and mat_ka_folds.tsv. Usage: python3 mat_ka.py [--check]
"""
import collections, csv, os, random, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import interlinear_align as IA  # noqa: E402
IA.FOLD_FS = False   # --keep-fs
IA.WORD_PFX = '%'    # --word-code-prefix %
BLOCKS = ['A', 'B', 'C', 'D', 'E', 'F']
INS = ['f91', 'f91c', 'f91e']
LABELS = [('U', 'e', 'h', None), ('T', 'r', 'L', None), ('D2', 'a', 'e', 'X'), ('BOX2', 'u', 's', None), ('+', 'm', '4+', None)]
DRAWS, SUBS = 200, 20
FOLD = str.maketrans('vj', 'ui')

def fold(s):
    s = unicodedata.normalize('NFKD', s.lower()); return ''.join(c for c in s if 'a' <= c <= 'z').translate(FOLD)

key = {r['code']: (r['value'], r['grade']) for r in csv.DictReader(open(os.path.join(HERE, '..', 'key.tsv')), delimiter='\t')}
HKEY = {c: fold(v) for c, (v, g) in key.items() if g == 'H' and len(v) == 1}
signs = collections.defaultdict(list)
for i in INS:
    for r in csv.DictReader(open(os.path.join(HERE, f'ciphertext_draft_{i}.tsv')), delimiter='\t'):
        if r['line'][0] in BLOCKS:
            signs[r['line'][0]].append(r['sign'] if r['confidence'] == 'H' else '?')
gloss = collections.defaultdict(list)
for i in INS:
    for r in csv.DictReader(open(os.path.join(HERE, f'gloss_{i}.tsv')), delimiter='\t'):
        if r['block'] in BLOCKS: gloss[r['block']] += r['normalised'].split()

def is_word(s): return s.isdigit() and int(s) >= 10

def align(masked_h=None):
    """-> {block: [(sign, letter-or-'')...]} with every non-H code (and masked_h) uniquified."""
    prior = {c: collections.Counter({v: 1}) for c, v in HKEY.items() if c != masked_h}
    out = {}
    for b in BLOCKS:
        toks = []
        for k, s in enumerate(signs[b]):
            if is_word(s): toks.append('%' + s)
            elif s in HKEY and s != masked_h: toks.append('@' + s)
            else: toks.append(f'@{s}#{b}{k}')
        prep, res, _, _ = IA.run_align([{'plain_raw': ' '.join(gloss[b]), 'cipher_raw': ' '.join(toks)}], prior=prior,
                                       code_prefix='@', max_chunk=12)
        letters = prep[0][3]
        out[b] = [(s, fold(letters[c[0]:c[1]]) if c and c[1] > c[0] else '') for s, c in zip(signs[b], res[0])]
    return out

def lobo(pos):
    """pos: {block: [letters at the label's scored positions]} -> (hits, n, folds, overall majority)."""
    hits = n = 0; folds = {}
    for b in BLOCKS:
        if not pos.get(b): continue
        fit = collections.Counter(x for o in BLOCKS if o != b for x in pos.get(o, []))
        if not fit: continue
        top = sorted(fit.items(), key=lambda kv: (-kv[1], kv[0]))[0][0]
        h = sum(x == top for x in pos[b]); hits += h; n += len(pos[b]); folds[b] = (top, h, len(pos[b]))
    allc = collections.Counter(x for b in BLOCKS for x in pos.get(b, []))
    maj = sorted(allc.items(), key=lambda kv: (-kv[1], kv[0]))[0][0] if allc else ''
    return hits, n, folds, maj

def label_pos(al, lab):
    return {b: [x for s, x in al[b] if s == lab and x] for b in BLOCKS}

def pool(al):
    return {b: [x for s, x in al[b] if s != '?' and not is_word(s) and x] for b in BLOCKS}

def null(al, counts, seed0=0):
    pl = pool(al); accs = []
    for d in range(1, DRAWS + 1):
        rnd = random.Random(seed0 * 1000 + d)
        pos = {b: rnd.sample(pl[b], counts[b]) for b in BLOCKS if counts.get(b)}
        h, n, _, _ = lobo(pos); accs.append(h / n if n else 0.0)
    accs.sort(); return sum(accs) / len(accs), accs[int(0.95 * DRAWS) - 1], accs[-1]

def main():
    base = align()
    # sanity: masked alignment's R on H codes
    hh = sum(1 for b in BLOCKS for s, x in base[b] if s in HKEY and x == HKEY[s])
    hn = sum(1 for b in BLOCKS for s, x in base[b] if s in HKEY and x)
    rows = [('sanity_R_H', f'{hh / hn:.3f}', f'{hh}/{hn}', '', '', '', '', '')]
    frows = []
    cache = {}
    for lab, cand, pcode, pcode2 in LABELS:
        pos = label_pos(base, lab)
        counts = {b: len(pos[b]) for b in BLOCKS}
        h, n, folds, maj = lobo(pos)
        acc = h / n if n else 0.0
        mean, p95, mx = null(base, counts)
        for b, (t, fh, fn) in folds.items(): frows.append((lab, b, t, fh, fn))
        powers = []
        for pc in [pcode] + ([pcode2] if pcode2 else []):
            if pc not in cache: cache[pc] = align(masked_h=pc)
            pal = cache[pc]; ppos = label_pos(pal, pc)
            flat = [(b, x) for b in BLOCKS for x in ppos[b]]
            beat = fitok = 0; accs = []
            for s in range(1, SUBS + 1):
                rnd = random.Random(s)
                sub = flat if len(flat) <= n else rnd.sample(flat, n)
                sp = collections.defaultdict(list)
                for b, x in sub: sp[b].append(x)
                ph, pn, pf, pmaj = lobo(sp); pacc = ph / pn if pn else 0.0
                _, pp95, _ = null(pal, {b: len(sp[b]) for b in BLOCKS}, seed0=s)
                beat += pacc > pp95; fitok += pmaj == HKEY[pc]; accs.append(pacc)
            ok = beat >= 11 and fitok >= 11
            powers.append((pc, HKEY[pc], min(len(flat), n), beat, fitok, sorted(accs)[SUBS // 2], ok))
        pw = powers[0][-1]
        if not pw: verdict = 'too-short'
        elif acc > p95 and maj == cand: verdict = 'candidate-S'
        elif acc > p95: verdict = f'candidate-S-at-{maj}(flag)'
        else: verdict = 'fails-held-out'
        rows.append((lab, cand, f'{h}/{n}={acc:.3f}', f'{mean:.3f}/{p95:.3f}/{mx:.3f}', maj,
                     '; '.join(f'{pc}={v} n{pn} beat{bt}/20 fit{ft}/20 med{md:.3f} {"PASS" if ok else "FAIL"}'
                               for pc, v, pn, bt, ft, md, ok in powers), 'PASS' if pw else 'FAIL', verdict))
    res = 'label\tcandidate\tlobo_acc\tnull_mean/p95/max\tall_block_majority\tpower\tpower_gate\tverdict\n' + \
          ''.join('\t'.join(map(str, r)) + '\n' for r in rows)
    fol = 'label\theld_out_block\tfit_letter\thits\tn\n' + ''.join('\t'.join(map(str, r)) + '\n' for r in frows)
    rp, fp = os.path.join(HERE, 'mat_ka_result.tsv'), os.path.join(HERE, 'mat_ka_folds.tsv')
    if '--check' in sys.argv:
        stale = open(rp).read() != res or open(fp).read() != fol
        print('STALE' if stale else 'OK'); sys.exit(1 if stale else 0)
    open(rp, 'w').write(res); open(fp, 'w').write(fol); print(res + '\n' + fol)

if __name__ == '__main__':
    main()
