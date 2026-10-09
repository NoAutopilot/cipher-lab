#!/usr/bin/env python3
"""Offline test for `sign_sorter.py --oddness-audit` (MQS-SORTER, 9 Oct 2026). Run: python3 tools/tests/test_sign_sorter_oddness.py
Must catch: planted misfits among three visibly different sign shapes sit in the first 10% of their new pile (recall high, above the
shuffled p95). Must NOT flag: three piles of the same noise texture (no pile has a shape to be odd against): the recall does not beat the
shuffled order. The shuffled null can fail differently from the target: it only reorders tiles within a pile."""
import random, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import sign_sorter as ss
from PIL import Image, ImageDraw

fails = 0
def check(name, ok):
    global fails
    print('PASS' if ok else 'FAIL', name); fails += not ok

def make(d, shapes):
    d.mkdir(); im = Image.new('L', (1600, 100), 255); g = ImageDraw.Draw(im); rng = random.Random(3)
    rows, labs = [], []
    for i in range(60):
        x, fam = 10 + 25 * i, i % 3
        if shapes:
            j = rng.randint(0, 2)
            [lambda: g.line((x, 40 + j, x + 18, 70 - j), fill=0, width=3),
             lambda: g.ellipse((x + j, 42, x + 18, 68), outline=0, width=3),
             lambda: g.rectangle((x, 45 + j, x + 18, 52), fill=0)][fam]()
        else:
            for _ in range(40):
                px, py = rng.randint(x, x + 18), rng.randint(40, 70); g.point((px, py), fill=0)
        rows.append(f's{i:02d}\tp\t{x}\t38\t20\t34'); labs.append(f's{i:02d}\tF{fam}\tF{fam}')
    im.save(d / 'p.png')
    (d / 'signs.tsv').write_text('sid\tpage\tx\ty\tw\th\n' + '\n'.join(rows) + '\n')
    (d / 'labels.tsv').write_text('sid\tsign\tfamily\n' + '\n'.join(labs) + '\n')
    return str(d / 'signs.tsv'), str(d / 'labels.tsv'), str(d)

with tempfile.TemporaryDirectory() as t:
    t = Path(t)
    s, l, p = make(t / 'shapes', True)
    rows, sm = ss.oddness_audit(s, l, p, frac=0.1, kind='random', seeds=8)
    check('shapes: planted misfits first (mean recall >= 0.6, above the shuffled p95 in every seed)',
          sm['mean_recall'] >= 0.6 and sm['seeds_above_p95'] == 8 and sm['planted_per_seed'] == 6 and sm['tiles'] == 60)
    s, l, p = make(t / 'noise', False)
    rows, sm = ss.oddness_audit(s, l, p, frac=0.1, kind='random', seeds=8)
    check('noise (no shape to be odd against): does not beat the shuffled order in most seeds', sm['seeds_above_p95'] <= 4)
    rows_a, sm_a = ss.oddness_audit(s, l, p, frac=0.1, kind='random', seeds=3, variant='knn3')
    check('variants run and report their name', sm_a['variant'] == 'knn3' and len(rows_a) == 3)
    (t / 'conf.tsv').write_text('label_a\tlabel_b\tn\nF0\tF1\t5\n')
    s, l, p = make(t / 'shapes2', True)
    rows, sm = ss.oddness_audit(s, l, p, frac=0.1, kind='lookalike', confusion_p=str(t / 'conf.tsv'), seeds=4)
    check('look-alike plants use only tiles whose pile has a partner pile (F0, F1 of three piles)', sm['eligible'] == 40)
    check('the page oddness function is the audit function', ss.pile_oddness({'a': [0.0] * 576, 'b': [1.0] * 576}, ['a', 'b'])[1] == {'a': 0.5, 'b': 0.5})
print('FAILED' if fails else 'ALL PASS'); sys.exit(1 if fails else 0)
