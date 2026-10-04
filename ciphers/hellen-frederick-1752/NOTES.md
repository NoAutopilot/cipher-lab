partial
Politische Correspondenz Friedrichs des Grossen vols. 9-10 (1752), 13 (1756) and 23 (1763) --
archive.org identifiers politischecorres09fred, politischecorres10fred (both full-text searched for
"Hellen" and fetched as djvu.txt and read directly by this worker, LANE CX2 25 Sept 2026, correcting
the earlier line-2 attribution to "a prior LANE N4 pass") plus vol. 13/23 djvu.txt already read
directly by a prior LANE CX2 pass -- cover all 8 target dates and print only Frederick's own outgoing
replies to Hellen, none marked dechiffrirt/entziffert/déchiffré, so the ciphertexts themselves are
letter absent in the one edition most likely to print a deciphered report from this correspondent.

## Check-solved (LANE CX2 worker CX2-FIX, 25 Sept 2026) -- own-read attribution fix, vols. 9-10

Line 2 previously attributed vols. 9-10's reading to "a prior LANE N4 pass" -- check-solved.md says a
citation to another source's read is not this worker's own read, so this pass opened both volumes
independently before writing anything.

1. Confirmed the archive.org identifiers directly: `archive.org/metadata/politischecorres09fred` and
   `.../politischecorres10fred` both resolve (title "Politische Correspondenz Friedrichs des Grossen",
   1879, Böhlau, Köln; a guessed `...freduoft` suffix for both, tried first, does not exist -- checked
   against an empty `{}` metadata response, not assumed).
2. `be-api.us.archive.org/fts/v1/search?q=Hellen&identifier=politischecorres09fred`: 1 hit, highlighted
   snippets reproduce the same five entries already on file ("Berlin, 8 janvier 1752", "Berlin, 22
   janvier 1752", "Potsdam, 8 février 1752", "Potsdam, 15 février 1752", plus an 18 August entry) --
   independently reproduced by this worker, not merely re-quoted. **Control**: the same query for
   "Podewils" (another minister named throughout this volume) also hits 1/1, confirming the search path
   itself works on this identifier.
3. Fetched `archive.org/download/politischecorres09fred/politischecorres09fred_djvu.txt` (1 request,
   1,478,571 bytes) and read entry 5273 in full on disk: "AU SECRÉTAIRE VON DER HELLEN A LA HAYE.
   Berlin, 8 janvier 1752. J'ai reçu votre rapport du 31 de décembre dernier..." -- Frederick
   acknowledging receipt of Hellen's 31 Dec report (the window immediately before R1953's 4 Jan 1752
   ciphertext), not a decipherment of it; grepped all 47 "Hellen" occurrences in the fetched text
   against "chiffr"/"dechiffr"/"entziffer": zero co-occurrences.
4. Vol. 10 (`politischecorres10fred`): same fts query, 1 hit, snippets span Oct 1753-Jan 1754 (a
   different correspondence window, outside this target's 1752/1756/1763 dates) -- read for
   completeness per this pass's brief, adds nothing for the 1752 date.

No change to the verdict (`open`, unchanged) or to any fact already on file -- this corrects only who
read vols. 9-10, per check-solved.md's rule that a citation to another worker's read does not satisfy
"read by this worker." Requests: archive.org/metadata 4 (2 guessed + 2 confirmed identifiers),
be-api.us.archive.org/fts 4 (Hellen x2, Podewils x1, plus one retry after a guessed-identifier 503),
archive.org/download 1, all >=1.5s apart.

## Check-solved (LANE CX2, 25 Sep 2026) -- re-check, extending the edition search to 1756 and 1763

This target already carries a full six-source sweep (24 Sept 2026, LANE N4 csNA) plus a duplicate-
collection recovery check (25 Sept, OX-HEL2), both kept intact below. Both are still current: DECODE
status, Bourdeau's and Aymeloglu's pages, and the NA Fagel inv. 5206 finding were not re-checked
today (nothing suggests any of them changed in the intervening day). This pass's job (per
`.claude/briefs/runs/2026-09-25-lane-cx2-nord.md`) was to extend the one gap the prior sweep left:
it read Politische Correspondenz vols. 9-10 for the **1752** letter (R1953) only, and never checked
the volumes covering the **1756** letter (R1049, 7 Sept) or the six **1763** letters (R1045-R1048,
R1060, R1061).

1. **Located the right volumes first, by full-text search rather than guessing from publication
   dates** (archive.org's own volume metadata gives no date range, only a Roman-numeral part
   number). Queried `be-api.us.archive.org/fts/v1/search?q=Hellen&identifier=<id>` across all 15
   Google-scanned `politischecorres09fred..182freduoft` volumes (9, 10, 11, 12, 13, 14, 15, 16,
   17, 18/1, 18/2, 19, 20, 21, 22) plus 23, 24 and 25: every volume from 9 through 23 shows
   "Hellen" hits with a dated snippet (e.g. vol. 13: "Potsdam, 3 juillet 1756" and "Haag ... 6
   août"; vol. 22: "11 aoüt 1762" and "3 Sep[tembre 1762]"; vol. 23: "Berlin, 16 avril 1763",
   "le 6 mai", "le 27 mai", "Haag 26 juillet"); vols. 24 and 25 return zero "Hellen" hits, so the
   correspondence with Hellen (or his successor) ends within vol. 23. **Vol. 13 is therefore the
   volume for the 7 Sept 1756 letter (R1049); vol. 23 is the volume for all six 1763 letters
   (R1045-R1048, R1060, R1061), which run 15 Apr-5 Jul 1763 -- exactly inside vol. 23's dated
   range of 16 Apr-26 Jul 1763.**
2. **Read vol. 13 and vol. 23 directly** (`archive.org/download/<id>/<id>_djvu.txt`, 2 requests,
   1 fetch each, then grepped and read on disk -- not re-fetched per request per the good-citizen
   rule). Grepped every "Hellen" occurrence (115 in vol. 13, matching count not separately logged
   for vol. 23) against "chiffr", "entziffer", "dechiffr" and "déchiffr" in the surrounding lines:
   the only "déchiffré"/"déchiffrée" hits in either volume (vol. 23, two occurrences) are in
   unrelated letters about a Rexin dispatch from Constantinople and a report from Vienna -- not
   near any Hellen passage. **No entry anywhere in vol. 13 or vol. 23 marks a Hellen report as
   deciphered; every dated entry near "Hellen" is either Frederick's own outgoing letter or an
   editorial footnote summarising what Hellen "berichtet" (reports), never a decoded text quoted
   in the edition.** This matches the pattern already established for vols. 9-10 (1752) by the
   prior pass, now confirmed to hold for 1756 and 1763 as well, and is consistent with Bourdeau's
   cited De Leeuw fact ("no Prussian codes broken between April 1757 and October 1763") -- though
   that citation alone did not cover the 7 Sept 1756 letter (R1049), which this pass's vol. 13
   read now separately clears.
3. Not re-run this pass (unchanged from 24-25 Sept, still current): DECODE listing (all 8 still
   Non-decrypted per the cached TSV), Bourdeau's `hellen1752.html`, Aymeloglu's repository grep,
   Tomokiyo's `dutch.htm`, and the NA Fagel inv. 5206 page-by-page finding (closed as a false lead
   for all 8 dates, per the 25 Sept correction below).

**Verdict stands `open`**, now with the full 1752-1763 span of the standard edition actually read
by a check-solved worker for every one of the 8 target dates, not only the 1752 one. Rule 10: no
novelty wording used above; this is a search result, not a verifier's classification.

Requests this pass: `be-api.us.archive.org` 18 (fts search, 15 volumes 9-22 plus 23/24/25, run as
one background batch, >=1.6s apart, no 429/403), `archive.org/download` 2 (vol. 13 and vol. 23
djvu.txt, full fetch then read from disk). No DECODE, no GitHub clones, no WebSearch this pass.

## Prior check-solved and recovery-lane passes (24-25 September 2026, kept intact below)

# W.B. von der Hellen to Frederick II of Prussia, 8 ciphertexts, 4 Jan 1752 – 5 Jul 1763

QUEUE row: CS2-18 (`sources/solver-diffs/2026-09-24-cyphersolver-site.tsv`, catalogue items 214/223 at
dbourdeau.github.io/cyphersolver/catalogue.html). Check-solved run 24 September 2026 by LANE N4 csNA
(session_01PKTy3iKiH3LzJpQauLb8Wu), brief `.claude/briefs/runs/2026-09-24-lane-n4-csNA.md`. State just flipped
copy-order -> copy-free by LANE N4 scARCH (ROOM.md, 24 Sept 2026 19:00 UTC): the strongest lead, NA Fagel inv.
5206, serves full-size images with no login.

## What it is

Eight intercepted despatch copies from W.B. von der Hellen, Prussian chargé at The Hague, to Frederick II,
held at KHA Prins Willem V inv. 196 and transcribed on DECODE as R1953 (4 Jan 1752), R1049 (7 Sept 1756), R1046
(15 Apr 1763, "related/supporting"), R1047 (29 Apr 1763), R1060 (6 May 1763), R1061 (13 May 1763), R1048
(20 May 1763) and R1045 (5 Jul 1763) — 6 of the 7 catalogue-numbered records are the 1763 cluster. All are
DECODE status "Non-decrypted" (`sources/decode/records-non-decrypted-2026-09-24.tsv`, ids 1953/1049/1061/1060/
1049/1046/1045 all present, none "Partially decrypted" or "Decrypted"; no hard filter applies here per LANE N2
addition (c)).

## Six-source search log (24 September 2026)

1. **Bourdeau, quoted verbatim** (`hellen1752.html`, posted 20 Sept, updated 24 Sept 2026 — same-day fresh):
   *"No key was recovered and no enciphered passage was decoded... An archive collection of deciphered letters
   offers a lead for 1752, but no matching decipherment has been retrieved."* His audit corrected transcription
   errors (stray question marks turned into definite digits, a duplicated three-line passage on R1953 image
   13448 wrongly deleted as a transcription artefact) but found no key. He names the same Fagel inv. 5206 lead
   this row is nominated on, and reports it as **not yet retrieved** as of his last update — this worker is the
   first to open the NA viewer for it (below).
2. **Standard printed edition — actually read.** *Politische Correspondenz Friedrichs des Großen*, vols. 9 and
   10 (Frederick's own outgoing letters, covering Jan 1752 onward), archive.org `politischecorres09fred` and
   `politischecorres10fred`, full-text searched (`be-api.us.archive.org/fts/v1/search?q=Hellen&identifier=...`)
   for "Hellen": **hits in vol. 9**, all headed "Au secrétaire von der Hellen à la Haye" — Frederick's own replies
   to Hellen, e.g. "Berlin, 8 janvier 1752", "Berlin, 22 janvier 1752", "Potsdam, 8 février 1752", "Potsdam,
   15 février 1752" (dates matching the window around R1953's 4 Jan 1752 report). **These are Frederick's
   outgoing side of the correspondence, not a decipherment of Hellen's incoming cipher reports, and no
   plaintext of the target ciphertexts is printed here** — letter absent. This corroborates, independently, what
   Bourdeau's page states in one sentence: "A search of the printed Politische Correspondenz found replies and
   contextual references, but no matching plaintext for these targets."
3. **DECODE** (`sources/decode/records-non-decrypted-2026-09-24.tsv`): all 8 records Non-decrypted, no key or
   attached decipherment document for any of them per the cached listing (no login used this pass).
4. **Aymeloglu** (fresh shallow clone, `unsolved-ciphers`, 24 Sept 2026): "Hellen"/"Fagel" appear only inside his
   raw DECODE catalogue scrape files (`catalogue/decode-records.jsonl`, `catalogue/decode-catalog.csv`), not in
   any of his 8 solved/attempted write-ups — not attempted there.
5. **Cryptiana / Tomokiyo** (`sources/cryptiana/web/dutch.htm`, decoded as Shift-JIS — the file is Japanese
   text, not mojibake): confirms the same episode Bourdeau cites via De Leeuw — in autumn 1751 the Dutch
   intercepted a letter to the newly arrived Prussian envoy "De Hellen" (デ・ヘレン), but the previous envoy
   D'Ammon's codebook had been updated in the meantime and England was asked to decipher it instead. No sentence
   in this page names a decipherment of the 1752–1763 letters specifically, and "Roell"/"Dedem" do not occur in
   it at all (relevant to CS2-21/-22 below).
6. **Web search**: nothing beyond Bourdeau's own page and the DECODE catalogue turned up.

## Archival lead: NA Fagel inv. 5206 (duplicate-collection check, Luzerne lesson)

Tested `https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/5206` (1 request, 24 Sept 2026):
`availability: DIGITALIZED`, **185 page scans**, unittitle "Van Von Hellen ('Sieur H'), Pruisisch
zaakgelastigde bij de Republiek, 1752-1753". The item sits inside toegang 1.10.29's finding-aid hierarchy under
the range 5204–5208, titled "Afschriften van ontcijferde brieven van vreemde gezanten hier te lande en elders
aan hun regeringen, bestemd voor de griffier Hendrik Fagel de Oude" ("copies of **deciphered** letters of
foreign envoys here and elsewhere to their governments, for the griffier Hendrik Fagel de Oude") — a genuine
decipherment series, not a raw-cipher one. Fetched the first scan's thumbnail
(`service.archief.nl/api/file/v1/thumb/61afd335-64a5-4282-bfd4-3388e3a09cf2`, 1 request): the page is continuous
cursive **clear French prose**, not cipher digits — image-confirmed as a decipherment, not a re-copy of the
cipher.

**This does not resolve CS2-18 by itself.** Inv. 5206's own unittitle date range is **1752–1753 only**. Of the
8 target ciphertexts, that window covers just R1953 (4 Jan 1752); the 1756 letter (R1049) and the six 1763
letters (R1045–R1048, R1060, R1061) fall outside it and are not addressed by this item. Bourdeau's page also
already flags a structural reason not to expect Prussian decipherments for the later cluster: citing De Leeuw,
"no Prussian codes broken between April 1757 and October 1763." **Whether inv. 5206's 185 pages include the
specific 4 January 1752 report matching R1953 has not been checked page-by-page here** (out of this brief's
scope — check-solved does not transcribe or align); that is a recovery-lane task once fetched.

## Verdict

**`open -- Politische Correspondenz Friedrichs des Großen vols. 9-10 (archive.org politischecorres09fred,
politischecorres10fred) full-text searched for "Hellen", letter absent (only Frederick's own outgoing replies
printed); Bourdeau's hellen1752.html (updated 24 Sept 2026) read in full, no key or decipherment recovered.`**
No source claims a decipherment of any of the 8 target ciphertexts. **Recovery-lane flag**: NA Fagel inv. 5206
(copy-free, 185 scans, image-confirmed clear-text decipherment series, 1752–1753) is a ready-to-fetch source for
R1953 specifically (4 Jan 1752), not for the 1756/1763 letters, which need a different Fagel or KHA inventory
covering those years (not identified this pass).

Grade counts: H 0, C 0, S 0, M 0, I 0 (nothing read here; check-solved does not decode). Rule 10: no novelty
claim made; this is a search result, not a verifier's classification.

Credit: D. Bourdeau, cyphersolver, https://dbourdeau.github.io/cyphersolver/hellen1752.html (catalogue items
214/223; transcription audit, De Leeuw citation, Fagel lead), CC BY 4.0 — prior attempt, not a solution.
S. Tomokiyo, cryptiana `dutch.htm` (De Leeuw episode, cited independently of Bourdeau from the local snapshot).

Requests this pass: `nationaalarchief.nl` 1, `service.archief.nl` 1, `archive.org`/`be-api.us.archive.org` 4
(2 advancedsearch, 2 fts search), `github.com` 2 shallow clones (dbourdeau/cyphersolver, aaymeloglu/
unsolved-ciphers, grep only), WebSearch 2. No DECODE login used.

## 25 September 2026: NA Fagel inv. 5206 checked page-by-page -- correction to the recovery-lane flag above

LANE OX worker OX-HEL (session_01CVGMSmAMAL3MFLp3mTVTJw) claimed this target at 02:01 UTC to do this check but
stalled on an AskUserQuestion call and pushed nothing (see ROOM.md); this is its successor, OX-HEL2
(session_01YZCsFUNEa1AuogYssdh82q).

**The finding-aid page for inv. 5206 embeds the complete scan list for all 185 scans in one HTTP response**
(Drupal's `drupal-settings-json` script tag carries `viewer.response`, itself a JSON string, with a `scans`
array giving `id` (file UUID), `label`, `order`, and `thumbnail`/`default`/`iiif` URLs for every one of the 185
pages) -- no pagination or per-scan API call was needed to get the full manifest. Saved verbatim as
`images/manifest_na5206.json`. All 185 thumbnails were then fetched to `images/thumbs/` (1 request each,
`service.archief.nl`, >=1.6 s apart). Thumbnails proved too small (169x256 to 256x204 px) to read the
handwritten item-number/date headers reliably, so 9 representative scans were also fetched at full resolution
(`images/full/`, same host, same pacing) and their top ~20% cropped for legibility (rule 2, image over
transcription): scan orders 1, 2, 3 (the opening of the volume), 30, 70, 110, 150 (spread through the middle),
and 183, 184 (the end, before the blank flyleaf at 185).

Every header read gives an item number ("No. 83", "No. 86", "Ad Relat. 26", etc.) and a date, all in French, all
headed "Lettre du Sieur H." (or a postscript "P.S. du Sieur H."):

| scan order | item no. | date |
|---|---|---|
| 1 | 83 | 24 October 1752 |
| 3 | 86 | 27 October 1752 |
| 30 | 98 | 8 December 1752 |
| 70 | 30 | 12 February 1753 (item counter has reset for the new year) |
| 110 | Ad Relat. 26 (a postscript, separately numbered) | 30 March 1753 |
| 150 | -- (mid-letter continuation page, no header) | -- |
| 183 | 59 | 24 July 1753 |
| 184 | -- (continuation of item 59) | -- |

The sequence is chronological throughout (item numbers climb through 1752, reset at the year boundary, and
climb again through 1753), and **scan order 1 -- the physically first page of the entire bound volume -- is
already dated 24 October 1752.** There is no scan before it in this inventory number. The volume runs through
at least 24 July 1753 (scan 183, two scans before the final blank flyleaf).

**Correction: NA Fagel inv. 5206 does not contain the 4 January 1752 despatch (R1953), and cannot** -- the
volume's own first page starts nine months later. It also cannot contain any of the other 7 target ciphertexts
(R1049, 7 Sept 1756; R1045-R1048/R1060/R1061, all 1763): none of those dates fall within 24 Oct 1752-24 Jul
1753 either. **This closes the recovery-lane flag written 24 Sept 2026** ("a ready-to-fetch source for R1953
specifically") -- it was written from the finding aid's unittitle date range ("1752-1753") without opening the
volume; opening it shows the Hellen sub-series here only starts in October. This is consistent with Tomokiyo's
`dutch.htm` account (search log item 5 above): Hellen was newly arrived and his cipher initially resisted
Dutch/English decipherment, so a plausible explanation is that this Fagel decrypted-letters series for Hellen
only begins once his traffic started being broken, several months after the 4 Jan 1752 letter was sent -- not
that the 1752 letter is filed elsewhere in this same box.

**Not further pursued, out of this brief's scope:** whether the *same* cipher system is used across inv. 5206's
run (Oct 1752-Jul 1753+) as in R1953 (4 Jan 1752) -- if so, one of these deciphered letters could still key the
1752 ciphertext by contemporary-system alignment (LESSONS.md's "sibling" pattern) even without matching dates.
That comparison needs the R1953 ciphertext image itself, which this brief did not fetch (see next section), and
is a job for a solver session, not this recovery check.

**R1953 ciphertext image location (this brief's step 3):** DECODE record R1953 is the only place this NOTES.md
names for the ciphertext image (`sources/decode/records-non-decrypted-2026-09-24.tsv`; status "Non-decrypted",
no attached decipherment). Per this brief, not logged in to check it directly. Context for whoever does: LANE DX's
login worker (ROOM.md, 25 Sept 2026 01:40 and 02:08 UTC) confirmed DECODE login now succeeds on the owner
account but every document and full-size image fetched across 5 other records (8725, 413, 4930, 1172, 1180) came
back as the same account-wide "Insufficient permissions" placeholder (ASKS row 1/42) -- R1953 itself was not
tried, but the block looks systemic rather than per-record. **owed: DECODE login worker (LANE DX)** to confirm
R1953 specifically once/if the permissions issue is resolved. KHA Prins Willem V inv. 196 (the primary holding
archive) was not checked this pass -- out of this brief's host scope (nationaalarchief.nl only).

Status stays `open`: this pass corrects a lead, it does not close the target and finds no decipherment.

Requests this pass: `nationaalarchief.nl` 6 (1 finding-aid page fetch for the full scan list + 5 sibling-inventory
page fetches to confirm 5204/5205/5207/5208 are each a *different* diplomat's whole file, not a chronological
continuation of 5206 -- ruling out that a Jan 1752 Hellen item sits in an adjacent inventory number instead),
`service.archief.nl` 194 (185 thumbnails + 9 full-resolution fetches), all >=1.6 s apart, one at a time, no
429/403 seen. No DECODE login used (per brief). No subagents used (thumbnails were too small to save a
sub-agent pass; the full-resolution header crops were read directly).

## ZX2-HEL: pool (25 Sept 2026, LANE ZX2)

Job: assemble the sign pool across the 8 despatches and write specs/hellen-frederick-1752.json (job brief
`.claude/briefs/runs/2026-09-25-lane-zx2-hel.md`). Intake gate: `python3 tools/intake_gate_check.py
hellen-frederick-1752` -> `hellen-frederick-1752: open (line 1) -- edition/page or full-text-search citation
found within 6 lines`, exit 0.

**1. Ciphertext recovered from Bourdeau (dbourdeau/cyphersolver), credited, text CC BY 4.0.** DECODE images
for all 8 records remain account-blocked in this environment (ASKS row 1/42; not logged in, per brief). His
`hellen1752/` folder does not distribute the raw manuscript images or DECODE `DOC_*.txt` transcriptions ("not
distributed in this publication", his NOTES.md), but does publish `audit/R1953.txt`, `audit/R1049.txt` and
`audit/set1763.txt` (his own 20 Sept 2026 conservative re-parse, `audit_transcription.py`, which -- unlike his
earlier `parse.py` -- keeps uncertain digits, underlines/carets and cipher adjacent to cleartext tags rather
than discarding them; see his `AUDIT_2026-09-20.md`). `set1763.txt` is six lines in the fixed order his own
script writes them (`audit_transcription.py`'s tuple `('1045','1046','1047','1048','1060','1061')`), split back
into per-record files here and verified byte-for-byte against his `audit/summary.json` segment counts (all 8
match exactly: 383/218/199/191/516/136/162/846). Copied into this repo as `ciphertext_R<id>.txt` (8 files) plus
`bourdeau_audit_summary.json` (his summary, for reference). These are **his transcriber-uncertainty-preserving
audit projections, not a finished transcription** (his own wording) -- a future worker doing cryptanalysis
proper should still get the manuscript image once DECODE access is resolved (rule 2, image over transcription);
this pool assembly is a structural pass, not a claimed reading.

Credit: D. Bourdeau, cyphersolver, `hellen1752/` folder (`audit_transcription.py`, `AUDIT_2026-09-20.md`,
`audit/*`), CC BY 4.0 text, MIT code (not copied here, only the audit-projection ciphertext files themselves).
His own outcome: `class: "not read"`, `fraction_read: 0` -- prior attempt, not a solution. His `profile.json`
also records: literature search failed (Politische Correspondenz 9/13/22/23, de Leeuw thesis, Tomokiyo, all
already independently re-confirmed by this repository's own CX2 check-solved passes above); one-part
alphabetical-code hypothesis tested and failed (density correlation -0.25 to 0.34 against period French word
lists); sibling-key lead R2824 (Fagel 5345, 1746, a 23-page cipher key) identified then **rejected** -- the full
public DECODE record identifies it as Baron van Reede's key for the Dutch mission *to* Prussia, not a Prussian
chancery key of Hellen's own. This rejection was not previously on file in this repository; recorded here.

**2. `tools/decode_list.py` metadata: reused the existing cached listing rather than re-fetching** (good-citizen
rule -- fetch once, read from disk after; `sources/decode/records-non-decrypted-2026-09-24.tsv` already covers
all 8 record IDs from a prior pass). All 8 confirmed Non-decrypted, Cipher type, same shelfmark family (KHA A31
PWV inv.196), with `number_of_pages` per record: R1953=3, R1049=3, R1045=1, R1046=2, R1047=1, R1048=2, R1060=2,
R1061=4. No new DECODE requests made this pass.

**3. Structural stats and one-key pool test** (`ciphers/hellen-frederick-1752/pool_stats.py`, output in
`pool_stats_output.json`): per-record token/distinct/range/digit-width stats (see spec's `ciphertext` block for
the numbers, not repeated here). **Cross-family test**: Jaccard of numeric type-sets between the three date
groups is low throughout -- 1752 vs 1756 0.1311, 1752 vs 1763-pooled 0.0846, 1756 vs 1763-pooled 0.0803 --
independently reproducing Bourdeau's own repeated-bigram finding of three separate codes by a different
statistic. **1763-cluster one-key test** (the pools-first question): real cross-record mean pairwise Jaccard
across the six 1763 despatches is 0.1456; a control of 200 random re-splits of the same pooled 1234-token
stream into six groups of the same sizes (seed 20260925) gives mean 0.1372, range 0.1241-0.1522, with only 8%
of control trials scoring higher than the real split. The real value is **not distinguishable from a random
partition of one shared vocabulary** -- consistent with (not proof of) the six 1763 despatches sharing one
code. This does not rule out two very similar but distinct codebooks; it is a structural screen, not a key
recovery. Grade: S (cryptanalytic result with a control), not a reading.

**4. Pool size**: the 1763 cluster alone is 1,289 segments (1,234 numeric) across 6 despatches -- just under
the CLAUDE.md pools-first >=2,000-sign threshold. All 8 despatches pooled (including the two isolated,
below-threshold 1752 and 1756 singletons, which the cross-family test above shows do NOT share the 1763 code)
total 2,651 segments, but that combined figure is not a meaningful "one key" pool given result 3 -- it is three
separate, much smaller pools (846 / 516 / 1,289).

**5. NA Fagel inv. 5206 stray-numeral check** (job brief step 3): re-viewed all 9 full-resolution scans already
on disk (`images/full/001,002,003,030,070,110,150,183,184.jpg`, fetched by the 25 Sept OX-HEL2 pass) at full
size, not just the top-crop date headers previously read. All 9 are continuous clear French prose throughout;
**no cipher numerals, code groups, half-deciphered words or marginal digits anywhere on any of the 9 scans.**
No new fetch needed (per brief's <=10-request allowance, 0 used). This is consistent with, and adds direct
image confirmation to, the already-established finding that this series (24 Oct 1752-24 Jul 1753+) falls
outside all 8 target dates and is closed as a false lead.

**Spec written**: `specs/hellen-frederick-1752.json` -- ciphertext pointers (8 files), alphabet, constraints
(design, prior attempts, check-solved verdict), cheap tests in order (pool test done as test 1; homophonic
anneal on the 1763 pool as test 2, gated on an era-matched French corpus), judge block. **Judge block flag**:
`tools/judge_plaintext.py`'s only wired `fr` corpus is `fr16` (16th-century, Catherine de Medici's letters) --
not era-matched to this 1752-1763 target, per CLAUDE.md's pt17-vs-pt18 lesson. LANE ZX2 worker ZX2-FR18 is
building an era-matched corpus concurrently (per ROOM.md 19:16); noted in the spec's `judge.note` so a future
judge run does not trust a FAIL/PASS against fr16 uncritically.

**Not done, out of this brief's scope**: the homophonic anneal itself (test 2, needs fr18); a second sweep for
1752/1756 siblings elsewhere in KHA/BnF holdings (only the printed edition and DECODE were checked, both
already covered by check-solved); reading the original DECODE cleartext-interspersed transcription (account-
blocked).

Grade counts this pass: H 0, C 0, S 4 (cross-family Jaccard x3, cluster one-key test), M 0, I 0. Rule 10: no
novelty wording used; this is a search/structural result, not a verifier's classification.

Requests this pass: `github.com` 1 shallow clone (dbourdeau/cyphersolver, deleted from the scratchpad after
grep and file extraction), no other hosts (decode_list.py metadata reused from disk, NA Fagel images already
on disk). No subagents used.

## Web and blog check (WEBCHECK-hellen-frederick-1752, 1 Oct 2026)

Run 1 Oct 2026, 23:35-23:4x UTC (clock read), by WEBCHECK-hellen-frederick-1752 (account-4, Fable 5.1), per
`.claude/briefs/check-solved.md` "Required step: Open web and blog comment threads" (CHECK-SOLVED-WEB, 28 Sept 2026)
and `.claude/briefs/runs/2026-10-01-account4-webcheck.md`. All eight ciphertext files are numeric only (no clear word
in any of them, checked by grep), so the "distinctive phrase" query used a quoted run of the first four groups of
R1953 plus the DECODE record id instead of a clear-text phrase. Search engine: the session's web-search tool
(US index); blog site searches were run twice each, once domain-restricted in the search engine and once through the
blog's own search page. Every hit judged plausible was opened and its comment thread read (or its absence noted).

**(a) Plain web searches (7, plus the model-solve query):**

| # | Query | Result |
|---|---|---|
| a1 | `"von der Hellen" Frederick 1752 cipher Hague intercepted` | 10 links; only dbourdeau.github.io/cyphersolver/index.html concerns this item (opened, below); the rest are Wikipedia pages (Blencowe, Jaupain, d'Alonne, Copiale, Prussian invasion of Holland 1787) and HistoCrypt 2018 proceedings, none about Hellen. |
| a2 | `"Prins Willem V" "inv. 196" OR "inv.nr. 196" Hellen Chiffre OR cipher OR cijfer` (shelfmark + cipher word) | 10 links, all generic (Vigenère pages, William V's picture gallery); nothing on KHA Prins Willem V inv. 196 or Hellen. |
| a3 | `"1208 1049 820 578" OR "Hellen" DECODE R1953 cipher Frederick` (distinctive ciphertext run + record id) | 9 links; only Bourdeau's index page concerns the item; the rest are cipher-tool sites and Wikipedia year pages. |
| a4 | `Hellen Frederick II 1752 1763 ciphered despatches The Hague Prussian envoy decipherment` (the folder's descriptive title) | 10 links; Bourdeau's index page again; H.M. Scott 1977 (Russo-Prussian alliance), Klawitter 2026 in *Historical Research* (opened, below), Wikipedia (Thulemeyer, Keith, Mitchell, Lucchesini). |
| a5 | `"Hellen" "Friedrich" Gesandter Haag 1752 Chiffre entziffert OR Geheimschrift OR Dechiffrierung` (German) | 9 links, all generic Geheimschrift pages (Zeno Meyers 1905, Wikisource, Wikipedia); nothing on Hellen. |
| a6 | `"de Hellen" OR "von der Hellen" Lyonet Fagel onderschepte brieven Pruisen cijferschrift 1752` (Dutch) | 9 links: De Leeuw 1995 on DBNL (opened, below), NA finding aids 3.01.19 / 1.10.29 / 1.10.102 (the Fagel 1.10.29 aid is already worked through above, inv. 5206), Wikipedia for two unrelated van der Hellens, a Taco Tichelaar blog post on Frederick II (opened, below), the Thomassen 2009 UvA thesis chapter (opened, below), an Open Archieven Staten-Generaal transcription of 17 Mar 1706 (opened, below). |
| a7 | `"Hellen" Prussian chargé OR secretary Hague 1763 Frederick letters intercepted deciphered Lyonet OR "Zwarte Kamer" OR "black chamber"` | 10 links: De Leeuw 2000 thesis chapter on the War of the Spanish Succession black chamber (opened, below), SPK-Magazin interview "Many dispatches have still not been deciphered" (opened, below), Bourdeau's index page, Carlyle's *Friedrich II* vol. VII on Gutenberg, Wikipedia/Cipher Museum pages on cabinets noirs. |
| a8 | `Hellen Frederick 1752 cipher solves OR solved Claude OR GPT OR ChatGPT` (model-solve announcements) | 9 links: Schneier "Claude Fable Solves a Historical Cipher" (Sept 2026) and 36kr "Claude AI Solves 370-Year-Old Unsolved Ciphertext" (both opened, below: the Cyphral Distich, Urquhart 1653, not this item); HN "GPT-6 Astra Solves a WWI German Radio Cipher" (a WWI radio cipher by its title, not opened); a Kryptos K4 gist; Bourdeau's index page; two arXiv papers on LLM cipher reasoning. No announcement names Hellen or this correspondence. |

A further domain-restricted query over the three blogs plus github.com (`"Hellen" Frederick Prussia intercepted letters
1752 Hague cipher unsolved DECODE`) returned only unrelated GitHub repositories and Cipher Mysteries archive pages
(Blitz Ciphers, Zodiac, Ferdinand III posts on Cipherbrain); the same query with reddit.com added was refused by the
search tool (reddit.com is not accessible to its crawler), so Reddit is **not covered** by this check.

**(b) Blog site searches (two routes each):**

| Blog | Route 1: search engine, domain-restricted | Route 2: the blog's own search page | Result |
|---|---|---|---|
| Cipherbrain (scienceblogs.de/klausis-krypto-kolumne) | `Hellen Friedrich Preußen Chiffre 1752 Haag` -> 10 posts (Bernotat PDF, an Adelige's Nachlass 2016, Catinat 2016, Utah war, Freimaurer medal 2014, Bonn Stadtarchiv 2015, Ferdinand III 2014, antique-clock note 2022, book cipher 2013), none on Hellen or The Hague | `?s=Hellen` -> 6 posts (yellow laser dots 2022, Goldene Alice 2021, Verkehrsschild 2021, Kryptos/Fenn 2021, Freimaurer inscriptions 2021, typewriter postcard 2019): "Hellen" matches only as a substring; `?s=Friedrich+der+Große+Haag` -> "Wir konnten leider keine Beiträge finden" | no post on this item; no comment thread to read |
| Cryptiana blog (cryptiana.blogspot.com) and Tomokiyo's cryptiana.web.fc2.com | `Hellen Frederick Prussia Hague cipher 1752` restricted to both hosts -> no links | `/search?q=Hellen` -> "No posts matching the query: Hellen"; `/search?q=Prussia` -> one post, "Frederick I of Prussia's Transposition Cipher" (25 Oct 2024), Frederick I not II, transposition not this nomenclator, not opened further. On-disk snapshot `sources/cryptiana/` grepped for "Hellen" (0 requests): `charlesi.htm` (a pseudonym "Hellen" in a 1640s English letter, unrelated) and `dutch.htm` (Tomokiyo's Japanese digest of De Leeuw, p.25: in autumn 1751 a letter addressed to the newly arrived Prussian envoy De Hellen was seized; D'Ammon's codebook obtained that summer had apparently been renewed and did not serve directly, so England was asked to decipher it -- a cipher-family fact already cited above via `dutch.htm`, concerning a letter *to* Hellen in 1751, not any of the eight 1752-1763 despatches *from* him; no plaintext printed) | no post on this item |
| Cipher Mysteries (ciphermysteries.com) | `Hellen Frederick Prussia Hague cipher 1752 1763` -> 3 Cipher Mysteries posts (van Heeck 2016, d'Agapeyeff 2008, Voynich page), none relevant | `?s=Hellen` -> 3 posts (shorthand marginalia challenge 2014, Filelfo 1465, Alberti c.1465), substring matches only; `?s=Frederick+the+Great+Prussia` -> "Nothing Found" | no post on this item |

**(c) Hits opened and read, with comment threads:**

1. https://dbourdeau.github.io/cyphersolver/hellen1752.html (posted 20 Sept 2026, "Last updated: 24 September 2026", status "not solved"): "No key was recovered and no enciphered passage was decoded." and "None of the enciphered passages was decoded. No plaintext value has been verified." No comment thread on the page. Links out to NA 1.10.29 inv. 5206 (already checked page-by-page above, 25 Sept 2026), the GitHub working record `targets/hellen1752`, and De Leeuw's dissertation. The only hit anywhere in this check that is about this item.
2. https://www.schneier.com/blog/archives/2026/09/claude-fable-solves-a-historical-cipher.html -- the Cyphral Distich (Urquhart 1653); 13 comments read, none mention Hellen, Frederick II, Prussia, The Hague, 1752/1763 or DECODE R1953/R1049.
3. https://eu.36kr.com/en/p/3984219694856961 -- same Cyphral Distich story; no mention of this item.
4. Klawitter, "The diplomatic correspondence between Heinrich Friedrich Diez ... and Christian Konrad Wilhelm Dohm: its decipherment and historical relevance", *Historical Research* 99 (2026) 338-348 (OUP PDF via its silverchair redirect, text extracted locally with pdftotext, 44,912 chars): Diez at Constantinople 1784; 0 occurrences of "Hellen", 0 of "Lyonet".
5. Karl de Leeuw, "Een lexicaal geheimschrift van Wilhelmina van Pruisen op Hampton Court", *De Achttiende Eeuw* 1995 (DBNL): no "Hellen"; states "In 1751 en 1752 slaagde Lyonet er inderdaad in, enkele Pruisische en Franse codes te breken" (n.18) and reproduces as Afb. 1 "K.H.A., Stadhouder Willem V, inv. nr. 198, onderschepte brief van de Pruisische ambassadeur te Londen van 22 september 1752, met oplossing door Lyonet" -- a different letter (the London envoy, inv. 198, not inv. 196) and an image, not a printed plaintext of any Hellen despatch. No comments. **Lead for the folder, not a decipherment of this item:** inv. 198 carries a Lyonet-solved Prussian intercept of Sept 1752, nine months after R1953; whether it is the same Prussian code is a cheap check once the R1953 image is in hand.
6. https://tacotichelaar.nl/wordpress/frederik-ii-van-pruisen-de-filosoof-en-valsemunter/ -- Frederick II biography/coinage post; no Hellen, Lyonet, Zwarte Kamer or intercepts; no visible comment section.
7. Thomassen, *Instrumenten van de macht. De Staten-Generaal en hun archieven 1576-1796* (UvA 2009, chapter PDF, 101,821 chars extracted locally): 0 "Hellen", 0 "Lyonet".
8. De Leeuw, *Cryptology and statecraft in the Dutch Republic* (UvA 2000), chapter "The Black Chamber in the Dutch Republic during the War of the Spanish Succession" (PDF, 82,952 chars extracted locally): 0 "Hellen", 0 "Lyonet" (the chapter covers 1702-1713).
9. https://www.spkmagazin.de/en/many-dispatches-have-still-not-been-deciphered.html -- interview with Franziska Mücke (GStA PK) on Lucchesini's and Humboldt's ciphered dispatches and a 1729 dispatch with a lost key; no Hellen, The Hague, 1752 or 1763; no comment thread.
10. https://www.openarchieven.nl/transcripties/toon/NL-HaNA_1.01.02_3358_0400 -- Staten-Generaal resolution of 17 Mar 1706 (a Cleves guardianship petition naming the King of Prussia); unrelated.
11. dbourdeau.github.io/cyphersolver/index.html (the index row behind hits a1/a3/a4/a7/a8): "Hellen to Frederick II, 1752-1763 -- not solved; transcription audited, archival lead identified; Fagel 5206 may supply a parallel decipherment for 1752" (the search tool's rendering of the row; the per-target page in hit 1 is the authority and says no passage was decoded).

**Result:** no decipherment or plaintext of this item located by these queries on 1 Oct 2026 (a search result, never a
novelty verdict, rule 10). Status word unchanged (`open`). Not covered: Reddit (search tool cannot crawl it) and
any comment thread behind a login. Requests per host, all one at a time: scienceblogs.de 2, cryptiana.blogspot.com 2,
ciphermysteries.com 2, dbourdeau.github.io 1, schneier.com 1, eu.36kr.com 1, academic.oup.com 1 + watermark02.silverchair.com 1,
dbnl.org 1, tacotichelaar.nl 1, pure.uva.nl 2, spkmagazin.de 1, openarchieven.nl 1; search-engine queries 12 (one refused
for the reddit.com domain); sources/cryptiana on disk 0. No 403, 429 or challenge page met.

Intake gate re-run after this section (output pasted verbatim):

```
hellen-frederick-1752: open (line 1) -- edition/page or full-text-search citation found within 6 lines
$ python3 tools/intake_gate_check.py hellen-frederick-1752 ; echo exit=$?   -> exit=0
```

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/targets/hellen1752/NOTES.md ; https://dbourdeau.github.io/cyphersolver/hellen1752.html
- Their extent, in their words: in progress: no cipher plaintext or key verified
- Their date: 20 Sept 2026
- Note: already cited in our NOTES.md
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## HEL-T2 (2 Oct 2026, account-4): spec test 2 -- homophonic and nomenclator anneals on the pooled 1763 cluster, both controls below gate (non-tests, not negatives)

Job brief `.claude/briefs/runs/2026-10-01-account4-hel-t2.md` (Fable 5.1, disk only, no network, no vision). Box
00:14-00:54 UTC; both families ran well inside it (homophonic battery 12 s; nomenclator 6 m 51 s per seed).

Intake gate, run before anything else (CLAUDE.md pipeline item 2): `python3 tools/intake_gate_check.py
hellen-frederick-1752` -> `hellen-frederick-1752: open (line 1) -- edition/page or full-text-search citation found
within 6 lines`, exit 0 (00:14 UTC, after WEBCHECK-hellen-frederick-1752's web and blog check above).

**Pooled stream.** The spec's `ciphertext` block is a dict of per-record pointers, which `tools/family_run.py` cannot
read ("give --cipher PATH"), so `pool_1763.py` (beside this file) writes `pooled_1763.txt`: the six 1763 records in
Bourdeau's audit order (1045, 1046, 1047, 1048, 1060, 1061), one record per line, numeric tokens only (1-4 digits
after stripping the `_`/`^` transcriber marks; `?` tokens dropped -- the same rule as `pool_stats.py`). It exits
non-zero if the count drifts from the spec's 1234. Result: N=1234, K=634 distinct values (364/206/192/188/134/150
per record); 411 of the 634 values are singletons and the commonest (902) occurs 18 times, so the stream carries
about 1.9 tokens per sign type.

**Family 1, homophonic (the spec's named test 2).** `tools/family_run.py specs/hellen-frederick-1752.json --family
homophonic --param profile=target --seeds 3 --corpus tools/data/fr18 --cipher ciphers/hellen-frederick-1752/pooled_1763.txt
--tokens space` (restarts 8, default). The control is a window of fr18 (French official prose 1680-1790, the spec's
own judge corpus; fr16 was not used, per the spec's judge note) enciphered at N=1234 with the target's own
sign-count profile and solved blind:

| seed | realised control K | recovery |
|---|---|---|
| 1 | 479 | 0.113 |
| 2 | 455 | 0.090 |
| 3 | 471 | 0.096 |

Mean 0.100 (0.090-0.113) against the 0.6 gate: CONTROL BELOW GATE, exit 3, **target not run**. The realised control
K is below the target's 634 (singleton buckets drawn by weight are not all used), so the control is if anything
easier than the target, which only strengthens the reading of this as a non-test.

**Family 2, nomenclator (the brief's named next instrument).** `--family nomenclator --restarts 3 --param sweeps=30
--param phase1=20` (ARM-C1's settings, 26 Sept 2026; holdout index 5 = the Maintenon volume held out of the trigram
LM), run as two single-seed calls because one seed costs about 7 minutes: seed 1 recovery 0.092 (control build:
1234 coded tokens, 363 distinct values of which 308 book and 55 particle, 247 OOV words, 217 wild tokens, 595
particle tokens); seed 2 recovery 0.109 (378 distinct, 322 book / 56 particle). Mean 0.100 (0.092-0.109) against
the 0.6 gate: CONTROL BELOW GATE, exit 3, **target not run**. This family is built for the Armstrong two-level
decade/slot design with an English (`tools/data/uscodes-1800`) book prior, neither of which this French target is
known to share; it was run as the nearest instrument on file, not as a design claim.

**Judge:** not run -- no target decode exists for it to score (rule 3: the judge gates a decode, and neither family
cleared its control). No `--shuffle-target` run either, for the same reason.

**Reading of the result (rule 3, rule 5).** Two control-backed non-tests, not a negative on the target: a solver that
reads 9-11 percent of its own matched design says nothing about what the Hellen 1763 code is. This is the BER-HOMO
shape (27 Sept 2026, berthier-napoleon-1812, N=325/K=207, control 0.061) at a larger N and a larger K: at 1.9
tokens per sign type neither anneal has power. Status stays `open`. The design question stands where Bourdeau's
profile.json left it (two-part code, flat code-group frequencies).

**Named next step.** Not a third family at this N (a repeat of the same approach with one knob changed is the
RETRO-2026-09-26f shape CLAUDE.md rule 3 warns against). The pool has to grow or a known text has to arrive: more
1763 Hellen despatches (KHA inv. 196 beyond these six, or a Fagel-series copy), a period key or decipherment, or a
printed Politische Correspondenz text matching one of the six dates (check-solved above found none for 15 Apr-5 Jul
1763). The spec's `cheap_test_done["2"]` carries the same numbers and the same next step.

Grade counts this pass: H 0, C 0, S 0 readings (two control-backed non-tests), M 0, I 0. Rule 10: nothing claimed.
Files: `pool_1763.py`, `pooled_1763.txt`, `HYPOTHESES.md` (three tool-written rows), `specs/hellen-frederick-1752.json`
(`cheap_test_done["2"]`), this section. No `families/` decode files were written (no target run). Requests: none
(disk only). Subagents: none.

## Premise check (GF4-BATCH2, account-4, 2 Oct 2026)

Adversarial pass per `.claude/briefs/check-solved.md` "Premise check": asked to prove the eight despatches are
already read. Result first: **not found** -- no decipherment, clear copy or printed plaintext of any of the eight
target despatches located by (a)-(d) below on 2 Oct 2026 (a search result, rule 10). Status stays `open`. Two
leads for the folder (neither a decipherment of this item) are in (c) and (d).

**(a) Decipherments the folder itself mentions -- not found (each opened or already opened and re-read here).**
NA Fagel 1.10.29 inv. 5206 ("copies of deciphered letters", Bourdeau's lead): all 185 scans were opened
page-by-page on 25 Sept 2026 (section above) and do not contain the 4 Jan 1752 despatch; re-read the section,
nothing to add. De Leeuw 1995 Afb. 1 (KHA PWV inv. 198, Lyonet's solution of a Prussian London intercept of
22 Sept 1752): a different letter and envoy (Michell, London), see (c). Politische Correspondenz vols. 9, 10, 13,
23: Frederick's outgoing replies only, already read on disk (sections above). DECODE: R1046, R1060 and R1061 carry
"Plaintext: French" in the catalogue language field (Aymeloglu's scrape of the DECODE catalogue,
`catalogue/decode-catalog.csv`, read 2 Oct 2026) -- but all eight read status "Non-decrypted" in the same row, so
the field is a language tag, not an attached decipherment; the documents themselves sit behind the DECODE
permissions block (ASKS row 1/42), not opened.

**(b) Other solvers' working files -- not found.** Fresh shallow clone of dbourdeau/cyphersolver (2 Oct 2026):
`targets/hellen1752/` holds only `NOTES.md`, `AUDIT_2026-09-20.md`, `audit_transcription.py`, `profile.json` and
`audit/{R1049,R1953,set1763,summary}.txt|json`; no key file, no apply-key script, no rendering; `profile.json`
gives `plaintext.location: ["none"]` for R1953; his AUDIT says "No long coherent plaintext has been recovered under
any model" and rejects DECODE R2824 (Fagel 5345, "cipher Prussia 1746") as a Dutch, not Prussian, key. Fresh shallow
clone of aaymeloglu/unsolved-ciphers: "Hellen" occurs only in the two catalogue scrape files, no script, key or
output touches these records (grep, no code copied; rule 8).

**(c) Physical neighbours -- not found for the item; one sibling lead.** No page images of KHA inv. 196 are
reachable (DECODE images blocked; KHA's own catalogue, below, shows no scans), so the facing pages and laid-in slips
cannot be viewed from here: **unreachable** for the leaves themselves. Neighbouring records in the same Lyonet
intercept series, from the DECODE catalogue scrape: **R1051** (Michell, Prussian envoy London, to Frederick II,
12 Nov 1751) and **R1050** (Michell to Frederick II, 5 Sept 1752), both KHA PWV inv. 198, status **"Decrypted"**,
Plaintext French -- Prussian chancery cipher solved by the Dutch in the same months as R1953 (4 Jan 1752); and
R1955/R1957 (Frederick to Michell, 28 Dec 1751), Non-decrypted on DECODE but printed in clear in PC vol. 8 no. 5263
(QUEUE.md line 1489). Whether Michell's 1751-52 code is the one Hellen used is untested; it is a **key-sibling lead,
not a decipherment of this item** (envoys normally held different codes; Bourdeau's repeated-bigram audit and the
folder's own Jaccard test show the 1752, 1756 and 1763 Hellen sets are three different codes). KHA catalogue
(koninklijkeverzamelingen.nl, archiefvormer Willem V, `zoekterm=Hellen`, headless browser, 4 requests): 3 hits,
**A31-1148-1149** "Briefwisseling van de zaakgelastigde W.B. von der Hellen, 1751-1757 en 1763. Afschriften, ten
dele in tweevoud" (2 pakken: A31-1148 1751-1755, A31-1149 1756-1763) -- the target's own holding under its current
number; no scan count on any of the three nodes (by the convention QUEUE.md records for this viewer, not digitised).
Its neighbour A31-1154-1171 "Briefwisseling van F.W. von Thulemeyer ... 1763-1783 en 1786. Afschriften, ten dele in cijfer"
(Hellen's successor at The Hague) is the next series on the same shelf, likewise without scans.

**(d) Recipient side -- not found for the eight dates; one adjacent print.** The recipient is Frederick II; his
edition (Politische Correspondenz) prints only his outgoing letters plus editorial summaries ("Hellen berichtet,
Haag 26. Juli [1763]", Google Books API snippet, vol. 23, 1896, full view; already read on disk). Google Books API
(country=US, keyed), 3 queries: `"von der Hellen" Haag 1763 Bericht` (14 hits: PC vols., a 2009 Prussian
officials handbook, and a 2025 edition of a Saint-Germain biography whose snippet says "Berichte des preußischen
Geschäftsträgers von der Hellen ... sind dem Geheimen Staatsarchiv in Berlin entnommen"), `"Hellen" "Haye" 1752
rapport déchiffré` (0), `"von der Hellen" Gesandter Haag Friedrich dechiffriert` (0). The Saint-Germain print quotes
Hellen's GStA reports of the 1760 Saint-Germain affair -- outside all eight target dates (1752, 1756, 1763), but it
shows the decoded receiving-side reports exist in GStA PK and have been printed in part; for the eight target dates
no print of them was found. OpenAlex (`"von der Hellen" Prussia Hague`): 1 hit, unrelated. The Dutch intercepting
side (Fagel 5206, De Leeuw) is covered in (a).

Requests this pass: koninklijkeverzamelingen.nl 4 (1 curl, 3 browser), googleapis 3, api.openalex.org 1,
github.com 2 shallow clones (grep only); all >=1.5 s apart; no 403/429/challenge. Nothing read, graded or tested.

## First cheap test: Michell sibling key (FT4-hellen-frederick-1752, account-4, 3 Oct 2026)

Lead from the Premise check (c). **What R1050/R1051 hold:** login-free metadata (cached listing
`sources/decode/records-decrypted-2026-09-24.tsv`, no fresh listing call): both "Decrypted", Cipher, KHA PWV inv. 198,
French, R1050 2 pp. (Michell to Frederick II, London 28 Aug/8 Sept 1752), R1051 1 p. (1/12 Nov 1751). After one browser
login: each has one document, DECODE's transcription (transcriber "XZ", March 2020) of the 4-digit code lines with the
period Dutch decipherer's interlinear French over them, and full-size page images (3, served at 5472x3648, not
committed; sha1s in `sibling_michell/README.md`). No key sheet: the key is the glosses themselves.
Built `sibling_michell/key_sibling.tsv` (268 codes, 14 with conflicting glosses; `build_key.py --check`), grade S.

**Overlap first:** ranges overlap (Michell 2-~3600; Hellen 1752 up to ~1650, 1756 up to ~3100, 1763 up to ~3900), so the
test ran. **Test vs control** (`sibling_michell/test_sibling.py`, table in HYPOTHESES.md): mean fr18 word log-prob of the
decoded covered tokens vs 200 value-shuffled keys. R1953: real -9.641 vs shuffle mean -9.367, p=0.695 (98/836 covered);
the other seven p 0.050-0.480. Positive control (R1050-only key on R1051): -5.735 vs -9.236, p=0.000, and power 0.99-1.00
at every target's covered count. **The Michell 1751-52 code is not Hellen's code** for any of the eight letters
(control-backed; conditional on DECODE's transcriptions, rule 2). Supporting: 37% of Michell's glossed tokens are above
1732, R1953 has 1 of 836 there; Michell's half-code mark (40½ la) is absent from every Hellen transcription.
`decode_key.py ciphers/hellen-frederick-1752/sibling_michell --check` passes (the sibling decode is kept as the negative's
reproduction, not a reading: H 0, C 0, S 96, M 3, U 747). No reading claimed; status stays `open`.

Requests: de-crypt.org 13 after one login (record 1050, 1051, DocumentsList x2, ImagesList x2, 2 documents, 3 thumbnails,
3 full-size images), 1.6 s apart, no challenge; account name not in any saved file. Vision calls 0.
Next suggestion (not run): other Prussian chancery sibling keys of 1751-56 with a code range near 1-1650 (DECODE key
records, GStA PK); the folder's 1763 cluster (range to ~3900) is the one a Michell-sized code could still fit, and it tested negative here.

## FT4b: other Prussian sibling keys 1751-56 (FT4b-hellen-frederick-1752, account-4, 3 Oct 2026)

Step run: the FT4 "Next suggestion": other Prussian chancery keys of 1751-56 with a code range near 1-1650.

**What was listed.** I used the cached login-free DECODE key listing (`sources/decode/keys-all-2026-09-28-merged.tsv`, 6,324
Key rows, plus `keys-na-p58-2026-10-02.tsv`; no fresh `decode_list.py` call) and Aymeloglu's DECODE catalogue scrape
(`catalogue/decode-catalog.csv`, 10,106 rows, which has the sender/region field the listing lacks; shallow clone,
grep only, no code copied; rule 8). There are 392 Key records dated 1740-1765. By holder/sender: the only rows
naming Prussia or Berlin outside one BL volume are R2824 (Fagel 5345, 1746: Bourdeau rejected it as van Reede's
Dutch key for the mission *to* Prussia) and Dresden R2332/R2429 (Saxon Dresden-Berlin keys of 1764-77, the wrong
chancery and dates). **BL Add MS 32276 is the English Deciphering Branch's Prussian key volume** (DECODE region
notes "Berlin", "Potzdam", "Prufsia"). It has 66 Key records running from 1722 to 1794, all N/A, mostly 2 pp. Those
inside or next to the target dates:
1751 R4369 (f.44), R4370 (f.46), R4373 (f.50); 1752 R4374 (f.52), R4380 (f.64); 1754 R4376 (f.56); 1756 R4377
(f.58, Potzdam), R4378 (f.60), R4379 (f.62, Potzdam); 1761-62 R4381-R4385; 1764-65 R4387, R4389-R4391. In the other
Deciphering Branch volumes the only Prussian row is R2881 (Add MS 32277 f.7, 1800, "Roy de Pfse").

**Two candidates fetched.** I picked the two dated 1752, the year of R1953, whose range (to ~1650) the step names. I
used one browser login (`tools/decode_browser_login.js`; certutil proxy-CA fix applied first) and wrote no account name to any file:
- **R4380** (Add MS 32276 f.64, 1752; sender "Kniph_n", i.e. Knyphausen, Prussian envoy at Paris; receiver "Roy de
  Prufse"; Cipher Type Unknown). On the image (P2+P3, one vision call) it is a Deciphering Branch **tally sheet, not
  a key**: printed numbers 1-1000 in columns, each with lower-case letter marks (a-p, apparently one letter per
  intercepted despatch the group occurred in). There are also cross-references in a 4001-4300 series and column-head offsets
  (200/310/210/320...). It gives **no plaintext meaning for any code**, so no known-key test can be built from it.
- **R4374** (Add MS 32276 f.52, 1752; sender "Michel", receiver "Roy de Prufse"; Simple substitution + Nomenclatures,
  syllables). It is a full reconstructed code table, 1-1000 with French meanings and margin additions (P2+P3, one vision call).
  The entries I could read at contact-sheet resolution match FT4's R1050-derived Michell key
  (`sibling_michell/key_sibling.tsv`): 100 ant, 149 aussi, 201 affaire. So this is **the same Michell code** that FT4 already
  tested against R1953 and found negative with its control (real -9.641 vs shuffle mean -9.367, p=0.695; positive
  control power 1.00 at R1953's covered count). A second test of it would be the same test. I also checked R1953's own range against
  this table on disk: 498 of 835 tokens (59.6%) are 1-1000, 336 are 1001-1650 and 1 is above, so a 1-1000 table could
  not cover R1953 by itself anyway.

**Result.** Neither fetched candidate gives a new key with meanings for any of the eight Hellen letters: R4380 has
no meanings and R4374 is the code already tested. No test was run, so there are no numbers and no control.
This is not a negative on the target (rule 3): no key was tested. Status stays `open`. Grade counts: H 0, C 0,
S 0, M 0, I 0 (nothing read).

**Next suggestion (not run).** The 1756 Potsdam sheets R4377 and R4379 (and R4378), for R1049 (7 Sept 1756,
range to ~3100), and the three 1751 sheets R4369/R4370/R4373 (senders unknown until RecordsView is read), for R1953.
Each one is only worth a test if its sheet carries meanings the way R4374 does, not tallies like R4380. Cheapest
route: one login, RecordsView plus thumbnails for the six records (~14 requests, sender field and a thumbnail look,
~USD 2). Then transcribe a meaning-bearing table with `tools/iiif_lines.py --image` column crops, 2 blind passes
+ 1 reconciliation, about 20 calls, ~USD 15. Then run FT4's `test_sibling.py` against it (value-shuffle x200, positive
control power at the target's N).

Images (not committed; re-fetch with `tools/decode_browser_login.js 4374 OUT --guess-fullsize --fetch-page
.../RecordsView/4380,...ImagesList?showmaster=records&fk_id=4380`), sha1:
R4374 P1-P4 9f36f952db0a3198f03e837a9954a7d23793e975, 04800426dd94387e492909a021828afbc37b35ee,
09785cbfb7ed00b253b1e7ca454f565758cc69b4, f3a0d7f31aa4e78c973a59621d10e58e712586d4 (4375-4426 x 5625-5748 px);
R4380 P1-P4 02a38d513fba4f2dad34877cb91e30197394d723, 975cea1c7cd5b15b703eafaaebefe26fd348f11a,
f58f12cdcaf882e5f05449dc0d246777cb9bdfe9, 62461d15ca24b7017748f49bdcb7a1ceb9c04450 (4327-4448 x 5550-5611 px).

Requests: de-crypt.org 22 after one login (RecordsView x2, DocumentsList x2 -- both "No records found", ImagesList x2,
8 thumbnails, 8 full-size images), 1.7 s apart, no challenge. github.com 1 shallow clone. Vision calls 2 of 3.

## IMG-DECODE1: DECODE sheets R4369-R4379 (account 2 worker for LANE-IMAGES, 3 Oct 2026)

Step run: FT4b's "Next suggestion": RecordsView for six BL Add MS 32276 key records, a look at each sheet, and full size only
for sheets that carry meanings. One browser login (`tools/decode_browser_login.js ... --guess-fullsize --listen`, shared with
two other targets). **Full-size images are served for every record asked** (no forbidden.png). Not committed: every RecordsView
says "The image is not in the public domain. Publishing it is only possible with the permission of the Library." Sha1s, native
sizes and URLs are in `images/decode/manifest.json`. Nothing was transcribed or graded, and no test was run.

| Record | BL Add MS 32276 | DECODE date | Sender -> receiver (DECODE) | DECODE cipher type | Sheet on the image (P2; P3 where fetched) | Full size fetched |
|---|---|---|---|---|---|---|
| R4369 | f.44 | 1751 | **Hellen/Ellen a la Haye -> Roy de Prufse** | homophonic + nomenclature, syllables | **code table with French meanings**, headed "Hellen avec le Roy de [Prusse]" across P2-P3; codes seen at least 927-948 (P2) and 1026-1548 (P3), e.g. 939 pretexte, 1535 comment, 1548 expedi | P1-P4 |
| R4370 | f.46 | 1751 | (blank) | simple + nomenclature, syllables | code table with French meanings (e.g. 131 la, 134 comme, 139 impossible, 141 meme, 148 attention) | P2, P3 |
| R4373 | f.50 | 1751 | Michel -> Roy de Prufse | simple + nomenclature, syllables | code table with French meanings, sparsely filled (e.g. 132 impart, 134 expos, 146 quelle) | P2, P3 |
| R4377 | f.58 | 1756 | Roy de Prufse -> Michel, Potzdam | simple + nomenclature, syllables, nulls | code table with French meanings (e.g. 129 mettre, 132 moyennant, 135 l'Electr., 144 raisons) | P2, P3 |
| R4378 | f.60 | 1756 | (blank) | simple + nomenclature, syllables, nulls | P2 is a ruled numbered form, essentially empty apart from "1756" at the head; P1, P3 and P4 not seen | P2 only |
| R4379 | f.62 | 1756 | Roy de Prufse -> Michel, Potzdam | homophonic + nomenclature, syllables, nulls | **tally sheet** like R4380: numbered columns with letter marks (530 a, 547 b, 632 c, 643 c), no meanings | P2 only |

(Readings in the table are what one vision call on a contact sheet showed, at contact-sheet resolution. They are labels for
sorting the sheets, not transcriptions, and not graded.)

What this changes:
- **R4369 is the English Deciphering Branch's reconstructed key for Hellen's own correspondence with Frederick II.** DECODE
  dates it 1751, and its header names Hellen. This is not a sibling chancery's key. Its codes run past 1500, and R1953 (4 Jan 1752)
  has 834 of 835 tokens at or below about 1650 (FT4b). It is the only candidate key in this folder attributed to Hellen's own
  line.
- R4373 and R4377 are Michel's (London) tables. R4373 may be the 1751 counterpart of R4374, which FT4b found is the Michell code
  already tested negative. R4377 is the 1756 Potsdam-to-Michel table, a different correspondent from Hellen.
- R4370 has no named holder. R4378's P2 is empty. R4379 is a tally sheet and gives no meanings.

Next step (not run; for the next lane): transcribe R4369 P1-P4 into a key.tsv (column crops with `tools/iiif_lines.py --image`,
2 blind passes + 1 reconciliation, per TRANSCRIPTION.md; P1 and P4 were fetched but not looked at). Then run the known-key test on
R1953 the way FT4 did (`sibling_michell/test_sibling.py`: value-shuffle x200, with the positive control's power at R1953's covered
count). The images must be re-fetched (manifest gives the URLs; one login). Status stays `open`. Grades: none (nothing read).

Requests: de-crypt.org 18 for this target (6 RecordsView, 12 full-size images), part of about 39 for the shared one-login job,
1.7 s apart, no challenge. Vision calls: 1 for this target (3 in the job). Account name not in any committed file.

## READ2-HEL (3 Oct 2026): R4369 key transcribed, known-key test on R1953 (account 2 worker for LANE-READ2)

Step run: IMG-DECODE1's next step. **Route:** one browser login (`tools/decode_browser_login.js 4369 <scratchpad> --fetch
<4 absolute filesrv URLs>`). R4369 P1-P4 were re-fetched full size, and all four sha1s match `images/decode/manifest.json`. The
images are kept in the scratchpad and are not committed (not public domain), and the account name is in no file.
Requests: de-crypt.org about 8 (login page, login submit, landing page, RecordsView/4369, 4 images), 1.7 s apart, no challenge;
no other host.

**What the sheet is.** P1 is the docket only ("Ellen a la Haye avec le Roy de Prusse 1751"). P4 is blank. P2+P3 are one spread
headed "Hellen avec le Roy de Prusse", printed code numbers in blocks of 100: P2 has 901-1300 and a cut-off copy of 1401, and P3
has 1401-1800 (entries up to 1796) plus a hand-numbered, unruled block 801-900 at the right.
**Codes 1-800 are not on this record.** A row can carry two meanings: a LEFT one written straight after the number ("1202- vie"),
and a RIGHT one, right-aligned against the next block's divider and ending in a dash ("avec -"). Many right entries are names
(la Cour de Vienne, le Roy de Pologne, bruhl, les Puiss. Maritimes, baron, van) or syllables (ma me mi mo mu).

**Transcription** (TRANSCRIPTION.md pipeline, shortened: no benchmark item of this hand exists). Column crops were cut with
`python3 tools/iiif_lines.py --image <P2|P3 file> --out <scratchpad>/crops --region <x>,400,<665|660|950>,4880 --centres
625,1835,3045,4255 --prefix P<p>_c<block> --debug`, once for each of the 10 blocks. That gives **40 crops** (4 per block, about
25 rows each). Automatic line detection found 0 lines on the ruled table, so the centres were given by eye. The two blind Sonnet
passes for each page each saw only that page's 20 crop paths (4 subagent calls). Their outputs were compared with a script keyed
on the code: `reconcile_passes.py` aligns sequences of signs, but these passes are rows keyed by code number, so no alignment was
needed and a code-keyed diff was used instead. I settled 44 disagreements from a strip montage of the disputed rows (my own
vision reads: contact sheet, 2 header strips, 2 crop checks, 1 montage).
**err_2reader 4.8%** (44 of 908 written cells: P2 26/564, P3 18/344). Most splits were spelling (cedilla, abbreviation dots).
Six were row assignments of right entries, which sit about half a row low. One cell both readers got wrong: 1125 is "saxe",
not "sacre"/"sage". **err_true is not measurable** (no benchmark item of this hand).
`key_r4369/key.tsv`: 716 rows, 902 meaning cells, grade H 881 / M 21 (H = read from a period key sheet, rule 4).

**Which code a right entry belongs to** is not stated on the sheet. A complementarity check (does a right entry sit beside an
empty left cell?) gives no signal at offset 0, +100 or +-1 (178-191 of 321 against a 57% base rate). So three attributions were
tested as separate keys (`key_r4369/build_keys.py [--check]`): L (left meanings), R0 (a right entry belongs to its own row's
code), R100 (it belongs to the code on the same row of the next block, the one its dash points at).

**Gate (brief step 4):** key_L covers 359 of R1953's 836 tokens, **42.9%**, so the gate (40% or more) is met. key_LR100 covers 470
(56.2%).

**Known-key test** (`sibling_michell/test_sibling.py --key <key> --out <file>`). This is a new mode in FT4's script (not a
private copy). Its unigram numbers reproduce FT4's Michell row exactly (-9.641, p 0.695). Statistics: (uni) FT4's mean fr18
word log-prob of the covered tokens; (bi) the mean fr18 PMI of the junction word pair over adjacent covered tokens.
Controls, 200 each: (a) value-shuffled keys, applied to both statistics. (b) The target's token ORDER shuffled, applied to bi
only. **Brief correction:** the brief said FT4's statistic is order-sensitive, but a mean over covered tokens is identical under
any order shuffle by construction (CLAUDE.md rule 3, the bCAS / AX-5799 shape). That is why the bigram statistic was added: so
that (b) can differ from the target. (c) Positive control: fr18 prose encoded with the same key, decoded windows at R1953's
covered count (uni) or pair count (bi); power is the share of 200 windows reaching p<=0.05. Full table in HYPOTHESES.md.

| key (R1953) | covered | uni real / shuffle mean / p95 | uni p | pairs | bi real / val-shuffle mean | bi val p | bi order-shuffle mean / p95 | bi order p | power uni / bi |
|---|---|---|---|---|---|---|---|---|---|
| L | 359 (42.9%) | -8.985 / -9.750 / -9.229 | 0.005 | 148 | -0.756 / -0.880 | 0.025 | -0.858 / -0.758 | 0.040 | 1.00 / 1.00 |
| R0 | 195 (23.3%) | -8.891 / -8.604 / -8.046 | 0.805 | 44 | -0.896 / -0.875 | 0.545 | -0.846 / -0.656 | 0.645 | 1.00 / 1.00 |
| **R100** | 315 (37.7%) | -6.930 / -8.578 / -8.185 | **0.000** | 125 | -0.455 / -0.865 | **0.000** | -0.656 / -0.541 | **0.010** | 1.00 / 1.00 |
| L on codes R100 does not reach (Lonly) | 155 (18.5%) | -7.193 / -9.667 / -8.958 | **0.000** | 26 | -0.212 / -0.867 | **0.000** | -0.762 / -0.544 | **0.000** | 1.00 / 1.00 |
| L on the 189 codes R100 also reaches | 204 (24.4%) | -10.346 / -9.949 / -9.418 | 0.855 | 48 | -0.836 / -0.889 | 0.285 | -0.899 / -0.755 | 0.220 | 1.00 / 1.00 |
| **LR100** (R100 wins conflicts) | 470 (56.2%) | -7.017 / -9.157 / -8.755 | **0.000** | 266 | -0.361 / -0.877 | **0.000** | -0.694 / -0.609 | **0.000** | 1.00 / 1.00 |

Seed 2 reproduces LR100 (uni -7.017 vs -9.181, p 0.000; bi order p 0.000). Under LR100 none of the other seven letters (R1045-R1049,
R1060, R1061; 1756 and 1763) beats its controls. Under LR100 their uni p values run 0.665-0.98 at 16-34% coverage. The
lowest of the 14 bigram p values is R1046's order p of 0.025, on 34 covered tokens with uni p 0.94, which does not survive a
multiple-test correction. They are another code, as their ranges already suggested.

**Reading of the result.** The right entries belong to code+100, and the left entries hold only where no right entry lands. On
the 189 codes where both land, the left meanings carry no signal (p 0.855); they look like superseded or other-series values.
The sheet does not say this. It is the control-backed test's choice, so those 305 key values are graded **S**, not H.
**R1953 decoded with a period key:** `tools/decode_key.py ciphers/hellen-frederick-1752/key_r4369` with `decode.json` gives
`reading_R1953.txt`, and `--check` passes ("reading up to date"). Tokens 846: **H 152, C 0, S 304, M 16, I 0, U 374**. U are codes
1-800 (not on this sheet) and 14 empty cells. The decoded spans are French fragments, e.g. "si feu pce d'Orange a [643] un ...",
"eu le tems [486] son", "lieu qu' ... les plus", "prince de ... le ordre avance". Willem IV of Orange died 22 Oct 1751, so
"feu" fits a 4 Jan 1752 letter. That is a fit, not a check.

**Judge** (`python3 tools/judge_plaintext.py specs/hellen-frederick-1752.json --file ciphers/hellen-frederick-1752/key_r4369/reading_R1953.txt`):
```
ok   length: got=1322, min=200, max=1000000000
FAIL language: score=-0.976, null_p99=-1.741, real_p05=-0.954, real_median=-0.827, mode=both, N=1322
FAIL - hellen-frederick-1752 (a PASS is a gate for a verifier, not a reading; rule 10)
```
Calibration (`key_r4369/judge_calib.py`, output in `judge_calib_output.txt`): real fr18 prose was encoded with this key and
decoded with the same gaps (uncovered words dropped), in windows of 846 tokens (358-406 covered). It scores -0.882 to -0.980
and FAILs 2 of 8 windows (-0.972, -0.980), the same place R1953 sits. **At this key's coverage the judge cannot decide:** this
is a FAIL near the gate and far above the null, not a negative.

Status: **partial** (rule 5: a key beat its matched controls by a reproducible margin). Nothing is called more than "read with a
period key, grade H for 152 tokens" (plus S 304 by attribution). Conditional on DECODE's transcription of R1953 (rule 2). Rule 7's
fresh-session re-derivation has not been run; that is the orchestrator's step. Report what was found and where it was not found:
codes 1-800 of this key were not found on R4369 P1-P4. Calls: 4 Sonnet subagent passes and 6 own image reads (no further passes).

## READ2-HEL2 (3 Oct 2026): R4370 transcribed and tested as codes 1-800 on R1953 (account 2 worker for LANE-READ2)

Step run: READ2-HEL's named next step. Pre-registration (`key_r4370/PREREG.md`, commit f275f41d) was pushed before any image was
looked at. **Route:** one browser login (`tools/decode_browser_login.js 4370 <scratchpad> --fetch <4 filesrv URLs>`). P1-P4 were
fetched full size; the P2/P3 sha1s match `images/decode/manifest.json`. P1 sha1 666c481b..., P4 0dc248ee...; neither was listed. The
images stay in the scratchpad (not public domain) and the account name is in no file. Requests: de-crypt.org about 8 (login page,
submit, landing, RecordsView/4370, 4 images), 1.7 s apart, no challenge; no other host.

**What the sheet is.** P1 carries only the docket "1751"; P4 is blank (P3's edge shows). P2+P3 are one spread with the same printed form
as R4369: printed codes in blocks of 100, a LEFT meaning straight after the number and a RIGHT entry right-aligned against the next
block's divider, ending in a dash. P2 holds 1-400 plus 401-500 (whose right entries also appear photographed again at the left of P3),
and P3 holds 501-900 plus a strip of 901-1000 numbers. **R4370 carries codes 1-1000**, so it does reach R1953's codes 1-800.

**Transcription.** Column crops: `python3 tools/iiif_lines.py --image <P2|P3 file> --out <scratchpad>/crops --region <x>,230,<w>,5020
--centres 628,1883,3138,4393 --prefix P<p>_c<block> --debug`, once per block (P2 x/w 190/840, 940/820, 1700/820, 2450/840, 3200/808;
P3 590/820, 1360/790, 2120/800, 2880/820). That makes **36 crops** (9 blocks x 4 bands), cut before any subagent call. Four blind
Sonnet passes (2 per page) saw only that page's crop paths. A code-keyed diff (letters only: case, accents and punctuation ignored)
gives **err_2reader 13.1%** (122 of 934 written cells; 16.0% raw). That is higher than R4369's 4.8%. Most splits are row or side
placement of right entries, crossed words, and abbreviation dots. I settled the 46 disputed codes that bear on R1953 (code c or c+100
in R1953) from two strip montages (my own reads). The other 60 disputed codes take pass A's cell (B's when A is empty) at grade M.
The montage also corrected one cell both readers got wrong: 175 R is "gueres", not "queres". 413 R is "douteux".
`key_r4370/key.tsv`: 689 rows, 917 meaning cells, grade H 836 / M 81 (H = read from a period key sheet). err_true is not measurable
(no benchmark item of this hand).

**Gate A (range/overlap).** R4370 carries codes 2-1000. On 801-1000 it shares 70 codes with R4369 LR100, and **none has the same
meaning** (R4369's hand block 801-900 runs son, sont, sort ... prison, publie; R4370's runs entrave, munic, ... reste, disposition).
So on that range it is a rival series, not a continuation. Per PREREG it was also tested whole as a rival (row "full").
**Gate B (coverage):** R1953 has 349 numeric tokens at codes 1-800. L covers 191 (51% of 374), R0 158, R100 145, LR100 243. The gate
(113) is met.

**Test** (`sibling_michell/test_sibling.py --key key_r4370/key_<X>.tsv --out key_r4370/test_key_<X>.txt`, seed 1). Each key is
restricted to codes 1-800, so it covers only the tokens R4369 cannot reach. Pass = uni value-shuffle p and bi order-shuffle p both
<= 0.05/4 = 0.0125, power >= 0.8.

| R4370 key on R1953 | covered | uni real / shuffle mean / p95 | uni p | pairs | bi real / val-shuffle mean | bi val p | bi order-shuffle mean / p95 | bi order p | power uni / bi | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| L | 191 | -9.283 / -9.383 / -8.758 | 0.370 | 48 | -1.047 / -0.809 | 0.985 | -0.837 / -0.648 | 0.985 | 1.00 / 1.00 | fail |
| R0 | 158 | -10.106 / -10.225 / -9.566 | 0.350 | 28 | -0.817 / -0.811 | 0.510 | -0.797 / -0.615 | 0.535 | 1.00 / 1.00 | fail |
| R100 | 145 | -10.719 / -10.143 / -9.552 | 0.935 | 29 | -0.830 / -0.822 | 0.550 | -0.831 / -0.628 | 0.505 | 1.00 / 1.00 | fail |
| LR100 | 243 | -10.036 / -9.664 / -9.221 | 0.875 | 79 | -0.908 / -0.813 | 0.840 | -0.888 / -0.769 | 0.595 | 1.00 / 1.00 | fail |
| full (rival, 1-1000, outside k) | 341 | -10.259 / -9.849 / -9.518 | 0.950 | 146 | -0.905 / -0.807 | 0.915 | -0.867 / -0.780 | 0.825 | 1.00 / 1.00 | fail |

For comparison, R4369 LR100 on its own codes reads -7.017 against -9.157 (p 0.000), with bi order p 0.000, at the same power.
**Secondary rows (not gated):** across the five R4370 keys, none of the other seven letters (R1045-R1049, R1060, R1061) clears 0.0125 on
both statistics. The lowest are R100 on R1061, uni p 0.020 with bi order p 1.000 at bi power 0.00, and full on R1061, bi order p 0.035
with uni p 0.635.

**Result.** At full power (1.00), no attribution of R4370 reads R1953's codes 1-800, and none reads any of the other letters.
**R4370 is not the first half of the Hellen key that R4369 reads.** Its 801-1000 conflicts with R4369 on every shared code, and the
sheet names no holder: it is another 1751 code in the volume. **R4369's result stands unchanged** (H 152 / S 304 / M 16 / U 374). No
merged key was built (brief step 5 is gated on a pass). Calls: 4 Sonnet subagent passes, plus my own reads (contact sheet, 4 edge and
header strips, 2 crop checks, 2 reconciliation montages). Report what was found and where it was not found: R1953's codes 1-800 have
no key on R4369 P1-P4 or R4370 P1-P4.

## Remaining gaps (READ2-HEL2, 3 Oct 2026)
Read so far: 456 of 846 R1953 tokens carry a key value (H 152, S 304) plus M 16; 374 U
- codes 1-800 of the Hellen key (374 R1953 tokens) - blocker: not-attempted; not on R4369, and R4370 tested negative at power 1.00 (READ2-HEL2); next: open the Add MS 32276 key records not yet looked at, R4376 (f.56, 1754) and the 1740s records before f.44, contact sheet first, then the same --key test on any sheet carrying 1-800 meanings, ~$6
- empty cells inside 801-1796 (14 tokens) and the 16 M tokens - blocker: open-codes; scattered codes the sheet leaves blank or the readers could not settle
- the other seven letters (1756, 1763 cluster) - blocker: no-key-material; neither R4369 nor R4370 reads them (controls above), and FT4b/IMG-DECODE1 found no meaning-bearing 1756/1763 Hellen table among the DECODE Add MS 32276 records looked at

## Escalation (READ2-HEL2, 3 Oct 2026)
- [x] siblings: Michell keys tested negative (FT4, FT4b); R4370 (f.46) tested negative as the first half (READ2-HEL2)
- [n/a] clear-pages: no clear passage of R1953 is known on disk to serve as a crib
- [x] known-keys: R4369 transcribed and tested, reads R1953 above every control; R4370 transcribed and tested, does not
- [x] print: Politische Correspondenz vols. 9-10 searched for the letter (check-solved sections above)
- [ ] key-rebuild: infer values for codes 1-800 from context in the R4369-decoded spans (cryptanalytic, needs its own control)
- [x] image-check: R4369 and R4370 read from the full-size images, two blind passes plus reconciliation each
- [ ] retry: an image check of R1953 itself against DECODE's transcription where decoded spans break (rule 2)
Verdict: keep going: 2 internal gaps; cheapest next: open R4376 and the pre-f.44 Add MS 32276 key records for codes 1-800, ~$6

## READ2-HELRD rule-7 re-derivation (3-4 Oct 2026)

Fresh worker (account 2, for LANE-READ2) that had seen only the spec, `ciphertext_R1953.txt`, `key_r4369/key.tsv` and `decode.json`. Script: `key_r4369/rederive_helrd.py` (output `rederive_helrd.txt`, one line per token, `?` for unkeyed). Rules it applied, from decode.json's header and key.tsv alone: left cell -> its own code; right cell -> code+100, and where both land on one code the right (code+100) cell is used; `_`/`^` marks stripped; an inner `?` (doubtful digit, e.g. `128?3`) -> unkeyed; a trailing `?` (e.g. `990?`) read as usual.

`python3 tools/decode_key.py ciphers/hellen-frederick-1752/key_r4369 --check`: `R1953_pipe.txt: tokens 846: H 152, M 16, S 304, U 374` / `reading up to date` (exit 0).

Diff against `reading_R1953_tokens.tsv` (opened only after the script and its output were written): 846 tokens, 845 agreements, 1 difference.
- Token 355 (sign 1023, line L01 pos 354): re-derivation `~satisfa` (key.tsv left cell, H); committed reading `?`, grade U. Not an M-graded token. Cause: the committed key drops crossed-out cells (a `~` prefix; stated in `build_keys.py`'s docstring, not in decode.json or the key's header), which a spec-plus-key reader cannot know. Applying that `~` rule makes it 846/846.
- Two choices were not stated in the files this pass read and were matched to the committed reading only by trial: right-over-left on a shared code (207 tokens, committed S/M), and trailing `?` as read-but-M (990?, 1421?, two M tokens).

Verdict: on the letter of the brief (every difference on an M-graded token, else SEND BACK), SEND BACK, narrowly: one U-graded token, from an unstated convention rather than a key error. Suggested fix, for the lane orchestrator: state the `~` rule, the right-over-left rule and the trailing-`?` rule in decode.json's header or README, then this reading can be accepted at 846/846. This check says "worth a verifier", never "right" (rule 10).

## NEAR3-HEL3 (4 Oct 2026): DECODE key records in BL Add MS 32276 looked at for codes 1-800 (account 2 worker for LANE-NEAR3)

Step run: READ2-HEL2's named next step. No transcription, test or grades in this job.
**Step 1 (no login).** I listed every DECODE key record in BL Add MS 32276 from the login-free listing already on disk
(`sources/decode/keys-all-2026-09-28-merged.tsv`; no refetch). There are 63 records, R4343-R4408 (ff. 1-127, 1722-1794; R4349,
R4350, R4365 and **R4371 do not exist**). Sender and receiver come from each RecordsView page. **No record outside R4369 names
Hellen/Ellen.** `key_search/add32276_records.tsv` has the full list, with sender, receiver, cipher type and what each sheet is.
**Step 2 (one browser login).** `NODE_PATH=$(npm root -g) node tools/decode_browser_login.js 4376 <scratchpad> --delay 1700
--max-files 0 --listen <cmdfile>`. Fetched: RecordsView for R4376 and for the 25 records not yet opened (R4343-R4368 before
f.44, plus R4372 and R4375); full-size P2 of every record that has one; P1+P3 of R4345, R4354, R4363, R4372 and R4376; and
R4369 P2 again for comparing hands (its sha1 matches the manifest). No forbidden.png. Images stay in the scratchpad (not public
domain). Sha1s, native sizes and URLs are in `images/decode/manifest.json` (now 32 records, 46 files).
**Step 3 (5 contact sheets + 1 detail strip = 6 vision calls).** What each sheet is, by period:
- 1722-1739 (R4343-R4360): Reichenbach, Degenfeld, Grumkow, Borck and Michel (1722) tables. Most have German meanings
  (Degenfeld) or are name lists. R4344 (Michel 1722) and R4360 (Andrie, London, 1739) are filled French tables, but both are
  named for another holder and predate Hellen by 12-29 years.
- 1743-1746 (R4361-R4368): Mardefeldt tables (one is letter tallies only, one sparse German); R4363 is blank; R4364 is tallies
  only; Scholing 1744; Andrie 1745 and Roy de Prusse -> Andrie 1745-46 (dense French, named for Andrie).
- **R4372 (f.48, DECODE date "1724 - 1844", no sender or receiver).** This uses **the same printed form and the same entry
  layout as R4369**: printed codes in blocks of 100; a LEFT meaning right after the number; a RIGHT entry right-aligned
  against the next block's divider, ending in a dash. Nulls are written "zero". The hand looks like R4369's at strip
  resolution (one detail strip, R4372 P2 codes ~20-29/120-130 beside R4369 P2 codes 1026-1037; e.g. 21 objet, 24 prusse,
  122 dent, 125 quoique, 126 aucun, 128 arrangement, right entries "appro..", "par", "inform", "opinion", "cote").
  P1 is blank (docket "48" only). P2 holds codes 1-500, well filled. P3 holds 501-800, sparser (501 au, 502 com/m, 701 ver),
  with 801-900 and 901-1000 almost empty. **So R4372 carries meanings for codes 1-800 and stops about where R4369 begins (801).**
  It is bound at f.48, between Hellen's f.44 and the unnamed f.46 on one side and Michel's 1751 f.50 on the other. **No header
  names Hellen.** R4369's header ("Hellen avec le Roy de [Prusse]") sits on its own P2 top band, and R4372's P2/P3 top bands carry
  only "200" at the top left. The attribution therefore rests on the form, the layout, the hand and the code range, not on a
  header. Unlike R4370, its 801-900 does not clash with R4369 because it is nearly empty there.
- R4375 (f.54, Michel -> Roy de Prusse, undated): dense French table, named for Michel.
- R4376 (f.56, 1754): P1 is the docket "1754", P2 is a blank ruled form, and P3 is a filled French table of codes 1-500 with
  "zero" nulls. Entries include "la Haye" and "pays bas", but no holder is named. It is worth a later look for the 1756 letter
  (R1049), not for R1953.

**Step 4 (stop: a candidate sheet).** These are the facts the transcription brief needs. Record R4372 = BL Add MS 32276 f.48
(https://de-crypt.org/decrypt-web/RecordsView/4372). Pages: P2 (codes 1-500), 3999x5519 px,
`https://de-crypt.org/decrypt-custom/filesrv/?file=IMG_R4372_I26137_P2.jpg`, sha1 d6de7162...; P3 (codes 501-1000, filled only
to ~800), 3928x5517 px, `...IMG_R4372_I26137_P3.jpg`, sha1 4871a1f6...; P1 is blank, 3991x5517, sha1 46e30c65... The layout is
the same as R4369/R4370, so READ2-HEL2's column-crop recipe applies with re-measured x positions (P2 has 5 blocks, P3 has
5 blocks). Then run `sibling_michell/test_sibling.py --key <R4372 key restricted to 1-800>` on R1953 with the L/R0/R100/LR100
attributions pre-registered, exactly as READ2-HEL2 did. Like R4370 it is a candidate until that test passes: the matching form is
not proof, because R4370 used the same form and failed.

Requests: de-crypt.org about 64 (login page, submit, landing, RecordsView/4376, 25 RecordsView pages, 35 full-size images), 1.7 s
apart, no challenge, one login; no other host. Subagent calls: 0. Vision calls: 6. The account name is in no file. Report what was
found and where it was not found: no Add MS 32276 record other than R4369 names Hellen. R4343 P2 was not looked at (1729
Reichenbach, one page). Post-1756 records R4381-R4408 were not opened (outside this job; relevant only to the 1763 letters).

## Remaining gaps (NEAR3-HEL3, 4 Oct 2026)
Read so far: 456 of 846 R1953 tokens carry a key value (H 152, S 304) plus M 16; 374 U (READ2-HEL2, unchanged)
- codes 1-800 of the Hellen key (374 R1953 tokens) - blocker: not-attempted; candidate sheet found, R4372 (f.48), the same form, layout and hand as R4369, codes 1-800 filled (NEAR3-HEL3); next: transcribe R4372 P2-P3 (2 blind passes + reconciliation, READ2-HEL2 recipe) and run the pre-registered --key test on R1953 codes 1-800, ~$12
- empty cells inside 801-1796 (14 tokens) and the 16 M tokens - blocker: open-codes; scattered codes the sheet leaves blank or the readers could not settle
- the 1756 letter (R1049) - blocker: not-attempted; R4376 (f.56, docket 1754, French table 1-500 with "la Haye", no holder) not yet tested; next: transcribe R4376 P3 and test on R1049, after the R4372 test, ~$8
- the 1763 letters (R1045-R1048, R1060, R1061) - blocker: no-key-material; neither R4369 nor R4370 reads them, and no 1763 Hellen table has been found among the Add MS 32276 records looked at (post-1756 records R4381-R4408 not yet opened)

## Escalation (NEAR3-HEL3, 4 Oct 2026)
- [x] siblings: Michell keys tested negative (FT4, FT4b); R4370 (f.46) tested negative as the first half (READ2-HEL2); all 25 unopened Add MS 32276 records up to f.56 looked at (NEAR3-HEL3)
- [n/a] clear-pages: no clear passage of R1953 is known on disk to serve as a crib
- [ ] known-keys: R4369 transcribed and tested, reads R1953; R4372 (f.48) is the candidate first half and is not yet transcribed or tested
- [x] print: Politische Correspondenz vols. 9-10 searched for the letter (check-solved sections above)
- [ ] key-rebuild: infer values for codes 1-800 from context in the R4369-decoded spans (cryptanalytic, needs its own control); only if R4372 fails
- [x] image-check: R4369 and R4370 read from the full-size images, two blind passes plus reconciliation each
- [ ] retry: an image check of R1953 itself against DECODE's transcription where decoded spans break (rule 2)
Verdict: keep going: 3 internal gaps; cheapest next: transcribe R4372 (f.48) P2-P3 and run the pre-registered --key test on R1953 codes 1-800, ~$12
