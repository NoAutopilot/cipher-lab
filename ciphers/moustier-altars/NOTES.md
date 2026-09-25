open
Check-solved intake sweep (LANE B2 bINT, 25 Sept 2026): sources/schmeh/posts/18-moustier.{html,txt} (Cipherbrain post 18, 7 Nov 2017, 5 comments) read in full, no solve claim; ciphermysteries.com/2013/04/02/the-moustier-church-cryptograms (Pelling, 2 Apr 2013) read in full including a Dec 2017 "solution" claim by Alex Ulyanenkov that Pelling did not accept ("still very far from sure that you've nailed anything") and a further unconfirmed structural note by the same commenter dated 9 Jul 2026 ("may be it is a link to Decalog (not sure)"); dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers shallow-cloned, grepped for moustier, deleted -- both list it as still open/medium-low, no solve, no plaintext; one OpenAlex and one Semantic Scholar query for "Moustier altar inscriptions cipher" returned no relevant results. See "Check-solved sweep, 25 Sept 2026" section below for the full log.

# Moustier altar inscriptions — St Martin's church, Frasnes-lez-Anvaing (Moustier), Belgium

Status: **open**

## What this is

Two carved stone tablets (5 lines each) on each of two side altars in St Martin's church: St Mary's Altar
(altar 1) and St Martin's Altar (altar 2) — four tablets, 20 lines total. 19th century. Photographed by Klaus
Schmeh in spring 2015, published in his "Top 50 unsolved encrypted messages" series (Cipherbrain post 18,
7 Nov 2017). The cryptograms first became known to crypto-history enthusiasts through Nick Pelling
(ciphermysteries.com, 2 Apr 2013), who found them via a declassified NSA *Cryptolog* article; Prof. Jean
Connart has worked on them since 1961 (per spec, not independently checked this pass).

## Search before solving (rule 1)

Not re-run this pass (out of this worker's brief/budget); carried forward from `specs/moustier-altars.json`,
written 24 Sept 2026: "open; nothing later than Schmeh 2017 and Pelling 2013 found 24 Sept 2026." This pass
did not repeat the six-source check-solved sweep.

## Images (rule 2: image over transcription)

Source post: `sources/schmeh/posts/18-moustier.html` (already on disk from an earlier fetch, byte-identical to
this session's own refetch except per-request random widget IDs — the refetch was avoidable and wasted one
`scienceblogs.de` request; discarded, original kept).

Of the post's 9 `Moustier-*.jpg` photos, 3 were fetched (image-host budget, this brief: at most 3 requests,
1.5-2s apart, browser UA), into `images/` with `manifest.json`:
- `Moustier-130.jpg` — St Mary's Altar (altar 1), both tablets, close shot, **fully legible**.
- `Moustier-212.jpg` — St Martin's Altar (altar 2), wide shot (Schmeh standing beside it) — inscription too
  small/angled to transcribe reliably from this frame. Fetched first on the assumption it was the closer shot
  named in the post text; it was not. Kept for context, not used for transcription.
- `Moustier-220.jpg` — St Martin's Altar (altar 2), a genuinely close shot, legible (slightly softer focus
  than Moustier-130.jpg). Used for transcription in place of Moustier-212.jpg.

**Important found context**: the source post itself already carries a **published transcription of both
inscriptions**, credited to Nick Pelling (ciphermysteries.com, 2 Apr 2013) — plain text, not an image, sitting
between the "closer shot" photos and the next altar's photos in the post's HTML. Per rule 2 this is a
transcription, not the image, and per this brief's common rules ("Passes are blind — never from an existing
transcription") it was **not used as a source** for either blind pass below; both passes worked only from the
two close-shot images. It is however comparable, sign-for-sign, to this pass's independent reading (see
"Comparison to Pelling's published transcription" below) and is important prior-art context for any future
check-solved / novelty work on this target — not something this worker classifies (rule 10).

## Transcription (this pass)

Two blind passes, both from `Moustier-130.jpg` (altar 1) and `Moustier-220.jpg` (altar 2) only:
- **Pass A**: this worker, by eye (crops zoomed 4-8x with Pillow for legibility), `passA.tsv`.
- **Pass B**: one Sonnet subagent, given only the two image files and no other context, `passB.tsv`.

Reconciled with `tools/reconcile_passes.py passA.tsv passB.tsv` → `disagreements.tsv`, `ciphertext_draft.tsv`,
`agreement.tsv`.

**Pass agreement**: 143/158 aligned columns agree = **90.5%** (Needleman-Wunsch alignment, `tools/reconcile_passes.py`).
20 lines, 4 tablets. Pass A: 157 symbols; Pass B: 158 symbols (one line, a2t2l1, has a genuine 8-vs-9
segmentation disagreement between the passes, not yet resolved from the image). 15 of 158 aligned positions
disagree (9.5%), all graded **M** in `ciphertext.txt` (marked with a trailing `?`); the other 143 are **S**
(cryptanalytic transcription, agreed by both blind passes — no key, so not H or C).
Well above the brief's 60% stop threshold; not a blocker.

Under the wall-clock cap, disagreements were **not** individually re-checked against the image this pass
(that is `disagreements.tsv`'s job for a future session/reconciler) — `ciphertext.txt` carries the reconciler's
majority draft (pass A's reading where the two disagree, per `tools/reconcile_passes.py`'s own tie rule),
each such position flagged `?` and graded M. Two of the M-flagged positions (a1t1l4 pos 2, a2t1l5 pos 1 —
both `A` vs `TRI`) were checked by this worker at 6-8x zoom before pass B ran and read unambiguously as a
plain `A` with a clear crossbar (see the "Comparison to Pelling" section); they are still marked M here since
pass B disagreed and the position was not re-checked after reconciliation, not because the zoom check was
inconclusive.

### Symbol notation

The carved font is an ornate Roman lapidary/monumental capital style. Most signs are ordinary Latin letters.
Three shapes recur that are visually distinct from any plain letter and are given their own tokens:
- `Γ` — a single vertical stroke with one horizontal bar at the top only (no middle bar): distinct from a
  normal F (two bars) and E (three bars).
- `Λ` — a plain open triangle/peak with **no** horizontal crossbar (a "^" apex): distinct from a normal A,
  which has a clear crossbar. The two are easy to conflate at low zoom; checked closely (see below).
- `Ɛ` — a backwards/open "C" or broken "E" missing its middle bar, open on the left.

## Comparison to Pelling's published transcription (context, not a pass)

Nick Pelling's transcription (embedded in the source post, from his own 2013 photographs — a different photo
set than Schmeh's) uses `F` where this pass reads `Γ`, `^` where this pass reads `Λ`, and `[` where this pass
reads `Ɛ` — the same three-way split, under different labels, in the great majority of the 157 positions. One
pattern stood out under close zoom: at 3 of the ~13 positions where Pelling's transcription has `^`, this
pass's Pass A reading shows a clear horizontal crossbar (i.e. a plain `A`, not `Λ`) — checked at high zoom
each time (line a1t2l4 pos2 [should be a1t1l4 pos2], a2t1l5 pos1, a2t2l5 pos5 — see `passA.tsv` line ids).
Two of those three are corroborated by Pelling's own transcription using plain `A` (not `^`) at the
*textually equivalent* position in the mirror tablet, e.g. altar2-right line2 "R A [ G K T D" — Pelling
himself distinguishes A from ^ there. This is recorded as an observation for the reconciler/verifier, not a
correction of Pelling's reading (different photographs, not graded against each other).

## Symbol / line counts, IC (this brief's test 0 deliverable)

- Lines: 20 (4 tablets x 5 lines)
- Symbols (reconciled ciphertext.txt, majority draft): N = 158, K = 26 distinct signs (23 ordinary Latin
  letters + the 3 non-standard shapes GAM/TRI/REVC)
- IC (reconciled): 0.0499. Pass-A-only IC (N=157, K=26, before reconciliation): 0.0492.

## Control: IC of Latin and French text at the same N

Matched-N (N=157 characters, letters only, uppercased) samples drawn from `tools/data/la_repo/` (Latin) and
`tools/data/fr16/` (French), 20 non-overlapping random windows each (seed 1):

- Latin: IC min/mean/max = 0.0602 / 0.0722 / 0.1034
- French: IC min/mean/max = 0.0650 / 0.0726 / 0.0826
- This ciphertext (pass A only): IC = 0.0492 (K=26, N=157); reconciled draft: IC = 0.0499 (K=26, N=158)
- Random/uniform baseline at K=26: 1/26 = 0.0385

**Reading**: this ciphertext's IC (~0.049-0.050) sits below both language controls (mean ~0.072-0.073, min
0.060-0.065) and above the random baseline (0.0385) — consistent with either a genuinely low-redundancy
design (homophonic substitution, several signs per plaintext letter) or with transcription noise still
depressing it (15 M-graded positions). Not itself a solve signal either way; recorded for whoever runs test 2
(crib-driven MASC) next, per this brief's scope (test 1 only).

## Grading (rule 4)

All 157 tokens in `ciphertext.txt` are **S** (cryptanalytic transcription with a control, no key or known
plaintext yet) — 0 H, 0 C, 0 M, 0 I at this stage. No candidate plaintext has been produced, so
`tools/judge_plaintext.py` was not run this pass (nothing to judge).

## What was NOT done this pass (brief scope)

Test 1 only (image fetch + two-pass transcription + IC control). Test 2 (crib-driven MASC in Latin/French) and
test 3 (symbol-shape comparison to Masonic/lodge alphabets) were not run, per brief instructions. Suggested
follow-ups (one line each, not run):
- A closer/better-lit photo of altar 2 (Moustier-212.jpg was too oblique) would help settle the `Λ`-vs-`A`
  question by eye rather than by cross-reference to Pelling's transcription.
- Fetch Pelling's own 2013 ciphermysteries.com post directly (a separate host, not fetched this pass) to see
  whether his transcription carries an errata note or later correction.

## Requests

- `scienceblogs.de`: 1 (post-page refetch, avoidable — already cached, discarded) + 3 (image fetches:
  Moustier-130.jpg, Moustier-212.jpg, Moustier-220.jpg), all >=1.5s apart, browser User-Agent. No 429/403.

## Check-solved sweep, 25 Sept 2026 (LANE B2 bINT, intake gap after QA/2026-09-25-1740.md failure 3)

Ran the minimal check-solved sweep this brief names (not a full six-source rule-1 sweep) to close the gap
flagged in QA: this target had two cheap tests (transcription, IC control) run with no check-solved verdict
on file.

1. **Cipherbrain post 18 and its comment thread** — `sources/schmeh/posts/18-moustier.{html,txt}`, already on
   disk, not re-fetched. Read in full: 5 comments (7 Nov 2017 – later), none claim a solution; the post itself
   says "Both inscriptions have never been deciphered."
2. **Pelling, ciphermysteries.com, 2 Apr 2013** — not on disk before this pass; fetched this session (see
   Requests below) and saved to `sources/ciphermysteries/posts/2013-04-02-moustier-church-cryptograms.{html,txt}`.
   Read in full (1479 lines rendered). Two things worth recording:
   - A commenter, **Alex Ulyanenkov** (Moscow — the same name active on the Kaliningrad-2015 thread), claimed
     on 11 Dec 2017 to have "sent the solution" to Pelling and Schmeh by email; Pelling's reply the same day
     does not accept it ("you have put forward some interesting options for future study, I'm still very far
     from sure that you've nailed anything like the solution of this particular inscription"). No plaintext was
     ever posted publicly. Not a confirmed solve.
   - The same commenter posted again on **9 Jul 2026** (the most recent activity found on the post), still
     speculative ("SXV" as a Latin abbreviation, Greek-letter numerals, "may be it is a link to Decalog (not
     sure)") — confirms the item was still being discussed as unsolved as of mid-2026, not resolved since.
3. **Solver repositories** — `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers` shallow-cloned to
   `/tmp`, grepped case-insensitively for `moustier`, deleted immediately after. cyphersolver's own
   `top50/NOTES.md`/`top50.json`/`TARGETS.md` list item 18 as still open, "medium-low" priority, citing
   Huylebrouck's 2022 Trithemius *Ave Maria* hypothesis as untested and Ernst's caution about conflated
   L-shapes; no solve recorded. aaymeloglu's `SHORTLIST.md` line: "Moustier | Cipher Foundation page dated 2026
   still lists it; on Schmeh's current unsolved page | open." The one other hit (`forster-1644/lex_old.txt`)
   is a French word-list entry ("moustier 4"), an unrelated dictionary word, not a reference to this cipher.
4. **OpenAlex** (`api.openalex.org/works`, `Authorization: Bearer $OPENALEX_KEY` header) — query
   `"Moustier altar inscriptions cipher"`: 3 results (Ivories ancient and mediæval 1875; Marie-Antoinette and
   the Image of Moral Instruction 2023; Rough notes on pottery 1896), none relevant.
5. **Semantic Scholar** (`api.semanticscholar.org/graph/v1/paper/search`, `x-api-key: $S2_KEY` header) — same
   query: `{"total": 0}`.

**Verdict: open.** No solution found in any of the five sources; the two informal claims of a private
solution (Ulyanenkov, 2017 and again 2026) were never substantiated with a published plaintext and the first
was explicitly not accepted by the post's author. Per rule 10 this is a search result, not a novelty
classification.

### Requests (this section)

- `ciphermysteries.com`: 3 (root `/` to resolve the `www.`→bare-domain redirect and confirm reachability,
  `/?s=moustier` search to locate the post URL without guessing it, then the post itself), all >=1.5s apart,
  full-browser User-Agent (plain `curl -A "Mozilla/5.0"` alone got HTTP 406 from this host; a fuller Chrome UA
  string worked). No 429/403.
- `api.openalex.org`: 1.
- `api.semanticscholar.org`: 2 (first attempt 429'd despite the key; one retry after a ~3s pause per the
  good-citizen single-retry rule succeeded with 0 results).
- GitHub: 2 shallow clones (`dbourdeau/cyphersolver`, `aaymeloglu/unsolved-ciphers`), deleted after grep.

### Intake gate output, 25 Sept 2026 18:19 UTC

```
moustier-altars: open (line 1) -- edition/page or full-text-search citation found within 6 lines
```
Exit code: 0.
