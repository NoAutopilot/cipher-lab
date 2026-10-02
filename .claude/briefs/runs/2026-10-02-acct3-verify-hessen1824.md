# VERIFY-HESSEN-1824 (2 Oct 2026, written by account 3; runs on account 2): found-solved check and N-class

Model: Fable while it answers, else Opus 5.5. Cap USD 4, box 45 min. You are a verifier (CLAUDE.md "Verifier brief"), not a solver.

Claim under audit: account 2's SOLVERDIFF-BOURDEAU (2 Oct 2026, sources/solver-diffs/2026-10-02-bourdeau.tsv) found that
ciphers/hessen-1824 (HStAM 9 a Nr. 259 f.249, HCPortal 513; ours: `partial`, with a NEAR.md row) was read in full by
D. Bourdeau on 28 Sept 2026: https://github.com/dbourdeau/cyphersolver/blob/main/targets/hesse1824/NOTES.md and
https://dbourdeau.github.io/cyphersolver/hesse1824.html (the decipherer's own Anmerkung on the leaf gives the method:
sympathetic ink, the key table, running key letters b-g over the cipher; first word "schiket").

1. `python3 tools/room.py --start`; claim in ROOM.md.
2. Confirm it is the same leaf (shelfmark, HCPortal id, image) and that his reading regenerates: apply his stated key and method
   to OUR transcription (ciphers/hessen-1824) with a short script under ciphers/hessen-1824/bourdeau_check/, and report the
   per-token agreement with his plaintext (his code is MIT; cite it). Note where our transcription differs from his.
3. Write ciphers/hessen-1824/AUDIT.md: class N0 (plaintext and decipherment of this very item already known), key source
   `published` (Bourdeau 28 Sept 2026, credited), earliest citation, the safe sentence, and that our own work (bHCP, family
   runs on the de20 corpus) did not reach it -- with the lesson that the leaf's own Anmerkung was the crib.
4. Then, because the class is set: change the first status line of ciphers/hessen-1824/NOTES.md to `found-solved` (add a dated
   line under it citing AUDIT.md), remove the hessen-1824 row from NEAR.md AND from status.json's `near` list (keep them in
   step; run `python3 tools/near_check.py`), and set the target's status.json entry to found-solved with key `published`,
   text `known`. Append to the finish-or-blocker section in NOTES.md a line: "Superseded 2 Oct 2026: found-solved (AUDIT.md)."
5. Commit by explicit path, `python3 tools/file_shrink_guard.py <paths>`, `python3 tools/room.py --push <paths>`, done line.
Do not decode beyond the check in step 2; do not touch other targets.
