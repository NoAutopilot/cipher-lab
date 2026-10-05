# LANE-NEAR9 wave 2 (5 Oct 2026, written 05:4x UTC by LANE-NEAR9, account 2 / ytbiz, session_011SW24uoRbdvoyBAWiy9m98)

Common rules, do-not-touch list and model rules: exactly as `.claude/briefs/runs/2026-10-05-ytbiz-near9-wave1.md` header. Pricing: units are
priced per pass (Usage 6 AX-COMP2): each Sonnet read call ~USD 0.6-1.2, the reconciliation one more unit; stop before a unit that would cross 80% of
cap or box. Wave-1 lesson: an Opus worker's start-up reading costs ~2.5 by itself -- do not re-read files you do not need (read only the NOTES
sections named, not the whole NOTES.md).

## N9-BAL2 -- baluze167-davaux-1637: Baluze 168 c511 run 2 vs Tomokiyo F2 known-answer (cap USD 6; box 70 min)
N9-BAL (a4f17155) placed Tomokiyo's fragment F2 ("...si ce n est que le") on c511 (f.247v) run 2, so N8-BAL's F2 overlaps were scored on the
wrong leaves. PREREG first (addendum to the N8-BAL prereg; push before reading): fit sign values on F2 alone at C where the alignment is
unambiguous, hold out F1 (and any other Tomokiyo fragment) as the known-answer test; statistic = agreement of the F2-fitted decode with F1
under one normalized convention vs shuffled-key p99 and letter-order-shuffle p99; positive control = the same procedure on a planted synthetic of
the same N at the measured err_2reader. Crops of c511's 5 runs (`tools/iiif_lines.py`, pasted), 2 blind Sonnet passes + 1 reconciliation, align,
report both numbers. Grades per rule 4; decode --check; gaps refresh. If F1 is not on c511 or the leaf beside it, say so and report F2 fit only (no
test claimed).

## N9-COS2 -- costabili-modena-1491: third-shape split + R1163/R1165 slips by group crops (cap USD 6; box 70 min)
N9-COSV (4de54ee7, AUDIT "Verification of the N8-COS C values") found every A-z/B-o split is a third shape (dash + open loop, reads t at 5
glossed groups) the label list lacks, and that N8-COS boxes p1_u03/p1_u18 cut a g at the left edge. Steps: (1) add the third shape as its own label
in the folder's label list, re-cut p1_u03/p1_u18 wider, re-score the committed passes under the same PREREG-N8-COS (no knob change; say so);
(2) group-level crops of the R1163 and R1165 cipher slips against their clear slips (one DECODE browser login, images never committed), 2 blind
Sonnet passes + reconcile per slip (6 units), under a short PREREG addendum pushed first (same statistic, same floor and null as N8-COS). New
values at C only where both passes and the gloss agree on >= 2 groups. Update key file, NOTES, gaps. No verifier work (that is a later session).

## N9-GRA4 -- fr2980-gramont: fr.3040 f.18r L11-L26 vs Le Grand III pp.454-455, more HASH/A2/Mx occurrences (cap USD 6; box 70 min)
NOTES Verdict "then siblings, fr.3040 f.18r L11-L26 (16 lines, unread) ... under PREREG-N8-GRA3, ~$3" (price per pass: 16 lines in ~2 crop
batches x 2 passes + 1 reconcile = 5 units). Gallica btv1b9059870w canvas 32. Same instrument and gate as N8-GRA3 (no change; say so). Report
score vs both nulls and the planted control; list every HASH, A2, Mx, zb occurrence with the aligned print letter; key a currently-unkeyed sign at C
only under the N8-GRA3 per-code rule. Also settle the check-tool mismatch both N9 Gramont workers flagged: `tools/decode_key.py ciphers/fr2980-gramont
--check` says reading.txt STALE while the folder's decode.py --check exits 0 -- find which is canonical for this folder (decode.json vs decode.py),
fix the stale artefact or the config so both agree, and note it in NOTES (one line). Gaps refresh.

## N9-XMFIX -- tools/key_crossmatch.py: exclude control keys + per-pair null before a lead is posted (cap USD 4; box 50 min)
N9-XM (e83752c4; ROOM flag 05:24) showed all four 5 Oct nightly leads were false: two were clair1161's own shuffled control keys
(key_shuf*_s1.tsv) in the sweep, and the per-pair ~1% gate over ~815 pairs yields ~8 noise hits a night. Implement in the shared tool (Usage 8, no
private copy): (1) exclude key files whose name matches shuf/shuffled/control/null (KEY_EXCLUDE, ~line 79); (2) for any pair over the gate, before it
is reported as a lead, run the per-pair 200-draw in-class shuffled-key p99 and the order-shuffled-target z4gram check (port research/n9xm/
xmatch_pair_null.py into the tool as a function), and report a lead only if it beats both; (3) offline test in tools/tests/ covering one pair that must
be dropped (a shuffled key) and one that must survive (a true key on its own ciphertext), stated in the docstring as scope (8a); (4) re-run the tool
once on the current tree (no network) and paste the lead count before/after. Name the change in SYSTEM.md if the tool's entry there needs it
(system_map_check.py). Do NOT edit any routine or trigger; the nightly job picks the tool up from main.

## N9-MANT -- sachsstaatsarchiv-manteuffel-1712: search the Loc. 694/08 pool for duplicate copies of f.409/f.410 passages (cap USD 4; box 50 min)
NOTES Verdict line. Disk first: the folder's transcriptions/manifest of the 694/08 pool. Method: n-gram (cipher-group 4-gram and 6-gram) search of
every transcribed leaf in the pool against f.409/f.410's cipher, plus the clear/gloss text where transcribed; a duplicate is >= 2 shared 6-grams in
order. Control: the same search against a group-shuffled copy of f.409/f.410 (must give ~0 hits). If the pool has untranscribed leaves, list them
with canvas/image ids and price a pass. Report hits (leaf, span, length) and whether any adds glossed runs (lifts N for the RUN5-MANT gates). Do not
re-decide leaf 0501 (orchestrator decision; leave it). Gaps refresh.

```
baluze167-davaux-1637: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
costabili-modena-1491: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
fr2980-gramont: partial (line 3) -- edition/page or full-text-search citation found within 6 lines
sachsstaatsarchiv-manteuffel-1712: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
```
