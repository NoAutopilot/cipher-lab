#!/usr/bin/env python3
"""Offline test for tools/decode_key.py: regenerates the committed readings of three targets from their own
transcriptions and keys (configs in tools/tests/decode_configs/) and compares them byte for byte, without writing;
then checks that --check exits 1 on a stale reading (in a scratch copy). Run: python3 tools/tests/test_decode_key.py"""
import json, os, shutil, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import decode_key

CFG = os.path.join(ROOT, 'tools', 'tests', 'decode_configs')
fails = 0
for name in sorted(os.listdir(CFG)):
    cfg = json.load(open(os.path.join(CFG, name)))
    target = os.path.join(ROOT, cfg['target'])
    for job in cfg['jobs']:
        job = dict(cfg.get('defaults', {}), **job)
        outputs, cnt, ct = decode_key.run_job(target, job)
        for f, s in outputs.items():
            ok = open(os.path.join(target, f), encoding='utf-8').read() == s
            fails += not ok
            print(('PASS' if ok else 'FAIL'), cfg['target'], f)
# stale detection on a scratch copy
tmp = tempfile.mkdtemp()
try:
    src = os.path.join(ROOT, 'ciphers', 'fr20140-danzay-1557')
    for f in ('ciphertext.txt', 'ciphertext_f36.tsv', 'key.tsv', 'reading.txt', 'reading_tokens.tsv',
              'reading_f36.txt', 'reading_tokens_f36.tsv'):
        shutil.copy(os.path.join(src, f), tmp)
    conf = os.path.join(CFG, 'fr20140-danzay-1557.json')
    r0 = decode_key.main([tmp, '--config', conf, '--check'])
    open(os.path.join(tmp, 'reading.txt'), 'a').write('stale\n')
    r1 = decode_key.main([tmp, '--config', conf, '--check'])
    ok = r0 == 0 and r1 == 1
    fails += not ok
    print('PASS' if ok else 'FAIL', '--check exits 0 when current, 1 when stale')
finally:
    shutil.rmtree(tmp)
# load_keys: merging two key files (clair349-este-guise-1556's alphabet key + nomenclator key)
tmp2 = tempfile.mkdtemp()
try:
    open(os.path.join(tmp2, 'keyA.tsv'), 'w').write('code\tvalue\tgrade\nS01\ta\tH\n9\tc\tH\nS02\tf\tM\n')
    open(os.path.join(tmp2, 'keyB.tsv'), 'w').write('code\tvalue\tgrade\nS10\tword1\tM\n9\tword2\tM\n')
    merged = decode_key.load_keys(tmp2, ['keyA.tsv', 'keyB.tsv'])
    ok = (merged['S01']['value'] == 'a' and merged['S10']['value'] == 'word1'
          and merged['9']['value'] == 'c|word2' and merged['9']['grade'] == 'M')
    fails += not ok
    print('PASS' if ok else 'FAIL', 'load_keys merges two files, colliding code becomes a|b at grade M')
    single = decode_key.load_keys(tmp2, 'keyA.tsv')
    ok2 = single['S01']['value'] == 'a' and 'S10' not in single
    fails += not ok2
    print('PASS' if ok2 else 'FAIL', 'load_keys accepts a single filename (non-list) unchanged')

    # intra-file collision (clair349-este-guise-1556's key_alpha.tsv: C=9 and DOUBLES:ss=9 in one file)
    open(os.path.join(tmp2, 'keyC.tsv'), 'w').write('letter\tcode\tkind\tgrade\tcrop\tnote\n'
                                                     'C\t9\tdigit\tH\tx.jpg\tclear\n'
                                                     'DOUBLES:ss\t9\tdigit\tM\ty.jpg\tuncertain\n'
                                                     'A\t12\tdigit\tH\tx.jpg\tclear\n'
                                                     'L\t?\tunresolved\tM\tz.jpg\tnot safe to commit\n')
    kc = decode_key.load_key(os.path.join(tmp2, 'keyC.tsv'))
    ok3 = (kc['9']['value'] == 'C|DOUBLES:ss' and kc['9']['grade'] == 'M' and kc['12']['value'] == 'A'
          and '?' not in kc)
    fails += not ok3
    print('PASS' if ok3 else 'FAIL', 'load_key: value-first header (letter/code cols), '
                                     'intra-file code collision merges, unresolved "?" code skipped')
finally:
    shutil.rmtree(tmp2)

# --split-check (1 Oct 2026, espagnol142-mercy-1648: 65 52 48 72 against a key of 2-34 were two digits written
# together, and had been keyed as M rows, so the range comes from the confident rows only)
tmp3 = tempfile.mkdtemp()
try:
    import contextlib, io
    letters = 'abcdefghijklmnopqrstuvwxyzabcdefg'
    krows = ''.join(f'{c}\t{letters[c - 2]}\tS\n' for c in range(2, 35))
    open(os.path.join(tmp3, 'key.tsv'), 'w').write('code\tletter\tgrade\n' + krows + '48\td\tM\n[MARK:box]\t_\tM\n')
    toks = ['2', '48', '3', '99', '[MARK:box]', '1234', '48', 'X7']
    open(os.path.join(tmp3, 'ciphertext.tsv'), 'w').write(
        'line\tposition\tsign\tconfidence\n' + ''.join(f'r01\t{i}\t{t}\tH\n' for i, t in enumerate(toks, 1)))
    json.dump({'format': 'tsv'}, open(os.path.join(tmp3, 'decode.json'), 'w'))
    rows, meta = decode_key.split_check(tmp3, {'format': 'tsv'})
    by = {r['token']: r for r in rows}
    ok = (meta['range'] == (2, 34) and set(by) == {'48', '99', '1234', 'X7'}
          and by['48']['status'] == 'out-of-range' and by['48']['n'] == 2
          and by['48']['positions'] == ['r01:2', 'r01:7'] and by['48']['splits'] == ['4|8']
          and by['48']['decoded'] == ['c g']
          and by['99']['status'] == 'unkeyed,out-of-range' and by['99']['splits'] == ['9|9']
          and '12|34' in by['1234']['splits'] and '12|3|4' in by['1234']['splits']
          and '1|2|34' not in by['1234']['splits']          # '1' is not a key code
          and by['X7']['status'] == 'unkeyed' and by['X7']['splits'] == [])
    fails += not ok
    print('PASS' if ok else 'FAIL', 'split_check: out-of-range M row, unkeyed, 2- and 3-way splits, confident range')
    out = os.path.join(tmp3, 'split.tsv')
    with contextlib.redirect_stdout(io.StringIO()) as buf, contextlib.redirect_stderr(io.StringIO()):
        r0 = decode_key.main([tmp3, '--split-check', '--split-tsv', out])
        r2 = decode_key.main([os.path.join(tmp3, 'nope'), '--split-check'])
    lines = open(out).read().splitlines()
    ok = (r0 == 0 and r2 == 2 and lines[0].split('\t') == decode_key.SPLIT_TSV_COLUMNS and len(lines) == 5
          and 'split-check total: 4 flagged tokens' in buf.getvalue()
          and not os.path.exists(os.path.join(tmp3, 'reading.txt')))
    fails += not ok
    print('PASS' if ok else 'FAIL', '--split-check exits 0 with findings, 2 on an unloadable target, writes the TSV '
                                    'and no reading')
    # every fixture config still loads under --split-check (report only)
    for name in sorted(os.listdir(CFG)):
        cfg = json.load(open(os.path.join(CFG, name)))
        with contextlib.redirect_stdout(io.StringIO()):
            rc = decode_key.main([os.path.join(ROOT, cfg['target']), '--config', os.path.join(CFG, name),
                                  '--split-check'])
        fails += rc != 0
        print('PASS' if rc == 0 else 'FAIL', '--split-check loads', cfg['target'])
finally:
    shutil.rmtree(tmp3)

# '#' as a cipher sign (TOOL-DK-HASH, 3 Oct 2026): '#<TAB>a' is a key row, '# note' and '##' are comments
tmp4 = tempfile.mkdtemp()
try:
    open(os.path.join(tmp4, 'key.tsv'), 'w').write(
        '# sign\tvalue\n## a comment\n#\n# another comment\n#\ta\n#~\tb\n7\tc\n')
    open(os.path.join(tmp4, 'ciphertext.tsv'), 'w').write(
        'line\tposition\tsign\tconfidence\nr01\t1\t#\tH\nr01\t2\t#~\tH\nr01\t3\t7\tH\n')
    job = {'format': 'tsv'}
    outputs, cnt, ct = decode_key.run_job(tmp4, job)
    toks = outputs['reading_tokens.tsv']
    hdr, rows = decode_key.data_lines(os.path.join(tmp4, 'key.tsv'))
    ok = (hdr == ['sign', 'value'] and [r[0] for r in rows] == ['#', '#~', '7']
          and '\tU' not in toks and toks.count('\tH') >= 3
          and all(decode_key.is_comment(c) for c in ('#', '# x', '##', '#\n'))
          and not any(decode_key.is_comment(c) for c in ('#\ta', "#'\tl'Empereur", '#~\tb', 'a#')))
    fails += not ok
    print('PASS' if ok else 'FAIL', "'#' sign rows decode; '# ...', '##' and bare '#' lines stay comments")
finally:
    shutil.rmtree(tmp4)

# s_words (READ2-PAG, 3 Oct 2026): a key row whose note names a passed test grades S where its vote agrees or is
# absent, disagree_grade where it disagrees; checked before m_words (the same note may still say 'unsettled')
tmp5 = tempfile.mkdtemp()
try:
    open(os.path.join(tmp5, 'key.tsv'), 'w').write(
        'code\tvalue\tgrade\tsource\tnote\n146\tle\tS\tgloss\tunsettled; homophone pass S\n'
        '30\ta\tM\tgloss\tunsettled\n52\tet\tH\tgloss\t3/5 agree\n')
    open(os.path.join(tmp5, 'ciphertext.tsv'), 'w').write(
        'line\tposition\tsign\tconfidence\n' + ''.join(f'r01\t{i}\t{t}\tH\n' for i, t in
                                                     enumerate(['146', '146', '146', '30', '52'], 1)))
    open(os.path.join(tmp5, 'votes.tsv'), 'w').write(
        'line\tposition\tvalue\nr01\t1\tle\nr01\t2\tla\nr01\t4\ta\nr01\t5\tet\n')
    job = {'format': 'tsv', 'votes': {'file': 'votes.tsv', 'value_column': 'value'}, 'voted_grade': 'H',
           'disagree_grade': 'M', 'm_words': ['unsettled'], 's_words': ['homophone pass S']}
    outputs, cnt, ct = decode_key.run_job(tmp5, job)
    g = [l.split('\t')[-1] for l in outputs['reading_tokens.tsv'].splitlines() if l.startswith('r01')]
    ok = g == ['S', 'M', 'S', 'M', 'H']
    fails += not ok
    print('PASS' if ok else 'FAIL', 's_words: agreeing/absent vote S, disagreeing M, m_words and votes unchanged', g)
finally:
    shutil.rmtree(tmp5)

print('decode_key:', 'all tests pass' if not fails else f'{fails} failures')
sys.exit(1 if fails else 0)
