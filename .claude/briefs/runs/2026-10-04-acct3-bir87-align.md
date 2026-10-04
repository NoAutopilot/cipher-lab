# BIR87-ALIGN (account 3 worker) -- 4 Oct 2026 15:5x UTC (account-3 orchestrator)
Target: ciphers/nevers-birago-fr3251-1572. The owner finished the no.87 sorter (sorter/no87/owner-sort-2026-10-04/: settled_no87.tsv,
summary.json) and corrected 7 of his earlier picks (sorter/owner-sort-2026-10-04/corrections.tsv). This is BIR-KEYFIT's named next step
(harvest/keyfit/RESULTS.md "Next"): a C value per OWNER pile from the clerk's period decipherment of no.87, by alignment, no LM.
Read harvest/keyfit/RESULTS.md, NOTES.md NEVBIR-87ALIGN and the two owner-sort READMEs first.
1. Build the owner-labelled no.87 sequence: no.87 tokens (f.178r/f.178v/f.179r) relabelled by settled_no87.tsv where the owner's sorter
   covered them, atlas/line-read labels elsewhere; state the count of each. Apply corrections.tsv to the 4 Oct sort labels (f.117/f.144r/
   f.168) the same way, documented.
2. PREREG (pushed before alignment): `tools/interlinear_align.py` against the clerk sheet exactly as NEVBIR-87ALIGN ran it, with its
   shuffled-sheet null (report real agreement vs shuffled max, as 0.896 vs 0.376 there). Per owner pile: aligned occurrences, C value,
   agreement share; a split family (e.g. T60 vs T60-c/T60-d/T60-e, T19 vs T19-b/c/d, T86, T83-b, T85-b, X_NEW-l) is a REAL homophone
   split only if the sub-piles get different clerk letters at >= 2 occurrences each and above the shuffled null; same letter = an
   over-split (merge recommended, not applied). Piles with < 2 aligned occurrences: "no evidence", never guessed.
3. Then, only for piles that got a C value: re-decode f.144r, f.168 and f.117r under the owner's labels + those C values (decode script
   on file, --check), judge (it16dip/fr16 as the folder uses) vs the current reading, and the existing shuffled-key control. Report
   whether the decode gate that failed under the owner sort (BIR-OWNERSORT/BIR-ADJ: judge FAIL) now moves; nothing claimed beyond.
4. Write harvest/bir87align/RESULTS.md, NOTES.md section, HYPOTHESES.md row; key changes only as proposals (grade C needs the clerk
   alignment, which this is -- write C-grade proposals to a proposals TSV, do not edit key files); ROOM line for a verifier.
Disk only, no network, no vision calls. Model Opus 5.5. Cap USD 7, box 75 min (stop before a step that would cross 80% of either).
ROOM claim/done via tools/room.py. Do not touch other targets.
