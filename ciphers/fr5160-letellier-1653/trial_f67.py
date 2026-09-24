#!/usr/bin/env python3
"""Canvas 129/130 (folio 67, Brienne to Servien, 10 Oct 1659): does key_1659 (recovered from f.86-88, 21 Nov
1659) read this letter too?

    python3 trial_f67.py            write trial_f67.tsv, print the table
    python3 trial_f67.py --check    exit 1 if the committed file differs from what this script writes

Input: passA_f67.tsv (blind pass A, NOTES.md 'Canvas 129/130 and canvas 32'), read in its own line order, which is
physical-row order for the whole letter (f129_L01..L16 = canvas 129's 16 lines, f130a_L01..07 = canvas 130's first
cipher block continuing the same run, f130b_L01..07 = canvas 130's second cipher block after the clear-French
aside). Bracketed clear-French tokens and scribal marks (comma, dash, period, semicolon, colon, the "X" correction
mark) are run breaks, not cipher.

Measure: mean log2 probability per character of the decoded text under tools/french16_ngram.py (order-5 period
French), over maximal runs of keyed signs of at least 2 characters (same measure as trial_1653.py). Control (rule
3): the key's 79 values permuted over its 79 codes, 20 derangements (no code keeps its value), seed 1659.
Coverage: share of cipher groups (tokens that are not clear French or a scribal mark) for which key_1659 has a code.
"""
import csv, io, os, random, statistics, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import french16_ngram as fr

NDER = 20
SEED = 1659
KEY_FN = os.path.join(HERE, 'key_1659.tsv')
PASS_FN = os.path.join(HERE, 'passA_f67.tsv')
MARKS = {',', '—', '.', ';', ':', 'X', '(4)', '_9', 'X{H::dot before it}'}  # scribal/correction marks kept as None (run breaks); '(4)' etc. not expected here


def load_key(fn):
    k = {}
    for r in csv.DictReader(open(fn, encoding='utf-8'), delimiter='\t'):
        v = r['value'].strip()
        v = '' if v == '0' else ''.join(ch for ch in fr.fold(v) if ch.isalpha())
        k[r['code'].strip()] = v
    return k


def load_stream(fn):
    """passA_f67.tsv -> list of str-or-None (None = clear French / scribal mark / run break)."""
    out = []
    for r in csv.DictReader(open(fn, encoding='utf-8'), delimiter='\t'):
        g = r['group'].strip()
        if not g or g.startswith('[') or g in (',', '—', '.', ';', ':', 'X', '?'):
            out.append(None)
        else:
            out.append(g)
    return out


def runs(values):
    out, cur = [], []
    for v in values:
        if v is None:
            if cur: out.append(''.join(cur))
            cur = []
        else:
            cur.append(v)
    if cur: out.append(''.join(cur))
    return [r for r in out if len(r) >= 2]


def score(values, m):
    rs = runs(values)
    n = sum(len(r) for r in rs)
    return (sum(m.logp(r) for r in rs) / n if n else float('nan')), n


def derangements(key, rng, n):
    codes = sorted(key)
    vals = [key[c] for c in codes]
    out = []
    while len(out) < n:
        p = vals[:]
        rng.shuffle(p)
        if all(a != b for a, b in zip(p, vals)):
            out.append(dict(zip(codes, p)))
    return out


def run_all():
    m = fr.load()
    key = load_key(KEY_FN)
    toks = load_stream(PASS_FN)
    nsig = sum(t is not None for t in toks)
    keyed = [t if (t is not None and t in key) else None for t in toks]
    ncov = sum(t is not None for t in keyed)
    rng = random.Random(SEED)
    ders = derangements(key, rng, NDER)
    real, nch = score([key[t] if t else None for t in keyed], m)
    ctrl_scores = [score([d[t] if t else None for t in keyed], m)[0] for d in ders]
    ctrl_mean = statistics.mean(ctrl_scores)
    ctrl_sd = statistics.pstdev(ctrl_scores)
    ctrl_max = max(ctrl_scores)
    z = (real - ctrl_mean) / ctrl_sd if ctrl_sd else float('nan')
    ge = sum(c >= real for c in ctrl_scores)
    rows = [['letter', 'cipher_tokens', 'keyed', 'coverage', 'chars_scored', 'real_bpc', 'shuffled_mean',
             'shuffled_sd', 'shuffled_max', 'shuffled_ge_real', 'z', 'n_derangements', 'beats_control'],
            ['f67', nsig, ncov, '%.3f' % (ncov / nsig if nsig else 0), nch, '%.3f' % real, '%.3f' % ctrl_mean,
             '%.3f' % ctrl_sd, '%.3f' % ctrl_max, ge, '%.2f' % z, NDER, 'yes' if real > ctrl_max else 'no']]
    return rows


def render():
    rows = run_all()
    b = io.StringIO()
    w = csv.writer(b, delimiter='\t', lineterminator='\n')
    w.writerows(rows)
    return b.getvalue()


def main():
    s = render()
    dst = os.path.join(HERE, 'trial_f67.tsv')
    if '--check' in sys.argv:
        if not os.path.exists(dst) or open(dst, encoding='utf-8').read() != s:
            print('stale: trial_f67.tsv'); sys.exit(1)
        print('ok: trial_f67.tsv'); return
    open(dst, 'w', encoding='utf-8').write(s)
    print(s)


if __name__ == '__main__':
    main()
