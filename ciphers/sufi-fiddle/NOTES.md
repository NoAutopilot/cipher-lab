open
Bulliet, "The Diviner's Handbook" (Mizan Project, mizanproject.org/the-diviners-handbook/, 31 Dec 2021) read in full by GF4-BATCH18 on 3 Oct 2026: the author's own latest account; the violin inscription is still untranslated (only the name Muhammad in line 5 read), Maranao ruled out by M. Kawashima, Tausug/Sulu proposed, a query to R. D. Trimillos pending.

Intake (25 Sept 2026, LANE B4 worker bSUF, minimal check-solved per breadth.md's intake step):
Cipherbrain post "The Top 50 unsolved encrypted messages: 38. The Sufi Fiddle mystery" (Klaus
Schmeh, 3 April 2017) and its full 6-comment thread read in full from
`sources/schmeh/posts/38-sufi-fiddle.txt` (already on disk, fetched 25 Sept 2026). The post's
own account (relaying Louis Kruh's review in Cryptologia 3/1991, pp. not given by Schmeh) states
the inscription "is never solved" in the novel, and Schmeh's own 2014 investigation and direct
email exchange with the author, Richard Bulliet, produced no reading -- only Bulliet's own
unpublished hypothesis (Philippine/Maranao origin). None of the 6 comments (#1 James Simpson via
Facebook: "It's in Arabic or Farsi... that's about all I can see"; #2 tomtoo, off-topic; #3
Bernhard Gruber asking for news; #4 Schmeh replying with the Philippines hypothesis, no reading;
#5 MF, 24 Jan 2019: "Not Farsi, but could be Kurdish"; #6 J Muso, 18 Feb 2023: spoke to an Iraqi,
Iranian, Afghan and Kurdish reader, none could read it) claims a decipherment or even a firm
script identification.

Both solver repositories shallow-cloned (25 Sept 2026), grepped case-insensitively for
"sufi"/"fiddle", then deleted per CLAUDE.md item 3 (digests, not repositories): both repos'
`top50/top50.*` files (dbourdeau/cyphersolver) carry only the same unsolved-list entry ("38. The
Sufi Fiddle mystery -- An inscription found on the inside of an old fiddle has never been
deciphered", linking the same Cipherbrain post); aaymeloglu/unsolved-ciphers had no relevant hit
at all. No decryption or transcription of this item in either repository.

One OpenAlex query (`works?search=sufi fiddle violin inscription decrypted`, key via
Authorization header) returned 0 results. One Semantic Scholar query (same terms, `x-api-key`
header) returned `total: 0`. Full-text search of the open indexes found nothing pre- or
post-1990 corroborating or solving the inscription, consistent with Schmeh's own pre-2017
search finding no independent reference outside Bulliet's novel.

Verdict: open. No transcription of the inscription's script exists anywhere (not in Schmeh's
post, not in Kruh's review as relayed, not published by Bulliet beyond the two low-resolution
images embedded in the post) -- this is fundamentally an authenticity/provenance question before
it is a cryptanalytic one (spec's own framing, specs/sufi-fiddle.json). intake_gate_check.py
output pasted below.

## Intake gate check

```
$ python3 tools/intake_gate_check.py sufi-fiddle
sufi-fiddle: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit 0
```

## Cheap test 1: script identification (25 Sept 2026, worker bSUF)

Fetched `Suffi-Fiddle-614.png` (scienceblogs.de, 2 requests total including the cover image;
browser UA, 2 s apart; host now free for the next holder). The image is a hand copy of the
seven lines captioned "copied by V. Castle Winter" (name partly illegible), overlaid on a page
of English prose visible faintly behind the ink -- consistent with a scan of a page from
Bulliet's own novel (or working notes), **not** a photograph of the violin panel itself. Rule 2
therefore applies twice over here: this pass reads the image, but the image is already a
secondary hand-copy of an inscription whose primary source (the violin) has never been
photographed or published, per the spec. Any script judgement below is conditional on the copy
being a faithful visual rendering of the original -- unverifiable and, per the spec's own
`authenticity_caveat`, not corroborated by any named third party.

One blind single-pass sign transcription of the copy: **N=165** visible signs, **K=21** distinct
visual shape-types (own sign ids and labels in `ciphertext.txt`; two spans illegible under a
crosshatched "glue" repair mark on the original copy, line 3 mid-line and line 4 line-end, are
excluded from N; two further signs the copyist herself flagged "hard to read?" are recorded but
excluded). K is likely a slight undercount: several dotted-letter clusters (b/t/th; j/h/kh) were
pooled as one label each where the dot pattern was not resolvable at this image's resolution --
noted, not corrected, since resolving it needs a better source image this pass does not have.

### Script checklist: target vs. two reference lines

Reference lines are stated from memory (training-data knowledge of the two script families), not
fetched this pass -- the $1 cap for test 1 was spent on the fetch and the sign pass; no
Wikimedia request was made.

| Checklist item | Target (Suffi-Fiddle-614.png) | Reference: ordinary Arabic-script line (naskh hand) | Reference: Baybayin line (pre-colonial Philippine abugida, e.g. Doctrina Christiana 1593 style) |
|---|---|---|---|
| Sign inventory size | ~21 distinct shapes observed in 165 signs (likely undercounted toward the high 20s/low 30s once positional/dot variants are resolved) | ~28 base letters (abjad), each with up to 4 positional forms | ~17 base characters (3 independent vowels + 14 consonant symbols with inherent /a/) |
| Repeats | High -- top shapes (kaf 23x, lam 19x, waw 15x) recur many times across only 7 lines | High -- any line of ordinary length reuses the ~28 letters repeatedly | High -- reuses the small ~17-symbol set repeatedly |
| Direction | Right-to-left within each line (denser word-initial forms at the line's right edge, trailing connective strokes to the left); Latin numerals 1-7 added in the left margin by the (apparently English-speaking) copyist, not part of the script | Right-to-left | Traditionally top-to-bottom in columns read left-to-right, or (later/printed, e.g. Doctrina Christiana) left-to-right horizontal lines -- not right-to-left |
| Ligature/joining | Strong: letters within each word-group are connected by a continuous cursive baseline stroke, word-groups separated by small gaps -- the same visual joining behaviour as Arabic naskh/ruq'ah cursive | Strong: most letters join to both neighbours; a handful of non-joining letters (alif, dal, ra, waw, zay, ...) still join to the preceding letter | None: each character is a discrete, unconnected glyph; no cursive joining between adjacent syllable-signs |
| Diacritic-like marks | Dots above and below several letters, in clusters of 1-3 dots, on lines 2, 3, 4 and 6 -- visually matches Arabic i'jam (dot-clusters distinguishing e.g. b/t/th or j/h/kh) rather than a single mark per glyph | Dots (i'jam) integral to about half the letters' identity, 1-3 dots above or below; vowel marks (harakat) optional and usually absent in ordinary prose | Kudlit: a single dot (or small stroke) placed above or below a character to change its inherent vowel -- one mark per glyph, not the multi-position dot-clusters seen here |

**Verdict (script ID only, not a reading):** the target is consistent with the Arabic-script
family (an abjad written in a cursive, naskh-like hand -- Arabic, Persian, Urdu, Ottoman Turkish,
or a Jawi-style script such as Maranao, all of which share this checklist profile) on every
checklist axis: small alphabetic inventory with high repeats, right-to-left direction, strong
cursive joining, and multi-position dot-diacritics. It is **not** consistent with Baybayin
specifically: Baybayin has no cursive joining at all and is not written right-to-left, both of
which the target clearly shows (joining, RTL). This does not contradict Bulliet's own
"Philippine" hypothesis as relayed in the post -- comment #6 (J Muso) and the post's own
paragraph about "a linguist" both point to **Maranao**, a Muslim Mindanao language historically
written in a Jawi-style Arabic-derived abjad, not in Baybayin (which is used for Tagalog and
other non-Muslim Philippine languages, not for Mindanao's Muslim languages). So the visual
evidence here is consistent with the Maranao/Jawi strand of the hypothesis already in the post,
while ruling out the generic "Baybayin" framing the spec's `language_candidates` field uses as
shorthand for it. Test 3 (Baybayin character-set comparison) is accordingly **not run**: its own
trigger condition in the spec ("if test 1 supports the Philippine/Baybayin-family hypothesis
specifically") is not met -- the checklist points away from Baybayin, not toward it.

No cryptanalytic claim is made. No pseudo-script judgement is made either: the letterforms
resemble real, distinguishable Arabic-family letters closely enough (not a small set of
repeated abstract squiggles) that a pseudo-script verdict is not supported by this pass, but
whether the text is meaningful Maranao/Arabic/Persian/Urdu, a different Jawi-family language, or
meaningless letter-strings arranged to look like one is outside this test's scope.

Status stays `open`. Next test in the spec's order (test 2, an independent pre-1990 provenance
search) and test 3 (not triggered, see above) are not run this pass, per the brief.

## Cheap test 3: read the hand copy as Arabic script (25 Sept 2026, worker bSUF3)

Note: this is a different test 3 from the spec's original `cheap_tests_in_order` item 3 (a
Baybayin character-set comparison, not triggered since test 1 ruled out Baybayin specifically).
Parent 7d approved this replacement test 3 in ROOM.md at 23:10 UTC 25 Sept 2026: attempt an actual
transliteration and reading of the hand copy as Arabic-family script, now that test 1 established
the script family.

Full transliteration table (letter-by-letter, sure/probable/guess), the (weak, stated-why) control
discussion, and the segmentation attempt across Arabic/Persian/Ottoman Turkish/Malay-Jawi/Maranao
are in `ciphers/sufi-fiddle/reading-attempt.md`. Summary: no coherent line reading in any of the
five languages tried; no primary Sufi formula (Allah, Hu, ya, bismillah, la ilaha illa llah, named
tariqa order) matches any word-group. Three isolated M-graded word-level guesses only: L1 g4
standalone waw ("and", weak); L6 g4 "برکت", one letter from "بركة/بركت" (baraka(t), "blessing" --
a loanword common to Arabic/Persian/Ottoman/Malay/Maranao, the best candidate of the pass but
resting on three guess-or-probable letters); L6 g7/g9 "عل", possibly "على" ("on/upon") with a
dropped final alif, weaker still. No ar/fa/ota/ms/mrw judge corpus exists in `tools/data`, so
`tools/judge_plaintext.py` was not run -- reported as "no judge" per the brief, not omitted.
Every letter graded I (inferred from visual resemblance in a hand copy); counts: sure ~39,
probable ~60, guess ~60, excluded (obscured/uncertain, unchanged from bSUF's own marks) 4
spans/signs. Not a solve; not closed-negative either (no matched synthetic control exists to
license that verdict -- rule 3's own headline paragraph: a negative means nothing without one).
Status stays `open`.

## Web and blog check (GF4-BATCH18 (account-4), 3 Oct 2026)

Plain web searches (WebSearch): (1) `Sufi Fiddle inscription Bulliet violin solved` -- Cipherbrain Top 50 no. 38, Amazon listing of the 1991 novel, Mizan Project "The Diviner's Handbook"; all say unread, none gives a reading; (2) `"Sufi Fiddle" Bulliet inscription decipherment Arabic Maranao` -- the same plus Goodreads, a Columbia Seminar on Religion and Writing abstracts page (blogs.cuit.columbia.edu, WebFetch HTTP 403, not retried) and Mindanao manuscript papers on academia.edu (unrelated to the violin, not opened: academia.edu is 403 from the cloud); (3) `Sufi Fiddle cipher Claude solves OR GPT solves 2026` (model-solve family) -- only the Vals AI / Fable Cyphral Distich announcements (another item) and the "No, ChatGPT didn't solve Kryptos 4" gist; no AI-solve claim for this item; (4) `violin Boston 1968 Harvard Arabic script talisman inscription "Sufi Fiddle" hoax` (descriptive title) -- Mizan Project essay again; (5) `Bulliet violin inscription Tausug biyula Trimillos translation` -- Mizan essay again and Tausug music pages; no published reply from Trimillos and no translation.
**Hit read in full:** Richard W. Bulliet, "The Diviner's Handbook", Mizan Project, 31 Dec 2021 (curl, HTTP 200). The author's own account, later than everything the folder had: the seven lines were copied in 1968 by Labib Zuwiyya-Yamak (Widener Library, Middle East division) from the back plate; Schimmel and Frye saw it; "no one ... could read a single word, except for the name Muhammad in line 5"; Bulliet's own careful copy is printed as Figure 1 (a second, independent copy beside the folder's "V. Castle Winter" hand copy); a 1983 letter relays three Philippine embassy staff who "read the inscription but none of them could really translate it", calling it an anting-anting charm, "Tausug, Maguindanaw or Maranaw"; a bundle of texts bought ca. 2001 from a Boston curio shop (the "Blue Booklet", identified as Maranao) is written in a similar hand; Prof. Midori Kawashima (Sophia University) assured him the violin inscription "is not" Maranao and suggested the Sulu archipelago (Tausug *biyula*); he was awaiting a reply from R. D. Trimillos (Tausug music, UCLA PhD 1972). No translation of the inscription is given anywhere in the essay. Status of this account: the author's own report of an unread text -- not a decipherment, not claimed as one.
Blog site searches: Cipherbrain (scienceblogs.de, Top 50 no. 38, 3 Apr 2017, live re-fetch: still 6 comments, same as bSUF's 25 Sept read -- Simpson, tomtoo, Gruber, Schmeh, MF, J Muso; no reading); klausschmeh.net `?s=Sufi+Fiddle`: Nothing Found; Cryptiana blog `search?q=Sufi+Fiddle`: no posts; Cipher Mysteries `?s=Sufi+Fiddle`: Nothing Found; Apeiron (apeiron.re: no working site search; its Next.js build manifest lists one publication only, `/publication/apeiron-koehler-cryptograms`) -- nothing on this item. Reddit r/codes (OAuth search `sufi fiddle`): 0 results.
Solver repos (fresh shallow clones, 3 Oct 2026, deleted after): dbourdeau/cyphersolver HEAD 46f8056 (2 Oct 2026) -- research/top50/NOTES.md row 38 "low ... no transcription has ever been published ... A palaeography problem before it is a cipher problem", no targets/ folder; aaymeloglu/unsolved-ciphers HEAD d2800bb (27 Sept 2026) -- no "sufi"/"fiddle" anywhere. DECODE: 0 hits for "sufi"/"fiddle" in the on-disk listings (sources/decode/*.tsv).
Requests: mizanproject.org 1 + 1 WebFetch, scienceblogs.de 1, klausschmeh.net 1, cryptiana.blogspot.com 1, ciphermysteries.com 1, apeiron.re 3 (search, home, build manifest; shared across this batch's three targets), oauth.reddit.com 1 (+1 token, shared), blogs.cuit.columbia.edu 1 WebFetch (403), github.com 2 clones (shared); all >= 1.5 s apart.

## Premise check (GF4-BATCH18 (account-4), 3 Oct 2026)

(a) Folder's own mentions of a decipherment or clear copy: none. bSUF3's reading-attempt.md is our own I-graded transliteration (no formula found; best M guess "baraka(t)" in L6). Cross-check from the Mizan essay: Harvard readers and Bulliet read "Muhammad" in line 5; reading-attempt.md lists no محمد and its L5 group 4 is مهيد (m-h-y-d), one letter from محمد -- a lead for the next reader, not a reading.
(b) Other solvers' working files: none -- Bourdeau a list row only, Aymeloglu nothing, no DECODE record; Bulliet's own decades of queries (Schimmel, Frye, embassy staff, Leiden, Kawashima) produced no translation.
(c) Physical neighbours: FIND (provenance, not a reading). Bulliet's Figure 1 is a second hand copy of the same seven lines, independent of the folder's image [corrected by FT4-sufi-fiddle, 3 Oct 2026: NOT independent -- Figure 1 is a photograph of the same sheet; see the FT4 section below]; and the "Blue Booklet" text bundle (Maranao, a similar hand, Bulliet's own possession) is the closest sibling material. Neither carries a translation of the violin lines.
(d) Recipient / owner side: the violin's owner was never identified (the instrument first went to Widener's Hebrew Division); Bulliet's query to Trimillos was open at Dec 2021, no published answer located.
Result: no decipherment located; the language hypothesis has moved from Bulliet's 2014 "Maranao" (as relayed by Schmeh) to Tausug (Kawashima, 2021). Status stays open.

## Verdict (GF4-BATCH18 (account-4), 3 Oct 2026)

**open (unchanged).** No published or accepted reading of the violin inscription in Bulliet's own 2021 essay (read in full), Cipherbrain no. 38 and its 6-comment thread, klausschmeh.net, Cryptiana, Cipher Mysteries, Apeiron, r/codes, DECODE listings, or either solver repository, searched 3 Oct 2026. Claimed-but-unaccepted: none (only script/language guesses: Arabic or Farsi, Kurdish, Maranao, Tausug).

## FT4-sufi-fiddle (3 Oct 2026, account-4): Bulliet Figure 1 diffed against the folder copy

Step (GF4-BATCH18's While waiting): diff Bulliet's Mizan 2021 Figure 1 ("My copy of the violin inscription") sign by sign against `images/Suffi-Fiddle-614.png`.
Fetch: mizanproject.org/wp-content/uploads/2021/12/Diviners-Handbook.docx-10.jpg, 2500x1301, sha1 2825b442...; the essay page states no licence, so the image is **not committed** (URL, sha1 and finding in `images/manifest.json` under `external_not_committed`).
Crops (pasted commands, scratchpad output, not committed):
```
python3 tools/iiif_lines.py --image <scratch>/fig1.jpg --out <scratch>/fig1crops --prefix fig1 --centres 105,290,440,620,830,1000,1200 --max-width 2499 --overlap 0 --debug
python3 tools/iiif_lines.py --image ciphers/sufi-fiddle/images/Suffi-Fiddle-614.png --out <scratch>/wincrops --prefix win --centres 36,78,112,158,202,245,288 --debug
```
(the tool's own autocorrelation found 5 and 6 lines; centres were set from the row-ink profile, 7 lines each.) Each Fig.1 line strip was paired above the same folder line at equal width; 2 vision reads (lines 1-4; lines 5-7 plus the top and bottom margins).

**Result: Figure 1 is not an independent copy. It is a photograph of the same sheet** as the folder's image: every non-text mark recurs in place on both -- the "glue" arrow and crosshatch over line 3 mid-line and line 4's end, the "hard to read?" notes over line 3 and under line 2, the square bracket "[r]" with "?->" and "hard to read ->" on line 5, the bracketed final group with "?->" on line 6. Figure 1 is cropped above the "copied by ... Winter" caption, which the folder copy carries under line 7; the folder copy is the same sheet printed over prose (Bulliet calls it "my copy", 1968 or after).
Sign-level comparison: 7/7 lines, 166 folder sign tokens (script count of ciphertext.txt, excl. OBSCURED/UNCERTAIN; bSUF's figure 165), **0 differing = 0.0 pct disagreement**, but this measures two images of one copy, not two copyists: it says nothing about copyist error against the violin. Per-line table: `fig1-diff/diff.tsv`. Numeric support (`fig1-diff/profile_corr.py`, column ink-profile correlation at best scale+shift): same line r mean 0.493 (min 0.307) vs mismatched-line control (42 pairs) mean 0.235 (max 0.546) -- separates on the mean, not on every pair (the folder image is 614 px, so the profile is coarse); the shared annotations are the decisive evidence.
Disputed signs: none between the two images. One dispute against OUR transcription: L5 group 4, transcribed "mim ha ya dal" by bSUF, shows a mim loop in third position on Figure 1 (m-h-m-d, the name Muhammad Bulliet and the 1968 readers read in line 5). Recorded as a comment in `ciphertext.txt`; the row is not changed. Grade I.
10 pct rule (Usage 6): disagreement 0.0 pct, under 10 pct -- but moot, since no second copy exists to disagree. What Figure 1 does give is the same copy at about 4x the resolution (2500 px vs 614 px), which is the better image for any re-transcription (resolving bSUF's pooled dot clusters b/t/th, j/h/kh, and the L5 g4 dispute).
No decipherment attempted. Requests: mizanproject.org 2 (Figure 1, essay page for the licence), 2 s apart. Vision calls: 2 of 3.

## GAPS87-sufi-fiddle (3 Oct 2026, account-4): Figure 1 re-transcribed from line crops

Step (FT4 Verdict): re-transcribe from Bulliet's Mizan 2021 Figure 1 (2500x1301, sha1 2825b442..., refetched once from mizanproject.org, still not committed: manifest only) per TRANSCRIPTION.md's LLM line-read fallback (an inscription in a known script, no key family, no atlas).
Crops (scratch only, pasted command; the profile found 5 of 7 lines, so centres were set from the --debug overlay; region trimmed to 2490 px so each line is one crop under the 2500 px limit):
```
python3 tools/iiif_lines.py --image <scratch>/fig1.jpg --out <scratch>/crops --prefix fig1 --region 0,0,2490,1301 --max-width 2490 --centres 148,289,445,613,820,1000,1195 --debug
```
Passes: two blind Opus calls over the 7 crops only (`fig1-tx/prompt_pass.txt`, grep-checked for unfilled placeholders: one unfilled output path caught and fixed before launch), dots resolved per sign, group gaps as `|`. `tools/reconcile_passes.py fig1-tx/passA.tsv fig1-tx/passB.tsv`: A 176 signs, B 181; 205/242 columns agree incl. gaps; **err_2reader 34/184 sign columns = 18.5 pct** (over a tenth). So, per the brief, no third full pass: one look-alike re-read of the 34 split signs only (`prompt_lookalike.txt`, candidates A/B shown, `reread.tsv`), folded by `tools/lookalike_pass.py reconcile` (fixed 2-of-3 rule; tiles/passC built from the reconcile_passes draft by a scratch adapter, since the packet subcommand needs a symbol sheet this script does not have): 28 settled, 15 relabelled, **6 UNSETTLED (residual 6/184 = 3.3 pct, agreement not accuracy)** -> `fig1-tx/focus.tsv` for the sign sorter, never blocking. err_true not measurable: no benchmark item of this hand.
Result: `ciphertext_fig1.txt` (176 signs, 7 lines, 2 OBSCURED spans; `ciphertext.txt` left as transcribed, rule 1). Against bSUF's 166-sign pooled read the new read has 10 more signs and resolves the pooled dot clusters except 5 `tooth`. **L5 group 4: both blind passes read `mim ha2 mim dal`** (agreed, M) -- the FT4 dispute is settled against bSUF's `mim ha ya dal`; the shape matches the name Muhammad that Bulliet reports, a script reading graded I here (no reading claimed). Commonest signs: lam 20, waw 17, dal 14, kaf 14, sin 13, mim 13, ta 12. Splits concentrate on dot counts (tooth vs nun/ba/tha, nga vs ghayn x3) and lam/dal/alif strokes.
Vision calls: 2 passes + 1 look-alike re-read (3 of 3). Requests: mizanproject.org 1. No decipherment attempted.

## GAPS90-sufi-fiddle (3 Oct 2026, account-4): Tausug word-list match on ciphertext_fig1.txt

Step (GAPS87 Verdict): match the 7 lines against a Tausug word list with a control. Pre-registered and pushed before scoring
(`tausug/PREREG.md`, commit 220d26e7); script `tausug/match.py`, output `tausug/results.json` (seed 1); sources in
`tausug/manifest.json`, none committed. Lists: L_PD = Cowie, *English-Sulu-Malay Vocabulary* (1893, public domain, archive.org
OCR; Sulu and Malay columns not separable, so Malay rides along), 5,575 skeletons; L_NT = Tausug New Testament word types
(Wycliffe 1998/2018, eBible tsg, all rights reserved -- local statistics only), Revelation held out, 4,772 skeletons.
Wiktionary's Tausug lemmas (CC BY-SA) were tried first: HTTP 429 twice, left alone.
Statistic: consonant-skeleton coverage C3 by a tiling of 1-3 consecutive visible groups (word boundaries only at gaps),
spans of skeleton length >= 3; 128 target consonants. Null: 1000 random permutations of the 13 consonant classes over
the cipher signs (identities scrambled, structure kept -- a null that can move the statistic, unlike group-order
shuffling). Positive control: 20 held-out Revelation chunks rendered as Jawi-like groups at the target's consonant count,
0/10/20 pct class substitution (brackets the 18.5 pct err_2reader), each against its own 200-permutation null.

| list | target C3 | null mean / p95 | p (seed 1; seed 2) | C2 p | control C3 at 0/10/20 pct | control power at 0/10/20 pct | gate |
|---|---|---|---|---|---|---|---|
| L_NT (Tausug NT) | 0.398 | 0.295 / 0.422 | 0.092; 0.103 | 0.071; 0.075 | 0.70 / 0.60 / 0.51 | 1.0 / 1.0 / 1.0 | **FAIL** |
| L_PD (Cowie, Sulu+Malay) | 0.594 | 0.429 / 0.547 | 0.015; 0.004 | 0.010; 0.004 | 0.58 / 0.53 / 0.52 | 0.75-0.9 / 0.60-0.65 / 0.35-0.55 | NON-TEST (power < 0.8 at 20 pct) |

Per-length breakdown (spans chosen in the tiling, L=2/3/4+): L_NT C3 0/14/2, C2 18/15/0; L_PD C3 0/24/1, C2 14/25/0.
Singleton-group matches (L=2/3/4+): L_NT 25/7/0; L_PD 25/13/0. No span of skeleton length >= 5 matched in either list.
Reading of the numbers: against the clean Tausug list, which reads real held-out Tausug at full power even at 20 pct
noise, the inscription's coverage (0.398) is inside its own null (p 0.09-0.10) and below the noisy control's mean (0.51):
a control-backed FAIL for Tausug *under this rendering convention* (vowel letters dropped, g=k, fa=p, nga/ghayn=N, tooth
as wildcard; the true Sulu Jawi spelling of 1968 or earlier is not known and may differ). Against the Sulu+Malay list the
inscription sits above its null (p 0.004-0.015) and above real Tausug's own coverage of that list (0.594 vs 0.52-0.58),
but that list's power is under the pre-registered 0.8, so it is not a pass -- the gap between the two lists points at the
Malay (or Arabic-loan) part of Cowie's vocabulary, not at Tausug; a lead for the next test, not a finding. No token is
read or graded by this test (0 H, 0 C, 0 S, 0 M, 0 I); no decipherment attempted.
Requests: ebible.org 3, en.wiktionary.org 2 (both 429), archive.org 3 (advancedsearch 1, one 500 on the first Cowie
identifier, Cowie djvu 1); all >= 2 s apart. Vision calls: 0.

## GAPS93-sufi-fiddle (3 Oct 2026, account-4): Malay and Arabic word-list match on ciphertext_fig1.txt

Step (GAPS90 Verdict): the same match design against a Malay and an Arabic word list, separately. Pre-registered and pushed
before scoring (`malay-arabic/PREREG.md`, commit f7d6bdd3); script `malay-arabic/match2.py` (imports the statistic, null and
renderer from `tausug/match.py`), output `malay-arabic/results.json` (seed 1) and `results_seed2.json`; sources in
`malay-arabic/manifest.json`, none committed. L_MS = Leipzig `msa_wikipedia_2021_30K` (CC BY 4.0), first 80 pct of sentences
as the list (18,407 skeletons), last 20 pct held out for the control. L_AR = Tanzil Quran simple-clean (CC BY 3.0), suras
1-77 as the list (5,643 skeletons), suras 78-114 held out (2,462 words; the prereg's 91-114 fallback rule applied, since 91-114
is under 1,000 words). Arabic letters mapped to the cipher's own 13 classes (PREREG). One fix after the prereg commit, before
any score was read: Malay held-out words spell x as "ks" before rendering (the GAPS90 renderer maps one letter to one class
and crashed on x); lists and statistic unchanged.

| list | target C3 | null mean / p95 | p (seed 1; seed 2) | C2 p | control C3 at 0/10/20 pct | control power at 0/10/20 pct | gate |
|---|---|---|---|---|---|---|---|
| L_MS (Malay, Leipzig wiki) | 0.703 | 0.587 / 0.695 | 0.047; 0.047 | 0.005; 0.009 | 0.84-0.86 / 0.75-0.76 / 0.69-0.73 | 1.0 / 0.95-1.0 / 0.85-0.95 | PASS (marginal) |
| L_AR (Arabic, Quran 1-77) | 0.523 | 0.367 / 0.492-0.500 | 0.019; 0.025 | 0.018; 0.019 | 0.75-0.76 / 0.67-0.69 / 0.57-0.60 | 1.0 / 1.0 / 0.95-1.0 | PASS |

Per-length (spans chosen, L=2/3/4+): L_MS C3 0/20/7, C2 17/19/6; L_AR C3 0/15/5, C2 16/17/3. Singleton-group matches
(L=2/3/4+): L_MS 25/12/4; L_AR 25/7/3.
Reading of the numbers: both lists pass the pre-registered gate (p < 0.05 and power >= 0.8 at 20 pct noise), Arabic more
clearly than Malay. The Malay p (0.047 on both seeds) sits on the line and would not survive a Bonferroni correction for the
two lists of this step (0.025), nor for the four lists run on this transcription so far (GAPS90 + GAPS93, 0.0125); the Arabic
p (0.019-0.025) survives the two-list correction at seed 1 only and not the four-list one. The inscription's C3 against each
list sits at or just below that list's own held-out text at 20 pct noise (Malay 0.703 vs 0.69-0.73; Arabic 0.523 vs 0.57-0.60),
i.e. about where real text of that language would land through a transcription this noisy. With GAPS90 (Tausug NT FAIL,
Cowie Sulu+Malay p 0.004-0.015 at low power) the pattern is: Arabic and Malay vocabularies cover the skeletons better than
chance, the Tausug NT list does not. "Worth a reader", not a reading: no token is read or graded by this test (0 H, 0 C, 0 S,
0 M, 0 I). Possible confounds not tested here: Arabic loanwords and formulae shared by Malay and Tausug (a Sufi divination
text would carry them under any of the three), and the size difference between lists (handled by the per-list null, not
removed).
Requests: downloads.wortschatz-leipzig.de 2 (1 HEAD, 1 GET), tanzil.net 2 (1 HEAD, 1 GET), gutendex.com 1 HEAD (not used),
all >= 3 s apart. Vision calls: 0.

## GAPS94-sufi-fiddle (3 Oct 2026, account-4): matched-span dump and one blind Opus Jawi/Arabic reading pass

Step (GAPS93 Verdict). Pre-registered and pushed before the reader call (`reader/PREREG.md`, commit 1015a6a4, with the prompt,
the render script and the comparison script). (1) `malay-arabic/dump_spans.py` -> `malay-arabic/spans.tsv`: 136 rows (every
1-3-group span whose skeleton is in the Malay or Arabic list at length >= 2, words with counts, tiling marks); the chosen C3
tiling reproduces GAPS93 exactly (Malay 27 spans, 90/128 consonants = 0.703; Arabic 20 spans, 67/128 = 0.523). (2) One blind
Opus 5.5 call, text only, no tools, no image, no word-list results (`reader/prompt_reader.txt`; input `reader/fig1_arabic.txt`,
the sign names rendered in Arabic/Jawi letters by `reader/render_arabic.py`). Output `reader/reader_out.json`: 12 items
(1 H, 2 M, 9 L). The reader's own overall view: Jawi-type spelling (nga, possibly fa for pa), Malay-world language (Malay, or
a Philippine Jawi such as Tausug or Maranao) with Arabic religious words, perhaps an amulet or devotional formula; "I could not
get a running reading" (language confidence L).

| line, groups | reader's word (gloss) | reader conf | grade | S1: in a chosen C3 span | S2: same word in a list at that span |
|---|---|---|---|---|---|
| L05 g4 | muhammad (name) | H | M | yes | AR |
| L01 g1 | huwa (He, invocation) | M | M | yes | no (skeleton h, under length 2) |
| L04 g7 | kamu (you) | M | M | yes | MS |
| L04 g13 | beserta (together with) | L | I | yes | MS |
| L06 g7 | barakat (blessing) | L | I | yes | no |
| L02 g13 | sabi' (seventh) | L | I | no | no |
| L04 g10 | kufr/kafir | L | I | yes | AR |
| L04 g1-2 | pangku (lap) | L | I | yes | no |
| L04 g4 | -mu (your) | L | I | yes | no |
| L06 g6 | tang (unclear) | L | I | no | MS |
| L06 g8 | dua (two) | L | I | yes | no |
| L06 g15 | la mahala (inevitably) | L | I | no | no |

Pre-registered statistics (`reader/compare.py`, `reader/compare.json`): **S1 all items 9 of 12 overlap a chosen C3 span, expected
8.91 under uniform placement, p 0.63; H/M items 3 of 3, expected 2.05, p 0.30** -- no agreement beyond chance, because the
tiling already covers about three quarters of the visible groups (the statistic has little room to move at this coverage;
reported, not read as a negative). **S2: 5 of 12 reader words (2 of 3 at H/M) are the very word a list holds at that span**
(muhammad and kufr in the Arabic list; kamu, beserta, tang in the Malay list); descriptive only, no gate.
Grades (rule 4): 0 H, 0 C, 0 S, 3 M (muhammad, huwa, kamu), 9 I. The only reading at the reader's own H, Muhammad at L5 g4,
is the name Bulliet already reported; nothing else reaches a running text. Worth noting, not a finding: the reader's
independent language view (Malay-world Jawi with Arabic loans) points the same way as GAPS93's word-list result, which the
reader never saw; both rest on the same transcription (err_2reader 18.5 pct), so this is consistency, not confirmation.
Calls: 1 text-only subagent call (no vision). Requests: downloads.wortschatz-leipzig.de 1, tanzil.net 1 (refetch of the GAPS93
sources, sha1 match), both >= 3 s apart.

## GAPS98-sufi-fiddle (3 Oct 2026, account-4): one blind Opus vision reading pass on the 7 Figure 1 line crops

Step (GAPS94 Verdict). Pre-registered and pushed before the call (`vision/PREREG.md`, `vision/prompt_vision.txt`,
`vision/compare_vision.py`, commit a6350b0e). Figure 1 refetched once (mizanproject.org, sha1 2825b442... = GAPS87's), cut with
the GAPS87 command (`tools/iiif_lines.py --image <scratch>/fig1.jpg --out <scratch>/crops --prefix fig1 --region 0,0,2490,1301
--max-width 2490 --centres 148,289,445,613,820,1000,1195 --debug`; boxes identical to `fig1-tx/crops_manifest.json`), scratch
only, image and crops not committed. One blind Opus 5.5 vision call on the 7 crops only (no sign transcription, no word-list
hits, no prior readings; only the per-line group counts so positions can be located). Output verbatim `vision/vision_out.json`;
comparison `vision/compare_vision.json` (S1/S2 by `reader/compare.py` unchanged, on `vision/vision_items_valid.json`).
The reader saw group counts L01 5, L02 16, L03 5, L04 15, L05 6, L06 17, L07 4 (ours 6/15/4/15/6/15/4), so its L06 numbering
can sit one or two groups off ours; per the prereg nothing was re-mapped by x position. 7 items, 1 dropped (L06 g17, out of
range: "la ... Muhammad?", L, a possible shahada end), 6 scored.

| line, groups | vision reader's word (gloss) | conf | grade | S1 in C3 span | S2 list word | S3 overlaps text reader | S4 same skeleton |
|---|---|---|---|---|---|---|---|
| L05 g4 | muhammad (name) | H | M (two readers) | yes | AR | muhammad | yes |
| L06 g8-9 | barakat (blessing) | M | M | yes | no | dua (text reader's barakat sits at g7) | no |
| L06 g13-14 | 'ala kull(i) (upon all) | L | I | yes | no | -- | -- |
| L04 g2 | -ku / aku (I, my) | L | I | yes | no | pangku | no |
| L04 g4 | -mu (your) | L | I | yes | no | -mu | yes |
| L02 g12-13 | sabi' (seventh) | L | I | no | no | sabi' | yes |

Pre-registered statistics: **S1 (vs spans.tsv chosen C3) 5/6, expected 5.12, p 0.79; H/M 2/2 vs 1.83, p 0.83** -- no agreement
beyond chance (the tiling covers about three quarters of the groups, as in GAPS94). **S2 1/6** (muhammad, Arabic list).
**S3 (vs GAPS94 text reader) 5/6 overlap, expected 1.88, p 0.010; H/M 2/2 vs 0.52, p 0.060. S4: 3 of 5 overlapping pairs share
the consonant skeleton (muhammad, -mu, sabi'), chance rate r 0.042, expected 0.21** -- descriptive, no gate. Reading of the
numbers: the two Opus readers converge on the same few spots and words well beyond chance, but this is two readers of ONE hand
copy from one model family, and the text reader's signs were themselves Opus reads of these crops (GAPS87): convergence, not
confirmation. Only muhammad (L5 g4) reaches H with either reader, and that is the name Bulliet already reports. barakat is given
by both readers at M/L but one group apart (g7 text, g8-9 vision -- the vision reader saw 17 groups in L06), so S4 does not count
it. Language view, independent of GAPS93/94's lists: "Malay in Jawi (possibly Tausug, Maranao, or Javanese Pegon) with Arabic
religious loanwords", confidence L; "not continuous readable prose ... a devotional or amuletic text ... or a garbled copy or
cipher of one". New candidates raised (I, not tested): L06 g13-14 'ala kull(i) (as in 'ala kulli shay'in qadir) and a shahada
ending at the L06 tail.
Grades (rule 4), this pass: 0 H, 0 C, 0 S, 2 M (muhammad, barakat), 4 I. Combined with GAPS94 (distinct words): 4 at M
(muhammad L5 g4 -- both readers; huwa L1 g1; kamu L4 g7; barakat L6 g7/g8-9 -- both readers, span differs), the rest I; no
running reading.
Calls: 1 vision subagent (Opus). Requests: mizanproject.org 1, downloads.wortschatz-leipzig.de 1, tanzil.net 1 (sha1 matches the
GAPS93 manifest), all >= 3 s apart. No decipherment attempted.

## Remaining gaps (GAPS87-sufi-fiddle, 3 Oct 2026; updated GAPS93, GAPS94, GAPS98)
Read so far: 4 words at M (muhammad L5 g4 and barakat L6 -- both readers; huwa L1 g1, kamu L4 g7 -- text reader GAPS94), the rest I, 0 H/C/S; no running reading.
- independent copy of the violin text - blocker: needs-physical-access; the violin is unlocated (its holder never identified, Bulliet 2021) and Figure 1 is the same sheet as the folder image, so every image on record is one hand copy
- language identification (Tausug vs Maranao) - blocker: waiting-on R. D. Trimillos's reply to Bulliet; Kawashima ruled Maranao out and Bulliet's query on Tausug was pending at 31 Dec 2021 (Mizan essay, GF4-BATCH18)
- Malay/Arabic-loan reading of ciphertext_fig1.txt - blocker: not-attempted; text-only reader (GAPS94) and blind vision reader (GAPS98, 3 Oct 2026) done: vision 6 scored items, S1 5/6 vs 5.12 (p 0.79), S3 vs text reader 5/6 vs 1.88 (p 0.010), S4 3/5 same skeleton vs 0.21 expected; 4 words at M, no running reading; next: script test of the two formula candidates the vision reader raised (L06 g13-15 'ala kulli shay'in qadir; L06 tail shahada) against ciphertext_fig1.txt's sign sequence with an edit-distance null over random Quran/formula spans, ~$1

## Escalation (3 Oct 2026)
- [n/a] siblings: no other inscription by this hand known; the Blue Booklet is a different text
- [n/a] clear-pages: an inscription, no clear text beside it
- [n/a] known-keys: not a cipher on present evidence; script reading, no key
- [x] print: Bulliet's own 2021 essay read in full (GF4-BATCH18); its Figure 1 diffed here (FT4)
- [n/a] key-rebuild: no key involved in a script reading
- [x] image-check: Figure 1 re-transcribed from 2500 px line crops (GAPS87, 3 Oct 2026): err_2reader 18.5 pct, look-alike residual 3.3 pct
- [n/a] retry: no failed attempt with a changed knob to retry
Verdict: keep going: 1 internal gaps; cheapest next: script test of the vision reader's formula candidates (L06 g13-15 'ala kulli shay'in qadir; L06 tail shahada) against ciphertext_fig1.txt's signs, edit distance vs a null of random formula/Quran spans of equal length, no vision call, ~$1

## While waiting (GAPS87-sufi-fiddle, 3 Oct 2026)

Nothing here waits on a person for the next step: the zero-dependency action is the formula script test (Verdict above; GAPS98's vision reader converged with the text reader, S3 p 0.010; Tausug NT FAILed in GAPS90, Malay and Arabic passed the gate in GAPS93, the text-only reader of GAPS94 read 3 words at M). Trimillos's reply on Tausug and the sign sorter's 6 tiles are the outside waits; neither blocks it.

## Intake gate (GF4-BATCH18, 3 Oct 2026)

$ python3 tools/intake_gate_check.py sufi-fiddle
sufi-fiddle: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit 0

$ python3 tools/next_steps.py --wait-only | grep sufi-fiddle
(no line)
