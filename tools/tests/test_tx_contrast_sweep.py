#!/usr/bin/env python3
"""Offline test for tools/tx_contrast_sweep.py (TXE-I): a synthetic page with (1) a sign whose faint tail appears only at the
hard levels, (2) a sign with a speck that joins its stroke at the hard levels (vanishing as a separate stroke) and (3) a solid
sign; `stable` flags (1) and (2) uncertain with the right counts and leaves (3) unflagged. No network, no model."""
import os, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import tx_contrast_sweep as cs  # noqa: E402


def page(faint=150, bridge=150):
    rng = np.random.RandomState(0)
    g = np.clip(rng.normal(215, 8, (200, 400)), 0, 255).astype(np.uint8)   # parchment
    g[150:200, 250:400] = 60                 # a block of ordinary ink so Otsu sits between ink and parchment
    g[40:90, 40:50] = 30                     # (1) stem, dark
    g[90:120, 40:46] = faint                   # (1) faint tail below it: ink only at the hard thresholds
    g[40:90, 140:150] = 30                   # (2) stem
    g[60:66, 155:161] = 30                   # (2) speck, dark, 5 px right of the stem ...
    g[60:66, 150:155] = bridge                 # ... joined to it by a grey bridge from level 3 on
    g[40:90, 240:260] = 30                   # (3) solid block
    return g


def test_flags():
    ts = [l['t'] for l in cs.page_levels(page(), 5, 0.06)['levels']]
    g = page(int((ts[2] + ts[3]) / 2) + 1,   # faint grey: ink only at levels 4 and 5
             int((ts[1] + ts[2]) / 2) + 1)   # bridge grey: ink from level 3 on (speck seen apart at 1-2 only)
    lv = cs.page_levels(g, 5, 0.06)
    ts = [l['t'] for l in lv['levels']]
    f = int(g[100, 42])
    assert ts[2] <= f < ts[3], (ts, f)
    boxes = {'tail': (35, 35, 20, 60), 'speck': (135, 35, 30, 60), 'solid': (235, 35, 30, 60)}
    res = {}
    for k, b in boxes.items():
        others = [o for kk, o in boxes.items() if kk != k]
        comps = [cs.box_components(g, b, others, l, 0.5, 6)[0] for l in lv['levels']]
        res[k] = cs.analyse(comps, 6)
    assert res['tail']['n_appearing'] >= 1 and res['tail']['n_vanishing'] == 0, res['tail']
    assert res['speck']['n_vanishing'] == 1, res['speck']
    assert res['solid']['n_appearing'] == 0 and res['solid']['n_vanishing'] == 0, res['solid']
    assert res['solid']['n_stable'] == 1


def test_render_levels():
    g = page()
    lv = cs.page_levels(g, 5, 0.06)
    hard = cs.render(g, lv['levels'][-1])
    assert set(np.unique(hard)) <= {0, 255}
    soft = cs.render(g, lv['levels'][0])
    assert len(np.unique(soft)) > 2


if __name__ == '__main__':
    test_flags(); test_render_levels(); print('ok')
