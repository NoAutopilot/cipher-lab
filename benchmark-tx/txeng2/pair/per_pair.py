# TXE2-PAIR post-score breakdown (run only AFTER tx_bench scored the committed outputs): per pair fixed/broken of the
# positions each output changed vs L, via tools/tx_bench.position_errors. Usage: python3 benchmark-tx/txeng2/pair/per_pair.py
import csv, os, sys
from collections import Counter
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(R, 'tools'))
import tx_bench as B
item = [r for r in B.read_tsv(os.path.join(R, 'BENCHMARK-TX.tsv')) if r['item'] == 'birago1572-no87'][0]
truth = B.read_tsv(os.path.join(R, item['truth']))
L = B.load_output([os.path.join(R, 'benchmark-tx/txeng/units/labels_dev_tune.tsv')], None)
eb = B.position_errors(truth, L)
for tag in [''] + [f'ctrl{s}_' for s in range(1, 6)]:
    o = os.path.join(R, f'benchmark-tx/outputs/birago1572-no87/passX2_pair_{tag}dev_tune.tsv')
    eo = B.position_errors(truth, B.load_output([o], None))
    lrd = {(r['line'], r['pos']): r['sign'] for r in csv.DictReader(open(os.path.join(R, 'benchmark-tx/txeng/units/labels_dev_tune.tsv')), delimiter='\t')}
    ord_ = {(r['line'], r['pos']): r['sign'] for r in csv.DictReader(open(o), delimiter='\t')}
    c = Counter()
    for k, s in ord_.items():
        if s == lrd[k] or k not in eb or k not in eo:
            if s != lrd[k]: c[(f'{lrd[k]}->{s}', 'unscored')] += 1
            continue
        c[(f'{lrd[k]}->{s}', 'fixed' if eb[k] and not eo[k] else 'broken' if eo[k] and not eb[k] else 'both-wrong')] += 1
    print(tag or 'real', ' '.join(f'{m}:{k}={v}' for (m, k), v in sorted(c.items())))
