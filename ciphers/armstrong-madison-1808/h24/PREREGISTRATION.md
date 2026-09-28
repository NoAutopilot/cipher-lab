# H24 pre-registration (written 28 Sept 2026, 00:39 UTC clock read, before any reader output existed)

Instrument: a Sonnet subagent that sees ONLY (a) one period alphabet plate and (b) line strips of shorthand, and
returns letters per word. No text, title, author or system name is given; web tools are forbidden in the prompt.

Known-answer control per system (run FIRST, rule 3 / family_run.py order):
- Mavor 1792: plate `images/shorthand/specimens/mavor1792_alphabet_plateI.jpg`; specimen = the book's own Plate V,
  Job xxix 7-22 (archive.org bim_eighteenth-century_universal-stenography-o_mavor-william-fordyce_1792 leaf 74),
  lines 1-4 (`h24/specimens/mavor_plateV_line{1..4}.jpg`). Reference: KJV Job 29:7-22.
- Byrom 1796 abridgement: plate `images/shorthand/specimens/byrom1796_alphabet_p12.jpg` (typeset consonant list);
  specimen = the book's own Plate I, the Lord's Prayer and Psalm 1 (leaf 94; contents leaf 93 says "Common Prayer"),
  lines 1-4 of the plate body (`h24/specimens/byrom_plateI_line{1..4}.jpg`). Reference: BCP and KJV texts, best of the two.

Scoring (`h24/score.py`, fixed before the reads):
- Normalize reader output and reference to consonant skeletons: drop a e i o u y, map c/q->k, j->g, z->s, x->ks,
  ph->f, collapse doubles.
- S1 = Smith-Waterman local alignment (match +1, mismatch -1, gap -1) of the reader's concatenated skeleton
  against the reference skeleton, reported as matched consonants / reader consonants.
- S2 = number of reader words (skeleton length >= 2) whose skeleton equals some reference word skeleton.
- Null: 200 random bijections of the consonant alphabet applied to the reader's output, S1 and S2 recomputed;
  p95 of each.
- CONTROL PASS iff S1 > null p95 AND S2 >= 3 AND S2 > null p95. Otherwise CONTROL FAIL = the instrument cannot
  read this system from its plate at this reader; the target is NOT read with that system (non-test, not a
  negative on the system).

Target read (only for a system whose control passes; at most 2 calls in this step): the same reader, same plate,
given the target's pure-mark lines (page 1 L09, L12, L13 and page 3 L13 crops from `images/shorthand/`), returns
letters per word. Scoring: T2 = number of reader words (skeleton >= 3) whose skeleton matches a word skeleton of
the en18 corpus (tools/data/en18), against the same 200-bijection null; a target result is "worth a look" only if
T2 > null p95, and is reported as M-grade candidate words with their neighbouring code groups, never a reading.

Budget: 4 vision subagent calls max, cap 6 USD over the claim-time cost (2.09 USD at 00:36 UTC).
