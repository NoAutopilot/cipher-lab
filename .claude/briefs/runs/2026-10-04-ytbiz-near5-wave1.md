# LANE-NEAR5 wave 1 (4 Oct 2026, written 06:2x UTC by LANE-NEAR5, account 2 / ytbiz, session_012hS4hPgLzzQfHLW7vuq5KC)

Common rules: the "Common to every job below" section of `.claude/briefs/runs/2026-10-04-ytbiz-near4-wave1.md`, with
"LANE-NEAR4" read as "LANE-NEAR5" everywhere (claims, done line addressed "for LANE-NEAR5 (account 2)").

## N5-VIVK -- fr16104-vivonne-spain-1572: known-plaintext test of the 4 June 1573 cipher letter against its clerk decipherment (Opus; cap USD 30; box 170 min)
Facts (NOTES.md N4-VIV2/N4-VIV3; read those two sections first). fr.16105 = ark btv1b9009663p; canvas c shows f.(c-4)v left and
f.(c-3)r right (`tools/gallica_folio.py` fit, residual 0). Cipher letter ink 40: cipher block f.100 (lower) - f.103r. Its clerk
decipherment ink 41 ("dechiffre de la precedente"): ff.104r-108v; f.104r illegible, ff.104v-108v legible plain French; it ends on
f.108v "... de ses necessitez". Tomokiyo (sources/cryptiana/web/henryiii.htm, "Vivonne in Spain") publishes the key used April
1572-Nov 1574 as images henryiii_Vivonne1.png ... Vivonne6.png (+ VivonneSig.png) at cryptiana.web.fc2.com, not on disk.
Intake gate: `python3 tools/intake_gate_check.py fr16104-vivonne-spain-1572` rc=0 (06:1x UTC, pasted by LANE-NEAR5).

Units (CLAUDE.md Usage 6, ~USD 1.5 per Sonnet one-page call): cipher f.102r, f.102v, f.103r (canvas 105 right, 106 left, 106 right)
x (2 blind passes + 1 reconciliation) = 9 units; decipherment pages that carry the plaintext of those three cipher pages -- by
proportion about ff.106v-108v (canvas 110 left - 112 left, 5 pages; confirm the start by finding the plaintext of f.102r's first
cipher words, widen by at most one page) x 2 blind passes, reconcile in the worker's own read = 10-12 units; Tomokiyo key images to
key data 2 units. ~22 units, ~USD 33 ceiling; stop before a unit that would cross 80% of the cap or box.

Steps.
1. Key on disk: fetch henryiii_Vivonne1..6.png and VivonneSig.png once (1.5 s apart, descriptive UA) into sources/cryptiana/web/
   (unmodified snapshots); turn the alphabet/nomenclator into `ciphers/fr16104-vivonne-spain-1572/key_tomokiyo.tsv` (code,
   meaning, source image, note). This is a `published` key (Tomokiyo), credited in NOTES.md. It is also the transcription
   reference sheet: give the subagents the sign inventory from it.
2. Crops: `tools/iiif_lines.py --ark btv1b9009663p --canvas N --region ... --out ciphers/fr16104-vivonne-spain-1572/images --debug`
   per page, command and output pasted in NOTES before the first subagent call; check the debug overlay. Subagents get crop paths only.
3. Cipher transcription: two blind Sonnet passes per page, `tools/reconcile_passes.py`, reconciliation by you from the crops; report
   err_2reader per page (TRANSCRIPTION.md row 2). Decipherment: two blind passes per page, merged by you; record abbreviations as
   written and keep a normalized version (lowercase, letters only, u/v and i/j folded, abbreviations expanded) -- rule 3's
   PX-BRODEC lesson: compare normalized to normalized only.
4. PREREG (push `ciphers/fr16104-vivonne-spain-1572/PREREG-N5VIVK.md` BEFORE any decode of f.103r is compared with any plaintext):
   held-out page = cipher f.103r and the plaintext span after the training span's end. Statistic: letter agreement of the decoded
   held-out page against that plaintext span after a fixed alignment (name the tool and its settings, e.g. tools/stream_align.py or
   `interlinear_align.py stream` band/step), normalized as step 3.
   Arm A (C, independent): `tools/interlinear_align.py stream` on f.102r+f.102v vs their plaintext from a FLAT start (no --prior),
   key frozen, decode f.103r with it (codes unseen in training = unread).
   Arm B (published key): decode f.103r with key_tomokiyo.tsv, no training.
   Nulls for each arm, 200 draws each: (i) shuffled key (meanings permuted across the arm's codes), (ii) shuffled order (f.103r token
   order permuted, same key). Both can move the statistic. Pass for an arm: real > the 95th percentile of BOTH nulls, and you state
   in the PREREG the expected ceiling check (a null whose median is >= 0.95 voids the arm). Report both arms side by side, plus the
   per-code agreement of Arm A's frozen key with key_tomokiyo.tsv on codes with >= 3 training occurrences.
5. If at least one arm passes: write key.tsv for this target (Tomokiyo values, with C counts from Arm A where they agree; disagreements
   listed, never settled by majority -- rule 4), and STOP there (applying it to fr.16104 ff.157-159v is wave 2, not yours). If both
   fail: log the numbers in HYPOTHESES.md as a known-plaintext test, name the next step, stop.
NOTES "N5-VIVK" section, Remaining gaps / Escalation refresh, gaps_check OK line. Report what was found and where it was not found;
do not classify novelty. Gallica requests one at a time, >= 2 s apart; count requests per host.
