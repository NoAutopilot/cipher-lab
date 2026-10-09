#!/usr/bin/env python3
"""TXE2-WEIGHT post-score breakdown (run only after tx_bench scored the committed outputs): per changed position of the
X5 and uniform dev_tune outputs, the truth, the base (L) sign, the output sign, every reader's aligned read and, for X5,
the LOO weights' top three; plus the fate of L's all-same-wrong positions and the registered B T24 / F X_NEW biases."""
import os, sys
from collections import Counter
sys.path.insert(0, 'tools')
import tx_bench, tx_taxonomy, tx_weighted_vote as W
D = 'benchmark-tx/outputs/birago1572-no87'; U = 'benchmark-tx/txeng/units'
RD = [('A', 'passA.tsv'), ('B', 'passB.tsv'), ('E', 'passE_sheet.tsv'), ('F', 'passF_fable.tsv'),
      ('K2', 'passK2_sr4_dev_tune.tsv'), ('V_s0', 'passV_s0_dev_tune.tsv'), ('V_s1', 'passV_s1_dev_tune.tsv')]
readers = [(n, tx_bench.load_output([os.path.join(D, p)])) for n, p in RD]
T = W.key_signs('ciphers/nevers-birago-fr3251-1572/harvest/key_1572_sheet.tsv')
tl = set(W.unit_lines(U + '/labels_dev_tune.tsv'))
truth = [r for r in W.truth_rows('BENCHMARK-TX.tsv', 'birago1572-no87') if r['line'] in tl]
base = tx_bench.load_output([U + '/labels_dev_tune.tsv'])
breads, _ = tx_taxonomy.aligned_reads(truth, base)
rreads = {n: tx_taxonomy.aligned_reads(truth, rl)[0] for n, rl in readers}
tmap = {(r['line'], r['pos']): r for r in truth if r['status'] == 'scored'}
def ok(k, s):
    return s in set(filter(None, tmap[k]['truth'].split('|')))
for tag in ('weighted', 'uniform'):
    out = tx_bench.load_output([os.path.join(D, 'passX5_%s_dev_tune.tsv' % tag)])
    oreads, _ = tx_taxonomy.aligned_reads(truth, out)
    print('\n## %s: changed scored positions (truth-aligned)' % tag)
    print('| line pos | truth | L | out | verdict | reads A B E F K2 V_s0 V_s1 |'); print('|---|---|---|---|---|---|')
    for k in sorted(tmap):
        if k not in breads or k not in oreads or breads[k] == oreads[k]:
            continue
        v = {(True, False): 'fixed', (False, True): 'broken', (True, True): 'both right (homophone)', (False, False): 'both wrong'}[(ok(k, oreads[k]), ok(k, breads[k]))]
        rs = ' '.join(rreads[n].get(k, '.') for n, _ in readers)
        print('| %s %s | %s | %s | %s | %s | %s |' % (k[0], k[1], tmap[k]['truth'], breads[k], oreads[k], v, rs))
# all-same-wrong: every covering reader wrong with L's sign
print('\n## L errors and their fate under X5 / uniform')
outw = tx_taxonomy.aligned_reads(truth, tx_bench.load_output([D + '/passX5_weighted_dev_tune.tsv']))[0]
outu = tx_taxonomy.aligned_reads(truth, tx_bench.load_output([D + '/passX5_uniform_dev_tune.tsv']))[0]
for k in sorted(tmap):
    if k in breads and not ok(k, breads[k]):
        rs = [rreads[n][k] for n, _ in readers if k in rreads[n]]
        cls = 'all-same-wrong' if all(s == breads[k] for s in rs) else 'all-wrong' if not any(ok(k, s) for s in rs) else \
              '%d/%d readers right' % (sum(ok(k, s) for s in rs), len(rs))
        print('| %s %s | truth %s | L %s | %s | X5 %s | uniform %s |' % (k[0], k[1], tmap[k]['truth'], breads[k], cls,
              outw.get(k), outu.get(k)))
# registered biases: full-dev counts for B read T24 and F read X_NEW
c, _ = W.learn_counts(readers, truth, tl)
for n, s in (('B', 'T24'), ('F', 'X_NEW')):
    cc = c[n].get(s, Counter())
    w = W.weight_fn(c, T | set(t for x in c.values() for y in x.values() for t in y))
    top = sorted(((w(n, s, t), t) for t in T), reverse=True)[:3]
    print('\n%s read %s on dev_tune: truth counts %s; w top3 %s' % (n, s, dict(cc), ['%s %.2f' % (t, v) for v, t in top]))
