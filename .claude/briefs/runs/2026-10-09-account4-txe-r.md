# TXE-R: the live letter -- fr.3252 f.117r re-transcribed with today's pipeline, decoded under the folder's own PREREG (LANE TX-ENGINEER round 3, Amendment 2 guard 3; account 4, Opus 5.5; cap 15, box 150 min)

Read `.claude/briefs/runs/2026-10-09-account4-txe-COMMON.md` first, then `benchmark-tx/PREREG-txeng-3.md` ("Decision"),
TRANSCRIPTION.md, and in `ciphers/birago-fr3252-1571-72/`: NOTES.md sections "f.117r (no.77, 13 Mar 1572): first test under
the printed 1572 key", "NEVBIR-117C", "TX-DECODE", "BIR-APPLY", "BIR-OWNER", HYPOTHESES.md rows D2-B117KAPC (the folder's
power control: printed 1572 key on la/recon_f117_3r.tsv, power 18/20 at error 0.126, 16/20 at 0.183) and
`RD7-2026-10-04-f117.md` (the committed reading: 279 tokens, S 190 / M 63 / U 26, from
`../nevers-birago-fr3251-1572/harvest/tx_decode/eye/apply/decode_apply.json` job 1, key `harvest/key_1572_sheet.tsv`).
Why this job exists: Amendment 2 guard 3 -- the campaign's pipeline is applied to one live unread Birago 1572 letter and
reported as "the key now licenses N more tokens at grade S" (or does not). f.117r has the most reader-split tokens of
f.117/f.144/f.168 (11 M picks owner-side; 63 M tokens committed). Round 2 found no instrument that moves eval; today's
pipeline is: `iiif_lines.py --band-extent 0.1 --mask-neighbours --overlap-note` (+ `--follow-slope` on any line the
debug overlay shows sloping), two blind Opus 5.5 passes with the folder's own blind brief and sheet
(`harvest/f117/blind_pass_brief_f117.md`; sheet as it names), `reconcile_passes.py`, a Sonnet third-reader adjudication
from the crops, then `decode_key.py` under the committed decode config and the printed key.

## Order of operations (binding)
0. `python3 tools/prior_work.py birago-fr3252-1571-72 --item f117r --step-type transcribe --offline` (warn-first; paste);
   `python3 tools/intake_gate_check.py birago-fr3252-1571-72` (paste; it reads partial today).
1. Write `ciphers/birago-fr3252-1571-72/harvest/f117/PREREG-TXE-R.md` and push BEFORE any read: crops command, the two
   passes, reconciliation, the decode command (the committed config, unchanged key and exceptions), and the gates:
   (a) err_2reader of the two new passes (share of aligned positions where they differ) reported beside the folder's
   earlier passes' 0.56 agreement (passA/passB_L01-04, NOTES "NEVBIR-3252-B"); (b) the new reconciled ciphertext decoded
   under the committed config: tokens by grade vs the committed 190 S / 63 M / 26 U; "N more tokens at grade S" = the S
   count minus 190, with the list of positions that changed grade and their new values; (c) the folder's power control
   re-read at the NEW measured err_2reader (HYPOTHESES D2-B117KAPC's curve: if the new error sits where power < 16/20, say
   the key cannot license the change at that error and report the count as unlicensed); (d) `tools/judge_plaintext.py`
   on the new reading with the folder's spec (`specs/birago-fr3252-f117.json`), pasted. A gain is "the key now licenses N
   more tokens at grade S" only when (c) licenses it and (d) does not FAIL worse than the committed reading's judge line.
2. Crops: `tools/iiif_lines.py --image <the f117 source on disk; images/f117 holds 33 crops, find its src_ or re-cut from
   the committed region per images/manifest.json> --band-extent 0.1 --mask-neighbours --overlap-note --debug`; check the
   overlay; `--follow-slope` only where it shows a slope. Paste the command and the box-check if atlas boxes exist for
   f117r (`../nevers-birago-fr3251-1572/atlas/signs.tsv` page f117r). Commit crops + manifest.
3. Two blind Opus 5.5 passes (value-blind; the folder's brief + sheet + the generated crops note; one call per 20-40 crops).
   Commit each pass. `tools/reconcile_passes.py passA passB --crops`; one Sonnet third-reader call on disagreements.tsv +
   uncertain.tsv with the agreed neighbours as landmarks; write the new ciphertext as `harvest/f117/ciphertext_f117_txer.tsv`
   (never overwrite the committed `ciphertext_f117_top1.tsv`); commit.
4. Decode: copy the committed config to `harvest/f117/decode_txer.json` with only the ciphertext path and the output
   paths changed; `python3 tools/decode_key.py ciphers/nevers-birago-fr3251-1572 --config <that>`; grade counts; the
   changed-grade list; the judge line; the power statement from (c). Write everything to
   `ciphers/birago-fr3252-1571-72/harvest/f117/RESULTS-TXE-R.md` and a NOTES.md section "TXE-R (9 Oct 2026)". No grade
   above S; the committed reading and its RD7 stay as they are; the new reading is a candidate for a verifier
   (post the "reading ready" ROOM line only if (c) and (d) hold; else "no licensed change").

## Report
Results-log row in research/TX-IDEAS-2026-10-09.md (id LIVE-F117; rebase before editing). Vision calls: crops 0, passes
2-4, adjudication 1, no hosts (disk only; Gallica is 403 today -- if the f117 source image is not on disk, stop and say
so). Cap 15; stop before a call that crosses 80% of cap or box. Report in a short paragraph (first line: err_2reader new
vs old, S tokens new vs 190, licensed yes/no with the power figure, judge line) and stop. Rule 10 wording only.
