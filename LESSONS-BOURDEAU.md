# Bourdeau method digest (not a status list)

Source: `github.com/dbourdeau/cyphersolver`, HEAD `648309e85b8ae0c3dce23825a54c4b3b06148849`, read 27 Sept 2026
(shallow clone, deleted after this session). Licence: code MIT, text and notes CC BY 4.0 (Daniel Bourdeau).
Every row below cites the file it came from; quotes are short, paraphrase does the rest.

This is a method digest, not a status list: it exists to extract *how* Bourdeau's sessions work, for us to copy,
not to track his targets (his own README/TARGETS.md/CATALOGUE.md do that; our LANDSCAPE.md already corrects our
own catalogue against his solves). Counts below (315 target folders, up from the 99 LESSONS.md read on
19 Sept 2026) are from `targets/*/profile.json`'s `outcome.class`/`outcome.method` fields, read by script:
`read` 83, `already solved` 71, `read in part` 66, `not read` 64, `not a cipher` 13, `offline only` 11; by method,
`key recovered from ciphertext-only` 25 (15 read + 10 read in part) -- up from "about a dozen" in our 19 Sept
LESSONS.md, so the ciphertext-only share of his solves has roughly doubled in the intervening week.

## Section 1 -- Case studies

One row per read/read-in-part/closed target, drawn from `README.md`'s own Results tables (his maintained digest
of each folder's `NOTES.md`/`profile.json`, cited per row below with the section it came from).

### Genuine ciphertext-only breaks

| Folder | Target, era | Ciphertext shape | What broke it | His file |
|---|---|---|---|---|
| `siena1421/` | Sienese envoys to Concistoro di Siena, 1421-1547 (44 letters, one 43-key filed corpus fits none) | multi-system busta, 43 filed keys, none fits any of the 44 letters | Ciphertext-only key rebuilt per letter from crib fragments/glosses; four of ~15 attempted letters yielded (58.6-96.2% coherent); rest open for want of a photograph or a second system | README.md "Key recovered from ciphertext-only" |
| `harley1582r8505/` | "L'Estat du Roy de Navarre...", after 1580, BL Harley 1582 ff.263-64 | ~50-sign homophonic alphabet, catalogued "English?" | The letter *m* is a run of two-to-four dots, taken for punctuation by every earlier pass, which is why no key fit; a control run (real French under a key of the same shape) proved the fault was in the solver's Sukhotin constraint, not the manuscript -- the control read 100% once fixed, the real text broke at once | README.md "ciphertext-only" |
| `ferdinand1619/` | Elector of Cologne to Duke Maximilian I, 1619, BayHStA Kurbayern 4591 ff.281-86 | homophonic on even two-digit figures 10-78 + a 3-digit nomenclator, 2,482 letters | Annealed against `de-1500s`; ~60 single-digit transcription slips (0/6, 3/5, 1/4, 2/7) repaired by re-checking a sample against the images; **control was the sibling record R9425, re-read unchanged by the same key** | README.md "ciphertext-only" |
| `lorraine1592/` | Charles III of Lorraine to Vaudémont, 1592 | reciprocal letter-pair substitution wrongly read as a 44-symbol key because the earlier transcription merged e/c and b/h | An 18 Sept ciphertext-only break (790/1,105 tokens read, up from the earlier key's 40.6% on the same words) came only after the transcription itself was redone letter by letter against the page with the *new* key in hand -- the wrong key had been hiding the true, simpler system | README.md "ciphertext-only"; also our own CLAUDE.md rule 3 cites this as the SALV-DIAG-style lesson pattern |
| `bl32305/` (attempted, negative) | Carré code letters 1742-45, BL Add MS 32305 | two-part ~800-entry code, 1,323 groups transcribed, 381 distinct | Letter-homophonic anneal scored no better than a shuffled control; one-part alphabetical order tested and ruled out (r = -0.26) *before* concluding it is a two-part code with no crib -- closed only after both hypotheses were controlled | README.md "Not solved" |

### Key from adjacent/sibling plaintext (the productive route)

| Folder | Target, era | Ciphertext shape | What broke it | His file |
|---|---|---|---|---|
| `jqa/` | J. Q. Adams to Sec. of State, St Petersburg, 1812 (Ford's "nine lines...not decyphered") | Adams's own code, wrongly assumed to be Armstrong's THE=972 by the Madison editors | Code rebuilt to 1,166 numbers from the clerk's own interlinear decodes on other frames of the same reel, plus Ford's printed decipherments of neighbouring despatches used as a second crib; refuted the printed premise before rebuilding | README.md "adjacent plaintext" |
| `balbases1677/` | Marqués de los Balbases, 14 letters 1677-78, no filed key fits | letter+syllable code, ~20 word codes, nulls | Ten of fourteen letters carry a contemporary margin decipherment; a hard-EM aligner anchored on repeated words rebuilt the key from those ten margins and read the four undeciphered letters at 97% of 8,150 groups | README.md "adjacent plaintext" |
| `carpio1677/`, `moncada1524/`, `adrian1521/`, `sessa1524/` | Habsburg/Spanish diplomatic letters, various | nomenclators/homophonic ciphers | Same shape every time: a sibling in the *same key* carries the period's own decipherment (margin gloss, calendared translation, or a duplicate record), and the key is rebuilt by EM/token-tiling alignment, then read forward onto the unglossed letters | README.md "adjacent plaintext"/"external plaintext" |
| `mondoucet/` | Mondoucet to Charles IX, Brussels 1572-73 | homophonic letter cipher | First pass failed because the glyph segmenter split single letters into 1.3-1.4 glyphs each; by-hand resegmentation (one glyph = one letter) then let a beam decoder reproduce the *contemporary decipherer's own gloss* verbatim, and the same key later read a fourth letter that turned out to be independently printed in Didier 1891 -- confirming, not just matching | README.md "adjacent plaintext" |

### Read with a known/external key, or from an existing decipherment

| Folder | Target, era | Result | His file |
|---|---|---|---|
| `moncada1524/`, `adrian1521/` | 1524, 1521 Spanish despatches "filed as decrypted/non-decrypted" | Already solved in print (1854, 1899) but mis-filed by DECODE/the catalogue as undeciphered; found by OCR/full-text search on the printed edition once the catalogue gave date and place, then the print used to *complete* gaps the original edition left | README.md "external plaintext" |
| `andreae1616/` | *Chymische Hochzeit*, 1616 printed romance | Not a letter -- four printed "cipher" inscriptions, glossed by the text itself two pages later | README.md "external plaintext"; a caution that not every "unsolved cipher" catalogue entry is a real cryptogram |
| `vatican5/` | Farnese-Poggio, AAV Segr. Stato Spagna, "Vatican Challenge 5" | Own seven-session diagnosis (an Antonio Elio polyphonic syllabary) **withdrawn** on finding Simon Klee's independent MysteryTwister solution (16 Sept 2026): a mixed one-/two-digit monoalphabetic key with a null, not a polyphonic syllabary | README.md "Not solved" (`vatican5/SOLUTION.md` is the retraction) |

### Well-documented failures (his own stated reasons)

| Folder | Blocker | Stated reason | His file |
|---|---|---|---|
| `sp53/` (SP 53/16 nos.78-79, SP53/22 f.52) | Design excluded by control, not access | Three-session escalation: session 2 found the two letters share a key (10/20 commonest symbols in common vs 2.9 expected) and pooled them; session 3 built a pipeline that reads clean 507- and 1,151-token controls cleanly, then found no.78 shows no language basin in five languages tried and pooling scores *worse* than either letter alone -- the shared-key claim was **withdrawn**, not just left unsolved | README.md "Not solved" |
| `birago/` | Design beyond the annealer at this homophony | Glyph-level re-transcription (483 digits + 16 marked + 9 wavy + 6 null signs) settled the design as two-digit letters plus 1-2 digit marked code groups (228 tokens/62 symbols); at that homophony **the annealer fails matched synthetic controls of the same shape**, so the negative is "the method's limit", explicitly distinguished from "no system found" | README.md "Not solved" |
| `chaulnes/` | Below-unicity nomenclator | Ciphertext verified from images, the code's ten-column design established, but 300 groups can't determine a 116-entry nomenclator: **the annealer recovers only 4-12% of a matched control**, and wrong keys score within noise of the true one | README.md "Not solved" |
| `ottobon/` (R2252/R994) | Access, not cryptanalysis | "One browser session": the manuscript is digitised but bne.es sits behind a Cloudflare Turnstile that blocks scripts, and DECODE (a second copy) needs a login -- filed as blocked-on-access with the candidate key already built, not as a cryptanalytic negative | README.md "Not solved" |
| `orpo1942/` | Known-plaintext solver excluded by a control, then a real mismatch | A double-Playfair; five different solvers (annealing, tempering, Sinkhorn relaxation, EM) **all fail a synthetic 970-letter control with a known key** before the real message is tried -- and even a working known-plaintext solver (recovers the boxes from ~80 pairs) then fails because the one available decrypt doesn't align to the ciphertext under any spelling/layout tried | README.md "Not solved" |
| `voynich/`, `indus/`, `lineara/` | Famous/undeciphered scripts | Kept **outside** `profile.json`/the paper dataset entirely (`FAMOUS` list, `docs/_check_writeup.py`) -- negative results (entropy tests, hypothesis registries: "2,364 hypotheses registered before testing, 1,224 held") are reported but never mixed into the solved-rate statistics | README.md "Not solved"; CLAUDE.md "Except the famous targets" |

## Section 2 -- His approach (numbered practices)

1. **Outcome is classed by *how the text was obtained*, not by "solved"/"unsolved".** Seven categories (George
   Lasry's, by email 21 Sept 2026, plus his own "existing decipherment"): key from ciphertext-only / from external
   plaintext / from adjacent plaintext / read after matching an external key / read with a known key / read from
   an existing decipherment / not solved / not applicable. "Read" and "solved" are never used alone; a page says
   what happened. A linter (`docs/_check_terms.py`) enforces the wording. -- CLAUDE.md "Outcome method and
   priorities"; README.md "Outcome method".
2. **A fixed-field `profile.json` per target**, written on the first session and appended to after *every* move
   including failed ones ("This record cannot be rebuilt accurately afterwards"). Fields include measured
   (not remembered) lengths, whether a reading already existed anywhere and when found (the "contamination
   question"), and a `solution` list of dated steps with a result (`worked`/`partial`/`failed`). -- CLAUDE.md
   "Every target keeps a profile.json".
3. **A precise, numeric bar for "read" vs "read in part".** Complete = >=95% of tokens give sense (measured, not
   estimated), no gap left untried, every document covered, and what remains open is either scattered
   codes/names or blocked from outside (no key, illegible, needs physical access). He notes there is no external
   standard to borrow -- DECODE's own labels are assigned per-record by whoever filed it, and the closest academic
   precedent (Ravi & Knight 2011, Zodiac-408) calls ~97.8% "solved" without fixing a cutoff. -- README.md
   "Conventions".
4. **A target read by more than one route is classed by its primary achievement; genuinely different achievements
   split into `outcome.parts`.** (Lasry, 25 Sept 2026.) Prevents one big nomenclator recovery from being
   overstated as five separate "solves" when four of the five just apply the same rebuilt key. -- README.md
   "Conventions".
5. **A target is not finished until it is written up, in the same session.** A `/writeup` skill checklist reaches
   nine separate surfaces (the docs page, two build manifests, the README row, "Recent findings", three catalogue
   files, and the DECODE correction queue); a checker must print `result: complete`; a Stop hook blocks the
   session once if a target it worked on reads as finished but has no write-up. -- CLAUDE.md "A target is finished
   only when it is written up".
6. **DECODE gets a correction every session that adds anything, even with no reading.** Corrected metadata,
   sibling/duplicate records, and any transcription go into `decode_updates/queue.json` the same session, whether
   or not the target itself moved. -- CLAUDE.md.
7. **Grades: H (primary key source), C (known-plaintext letter), M (uncertain), I (inferred/alphabetical).** Four
   grades, not our five -- no separate cryptanalytic-with-control grade; a ciphertext-only S-shaped result is
   graded on the *evidence class it ends at* (H once a sibling confirms it, M if not). -- README.md "Conventions".
8. **One shared `lang/` registry, not a per-target `lm.py`.** Era- *and* register-specific corpora, not just
   per-language: `fr-1530-despatches` (François I-Henri III) vs `fr-1600-letters` (Henri IV) vs `fr-1650-rome`
   (mid-17th c. code-group work, order 7, no spaces) vs `fr-grand-siecle` (literary); similarly `it-cinquecento`
   vs `it-modern`, `de-1500s` vs `de-1640s` vs `de-enigma`. Four *normalisation* schemes (`modern`/`early` [j->i,
   v->u]/`latin` [+k->c,y->i,w->u]/`enigma`) are named and matched to the model, not applied ad hoc. A "known
   gaps" section names which corpora have no remote-fetch recipe and only build in a checkout that still has the
   files, and which targets use a non-n-gram model (a Chinese dictionary, a word list, Enigma trigram tables) not
   migrated into the registry. -- `lang/README.md`.
9. **Structural read of the design always precedes the solver run**, and a wrong first reading is caught by a
   *control experiment*, not a re-read of the manuscript: `harley1582r8505`'s "m = a run of dots" was found only
   after a control run under the presumed constraint solved cleanly while the real text did not, isolating the
   fault to the solver's assumption rather than the source. -- README.md "ciphertext-only".
10. **Sweep the whole volume once a key is found.** (Already in our own LESSONS.md #2 "Look for the sibling" --
    matches his `mondoucet/`, Gallica-sweep finds.)
11. **Credit-sharing with a named collaborator (George Lasry) by private email, logged as such.** Several
    "solved here" rows carry "Lasry solved it independently in 20xx, unpublished (private communication)" --
    an independent re-solution is marked, not silently claimed as a first, and the write-up says which happened
    first when known. The Lasry paper collaboration (`papers/`, HistoCrypt-format drafts) is the same
    relationship formalised. -- README.md rows throughout "ciphertext-only"/"adjacent plaintext"; CLAUDE.md
    "the project is being written up with George Lasry as a paper".
12. **Two flagship results kept independently reproducible from the README itself** (Armstrong-Madison, 30 Aug
    1808; Richelieu-Rancé, July 1629), with the exact commands to rerun them named in the README, not only in the
    target folder -- a reproducibility floor above just "there is a script", closer to our rule 7's spirit but
    surfaced at the repository's front door. -- README.md "Reproducing the two flagship results".
13. **Working-tree hygiene for concurrent sessions**: `git status -sb` before every commit (several sessions
    share one checkout and switch its branch); stage by explicit path, never `git add -A`; if the branch is
    wrong, commit from your own worktree and push `HEAD:main` rather than fixing the shared branch. --
    CLAUDE.md "Working in the shared checkout".
14. **A negative that changes the manuscript's own known text is itself reported and corrected** (`lopehurtado/`:
    "Correction to DECODE: R9652 carries no cipher at all"; an 8x zoom that downgraded ten alphabet-sign
    assignments from confirmed to probable after they turned out to look identical at the magnification first
    read). Corrections to the record are logged with the same weight as a positive result. -- README.md
    "adjacent plaintext".

## Section 3 -- What we do not do yet

| # | Practice | Status | Detail |
|---|---|---|---|
| 1 | Outcome classed by *route*, not solved/unsolved | (c) tool option | Our CLAUDE.md rule 4 grades (H/C/S/M/I) plus rule 7's `kind` (recovery/cryptanalysis/contribution) are coarser than his 7-way `outcome.method`. A `method` sub-field on `status.json`'s target entries (ciphertext-only / external-plaintext / adjacent-plaintext / known-key / existing-decipherment) would let NEAR.md and the result label distinguish "we broke this cold" from "we applied someone else's key" the way his site badges do. Cite: `dbourdeau/cyphersolver` README.md "Outcome method", `docs/_methods.py`. |
| 2 | A fixed-field profile record, appended after every move including failures | (a) already have, differently shaped | Our NOTES.md failure log (CLAUDE.md Layout; LESSONS.md #7 "Write it down") does the same job in prose rather than fixed JSON fields; his `profile.json` buys him a script-checkable measured-length field and a `_check_profile.py --measure` step we don't have an equivalent script for. Not a gap worth building a parallel schema for -- our prose NOTES.md already serves the same "cannot be rebuilt afterwards" purpose. |
| 3 | Numeric >=95%-coherent, no-untried-gap bar for "read" vs "read in part" | (a) already in CLAUDE.md/tools | CLAUDE.md rule 5's amendment (`tools/near_check.py`) and the pipeline's stage vocabulary already gate `partial` vs `solved` on a control and a named next step; our bar is procedural (a control gate) rather than his single measured percentage, but the same "no gap left untried" discipline is enforced by NEAR.md + `near_check.py`. |
| 4 | Primary-achievement classing / `outcome.parts` split | (c) tool option | Nothing in our schema stops a target read partly by inherited key and partly by our own cryptanalysis from being labelled with only one `kind`. A `parts` list on multi-route targets (mirroring his) would need a `status.json` schema change and a checker; name it as a future `tools/near_check.py` or result-label option, not built here. |
| 5 | Write-up-in-the-same-session, checked by script across nine surfaces | (b) brief addendum | Our worker discipline (CLAUDE.md "Workers", "A worker session does one job... and stops") already requires updating NOTES.md/status.json/STATUS.md, but nothing scripts a "did every surface get touched" check the way `docs/_check_writeup.py`/the Stop hook do. Diff text for a COMMON addendum: *"Before a `done:` line reporting a target as `solved`/`partial` with a new reading, run `tools/next_steps.py --check <target>` (a version of it extended to assert NOTES.md, NEAR.md/status.json and the verifier hand-off line are all present) and paste its output; a worker whose reading changes a target's stage without touching all three is not finished."* Not applied here -- text only. |
| 6 | Era- and register-specific corpora, not just per-language, with named normalisation schemes | (a) already in CLAUDE.md/tools, one gap | Our CLAUDE.md rule 3's pt17/pt18/es17c/en-fold lessons are exactly this practice, independently discovered. Gap: his four *named* normalisation schemes (`modern`/`early` j->i,v->u/`latin`/`enigma`) are a reusable convention we don't name as such; `tools/judge_plaintext.py` likely folds some of this ad hoc per corpus. Cite as a tool option: add a `--norm {modern,early,latin,enigma}` flag to `judge_plaintext.py`/`family_run.py` so a period corpus and its normalisation travel together the way his `models.json` pairs them, rather than each corpus reimplementing its own cleaning. |
| 7 | Control experiment isolates a wrong *assumption*, not just a wrong key | (a) already in CLAUDE.md | This is exactly our rule 3's repeated-attempt paragraph and the SALV-DIAG/AX2-4612S lessons (a control that moves the wrong way, or a family that fails three times, points at the instrument, not just the target). No new practice to add; noted as independent convergence. |
| 8 | DECODE-style correction queue for every touched record | (d) partial -- we already write outreach/second-opinion queues, no catalogue-correction queue | We have `outreach/`, `SECOND-OPINIONS-QUEUE.tsv`, `JSTOR-QUEUE.tsv`, `LOCAL-QUEUE.tsv` but nothing that logs a catalogue-metadata correction (a misfiled date, a wrongly-linked sibling record) the way his `decode_updates/queue.json` does. Given DECODE access is our own account's problem too (Access playbook), a `DECODE-CORRECTIONS.tsv` alongside the existing queues, filled whenever a worker finds a DECODE record mis-catalogued, would be a small addition -- naming it here as a tool option, not building it. |
| 9 | Named untried step on a target we hold | (d), sampled, none found live | Spot-checked 13 folders that share a target with his repo by name (`sp53-16-78/79`, `sp53-22-f52`, `fr3621-dinteville-1592`, `fr3975-vieuville-1587`, `roell-vandedem-1809`, `vanspaen-vandergoes-1808`, `hellen-frederick-1752`, `zeschau-seebach-1841`, `riksarkivet-r4282-1628`, `sforza-maino-1446`, `siena-concistoro-2308`, `rah-salazar-soria-sanchez-1524-28`, `lope-hurtado-1522`, `fr15564-mercoeur-1586`, `castelcicala-1816`) against their own NOTES.md: every one already carries an explicit cross-check against his repo (commit hash cited, folder read) from a LANE B5/B6/N4/NX2 worker, several already past his own stated next step (e.g. `castelcicala-1816`'s bCAS retried his own named "hand-read the un-glossed letters" escalation item). No fresh (d) row survives this sample; the queue-diff (`sources/solver-diffs/2026-09-26-crypt-bourdeau-queue.tsv`, this session's U1) is the mechanical way to find one, not a manual name match. |

## Queue diff (U1)

`sources/solver-diffs/2026-09-26-crypt-bourdeau-queue.tsv`: 95 data rows (96 incl. header) against QUEUE.md as of
27 Sept 2026, using fresh shallow clones of both repos (Bourdeau HEAD `648309e85b8ae0c3dce23825a54c4b3b06148849`,
Aymeloglu HEAD `2495c45e8b94ffbc4f09a085224aa5ebce5cdf9f`, both 27 Sept 2026). 63 queue rows are new (by `queue_row`
text) since `sources/solver-diffs/2026-09-23-queue-vs-solver-repos.tsv` (36 data rows then) -- QUEUE.md itself grew
from 37 to 96 lines over the four days, so this is mostly QUEUE.md's own growth, not a fresh diff signal; 16 of
the current 95 rows carry a Bourdeau or Aymeloglu hit (vs 18 of 36 on 23 Sept -- proportionally fewer, consistent
with QUEUE.md adding rows faster than the two repos add matching targets). Targets named are for the parent to
route to a lane; not acted on here.
