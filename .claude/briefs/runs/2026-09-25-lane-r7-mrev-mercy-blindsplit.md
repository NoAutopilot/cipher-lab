LANE R7 MREV -- espagnol142-mercy-1648: carry the blind eye-check into the reading (Sonnet, cap $3, box 35 minutes; disk only, no hosts, no subagents).
Common: 2026-09-25-lane-r7-common.md. NEAR.md row "espagnol142-mercy-1648".
Intake gate (live, 25 Sept 20:00 UTC): "espagnol142-mercy-1648: partial (line 1) -- edition/page or full-text-search citation found within 6 lines" (exit 0).
State: exceptions.tsv re-reads five glyphs that both original blind passes read as 19 as 14 (grade M; they make "Cheureuse", "Cleues" and
"y con co..."). R7-MEYE (meye/README.md, meye/compare.tsv), a third blind reading, agrees 14 at r06 pos14 and r17 pos5 but reads 19 at r14 pos7,
r16 pos3 and r16 pos6. So at those three, every blind reading (three of three) says 19 and only the non-blind M2 re-read says 14.
Job:
(1) Make the reading follow the blind majority: remove the r14/7, r16/3, r16/6 rows from exceptions.tsv (keep r06/14 and r17/5, adding "blind
    re-read R7-MEYE agrees" to their reason), regenerate with `python3 tools/decode_key.py ciphers/espagnol142-mercy-1648` and confirm `--check`
    exits 0. List every word that changes (before -> after) and the new grade counts (H/C/S/M/I).
(2) v07 pos15-16: MEYE reads two tokens (3, 17) where ciphertext.tsv has one (7). Look at meye/ crops and images/f22v_canvas59.jpg at 4x and settle it
    (one token or two). If two, record it in corrections.tsv (never silently edit ciphertext.tsv: add the row with reason and source) the way
    the folder already does, regenerate, `--check` 0, and list the word change. If unsure, grade M and leave the stream as is.
(3) Judge: `python3 tools/judge_plaintext.py` with the target's spec if one exists (specs/ grep for mercy), else skip and say so; paste the output.
(4) Append "## MREV: blind split applied (25 Sept 2026, LANE R7)" to NOTES.md with the before/after word table, grade counts and the judge output.
    Do NOT edit AUDIT.md (the verifier's file); the orchestrator tells LANE V6.
ROOM done: "done: for LANE R7: mercy mrev -- exceptions 5 -> 2, words changed <n> (Cleues -> <x>), grades S <s> M <m>, v07 15-16 <one|two|M>, --check 0".
Report what was found and where it was not found; do not classify novelty.
