#!/usr/bin/env python3
"""FT4ab (account-4, 3 Oct 2026): value readout on FT4aa's locators (PREREG-FT4ab.md, pushed before any run).
121 = s pinned. Pair A = F206 + F216V with {338} released in F206; pair B = F206 + f.266r S1 with {347, 534} released.
Per code, complete enumeration of its feasible chunk under exact fit: solve, read chunk, forbid it, re-solve until
INFEASIBLE (complete) or unresolved (incomplete). Same exact CP-SAT as ft4x_pool.solve_exact (FT4x/FT4z/FT4aa), plus
(i) the read-out code always gets a chunk variable, (ii) the solution loop. Then, for a unique F206-side value, the
witness check: that value pinned in every other block holding the code, each solved alone exactly.
  python3 ft4ab_readout.py [--secondary]
"""
import inspect, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ft4s_seg as fs
import ft4x_pool as fx
import ft4z_pool as fz
from ft4x_pool import solve_exact, PINS, LIMIT

_src = inspect.getsource(fs.solve_pins)
for old, new in [
        ('def solve_pins(toks, text, pins, limit, force=None):', 'def solve_enum(toks, text, pins, limit, code, cap=300):'),
        ('cnt[t] > 1) | set(P))', 'cnt[t] > 1 or t == code) | set(P))'),
        ('m.Add(sum(edv) <= 1)', 'm.Add(sum(edv) == 0)')]:
    assert _src.count(old) == 1, old
    _src = _src.replace(old, new)
head, tail = _src.split('    if force:', 1)
_src = head + '''    inv = {v: k for k, v in chunks.items()}
    s = cp_model.CpSolver()
    s.parameters.max_time_in_seconds = limit
    s.parameters.num_search_workers = 1
    found = []
    for _ in range(cap):
        r = s.Solve(m)
        if r in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            v = s.Value(kc[code]); found.append(inv.get(v, '<empty>')); m.Add(kc[code] != v)
        elif r == cp_model.INFEASIBLE:
            return found, 'complete'
        else:
            return found, 'incomplete (unresolved)'
    return found, 'incomplete (cap)'
'''
_ns = dict(fs.__dict__)
exec(_src, _ns)
solve_enum = _ns['solve_enum']


def main():
    B, _ = fz.blocks()
    B2, (gt, gw) = fx.blocks()
    allb = {'F216V': B['F216V'], 'S1': B['S1'], 'S2': B2['S2'], 'F249': B2['F249'], 'F252R': (gt, ''.join(gw))}
    A, ta = B['F206']
    pins = dict(PINS, **{'121': 's'})
    for pair, partner, rel in (('A', 'F216V', {'338'}), ('B', 'S1', {'347', '534'})):
        t2, x2 = B[partner]
        A2 = [t if t not in rel else 'R' + t for t in A]
        toks, text = fz.join([(A2, ta), (t2, x2)])
        print(f'PAIR {pair} F206+{partner} release {sorted(rel)} pins {sorted(pins)}: exact {solve_exact(toks, text, pins, LIMIT)}', flush=True)
        for c in sorted(rel, key=int):
            for code, side in (('R' + c, 'F206'), (c, partner)):
                found, st = solve_enum(toks, text, pins, LIMIT, code)
                uniq = st == 'complete' and len(found) == 1
                print(f'  readout {code} ({side} side): {st}; feasible {len(found)} {found}; UNIQUE {uniq}', flush=True)
                if uniq and side == 'F206':
                    v = found[0]
                    for k, (t, x) in allb.items():
                        if c not in t:
                            continue
                        print(f'    witness {k}: {c}={v!r} pinned alone exact '
                              f'{fz.lab(solve_exact(t, x, dict(pins, **{c: v}), LIMIT))}', flush=True)



def secondary():
    """Unregistered secondary (not in PREREG-FT4ab): the unique PARTNER-side values pinned alone in every block holding
    the code, F206 included. Diagnostic only; drives no flag."""
    B, _ = fz.blocks()
    B2, (gt, gw) = fx.blocks()
    allb = {'F206': B['F206'], 'F216V': B['F216V'], 'S1': B['S1'], 'S2': B2['S2'], 'F249': B2['F249']}
    pins = dict(PINS, **{'121': 's'})
    for c, v in (('338', 'tou'), ('534', 'che')):
        for k, (t, x) in allb.items():
            if c in t:
                print(f'SECONDARY {c}={v!r} pinned alone in {k}: exact '
                      f'{fz.lab(solve_exact(t, x, dict(pins, **{c: v}), LIMIT))}', flush=True)


if __name__ == '__main__':
    sys.exit(secondary() if sys.argv[1:] == ["--secondary"] else main())
