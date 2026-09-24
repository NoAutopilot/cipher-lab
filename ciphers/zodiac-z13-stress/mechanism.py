#!/usr/bin/env python3
"""The ARTHUR LA keyboard mechanism (CLAIM.md) as explicit, parameterised code.

Board: QWERTY letter rows, staggered (row 1 offset +0.25 key, row 2 +0.75).
Track: T = QWERTYUIOPASDFGHJKLZXCVBNM, index 0 (Q) .. 25 (M); the poster's "reverse track" is T read backwards.

Global parameters (Params):
  move      physical move for a 'moved' letter: UR, UL, DR, DL (poster: UR, A->W and N->J)
  npass     keys passed before taking the next (poster: 1)
  slide_dir track direction for pass-and-take after a move/slide: +1 toward M, -1 toward Q (poster: +1)
  count     eight-count length on each 8-like symbol (poster: 8)
  start1    True = the starting key counts as 1 (poster), False = it counts as 0
  count_dir -1 = the poster's reverse track (toward Q), +1 = toward M
  boundary  'reflect' at Q and M (poster) or 'wrap'
  chain_from which cipher position seeds the eight-count chain (poster: 3, the N)

Per-position operations (ops), one per cipher letter position:
  L  copy the letter          ('A = A anchor')
  M  move, then pass npass and take next
  S  pass npass and take next, no move ('E -> pass R -> T')
  LM emit the letter AND its moved result (poster's first A gives A and R)
  X  emit nothing (K and the middle M 'confirm'; the chain seed N; the terminal M)
Chain: from chain_from's letter, for each 8-like symbol: count, then pass npass in the current direction and take
next; emit; the output seeds the next count. Reflection flips the current direction.
"""
import argparse, sys
from dataclasses import dataclass

T = "QWERTYUIOPASDFGHJKLZXCVBNM"
ROWS = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
OFF = [0.0, 0.25, 0.75]
POS = {c: (r, i + OFF[r]) for r, row in enumerate(ROWS) for i, c in enumerate(row)}


@dataclass(frozen=True)
class Params:
    move: str = "UR"
    npass: int = 1
    slide_dir: int = 1
    count: int = 8
    start1: bool = True
    count_dir: int = -1
    boundary: str = "reflect"
    chain_from: int = 3


POSTER = Params()
POSTER_OPS = {1: "LM", 2: "S", 3: "X", 6: "X", 8: "X", 11: "M", 12: "L", 13: "X"}


def phys_move(c, move):
    r, x = POS[c]
    rr = r - 1 if move[0] == "U" else r + 1
    if not 0 <= rr < 3:
        return None
    cands = [(k, xx) for k, (r2, xx) in POS.items() if r2 == rr]
    if move[1] == "R":
        cands = [(k, xx) for k, xx in cands if x < xx <= x + 1]
    else:
        cands = [(k, xx) for k, xx in cands if x - 1 <= xx < x]
    return min(cands, key=lambda t: abs(t[1] - x))[0] if cands else None


def step(i, d, n, boundary):
    """Move n keys from index i in direction d; return (index, direction)."""
    for _ in range(n):
        j = i + d
        if 0 <= j < 26:
            i = j
        elif boundary == "wrap":
            i = j % 26
        else:
            d = -d
            i = i + d
    return i, d


def take(c, p, d):
    i, d = step(T.index(c), d, p.npass + 1, p.boundary)
    return T[i], d


def op_out(c, op, p):
    if op == "X":
        return ""
    if op == "L":
        return c
    if op == "S":
        return take(c, p, p.slide_dir)[0]
    m = phys_move(c, p.move)
    if m is None:
        return None
    moved = take(m, p, p.slide_dir)[0]
    return moved if op == "M" else c + moved


def chain(seed, n8, p):
    out, c, d = [], seed, p.count_dir
    for _ in range(n8):
        i, d = step(T.index(c), d, p.count - 1 if p.start1 else p.count, p.boundary)
        i, d = step(i, d, p.npass + 1, p.boundary)
        c = T[i]
        out.append(c)
    return out


def run(tokens, p=POSTER, ops=None, trace=False):
    """tokens: list of 13 cipher tokens. Returns the output string, or None if an op is impossible."""
    ops = POSTER_OPS if ops is None else ops
    n8 = [k for k, t in enumerate(tokens, 1) if t == "8"]
    ch = chain(tokens[p.chain_from - 1], len(n8), p)
    out = []
    for k, t in enumerate(tokens, 1):
        if t == "8":
            s = ch[n8.index(k)]
        elif t.isalpha():
            s = op_out(t, ops.get(k, "X"), p)
            if s is None:
                return None
        else:
            s = ""
        if trace:
            print(f"{k:2d} {t}  op={'8-count' if t == '8' else (ops.get(k, 'X') if t.isalpha() else '-'):7s} -> {s}")
        out.append(s)
    return "".join(out)


def load(path="ciphertext.txt"):
    return [l for l in open(path) if l.strip() and not l.startswith("#")][0].split()


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="exit 1 unless the poster's rules give ARTHURLA")
    a = ap.parse_args()
    z = load()
    o = run(z, trace=True)
    print("output:", o)
    if a.check and o != "ARTHURLA":
        sys.exit(1)
