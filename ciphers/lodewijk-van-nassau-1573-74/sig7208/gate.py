#!/usr/bin/env python3
"""SIG-7208 transcription/table gate (PREREG.md section i), 9 Oct 2026.

Decode ciphertext_7208.tsv under key_full (codes 1-120 with a one-letter value; NULL dropped; codes > 120 and clear
words are carried as letters that are not scored), align the whole cipher stream (from the first numeral on) to the
period decipherment decipherment_7208.txt by Levenshtein edit operations (rapidfuzz), and report per page the share of
aligned scored tokens whose key_full letter equals the decipherment letter (gate >= 0.80 each page). Null: 200 draws
of key_full with the one-letter values permuted among codes 1-120 (same codes, same frequencies), aligned identically;
the target must also exceed the null p99 on each page.

    python3 sig7208/gate.py [--draws 200] [--seed 7208]     (needs: pip install rapidfuzz)
"""
import argparse, csv, os, random, re
from rapidfuzz.distance import Levenshtein

TOP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def letters(s):
    return re.sub(r'[^a-z]', '', s.lower().replace('&', 'et'))


def plain():
    t = ' '.join(l for l in open(os.path.join(TOP, 'decipherment_7208.txt'), encoding='utf-8') if not l.startswith('#'))
    t = re.sub(r'\[(\d+)\]', ' ', t).replace('[?]', '')
    return letters(t)


def tokens():
    rows = list(csv.DictReader(open(os.path.join(TOP, 'ciphertext_7208.tsv'), encoding='utf-8'), delimiter='\t'))
    first = next(i for i, r in enumerate(rows) if r['sign'].isdigit())
    return rows[first:]


def stream(rows, key):
    """chars and, per char, (page, scored) -- scored only for 1-120 codes with a one-letter key value"""
    chars, meta = [], []
    for r in rows:
        s, page = r['sign'], r['line'].split('_')[1]
        if s.startswith('='):
            for ch in letters(s[1:]):
                chars.append(ch); meta.append((page, False))
        elif s.isdigit():
            v = key.get(s)
            if v is None or v == 'NULL':
                continue
            sc = 1 <= int(s) <= 120 and len(v) == 1
            for ch in letters(v):
                chars.append(ch); meta.append((page, sc))
    return ''.join(chars), meta


def score(rows, key, P):
    a, meta = stream(rows, key)
    eq, al = {}, {}
    for op in Levenshtein.opcodes(a, P):
        if op.tag in ('equal', 'replace'):
            for k in range(op.src_start, op.src_end):
                pg, sc = meta[k]
                if sc:
                    al[pg] = al.get(pg, 0) + 1
                    if op.tag == 'equal':
                        eq[pg] = eq.get(pg, 0) + 1
    return {pg: (eq.get(pg, 0), al[pg]) for pg in al}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--draws', type=int, default=200)
    ap.add_argument('--seed', type=int, default=7208)
    a = ap.parse_args()
    key = {r['code']: r['value'] for r in csv.DictReader(open(os.path.join(TOP, 'key_full.tsv'), encoding='utf-8'), delimiter='\t')}
    rows, P = tokens(), plain()
    tgt = score(rows, key, P)
    one = [c for c, v in key.items() if c.isdigit() and 1 <= int(c) <= 120 and len(v) == 1 and v != 'NULL']
    rng = random.Random(a.seed)
    nulls = {pg: [] for pg in tgt}
    for _ in range(a.draws):
        vals = [key[c] for c in one]; rng.shuffle(vals)
        k2 = dict(key); k2.update(zip(one, vals))
        s = score(rows, k2, P)
        for pg in nulls:
            e, n = s.get(pg, (0, 1)); nulls[pg].append(e / n)
    ok_all = True
    print('page\tagree\taligned\tshare\tnull_mean\tnull_p99\tnull_max\tgate(>=0.80 and >p99)')
    for pg in sorted(tgt):
        e, n = tgt[pg]; sh = e / n
        ns = sorted(nulls[pg]); p99 = ns[int(0.99 * (len(ns) - 1))]
        ok = sh >= 0.80 and sh > p99; ok_all &= ok
        print('%s\t%d\t%d\t%.3f\t%.3f\t%.3f\t%.3f\t%s' % (pg, e, n, sh, sum(ns) / len(ns), p99, ns[-1], 'PASS' if ok else 'FAIL'))
    print('overall:', 'PASS' if ok_all else 'FAIL')


if __name__ == '__main__':
    main()
