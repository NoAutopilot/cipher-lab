# erba-2006

open

Minimal check-solved (LANE B3 bERB, 25 Sept 2026, no `ciphers/<slug>` folder existed before this pass, so the
breadth.md intake step's minimal check-solved route was used, not `tools/intake_gate_check.py`'s edition/page
citation form -- there is no edition to cite; the source is a blog post read in full, quoted below): read
Schmeh's Cipherbrain post 24 in full (`sources/schmeh/posts/24-erba.txt`, already on disk, fetched by bSPEC2
25 Sept 2026), including its 10-comment thread. Schmeh's own text: "I don't know if police has deciphered this
message. If so, they have never published the solution. Can a reader solve it?" -- distinguishing this 2013
bible-hidden message from the OTHER, already-solved 2006 MASC-with-nulls cryptogram police broke at trial
("Police had no trouble breaking it," out of scope for this target). Shallow-cloned both solver repositories
(`git clone --depth 1`, grepped, deleted): dbourdeau/cyphersolver's `TARGETS.md` line 242 lists it as a target,
"Erba murder, 2006 | low | Blocker is sourcing: only a press photograph, no authoritative transcription" -- no
folder for it under the repo's per-target directories, i.e. no attempt or reading on file there; word-boundary
grep for `erba`/`olindo` found nothing else project-specific (broad substring hits were noise from unrelated
Latin/French corpus text, discarded). aaymeloglu/unsolved-ciphers: no hits for `erba` or `olindo` anywhere in
the repo. OpenAlex (`works?search=Erba murder cipher Olindo Romano`, keyed): 0 results. Semantic Scholar
(`paper/search?query=Erba murder cipher Olindo Romano`, keyed, one 429 then one retry after a pause per the
good-citizen rule): 0 results. Verdict: **open**, unsolved as far as any of these five sources shows; nothing
found contradicts Schmeh's own "never published" note. Per rule 10, this is a search result, not a novelty
class -- no verifier has run.

Status vocabulary (rule 5): `open`.

Intake gate output (`python3 tools/intake_gate_check.py erba-2006`):
```
erba-2006: open (line 3) -- edition/page or full-text-search citation found within 6 lines
exit=0
```

## Cheap test 1 (25 Sept 2026, LANE B3 bERB)

Fetched both images named in the spec from scienceblogs.de (2 requests, >=2 s apart, browser UA):
`Erba-Cryptogram.png` (300x436, the cryptogram page itself) and `Erba-Bible.png` (614x460, the wider bible-page
photo for context); both to `images/`, manifest at `images/manifest.json` (URL, sha1, size). Folder 4.4 MB,
well under the 30 MB cap.

**Blindness caveat, stated plainly (rule 4/7 honesty over a clean claim):** the brief's intended order was
transcribe-from-image first, then open comment #3's text. That order was not achievable here: `specs/erba-2006.json`
(read in full before any test could be run, to learn what test 1 even was) already quotes comment #3's full
transcription verbatim in its `ciphertext` field. So this re-transcription is independent in the sense that it
was done by looking only at the image (not at the transcription text while reading pixels), but not blind in
the stronger sense of "written before ever seeing Marc's reading" -- I had already read Marc's string once,
earlier in this same session, before opening the image. Flagging this rather than calling it blind.

Re-transcription method: upscaled `Erba-Cryptogram.png` 8x (Lanczos, via Pillow -- `pip install pillow`, no
other image tooling available in this container) and read it in four overlapping horizontal strips plus five
targeted zoom crops on specific ambiguous tokens (`specs/cheap-tests/erba-2006/`; crop scripts inline in this
NOTES section were one-off `python3 -c` calls, not saved as a separate tool -- not reused elsewhere in the
repo). Read in natural page order: two full-width lines at the top (the plaintext Italian lead-in "Pochi
giorni prima - Poi" then cipher begins), then eight ruled lines each split left/right by the flower
illustration in the page's middle, then three more full-width lines, then two side blocks (highlighted yellow)
beside the child illustration and the glued-in "Amare" ("to love", Italian) magazine clipping at the bottom --
both illustrations and the clipping confirmed non-cipher by eye, consistent with comment #3's "(Bild)" markers.

Transcriptions: `specs/cheap-tests/erba-2006/transcription_bERB.txt` (this pass) and
`transcription_marc.txt` (comment #3, reordered from its own slash/Bild-separated single string into one
cipher-fragment per line, same order, to make the diff mechanical -- no token content changed). Diff script
`diff_transcriptions.py`, output `diff_output.txt`:

```
tokens: bERB=114 marc=114 compared=114
case-sensitive exact match: 105/114 = 92.1%
case-insensitive (digraph-identity) match: 106/114 = 93.0%

disagreements (index, bERB, marc):
    8  'me'   vs 'ne'
   14  'me'   vs 'ne'
   29  'me'   vs 'ne'
   31  'me'   vs 'ne'
   41  'me'   vs 'ne'
  102  'me'   vs 'ne'
  111  'me'   vs 'ne'
  113  'me'   vs 'ne'
```
Plus one case-only disagreement not in that list (index 5, "Ro" vs "ro" -- I read it capitalised, matching
every other "Ro" token in the document including Marc's own; likely a one-off casing slip in the comment, not
a digraph disagreement).

**Reading: 93.0% digraph-identity agreement (106/114 tokens), all 8 disagreements the same me/ne pair.**
Every position where I read "me" or "ne" was individually judged from the pixels, not applied uniformly (my
own transcription itself contains both readings in different places, matching Marc's "ne" at every position
except these 8) -- so this is not a systematic misreading of one hand for the other, but eight specific tokens
where the cursive "m" (three humps) and "n" (two humps) before "e" are hard to tell apart at this photograph's
resolution. Zoomed crops for the clearest two cases are on disk
(`ciphers/erba-2006/images/zoom_blockleft.png`, `zoom_blockright.png`): both show a clear three-hump "m",
which is why I read "me" there against Marc's "ne" -- but I did not independently re-verify a period professional's
eye against a higher-resolution original, so this stays a call, not a settled correction. Grade M (uncertain,
single pass, not reconciled against a second reader) for the 8 me/ne tokens and the 1 Ro/ro token; grade S
(this pass's own cryptanalytic-adjacent read) is not applicable here -- this is transcription, not decipherment.

**Material spec update, flagged, not applied here beyond the `alphabet` field below:** if any of the 8 "me"
readings is correct, the base-token alphabet is 9 tokens (cu, mi, xs, fi, un, ro, ne, pi, **me**), not the 8 the
spec's `alphabet` field states following comment #2/#3's count. `specs/erba-2006.json` `alphabet` field updated
to note this open question; `cheap_tests_in_order[2]`'s K=8-14 estimate is now K=9-16ish pending resolution.
This is exactly the kind of image-vs-transcription gap rule 2 warns about -- the community transcription was
the only thing on file before this pass.

No control applies to a transcription-agreement test (not a decode); reporting per rule 7 without one, as the
breadth brief's test 1 asks (a control gate applies from test 3 onward). No judge run this test (nothing to
judge -- a transcription, not a candidate plaintext).

Requests this pass: scienceblogs.de 2 (image fetches, >=2 s apart; the post fetch itself was bSPEC2's, not
recounted here), github.com 2 shallow clones (dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers, both
deleted after grep), api.openalex.org 1, api.semanticscholar.org 1 (429 then one retry after a pause).
