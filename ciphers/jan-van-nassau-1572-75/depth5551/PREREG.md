# D3-5551 PREREG (8 Oct 2026; account 4, LANE DEPTH)

Order note: written at 18:50 UTC by date -u, AFTER the one `tools/depth_stats.py` run in this folder (18:50 UTC). The run used
the tool's documented defaults (cipher class len<=3, shuffle classes, seeds 8100-8199) and the era-matched German corpus
tools/data/de1600 (de16 is a model-composed 8.5 KB text with no .txt.gz, which the tool cannot read); nothing was varied
after seeing the result, and no second run was made.

Depth bar copied literally from .claude/briefs/runs/2026-10-08-acct3-depth-bar.md:

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

Command:
python3 tools/depth_stats.py --tokens ciphers/jan-van-nassau-1572-75/reading_5551_full_tokens.tsv \
  --key ciphers/lodewijk-van-nassau-1573-74/key_full.tsv --line-prefix L --cipher-class 'len<=3' --shuffle classes \
  --seeds 8100-8199 --out ciphers/jan-van-nassau-1572-75/depth5551 --corpus tools/data/de1600
