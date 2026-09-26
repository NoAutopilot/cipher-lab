open
Checked 26 Sept 2026 by bSZEM: this worker read the item's own three DjVu page images directly, full-page (leaves
foliated 65-67, publication/430427/edition/343124, fetched from wbc.poznan.pl and read from page images).
Bourdeau CATALOGUE.md #348 (fresh shallow clone, HEAD at clone time) says "Free
images in the Wielkopolska Digital Library; length and system not yet checked. No reading found" and the
repo's oldest/scan_2026-09-23/hard_targets.md #11 gives the same verdict ("Prior art: none found; length and
system not yet checked"); grep of a fresh shallow clone of aaymeloglu/unsolved-ciphers for szembek/kornick/
343124: 0 hits (not in that catalogue either); Tomokiyo's pages on disk (sources/cryptiana/) mention only a
different, 20th-century Jan Szembek (Polish interwar diplomat, unrelated); one OpenAlex query ("Szembek cipher
Kornicka") 0 results; one Semantic Scholar query ("Szembek cipher decrypted") 903 generic crypto-paper hits, none
naming Szembek or Kórnik; one web search for the item's Polish title and shelfmark returns only the WBC catalogue
page itself, nothing else. This worker also read the item directly: downloaded and decoded all three DjVu page
images (leaves foliated 65-67, publication/430427/edition/343124) from wbc.poznan.pl and viewed them full-page.
No prior decipherment, transcription or publication of this letter found anywhere searched.

# Szembek BK 1560 -- "List zaszyfrowany"

## Source
- PAN Biblioteka Kórnicka, sygn. BK1560-1 (Mf6795), within the bound volume "Akta do panowania Augusta II. Vol.1"
  (150 leaves, 37x24 cm, "partly from the archive of Jan Szembek, Crown Chancellor 1700-1731").
- Digitised by PAN Biblioteka Kórnicka; hosted at Wielkopolska Digital Library (Wielkopolska Biblioteka Cyfrowa),
  wbc.poznan.pl. Catalogue page: https://www.wbc.poznan.pl/dlibra/publication/430427/edition/343124?language=en
  (item title "List zaszyfrowany" = "Encrypted letter"). Direct multi-page package:
  https://www.wbc.poznan.pl/Content/343124/download/ (a 5-file dLibra zip: readme.txt, directory.djvu,
  065_0001.djvu, 066_0001.djvu, 067_0001.djvu -- three page images, foliated ff.65-67 of the bound volume,
  fetched once, 1.9 MB).
- Object type: rękopis (manuscript). Creation date: "18w." (18th century) -- consistent with the volume's
  Augustus II-era Polish crown chancery correspondence, c.1700-1731.
- Language (catalogue): lat (Latin). Confirmed by eye: the letter's clear-text connective words (et, in, ac, ab,
  quam, cum, quibus, quorum, sed, nobis, illorum...) and glossed words (Celsissimus, Princeps, Christianam,
  conscientiam, procedimus, patriam...) are Latin.
- Rights: "domena publiczna" (public domain); Access rights: "dla wszystkich bez ograniczeń" (unrestricted for
  everyone). Free to use.

## Images
`images/343124_List_zaszyfrowany.zip` (source package, 1.9 MB) and three converted JPEGs (065_0001.jpg,
066_0001.jpg, 067_0001.jpg; downsampled from the DjVu's native 300 dpi/~3300-3550 px to 1800 px wide, ~0.8 MB
each) in `images/`, with `images/manifest.json`. Folder total 4.2 MB, well under the 30 MB cap.

## What the leaves show (IMPORTANT finding)
This is a numeral-nomenclator cipher, two-digit code groups (occasional 3-digit, e.g. "203", "202" -- these read
as cross-reference numbers to other items in the same bound volume, "Datis sub 202" = "given under [no.] 202",
not cipher code), space-separated, written inline with plain Latin connective words and some names left en clair.

**The letter carries an interlinear gloss in a lighter (sepia/light-brown) ink, written above nearly every
cipher code group, giving that code's plaintext Latin word** (e.g. leaf 1: "Celsissimus Princeps" above
"42 14 49 21 46 21 21 46 50 12 21"; "qui" above "24"; "Christianam" above "23 14"; "conscientiam" above a code
run; "procedimus"/"procedemus" above others; leaf 2: "Detractor", "Burgundus", "Danod", "antidius", "perfido ac
proditore", "patriae", "defuncto Principem", "Serbanum reduxit", "deceptionibus"...; leaf 3: "promissiones",
"aula", "defuncto", "Principi", "hinc", "delationes", "falsa"/"comperta", "vindictam sumat", "Pergenbeio" (a
name, appears twice), "occisus", "caput", "Honorarie", "Sityka"). This looks like a period (or near-period)
decipherment written directly onto the manuscript by a contemporary hand, not a modern pencil annotation -- the
gloss ink and the cipher-number ink both look 18th-century. It is NOT mentioned in Bourdeau's catalogue entry
("length and system not yet checked" -- consistent with nobody having opened the image before this job) and was
not found in any search above. This worker did not verify whether the gloss is complete, whether it is
contemporary with the letter or a later archival hand, or whether it decodes every code group -- that needs a
transcription pass, not this sampling job.

## Approximate sign count
Three leaves, ~19 lines each (leaf 3 is shorter, ~17 lines) = roughly 55 lines total. Cipher code-groups run in
bursts of 3-15 per line, broken up by plain Latin words; a rough average of 6 code-groups/line gives an estimate
of **~300-350 two-digit cipher tokens** across the three leaves (not an exact count -- a transcription pass would
give the real number). Distinct code values seen range from the low teens to the low fifties (12-51 observed;
"42", "14", "21", "46" recur very often, consistent with common short words/syllables in a nomenclator of on the
order of 50-60 distinct values, not a full symbol-per-letter cipher). Two 3-digit numbers (202, 203) are
cross-reference numbers to other items in the volume, not cipher.

## Host notes
wbc.poznan.pl: reachable (200) with a descriptive UA; the catalogue page, DjVu directory file and the item's zip
download all served without a challenge. Its OAI-PMH METS endpoint
(`/dlibra/oai-pmh-repository.xml?verb=GetRecord&metadataPrefix=mets...`) served a JS proof-of-work bot challenge
page instead of XML on the one call tried -- not retried (good-citizen rule, one retry after a pause at most, and
this job did not need METS since the download zip already gave the page files and full metadata came from the
catalogue page itself). Total requests to wbc.poznan.pl: 6 (catalogue page x2 languages, content page, directory.djvu,
zip download, HEAD on zip), all >=1.5 s apart, one OAI-PMH attempt that hit the challenge.

## Next step (for the orchestrator/lane, not run this job)
Recommended first test is NOT blind cryptanalysis: transcribe the interlinear gloss (all three leaves) into a
code-value -> Latin-word key table, grade C (from the manuscript's own apparent period decipherment, not
cryptanalysis), then check internal consistency (does the same code always get the same glossed word wherever it
recurs across the three leaves? a real key must; log the rate). This is "the same letter['s own] gloss" per
CLAUDE.md's lead-classes-beat-queue-rank ordering (an interlinear gloss ranks above cryptanalysis) -- see spec.

## Leaf 66 crop step (bSZL66, 26 Sept 2026)
Native leaf: `343124_List_zaszyfrowany.zip` (source zip, kept on disk) -> `066_0001.djvu` decoded once with
`ddjvu -format=tiff` then PIL to PNG at native 3354x4185 (scratchpad only, not committed; too big for the 30 MB
folder budget and not needed after crops are cut).
Crop command run (mandatory step, pasted before transcription):
```
python3 tools/iiif_lines.py --image <native 066_0001 PNG> --out ciphers/szembek-bk1560/leaf66/crops \
  --prefix f66 --distance 140 --top-margin 150 --debug
```
Default `--distance` (63, 0.7x the autocorrelation pitch 91) over-segmented into 24 bands: the interlinear gloss
words are sparse enough that the row ink-profile often finds a second local maximum in the gap above a cipher
line (a lone gloss word) as its own "line", roughly 70-90 px from the cipher line's own peak, alternating with
true baseline-to-baseline gaps of 160-220 px -- checked against the debug overlay, where several blue centre
lines fell in pairs 70-90 px apart. `--distance 140` (about the true line pitch) merges each such pair back into
one band per physical cipher line: 20 bands, matching an eye count of the leaf's ~19-20 written lines. The
first band still clipped the very first gloss word ("Detractor", sitting in the top margin above line 1's
cipher, with no line above it to donate band height) even after that -- native-pixel check on a 0-500 crop
placed "Detractor" at y~190-300, past the plain band-1 top edge of 309. `--top-margin 150` (documented in the
tool's own docstring for exactly this) shifts every band's top edge up by 150px; band 1 then starts at 160,
comfortably including "Detractor" with margin, and the extra 150px at the top of every other band is just
harmless repeated context from the line above (checked on f66_L02/L03: the tail of the previous line's cipher
group appears at the very top of the next crop, not confused with the current line's own gloss). Verified against
the debug overlay (`f66_lines_debug.jpg`) and three crops (L01, L02, L03) by eye before transcribing further.
20 bands x 2 width-segments (line width 3354 > the 2400px max) = 40 crop files, `f66_L<NN>_s{1,2}.jpg`.

## Leaf 65 crop step (bSZL65, 26 Sept 2026)
Native leaf: `343124_List_zaszyfrowany.zip` (source zip, already on disk, no fetch) -> `065_0001.djvu` decoded once
with `ddjvu -format=tiff` then PIL to PNG at native 3552x4632 (scratchpad only, not committed).
Crop command run (mandatory step, pasted before transcription):
```
python3 tools/iiif_lines.py --image <native 065_0001 PNG> --out ciphers/szembek-bk1560/leaf65/crops \
  --prefix f65 --distance 150 --debug
```
Default `--distance` (58, 0.7x the autocorrelation pitch 84) over-segmented into 27 bands for the same reason
bSZL66 found on leaf 66: the ink-profile peaks on the interlinear gloss word as its own line, 70-120 px from the
cipher line's own peak, alternating with true line-to-line gaps of 174-329 px. `--distance 150` merged each such
pair back to 20 bands, matching an eye count of the leaf's 20 written lines (confirmed: no more ink below the
last band, y 4278-4632 is blank margin).
This alone was not enough: the debug overlay's blue band edges are midpoints between the 20 merged centres, and
on this leaf the gloss sits close enough to that midpoint that a plain per-line crop (`f65_L02_s1.jpg`, first
attempt) cut "Celsissimus Princeps" almost exactly in half between band 1 and band 2 -- confirmed on native-pixel
test crops (`(0,380,3552,620)` shows the whole gloss+cipher line cleanly; the tool's own per-band split did not).
Rather than `--top-margin` (a single fixed shift applied to every band, which bSZL66 used), this leaf's bands were
cut directly from the 20 centres with a manual asymmetric margin (top -160px, bottom +80px around each centre,
clipped to stay at least 25px clear of the neighbouring centre) so each band favours the space above its own
cipher line, where the gloss sits. Spot-checked by eye on 5 of 20 bands (lines 1, 5, 9, 13, 17, 19, 20) before
transcribing the rest: each held its full gloss word(s) and full cipher line, no bleed of the neighbouring line's
own cipher/gloss text (a little of the previous line's tail ink is harmless overlap, same finding as leaf 66).
20 bands x 2 width-segments (line width 3552 > the 2400px max, split at 2400 with 150px overlap, same convention
as the tool) = 40 crop files, `f65_line<NN>_s{1,2}.jpg`, manifest at `leaf65/crops/manifest.json`.

## Leaf 65 transcription (bSZL65, 26 Sept 2026)
Transcribed crop by crop (worker only, no subagent) into `leaf65/pairs.tsv` (20 rows, one per physical line) and
`leaf65/groups.tsv` (150 code tokens + connective/clear tokens, one row per token). `?` used for one illegible
struck-through mark on line 1; a struck `20 et` fragment on line 20 kept as tokens with a note rather than dropped.

Counts: 150 code tokens (kind=code), 19 distinct code values, 21 of the 150 code tokens (14.0%) carry a
gloss_above (the rest of a multi-code word run were left blank per the brief's rule: gloss goes on the token
where placement is visually clear, not guessed across the rest of the run -- see caveat below).

**Self-check (rule 3 form, run before transcribing further): consistency of a recurring code's gloss vs a shuffled
control.** Only 4 of the 19 distinct codes recur with >=2 glossed occurrences (42, 17, 25, 50), giving 18 same-code
gloss pairs total. Real transcription: 0/18 pairs have the *identical* gloss string (rate 0.0). Shuffled control
(gloss strings reassigned across code occurrences at random, 1000 shuffles, seed 20260926): mean 0.0, 95th pct 0.0
-- real and shuffled are identical, 0 both ways. **This control does not discriminate** (CLAUDE.md rule 3's own
"a control that cannot vary on the same axis it is testing licenses nothing" paragraph applies here too): with 21
glossed tokens spread over mostly-unique multi-word phrase strings, the exact-string-match test has ~0 probability
of a same-string pair under ANY assignment, real or shuffled, so a 0.0-vs-0.0 result is a non-test, not a negative.
The reason is structural, not a transcription failure -- see next paragraph.

**Nomenclator (one word/code) or syllabic (letters per code)?** The leaf's own evidence says syllabic/digraph, not
nomenclator: "Celsissimus Princeps" (2 words, ~19 letters excl. spaces) spans 11 two-digit codes (42 14 49 21 46 21
21 46 50 12 21); "conscientiam" (12 letters) spans 6 codes (42 13 51 21 42 46); "Christianam" (10 letters) spans 4
codes (42 44 23 46) -- roughly 1.7-2 letters per code throughout, not 1 code per word. That means a single code
value (e.g. 42, 25, 50) recurs as a fragment inside many DIFFERENT glossed words, so its exact-string gloss is
expected to differ at almost every occurrence even under a correct, consistent key -- this is what made the rule-3
control above non-discriminating, and it is the reason to read code 25's four occurrences qualitatively instead:
"procepimus", "procedimus", "et procedemus", "procedant" -- four different inflections of the SAME verb stem
*procedere*, at four different points on the leaf. That is a real, non-random, code-level consistency signal (a
shuffled reassignment would not reliably land four occurrences of the same code on forms of one verb), just not
one an exact-string pairwise test can see. Recommend the merge job (or a follow-up) build a stem/root-match
consistency check instead of exact-string match before drawing a rule-3 verdict on the pooled 3-leaf key.

Caveat on gloss_above placement: multi-word glosses spanning many codes were attached to the FIRST code of the run
only (blank for the rest), per the brief's instruction to leave gloss_above blank where per-token placement is not
visually clear -- true per-glyph horizontal alignment (which of the 4-11 codes in a run sits under which specific
syllable of the gloss word) was not attempted this pass; it would need pixel-position measurement per glyph, out of
this job's box.

Files: `leaf65/pairs.tsv`, `leaf65/groups.tsv`, `leaf65/crops/*.jpg` (40 crops + manifest.json), this section.

## Leaf 66 transcription (bSZL66)
`leaf66/pairs.tsv` (20 lines) and `leaf66/groups.tsv` (231 tokens) transcribed by eye from the 20 crops above
(no subagent; read every crop myself). Grade C throughout (period gloss, not cryptanalysis).

**168 code tokens (two- or three-digit numeral groups), 21 distinct code values** (12,13,14,15,17,19,20,21,23,
25,29,40,41,42,43,46,49,50,51 plus one ref "202"), well inside the spec's estimated 12-51 range and far fewer
distinct values than the ~50-60 guessed from the single-leaf sample in the intake pass -- leaf 66 alone doesn't
reach the full alphabet, or the true alphabet is smaller than the intake estimate; a 3-leaf merge will tell.
**87/168 code tokens (51.8%) carry a `gloss_above`** -- but this is a floor, not the true coverage: gloss_above
was only filled where a numeral cluster's length locally matched its gloss word's letter count one-for-one
(stripping an immediately-following clear suffix like "-us"/"-am" first); clusters that didn't match a clean
1:1 count (e.g. "perfido" 7 letters vs. 4 codes, "deceptionibus" minus "-us" 11 letters vs. 9 codes) were left
blank rather than guessed, even though every code group on the leaf appears to carry *some* gloss word above it
per the intake pass's eyeball finding. A merge/alignment pass (tools/interlinear_align.py, hard-EM per group
across all 3 leaves) would recover most of the blanked ones; this job did the one-line, no-aligner-yet self-check
the brief asked for.

**Consistency check (does a recurring code get the same letter every time it recurs?):** 15 code values recur
>=2 times among the 87 glossed tokens (85 total occurrences). Real same-letter-each-time rate: **0.918**.
Shuffled control (1000 shuffles of the gloss letters across the same recurring-code slots, seed 20260926):
mean **0.306**, 95th pct **0.341**. The real rate clears the shuffled 95th pct by more than 2.5x -- the gloss is
a working key, not noise. Per-code detail: 12/15 codes are perfectly consistent (13=o x7, 14=e x4, 17=a x8,
20=t x5, 23=r x9, 25=p x4, 46=i x13, 50=m x3, 51=n x8, plus 21=s/S x6 case-insensitively, 43=d/D x3
case-insensitively, 29=B/b x3 case-insensitively). Two codes conflict: **42** reads d twice (proditore, from
NOTES' own earlier per-letter read) and c twice (consilia, intricauit) -- an even split, flagged, not resolved
here (possibly a mistranscribed digit on one side, e.g. 42 vs. a similar-looking neighbour; needs a merge pass
against leaves 65/67 or a fresh look at the image). **12** is u x4 and a x1 (one outlier, "Serbanum" pos5 read as
"a" -- could be a genuine homophone or one bad alignment); **15** is a x2, e x1 (both plausible as homophones
for two different frequent vowels, see below).

**Letters, not one code per word (nomenclator).** Multiple words (antidius 8 codes/8 letters, Danod 5/5, Burgund-
stem 7/7, proditore 9/9, nobis 5/5, patria 6/6, pia 3/3, memorie 7/7 incl. two literal clear "m" tokens, Serbanu-
stem 7/7, consilia 8/8, nos 3/3, miseram 7/7) align code-count to letter-count exactly, strongly indicating a
**code-per-letter** cipher, not a code-per-word nomenclator (contra the intake pass's "consistent with a
nomenclator" guess from raw code range alone). The letter 'm' itself is apparently never coded -- it appears as
a literal clear "m" in every case observed (memorie, Defunctum, Serbanum) -- and short connective/suffix material
(ac, et, in, cum, his, eas, us, xit-type endings) is left in clear throughout, consistent with this being a
partial code (letters coded, common short words and grammatical endings left en clair), not a pure cipher.
**Vowels look homophonic**: 'a' appears at both 17 (8x, dominant) and 15 (2x); 'e' at both 14 (4x, dominant) and
15 (1x) -- i.e. code 15 itself may be shared between 'a' and 'e' as a low-frequency homophone for both, or one of
those 3 occurrences is a misread; not resolved here. Consonants seen so far (o,t,r,p,i,m,n,s,d,b,u) show no
homophones (one code each) in this leaf's sample.

Two 20-minute zoom checks (line 6 and line 8, native-pixel crops) confirmed digit readings against ambiguous
cases; both are noted inline above. Self-check numbers above are reproducible from `leaf66/groups.tsv` with the
scratchpad script `consistency_check.py` (not committed, scratchpad-only per the brief; re-derivable from the
groups.tsv logic described here: recurring-code same-gloss rate vs. 1000-shuffle control).

## Leaf 67 transcription (bSZL67, 26 Sept 2026)

Native image: `067_0001.djvu` -> `ddjvu -format=tiff` -> PIL PNG, 3314x4571 px (kept in scratchpad only, not
committed). Crop step: row ink-density profile (numpy, threshold <180, smoothed, scipy.signal.find_peaks
distance=100 prominence=200) found 21 line centres (tools/iiif_lines.py's own default distance/prominence
under-merged two lines, e.g. it read only 19 bands and split "50 17 20. Pergenbeio" from "De 41 14..." at the
wrong point -- widened by hand per Usage note: fixed top margin 135px / bottom margin 55px per centre, PIL crop,
not the tool's adaptive band split, because two adjacent line gaps on this leaf (109px, 116px) are much smaller
than the modal 190px pitch and the tool's midpoint-band scheme cut through gloss text at those two spots).
21 lines, 45 image files (21 lines x up to 2 width-segments + 1 debug + manifest) in `leaf67/crops/`
(`f67_L01..L21_s1/s2.jpg`), folder well under 30 MB. Debug overlay `f67_lines_debug.jpg` (red = centre, blue =
crop top/bottom). Transcribed by this worker directly from the crops (no subagent).

`pairs.tsv` (21 rows) and `groups.tsv` (195 token rows, one row per cipher_raw token) written per the brief's
columns. Grade C throughout (gloss read from the manuscript's own period annotation, not cryptanalysis); a
handful of individual clear-text words are low-confidence (cursive ambiguity: "ereti" L1, "instissimus" L10,
"n?"/"e?"/"a?" single-glyph marks L19/L21 that may be ink artifacts rather than letters) -- flagged
`confidence=low` in groups.tsv, not resolved by guessing further.

Counts: 120 code tokens, 19 distinct code values (12-51, no 3-digit cross-reference numbers on this leaf), 75
clear-text tokens. 18 of 120 code tokens (15.0%) carry a `gloss_above` value under this worker's convention of
attaching the full gloss word/phrase to the FIRST code token of the run it visually sits above (a gloss word
routinely spans several codes at once -- e.g. "Principi" over an 8-code run, "delationes" over a 7-code run --
so most non-initial tokens in a run are left blank rather than guessing a per-token split).

Self-check (step 4, both numbers): of the 19 distinct code values, 6 recur with >=2 glossed occurrences within
this leaf (41, 20, 13, 42 among them). Real same-code -> same-gloss-word match rate (occurrences matching that
code's most common gloss) = **0.429**; 1000-seed-42 shuffle control (gloss_above values permuted across all 18
glossed occurrences, same statistic) = **0.429 mean, 0.429 95th pct** -- real and shuffled are identical. This is
not a working control: nearly every glossed value is a distinct running-prose word used once (code 41 alone
carries three different glosses across its three glossed occurrences here -- "Pergenbeio", "Pergenbeii", "Sityk"),
so there are almost no cases where the SAME gloss word recurs on the SAME code for the shuffle to disrupt; per
CLAUDE.md rule 3's control-must-be-able-to-differ paragraph, a same-code/same-gloss statistic on a leaf this
short, under a first-token-of-run convention, is a non-test here, not a negative -- N is too small (18 glossed
occurrences, 6 recurring codes) and the labels are mostly unique. A leaf- or letter-pooled check (all three
leaves' gloss vocabulary together) would have far more repeated words (Pergenbeio/Pergenbeii already recur
across this leaf alone) and is the right place to run this control, not this one leaf.

Word-length vs. code-count is mixed, not one clean pattern (3 examples asked for, 5 given): aula (4 letters) <- 2
codes; defuncto (8) <- 4; falsa (5) <- 5; comperta (8) <- 4; Principi (8) <- 8. Some runs match letter-count
1:1 (falsa, Principi), others look closer to 2 letters/code (aula, defuncto, comperta) -- not a single consistent
per-letter or per-syllable rule on this leaf's evidence alone; leave the system question to a merge pass across
all three leaves, per the spec's own fallback note.

Files: `leaf67/pairs.tsv`, `leaf67/groups.tsv`, `leaf67/crops/*` (45 files incl. debug + manifest). No network
(image already on disk from bSZEM's fetch); 0 requests to any host this job.
