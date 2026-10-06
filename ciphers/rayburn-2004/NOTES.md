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

## Second blind pass, reconciliation and test 2 (R8-RAY2, account 2, 6 Oct 2026)

Crops (mandatory step, pasted): `python3 tools/iiif_lines.py --image ciphers/rayburn-2004/images/Rayburn-Cryptogram.jpg
--out <scratch>/crops --prefix main --region 125,30,632,740 --centres 38,98,170,228,300,382,452,522,585,655 --debug`
(autodetection split sloped rows, so centres were given by eye and checked on the debug overlay), plus three PIL crops
(left margin x 40-130, right margin x 680-850, bottom circle). One blind Sonnet pass on those 13 crops only
(`pass2/passB_raw.tsv`); `tools/reconcile_passes.py pass2/passA.tsv pass2/passB.tsv` (pass A = ciphertext.tsv as is):
agreement 40/85 aligned columns = 47.1% (7 agreed-H, 33 agreed-uncertain, 45 disagreements; per line 0.29-0.75 in the
grid, 0.11-0.13 in the margins). `pass2/disagreements.tsv`, `agreement.tsv`, `ciphertext_draft.tsv` hold the detail.
All 7 white-out-adjacent margin tokens (copy_condition.tsv) are among the flagged columns: pct/% and hash/#H agree in
substance, the other five (`4/h7`, `d-loop`/@, `K*`/asterisk, `amp(&)`/8,
`H-hash`/#H) differ in identity.
Reconciliation by the worker from the image (`pass2/reconciled.tsv`, every token grade M, source column says which
passes back it):
- Pass A misses six main-grid tokens: row 5 `n` (2nd), row 8 `f` (4th), row 9 `C`, `X`, `a`, `Z` (row 9 has 7 tokens,
  not 3). Pass B misses row 10 `r`. ciphertext.txt is left as transcribed (rule 2); the reconciled grid is
  W j u P D / a X o R w i s / M m g / H k e E B f e / X n L o Y u I / w A z Q Y / b U k+r t P s q / A+m c Z f i Y z D /
  C R+H V h X a Z / E f b d a+v a r O. Composites (a small sign under a letter): k+r, A+m, R+H, a+v.
- Reconciled N = 80 (64 grid + 8 left + 8 right), matching Schmeh's "about 80 characters"; K = 58 case-sensitive.
- Margins: every margin symbol has a short vertical stroke on its left, where grid symbols have a horizontal line --
  consistent with the margin columns having been written with the sheet turned 90 degrees, the vertical stroke playing
  the underline. Read that way, the two `K`-looking signs (left 3, right 5) are a `<` beside its line, i.e. a turned `V`
  (pass B read right 5 as V). Not settled: identities of the margin signs under rotation.
- The vertical word beside right-margin 2: pass B read "Append", pass A's note "Approved/Appeared"; both treat it as a
  note, not a cipher token. Excluded from N.
- The circled mark below the grid: `d` or `8` (pass B), `d`/`cl` (pass A); excluded from N as before.

Test 2 (spec: diagram hypothesis), pre-registered in `pass2/PREREG-test2.md` (pushed 7139aa956 before the run), script
`pass2/test2_case_mark.py`, output `pass2/test2_result.txt`. Schmeh's mechanism (each object underlined or crossed out
after an action) predicts the mark is independent of the label's form. On the blind pass-B marks and case as written:
| set | N letters | A (capital-U or lower-S) | permutation control mean | control p95 | p |
|---|---|---|---|---|---|
| primary, all grid letters | 60 (31 upper, 29 lower) | 0.867 | 0.499 | 0.600 | <0.0001 |
| secondary, case not size-only | 35 | 0.914 | 0.499 | 0.629 | <0.0001 |
Gate (A >= 0.85 and p < 0.01): case-mark coupling supported. The 8 exceptions are mostly letters whose case is judged by
size (j U, o U, S S, Y S twice, Z S) plus f U and an edge-fragment D. Reading: the underline/strike is largely a case
marker (capitals underlined, lower case struck), so it adds little per-object information; this takes away the main
support for the "crossed out after an action" form of the diagram hypothesis. It does not exclude a list or diagram of
another kind (Bourdeau's password-list reading), and it does not show running text. Layout, descriptive only: ten
left-aligned rows of 3-8 signs with ragged right ends, plus two margin columns -- the shape of written lines or a list,
not of a grid tableau. Spec test 3 (homophonic/keyboard judge with matched control) is the next test; the case marking
means the effective alphabet may be case-folded (K about 40 when folded), which test 3's control should match.
Requests: none (all local). Grades: 0 H, 0 C, 0 S read tokens; nothing read.

### Remaining gaps (R8-RAY2, 6 Oct 2026; superseded by R9-RAYSORT below)
Read so far: nothing read; 80 tokens reconciled from two blind passes (grade M); test 2 run (mark = case marker, p<0.0001 vs permutation control).
- 2006 Wayback capture of the post and image - blocker: not-attempted; low value since the 2006 upload is byte-identical to our file; next: one retry from a later session, ~$0.2
- Margin sign identities under the rotated-writing reading (8+8 signs) - blocker: not-attempted; needs an eye pass on the margin crops turned 90 degrees; next: one Sonnet pass on rotated margin crops + reconciliation, ~$1.5
- Test 3 of specs/rayburn-2004.json (homophonic/keyboard judge, matched control at N=80, case-folded and case-sensitive K) - blocker: not-attempted; test 2 only ran this session; next: test 3 with family_run.py homophonic, ~$2.5

### Escalation (R8-RAY2, 6 Oct 2026; superseded by R9-RAYSORT below)
- [x] siblings: none; a single sheet, original with the family/police (Premise check)
- [x] clear-pages: none; the suicide note's text is quoted in the Schneier thread and gives no crib
- [x] known-keys: none exists; no decipherment located (Verdict, 3 Oct 2026)
- [x] print: Schneier thread, Bauer snippet, Cipherbrain, blogs, solver repos (GF4-BATCH18)
- [ ] key-rebuild: not applicable until test 3 says whether there is a substitution to rebuild
- [x] image-check: copy condition mapped 5 Oct 2026; second blind pass and reconciliation done 6 Oct 2026
- [ ] retry: Wayback capture, once, later session
Verdict: keep going: 3 internal gaps; cheapest next: test 3 (homophonic judge at N=80 with matched control) ~$2.5, then rotated margin pass ~$1.5

## Owner sign sorter built (R9-RAYSORT, account 2, 6 Oct 2026)
`sorter/` (README.md there): 80 tiles = the 80 reconciled tokens, cut by `sorter/build_inputs.py` from the image on disk
(connected components on row base lines, no vision model, no network), 58 case-sensitive starting piles, 40 focus tiles
(every position where blind passes A and B differ). `python3 tools/sorter_preflight.py` PASS (template, answerable,
right line 0/80 bad, contact sheet); 24 contact-sheet tiles and 8 further random tiles opened against the line image, all
on their sign. Handed to the account-3 orchestrator to publish (ROOM flag); not published here, no ASKS row written.
Requests: none. Grades unchanged: 0 H, 0 C, 0 S; nothing read.

## Remaining gaps (R9-RAYSORT, 6 Oct 2026)
Read so far: nothing read; 80 tokens reconciled from two blind passes (grade M); test 2 run (mark = case marker, p<0.0001 vs permutation control); owner sign sorter built and preflighted.
- Sign alphabet and margin identities settled by a person (80 tiles, 40 focus) - blocker: waiting-on the owner's reply in the Rayburn sign sorter; two blind passes split 52.9% (pass2/), over the 10% line, so Usage 6 sends it to a person (sorter/README.md; the account-3 orchestrator publishes it)
- Test 3 of specs/rayburn-2004.json (homophonic/keyboard judge, matched control at N=80, K from the settled alphabet) - blocker: waiting-on the owner's reply in the Rayburn sign sorter; the matched control's K (case-folded or not, 16 margin signs) comes from the settled alphabet (sorter/README.md)
- 2006 Wayback capture of the post and image - blocker: not-attempted; low value since the 2006 upload is byte-identical to our file; next: one retry from a later session, ~$0.2

## Escalation (R9-RAYSORT, 6 Oct 2026)
- [x] siblings: none; a single sheet, original with the family/police (Premise check)
- [x] clear-pages: none; the suicide note's text is quoted in the Schneier thread and gives no crib
- [x] known-keys: none exists; no decipherment located (Verdict, 3 Oct 2026)
- [x] print: Schneier thread, Bauer snippet, Cipherbrain, blogs, solver repos (GF4-BATCH18)
- [ ] key-rebuild: not applicable until test 3 says whether there is a substitution to rebuild
- [x] image-check: copy condition mapped 5 Oct 2026; second blind pass and reconciliation 6 Oct 2026; sorter built 6 Oct 2026 (the rotated-margin eye pass is folded into the sorter's margin focus questions)
- [ ] retry: Wayback capture, once, later session
Verdict: keep going: 1 internal gaps; cheapest next: Wayback retry, ~$0.2 (test 3 waits on the owner's sorter pass)
