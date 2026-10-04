#!/usr/bin/env python3
"""Offline test for tools/sign_sorter.py: a synthetic two-sign page, one sign with a mark above it.
Checks that the tile is cut around the mark (the Debosnys clipping lesson), piles and families come out,
oddness is computed, and the template placeholders are all filled. Run: python3 tools/tests/test_sign_sorter.py
(Browser click tests: tools/sign_sorter/browser_tests/*.js, run with node + playwright against a built page.)"""
import json, os, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import sign_sorter as ss
from PIL import Image, ImageDraw

fails = 0
def check(name, ok):
    global fails
    print('PASS' if ok else 'FAIL', name); fails += not ok

with tempfile.TemporaryDirectory() as d:
    d = Path(d); (d / 'pages').mkdir()
    im = Image.new('L', (200, 100), 255); g = ImageDraw.Draw(im)
    g.line((20, 40, 40, 70), fill=0, width=3); g.line((40, 40, 20, 70), fill=0, width=3)   # X at 20..40 x 40..70
    g.ellipse((28, 10, 33, 15), fill=0)                                                       # dot well above it
    g.line((100, 40, 120, 70), fill=0, width=3); g.line((120, 40, 100, 70), fill=0, width=3)
    im.save(d / 'pages' / 'p1.png')
    (d / 'signs.tsv').write_text('sid\tpage\tx\ty\tw\th\ns1\tp1\t20\t40\t21\t31\ns2\tp1\t100\t40\t21\t31\ns3\tp1\t300\t40\t5\t5\n')
    (d / 'labels.tsv').write_text('sid\tsign\tfamily\ns1\tX-DOT\tX\ns2\tX\tX\ns3\tX\tX\nmissing\tX\tX\n')
    (d / 'marks.tsv').write_text('mid\tpage\tx\ty\tw\th\tsid\nm1\tp1\t28\t5\t6\t6\ts1\n')
    data = ss.build(str(d / 'signs.tsv'), str(d / 'labels.tsv'), str(d / 'pages'), str(d / 'marks.tsv'))
    piles = {p['id']: p for p in data['piles']}
    check('two piles, family kept', set(piles) == {'X', 'X-DOT'} and piles['X-DOT']['family'] == 'X')
    s1 = piles['X-DOT']['items'][0]
    check('tile box grows to include the mark above', s1['b'][1] == 5 and s1['b'][3] == 66)
    check('missing sid and off-page box skipped (2 tiles, 2 skipped)', sum(len(p['items']) for p in data['piles']) == 2 and data['skipped'] == 2)
    check('oddness present', all('d' in it for p in data['piles'] for it in p['items']))
    check('page image embedded', 'p1' in data['pages'])
    html = ss.render(data, 'Test <Sorter>', 'Lede & more')
    # --- N4-NXS (4 Oct 2026): size options for long letters ---
    import base64, io
    small = ss.build(str(d / 'signs.tsv'), str(d / 'labels.tsv'), str(d / 'pages'), str(d / 'marks.tsv'),
                     thumb=32, tile_q=50, page_scale=0.5, page_q=40)
    t = base64.b64decode(small['piles'][0]['items'][0]['img'])
    pg = Image.open(io.BytesIO(base64.b64decode(small['pages']['p1'])))
    check('size options: JPEG tiles <= 32 px, page halved, mime and scale recorded',
          t[:2] == b'\xff\xd8' and max(Image.open(io.BytesIO(t)).size) <= 32 and pg.size == (100, 50)
          and small['tileMime'] == 'image/jpeg' and small['pageScale'] == 0.5
          and small['piles'][0]['items'][0]['b'] == next(p for p in data['piles'] if p['id'] == small['piles'][0]['id'])['items'][0]['b'])
    check('defaults unchanged: PNG tiles, full-size page', data['tileMime'] == 'image/png' and data['pageScale'] == 1.0
          and base64.b64decode(data['piles'][0]['items'][0]['img'])[:4] == b'\x89PNG')
    check('placeholders filled and escaped', '__DATA__' not in html and '__TITLE__' not in html and '__LEDE__' not in html
          and 'Test &lt;Sorter&gt;' in html and 'Lede &amp; more' in html)
    # --- TX-SORTER (3 Oct 2026): clusters, rank box, confusion fallback ---
    (d / 'clusters.tsv').write_text('id\tkind\tcluster\tdist\ns1\tsign\t4\t0.1\ns2\tsign\t4\t0.2\nm1\tmark\t4\t0.1\n')
    clu = ss.read_clusters(str(d / 'clusters.tsv'))
    check('atlas clusters.tsv read, marks skipped', clu == {'s1': '4', 's2': '4'})
    data2 = ss.build(str(d / 'signs.tsv'), str(d / 'labels.tsv'), str(d / 'pages'), str(d / 'marks.tsv'), clusters=clu)
    check('tiles carry cluster id', all(it.get('c') == '4' for p in data2['piles'] for it in p['items']))
    conf = [{'label_a': 'X', 'label_b': 'X-DOT', 'n': '10'}, {'label_a': 'X', 'label_b': 'Y', 'n': '5'}]
    rk = ss.rank_from_confusion(data2, conf, focus_sids=['s2'])
    check('confusion rank: one row per cluster group, focus tile shown, conf 1.0 x 1 tile',
          [x['sid'] for x in rk] == ['s1', 's2'] or [x['sid'] for x in rk] == ['s2', 's1'])
    rk0 = ss.rank_from_confusion(data, [{'label_a': 'X', 'label_b': 'Y', 'n': '4'}, {'label_a': 'Q', 'label_b': 'R', 'n': '8'}])
    check('confusion rank: score = n/max x tiles flipped; alt = top partner', rk0 == [{'sid': 's2', 'score': 0.5, 'alt': 'Y', 'why': 'X or Y?', 'detail': 'flips 1 tile'}])
    (d / 'rank.tsv').write_text('sid\tscore\talt\twhy\n' + ''.join(f's{i}\t{i}\tY\tq\n' for i in range(30)))
    rr = ss.read_rank(str(d / 'rank.tsv'))
    check('rank file capped at 20, highest first', len(rr) == 20 and rr[0]['score'] == 29)
    # provisional clusters inside a pile of 6 near-identical tiles
    big = {'piles': [{'id': 'P', 'items': [{'sid': f'v{i}'} for i in range(6)]}], '_vecs': {f'v{i}': [float(i > 2)] * 4 for i in range(6)}}
    ss.auto_clusters(big, 3)
    cs = {it['c'] for it in big['piles'][0]['items']}
    check('auto clusters: provisional ids inside the pile', big['clusterSource'] == 'provisional' and all(c.startswith('P~') for c in cs) and len(cs) == 2)
    out = d / 'page.html'
    ss.main(['--signs', str(d / 'signs.tsv'), '--labels', str(d / 'labels.tsv'), '--pages', str(d / 'pages'), '--clusters', str(d / 'clusters.tsv'),
             '--rank-confusion', str(d / 'conf.tsv') if (d / 'conf.tsv').write_text('label_a\tlabel_b\tn\nX\tY\t3\n') else '',
             '--rank-out', str(d / 'rk.tsv'), '--title', 'T', '--out', str(out), '--atlas', 'atlas/labels.json'])
    html = out.read_text()
    check('CLI page carries rank, clusters and atlas, no private keys', '"rank": [' in html and '"clusterSource": "atlas"' in html
          and 'atlas/labels.json' in html and '_vecs' not in html and (d / 'rk.tsv').read_text().startswith('sid\tscore'))
    check('"</" escaped in embedded JSON', '</script>' not in ss.render({'piles': [], 'note': '</script>'}, 't', 'l').split('const DATA')[1].split('\n')[0])
    # --atlas-topk inputs and the lattice value score (tiny corpus, offline)
    (d / 'tk.tsv').write_text('page\tline\tbox\tpos\tx\ty\tw\th\tk1\ts1\tk2\ts2\tk3\ts3\n'
                              'p1\t1\tb1\t1\t20\t40\t21\t31\tA\t0.6\tB\t0.4\t_\t0\n'
                              'p1\t1\tb2\t2\t100\t40\t21\t31\tC\t1.0\t_\t0\t_\t0\n'
                              'p1\t1\tb3\t3\t60\t40\t5\t5\t_\t1.0\tA\t0\t_\t0\n')
    sp, lp = ss.atlas_topk_inputs([str(d / 'tk.tsv')], str(d))
    check('atlas topk: "_" boxes dropped, piles by k1', Path(lp).read_text().splitlines()[1:] == ['b1\tA\tA', 'b2\tC\tC'])
    lat = ss.lattice_from_atlas_topk([str(d / 'tk.tsv')])
    check('atlas topk lattice: line key, box id, weights renormalised', lat == [(('p1_01', 'b1'), {'A': 0.6, 'B': 0.4}), (('p1_01', 'b2'), {'C': 1.0})])
    (d / 'key.tsv').write_text('sign\tvalue\nA\tqz\nB\tla\nC\tera\n')
    (d / 'tk.tsv').write_text('page\tline\tbox\tpos\tx\ty\tw\th\tk1\ts1\tk2\ts2\tk3\ts3\n'
                              'p1\t1\tb2\t1\t100\t40\t21\t31\tC\t1.0\t_\t0\t_\t0\n'
                              'p1\t1\tb1\t2\t20\t40\t21\t31\tA\t0.6\tB\t0.4\t_\t0\n'
                              'p1\t1\tb4\t3\t100\t40\t21\t31\tC\t1.0\t_\t0\t_\t0\n')   # era ?? era: context for the 4-gram model
    (d / 'signs2.tsv').write_text(Path(sp).read_text() + 'b4\tp1\t100\t40\t21\t31\n'); sp = str(d / 'signs2.tsv')
    (d / 'labels2.tsv').write_text(Path(lp).read_text() + 'b4\tC\tC\n'); lp = str(d / 'labels2.tsv')
    (d / 'corpus.txt').write_text('la sera era bella e la terra era nera ' * 400)
    dd = ss.build(sp, lp, str(d / 'pages'))
    rk2, unm = ss.rank_from_lattice(dd, str(d / 'tk.tsv'), str(d / 'key.tsv'), corpus=[str(d / 'corpus.txt')])
    check('lattice value: the A/B tile ranks, the language model prefers B (decode) over top-1 A', unm == 0 and len(rk2) == 1
          and rk2[0]['sid'] == 'b1' and rk2[0]['why'] == 'A (top-1) or B (decode)?' and rk2[0]['score'] > 0)
    (d / 'pages.json').write_text(json.dumps({'p1': {'image': str(d / 'pages' / 'p1.png'), 'box': None}}))
    dj = ss.build(str(d / 'signs.tsv'), str(d / 'labels.tsv'), str(d / 'pages.json'))
    check('--pages takes a glyph_atlas pages.json', sum(len(p['items']) for p in dj['piles']) == 2 and 'p1' in dj['pages'])
    # --- BIR87-SORTER (4 Oct 2026): --refs marks locked reference tiles (and drops any cluster id); others untouched ---
    (d / 'rs.tsv').write_text('sid\tpage\tx\ty\tw\th\ns1\tp1\t20\t40\t21\t31\ns2\tp1\t100\t40\t21\t31\n')
    (d / 'rl.tsv').write_text('sid\tsign\tfamily\ns1\tX-DOT\tX\ns2\tX\tX\n')   # (signs.tsv was rewritten by the --atlas-topk test)
    dr = ss.build(str(d / 'rs.tsv'), str(d / 'rl.tsv'), str(d / 'pages'), clusters={'s1': 'k1', 's2': 'k1'})
    n = ss.mark_refs(dr, ['s1', 'nope'])
    its = {it['sid']: it for p in dr['piles'] for it in p['items']}
    check('--refs: one tile flagged r=1 with no cluster id, the other keeps its cluster and no flag',
          n == 1 and its['s1'].get('r') == 1 and 'c' not in its['s1'] and 'r' not in its['s2'] and its['s2'].get('c') == 'k1')
    (d / 'refs.tsv').write_text('sid\ns1\n')
    out = d / 'refs.html'
    ss.main(['--signs', str(d / 'rs.tsv'), '--labels', str(d / 'rl.tsv'), '--pages', str(d / 'pages'),
             '--refs', str(d / 'refs.tsv'), '--title', 'T', '--out', str(out)])
    check('--refs reaches the page data', '"r": 1' in out.read_text())
print('FAILED' if fails else 'ALL PASS'); sys.exit(1 if fails else 0)
