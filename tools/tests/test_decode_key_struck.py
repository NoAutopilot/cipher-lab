#!/usr/bin/env python3
"""Offline tests for tools/decode_key.py corrections on the page (MQS-STRUCK, 9 Oct 2026): 'X{struck}', '{over=OLD>NEW}',
the tsv `state` column and decode.json/--corrections final|original. No network.

  python3 tools/tests/test_decode_key_struck.py              offline tests + control K1 / null N1 (10 seeds)
  python3 tools/tests/test_decode_key_struck.py --controls   print only the per-seed control table
Never writes into a target folder (temporary directories only). Prereg: tools/tests/PREREG-MQS-STRUCK.md.
"""
import os, random, shutil, string, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE)))
import decode_key as dk

fails = []
TEXT = ("monsieur jay receu vostre lettre du douziesme de ce mois par laquelle vous me mandez que le roy est en bonne "
        "disposition et que les affaires de flandres se portent mieux que lon ne pensoit ie vous prie de continuer a me "
        "faire scavoir tout ce qui se passera de dela et principalement ce que vous apprendrez des desseins de lennemy "
        "sur les places de la frontiere car il importe grandement au service du roy que nous en soyons advertis de bonne "
        "heure afin dy pourvoir comme il appartient ie suis bien ayse dentendre que monsieur le mareschal a este si bien "
        "receu en ceste court et que la royne luy a faict tant de demonstrations damitie vous luy direz de ma part que ie")
PLAIN = [c for c in TEXT if c.isalpha()][:600]


def check(ok, msg):
    print(('PASS ' if ok else 'FAIL ') + msg)
    if not ok:
        fails.append(msg)


def decode(rows, job, keyrows):
    d = tempfile.mkdtemp()
    try:
        open(os.path.join(d, 'key.tsv'), 'w').write('code\tvalue\n' + ''.join(f'{c}\t{v}\n' for c, v in keyrows))
        open(os.path.join(d, 'ciphertext.tsv'), 'w').write('\n'.join(rows) + '\n')
        recs, _ = dk.graded_recs(d, dict(dict(format='tsv'), **job))
        outs, _, _ = dk.run_job(d, dict(dict(format='tsv', style='concat'), **job))
        return recs, outs
    finally:
        shutil.rmtree(d)


def plumbing():
    key = [('A', 'a'), ('B', 'b'), ('C', 'c'), ('D', 'd')]
    rows = ['line\tpos\tsign\tconf', 'L1\t1\tA\t', 'L1\t2\tB{struck}\t', 'L1\t3\t{over=D>C}\t', 'L1\t4\tA>B\t',
            'L1\t5\t{x}\t']
    recs, outs = decode(rows, {}, key)
    s = [r for r in recs if r['kind'] in ('sign', 'struck')]
    check([r['kind'] for r in s] == ['sign', 'struck', 'sign', 'sign', 'sign'], 'struck sign is kind struck, index kept')
    check(s[2]['value'] == 'c' and s[2]['state'] == 'over=D>C', 'final: overwrite reads NEW, state kept')
    check(s[3]['sign'] == 'A>B' and s[4]['sign'] == '{x}' and 'state' not in s[3], "must-not: 'A>B' and '{x}' stay signs")
    rd = outs['reading.txt']
    body = rd.split('|', 1)[-1]
    check('b' not in body and 'ac' in body, 'final: reading skips the struck b')
    check('\tB\t' not in outs['reading_tokens.tsv'] and 'struck' not in outs['reading_tokens.tsv'],
          'final: struck sign not in the token file')
    recs, outs = decode(rows, dict(corrections='original'), key)
    s = [r for r in recs if r['kind'] in ('sign', 'struck')]
    check([r['value'] for r in s][:3] == ['a', 'b', 'd'], 'original: struck read as written, overwrite read as OLD')
    rows2 = ['line\tpos\tsign\tstate', 'L1\t1\tA\t', 'L1\t2\tB\tstruck', 'L1\t3\tD\tover=D>C', 'L1\t4\tC\tweird']
    recs, _ = decode(rows2, {}, key)
    s = [r for r in recs if r['kind'] in ('sign', 'struck')]
    check([(r['kind'], r.get('value')) for r in s] == [('sign', 'a'), ('struck', None), ('sign', 'c'), ('sign', 'c')],
          'state column: struck / over=OLD>NEW applied, unknown state ignored')
    try:
        decode(rows, dict(corrections='bogus'), key); check(False, 'bad corrections value refused')
    except ValueError:
        check(True, 'bad corrections value refused')


def control(seed, n_struck=12, n_over=12):
    rnd = random.Random(seed)
    letters = sorted(set(PLAIN))
    codes = rnd.sample(range(10, 99), len(letters))
    enc = {l: str(c) for l, c in zip(letters, codes)}
    key = [(v, k) for k, v in enc.items()]
    toks = [enc[c] for c in PLAIN]
    wrong = lambda true: rnd.choice([v for v in enc.values() if v != true])
    over_at = set(rnd.sample(range(len(toks)), n_over))
    toks = [f'{{over={wrong(t)}>{t}}}' if i in over_at else t for i, t in enumerate(toks)]
    for _ in range(n_struck):
        i = rnd.randrange(len(toks) + 1)
        toks.insert(i, wrong(toks[i] if i < len(toks) and not toks[i].startswith('{') else '') + '{struck}')
    rows = ['line\tpos\tsign'] + [f'L1\t{i}\t{t}' for i, t in enumerate(toks, 1)]
    out = {}
    for mode in ('final', 'original'):
        recs, _ = decode(rows, dict(corrections=mode), key)
        got = [r['value'] for r in recs if r['kind'] == 'sign']
        n = max(len(got), len(PLAIN))
        out[mode] = sum(a == b for a, b in zip(got, PLAIN)) / n
    return out


def controls(seeds=10):
    print('seed\tK1_final\tN1_original')
    rows = [control(s) for s in range(seeds)]
    for s, r in enumerate(rows):
        print(f"{s}\t{r['final']:.3f}\t{r['original']:.3f}")
    k = sum(r['final'] == 1.0 for r in rows); nl = sum(r['original'] < 0.99 for r in rows)
    print(f'K1 1.000 on {k}/{seeds} (gate {seeds}/{seeds}); N1 < 0.99 on {nl}/{seeds} (gate {seeds}/{seeds})')
    return k == seeds and nl == seeds


if __name__ == '__main__':
    if '--controls' in sys.argv:
        sys.exit(0 if controls() else 1)
    plumbing()
    check(controls(), 'control K1 / null N1 meet the prereg gates')
    print('decode_key struck: ' + (f'{len(fails)} failures' if fails else 'all passed'))
    sys.exit(1 if fails else 0)
