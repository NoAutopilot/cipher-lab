# Research director, wave 18 (18 Oct 2026, 10:1x UTC by date -u): re-issue the Sherwood reading after the rule-7 send-back

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself, `tools/experiment_log.py --check`). Report what was found and where it was not found; no novelty class (rule 10).

## JOB SHERWOOD-FIX (account 4; Opus 5.5; cap USD 5; box 45 minutes; hosts: archive.org (11280377bsb jp2.zip once, or single page images for pp.33, 84, 153, 278, 312), link.springer.com (one request: the chapter page of Leighton and Matyas, "The History of Book Ciphers", CRYPTO '84, LNCS 196, for its free preview), Google Books API (&country=US, key; at most 6); Price: vision calls: 3 x USD 0.5 + 1 reconciliation = 2.0)

SHERWOOD-VERIFY (ciphers/sherwood-cossit-1781/AUDIT.md) sent the reading back under rule 7: on pp.33, 84, 278 and 312 the solver's line
grid put line 1 one line low (9 cells; verify/diff_settled.tsv), changing 6 tokens, 3 of them S; 153-7 c2 depends on how a two-line drop
initial counts. The gate held 8/8 under the verifier's own grid.
1. Fix the instrument, not just the cells: find why build_entick_lines.py misplaced line 1 on those four pages and whether the same
   cause touches any other cited page. Check every cited page's column tops against a top-strip montage, not only the columns the old
   check flagged (127 pages, two columns; montage sheets of top strips; 3 sheets). Correct book/top_fix.tsv and book/entries_image.tsv
   to match; adopt verify/diff_settled.tsv where the image agrees.
2. Settle the drop-initial rule on 153-7 (and any other drop-initial page the cypher cites) from the image, and write the rule in NOTES.md.
3. Re-run `decode_entick.py` and `--check`, re-grade, re-run the controls and paste `tools/judge_plaintext.py` output (rule 7). Say what
   33-35 ("Beyond") now reads and whether a miscount by the encoder is the likelier explanation (an I grade if repaired, never silently).
4. Leighton and Matyas: one request to the Springer chapter page and up to six Google Books API calls. Quote anything visible on whether
   they name this cypher, Cossit, Sumner or B.178, or this Entick edition. Do not buy or log in.
5. NOTES.md "## Re-issue after rule-7 send-back (SHERWOOD-FIX, 18 Oct 2026)": what changed, new grade counts, judge and control numbers,
   the drop-initial rule, the Leighton and Matyas result. Update the verifier note so the folder carries one current set of numbers.
Report: cause of the grid error and pages affected, new grade counts, judge vs controls, Leighton and Matyas visible or not, five lines.
