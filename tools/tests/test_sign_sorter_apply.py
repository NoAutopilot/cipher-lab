#!/usr/bin/env python3
"""Offline test for tools/sign_sorter_apply.py on hand-made decisions. Run: python3 tools/tests/test_sign_sorter_apply.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import sign_sorter_apply as sa

fails = 0
def check(name, ok):
    global fails
    print('PASS' if ok else 'FAIL', name); fails += not ok

labels = [{'sid': s, 'sign': g} for s, g in [('a', 'X'), ('b', 'X'), ('c', 'X'), ('d', 'XB'), ('e', 'XB2'), ('f', 'DOT'), ('g', 'X'), ('h', 'X')]]
piles = [{'pile': 'X', 'verdict': 'same', 'outliers': ['g']}, {'pile': 'XB2', 'merge_into': 'XB'}, {'pile': 'XB', 'merge_into': 'XBAR'},
         {'pile': 'DOT', 'verdict': 'mark'}, {'pile': 'Q1', 'merge_into': 'Q2'}, {'pile': 'Q2', 'merge_into': 'Q1'}]
moves = [{'sid': 'b', 'to': 'X1'}, {'sid': 'c', 'to': 'BAD-CUT'}, {'sid': 'h', 'to': 'ASIDE'}]
rows, summ = sa.apply(labels, piles, moves, [{'id': 'X1'}])
r = {x[0]: x for x in rows}
check('untouched tile kept', r['a'][2:] == ('X', 'kept'))
check('moved to new pile', r['b'][2:] == ('X1', 'moved'))
check('bad cut', r['c'][3] == 'bad-cut' and r['c'][2] == '')
check('merge followed transitively', r['d'][2:] == ('XBAR', 'merged') and r['e'][2:] == ('XBAR', 'merged'))
check('not-letter pile', r['f'][3] == 'not-letter')
check('legacy outlier and ASIDE both aside', r['g'][3] == 'aside' and r['h'][3] == 'aside')
check('merge cycle does not hang', sa.apply([{'sid': 'z', 'sign': 'Q1'}], piles, [], [])[0][0][2] in ('Q1', 'Q2'))
check('summary counts', summ['by_status']['bad-cut'] == 1 and summ['confirmed_piles'] == ['X'] and summ['new_piles'] == ['X1'])

# --- TX-SORTER (3 Oct 2026): cluster decisions and the family atlas ---
import json, os, subprocess, tempfile
lab2 = [{'sid': s, 'sign': g} for s, g in [('s1', 'T24'), ('s2', 'T24'), ('s3', 'T24'), ('s4', 'T29'), ('s5', 'T29'), ('s6', 'DOT'), ('s7', 'T60')]]
clu = {'s1': '7', 's2': '7', 's3': '7', 's4': '9', 's5': '9', 's6': '12', 's7': '3'}
pil2 = [{'pile': 'T29', 'merge_into': 'T83'}, {'pile': 'DOT', 'verdict': 'mark'}]
mov2 = [{'sid': 's1', 'to': 'T83'}, {'sid': 's2', 'to': 'T83'}, {'sid': 's7', 'to': 'T86'}]   # s3 missed: a sibling letter's tile
cdoc = [{'cluster': '7', 'to': 'T83', 'from_sid': 's1', 'n': 3}, {'cluster': 'T60~1', 'to': 'T86'}]
rows2, sm2 = sa.apply(lab2, pil2, mov2, [], cdoc, clu)
r2 = {x[0]: x for x in rows2}
check('cluster decision reaches a tile with no move of its own', r2['s3'][2:] == ('T83', 'cluster-moved'))
check('own moves stay "moved"', r2['s1'][3] == 'moved' and r2['s7'][2:] == ('T86', 'moved'))
check('summary lists the decision', sm2['cluster_decisions'] == {'7': 'T83', 'T60~1': 'T86'} and sm2['by_status']['cluster-moved'] == 1)
check('old save (no clusters collection) has no new status key', 'cluster-moved' not in summ['by_status'] and 'cluster_decisions' not in summ)
L = {'signs': {'7': 'T24', '9': 'T29', '12': 'DOT', '3': 'T60'}, 'marks': {}, 'override': {'s5': 'T29'}}
log = sa.write_atlas(L, rows2, pil2, mov2, cdoc, clu, 'test')
check('atlas: cluster decision written', L['signs']['7'] == 'T83')
check('atlas: merge relabels signs and override', L['signs']['9'] == 'T83' and L['override']['s5'] == 'T83')
check('atlas: not-letter pile becomes _', L['signs']['12'] == '_')
check('atlas: lone move becomes an override, cluster untouched', L['signs']['3'] == 'T60' and L['override']['s7'] == 'T86')
check('atlas: provisional cluster never written', 'T60~1' not in L['signs'])
check('atlas: log entry', L['sorter_log'][-1]['cluster_decisions'] == 1 and log['overrides'] == 1 and log['source'] == 'test')
with tempfile.TemporaryDirectory() as d:
    for coll, docs in (('piles', pil2), ('moves', mov2), ('clusters', cdoc)):
        os.makedirs(os.path.join(d, 'db', coll))
        for i, doc in enumerate(docs):
            json.dump({'data': doc}, open(os.path.join(d, 'db', coll, f'{i}.json'), 'w'))
    open(os.path.join(d, 'labels.tsv'), 'w').write('sid\tsign\n' + ''.join(f"{x['sid']}\t{x['sign']}\n" for x in lab2))
    open(os.path.join(d, 'clusters.tsv'), 'w').write('id\tkind\tcluster\tdist\n' + ''.join(f'{k}\tsign\t{v}\t0.1\n' for k, v in clu.items()) + 'm1\tmark\t7\t0.1\n')
    json.dump({'signs': {'7': 'T24'}, 'marks': {}}, open(os.path.join(d, 'atlas.json'), 'w'))
    tool = str(Path(__file__).resolve().parent.parent / 'sign_sorter_apply.py')
    p = subprocess.run([sys.executable, tool, '--labels', f'{d}/labels.tsv', '--db', f'{d}/db', '--out', f'{d}/out.tsv',
                        '--clusters', f'{d}/clusters.tsv', '--atlas-labels', f'{d}/atlas.json'], capture_output=True, text=True)
    A = json.load(open(f'{d}/atlas.json'))
    check('CLI writes the atlas in place', p.returncode == 0 and A['signs']['7'] == 'T83' and A['override'].get('s7') == 'T86')
    p2 = subprocess.run([sys.executable, tool, '--labels', f'{d}/labels.tsv', '--db', f'{d}/db', '--out', f'{d}/o2.tsv',
                         '--atlas-labels', f'{d}/atlas.json'], capture_output=True, text=True)
    check('--atlas-labels without --clusters refused', p2.returncode != 0)
print('FAILED' if fails else 'ALL PASS'); sys.exit(1 if fails else 0)
