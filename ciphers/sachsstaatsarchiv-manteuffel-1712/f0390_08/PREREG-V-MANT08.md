# PREREG-V-MANT08 (verifier V-MANT08, account 2, LANE FAMILY, 8 Oct 2026, pushed before any depth ruling)

Depth bar (copied from .claude/briefs/runs/2026-10-08-acct3-depth-bar.md, applies CLAUDE.md rule 4a literally):
- Cipher clause: a contiguous H/C/S stretch longer than the authentication distance (AD, about 1.5 x unicity; H(K) = key space
  plus every liberty: M tokens, r|re|ro and o|ou|ous choices, repairs). An unfitted external key does not shrink H(K).
- External check: a D3/D4 element; does NOT replace the clause at D2.
- Code clause: a code value that reads sensibly in >= 2 independent contexts; an H/C grade alone does not satisfy it; a verbatim
  repeated phrase counts once.
- D2 = one clause plus the verifier's own true, specific sentence about the content, written from the reading. Otherwise D1.

Unit: each frame (letter) is an item: 0390 (10 Oct 1712), 0391 (P.S. 13 Oct 1712), 0395 (Oct 1712), 0485 (Nov 1712).

How the code clause is tested here (fixed before ruling). FAM-MANTV flagged that tools/depth_stats.py builds its value window
from cipher tokens only, so on leaves where each code is an island in clear French the window splices neighbouring runs, not the
real context. These four leaves have that shape (singleton nomenclator codes in clear text). So the clause is tested on the real
clear-text context read by the verifier from the image, not on depth_stats windows:
- a code value counts if it occurs >= 2 times on the item in two different, non-verbatim clear sentences;
- each occurrence's sentence must read sensibly with the key value (Krauske table, as in key.tsv) and the same sentence must NOT
  read sensibly with a generic substitute of another class (a place for a person or vice versa) -- a coarse class check;
- the value must be consistent with at least one independently letter-spelled run of the same item (e.g. a sovereign code beside
  that sovereign's ministers spelled letter by letter), since a singleton sovereign code in diplomatic prose is otherwise near
  certain to "read sensibly" for any sovereign.
- Codes that recur only because the transcription missed them are counted only if the verifier sees them on the image.
If no code meets all three, the item holds D1 (or D0 if nothing reads). The cipher clause is computed from the longest all-C run
in letters against AD as FAM-MANTV computed it (AD ~127-138 letters for this key at these sizes); it is expected to fail.
