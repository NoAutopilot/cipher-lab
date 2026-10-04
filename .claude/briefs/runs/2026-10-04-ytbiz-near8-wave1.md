# LANE-NEAR8 wave 1 (4 Oct 2026, written 16:2x UTC by LANE-NEAR8, account 2 / ytbiz, session_01HcZrXzQiZna9e3nfwzFqh6)

Lane brief: `.claude/briefs/runs/2026-10-04-acct3-lane-near8.md`. Theme (research/MARY-STUART-METHOD-2026-10-04.md): known plaintext --
a period clear copy, decipherment or gloss -- tested with ONE pre-registered known-answer test per target, control first (RUN5-PIS3 shape).
Common rules: the "Common to every job below" section of `.claude/briefs/runs/2026-10-04-ytbiz-near4-wave1.md`, with "LANE-NEAR4" read as
"LANE-NEAR8" everywhere (claims, done line addressed "for LANE-NEAR8 (account 2)"). Model: you run on Opus 5.5; transcription subagents
Sonnet (TX-FABLE FAIL 4 Oct 15:58: Fable is not used for reads). Subagent readers RETURN text; you write files. One target, one step; stop
when met (Usage 7); a follow-up is a one-line suggestion in NOTES. Do not touch fr16045-pisany-rome-1585, nevers-birago-fr3251-1572,
armstrong-madison-1808, ceppo-nevers-fr3251-1570s, or any owner sorter file. Do not edit status lines, status.json, STATUS.md: flag instead.
Never write a dollar figure for yourself. No novelty words (rule 10).

Intake gates (pasted by LANE-NEAR8, 16:1x UTC, all rc=0):
`fr2980-gramont: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`
`fr3151-seure-1558: blocked (line 1) -- already terminal, nothing to gate`
`fr15575-syllabic-1592-95: blocked (line 1) -- already terminal, nothing to gate`
`birago-fr3252-1571-72: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
`baluze167-davaux-1637: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
`thurloe-printed: partial (line 2) -- edition/page or full-text-search citation found within 6 lines`

## N8-GRA -- fr2980-gramont: fr.3038 no.19 period decipherment as known plaintext (cap USD 5; box 60 min)
The folder's Verdict step (A2-GRA6; A2-GRA7 was interrupted with no commit -- check `git log origin/main -- ciphers/fr2980-gramont` first):
locate fr.3038 no.19 (period decipherment of Gramont's 27 Feb 1530 Villandry letter, printed Le Grand III pp.391-393) and its cipher original
on Gallica (`tools/gallica_folio.py`, BnF finding aid). Before any transcription, check the cipher original's shared signs against key.tsv
(same key family?); if not on Gallica or not this family, stop and record where it was looked. If both exist: PREREG first (statistic = share of
cipher tokens whose key.tsv value agrees with the aligned decipherment, null = shuffled-plaintext / shuffled-key p99, positive control =
planted alignment at the transcription's measured err_2reader), then crops + 2 blind passes + 1 reconciliation (3 units ~USD 1.5 each), align
(`tools/interlinear_align.py` or the folder's aligner), report both numbers; a PASS keys shared open codes at grade C (key.tsv, decode --check,
flag VERIFIER WANTED). Gaps refresh + gaps_check.

## N8-SEU -- fr3151-seure-1558: 44-clear vs 43-cipher alignment, nomenclator model (cap USD 5; box 60 min)
The Verdict step (SEURE-KP, 3 Oct): f85R clear L01-08 (item 44) vs f81R cipher L01-20 (item 43) with word/name codes allowed
(interlinear_align numeral floor for the 12-100 numerals), a MATCHED nomenclator control (synthetic nomenclator cipher of the same N, symbol
count and code share, at the measured reader error -- design matched, rule 3 Salviati paragraph), and a second f81R reader (one Sonnet pass on
the existing kp/ crops; err_2reader against the first). PREREG before the statistic (S* or the aligner's score vs shuffled-clear p95 as SEURE-KP,
plus the control's own power). Report target, null and control side by side. Gaps refresh + gaps_check.

## N8-NV05 -- fr15575-syllabic-1592-95: f.228 L01-L04 full-width gloss re-read and re-score (cap USD 3; box 45 min)
NV05E's registered FAIL (S 0.430 vs shuffled p99 0.186, 0.60 floor) stands. The named step: a prereg ADDENDUM (pushed first; same statistic,
same floor, same null, plus the one change: the gloss read full-width from native crops by two blind Sonnet passes + reconcile, normalized to
one convention with the decode -- rule 3 PX-BRODEC paragraph) then re-score. Grades per VERIFY-NV05 (syllables from the period sheet are H).
AUDIT.md exists (N0): if the reading changes, add a dated "Revision after AUDIT" note (rule 10 propagation) and carry it into any
SECOND-OPINIONS-QUEUE row for this target. If the gate passes, price the next 4-line batch in the Verdict; do not start it. Gaps refresh.

## N8-BIRNUM -- birago-fr3252-1571-72: f.100r + f.119 dotted groups and 1x/5x/8x units as nomenclator codes against the clear text (cap USD 3; box 45 min; disk only)
The Verdict step (~$1). Read NOTES sections BIRAGO-NUM, -NUM2, -NUM3, -NUM4, -NUM-TOOLS, -NUM-SCOUT first; the joint anneal and spelled-crib tests
are retired/powerless -- this is a different instrument (code reading from the clear context around each run). PREREG first: which units are
candidate codes, what clear-context evidence licenses a meaning, and a control that can fail (the same procedure on shuffled run positions or
on the clear text of a different letter, scored the same way). Any meaning is grade M unless a second occurrence agrees (then S with the
control). Never touch nevers-birago-fr3251-1572 files or the sorter. Gaps refresh + gaps_check.

## N8-BAL -- baluze167-davaux-1637: 168 f.246-247 bare passage, known-answer against Tomokiyo's quoted fragments (cap USD 4; box 60 min)
The Verdict step (A3V3-BALB). Tomokiyo (louisxiii.htm, on disk under sources/ or the folder) quotes fragments of this passage ("de ne consentir
aucune suspension d'armes ..."). PREREG first: the known-answer statistic (token agreement of your decode with his quoted words where they
overlap, normalized to one convention) vs a shuffled-key null p99, gate fixed before reading. Crops of c508-510 cipher lines (`tools/iiif_lines.py`,
pasted), a letter-sign glossary for this hand built from the leaf's own glossed letters if any (NOT from his quote -- the quote is the test),
2 blind passes + reconcile (~USD 1.2/unit), decode_key --check. Report agreement vs null; graded counts. Do not start 170 ff.228-230.

## N8-THUR -- thurloe-printed: one-vote boundary test v3 on the remaining three cipher pages + two decipherment paragraphs from the image (cap USD 9; box 90 min)
The Verdict step (A3V2-THURBT). PREREG v3 stands unchanged (same gate: K coverage >= 60% and CONFIRM >= 80%, W control); this is the same
instrument on new material, so state in NOTES that it is NOT a fourth tuning (no knob changes) -- the djvu-OCR instrument stays retired. Units:
per page 2 blind passes (line crops only, `tools/iiif_lines.py` pasted) + 1 reconciliation; per decipherment paragraph 1 read + your check.
State the unit count x per-pass estimate in NOTES before the first call; stop before a unit that crosses 80%. Report pooled v3 (old 2 pages
+ new) and new-only numbers beside the control. Key/grade changes only as PREREG v3 allows; decode --check; gaps refresh.
