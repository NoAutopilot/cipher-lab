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
print('decode_key:', 'all tests pass' if not fails else f'{fails} failures')
sys.exit(1 if fails else 0)
