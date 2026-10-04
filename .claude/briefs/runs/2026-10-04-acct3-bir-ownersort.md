# BIR-OWNERSORT (account 3 worker) -- 4 Oct 2026 06:5x UTC (account-3 orchestrator)

Target: ciphers/nevers-birago-fr3251-1572. Input: sorter/owner-sort-2026-10-04/ (owner's sign sort of 488 tiles on f.117, f.144r
and f.168: 203 moved, 52 piles -> 105; README there). Read NOTES.md (NEVBIR-LOOKALIKE, GAPS4, RD7 files) and TRANSCRIPTION.md first.

Job:
1. Fold the owner sort in as a THIRD READER (never ground truth): for every tile, the two machine labels + the owner's pile. Write
   harvest/ownersort/three_reader.tsv and the per-sign agreement table.
2. The 52 -> 105 split: for each owner split (T45 -> T45-b/-c/-d etc.), decide with a pre-registered test whether it is a real
   distinction (homophone/variant carrying different values) or an over-split: the key-constrained decode (tools/decode_key.py,
   the existing keys/) and positional/contextual statistics, with a matched control (random re-split of the same pile sizes).
   Merges the data supports are recorded as such; splits it cannot separate stay as owner-only distinctions, flagged.
3. Re-run the f.144r / f.168 / f.117 decode with the settled inventory, grade per token (rule 4), and report what moved versus the
   prior reading (counts by grade, words gained/lost). decode --check must pass; judge with the it16 corpus if one is on file.
4. The 5 aside and 3 bad-cut tiles: list them for a recut (tools/iiif_lines.py), do not guess.
Rule 3 control before target; rule 4a depth noted (no novelty claims, rule 10). Cap 12 (rate-limit measure), box 90 min,
price per pass. ROOM claim and done lines; NOTES.md section "BIR-OWNERSORT (4 Oct 2026)".
