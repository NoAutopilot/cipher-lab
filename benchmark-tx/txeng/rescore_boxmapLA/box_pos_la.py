#!/usr/bin/env python3
"""BOXMAP-RESCORE (others), 11 Oct 2026, account 3: the txeng box<->position files rebuilt from the label-aware no.87 map.

benchmark-tx/txeng/compare/box_pos.tsv (tools/tx_compare.py `map`; the same file as gate/box_pos.tsv) and
pair/{dev_tune,eval_heldout}/box_pos.tsv (tools/tx_pair_reread.py) were built by copies of atlas/no87_map.py's width DP and match
the old atlas/no87_box_token.tsv on every shared box. This writes, beside them:
  box_pos.tsv              sid line pos op, f178v/f179r rows from atlas/no87_box_token_labelaware.tsv in the old row convention
                           (a 2:1 pair -> its first box, a 1:2 box -> its first token; unsure / bad-cut kept with their own op, never
                           1:1), f178r rows copied unchanged from compare/box_pos.tsv (the label-aware map does not cover f178r);
  box_pos_1to1_<unit>.tsv  the pair re-read's per-unit form (sid line pos, 1:1 rows of that unit's lines only);
  shifted_positions.tsv    every f178v/f179r position whose 1:1 box differs between the old and the new file (old_sid, new_sid;
                           empty = no 1:1 box), the join a consumer used to cut, label or show that position.
No truth file is read. Usage: python3 benchmark-tx/txeng/rescore_boxmapLA/box_pos_la.py
"""
import csv, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
HERE = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(ROOT, 'ciphers/nevers-birago-fr3251-1572/atlas')
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))


def main():
    old = rd(os.path.join(ROOT, 'benchmark-tx/txeng/compare/box_pos.tsv'))
    rows, s2, s12 = [r for r in old if r['line'].startswith('f178r')], set(), set()
    for r in rd(os.path.join(A, 'no87_box_token_labelaware.tsv')):
        if r['op'] == '2:1':
            if (r['line'], r['pos']) in s2: continue
            s2.add((r['line'], r['pos']))
        elif r['op'] == '1:2':
            if r['sid'] in s12: continue
            s12.add(r['sid'])
        rows.append(dict(sid=r['sid'], line=r['line'], pos=r['pos'], op=r['op']))
    with open(os.path.join(HERE, 'box_pos.tsv'), 'w') as f:
        f.write('sid\tline\tpos\top\n' + ''.join(f"{r['sid']}\t{r['line']}\t{r['pos']}\t{r['op']}\n" for r in rows))
    for unit, pre in (('dev_tune', [f'f178v_L{i:02d}' for i in range(1, 13)]),
                      ('eval_heldout', [f'f178v_L{i:02d}' for i in range(13, 24)] + [f'f179r_L{i:02d}' for i in (1, 2, 3)])):
        with open(os.path.join(HERE, f'box_pos_1to1_{unit}.tsv'), 'w') as f:
            f.write('sid\tline\tpos\n' + ''.join(f"{r['sid']}\t{r['line']}\t{r['pos']}\n" for r in rows
                                                if r['op'] == '1:1' and r['line'] in pre))
    o11 = {(r['line'], r['pos']): r['sid'] for r in old if r['op'] == '1:1' and not r['line'].startswith('f178r')}
    n11 = {(r['line'], r['pos']): r['sid'] for r in rows if r['op'] == '1:1' and not r['line'].startswith('f178r')}
    keys = sorted(set(o11) | set(n11), key=lambda k: (k[0], int(k[1])))
    sh = [(k, o11.get(k, ''), n11.get(k, '')) for k in keys if o11.get(k) != n11.get(k)]
    with open(os.path.join(HERE, 'shifted_positions.tsv'), 'w') as f:
        f.write('line\tpos\told_sid\tnew_sid\n' + ''.join(f'{k[0]}\t{k[1]}\t{a}\t{b}\n' for k, a, b in sh))
    print(f'box_pos.tsv {len(rows)} rows; positions whose 1:1 box changed: {len(sh)} '
          f'(dev_tune {sum(1 for k, _, _ in sh if k[0] < "f178v_L13")}, eval_heldout {sum(1 for k, _, _ in sh if k[0] >= "f178v_L13")})')


if __name__ == '__main__':
    main()
