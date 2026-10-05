#!/usr/bin/env python3
"""DEF1-1411 frozen tables (PREREG-DEF1-1411.md): T = GAPS146 frozen residue table; T21r = T with residue 21 = r.
Importable: tables() -> {"T": tab, "T21r": tab}, tab in residue/rule.py format. Prints both."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "residue"))
import rule  # noqa: E402


def tables():
    t = rule.table()
    t21 = dict(t); t21[21] = ("r", "prereg-DEF1-1411", t[21][2])
    return {"T": t, "T21r": t21}


if __name__ == "__main__":
    for k, tab in tables().items():
        print(k, " ".join(f"{r}{tab[r][0]}" for r in range(24)))
