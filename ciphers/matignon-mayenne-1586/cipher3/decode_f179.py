#!/usr/bin/env python3
"""decode_f179.py -- Matignon Cipher-3, BnF fr.15571 f.179 (MAT-F179, 9 Oct 2026).

Applies Tomokiyo's published Cipher-3 table (code_key.tsv: blind random codes -> his column letter or word) to the
reconciled transcription (f179_reconciled.tsv) and scores the reading under the fr16 character model against a
shuffled-key control (the code->value map permuted N times, same transcription). Key source: published (Tomokiyo).
  python3 decode_f179.py            write f179_reading.txt and print the scores
  python3 decode_f179.py --check    exit 1 if the committed reading is stale (rule 7)
  python3 decode_f179.py --tx passA_f179.tsv --no-write    the MAT-F179 control numbers (no reading committed: FAIL)
"""
import argparse, os, random, sys, statistics
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import french16_ngram as F

def load_key():
    k = {}
    for ln in open(os.path.join(HERE, 'code_key.tsv'), encoding='utf-8').read().splitlines()[1:]:
        c, v = ln.split('\t')[:2]
        k[c] = v.split('(')[0]
    return k

def load_tx(name='f179_reconciled.tsv'):
    rows = []
    for ln in open(os.path.join(HERE, name), encoding='utf-8').read().splitlines():
        if not ln.startswith('L'):
            continue
        p = ln.split('\t')
        rows.append((p[0], p[1].split()))
    return rows

def decode(rows, key):
    out = []
    for lab, toks in rows:
        out.append((lab, ''.join(key.get(t, '_') if t.startswith('K') else '_' for t in toks)))
    return out

def score(model, lines):
    segs = [F.fold(s) for _, l in lines for s in l.split("_") if s]
    n = sum(len(s) for s in segs)
    return sum(model.logp(s) for s in segs) / max(n, 1), n

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--check', action='store_true')
    ap.add_argument('--draws', type=int, default=200)
    ap.add_argument('--tx', default='f179_reconciled.tsv', help='transcription TSV in this folder (passA_f179.tsv, passB_f179.tsv reproduce the MAT-F179 numbers with --no-write)')
    ap.add_argument('--no-write', action='store_true'); a = ap.parse_args()
    key, rows = load_key(), load_tx(a.tx)
    lines = decode(rows, key)
    text = ''.join(f'{lab}\t{l}\n' for lab, l in lines)
    path = os.path.join(HERE, 'f179_reading.txt')
    if a.check:
        old = open(path, encoding='utf-8').read() if os.path.exists(path) else ''
        if old != text:
            print('STALE: f179_reading.txt differs from a fresh decode'); sys.exit(1)
        print('OK: f179_reading.txt matches'); return
    if not a.no_write:
        open(path, 'w', encoding='utf-8').write(text)
    m = F.load()
    real, n = score(m, lines)
    rnd = random.Random(17926); codes = sorted(key); vals = [key[c] for c in codes]; null = []
    for _ in range(a.draws):
        v = vals[:]; rnd.shuffle(v); null.append(score(m, decode(rows, dict(zip(codes, v))))[0])
    null.sort()
    toks = sum(len(t) for _, t in rows); keyed = sum(1 for _, t in rows for x in t if x in key)
    print(f'tokens {toks}, keyed {keyed} ({keyed/toks:.1%}), letters scored {n}')
    print(f'fr16 log2/char: real {real:.3f}; shuffled-key null (n={a.draws}) mean {statistics.mean(null):.3f}, '
          f'p95 {null[int(0.95*len(null))-1]:.3f}, max {null[-1]:.3f}')
    print('PASS (real above null max)' if real > null[-1] else 'FAIL (real not above null max)')

if __name__ == '__main__':
    main()
