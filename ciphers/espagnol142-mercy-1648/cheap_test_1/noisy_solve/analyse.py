#!/usr/bin/env python3
"""Campaign step H9 (28 Sept 2026): what the error-tolerant solve (--noise 0.05) names, on the target and on its control.
Control: the 5-percent-corrupted exact-profile Cartas controls (H1); precision/recall of the solver's free positions
against the truly corrupted positions (control_truth_seed*.json). Target: the free positions mapped onto
cipher_codes.tsv rows (line, position, sign) and reading_tokens.tsv (current letter, grade).
  python3 ciphers/espagnol142-mercy-1648/cheap_test_1/noisy_solve/analyse.py
"""
import json, os, collections
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(H, '..', '..')
print('== control: 5% corrupted exact-profile Cartas windows, es17 model, --noise 0.05')
for s in (1, 2, 3):
    o = json.load(open(f'{H}/control_es17_n0.05_seed{s}.json')); tr = json.load(open(f'{H}/control_truth_seed{s}.json'))
    free = {int(k): v for k, v in o['free'].items()}; truth = set(tr['corrupted_positions_letter_changed'])
    hit = sorted(set(free) & truth)
    p = tr['plain']; dec = o['decoded']; ok = sum(1 for a, b in zip(dec, p) if a == b)
    fixed_right = sum(1 for i in hit if free[i] == p[i])
    print(f'  seed {s}: score {o["score"]:.1f}, named {len(free)}, truly corrupted {len(truth)}, named&corrupted {len(hit)} '
          f'(precision {len(hit)/max(1,len(free)):.2f}, recall {len(hit)/len(truth):.2f}), letter right at those {fixed_right}; '
          f'corrected decode reads {ok}/{len(p)} = {ok/len(p):.1%}')
rows = [l.rstrip('\n').split('\t') for l in open(f'{T}/cipher_codes.tsv')][1:]
rt = {}
for l in open(f'{T}/reading_tokens.tsv'):
    c = l.rstrip('\n').split('\t')
    if c[0] != 'line': rt[(c[0], c[1])] = c
print('== target: positions named as misread (line:pos sign -> solver letter | reading letter grade)')
count = collections.Counter(); named_by = collections.defaultdict(list)
for model in ('es17', 'es17c7'):
    for s in (1, 2, 3):
        o = json.load(open(f'{H}/target_{model}_n0.05_seed{s}.json'))
        free = {int(k): v for k, v in o['free'].items()}
        print(f'  {model} seed {s}: score {o["score"]:.1f}, restarts {o["restart_scores"][:3]}, named {len(free)}')
        for i, v in free.items():
            count[i] += 1; named_by[i].append(f'{model}/s{s}:{v}')
print('  position | sign | times named (of 6) | solver letters | reading letter, grade | note')
flags = {('r16', '21'): 'code 72', ('r17', '10'): 'code 52', ('r17', '20'): 'code 48', ('r20', '15'): 'code 48', ('r24', '4'): 'code 65',
         ('r06', '3'): 'code 9 (H11)', ('r06', '14'): 'MEYE 14/19', ('r14', '7'): 'MEYE 14/19', ('r16', '3'): 'MEYE 14/19', ('r16', '6'): 'MEYE 14/19', ('r17', '5'): 'MEYE 14/19'}
for i, n in sorted(count.items(), key=lambda x: (-x[1], x[0])):
    line, pos, sign = rows[i][0], rows[i][1], rows[i][2]
    r = rt.get((line, pos)); rl = f'{r[4]} {r[5]}' if r else '?'
    print(f'  {line}:{pos} | {sign} | {n} | {",".join(named_by[i])} | {rl} | {flags.get((line, pos), "")}')
m_named = sum(1 for i in count if rt.get((rows[i][0], rows[i][1]), ['']*6)[5] == 'M')
print(f'  distinct positions named {len(count)}; named by >=3 of 6 runs {sum(1 for v in count.values() if v>=3)}; M-graded among named {m_named}')
