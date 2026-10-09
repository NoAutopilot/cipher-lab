#!/usr/bin/env python3
"""MQS-SORTER Unit 4 (9 Oct 2026): score the owner's 4 Oct no.87 sort against BENCHMARK-TX, by the label-map rule written in
tools/tests/PREREG-MQS-SORTER.md section B before this ran. Read-only on ciphers/ and benchmark-tx/.

  python3 tools/tests/mqs_sorter_score_owner.py [--json]

Tiles: the settled tiles (sorter/no87/owner-sort-2026-10-04/settled_no87.tsv) that have a box<->token position
(atlas/no87_box_token.tsv: f.178v, f.179r; f.178r tiles have no position map and are reported unmapped).
Output to score = the committed line reads (benchmark-tx/outputs/birago1572-no87/labels.tsv) with the owner's mapped pile at each sorted
position: a plain sign id with a row in harvest/key_1572_sheet.tsv keeps its id (truth sets in BENCHMARK-TX are sign sets, so "that sign's
printed value" is the sign itself); an owner-made new pile (suffixed T60-d, T89-b, X_NEW-*) reads '?'; a plain sign with no key row is
unmapped and left out; bad-cut / not-letter / aside tiles are left out. Base = the committed reads on the same positions. err_true is per
sorted position (scored positions only), Wilson 95%; fixed/broken separately for tiles the owner MOVED and tiles he left KEPT."""
import csv, json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import tx_bench as tb
B = os.path.join(ROOT, 'ciphers', 'nevers-birago-fr3251-1572')
rd = lambda p: list(csv.DictReader(open(p, newline=''), delimiter='\t'))


def main(as_json=False):
    key = {r['sign'] for r in rd(os.path.join(B, 'harvest', 'key_1572_sheet.tsv'))}
    settled = rd(os.path.join(B, 'sorter', 'no87', 'owner-sort-2026-10-04', 'settled_no87.tsv'))
    pos = {r['sid']: r for r in rd(os.path.join(B, 'atlas', 'no87_box_token.tsv'))}
    truth = [r for r in tb.read_tsv(os.path.join(ROOT, 'benchmark-tx', 'birago1572-no87.truth.tsv'))]
    base_lines = tb.load_output([os.path.join(ROOT, 'benchmark-tx', 'outputs', 'birago1572-no87', 'labels.tsv')])
    own = {k: list(v) for k, v in base_lines.items()}
    cohort, left = {}, {'no position map (f.178r)': 0, 'bad-cut / not-letter / aside': 0, 'plain sign with no key row (unmapped)': 0}
    new_unknown = 0
    unk = set()
    rows_by_line = {}
    for ln, signs in base_lines.items():
        rows_by_line[ln] = {int(float(r['pos'])): i for i, r in enumerate(sorted((x for x in tb.read_tsv(os.path.join(ROOT, 'benchmark-tx', 'outputs', 'birago1572-no87', 'labels.tsv')) if x['line'] == ln), key=lambda x: float(x['pos'])))}
    for r in settled:
        p = pos.get(r['sid'])
        if not p:
            left['no position map (f.178r)'] += 1; continue
        if r['status'] in ('bad-cut', 'not-letter', 'aside', 'taken-out') or not r['new_sign']:
            left['bad-cut / not-letter / aside'] += 1; continue
        ns = r['new_sign']
        plain = ns.split('-')[0] == ns and not ns.startswith('X_')
        if plain and ns not in key:
            left['plain sign with no key row (unmapped)'] += 1; continue
        mapped = ns if plain else '?'
        new_unknown += mapped == '?'
        i = rows_by_line[p['line'].replace('_L', '_L')][int(p['pos'])] if p['line'] in rows_by_line else None
        if i is None:
            left['no position map (f.178r)'] += 1; continue
        own[p['line']][i] = mapped
        if mapped == '?': unk.add((p['line'], p['pos']))
        cohort[(p['line'], p['pos'])] = 'moved' if r['status'] in ('moved', 'cluster-moved') else 'kept'
    ob, ow = tb.position_errors(truth, base_lines), tb.position_errors(truth, own)
    out = {'tiles_settled': len(settled), 'scored_cohort': len(cohort), 'left_out': left, 'owner_new_piles_read_unknown': new_unknown}
    for name, sel in (('all', lambda c: True), ('moved', lambda c: c == 'moved'), ('kept', lambda c: c == 'kept')):
        keys = [k for k, c in cohort.items() if sel(c) and k in ow and k in ob]
        n = len(keys); eb = sum(ob[k] for k in keys); eo = sum(ow[k] for k in keys)
        fixed = sum(1 for k in keys if ob[k] and not ow[k]); broken = sum(1 for k in keys if ow[k] and not ob[k])
        out[name] = {'scored_positions': n, 'owner_wrong': eo, 'owner_err_true': round(eo / n, 3) if n else None,
                     'owner_ci95': [round(x, 3) for x in tb.wilson(eo, n)], 'committed_wrong': eb,
                     'committed_err_true': round(eb / n, 3) if n else None, 'committed_ci95': [round(x, 3) for x in tb.wilson(eb, n)],
                     'fixed': fixed, 'broken': broken, 'sign_test_p': round(tb.sign_test(fixed, broken), 4) if fixed + broken else None}
    # diagnostic, NOT the registered score: the same positions with the owner-made-pile ('?') tiles left out
    plain = [k for k in cohort if k not in unk and k in ow and k in ob]
    ew = sum(ow[k] for k in plain); eb2 = sum(ob[k] for k in plain)
    out['diagnostic_plain_piles_only'] = {'scored_positions': len(plain), 'owner_wrong': ew, 'owner_err_true': round(ew / len(plain), 3),
                                          'owner_ci95': [round(x, 3) for x in tb.wilson(ew, len(plain))], 'committed_wrong': eb2,
                                          'committed_err_true': round(eb2 / len(plain), 3)}
    print(json.dumps(out, indent=1))


if __name__ == '__main__':
    main('--json' in sys.argv)
