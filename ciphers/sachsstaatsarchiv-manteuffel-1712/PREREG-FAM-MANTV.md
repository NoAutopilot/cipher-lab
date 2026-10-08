# PREREG-FAM-MANTV (verifier FAM-MANTV, account 2, 8 Oct 2026, written before any depth statistic was computed)

Items: A = Loc. 694/09 URL files 0015+0016 (f.8-8v, Gersdorff relation 3 Jan 1713, enclosed to Manteuffel 13 Jan 1713), 69 tokens,
f0015_09/reading_tokens.tsv; B = 694/09 0052 (slip beside the extract sent with Manteuffel's letter of 11 Feb 1713), 43 tokens,
f0052_09/reading_tokens.tsv. Already computed before this file (re-derivation, not depth): decode_key --check exit 0 on ., f0015_09,
f0052_09; shuffle gates re-run at fresh seeds 77113 (A: 0/1000 >= real, p99 -1.597 vs real -1.010; power 1/1000) and 77152
(B: 1/1000, p99 -1.553 vs real -1.394).

Depth statistics, as DEPTH-MH did for f.410 (same tool, same options): `python3 tools/depth_stats.py --tokens <item tokens>
--key ciphers/sachsstaatsarchiv-manteuffel-1712/key.tsv --cipher-class 'code<=120' --shuffle classes --seeds 8100-8299
--out <item dir>/depth_mantv` (corpus default fr18).

Rulings (no other rule used):
- Cipher clause met iff the primary longest H/C/S run (cipher codes 1-120 only) > AD at model R. Expected to fail (runs <= 21 tokens).
- Code clause met iff a code-class value occurs in >= 2 independent contexts (verbatim repeats once), each context reads sensibly to
  me (reading written out below in AUDIT.md with its liberties), and control (ii) puts each counted context's 8+value+8 window above
  the 200-shuffle p95. The C grade on the code does not by itself meet it. Candidate before computing: 198 (Stanislas), 0015 r3 and
  0016 r1.
- D2 = one clause + my own true, specific sentence about the content written from the reading. An external print (Colyer to
  Heinsius, 12 Nov 1712, Heinsius Briefwisseling Deel 14 no. 336) may confirm the sentence, never supply it. Otherwise D1 (or D0).
- D3 needs >= 80% H/C/S; A is C 47/69 = 68.1%, so D3 is out whatever the statistics say.

## Depth bar (copied verbatim from .claude/briefs/runs/2026-10-08-acct3-depth-bar.md)
Source: acct3-next-jobs-scout critic (wf_e0950d6a-d50) found four depth rulings would otherwise disagree on whether an external check or an H/C code grade admits D2. This applies CLAUDE.md rule 4a literally; research/DECIPHERMENT-STANDARDS-2026-10-04.md section 3's alternatives are NOT adopted. Changing this is an owner decision (ASKS row).

- CLAUDE.md 4a governs where it differs from the research note.
- Cipher clause: a contiguous H/C/S stretch longer than the authentication distance (AD) for the design, about 1.5 x unicity.
  - H(K) = the design's key space plus every liberty the reading took: U wildcards, M tokens, r|re|ro and o|ou|ous choices, repairs.
  - An unfitted external or period key does NOT shrink H(K) to the liberties alone.
  - The zero-liberty (H_lib+20)/R reading (about 6-8 letters here) is not used.
- External check: an external check (key agreement with period glosses, a period key sheet) is a D3/D4 element under CLAUDE.md 4a. It does NOT replace the clause at D2, although research section 3 offers it as an alternative.
- Code clause: a code value that reads sensibly in >= 2 independent contexts.
  - An H or C grade on the value does not satisfy this on its own, although research section 3 says 'or carry H/C grade'.
  - A verbatim repeated phrase counts once (lodewijk precedent).
- D2 = one clause plus your own true, specific sentence about the content, written from the reading. Droysen or Fagel 5177 may confirm the sentence, never supply it. Otherwise hold D1.
- If you think the convention is wrong, post one ROOM flag for the parent and still rule under this bar.

