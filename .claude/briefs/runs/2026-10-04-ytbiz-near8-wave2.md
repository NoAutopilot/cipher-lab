# LANE-NEAR8 wave 2 (4 Oct 2026, written 16:4x UTC by LANE-NEAR8, account 2 / ytbiz, session_01HcZrXzQiZna9e3nfwzFqh6)

Common rules: everything above the first job heading of `.claude/briefs/runs/2026-10-04-ytbiz-near8-wave1.md` (its own common section,
the off-limits list, Opus worker + Sonnet readers, rule-10 words, no self-reported dollar figure). Done lines "for LANE-NEAR8 (account 2)".
Intake gates (pasted by LANE-NEAR8, 16:4x UTC, all rc=0):
`fr2980-gramont: partial (line 3) -- edition/page or full-text-search citation found within 6 lines` (16:1x, unchanged)
`fr15575-syllabic-1592-95: blocked (line 1) -- already terminal, nothing to gate` (status line flagged stale by N8-NV05; not yours to edit)
`fr16142-noailles-constantinople-1571: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
`costabili-modena-1491: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`

## N8-GRA2 -- fr2980-gramont: Le Grand III p.399 vs fr.3040 f.18 no.6 as known plaintext (cap USD 5; box 60 min)
The Verdict step N8-GRA wrote (NOTES "N8-GRA"): check that Le Grand III p.399 (MDZ bsb10280117) prints Gramont's Boulogne 27/28 March 1530
letter; locate its cipher original fr.3040 f.18 no.6 on Gallica (N8-GRA: IIIF answered 404 ark-unknown on most canvases, `.highres` worked);
check its signs against key.tsv before transcribing. If the pair exists and is this family: PREREG first (statistic = share of cipher tokens
whose key.tsv value agrees with the aligned print; nulls shuffled-plaintext and shuffled-key p99; positive control planted at the measured
err_2reader), crops + 2 blind passes + reconcile (~USD 1.5/unit), align, both numbers; PASS keys shared open codes at C (decode --check, flag
VERIFIER WANTED). Print wording vs letter: normalise both to one convention (rule 3 PX-BRODEC). If not, stop and record where looked.

## N8-NV05B -- fr15575-syllabic-1592-95: f.228 L05-L08 batch against its own gloss (cap USD 8; box 75 min)
The Verdict step N8-NV05 priced (5 units: crops, 2 cipher + 2 gloss passes, reconcile). Same PREREG-ADDENDUM-N8 statistic, floor 0.60 and
value-shuffled null, registered for L05-L08 in a short addendum pushed before any read (and the line-placement rule from crop geometry that
N8-NV05 needed for GB). Decode with the no.54 sheet (syllables H, letter signs I per VERIFY-NV05). Report L05-L08 and pooled L01-L08 beside
the null. AUDIT.md is N0: add a dated revision note if the reading grows; SECOND-OPINIONS-QUEUE row if one exists. Do not start L09+.

## N8-NOX -- fr16142-noailles-constantinople-1571: pre-registered basin test of the locked-on alignment runs (cap USD 2.5; box 45 min; disk only)
The Verdict step (~$1): NOX-CONFIRM found 8/20 nearest single merges also lock onto Dupuy 221R-226R. Test: do the six locked runs learn one common
key (pairwise agreement of key_learned over shared signs) vs a matched null (the same agreement among runs on a shuffled-Dupuy or non-locking
alignment, same N)? PREREG pushed before computing. Then, only if it passes, the key_learned vs key.tsv (Tomokiyo) agreement (the next gap) with
its own null. Report both numbers. Gaps refresh + gaps_check.

## N8-COS -- costabili-modena-1491: group-level crops on R1166 P1-P2 against the period decipherment for the C grade (cap USD 6; box 75 min)
NOTES RUN3-COSK, RUN3-COSK2 and the gaps: line-crop blind passes are retired for C (two attempts); this is a different instrument -- crops of one
cipher group with its gloss above, cut by the reconciled boxes. One DECODE login (`tools/decode_browser_login.js`, images to scratch, never
committed; scrub the account name). PREREG first (same gate as RUN3-COSK2: pass agreement vs 0.430 floor and the shuffle control). Units: per
page 2 blind passes + 1 reconciliation (~USD 1.2 each), stated in NOTES before the first call. Also the Vestigia image map for 2955/2977 (~1) only
if cap allows after the main step. Key changes at C only on PASS; decode --check; gaps refresh.
