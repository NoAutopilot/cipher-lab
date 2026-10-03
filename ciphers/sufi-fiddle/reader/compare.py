#!/usr/bin/env python3
"""GAPS94: pre-registered comparison of the blind reader's items (reader_out.json) with the matched-span dump (spans.tsv).

Usage: compare.py --leipzig MSA_SENTENCES_TXT --quran TANZIL_TXT2 [--out compare.json]   (see PREREG.md)
S1: reader items sharing >= 1 group with a chosen_C3 span (union of MS and AR) vs a uniform-placement expectation,
exact Poisson-binomial one-sided p. S2: reader word's skeleton = a spans.tsv row's skeleton at the same group span AND
the word itself is in that list's index (descriptive).
"""
import argparse, collections, csv, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'tausug'))
sys.path.insert(0, os.path.join(HERE, '..', 'malay-arabic'))
from match import read_target, roman_skel  # noqa: E402
from match2 import leipzig, quran, ar_skel  # noqa: E402


def poibin_ge(ps, o):
    dist = [1.0]
    for p in ps:
        nd = [0.0] * (len(dist) + 1)
        for k, v in enumerate(dist):
            nd[k] += v * (1 - p)
            nd[k + 1] += v * p
        dist = nd
    return sum(dist[o:])


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--leipzig', required=True)
    ap.add_argument('--quran', required=True)
    ap.add_argument('--spans', default=os.path.join(HERE, '..', 'malay-arabic', 'spans.tsv'))
    ap.add_argument('--reader', default=os.path.join(HERE, 'reader_out.json'))
    ap.add_argument('--out', default=os.path.join(HERE, 'compare.json'))
    a = ap.parse_args()
    target = read_target()
    spans = list(csv.DictReader(open(a.spans, encoding='utf-8'), delimiter='\t'))
    covered = collections.defaultdict(set)
    for r in spans:
        if r['chosen_C3'] == 'y':
            covered[r['line']].update(range(int(r['group_from']), int(r['group_to']) + 1))
    ms_list, _ = leipzig(a.leipzig)
    ar_list, ar_held = quran(a.quran, 91)
    if len(ar_held) < 1000:
        ar_list, _ = quran(a.quran, 78)
    idx = {'MS': collections.defaultdict(set), 'AR': collections.defaultdict(set)}
    for w in ms_list:
        idx['MS'][roman_skel(w)].add(w.lower())
    for w in ar_list:
        idx['AR'][ar_skel(w)].add(w)
    items = json.load(open(a.reader, encoding='utf-8'))['items']
    res = {'items': []}
    for it in items:
        ln, g0, g1 = it['line'], int(it['group_from']), int(it['group_to'])
        li = int(ln[1:]) - 1
        groups = target[li]
        width = g1 - g0 + 1
        valid = [j for j in range(1, len(groups) - width + 2) if all(groups[k - 1] is not None for k in range(j, j + width))]
        hit_pos = [j for j in valid if covered[ln] & set(range(j, j + width))]
        p_exp = len(hit_pos) / len(valid) if valid else 0.0
        s1 = bool(covered[ln] & set(range(g0, g1 + 1)))
        ar_w = ''.join(c for c in it.get('arabic', '') if 'ء' <= c <= 'ي')
        sk_ar, sk_ro = ar_skel(ar_w), roman_skel(it.get('roman', ''))
        s2 = []
        for r in spans:
            if r['line'] == ln and int(r['group_from']) == g0 and int(r['group_to']) == g1:
                if r['list'] == 'AR' and sk_ar == r['skeleton'] and ar_w in idx['AR'][r['skeleton']]:
                    s2.append('AR')
                rw = it.get('roman', '').lower().replace('-', '').replace(' ', '')
                if r['list'] == 'MS' and sk_ro == r['skeleton'] and rw in idx['MS'][r['skeleton']]:
                    s2.append('MS')
        grade = 'M' if it.get('confidence') in ('H', 'M') else 'I'
        res['items'].append({'line': ln, 'groups': [g0, g1], 'arabic': it.get('arabic'), 'roman': it.get('roman'),
                             'language': it.get('language'), 'gloss': it.get('gloss'), 'confidence': it.get('confidence'),
                             'grade': grade, 'S1_overlap_C3': s1, 'S1_p_expected': round(p_exp, 4), 'S2_word_match': s2})
    for tag, sel in (('all', lambda x: True), ('HM', lambda x: x['confidence'] in ('H', 'M'))):
        its = [x for x in res['items'] if sel(x)]
        o = sum(x['S1_overlap_C3'] for x in its)
        ps = [x['S1_p_expected'] for x in its]
        res['S1_' + tag] = {'N': len(its), 'observed': o, 'expected': round(sum(ps), 3),
                            'p_one_sided': round(poibin_ge(ps, o), 4) if its else None}
        res['S2_' + tag] = {'N': len(its), 'W': sum(bool(x['S2_word_match']) for x in its)}
    res['grades'] = dict(collections.Counter(x['grade'] for x in res['items']))
    js = json.dumps(res, indent=1, ensure_ascii=False)
    print(js)
    open(a.out, 'w', encoding='utf-8').write(js + '\n')


if __name__ == '__main__':
    main()
