# PREREG-LINLAB2 (LIN-LAB2, LANE DEFAULT-A4-0235-15, account 4, 15 Oct 2026, written 03:1x UTC by date -u, pushed before any label exists)

Question: does a second blind labeller, a different model from LIN-CAL's (Sonnet), labelling the same committed sheets
`images/rows_hires/sheets/sheet_0255_c3_1.jpg` (sha1 98129ec4...) and `_2.jpg` (sha1 bc9a1664...) under PREREG-LINCAL's
label set and count rule, put "Jus" or "Justa" at FLUSH rank 15 of p.241 col 3 (group 3241315)?

Labeller: one Opus subagent call (model "opus"), both sheets in the one call, told nothing about the key, headwords, ranks,
the target, the earlier labels or that a calibration exists. A Sonnet pass would repeat LIN-CAL's instrument (PREREG-LINCAL:
"the same model on each sheet ... is one instrument"), so the "different model" of NOTES option (b) is taken literally;
the brief's "(Sonnet)" is read as naming LIN-CAL's model. Prompt = PREREG-LINCAL's label definitions verbatim (FLUSH / INDENT /
DROPCAP / OTHER, first word for FLUSH/INDENT, note for OTHER). Labels saved verbatim to `hocr/lincal_labels/0255_c3_lab2.tsv`,
never edited by the worker. Score: `python3 hocr/lincal_score.py --rank 0255_c3_lab2 15` (scorer unchanged).
Caveat fixed now: this second model is NOT itself calibrated on LIN-CAL's held-out columns (cap 1 does not cover 4 more calls);
it is a second reader of a column whose instrument passed with Sonnet, not a second calibrated instrument.

Decision rule (fixed now):
- (A) rank 15 FLUSH word normalises to "jus" exactly (not "justa"...) and no OTHER row inside the span: the count "Jus" is
  reproduced by a second model; with LX-DEC's subagent, LX-QAFIX and LIN-CAL that is four blind readers against LX-DEC's own
  count. The word change justa -> jus for 3241315 is LICENSED; it is not applied in this job (cap 1): propagation (key.tsv,
  reading.txt/reading_tokens.tsv, decode_key --check, AUDIT.md, SO-LINHARES-M0002 row, rule-7 re-derivation, ~$1.5) is named
  as the next step. Grade stays **M** either way (no rule here moves it; a person's count is still the H route).
- (B) rank 15 = "Justa" (decided): the two models disagree; word not changed, licence withheld; person's count decides.
- (C) undecided (OTHER inside the span) or any other word at rank 15: non-test for this question; nothing changes.
Also reported, not scored: whether "Junto," heads col 3 as its own FLUSH row, and the total FLUSH count.
Units: 1 Opus vision call (2 sheets) + session floor; stop at 80% of cap 1 or box (03:06-03:46 UTC, 80% line 03:38).
