#!/usr/bin/env python3
"""GAPS94: dump every word-list-matched span of ciphertext_fig1.txt (Malay and Arabic lists of GAPS93) to a TSV.

Usage: dump_spans.py --leipzig MSA_SENTENCES_TXT --quran TANZIL_TXT2 [--out spans.tsv]
Same lists, skeletons and tiling as match2.py / ../tausug/match.py (imported). One row per span of 1-3 consecutive
visible groups (no OBSCURED inside) whose consonant skeleton (tooth expanded) is in a list at length >= 2; `chosen_C3`
/ `chosen_C2` mark the spans the coverage tiling actually picked. `words` = the list's commonest words with that
skeleton (up to 6, with counts). Sources fetched to scratch; neither committed (manifest.json).
"""
import argparse, collections, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tausug'))
from match import read_target, span_skels, roman_skel, CT  # noqa: E402
from match2 import leipzig, quran, ar_skel  # noqa: E402


def raw_groups():
    import re
    out = []
    for raw in open(CT, encoding='utf-8'):
        if re.match(r'^L\d\d:', raw):
            out.append([g.strip() for g in raw.split(':', 1)[1].split('|')])
    return out


def tiling(groups, S, minlen):
    n = len(groups)
    best = [(0, [])] * (n + 1)
    for i in range(1, n + 1):
        best[i] = best[i - 1]
        for k in (1, 2, 3):
            j = i - k
            if j < 0 or any(g is None for g in groups[j:i]):
                continue
            signs = [c for g in groups[j:i] for c in g]
            hit = max([len(s) for s in span_skels(signs) if len(s) >= minlen and s in S] or [0])
            if hit and best[j][0] + hit > best[i][0]:
                best[i] = (best[j][0] + hit, best[j][1] + [(j, i)])
    return set(best[n][1])


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--leipzig', required=True)
    ap.add_argument('--quran', required=True)
    ap.add_argument('--out', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spans.tsv'))
    a = ap.parse_args()
    target, raw = read_target(), raw_groups()
    ms_list, _ = leipzig(a.leipzig)
    ar_list, ar_held = quran(a.quran, 91)
    if len(ar_held) < 1000:
        ar_list, _ = quran(a.quran, 78)
    lists = {}
    for name, words, sk in (('MS', ms_list, roman_skel), ('AR', ar_list, ar_skel)):
        idx = collections.defaultdict(collections.Counter)
        for w in words:
            s = sk(w)
            if len(s) >= 2:
                idx[s][w.lower() if name == 'MS' else w] += 1
        lists[name] = idx
    rows = []
    for name, idx in lists.items():
        S = set(idx)
        for li, groups in enumerate(target):
            ch3, ch2 = tiling(groups, S, 3), tiling(groups, S, 2)
            for j in range(len(groups)):
                for k in (1, 2, 3):
                    i = j + k
                    if i > len(groups) or any(g is None for g in groups[j:i]):
                        continue
                    signs = [c for g in groups[j:i] for c in g]
                    hits = sorted({s for s in span_skels(signs) if len(s) >= 2 and s in S}, key=len, reverse=True)
                    if not hits:
                        continue
                    s = hits[0]
                    ws = ' '.join('%s:%d' % wc for wc in idx[s].most_common(6))
                    rows.append([name, 'L%02d' % (li + 1), str(j + 1), str(i), ' | '.join(raw[li][j:i]), s, str(len(s)),
                                 'y' if (j, i) in ch3 else '', 'y' if (j, i) in ch2 else '', str(sum(idx[s].values())), ws])
    with open(a.out, 'w', encoding='utf-8') as f:
        f.write('list\tline\tgroup_from\tgroup_to\tsigns\tskeleton\tskel_len\tchosen_C3\tchosen_C2\tlist_tokens\twords\n')
        for r in rows:
            f.write('\t'.join(r) + '\n')
    print('%d rows -> %s' % (len(rows), a.out))
    for name in lists:
        c3 = [r for r in rows if r[0] == name and r[7]]
        print(name, 'chosen_C3 spans', len(c3), 'consonants', sum(int(r[6]) for r in c3))


if __name__ == '__main__':
    main()
