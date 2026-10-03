# TX-ATLAS-B72 (3 Oct 2026): name the atlas's clusters from the no.87 known answer (the clerk's clear sheet), tune lines only.
# A tune tile (f.178v L01-L12, mapped 1:1 by no87_map.py) is VERIFIED when its line-read sign's value under the key equals
# the clerk-sheet letter at that position; its sign is then a known-answer label (override) and a vote for its cluster's
# name (majority of verified labels). Clusters with no verified tune tile are left for the exemplar-sheet read
# (named_by_model.json, merged here when present). Run from the repo root; writes atlas/labels.json and
# atlas/cluster_names.tsv. Values: keys/key_1572_clerk.tsv (C grade), else harvest/key_1572_sheet.tsv (printed).
import csv, os, json, collections
R = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(R, '..')
rd = lambda p: [r for r in csv.reader(open(p), delimiter='\t') if r and not r[0].startswith('#')]


def value_map():
    V = {}
    for r in rd(os.path.join(D, 'harvest', 'key_1572_sheet.tsv'))[1:]:
        V[r[0]] = r[1]
    for r in rd(os.path.join(D, 'keys', 'key_1572_clerk.tsv'))[1:]:
        if r[0].startswith('T'):
            V[r[0]] = r[1]
    return V


def main():
    V = value_map()
    M = list(csv.DictReader(open(os.path.join(R, 'no87_box_token.tsv')), delimiter='\t'))
    cl = {r['id']: r['cluster'] for r in csv.DictReader(open(os.path.join(R, 'clusters.tsv')), delimiter='\t') if r['kind'] == 'sign'}
    size = collections.Counter(cl.values())
    over, votes = {}, collections.defaultdict(collections.Counter)
    for r in M:
        if r['split'] == 'tune' and r['op'] == '1:1' and r['truth'] and V.get(r['sign']) == r['truth']:
            over[r['sid']] = r['sign']; votes[cl[r['sid']]][r['sign']] += 1
    names = {}
    rows = []
    model = {}
    mp = os.path.join(R, 'named_by_model.json')
    if os.path.exists(mp):
        model = json.load(open(mp))
    for c in sorted(size, key=int):
        v = votes.get(c)
        if v:
            code, n = v.most_common(1)[0]; names[c] = code; src = f'clerk {n}/{sum(v.values())}'
        elif c in model:
            names[c] = model[c]; src = 'model sheet read'
        else:
            names[c] = '_'; src = 'unnamed'
        rows.append((c, size[c], names[c], src, ' '.join(f'{k}:{n}' for k, n in (v or {}).items())))
    json.dump({'signs': names, 'marks': {}, 'override': over,
               'desc': {'_': 'not a cipher sign or not yet named'}}, open(os.path.join(R, 'labels.json'), 'w'), indent=0)
    with open(os.path.join(R, 'cluster_names.tsv'), 'w') as f:
        f.write('cluster\tsize\tcode\tsource\tverified_votes\n')
        for r in rows: f.write('\t'.join(map(str, r)) + '\n')
    src = collections.Counter(r[3].split()[0] for r in rows)
    print(f'{len(over)} verified tune tiles; clusters by source {dict(src)}; '
          f'tiles in unnamed clusters {sum(r[1] for r in rows if r[3] == "unnamed")} of {sum(size.values())}')


if __name__ == '__main__':
    main()
