#!/usr/bin/env python3
"""FT4s post hoc (not registered): per 722 value, the no-edit model and every single edit class that fits S1 (10 s each)."""
from multiprocessing import Pool
import ft4s_seg as s
t, x, _ = s.segment1()
for v in ['ti', 'i']:
    pins = dict(s.PINS, **{'722': v})
    cls = s.edit_classes(t, pins)
    with Pool(4) as p:
        e0 = s.solve_pins(t, x, pins, 30)
        res = p.map(s._force, [(t, x, pins, 10, f) for f in cls])
    ok = [f for f, r in zip(cls, res) if r]
    print(f'722={v}: no-edit fit {e0}; edit classes fitting {len(ok)} of {len(cls)}; timeouts {sum(r is None for r in res)}; '
          + ' '.join(f'{k}{i}({t[i] if i < len(t) else "end"})' for k, i in ok), flush=True)
