LANE R7 MSHUF -- espagnol142-mercy-1648: the shuffled-stream control V6-MERCY named as missing (Sonnet, cap $3, box 40 minutes; disk only, no hosts).
Common: 2026-09-25-lane-r7-common.md. NEAR.md row "espagnol142-mercy-1648"; AUDIT.md section 3 item 1 ("Missing control").
Intake gate (live, 25 Sept 20:00 UTC): "espagnol142-mercy-1648: partial (line 1) -- edition/page or full-text-search citation found within 6 lines" (exit 0).
Question: is the anneal gap (target best -1154.3 vs matched control best -1321.7, K=38, N=521, es17 corpus) due to sequential plaintext structure,
or only to the target's skewed symbol profile (38 codes, about 17 letters used)? The test: anneal shuffles of the target's own code stream (same
multiset, order destroyed) with exactly cheap_test_1/rerun.sh's settings.
Job:
(1) Reproduce one target seed from rerun.sh (marks variant, seed 3) to confirm the setup reads about -1154.
(2) Build 5 shuffles of cipher_codes.tsv (seeds 1-5, a committed script cheap_test_1/shuffle_control.py that writes shuffled_s<k>.tsv) and anneal each
    with the same corpus, --restarts 8 --iters 40000, one anneal seed per shuffle; also 2 extra anneal seeds on shuffle 1 to see the spread.
(3) Also shuffle within lines only (keeps line-level profile, destroys word order): 3 shuffles, same settings.
(4) Report: target best, matched-control best (on file), shuffle best/mean/range, line-shuffle best/mean. Verdict rule, fixed in advance: if the full-shuffle
    mean is within 40 points of the target (i.e. above -1194), the gap is profile, not sequence, and the reading's anneal basis is void; if the shuffle
    mean sits at or below the matched-control band (-1321.7 to -1335.5 +/- 40), the sequence carries the gap. In between: say so with the numbers.
Write: cheap_test_1/shuffle_control.py, cheap_test_1/shuffle_*.json (the anneal outputs), and ciphers/espagnol142-mercy-1648/shuffle_control.md (a short
section with the table). Append the one-line command to rerun.sh. Do not edit NOTES.md, AUDIT.md, key.tsv or reading files.
ROOM done: "done: for LANE R7: mercy shuffle control -- target -1154.3 vs shuffle mean <x> (range <a>..<b>) vs matched control -1321.7; line-shuffle <y>; verdict <sequence|profile|between>".
