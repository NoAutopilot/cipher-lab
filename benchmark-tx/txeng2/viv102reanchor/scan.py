#!/usr/bin/env python3
"""DV1d step (1), the registered anchor scan (PREREG-txeng2-16 DV1d, TXE2-VIV102-REANCHOR, 10 Oct 2026).

Reuses benchmark-tx/txeng2/viv102anchor/j0scan.py unchanged (its share(): the f.102r collapsed stretch aligned by the builder's
DP, tools/stream_align band 400, to a W=2700-letter window of dec_norm starting at offset s; published-key match share).
Scan s = 0..2000 step 50 (41 offsets). s* = argmax of the published-key share. At s*: 200 value-shuffled keys (seed 20261009,
the builder's shuffle) -> mean/p95/max. Selection-fair null: each shuffled key's BEST share over the same 41 offsets.
ANCHORED iff real(s*) - max(selection-fair null) >= 0.03. Prints shares only (no letter, no truth, no decode).
"""
import json, os, random, sys
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'viv102anchor'))
import j0scan as J  # noqa: E402

OFFS = list(range(0, 2001, 50))
N, SEED, GATE = 200, 20261009, 0.03


def row(key):
    return [J.share(key, J.allet[s:s + J.W]) for s in OFFS]


def main():
    ids, vv = list(J.pub), [J.pub[c] for c in J.pub]
    rng = random.Random(SEED)
    keys = []
    for _ in range(N):
        rng.shuffle(vv); keys.append(dict(zip(ids, vv)))
    with Pool(4) as p:
        res = p.map(row, [J.pub] + keys, chunksize=4)
    real, sh = res[0], res[1:]
    k = max(range(len(OFFS)), key=lambda i: real[i]); s_star = OFFS[k]
    at = sorted(r[k] for r in sh); best = sorted(max(r) for r in sh)
    out = dict(offsets=OFFS, real={s: round(x, 4) for s, x in zip(OFFS, real)},
               shuf_max_per_offset={s: round(max(r[i] for r in sh), 4) for i, s in enumerate(OFFS)},
               s_star=s_star, real_s_star=round(real[k], 4),
               at_s_star=dict(mean=round(sum(at) / N, 4), p95=round(at[189], 4), max=round(at[-1], 4),
                              rank=1 + sum(x >= real[k] for x in at), margin_max=round(real[k] - at[-1], 4)),
               selection_fair=dict(mean=round(sum(best) / N, 4), p95=round(best[189], 4), max=round(best[-1], 4),
                                   rank=1 + sum(x >= real[k] for x in best), margin=round(real[k] - best[-1], 4)),
               n_shuffles=N, seed=SEED, W=J.W, n_seg=len(J.seg), gate=GATE)
    out['anchored'] = out['selection_fair']['margin'] >= GATE
    json.dump(out, open(os.path.join(HERE, 'scan.json'), 'w'), indent=1)
    print(json.dumps({k_: v for k_, v in out.items() if k_ not in ('offsets',)}, indent=1))


if __name__ == '__main__':
    main()
