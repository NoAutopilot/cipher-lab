#!/usr/bin/env python3
"""MONL-K14TRY (15 Oct 2026): K14/K34-for-s and K62-for-m --try with power and wrong-facing controls (k14try/PREREG-MONL-K14TRY.md).
Same design as k04try/run_k04try.py (reuses its build()); key.tsv here is never written. Writes k14try/try_log.tsv, runs.txt,
per_occurrence.tsv. Usage: python3 k14try/run_k14try.py SCRATCH_DIR (from the target folder)."""
import csv, os, random, re, subprocess, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(HERE, 'k04try'))
from run_k04try import build, TOOL

ROWS = list(csv.DictReader(open(os.path.join(HERE, 'align_c268.tsv')), delimiter='\t'))
def pos(signs, clear):
    return sorted((r['line'], r['pos']) for r in ROWS if r['sign'] in signs and r['clear'] == clear)
def draw(p, k):
    return sorted(random.Random(415).sample(p, k))

def runs():
    t14, t34 = pos({'K14'}, 's'), pos({'K34'}, 's')
    pcs = pos({'K37', 'K67'}, 's')
    ncs = pos({'K14', 'K34'}, 'p')
    tm, pcm = pos({'K62'}, 'm'), pos({'K11', 'K65'}, 'm')
    ncm = draw(pos({'K10'}, 'l'), 11)
    assert (len(t14), len(t34), len(pcs), len(ncs), len(tm), len(pcm)) == (19, 3, 19, 17, 11, 5)
    return [('R0s', [], None, None, 'K14=s'), ('R0m', [], None, None, 'K62=m'),
            ('T14', t14, 'K14S', 'p', 'K14S=s'), ('PCs', pcs, 'K37X', 'p', 'K37X=s'), ('NCs', ncs, 'K14P', 'p', 'K14P=s'),
            ('T34', t34, 'K34S', 'p', 'K34S=s'), ('PC3', draw(pcs, 3), 'K37X', 'p', 'K37X=s'),
            ('NC3', draw(pos({'K34'}, 'p'), 3), 'K34P', 'p', 'K34P=s'),
            ('Tm', tm, 'K62M', 'l', 'K62M=m'), ('PCm', pcm, 'K11X', 'l', 'K11X=m'), ('NCm', ncm, 'K10L', 'l', 'K10L=m')]

def main():
    scratch = sys.argv[1]
    log = os.path.join(scratch, 'try_log.tsv')
    if os.path.exists(log): os.remove(log)
    R, out = runs(), []
    for name, p, code, val, hyp in R:
        d = build(scratch, name, p, code, val)
        out.append(f'== {name} {hyp} n={len(p) or "code-wide"} positions: ' + ' '.join(f'{l}:{q}' for l, q in p))
        r = subprocess.run([sys.executable, TOOL, d, '--try', hyp, '--try-log', log], capture_output=True, text=True)
        out.append(r.stdout + r.stderr)
    open(os.path.join(HERE, 'k14try', 'runs.txt'), 'w').write('\n'.join(out).replace(scratch, 'scratch'))
    per = ['set\tline:pos\tgain_bits']
    for name, p, code, val, hyp in R:
        if not p or name in ('PC3',):
            continue
        for i, lp in enumerate(p):
            d = build(scratch, f'{name}_{i}', [lp], code, val)
            r = subprocess.run([sys.executable, TOOL, d, '--try', hyp, '--nulls', '1'], capture_output=True, text=True)
            m = re.search(r'statistic (-?[0-9.]+) bits', r.stdout)
            per.append(f'{name}\t{lp[0]}:{lp[1]}\t{m.group(1) if m else "NA"}')
    open(os.path.join(HERE, 'k14try', 'per_occurrence.tsv'), 'w').write('\n'.join(per) + '\n')
    for name in [x[0] for x in R if x[1]]:
        g = [float(x.split('\t')[2]) for x in per[1:] if x.startswith(name + '\t') and x.split('\t')[2] != 'NA']
        if g: print(name, 'positive', sum(v > 0 for v in g), 'of', len(g), 'lose>3', sum(v < -3 for v in g))
    lines = open(log).read().replace(scratch, 'scratch').splitlines()
    open(os.path.join(HERE, 'k14try', 'try_log.tsv'), 'w').write('\n'.join(lines) + '\n')
    print('\n'.join(lines))

if __name__ == '__main__':
    main()
