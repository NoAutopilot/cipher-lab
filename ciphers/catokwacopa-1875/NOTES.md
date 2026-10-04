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

Account 2 worker NEXT-CAT, Opus 5.5, 2 Oct 2026 03:14-03:2x UTC. Ran the Verdict's cheapest next step and nothing else.

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

## Step A2-CAT (2 Oct 2026): the 2015 and 2018 comment threads, the 27 March 1875 ad filed as a sibling

Account 2 worker A2-CAT, Opus 5.5, 2 Oct 2026 21:14-21:2x UTC. Ran the Verdict's cheapest next step (gap 3) and nothing else.

Intake gate, pasted before the work (`python3 tools/intake_gate_check.py catokwacopa-1875`, exit 0):
`catokwacopa-1875: blocked (line 3) -- already terminal, nothing to gate`

1. **Fetch.** Both posts were fetched once with every comment on one page (`?all=1`; 2 requests to scienceblogs.de,
   2.2 s apart, both HTTP 200, no challenge). They are saved unmodified as `sources/schmeh/posts/08a-catokwacopa-2015-08-17.*`
   (the original post, 7 comments) and `08b-catokwacopa-2018-01-26-revisited.*` ("Revisited", 32 comments), with rows in
   `sources/schmeh/manifest.tsv`.
2. **The 27 March 1875 ad.** There are two witnesses. Both are now copied verbatim into `sibling-1875-03-27.txt`:
   - A: Schmeh, 2015 comment #6 (23 Aug 2015), answering Gaffney's #5 ("the previous one from the 27th March"):
     `W. TITOLLUM Endive Oeman. Soomoom Biffot. Coxel. Dritterfo. Cardebog. Wapalinok. Sikrinad. Sepp?`
   - B: Ernst, 2018 comment #23 (27 Jul 2018), read from the BNA scan at p. 1, col. 2, row 2, which is the same column as
     the May ads (rows 4 and 10, #24-#25). B differs from A at word 3, `[Oonran/Ooman]` against `Oeman`, and marks word 5
     `Biff[?]ot` because of a crease, so its second o may be a b. Neither witness is checked here against a page image
     (rule 2): no image of this ad is on disk, and BNA is login-gated from the cloud (the L13 route).
3. **Counterpart.** Ernst's comment #27 (27 Jul 2018) says he checked every issue of *The Standard* for March and April 1875
   and found no other ad by W., so "the ad in the March 27 issue ... appears to be a self-contained singleton". No second half
   is known, and the 11-word ad cannot be paired the way the May ads are. `pairs.py` does not read the new file, and its
   `--check` result is unchanged. No reading is attempted or graded.
4. **More W. ads, not fetched.** Ernst's comment #26 (27 Jul 2018) reports that the 1879 "Fact or Fiction" ads appear in the
   same place in *The Standard* (p. 1, col. 2, top rows) and that he has "positively no doubt" they are by the same author.
   They have their own Cipherbrain post, 24 Jul 2018 (`.../2018/07/24/the-fact-or-fiction-cryptograms/`). His #30 refers to
   "the eight ads in the Standard in 1875 and 1879". That post is not in this repo and was not fetched, because it is
   outside this step. It is gap 3's next step below.
   Ernst's August-September 1875 monthly-pair guess (Top-50 post, `08-catokwakopa.txt` line 250) was written before his
   own #27 found nothing in March-April. It remains untested: no issue later than April 1875 has been searched.

Requests: scienceblogs.de 2. Vision calls 0. Subagents 0.

## Step A2-CAT2 (2 Oct 2026): the 24 Jul 2018 "Fact or Fiction" post, the 1879 ads filed as siblings

Account 2 worker A2-CAT2, Opus 5.5, 2 Oct 2026 22:28-22:4x UTC. Ran the Verdict's cheapest next step (gap 3) and nothing else.

Intake gate, pasted before the work (`python3 tools/intake_gate_check.py catokwacopa-1875`, exit 0):
`catokwacopa-1875: blocked (line 3) -- already terminal, nothing to gate`

1. **Fetch.** The post was fetched once with all 9 comments on one page (`?all=1`, HTTP 200, no challenge). It is saved
   unmodified as `sources/schmeh/posts/08c-fact-or-fiction-2018-07-24.{html,txt}`, together with its four ad images
   (`sources/schmeh/posts/08c-img/`). Each file has a row in `sources/schmeh/manifest.tsv`. **The images are typeset
   re-renderings in a modern font, not newspaper scans.** They agree letter for letter with the post text, but they do
   not meet rule 2.
2. **Filed.** Four ads are filed verbatim in `siblings-1879-fact-or-fiction.txt` from two witnesses: S is Schmeh's post body
   (from Palmer/Gaffney) and E is Ernst's #8 (27 Jul 2018), "double-checked" against *The Standard* with p./col./row
   positions. The ads are 25 Mar 1879 (43 letters, 11 distinct; E #9 says it ran again unchanged on 26 Mar), 25 Apr 1879
   (clear: "A simple impossibility."), 11 Jun 1879 (49 letters) and 13 Jun 1879 (50 letters). Witnesses S and E agree
   letter for letter on all four. The one difference is a clear-text sentence that only E has, at the end of 11 Jun: "See
   advertisement under same heading in 'The Standard' of 25th April." All four sit in p. 1, col. 2, rows 3-8, the slot the
   1875 ads used. That is Ernst's ground for the attribution (#8: "Absolutely no doubt"). Nothing in this repo establishes
   it: the ads are unsigned, unlike the 1875 "W." ads. By the letters alone, 13 Jun repeats 11 Jun for the first 46 letters
   once I and J are taken as the same letter. The tails differ: GIS in 11 Jun, M HLF in 13 Jun. Ernst (#1) reads 13 Jun as
   a correction of 11 Jun.
3. **Not done.** No reading or analysis was attempted. Ernst's #2-#6 are partial-substitution guesses and are not
   graded or re-derived here. No ad has been checked against a page image (no BNA access from the cloud, same route as
   L13). Ernst (#1, #7) expects "more of them", and no 1879 issue search is on record.
   Ernst's #26 in the Revisited thread counts "eight ads in the Standard in 1875 and 1879". The repo now has 2 May 1875 +
   1 Mar 1875 + 4 dated 1879 = 7, or 8 with the 26 Mar 1879 repeat. That reconciliation is inferred, not stated by Ernst.

Requests: scienceblogs.de 5 (post 1, images 4), >=2 s apart, all 200. Vision: 4 image reads by this session, no subagents.

## GAPS205 (3 Oct 2026, account-4): content-axis pairing test on Ernst's line pairs

Worker GAPS205-pollaky-1865-1875 (account-4), Opus 5.5, 19:01-19:07 UTC, script only, 0 vision, 0 subagents, 0 external
requests. Step: pollaky-1865-1875's gap 3 Verdict (copy the ads 3-4 text, Ernst's pair segmentation, pairing permutation
test with a synthetic-line control). The copy, the segmentation and the length test were already on disk from step NEXT-CAT
(2 Oct 2026); `python3 pairs.py --check` reproduces them (exit 0: 29 pairs, 0 mismatches vs Bourdeau's ads.py, S 33,
0/100,000). So this step adds the same permutation test on a second axis, the letter content, which S cannot see.
It was pre-registered in PREREG-GAPS205.md (f418da80, and addendum A b333caa3, each committed before its run).
Credit: the line division is Thomas Ernst's (Cipherbrain, 2018, comment #29 via Bourdeau's ads.py). The length test is
David Bourdeau's (cyphersolver catokwacopa, MIT). The design reading is the published community one.

- T = sum over the 24 letter lines of the best order-preserving merge of the two halves under an English letter-bigram model
  (tools/data/en Huck Finn + Gatsby). Target p 0.00045 and control power 1.0/1.0, but the unpaired control U-half is flagged
  at p < 0.05 in 15 of 20 texts (FPR 0.75 > gate 0.15): **non-test**. The merge score grows with C(n+m, n), so T leaks
  the length pairing that S already measures.
- T' (addendum A, one run) subtracts E[n][m], the mean merge score of independent corpus halves of the same lengths.
  **T' (length-corrected merge score) is a valid test and does not detect W.'s pairing**: target p 0.254 (T' -35.05, 20,000 re-pairings) vs positive controls P-coin/P-half power 0.95/1.00 at p < 0.001 and unpaired control U-half false-positive rate 0.05 at p < 0.05. Verdict by the registered gate: **not detected**, control-backed for this statistic only.
- Reading the result: synthetic English phrases split across two halves are re-paired by letter content almost every time.
  W.'s pairs are not, once length is taken out. The halves do not merge into English-like bigram text better than mismatched
  halves do. **Caveat (rule 3, SALV-DIAG shape):** the controls drop 0-3 letters per line, as in pairs.py, but the published
  design drops 3-12. The controls therefore do not bracket the target's omission level, so this is not a design negative.
  If T' power holds at 3-12 omissions, the result says that W.'s halves are not plain-English splits at the bigram level
  (heavy omission, abbreviation or another design). If power collapses there, T' is untestable at this N.
- No reading attempted, nothing graded (rule 4 n/a). Reproduce: `python3 gaps205_content.py --check` (writes and checks
  content_test.json, about 15 s).

## GAPS211 (4 Oct 2026, STALE4 for account 4, account 1 worker): T' with controls at 3-12 omissions

Account 4's GAPS211 claim (3 Oct 2026 19:18 UTC) had no done line and nothing pushed; re-run under STALE4
(.claude/briefs/runs/2026-10-04-acct3-stale4.md job 6). Script only, 0 vision, 0 subagents, 0 external requests.
Pre-registered in PREREG-GAPS211.md (commit 060e474f, pushed before any statistic was computed).

- Only change from GAPS205: the controls' omission count is drawn from 3-12 per line (pairs.synth had 0-3). Statistic,
  bigram model, E table, target null and seed are gaps205_content.py's own, imported unmodified.
- **T' (statistic unchanged from GAPS205) with controls at the design's 3-12-letter omission budget: target p 0.254 (T' -35.05, 20,000 re-pairings, reproduced exactly) vs positive controls P-coin/P-half power 0.65/0.45 at p < 0.001 (0.90/0.95 at p < 0.05) and unpaired control U-half FPR 0.05. Gate (max power >= 0.5, FPR <= 0.15) met: valid. Verdict by the registered rule: not detected at the
  design's omission budget**, control-backed for T' only. GAPS205's 0-3 negative is now bracketed at 3-12.
- Descriptive bands (10 texts per arm, no gate): power at p < 0.001 (coin/half) 0.80/1.00 at 3-5 omissions, 0.70/0.50 at
  6-8, 0.40/0.50 at 9-12; at p < 0.05 it stays 0.90-1.00 in every band; U-half FPR 0.00/0.00/0.10. Power thins at
  the top of the budget but the target (p 0.254) is far outside the 0.05 line that the controls clear 90-100% of the time.
- Reading: at the bigram level, W.'s halves do not merge into English better than mismatched halves, even against
  controls dropping as many letters as the published design. Either the halves are not plain-English splits (heavy
  abbreviation, names, Latin, another design) or the line pairing is not Ernst's; this test cannot say which. No bearing on
  any reading; nothing graded (rule 4 n/a).
- Reproduce: `python3 gaps211_content.py --check` (content_test_gaps211.json, about 13 s).

## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)
Read so far: unmeasured, because this repo holds no reading of its own (no key or plaintext, only the segmented ciphertext and the pairing test of step NEXT-CAT, 2 Oct 2026). The line structure is now measured. pairs.tsv has 29 pairs, 24 of them letter lines, and Bourdeau line k = Ernst [k] (k <= 10), [10a] (k = 11), [k-1] (k >= 12). Bourdeau's catokwacopa/NOTES.md (snapshot sources/cyphersolver/2026-10-02/catokwacopa/, sections 4-5) gives 7 lines decided by ordinary vocabulary, 5 name-frame lines that admit a unique name, and 5 lines not decided by the letters (his 9, 12, 23, 26, 29 = Ernst [9], [11], [22], [25], [28]).
- Bourdeau's lines 9, 12, 23, 26, 29 (Ernst [9], [11], [22], [25], [28], measured in pairs.tsv, step NEXT-CAT), both ad halves of each - blocker: not-attempted; no published reading is forced on these lines. Bourdeau's line-29 Latin search had only a positive control (line 17 -> QUI FIT) and no matched uniqueness control. Spec cheap test 3 never ran (specs/catokwacopa-1875.json). So "the omission rule fits almost anything" is untested here and cannot yet be graded too-short; next: run spec test 3 on our own copy (pairs.tsv, now on disk). Do an exact-fit search of the five lines against an enlarged period vocabulary under the 3-12-letter omission budget, with a matched control of synthetic English lines of the same length and budget, reporting both rates. As a second instrument, run QUEUE.md row 18's phrase-level LM search on line 23 with Bourdeau's positional prior (cyphersolver catokwacopa/search.py, MIT, cited), ~$5
- Lines with published but unforced readings (Bosbach's DYING DECLARATION; Estes/Dave's SUM TERM, 1853, BALLIOL; Ernst's 2018 [12]-[27] glosses, e.g. "[13] MOPT A PURLY ... IN COLLEGE", "[25] MOISTANT PURL", comment #26) - blocker: not-attempted; this repo has re-derived none of them, and spec cheap test 2 (re-derive the exact-fit name search over 1,645 period proper nouns) is unrun; next: run spec test 2, widened to names plus vocabulary from our own list, using gap 1's synthetic control. Grade each line forced (S) or guessed (M) per rule 4, and record where both reads agree, ~$3
- Further ads by W.: any 1875 ads after April, and any 1879 "FACT or FICTION" ads beyond the four on file. Ernst (24 Jul 2018 #1, #7) expects more, and no full 1879 issue search is on record. Filed so far: 27 Mar 1875 (sibling-1875-03-27.txt, step A2-CAT) and the four 1879 ads with two witnesses each (siblings-1879-fact-or-fiction.txt, step A2-CAT2, 2 Oct 2026). The 1879 attribution to W. is Ernst's, from placement, and is not established here. - blocker: not-attempted; the issue search and a page-image check of every filed sibling need BNA, which is login-gated from the cloud (the L13 route); next: file a LOCAL-QUEUE.tsv bna-search row beside L13 (The Standard p. 1 col. 2, May-Dec 1875 and Jan-Dec 1879, "W." and "FACT or FICTION", plus images of the five filed sibling ads), ~$0.5
- Ciphertext of both ads checked against the original Evening Standard issues of 8 and 20 May 1875 (BNA/newspapers.com) - blocker: waiting-on LOCAL-QUEUE.tsv row L13 (bna-verify, owner's desk runner, status queued); BNA and newspapers.com are login-gated from the cloud (LANE CX2 above). This does not block the gaps above, because the scienceblogs/Gaffney-Gluecklich scan and Ernst's BNA-checked text already agree 72/72 (ciphers/pollaky-1865-1875/NOTES.md, Test 2)

## Escalation (1 Oct 2026)
- [ ] siblings: pollaky-1865-1875 ads 3-4 are the same two ads from a second scan (two blind passes agree 78/80, and 72/72 against Ernst; see the NEAR.md pollaky row and the bPOL2 pointer above). The 27 March 1875 ad is filed (step A2-CAT; a singleton per Ernst #27). The four 1879 "FACT or FICTION" ads (25 Mar, 25 Apr clear, 11 Jun, 13 Jun) are filed as of 2 Oct 2026 (step A2-CAT2, siblings-1879-fact-or-fiction.txt). Schmeh's and Ernst's witnesses agree letter for letter. The attribution is Ernst's, by placement, and no page image has been checked. Not yet opened: any 1875 issue after April, any further 1879 ads, and other W. ads in Palmer/Gaffney. All of these need BNA (owner's desk). Planned: a LOCAL-QUEUE row beside L13 (gap 3), about $0.5.
- [x] clear-pages: the only clear text is the tail of ad 4 ("This will be intelligible if read in connection with my communication published in this column on the 8th inst.", ciphers/pollaky-1865-1875/ciphertext.txt AD 4). It is the pairing instruction, which every reading already uses. No clear copy or period decipherment of the plaintext is known.
- [n/a] known-keys: the design has no key. Each phrase is split into order-preserving halves across the two ads, with 3-12 letters dropped per line, so there is no key or nomenclator to try. KEY-OFFICES.tsv and KEY-DESIGN.tsv have no row for this target, and design_prior.py's code and nomenclator families do not fit this design.
- [x] print: read Cipherbrain's Top-50 post 8 with its 48 comments (on disk, sources/schmeh/posts/08-catokwakopa.txt), Bourdeau's catokwacopa/NOTES.md (commit 24 Sept 2026), Aymeloglu's SHORTLIST.md lines 81 and 148, and a web search for model-solve announcements (23 and 25 Sept 2026). None gives a unique plaintext. Not read: the newspaper issues (L13) and the 2015/2018 thread comments (folded into siblings).
- [ ] key-rebuild: the segmented line pairs are now on disk (pairs.tsv, step NEXT-CAT, 2 Oct 2026; pairing test 0/100,000 vs a control with power 0.80-1.00). We have run no forced-fit, vocabulary or LM search, and none appears in NOTES.md, ROOM.md or LEDGER.md. Bourdeau's exact-fit name search and his line-29 Latin search are his work, not re-derived, and neither has a matched uniqueness control. Planned: spec tests 2-3 with a synthetic-line control, plus the line-23 LM search from QUEUE.md row 18 (gaps 1-2). 3 Oct 2026 (GAPS205): content-axis pairing test T' run: target p 0.254 vs control power 0.95-1.00 and FPR 0.05, so pairs are not detected by letter content at 0-3 control omissions; the controls do not yet bracket the 3-12 budget. 4 Oct 2026 (GAPS211): bracketed: at 3-12 control omissions T' is still valid (power 0.65/0.45, FPR 0.05) and the target p 0.254 is still not detected.
- [x] image-check: ciphers/pollaky-1865-1875/NOTES.md Test 2. Two blind passes over the scienceblogs/Gaffney-Gluecklich scans agree 78/80, and both disagreements were settled from the image (caselcluchozamot S; Ngtndusdcndo M, low-resolution scan). The result matches Ernst's BNA-checked ads.py 72/72 letter-words with digits and dashes stripped; Hrsclam and 138 match Ernst, against Schmeh's printed Hfsclam and 139.
- [ ] retry: nothing to rerun yet, because key-rebuild has not run. Planned: after spec tests 2-3, re-score every line pair (the five unread lines and the unforced lines) with the extended vocabulary and regrade S/M per rule 4.
Verdict: keep going: 3 internal gaps; cheapest next: file a LOCAL-QUEUE.tsv bna-search row beside L13 for The Standard p. 1 col. 2 (May-Dec 1875, 1879) and page images of the five filed sibling ads (gap 3), ~$0.5; then spec tests 2-3 with a synthetic-line control (gaps 1-2), ~$5. GAPS211 (4 Oct 2026): T' re-run with controls at the published 3-12-letter omission budget: target p 0.254 vs power 0.65/0.45 at p < 0.001 (0.90/0.95 at p < 0.05), FPR 0.05: valid, not detected at the design's budget (GAPS205's 0-3 negative now bracketed)

## While waiting (RUN4-WAITBF, 4 Oct 2026)

- Action that depends on nobody: spec tests 2-3 (specs/catokwacopa-1875.json) on our own pairs.tsv with the synthetic-line control at the 3-12-letter omission budget (gaps 1-2, the Verdict's second step), ~$5; the LOCAL-QUEUE bna-search row (gap 3) is the only part that waits on the owner's runner.
