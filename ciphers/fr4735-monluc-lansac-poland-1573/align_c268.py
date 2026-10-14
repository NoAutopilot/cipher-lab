#!/usr/bin/env python3
"""MONL-ALIGN (14 Oct 2026): align the c268 (f.138) cipher lines 1-5 against the reconciled clear text of ff.140r-141r.

Usage: python3 align_c268.py [--draws 200] [--seed 140] [--check] [--clear passes/align/f140r_passA.tsv] [--no-fold-iy]

Inputs: ciphertext_c268.tsv (pass A base, K38 relabel; the transcription as committed), key.tsv (Tomokiyo's published Monluc
Cipher 1 table), clear_f140.tsv (MONL-ALIGN reconciled clear text of ff.140r-141r; a word in [..] is unsure, still used).
Method (no cryptanalysis; every meaning comes from the clear text): one dynamic-programming alignment of the whole c268 token
stream against a local span of the whole clear letter (free start and end in the clear). A keyed token takes one clear
letter (+2 when it equals its table letter, i/j/y, u/v folded (y since MONL-EYE); -1 when it differs = a contradiction) or none (-2, an extra sign);
a clear letter no token takes costs -2 (an omission); an unkeyed sign (?...) or a W: word token takes 0-14 clear letters at
0 (-0.1 per letter) -- these are the name/code groups the clear text fills. Per token the result is confirm / contradict /
extra / fill. Statistic: confirm share of keyed tokens (confirmed / keyed).
Controls (rule 3; each can move the statistic): (1) shuffled clear: the clear letter's words dealt in random order, the same
alignment, --draws times; (2) a clear text of a different letter: f.139 (c270_text.txt), the letter's clear continuation.
Writes align_c268.tsv (per token), results_align_c268.json, votes_c268.tsv and exceptions_c268.tsv (decode.json job c268); --check exits 1 when either is stale (rule 7).
"""
import argparse, json, random, re, sys, unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAXCHUNK = 14
# unkeyed signs the clear text fills (MONL-ALIGN): C where the chunk is the same at every occurrence of the sign or a
# whole clear word; M where the chunk boundary is set by the alignment alone. Asserted against the alignment on each run.
FILLS = {
    ('L01', 16): ('lempereur', 'C', 'W:mihil + W:Cur = lempereur (clear f.140r L07), name pair; letters on mihil'),
    ('L01', 17): ('NULL', 'C', 'second word of the lempereur pair'),
    ('L02', 8): ('c', 'C', 'h_bar = c (3/3 occurrences in L01-L05)'), ('L02', 34): ('c', 'C', 'h_bar = c (3/3 occurrences in L01-L05)'),
    ('L03', 32): ('c', 'C', 'h_bar = c (3/3 occurrences in L01-L05)'),
    ('L02', 26): ('c', 'C', 'double_slash = c in conscience'), ('L02', 30): ('c', 'C', 'double_slash = c in conscience'),
    ('L05', 22): ('onc', 'M', 'double_slash in conclusion; chunk boundary set by the alignment'),
}


def fold(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if c.isalpha() and ord(c) < 128)
    s = s.replace('j', 'i').replace('v', 'u')
    return s.replace('y', 'i') if FOLD_IY else s


FOLD_IY = True  # MONL-EYE (PREREG-MONL-IY.md): y -> i fold kept, all three registered conditions met; --no-fold-iy for the unfolded run


def load_tokens():
    rows = [l.rstrip('\n').split('\t') for l in open(HERE / 'ciphertext_c268.tsv', encoding='utf-8')][1:]
    key = {}
    for l in list(open(HERE / 'key.tsv', encoding='utf-8'))[1:]:
        f = l.rstrip('\n').split('\t')
        key[f[0]] = f[2]
    toks = []
    for f in rows:
        sign = f[2]
        val = key.get(sign)
        toks.append({'line': f[0], 'pos': int(f[1]), 'sign': sign, 'conf': f[3],
                     'value': fold(val) if val else None})
    return toks


CLEAR = 'clear_f140.tsv'


def load_clear():
    words = []
    for l in list(open(HERE / CLEAR, encoding='utf-8'))[1:]:
        f = l.rstrip('\n').split('\t')
        for w in f[2].split():
            fw = fold(w)
            if fw:
                words.append((f[0], f[1], fw, w.startswith('[') and not w.startswith('[?')))
    return words


def align(toks, clear):
    """clear: string of letters. Returns (score, path) with path = list of (token index, clear start, clear end)."""
    n, m = len(toks), len(clear)
    NEG = -1e9
    dp = [[NEG] * (m + 1) for _ in range(n + 1)]
    bk = [[None] * (m + 1) for _ in range(n + 1)]
    for j in range(m + 1):
        dp[0][j] = 0.0  # free start in the clear
    for i in range(1, n + 1):
        t = toks[i - 1]
        row, prev = dp[i], dp[i - 1]
        for j in range(m + 1):
            best, arg = NEG, None
            if t['value'] is not None:
                if j >= 1 and prev[j - 1] > NEG:
                    s = prev[j - 1] + (2.0 if clear[j - 1] == t['value'] else -1.0)
                    if s > best:
                        best, arg = s, ('tok', j - 1)
                if prev[j] - 2.0 > best:
                    best, arg = prev[j] - 2.0, ('tok', j)
            else:
                for k in range(0, min(MAXCHUNK, j) + 1):
                    s = prev[j - k] - 0.1 * k
                    if s > best:
                        best, arg = s, ('tok', j - k)
            if j >= 1 and row[j - 1] - 2.0 > best:  # clear letter with no token
                best, arg = row[j - 1] - 2.0, ('gap', j - 1)
            row[j], bk[i][j] = best, arg
    j = max(range(m + 1), key=lambda x: dp[n][x])  # free end
    score, end = dp[n][j], j
    path, i = [], n
    while i > 0:
        kind, pj = bk[i][j]
        if kind == 'tok':
            path.append((i - 1, pj, j)); i, j = i - 1, pj
        else:
            j = pj
    path.reverse()
    return score, path, (path[0][1] if path else 0), end


def classify(toks, clear, path, unsure=None):
    out = []
    for ti, a, b in path:
        t, chunk = toks[ti], clear[a:b]
        uns = bool(unsure and any(unsure[a:b]))
        if t['value'] is None:
            kind = 'fill' if chunk else 'fill-empty'
        elif not chunk:
            kind = 'extra'
        elif chunk == t['value']:
            kind = 'confirm'
        else:
            kind = 'contradict'
        out.append({**t, 'clear': chunk, 'kind': kind, 'cpos': a, 'unsure': uns})
    return out


def stats(rows):
    keyed = [r for r in rows if r['value'] is not None]
    c = sum(r['kind'] == 'confirm' for r in keyed)
    return {'keyed': len(keyed), 'confirm': c, 'contradict': sum(r['kind'] == 'contradict' for r in keyed),
            'extra': sum(r['kind'] == 'extra' for r in keyed), 'confirm_share': round(c / len(keyed), 4)}


def run(draws, seed):
    toks = load_tokens()
    words = load_clear()
    clear = ''.join(w[2] for w in words)
    unsure = [w[3] for w in words for _ in w[2]]
    score, path, a, b = align(toks, clear)
    rows = classify(toks, clear, path, unsure)
    real = stats(rows)
    rng = random.Random(seed)
    ws = [w[2] for w in words]
    shuf = []
    for _ in range(draws):
        rng.shuffle(ws)
        sc, p, _, _ = align(toks, ''.join(ws))
        shuf.append(stats(classify(toks, ''.join(ws), p))['confirm_share'])
    shuf.sort()
    c270 = fold(open(HERE / 'c270_text.txt', encoding='utf-8').read())
    sc, p, _, _ = align(toks, c270)
    other = stats(classify(toks, c270, p))
    # map the aligned clear span back to its page/line
    pos, spans = 0, []
    for pg, ln, w, _u in words:
        if pos + len(w) > a and pos < b:
            spans.append(f'{pg}:{ln}')
        pos += len(w)
    res = {'real': real, 'score': round(score, 1), 'clear_span': [spans[0], spans[-1]] if spans else None,
           'clear_letters': len(clear),
           'shuffled_clear': {'draws': draws, 'seed': seed, 'mean': round(sum(shuf) / len(shuf), 4),
                              'p95': shuf[int(0.95 * (len(shuf) - 1))], 'max': shuf[-1],
                              'ge_real': sum(s >= real['confirm_share'] for s in shuf)},
           'other_letter_c270': other,
           'fills': [{'line': r['line'], 'pos': r['pos'], 'sign': r['sign'], 'clear': r['clear']} for r in rows
                     if r['value'] is None],
           'contradictions': [{'line': r['line'], 'pos': r['pos'], 'sign': r['sign'], 'conf': r['conf'],
                               'table': r['value'], 'clear': r['clear']} for r in rows if r['kind'] == 'contradict']}
    res['real']['facing_unsure_clear'] = sum(r['unsure'] for r in rows)
    tsv = 'line\tpos\tsign\tconf\ttable\tclear\tkind\tclear_unsure\n' + ''.join(
        f"{r['line']}\t{r['pos']}\t{r['sign']}\t{r['conf']}\t{r['value'] or ''}\t{r['clear']}\t{r['kind']}\t{int(r['unsure'])}\n"
        for r in rows)
    # decode_key.py inputs (decode.json job c268): a vote is the clear letter a keyed token faces, only where that letter
    # comes from a word the reconciled clear reads without brackets; a fill is an unkeyed sign's chunk (FILLS below).
    votes = 'line\tpos\tvalue\n' + ''.join(f"{r['line']}\t{r['pos']}\t{r['clear']}\n" for r in rows
                                         if r['value'] is not None and len(r['clear']) == 1 and not r['unsure'])
    exc = 'line\tpos\tvalue\tgrade\tnote\n'
    for r in rows:
        if CLEAR == 'clear_f140.tsv' and r['value'] is None and (r['line'], r['pos']) in FILLS:
            v, g, note = FILLS[(r['line'], r['pos'])]
            assert r['clear'] == v.replace('NULL', '') or g == 'M', (r['line'], r['pos'], r['clear'], v)
            exc += f"{r['line']}\t{r['pos']}\t{v}\t{g}\t{note}\n"
    return tsv, json.dumps(res, indent=1, ensure_ascii=False) + '\n', votes, exc


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--draws', type=int, default=200)
    ap.add_argument('--seed', type=int, default=140)
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--clear', help='sensitivity run: another clear TSV (e.g. a single blind pass); prints, writes nothing')
    ap.add_argument('--no-fold-iy', action='store_true',
                    help='sensitivity run without the MONL-EYE y -> i fold (PREREG-MONL-IY.md); prints, writes nothing')
    a = ap.parse_args()
    global CLEAR, FOLD_IY
    if a.no_fold_iy:
        FOLD_IY = False
        print(run(a.draws, a.seed)[1]); return
    if a.clear:
        CLEAR = a.clear
        print(run(a.draws, a.seed)[1]); return
    outs = dict(zip(['align_c268.tsv', 'results_align_c268.json', 'votes_c268.tsv', 'exceptions_c268.tsv'], run(a.draws, a.seed)))
    if a.check:
        ok = all((HERE / f).exists() and (HERE / f).read_text(encoding='utf-8') == t for f, t in outs.items())
        print('align_c268: OK' if ok else 'align_c268: STALE'); sys.exit(0 if ok else 1)
    for f, t in outs.items():
        (HERE / f).write_text(t, encoding='utf-8')
    js = outs['results_align_c268.json']
    print(js)


if __name__ == '__main__':
    main()
