# LANE FAMILY jobs (account 2, incarnation DEFAULT-account-2-20261010-0909, "FAMILY-A2p") -- 10 Oct 2026 09:2x UTC, lane orchestrator session_012hc8DarhcArSYEVNFRGewc

Lane brief: .claude/briefs/lane-family.md (+ lane-common-blast.md). Cap 60, box 09:09-19:09 UTC 10 Oct (80% 17:09). Started from STATUS.md
"LANE FAMILY handoff (incarnation DEFAULT-account-2-20261010-0510)" next list and a fresh `next_steps.py --hot-only` read at 09:1x UTC.
Supply check at 09:1x UTC: the in-scope hot rows were re-read in their dated sections. Spent or gated: wallis (Thurloe 2-5 grep done
R8-SPLOOK), Suriname (series screens spent; legends read), Manteuffel (unglossed leaves under ~60 tokens not worth Opus reads),
hessen-daenemark (retired), la-garde (needs pooling/higher-res image), pro3055 (text known), hellen R1049 (no-key-material),
decode-1411 (ASKS 120), jvn/oldenbarnevelt-2442 (ASKS 161). Runnable steps taken below. Gate 0a: SESSION-SWEEP-account-2 stale-claimed
since 5 Oct (prior incarnations proceeded; so do we). Exclusions: eckert-* and Huntington ledgers (LANE LEDGER, account 1, live), Gallica
fetches, Armstrong/Debosnys/Birago, any folder with a ROOM claim < 6 h and no done.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with these
substitutions: address every ROOM line "for LANE FAMILY-A2p (account 2)"; the "Hosts this wave" bullet there is replaced by the one below.
Halfway line: one ROOM line at half the box or half the cap, whichever first (skip if done before). Account 2 is at seven_day
`allowed_warning`: continue (blast rules) and say so in the done line.
Hosts this wave: de-crypt.org ("DECODE": FAM-BNEDEC only, ONE browser login, `tools/decode_browser_login.js`); service.archief.nl /
www.nationaalarchief.nl ("NA": FAM-OBRSG only); the Cremonini pdf host (FAM-COSCREM only, one fetch); digitarq.arquivos.pt only if
FAM-LINCAL finds its images are not on disk (>= 3 s, <= 40 requests).

## Wave 1 (09:2x UTC 10 Oct)

### FAM-LINCAL (Opus, cap 4.5, box 80 min, disk first): antt-linhares-chave, fresh-PREREG re-calibration of the 1897 px per-row labeller
The folder's own "## While waiting (9 Oct 2026)" first bullet, verbatim scope: LIN-COUNT's gate failed only on its "undecided" clause (every
rank exact in 14/14 column-passes), so a NEW pre-registration with that clause rewritten, scored on calibration columns NOT used by LIN-COUNT
(other known-rank groups, fresh leaves at 1897 px), is a legitimate new test; only if it passes are 83/2 and 241/3 labelled. NOT a re-score of
LIN-COUNT's sheets. Read ONLY: NOTES "## While waiting (9 Oct 2026)", the LIN-COUNT section (grep "LIN-COUNT"), its PREREG and scripts, the
Remaining gaps / Escalation, and the column/rank files it cites. Check 1 of prior-work-step.md first (grep ROOM/NOTES for a re-calibration
already run after LIN-COUNT; if found, one ROOM line and stop). PREREG-LINCAL.md pushed in its own commit BEFORE any calibration column is
labelled: which held-out columns (named, with their known ranks and where the rank comes from), the rewritten "undecided" clause (state the
old wording and why the new one is not threshold-shopping: it must be fixed before any held-out score is seen), the pass/fail gate, and what
is labelled on PASS. Images: use the 1897 px files already on disk; if the held-out columns need a fetch, digitarq only, <= 40 requests,
>= 3 s, manifest. Crop step pasted; one column per vision call. On PASS: label 83/2 and 241/3 as the PREREG says, grade M at most (a person's
count is still owed; do not withdraw that ask). On FAIL/non-test: rule 3 third-attempt clause check (this is the second labeller attempt;
log it plainly). NOTES "## LIN-CAL", Remaining gaps / Escalation / Verdict, gaps_check.py. Report what was found and where it was not found;
do not classify novelty. Units: ~4 held-out column calls + 2 target calls + 1 reconciliation at ~0.5 each, plus session floor.

### FAM-BNEDEC (Opus, cap 4, box 80 min, DECODE one login): bne20211-ferdinand-1478, the period decipherment re-cut at its own 29 px pitch
The folder Verdict's cheapest next ("re-cut the period decipherment at its own 29 px pitch and reconcile its passes, ~$2"). Read ONLY NOTES
step 3 of the decipherment work (grep "29 px", ~line 382), "## Remaining gaps", "## Escalation", "## BNE-DECODE re-test" and "## BNE-1180",
and `period_decipherment_passes.tsv`. The committed `decode/IMG_*.png` are 17,947 B placeholders; the owner screenshots are not in this
repository. So: ONE DECODE login (`NODE_PATH=$(npm root -g) node tools/decode_browser_login.js 1172 <scratch> --guess-fullsize --max-files 6`,
the BNE-DECODE command that served full-size R1172 P1/P2 on 9 Oct; confirm by size/sha1 against that section's table, never commit the saved
pages, scrub the account name). Identify which page carries the 15-line period decipherment (the notes say f.1r, item 123 = R1172). Commit
that page (or only the decipherment block region of it, JPEG, under 3 MB) to `images/` with a manifest entry, so later passes read disk.
Crop with `tools/iiif_lines.py --image <file> --out images/dec_lines --debug` at the block's own pitch (tune `--distance` to ~29 px at the
image's scale; paste the command and check the overlay). Two blind passes (Sonnet subagents, one half-block per call, crops only, never the
whole page), then `tools/reconcile_passes.py` and your own reconciliation from the crops, using the cipher's "charles"/"por que" anchors only
as the notes describe. Write `period_decipherment_reconciled.tsv` (line, text, agreement, doubt marks); measure two-pass agreement before
reconciliation and report it. Then, only if the reconciled text has >= 10 lines with doubt below a third, run `tools/print_check.py` on 3-4
distinctive phrases (the Escalation print rung). No cipher transcription (that waits on ASKS 143). NOTES "## BNE-DEC29", Remaining gaps /
Escalation / Verdict, gaps_check.py. Report what was found and where it was not found; do not classify novelty. Units: 2 passes x 2 halves
+ 1 reconciliation at ~0.6 each, plus login/session floor.

### FAM-COSCREM (Opus, cap 2.5, box 60 min, one pdf fetch): costabili-modena-1491, Cremonini 2017 cifrario n.1 vs the R1166 sign inventory
The folder Verdict's cheapest next. Read ONLY NOTES "## COS-CREM" (where the pdf URL and the image pages 10.1-10.2 are named), the R1166
key/inventory files (`key*.tsv`, the N8-COS / N9-COS2 sections' tables), "## Remaining gaps" and "## Escalation". Check 1 first. One fetch
of the pdf to scratch (good-citizen rule, descriptive UA), extract the two pages as images (`pdftoppm` or the pdf skill), commit only the
alphabet crops (`images/cremonini_n1/`, with source, page, licence note in a manifest; short crops, not the article). The cifrario n.1 is a
1486 key (Beatrice to Eleonora) in a 19th-century reconstruction -- a known-keys rung, not this letter's key. Pre-register in
PREREG-COSCREM.md (own commit, before any comparison): the shape-match procedure (blind: list the n.1 signs with their values hidden from the
matcher, match R1166 sign labels to n.1 shapes, then reveal), the statistic (count of R1166 C-grade signs whose matched n.1 value equals our C
value), the control (the same matcher on n.1 with its values permuted 1000x, and/or R1162/R1168 keys as a non-matching design; check the
control CAN differ: rule 3), and the decision. Then, only for values that pass: `tools/decode_key.py ciphers/costabili-modena-1491 --try
CODE=VALUE` per candidate (never writes key.tsv; accepted values stay M). NOTES "## COS-CREM2", Remaining gaps / Escalation / Verdict,
gaps_check.py. Report what was found and where it was not found; do not classify novelty.

### FAM-OBRSG (Sonnet, cap 2.5, box 75 min, NA <= 120 requests + one dbnl retry): oldenbarnevelt-brederode-1605, States-side trace and Den Tex
Two cheap steps the folder names: (1) the Escalation retry rung: one retry of the Den Tex biography on dbnl.org from this fresh container
(it TLS-failed twice on 25 Sept 2026); if it answers, grep it (once fetched to scratch) for Brederode 1604-1605, "cijfer", "chiffre",
"Stettin", and report the hits with page refs; one request plus one retry after a pause at most. (2) the Remaining gap "States-side trace of
the 17 Oct 1604 letter (the griffier's papers, R.A. S.G. 5888/5968 files)": read NOTES "## OBRED-DP" for what was named, then the NA 1.01.02
EAD (the copy the folder already has, or one request) for the S.G. lias inventory numbers that hold incoming letters from Germany / Brederode
for Oct 1604 - mid 1605; for each digitised one, METS + IIIF 400 px contact-sheet screen of the scans for those months exactly as OBRED-S3
(three disk controls per sheet including CTRL-PS = scan 187 reduced; sheet key opened only after calls are written; 1200 px re-look at
most 6). NA take/release lines; >= 2.0 s apart. Output `images/sg_<inv>_screen.tsv` and the table of which inventory numbers were looked at.
A numeral hit: transcribe nothing; 1200 px crop committed and one ROOM flag line for the lane. NOTES "## OBRED-SG", Remaining gaps /
Escalation / Verdict, gaps_check.py. Report what was found and where it was not found; do not classify novelty.

## Wave 1 results (09:4x UTC, costs by get_session)
FAM-LINCAL 4.76: PREREG-LINCAL first, held-out 4/4 PASS; 83/2 r19 Cagar, 241/3 r15 Jus labelled, both stay M (a person's count of 241/3
decides jus/justa). FAM-BNEDEC 5.89: decipherment re-cut (pitch ~24 px with --follow-slope), 2 blind passes 26.6% agreement, reconciled 12/15
lines doubt < 1/3 (M); print rung: "reposo al regno de navarra" in Paz y Melia 1914 (IA elcronistaalonso0000unse, gbooks 7q9CAAAAYAAJ), page
unread. FAM-COSCREM 2.34: Cremonini n.1 1/11 vs null p95 2, FAIL (different design). FAM-OBRSG 1.42: Den Tex no cipher note; the
Resolutien footnote numbers are old numbering; the Hoogduytschlandt liassen (6034/6035) are not digitised.

## Wave 2 (09:5x UTC 10 Oct)

### FAM-BNEPRINT (Sonnet, cap 1.5, box 50 min, Google Books API + be-api only): bne20211-ferdinand-1478, is the decipherment's text in Paz y Melia 1914?
Prior-work check 5 for the reconciled period decipherment. Read ONLY NOTES "## BNE-DEC29" (FAM-BNEDEC's section: the phrases, print-check.tsv),
`period_decipherment_reconciled.tsv`, "## Remaining gaps" and "## Escalation". Question: does Paz y Melia, *El cronista Alonso de Palencia*
(1914) print this letter (Ferdinand, Trujillo, Dec 1478) or its deciphered passage, and on which page? Route (no page images from the cloud:
books.google page view is blocked; IA is lending/print-disabled): (1) Google Books API volume 7q9CAAAAYAAJ (`&country=US&key=$GOOGLE_BOOKS_KEY`,
never print the key): read its accessInfo (viewability; a full-view volume may expose a text or pdf link -- try it once); then `volumes?q=`
searches restricted to that volume id for 8-10 distinct phrases from the reconciled lines (lowest doubt first, 3-5 words each, original
spelling and one normalised variant) and record each searchInfo.textSnippet; (2) be-api fts on `elcronistaalonso0000unse` for the same phrases
(snippets only; page_num is not a page). Positive control: the known hit "reposo al regno de navarra" must return; negative control: 2 phrases
from an unrelated 1478 Castilian letter text (or the decipherment's lines shuffled into nonsense 4-grams) must not. Score: share of the
decipherment's phrases found, against the controls. Outcome lines: "printed (N of M phrases, snippets quoted, page if any snippet shows it)",
"partly quoted", or "one phrase only". If a person's page read is still needed to settle it, draft ONE LOCAL-QUEUE.tsv row (rebase first;
the row format from the file's header; the IA reader page, the phrases to check) rather than an ASKS row. Do NOT classify novelty and do not
edit AUDIT.md: write the finding into NOTES "## BNE-PRINT", update the print rung / Remaining gaps / Verdict, gaps_check.py, and one ROOM flag
line asking the lane for a verifier if >= 3 phrases hit. Requests: googleapis <= 25, be-api <= 15, 1.5 s apart.
