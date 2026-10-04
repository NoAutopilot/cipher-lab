# NOX-OWNERSORT (account 3 worker) -- 4 Oct 2026 07:4x UTC (account-3 orchestrator)

Target ciphers/fr16142-noailles-constantinople-1571. Input sorter/owner-sort-2026-10-04 (owner's quick pass: 18 pile merges over
1,835 tiles, 36 moves, 4 bad cuts). Read NOTES.md (RUN2-NXATL, N4-NXS), sorter/README.md, TRANSCRIPTION.md first. Rebuild the atlas
inputs with sorter/build.sh if needed (pip numpy scikit-image scikit-learn opencv-python-headless first).
Question for the owner, to answer plainly at the end: does deeper hand sorting help this letter, and if so exactly where?
1. Pre-register, then corroborate each of the 18 merges against the two RUN2 machine readers (NXTA/NXTB): for tiles in the merged
   piles, do the readers give both piles the same reader label more often than for a matched control (random pairs of piles with
   the same tile counts)? Per merge: corroborated / not / readers silent.
2. Measure the effect on transcription error (TRANSCRIPTION.md): two-reader disagreement and, where BENCHMARK-TX has known-answer
   rows, err_true, before vs after the owner's sort.
3. Rank what is left by expected value to the reading: piles that look mixed (bimodal on the readers' labels or atlas features),
   and tiles whose flip changes the most decoded positions (tools/sign_sorter.py --rank-confusion or the lattice if available).
   Output a short owner list (at most 3 piles + 40 tiles), each with why, in sorter/owner-sort-2026-10-04/next_targets.tsv.
4. Verdict line for the owner: "deeper sorting would / would not help, because ...". No reading claims.
Cap 10 (rate-limit measure), box 90 min. ROOM claim/done; NOTES.md section "NOX-OWNERSORT (4 Oct 2026)".
