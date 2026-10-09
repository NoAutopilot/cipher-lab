#!/usr/bin/env python3
"""Offline tests for tools/decode_key.py --try / --avalanche (MQS-CROSSWORD, 9 Oct 2026). No network.

  python3 tools/tests/test_decode_key_try.py               the offline tests (Danzay config + a planted fixture)
  python3 tools/tests/test_decode_key_try.py --controls K1b [--out FILE]   known-answer controls of
        tools/tests/PREREG-MQS-CROSSWORD.md: K1a DIR (Gramont as committed in e8567d0a8, copied to DIR), K1b (current
        Gramont vs infer_unkeyed.py, row identity), K2 (Blathwayt words, fr18), K3 (Danzay letters, fr16).
        Slow (minutes); writes only --out (default: print). Never writes into a target folder.
"""
import hashlib, importlib.util, json, os, random, shutil, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import decode_key as dk

DANZAY_CFG = os.path.join(HERE, 'decode_configs', 'fr20140-danzay-1557.json')
GRAMONT_JOBS = [dict(ciphertext='ciphertext.txt', format='pipe', uncertain_conf=['?']),
                dict(ciphertext='ciphertext_f30.tsv', format='tsv', split_line='_', uncertain_conf=['l'])]
fails = []


def check(ok, msg):
    print(('PASS ' if ok else 'FAIL ') + msg)
    if not ok:
        fails.append(msg)


def danzay():
    cfg = json.load(open(DANZAY_CFG, encoding='utf-8'))
    target = os.path.join(ROOT, cfg['target'])
    jobs = [dict(cfg.get('defaults', {}), **j) for j in cfg['jobs']]
    return target, jobs


def letter_codes(cw, key, nmin):
    """H-graded codes whose value is one letter, with n >= nmin, commonest first."""
    out = []
    for c, n in cw.count.most_common():
        r = key.get(c)
        if r and n >= nmin and (r['grade'] or 'H') == 'H' and len(dk.lm_fold(r['value'])) == 1 \
                and '|' not in r['value'] and r['value'].upper() != 'NULL':
            out.append(c)
    return out


def merged_key(target, jobs):
    key = {}
    for job in jobs:
        for c, r in dk.load_keys(target, job.get('key', 'key.tsv')).items():
            key.setdefault(c, r)
    return key


def offline():
    model = dk.lm_load('fr16')
    target, jobs = danzay()
    key = merged_key(target, jobs)
    kpath = os.path.join(target, 'key.tsv')
    h0 = hashlib.sha256(open(kpath, 'rb').read()).hexdigest()
    cw = dk.Crossword(target, jobs, model)
    codes = letter_codes(cw, key, 5)
    code = codes[0]
    true = key[code]['value']
    rnd = random.Random(0)
    wrong = rnd.sample([a for a in model.alpha if a != dk.lm_fold(true)], 9)
    cw.hide([code])
    r = cw.ranked(code, [true] + wrong)
    check(dk.lm_fold(r[0][1]) == dk.lm_fold(true),
          f'hidden H code {code} (n {cw.count[code]}): true value {true} ranks above 9 wrong letters ({r[0][1]} first)')
    # must catch: a wrong value for a frequent keyed code is rejected
    cw = dk.Crossword(target, jobs, model)
    cands = list(model.alpha) + ['NULL']
    bad = dk.try_value(cw, code, wrong[0], cands, nulls=20)
    check(bad['verdict'] == 'reject', f'wrong value {code}={wrong[0]}: reject ({bad["verdict"]}, {bad["stat"]:.1f} bits)')
    # must not block: the current value returns a zero statistic, not an error
    same = dk.try_value(cw, code, true, cands, nulls=20)
    check(same['stat'] == 0.0 and same['verdict'] == 'undecided', f'{code}={true} (current): zero statistic, undecided')
    # must not flag: a true value tried on the hidden code (no current value) is not rejected
    cw.hide([code])
    good = dk.try_value(cw, code, true, cands, nulls=20)
    check(good['verdict'] != 'reject', f'true value on hidden {code}: not rejected ({good["verdict"]}, '
                                       f'{good["stat"]:.1f} bits over {good.get("ref")})')
    # n = 1 is undecided, never rejected
    cw = dk.Crossword(target, jobs, model)
    one = next(c for c, n in cw.count.items() if n == 1 and c in key and dk.lm_fold(key[c]['value']))
    r1 = dk.try_value(cw, one, 'Q' if dk.lm_fold(key[one]['value']) != 'Q' else 'X', cands, nulls=10)
    check(r1['verdict'] == 'undecided', f'n = 1 ({one}): undecided ({r1["why"]})')
    # the CLI leaves key.tsv unchanged (hypotheses in memory only)
    with tempfile.TemporaryDirectory() as td:
        log = os.path.join(td, 'log.tsv')
        rc = dk.main([target, '--config', DANZAY_CFG, '--try', f'{code}={wrong[0]},{codes[1]}={key[codes[1]]["value"]}',
                      '--nulls', '5', '--try-log', log])
        rows = open(log, encoding='utf-8').read().splitlines()
    check(rc == 0 and len(rows) == 3 and rows[1].endswith('non-blind'), '--try CLI: exit 0, two log rows flagged non-blind')
    check(hashlib.sha256(open(kpath, 'rb').read()).hexdigest() == h0, 'key.tsv hash unchanged after --try')
    # french16_ngram.load(corpus_dir=...): every *.txt / *.txt.gz in the folder, cached outside the repository
    import french16_ngram
    with tempfile.TemporaryDirectory() as td:
        open(os.path.join(td, 'a.txt'), 'w').write('Je vous prie de croire que je suis votre serviteur. ' * 50)
        os.environ['CIPHERLAB_LM_CACHE'] = os.path.join(td, 'cache')
        m2 = french16_ngram.load(corpus_dir=td)
        cached = os.listdir(os.path.join(td, 'cache'))
    check('V' in m2.alpha and 'J' not in m2.alpha and len(cached) == 1 and
          french16_ngram.cache_path() == os.path.join(ROOT, 'tools', 'data', 'fr16', 'model_o5.pkl.gz'),
          'corpus_dir model: same folding (J->I, U->V), one cache file outside the repo; fr16 cache path unchanged')
    # a planted blank: --avalanche proposes the planted value first
    text = ('MONSIEVRIAYRECEVLAVOSTRELETTREDVQVINZIESMEDESTEMOIStPARLAQVELLEIAYENTENDVCEQVIESTADVENVAVOSTRE'
            'FRONTIEREETDELAVOLONTEDEVOSTREMAIESTEPOVRLEBIENDESESAFFAIRESIEVOVSPRIEDECROIREQVEIESVISTOVSIOVRS'
            'VOSTRETRESHVMBLESERVITEVRETQVEIEFERAYCEQVILVOVSPLAIRADEMECOMMANDER').upper()
    with tempfile.TemporaryDirectory() as td:
        toks = [f'c{ch}' for ch in dk.lm_fold(text)]
        with open(os.path.join(td, 'ciphertext.tsv'), 'w') as f:
            f.write('line\tpos\tsign\tconf\n' + ''.join(f'L{i // 40:02d}\t{i % 40}\t{t}\tH\n' for i, t in enumerate(toks)))
        with open(os.path.join(td, 'key.tsv'), 'w') as f:
            f.write('code\tvalue\tgrade\n' + ''.join(f'c{ch}\t{ch}\tH\n' for ch in sorted(set(dk.lm_fold(text))) if ch != 'R'))
        out = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'decode_key.py'), td, '--avalanche'],
                             capture_output=True, text=True)
        first = [l.split('\t') for l in out.stdout.splitlines() if l and not l.startswith(('#', 'order'))]
    check(bool(first) and first[0][1:3] == ['cR', 'R'], f'planted blank cR: avalanche proposes R first ({first[:1]})')


# ---------------------------------------------------------------- known-answer controls (PREREG-MQS-CROSSWORD.md)

SMALL_WORDS = ['ET', 'COM', 'SS', 'LL']
DOUBTFUL = {'Tb', 'eh', 'H', 'q'}


def gramont_draws(cw, key, draws):
    """infer_unkeyed.matched_draw, reimplemented on the Crossword's counts (same order, same seeds)."""
    keyval = lambda s: (key[s]['value'] if s in key and key[s]['value'] not in ('', '?') else None)
    unkeyed = [s for s, n in cw.count.most_common() if keyval(s) is None and n >= 2 and s != '[?]']
    out = []
    for d in draws:
        rnd = random.Random(1000 + d)
        pool = [s for s in cw.count if keyval(s) and (key[s]['grade'] or '') == 'H' and s != '[?]' and s not in DOUBTFUL]
        pick = []
        for u in unkeyed:
            cand = sorted((s for s in pool if s not in pick),
                          key=lambda s: (abs(cw.count[s] - cw.count[u]), rnd.random()))[:5]
            pick.append(rnd.choice(cand))
        out.append(pick)
    return out


def k1(target, draws=range(10)):
    import copy
    model = dk.lm_load('fr16')
    base = dk.Crossword(target, GRAMONT_JOBS, model)
    key = merged_key(target, GRAMONT_JOBS)
    rows = ['draw\tsign\tcount\ttrue\tproposed\tmargin\tsecond\tcorrect']
    for d, hid in zip(draws, gramont_draws(base, key, draws)):
        cw = copy.copy(base); cw.S = [[list(e) for e in s] for s in base.S]
        cw.hide(hid)
        for s, v, m, sec, n in dk.avalanche(cw, hid, list(model.alpha) + ['NULL'] + SMALL_WORDS):
            rows.append(f"{d}\t{s}\t{n}\t{key[s]['value']}\t{v}\t{m:.1f}\t{sec}\t{int(v == key[s]['value'])}")
        print(f'draw {d}', flush=True)
    return rows


def k1_summary(rows):
    r = [x.split('\t') for x in rows[1:]]
    acc = [x for x in r if x[4] != 'NULL' and int(x[2]) >= 5 and float(x[5]) >= 10 and int(x[0]) >= 5]
    return (f"proposals right {sum(int(x[7]) for x in r)}/{len(r)}; accepted right on draws 5-9 "
            f"{sum(int(x[7]) for x in acc)}/{len(acc)}")


TITLES = {'ROY', 'REINE', 'EMPEREVR', 'PRINCESSE', 'FRANCE', 'COVR'}


def leave_one_out(target, jobs, lm, codes_of, distractors_of, label):
    """Hide each code in turn (others keep their values); rank its candidates; per distinct code."""
    model = dk.lm_load(lm)
    base = dk.Crossword(target, jobs, model)
    key = merged_key(target, jobs)
    rows = ['class\tcode\tn\ttrue\ttop\tmargin\tsecond\trank1\tfalse_accept\tunigram_top\tunigram_rank1']
    uni = model.words
    for cls, c in codes_of(base, key):
        true = key[c]['value']
        cands = distractors_of(base, key, c, true)
        cw = base; saved = [(k, i, list(cw.S[k][i])) for k, i in cw.occ(c)]; cur = cw.cur
        cw.hide([c])
        r = cw.ranked(c, cands)
        for k, i, e in saved:
            cw.S[k][i] = e
        cw.cur = cur
        top, m, sec = r[0][1], r[0][0] - r[1][0], r[1][1]
        ok = dk.lm_fold(top) == dk.lm_fold(true)
        n = cw.count[c]
        fa = (not ok) and dk.accepted(top, n, m, dict(margin=10.0, n=5, null=False))
        ut = max(cands, key=lambda v: (unigram(model, v), -cands.index(v)))
        rows.append(f'{cls}\t{c}\t{n}\t{true}\t{top}\t{m:.1f}\t{sec}\t{int(ok)}\t{int(fa)}\t{ut}\t'
                    f'{int(dk.lm_fold(ut) == dk.lm_fold(true))}')
    return rows


_UNI = {}


def unigram(model, v):
    """Unigram-only score: a word's corpus count; a letter's corpus frequency (NULL scores 0)."""
    f = dk.lm_fold(v) if v.upper() != 'NULL' else ''
    if not f:
        return -1
    if len(f) == 1:
        if id(model) not in _UNI:
            cnt = __import__('collections').Counter()
            for w, n in model.words.items():
                for ch in w:
                    cnt[ch] += n
            _UNI[id(model)] = cnt
        return _UNI[id(model)][f]
    return model.words.get(f, 0)


def k2():
    target = os.path.join(ROOT, 'ciphers', 'huntington-blathwayt-madrid-1728')
    jobs = [dict(ciphertext='ciphertext.tsv', key='key.tsv', format='tsv', unknown_values=[], unkeyed_value='?',
                 uncertain_conf=['M'])]

    def codes_of(cw, key):
        out = []
        for c, n in sorted(cw.count.items()):
            r = key.get(c)
            if not r or n < 3 or '|' in r['value'] or len(dk.lm_fold(r['value'])) < 2:
                continue
            cls = 'title' if dk.lm_fold(r['value']) in TITLES or r['value'][:1].isupper() else 'word'
            out.append((cls, c))
        return out

    def distractors_of(cw, key, c, true):
        ft = dk.lm_fold(true)
        band = 1 if len(ft) < 6 else 2
        pool, seen = [], {ft}
        for r in sorted({r['value'] for r in key.values() if '|' not in r['value']}):
            f = dk.lm_fold(r)
            if len(f) >= 2 and f not in seen and abs(len(f) - len(ft)) <= band:
                seen.add(f); pool.append(r)
        rnd = random.Random(f'{c}')
        return [true] + rnd.sample(pool, min(9, len(pool)))

    return leave_one_out(target, jobs, 'fr18', codes_of, distractors_of, 'K2')


def k3():
    target, jobs = danzay()

    def codes_of(cw, key):
        return [('letter', c) for c in letter_codes(cw, key, 5)]

    def distractors_of(cw, key, c, true):
        return [true] + [a for a in cw.M.alpha if a != dk.lm_fold(true)] + ['NULL']

    return leave_one_out(target, jobs, 'fr16', codes_of, distractors_of, 'K3')


def loo_summary(rows):
    r = [x.split('\t') for x in rows[1:]]
    out = []
    for cls in sorted({x[0] for x in r}):
        x = [y for y in r if y[0] == cls]
        n5 = [y for y in x if int(y[2]) >= 5]
        out.append(f"{cls}: rank-first {sum(int(y[7]) for y in x)}/{len(x)}; unigram baseline "
                   f"{sum(int(y[10]) for y in x)}/{len(x)}; false accept (n >= 5) "
                   f"{sum(int(y[8]) for y in n5)}/{len(n5)}")
    return out


if __name__ == '__main__':
    if '--controls' in sys.argv:
        which = sys.argv[sys.argv.index('--controls') + 1]
        out = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else None
        if which == 'K1a':
            rows = k1(sys.argv[sys.argv.index('K1a') + 1]); summ = [k1_summary(rows)]
        elif which == 'K1b':
            rows = k1(os.path.join(ROOT, 'ciphers', 'fr2980-gramont')); summ = [k1_summary(rows)]
        elif which == 'K2':
            rows = k2(); summ = loo_summary(rows)
        else:
            rows = k3(); summ = loo_summary(rows)
        if out:
            open(out, 'w').write('\n'.join(rows) + '\n')
        print('\n'.join(summ))
        sys.exit(0)
    offline()
    print(f'decode_key --try: {len(fails)} failures' if fails else 'decode_key --try: all passed')
    sys.exit(1 if fails else 0)
