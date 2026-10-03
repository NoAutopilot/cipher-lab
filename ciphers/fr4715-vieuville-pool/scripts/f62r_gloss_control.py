#!/usr/bin/env python3
"""GAPS-fr4715-vieuville-pool-11 (3 Oct 2026): rule 3's per-unit gate for no.39 f.62r's interlinear glosses.
f44r_gloss_control.py's within-leaf statistic (a recurring code's gloss consistency) cannot vary here: every f.62r
code is glossed once, so it has no pairs to score (n = 0, a non-test). This leaf instead carries glosses over
letter-cipher spans, which the printed letter key (key_vieuville_nevers.tsv, independent of the glosses) can check.
Statistic: mean difflib ratio between the letter-key decode of each C/M gloss span whose groups are all in the
key and the gloss (normalised: lower case, u=v, i=j=y, letters only). Control: the key's values permuted among
its signs (homophone counts kept), N shuffles, same spans; a permuted key changes every decoded letter, so the
control can move the statistic. Clearing it says the glossing hand writes decipherments registered to the groups
under them on this leaf; it does not test a single word-code pairing glossed once (that stays M, by adjacency).
usage: f62r_gloss_control.py witness/f62r_glosses_reconciled.tsv [--shuffles 1000] [--seed 1]"""
import csv, difflib, random, sys, os
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEY = os.path.join(HERE, '../fr4715-montholon-1589/keys/key_vieuville_nevers.tsv')

def norm(s):
    s = ''.join(c for c in s.lower() if c.isalpha())
    return s.replace('v', 'u').replace('j', 'i').replace('y', 'i')

def main():
    a = sys.argv[1:]
    S = int(a[a.index('--shuffles') + 1]) if '--shuffles' in a else 1000
    rnd = random.Random(int(a[a.index('--seed') + 1]) if '--seed' in a else 1)
    key = {r['sign']: r['value'] for r in csv.DictReader((l for l in open(KEY) if not l.startswith('#')), delimiter='\t')}
    spans = []
    for r in csv.DictReader((l for l in open(a[0]) if not l.startswith('#')), delimiter='\t'):
        groups = r['code'].split()
        if r['grade'] in ('C', 'M') and r['kind'] == 'span' and groups and all(g in key for g in groups):
            spans.append((groups, norm(r['gloss'])))
    score = lambda k: sum(difflib.SequenceMatcher(None, norm(''.join(k[g] for g in gs)), gl).ratio()
                          for gs, gl in spans) / len(spans)
    real = score(key)
    for gs, gl in spans:
        print(f"  span {' '.join(gs)} -> {''.join(key[g] for g in gs)} | gloss {gl}")
    signs = list(key); vals = list(key.values()); out = []
    for _ in range(S):
        rnd.shuffle(vals); out.append(score(dict(zip(signs, vals))))
    out.sort(); ge = sum(1 for v in out if v >= real)
    print(f'letter spans used (C/M): {len(spans)}; REAL mean ratio {real:.3f}; permuted-key mean {sum(out)/S:.3f} '
          f'p95 {out[int(0.95*S)-1]:.3f} max {out[-1]:.3f}; shuffles >= REAL {ge}/{S} (p {(ge+1)/(S+1):.4f})')

if __name__ == '__main__':
    main()
