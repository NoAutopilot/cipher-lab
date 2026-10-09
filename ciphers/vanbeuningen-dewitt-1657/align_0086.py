#!/usr/bin/env python3
"""VB-0086 (9 Oct 2026): key test of inv.1537 scan 0086 (Van Beuningen to De Witt, 10 Dec 1656) against the 1657 key.

Pre-registered in PREREG-VB0086.md (pushed before any score). Known-text work: the letter is printed in clear in
Brieven aan Johan de Witt I (1919) pp.365-366 (print_0086.txt); it is used only as a key source.

  python3 align_0086.py --pairs     key-free DP pairing of ciphertext_0086.tsv items to print words -> pairs_0086.tsv
  python3 align_0086.py --score     statistic S, 1,000-permutation null (seed 0), gate S > p99 -> score_0086.json,
                                    key_1656_candidates.tsv, codes_0086.tsv
  python3 align_0086.py --check     re-run both and exit 1 if any committed output differs (rule 7)
"""
import argparse, csv, difflib, json, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
P = lambda f: os.path.join(HERE, f)


def norm(s):
    s = s.lower().replace('ij', 'y')
    s = re.sub(r'[^a-z]', '', s)
    return s.replace('j', 'i').replace('v', 'u')


def load_items():
    items = []
    for r in csv.DictReader(open(P('ciphertext_0086.tsv'), encoding='utf-8'), delimiter='\t'):
        items.append(dict(r))
    # join a C item ending '>' (word continued on the next line) with the next C item
    out, carry = [], None
    for r in items:
        if r['kind'] == 'C':
            if carry is not None:
                r = dict(r, text=carry['text'][:-1] + ',' + r['text'], line=carry['line'] + '+' + r['line'],
                         conf='M' if 'M' in (carry['conf'], r['conf']) else r['conf'])
                carry = None
            if r['text'].endswith('>'):
                carry = r
                continue
        out.append(r)
    return out


def codes_of(text):
    return [c for c in text.rstrip(':').split(',') if c]


def load_print():
    lines = [l.rstrip('\n') for l in open(P('print_0086.txt'), encoding='utf-8') if not l.startswith('#')]
    txt = ''
    for l in lines:
        txt += l[:-1] if l.endswith('-') and not l.endswith(' -') else l + ' '
    txt = txt.replace("'t ", "'t_").replace(' - ', ' ')
    words = []
    for w in txt.split():
        w = w.replace("'t_", "'t ")
        if w.startswith("'t ") and w[3:4].isalpha() and not w[3:].startswith('oogh'):
            w = w.replace(' ', '')        # 'tgetracteerde, 'tgeen: one word in the print
        for part in [w] if not w.startswith("'t ") else ["'t", w[3:]]:
            n = norm(part)
            if n:
                words.append((part.strip('.,;:()'), n))
    return words


def item_kind(r):
    if r['kind'] != 'C':
        return 'W'
    cs = codes_of(r['text'])
    if len(cs) == 1 and len(re.sub(r'\D', '', cs[0])) == 3:
        return 'N'
    return 'L'


def pair():
    items, words = load_items(), load_print()
    n, m = len(items), len(words)
    INF = 1e9
    D = [[INF] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0
    SKIP_I, SKIP_W = 1.0, 1.0
    for i in range(n + 1):
        for j in range(m + 1):
            d = D[i][j]
            if d >= INF:
                continue
            def relax(ii, jj, c, how):
                if ii <= n and jj <= m and d + c < D[ii][jj]:
                    D[ii][jj] = d + c; B[ii][jj] = (i, j, how)
            relax(i + 1, j, SKIP_I, 'skip_item')
            relax(i, j + 1, SKIP_W, 'skip_word')
            if i < n:
                r = items[i]; k = item_kind(r)
                if k == 'W' and j < m:
                    sim = difflib.SequenceMatcher(None, norm(r['text']), words[j][1]).ratio()
                    relax(i + 1, j + 1, (1 - sim) if sim >= 0.5 else 1.8, 'W')
                elif k == 'L':
                    kk = len(codes_of(r['text']))
                    for run in (1, 2):
                        if j + run <= m:
                            ln = sum(len(words[j + t][1]) for t in range(run))
                            relax(i + 1, j + run, 0.5 * abs(kk - ln) + (0.3 if run == 2 else 0), 'L%d' % run)
                elif k == 'N':
                    for run in (1, 2, 3, 4):
                        relax(i + 1, j + run, 0.5 + 0.05 * run, 'N%d' % run)
    i, j, path = n, m, []
    while (i, j) != (0, 0):
        pi, pj, how = B[i][j]
        path.append((pi, pj, i, j, how)); i, j = pi, pj
    path.reverse()
    rows = []
    for pi, pj, i, j, how in path:
        it = items[pi] if i > pi else None
        ws = words[pj:j]
        rows.append({'line': it['line'] if it else '', 'kind': it['kind'] if it else '',
                     'text': it['text'] if it else '', 'conf': it['conf'] if it else '',
                     'move': how, 'print': ' '.join(w[0] for w in ws), 'print_norm': ''.join(w[1] for w in ws)})
    return rows, D[n][m]


def write_tsv(path, rows, cols):
    with open(path, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(cols)
        for r in rows:
            w.writerow([r[c] for c in cols])


def load_key():
    key = {}
    for r in csv.DictReader(open(P('key.tsv'), encoding='utf-8'), delimiter='\t'):
        c = r['code'].rstrip(':')
        if re.fullmatch(r'\d+', c):
            key[c] = (r['value'], r['grade'])
    return key


def scored_positions(pairs, key):
    pos, extra = [], []
    for r in pairs:
        if r['kind'] != 'C' or r['conf'] == 'M' or r['move'] == 'skip_item':
            continue
        cs = codes_of(r['text'])
        if r['move'].startswith('L') and len(cs) == len(r['print_norm']):
            for c, ch in zip(cs, r['print_norm']):
                (pos if c in key else extra).append(('L', c, ch, r['line'], r['print']))
        elif r['move'].startswith('N'):
            (pos if cs[0] in key else extra).append(('N', cs[0], r['print_norm'], r['line'], r['print']))
    return pos, extra


def agree(cls, val, target):
    v = norm(val)
    if cls == 'L':
        return v == target
    return difflib.SequenceMatcher(None, v, target).ratio() >= 0.75


def S(pos, vals):
    a = [agree(cls, vals[c], t) for cls, c, t, _, _ in pos]
    return sum(a) / len(a) if a else 0.0, a


def score():
    pairs = list(csv.DictReader(open(P('pairs_0086.tsv'), encoding='utf-8'), delimiter='\t'))
    key = load_key()
    vals = {c: v for c, (v, g) in key.items()}
    pos, extra = scored_positions(pairs, key)
    s_real, ag = S(pos, vals)
    cls_stats = {}
    for cls in ('L', 'N'):
        sub = [x for x, a in zip(pos, ag) if x[0] == cls]
        cls_stats[cls] = [sum(a for x, a in zip(pos, ag) if x[0] == cls), len(sub)]
    rng = random.Random(0)
    codes = sorted(vals)
    null = []
    for _ in range(1000):
        perm = [vals[c] for c in codes]; rng.shuffle(perm)
        null.append(S(pos, dict(zip(codes, perm)))[0])
    null.sort()
    p99 = null[989]   # 99th percentile of 1,000 (nearest-rank, index 990-1)
    res = {'scored_tokens': len(pos), 'agreements': sum(ag), 'S_real': round(s_real, 4),
           'per_class': {'letter': cls_stats['L'], 'name': cls_stats['N']},
           'null_mean': round(sum(null) / len(null), 4), 'null_p99': round(p99, 4), 'null_max': round(null[-1], 4),
           'gate': 'PASS' if s_real > p99 else 'FAIL',
           'excluded_M_items': sum(1 for r in pairs if r['kind'] == 'C' and r['conf'] == 'M'),
           'unscored_C_items': sum(1 for r in pairs if r['kind'] == 'C' and r['conf'] != 'M' and
                                   not (r['move'].startswith('N') or (r['move'].startswith('L') and
                                        len(codes_of(r['text'])) == len(r['print_norm']))))}
    # per-code table
    per = {}
    for (cls, c, t, line, pr), a in zip(pos, ag):
        d = per.setdefault(c, {'code': c, 'key_value': vals[c], 'key_grade': key[c][1], 'n': 0, 'agree': 0, 'print': []})
        d['n'] += 1; d['agree'] += a; d['print'].append(t if cls == 'L' else pr)
    rows = []
    for c in sorted(per, key=int):
        d = per[c]; rows.append(dict(d, print=' '.join(d['print'])))
    write_tsv(P('codes_0086.tsv'), rows, ['code', 'key_value', 'key_grade', 'n', 'agree', 'print'])
    res['M_codes_second_context'] = [r['code'] for r in rows if r['key_grade'] == 'M' and r['agree'] > 0]
    res['disagreements'] = [(r['code'], r['key_value'], r['print']) for r in rows if r['agree'] < r['n']]
    cand = {}
    for cls, c, t, line, pr in extra:
        d = cand.setdefault(c, {'code': c, 'class': 'letter' if cls == 'L' else 'name', 'print_values': [], 'lines': [],
                                'grade': 'C', 'source': 'print alignment, Brieven aan Johan de Witt I pp.365-366 (VB-0086)'})
        d['print_values'].append(t if cls == 'L' else pr); d['lines'].append(line)
    crow = [dict(d, print_values=' | '.join(d['print_values']), lines=' '.join(d['lines'])) for c, d in
            sorted(cand.items(), key=lambda x: int(x[0]))]
    write_tsv(P('key_1656_candidates.tsv'), crow, ['code', 'class', 'print_values', 'lines', 'grade', 'source'])
    res['candidates'] = len(crow)
    with open(P('score_0086.json'), 'w') as f:
        json.dump(res, f, indent=1, ensure_ascii=False); f.write('\n')
    return res


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--pairs', action='store_true'); ap.add_argument('--score', action='store_true')
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    if a.check:
        outs = ['pairs_0086.tsv', 'score_0086.json', 'codes_0086.tsv', 'key_1656_candidates.tsv']
        before = {f: open(P(f), encoding='utf-8').read() for f in outs}
        rows, _ = pair(); write_tsv(P('pairs_0086.tsv'), rows, ['line', 'kind', 'text', 'conf', 'move', 'print', 'print_norm'])
        score()
        stale = [f for f in outs if open(P(f), encoding='utf-8').read() != before[f]]
        for f in outs:
            open(P(f), 'w', encoding='utf-8').write(before[f])
        print('stale: ' + ', '.join(stale) if stale else 'up to date')
        sys.exit(1 if stale else 0)
    if a.pairs:
        rows, cost = pair()
        write_tsv(P('pairs_0086.tsv'), rows, ['line', 'kind', 'text', 'conf', 'move', 'print', 'print_norm'])
        print('pairs_0086.tsv: %d rows, DP cost %.2f' % (len(rows), cost))
    if a.score:
        print(json.dumps(score(), indent=1, ensure_ascii=False))


if __name__ == '__main__':
    main()
