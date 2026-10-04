# Compare the worker's own audit read of a line with reconciled.tsv and with each raw (mapped) pass, NW-aligned (difflib).
import csv, sys, difflib, collections
rec = collections.defaultdict(list)
for r in csv.DictReader(open(sys.argv[1]), delimiter='\t'): rec[r['line']].append((r['label'], r['grade']))
def passrows(f):
    d = collections.defaultdict(list)
    for r in csv.DictReader(open(f), delimiter='\t'): d[r['line'].split('_',1)[1]].append(r['sign'])
    return d
A, B = passrows(sys.argv[3]), passrows(sys.argv[4])
tot = collections.Counter()
for row in open(sys.argv[2]):
    ln, toks = row.rstrip('\n').split('\t'); mine = toks.split()
    for name, seq in (('rec', [x[0] for x in rec[ln]]), ('A', A[ln]), ('B', B[ln])):
        sm = difflib.SequenceMatcher(None, mine, seq, autojunk=False)
        m = sum(b.size for b in sm.get_matching_blocks()); n = max(len(mine), len(seq))
        tot[name, 'm'] += m; tot[name, 'n'] += n
        print(ln, name, f'{m}/{n}', f'err={1-m/n:.3f}')
    # H-grade accuracy
    sm = difflib.SequenceMatcher(None, mine, [x[0] for x in rec[ln]], autojunk=False)
    ok = set()
    for b in sm.get_matching_blocks(): ok.update(range(b.b, b.b + b.size))
    for i, (lab, g) in enumerate(rec[ln]):
        tot['g' + g, 'n'] += 1; tot['g' + g, 'm'] += i in ok
for k in ('rec', 'A', 'B', 'gH', 'gM'):
    if tot[k, 'n']: print('TOTAL', k, f"{tot[k,'m']}/{tot[k,'n']}", f"err={1-tot[k,'m']/tot[k,'n']:.3f}")
