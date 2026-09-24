#!/usr/bin/env python3
"""Folio 67 (canvas 129/130, Brienne to Servien, 10 Oct 1659): read ciphertext_f67.tsv with key_1659.tsv, grade per
token, and run the word-level control (24 Sept 2026).

    python3 read_f67.py            write exceptions_f67.tsv and control_f67.tsv, print the tables
    python3 read_f67.py --check    exit 1 if either committed file differs from what this script writes
Then: python3 ../../tools/decode_key.py . --config decode_f67.json [--check] writes reading_f67.txt / reading_f67.tsv.

Grades (brief lane-g2-m). key_1659 is grade C on the f.86/f.88 letter it was recovered from; on this different letter:
  S  keyed, key row not 'conflict', the group read at conf H, and its letters fall inside a French word (below);
  M  keyed but the key row is 'conflict', or the group is conf M, or its letters fall outside every French word;
  U  code not in key_1659 and no proposal;
  I  code not in key_1659, value proposed from context only (PROPOSE below; each used at least twice or in a
     word that is otherwise fully keyed). No H: no key source.
French word test: the reading of each run (maximal stretch of cipher groups between clear words and punctuation,
continuing over line ends) is segmented by dynamic programming into lexicon words, maximising the letters covered;
lexicon = words of 3+ letters seen at least 5 times in tools/data/fr16 (period French letters), folded as
tools/french16_ngram.fold (J->I, U->V). A letter is 'in a French word' if the best segmentation covers it.

Control (rule 3): key_1659's values permuted over its codes, 200 derangements (no code keeps its value), seed 1659;
the same segmentation on the same runs; statistic = share of keyed letters covered by lexicon words (I values are
not used in the true or the control score). Holdout: the same statistic with key_1659_f86only.tsv (65 groups, f.86
alone, before f.88 was aligned)."""
import collections, csv, os, random, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
import french16_ngram as fr

NONSIGN = {',', ';', '.', ':', '—', 'X'}
NDER, SEED, MINCOUNT, MINLEN = 200, 1659, 5, 3
# code -> (value, where it is needed); proposals from context only, grade I
PROPOSE = {
    '72': ('ni', 'f129 L08 "du ma[ni]ement des affaires"; L13 "mi[ni]stres" (with 67)'),
    '67': ('mi', 'f129 L13 "[mi]nistres" (with 72)'),
    '32': ('ci', 'f129 L12 "prin[ci]paux"'),
    '43': ('fo', 'f129 L04 "[fo]rt d\'estre"; f130a L04 "[fo]ndement"'),
    '68': ('mo', 'f130a L05, L06 "Ma de[mo]iselle" twice'),
    '63': ('lo', 'f130a L04 "que [lo]n publie"'),
}


def load_key(fn):
    k = {}
    for r in csv.DictReader(open(os.path.join(HERE, fn), encoding='utf-8'), delimiter='\t'):
        k[r['code']] = (r['value'], 'conflict' in r.get('note', ''))
    return k


def load_ct():
    rows = []
    for r in csv.DictReader(open(os.path.join(HERE, 'ciphertext_f67.tsv'), encoding='utf-8'), delimiter='\t'):
        folio, line = r['line'].split('_', 1)
        rows.append(dict(folio=folio, line=line, pos=int(r['pos']), g=r['group'], conf=r['conf']))
    return rows


def runs(rows):
    """Maximal stretches of cipher groups (indexes into rows)."""
    out, cur = [], []
    for i, r in enumerate(rows):
        if r['g'].startswith('[') or r['g'] in NONSIGN:
            if cur:
                out.append(cur); cur = []
        else:
            cur.append(i)
    if cur:
        out.append(cur)
    return out


def lexicon():
    c = collections.Counter(fr.corpus_words())
    return {w for w, n in c.items() if n >= MINCOUNT and len(w) >= MINLEN}


def fold(v):
    return ''.join(ch for ch in fr.fold(v) if 'A' <= ch <= 'Z')


def covered(s, lex, maxw=16):
    """Best segmentation of s: boolean per letter, True where a lexicon word covers it. '?' never covered."""
    n = len(s)
    best = [0] * (n + 1); back = [None] * (n + 1)
    for i in range(1, n + 1):
        best[i], back[i] = best[i - 1], (i - 1, False)
        for j in range(max(0, i - maxw), i - MINLEN + 1):
            w = s[j:i]
            if '?' not in w and w in lex and best[j] + (i - j) > best[i]:
                best[i], back[i] = best[j] + (i - j), (j, True)
    cov = [False] * n; i = n
    while i > 0:
        j, isw = back[i]
        if isw:
            for t in range(j, i):
                cov[t] = True
        i = j
    return cov


def score(rows, rs, val, lex):
    """val: code -> folded value. Returns (covered keyed letters, keyed letters, per-row covered flag)."""
    tot = cov_n = 0; flag = {}
    for run in rs:
        s, owner = '', []
        for i in run:
            v = val.get(rows[i]['g'])
            v = '?' if v is None else v
            s += v; owner += [i] * len(v)
        cov = covered(s, lex)
        for ch, i, c in zip(s, owner, cov):
            if ch != '?':
                tot += 1; cov_n += c
                flag.setdefault(i, []).append(c)
    return cov_n, tot, {i: all(f) for i, f in flag.items()}


def derange(codes, vals, rng):
    while True:
        p = vals[:]; rng.shuffle(p)
        if all(a != b for a, b in zip(p, vals)):
            return dict(zip(codes, p))


def build():
    rows, key, lex = load_ct(), load_key('key_1659.tsv'), lexicon()
    rs = runs(rows)
    kval = {c: fold(v) for c, (v, _) in key.items()}
    # true and control
    t_cov, t_tot, _ = score(rows, rs, kval, lex)
    codes = sorted(kval); vals = [kval[c] for c in codes]
    rng = random.Random(SEED); ctl = []
    for _ in range(NDER):
        c, t, _ = score(rows, rs, derange(codes, vals, rng), lex)
        ctl.append(c / t)
    hk = load_key('key_1659_f86only.tsv')
    h_cov, h_tot, _ = score(rows, rs, {c: fold(v) for c, (v, _) in hk.items()}, lex)
    cip = [r for r in rows if not (r['g'].startswith('[') or r['g'] in NONSIGN)]
    keyed = sum(r['g'] in key for r in cip); hkeyed = sum(r['g'] in hk for r in cip)
    differ = sum(r['g'] in key and r['g'] in hk and key[r['g']][0] != hk[r['g']][0] for r in cip)
    # grading, with I proposals filled in for the segmentation
    full = dict(kval); full.update({c: fold(v) for c, (v, _) in PROPOSE.items()})
    _, _, inword = score(rows, rs, full, lex)
    exc = ['folio\tline\tpos\tvalue\tgrade\treason']; counts = collections.Counter()
    for i, r in enumerate(rows):
        g = r['g']
        if g.startswith('[') or g in NONSIGN:
            continue
        if g in key:
            v, conflict = key[g]
            if conflict:
                gr, why = 'M', 'key row conflict'
            elif r['conf'] != 'H':
                gr, why = 'M', 'group read at conf M'
            elif inword.get(i):
                gr, why = 'S', 'inside a French word'
            else:
                gr, why = 'M', 'outside every French word'
        elif g in PROPOSE:
            v, why = PROPOSE[g]; gr = 'I'; why = 'proposed from context: ' + why
        else:
            counts['U'] += 1
            continue
        counts[gr] += 1
        exc.append(f"{r['folio']}\t{r['line']}\t{r['pos']}\t{v}\t{gr}\t{why}")
    m, sd = statistics.mean(ctl), statistics.pstdev(ctl)
    ctl_rows = ['measure\tvalue',
                f'cipher_groups\t{len(cip)}', f'keyed_key_1659\t{keyed}', f'coverage\t{keyed/len(cip):.3f}',
                f'lexicon_words\t{len(lex)}',
                f'true_covered_letters\t{t_cov}/{t_tot}', f'true_rate\t{t_cov/t_tot:.3f}',
                f'control_derangements\t{NDER}', f'control_mean\t{m:.3f}', f'control_sd\t{sd:.3f}',
                f'control_max\t{max(ctl):.3f}', f'control_ge_true\t{sum(c >= t_cov/t_tot for c in ctl)}',
                f'z\t{(t_cov/t_tot - m)/sd:.2f}',
                f'holdout_f86only_keyed\t{hkeyed}', f'holdout_f86only_covered_letters\t{h_cov}/{h_tot}',
                f'holdout_f86only_rate\t{h_cov/h_tot:.3f}', f'holdout_tokens_value_differs\t{differ}',
                'grades\t' + ' '.join(f'{g} {counts[g]}' for g in 'SMUI')]
    return '\n'.join(exc) + '\n', '\n'.join(ctl_rows) + '\n'


def main():
    exc, ctl = build()
    files = {'exceptions_f67.tsv': exc, 'control_f67.tsv': ctl}
    if '--check' in sys.argv:
        bad = [f for f, t in files.items() if open(os.path.join(HERE, f), encoding='utf-8').read() != t]
        print('stale: ' + ', '.join(bad) if bad else 'exceptions_f67.tsv, control_f67.tsv up to date')
        sys.exit(1 if bad else 0)
    for f, t in files.items():
        open(os.path.join(HERE, f), 'w', encoding='utf-8').write(t)
    print(ctl)


if __name__ == '__main__':
    main()
