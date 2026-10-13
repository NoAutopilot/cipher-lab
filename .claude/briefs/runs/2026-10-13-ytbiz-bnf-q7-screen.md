# BNF-Q7-SCREEN (Opus worker for LANE BNF-FOCUS, account 2 / ytbiz), 13 Oct 2026

Job: build and validate ONE decode-level, order-sensitive key-screening test for `ciphers/fr3982-nevers-toscana-1592`
(BnF fr.3982 f.25, Nevers to the Grand Duke of Tuscany, 26 Aug 1592, 260 continuous digits), then run it on the two
keys already on disk: Nevers no.46 (`q7test/key_no46_codes.tsv`, from D. Bourdeau's key46.txt series A/N/P, CC BY 4.0)
and Nevers no.70 alphabet (`q7test/key_no70_codes.tsv`). Disk only. Nothing above grade M; a pass goes to a separate
verifier. Cap USD 6, box 120 min; stop before a unit that would cross 80% of either. Units: read (~0.8), PREREG (~0.5),
validation on no.62 (~1.5), two keys (~1.5), write-up (~1). Model: Opus.

Why: the structural parse-share check (q7test/structural.py) worked for no.62 (sparse table: control power 0.99-1.00,
target misfit p 0.30, retired) but is a NON-TEST for dense two-digit tables -- no.46 parses every string, real or
shuffled (1.000 vs 0.997). See the folder's NOTES.md sections BNF-Q7-TEST, "Key no.70 alphabet" and "Key no.46".

Read first: CLAUDE.md rule 3 in full (matched design, error band, orthogonality, calibration-as-gate, third-attempt
clause), rule 4; the folder's NOTES.md; `q7test/*.py` (reuse the parsing and control code); last 30 lines of ROOM.md.
Paste `python3 tools/intake_gate_check.py fr3982-nevers-toscana-1592` first.

Steps
0. ROOM claim (tools/room.py, single quotes) with box end and cap.
1. PREREG (`PREREG-Q7-SCREEN.md`, committed before any score). Decoder: DP over the key's code lengths, homophones and
   polyphones expanded, best path under a 4-gram model of the letter's language (Italian: tools/data/it16dip, held out
   from control windows; for no.46, whose known letters are French, ALSO a French run with tools/data/fr16 -- say which
   counts). Statistic: per-character log-likelihood of the best decode (grows more reliable with N; not coverage, which
   is order-blind). Nulls, both able to move the statistic: (a) 1000 keys with values shuffled within the key's own
   classes (letters among letters, nulls kept); (b) 1000 digit-order shuffles of the target decoded with the real key.
   Gate: validation power >= 0.8 at p <= 0.01 at 10% digit error (the passes disagree ~9.5%), else NON-TEST.
2. Validation, before either target run: 200 synthetic Italian texts of f.25's plaintext length enciphered with
   key_no62.tsv (a key we know is NOT f.25's) at 0/5/10/15% digit error -> power; and 200 synthetic texts enciphered
   with key_no46 the same way -> power for a DENSE table (the case the structural check could not handle). Both must pass
   the gate at 10% for the screen to be used; if the dense-table power fails, stop and log "decode-level screen
   non-test for dense tables at N=260".
3. Targets: f.25 under no.46 and under no.70 (alphabet only: say the nomenclator gap), each with both nulls. Report the
   statistic, p_a, p_b, and the best decode only as a draft (M at most) in NOTES.md.
4. NOTES.md section "## BNF-Q7-SCREEN (13 Oct 2026, account 2)" with an ITERATE-style row per key and a "next best
   attempt" line; update "## Remaining gaps"/"## Escalation" so `python3 tools/gaps_check.py fr3982-nevers-toscana-1592`
   still passes. Put the screen script in `q7test/` with --help so the next keys (no.44, 45, 47, 56, 35, 63 once
   transcribed) run through it unchanged.
5. Commit by explicit path, `tools/file_shrink_guard.py` on touched files, push (`tools/room.py --push <paths>`), ROOM
   done line "for LANE BNF-FOCUS (account 2)": validation powers, per-key statistic and p-values, verdicts.

Report what was found and where it was not found; do not classify novelty (rule 10). Never print credentials. Never the
words solved, cracked, novel, first, new for anything this project did. Never call AskUserQuestion. If
`tools/room.py --start` fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
