#!/usr/bin/env python3
"""GAPS98: pre-registered comparison of the blind VISION reader (vision_out.json) with spans.tsv and the GAPS94 text reader.

Usage: compare_vision.py --leipzig MSA_SENTENCES_TXT --quran TANZIL_TXT [--out compare_vision.json]   (see PREREG.md)
Items whose line/groups fall outside ciphertext_fig1.txt's group counts are dropped and counted.
S1/S2: ../reader/compare.py run unchanged on the valid vision items (same statistics as GAPS94).
S3: vision items sharing >= 1 group with a GAPS94 text-reader item on the same line, vs uniform placement of a span of the
    same width among valid positions; exact Poisson-binomial one-sided p (all items, and H/M items).
S4: among S3-overlapping (vision, text) pairs, equal Arabic consonant skeleton (match2.ar_skel); chance rate r = share of
    ALL (vision item, text item) pairs with equal skeleton, expected = r x number of overlapping pairs; descriptive.
"""
import argparse, json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'tausug'))
sys.path.insert(0, os.path.join(HERE, '..', 'malay-arabic'))
sys.path.insert(0, os.path.join(HERE, '..', 'reader'))
from match import read_target  # noqa: E402
from match2 import ar_skel  # noqa: E402
from compare import poibin_ge  # noqa: E402


def letters(s):
    return ''.join(c for c in (s or '') if 'ء' <= c <= 'ي')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--leipzig', required=True)
    ap.add_argument('--quran', required=True)
    ap.add_argument('--vision', default=os.path.join(HERE, 'vision_out.json'))
    ap.add_argument('--text', default=os.path.join(HERE, '..', 'reader', 'reader_out.json'))
    ap.add_argument('--out', default=os.path.join(HERE, 'compare_vision.json'))
    a = ap.parse_args()
    target = read_target()
    raw = json.load(open(a.vision, encoding='utf-8'))
    valid, dropped = [], []
    for it in raw.get('items', []):
        try:
            li = int(it['line'][1:]) - 1
            g0, g1 = int(it['group_from']), int(it['group_to'])
            ok = 0 <= li < len(target) and 1 <= g0 <= g1 <= len(target[li])
        except (KeyError, ValueError, TypeError):
            ok = False
        (valid if ok else dropped).append(it)
    vpath = os.path.join(HERE, 'vision_items_valid.json')
    json.dump({'items': valid}, open(vpath, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    spath = os.path.join(HERE, 'compare_spans.json')
    subprocess.run([sys.executable, os.path.join(HERE, '..', 'reader', 'compare.py'), '--leipzig', a.leipzig,
                    '--quran', a.quran, '--reader', vpath, '--out', spath], check=True, stdout=subprocess.DEVNULL)
    s12 = json.load(open(spath, encoding='utf-8'))
    text = json.load(open(a.text, encoding='utf-8'))['items']
    res = {'n_raw': len(raw.get('items', [])), 'n_valid': len(valid), 'n_dropped': len(dropped),
           'group_count_seen': raw.get('group_count_seen'), 'S1_all': s12['S1_all'], 'S1_HM': s12['S1_HM'],
           'S2_all': s12['S2_all'], 'S2_HM': s12['S2_HM'], 'items': []}
    pairs_all = [(ar_skel(letters(v.get('arabic'))), ar_skel(letters(t.get('arabic')))) for v in valid for t in text]
    r = sum(x == y for x, y in pairs_all) / len(pairs_all) if pairs_all else 0.0
    n_pairs = n_eq = 0
    for v, s in zip(valid, s12['items']):
        ln, g0, g1 = v['line'], int(v['group_from']), int(v['group_to'])
        groups = target[int(ln[1:]) - 1]
        width = g1 - g0 + 1
        tcov = set()
        for t in text:
            if t['line'] == ln:
                tcov.update(range(int(t['group_from']), int(t['group_to']) + 1))
        vpos = [j for j in range(1, len(groups) - width + 2) if all(groups[k - 1] is not None for k in range(j, j + width))]
        p_exp = len([j for j in vpos if tcov & set(range(j, j + width))]) / len(vpos) if vpos else 0.0
        over = [t for t in text if t['line'] == ln and set(range(int(t['group_from']), int(t['group_to']) + 1)) & set(range(g0, g1 + 1))]
        eq = [t['roman'] for t in over if ar_skel(letters(t.get('arabic'))) == ar_skel(letters(v.get('arabic')))]
        n_pairs += len(over)
        n_eq += len(eq)
        res['items'].append(dict(s, x=[v.get('x_from'), v.get('x_to')], assumed_misreads=v.get('assumed_misreads'),
                                 S3_overlap_text=bool(over), S3_p_expected=round(p_exp, 4),
                                 S4_text_overlaps=[t['roman'] for t in over], S4_same_skeleton=eq))
    for tag, sel in (('all', lambda x: True), ('HM', lambda x: x['confidence'] in ('H', 'M'))):
        its = [x for x in res['items'] if sel(x)]
        o = sum(x['S3_overlap_text'] for x in its)
        ps = [x['S3_p_expected'] for x in its]
        res['S3_' + tag] = {'N': len(its), 'observed': o, 'expected': round(sum(ps), 3),
                            'p_one_sided': round(poibin_ge(ps, o), 4) if its else None}
    res['S4'] = {'overlapping_pairs': n_pairs, 'same_skeleton': n_eq, 'chance_rate_r': round(r, 4),
                 'expected': round(r * n_pairs, 3)}
    res['grades'] = s12['grades']
    res['dropped'] = dropped
    for k in ('overall', 'language_guess', 'language_confidence'):
        res[k] = raw.get(k)
    js = json.dumps(res, indent=1, ensure_ascii=False)
    print(js)
    open(a.out, 'w', encoding='utf-8').write(js + '\n')


if __name__ == '__main__':
    main()
