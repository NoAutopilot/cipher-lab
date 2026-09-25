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

print('decode_key:', 'all tests pass' if not fails else f'{fails} failures')
sys.exit(1 if fails else 0)
