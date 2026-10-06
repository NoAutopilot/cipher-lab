#!/usr/bin/env python3
"""D4-PAG13 (6 Oct 2026): apply the sister folder's 1714 Paget key to the 1714 letters' cipher tokens and
write the residue tables this folder needs for the day Clairambault 297 p.249 (14 Jan 1713) is reproduced.

Reads, never writes, ../clairambault1225-paget-1714/{key.tsv, ciphertext.tsv, reading_tokens.tsv, votes.tsv}.
Writes residue_1714_codes.tsv (one row per code seen in the 1714 letters, plus key codes never seen in them)
and residue_1714_unglossed.tsv (the cipher tokens with no period gloss chunk of their own, key applied).
A token is 'glossed' when votes.tsv carries a non-empty value for its (line, position).
--check exits 1 if either committed table differs from a fresh regeneration (rule 7).
"""
import csv, os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
SIS = os.path.join(HERE, '..', 'clairambault1225-paget-1714')

def rows(name):
    with open(os.path.join(SIS, name), newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))

def build():
    key = {r['code']: r for r in rows('key.tsv')}
    letter = {}
    for r in rows('ciphertext.tsv'):
        letter[(r['line'], r['position'])] = r['letter']
    votes = {(r['line'], r['position']): r['value'] for r in rows('votes.tsv')}
    toks = rows('reading_tokens.tsv')
    exc = {(r['line'], r['position']) for r in rows('exceptions.tsv')}
    by = collections.OrderedDict()
    ungl = []
    for t in toks:
        k = (t['line'], t['pos'])
        glossed = votes.get(k, '') not in ('', '?')
        code = t['sign']
        d = by.setdefault(code, {'n': 0, 'gl': 0, 'L': set(), 'pos': [], 'gr': collections.Counter(), 'rd': collections.Counter()})
        d['n'] += 1; d['gl'] += glossed; d['L'].add('L' + letter.get(k, '?'))
        d['pos'].append(f"{t['line']}:{t['pos']}" + ('' if glossed else '*'))
        d['gr'][t['grade']] += 1
        d['rd'][t['value'] + ('(exc)' if k in exc else '')] += 1
        if not glossed:
            kv = key.get(code)
            ungl.append([t['line'], t['pos'], 'L' + letter.get(k, '?'), code,
                         kv['value'] if kv else 'OPEN', kv['grade'] if kv else '-', t['grade'],
                         t['value'], 0])
    # final occurrence counts for the unglossed table
    for u in ungl:
        u[8] = by[u[3]]['n']
    out = []
    def numkey(c):
        return (0, int(c)) if c.isdigit() else (1, c)
    for code in sorted(set(by) | set(key), key=numkey):
        d = by.get(code)
        kv = key.get(code)
        if kv is None:
            status = 'OPEN'
        elif kv['grade'] in ('H', 'C', 'S'):
            status = 'firm'
        else:
            status = 'weak'
        if d is None:
            status += ',unseen'
        rd = ' '.join(f"{v}:{n}" for v, n in sorted(d['rd'].items())) if d else ''
        gr = ' '.join(f"{g}{n}" for g, n in sorted(d['gr'].items())) if d else ''
        out.append([code, d['n'] if d else 0, d['gl'] if d else 0, (d['n'] - d['gl']) if d else 0,
                    ','.join(sorted(d['L'])) if d else '', kv['value'] if kv else 'OPEN', kv['grade'] if kv else '-',
                    gr, rd, status, ' '.join(d['pos']) if d else ''])
    t1 = [['code', 'n_tokens', 'n_glossed', 'n_unglossed', 'letters', 'key_value', 'key_grade',
           'token_grades', 'read_as(value:n; exc=exceptions.tsv image/settle ruling)', 'status', 'positions(*=unglossed)']] + out
    t2 = [['line', 'pos', 'letter', 'code', 'key_value', 'key_grade', 'token_grade', 'read_as', 'code_n_tokens']] + ungl
    return {'residue_1714_codes.tsv': t1, 'residue_1714_unglossed.tsv': t2}

def render(t):
    return ''.join('\t'.join(str(c) for c in r) + '\n' for r in t)

if __name__ == '__main__':
    tabs = build()
    if '--check' in sys.argv:
        stale = [n for n, t in tabs.items()
                 if not os.path.exists(os.path.join(HERE, n)) or open(os.path.join(HERE, n)).read() != render(t)]
        print('stale: ' + ', '.join(stale) if stale else 'residue_1714 up to date'); sys.exit(1 if stale else 0)
    for n, t in tabs.items():
        open(os.path.join(HERE, n), 'w').write(render(t))
        print(n, len(t) - 1, 'rows')
