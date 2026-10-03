# BIR-ROUND2 (account-3 worker, 3 Oct 2026 12:4x UTC)

Targets: nevers-birago-fr3251-1572 (f.168, f.144r) and birago-fr3252-1571-72 (f.117r). Opus 5.5. Cap USD 8, box 50 min.
Vision calls <= 4 x USD 1.5 (one per leaf + 1 reconciliation), line crops via tools/iiif_lines.py (or the existing crops under
harvest/tx_decode/eye/verify), paths pasted before the first call. Claim in ROOM.md first (tools/room.py); done line at the end.

Where it stands (A1-BIR-VERIFY, 12:25 UTC): 24 lattice corrections confirmed by blind readers with ambiguity-matched decoys and
applied at S; reading files harvest/tx_decode/eye/verify/reading_f{117,168,144r}_verify.txt. f.117r now shows French runs to the eye
(orchestrator's interpretation only: "sans intention de conuenir", "ce qui s'est ... qui se rendroit", "plus facile et", "soing et si
vous"); f.168 shows Italian ("quanto il procedere", "molto con"). Judge still FAILs (f.117r fr -1.30 vs real_p05 -0.90, null p99 -1.81;
f.168 it -1.39 vs -1.01, null -1.67): well above the null, short of real prose. The remaining error is the 74 M + 26 U tokens on f.117r.

Job (round 2 of the same instrument that just worked, now on the M tokens -- not a third attempt at a failed knob: round 1 PASSED):
1. Pre-register (commit + push before any score or crop): the decode base = the verify ciphertext with the 24 S corrections; the
   candidate set per M position = the two readers' alternatives + tools/lookalike_pass.py pairs; run tools/key_decode_lattice.py at
   lam 4 (same as round 1) on that base; the changed positions are the round-2 candidates; an equal number of ambiguity-matched decoys
   (lattice ratio matched, as A1-BIR-VERIFY's G2 arm); gate per leaf = key-implied pick rate on changed > matched-decoy swap rate,
   binomial p < 0.05, AND the position-shuffled-lattice null (A1-POSNULL design, 200) still passes on the new base.
2. U tokens: list every X_NEW / uncovered sign with counts and context; check the printed 1572 key's nomenclator and nulls (key file
   on disk) for a match by shape description; report, do not guess values.
3. One blind Opus reader per leaf on masked crops, two options per position, order randomized (A1-BIR-EYE protocol).
4. Apply survivors at S via exceptions_*.tsv; tools/decode_key.py --check; tools/judge_plaintext.py on each leaf (fr for f.117r,
   it for f.168/f.144r, copy the spec with judge.language changed if needed -- say so); paste the judge lines in NOTES.md.
5. Write a NOTES.md section in both folders, gaps_check, file_shrink_guard, commit by explicit path, push.
Grades H/C/S/M/I/U counts per leaf. Report what was found and where it was not found; do not classify novelty; no English gist in
repo files beyond what NOTES already carries.
