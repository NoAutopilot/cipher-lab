# PREREG-F5160-WORD: word-placement (dictionary-constrained) solver, matched control on control_pool.txt (9 Oct 2026, written 14:3x UTC by date -u, before any score)

Worker F5160-WORD (account 4, Opus), LANE DEFAULT-account-4-20261009-1340, job J12. A different instrument from the
two failed nomenclator_anneal.py runs (25.7% at 752 tokens, 24 Sept; 26.0% at 972 tokens, F5160-POOL): the *score* is
unchanged (nomenclator_anneal.Problem, same fr16 order-5 model rebuilt without control paragraphs, same prior, same caps,
under which the true control key already beats every key found by 703-1051 nats), the *search* changes. F5160-POOL
diagnosed the failure as search, not scoring; this tests that diagnosis.

**Why a private script (`word_solve.py`).** No shared tool fits: `tools/family_run.py` always builds its own control and
cannot score against the committed `control_pool.txt` / `control_pool.truth.json` the brief names; its `wordcode` family
has letters and whole words but no syllable values (this design has 94 syllable signs, 80% of the control's tokens);
`tools/segmenter.py` divides a decode, it does not search a key. `word_solve.py` imports nomenclator_anneal.py's
Problem/eval unchanged and adds only the move set.

**Move set.** Per iteration: with p = 0.5 a *word placement*: a random window of k = 1..6 consecutive cipher tokens inside
one cipher run, and a French word drawn (weight sqrt of its count) from the fr17 lexicon (tools/data/fr17, folded by
italian_ngram.norm, the 4,000 commonest word types of length >= 2 with count >= 3, plus 'a' and 'y'), split into exactly k
pieces each a value the design allows (letter, one of the --syl cv + control_1653_syl.txt syllables, one of the 16 words);
the window's signs take those pieces (a sign twice in the window must take the same piece; a fixed sign must already hold
its piece); otherwise the same single-sign / swap move as nomenclator_anneal.anneal. Metropolis on Problem.score, T0 2 ->
T1 0.02 geometric, the F5160-POOL caps (max-syl 100, max-word 16, max-null 3, max-homo 4), the same four fixes S8=de
S91=ques S32=le S43=se, 4 restarts (seeds 7000-7003), greedy single-sign polish at the end (nomenclator_anneal.polish).
Iterations per restart: fixed from a timing run of 20k iterations whose output is not evaluated, so that 4 parallel
restarts fit in about 20 minutes; the figure is reported, the gate does not move with it.

**Gate (control), unchanged from PREREG-F5160-POOL**: token accuracy (nomenclator_anneal.py eval against
control_pool.truth.json) of the **highest-scoring** restart >= **0.60**. Also reported: max token accuracy over restarts,
letter accuracy, best score vs the true key's score (-2978.9 on file).
- PASS -> run the four real letters (`real_pool.txt`, 972 tokens) with identical settings, fixes = the key_1659 signs the
  1653 pieces carry for de/ques/le/se as in F5160-POOL's prereg; any output is a candidate only (grade S at most after a
  judge under fr17, rule 7; no reading reported without the judge output).
- FAIL -> no target run. HYPOTHESES.md row: word-placement search on the nomenclator_anneal score, control below gate;
  rule 3's third-attempt clause then applies to the *score/model* shared by all three attempts if the best key still
  scores below the true key (search) or above it (model).
