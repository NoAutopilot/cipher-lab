#!/usr/bin/env python3
"""Offline tests for tools/key_design.py --compare (MQS-KEY-COMPARE, 9 Oct 2026; Lasry, Biermann and Tomokiyo 2023,
Cryptologia 47:2, pp.128-130). Catches: two keys sharing nomenclature vocabulary and design under different sign labels.
Must NOT flag: disjoint vocabulary and a different design (S < 0.5); two empty vocabularies never give V = 1.
Synthetic tables only; no network, no file under ciphers/ is read."""
import subprocess
import sys
import tempfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))
import key_design as kd  # noqa: E402

fails = 0


def check(name, cond):
    global fails
    print(('PASS ' if cond else 'FAIL ') + name)
    fails += not cond


LET = 'abcdefghilmnopqrstuz'
a = {f'G{i}': l for i, l in enumerate(LET * 2)}
a.update({'W1': 'carmagnola', 'W2': 'quello', 'W3': 'per', 'W4': 'che', 'W5': 'turino'})
# sibling: other labels, one homophone fewer per few letters, same vocabulary minus one plus one
b = {f'T{i}': l for i, l in enumerate(LET * 2) if i % 7}
b.update({'T90': 'carmagnola', 'T91': 'quello', 'T92': 'per', 'T93': 'che', 'T94': 'catholici'})
# stranger: numeric labels, one code per letter, a different vocabulary, many nulls
c = {str(10 + i): l for i, l in enumerate('abcdefghilmnopqrstuxyz')}
c.update({str(40 + i): w for i, w in enumerate(['roy', 'reyne', 'pape', 'espagne', 'madame', 'monsieur'])})
c.update({str(60 + i): 'null' for i in range(10)})

r = kd.compare_keys(a, a)
check(f'identity S = 1.000 ({r["S"]:.3f})', abs(r['S'] - 1) < 1e-9)
sib = kd.compare_keys(a, b)
check(f'sibling under different labels scores high (S {sib["S"]:.3f}, V {sib["V"]:.3f})', sib['S'] > 0.75 and sib['V'] > 0.5)
check('sibling: no shared labels, so no code agreement figure', sib['code_agree'] is None and sib['shared_codes'] == 0)
st = kd.compare_keys(a, c)
check(f'must NOT flag: disjoint vocabulary and different design (S {st["S"]:.3f} < 0.5)', st['S'] < 0.5 and st['V'] == 0)
check('sibling ranks above stranger', sib['S'] > st['S'])
e1 = {str(i): l for i, l in enumerate(LET)}
e2 = {str(i + 50): l for i, l in enumerate(LET[::-1])}
check('two empty vocabularies give V = 0, not 1', kd.compare_keys(e1, e2)['V'] == 0.0)
check('symmetric', abs(kd.compare_keys(a, c)['S'] - kd.compare_keys(c, a)['S']) < 1e-9)
shared = dict(a)
shared['G0'] = 'z'
r = kd.compare_keys(a, shared)
check(f'shared labels give a code agreement figure ({r["code_agree"]:.3f})', r['code_agree'] is not None and r['code_agree'] < 1)
with tempfile.TemporaryDirectory() as d:
    for name, k in (('a.tsv', a), ('b.tsv', b)):
        Path(d, name).write_text('code\tvalue\n' + ''.join(f'{x}\t{y}\n' for x, y in k.items()), encoding='utf-8')
    out = subprocess.run([sys.executable, str(TOOLS / 'key_design.py'), '--compare', str(Path(d, 'a.tsv')),
                          str(Path(d, 'b.tsv'))], capture_output=True, text=True)
    check('CLI --compare prints S and never the shared values',
          out.returncode == 0 and 'S composite' in out.stdout and 'carmagnola' not in out.stdout)
out = subprocess.run([sys.executable, str(TOOLS / 'key_design.py'), '--help'], capture_output=True, text=True)
check('--help names --compare and Lasry', '--compare' in out.stdout and 'Lasry' in out.stdout)
print(f'{fails} failure(s)')
sys.exit(1 if fails else 0)
