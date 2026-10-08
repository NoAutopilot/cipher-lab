# Siblings and ledger round 3 (account-3 orchestrator, 8 Oct 2026 09:5x UTC). default-lane common tail; Opus 5.5 lane orchestrators.

Why: the board stands at 58 counted (75 by 14 Oct is the owner's benchmark). Every one-audit N3+ D2+ item already has its second
audit; the twelve two-audit D1 items need more reading, not more auditing. New counted items now come only from NEW readings of
UNGLOSSED leaves under keys already in hand. A leaf with a period decipherment on it reads N0 (rule 10), so glossed siblings do
not move the board; use their glosses as C-grade known answers, not as targets. Source list: SIBLINGS-2026-10-08.tsv
(SUCCESS-SIBS, 8 Oct; p and cost are the compiler's estimates, not claims). Depth rulings follow
.claude/briefs/runs/2026-10-08-acct3-depth-bar.md. Expected counted gain is modest (0.1-0.3 per unit); report honestly either way.

Common to both lanes:
- Before spawning: check this account's usage bar; on allowed_warning write one ROOM line and stop.
- Paste `python3 tools/intake_gate_check.py <target>` before any deep-work worker brief; nonzero exit blocks it.
- Per unit: transcription with the mandatory crop step (`tools/iiif_lines.py ... --out`, paste the command), two blind
  passes + one reconciliation priced per pass (Usage 6), decode with `tools/decode_key.py <t> --check`, and the matched control
  (shuffled-key or shuffled-order, one that CAN differ for the statistic, rule 3) before any reading is claimed.
- A reading that beats its control goes to a SEPARATE first-verifier session (CLAUDE.md verifier template: N-class, key source,
  depth per the depth bar, AUDIT.md, status.json row, SO row at N3+). Never verify in the session that read. After a first audit
  at N3+ D2+, add one WORK-QUEUE row for its second audit on a different account (shape: AUD2-LS-C in
  .claude/briefs/runs/2026-10-08-acct3-ledger2.md) and name it in ROOM for the account-3 orchestrator.
- Workers report what was found and where it was not found; do not classify novelty. Rule 10 wording only.
- Stop before a unit that would cross 80% of cap or box. Hand-off in STATUS.md, LEDGER rows, no orphaned triggers at close.

## SIBS-READ (account 1), lane orchestrator, cap $45, box 8 h: unglossed siblings under keys in hand
Units, in this order (skip any whose NOTES show it already run since 8 Oct 04:45 UTC; read the target's "## Siblings" section):
1. fr16104-vivonne-spain-1572: fr.16104 ff.157-159v, 5 Sept 1572 ("sans le dechiffrement", same pool), key.tsv/key_tomokiyo.tsv via
   the viv54 pipeline, shuffled-key control. ~$3.
2. lodewijk-van-nassau-1573-74: WVO 5810 (6 Jan 1574) with key_full_v2.tsv/key_5801.tsv, shuffled-key control (5811 is printed:
   skip it). ~$1.5.
3. august-van-saksen-1561-64: WVO 53 page 2 unread cipher block, key_53.tsv. ~$3.
4. fr3621-dinteville-1592: the fr.3621 letters of 5 and 13 July 1592 ("not checked") and fr3631 no.27 f.28 (14 June 1593), each
   with f130/key_dk.tsv and a shuffled-key control; check length before reading. ~$3 each.
5. hellen-frederick-1752: transcribe the R4376 (f.56, 1754) table, test it on R1049 (7 Sept 1756) with control. ~$8.
6. ceppo-nevers-fr3251-1570s: fr.4715 f.20 (unnamed to Nevers, Mar 1571): count cipher signs first; key rank test only if long
   enough. ~$2.
Then the first verifiers for whatever cleared its control.

## ST-LEDGER-3 (account 2), lane orchestrator, cap $40, box 8 h: the Eckert leftovers ST-LEDGER-2 named
Read the ST-LEDGER-2 handoff in STATUS.md (around line 6150) and ciphers/eckert-1864/NOTES.md first. Work, in order:
(a) the "10" book check for E69 and E75 (~$1.5); (b) the 1865 key-book check (~$1); (c) Cipher No. 9 entries of mssEC 19
(decode_no9.py, ~43 guessed, ~$2); (d) remaining unread 1862-ledger entries (mssEC 15) with the eckert-1862 key (~$5);
(e) mssEC 18, the parallel sent ledger (Huntington object 10074): fetch the 21-22 Apr 1864 pages via the documented
CISOSEARCHALL route, transcribe, apply key.md, with the same pre-filter as mssEC 19 (~$6); (f) object 5952 (Fort Monroe 1864-65)
only if (a)-(e) run dry. Readers Sonnet where the filter makes them mechanical; first verifiers Opus, separate sessions, LS-V
pattern, then WORK-QUEUE second-audit rows as above. An entry whose clear text is in print (OR, the Huntington transcription,
the press of the day) is N1/N2: record it and move on.

# Round 3b (account-3 orchestrator, 8 Oct 2026 11:4x UTC by date -u), from SIBS-READ's, ST-LEDGER-3's and DEFAULT-account-4's hand-ups

Common rules as above (usage bar first; intake gate pasted; crops command pasted; control first; separate verifier sessions;
depth bar file; rule 10 wording; stop before 80% of cap or box; STATUS.md/LEDGER/WORK-QUEUE at close).

## VIV52 (account 1), lane orchestrator, cap $35, box 6 h: fr.16104 piece 52, Vivonne to the Queen, 5 Sept 1572
The lead SIBS-READ handed up: ff.164r-168r (canvases 178-182), full cipher, about 270 lines, no gloss seen at 1200 px, "not in
Gachard" (ciphers/fr16104-vivonne-spain-1572/NOTES.md lines 329, 374, 391). Steps: (1) premise, ~$1: Gachard II's entry for this
letter, and the leaves after f.165 for a "dechiffré" or clear copy; stop and report if either exists. (2) crops with
`tools/iiif_lines.py` from native Gallica regions (paste the command), two blind passes + one reconciliation per canvas, priced per
pass. (3) decode with key.tsv / key_tomokiyo.tsv through the viv54 pipeline, `--check`, shuffled-key control, fr16 judge.
(4) a separate first-verifier session if the reading beats its control. The existing Vivonne fragments are D1; say so if this
letter reads no further than they do.

## AUD1-B167 (account 2), verifier, Opus, cap $5, box 60 min: first audit of baluze167-davaux-1637, 170 f.229r-v
Reading by D4-B167, re-derived exactly by D4V-B167 (H106/M258/I1/U1, fr17 judge PASS). You are separate from both. Verifier
template (CLAUDE.md): N-class with logged search, key source (Tomokiyo's published letter table: `published`, credited), depth per
the depth bar with the verifier's own sentence if D2, AUDIT.md, status.json row, SO row at N3+.

## B167-228 (account 4), solver, Opus, cap $3, box 45 min: provisional decode of 170 f.228r-v with the f.229 letter values
NOTES.md line 947's cheapest next. Crops already re-cut and re-passed (D1-BAL170, D1-BAL170B). decode_key.py --check, shuffled-key
control, fr17 judge. Report what was found and where it was not found; do not classify novelty.

## LS3-V86 (account 2), verifier, Opus, cap $3, box 45 min: first audit of eckert-1864 E86 and O9-BC (LS3-R18b)
Separate from LS3-R18b, LS3-V18a and LS3-V18b. Same LS-V pattern; pre-filter OR ser. I, II and III and ORN (LS3-V18a found an entry in
ser. III that earlier audits missed), the Huntington public transcription and the press of the day.

## SIBS-PREMISE (account 4), Sonnet worker, cap $3, box 45 min: premise-pass SIBLINGS-2026-10-08.tsv
SIBS-READ found 6 of 7 checked rows' state column wrong. Disk only, no network: for every row with p_counted >= 0.1, read the
target's NOTES.md, AUDIT.md and Siblings section and set state to one of read / glossed / printed / unread-unglossed /
needs-image / not-located, quoting the NOTES line. Write SIBLINGS-2026-10-08.tsv in place (shrink guard) and append the ten best
unread-unglossed rows, with keys in hand, to the "Round 3b" section of this brief's file as a "## Next sibling round" list.

## AUD2-B167 (account 1 or 3, never 2 or 4), verifier, Opus, cap $5, box 60 min: second adversarial audit of baluze167-davaux-1637, 170 f.229r-v
Added by AUD1-B167 (account 2), 8 Oct 2026, after its first audit (N3, D2, key published). A session that has not touched this target:
not D4-B167/D4V-B167 (account 4) nor AUD1-B167 (account 2). Read AUDIT.md '## AUDIT (AUD1-B167)' and try to break it: (1) search for a
prior print or decipherment of the 25 Aug 1640 Chavigny despatch where AUD1 did not (the BnF archivesetmanuscrits record for Baluze 170,
Acta Pacis Westphalicae Serie I Bd 1, Grotius Briefwisseling Aug-Sept 1640, Semantic Scholar keyed, the three phrases that got HTTP 503
from Google Books in aud1b167/print-check.tsv); (2) re-rule depth under .claude/briefs/runs/2026-10-08-acct3-depth-bar.md, in particular
whether word codes 8: leur and 10: les meet the code clause; (3) check one spot of the reconciled ciphertext against the crops
(images/crops/b170f229v_L02, L12-L13). Write '## AUDIT 2 (AUD2-B167)' in AUDIT.md, update the status.json row (audit_status), and mark
the WORK-QUEUE row done. Rule 10 wording only.

## Next sibling round (SIBS-PREMISE, account 4, 8 Oct 2026, 12:40 UTC by date -u)
Premise pass on SIBLINGS-2026-10-08.tsv done for all 32 rows with p_counted >= 0.1 (disk only; state + NOTES line quoted in the
evidence column; rows below 0.1 left as they were, not premise-passed). Result: 12 glossed/read/printed rows that the old column called
`unread`, 9 `unread-unglossed` rows remain (fewer than ten exist at p >= 0.1). Ranked by yield_per_usd, key in hand marked:
1. eckert-1864 Cipher No.9 remainder (~33 of ~43), $2, p 0.20, key-no9.md + decode_no9.py in hand (O9-AH..BC already read/audited; pre-filter OR I-III, ORN, Huntington transcription first).
2. eckert-1864 Cipher No.2 headquarters entries (~180 of ~201 unread), $4, p 0.35, mssEC 47 key (H) in hand.
3. eckert-1864 Cipher No.1 remainder (~540 of ~583 guessed), $5, p 0.35, key.md in hand; most are N1/N2 in print, so filter first.
4. ceppo-nevers fr.4702 f.36r, $3, p 0.15, Ceppo-Nevers key in hand (ranks 1/201 on both passes); no gloss on f.36r (f.37 has it); next: reconcile the 136 '?' splits against the f.37 gloss, then judge (currently FAIL, 514 M).
5. lodewijk wvo-11008-certain-1572, $2, p 0.10, printed 1572 Orange-Nassau table (key_nepveu, numerals = multiples of 3) in hand; 54 numerals only, so small.
6. sachsstaatsarchiv-manteuffel Loc. 694/09 (302 frames) + uninventoried 694/08, $5, p 0.15, Krauske table (codes 1-401) in hand; first extend frame_classify.
7. eckert-1864 mssEC 18 (413 images, most unopened), $6, p 0.25, key.md in hand; same pre-filter.
8. hellen-frederick-1752 R1049, $8, p 0.10, NO key in hand (R4376 failed controls; R4377/R4379 Potsdam sheets untried, images not on disk).
9. hellen-frederick-1752 1763 cluster, $4, p 0.10, NO key in hand (HEL-T2 controls below gate; needs a 1763 table, Add MS 32276 R4381-R4408).
Also open but not a sibling-table row: fr.16105 ink piece 38 (4 June 1573 second copy), $1, p 0.08, Tomokiyo key in hand (SIBS-READ already handed up fr.16104 piece 52 as VIV52).
