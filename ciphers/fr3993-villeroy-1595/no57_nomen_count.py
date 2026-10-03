#!/usr/bin/env python3
"""A1B-VILL-M step 1 (3 Oct 2026): count the target's 3-figure groups that fall in no.57's nomenclator range 100-353,
under both transcriptions (Bourdeau's bourdeau/ct_*.txt via strips_score.tokens(); A1B-VILL-TX2 tx2/passB.tsv, '?'
stripped). Two counts per transcription: (a) greedy combined parse, left to right inside each digit run: three digit
tokens reading 100-353 = one nomenclator code (tokens consumed 3), else advance; (b) digit runs of exactly three
figures reading 100-353 (the stricter 'group' sense). Share = tokens consumed / all tokens. The brief's stop rule:
under ~5 pct of tokens -> a nomenclator read cannot move the letter score.
Usage: python3 no57_nomen_count.py [--check]   (writes no57_nomen_count.tsv; --check exits 1 if stale)"""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import strips_score as ss
import no57_score as ns
DIG = ss.DIG

def runs(lines):
    for toks in lines:
        cur = []
        for t in toks + ["|"]:
            if t in DIG: cur.append(t)
            else:
                if cur: yield cur
                cur = []

def val(seq): return int("".join(seq).replace("o", "0"))

def count(lines):
    ntok = sum(len(t) for t in lines); ndig = sum(1 for t in lines for x in t if x in DIG)
    greedy, exact3, rl = 0, 0, {}
    for r in runs(lines):
        rl[len(r)] = rl.get(len(r), 0) + 1
        if len(r) == 3 and r[0] != "o" and 100 <= val(r) <= 353: exact3 += 1
        i = 0
        while i + 3 <= len(r):
            if r[i] != "o" and 100 <= val(r[i:i + 3]) <= 353: greedy += 1; i += 3
            else: i += 1
    return ntok, ndig, greedy, exact3, rl

def main():
    out = ["transcription\ttokens\tdigit_tokens\tgreedy_3fig_100_353\tgreedy_token_share\texact3_runs_100_353\texact3_token_share\trun_length_hist"]
    for name, lines in [("bourdeau", ss.tokens()), ("tx2_passB", ns.passb_tokens())]:
        n, d, g, e, rl = count(lines)
        out.append(f"{name}\t{n}\t{d}\t{g}\t{3*g/n:.3f}\t{e}\t{3*e/n:.3f}\t" + ",".join(f"{k}:{rl[k]}" for k in sorted(rl)))
    txt = "\n".join(out) + "\n"
    p = HERE / "no57_nomen_count.tsv"
    if "--check" in sys.argv:
        if not p.exists() or p.read_text() != txt: print("STALE"); sys.exit(1)
        print("up to date"); return
    p.write_text(txt); print(txt, end="")

if __name__ == "__main__": main()
