# PREREG MONL-SORT2 (15 Oct 2026, account 4, Opus worker MONL-SORT, LANE DEFAULT-A4-1236-15)

Addendum to sort/ctl/PREREG-MONL-CTL.md (same tile format, prompt wording, reconciliation rule), written and pushed before any crop is
regenerated, any tile cut or any sort run. Job: brief .claude/briefs/runs/2026-10-15-acct4-default-1236-jobs.md, MONL-SORT.

## Tiles (40; c268 line:pos, all in L06-L25, crops from regen_monll11.sh / regen_monll16.sh / regen_monll21.sh)
Family A, cells K04|K12 (leads face clear n, the 15 of MONL-K04TRY):
- leads (15): L06:18 L06:23 L06:34 L08:10 L08:19 L09:27 L10:33 L13:14 L15:4 L16:16 L18:18 L21:9 L22:14 L24:12 L25:26
- controls, K04 facing clear d, bands not used by MONL-CTL (3): L14:14 L23:16 L25:17
- references, K12 facing clear n (2): L12:8 L14:13
Family B, cells K14|K37 (leads: K14 facing clear s; L01-L05 tokens left out, their crops need a fourth request):
- leads (6, weakest --try gain first): L08:6 L08:22 L15:11 L11:20 L24:10 L21:7
- controls, K14 facing clear p (2): L12:9 L17:7
- references, K37 facing clear s (2): L11:5 L21:18
Family C, cells K40|K41 and K45|K39 (MONL-L21's leads plus L12:21, a fourth K40 facing z found while choosing tiles):
- leads K40|K41 (4): L12:21 (faces z) L22:6 (t) L24:29 (z) L25:16 (z); leads K45|K39 (2): L24:3 (o) L24:16 (u)
- references K41 facing a (2): L21:13 L24:26; K39 facing u (2): L13:13 L18:25
- no in-band negative control exists: no K40 faces y and no K45 faces m anywhere in L06-L25.
Counts: 20 + 10 + 10 = 40 (one call per sort). (Correction made before any run: a first count read 41 and dropped L21:7; the true count is 40, so L21:7 stays.)

## Sorts
Two Sonnet calls, A and B (B lists the tiles in reverse order), crop paths and montages only; no value, reading, clear text, current label,
role or decode shown. Each tile carries its own candidate pair. Answers sort/srt/sortA.tsv, sortB.tsv; reconciliation by script
(sort/srt/reconcile_srt.py) -> sort/srt/reconciled.tsv.

## Decision rule (fixed now)
A tile "goes X" when both sorts say X and neither conf is L.
- Family A: relabel a lead K04 -> K12 (tag `monl-sort2`, conf M) when it goes K12, unless 2 or more of the 3 d-facing controls go K12
  (then no Family A relabel: non-discriminating) or both K12 references go K04 (non-discriminating).
- Family B: relabel a lead K14 -> K37 (tag `monl-sort2`, conf M) when it goes K37, unless 1 or more of the 2 p-facing controls go K37 or
  both K37 references go K14 (then no Family B relabel).
- Family C: leads only, no relabel in any outcome (no in-band negative control exists). Reported: each lead's call, and whether the
  references stay (K41 refs K41, K39 refs K39).
- Splits and low-conf agreements are not applied. After any relabel: score_c268.py, align_c268.py, decode_key.py, then every --check.
  Keep condition for relabels: align L01-L25 shuffled-clear 0/200 at or above (as MONL-CTL); otherwise revert.
