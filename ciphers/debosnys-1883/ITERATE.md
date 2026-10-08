# debosnys-1883 -- ITERATE.md (standing lane DEB-RUN, account 4)

Framework: `.claude/briefs/runs/2026-10-07-acct3-standing.md`. One table, appended, never rewritten. Status of the
target stays `open` (NOTES.md line 1); nothing is read. Public material only in this file (RESTRICTED.md).

## Seed: instrument families already run (from CAMPAIGN.md H1-H65 and swarm/DIGEST-1, DIGEST-2; 28-29 Sept 2026)

Compressed, not re-run. "dead" = control-backed negative for that design at the current transcription (14-18 pct
sign error on c1/c2, 7-12 pct on the verse; public pixels are the limit, R2-2/H51/H63/H65).

| family | verdict | deciding numbers (source) |
|---|---|---|
| homophonic letters FR / EN / PT, line order | dead | A 0/8 vs ctl 5/8; B 8th pct vs ctl 100/100; G 0/24 vs ctl 4/4; D order battery 0-1/40 (DIGEST-2 s6) |
| any order-keeping letter/syllable design on c2 | dead up to ~30 pct noise | R2-1 real 0.27-2.56 vs thresholds 5.1-5.6; H60 battery still separates at 30 pct |
| periodic polyalphabetic, autokey, word code (60 words) | dead | D escape.py, controls read each |
| columnar transposition / vertical writing (stream heights 2-60) | retired (rule 3 third attempt) | R34 lead p 0.03 fragile; H62, H64 controls failed: untested-by-this-tool |
| Masonic / Copiale alphabets, Copiale word symbols | dead | F, H |
| X as word space | dead | D, F, E3 |
| c4 = contiguous copy of 8 pool texts | dead | R2-3 |
| c3 clear poem / Greek verso (Gaffney) as crib | dead | H4 0/24, H17 0/48, planted clears at 15 pct |
| automatic solvers (homophonic, syllabic, Copiale method) | untestable until noise < ~5-8 pct | C, H, GOLD-D1 curve |
| running key, word-internal anagram, random nulls >= 35 pct drawn from the text's own curve | NOT excluded (order tests blind to them) | escape2.py |
| better transcription from public pixels | retired (H61 folds do not carry, H63, H65 classifier) | public pixels are the limit |

Positive structure on record (licensed): one key across all four (H15/H52); couplet rhyme at line ends on c4 (H5);
pictograms open lines (H31/H35, p 0.0002); X uniform inside lines but avoids line edges (H19); WAVE bound to PCT (H48);
the real sequence is closest to signs drawn iid from a table (D).

## Attempts (DEB-RUN)

| date | hypothesis | instrument | matched control | result (both numbers) | verdict | what it taught |
|---|---|---|---|---|---|---|
| 2026-10-07 21:5x | H66: c2 = homophonic letters + nulls in their OWN sign types (disjoint from text signs), q 0.35/0.50 | `h66/h66_null_types.py` greedy type elimination maximising S=z(mi1)+z(bg2)+z(rep3) vs within-line shuffles; search-null = same greedy on shuffles (PREREG committed 5119505a before scoring) | FR homophonic + disjoint null types at q, c2 lengths/curve, 15 pct noise, 10 seeds per q | control beats own search-null p95 in 0/10 (q .35, p95 24.8) and 2/10 (q .50, p95 24.1); null-type precision 0.17-0.61 = base rate; real c2 S_max median 18.1 vs its search-null p95 28.0 (20 pct of nulls >= real) | **non-test** (no passable control at c2 N with this instrument) | greedy max over ~80 types is dominated by selection inflation (search-null spans 8-28); a selector must be scored out of sample. Next best attempt: H67, same design, types chosen on one half of the lines and S scored on the other half (honest null, no search-null needed) -- cheap CPU, same control. |
| 2026-10-07 21:5x | H67 (planned): H66 with out-of-sample selection (fit on alternate lines, score held-out) | `h66/h67_cv.py` (smoke run only: control q .50 seed 1 CV 0.52) -- battery NOT run after the oracle below | oracle ceiling: the H66 control with its TRUE null types deleted by hand, S at 200 shuffles (`h66/h67_oracle.py`, `oracle.json`, `oracle_pooled.json`) | c2 shape: oracle S -1.0 to 11.5 (median ~3), half-lines -3.0 to 5.1; pooled c1-c4 shape (N 1138, one key per H52): oracle 3.0-10.5 (median ~5.5), half-lines 1.1-7.1 (median ~3.4) | **untestable at this N and noise** (any type selector is bounded by an oracle that barely clears a shuffle null) | the order family is now spent for every nulls design (curve-drawn: escape2; type-disjoint: here): at 15 pct noise even a perfect null-stripper leaves too little order on 1,138 signs. Nothing on public data moves this further; the lever is noise (hi-res images, H18/DEB-HIRES-REQ) or new text (museum scans, private repo). Next best attempt: a private-repo row for account 4 -- an inventory of what has been done on the 43 museum scans, then a sign-match pass for cipher signs, monograms or numerals inside his clear writings (a crib route no order test needs). |
| 2026-10-07 22:3x | DEB-PRIV1: sign-match crib pass on the museum scans (private) | step 1 inventory of the private repo only (no image calls) | -- (inventory; no test run) | earlier private rounds (1 Oct) already cover parts (a)-(c) of the brief; part (d), letter-form habits, never run | non-test (stopped at step 1 per brief) | held per RESTRICTED.md; next best attempt: a (d)-only pass with decoy hands, ~$7.5, private repo, account-4 standing session |
| 2026-10-08 00:5x | (record) ATTEMPTS.md for the owner's museum note (due 10 Oct 18:00) | Sonnet drafter from CAMPAIGN/HYPOTHESES/ITERATE/DIGESTs; lane review corrected 15 sentences against source (couplet rhyme 4-5/9-10 not all, Sp/La control power order, H17 0/48 each, numerals 31 not 9, X-as-null contradiction with H39, Cipher Mysteries attribution) | -- | -- | written (draft for owner review) | the record exists; next public-side work waits on DEB-PRIV1D/2A/2B (private) or new material |
| 2026-10-08 01:4x | DEB-PRIV1D: frequent cipher signs share a form with a letter habit of his clear hand (private) | 11 Sonnet shape-match calls on line crops vs a 14-sign reference sheet built from the public glyph crops; 2 public non-Debosnys 19th-c. decoy hands per item | positive control: same prompt on PUBLIC cipher-line strips (c2a L03-06, c4a L03-06) that contain the reference signs: 0 of 4 items answered yes; decoys 0 | NON-TEST: the reader never answers yes even where a match is certain | non-test (positive control failed) | target result held per RESTRICTED.md; the instrument must be validated on the public positive control before any rerun (reworded similarity-score prompt, gate >= 6/8 signs found on cipher strips, decoys <= 1), ~$5 |
| 2026-10-08 01:5x | DEB-PRIV2A: the museum material is a better transcription source (private gate) | registration of the public cryptogram images to the museum scans; known-answer page by the swarm/R2/R2-2 t_low.py recipe (96 targets, tiles from the museum image), two blind Opus readers, PREREG pushed first (private) | public-image control of the same recipe (R2-2): 15.6 pct | held per RESTRICTED.md (private repository, debosnys/HELD-FROM-PUBLIC-2026-10-08.md) | held | held; DEB-PRIV2B not run |
| 2026-10-08 04:4x | DEB-PRIV2A2: the public truth labels on PRIV2A's agreed-but-different control tiles are wrong (private) | one blind Opus adjudicator over the source boxes behind those tiles + decoy boxes graded H in the public draft, candidate ids in random order, PREREG pushed first (private) | decoys: adjudicator must keep the public truth on a pre-registered share | held per RESTRICTED.md (private repository, debosnys/HELD-FROM-PUBLIC-2026-10-08.md) | held | held; DEB-PRIV2B not run; no second model adjudication of the pair; next: the owner's sign sorter (ASKS 151) |
| 2026-10-08 04:4x | DEB-PRIV1D2: frequent cipher signs share a form with a letter habit of his clear hand (private; second attempt at the PRIV1D instrument) | 0-5 similarity score per crop x sign, 14-sign reference sheet from public glyph crops, 11 Sonnet calls on clear-hand line crops + public decoy hands; PREREG pushed first (private) | positive control on PUBLIC cipher strips: 7 of 8 signs found at >= 3, 0 false finds on decoys (PASS); specificity weak: absent signs also scored >= 3 in 36 pct of strip pairs vs 72 pct for present signs | held per RESTRICTED.md (private repository, debosnys/HELD-FROM-PUBLIC-2026-10-08.md) | held | held; next: a person checks the pointers (ASKS 151); no third model attempt at this instrument (rule 3) |

## Retrospective after wave 4 (DEB-RUN, 8 Oct 2026 07:2x UTC by date -u; attempts H66, H67, DEB-PRIV1, PRIV1D, PRIV2A, PRIV2A2, PRIV1D2)

- **Moved anything:** only the instruments that change the evidence, not the statistic. PRIV1D2's reworded instrument
  passed its public positive control (7/8, 0 false finds). Results of the private runs (PRIV2A, PRIV2A2, PRIV1D2) are
  held per RESTRICTED.md.
- **Never moved:** every order statistic on the public transcription (H66 selection, H67 oracle).
- **What the data say the cipher is NOT (new this window):** not testable as letters + nulls-in-own-types by any order
  instrument at N 1,138 and 15 pct noise (oracle ceiling) -- an untestable, not a negative.
- **Retired:** model shape-match on the clear hand (PRIV1D, two attempts; a third needs a person, rule 3); model
  adjudication of a sign pair (PRIV2A2). Not retired, waiting on a person: two owner-side checks in the private
  repository (ASKS 151).
- **State:** idle-standing. Every machine instrument on public and private material in hand is spent or retired; the
  next steps are owner-side (ASKS 151) or new material: the 600 dpi images of all four sheets (ASKS 100), a museum
  reply to the owner's next note (drafted from ATTEMPTS.md by the account-3 orchestrator).
