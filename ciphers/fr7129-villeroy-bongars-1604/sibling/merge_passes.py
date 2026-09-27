#!/usr/bin/env python3
"""Mechanical merge of two blind transcription passes per line (VB-KP, 27 Sept 2026; same rule as VB-DECODE2).

  python3 merge_passes.py PASSDIR OUT.tsv --lines 2 3 4 5 6 --side r

PASSDIR holds L<n>A and L<n>B, each one line 'id/conf id/conf ...' (conf h/m/l), the subagents' raw answers.
Rule: tokens where A and B agree are kept (agree=AB); over a stretch where they differ, the pass with the higher mean
confidence (h=3, m=2, l=1; ties go to A) is taken (agree=A or B); a token found by one pass only is kept only if that
pass marked it h. No eye reconciliation. Prints per-line agreement (A=B tokens over merged tokens).
"""
import argparse
import difflib
from pathlib import Path

W = {"h": 3, "m": 2, "l": 1}


def read(p):
    out = []
    for t in Path(p).read_text().split():
        tok, _, c = t.rpartition("/")
        out.append((tok, c if c in W else "l"))
    return out


def merge(a, b):
    sm = difflib.SequenceMatcher(a=[t for t, _ in a], b=[t for t, _ in b], autojunk=False)
    out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            out += [(t, "AB") for t, _ in a[i1:i2]]
        elif op == "replace":
            sa = sum(W[c] for _, c in a[i1:i2]) / (i2 - i1)
            sb = sum(W[c] for _, c in b[j1:j2]) / (j2 - j1)
            out += [(t, "A") for t, _ in a[i1:i2]] if sa >= sb else [(t, "B") for t, _ in b[j1:j2]]
        elif op == "delete":
            out += [(t, "A") for t, c in a[i1:i2] if c == "h"]
        else:
            out += [(t, "B") for t, c in b[j1:j2] if c == "h"]
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("passdir")
    ap.add_argument("out")
    ap.add_argument("--lines", nargs="+", type=int, required=True)
    ap.add_argument("--side", default="r")
    ap.add_argument("--header", default="")
    a = ap.parse_args()
    rows, tot_ab, tot = [], 0, 0
    for n in a.lines:
        pa, pb = read(Path(a.passdir) / f"L{n}A"), read(Path(a.passdir) / f"L{n}B")
        m = merge(pa, pb)
        ab = sum(1 for _, g in m if g == "AB")
        tot_ab, tot = tot_ab + ab, tot + len(m)
        print(f"line {n}: A {len(pa)} / B {len(pb)} tokens, merged {len(m)}, A=B {ab} ({100 * ab / len(m):.0f}%)")
        rows += [f"{a.side}\t{n}\t{i}\t{t}\t{g}" for i, (t, g) in enumerate(m, 1)]
    print(f"all: merged {tot}, A=B {tot_ab} ({100 * tot_ab / tot:.0f}%)")
    Path(a.out).write_text(a.header + "side\tline\tpos\ttoken\tagree\n" + "\n".join(rows) + "\n")


if __name__ == "__main__":
    main()
