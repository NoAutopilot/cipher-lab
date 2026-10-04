# PREREG dup-settle -- es132-vargas-mexia-1578: settling the f.89 letter's '?' tokens from the f.93-95 duplicate (A3V3-ES132S, account 3 worker for LANE-A3V3, 4 Oct 2026, written 06:38 UTC by `date -u`, before any settlement is computed or applied)

Brief: `.claude/briefs/runs/2026-10-04-acct3-a3v3-wave2.md` section A3V3-ES132S. Input: `dup_settlements.tsv` / `dup_align.tsv` as committed by
A3V3-ES9396 (frozen copies `dup_settlements_pre.tsv`, `dup_align_pre.tsv`, byte-identical, so the rule reads the pre-settlement state after
`align_dup.py` is re-run). Script: `settle_dup.py` (to be written after this file is pushed; `--check` exits 1 if stale).

## Scope
Only the f.89 letter's unprinted pages (f.89r, f.89v, f.90r, f.91r; page_kind `unprinted`, 83 rows). The 36 `teulet-f90v` rows are NOT applied:
f.90v L10-L26 is test 1's printed known-answer calibration, and changing its transcription from the duplicate would leak a second copy into the
known-answer score. They are listed in the output only.

## Rule (applied per row of dup_settlements_pre.tsv, f.89 token x flagged '?', duplicate token y unflagged)
R1 (blind agreement): y lies inside an `equal` opcode of the two blind passes of its duplicate page (difflib over `test2.load_pass` tokens per
   line, exactly as `run2/reconcile_dup.py` aligns them), i.e. both blind readers wrote y and the reconciler made no decision there
   (the declared mechanical <n>0ρ -> <n>ρ rule counts as agreement if both passes wrote <n>0ρ).
R2 (confirm): action `confirm` or `confirm-text` (same token, or the clerk-variant/notation classes of align_dup.py: same decoded text) and R1 ->
   the '?' flag on x is removed; x's token is NOT replaced (a variant/notation y is the clerk's or the other reader's spelling of the same text).
R3 (propose): action `propose-mark|vowel|base` and R1 and
   (a) isolation: the aligned pairs immediately before and after the pair in `dup_align_pre.tsv` are both anchors (class same/variant/notation)
       -- a 1:1 substitution, not a re-segmented window (the ES9396 image sample showed re-segmented windows are the clerk's re-encipherment);
   (b) y does not use a duplicate-side notation form of align_dup.NOTATION (base 14, 0, rum, rom), which the f.89 reading writes otherwise;
   -> x is replaced by y, unflagged.
Anything else stays as it is ('?' kept).

## Grade (rule 4)
The f.89 pages' reading grade is M for every key-decoded token (test2_result.json, gate (b) page-level; no S/H/C on these pages). A settled
token is graded M (never above the reading's own grade); a token that becomes a code word / unreadable stays U. Counts before/after per page.

## Control (rule 3; can it differ? yes: it counts token *replacements*, which depend on the dup/f.89 token identity, the R1 agreement and the
isolation of each pair -- none orthogonal to the statistic)
50 already-firm f.89 tokens (unflagged, unprinted pages, aligned 1:1 to an unflagged duplicate token; random.Random(1578).sample over that
population, sorted) are treated as if flagged and run through R1-R3; statistic = share left unchanged (not replaced). Gate: >= 95% unchanged
(<= 2 of 50 replaced). The same share over the whole firm population is reported beside it.
If the control gate FAILS: R3 replacements are not applied (they would overwrite firm tokens at a rate above 5%); only R2 flag removals are
applied, and the R3 candidates are written as image-check pointers.

## After
`align_dup.py`, `test2.py` re-run (readings regenerate); `test2.py --check`, `align_dup.py --check`, `settle_dup.py --check` exit 0; test1 and
test0 `--check` untouched. Rule-7 fresh re-derivation owed afterwards (not by this worker).
