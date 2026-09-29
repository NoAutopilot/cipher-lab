#!/usr/bin/env python3
"""Pick the frozen threshold per score (c1, c2, pair) on the CALIBRATION set only (p 0.15 rows, x 0 and 0.13):
maximise balanced accuracy of NULL-IID against the four brief language designs (FR-HOMO, EN-HOMO, PT-HOMO,
FR-SYLL). Writes threshold.json. Also the target's percentile in every calibration cell."""
import json, glob, dcore, collections
rows = [json.loads(l) for f in sorted(glob.glob('calib_*.jsonl')) for l in open(f)]
LANG = {'FR-HOMO', 'EN-HOMO', 'PT-HOMO', 'FR-SYLL'}
cal = [r for r in rows if r['p'] == 0.15 and (r['design'] in LANG or r['design'] == 'NULL-IID')]
th = {}
for w in ('c1', 'c2', 'pair'):
    best = None
    for t in [x / 10 for x in range(-50, 200)]:
        tl = sum(dcore.score(r['f'], w) > t for r in cal if r['design'] in LANG) / sum(r['design'] in LANG for r in cal)
        tn = sum(dcore.score(r['f'], w) <= t for r in cal if r['design'] == 'NULL-IID') / sum(r['design'] == 'NULL-IID' for r in cal)
        if best is None or (tl + tn) / 2 > best[0]: best = ((tl + tn) / 2, t, tl, tn)
    th[w] = dict(t=best[1], bal_acc=round(best[0], 3), lang_recall=round(best[2], 3), null_recall=round(best[3], 3))
print(th); json.dump(th, open('threshold.json', 'w'), indent=1)
T = json.load(open('target_score.json'))['withX']['score']
tgt = {w: sorted(v)[2] for w, v in T.items()}
by = collections.defaultdict(list)
for r in rows: by[(r['p'], r['xnull'], r['design'])].append(r['f'])
print('target median score', tgt)
for k in sorted(by):
    print(k, ' '.join(f"{w}: {sum(dcore.score(f, w) <= tgt[w] for f in by[k]) / len(by[k]):.3f}" for w in ('c1', 'c2', 'pair')))
