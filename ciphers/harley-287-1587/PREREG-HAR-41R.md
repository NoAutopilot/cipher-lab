# PREREG-HAR-41R (15 Oct 2026, 16:3x UTC by date -u), pushed before any image fetch, read or score

Job: `.claude/briefs/runs/2026-10-15-ytbiz-default-1616-jobs.md` "HAR-41R". Unit: BL Harley MS 287 f.41r (DECODE R8480 P1), the
cipher block of about 7 lines and the running clear version in the left margin (HAR-39V2 by eye on a reduced copy). Key under test:
Bourdeau's needham1587 three-grid pigpen (github.com/dbourdeau/cyphersolver targets/needham1587, commit 0445769; MIT code / CC BY 4.0
text), unchanged: J=⌟ U=⊔ L=⌞ / C=⊏ O=□ F=⌜ / N=⊓ 7=⌝ D=⊐; plain a-i, dot below k-s, dot inside t u w x y z (no j; u = v).

Image: one DECODE browser login (`tools/decode_browser_login.js 8480 --guess-fullsize --fetch-page RecordsView/8479`), scratchpad only.
R8479 P4 (f.39v, sha1 7076557b0b0e) is fetched in the same login only for the reader control below.

Crops (`tools/iiif_lines.py --image`, command pasted in NOTES before the first reader call): cipher rows cut tight to the box-sign row,
the interlinear gloss and the margin out of view; the margin clear text cut separately. Runs = cipher lines; at most the first 4 are read
(if the block has more, said so).

Readers (all blind): one Opus subagent call per cipher run, given only that run's crop(s), the nine shapes described by their strokes
exactly as in Bourdeau's table above (not by grid cell -- HAR-39V2's naming error), the three mark states, and asked for shape+mark per
sign with '|' at word gaps and '?' for an unsure sign. Never told the key, any plaintext, the margin, the gloss or Bourdeau's strings.
Reader control: call 1 also gets the f.39v line G crop of words 1, 5, 8 (channel, hoyes, fastened; 19 signs, HAR-39V 19/19), labelled
in random order with the run crop, not told which is a check. Control gate: >= 17/19 signs equal in shape and mark to HAR-39V's
tx/f39v_lineG_har39v.tsv. Control FAIL -> the target score is reported but labelled a non-test of the key.
Margin: one Opus call reads the margin clear text from its crops only (never shown the cipher crops). One further unit only if budget
allows: a blind re-look (Opus) at the signs the readers marked '?', from the same crops.

Normalisation (rule 3, PX-BRODEC), identical on decode and margin: lowercase; letters only; j->i, v->u, y->i, w kept; collapse doubled
letters; "yt"->"that", "ye"->"the", "&"->"and", "L."/"Lo."->"lord"; '?' signs decode to '?' (cost 1 against any letter).

Statistics. D = key decode of the read runs concatenated (word gaps dropped for S1); M = normalised margin text.
- S1 = 1 - ed(D, M[best substring]) / len(D), ed the semi-global edit distance (D aligned in full, free start and end in M).
- S2 = fraction of decoded cipher words with >= 3 letters that occur as an exact word in the normalised margin word list.
Null: 1000 value-shuffled keys (random.Random(41)): the 24 letter values permuted among the 24 sign forms, the read sign strings fixed;
S1 and S2 recomputed per draw; p95 and fraction >= real reported. The shuffle changes the letters the decode yields, which is what both
statistics measure, so the null can fail differently from the target (rule 3 bCAS/AX-5799 clause).

Gate (fixed now):
- A: S1 > p95(S1_null) AND S1 >= 0.60 AND S2 > p95(S2_null), control PASS -> the key reads f.41r's block against the margin; aligned
  signs matching the margin are C (known plaintext), the rest M.
- B: S1 > p95 and S2 > p95 but S1 < 0.60 -> key holds, reader or margin-paraphrase noise; report the aligned pairs, grades stay M.
- C: S1 <= p95 or S2 <= p95 -> non-test or key does not hold on this leaf; the control and the '?' share decide which; reported as such.
- Margin extent: if the crops cannot fix which margin lines run beside the cipher block, S1's free-end alignment covers it; a margin read
  under 40 letters makes the test a non-test.
Units priced: ~4 cipher calls + 1 margin + (1 re-look) at ~0.6-1.0, floor ~1; stop before a unit that would cross 80% of cap 4.5 or box.
No key.tsv edit (Bourdeau's key is used, not changed); a sign that conflicts with the margin under an agreeing alignment is logged as a
candidate, not a key change.
