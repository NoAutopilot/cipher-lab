# TXE-Q results: the confirm item, read ONCE with today's pipeline (9 Oct 2026, 08:26-08:37 UTC by date -u)

PREREG `benchmark-tx/txeng/confirm/PREREG.md` (b122ccf46, pushed before any read). Raw reads committed before scoring:
passA d63e0cfd5, passB c6c1d316b, reconciliation 6deea7a0a, adjudication + passZ 13cc414cd. One look, no re-read after.

## Headline (this leaf only; never a figure for the hand beyond it)
```
spinelli-c1519-confirm [confirm] err_true 0.088 (17/193) 95% 0.056-0.137 | wrong 12 deleted 2 inserted 3 | excluded 66 | lines missing 0
  top confusions (truth value <- read): r<-SIX x4, h<-<deleted> x2, u<-JHOOK x2, t<-TEE x1, i<-EIGHT x1, e<-SIX x1, p<-THREE x1, s<-JHOOK x1
paired passZ_pipeline.tsv vs committed.tsv: 193 common scored signs; base wrong 4, output wrong 14; fixed 1, broken 11; sign test p = 0.0063
```
(`--label-map collapse_map.tsv`, the pre-registered notation collapse of key split codes to their v3 parent codes.)
Unmapped, same file: err_true 0.518 (100/193) 95% 0.448-0.588 -- notation only (the v3 sheet has no split codes; top
"confusions" are e<-SEVEN/NINE, a/t<-HOOK, i<-PHI, all parent codes of the truth's split cells).
committed.tsv is the reference sequence (home advantage: it errs only on its own conflicts), so the paired line says the
pipeline is behind the folder's settled transcription by 10 positions net, not that it is behind truth by chance.

## Single passes (reported, not a second look at the pipeline)
- passA alone: err_true 0.104 (20/193) 95% 0.068-0.155; vs passZ fixed 0 / broken 3, p 0.25 (A wrote NEW: for the shapes the
  adjudicator later named SIX/PHI/JHOOK).
- passB alone: err_true 0.083 (16/193) 95% 0.052-0.130; vs passZ fixed 1 / broken 0, p 1.0 -- the adjudicator's one net loss
  is p1c_L01 col 3 (A TEE, B HOOK; adjudicated TEE; truth t's H code is not TEE).
- Pair agreement 236/252 = 93.7% (H29c's Opus pair on the folder's montages: 93.1%).

## Taxonomy (tools/tx_taxonomy.py, mapped; score/taxonomy.md)
14 wrong-or-deleted (+3 inserted). By cause, from the confusion pairs:
- **Sheet inventory gap, 8**: the "tall l with a bottom loop" shape read SIX (truth r x4, e x1) and the long-s / J shape read JHOOK
  (truth u x2, s x1). passA flagged both as NEW (5 + 3 positions); the v3 sheet has no row for them (atlas v2 had RHO; the
  key's split cells sit under other parents). The readers saw the gap; the vocabulary, not the eye, lost these.
- **Missed sign, 2** (h deleted, L01.14, L03.25, both passes).
- **Shape misread, 4** (t<-TEE, i<-EIGHT, p<-THREE, n<-PHI), all single.
- Position: 13 of 14 inner; no segment-edge, overlap or band-cut errors (the follow-slope re-cut left no crop-class error);
  fatigue axis flat after the 3rd line.

## Protocol notes (deviations stated)
- Crops re-cut with `--follow-slope 400 --band-extent 0.1 --mask-neighbours --overlap-note` on all 10 lines (drift -77..-142 px on
  9 of 10; the folder's flat crops overlapped 1800 of 2400 px). Commands in PREREG.
- Adjudication (one Sonnet subagent): its first hand-back viewed 11 of 20 crops and settled unviewed-line rows by rule (kept as
  `adjud_out_first.tsv`, c64c51894). The SAME subagent was sent back once to view every crop; its final output settles all 16
  disagreements from the image and keeps the 81 agreed-uncertain rows' agreed reading unchecked (viewed=no). 12 positions
  changed vs the reconciler's draft. Counted as one adjudication with one resume, not a second reader.
- The worker saw NOTES.md lines 357-359 (an early v1 Sonnet read of p1 L1-2) through a grep before PREREG (disclosed there);
  readers never saw it.

## Reader task text
Passes A/B: `reader_task.txt` (OUTPUT_PATH passA.tsv / passB.tsv); adjudicator: `adjud_task.txt` + the resume message
("view the crops for every line you did not view ... settle every queue row on those lines from the image ... add 'viewed'").

## Calls and cost
3 vision subagents: 2 Opus (about 127k and 129k tokens), 1 Sonnet (about 119k + 134k with the resume). Dollar figure: the lane
reads it from get_session (CLAUDE.md, cost comes from the orchestrator).

## Verdict
Confirm figure (guard 2): **err_true 0.088 (0.056-0.137)** on spinelli-c1519-confirm with today's pipeline; best single pass
0.083 (B), pass A 0.104; the adjudication step did not help on this leaf (vs B 0/1). Over half the errors are a sheet
inventory gap the readers themselves flagged as NEW.
Follow-up (one line, not started): give the reader the key-vocabulary sheet (v3 plus the shapes the readers flag NEW, with the
folder's own labels) -- 8 of 14 errors sit there.
