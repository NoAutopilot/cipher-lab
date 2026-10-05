open
Schneier, "Handwritten Real-World Cryptogram" (schneier.com, 30 Jan 2006) and its full 409-comment thread (to 15 Apr 2012) read by GF4-BATCH18 on 3 Oct 2026, plus Bauer, Unsolved! (2019, Google Books l8iXDwAAQBAJ, snippet only): no decipherment; the dominant reading is a password list, never confirmed.

Intake (25 Sept 2026, LANE B3 worker bRAY, minimal check-solved per breadth.md's intake step):
Cipherbrain post "The Top 50 unsolved encrypted messages: 43. The Rayburn murder cryptogram"
(6 March 2017) and its full 7-comment thread read in full from
`sources/schmeh/posts/43-rayburn.txt` (already on disk); the post's own text states "So far,
nobody has come up with a plausible solution" and none of the 7 comments (Hendrik, Serapio,
Thomas, Nick Pelling, Aaron Turner, and two from Juha in 2019) claims a solution -- Juha's two
comments offer an unworked "overlined letters are notes" idea, not a reading. The post also
covers Bruce Schneier's original 2006 post (schneier.com/blog/archives/2006/01/handwritten_rea.html)
and its own long comment thread, which Schmeh says produced no plausible solution either. Both
solver repositories grepped (shallow clone, `grep -ril rayburn`, deleted after): dbourdeau's
`top50/NOTES.md` and `TARGETS.md` (row 43) both read "plausibly a handwritten password list, not
a cipher", citing "the recurring and plausible reading across both the Schneier and Cipherbrain
threads" -- no claimed decipherment of any standing; no match anywhere in
aaymeloglu/unsolved-ciphers. One OpenAlex query (`search=Rayburn cryptogram solved`) returned 1
result, unrelated (a survival-research essay-competition reflection paper). One Semantic Scholar
query (`query=Rayburn cryptogram decrypted`) returned 23 results, none naming Rayburn or this
cryptogram (cryptanalysis papers on unrelated ciphers). No solve found by any of the six checks.

Cheap test 1 (25 Sept 2026, LANE B3 worker bRAY): image fetched (1 request, scienceblogs.de,
browser UA, HTTP 200; free for the next holder) to `images/Rayburn-Cryptogram.jpg` and
transcribed blind, one pass, no subagent, recording each symbol's identity, position and its
underline/strikethrough/overline state separately -- see `ciphertext.txt` and `ciphertext.tsv`.
N = 74 tokens (58 in the main grid inside/below the drawn enclosure, 8 in a left-margin column,
8 in a right-margin column; a small circled mark at the bottom was excluded as a likely page
mark, not a cipher symbol -- see ciphertext.txt's caveat). K = 59 distinct type ids (case
preserved; symbols that look like two letters combined are kept as their own type). IC:

  target IC = 0.0056
  English control (same N=74, 200 samples, tools/data en corpus, 26-letter alphabet):
    mean 0.0618 [0.0311, 0.0911]
  uniform-random control (same N=74, K=59, 200 draws): mean 0.0171 [0.0115, 0.0255]
    (expected ~1/K = 0.0169)

Target IC is below both controls' ranges, and below the uniform-random floor -- consistent
with Schmeh's own observation ("most characters appear only once") and with either a
high-homophone substitution or non-linguistic content (Schmeh's diagram-of-objects
hypothesis; the source's own alternative reading is a password/directory list). This is not a
control-backed negative in the rule-3 sense (no substitution family was fit or judged here,
only a raw IC comparison as the spec's cheap test 1 asks for); it does rule out plain
monoalphabetic substitution on frequency grounds alone, matching Schmeh's "frequency analysis
is obviously useless" caveat. Test 2 (diagram-layout hypothesis) and test 3 (matched
homophonic/keyboard-substitution judge) are out of this brief's scope -- next test per the
spec's `cheap_tests_in_order`.

Transcription caveats: several symbols are genuinely ambiguous by eye at this resolution
(flagged with `?` in ciphertext.tsv/.txt); the mark state on most of the left- and
right-margin column is unclear because a continuous ruled line runs down each margin. K=59 is
this pass's best count, not a settled number -- a second blind pass would be the way to
tighten it (not run here, out of a $1-2 single-pass test's scope).


## Web and blog check (GF4-BATCH18 (account-4), 3 Oct 2026)

Plain web searches (WebSearch): (1) `Rayburn cipher 2004 Schmeh Top 50 solved` -- Cipherbrain Top 50 no. 43, two GitHub forks of Bourdeau's cyphersolver (arya1515, setsunaatto; not opened -- forks of a repo already grepped), a spiked review of Bauer's *Unsolved!*; all unsolved; (2) `David Rayburn Saugus 2004 cryptogram code Linda Rayburn Michael Berry decoded` (sender + victims + date) -- Schneier 2006 post, the Boston Globe obituary of Michael Berry (legacy.com, not opened: no cipher content expected); (3) `Rayburn cryptogram Bauer "Unsolved!" password list Saugus police cipher` -- Cipherbrain, Schneier, the spiked review ("Bauer's favoured solution is ... file directories and passwords rather than any message"); (4) `Rayburn murder cryptogram solved Claude OR GPT OR AI 2026` (model-solve family) -- only the Cyphral Distich and Enigma/ADFGVX announcements (other items); no AI-solve claim for this item.
Google Books API (`country=US`, keyed, 2 calls): `"Rayburn" Saugus cryptogram` -> Bauer, *Unsolved!* (l8iXDwAAQBAJ, 2019 pbk), snippet quoting the Schneier post's account (Rayburn, 44, Michael Berry, 23, Saugus); `"Rayburn" password cryptogram Bauer` -> 0. Bauer's chapter was not opened beyond the snippet; the review and Schmeh both report it as unsolved with a password-list preference.
**Schneier thread read:** "Handwritten Real-World Cryptogram", 30 Jan 2006, 409 comments on one page (curl, HTTP 200; 398 in 2006, the rest 2007 - 15 Apr 2012). Guesses only: boxed letters = letter counts of "Linda Rayburn and Michael Rayburn Berry"; keyboard-path sums (Jaime Kemp, 13 Mar 2009: both sideways strings sum to 27, as many as the body's capitals); phonetic "would you put a ..." (sarah, 15 Apr 2012); "Joey Mcoy" (2008); and the majority view, a password list / cheat sheet (no confirmation from the family or police). No commenter claims a decipherment and none is accepted. The poster who sent it to Schneier (a friend of the family) adds: the sheet was found in an open briefcase next to where he hanged himself; the suicide note on the kitchen table read "forgive me, it had to be this way"; a laptop was near the briefcase; "This is a copy of the original. I whited out the areas where friends were trying to decipher it ... The folds in the paper are also mine"; the police did not investigate further.
Blog site searches: Cipherbrain (Top 50 no. 43, 6 Mar 2017, live re-fetch: still 7 comments, same as bRAY's 25 Sept read -- no reading); klausschmeh.net `?s=Rayburn`: Nothing Found; Cryptiana `search?q=Rayburn`: no posts; Cipher Mysteries `?s=Rayburn`: Nothing Found; Apeiron (one publication only, Koehler): nothing. Reddit r/codes (OAuth search `Rayburn`): 0 results.
Solver repos (fresh shallow clones, 3 Oct 2026, deleted after): dbourdeau/cyphersolver HEAD 46f8056 (2 Oct 2026) -- research/top50/NOTES.md row 43 "low ... plausibly a handwritten password list, not a cipher", no targets/ folder; aaymeloglu/unsolved-ciphers HEAD d2800bb (27 Sept 2026) -- no "rayburn". DECODE: 0 hits for "rayburn" in the on-disk listings (sources/decode/*.tsv).
Requests: schneier.com 1, scienceblogs.de 1, klausschmeh.net 1, cryptiana.blogspot.com 1, ciphermysteries.com 1, googleapis.com 2, apeiron.re / oauth.reddit.com / github.com shared with this batch; all >= 1.5 s apart.

## Premise check (GF4-BATCH18 (account-4), 3 Oct 2026)

(a) Folder's own mentions of a decipherment or clear copy: none; NOTES.md, test1_result.txt and the spec record only the password-list hypothesis.
(b) Other solvers' working files: none beyond Bourdeau's list row and the Schneier thread's guesses; no DECODE record.
(c) Physical neighbours: FIND (source condition, not a reading). The image every source reproduces is, per the family friend who released it (Schneier thread), a *copy* of the original with white-out over friends' decipherment attempts and folds added by the copier. Our transcription (bRAY, test 1) is therefore conditional on a copy that has had marks removed (rule 2); the circled mark bRAY excluded may be one of the copier's survivals. The original sheet, the suicide note and the laptop were with the family/police in 2004-06.
(d) Recipient / investigator side: Saugus police treated the case as closed (murder-suicide); no police reading or forensic examination of the laptop is reported anywhere read.
Result: no decipherment located; status stays open.

## Verdict (GF4-BATCH18 (account-4), 3 Oct 2026)

**open (unchanged).** No published or accepted decipherment located in the Schneier 2006 post and its full 409-comment thread, Bauer's *Unsolved!* (Google Books snippet), Cipherbrain no. 43 and its 7-comment thread, klausschmeh.net, Cryptiana, Cipher Mysteries, Apeiron, r/codes, DECODE listings, or either solver repository, searched 3 Oct 2026. Claimed-but-unaccepted: Bauer's and the Schneier majority's password-list interpretation (a classification, not a reading); comment guesses 2006-2012 (letter-count names, keyboard sums, phonetic, "Joey Mcoy") -- recorded as claimed, none accepted.

## While waiting (GF4-BATCH18, 3 Oct 2026)

Nothing here waits on a person. The zero-dependency step: compare the earliest captured image of the Schneier post (Wayback CDX for schneier.com/blog/archives/2006/01/handwritten_rea.html, Jan-Feb 2006) with images/Rayburn-Cryptogram.jpg for any difference in whited-out areas, and annotate ciphertext.tsv with which tokens border a white-out (copy condition), before any test 2.

## Intake gate (GF4-BATCH18, 3 Oct 2026)

$ python3 tools/intake_gate_check.py rayburn-2004
rayburn-2004: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit 0

$ python3 tools/next_steps.py --wait-only | grep rayburn-2004
(no line)

## Next step (NO-CRACKS, 5 Oct 2026)

next: compare the earliest Wayback capture of the Schneier post (Jan-Feb 2006) with images/Rayburn-Cryptogram.jpg for differences in the whited-out areas and mark the tokens that border a white-out in ciphertext.tsv, before test 2, ~$0.5. Who acts: agent. Source: this file's "## While waiting (GF4-BATCH18)"; written by NO-CRACKS (account 3) because tools/next_steps.py found no next-step line in this file.

## Copy condition: earliest image vs ours, white-out map (D2B-RAY, account 2, 5 Oct 2026)

Wayback route blocked this session: `web.archive.org/cdx` reset the connection twice (one retry after a 5 s pause) and
`archive.org/wayback/available` answered HTTP 429; host stopped per the good-citizen rule, no capture fetched.
Fallback that answers the same question: the live post (schneier.com, 1 request, HTTP 200) embeds
`wp-content/uploads/2006/01/cryptogram1-450px.jpg` and links `.../2006/01/cryptogram1-850px.jpg` -- the files uploaded
with the 30 Jan 2006 post (upload path 2006/01; server Last-Modified 24 Jan 2020, a site migration). The 850px file
(1 request, 240,374 bytes) is **byte-identical** to images/Rayburn-Cryptogram.jpg (SHA-1 93e1f92a...a923436 both): our
scienceblogs.de copy (2013 path) is Schneier's own 2006 file, unchanged, so no white-out area differs between the
2006 publication and our image. Not checked: whether Schneier's 2006 file differs from the family friend's emailed
original (not public); a 2006 Wayback capture of the post (blocked today); the derivative enhanced image a commenter
linked (bitculture.org `cryptogram1-850px_dhc.jpg`, not fetched -- a processed copy, not a source).
Source fact from the post body, not previously in this folder: "The rectangle drawn over the top two lines was not done
by the murderer. It was done by a family member afterwards." So the enclosure around main rows 1-2 is a later addition,
like the white-out and the folds (Premise check (c)); it carries no information about the writer.

White-out map (`python3 whiteout_map.py`, threshold 253 against a paper median of 247, then one look at the contrast
stretch): seven flat, sharp-edged pure-white patches, all in the outer margins, outboard of the two margin columns --
four on the left (beside left-margin rows 2, 4, 6, 8: `pct(%)`, `4/h7?`, `d-loop?`, `K*`) and three on the right (beside
right-margin rows 2, 3, 6: `amp(&)`, `hash(#)`, `H-hash?`). Other components the script lists are the paper's bottom
edge (y > 730), the horizontal fold crease (y ~ 330-360) and one soft lighter area at x 703-738 (paper texture, no sharp
edge); none sits beside a main-grid token. Per-token flags in `copy_condition.tsv` (sidecar, because
specs/cheap-tests/rayburn-2004/transcribe.py rewrites ciphertext.tsv): 7 of 74 tokens border a white-out, all margin
tokens; 0 of 58 main-grid tokens. Reading: what the friends wrote (per the friend's own comment) was in the side margins
next to the margin symbols, alternating rows on the left, so the margin columns may have carried more marks (or glosses)
than the 16 transcribed; the main grid is untouched by white-out. Also seen, not in the transcription: a small vertical
handwritten word beside right-margin row 2 (`amp(&)`), looks like "Approved"/"Appeared" -- either the writer's or a
friend's; a second blind pass should decide whether it is a cipher token.
Requests: web.archive.org 2 (both reset), archive.org 1 (429), www.schneier.com 2 (page, 850px image), all >= 2 s apart.

## Remaining gaps (D2B-RAY, 5 Oct 2026)
Read so far: nothing read; 74 tokens transcribed in one blind pass (bRAY); copy condition mapped (7 margin tokens border white-out, 0 main-grid tokens).
- 2006 Wayback capture of the post and image - blocker: not-attempted; web.archive.org reset / archive.org 429 on 5 Oct 2026, low value now that the 2006 upload matches our file byte for byte; next: one retry from a later session, ~$0.2
- Second blind transcription pass (K=59 unsettled; vertical word beside right-margin row 2 not classed) - blocker: not-attempted; K and the margin word need an independent eye; next: one crop-scoped blind pass + reconciliation, ~$1.5
- Tests 2 and 3 of specs/rayburn-2004.json (diagram layout; matched homophonic/keyboard judge with control) - blocker: not-attempted; waits on the second pass settling K; next: test 2, ~$1

## Escalation (D2B-RAY, 5 Oct 2026)
- [x] siblings: none; a single sheet, original with the family/police (Premise check)
- [x] clear-pages: none; the suicide note's text is quoted in the Schneier thread and gives no crib
- [x] known-keys: none exists; no decipherment located (Verdict, 3 Oct 2026)
- [x] print: Schneier thread, Bauer snippet, Cipherbrain, blogs, solver repos (GF4-BATCH18)
- [ ] key-rebuild: not applicable until tests 2-3 say whether there is a substitution to rebuild
- [ ] image-check: done 5 Oct 2026 (copy condition, this file); not done: second blind pass
- [ ] retry: Wayback capture, once, later session
Verdict: keep going: 3 internal gaps; cheapest next: Wayback retry ~$0.2, then second blind transcription pass ~$1.5, then test 2 ~$1
