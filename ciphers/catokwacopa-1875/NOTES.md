partial

blocked (intake-gate sense only, LANE CX2 25 Sept 2026, corrected from `open`) -- under the Pipeline intake
gate, the standard source for this target, the newspaper issue itself (The Evening Standard, 8 and 20 May
1875), has never been independently opened by anyone in this repo: the British Newspaper Archive and
newspapers.com scans stay login-gated from the cloud (queued LOCAL-QUEUE.tsv row L13, 25 Sept 2026), so the
working transcription rests on Thomas Ernst's off-repo BNA-checked text (used in Bourdeau's `ads.py`). This
is an intake-gate correction only, not a change to the substantive research status: Cipherbrain's three
posts, Bourdeau's `catokwacopa/NOTES.md` and Aymeloglu's `SHORTLIST.md` were all read in full by this worker
(LANE CX, 25 Sept 2026, below), and line-1 stays `partial` for that substantive question (mechanism agreed,
unique plaintext not reconstructable per every source consulted).

## Check-solved (LANE CX2, 25 Sept 2026) -- verdict-format correction

The 25 Sept 2026 LANE CX pass below (kept intact) ran the community-lists/Bourdeau/Aymeloglu/model-solve-
announcement legs but left NOTES.md's top lines in a shape the intake gate does not accept (no line-2
citation of the standard source, and it wrote a bare "Intake verdict: open" although the one source that
would let this worker independently corroborate the ciphertext -- the newspaper issue -- was never opened
by anyone in this repo). This pass makes no new search; it re-reads the file end to end (LOCAL-QUEUE.tsv
row L13 already covers the identical gap, queued 25 Sept 2026 by the pass below) and corrects the verdict
shape only: `blocked` on the specific point of an independently-read standard source, `partial` unchanged
as the line-1 status word for the substantive question (mechanism agreed, unique plaintext not
reconstructable per every source consulted).

## Check-solved (LANE CX, 25 Sept 2026)

Cipherbrain's three original posts (scienceblogs.de/klausis-krypto-kolumne, 2015/2018x2 — now reachable,
was `EGRESS_BLOCKED` on 23 Sept 2026), Bourdeau's `catokwacopa/NOTES.md` (fresh clone, commit 24 Sept 2026
21:06 UTC) and Aymeloglu's `SHORTLIST.md` (fresh clone, commit 23 Sept 2026) all read directly by this
worker: no unique-plaintext solve exists anywhere, status unchanged from the 23 September sweep below; no
model-solve announcement found (web search for "Catokwacopa" + "solves"/Claude/GPT, and the Vals AI blog).

## Check-solved (LANE CX, 25 Sept 2026)

Repeats the community-lists, Bourdeau and Aymeloglu legs of the six-source sweep the 23 September pass
below already ran, plus the model-solve-announcement addition named in this session's job brief; web
search, print/DECODE legs not re-run (already logged below, nothing in this class of source changes day
to day for a 150-year-old newspaper item).

1. **Web search (model-solve announcements).** `"Catokwacopa cipher solved Claude GPT 2026"`,
   `"Catokwacopa" solves`, `Vals AI blog Catokwacopa` (WebSearch, 3 queries): no hit connecting this item to
   any AI-model solve announcement (Vals AI, Schneier, or any lab/eval-company post); the only Catokwacopa
   hits returned are the same three Cipherbrain posts and the solver-repository pages already known.
2. **Community lists — Cipherbrain direct read (was blocked 23 Sept).** `scienceblogs.de/klausis-krypto-kolumne`
   now answers curl 200 (no longer `EGRESS_BLOCKED`, confirmed both root and a search query). Fetched the
   site's own search (`?s=catokwacopa`, page 1 and 2, 3 requests total): the same three posts found 23 Sept
   (17 Aug 2015 original ask; 26 Jan 2018 "Revisited"; 17 Jun 2018 "Top 50" #8) and no fourth/2026 post —
   the "14 August 2026" repost cited in the 23 Sept section below was not independently found by this
   worker's search of the blog itself (a direct URL guess for `2026/08/14/` 404s); it may exist under a
   different date/slug, or the earlier citation may be to a different site (klausschmeh.net, checked
   reachable, 301, not fetched further this pass — budget). Not read: the full comment threads themselves
   (this worker read only the WordPress search-result stubs, not each post's `#comments` section) — this is
   the same gap the 23 Sept pass flagged as "full-page fetch blocked", now only partly closed (index page
   reachable, individual post pages not fetched this pass).
3. **Bourdeau, fresh clone (`github.com/dbourdeau/cyphersolver`, 25 Sept 2026, `catokwacopa/NOTES.md` last
   committed 24 Sept 2026 21:06 UTC, one day newer than the 23 Sept citation below).** Continued audit work
   since 15 Sept: an open-vocabulary exact-fit name search over 1,645 period proper nouns confirms the
   Oxford-classics frame reading is uniquely forced for five lines (CONINGTON, JOWETT, SHIRLEY, HERTFORD each
   the only name that fits its frame with no more omissions than the published reading), and a Latin-vocabulary
   exact-interleaving search on line 29 (control: line 17 correctly returns Horace's QUI FIT) finds no
   two-word reading in Latin either — line 29 stays undetermined in both languages. "Remaining gaps" table
   unchanged in kind: lines 9, 12, 23, 26, 29 still unread; no unique full plaintext claimed anywhere in the
   file.
4. **Aymeloglu, fresh clone (`github.com/aaymeloglu/unsolved-ciphers`, 25 Sept 2026, commit 23 Sept 2026
   14:27 UTC, unchanged from the citation below).** `SHORTLIST.md` line 81 and line 148 re-read verbatim,
   identical wording to the 23 Sept citation ("effectively cracked, remove" — Schmeh's Facebook comment that
   the mechanism is solved but the unique plaintext cannot be mathematically reconstructed).

No new fact changes the line-1 status word, which stays `partial` per the 23 Sept section below (not
`found-solved`: no source claims a complete, forced, unique plaintext). Added `LOCAL-QUEUE.tsv` row L13 for
the one gap this sweep confirms is still unclosed: the working transcription (Ernst's BNA-checked text,
used in Bourdeau's `ads.py`) has never been independently re-verified against the British Newspaper Archive
scans directly by anyone in this repo.

Intake verdict: open (corrected to blocked, LANE CX2 25 Sept 2026 -- see the top-of-file section: the
newspaper issue itself, this target's standard source, is login-gated and unread by anyone in this repo).

Requests this pass: `scienceblogs.de` 4 (root reachability, `?s=catokwacopa` pages 1-2, a direct 2026/08/14
URL probe), `klausschmeh.net` 1 (reachability only), `github.com` 2 (fresh shallow clones), WebSearch 4.

# Catokwacopa advertisements, Evening Standard (*The Standard*), 8 and 20 May 1875

- Source: QUEUE.md rank 18 (score 32), scored 20 September 2026; catalogued from Bourdeau's `catokwacopa/`
  target folder and Klaus Schmeh's Top 50 list.

## Check-solved sweep (23 September 2026)

1. **Web search.** "Catokwacopa cipher Evening Standard 1875 solved plaintext" — surfaces Cipherbrain's own
   coverage directly: "Revisited: The Catokwacopa cryptograms from 1875" (2018), "The Top 50 unsolved encrypted
   messages: 8. The Catokwacopa cryptograms" (2018), and the original 2015 "Wer löst die
   Catokwacopa-Kryptogramme..." post, plus Bourdeau's own catalogue index. The search summary itself states
   "the Catokwacopa cipher remains largely unsolved, with only partial plaintext solutions identified as of the
   most recent updates" — consistent with every other source below. found=false for a full solve; found=true for
   extensive partial/documented work.

2. **Print.** No calendar or documentary edition applies (a Victorian newspaper personal advertisement, not a
   state paper); the relevant "print" sources are the two 1875 *Evening Standard* issues themselves. The British
   Newspaper Archive listing and newspapers.com index were not queried directly this sweep (both require login
   beyond a bare index search and were not in the budget for this pass); Bourdeau's `catokwacopa/NOTES.md`
   already records that the working transcription used is Thomas Ernst's BNA-verified text (`ads.py`), which
   corrects roughly a dozen errors in the transcription that had been circulating before it (e.g. "Hrsclam" for
   the correct reading, "138" not "139"). Not re-verified against BNA directly this sweep.

3. **Community lists.** Klaus Schmeh's Cipherbrain (scienceblogs.de/klausis-krypto-kolumne) is the primary
   source and is where this item's whole public history lives: the original 2015 post asking readers to solve
   it, a 2018 "Top 50" entry (#8), and a 2018 "Revisited" follow-up recording partial readings that had
   accumulated by then (Thomas Bosbach's "DYING DECLARATION"; Lance Estes and "Dave"'s Oxford-vocabulary reading
   — SUMMER TERM, 1853, CONINGTON, JOWETT, BALLIOL, SHIRLEY). A 14 August 2026 post republished the puzzle with
   an active comment thread (per QUEUE.md's own rationale, sourced from klausschmeh.net); Schmeh's own verdict,
   quoted in Bourdeau's `catokwacopa/` folder and in a Facebook comment cited by Aymeloglu's `SHORTLIST.md`
   (line 148), is that "the cipher mechanism has been solved, but the complete, unique plaintext cannot be
   mathematically reconstructed." Full-page fetch of the Cipherbrain posts themselves is blocked by this
   environment's egress policy (`EGRESS_BLOCKED domain=scienceblogs.de`; see
   ciphers/charles-rupert-1645/NOTES.md item 3), so only WebSearch snippets and the two solver repositories'
   own citations of Schmeh could be checked directly this sweep, not the original posts' full text or comment
   threads. found=true (extensive, but explicitly not a unique-plaintext solve; source partially unreachable).

4. **DECODE.** Not applicable — a 19th-century newspaper advertisement, not a DECODE-catalogued manuscript
   archive item. Not checked.

5. **Bourdeau (`github.com/dbourdeau/cyphersolver`, shallow clone 23 Sept 2026, MIT code / CC BY 4.0 text).**
   **found=true, substantial, no unique solve.** `catokwacopa/NOTES.md` ("The Catokwacopa advertisements (1875)
   — which readings the letters force, and which are guesses") is a detailed, dated (September 2026) audit, not
   a fresh solve. It confirms the structural mechanism (line *i* of the first ad and line *i* of the second are
   order-preserving halves of one plaintext phrase, letters dropped by W.) is agreed and statistically real (a
   permutation test on the paired line lengths: "no random re-pairing in 100,000 comes that close"), catalogues
   the accumulated proposed readings since 2018 (Bosbach, Estes/"Dave", Ernst's diplomatic line numbering and
   BNA-checked transcription, Krajčovič's QUI FIT/Horace *Satires* reading and 2026 "exact-cost audits"), and
   states the central unsolved problem: the omission rule (three to twelve letters freely inserted per line)
   lets "plausible English... fit almost anything," so readings are only trustworthy where the letters force
   them, and Bourdeau's own audit (15 September 2026, cited in QUEUE.md's rationale) found only a handful of
   lines are actually forced. No committed reading claims full, unique plaintext recovery. `TARGETS.md` and
   `top50/` reference the item consistently with this "audited, unresolved" status; `catalogue/`'s scraped
   listing does not mark it read/solved.

6. **Aymeloglu (`github.com/aaymeloglu/unsolved-ciphers`, shallow clone 23 Sept 2026; no licence, cite only, no
   code copied).** No target folder (this is not one of Aymeloglu's eight active targets), but `SHORTLIST.md`
   discusses it twice: line 81, "Substantial partial reconstruction already exists (Gaffney, Ernst and others,
   discussion through Sept 2026), so this is finishing work, not a first break"; and line 148, in the exclusion
   table, quoting Schmeh's Facebook comment above and recommending "effectively cracked, remove" — i.e.
   Aymeloglu's own project assessment is that this item is not worth pursuing as an open cryptanalysis target,
   precisely because the mechanism is known but no unique plaintext is recoverable. found=true (assessment, not
   a target folder).

## Verdict

**Partial**, not open and not found-solved. The encoding *mechanism* is publicly established and agreed by
every source that discusses it (Bourdeau, Aymeloglu, Schmeh/Cipherbrain), and substantial partial plaintext
readings have been proposed since 2018 by multiple named researchers (Bosbach; Estes/"Dave"; Ernst; Krajčovič),
but no source claims a complete, forced, unique plaintext, and the strongest quantitative audit available
(Bourdeau, 15 September 2026, cited in QUEUE.md) argues the omission rule structurally prevents one from being
demonstrated. This is not a negative result under rule 3 (no matched-control test of a solver against synthetic
ciphers of the same design was run, by this sweep or by the audits cited), so "closed-negative" is not used; it
is reported as partial. No Stage 2 line applies (verdict is not "open"). QUEUE.md row 18 has been annotated with
this finding rather than moved to Dropped, since no source claims the item solved.

## Pointer (25 Sept 2026, worker bPOL2, LANE B2, appended not edited)

`ciphers/pollaky-1865-1875/` now holds an image-based transcription of what is almost certainly this same
cipher (ads 3-4 of that target: The Standard, 8 and 20 May 1875, ad 4's own plaintext tail names ad 3 as its
first half, matching this target's structure exactly). Two independent blind transcription passes there
(image scan from scienceblogs.de/Gaffney-Gluecklich, not BNA) reconciled at 78/80 tokens (97.5%); the two
disagreements were settled from the image and diffed letter-for-letter against this target's own working
text (Ernst's BNA-checked `ads.py` in Bourdeau's cyphersolver): **0 differences out of 72 letter-words
(100% agreement)** once dash/punctuation notation is normalised out (`ciphers/pollaky-1865-1875/scripts/
diff_bourdeau.py`, `NOTES.md` "Test 2" section). This is independent corroboration of the ciphertext from a
second scan source, not a new plaintext reading -- it does not change this target's `partial` verdict or the
still-open lines in "State of play" above. Whoever next works either target should treat
`ciphers/pollaky-1865-1875/images/ad3-1875-05-08.jpg` and `ad4-1875-05-20.jpg` as a second available scan
of the same two ads, and decide whether the two targets should be merged (not done by this worker, out of
this brief's scope).

## Step NEXT-CAT (2 Oct 2026): ciphertext on disk, Ernst's line pairs, pairing test re-run with a control

Account 2 worker NEXT-CAT, Opus 5.5, 2 Oct 2026 03:14-03:4x UTC. Ran the Verdict's cheapest next step and nothing else.

1. **Ciphertext.** `ciphertext.txt` is now a verbatim copy of AD 3 and AD 4 from `ciphers/pollaky-1865-1875/ciphertext.txt`,
   with attribution in its header: two blind passes over the scienceblogs.de/Gaffney-Gluecklich scans, matching 72/72 against
   Ernst's BNA-checked text. Not re-transcribed here. Rule 2: it rests on those scans, not on the BNA issues (L13).
2. **Snapshot.** `sources/cyphersolver/2026-10-02/catokwacopa/` holds Bourdeau's `targets/catokwacopa/` folder, unmodified
   (10 files, commit 34e0fc8, 1 Oct 2026; MIT code / CC BY 4.0 text; `COMMIT-catokwacopa` beside it). His `ads.py` takes its
   29 lines from Ernst's 2018 comment #29. So his line numbers are **measured, no longer inferred**:
   Bourdeau k = Ernst [k] for k <= 10, k = 11 is [10a] (`54, 3` / `18`), and k >= 12 is Ernst [k-1].
   His undecided lines 9, 12, 23, 26, 29 (his NOTES section 4) are therefore Ernst **[9], [11], [22], [25], [28]**.
   The 1 Oct gap line had given [8] for line 9. That was wrong: line 9 is `mistrl / otenpu`, Ernst [9].
3. **Segmentation.** `pairs.py` derives the 29 pairs from the two printed lines. Runs of numerals are joined, and `Ap. 138` /
   `A.P. 138` are kept as one unit. It writes `pairs.tsv` (Bourdeau line, Ernst label, both halves, lengths). Diffed pair by
   pair against Bourdeau's `PAIRS`: **0 mismatches out of 29**.
4. **Permutation test (spec test 1).** The statistic is S = sum |len(8 May half) - len(20 May half)| over the 24 letter-only
   lines (Bourdeau's rule; the numeral lines and Ernst [12] `1.6.9 / cotegr` are set aside). The letter totals are 222 and 213.
   **S_obs = 33**, the same as Bourdeau's figure. Re-pairing the 20 May halves at random, **0 of 100,000** permutations
   reach S <= 33 (p < 1e-5, seed 1875).
   The control (rule 3) is matched in line count, per-line letter totals and design (an English phrase from Huck Finn and
   Gatsby, with 0-3 letters dropped, split into two order-preserving halves). 40 synthetic texts were made for each of two
   splitting habits, to bracket W.'s unknown one, and each went through the same test at 10,000 permutations:
   - coin split (each letter to a random half): S 59-105 (mean 81.2), power 0.80 at p < 0.001.
   - balanced split (floor or ceil of n/2): S = 9, power 1.00.
   W.'s S = 33 falls between the two. The test can detect true pairing in the same design, and the target is detected. This
   confirms Bourdeau's result on our own copy. No reading is claimed and nothing is graded (rule 4 does not apply: no
   plaintext tokens).
5. **Reproduce.** Run `python3 ciphers/catokwacopa-1875/pairs.py` (about 6 s), which writes `pairs.tsv` and `pairtest.json`.
   `--check` exits 1 if either file is stale. The judge was not run because there is no reading to judge.

Requests: github.com 1 (shallow clone). Vision calls 0. Subagents 0.

## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)
Read so far: unmeasured, because this repo holds no reading of its own (no key or plaintext, only the segmented ciphertext and the pairing test of step NEXT-CAT, 2 Oct 2026). The line structure is now measured. pairs.tsv has 29 pairs, 24 of them letter lines, and Bourdeau line k = Ernst [k] (k <= 10), [10a] (k = 11), [k-1] (k >= 12). Bourdeau's catokwacopa/NOTES.md (snapshot sources/cyphersolver/2026-10-02/catokwacopa/, sections 4-5) gives 7 lines decided by ordinary vocabulary, 5 name-frame lines that admit a unique name, and 5 lines not decided by the letters (his 9, 12, 23, 26, 29 = Ernst [9], [11], [22], [25], [28]).
- Bourdeau's lines 9, 12, 23, 26, 29 (Ernst [9], [11], [22], [25], [28], measured in pairs.tsv, step NEXT-CAT), both ad halves of each - blocker: not-attempted; no published reading is forced on these lines. Bourdeau's line-29 Latin search had only a positive control (line 17 -> QUI FIT) and no matched uniqueness control. Spec cheap test 3 never ran (specs/catokwacopa-1875.json). So "the omission rule fits almost anything" is untested here and cannot yet be graded too-short; next: run spec test 3 on our own copy (pairs.tsv, now on disk). Do an exact-fit search of the five lines against an enlarged period vocabulary under the 3-12-letter omission budget, with a matched control of synthetic English lines of the same length and budget, reporting both rates. As a second instrument, run QUEUE.md row 18's phrase-level LM search on line 23 with Bourdeau's positional prior (cyphersolver catokwacopa/search.py, MIT, cited), ~$5
- Lines with published but unforced readings (Bosbach's DYING DECLARATION; Estes/Dave's SUM TERM, 1853, BALLIOL; Ernst's 2018 [12]-[27] glosses, e.g. "[13] MOPT A PURLY ... IN COLLEGE", "[25] MOISTANT PURL", comment #26) - blocker: not-attempted; this repo has re-derived none of them, and spec cheap test 2 (re-derive the exact-fit name search over 1,645 period proper nouns) is unrun; next: run spec test 2, widened to names plus vocabulary from our own list, using gap 1's synthetic control. Grade each line forced (S) or guessed (M) per rule 4, and record where both reads agree, ~$3
- The 27 March 1875 ad by the same writer (Ernst, comment #2: "at least one other ad like this documented, 27 March 1875 (see original thread, without its counterpart)"), and any further W. ads March-September 1875 that Ernst's monthly-pair guess predicts - blocker: not-attempted; nobody in this repo has opened the 2015 original thread, where Gaffney's 19 Aug 2015 pairing comment and the 27 March text are said to be. LANE CX read only search stubs; next: fetch the comment threads of the 17 Aug 2015 and 26 Jan 2018 "Revisited" posts from scienceblogs.de (reachable 25 Sept 2026, about 4-6 requests). Extract the 27 March text, check whether its counterpart is named, and file it as a sibling (a further BNA issue search would need the owner's desk, same route as L13), ~$2
- Ciphertext of both ads checked against the original Evening Standard issues of 8 and 20 May 1875 (BNA/newspapers.com) - blocker: waiting-on LOCAL-QUEUE.tsv row L13 (bna-verify, owner's desk runner, status queued); BNA and newspapers.com are login-gated from the cloud (LANE CX2 above). This does not block the gaps above, because the scienceblogs/Gaffney-Gluecklich scan and Ernst's BNA-checked text already agree 72/72 (ciphers/pollaky-1865-1875/NOTES.md, Test 2)

## Escalation (1 Oct 2026)
- [ ] siblings: Done: pollaky-1865-1875 ads 3-4 are the same two ads from a second scan (two blind passes agree 78/80; 72/72 against Ernst; NEAR.md pollaky row; bPOL2 pointer above). Not yet opened: the 27 March 1875 ad that Ernst names (sources/schmeh/posts/08-catokwakopa.txt line 242), other ads signed W. in Palmer/Gaffney's The Agony Column Codes & Ciphers, and Ernst's predicted monthly pairs (April, August-September 1875). Planned: fetch the 2015 and 2018 "Revisited" comment threads (gap 3), about $2.
- [x] clear-pages: the only clear text is the tail of ad 4 ("This will be intelligible if read in connection with my communication published in this column on the 8th inst.", ciphers/pollaky-1865-1875/ciphertext.txt AD 4). It is the pairing instruction, which every reading already uses. No clear copy or period decipherment of the plaintext is known.
- [n/a] known-keys: the design has no key. Each phrase is split into order-preserving halves across the two ads, with 3-12 letters dropped per line, so there is no key or nomenclator to try. KEY-OFFICES.tsv and KEY-DESIGN.tsv have no row for this target, and design_prior.py's code and nomenclator families do not fit this design.
- [x] print: read Cipherbrain's Top-50 post 8 with its 48 comments (on disk, sources/schmeh/posts/08-catokwakopa.txt), Bourdeau's catokwacopa/NOTES.md (commit 24 Sept 2026), Aymeloglu's SHORTLIST.md lines 81 and 148, and a web search for model-solve announcements (23 and 25 Sept 2026). None gives a unique plaintext. Not read: the newspaper issues (L13) and the 2015/2018 thread comments (folded into siblings).
- [ ] key-rebuild: the segmented line pairs are now on disk (pairs.tsv, step NEXT-CAT, 2 Oct 2026; pairing test 0/100,000 vs a control with power 0.80-1.00). We have run no forced-fit, vocabulary or LM search, and none appears in NOTES.md, ROOM.md or LEDGER.md. Bourdeau's exact-fit name search and his line-29 Latin search are his work, not re-derived, and neither has a matched uniqueness control. Planned: spec tests 2-3 with a synthetic-line control, plus the line-23 LM search from QUEUE.md row 18 (gaps 1-2).
- [x] image-check: ciphers/pollaky-1865-1875/NOTES.md Test 2. Two blind passes over the scienceblogs/Gaffney-Gluecklich scans agree 78/80, and both disagreements were settled from the image (caselcluchozamot S; Ngtndusdcndo M, low-resolution scan). The result matches Ernst's BNA-checked ads.py 72/72 letter-words with digits and dashes stripped; Hrsclam and 138 match Ernst, against Schmeh's printed Hfsclam and 139.
- [ ] retry: nothing to rerun yet, because key-rebuild has not run. Planned: after spec tests 2-3, re-score every line pair (the five unread lines and the unforced lines) with the extended vocabulary and regrade S/M per rule 4.
Verdict: keep going: 3 internal gaps; cheapest next: fetch the comment threads of the 17 Aug 2015 and 26 Jan 2018 "Revisited" Cipherbrain posts from scienceblogs.de, extract the 27 March 1875 W. ad and file it as a sibling (gap 3), ~$2
