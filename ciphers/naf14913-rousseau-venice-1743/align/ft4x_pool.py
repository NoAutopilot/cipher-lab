#!/usr/bin/env python3
"""FT4x (account-4, 3 Oct 2026): pooled EXACT pin run, f.252r gloss jointly with the control-backed f.266r segments
(S1 groups 0-74, S2 groups 76-138) and, only if it fits exactly on its own, the f.249 FT4t segment (groups 39-100).
Pre-registered in PREREG-FT4x.md, pushed before any run.

Instrument (new; the one-edit family is [retired] for f.249): the ft4s_seg segment CP-SAT with ZERO edits (no release,
no drop) on one concatenated model: blocks joined by a separator token '#SEP' pinned to the chunk '|', so a code that
occurs in two blocks must carry the same chunk in both (shared code = joint pin). C pins of the current key inside the
blocks: 22 de, 66 r, 581 au (never released). 722 left free (undecided). J = fit / nofit (proved) / unresolved.
Controls (seed 3, n 40), only the f.252r block is perturbed, the other blocks stay real:
  (s) f.252r gloss words shuffled; (g) f.252r group order shuffled.  Unresolved counts high (as a fit).
  python3 ft4x_pool.py --stage0          (exact fit of each block alone; shared-code list)
  python3 ft4x_pool.py --ctrl s|g        (40 draws, Pool(4))
  python3 ft4x_pool.py --real            (J_real, then the unique-chunk readout if it fits)
"""
import argparse, inspect, os, random, sys, time
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ft4s_seg as fs
import ft4u_seg as fu
import ft4t_seg as ftt
import ft4v_pair as fv

# exact (0-edit) variant of ft4s_seg.solve_pins, plus an optional 'forbid' {code: chunk} for the uniqueness readout
_src = inspect.getsource(fs.solve_pins)
assert _src.count('m.Add(sum(edv) <= 1)') == 1
_src = _src.replace('def solve_pins(toks, text, pins, limit, force=None):',
                    'def solve_exact(toks, text, pins, limit, force=None, forbid=None):')
_src = _src.replace('m.Add(sum(edv) <= 1)', 'm.Add(sum(edv) == 0)\n'
                    '    for _c, _v in (forbid or {}).items():\n'
                    '        if _v in chunks:\n'
                    '            m.Add(kc[_c] != chunks[_v])')
_ns = dict(fs.__dict__)
exec(_src, _ns)
solve_exact = _ns['solve_exact']

PINS = {'22': 'de', '66': 'r', '581': 'au', '#SEP': '|'}
LIMIT = 30.0


def blocks():
    s1t, s1x, _ = fs.segment1()
    s2t, s2x, _ = fu.segment('S2')
    s9t, s9x, _ = ftt.segment()
    gt, gw = fv.load('primary')
    return {'S1': (s1t, s1x), 'S2': (s2t, s2x), 'F249': (s9t, s9x)}, (gt, gw)


def pooled(blks, gt, gx):
    toks, text = [], ''
    for t, x in blks + [(gt, gx)]:
        if toks:
            toks.append('#SEP'); text += '|'
        toks += t; text += x
    return toks, text


def J(job):
    toks, text, forbid = job
    return solve_exact(toks, text, PINS, LIMIT, forbid=forbid)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--stage0', action='store_true')
    ap.add_argument('--real', action='store_true')
    ap.add_argument('--ctrl', choices=['s', 'g'])
    ap.add_argument('--with249', action='store_true', help='include F249 (only if stage0 shows it fits exactly)')
    a = ap.parse_args()
    B, (gt, gw) = blocks()
    use = ['S1', 'S2'] + (['F249'] if a.with249 else [])
    if a.stage0:
        for k, (t, x) in B.items():
            t0 = time.time()
            print(f'stage0 {k}: groups {len(t)} letters {len(x)} exact {solve_exact(t, x, PINS, LIMIT)} {time.time()-t0:.1f}s')
        print(f'stage0 f252r alone exact {solve_exact(gt, "".join(gw), PINS, LIMIT)}')
        for k, (t, x) in B.items():
            print(f'shared f252r/{k}: {sorted(set(gt) & set(t))}')
        return
    blks = [B[k] for k in use]
    if a.real:
        toks, text = pooled(blks, gt, ''.join(gw))
        t0 = time.time(); r = J((toks, text, None))
        print(f'REAL blocks {use}+f252r: J {"unresolved" if r is None else ("fit" if r else "nofit")} {time.time()-t0:.1f}s', flush=True)
        if r:
            sh = sorted(set(gt) & set(t for b in blks for t in b[0]))
            for c in sh:   # unique-chunk readout: does any chunk other than each feasible one also fit? enumerate
                feas = []
                for l in range(1, fs.MAXLEN + 1):
                    for p in range(len(''.join(gw)) - l + 1):
                        v = ''.join(gw)[p:p + l]
                        if v in feas:
                            continue
                        pins = dict(PINS, **{c: v})
                        if solve_exact(toks, text, pins, LIMIT) is not False:
                            feas.append(v)
                print(f'readout {c}: feasible chunks {len(feas)} {feas[:12]}', flush=True)
        return
    rng = random.Random(3)
    js, jg = [], []
    for _ in range(40):
        x = gw[:]; rng.shuffle(x); js.append((gt, ''.join(x)))
    for _ in range(40):
        x = gt[:]; rng.shuffle(x); jg.append((x, ''.join(gw)))
    D = js if a.ctrl == 's' else jg
    jobs = [pooled(blks, t, x) + (None,) for t, x in D]
    with Pool(4) as pool:
        res = pool.map(J, jobs)
    hi = 0
    for i, r in enumerate(res):
        hi += r is not False
        print(f'draw {a.ctrl} {i} J {"unresolved" if r is None else ("fit" if r else "nofit")}')
    print(f'CONTROL {a.ctrl} blocks {use}: fit-or-unresolved {hi}/40 share {hi/40:.3f}; unresolved {sum(r is None for r in res)}')


if __name__ == '__main__':
    sys.exit(main())
