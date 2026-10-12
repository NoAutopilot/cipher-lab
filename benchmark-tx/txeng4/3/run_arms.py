#!/usr/bin/env python3
"""TXE4-3 ATLAS-NCA units 3-4 (12 Oct 2026, account 3): run the arms of benchmark-tx/PREREG-txeng4-3.md through
tools/glyph_atlas.py classify and write tx_bench outputs as per-line BOX SEQUENCES of top-1 codes (atlas page f178v row li
= letter line Lli, f179r rows 1-3 = L01-03; boxes in x order; a '_'/'_held' top-1 is written as '_', never the line read).
No truth is read here; scoring is a separate step (score.py) that runs tools/tx_bench.py once per output.

  grid        the 18 dev settings (features x NCA dim x k) on the AGREED LABELS -> runs/grid_*.tsv, out/dev_*.tsv
  eval ARGS   the eval arms with the frozen setting (--features F --metric-dim D --knn K): A0, A0', A1, A2, A3 seeds 1-20,
              A4 (leave-one-line-out), A5 -> runs/*.tsv, out/eval_<arm>.tsv (eval_heldout lines), out/f152r_<arm>.tsv
Run from the repo root."""
import csv, os, sys, json, subprocess, collections, hashlib, random
A = 'ciphers/nevers-birago-fr3251-1572/atlas'; W = 'benchmark-tx/txeng4/3'; L = f'{W}/labels'
R, O = f'{W}/runs', f'{W}/out'; os.makedirs(R, exist_ok=True); os.makedirs(O, exist_ok=True)
CACHE = os.environ.get('TXE4_TOPO_CACHE', f'{W}/topo_cache.npy')
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
HOLD = ['--holdout', 'f152r_', '--holdout', 'f178r_', '--holdout', 'f178v_', '--holdout', 'f179r_']
DEV = [f'f178v_L{i:02d}' for i in range(1, 13)]
EVAL = [f'f178v_L{i:02d}' for i in range(13, 24)] + [f'f179r_L{i:02d}' for i in (1, 2, 3)]
XB = {'f152r_L01': lambda cx: cx > 2520, 'f152r_L04': lambda cx: cx < 2460}   # TXE3-7 map_f152r.py, prose bounds, unchanged
F152 = {2: 'f152r_L01', 3: 'f152r_L02', 4: 'f152r_L03', 5: 'f152r_L04'}
SIGNS = rd(f'{A}/signs.tsv')


def classify(tag, labels_json, train, extra, page='all'):
    tsv = f'{R}/{tag}.tsv'
    if os.path.exists(tsv):
        return rd(tsv)
    cmd = [sys.executable, 'tools/glyph_atlas.py', 'classify', '--out', A, '--labels', labels_json, '--page', page,
           '--tsv', tsv, '--topk', '3'] + extra
    if train:
        cmd += ['--train-labels', train, '--only-train-labels']
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit(f'{tag}: {r.stderr[-800:]}')
    return rd(tsv)


def box_sequences(res, lines, page_of_line=None):
    """{line: [(pos, code)]} from classify rows for the named letter lines (box sequences in x order)."""
    code = {r['box']: r['code'] for r in res}
    out = {}
    for line in lines:
        page, li = line.split('_L'); li = int(li)
        if line in F152.values():
            li = {v: k for k, v in F152.items()}[line]
        bx = sorted([s for s in SIGNS if s['page'] == page and int(s['line']) == li], key=lambda s: int(s['x']))
        if line in XB:
            bx = [s for s in bx if XB[line](int(s['x']) + int(s['w']) / 2)]
        seq = []
        for k, s in enumerate(bx, 1):
            c = code.get(s['sid'], '_')
            seq.append((k, '_' if c in ('', '_', '_held') else c))
        out[line] = seq
    return out


def write_out(path, seqs):
    with open(path, 'w') as f:
        f.write('line\tpos\tsign\n')
        for line in seqs:
            for k, c in seqs[line]:
                f.write(f'{line}\t{k}\t{c}\n')


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def grid():
    man = []
    for feats in ('hog', 'hog+zone+topo'):
        for dim in (16, 32, 64):
            for k in (3, 5, 9):
                tag = f'grid_{feats.replace("+", "")}_d{dim}_k{k}'
                res = classify(tag, f'{L}/labels_empty.json', f'{L}/agreed_labels.tsv',
                               HOLD + ['--features', feats, '--metric', 'nca', '--metric-dim', str(dim), '--knn', str(k),
                                       '--topo-cache', CACHE])
                out = f'{O}/dev_{tag}.tsv'; write_out(out, box_sequences(res, DEV))
                man.append(f'{sha(out)}  {out}'); print(tag, 'done', flush=True)
    open(f'{W}/SHA256SUMS.prescore.dev', 'w').write('\n'.join(man) + '\n')


def eval_arms(feats, dim, k):
    man = []
    base = ['--features', feats, '--metric', 'nca', '--metric-dim', str(dim), '--knn', str(k), '--topo-cache', CACHE]
    plain = ['--knn', str(k)]
    runs = {}
    # A0 / A0': the known-answer-named atlas (reference), labels.json voters with every no.87 page held out; f152r by
    # --exclude-page on a separate call
    for tag, lj in (('A0', f'{A}/labels.json'), ('A0p', f'{A}/labels_boxmapLA.json')):
        runs[tag] = classify(tag, lj, None, ['--knn', '5'] + HOLD)
        runs[tag + '_f152r'] = classify(tag + '_f152r', lj, None, ['--knn', '5', '--exclude-page'], page='f152r')
    runs['A1'] = classify('A1', f'{L}/labels_empty.json', f'{L}/agreed_labels.tsv', HOLD + ['--knn', '5'])
    runs['A2'] = classify('A2', f'{L}/labels_empty.json', f'{L}/agreed_labels.tsv', HOLD + base)
    # A3: permuted labels, seeds 1-20
    rows = rd(f'{L}/agreed_labels.tsv')
    for s in range(1, 21):
        codes = [r['code'] for r in rows]; random.Random(s).shuffle(codes)
        p = f'{L}/null_{s}.tsv'
        with open(p, 'w') as f:
            f.write('box\tcode\n'); f.writelines(f"{r['box']}\t{c}\n" for r, c in zip(rows, codes))
        runs[f'A3s{s}'] = classify(f'A3s{s}', f'{L}/labels_empty.json', p, HOLD + base)
    # A5: secure_tokens minus f152r (beside; gated by the join check in score step)
    sec = [r for r in rd(f'{A}/secure_tokens.tsv') if r['page'] != 'f152r']
    with open(f'{L}/a5_train.tsv', 'w') as f:
        f.write('box\tcode\n'); f.writelines(f"{r['sid']}\t{r['code']}\n" for r in sec)
    runs['A5'] = classify('A5', f'{L}/labels_empty.json', f'{L}/a5_train.tsv', HOLD + base)
    # A4: agreed labels + no.87 A/B tiles, leave-one-line-out per eval line (the evaluated line's tiles out of fit and vote)
    no87 = rd(f'{L}/no87_agreed.tsv')
    a4 = {}
    for line in EVAL:
        p = f'{L}/a4_train_{line}.tsv'
        with open(p, 'w') as f:
            f.write('box\tcode\n'); f.writelines(f"{r['box']}\t{r['code']}\n" for r in rows)
            f.writelines(f"{r['box']}\t{r['code']}\n" for r in no87 if r['line'] != line)
        page, li = line.split('_L')
        res = classify(f'A4_{line}', f'{L}/labels_empty.json', p,
                       ['--holdout', 'f152r_', '--holdout', f'{page}_{int(li):02d}_'] + base)
        a4.update(box_sequences(res, [line]))
    # A4 on f152r: all no.87 tiles in
    p = f'{L}/a4_train_all.tsv'
    with open(p, 'w') as f:
        f.write('box\tcode\n'); f.writelines(f"{r['box']}\t{r['code']}\n" for r in rows + no87)
    res = classify('A4_f152r', f'{L}/labels_empty.json', p, ['--holdout', 'f152r_'] + base)
    a4f = box_sequences(res, list(F152.values()))
    for tag, res in runs.items():
        if tag.endswith('_f152r'):
            out = f'{O}/f152r_{tag[:-6]}.tsv'; write_out(out, box_sequences(res, list(F152.values())))
        else:
            out = f'{O}/eval_{tag}.tsv'; write_out(out, box_sequences(res, EVAL)); man.append(f'{sha(out)}  {out}')
            if tag not in ('A0', 'A0p'):
                out = f'{O}/f152r_{tag}.tsv'; write_out(out, box_sequences(res, list(F152.values())))
        man.append(f'{sha(out)}  {out}')
    write_out(f'{O}/eval_A4.tsv', a4); man.append(f'{sha(f"{O}/eval_A4.tsv")}  {O}/eval_A4.tsv')
    write_out(f'{O}/f152r_A4.tsv', a4f); man.append(f'{sha(f"{O}/f152r_A4.tsv")}  {O}/f152r_A4.tsv')
    # can-vary counts before any score: eval boxes whose top-1 differs A2 vs A1, A2 vs each A3 seed
    def codes(tag):
        return {k: c for line, seq in box_sequences(runs[tag], EVAL).items() for k, c in [((line, p), c) for p, c in seq]}
    c1, c2 = codes('A1'), codes('A2')
    nulls = [sum(1 for k in c2 if codes(f'A3s{s}')[k] != c2[k]) for s in range(1, 21)]
    can = dict(eval_boxes=len(c2), A2_ne_A1=sum(1 for k in c2 if c1[k] != c2[k]),
               A2_ne_null=dict(min=min(nulls), mean=sum(nulls) / 20, max=max(nulls)),
               A2_blank=sum(1 for k in c2 if c2[k] == '_'), A1_blank=sum(1 for k in c2 if c1[k] == '_'))
    json.dump(can, open(f'{W}/can_vary.json', 'w'), indent=1); print(json.dumps(can))
    open(f'{W}/SHA256SUMS.prescore.eval', 'w').write('\n'.join(sorted(set(man))) + '\n')


if __name__ == '__main__':
    if sys.argv[1] == 'grid':
        grid()
    else:
        eval_arms(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
