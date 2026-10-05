# Pre-registration: two-pass blind sign-by-sign transcription of f.88r (R8492), A4-RFHAR, 5 Oct 2026

Committed before either pass ran. Question (NOTES.md Verdict, "cheapest next"): does a blind sign-level transcription of
f.88r, read with only the gloss-confirmed core values (RUN1-HAR masked read, grade C: # n, + b, 7 e, 8 c, A s/t, D d,
G g, H f, U a, z o, d o, y r/y), carry the key's signal, so that its unread runs can be worked from it?

Material. DECODE R8492 full-size image IMG_R8492_I39196_P1.jpg (one login, 5 Oct 2026 23:4x UTC, sha1 in
images/decode_sha1.txt, not committed), cut into 23 lines x 2 segments by
`tools/iiif_lines.py --image .../IMG_R8492_I39196_P1.jpg --region 2050,600,4500,3800 --centres 258,...,3662
--lines-per-crop 1 --max-width 2450 --overlap 120 --follow-slope 400 --slope-local --out images/f88r --prefix f88r`.
Crops checked by eye (L01, L07, L21, L23).

Readers. Two blind Sonnet passes, one call each over the 46 crops of this one page (`gloss/PASS_PROMPT_f88r.md`, the
same sign code as A2-HAR7/RUN1-HAR, no key values, no reading, no repository file named but the crops). Replies written
unchanged to gloss/passA_f88r.tsv and gloss/passB_f88r.tsv. f.88r has no interlinear gloss, so nothing is masked.

Reconciliation. Mechanical only (`gloss/score_f88r.py`): per band, difflib on tokens; agreed tokens kept, every split
or gap becomes ?. No eye arbitration (this worker has read Bourdeau's f88 strings and reading).

Statistics (`gloss/score_f88r.py`, docstring): err_2reader; L = share of eligible cipher words (3-10 signs, at least
half core signs) whose core-letter pattern matches a word of the same length in the 30,000 most frequent entries of
Bourdeau's wordfreq.tsv; control = L under 1000 random permutations of the core letter sets among the 12 core signs
(seed 88). The control changes exactly the quantity the test reads (which letter a core sign carries), so it can
fail differently from the target. Reported, not gated: L per pass; agreement of the reconciled string with Bourdeau's
f88 sign strings against a shuffled-run control; the words whose core pattern has exactly one lexicon match (grade M
candidates only, never readings).

Gates.
- G1: err_2reader <= 0.30. Fail -> the transcription is too noisy to license G2 either way ("non-test at this
  agreement"), whatever L reads.
- G2: L > control p95. Pass (with G1) -> the core values read on f.88r at this transcription; the reconciled string is
  usable as the solver input for the unread runs. Fail (with G1) -> the core values do not separate from a permuted
  key on this leaf at this N; logged as a measured negative for this instrument, not for the key.
- No ciphertext token is graded above M by this job.
