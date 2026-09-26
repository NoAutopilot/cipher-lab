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
