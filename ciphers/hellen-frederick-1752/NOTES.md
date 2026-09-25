open
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
