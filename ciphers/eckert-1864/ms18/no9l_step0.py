#!/usr/bin/env python3
"""NO9-L step 0 (10 Oct 2026, account 1, LANE LEDGER-11): the Step-0 ruling of LANE LEDGER-10 Wave 3 on the nine No. 9 leftovers, under each of No. 1/2/9.
(a) ordered LCS of the decoded content words vs the holder transcription of THAT entry's block(s); (b) same vs the block shuffled, 20 draws, p95;
(c) decoded words absent from the block, split into key meanings ([..] expansions) and plain. Functions are those of ms18/step0_ordered.py (exec of its definitions).
Controls: step0_ordered.tsv already ran E74/E378/E381 (must hit) and the transposed constructions (must not); not rerun here. Disk only."""
import os, sys, re, json, random
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); sys.path.insert(0, T)
src = open(os.path.join(HERE, "step0_ordered.py")).read(); exec(src[:src.index("EXTRA =")].replace("__file__", repr(os.path.join(HERE, "step0_ordered.py"))))
import decode
keys = {n: decode.load_key(__import__("pathlib").Path(T)/f) for n, f in [("no1","key.md"),("no2","key-no2.md"),("no9","key-no9.md")]}
ROWS = "9699/0 9694/2 9845/0 9679/0 9725/1 9762/1 9761/0 9862/1 9770/2".split()
PAGES = {"9725/1": [9725, 9726]}
print("row\tbook\tH\ta\tlcs/n\tb_p95\thit\tc_n\tc_key\tc_plain")
for (header, lines), row in zip(decode.load_ciphertext(__import__("pathlib").Path(HERE)/"no9l_entries.txt"), ROWS):
    text = decode.entry_text(lines); ptr = int(row.split("/")[0]); pages = PAGES.get(row, [ptr])
    for n in ("no9", "no1", "no2"):
        line, st = decode.decode_entry(text, keys[n]); line = line.replace("\n", " ")
        allw, codew = body(line)
        if n == "no9" or True:
            r = measure(row, allw, codew, windows(blocks(pages)), sum(map(ord, row)))
            print(f"{row}\t{n}\t{st['H']}\t{r['a']:.3f}\t{r['lcs']}/{r['n']}\t{r['b']:.3f}\t{'HIT' if r['hit'] else '-'}\t{r['c']}\t{' '.join(r['ck'])}\t{' '.join(r['cp'])}")
