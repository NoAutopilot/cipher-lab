LANE R4 WORKER E -- BOWES 1583 NUMERICAL NAME-CODES: collation and identifications (Opus, cap $5; disk and printed text only).
Target: ciphers/bowes-walsingham-1583 (status partial). Common rules: .claude/briefs/runs/2026-09-24-lane-r4-common.md.
Read NOTES.md "Solver session (23 September 2026)" and "Specialist reply, 24 Sept 2026 (Cryptiana)" first.
On disk: corpus/correspondenceof00bowerich_djvu.txt (Surtees Society, Correspondence of Robert Bowes, 1842), reading.tsv, key.tsv,
ciphertext.txt. The check source is CSP Scotland vol. vi (1910). If its text is not on disk, find it on archive.org (advancedsearch
API, then the item's _djvu.txt) -- host archive.org only, at most 6 requests, >= 3 s apart; save to corpus/ with manifest.json. No
image fetches.
1. Scripts read: extract every numerical code (all numbers in the Letter-Book passages that stand for persons or places, both letters
   and the Caligula B VIII fragments) with 200 characters of printed context each, from the Surtees text and the calendar; write
   codes.tsv (code, letter/date, page, context_surtees, context_csp, other occurrences).
2. Fix 189 = Montrose, grade C (Tomokiyo's check: the print's "Montrosse" stands for 189 in the manuscript).
3. Propose identifications for 870, 149, 19, 29, 85 and every other code: grade C only where the 1910 Calendar (or the 1842 print)
   names the person at that same place in the same sentence of the same letter; else M with the reasoning in one line (who fits the
   context, and what would settle it). Cross-check consistency: one code, one person, across every occurrence.
4. Write codes.tsv with the grade column, update reading.tsv/key.tsv only for C grades, keep check.py (or tools/decode_key.py --check)
   exiting 0, and add NOTES.md section "Numerical name-codes (24 Sept 2026, LANE R4 E)" with counts C/M/unread.
Report what was found and where it was not found; do not classify novelty. ROOM done line ends "for LANE V4: ciphers/bowes-walsingham-1583
name-codes ready" if any C identification beyond 189 lands.
