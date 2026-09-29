#!/usr/bin/env python3
"""H262 (runner 10 session_0148wt8Aokh6aZEdJsXzYiZX, 29 Sept 2026): hand-off table for VERIFY-F61-V9 -- every f.61 token in the meter's unread-or-null band
(CA, C6, LOOPBAR, CROSS, LL: 25 of 99) and the two still-wider classes (4PI x2, OTHER x2), one row per token, with the class's evidence in one cell and
the result files in another; Tomokiyo's markup character where the token falls inside one of his five spans (the F61-CAL DP under key v6's f.61 reading,
as H259). Descriptive: nothing here is a value or a merge; the class evidence is the runner's summary of the named steps, for the verifier to check
against the files.  H306 (runner 12 session_012eShPsWwW3quuzzUNV7nW5, 29 Sept 2026): one fixed NOTE row for L02's opening mark (pos 0, before the decode file's L02 1 PHI; not in the decode, which follows read_call_U pass 2's "Il"), carrying H302/H304/H305 for the verifier; band "note", counts unchanged.  H301 (runner 11 session_01RNzUvRTqBTAw7BukhKyKBU, 29 Sept 2026): one NOTE row for CH -- keyed e/m in the meter (two-way band), not in the band's 25, but a Tomokiyo dash class on f.61 (H281) whose letterform is the clear h (H298, n = 1); band "note", so the 25 + 4 counts VERIFY-F61-V9 endorsed do not move.  python3 f61_null_band.py [--check]"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.abspath(f"{HERE}/../scripts"))
from build_key_v6 import load_key_v6
from f61crib import align, load_read, load_spans
from f61crib4 import split_lines
from sbs_relabel import relabel
EV = {
 "CA": ("null drawn as the letter a: letterform of the scribe's clear a in two blind sorts, 10/10 CA with the text a's, cipher PHI/C43 0/12, non-a letters 0/6 (H256, H260); cipher hand by weight, baseline and spacing, 5 of 6 (H63); no letter in Tomokiyo's markup, 4/4 in-span, words complete without it (H259); his markup treats it as a null (H44); VERIFY-F61-V9 replicated the letterform with its own tiles and fresh readers (CA 10/10 with the clear a, cipher 0/11, permutation p 0.0013) and endorsed it as a published null in the letter a's form, f.61 reading only, never a pooled cell (the glossed leaves' CA rows unchanged)",
        "family/h256_ca_text_result.txt family/h260_ca_text_result.txt scripts/f61ca_result.txt family/h259_ca_span_result.txt scripts/f61_positions_all.tsv verify_v9/v9_ca_sort_result.txt AUDIT.md#VERIFY-F61-V9"),
 "C6": ("unread on f.61: Tomokiyo's dash at all 5 in-span positions (H259, H261); the pooled C6 = e (3 glossed tokens, f.101r/f.188r) gains and loses no span letter and f.61's plain 6 showed no glyph link to the glossed delta-shaped C6 (H237) -- rule-4 conflict row in HYPOTHESES.md; sits inside cipher runs, not at word boundaries (H253: 0 of 3 by a clear word); partial match to his word-code 'pour' drawing only (H247)",
        "family/h261_c6_markup_result.txt family/h237_c6_glyph_result.txt scripts/f61positions_result.txt family/h259_ca_span_result.txt HYPOTHESES.md"),
 "LOOPBAR": ("unread: the DP skips its one in-span token (L03 12) rather than pair it; glossed e on f.101r (1) and u on f.188r (1) -- one token per leaf with different letters, so no glyph-sort cell (H258 dropped); H253 places L03 2 next to a clear word",
        "family/h232_unread_census_result.txt family/h259_ca_span_result.txt scripts/f61_positions_all.tsv"),
 "CROSS": ("unread: Tomokiyo's dash at both in-span tokens (L01 1, L07 10; H259/H261); his reconstructed table's row-1 drawing (a cross with a stroke rising upper right) sits in the a/n column, a lead only under F61-CAL's mislabelling caveat (H247); glossed p once on f.101r (H232)",
        "family/h261_c6_markup_result.txt family/h232_unread_census_result.txt keys/key_mayenne_1592.tsv"),
 "LL": ("unread: Tomokiyo's dash at its one token (L05 16; H259); glossed e once on f.188r (H232); matches no table drawing (H247)",
        "family/h259_ca_span_result.txt family/h232_unread_census_result.txt"),
 "4PI": ("wider: f.61's two 4PI are a 4 over a Pi, a different sign from the 4-head hash that f.101r/f.108r code as 4PI (VERIFY-F61-V8 endorses the split); L11 9 reads n in Tomokiyo's span S5 (a/n grade M on his letter alone), L01 12 has no source (V8)",
        "AUDIT.md#VERIFY-F61-V8 family/h240_4head_testkey_result.txt family/h233_4pi_shape_result.txt"),
 "OTHER": ("wider: L02 2 a Pi with a double bar and no 4 (the base of the 4-over-Pi), L04 2 an S/8 loop into a b/d form, perhaps a handwriting abbreviation (H238); no atlas class with a period letter matches",
        "scripts/read_call_U.tsv NOTES.md#H238"),
}
NOTE = {
 "CH": ("note, not in the band: keyed e/m pooled (f.101r e 3, f.188r m 3 -- two leaves' letters merged, rule-4 conflict row HYPOTHESES.md H289); on f.61 its one token carries Tomokiyo's dash (H281) in 'les choses sont a [LOOPSTEM1] [CH] trop avancees', complete French without it (Correction, H295); letterform of the scribe's clear h in one blind sort, 1/1 with the 3 text h's, PHI/C43 0/4, at n = 1 flagged (H298); a blind positional reader listed it as the clear letter h (H297) -- an h-shaped mark reading as nothing on f.61, the CA pattern at n = 1; stays keyed in the meter until a verifier rules; on the family leaves the class is a letter inside words (H288/H291)",
        "family/h298_ca_text_result.txt family/passes/h298_sort.tsv family/f61_dash_need.tsv scripts/f61positions_L05B_result.txt family/f61_nulls_as_letters.tsv HYPOTHESES.md"),
}
L02START = ("note, not in the band and not in the decode: L02's opening mark, read_call_U pass 1 LL ('ll-shaped pair of stems ... could be handwritten Il') vs pass 2 'Il' (handwriting; the decode follows pass 2); two blind letterform sorts by fresh readers (H302, H304) each put it in a group of its own with f.61's LL (L05 16) -- 'two tall long-s-like stems side by side' -- apart from the clear 'Il'/I, the single l's and PHI/C43, but both sorts missed their own control gate on one tile (CONTROL FAIL), so descriptive only; no same-hand ll-only control exists on disk (H305); if a verifier took it as LL, the band's LL would be 2 tokens (a recount for the verifier, not applied)",
            "family/h302_ll_text_result.txt family/h304_ll_pair_result.txt family/passes/h302_sort.tsv family/passes/h304_sort.tsv family/h305_ll_census.tsv scripts/read_call_U.tsv scripts/passU2_classes.tsv")
def main():
    key = load_key_v6(f61=True); lines = split_lines(load_read()); relabel(lines); mk = {}
    for s, l, m in load_spans():
        pairs = align(m, lines[l], key)[1]; pj = {j: i for i, j in pairs}
        if pairs:
            for j in range(min(pj), max(pj) + 1): mk[(l, j + 1)] = (s, m[pj[j]] if j in pj else "(skipped)")
    d = list(csv.DictReader(open(f"{HERE}/f61_decode_period_v4_frac0.1_sbs.tsv"), delimiter="\t"))
    rows = ["line\tpos\tclass\tband\tv6_letters\tspan\ttomokiyo\tclass_evidence\tfiles"]; n = {"unread-or-null": 0, "wider": 0}
    for r in d:
        c = r["class"]
        if c not in EV and c not in NOTE: continue
        if c in NOTE: band = "note"; ev = NOTE[c]
        else: band = "wider" if c in ("4PI", "OTHER") else "unread-or-null"; ev = EV[c]
        n[band] = n.get(band, 0) + 1
        s, ch = mk.get((r["line"], int(r["pos"])), ("", ""))
        rows.append(f"{r['line']}\t{r['pos']}\t{c}\t{band}\t{r['period_letters']}\t{s}\t{ch}\t{ev[0]}\t{ev[1]}")
    rows.append("L02\t0\tLL?\tnote\t-\t\t\t" + L02START[0] + "\t" + L02START[1]); n["note"] = n.get("note", 0) + 1
    open(f"{HERE}/f61_null_band.tsv", "w").write("\n".join(rows) + "\n")
    txt = f"tokens: unread-or-null {n['unread-or-null']} (CA 10, C6 8, LOOPBAR 4, CROSS 2, LL 1 expected 25), wider {n['wider']} (4PI 2, OTHER 2); in a span with his character: {sum(1 for r in rows[1:] if r.split(chr(9))[6] and r.split(chr(9))[3] != 'note')}; note rows {n.get('note', 0)} (CH 1, keyed e/m, dash on f.61, H298/H301; L02 opening mark 1, LL or 'Il', H302-H306)\n"
    p = f"{HERE}/f61_null_band_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt and open(f"{HERE}/f61_null_band.tsv").read() == "\n".join(rows) + "\n"; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
