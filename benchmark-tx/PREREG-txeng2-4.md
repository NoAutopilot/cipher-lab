# PREREG TX-ENGINEER-2 round 4 (lane, 9 Oct 2026 17:4x UTC by date -u; pushed BEFORE any read or score; gate per PREREG-txeng2-0 Amendment 2: p < 0.05 on the flagged-excluded eval pool of 26)

## C1 Known-answer control of the kp2 truth recipe (TXP-KP2C; Opus 5.5; cap 2; read-free; TX-RED F3)
Nearest prior: R / TXP-REBUILD and R2 / TXP-KP2 (the recipe itself, scored only on leaves without an independent truth); TX-RED F3.
What is different: the same kp2 recipe is run on dint-f128-print, whose truth comes from the 1882 print (independent of any
gloss read): gloss = the print letters at the aligned positions (f128/print_align), S(L) from key_print as in kp2; report
per scored position whether the kp2 set equals / contains / misses the print truth set, and pass B's err_true under each
truth. Gate (declared): kp2 agrees with the print truth set on >= 90% of positions scored by both, else the kp2 items stay
out of every pool as truth-unknown.
## V1 Verifier look at f152r's three align-conflict flags (TXV-152; Opus 5.5; cap 3; a verifier session, never the solver)
Nearest prior: TX-TRUTH-VERIFY (no.87's 13 flags decided from the clerk-sheet image); TXP-152's RESULTS "treat the three as
truth-doubtful". What is different: a verifier decides L03.32, L04.16, L04.18 from the f.151v slip image (harvest/f152r/
slip_f151v_*.jpg, native) and the printed key, writing FLAG / CORRECT / KEEP with reasons through build_birago152.py's flag
column (never a hand edit of the truth), as TX-TRUTH-VERIFY did. No reading of cipher, no instrument. Outcome: the eval pool's
flagged-excluded count may rise by up to 3; the branch (p < 0.05) does not change.
## X1b Off-sheet detector on the unseen hands, read-free recall only (TXE2-SHEET2; Opus 5.5; cap 4)
Nearest prior: X1 / TXE2-SHEET (0/21 on the Dinteville items), TXE-Q (Spinelli 8 of 14 errors on two off-sheet shapes), TX-SHEET.
What is different: the same detector measured where the sheet gap was observed -- spinelli-c1519-confirm (passZ), f152r and
eval_heldout -- as read-free recall tables (NOT eval looks: no instrument output is scored, only flag/error overlap, as TXE-O's
eval tables); plus a value-blind tile census of the Spinelli filza's other pages on disk (images/beinecke_*) as the grown-sheet
source (new material: sibling leaves). Gate (declared): recall >= 0.5 of Spinelli's errors at <= 15% flagged licenses a PREREG
for the grown-sheet READ as the campaign's first eval look (a separate amendment, reviewed by TX-RED first); below it, X1 is
retired for all hands.
## S4 The sorter feed as a product (TXE2-FEED; Opus 5.5; cap 3; read-free)
Nearest prior: X9 / TXE2-DOUBT (feed), X6 / TXE2-SORT (curve: per-tile only, never cluster propagation), TX-SORTER.
What is different: no experiment -- `focus.tsv` + sorter inputs for eval_heldout, spinelli and f152r from the X9 combo feed
(latt+vote4+selfcons where inputs exist), per tile, with the taxonomy's question per tile, the predicted decisions-to-2% from
the curve, and a one-paragraph note for the orchestrator to publish for the owner (TRANSCRIPTION.md item 7). The lane never
resolves a tile.
## X8b Cost replication (TXE2-COST2; Opus 5.5; cap 6; S5 measurement)
Nearest prior: X8 / TXE2-COST (per-page call 0.30x the cost and better than per-line 2x calls, N=1 reader).
What is different: a second reader per arm on dint-f128-print and both arms on ceppo-f87-S (a second hand), so the S5 figure
rests on N=2 readers x 2 hands; err_true + token counts per arm; paired vs each item's best single pass; no gate.
Costs: 2 + 3 + 4 + 3 + 6 = 18. No eval look in this round.
