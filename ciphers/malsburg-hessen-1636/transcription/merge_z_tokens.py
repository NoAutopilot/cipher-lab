#!/usr/bin/env python3
"""One-off fixup for bMAL16 (f.16): some pass subagents wrote the ambiguous
hooked-diagonal stroke ('z') as a standalone token immediately before its
neighbouring digit (per one literal reading of bMALG's instruction, "not
merged into the next digit"), while others -- and every existing glyph_map.tsv
row -- fused it directly onto the digit ('z6', 'z9', ...). A standalone 'z'
next to a lone digit token is the same manuscript stroke as a fused 'zN'
token, just split into two TSV rows; left unmerged, it costs an alignment
gap/insertion against the other pass's fused reading and cascades into
spurious downstream mismatches for the rest of the line. This merges a bare
'z' (optionally '?'-flagged) with an immediately following bare 1-2 digit
token (optionally '?'-flagged) into one 'zN' token, matching the fused
convention already in glyph_map.tsv, before reconciliation. Renumbers pos
sequentially per line. Does not touch ILLEGIBLE, [PLAIN:...], or a 'z' not
followed by a plain digit token (left as-is for reconciliation as before).
"""
import csv
import re
import sys

DIGIT_RE = re.compile(r"^(\d{1,2})(\?)?$")
Z_RE = re.compile(r"^z(\?)?$")


def merge(rows):
    out = []
    i = 0
    n = len(rows)
    while i < n:
        line, pos, sign = rows[i]
        mz = Z_RE.match(sign)
        if mz and i + 1 < n and rows[i + 1][0] == line:
            nsign = rows[i + 1][2]
            md = DIGIT_RE.match(nsign)
            if md:
                merged = "z" + md.group(1)
                if mz.group(1) or md.group(2):
                    merged += "?"
                out.append([line, None, merged])
                i += 2
                continue
        out.append([line, None, sign])
        i += 1
    # renumber positions per line
    counters = {}
    for row in out:
        line = row[0]
        counters[line] = counters.get(line, 0) + 1
        row[1] = counters[line]
    return out


def main():
    if len(sys.argv) != 3:
        print("usage: merge_z_tokens.py IN.tsv OUT.tsv", file=sys.stderr)
        sys.exit(2)
    inp, outp = sys.argv[1], sys.argv[2]
    with open(inp, newline="") as f:
        r = csv.reader(f, delimiter="\t")
        header = next(r)
        rows = [[row[0], row[1], row[2]] for row in r]
    merged = merge(rows)
    n_merges = len(rows) - len(merged)
    with open(outp, "w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(header)
        for line, pos, sign in merged:
            w.writerow([line, pos, sign])
    print(f"{inp}: {len(rows)} rows -> {len(merged)} rows ({n_merges} z+digit merges)")


if __name__ == "__main__":
    main()
