# LANE-NEAR3 wave 2 (4 Oct 2026 01:3x UTC, written by LANE-NEAR3, account 2 / ytbiz, session_01Au8dSL1TXFoCk5P5opEMVv)

Common rules: exactly the "Common to every job below" section of `.claude/briefs/runs/2026-10-04-ytbiz-near3-wave1.md` (room.py
start/claim/push, cap and box, no dollar figures, no AskUserQuestion, rule 10 wording, clair1161 jobs write only `reports/<JOB>.md`).
Intake gate pasted 01:1x UTC (wave 1 file) for hellen and clair1161; thurloe-printed and taurello-roma-1527 below.

## NEAR3-C1TX-<LEAF> for c187R and c188L
Exactly the wave-1 job "NEAR3-C1TX-<LEAF>" (c187R = f188 right, 3950,50,3150,4650; c188L = f189 left, 100,50,3150,4600), with one change:
**the folder is 26 MB of 30.** Your committed crops + overlay must total <= 1.5 MB: grayscale JPEG q60 at the same dimensions, then lower
quality (never resize below the reading resolution you used) until under. `du -sh` before your push; if the folder would pass 29.5 MB,
commit only tx/ files and the crop manifest entries (crops regenerable with your pasted iiif_lines command) and say so in your done line.
Read `reports/NEAR3-C1TX-c186L.md` and `reports/NEAR3-C1TX-c187L.md` first: use their NEW1 labels the same way (c186L NEW1 = v with long
bar, c187L NEW1 = open arc at L24 -- give yours distinct names NEW_<leaf>_<n> if not clearly one of these); note `s` (5-hook) and arc-2.

## NEAR3-HEL4 -- hellen-frederick-1752: transcribe R4372 (f.48) codes 1-800 and test it on R1953 (Opus + Sonnet subagents; cap USD 10; box 60 min)
Why: NEAR3-HEL3 found R4372 = same printed form, layout and apparent hand as R4369 (the Hellen key, codes 801-1796), with codes 1-800
filled; R1953 has 374 U tokens in 1-800. Like R4370 (same form, failed), it is a candidate until the test passes.
Read: NOTES.md sections "READ2-HEL", "READ2-HEL2" (the recipe and the four attributions L/R0/R100/LR100), "NEAR3-HEL3" (URLs, sizes,
sha1s); `key_r4369/README.md`, `key_r4369/build_keys.py`, `sibling_michell/test_sibling.py --help`.
1. Pre-register FIRST (`key_r4372/PREREG.md`, pushed before any test): statistic and controls exactly as READ2-HEL2 (value-shuffle x200
   uni log-prob and order-shuffle PMI, power from the positive control at R1953's covered count), the four attributions, PASS rule as
   READ2-HEL2 stated it; plus the combined test: R4372(1-800) + R4369(801-1796) on all of R1953 vs the same controls.
2. One DECODE browser login; fetch R4372 P2 and P3 full size into your scratchpad (sha1 must match the manifest); never commit them.
3. Column crops per READ2-HEL2's recipe with re-measured x positions (`tools/iiif_lines.py --image <file> --out <scratchpad dir>`; paste
   the command before any subagent call). Units: P2 and P3, each 2 blind Sonnet passes + 1 reconciliation (yours) = 6 units at ~USD 1.3.
   Stop before a unit that would cross 80% of cap or box. Crops stay in the scratchpad (not public domain).
4. `key_r4372/key.tsv` (+ L/R variants built the way build_keys.py builds R4369's), err_2reader per page, grades H for read cells, M for
   doubtful. State every convention (crossed-out cells, right-over-left, trailing ?) in `key_r4372/README.md` (READ2-HELRD lesson).
5. Run the pre-registered tests; paste outputs. If the combined key PASSes, regenerate the reading with `tools/decode_key.py` into
   `key_combined/` (decode.json + key.tsv + reading) with `--check` exit 0, and paste `tools/judge_plaintext.py specs/hellen-frederick-1752.json
   --file <reading>`; else leave the R4369 reading as is.
NOTES.md: section "NEAR3-HEL4 (4 Oct 2026)", target vs controls side by side, grades counted; refresh gaps/escalation; NEAR.md row cells.

## NEAR3-THUR -- thurloe-printed: one-vote M boundary test (Opus; cap USD 5; box 40 min; disk only)
Intake gate: run `python3 tools/intake_gate_check.py thurloe-printed` and paste it; exit non-zero -> stop and flag.
Why: NEXT-STEPS row: "V3a's one-vote M boundary test (67, 153, 84, 275) against pool_1654/tokens.tsv, disk only, ~$1". Read NOTES.md
"Remaining gaps"/"Escalation" (end of file) and the V3a/SO-THURLOE-P4 passages they cite (grep "one-vote"). Pre-register in a short file
before running: what number-boundary evidence in the later Stamford letters would confirm or refute each of 67, 153, 84, 275, and a control
that can differ (e.g. the same check on codes with known H values, and on random codes of matched frequency). Run it, report per code,
update the key grade only where the pre-registered rule says so, `tools/decode_key.py --check` if anything changed. NOTES.md section
"NEAR3-THUR (4 Oct 2026)"; refresh gaps/escalation; gaps_check OK line.

## NEAR3-TAUR -- taurello-roma-1527: Sanuto Diarii full-text search (Sonnet; cap USD 3; box 30 min)
Intake gate: run `python3 tools/intake_gate_check.py taurello-roma-1527` and paste it (the target is `blocked` on unread editions; this
job IS the edition read, so a nonzero exit does not stop it -- say so). Read NOTES.md "Robert volume check (A2P4-TAUR)" and the end.
Find the archive.org identifiers of Marino Sanuto, *I Diarii*, vols 45 and 46 (June-July 1527) via advancedsearch (metadata only), then
be-api fts per volume for Taurello / Torello / Vetralla / "Pietro Antonio" / Orange-Oranges / "24 zugno"; positive control per volume (a
term certain to be there, e.g. "Borbon"). Read the hit snippets; if a hit is the letter or a report of it, fetch that volume's djvu.txt once
and quote the passage with page. Also Pastor appendix (Geschichte der Päpste IV.2, Anhang) if an identifier is found in the same way.
NOTES.md section "NEAR3-TAUR (4 Oct 2026)": identifiers, queries, hits per volume with the control, the request count per host; status
line unchanged unless the edition reading changes the check-solved verdict (then say what changed, rule 10 wording). Good-citizen: 1.5 s apart.
