#!/usr/bin/env python3
"""Known-answer check of a keyed decode against the clerk's clear decipherment sheet (GAPS4-nevers-birago, 2 Oct 2026).

The laid-in sheet on canvas 182 (harvest/f179r_sheet/decipherment_sheet.tsv, read by eye at native resolution) carries the
period decipherment of the whole no.87 cipher passage. This script decodes a reconciled sign sequence with a sign-id map
(the printed 1572 key, or the GAPS3 fitted one), folds both decode and sheet span to a-z (word codes expanded, u/v and i/j
merged, the clerk's dots and commas dropped), aligns them (difflib longest-matching blocks) and reports the share of
decoded letters that sit in a matched block. Rule 3 control: the same statistic for N value-shuffled keys (values moved
between sign ids, same homophone counts -- the decode_control.py shuffle), so a key that merely shares letter
frequencies with Italian cannot match the sheet by chance at the real key's rate.
  python3 align_sheet.py SEQ.tsv --map sign_id_map_1572_fit.json --sheet-lines L01-L03 [--sheet-cut "da loro"]
     [--shuffles 200] [--seed 1] [--show]
--sheet-lines: the sheet lines the SEQ covers; --sheet-cut: drop the sheet text from this phrase on (the span ends before it);
--sheet-from: keep the sheet text from this phrase on.
"""
import argparse, csv, difflib, json, random, re, statistics
from pathlib import Path
HERE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser(); ap.add_argument("seq"); ap.add_argument("--map", default=str(HERE / "sign_id_map_1572_fit.json"))
ap.add_argument("--sheet", default=str(HERE / "f179r_sheet/decipherment_sheet.tsv")); ap.add_argument("--sheet-lines", required=True)
ap.add_argument("--sheet-cut"); ap.add_argument("--sheet-from"); ap.add_argument("--shuffles", type=int, default=200)
ap.add_argument("--seed", type=int, default=1); ap.add_argument("--show", action="store_true")
a = ap.parse_args()
m = {e["id"]: e["value"] for e in json.load(open(a.map))}
seq = [r["sign_id"].strip() for r in csv.DictReader(open(a.seq), delimiter="\t")]
lo, hi = (int(x.lstrip("L")) for x in a.sheet_lines.split("-"))
sheet = " ".join(r["text"] for r in csv.DictReader(open(a.sheet), delimiter="\t") if lo <= int(r["line"].lstrip("L")) <= hi)
sheet = re.sub(r"\[[^\]]*\]", "", sheet)
if a.sheet_from:
    sheet = sheet[sheet.index(a.sheet_from):]
if a.sheet_cut:
    sheet = sheet[:sheet.index(a.sheet_cut)]
sheet = sheet.replace("car.la", "carmagnola").replace("ma.ta", "maesta")

def fold(s):
    s = s.lower().replace("v", "u").replace("j", "i").replace("&", "et")
    return re.sub(r"[^a-z]", "", s)

def decode(seq, m):
    return "".join(m.get(s, "") for s in seq if m.get(s) not in (None, "null"))

def matched(dec, clear):
    sm = difflib.SequenceMatcher(None, dec, clear, autojunk=False)
    return sum(b.size for b in sm.get_matching_blocks() if b.size >= 3) / max(1, len(dec))

clear = fold(sheet)
real_dec = fold(decode(seq, m)); real = matched(real_dec, clear)
ids = list(m); vals = [m[i] for i in ids]; rng = random.Random(a.seed); sh = []
for _ in range(a.shuffles):
    rng.shuffle(vals); sh.append(matched(fold(decode(seq, dict(zip(ids, vals)))), clear))
mu, sd = statistics.mean(sh), statistics.pstdev(sh)
rank = 1 + sum(1 for x in sh if x >= real)
print(f"signs {len(seq)}, decoded letters {len(real_dec)}, sheet letters {len(clear)}; real key matched (blocks >= 3) "
      f"{real:.3f}; {a.shuffles} value-shuffled keys mean {mu:.3f} max {max(sh):.3f}; rank {rank} of {a.shuffles + 1}; "
      f"z {(real - mu) / sd if sd else 0:.2f}")
if a.show:
    print("DECODE:", real_dec); print("SHEET :", clear)
    sm = difflib.SequenceMatcher(None, real_dec, clear, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            print(f"  {op:8s} decode[{i1}:{i2}]={real_dec[i1:i2]!r:20s} sheet[{j1}:{j2}]={clear[j1:j2]!r}")
