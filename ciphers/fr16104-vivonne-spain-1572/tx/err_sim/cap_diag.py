#!/usr/bin/env python3
"""ERR-SIM post-hoc diagnostic (descriptive, NOT in the PREREG gate): which key cells cap the all-H run at zero reader error.
Longest stretch of the synthetic plaintext free of the letters that cannot decode H under key.tsv, removing one break class at a time."""
import os, re, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.argv = sys.argv[:1]
import err_sim as E
pt, _ = E.plaintext(15762); key = E.load_key()
hl = {m for c, (m, g) in key.items() if g != 'M'}
ml = {m for c, (m, g) in key.items()} - hl
ul = set('abcdefghijklmnopqrstuvwxyz') - hl - ml
def longest(bad):
    return max((len(x) for x in re.split('[' + ''.join(sorted(bad)) + ']', pt)), default=0) if bad else len(pt)
out = {'M_only_letters': ''.join(sorted(ml)), 'no_code_letters': ''.join(sorted(ul)), 'run_as_key_stands': longest(ml | ul),
       'run_if_no_code_letters_got_H_codes': longest(ml), 'run_if_M_letters_were_H': longest(ul)}
for x in sorted(ml | ul):
    out[f'run_if_{x}_alone_fixed'] = longest((ml | ul) - {x})
for pair in ('fp', 'fm', 'pm', 'hb', 'fpm', 'fpmh', 'fpmhb'):
    out[f'run_if_{pair}_fixed'] = longest((ml | ul) - set(pair))
print(json.dumps(out, indent=1)); json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cap_diag.json'), 'w'), indent=1)
