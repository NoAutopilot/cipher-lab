# PREREG-HEID1623A (written before any native crop is fetched or any reader is called; 16 Oct 2026, 01:2x UTC by date -u)

Job: .claude/briefs/runs/2026-10-15-acct4-depth-steps-2.md, JOB HEID-1623A. Cap USD 14, box 100 minutes (01:12-02:52 UTC; no new
unit after 02:32 UTC, 80%). service.archief.nl <= 10 (3 used before this file: METS + scans 166, 171 at 1200 px, sha1 MATCH the
heid_6022j manifest). No decode, no key.tsv edit, no reading of the 1621 pair; rule 10 wording.

## Material
NL-HaNA 1.01.02 inv. 6022 (METS 412b1414-afa2-42fe-b56d-2b5f705e5005), Brederode, Straatsburg 12 Aug 1623 (Resolutien NR 6 p.260 res.
1721a). Three native regions, fetched once (IIIF pct regions of the 1200 px layout, full size):
- U1 = scan 166 cipher block, `pct:61,16.5,39,16`; U2 = scan 171 cipher block (duplicate), `pct:61.5,22,38.5,14`;
  U3 = scan 171 marginal note, `pct:50,18.5,11,14.5`. If a region clips the block or note, one widened re-fetch per unit (<= 3 more).
- Crops: `tools/iiif_lines.py --image <region> --out <dir> --prefix h166|h171|n171 --debug`, command and output pasted in NOTES.md
  before the first reader call; the debug overlay is checked; readers get line crops only.

## Units and pricing (CLAUDE.md Usage 6, per pass)
Three units x (2 blind Sonnet readers + 1 reconciliation by this worker against the crops) = 6 reader calls x USD 1.4 + 3 = 12.6.
Readers return text only: numerals, dots, letters, clear words in [clear: ...], other signs in [sym: ...], line by line; no key, no
other reader's output, no hint of what the note might be. Stop before starting a unit that would cross 80% of cap or box.

## Witness control (gate 0.90, the 375-vs-379 rule of PREREG-HEID1621G)
Token stream of each block = numerals and single letters in order ([clear]/[sym] dropped). Agreement = matched tokens
(difflib.SequenceMatcher, autojunk off) / max(len166, len171). Reported also per unit (units.py grammar of heid1621g: a maximal numeral
run closed by one letter; N = run with no letter). PASS >= 0.90 per token.

## Grade rule (S-as-transcribed: the sign is named as transcribed; no value is read, nothing is H or C)
A block token is **S** only if (a) the witness control PASSes, (b) both blind readers of that witness agree on it, and (c) it aligns to
an identical token in the other witness. Every other token is M. If the control FAILs, every token of both blocks is M.

## Marginal note: when is it a decipherment?
1. Reconciled note text (two readers + reconciliation), every word grade M. Classify by its own content first: a note that is a summary
   ("over ..."), a docket (date, receipt, "gelesen", "ontfangen"), or a clerk's remark is reported as such and NOT forced into an
   alignment. It is a **decipherment candidate** only if it is running text whose word count is at least half the block's unit count.
2. Alignment test (candidate only): `tools/interlinear_align.py align` on (group, span) pairs. Pairs = the block (the reconciled 166
   or 171 stream, whichever has more S tokens) cut at its clear words, each cipher run paired with the note span between the same
   clear words where the note carries them; where it does not, the block is cut into its written lines and the note into the same
   number of spans of proportional length. Statistic = the tool's CONSISTENT count (code values whose top chunk is non-empty, occurs
   >= 2 times on >= 2 pairs, >= 0.6 of its aligned occurrences). Control = `--shuffle 200` (note spans dealt to the wrong runs, seed
   1623). PASS = real > shuffle p95 AND real >= 3. Fewer than 3 pairs, or a shuffle that cannot move the statistic (every draw equal
   to the real value by construction), is a non-test, reported as "untestable by this tool at this N", not a negative.
   A second, tool-independent statistic is reported beside it (not gating): for every numeral that recurs in the block, whether the
   word-for-word monotone alignment gives it the same note word each time, against 200 random permutations of the note's words.
3. Only on PASS: `key_1623_draft.tsv` (value -> meaning, count, grade C, source = the note), for the parent and a verifier; it never
   touches key.tsv. On FAIL or non-test: no draft key.

## Also reported (descriptive, no gate)
Unit grammar of the 1623 block (pair+letter / number+letter / bare number shares) vs the 1621 pair (heid1621g/units.tsv), and which
1623 units coincide with a 1621 unit (same numbers and letter) -- a lead only, M.
