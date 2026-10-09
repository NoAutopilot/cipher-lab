"""TXE2-SHEET3: tx_offsheet.recall (as measured + --exclude-flagged) on the v4 baseline, plus a per-error listing
from the same detect rows, in one process (one opening of eval truth). Chance P: binomial P(>= caught) at the scored
flagged share (X1b's convention)."""
import json, sys
from math import comb
sys.path.insert(0, 'tools')
import tx_offsheet as xo, tx_bench as tb
D = 'benchmark-tx/txeng2/txe2-sheet3/'
cfg = json.load(open(D + 'items/spinelli-c1519-confirm.json'))
det = tb.read_tsv(D + 'detect_spinelli-c1519-confirm.tsv')
base = 'benchmark-tx/outputs/spinelli-c1519-confirm/passZ_v4.tsv'
def binp(n, k, p):
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))
out = []
for ex in (False, True):
    r = xo.recall(cfg, det, base, ex)
    r['chance_P'] = round(binp(r['errors'] - r['errors_untiled'] if False else r['errors'], r['caught'], r['share_scored']), 4)
    out.append(r)
with open(D + 'recall.jsonl', 'w') as f:
    for r in out:
        f.write(json.dumps(r) + '\n')
        print(json.dumps(r))
# per-error listing (flagged-excluded truth)
lm = tb.load_label_map(cfg['label_map'])
T = tb.map_truth(tb.drop_flagged(tb.read_tsv(cfg['truth_for_ref'])), lm)
o = tb.load_output([base]); o = {k: [lm.get(s, s) for s in v] for k, v in o.items()}
eb = tb.position_errors(T, o)
dd = {(r['line'], str(r['pos'])): r for r in det}
tr = {(r['line'], str(r['pos'])): r for r in T}
rows = []
for k, v in eb.items():
    if not v:
        continue
    d = dd.get(k)
    if d is None:
        cls = 'untiled'
    elif int(d['reader_flag']):
        cls = 'reader-flag'
    elif int(d['flagged']):
        cls = 'off-sheet-score'
    elif d['consensus']:
        cls = 'consensus-on-sheet'
    else:
        cls = 'split-unflagged'
    rows.append(dict(line=k[0], pos=k[1], truth=tr[k]['truth'], plain=tr[k]['plain'],
                     reads=d['reads'] if d else '', consensus=d['consensus'] if d else '',
                     rank_share=d['rank_share'] if d else '', flagged=d['flagged'] if d else '', cls=cls))
cols = ['line', 'pos', 'truth', 'plain', 'reads', 'consensus', 'rank_share', 'flagged', 'cls']
with open(D + 'errors_v4.tsv', 'w') as f:
    f.write('\t'.join(cols) + '\n')
    for r in rows:
        f.write('\t'.join(str(r[c]) for c in cols) + '\n')
        print('\t'.join(str(r[c]) for c in cols))
