#!/usr/bin/env python3
"""Default-alphabet regression outputs for tools/tests/test_homophonic_alphabet.py (A2P4-KAL4, 3 Oct 2026).
Run from the repository root: python3 tools/tests/homophonic_alphabet_default_gen.py TOOLS_DIR. The fixture
tools/tests/fixtures/homophonic_alphabet_default.json is this script's output against the tools/ of commit 85a7db4e."""
import json, os, subprocess, sys, tempfile
T = os.path.abspath(sys.argv[1]); R = os.getcwd()
COR = os.path.join(R, 'tools', 'data', 'de16', 'composed_enhg.txt')
CT = os.path.join(R, 'ciphers', 'kaliningrad-2015', 'ciphertext_signs_B.tsv')
out = {}
with tempfile.TemporaryDirectory() as t:
    p = os.path.join(t, 'ctl.txt'); open(p, 'w').write(open(COR, encoding='utf-8').read()[5000:9000])
    o = os.path.join(t, 'o.json')
    subprocess.run([sys.executable, os.path.join(T, 'homophonic_anneal.py'), '--control', p, '--signs', '20', '--length', '200',
                    '--corpus', COR, '--restarts', '2', '--iters', '15000', '--seed', '3', '--out', o], check=True, stdout=subprocess.DEVNULL)
    out['cli_control'] = open(o, encoding='utf-8').read()
    subprocess.run([sys.executable, os.path.join(T, 'homophonic_anneal.py'), CT, '--corpus', COR, '--restarts', '1',
                    '--iters', '15000', '--seed', '5', '--out', o], check=True, stdout=subprocess.DEVNULL)
    out['cli_target'] = open(o, encoding='utf-8').read()
sys.path.insert(0, T)
import homophonic_anneal as ha  # noqa
from families import homophonic as fh  # noqa
txt = open(COR, encoding='utf-8').read()
msgs = [[l.rstrip('\n').split('\t')[1] for l in open(CT, encoding='utf-8')][1:301]]
params = {'N': 300, 'K': len(set(msgs[0])), 'target_msgs': msgs, 'profile': 'target', 'iters': '15000'}
cm, plain, train = fh.make_control({}, 2, [txt], dict(params))
dec, sc, info = fh.solve(cm, {}, 2, 1, train, dict(params))
out['family'] = json.dumps({'control': cm, 'plain': plain, 'decode': dec, 'score': round(sc, 6)}, sort_keys=True)
import judge_plaintext as jp  # noqa
spec = {'judge': {'corpora': [COR], 'control_samples': 50, 'letters_min': 50}}
r = jp.judge(spec, "Wir haben euch geschrieben dass der Kurfuerst mit seinem Volk gegen die Stadt zieht und bald da sein wird")
out['judge'] = json.dumps(r, sort_keys=True)
print(json.dumps(out, sort_keys=True, indent=1))
