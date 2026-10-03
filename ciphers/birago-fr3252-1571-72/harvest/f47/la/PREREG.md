# NEVBIR-47C pre-registration (3 Oct 2026, written and pushed before the third reader runs)

Input: recon_norm.tsv (770 signs, 197 '?' or split positions) and recon_norm_agreement.tsv (two blind Sonnet passes, NEVBIR-47).
Tiles: the 197 positions whose two readers split (f47_split_tiles.tsv, built by `tools/lookalike_pass.py packet`, filtered to
why=split). The 60 gap positions (one reader saw a sign the other did not) are not in recon_norm.tsv and stay out, as before.
Third reader: one value-blind Opus subagent, prompt f47_reread_prompt.md (crops, blind sheet with ids only, f.36 reference
tiles; no key, no map, no pass files). Output f47_reread.tsv.

Rule (fixed now, `tools/lookalike_pass.py reconcile`): a firm re-read (conf H or M, not SPLIT) that matches reader A or B settles
the tile at 2-of-3 with that label; anything else stays '?' (UNSETTLED) and goes to focus.tsv. passD.tsv is the primary
sequence; passD_alt.tsv (every firm re-read) is a pointer only, never reported as the reading.

Test, unchanged from NEVBIR-47: `decode_control.py passD.tsv --shuffles 200 --windows 20 --err 0.33 --extra X_THETA2=r
--seed 1,2,3`, E = 0.33, the TWO-READER measured disagreement (LESSONS.md "Look-alike pass": the 2-of-3 residual is agreement,
not accuracy, and is never used as the control error). Judge: tools/judge_plaintext.py specs/ceppo-nevers-fr3251-1570s.json.

Grades: a decoded letter is S only if (i) the key ranks 1/201 on passD in all 3 seeds, (ii) power >= 18/20 at E, (iii) the
judge PASSes on passD's letters, and (iv) its sign is agreed or settled 2-of-3. Without (iii) every letter stays M and '?' U,
whatever the z. A fragment is reported as readable only if it is an Italian word of 4+ letters with every sign agreed or settled.
