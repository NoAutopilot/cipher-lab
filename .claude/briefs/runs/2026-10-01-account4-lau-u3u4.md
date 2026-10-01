# LAU-U3U4: fr3625-lauriere-1593 -- settle the f.58r disagreements (U3), then run the key57 control (U4)

Written 1 Oct 2026 23:4x UTC (clock read) by the account-4 parent (session_01SEzoee67SivPooFpTkxMme).
Role field for every ROOM.md line: `LAU-U3U4 (account-4)`. Model: Fable 5.1 (Opus 5.5 only if Fable fails). Cap:
USD 10 of usage. Box: 60 minutes. Vision calls: at most 16 (15 sheets, one per call, plus one reconciliation look);
stop before the call that would cross 80 pct of either figure and push what you hold.

## The job, in one line

Run the folder's own named next step (NOTES.md "Stopped on cap before U3 and U4", 27 Sept 2026, LAU-F58B): settle the
91 pass-A/pass-B disagreements on fr.3985 fol.58r's numeral lines from the deskewed sheets already on disk, write
`key57/f58s_ciphertext.tsv`, then run `key57/control_key57.py --apply-f58 key57/f58s_ciphertext.tsv --seeds 20` with
the gloss-marked `[PLAIN]` rows removed, and write both numbers (real vs 20 shuffled keys) to HYPOTHESES.md and NOTES.md.

## What is on disk (read before anything else)

- `ciphers/fr3625-lauriere-1593/NOTES.md`, sections "LAU-F58", "LAU-F58B" and "Stopped on cap before U3 and U4".
- `key57/f58s_passA.tsv`, `key57/f58s_passB.tsv` (two blind Opus passes), `key57/f58s_reconcile/` (disagreements.tsv,
  uncertain.tsv, ciphertext_draft.tsv, agreement.tsv from `tools/reconcile_passes.py`).
- The 49 deskewed sheets under `images/` (regen script `images/regen_f58s_sheets.sh`; the native region is cached --
  do not fetch from Gallica; gallica.bnf.fr requests this job: 0).
- `key57/control_key57.py` (`--apply-f58`), `key57/key57.tsv` or its equivalent (read the script's header for the path).
- `HYPOTHESES.md` (append-only; one row per run with both numbers).

## Steps

1. `python3 tools/room.py --start`; read the last 30 ROOM.md lines; append a claim line (`claim: U3+U4 on f.58r,
   box ends <clock time>, cap USD 10`).
2. U3 (vision, priced per sheet): from `disagreements.tsv` and `uncertain.tsv`, list the sheets that carry a
   disagreement or an uncertain numeral on lines L15-L38 (NOTES says about 15 sheets). For each such sheet (one
   subagent call per sheet, Fable or Opus, never the whole set in one call -- CLAUDE.md Usage 6), give the subagent
   only that sheet's path, the pass A and pass B readings of its rows and key57's code inventory (never meanings),
   and ask for a settled numeral per disputed column with H/M/L confidence. Settle plain-text columns as `[PLAIN]`.
   Write `key57/f58s_ciphertext.tsv` (one row per column: line, position, value, grade H/M/L, source A/B/settled).
   Paste the settled count (settled H / M / L / left open) into NOTES.md.
3. U4 (script, no vision): remove `[PLAIN]` rows, run
   `python3 key57/control_key57.py --apply-f58 key57/f58s_ciphertext.tsv --seeds 20`. Report the real score, the
   shuffled-key mean, range and how many of the 20 shuffles beat the real key (the LAU-F58 gate shape: real must sit
   outside the shuffle distribution). Append the row to HYPOTHESES.md with target and control numbers side by side.
4. Write a dated section in NOTES.md ("## LAU-U3U4 (1 Oct 2026, account-4)") with: the settled counts, the U4 numbers,
   the outcome in the folder's own (a)/(b)/(c) terms, and one named next step. The status word on line 1 stays
   `open` unless a verifier says otherwise (rule 5; this target has a NEAR.md row, never `closed-negative`).
   Edit the NEAR.md row's evidence cell to add one sentence with the U4 numbers and set its "Last touched" to the
   clock time (rebase before writing NEAR.md; keep every other row intact; run `python3 tools/near_check.py`).
5. Commit by explicit path (`git add ciphers/fr3625-lauriere-1593/... NEAR.md`), `git fetch origin main && git rebase
   FETCH_HEAD`, `python3 tools/restricted_guard.py --outgoing`, push to main. Done line in ROOM.md with both numbers,
   the vision-call count and the cost figure you were given (never your own guess -- write "cost per the parent").

## Rules that bind here

- Rule 3: no negative without the matched control; U4's 20 shuffled keys are that control. Rule 4: every settled
  numeral carries a grade. Rule 10: never "new", "first", "unpublished"; report what was read and what was not found.
- Never "solved"; a reading that FAILs its gate is a candidate that failed the gate.
- Stop when the brief is met: no U5, no sibling leaves, no fr.3632 work (ASKS 78 is the owner's). Write any
  follow-up as one line in NOTES.md.
- The common tail of `.claude/briefs/README.md` applies in full (claim/done lines, credentials, push discipline).
