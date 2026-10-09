#!/usr/bin/env python3
"""Offline tests for tools/decode_key.py special signs (MQS-SPECIAL-SIGNS, 9 Oct 2026): decode.json repeat_values /
delete_values and --special-scan (NULL / REPEAT-previous / DELETE-previous). No network.

  python3 tools/tests/test_decode_key_special.py                  offline tests (a fixture + one Danzay seed)
  python3 tools/tests/test_decode_key_special.py --controls [--seeds 10] [--out FILE]
        the controls of tools/tests/PREREG-MQS-SPECIAL-SIGNS.md (K1 synthetic fr18 repeats, K2 delete, K3 null,
        D1 decoy, D2 real codes, K4 Tomokiyo nulls; k=3 rows reported). Never writes into a target folder.
"""
import json, os, random, shutil, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import decode_key as dk

DANZAY_CFG = os.path.join(HERE, 'decode_configs', 'fr20140-danzay-1557.json')
fails = []


def check(ok, msg):
    print(('PASS ' if ok else 'FAIL ') + msg)
    if not ok:
        fails.append(msg)


def danzay():
    cfg = json.load(open(DANZAY_CFG, encoding='utf-8'))
    target = os.path.join(ROOT, cfg['target'])
    return target, [dict(cfg.get('defaults', {}), **j) for j in cfg['jobs']]


def danzay_key(target, jobs):
    key = {}
    for job in jobs:
        for c, r in dk.load_keys(target, job.get('key', 'key.tsv')).items():
            key.setdefault(c, r)
    return key


def plumbing():
    d = tempfile.mkdtemp()
    try:
        open(os.path.join(d, 'key.tsv'), 'w').write('code\tvalue\tgrade\nA\ta\t\nB\tb\t\nC\tc\tM\nR\tREP\t\nX\tDEL\t\n'
                                                    'N\tnull\t\n')
        rows = ['line\tpos\tsign\tconf', 'L1\t1\tA\tH', 'L1\t2\tC\tH', 'L1\t3\tR\tH', 'L1\t4\tN\tH', 'L1\t5\tR\tH',
                'L1\t6\tB\tH', 'L1\t7\tX\tH', 'L1\t8\tA\tH', 'L2\t1\tR\tH']
        open(os.path.join(d, 'ciphertext.tsv'), 'w').write('\n'.join(rows) + '\n')
        job = dict(format='tsv', style='concat', repeat_values=['REP'], delete_values=['DEL'])
        recs, _ = dk.graded_recs(d, job)
        s = [r for r in recs if r['kind'] == 'sign']
        txt = ''.join('' if r['null'] else r['value'] for r in s)
        check(txt == 'acccaa', f'repeat copies the previous value (nulls skipped, chains), delete cancels it: {txt!r}')
        check(s[2]['grade'] == 'M' and s[2]['special'] == 'repeat', 'a repeat takes the worse grade of the two (M)')
        check(s[5].get('special') == 'deleted' and s[6]['special'] == 'delete', 'deleted sign and delete sign marked')
        plain = dict(format='tsv', style='concat')
        recs2, _ = dk.graded_recs(d, plain)
        check([r['value'] for r in recs2 if r['kind'] == 'sign'][2] == 'REP' and
              not any(r.get('special') for r in recs2), 'must not change: no repeat/delete lists, key values as before')
    finally:
        shutil.rmtree(d)


def insert(S, entries, rnd):
    """Insert each entry (a list of tokens kept together) at a random slot of the streams; new streams."""
    T = [[list(e) for e in s] for s in S]
    for group in entries:
        slots = [(k, i) for k, s in enumerate(T) for i in range(1, len(s) + 1)]
        k, i = rnd.choice(slots)
        T[k][i:i] = [list(e) for e in group]
    return T


def fr18_spans(n_spans, length, seed):
    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    import french16_ngram
    text = ''.join(dk.lm_fold(w) for w in french16_ngram.corpus_words(os.path.join(ROOT, 'tools', 'data', 'fr18')))
    rnd = random.Random(seed)
    return [text[o:o + length] for o in (rnd.randrange(0, len(text) - length) for _ in range(n_spans))]


def k1_stream(span):
    s = []
    for i, ch in enumerate(span):
        s.append(['ZREP', None] if i and span[i - 1] == ch and s[-1][0] != 'ZREP' else [ch, ch])
    return [s]


def controls(seeds=10, out=None):
    model = dk.lm_load('fr16')
    target, jobs = danzay()
    key = danzay_key(target, jobs)
    base = dk.Crossword(target, jobs, model)
    rows = ['control\tseed\tk\tcode\tn\tbest\tsecond\tstat\tp95_reloc\tflag\tpass']

    def run(name, seed, k, cw, code, want, nulls=50):
        r = dk.special_scan_code(cw, code, model.alpha, nulls, seed)
        ok = (r['flag'] == want) if want else not r['flag']
        rows.append('\t'.join(map(str, [name, seed, k, code, r['n'], r['best'], r['second'], f"{r['stat']:.1f}",
                                        '' if r['p95'] is None else f"{r['p95']:.1f}", r['flag'], int(ok)])))
        print(rows[-1], flush=True)
        return ok

    res = {}
    letters = list(model.alpha)
    for sd, span in enumerate(fr18_spans(seeds, 638, 2026)):
        cw = dk.streams_from(model, k1_stream(span))
        res.setdefault('K1', []).append(run('K1', sd, cw.count['ZREP'], cw, 'ZREP', 'REPEAT'))
    for k in (6, 3):
        for sd in range(seeds):
            rnd = random.Random(1000 + sd)
            S = insert(base.S, [[['zz' + L, L], ['ZDEL', None]] for L in rnd.choices(letters, k=k)], rnd)
            res.setdefault(f'K2k{k}', []).append(run('K2', sd, k, dk.streams_from(model, S), 'ZDEL', 'DELETE'))
            rnd = random.Random(2000 + sd)
            S = insert(base.S, [[['ZNUL', None]] for _ in range(k)], rnd)
            res.setdefault(f'K3k{k}', []).append(run('K3', sd, k, dk.streams_from(model, S), 'ZNUL', 'NULL'))
    epos = [(a, i) for a, s in enumerate(base.S) for i, (t, v) in enumerate(s) if v == 'E']
    for sd in range(seeds):
        rnd = random.Random(3000 + sd)
        S = [[list(e) for e in s] for s in base.S]
        for a, i in rnd.sample(epos, 6):
            S[a][i][0] = 'ZLET'
        res.setdefault('D1', []).append(run('D1', sd, 6, dk.streams_from(model, S), 'ZLET', None))
    d2 = [c for c, n in base.count.most_common() if n >= 3 and key.get(c) and (key[c]['grade'] or 'H') == 'H'
          and '|' not in key[c]['value'] and key[c]['value'].upper() != 'NULL' and len(dk.lm_fold(key[c]['value'])) == 1]
    res['D2'] = [run('D2', 0, base.count[c], base, c, None) for c in d2]
    nulls = [c for c, r in key.items() if r['value'].upper() == 'NULL' and base.count[c]]
    cw4 = dk.Crossword(target, jobs, model)
    cw4.hide(nulls)
    res['K4'] = [run('K4', 0, base.count[c], cw4, c, 'NULL') for c in nulls]
    summ = []
    for name, v in res.items():
        summ.append(f'# {name}: {sum(v)}/{len(v)}')
    gate = dict(K1=sum(res['K1']) >= 8, K2=sum(res['K2k6']) >= 8, K3=sum(res['K3k6']) >= 8,
                D1=len(res['D1']) - sum(res['D1']) <= 1, D2=(len(res['D2']) - sum(res['D2'])) <= 0.10 * len(res['D2']))
    summ.append('# gates: ' + ', '.join(f'{g} {"PASS" if ok else "MISS"}' for g, ok in gate.items()))
    print('\n'.join(summ))
    if out:
        open(out, 'w', encoding='utf-8').write('\n'.join(summ + rows) + '\n')


def offline():
    plumbing()
    model = dk.lm_load('fr16')
    target, jobs = danzay()
    base = dk.Crossword(target, jobs, model)
    rnd = random.Random(1000)  # K2 seed 0 of the controls
    S = insert(base.S, [[['zz' + L, L], ['ZDEL', None]] for L in rnd.choices(list(model.alpha), k=6)], rnd)
    r = dk.special_scan_code(dk.streams_from(model, S), 'ZDEL', model.alpha, 20, 0)
    check(r['flag'] == 'DELETE', f"must catch: 6 wrong letters each followed by ZDEL flagged DELETE ({r['best']}, "
                                 f"{r['stat']:.1f} > p95 {r['p95']})")
    rnd = random.Random(2002)  # K3 seed 2: inserted nulls read NULL (the NULL op is shelf-weak: K3 6/10)
    S = insert(base.S, [[['ZNUL', None]] for _ in range(6)], rnd)
    r = dk.special_scan_code(dk.streams_from(model, S), 'ZNUL', model.alpha, 10, 0)
    check(r['best'] == 'NULL', f"6 inserted ZNUL tokens read best as NULL ({r['best']}, {r['stat']:.1f})")
    r = dk.special_scan_code(base, 'x', model.alpha, 10, 0)
    check(not r['flag'] and r['best'] == 'E', f"must not flag: Danzay code x (e, n {r['n']}) reads E, no flag")
    seq = [['a', 'A'], ['b', 'B'], ['q', None], ['c', 'C']]
    check(dk.render_special(seq, 'q', 'REPEAT') == 'ABBC' and dk.render_special(seq, 'q', 'DELETE') == 'AC'
          and dk.render_special(seq, 'q', 'NULL') == 'ABC', 'render_special: repeat, delete, null')


if __name__ == '__main__':
    if '--controls' in sys.argv:
        a = sys.argv
        controls(int(a[a.index('--seeds') + 1]) if '--seeds' in a else 10, a[a.index('--out') + 1] if '--out' in a else None)
        sys.exit(0)
    offline()
    print(f'decode_key special: {len(fails)} failures' if fails else 'decode_key special: all passed')
    sys.exit(1 if fails else 0)
