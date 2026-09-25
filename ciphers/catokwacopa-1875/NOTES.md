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
