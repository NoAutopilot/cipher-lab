#!/usr/bin/env python3
"""VIV-KEY (PREREG-VIVKEY.md): pool the ink-40 clerk word anchors (VIV-ANCHOR, tx/vivanchor_result.json) with the ink-67 clerk DP anchors
(VIV-67, tx/viv67_labels.tsv, dp_conf >= 0.5) per reader label, and apply VIV-ANCHOR's decision rule (top letter >= 3 positions and >= 2/3
of the pooled counting positions; a label whose ink-40 and ink-67 tops differ is a CONFLICT). Counts only: this script edits nothing.

    python3 ciphers/fr16104-vivonne-spain-1572/tx/vivkey.py [--check]

Writes tx/vivkey_tally.tsv and tx/vivkey_result.json; --check exits 1 if either is stale.
"""
import csv, json, os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
CONF = 0.5


def key_labels():
    """key.tsv as it stood before this job (rows whose source names VIV-KEY are its own output, not an input)."""
    return {r['code']: (r['meaning'], r['grade']) for r in csv.DictReader(open(os.path.join(T, 'key.tsv'), encoding='utf-8'), delimiter='\t')
            if 'VIV-KEY' not in r['source']}


def tally():
    a40 = json.load(open(os.path.join(HERE, 'vivanchor_result.json'), encoding='utf-8'))['target']['label_centric']
    i40 = {L: Counter(v['values']) for L, v in a40.items()}
    i67_all, i67 = {}, {}
    for r in csv.DictReader(open(os.path.join(HERE, 'viv67_labels.tsv'), encoding='utf-8'), delimiter='\t'):
        L, x = r['label'], r['aligned_letter']
        if L.startswith('{') or len(x) != 1 or not x.isalpha():
            continue
        i67_all.setdefault(L, Counter())[x] += 1
        if float(r['dp_conf']) >= CONF:
            i67.setdefault(L, Counter())[x] += 1
    return i40, i67_all, i67


def top(c):
    if not c:
        return None
    m = c.most_common()
    return m[0][0] if len(m) == 1 or m[0][1] > m[1][1] else None


def decide():
    key = key_labels(); i40, i67_all, i67 = tally(); rows = []
    for L in sorted(set(i40) | set(i67_all)):
        if L.startswith('{'):
            continue
        aligned = sum(i40.get(L, Counter()).values()) + sum(i67_all.get(L, Counter()).values())
        pooled = i40.get(L, Counter()) + i67.get(L, Counter())
        n = sum(pooled.values()); x = top(pooled); cx = pooled[x] if x else 0
        t40, t67 = top(i40.get(L, Counter())), top(i67.get(L, Counter()))
        keyed = L in key
        if aligned < 3:
            dec = 'not a candidate (< 3 aligned)'
        elif t40 and t67 and t40 != t67:
            dec = f'CONFLICT (ink 40 top {t40}, ink 67 top {t67})'
        elif x and cx >= 3 and cx / n >= 2 / 3:
            dec = f'-> {x}'
        else:
            dec = 'under rule'
        if keyed and dec.startswith('->'):
            dec = ('confirms key ' if x == key[L][0] else 'CONFLICT with key ') + f'{key[L][0]} ({dec}); report-only'
        elif keyed:
            dec = f'keyed {key[L][0]} {key[L][1]}; {dec}; report-only'
        fmt = lambda c: ','.join(f'{k}:{v}' for k, v in c.most_common()) if c else ''
        rows.append({'label': L, 'keyed': f'{key[L][0]} {key[L][1]}' if keyed else '', 'aligned_pooled': aligned,
                     'ink40': fmt(i40.get(L)), 'ink67_conf>=0.5': fmt(i67.get(L)), 'ink67_all': fmt(i67_all.get(L)),
                     'pooled_n': n, 'top': x or '', 'top_n': cx, 'share': round(cx / n, 3) if n else 0, 'decision': dec})
    return rows


def main():
    rows = decide()
    cols = list(rows[0])
    tsv = '\t'.join(cols) + '\n' + ''.join('\t'.join(str(r[c]) for c in cols) + '\n' for r in rows)
    js = json.dumps({'conf': CONF, 'rows': rows, 'assign': {r['label']: r['top'] for r in rows if r['decision'].startswith('->')}},
                    indent=1, ensure_ascii=False) + '\n'
    out = {os.path.join(HERE, 'vivkey_tally.tsv'): tsv, os.path.join(HERE, 'vivkey_result.json'): js}
    if '--check' in sys.argv:
        stale = [p for p, s in out.items() if not os.path.exists(p) or open(p, encoding='utf-8').read() != s]
        print('stale: ' + ', '.join(stale) if stale else 'ok'); sys.exit(1 if stale else 0)
    for p, s in out.items():
        open(p, 'w', encoding='utf-8').write(s)
    print(tsv)


if __name__ == '__main__':
    main()
