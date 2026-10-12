#!/usr/bin/env python3
"""TXE4-10 RECOG-CUT unit 1 (PREREG-txeng4-10.md 'Labels'): machine-only labels for TXE3-6's seg/sign TRAIN boxes.
1. consensus of six committed reads (reconcile_passes.py --vote; a label position has vote_share >= 0.83, i.e. 5 of 6);
2. join round 1: box_token_align.py --lam 0 --no-loo (width only, a seed) -> provisional labels on 1:1 label positions;
3. round-1 RecKNN (glyph_atlas.RecKNN, k 5) leave-one-out top-3 over every train box -> topk1.tsv, top1.tsv;
4. join round 2: box_token_align.py --topk topk1.tsv (--loo) with --check-labels top1.tsv --check-bound (join_check);
5. labels.tsv: boxes 1:1 at the same position in both rounds, at a label position, label a key code.
No truth file is opened. Test lines are never read. Writes everything under benchmark-tx/txeng4/10/labels/.
  python3 benchmark-tx/txeng4/10/labels.py [--uncheckable-fallback]
"""
import csv, collections, json, os, subprocess, sys
import numpy as np
ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(ROOT, '..', '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'tools'))
sys.path.insert(0, os.path.join(REPO, 'benchmark-tx/txeng3/6'))
from seg import TRAIN, TEST          # the TXE3-6 line split (L14 is in TEST there but has no truth; it is not used here)
import glyph_atlas as GA
SIX = ['benchmark-tx/outputs/vivonne1573-f102r-dev2/passA_sv.tsv', 'benchmark-tx/outputs/vivonne1573-f102r-dev2/passB_sv.tsv',
       'benchmark-tx/outputs/vivonne1573-f102r-dev2/passA_tl.tsv', 'benchmark-tx/outputs/vivonne1573-f102r-dev2/passB_tl.tsv',
       'benchmark-tx/outputs/vivonne1573-f102r-dev/passA_dv1.tsv', 'benchmark-tx/outputs/vivonne1573-f102r-dev/passB_dv1.tsv']
SEG = os.path.join(REPO, 'benchmark-tx/txeng3/6/seg/sign')
OUT = os.path.join(ROOT, 'labels')
LABEL_SHARE = 0.83
TRAIN_LINES = {f'f102r_{l}' for l in TRAIN}


def rd(p):
    return list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))


def wr(p, cols, rows):
    with open(p, 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows:
            f.write('\t'.join(str(r[c]) for c in cols) + '\n')


def sh(*cmd):
    r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True)
    open(os.path.join(OUT, 'commands.log'), 'a').write(' '.join(cmd) + '\n' + r.stdout + r.stderr + f'[exit {r.returncode}]\n')
    return r


def main():
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, 'commands.log'), 'w').close()
    key = {r['code'] for r in rd(os.path.join(REPO, 'ciphers/fr16104-vivonne-spain-1572/key.tsv'))}
    # 1. consensus
    vd = os.path.join(OUT, 'vote')
    os.makedirs(vd, exist_ok=True)
    r = sh(sys.executable, 'tools/reconcile_passes.py', *SIX, '--out-dir', vd, '--vote')
    if r.returncode:
        sys.exit(r.stdout + r.stderr)
    vote = [v for v in rd(os.path.join(vd, 'vote.tsv')) if v['line'] in TRAIN_LINES]
    read_p = os.path.join(OUT, 'consensus_read.tsv')
    wr(read_p, ['line', 'pos', 'sign', 'vote_share'], vote)
    label_pos = {(v['line'], v['pos']): v['sign'] for v in vote if float(v['vote_share']) >= LABEL_SHARE}
    # boxes -> box_token_align signs (page f102r, line NN, x in line coordinates)
    boxes = [b for b in rd(os.path.join(SEG, 'boxes.tsv')) if b['line'] in TRAIN_LINES]
    srows = {s['sid']: s for s in rd(os.path.join(SEG, 'signs.tsv'))}
    signs_p = os.path.join(OUT, 'signs_line.tsv')
    wr(signs_p, ['sid', 'page', 'line', 'x', 'w', 'h', 'rh', 'rw'],
       [dict(sid=b['sid'], page='f102r', line=int(b['line'].split('_L')[1]), x=b['x_line'], w=b['w'], h=b['h'],
             rh=srows[b['sid']]['rh'], rw=srows[b['sid']]['rw']) for b in boxes])
    # 2. round 1, width only
    map1 = os.path.join(OUT, 'map1.tsv')
    r = sh(sys.executable, 'tools/box_token_align.py', '--signs', signs_p, '--read', read_p, '--lam', '0', '--no-loo',
           '--out', map1, '--lines-out', os.path.join(OUT, 'map1_lines.tsv'))
    if r.returncode:
        sys.exit(r.stdout + r.stderr)
    m1 = {x['sid']: x for x in rd(map1) if x['op'] == '1:1'}
    prov = {sid: label_pos[(x['line'], x['pos'])] for sid, x in m1.items()
            if (x['line'], x['pos']) in label_pos and label_pos[(x['line'], x['pos'])] in key}
    rep = [f'consensus: {len(vote)} train positions, {len(label_pos)} at >= 5 of 6; train boxes {len(boxes)}',
           f'round 1 (lam 0): 1:1 boxes {len(m1)}, provisional labels {len(prov)} ({len(set(prov.values()))} codes)']
    # 3. round-1 RecKNN, leave-one-out top-3 over every train box
    bm_all = np.load(os.path.join(SEG, 'bitmaps.npz'))['signs']
    allrows = rd(os.path.join(SEG, 'signs.tsv'))
    idx = {s['sid']: i for i, s in enumerate(allrows)}
    ex = [b['sid'] for b in boxes if b['sid'] in prov]
    knn1 = GA.RecKNN(bm_all[[idx[s] for s in ex]], [allrows[idx[s]] for s in ex], [prov[s] for s in ex], k=5)
    exi = {s: i for i, s in enumerate(ex)}
    q = [b['sid'] for b in boxes]
    tk = knn1.topk(bm_all[[idx[s] for s in q]], [float(allrows[idx[s]]['rh']) for s in q],
                   [float(allrows[idx[s]]['rw']) for s in q], k=3, exclude=[{exi[s]} if s in exi else None for s in q])
    topk_p, top1_p = os.path.join(OUT, 'topk1.tsv'), os.path.join(OUT, 'top1.tsv')
    wr(topk_p, ['box', 'code', 'k1', 's1', 'k2', 's2', 'k3', 's3'],
       [dict(box=s, code=t[0][0], k1=t[0][0], s1=f'{t[0][1]:.3f}', k2=t[1][0] if len(t) > 1 else '_',
             s2=f'{t[1][1]:.3f}' if len(t) > 1 else '', k3=t[2][0] if len(t) > 2 else '_',
             s3=f'{t[2][1]:.3f}' if len(t) > 2 else '') for s, t in zip(q, tk)])
    wr(top1_p, ['sid', 'label'], [dict(sid=s, label=t[0][0]) for s, t in zip(q, tk)])
    loo_acc = sum(t[0][0] == prov[s] for s, t in zip(q, tk) if s in prov) / max(1, len(prov))
    rep.append(f'round-1 RecKNN: {len(ex)} exemplars, {len(knn1.codes)} codes; leave-one-out top-1 agreement with the '
               f'provisional label {loo_acc:.3f} (chance about {1 / len(knn1.codes):.3f})')
    # 4. round 2 with the top-3, --loo, and the bounded shift check (steered -> leave-one-out row)
    map2 = os.path.join(OUT, 'map2.tsv')
    r = sh(sys.executable, 'tools/box_token_align.py', '--signs', signs_p, '--read', read_p, '--topk', topk_p,
           '--check-labels', top1_p, '--check-bound', '--out', map2, '--lines-out', os.path.join(OUT, 'map2_lines.tsv'))
    rep.append('round 2: ' + r.stdout.strip().replace('\n', ' | '))
    verdict = {0: 'PASS', 2: 'FAIL', 3: 'UNCHECKABLE'}.get(r.returncode, f'exit {r.returncode}')
    r2 = sh(sys.executable, 'tools/join_check.py', '--map', map2, '--check-labels', top1_p, '--read', read_p, '--steered')
    rep.append(f'join_check --steered: exit {r2.returncode} | ' + r2.stdout.strip().replace('\n', ' | ')[:1500])
    # the check labels (top1) are the k1 of the --topk that steered the map, so the leave-one-out row is the one read
    # (PREREG step 5; R4a): --check-bound's own steered detection compares paths, so its PASS above is the in-sample row
    loo_verdict = {0: 'PASS', 2: 'FAIL', 3: 'UNCHECKABLE'}.get(r2.returncode, f'exit {r2.returncode}')
    rep.append(f'SHIFT CHECK, in-sample row (not the one read): {verdict}; leave-one-out row (READ): {loo_verdict}')
    verdict = loo_verdict
    dropped = []
    if verdict == 'FAIL':
        # R4a: drop the failing lines, list them, re-check once
        dropped = [l.split(':')[0].strip() for l in r2.stdout.splitlines() if ': fail placed=' in l]
        keep = sorted(ln for ln in TRAIN_LINES if ln not in dropped)
        map2 = os.path.join(OUT, 'map2b.tsv')
        r = sh(sys.executable, 'tools/box_token_align.py', '--signs', signs_p, '--read', read_p, '--topk', topk_p,
               '--lines', *keep, '--out', map2, '--lines-out', os.path.join(OUT, 'map2b_lines.tsv'))
        r2 = sh(sys.executable, 'tools/join_check.py', '--map', map2, '--check-labels', top1_p, '--read', read_p, '--steered')
        verdict = {0: 'PASS', 2: 'FAIL', 3: 'UNCHECKABLE'}.get(r2.returncode, f'exit {r2.returncode}')
        rep.append(f'RE-CHECK after dropping {dropped} (lines kept {len(keep)}): exit {r2.returncode} | '
                   + r2.stdout.strip().replace('\n', ' | ')[:1500])
    rep.append(f'SHIFT CHECK VERDICT (leave-one-out row, after at most one re-check): {verdict}; dropped lines {dropped}')
    # 5. labels: 1:1 at the same pos in both rounds, at a label position, a key code
    m2 = {x['sid']: x for x in rd(map2) if x['op'] == '1:1'}
    lab = {}
    for sid, x in m2.items():
        y = m1.get(sid)
        if y and y['pos'] == x['pos'] and (x['line'], x['pos']) in label_pos and label_pos[(x['line'], x['pos'])] in key:
            lab[sid] = label_pos[(x['line'], x['pos'])]
    mode = 'two-round'
    if verdict == 'UNCHECKABLE' and '--uncheckable-fallback' in sys.argv:
        # PREREG step 5 fallback: TXE3-6 labels.py's round-0 rule with reader consensus in place of truth
        cnt_c = collections.Counter(v['line'] for v in vote)
        byl = collections.defaultdict(list)
        for b in boxes:
            byl[b['line']].append(b)
        lab, kept = {}, []
        for ln, bs in byl.items():
            if len(bs) != cnt_c[ln]:
                continue
            if any(m1.get(b['sid'], {}).get('op') != '1:1' for b in bs):
                continue
            kept.append(ln)
            for b in sorted(bs, key=lambda b: int(b['pos'])):
                k = (ln, b['pos'])
                if k in label_pos and label_pos[k] in key:
                    lab[b['sid']] = label_pos[k]
        mode = f'round-0 fallback (count = consensus and round-1 all 1:1): lines {sorted(kept)}'
    wr(os.path.join(OUT, 'labels.tsv'), ['box', 'code'], [dict(box=s, code=c) for s, c in sorted(lab.items())])
    cnt = collections.Counter(lab.values())
    rep.append(f'LABELS ({mode}): {len(lab)} boxes, {len(cnt)} codes: ' + ', '.join(f'{c}:{n}' for c, n in cnt.most_common()))
    open(os.path.join(OUT, 'labels_report.txt'), 'w').write('\n'.join(rep) + '\n')
    print('\n'.join(rep))


if __name__ == '__main__':
    main()
