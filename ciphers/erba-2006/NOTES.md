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

## Web and blog check (GF4-BATCH21 (account-4), 3 Oct 2026)

Plain web searches (WebSearch, 3 Oct 2026): (1) `Olindo Romano Bibbia codice cifrato messaggio Rosa Bazzi decifrato` (people + document, Italian) -- hits are mostly the 2008 "codice Olindo" press (Tgcom24 399967, Pupia.tv, xmau.com, italoeuropeo, iltuocruciverba, hwupgrade forum, wildgreta), i.e. the EARLIER pigpen/MASC "Libro dei morti" system the police broke, out of scope here; two 2013 hits opened (below); (2) `"Erba murder cryptogram"` (folder's descriptive title) -- Cipherbrain posts only (2014, 2017, 2021 EN/DE), Wikipedia "Erba Massacre"; (3) `"cu Mi" "xs fi" cipher Erba` (distinctive ciphertext run in quotes) -- only Cipherbrain post 24 (on disk), rest noise; (4) `Erba murder cryptogram Olindo Romano bible solved OR solution OR Claude OR GPT` (model-solve check) -- no solve announcement, by a model or anyone; hits are the Cipherbrain posts and general case coverage (Il Sole 24 Ore, Scotsman, IMDb, HubPages).
Hits opened, what each says about THIS item (the 2013 digraph bible message):
- Tgcom24, "Il diario di Olindo scritto 'in codice' per Rosa", 18 June 2013 (tgcom24.mediaset.it/cronaca/articoli/1101029/...): prints two further coded phrases in the same digraph system from Olindo's prison writings, "Fimine Romixsmecu meficumixs" and "fine xs Romi cufiRome Ro", "almost certainly dedicated to his wife"; no decipherment, method or decipherer given. Sibling ciphertext only (noted for the transcription question: it contains `me`, cf. the me/ne note in Cheap test 1 -- not decoded here).
- il Giornale, "Il diario di Olindo in cella: un inno (in codice) a Rosa", 18 June 2013 (ilgiornale.it/news/interni/diario-olindo-cella-inno-codice-rosa-928061.html): same two phrases; "Cosa voglia dire lo sa solo Olindo Romano"; the journalist's own guess that one group "sembra un ti amo, chissà" -- a guess, not a decipherment.
Blog site searches, in the brief's order: Cipher Mysteries (`ciphermysteries.com/?s=Erba`): plain curl answered HTTP 406 (not retried by curl); the one permitted retry by a different route (WebFetch) returned 10 results, all herbal/Voynich posts ("erba" = herb), nothing on this item. Cipherbrain (`scienceblogs.de/klausis-krypto-kolumne/?s=Erba`, pages 1-2): relevant posts are (i) post 24, 15 Aug 2017, 10 comments -- read from disk (`sources/schmeh/posts/24-erba.txt`, zero requests): #1 Wilson (pairs), #2-#3 Marc (digraph inventory and transcription), #4-#5 KunstundKetschup (page/verse-number speculation), #6 Esme (gloss of the Italian lead-in), #7-#9 Davidsch (press background; "at least three bibles"; stops), #10 Schmeh (thanks); no decipherment; (ii) "Der Vierfachmord von Erba und das verschlüsselte Tagebuch", 18 Sept 2014, 9 comments (opened): mainly the solved 2008 system; werner67 posts the 2013 images; Dario describes the 2013 text as "mostly pronounceable", says he would "rather fold", and in his last comment that the 2013 solution is known to the authorities but "no complete description is publicly available" -- no plaintext; (iii) "Ein kryptologischer Cold Case: Das Erba-Kryptogramm", 10 July 2021, 1 comment (opened) and its English version "A Cryptological Cold Case: The Erba Cryptogram" (comments closed, redirected to the German post): Schmeh, "My readers posted numerous interesting comments, but no one found the solution. The police, on the other hand, are said to have succeeded in deciphering the text -- possibly with the help of additional information that was kept secret. However, details have never been published." The one comment (Christof Rieber, 11 July 2021) proposes a capital-letter word segmentation and a "+/-8" key idea, no plaintext. Other page-1/2 results (Riverbanks Ripper, criminal-gang codes 2015, "Cracking the Code" TV 2022, Fenn, RAF) are fuzzy matches, not about this item. klausschmeh.net (`?s=Erba`): "Nothing Found"; its "Solved cryptogram" category page (4 posts: Koehler, Copenhagen, WWII Enigma, ADFGVX): nothing on Erba. Cryptiana: on-disk `sources/cryptiana/` grep (zero requests) -- the only hit, `web/porta.htm`, is "verba" in a Porta chapter title, noise; live `cryptiana.blogspot.com/search?q=Erba`: "No posts matching the query".
New-publication check: apeiron.re front page: no listing of solved items, no mention of Erba; Cabinet Noir (github.com/el-descifrador/cabinet-noir, shallow clone HEAD 47b6db9, 2 Oct 2026, 26 historical diplomatic targets) word-boundary grep `erba|olindo|bazzi`: no hit.
Result: no decipherment or plaintext of this item located by these queries on 3 Oct 2026 (a search result, not a novelty verdict, rule 10). Two sources (Dario 2014, Schmeh 2021) report that the police are *said* to have deciphered it without publishing details; that is a rumour of an unpublished decipherment, not a published one, and is recorded here so a verifier weighs it (an N-class above N3 would need it excluded). Status word unchanged.
Requests: WebSearch 4; scienceblogs.de 5 (2 search pages, 3 posts opened); klausschmeh.net 2; cryptiana.blogspot.com 1; ciphermysteries.com 2 (curl 406, then one WebFetch retry); tgcom24.mediaset.it 1; ilgiornale.it 1; apeiron.re 1; github.com 3 shallow clones (cabinet-noir, dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers; the last two deleted after grep). All >=3 s apart, one at a time.

## Premise check (GF4-BATCH21 (account-4), 3 Oct 2026)

(a) Folder's own mentions: **not found** -- NOTES.md and `specs/erba-2006.json` mention no decipherment, gloss or clear copy of the 2013 message; the only "deciphered" material they name is the separate 2008 pigpen/MASC system (police, trial evidence), which is out of scope. The one clear-text element is the Italian lead-in "Pochi giorni prima - Poi", already flagged as plaintext, not a decipherment. No REQUEST.md exists.
(b) Other solvers' working files: **not found** -- dbourdeau/cyphersolver (shallow clone HEAD a439937, 3 Oct 2026): only `research/top50/NOTES.md:102` ("The blocker is sourcing: only a press photograph circulates") and the top-50 list files; no `targets/` folder, output or rendering for Erba. aaymeloglu/unsolved-ciphers (HEAD d2800bb, 27 Sept 2026): no `erba`/`olindo` anywhere. On-disk snapshots under `sources/` (cyphersolver, cyphersolver-site, bourdeau, openai, vals-ai): no hit. Cabinet Noir: no hit.
(c) Neighbours: **not found / partly unreachable** -- only one page of the bible is public (the frontedelblog.it 2013 photograph, cropped by Schmeh to Erba-Bible.png and Erba-Cryptogram.png, both on disk). Its other marks (yellow highlights, "8" and "1" near the flowers, "NE.Micu." between bible lines per comment #4) are discussed in the thread but none is a clear copy. Davidsch (2017) notes at least three bibles exist; the other pages and bibles are not online. Sibling ciphertext in the same system (Tgcom24 / il Giornale, 18 June 2013) is printed without a reading.
(d) Recipient's side: **unreachable** -- the recipients were Rosa Bazzi (in Bollate prison) and, for the 2013 bible, Olindo's lawyer (frontedelblog.it 2013, quoted in comment #7); any police decipherment would sit in Italian court or prison files, not in a public edition. Press coverage searched (queries 1 and 4 above) prints no decoded text.
Verdict: the premise holds -- no published decipherment located; the item stays `open`. Caveat for any later reading: an unpublished police decipherment is reported second-hand (Dario 2014, Schmeh 2021), so a reading's novelty class is capped accordingly by the verifier, not by this pass.

Gate after this pass (3 Oct 2026, GF4-BATCH21):
```
erba-2006: open (line 3) -- edition/page or full-text-search citation found within 6 lines
exit 0
```

## Next step (NO-CRACKS, 5 Oct 2026)

[done 6 Oct 2026 by R12D-ERBA, see Cheap test 2] spec test 2: re-segment the confirmed digraph sequence on `xs` and compare its word-length profile with an unsegmented and a randomly segmented control (specs/erba-2006.json cheap_tests_in_order[1]), ~$1. Who acts: agent. Source: specs/erba-2006.json (test 1 done 25 Sept 2026, test 2 not run); written by NO-CRACKS (account 3) because tools/next_steps.py found no next-step line in this file.

## Cheap test 2 (6 Oct 2026, R12D-ERBA, LANE LANE-RUN12-account-4): is `xs` a word space?

Pre-registered (`specs/cheap-tests/erba-2006/PREREG-test2.md`, pushed b9e4d2183 before the scored run). Disk only, zero
network requests. Input: the image-checked reading (`transcription_bERB.txt`, 114 tokens; the 8 open me/ne calls cannot move
this statistic, which depends only on where `xs` falls). Split on `xs` within three streams (main 95, block right 12, block
left 7); S = mean log P(word length) under `tools/data/it19` (Italian prose 1800-1830 -- era mismatch to a 2013 private
message, no modern Italian corpus on disk; it19's own README rates its gate reliability unknown). Null: 10,000 random
placements of the xs tokens. Matched control: 200 windows of real it19 prose in the design's units, real spaces as the
separator, same stream lengths, same statistic and null. Output: `specs/cheap-tests/erba-2006/test2_output.txt`.

| design | target S | target p | xs rank among 9 split tokens | control power (gate 80%) | separators: target vs control 5-95% | verdict |
|---|---|---|---|---|---|---|
| L: one token = one letter | -2.693 | 0.0039 | 1/9 | 190/200 = 95.0% | 14 vs 16-23 | PASS |
| Y: one token = one syllable | -5.466 | 0.481 | 4/9 | 200/200 = 100% | 14 vs 33-40 | FAIL (control-backed) |

Unsegmented streams: S -4.938 (L), -9.124 (Y). Word lengths between xs (main stream): 2, 7, 6, 10, 1, 12, 11, 11, 8, 9, 4,
3; side blocks 1, 6, 3 and 2, 4.

Post-hoc, not pre-registered (`posthoc_token_p.txt`, 5,000 permutations, same statistic, design L): fi p=0.025, ro p=0.039,
mi 0.091, un 0.137, cu 0.415 (xs 0.003). So the design-L PASS mostly measures that xs is evenly spread through the text
(never doubled), which a word separator would be but other tokens partly are too: xs is the strongest of six, not unique.

What this does and does not show: under a one-token-per-syllable design, xs cannot be the word space at this N (control-backed
negative: far too few separators). Under a letter-like design, xs-as-space is not excluded and xs fits best of the nine
tokens, but it is not established either: it gives fewer and longer words than Italian (four of 10-12 tokens), and the
press-printed sibling groups of 18 June 2013 (see Web and blog check above) write xs inside groups ("Romixsmecu",
"meficumixs") as well as alone ("fine xs Romi"). Segmentation remains open; nothing was read.

## Next step (R12D-ERBA, 6 Oct 2026)

[done 6 Oct 2026 by R12D-ERBA3, see Cheap test 3] spec test 3 (specs/erba-2006.json cheap_tests_in_order[2]): small-alphabet homophonic anneal against Italian with a
matched synthetic control at N=114, K=9 base tokens (14-16 with case); per test 2, model the design as letter-like units
(xs as an optional separator, run both with and without it), not one-syllable-per-token with xs as space, ~$2-3. Who acts:
agent. A modern (post-1950) Italian corpus in tools/data would remove the it19 era caveat from both tests (~12 min build).
[done 6 Oct 2026 by R12D-ERBA3, see Cheap test 3: corpus tools/data/it21news built; test 3 run in the letter-like design]

## Cheap test 3 (6 Oct 2026, R12D-ERBA3, LANE LANE-RUN12-account-4): letter-like design, modern corpus

**Corpus.** Built `tools/data/it21news` (Italian Wikinews dump of 1 Oct 2026, CC BY 2.5; five year-folds 2005-2026, 2.5M folded
letters; README and build.py there). Era-matched to a 2006-2013 note; register is news, not letters. LOFO real-prose
false-negative rate (judge_plaintext.py --holdout): N=114 14.1% (folds 8.0-21.0%), N=300 18.7% (11.0-30.0%).

**Test 2 era rerun** (PREREG-test2.md statistic and gate unchanged, corpus swapped; `test2_output_it21news.txt`): design L
S=-2.668, p=0.0032, xs rank 1/9, control power 179/200 = 89.5%, PASS; it19 gave -2.693, p=0.0039, 95.0%. The era caveat does
not move it. Modern-Italian control separators 14-21 (5-95%) now bracket the target's 14 (it19: 16-23).

**Test 3** (PREREG-test3.md, pushed c6e924c4b before the scored run; `test3_letterclass.py`, `test3_output.txt`). With 9
case-folded token types and ~21 Italian letters, a letter-per-token design must be polyphonic: each token stands for a class of
letters. Bigram LM from it21news 2005-2010; control windows from the held-out 2011-26 fold, same letter count, random K-class
partition; anneal over the letter->class key (8 restarts x 5000 moves), forward log-likelihood, Viterbi decode.

| variant | K | letters | control solver accuracy (5 windows) | true-key oracle | solver loglik >= true key | verdict |
|---|---|---|---|---|---|---|
| V1 xs = space | 8 | 100 | 0.232 (0.10-0.35) | 0.736 | 5/5 | CONTROL BELOW GATE (0.60) |
| V2 xs = class | 9 | 114 | 0.139 (0.06-0.24) | 0.742 | 5/5 | CONTROL BELOW GATE (0.60) |

Target not decoded (control-first order). The solver found keys *more* likely than the true one in all ten controls, so the
miss is identifiability, not search: at 100-114 letters a bigram model cannot pick the true letter-class partition out of the
many that fit, and even the true key reads only about 74% of letters. This is a non-test of the letter-class design at this N
by this instrument ("untestable by bigram-likelihood anneal at N=100-114"), not a negative on the design. Case variants were
folded (a case-sensitive variant was not run). Nothing was read.

## Next step (R12D-ERBA3, 6 Oct 2026)

next: a different instrument for the letter-class design, not more restarts of this one: a word-level constraint (decode only
into Italian dictionary words between xs, using the 14-group segmentation test 2 supports, with the same held-out control),
~$2. More ciphertext would help more: the two sibling phrases printed by Tgcom24/il Giornale (18 June 2013) are in the same
system and could be added to N if their token reading is checked against a press image. Who acts: agent.
