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

<!-- RECONCILE_RESULTS -->

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

<!-- COUNTS_RESULTS -->

## Control: IC of Latin and French text at the same N

Matched-N (N=157 characters, letters only, uppercased) samples drawn from `tools/data/la_repo/` (Latin) and
`tools/data/fr16/` (French), 20 non-overlapping random windows each (seed 1):

- Latin: IC min/mean/max = 0.0602 / 0.0722 / 0.1034
- French: IC min/mean/max = 0.0650 / 0.0726 / 0.0826
- This ciphertext (pass A): IC = <!-- IC_A --> (K=<!-- K_A -->, N=157)
- Random/uniform baseline at K=26: 1/26 = 0.0385

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
