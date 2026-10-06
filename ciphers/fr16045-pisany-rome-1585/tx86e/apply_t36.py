#!/usr/bin/env python3
"""R12A-PISRS (6 Oct 2026; pisrs/PREREG_t36commit.md): derive tx86e/ciphertext_f275r.tsv from the pre-edit reconciled file
tx86e/ciphertext_f275r_preT36.tsv by relabelling T31 -> T36 at the f275r tokens pis2/t31_tokens.tsv marks SETTLED-T36
(R9-PIS2 shape compare; copy s). Index over non-'/' tokens, 0-based; each target is asserted T31 with its pis2/tokens_pos.tsv context.
    python3 tx86e/apply_t36.py [--check]   (--check: exit 1 if the committed file differs from what this derives)"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
SRC, DST = os.path.join(H, 'ciphertext_f275r_preT36.tsv'), os.path.join(H, 'ciphertext_f275r.tsv')
picks, pos = {}, {}
for ln in open(os.path.join(T, 'pis2/t31_tokens.tsv')).read().splitlines()[1:]:
    f = ln.split('\t')
    if f[0] == 'f275r' and f[8] == 'SETTLED-T36':
        picks[(f[1], int(f[2]))] = 'T36'
for ln in open(os.path.join(T, 'pis2/tokens_pos.tsv')).read().splitlines()[1:]:
    f = ln.split('\t')
    if f[0] == 'f275r':
        pos[(f[1], int(f[2]))] = f[3]
assert len(picks) == 4, picks
out, done = [], set()
for ln in open(SRC):
    if not ln.strip():
        out.append(ln); continue
    lab, body = ln.rstrip('\n').split('\t', 1)
    t = body.split(); nz = [n for n, x in enumerate(t) if x != '/']
    for (l, i), v in picks.items():
        if l != lab:
            continue
        assert t[nz[i]] == 'T31', (l, i, t[nz[i]])
        c = [x for x in pos[(l, i)].split() if x != '/']; m = next(k for k, x in enumerate(c) if x.startswith('['))
        got = [t[nz[i - m + k]] if 0 <= i - m + k < len(nz) else None for k in range(len(c))]
        assert [g.strip('?[]') if g else None for g in got] == [w.strip('?[]') for w in c], (l, i, got, c)
        t[nz[i]] = v; done.add((l, i))
    out.append(f'{lab}\t{" ".join(t)}\n')
assert done == set(picks), (done, picks)
new = ''.join(out)
if '--check' in sys.argv:
    ok = open(DST).read() == new
    print('tx86e/ciphertext_f275r.tsv', 'up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(DST, 'w').write(new)
print('wrote tx86e/ciphertext_f275r.tsv:', ', '.join(f'{l} i{i} T31->T36' for l, i in sorted(picks)))
