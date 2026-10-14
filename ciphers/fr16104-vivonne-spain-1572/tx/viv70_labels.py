#!/usr/bin/env python3
"""VIV-70 (PREREG-VIV70 "If PASS" (a)): every token of tx/f211r_rec.tsv whose label is outside the published key
(key_tomokiyo.tsv) or M-graded in key.tsv, with the clerk letter the PREREG alignment puts against it and the local DP
confidence (share of keyed neighbours within 8 positions that decode to their aligned letter). Counts only: no key edit.
Alignment: PREREG-VIV70B's trimmed target (first int(519 x 1403/1270) + 200 = 773 letters of dec70; b.load(trim=True)), the run
whose control passed (tx/vivk70b_result.json); the untrimmed PREREG-VIV70 run failed and is never used here.

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv70_labels.py [--check]

Writes tx/viv70_labels.tsv (one row per occurrence) and tx/viv70_labels_summary.tsv (per label: n, aligned, top letters,
top letters at confidence >= 0.5); --check exits 1 if either committed file is stale.
"""
import os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'benchmark-tx'))
import build_vivonne_f211r as b  # noqa: E402


def main():
    pub, force, grade, let, stream = b.load(trim=True)
    seq = [t[0] for t in stream]
    amap, dec = b.c2.align(seq, let, pub)
    keyed = lambda k: dec[k] >= 0 and k in amap
    ok = lambda k: keyed(k) and dec[k] == let[amap[k]]
    rows, per = [], {}
    for k, (code, line, raws) in enumerate(stream):
        if code in pub and grade.get(code) != 'M':
            continue
        nb = [j for j in range(k - 8, k + 9) if j != k and 0 <= j < len(stream) and keyed(j)]
        conf = sum(1 for j in nb if ok(j)) / len(nb) if nb else 0.0
        letter = chr(97 + let[amap[k]]) if k in amap else '-'
        ctx = ''.join(chr(97 + let[amap[j]]) if j in amap else '.' for j in range(max(0, k - 4), min(len(seq), k + 5)))
        rows.append((code, 'f211r_' + line, raws[0], letter, '%.2f' % conf, ctx))
        per.setdefault(code, []).append((letter, conf))
    occ = 'label\tline\tpos\taligned_letter\tdp_conf\tclerk_context_k-4..k+4\n' + ''.join('\t'.join(map(str, r)) + '\n' for r in rows)
    summ = 'label\tstatus\tn\taligned\ttop_aligned\ttop_aligned_conf>=0.5\n'
    for code in sorted(per, key=lambda c: -len(per[c])):
        v = per[code]
        al = [l for l, c in v if l != '-']
        hi = [l for l, c in v if l != '-' and c >= 0.5]
        st = 'M (key.tsv %s=%s)' % (code, pub.get(code, '?')) if code in pub else 'outside published key'
        fmt = lambda xs: ','.join('%s:%d' % kv for kv in Counter(xs).most_common(4))
        summ += '%s\t%s\t%d\t%d\t%s\t%s\n' % (code, st, len(v), len(al), fmt(al), fmt(hi))
    outs = {'viv70_labels.tsv': occ, 'viv70_labels_summary.tsv': summ}
    if '--check' in sys.argv:
        stale = [n for n, w in outs.items() if open(os.path.join(HERE, n), encoding='utf-8').read() != w]
        print('stale: ' + ', '.join(stale) if stale else 'ok'); sys.exit(1 if stale else 0)
    for n, w in outs.items():
        open(os.path.join(HERE, n), 'w', encoding='utf-8').write(w)
    print(summ)


if __name__ == '__main__':
    main()
