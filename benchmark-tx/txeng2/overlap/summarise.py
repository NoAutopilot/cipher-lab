#!/usr/bin/env python3
"""TXE2-OVERLAP: per-item summary of run_overlap.sh's JSONs and the corrected overlap sentence per item (read-free)."""
import json, os, statistics, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../tools'))
from iiif_lines import overlap_sentence
from tx_bench import read_tsv
H = os.path.dirname(os.path.abspath(__file__))
ITEMS = [  # file, truth, declared passes (brief), supplementary, reader scale (crop px / box px on disk)
    ('no87_dev_tune', 'birago1572-no87', ['L', 'A', 'B'], []),
    ('no87_eval_heldout', 'birago1572-no87', ['L', 'A', 'B'], []),
    ('no87_f178r', 'birago1572-no87', ['L', 'A', 'B'], []),
    ('dint_f128', 'dint-f128-print', ['A', 'B', 'X21_sonnet_pipeline'], []),
    ('f152r', 'birago1572-f152r', ['Z'], []),
    ('spinelli', 'spinelli-c1519-confirm', ['Z'], []),
    ('f87', 'ceppo-f87-S', ['C'], ['A', 'B']),
]
SUF = sys.argv[1] if len(sys.argv) > 1 else ''
for f, item, decl, sup in ITEMS:
    d = json.load(open(os.path.join(H, f + SUF + '.json')))
    n_by = {}
    for r in read_tsv(os.path.join(H, '../../%s.truth.tsv' % item)):
        n_by[r['line']] = n_by.get(r['line'], 0) + 1
    ovs = sorted({o for L in d['lines'].values() for o in L['overlap_box_native']})
    pix = [p for L in d['lines'].values() for p in L['overlap_pixel'] if p]
    good = [p['native_px'] for p in pix if p['ncc'] >= 0.95]
    pitch = statistics.median((L['ink_extent'][1] - L['ink_extent'][0]) / n_by[ln] for ln, L in d['lines'].items())
    tot = {k: 0 for k in ('inside', 'seam', 'outside')}
    for p in decl:
        for k in tot:
            tot[k] += d['passes'][p]['counts'][k]
    n = sum(tot.values()); share = (tot['inside'] + tot['seam']) / n if n else None
    verdict = ('no indels: rule not applicable' if not n else
               'overlap-sentence-suspect' if share >= 0.5 else 'below half: sentence corrected for future briefs only')
    print('## %s (%s): %d lines; box overlaps %s; pixel match ncc>=0.95 on %d/%d pairs, values %s; pitch %.1f px'
          % (f, item, len(d['lines']), ovs, len(good), len(pix), sorted(set(good)), pitch))
    for p in decl + sup:
        P = d['passes'][p]
        print('  %s%s: %d indels, in %d seam %d out %d' % (p, '' if p in decl else ' (suppl.)', P['total'],
              P['counts']['inside'], P['counts']['seam'], P['counts']['outside']))
    print('  declared pooled: in %d seam %d out %d of %d -> share %s; chance %s; %s'
          % (tot['inside'], tot['seam'], tot['outside'], n, None if share is None else round(share, 3),
             d['chance_in_or_seam'], verdict))
    by_pre = {}
    for ln, L in d['lines'].items():
        by_pre.setdefault(ln.rsplit('_', 1)[0], []).append((L, (L['ink_extent'][1] - L['ink_extent'][0]) / n_by[ln]))
    for pre, Ls in sorted(by_pre.items()):
        o = statistics.median(x for L, _ in Ls for x in L['overlap_box_native'])
        pw = statistics.median(w for _, w in Ls)
        if o > 0:
            print('  sentence %s: %s' % (pre, overlap_sentence([(0, 1250), (1250 - int(o), 2500)], pw,
                                                               'sign pitch, ink extent / truth signs per line')[0]))
        else:
            print('  sentence %s: segments of a line do not overlap (cut at the column-ink minimum; 0 native px from the '
                  'boxes, no pixel match at ncc >= 0.95); continue the sign count across them and check the sign at each '
                  'cut once.' % pre)
