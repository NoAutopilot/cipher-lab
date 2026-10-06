#!/usr/bin/env python3
"""R10-ECK62T (6 Oct 2026; PREREG-ECK62-S2.md items 1): write the split2 flip and flip-control rows files mechanically.

Usage: ec18_fliprows.py --split2 [--write | --check]
  Reads s2/align_free_entries.tsv and s2/align_free_rows.tsv (committed, no network). PREREG-ECK62-FLIP rule 1 selects
  scored >= 5, agree_rate <= 0.10, conflict >= 1 -> s2/align_flip_rows.tsv; rule 2's control (scored >= 5, agree_rate
  >= 0.75) -> s2/align_flipctl_rows.tsv. Book swapped 1 <-> 2, source 'flip-<source>'. --check exits 1 if either is stale.
  Split2 only: the legacy align_flip_rows.tsv also carries 9991.571 from before the R7B-ECK62 carry, so rule 1 on today's
  legacy file does not reproduce it, and the legacy rows files stay as committed.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ec18  # noqa: E402


def main(argv):
    if not ec18.SPLIT2:
        sys.exit("split2 only (see docstring)")
    rd = lambda f: [l.split("\t") for l in ec18.src(f).read_text().splitlines()]
    fe, fr = rd("align_free_entries.tsv"), rd("align_free_rows.tsv")
    rows = {r[0]: r for r in fr[1:]}
    sel = [r[0] for r in fe[1:] if int(r[5]) >= 5 and float(r[11]) <= 0.10 and int(r[7]) >= 1]
    ctl = [r[0] for r in fe[1:] if int(r[5]) >= 5 and float(r[11]) >= 0.75]
    flip = lambda i: [i, {"1": "2", "2": "1"}[rows[i][1]], "flip-" + rows[i][2]] + rows[i][3:]
    want = {f"align_{k}_rows.tsv": "\n".join(["\t".join(fr[0])] + ["\t".join(flip(i)) for i in ids]) + "\n"
            for k, ids in (("flip", sel), ("flipctl", ctl))}
    stale = 0
    for f, txt in want.items():
        if "--write" in argv:
            (ec18.OUT / f).write_text(txt)
        elif not (ec18.OUT / f).exists() or (ec18.OUT / f).read_text() != txt:
            print("STALE", f)
            stale = 1
    print(f"flip {len(sel)}, flipctl {len(ctl)}")
    return stale


if __name__ == "__main__":
    sys.exit(main(sys.argv))
