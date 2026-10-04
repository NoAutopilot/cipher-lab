#!/usr/bin/env python3
"""N7-VIV54R: tally the value-blind shape judge (tx/lookalike54/viv54R_judge.tsv) under PREREG-N7VIV54R.md's decision rule and
built-in check, and write tx/lookalike54/viv54R_relabel.tsv (SIGMA at H/M -> Zu) or, on a NON-TEST, an empty overlay.

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv54R_apply.py

Check (PREREG): of the positions right after a 'to' label (the known-positive subset), >= 7 SIGMA at H/M; of all other positions,
<= 50% SIGMA at H/M. Writes tx/viv54R_tally.json.
"""
import csv, json, os, collections
HERE = os.path.dirname(os.path.abspath(__file__))
LA = os.path.join(HERE, 'lookalike54')


def rd(p):
    return list(csv.DictReader(open(p, encoding='utf-8'), delimiter='\t'))


def main():
    items = {r['id']: r for r in rd(os.path.join(LA, 'viv54R_items.tsv'))}
    prev = {}
    for page in ('f173r', 'f173v'):
        seq = {}
        for r in rd(os.path.join(LA, f'viv54L_{page}_passD.tsv')):
            seq.setdefault(r['passage'], {})[int(r['pos'])] = r['sign_id']
        for i in items.values():
            if i['page'] == page:
                prev[i['id']] = seq[i['passage']].get(int(i['pos']) - 1, '^')
    judge = {r['id'].strip(): r for r in rd(os.path.join(LA, 'viv54R_judge.tsv'))}
    missing = sorted(set(items) - set(judge))
    firm = lambda j: j and j['class'].strip().upper() == 'SIGMA' and j['conf'].strip().upper() in ('H', 'M')
    to_ids = [i for i in items if prev[i] == 'to']; other = [i for i in items if prev[i] != 'to']
    to_hit = sum(firm(judge.get(i)) for i in to_ids); oth_hit = sum(firm(judge.get(i)) for i in other)
    ok = to_hit >= 7 and oth_hit <= 0.5 * len(other)
    cls = collections.Counter((judge[i]['class'].strip().upper(), judge[i]['conf'].strip().upper()) for i in judge if i in items)
    bylab = collections.Counter((items[i]['label'], 'to' if prev[i] == 'to' else 'other') for i in items if firm(judge.get(i)))
    rows = [i for i in items if firm(judge.get(i))] if ok else []
    with open(os.path.join(LA, 'viv54R_relabel.tsv'), 'w') as o:
        o.write('page\tpassage\tpos\tlabel\tconf\twas\tprev\n')
        for i in rows:
            it = items[i]; o.write(f"{it['page']}\t{it['passage']}\t{it['pos']}\tZu\t{judge[i]['conf'].strip().upper()}\t{it['label']}\t{prev[i]}\n")
    res = {'positions': len(items), 'answered': len(judge), 'missing': missing, 'classes': {f'{a}/{b}': n for (a, b), n in sorted(cls.items())},
           'after_to': len(to_ids), 'after_to_sigma_HM': to_hit, 'other': len(other), 'other_sigma_HM': oth_hit,
           'sigma_HM_by_label': {f'{a}|{b}': n for (a, b), n in sorted(bylab.items())},
           'check': 'PASS' if ok else 'NON-TEST', 'relabelled': len(rows)}
    json.dump(res, open(os.path.join(HERE, 'viv54R_tally.json'), 'w'), indent=1); print(json.dumps(res))


if __name__ == '__main__':
    main()
