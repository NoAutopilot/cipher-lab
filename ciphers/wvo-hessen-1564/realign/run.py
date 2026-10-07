#!/usr/bin/env python3
"""WVO-REALIGN (7 Oct 2026): re-run the f.23 gloss alignment on the owner's settled signs (PREREG-WVO-REALIGN.md).
  python3 realign/run.py real       pairs, alignment (+ PREREG-R9 derangement control), key, tile figures -> realign/
  python3 realign/run.py control N  N within-row label permutations, seed 1564, full pipeline -> realign/control.json
Run from the target folder or anywhere."""
import csv, json, os, random, subprocess, sys, tempfile
from collections import Counter, defaultdict
D = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(D); R = os.path.dirname(os.path.dirname(T))
rd = lambda p: list(csv.DictReader(open(os.path.join(T, p)), delimiter='\t'))
gloss = {r['row']: r['gloss'].replace('|', ' ') for r in rd('r9align/gloss_reconciled.tsv')}
rows = sorted(gloss)
st = {r['sid']: r for r in rd('sorter/settled_labels.tsv')}
SKIP = {'aside', 'bad-cut'}
order = defaultdict(list)
for r in rd('r9align/tile_order.tsv'):
    order[r['row']].append(r['sid'])
CLEAR = 'f23_C01_01_014'


def label(sid):
    if sid == CLEAR:
        return 'EL'
    s = st[sid]
    return '@X' + sid[-6:].replace('_', '') if s['status'] in SKIP else '@' + s['new_sign']


def pipeline(labs, out, shuffle=0):
    """labs: row -> list of labels (x order). Returns figures; writes files under out."""
    os.makedirs(out, exist_ok=True)
    pp, ap, kp = (os.path.join(out, n) for n in ('pairs.tsv', 'align.tsv', 'key_raw.tsv'))
    with open(pp, 'w') as f:
        f.write('plain_line\tplain_raw\tcipher_line\tcipher_raw\n')
        for r in rows:
            f.write('%s\t%s\t%s\t%s\n' % (r, gloss[r], r, ' '.join(labs[r])))
    cmd = [sys.executable, os.path.join(R, 'tools/interlinear_align.py'), 'align', pp, ap, kp, '--code-prefix', '@',
           '--seg-bonus', '0', '--keep-fs', '--null-cost', '-1.0']
    if shuffle:
        cmd += ['--shuffle', str(shuffle), '--seed', '1564', '--shuffle-out', os.path.join(out, 'derangement.json')]
    log = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    al = list(csv.DictReader(open(ap), delimiter='\t'))
    per, rws, tiles = defaultdict(Counter), defaultdict(lambda: defaultdict(set)), []
    for a in al:
        lab = a['raw']
        if a['kind'] != 'code' or lab.startswith('@X'):
            tiles.append((a, None)); continue
        sg = lab[1:]
        tiles.append((a, sg))
        if a['plain_chunk']:
            per[sg][a['plain_chunk']] += 1
            rws[sg][a['plain_chunk']].add(a['cipher_line'])
    key, cons = {}, 0
    for sg in {s for _, s in tiles if s}:
        if not per[sg]:
            key[sg] = ('', 'M', 'none aligned'); continue
        (top, n), tot = per[sg].most_common(1)[0], sum(per[sg].values())
        ok = n >= 2 and len(rws[sg][top]) >= 2 and n >= 0.6 * tot
        cons += ok
        key[sg] = (top, 'C' if ok else 'M', '%d/%d aligned, %d rows; others %s' % (
            n, tot, len(rws[sg][top]), ','.join('%s:%d' % kv for kv in per[sg].most_common()[1:]) or '-'))
    fig = Counter()
    for a, sg in tiles:
        if sg is None:
            fig['clear' if a['kind'] == 'clear' else 'aside_badcut'] += 1; continue
        v, g, _ = key[sg]
        if g == 'C':
            fig['C'] += 1
            fig['C_agree' if a['plain_chunk'] == v else ('C_unaligned' if not a['plain_chunk'] else 'C_conflict')] += 1
        else:
            fig['M_valued' if v else 'M_blank'] += 1
    fig['CONSISTENT'] = cons
    fig['key_C'] = sum(1 for v in key.values() if v[1] == 'C'); fig['key_M'] = len(key) - fig['key_C']
    return dict(fig), key, al, log


if sys.argv[1] == 'real':
    labs = {r: [label(s) for s in order[r]] for r in rows}
    fig, key, al, log = pipeline(labs, D, shuffle=1000)
    with open(os.path.join(D, 'key.tsv'), 'w') as f:
        f.write('code\tvalue\tgrade\tsource\tnote\n')
        for sg in sorted(key):
            f.write('%s\t%s\t%s\tf.23 gloss re-aligned on settled signs (WVO-REALIGN)\t%s\n' % ((sg,) + key[sg]))
    old = {r['sid']: r for r in rd('settled/compare.tsv')}
    with open(os.path.join(D, 'tile_letters.tsv'), 'w') as f, open(os.path.join(D, 'ciphertext.tsv'), 'w') as g:
        f.write('sid\trow\tidx\tsettled_sign\tgloss_letter_r10\tgloss_letter_realign\tvalue_before\tgrade_before\tvalue_after\tgrade_after\n')
        g.write('line\tpos\tsign\tconf\n')
        for a in al:
            sid = order[a['cipher_line']][int(a['idx'])]
            o = old[sid]
            if a['kind'] == 'clear':
                sign, v, gr = '[PLAIN:E.L.]', 'E.L.', 'clear'
            elif a['raw'].startswith('@X'):
                sign, v, gr = 'X-' + st[sid]['status'], '', 'U'
            else:
                sign = a['raw'][1:]; v, gr, _ = key[sign]
            g.write('%s\t%d\t%s\t\n' % (a['cipher_line'], int(a['idx']) + 1, sign))
            f.write('\t'.join([sid, a['cipher_line'], a['idx'], o['settled_sign'], o['gloss_letter'], a['plain_chunk'],
                               o['settled_value'], o['settled_grade'], v, gr]) + '\n')
    json.dump(fig, open(os.path.join(D, 'figures.json'), 'w'), indent=1, sort_keys=True)
    print(json.dumps(fig, sort_keys=True)); print(log.strip().splitlines()[-3:])
else:
    n = int(sys.argv[2]); rng = random.Random(1564); draws = []
    tmp = tempfile.mkdtemp()
    for i in range(n):
        labs = {}
        for r in rows:
            L = [label(s) for s in order[r]]
            idx = [k for k, x in enumerate(L) if x != 'EL']
            vals = [L[k] for k in idx]; rng.shuffle(vals)
            for k, x in zip(idx, vals):
                L[k] = x
            labs[r] = L
        fig, *_ = pipeline(labs, tmp)
        draws.append(fig)
    real = json.load(open(os.path.join(D, 'figures.json')))
    out = {'seed': 1564, 'n': n}
    for k in ('C_agree', 'CONSISTENT', 'C'):
        xs = sorted(d.get(k, 0) for d in draws)
        out[k] = {'real': real.get(k, 0), 'mean': round(sum(xs) / n, 2), 'p95': xs[int(0.95 * n) - 1 if n >= 20 else -1],
                  'max': xs[-1], 'p': (1 + sum(x >= real.get(k, 0) for x in xs)) / (n + 1), 'draws': xs}
    json.dump(out, open(os.path.join(D, 'control.json'), 'w'), indent=1)
    print({k: {kk: vv for kk, vv in v.items() if kk != 'draws'} for k, v in out.items() if isinstance(v, dict)})
