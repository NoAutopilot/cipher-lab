# BIR-OWNER (account-3 worker, 3 Oct 2026 18:3x UTC; owner: "try it as is, see if it helps")

Targets: birago-fr3252-1571-72 (f.117r), nevers-birago-fr3251-1572 (f.168, f.144r). Opus 5.5. Cap USD 5, box 40 min. Vision 0.
Claim in ROOM.md first; done line at the end. Commit first, then fetch/rebase/push (no --autostash with pending edits).

Input: the owner's PARTIAL sorter decisions, dumped to
ciphers/nevers-birago-fr3251-1572/harvest/tx_decode/eye/open/sorter/owner-2026-10-03/ (moves/ 142 docs as {from,to,sid}, newpiles/ 26,
piles/ 1, checked/ 0; signs.tsv + labels.tsv = the joined page inputs). Read that folder's README and ../README.md ("How the owner's
picks are used") first.
1. Run tools/sign_sorter_apply.py on the dump (adapt only the input path handling if needed -- the files are flat JSON per doc, not the
   live db; add an option to the tool rather than a private copy, with its offline test). Output: settled sid -> sign table.
   Moves to OUT (taken out, not yet placed) = unsettled; auto-named new piles (T51-b, X_NEW-c ...) = new sign labels with no key value.
2. Pre-register before any score (commit): the grade rule = S only where the owner's pick agrees with at least one blind instrument
   (A1-BIR-VERIFY two-option; BIR-OPEN/BIR-OPEN-144 open-choice) on the same position; owner-only changes stay M; owner picks that move a
   sign into an auto-named new pile make that position U (no key value) unless the key already covers that shape. The comparison:
   judge score (fr for f.117r, it for f.168/f.144r) of (a) the current reading, (b) the reading with owner picks applied under the rule,
   (c) a control: the same number of changes applied at random positions with random in-family labels (200 draws) -- the owner's picks
   "help" only if (b) beats (a) and beats the control's p95.
3. Also report per-leaf agreement of owner picks with each blind instrument on the positions where both exist (counts), and how many of
   the 24 "Check these first" tiles the owner answered.
4. Apply nothing to the committed readings unless (b) passes the pre-registered gate; either way write a NOTES.md section in both folders
   with the numbers and the judge lines; decode_key --check; gaps_check; file_shrink_guard. Report in plain words: did the owner's sorting
   help, by how much, and what to sort next (the positions that would move the score most). No novelty classification.
