#!/usr/bin/env python3
"""MQS-SORTER-BOX known-answer control (pre-registered in tools/tests/PREREG-MQS-SORTER-BOX.md before this ran): does a missed sign
or a split box, saved by the sign sorter's rules, reach signs.tsv as a box on the right sign? Synthetic lines, simulated person
(the page's save rules replicated here, +-3 px jitter), real apply chain (sign_sorter_apply.py -> sorter_apply_recuts.py --added).
A plumbing control: it does not measure a person. Writes tools/tests/RESULTS-MQS-SORTER-BOX.tsv.
  python3 tools/tests/mqs_sorter_box_control.py [--seeds 20]"""
import argparse, contextlib, csv, io, json, random, sys, tempfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from PIL import Image, ImageDraw
import sign_sorter_apply as sa
import sorter_apply_recuts as ar

N, MISS, MERGE, J = 24, 2, 2, 3


def iou(a, b):
    ix = max(0, min(a[0] + a[2], b[0] + b[2]) - max(a[0], b[0])); iy = max(0, min(a[1] + a[3], b[1] + b[3]) - max(a[1], b[1]))
    u = a[2] * a[3] + b[2] * b[3] - ix * iy
    return ix * iy / u if u else 0.0


def coverage(truth, boxes):
    """share of truth boxes matched one-to-one (greedy by IoU) by a box at IoU >= 0.5"""
    pairs = sorted(((iou(t, b), i, j) for i, t in enumerate(truth) for j, b in enumerate(boxes)), reverse=True)
    ti, bj, n = set(), set(), 0
    for v, i, j in pairs:
        if v < .5:
            break
        if i not in ti and j not in bj:
            ti.add(i); bj.add(j); n += 1
    return n / len(truth)


def rect_quad(b):
    x, y, w, h = b
    return [[x, y], [x + w, y], [x + w, y + h], [x, y + h]]


def one(seed, mode, root):
    R = random.Random(seed); truth, x = [], 20
    for _ in range(N):
        w, h = R.randint(18, 30), R.randint(26, 36); truth.append([x, 40 - h // 2 + R.randint(-2, 2), w, h]); x += w + R.randint(6, 14)
    W = x + 20; im = Image.new('L', (W, 90), 250); g = ImageDraw.Draw(im)
    for tx, ty, tw, th in truth:   # random strokes inside each truth box, touching its edges
        g.line((tx, ty, tx + tw - 1, ty + th - 1), fill=0, width=3); g.line((tx, ty + th - 1, tx + tw - 1, ty), fill=0, width=3)
        for _ in range(2):
            g.line((tx + R.randint(0, tw - 1), ty + R.randint(0, th - 1), tx + R.randint(0, tw - 1), ty + R.randint(0, th - 1)), fill=0, width=2)
    d = Path(tempfile.mkdtemp(dir=root)); (d / 'pages').mkdir(); im.save(d / 'pages' / 'L01.png')
    idx = list(range(N - 1)); R.shuffle(idx); merged = []
    for i in idx:   # MERGE non-overlapping adjacent pairs
        if len(merged) < MERGE and all(abs(i - m) > 1 for m in merged):
            merged.append(i)
    rest = [i for i in range(N) if all(i not in (m, m + 1) for m in merged)]; missed = R.sample(rest, MISS)
    boxes, origin = [], {}   # machine boxes: sid -> box
    for i in range(N):
        if i in missed or any(i == m + 1 for m in merged):
            continue
        if i in merged:
            a, b = truth[i], truth[i + 1]; l, t = a[0], min(a[1], b[1])
            bx = [l, t, b[0] + b[2] - l, max(a[1] + a[3], b[1] + b[3]) - t]
        else:
            bx = list(truth[i])
        sid = 'L01_%03d' % (len(boxes) + 1); boxes.append((sid, bx)); origin[i] = sid
    with open(d / 'signs.tsv', 'w') as f:
        f.write('sid\tpage\tline\tpos\tx\ty\tw\th\n')
        for k, (sid, b) in enumerate(boxes):
            f.write('%s\tL01\tL01\t%d\t%d\t%d\t%d\t%d\n' % ((sid, k + 1) + tuple(b)))
    with open(d / 'labels.tsv', 'w') as f:
        f.write('sid\tsign\n' + ''.join('%s\tA\n' % s for s, _ in boxes))
    db = d / 'db'; (db / 'recuts').mkdir(parents=True); (db / 'added').mkdir()
    jit = lambda b: [b[0] + R.randint(-J, J), b[1] + R.randint(-J, J), max(3, b[2] + R.randint(-J, J)), max(3, b[3] + R.randint(-J, J))]
    near = lambda i: origin.get(i - 1) or origin.get(i + 1) or boxes[0][0]   # the tile the person opened the editor from
    adds = []
    for m in merged:   # split: recut to the left sign, the rest of the merged box added (the page's splitRest rule)
        sid = origin[m]; m0 = dict(boxes)[sid]; k = jit(truth[m]); k[0] = m0[0] if abs(k[0] - m0[0]) <= J else k[0]
        json.dump({'sid': sid, 'page': 'L01', 'x': k[0], 'y': k[1], 'w': k[2], 'h': k[3], 'old': m0, 'at': 't', 'quad': rect_quad(k), 'mask': []},
                  open(db / 'recuts' / (sid + '.json'), 'w'))
        r = k[0] + k[2]; right, left = m0[0] + m0[2] - r, k[0] - m0[0]
        rest_ = [r, m0[1], right, m0[3]] if right >= left else [m0[0], m0[1], left, m0[3]]
        adds.append((sid, 'split', rest_))
    for i in missed:
        adds.append((near(i), 'missed', jit(truth[i])))
    if mode == 'misplaced':
        adds = [(s, k, [R.randint(0, W - b[2]), b[1], b[2], b[3]]) for s, k, b in adds]
    if mode != 'off':
        n = {}
        for s, k, b in adds:
            n[s] = n.get(s, 0) + 1; aid = '%s+%d' % (s, n[s])
            json.dump({'id': aid, 'from': s, 'kind': k, 'page': 'L01', 'x': b[0], 'y': b[1], 'w': b[2], 'h': b[3], 'quad': rect_quad(b), 'mask': [], 'at': 't'},
                      open(db / 'added' / (aid.replace('+', '_43_') + '.json'), 'w'))
    with contextlib.redirect_stdout(io.StringIO()):
        sa.main(['--labels', str(d / 'labels.tsv'), '--db', str(db), '--out', str(d / 'settled.tsv')])
        a = ['--recuts', str(d / 'recuts.tsv'), '--signs', str(d / 'signs.tsv'), '--pages', str(d / 'pages'), '--tiles', str(d / 'tiles')]
        rc = ar.main(a + (['--added', str(d / 'added.tsv')] if (d / 'added.tsv').exists() else []))
    final = [[int(r[k]) for k in 'xywh'] for r in csv.DictReader(open(d / 'signs.tsv'), delimiter='\t')]
    return coverage(truth, final), rc, len(final)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0]); ap.add_argument('--seeds', type=int, default=20)
    ap.add_argument('--out', default=str(Path(__file__).resolve().parent / 'RESULTS-MQS-SORTER-BOX.tsv')); a = ap.parse_args(argv)
    root = tempfile.mkdtemp(); rows = []
    for s in range(1, a.seeds + 1):
        r = {m: one(s, m, root) for m in ('known', 'off', 'misplaced')}
        rows.append([s] + [round(r[m][0], 4) for m in ('known', 'off', 'misplaced')] + [r['known'][1], r['known'][2]])
    with open(a.out, 'w') as f:
        f.write('seed\tcoverage_known\tcoverage_off\tcoverage_misplaced\tapply_exit\tfinal_boxes\n')
        f.writelines('\t'.join(map(str, r)) + '\n' for r in rows)
    mean = lambda c: sum(r[c] for r in rows) / len(rows)
    above = sum(r[1] > max(r[2], r[3]) for r in rows)
    gate = mean(1) >= .95 and above == len(rows)
    print('known %.3f (min %.3f)  off %.3f  misplaced %.3f  above both nulls %d/%d  gate %s' % (
        mean(1), min(r[1] for r in rows), mean(2), mean(3), above, len(rows), 'PASS' if gate else 'FAIL'))
    return 0 if gate else 3


if __name__ == '__main__':
    sys.exit(main())
