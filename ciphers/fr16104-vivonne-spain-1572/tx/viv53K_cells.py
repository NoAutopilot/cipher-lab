#!/usr/bin/env python3
"""D1-F16104K (6 Oct 2026): ink 53 U labels against shape-read key cells, under PREREG-D1VIV53K.md (ii)-(iii).

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv53K_cells.py     # writes tx/viv53K_cells.json

For each U label: fr16 4-gram score of the whole ink-53 G stream with the label -> each of 22 letters (others dropped);
PASS if the shape-read candidate ranks 1st and beats the label-dropped decode.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import viv53G_decode as vg, viv63_test as t, viv54_decode as vd, judge_plaintext as jp  # noqa: E402

CAND = {'e': 'f', 'o': 'p', 'II': 'm', 'Z': 'm', '2': 'm', 'r': 'n', 'c': 'o', 'V': 'x'}
ALPHA = 'abcdefghilmnopqrstuxyz'


def stream():
    fold = vg.decoys()['pass_']
    return [c for p in vg.PAGES for _, seq in sorted(vg.page_tokens(p, fold).items()) for c, _, _ in seq]


def main():
    k = {c: v for c, (v, g) in vd.key().items()}
    model = jp.NgramModel([jp.read_corpus(p) for p in t.FR16])
    whole = stream()
    dec = lambda km: ''.join(km.get(c, '') for c in whole)
    base = model.score(dec(k))
    res = {'base': round(base, 5), 'labels': {}}
    for lab, cand in CAND.items():
        sc = {a: model.score(dec({**k, lab: a})) for a in ALPHA}
        order = sorted(sc, key=lambda a: -sc[a])
        wrong = max(v for a, v in sc.items() if a != cand)
        r = {'n': whole.count(lab), 'cand': cand, 'cand_score': round(sc[cand], 5), 'rank': order.index(cand) + 1,
             'best_wrong': max((a for a in ALPHA if a != cand), key=lambda a: sc[a]), 'best_wrong_score': round(wrong, 5),
             'top3': order[:3], 'beats_base': sc[cand] > base}
        r['pass'] = r['rank'] == 1 and r['beats_base']
        res['labels'][lab] = r
        print(lab, r)
    json.dump(res, open(os.path.join(HERE, 'viv53K_cells.json'), 'w'), indent=1)
    print('base', base)


if __name__ == '__main__':
    main()
