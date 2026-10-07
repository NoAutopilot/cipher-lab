#!/usr/bin/env python3
"""NA-MONL test 1 (spec fr4735-monluc-lansac-poland-1573): known-answer score of Tomokiyo's Monluc Cipher 1 table
(key.tsv, transcribed from sources/cryptiana/web/henryiii_Monluc1.png) on the three cipher lines of c172 (f.86),
against the leaf's own contemporary marginal decipherment (gloss_c172.txt).

  python3 score_c172.py [--draws 200] [--seed 1] [--check]

Statistic: decode every transcribed token through key.tsv (a K-id -> one letter; '?' or an id not in the key -> no
letter), normalise both sides to one convention (lower case, letters only, j->i, v->u, y->i, accents dropped; rule 3
PX-BRODEC paragraph), then align the decoded string semi-globally against the gloss string (end gaps on the gloss
free; match +2, mismatch -1, gap -2, so cipher nulls can drop out) and report matched letters / decoded letters.
Matched control: the same tokens in shuffled order (pooled over the three lines), same key, same gloss, same
alignment, --draws draws; the shuffle changes which token meets which gloss letter, so the control can differ from
the target (rule 3 orthogonality paragraph). Writes results_c172.json; --check exits 1 if the committed file is stale.
"""
import argparse, json, random, sys, unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if 'a' <= c <= 'z')
    return s.translate(str.maketrans('jvy', 'iui'))


def load_key():
    key = {}
    for ln in (HERE / 'key.tsv').read_text().splitlines()[1:]:
        f = ln.split('\t')
        key[f[0]] = f[2]
    return key


def load_tokens(name='ciphertext.txt'):
    toks = []
    for ln in (HERE / name).read_text().splitlines():
        if not ln.strip() or ln.startswith('#') or not ln.startswith('L'):
            continue
        lab, rest = ln.split('\t', 1)
        toks.extend(t for t in rest.split() if t not in ('END_CUT', '-'))
    return toks


def decode(toks, key):
    out = []
    for t in toks:
        k = t.split('/')[0]
        out.append(key.get(k, ''))
    return norm(''.join(out))


def align(a, b, m=2, x=-1, g=-2):
    """semi-global: all of a aligned, free leading/trailing gaps in b; returns matched letters."""
    n, mm = len(a), len(b)
    prev = [(0, 0)] * (mm + 1)  # (score, matches)
    for i in range(1, n + 1):
        cur = [(prev[0][0] + g, prev[0][1])] + [None] * mm
        for j in range(1, mm + 1):
            s = m if a[i - 1] == b[j - 1] else x
            d = (prev[j - 1][0] + s, prev[j - 1][1] + (1 if a[i - 1] == b[j - 1] else 0))
            u = (prev[j][0] + g, prev[j][1])
            l = (cur[j - 1][0] + g, cur[j - 1][1])
            cur[j] = max(d, u, l)
        prev = cur
    return max(prev)[1]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--draws', type=int, default=200)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--cipher', default='ciphertext.txt', help='token file (wide: label<TAB>tokens)')
    ap.add_argument('--gloss', default='gloss_c172.txt')
    ap.add_argument('--out', default='results_c172.json')
    a = ap.parse_args()
    key = load_key()
    toks = load_tokens(a.cipher)
    gloss = norm((HERE / a.gloss).read_text().split('\n#', 1)[0])
    dec = decode(toks, key)
    tgt = align(dec, gloss)
    rng = random.Random(a.seed)
    ctl = []
    for _ in range(a.draws):
        t = toks[:]
        rng.shuffle(t)
        ctl.append(align(decode(t, key), gloss) / max(1, len(dec)))
    ctl.sort()
    res = dict(tokens=len(toks), decoded_letters=len(dec), gloss_letters=len(gloss), decoded=dec, gloss=gloss,
               target_matched=tgt, target_rate=round(tgt / max(1, len(dec)), 4),
               control_mean=round(sum(ctl) / len(ctl), 4), control_p95=round(ctl[int(0.95 * len(ctl)) - 1], 4),
               control_max=round(ctl[-1], 4), draws=a.draws, seed=a.seed,
               rank_p=round(sum(1 for c in ctl if c >= tgt / max(1, len(dec))) / len(ctl), 4))
    out = HERE / a.out
    txt = json.dumps(res, indent=1) + '\n'
    if a.check:
        if not out.exists() or out.read_text() != txt:
            print('STALE results_c172.json')
            sys.exit(1)
        print('OK results_c172.json current')
        return
    out.write_text(txt)
    print(txt)


if __name__ == '__main__':
    main()
