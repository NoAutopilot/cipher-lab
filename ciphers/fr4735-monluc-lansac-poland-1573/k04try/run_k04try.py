#!/usr/bin/env python3
"""MONL-K04TRY (15 Oct 2026): K04-for-n --try with negative and power controls (PREREG-MONL-K04TRY.md).
Builds scratch copies of the folder (key.tsv here is never written), runs tools/decode_key.py --try, writes k04try/try_log.tsv
and k04try/runs.txt. Usage: python3 k04try/run_k04try.py SCRATCH_DIR (from the target folder)."""
import csv, os, re, random, shutil, subprocess, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOL = os.path.join(HERE, '..', '..', 'tools', 'decode_key.py')
FILES = ['decode.json', 'key.tsv', 'ciphertext_c172.tsv', 'ciphertext_c268.tsv', 'exceptions_c268.tsv', 'votes_c172.tsv', 'votes_c268.tsv']

def positions(sign, clear):
    with open(os.path.join(HERE, 'align_c268.tsv')) as f:
        return [(r['line'], r['pos']) for r in csv.DictReader(f, delimiter='\t') if r['sign'] == sign and r['clear'] == clear]

def build(scratch, name, pos, newcode, value):
    d = os.path.join(scratch, name)
    os.makedirs(d, exist_ok=True)
    for fn in FILES:
        shutil.copy(os.path.join(HERE, fn), d)
    if pos:
        ps = set(pos)
        rows = list(csv.reader(open(os.path.join(d, 'ciphertext_c268.tsv')), delimiter='\t'))
        hit = 0
        for r in rows[1:]:
            if (r[0], r[1]) in ps:
                r[2] = newcode; hit += 1
        assert hit == len(ps), (name, hit, len(ps))
        csv.writer(open(os.path.join(d, 'ciphertext_c268.tsv'), 'w'), delimiter='\t', lineterminator='\n').writerows(rows)
        with open(os.path.join(d, 'key.tsv'), 'a') as f:
            f.write(f'{newcode}\t1\t{value}\tH\tscratch pseudo-code MONL-K04TRY\n')
    return d

def main():
    scratch = sys.argv[1]
    log = os.path.join(scratch, 'try_log.tsv')
    if os.path.exists(log): os.remove(log)
    n_k04 = sorted(positions('K04', 'n'))
    d_k04 = sorted(random.Random(415).sample(sorted(positions('K04', 'd')), 15))
    n_k12 = sorted(random.Random(415).sample(sorted(positions('K12', 'n')), 15))
    assert len(n_k04) == 15
    runs = [('R0', [], None, None, 'K04=n'), ('T', n_k04, 'K04N', 'd', 'K04N=n'),
            ('NC', d_k04, 'K04D', 'd', 'K04D=n'), ('PC', n_k12, 'K12X', 'd', 'K12X=n')]
    out = []
    for name, pos, code, val, hyp in runs:
        d = build(scratch, name, pos, code, val)
        out.append(f'== {name} {hyp} positions: ' + ' '.join(f'{l}:{p}' for l, p in pos))
        r = subprocess.run([sys.executable, TOOL, d, '--try', hyp, '--try-log', log], capture_output=True, text=True)
        out.append(r.stdout + r.stderr)
    open(os.path.join(HERE, 'k04try', 'runs.txt'), 'w').write('\n'.join(out))
    # per-occurrence gains (n=1 runs, verdict undecided by design; only the statistic is read)
    per = ['set\tline:pos\tgain_bits']
    for name, pos, code, val, hyp in runs[1:]:
        for i, lp in enumerate(pos):
            d = build(scratch, f'{name}_{i}', [lp], code, val)
            r = subprocess.run([sys.executable, TOOL, d, '--try', hyp, '--nulls', '1'], capture_output=True, text=True)
            m = re.search(r'statistic (-?[0-9.]+) bits', r.stdout)
            per.append(f'{name}\t{lp[0]}:{lp[1]}\t{m.group(1) if m else "NA"}')
    open(os.path.join(HERE, 'k04try', 'per_occurrence.tsv'), 'w').write('\n'.join(per) + '\n')
    for name in ('T', 'NC', 'PC'):
        g = [float(x.split('\t')[2]) for x in per[1:] if x.startswith(name + '\t') and x.split('\t')[2] != 'NA']
        print(name, 'positive', sum(v > 0 for v in g), 'of', len(g), 'lose>3', sum(v < -3 for v in g))
    lines = open(log).read().replace(scratch, 'scratch').splitlines()
    open(os.path.join(HERE, 'k04try', 'try_log.tsv'), 'w').write('\n'.join(lines) + '\n')
    print('\n'.join(lines))

if __name__ == '__main__':
    main()
