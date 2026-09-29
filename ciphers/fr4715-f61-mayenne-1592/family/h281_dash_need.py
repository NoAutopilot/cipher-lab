#!/usr/bin/env python3
"""H281 (runner 10 session_0148wt8Aokh6aZEdJsXzYiZX, 29 Sept 2026), script-only: one row per dash in Tomokiyo's five spans (tomokiyo_spans.tsv) -- the sign
under it by the H259 alignment (scripts/f61crib.align under key v6's f.61 reading), our band for that class, and whether the French of his own phrase
needs a letter at the dash: 'no' when the span's letters with the dashes removed already spell his phrase (S1 avec, S2 estcapable, S3 tropavancees,
S4a+S4b jalousie au beau-pere), 'yes' for S5, where 'melentenoit' is not French and the lexicon wants 'melentendoit' (H268). Writes
f61_dash_need.tsv for the null-band table. Descriptive.  python3 h281_dash_need.py [--check]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); S = os.path.abspath(f"{HERE}/../scripts"); sys.path.insert(0, HERE); sys.path.insert(0, S)
from build_key_v6 import load_key_v6
from f61crib import align, load_read, load_spans
from f61crib4 import split_lines
from sbs_relabel import relabel
NEED = {"S1": "no (avec complete)", "S2": "no (estcapable complete)", "S3": "no (tropavancees complete)", "S4a": "no (jalousie complete)", "S4b": "no (au beau pere complete)", "S5": "YES (melentenoit is not French; entendoit, H268)"}
NULLBAND = {"CA", "C6", "LOOPBAR", "CROSS", "LL"}
key = load_key_v6(f61=True); lines = split_lines(load_read()); relabel(lines)
rows = ["span\tline\tpos\tclass\tv6_letters\tband\tfrench_needs_letter"]; n = 0
for s, l, m in load_spans():
    pairs = align(m, lines[l], key)[1]; i2j = {i: j for i, j in pairs}
    for i, ch in enumerate(m):
        if ch != "-": continue
        n += 1; j = i2j.get(i)
        if j is None: rows.append(f"{s}\t{l}\t-\t(no sign paired)\t-\t-\t{NEED[s]}"); continue
        c = lines[l][j]; v = "/".join(key.get(c, ())) or "-"
        band = "unread-or-null" if c in NULLBAND else ("keyed " + v)
        rows.append(f"{s}\t{l}\t{j + 1}\t{c}\t{v}\t{band}\t{NEED[s]}")
open(f"{HERE}/f61_dash_need.tsv", "w").write("\n".join(rows) + "\n")
keyed = [r for r in rows[1:] if "keyed" in r]
txt = f"dashes {n}; paired with a null-band class {sum(1 for r in rows[1:] if 'unread-or-null' in r)}; paired with a keyed class {len(keyed)}: " + "; ".join(r.split(chr(9))[1] + " " + r.split(chr(9))[2] + " " + r.split(chr(9))[3] for r in keyed) + f"; unpaired {sum(1 for r in rows[1:] if 'no sign paired' in r)}\n"
p = f"{HERE}/h281_dash_need_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(p) and open(p).read() == txt and open(f"{HERE}/f61_dash_need.tsv").read() == "\n".join(rows) + "\n"; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(p, "w").write(txt); print(txt, end=""); print("\n".join(rows))
