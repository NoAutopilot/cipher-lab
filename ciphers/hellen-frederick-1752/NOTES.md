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
   this row is nominated on, and reports it as **not yet retrieved** as of his last update — no earlier pass in this
   repository had opened the NA viewer for it (below; wording corrected by verifier NEAR3-VHEL, 4 Oct 2026, rule 10).
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
[Verifier NEAR3-VHEL, 4 Oct 2026: this explanation is contradicted by De Leeuw 2000 ch. 8 n.32. English-deciphered
copies of Hellen's letters from 30 Oct to 28 Dec 1751 are in NA Fagel inv. 5177, and that volume has no Hellen letter
between 28 Dec 1751 and 8 Sept 1752. See AUDIT.md section 3d. The finding that inv. 5206 starts on 24 Oct 1752 stands.]
[Verifier A3V-VHEL2, 4 Oct 2026: the register's own 1752 numbering is already at No 71 on 5 Sept 1752 (5177 scan 108), so
some 33-70 numbered intercepts of Jan-Aug 1752 are in neither 5177 nor 5206 (no other Fagel volume covers 1752; finding aid
read in full). The King's file of Hellen's 1752 reports is GStA PK I. HA Rep. 96 Nr. 38 G-H, not digitised. AUDIT.md, AUDIT 2.]

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

## NEAR3-HEL4 (4 Oct 2026): R4372 (f.48) transcribed and tested as codes 1-800 on R1953 (account 2 worker for LANE-NEAR3)

Step run: NEAR3-HEL3's named next step. **Pre-registration** `key_r4372/PREREG.md` (commit 453a570a) was pushed before the images
were fetched: READ2-HEL2's statistics, controls, four attributions and pass rule unchanged, plus a combined test (R4372 1-800 + R4369
LR100 801+), declared *reported, not gated*: R4369's half already passes on R1953 alone, so a combined key passes whatever the 1-800
half holds and its control cannot fail differently (rule 3).
**Route:** `tools/decode_browser_login.js 4372 <scratchpad> --delay 1700 --max-files 2 --fetch <P2,P3 filesrv URLs>`; both sha1s match
`images/decode/manifest.json` (d6de7162..., 4871a1f6...). Two logins, not one: my first call passed `--max-files 0`, which caps
explicit `--fetch` URLs too, so it saved only RecordsView; the second fetched both pages. Images stay in the scratchpad (not
public domain); the account name is in no file. Requests: de-crypt.org about 10 (2 x login page, submit, landing, RecordsView; 2 images), 1.7 s apart, no challenge; no other host.

**What the sheet is.** The same printed form as R4369/R4370. P2 = codes 1-500 in five blocks of 100, well filled (left entries plus
right entries ending in a dash, about half a row low, as on R4369). P3 = 501-1000: 501-600 and 701-800 carry left entries only;
601-700 is empty; 801-900 has 868 "pli" and two right entries (840 "grandes -", 900 "observ -"); 901-1000 (cut by the page edge) is
empty. A modern pencil folio "49" sits at the top of 801-900. Many entries are "zero" (nulls; 24 codes).
**Transcription.** Crops: `python3 tools/iiif_lines.py --image <P2|P3 file> --out <scratchpad>/crops --region <x>,250,<w>,5070
--centres 540,1570,2570,3590,4560 --prefix P<p>_c<block> --debug`, once per block (P2 x/w 230/820, 1005/800, 1755/800, 2505/800,
3270/729; P3 500/800, 1255/800, 2010/800, 2770/800, 3530/398): 50 crops of 20 rows each, cut at the printed form's 20-row gaps,
before any subagent call. Four blind Sonnet passes (2 per page, the second in reverse block order) saw only that page's 25 crop
paths. Code-keyed diff (letters only): **err_2reader P2 0.052 (20/386 cells), P3 0.113 (11/97)**, 0.064 overall. I settled the
disputes from one strip montage of the R1953-relevant rows (273 R, 276, 302/303 R, 502, 703, 744, 764, plus 16 and 521); the rest
take one pass's reading at grade M. `key_r4372/key.tsv`: 400 rows, 477 cells, **H 445 / M 32**. err_true not measurable (no
benchmark item of this hand). Conventions are stated in `key_r4372/README.md`.
**Gate A (range):** R4372 carries 1-1000 but 801+ holds only 868 (left) and 940/1000 (R100). Two codes shared with R4369 (868 pli
vs pour; 940 grandes vs S.M.), both different: the full key was also tested as a rival (outside k), per PREREG.
**Gate B (coverage):** best attribution LR100 covers 191 R1953 tokens (L 147, R0 63, R100 69); gate 113 met.

**Test** (`sibling_michell/test_sibling.py --key key_r4372/key_<X>.tsv`, seed 1; full table in HYPOTHESES.md). Pass = uni p and bi
order p both <= 0.0125, power >= 0.8.

| R4372 key on R1953 (1-800) | covered | uni real / shuffle mean | uni p | bi real / order-shuffle mean | bi order p | power uni / bi | verdict |
|---|---|---|---|---|---|---|---|
| L | 147 | -10.164 / -10.038 | 0.625 | -0.444 / -0.698 | 0.055 | 1.00 / 1.00 | fail |
| R0 | 63 | -10.512 / -10.263 | 0.670 | -0.602 / -0.800 | 0.278 | 1.00 / 0.97 | fail |
| R100 | 69 | -9.825 / -10.323 | 0.165 | -0.963 / -0.948 | 0.410 | 1.00 / 0.98 | fail |
| LR100 | 191 | -10.035 / -10.137 | 0.375 | -0.525 / -0.784 | 0.010 | 1.00 / 1.00 | fail (uni) |
| LR100 seed 2 | 191 | -10.035 / -10.196 | 0.295 | -0.525 / -0.786 | 0.000 | 1.00 / 1.00 | fail (uni) |
| full 1-1000 (rival) | 195 | -10.041 / -10.234 | 0.290 | -0.570 / -0.810 | 0.000 | 1.00 / 1.00 | fail (uni) |
| *for scale: R4369 LR100 on its own codes* | 470 | -7.017 / -9.157 | 0.000 | -0.361 / -0.694 | 0.000 | 1.00 / 1.00 | pass (READ2-HEL) |

**Combined (reported, not gated):** comb_LR100 covers 661 tokens (79.1%), uni -7.889 vs -9.516, p 0.000 -- but R4369 alone reads
-7.017, so adding R4372's half lowers the score by 0.87 (by 0.36-0.75 for the other attributions): the added tokens read worse than
R4369's own. Secondary rows (not gated): R1049 (1756) under LR100 uni p 0.010 with bi order p 0.310 -- one statistic of 35
secondary tests; no other letter under 0.0125.
**Diagnostic (not pre-registered, not a gate):** 15 of the 191 covered tokens are "zero" (code 405 ten times), which the word
statistic scores as a rare word; with the zero codes removed LR100 reads uni -9.704 vs -9.950, p 0.245 (bi order p 0.010) -- still
far from a pass, so the nulls do not explain the failure.

**Result.** At power 1.00 the unigram statistic fails for every attribution: **R4372 does not read R1953's codes 1-800 the way R4369
reads 801+** (pre-registered fail). One thing differs from R4370: R4372 LR100's order-sensitive bigram statistic sits at or under
the gate on both seeds (0.010, 0.000; R4370 0.595), on 42 adjacent pairs. A key that is wrong word-by-word should not raise junction
PMI over the order shuffle; a key that is right should raise both statistics. This is a mixed result, not a pass; it is not used to
grade anything. No combined key or reading was built (PREREG item 7); **R4369's reading stands unchanged** (H 152 / S 304 / M 16 /
U 374). Calls: 4 Sonnet subagent passes; my own reads: 2 page overviews, 2 crop checks, 1 reconciliation montage. Report what was
found and where it was not found: R1953's codes 1-800 have no reading from R4369, R4370 or R4372.

## Verifier NEAR3-VHEL (4 Oct 2026): AUDIT.md written, class N3, key source period

Separate verifier session (account 2, for LANE-NEAR3). No decoding. Class **N3** for the R1953 partial reading (456 of 846
tokens carry a key value: H 152, S 304; U 374). No printed plaintext and no period decipherment of the 4 Jan 1752 despatch
were located after a logged search across families a-g. The most likely holdings were checked: Politische Correspondenz
vol. 9 (replies to 31 Dec, 11 and 14 Jan, none to 4 Jan); De Leeuw 2000, all chapters; the BL and TNA catalogues; and
NA Fagel inv. 5177 (Hellen decipherments run to No 37, 28 Dec 1751, then none until 8 Sept 1752) and inv. 5206. Not
covered item by item: GStA PK (the receiving side) and the English decypher series. Full log, safe and unsafe sentences
and postmortem are in `AUDIT.md`. Phrase search: `phrases.txt`, `sources.tsv` -> `print-check.tsv`.
Suggestion for the lane (not run): Fagel inv. 5177's clear decipherments of Hellen's letters of Oct-Dec 1751 (scans ~2-93)
are the nearest same-writer context, and possibly same-code known plaintext, for codes 1-800; contact sheet first, ~$3.

## Remaining gaps (NEAR3-HEL4, 4 Oct 2026)
Read so far: 456 of 846 R1953 tokens carry a key value (H 152, S 304) plus M 16; 374 U (unchanged)
- codes 1-800 of the Hellen key (374 R1953 tokens) - blocker: not-attempted; R4370 and R4372 both fail the pre-registered test (READ2-HEL2, NEAR3-HEL4), R4372 with a bigram-only signal; next: a pre-registered diagnosis of R4372's bigram signal (which pairs carry it, a per-code check of whether R4372 values fit the R4369-decoded context on either side) before any cryptanalytic key-rebuild of 1-800 with its own control, ~$5
- empty cells inside 801-1796 (14 tokens) and the 16 M tokens - blocker: open-codes; scattered codes the sheet leaves blank or the readers could not settle
- the 1756 letter (R1049) - blocker: not-attempted; R4376 (f.56, docket 1754, French table 1-500 with "la Haye", no holder) not yet tested; R4372 LR100 gave R1049 a uni-only p 0.010 (secondary, not gated); next: transcribe R4376 P3 and test on R1049 with R4372 as a pre-registered second candidate, ~$8
- the 1763 letters (R1045-R1048, R1060, R1061) - blocker: no-key-material; neither R4369, R4370 nor R4372 reads them, and no 1763 Hellen table has been found among the Add MS 32276 records looked at (post-1756 records R4381-R4408 not yet opened)

## Escalation (NEAR3-HEL4, 4 Oct 2026)
- [x] siblings: Michell keys tested negative (FT4, FT4b); R4370 (f.46) and R4372 (f.48) tested negative as the first half (READ2-HEL2, NEAR3-HEL4); all 25 unopened Add MS 32276 records up to f.56 looked at (NEAR3-HEL3)
- [n/a] clear-pages: no clear passage of R1953 is known on disk to serve as a crib
- [x] known-keys: R4369 transcribed and tested, reads R1953; R4370 and R4372 transcribed and tested, neither reads codes 1-800
- [x] print: Politische Correspondenz vols. 9-10 searched for the letter (check-solved sections above)
- [ ] key-rebuild: infer values for codes 1-800 from context in the R4369-decoded spans (cryptanalytic, needs its own control); first diagnose R4372's bigram-only signal
- [x] image-check: R4369, R4370 and R4372 read from the full-size images, two blind passes plus reconciliation each
- [ ] retry: an image check of R1953 itself against DECODE's transcription where decoded spans break (rule 2)
Verdict: keep going: 3 internal gaps; cheapest next: pre-registered diagnosis of R4372's bigram-only signal on R1953, ~$5

## N4-HEL5 (4 Oct 2026): NA Fagel inv. 5177, Hellen's 1751 decipherments as known plaintext (account 2 worker for LANE-NEAR4)

Step run: NEAR3-VHEL's suggestion and A2.5's lead (De Leeuw 2000 ch. 8 n.32: English-deciphered copies of Hellen's letters
No 1-37, 30 Oct-28 Dec 1751, are in NA Fagel inv. 5177). Question: does 5177 carry Hellen's cipher beside the decipherments,
so that a pair could give known plaintext for codes 1-800?

**Catalogue record (step 1).** https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/5177 (4 Oct 2026 04:18 UTC):
`drupal-settings-json` -> `viewer.response`: unitid 5177, unittitle "1751-1752", **availability "DIGITALIZED"**, isDownloadable
true, 187 scans (file NL-HaNA_1.10.29_5177_0001.jpg ff.). Saved verbatim as `fagel5177/manifest_na5177.json`. Images through
the `iiif` URL of each scan on service.archief.nl (IIIF Image API).

**Volume map (step 2).** Odd scans 1-101 fetched at 700 px wide (51 requests), six contact sheets of 9 spreads each read (6
vision calls); seven header strips (scans 51, 53, 57, 59, 61, 65, 67, top 32% at 1600 px) read in the same sixth call budget
(one montage; 6 vision calls in total). Per-scan table: `fagel5177/letters.tsv`. What the volume holds in scans 1-101:
- **Hellen's letters to Frederick and Frederick's replies "Au Sr de Hellen", Oct-Dec 1751, in French clear text only** (scans
  5-49 and 67-93): headed "Mr de Hellen au Roi de Prusse, à la Haye le 9 Nov 1751" (35), "Ad Relat. 26, la Haye ce 19 Nov
  1751" with a P.S. "Le Greffier Fagel &c." (67), numbered "No 3x" headers in December (73, 79, 81) up to No 37 of 28 Dec
  (89, AUDIT 1); replies "Roy de Prusse au Sr de Hellen", Berlin/Potsdam, Nov-Dec 1751, signed "Federic" (13, 17, 19, 25, 27,
  39, 49, 69, 71, 77, 91), several with an endorsement slip on the facing page (17, 23, 31, 41, 49). The copies leave **dotted
  blanks** ("que . . . . a fait", "Mons. D . . . .") where a group was not read. **No cipher group, no interlinear and no
  facing cipher text appears on any Hellen page seen.**
- **Scans 51-65: a different correspondent's cipher, 1753.** Scan 51 is a covering note ("J'ai l'honneur de vous renvoier les
  Papiers que vous m'avez addressez hier au soir, parceque j'attens incessamment le Dechifre d'Angleterre ...") above a few
  lines of 3-digit groups; 53-65 are pages of 3-digit groups only, with a "Fagel 336" slip at 53 and the header "**No 59, le
  14 Novembre 1753, B. à St C.**" at 61 -- letters of "B." to "St C." (probably the French envoy Bonnac to Saint-Contest; the
  names are inferred from the initials, not read), bound into the 1751 run. Not Hellen; groups without decipherment.
- **Scans 95-101: Frederick to Michell (London), Dec 1751, in 4-digit groups** ("Au Sr Michell à Londres", signed "Federic"),
  with a covering note at 95. Not Hellen (Michell's code; cf. DECODE R1955/R1957, Frederick to Michell 28 Dec 1751,
  Non-decrypted).
Even scans 2-100 were not fetched (a letter that starts on an even scan has no header in this table); scans 102-187 were read
by AUDIT 1/AUDIT 2 (1752 Nos 71+, blanks).

**Ciphertexts elsewhere (step 3).** DECODE, login-free: the on-disk listings (`sources/decode/records-decrypted-2026-09-24.tsv`,
`records-non-decrypted-2026-09-24.tsv`, which includes "Partially decrypted"; 2,546 rows) plus a fresh `tools/decode_list.py
--status n/a` crawl today (700 of 718 N/A records; the last page returned no rows) have **no Hellen/Ellen record dated before
4 Jan 1752**: the only Hellen ciphers are R1953 (1752) and R1045-R1049/R1060/R1061 (1756, 1763), all KHA Prins Willem V inv.
196. No BL Add MS 32xxx Newcastle intercept of Hellen appears in any status. The 1751 KHA records are Michell's (R1051 decrypted,
R1955/R1957 Frederick to Michell 28 Dec 1751). Neighbouring Fagel volumes: AUDIT 2 already read the full finding aid (only 5177
and 5206 can hold Hellen decipherments of 1751-52); not repeated. **So no surviving 1751 Hellen ciphertext was located in 5177,
in DECODE (all four statuses) or in the Fagel series; the pairing test of step 3 (PREREG, held-out gate, interlinear_align) has
nothing to pair and was not run.**

**Can the 1751 plaintexts serve as cribs for R1953 (step 4)?** Partly, and only as context, not as code-value pairs. They are
the same writer to the same recipient in the same weeks: No 37 is dated 28 Dec 1751, R1953 is dated 4 Jan 1752, one week
later, and the replies of Frederick in the run answer the same reports. The topics overlap with what R4369 already reads in
R1953 (`phrases.txt`): the death of the Prince of Orange and the regency (scan 43 "la mort du Prince d'Orange"; R1953 "si feu
prince d'Orange"), the troop reduction (scan 15 "réduction des troupes"; R1953 "la reduction des troupes"), the Greffier Fagel
(scan 67) and the treaty negotiations (scans 15-19). What they cannot give is a code for any word: with no ciphertext of these
letters, nothing aligns. Two uses remain for a later job: (a) a writer- and week-matched French corpus (some 25 Hellen pages
and 15 reply pages in scans 5-93) for the codes 1-800 key-rebuild's language model and for an era/writer-matched judge corpus
(CLAUDE.md rule 3, the pt18 lesson), and (b) phrase cribs placed where R1953's decoded context (codes 801+) leaves a gap
whose neighbours match a phrase in the 1751 run -- probabilistic, graded M at best, and needing the key-rebuild's own control.
The dotted blanks also show London's 1751 decipherment left some groups unread; with no ciphertext beside them, which codes
those were cannot be said.

Requests: www.nationaalarchief.nl 1 (item page), service.archief.nl 58 (51 low-res scans + 7 header strips), de-crypt.org 16
(N/A listing pages, no login); all one at a time, >= 1.6-1.7 s apart, no 403/429/challenge. Subagent calls: 0. Vision calls: 6.
Images stay in the scratchpad (NA scans; re-fetchable from the manifest). Report what was found and where it was not found:
no Hellen 1751 ciphertext in 5177 (scans 1-101, odd scans), in DECODE's four status listings, or in the Fagel finding aid.
Lead for another target (Usage 7, not run): 5177 scans 95-101 copy Frederick's Dec 1751 cipher letters to Michell, and
DECODE R1955/R1957 (Frederick to Michell, 28 Dec 1751) are Non-decrypted; Michell's key is on file (`sibling_michell/`).

## Remaining gaps (N4-HEL5, 4 Oct 2026)
Read so far: 456 of 846 R1953 tokens carry a key value (H 152, S 304) plus M 16; 374 U (unchanged)
- codes 1-800 of the Hellen key (374 R1953 tokens) - blocker: not-attempted; R4370 and R4372 both fail the pre-registered test (READ2-HEL2, NEAR3-HEL4), R4372 with a bigram-only signal; no 1751 Hellen ciphertext survives beside Fagel 5177's clear copies, so that volume gives context, not code values (N4-HEL5); next: a pre-registered diagnosis of R4372's bigram signal, then a cryptanalytic key-rebuild of 1-800 with its own control, using the 5177 clear pages (scans 5-93) as a writer- and week-matched corpus, ~$5 then ~$10
- empty cells inside 801-1796 (14 tokens) and the 16 M tokens - blocker: open-codes; scattered codes the sheet leaves blank or the readers could not settle
- the 1756 letter (R1049) - blocker: not-attempted; R4376 (f.56, docket 1754, French table 1-500 with "la Haye", no holder) not yet tested; R4372 LR100 gave R1049 a uni-only p 0.010 (secondary, not gated); next: transcribe R4376 P3 and test on R1049 with R4372 as a pre-registered second candidate, ~$8
- the 1763 letters (R1045-R1048, R1060, R1061) - blocker: no-key-material; neither R4369, R4370 nor R4372 reads them, and no 1763 Hellen table has been found among the Add MS 32276 records looked at (post-1756 records R4381-R4408 not yet opened)

## Escalation (N4-HEL5, 4 Oct 2026)
- [x] siblings: Michell keys tested negative (FT4, FT4b); R4370 (f.46) and R4372 (f.48) tested negative as the first half (READ2-HEL2, NEAR3-HEL4); all 25 unopened Add MS 32276 records up to f.56 looked at (NEAR3-HEL3)
- [x] clear-pages: Fagel 5177's clear copies of Hellen's Oct-Dec 1751 letters looked at (N4-HEL5); no ciphertext of those letters survives in 5177, DECODE or the Fagel series, so they are context only, not a crib for R1953 itself
- [x] known-keys: R4369 transcribed and tested, reads R1953; R4370 and R4372 transcribed and tested, neither reads codes 1-800
- [x] print: Politische Correspondenz vols. 9-10 searched for the letter (check-solved sections above)
- [ ] key-rebuild: infer values for codes 1-800 from context in the R4369-decoded spans (cryptanalytic, needs its own control); first diagnose R4372's bigram-only signal; the 5177 clear pages are the matched corpus
- [x] image-check: R4369, R4370 and R4372 read from the full-size images, two blind passes plus reconciliation each
- [ ] retry: an image check of R1953 itself against DECODE's transcription where decoded spans break (rule 2)
Verdict: keep going: 3 internal gaps; cheapest next: pre-registered diagnosis of R4372's bigram-only signal on R1953, ~$5

## N4-HEL6 (4 Oct 2026): pre-registered diagnosis of R4372's bigram-only signal on R1953 (account 2 worker for LANE-NEAR4)

Step run: N4-HEL5's cheapest next. **Pre-registration** `key_r4372/PREREG_diag.md` (commit f5dd973f) was pushed before anything
was computed. Script `key_r4372/diag.py` (seeds 1 and 2, `--check` exits 0); the model, `words()` and `pmi()` are imported unchanged
from `sibling_michell/test_sibling.py`, and Part A reproduces NEAR3-HEL4's LR100 row (bi -0.525 on 42 pairs). Disk only: no
requests, no subagent or vision calls.

**Part A: which pairs carry the signal.** Order-shuffle mean -0.797, real -0.525 (order p 0.005 seed 1, 0.000 seed 2). Two pairs
are above the shuffle mean by more than the generic +0.797: "mon|peuple" (codes 414-422, PMI 3.24) and "trouvent|dans" (268-255,
2.40). Seventeen pairs score exactly 0, because one of their words is outside the fr18 vocabulary ("zero" seven times, "esperanc",
"consequen", "vigueurs", "sign."). The other 23 sit at the unseen-pair floor of -1.204. **Leave-out curve:** dropping "mon peuple"
alone raises order p to 0.030, and dropping both raises it to 0.140, so **k\* = 1**. The pre-registered artefact rule needs every
pair up to k\* to carry one mechanism tag: m1 repeated pair, m2 null, m3 doubled code, m4 function-word collocation. "mon peuple"
carries none of these, so **the rule did not fire**. Two repeated pairs exist, 540-774 "esperanc ami" x2 and 282-492 "feu presque"
x2, but they do not carry the excess.

**Part B: the gated context test.** It scores each R4372-decoded token (codes 1-800, nulls excluded) against the R4369 H/S words
on either side of it, so none of its junctions are in Part A's statistic. 93 codes, 139 tokens, J = 186 junctions.

| seed | S_B real | (i) R4372 values permuted: mean / p99 / p | (ii) R4370 values, size-matched: mean / p99 / p | power (R4369 held out at J=186) | gate |
|---|---|---|---|---|---|
| 1 | -0.794 | -0.814 / -0.658 / 0.310 | -0.794 / -0.636 / 0.460 | 1.00 | **FAIL** |
| 2 | -0.794 | -0.817 / -0.679 / 0.310 | -0.787 / -0.611 / 0.555 | 1.00 | **FAIL** |

The positive control is R4369's own 801+ values, each held out and scored against its H/S neighbours the same way. Over its full
pool of 502 junctions it reads -0.349, and subsampled to 186 it reaches p <= 0.01 in 200 of 200 draws. So at this N the test finds
a right key, and **R4372's values sit at the level of a permuted R4372 and of another 1751 French table (R4370)**. Per-code: 6 of
93 codes reach p <= 0.05 with n >= 2 junctions, against about 2.8 expected by chance. The gate failed, so PREREG B5 names none of
them as candidate values and grades nothing.

**Mechanism (not pre-registered, `key_r4372/diag_oov.py`, `diag_oov_output.txt`).** `pmi()` returns 0 when the left word is not in
fr18. That is above both the floor and the shuffle mean, so an abbreviated or null value scores better than a real French word
that has no attested continuation. In R1953's real order, 40.5% of the 42 covered pairs have an out-of-vocabulary word, against
25.2% (seed 2: 26.4%) under the order shuffle. Codes 405 "zero", 540 "esperanc" and 43 "consequen" sit next to other 1-800 tokens
more often than chance would place them. This is a property of where those codes stand in the ciphertext, whatever R4372 says
they mean. With those pairs set to the floor, the order p rises to 0.115 (seed 2: 0.105). With "mon peuple" also dropped, it is
0.505. **Verdict, by PREREG B5:** "R4372's values do not fit the R4369-decoded context beyond chance" (a control-backed negative,
target and controls side by side above, power 1.00). The bigram signal is not supported by the context check. Read outside the
pre-registration, it is one high-PMI pair plus the out-of-vocabulary scoring of clustered codes. It is not partial real values.
R4372 is retired as a source for codes 1-800, and **R4369's reading stands unchanged** (H 152 / S 304 / M 16 / U 374).
Tool note (Usage 7, not run): `test_sibling.py`'s `pmi()` should score an out-of-vocabulary left word at the unseen floor, not
at 0, before its bigram statistic gates anything else. R4369's own pass rests on its unigram p 0.000, which this does not touch.
Report what was found and where it was not found: no real codes 1-800 values were found in R4372 by the context check.

## Remaining gaps (N4-HEL6, 4 Oct 2026)
Read so far: 456 of 846 R1953 tokens carry a key value (H 152, S 304) plus M 16; 374 U (unchanged)
- codes 1-800 of the Hellen key (374 R1953 tokens) - blocker: not-attempted; R4370 and R4372 both fail the pre-registered test, and R4372's bigram-only signal is now diagnosed as one pair plus out-of-vocabulary scoring, with the context check at p 0.31-0.56 at power 1.00 (N4-HEL6); next: a cryptanalytic key-rebuild of 1-800 with its own control (context-fit anneal against the R4369-decoded neighbours, the Part B statistic as the objective and its held-out R4369 control as the gate), with the Fagel 5177 clear pages (scans 5-93) as a writer- and week-matched corpus, ~$10
- empty cells inside 801-1796 (14 tokens) and the 16 M tokens - blocker: open-codes; scattered codes the sheet leaves blank or the readers could not settle
- the 1756 letter (R1049) - blocker: not-attempted; R4376 (f.56, docket 1754, French table 1-500 with "la Haye", no holder) not yet tested; R4372 LR100 gave R1049 a uni-only p 0.010 (secondary, not gated); next: transcribe R4376 P3 and test on R1049 with R4372 as a pre-registered second candidate, ~$8
- the 1763 letters (R1045-R1048, R1060, R1061) - blocker: no-key-material; neither R4369, R4370 nor R4372 reads them, and no 1763 Hellen table has been found among the Add MS 32276 records looked at (post-1756 records R4381-R4408 not yet opened)

## Escalation (N4-HEL6, 4 Oct 2026)
- [x] siblings: Michell keys tested negative (FT4, FT4b); R4370 (f.46) and R4372 (f.48) tested negative as the first half (READ2-HEL2, NEAR3-HEL4, N4-HEL6 context check); all 25 unopened Add MS 32276 records up to f.56 looked at (NEAR3-HEL3)
- [x] clear-pages: Fagel 5177's clear copies of Hellen's Oct-Dec 1751 letters looked at (N4-HEL5); no ciphertext of those letters survives in 5177, DECODE or the Fagel series, so they are context only, not a crib for R1953 itself
- [x] known-keys: R4369 transcribed and tested, reads R1953; R4370 and R4372 transcribed and tested, neither reads codes 1-800; R4372's bigram signal diagnosed (N4-HEL6)
- [x] print: Politische Correspondenz vols. 9-10 searched for the letter (check-solved sections above)
- [ ] key-rebuild: infer values for codes 1-800 from context in the R4369-decoded spans (cryptanalytic, needs its own control); N4-HEL6's Part B statistic with its held-out R4369 positive control (power 1.00 at J=186) is a ready objective and gate; the 5177 clear pages are the matched corpus
- [x] image-check: R4369, R4370 and R4372 read from the full-size images, two blind passes plus reconciliation each
- [ ] retry: an image check of R1953 itself against DECODE's transcription where decoded spans break (rule 2)
Verdict: keep going: 3 internal gaps; cheapest next: cryptanalytic key-rebuild of codes 1-800 against the R4369-decoded context with its own held-out control, ~$10

## Remaining gaps (LANE-NEAR5 refresh, 4 Oct 2026)
Status unchanged: `partial`. R4372 (f.48) as a source for codes 1-800 stands as a control-backed negative (N4-HEL6 Part B: S_B -0.794
vs permuted-R4372 p 0.310 and size-matched R4370 p 0.460-0.555, power 1.00 at J=186); R4370 (f.46) likewise (READ2-HEL2, NEAR3-HEL4).
Both period tables are retired as instruments for codes 1-800 (rule 3 third-attempt clause: READ2-HEL2, NEAR3-HEL4 LR100, N4-HEL6 context
check, same family of test on the same tables); no further family run against either. New material that would reopen the period-key route:
a Hellen table carrying codes 1-800 of the R4369 series (the post-1756 Add MS 32276 records R4381-R4408 not yet opened, a Hellen key or
decipherment in the NA Fagel series beyond inv. 5177, or a recipient-side Prussian copy of the 1751-52 table), or an R1953-series letter
with its own clerk decipherment.
Read so far: 456 of 846 R1953 tokens carry a key value (H 152, S 304) plus M 16; 374 U (unchanged)
- codes 1-800 of the Hellen key (374 R1953 tokens) - blocker: not-attempted; the period-table route is retired (R4370, R4372, above); the one untried instrument is cryptanalytic, a key-rebuild of 1-800 with its own control; next: context-fit anneal against the R4369-decoded neighbours with N4-HEL6's Part B statistic as objective and its held-out R4369 control as gate, Fagel 5177 clear pages as matched corpus, ~$10
- empty cells inside 801-1796 (14 tokens) and the 16 M tokens - blocker: open-codes; scattered codes the sheet leaves blank or the readers could not settle
- the 1756 letter (R1049) - blocker: not-attempted; R4376 (f.56, docket 1754, French table 1-500, no holder) not yet tested; next: transcribe R4376 P3 and test on R1049 with a pre-registered gate and matched control (R4372 not used: retired above), ~$8
- the 1763 letters (R1045-R1048, R1060, R1061) - blocker: no-key-material; neither R4369, R4370 nor R4372 reads them, and no 1763 Hellen table has been found among the Add MS 32276 records looked at (post-1756 records R4381-R4408 not yet opened)

## Escalation (LANE-NEAR5 refresh, 4 Oct 2026)
- [x] siblings: Michell keys tested negative (FT4, FT4b); R4370 (f.46) and R4372 (f.48) tested negative as the first half (READ2-HEL2, NEAR3-HEL4, N4-HEL6 context check); all 25 unopened Add MS 32276 records up to f.56 looked at (NEAR3-HEL3)
- [x] clear-pages: Fagel 5177's clear copies of Hellen's Oct-Dec 1751 letters looked at (N4-HEL5); no ciphertext of those letters survives, so they are context only, not a crib for R1953 itself
- [x] known-keys: R4369 transcribed and tested, reads R1953; R4370 and R4372 retired for codes 1-800 after three tests of the same family (READ2-HEL2, NEAR3-HEL4, N4-HEL6)
- [x] print: Politische Correspondenz vols. 9-10 searched for the letter (check-solved sections above)
- [ ] key-rebuild: infer values for codes 1-800 from context in the R4369-decoded spans (cryptanalytic, a different instrument from the retired tables, needs its own control); N4-HEL6's Part B statistic with its held-out R4369 positive control is a ready objective and gate
- [x] image-check: R4369, R4370 and R4372 read from the full-size images, two blind passes plus reconciliation each
- [ ] retry: an image check of R1953 itself against DECODE's transcription where decoded spans break (rule 2)
Verdict: keep going: 3 internal gaps; cheapest next: cryptanalytic key-rebuild of codes 1-800 against the R4369-decoded context with its own held-out control, ~$10

## N5-HEL7 (4 Oct 2026): context-fit key-rebuild of codes 1-800, control first (account 2 worker for LANE-NEAR5)

Step run: the LANE-NEAR5 refresh's cheapest next. A different instrument from the retired period tables (R4370, R4372 not used):
cryptanalytic, grade S at best. **Pre-registration** `key_rebuild/PREREG-HEL7.md` (commit e72d62c7) pushed before any run. Disk only:
no requests, no subagent or vision calls.

**Tool fix first.** `sibling_michell/test_sibling.py` now has `fr18_counts()`, `pmi_from(u, b, oov_floor)` and `bigram(oov_floor=False)`;
with `oov_floor=True` an out-of-vocabulary left word scores at the unseen floor log(0.3) = -1.204 (N4-HEL6's tool note). The default is
unchanged, so earlier outputs reproduce (`key_r4372/diag.py --check`: up to date). Offline test `key_rebuild/test_oov.py`: OK.

**Instrument.** `key_rebuild/rebuild.py` (`--check` exits 0): Gibbs anneal assigning one word from the fr18 top 800 types to each free
code. 80 sweeps at T 1.5 -> 0.05, then 5 greedy sweeps, seeds 1-3. The objective sums junction scores over every adjacent pair that
touches a free code, against the R4369 H/S context (452 tokens with a word). Arm P: Part B PMI with the OOV floor. Arm L: log conditional
bigram probability. Target: 349 tokens, 201 codes, profile 1:133 2:38 3:10 4:9 5+:11.

**Control (rule 3; matched).** The 182 codes 801+ with an H/S word token in R1953 were blanked one tenth at a time (10 folds), with the
201 target codes free as in the target run. This keeps the context density at the target's. Recovery was weighted to the target's
occurrence profile (R_w) and compared with a shuffled-assignment baseline (200 permutations per fold). The PREREG said 183 codes; one has
no word value, so 182. Ceiling: 129 of 182 (0.71) of the true values are a single word in V.

| arm | seed | control R_w | shuffled baseline | unweighted | token-weighted | gate (R_w >= 0.20 and >= 3x baseline) |
|---|---|---|---|---|---|---|
| P (PMI) | 1 / 2 / 3 | 0.011 / 0.008 / 0.011 | 0.0015 / 0.0007 / 0.0011 | 0.011 / 0.005 / 0.011 | 0.020 / 0.002 / 0.020 | mean 0.010 vs 0.20: **FAIL** |
| L (log cond.) | 1 / 2 / 3 | 0.034 / 0.023 / 0.033 | 0.0060 / 0.0062 / 0.0053 | 0.049 / 0.027 / 0.038 | 0.104 / 0.055 / 0.069 | mean 0.030 vs 0.20: **FAIL** |

What the control does recover is function words only: une, le, de, les, l, d, n, il, ce (arm L), and une, le (arm P). These are 1 to 9 of
182 codes against a ceiling of 129. Both arms miss the 0.20 floor by a factor of 7 or more. Each is above 3x its own shuffled baseline,
but that is not enough on its own. **Per PREREG 4: no target run, no candidate values, no reading change** (`target_candidates.tsv` is
header-only). Verdict: **untestable by this instrument (context-fit anneal over fr18 top-800 bigrams) at this N.** This is not a
negative about codes 1-800. **R4369's reading stands unchanged** (H 152 / S 304 / M 16 / U 374). Report what was found and where it
was not found: no values for codes 1-800 were found, because the instrument cannot recover known values at this context density.
Reading outside the pre-registration, not gated: a bigram context model over a single letter cannot place content words. Either more
text of the same code is needed (a sibling letter in the R4369 series) or a writer-matched source of whole phrases is needed (Fagel 5177
transcribed, for phrase cribs) before a key-rebuild has a chance.

## Remaining gaps (N5-HEL7, 4 Oct 2026)
Read so far: 456 of 846 R1953 tokens carry a key value (H 152, S 304) plus M 16; 374 U (unchanged)
- codes 1-800 of the Hellen key (374 R1953 tokens) - blocker: not-attempted; period tables R4370/R4372 retired (rule 3); the context-fit anneal over fr18 bigrams is untestable at this N (N5-HEL7: control R_w 0.010 / 0.030 against a 0.20 gate, ceiling 0.71); next: transcribe Fagel 5177's clear Hellen pages (scans 5-93, two blind passes + reconciliation) as a writer- and week-matched phrase corpus, then a pre-registered phrase-crib placement in the R4369-decoded gaps with its own held-out control, ~$12
- empty cells inside 801-1796 (14 tokens) and the 16 M tokens - blocker: open-codes; scattered codes the sheet leaves blank or the readers could not settle
- the 1756 letter (R1049) - blocker: not-attempted; R4376 (f.56, docket 1754, French table 1-500, no holder) not yet tested; next: transcribe R4376 P3 and test on R1049 with a pre-registered gate and matched control (R4372 not used: retired), ~$8
- the 1763 letters (R1045-R1048, R1060, R1061) - blocker: no-key-material; neither R4369, R4370 nor R4372 reads them, and no 1763 Hellen table has been found among the Add MS 32276 records looked at (post-1756 records R4381-R4408 not yet opened)

## Escalation (N5-HEL7, 4 Oct 2026)
- [x] siblings: Michell keys tested negative (FT4, FT4b); R4370 (f.46) and R4372 (f.48) tested negative as the first half (READ2-HEL2, NEAR3-HEL4, N4-HEL6 context check); all 25 unopened Add MS 32276 records up to f.56 looked at (NEAR3-HEL3)
- [x] clear-pages: Fagel 5177's clear copies of Hellen's Oct-Dec 1751 letters looked at (N4-HEL5); no ciphertext of those letters survives, so they are context only, not a crib for R1953 itself
- [x] known-keys: R4369 transcribed and tested, reads R1953; R4370 and R4372 retired for codes 1-800 after three tests of the same family (READ2-HEL2, NEAR3-HEL4, N4-HEL6)
- [x] print: Politische Correspondenz vols. 9-10 searched for the letter (check-solved sections above)
- [ ] key-rebuild: the fr18-bigram context-fit anneal was tried with its control first and is untestable at this N (N5-HEL7, control R_w 0.010 / 0.030 vs gate 0.20); untried instrument: phrase-crib placement from a transcribed Fagel 5177 writer-matched corpus, with its own held-out control
- [x] image-check: R4369, R4370 and R4372 read from the full-size images, two blind passes plus reconciliation each
- [ ] retry: an image check of R1953 itself against DECODE's transcription where decoded spans break (rule 2)
Verdict: keep going: 3 internal gaps; cheapest next: transcribe R4376 P3 and test it on R1049 with a matched control, ~$8

## N6-HEL76 (4 Oct 2026): R4376 (f.56, 1754) P3 transcribed and tested on R1049 (7 Sept 1756) (account 2 worker for LANE-NEAR6)

Step run: the N5-HEL7 verdict's cheapest next. **Pre-registration** `key_r4376/PREREG.md` (commit a6f0668b) was pushed before the image
was fetched. It copies NEAR3-HEL4's method (four attributions, k = 4, uni value-shuffle + bi order-shuffle, power from fr18 prose encoded
with the key and subsampled to R1049's own covered count and pair count). Two changes, both stated before any run: "zero" nulls are
dropped from the gated keys (N4-HEL6), and the bigram uses N5-HEL7's OOV floor (`test_sibling.py --key ... --oov-floor`, an option added
in commit 622ce49c; the default is unchanged). R4370 and R4372 were not used (retired).
**Route:** one DECODE browser login (`tools/decode_browser_login.js 4376 <scratchpad> --delay 1700 --max-files 1 --fetch <P3 filesrv URL>`).
P3 sha1 84ef4ad7... matches `images/decode/manifest.json`. The image stays in the scratchpad (not public domain), and the account name
is in no file. Requests: de-crypt.org about 5 (login page, submit, landing, RecordsView/4376, 1 image), 1.7 s apart, no challenge; no
other host.

**What the sheet is.** P3 carries codes 1-500 in five blocks of 100 on the same kind of printed form as R4369/R4372. There are left
entries plus right-aligned right entries ending in a dash. A strip LEFT of block 1-100 holds right entries whose dashes point at codes
1-100, and the right page edge shows a 501-600 number column whose own entries are cut off. The sheet is densely filled with "zero"
nulls (78 cells). Names in it include Newcastle, Holdernesse, Guy Dickens, Colloredo, Bestuchef (?), "le Ministere", "la France",
"la G.de Bret.g", "Hollandois", "pays bas", "la Haye", "Livres St.g", "le R.y d'Ang.re" and "elect.r d'Han.re", which point to an
Anglo-Austrian-Russian context of the mid-1750s. No holder is named.
**Transcription.** Crops: `python3 tools/iiif_lines.py --image <P3 file> --out <scratchpad>/crops --region <x>,250,<w>,5100 --centres
500,1500,2500,3480,4500 --prefix P3_c<b> --debug`, once per block (x/w 230/1040, 1250/780, 2000/770, 2740/780, 3480/951). That gave
25 crops of 20 rows each, all cut before any subagent call. Two blind Sonnet passes (the second in reverse block order) saw only the
crop paths. Code-keyed diff (letters only): **err_2reader 0.113 (70/617 cells; raw 78)**. Most splits are about which row a right entry
sits on, or are cut 501-600 stubs. I settled 41 cells (row placements included) from two strip montages and one crop (e.g. 268 "p", 115 R "le Ministere",
222/223 R "est"/"royaume", 98/99 R "propre"/"~convenable", 89 "Livres St.g"). The other 29 take one pass's cell at grade M.
`key_r4376/key.tsv`: 480 rows, 609 cells, **H 507 / M 102**. err_true is not measurable (no benchmark item of this hand). Conventions
are in `key_r4376/README.md`.
**Gate B (coverage):** LR100 covers 145 R1049 tokens (L 121, R0 70, R100 91). The gate (54) is met.

**Test** (seed 1; full rows in `key_r4376/test_key_*.txt` and HYPOTHESES.md):

| R4376 key on R1049 | covered | uni real / shuffle mean | uni p | pairs | bi real / order-shuffle mean | bi order p | power uni / bi | verdict |
|---|---|---|---|---|---|---|---|---|
| L | 121 | -9.572 / -9.349 | 0.705 | 21 | -0.910 / -1.042 | 0.155 | 1.00 / 0.98 | fail |
| R0 | 70 | -9.529 / -9.730 | 0.350 | 9 | -1.090 / -1.018 | 0.485 | 1.00 / 0.90 | fail |
| R100 | 91 | -9.870 / -9.599 | 0.695 | 14 | -1.204 / -1.076 | 1.000 | 1.00 / 0.97 | fail |
| LR100 | 145 | -9.905 / -9.602 | 0.830 | 35 | -1.159 / -1.086 | 0.840 | 1.00 / 1.00 | fail |
| *for scale: R4369 LR100 on R1953 (READ2-HEL)* | 470 | -7.017 / -9.157 | 0.000 | | -0.361 / -0.694 | 0.000 | 1.00 / 1.00 | pass |

With nulls kept (`key_<X>_z`, reported, not gated), R1049's uni p is 0.64-0.89 and its bi order p 0.14-1.00. Seed 2 was not run,
because a pass has to hold on both seeds and seed 1 already fails. Secondary rows (not gated): the only cell at or under 0.0125 among
the other seven letters is R0 on R1953, bi order p 0.000 on 9 pairs. Its uni p there is 0.915, so it fails, and R1953's codes 1-500
belong to a different, 1751 key series in any case.

**Result.** At power 0.90-1.00, no attribution of R4376 reads R1049: **R4376 is not the key of the 7 Sept 1756 letter** (a pre-registered,
control-backed FAIL, conditional on DECODE's transcription of R1049, rule 2). R1049 now has no reading from R4369, R4372 or R4376.
No reading was built (PREREG item 6). Calls: 2 Sonnet subagent passes, plus my own reads (1 page overview, 1 crop check, 2
reconciliation montages, 1 detail crop). Report what was found and where it was not found: R1049's codes 1-600 have no key on R4376 P3.
The sheet's names (Newcastle, Holdernesse, Colloredo, Guy Dickens) suggest an English-Austrian table of about 1754. That is inference,
not tested. It is the reading of a next step (a holder search), not a conclusion.

## Remaining gaps (N6-HEL76, 4 Oct 2026)
Read so far: 456 of 846 R1953 tokens carry a key value (H 152, S 304) plus M 16; 374 U (unchanged)
- codes 1-800 of the Hellen key (374 R1953 tokens) - blocker: not-attempted; period tables R4370/R4372 retired (rule 3); the context-fit anneal over fr18 bigrams is untestable at this N (N5-HEL7: control R_w 0.010 / 0.030 against a 0.20 gate, ceiling 0.71); next: transcribe Fagel 5177's clear Hellen pages (scans 5-93, two blind passes + reconciliation) as a writer- and week-matched phrase corpus, then a pre-registered phrase-crib placement in the R4369-decoded gaps with its own held-out control, ~$12
- empty cells inside 801-1796 (14 tokens) and the 16 M tokens - blocker: open-codes; scattered codes the sheet leaves blank or the readers could not settle
- the 1756 letter (R1049) - blocker: not-attempted; R4369, R4372 and R4376 (N6-HEL76: LR100 uni p 0.830, bi order p 0.840 at power 1.00) do not read it; next: open the post-1756 Add MS 32276 key records R4381-R4408 (contact sheet first, as NEAR3-HEL3) for a table that carries R1049's codes, ~$4
- the 1763 letters (R1045-R1048, R1060, R1061) - blocker: no-key-material; neither R4369, R4370, R4372 nor R4376 reads them, and no 1763 Hellen table has been found among the Add MS 32276 records looked at (post-1756 records R4381-R4408 not yet opened)

## Escalation (N6-HEL76, 4 Oct 2026)
- [x] siblings: Michell keys tested negative (FT4, FT4b); R4370 (f.46) and R4372 (f.48) tested negative as the first half (READ2-HEL2, NEAR3-HEL4, N4-HEL6 context check); all 25 unopened Add MS 32276 records up to f.56 looked at (NEAR3-HEL3)
- [x] clear-pages: Fagel 5177's clear copies of Hellen's Oct-Dec 1751 letters looked at (N4-HEL5); no ciphertext of those letters survives, so they are context only, not a crib for R1953 itself
- [ ] known-keys: R4369 reads R1953; R4370 and R4372 retired for codes 1-800; R4376 tested on R1049 and fails (N6-HEL76); the post-1756 Add MS 32276 records R4381-R4408 are not yet looked at for R1049 and the 1763 letters
- [x] print: Politische Correspondenz vols. 9-10 searched for the letter (check-solved sections above)
- [ ] key-rebuild: the fr18-bigram context-fit anneal was tried with its control first and is untestable at this N (N5-HEL7, control R_w 0.010 / 0.030 vs gate 0.20); untried instrument: phrase-crib placement from a transcribed Fagel 5177 writer-matched corpus, with its own held-out control
- [x] image-check: R4369, R4370, R4372 and R4376 read from the full-size images, two blind passes plus reconciliation each
- [ ] retry: an image check of R1953 itself against DECODE's transcription where decoded spans break (rule 2)
Verdict: keep going: 3 internal gaps; cheapest next: open the post-1756 Add MS 32276 key records R4381-R4408 (contact sheet first) for R1049 and the 1763 letters, ~$4

## N6-HEL81 (4 Oct 2026): contact sheet of Add MS 32276 key records R4381-R4408 for R1049 and the 1763 letters (account 2 worker for LANE-NEAR6)

Step run: N6-HEL76's named cheapest next. Intake gate `python3 tools/intake_gate_check.py hellen-frederick-1752` rc=0:
`hellen-frederick-1752: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
No transcription, test or grades in this job. **No login**: DECODE's RecordsView pages turned out to be public (sender, receiver,
cipher type, start year and the 200px `TH_IMG_*` thumbnails all serve without an account), so the 28 RecordsView pages and their 128
thumbnails were fetched with plain curl (de-crypt.org, 155 requests, 1.7 s apart, no challenge; no other host). Thumbnails stay in the
scratchpad. Result per record: `key_search/R4381-R4408.tsv`.

**What was found.** No record in R4381-R4408 names Hellen/Ellen, and none carries a DECODE date of 1756 or 1763. Named holders: Knyphausen
(and Michell) in London 1761-62 (R4381, R4385), Hertzberg to Knyphausen 1762 (R4384, running text, not a table), Bandouin? 1764-65
(R4387, R4390), Thulemeyer 1767/1781, Maltzan 1769-70, Lusi 1784, Schlieffen, Alvensleben 1789, Rehern? 1791, Jacobi 1794. Eight records
are undated/unnamed (R4382, R4386, R4388, R4399, R4401, R4403, R4405, R4406). Almost every record is the same two-page printed form
(five bands per page, as R4369/R4372), i.e. about 1000 codes per record by the R4369 precedent (801-1796 on two pages); R4391 and R4398
(1765, 1770) are 11-page handwritten working lists. **Dockets and band heads are not legible at 200 px** (checked at 3x enlargement),
so no header, holder or code range could be read from a thumbnail.
**Fit.** Code ranges needed: R1049 median 701, 98th percentile 1990, max 3113; the 1763 letters medians 918-1242, 98th pct 3623-3812,
max ~3920 (stray 5627/9858). No single two-page record can cover the 1763 range; a fit would be one record of a multi-record set, as
R4372+R4369 were for 1752. **R1049 (1756): no candidate here** -- the 1756 sheets are R4377-R4379 (ff.58-62, already looked at), and
everything from f.66 on is 1761 or later. **1763 letters: two positional candidates only**, R4386 (f.75, homophonic nomenclator, no
sender/receiver/date) bound between 1762 (f.73) and 1764 (f.77), and more weakly R4388 (f.79). Nothing in the metadata or the thumbnails
ties either to Hellen or to 1763, so no full-size fetch was made (the brief allows one only for a record that fits).
**Where it was not found:** RecordsView metadata and thumbnails of all 28 records R4381-R4408 (no Hellen, no 1756/1763 date).

**Next (not run):** one DECODE browser login fetching full-size P1 docket and P2 top band of R4386 and R4388 only (4 images), to read the
docket/holder and the band-head code range -- a contact-sheet read, no transcription, ~$3. Transcription follows only if a docket names
Hellen or La Haye and a band head reaches above 1800.

## Remaining gaps (N6-HEL81, 4 Oct 2026)
Read so far: 456 of 846 R1953 tokens carry a key value (H 152, S 304) plus M 16; 374 U (unchanged)
- codes 1-800 of the Hellen key (374 R1953 tokens) - blocker: not-attempted; period tables R4370/R4372 retired (rule 3); the context-fit anneal over fr18 bigrams is untestable at this N (N5-HEL7); next: transcribe Fagel 5177's clear Hellen pages (scans 5-93, two blind passes + reconciliation) as a writer- and week-matched phrase corpus, then a pre-registered phrase-crib placement in the R4369-decoded gaps with its own held-out control, ~$12
- empty cells inside 801-1796 (14 tokens) and the 16 M tokens - blocker: open-codes; scattered codes the sheet leaves blank or the readers could not settle
- the 1756 letter (R1049) - blocker: no-key-material; R4369, R4372 and R4376 do not read it (N6-HEL76), the 1756 sheets R4377-R4379 are tallies/empty or Michel's, and no record in R4381-R4408 is dated 1756 or names Hellen (N6-HEL81); no further Add MS 32276 record remains unopened
- the 1763 letters (R1045-R1048, R1060, R1061) - blocker: not-attempted; no Hellen or 1763 record in R4381-R4408 by metadata and thumbnails (N6-HEL81), but undated R4386 (f.75, between 1762 and 1764) and R4388 (f.79) are unread positional candidates; next: one DECODE login, full-size P1 docket + P2 top band of R4386 and R4388 (4 images), read holder and code range, ~$3

## Escalation (N6-HEL81, 4 Oct 2026)
- [x] siblings: Michell keys tested negative (FT4, FT4b); R4370 (f.46) and R4372 (f.48) tested negative as the first half (READ2-HEL2, NEAR3-HEL4, N4-HEL6 context check); all Add MS 32276 records looked at, up to f.56 (NEAR3-HEL3) and R4381-R4408 by metadata and thumbnails (N6-HEL81)
- [x] clear-pages: Fagel 5177's clear copies of Hellen's Oct-Dec 1751 letters looked at (N4-HEL5); context only, not a crib for R1953 itself
- [ ] known-keys: R4369 reads R1953; R4370 and R4372 retired for codes 1-800; R4376 fails on R1049 (N6-HEL76); R4386/R4388 full-size dockets not yet read for the 1763 letters (N6-HEL81)
- [x] print: Politische Correspondenz vols. 9-10 searched for the letter (check-solved sections above)
- [ ] key-rebuild: the fr18-bigram context-fit anneal is untestable at this N (N5-HEL7); untried instrument: phrase-crib placement from a transcribed Fagel 5177 writer-matched corpus, with its own held-out control
- [x] image-check: R4369, R4370, R4372 and R4376 read from the full-size images, two blind passes plus reconciliation each
- [ ] retry: an image check of R1953 itself against DECODE's transcription where decoded spans break (rule 2)
Verdict: keep going: 3 internal gaps; cheapest next: one DECODE login for the full-size dockets and band heads of R4386 and R4388 (1763 candidates by binding position), ~$3

## N7-HELDK (4 Oct 2026): full-size dockets and band heads of R4386 (f.75) and R4388 (f.79) for the 1763 letters (account 2 worker for LANE-NEAR7)

Step run: N6-HEL81's named next. Intake gate (pasted by LANE-NEAR7, rc=0): `hellen-frederick-1752: partial (line 1) -- edition/page or
full-text-search citation found within 6 lines`. One DECODE browser login (`tools/decode_browser_login.js 4386 OUT --guess-fullsize
--fetch-page .../RecordsView/4388`): **full-size images served for both records** (8 pages, no forbidden.png). Not committed (BL images,
"not in the public domain"); kept in the session scratchpad only. Sha1 / native px:
R4386 P1-P4 117a5047a84081843ee234cee7c8c670d654ae7e, a9b8eda30c52775f81b3392186e20437042abc3f, cde8d04b66b59dda8cf830039c281bf28043a965,
7bc04b644e0eb59147295b6d1e0ac14fbba2e18b (3936-4083 x 5352-5361); R4388 P1-P4 3c99e61e2e8f79517a1a71ff060d0866f6d1a8b8,
6a7ab114baf8078a39646768bf51f98f1da1a590, 2f05358d1b3e7f0eff06252aba6f2e14c045a3a0, c7f4857fbe520c1bd533f25989ab869d38626bf9
(3736-3802 x 5262-5268). No transcription, no grades, no key test (brief). Result per record: `key_search/R4386-R4388.tsv`.

**What was found (one reader, by eye).**
- Neither record has a legible docket: R4386 P1 is the blank ruled back of the form with one faint, illegible two-word line; R4388 P1
  and P4 are blank. No holder, no date, no "Hellen" or "La Haye" docket on either.
- Both are filled French tables on the usual printed 1-1000 form, re-numbered by handwritten hundreds heads above each column, so the
  codes are four-digit, as the 1763 letters are.
- **R4388 = codes 2001-3900**: words right of the printed numbers read 2001-3000 (heads 2000, 210, ..., 290), words left of them read
  3101-3900 (heads 310, ..., 390), and a pasted strip carries 3001-3100. Scrambled (two-part) order. Names in cells: Lord Bute, le Duc de
  New[castle], Mr Pitt, Grenville, l'Opposition, la Haye, le Roi d'Angl., l'Imp. de Russie, le Roi de Dann., Ministere Autrich., Stockholm,
  Varsovie, Pologne, Versailles, Silesie -- a set that points to about 1762-63 (inference from names; no date on the sheet).
- **R4386 = about codes 1201-2200** (heads 120-190 over columns 3-10, 200 and 210 over columns 1-2, column 2 written 1101-1200; the head
  placement is not fully clear from one read). One-part, alphabetical (a ... n), with letter strings beside many printed numbers
  (e.g. "403-acfmpu", "910-abcdeg..."). Names: Bedford Duc, Conway, Choiseul, le Chev. Macartney, le Chev. Mitchel, le Sr Pitt, Temple,
  le Stadhouder, Yorke Gen., Winchelsea, Dutch Min. "Chev. Macartney" (knighted 1764) and Conway point to 1764 or later (inference).

**Fit to the 1763 letters (R1045-R1048, R1060, R1061).** Token share by band (pool of six letters, from ciphertext_R*.txt): 1-1200
55-63%, 1201-2000 6-13%, 2001-3000 13-21%, 3001-3100 1-3%, 3101-3900 9-10%. R4388's range covers the letters' upper codes (26-35% of
tokens); R4386 covers only the 1201-2000 band and by its names probably postdates 5 Jul 1763. **Indication against R4388 (not a test):**
on the 3001-3100 strip, which one read sees with about 32 of 100 cells blank (3003, 3005, 3006, 3011, 3012, 3017, 3018, 3020, 3022, 3026,
3027, 3029, 3033, 3035, 3037, 3038, 3042, 3051, 3056, 3057, 3060, 3061, 3064, 3066, 3067, 3071-3073, 3076, 3083, 3093, 3096), 11 of the 28
1763 tokens in that range (7 of 18 distinct codes: 3005 x2, 3011, 3035, 3037 x4, 3057, 3066, 3067) fall on blank cells -- about the
random base rate, against about 3% empty-cell tokens for the true-key precedent (R4369 on R1953: 14 of about 486 in-range tokens). That is
one reader, N=28, and no registered gate, so it is logged as an indication, not a negative (rule 3).

**Where it was not found:** no Hellen/La Haye holder or 1763 date on R4386 or R4388 at full size (dockets, band heads, P1/P4).

**Next (not run, priced):** the cheapest discriminating step is a pre-registered **blank-cell test** of R4388 for the 1763 pool: read
filled/blank (not the words) for only the distinct 2001-3900 codes the six letters use (about 180 cells, `tools/iiif_lines.py --image`
column crops, two blind Sonnet passes + one reconciliation = 3 units, ~USD 4), gate registered before reading: a true key puts <=10% of
tokens on blank cells (R4369/R1953 precedent ~3%), a random key the sheet's base rate (~30%); control = the same count over value-shuffled
codes. Only if it passes: transcribe R4388 in full (about 1900 cells, ~USD 12) and run `decode_key.py --key` with the value-shuffle
control. R4386 is not worth a test before a 1763 dating or a pass on R4388. Requests: de-crypt.org 18 (1 login + RecordsView 4386, 4388,
8 thumbnails, 8 full-size), 1.7 s apart, no challenge. Subagent calls: 0.

## Remaining gaps (N7-HELDK, 4 Oct 2026)
Read so far: 456 of 846 R1953 tokens carry a key value (H 152, S 304) plus M 16; 374 U (unchanged)
- codes 1-800 of the Hellen key (374 R1953 tokens) - blocker: not-attempted; period tables R4370/R4372 retired (rule 3); the context-fit anneal over fr18 bigrams is untestable at this N (N5-HEL7); next: transcribe Fagel 5177's clear Hellen pages (scans 5-93, two blind passes + reconciliation) as a writer- and week-matched phrase corpus, then a pre-registered phrase-crib placement in the R4369-decoded gaps with its own held-out control, ~$12
- empty cells inside 801-1796 (14 tokens) and the 16 M tokens - blocker: open-codes; scattered codes the sheet leaves blank or the readers could not settle
- the 1756 letter (R1049) - blocker: no-key-material; R4369, R4372 and R4376 do not read it (N6-HEL76), the 1756 sheets R4377-R4379 are tallies/empty or Michel's, and no record in R4381-R4408 is dated 1756 or names Hellen (N6-HEL81); no further Add MS 32276 record remains unopened
- the 1763 letters (R1045-R1048, R1060, R1061) - blocker: not-attempted; R4388 (f.79) is a filled French table for codes 2001-3900 with c.1762-63 names but no holder or date, and its 3001-3100 strip puts 11 of 28 1763 tokens on blank cells (indication, one reader); R4386 is alphabetical 1201-2200, probably 1764+ (N7-HELDK); next: pre-registered blank-cell test of R4388 on the ~180 distinct 2001-3900 codes the 1763 pool uses, two blind passes + reconciliation with a value-shuffle control, ~$4

## Escalation (N7-HELDK, 4 Oct 2026)
- [x] siblings: Michell keys tested negative (FT4, FT4b); R4370 (f.46) and R4372 (f.48) tested negative as the first half (READ2-HEL2, NEAR3-HEL4, N4-HEL6 context check); all Add MS 32276 records looked at, up to f.56 (NEAR3-HEL3), R4381-R4408 by metadata and thumbnails (N6-HEL81), R4386 and R4388 at full size (N7-HELDK)
- [x] clear-pages: Fagel 5177's clear copies of Hellen's Oct-Dec 1751 letters looked at (N4-HEL5); context only, not a crib for R1953 itself
- [ ] known-keys: R4369 reads R1953; R4370 and R4372 retired for codes 1-800; R4376 fails on R1049 (N6-HEL76); R4388 (2001-3900, c.1762-63 names) not yet tested on the 1763 letters, blank-cell test first (N7-HELDK)
- [x] print: Politische Correspondenz vols. 9-10 searched for the letter (check-solved sections above)
- [ ] key-rebuild: the fr18-bigram context-fit anneal is untestable at this N (N5-HEL7); untried instrument: phrase-crib placement from a transcribed Fagel 5177 writer-matched corpus, with its own held-out control
- [x] image-check: R4369, R4370, R4372 and R4376 read from the full-size images, two blind passes plus reconciliation each
- [ ] retry: an image check of R1953 itself against DECODE's transcription where decoded spans break (rule 2)
Verdict: keep going: 3 internal gaps; cheapest next: pre-registered blank-cell test of R4388 (codes 2001-3900) on the 1763 pool, ~$4

## N7-HELBC (4 Oct 2026): pre-registered blank-cell test of R4388 (f.79, codes 2001-3900) on the 1763 letters (account 2 worker for LANE-NEAR7)

Step run: N7-HELDK's named next. PREREG `key_r4388/PREREG-N7HELBC.md` pushed 1c8e6c67 before the images were fetched; the cell list
(`cells.tsv`, 270 target + 100 null codes, seed 4388) cf957cfd before reading; addendum A (a "zero" sub-state, geometry) 7832fb26/8e6b86fc
before any pass result. One DECODE browser login (`--guess-fullsize`), R4388 P1-P4 full size to scratch only (not committed; same sha1s as
N7-HELDK). Units stated in ROOM before the first subagent call: 2 blind Sonnet passes (one call each over 24 tiles of 16 three-row bands,
`key_r4388/crop_cells.py`) + 1 reconciliation by this worker.

**Target set.** The six 1763 letters, clean all-digit tokens only: 396 tokens / 270 distinct codes in 2001-3900 (the brief's "~180" was
an estimate; 270 stated in the PREREG before reading).

**Reading.** err_2reader 29/350 = 0.083 (classes F+Z / B / X; 20 cells `?` for pass A). The strip bands (3001-3100) were cut 2-3 rows off
by my strip geometry (both readers said so), so all 24 strip cells in the list were re-read by me from an aligned full-resolution view of
the strip (flag `r`, note in `settle.tsv`); the other 29 disagreements were settled from their crops. Six cells carry only an ink blot
after the number (X: 2407, 2491, 2520, 2593, 2760, 2853). Result per cell: `key_r4388/cells_read.tsv` (A, B, settled state, flag).

**Result** (`python3 key_r4388/blank_test.py --score`, output in `key_r4388/score.txt`):

| | S (blank-cell token share) | null at random code positions (100 cells, p0) | null p01 / p05 / median | control R4369 on R1953 at N=396, p95 / p99 | verdict |
|---|---|---|---|---|---|
| X as filled (primary) | 125/396 = **0.316** | 0.340 | 0.260 / 0.283 / 0.338 | 0.048 / 0.056 (power OK) | **FAIL** |
| X as blank (sensitivity) | 129/396 = 0.326 | 0.370 | 0.288 / 0.311 / 0.369 | 0.048 / 0.056 | FAIL |

Strip 3001-3100 alone (not gated): 11/28 = 0.393, the same figure N7-HELDK saw by one reader. Not gated: 28 of the 270 target cells and 7
of the 100 null cells carry the word "zero" (38 of 396 target tokens on "zero" cells).

**Verdict (pre-registered rule): FAIL -- R4388 is retired as the key of the 1763 letters (instrument: blank-cell test).** The 1763 tokens
fall on blank cells at the sheet's own base rate (0.316 vs null median 0.338); a key that enciphered them would leave about 3-6% (control
p99 0.056 at the same N). Rule 3: the control can differ on this statistic (it sits ~5x lower) and does. No full transcription of R4388.

**Where it was not found:** R4388 does not carry the 1763 code values (this test); no docket, holder or date on R4386/R4388 (N7-HELDK).
Untried: R4386 (alphabetical 1201-2200, names point to 1764+) under the same instrument on the 1201-2000 band (63 distinct codes / 121 clean
tokens; control power to be re-checked at that N), ~$3, low prior. Requests: de-crypt.org about 10 (1 login + RecordsView 4388 + 4 thumbnails + 4 full-size), no
challenge. Subagent calls: 2 (Sonnet). Cost: see the lane ledger.

## Remaining gaps (N7-HELBC, 4 Oct 2026)
Read so far: 456 of 846 R1953 tokens carry a key value (H 152, S 304) plus M 16; 374 U (unchanged)
- codes 1-800 of the Hellen key (374 R1953 tokens) - blocker: not-attempted; period tables R4370/R4372 retired (rule 3); the context-fit anneal over fr18 bigrams is untestable at this N (N5-HEL7); next: transcribe Fagel 5177's clear Hellen pages (scans 5-93, two blind passes + reconciliation) as a writer- and week-matched phrase corpus, then a pre-registered phrase-crib placement in the R4369-decoded gaps with its own held-out control, ~$12
- empty cells inside 801-1796 (14 tokens) and the 16 M tokens - blocker: open-codes; scattered codes the sheet leaves blank or the readers could not settle
- the 1756 letter (R1049) - blocker: no-key-material; R4369, R4372 and R4376 do not read it (N6-HEL76), the 1756 sheets R4377-R4379 are tallies/empty or Michel's, and no record in R4381-R4408 is dated 1756 or names Hellen (N6-HEL81); no further Add MS 32276 record remains unopened
- the 1763 letters (R1045-R1048, R1060, R1061) - blocker: not-attempted; R4388 (f.79, 2001-3900) retired by the pre-registered blank-cell test (S 0.316 vs null median 0.338, control p99 0.056; N7-HELBC); next: the same blank-cell test of R4386 (f.75, alphabetical 1201-2200, names point to 1764+) on the 63 distinct 1201-2000 codes (121 clean tokens), one login + 2 blind passes + reconciliation, ~$3, low prior

## Escalation (N7-HELBC, 4 Oct 2026)
- [x] siblings: Michell keys tested negative (FT4, FT4b); R4370 (f.46) and R4372 (f.48) tested negative as the first half (READ2-HEL2, NEAR3-HEL4, N4-HEL6 context check); all Add MS 32276 records looked at, up to f.56 (NEAR3-HEL3), R4381-R4408 by metadata and thumbnails (N6-HEL81), R4386 and R4388 at full size (N7-HELDK)
- [x] clear-pages: Fagel 5177's clear copies of Hellen's Oct-Dec 1751 letters looked at (N4-HEL5); context only, not a crib for R1953 itself
- [ ] known-keys: R4369 reads R1953; R4370 and R4372 retired for codes 1-800; R4376 fails on R1049 (N6-HEL76); R4388 fails the blank-cell test on the 1763 letters (N7-HELBC); R4386 untested (blank-cell test, ~$3)
- [x] print: Politische Correspondenz vols. 9-10 searched for the letter (check-solved sections above)
- [ ] key-rebuild: the fr18-bigram context-fit anneal is untestable at this N (N5-HEL7); untried instrument: phrase-crib placement from a transcribed Fagel 5177 writer-matched corpus, with its own held-out control
- [x] image-check: R4369, R4370, R4372 and R4376 read from the full-size images, two blind passes plus reconciliation each
- [ ] retry: an image check of R1953 itself against DECODE's transcription where decoded spans break (rule 2)
Verdict: keep going: 3 internal gaps; cheapest next: blank-cell test of R4386 on the 1763 1201-2000 band, ~$3 (low prior); larger: Fagel 5177 phrase corpus for codes 1-800, ~$12

## N7-HEL86 (4 Oct 2026): pre-registered blank-cell test of R4386 (f.75, codes 1201-2000) on the 1763 letters (account 2 worker for LANE-NEAR7)

Step run: N7-HELBC's named next. PREREG `key_r4386/PREREG-N7HEL86.md` (PREREG-N7HELBC's rule copied; seed 4386) and `cells.tsv` (63 target
codes / 121 clean 1763 tokens in 1201-2000, 100 null codes) pushed 4958d37b before the images were fetched; addendum A (attribution, geometry)
872c5d3d before any cell was read. One DECODE browser login (`--guess-fullsize`), R4386 P1-P4 full size to scratch only (not committed; P2/P3
sha1 as N7-HELDK). Units: 2 blind Sonnet passes (one call each, 11 tiles of 16 three-row bands, `key_r4386/crop_cells.py`) + 1 reconciliation.

**Layout (addendum A).** Each printed column carries a letter string or name right of printed n and a right-aligned word left of the next
column's number; the heads 120..190 stand over the left-of-n entries of printed 201-1000, so **code 1000+n = the entry left of printed n**.
One alphabetical run checked by eye: left of 201 "zero, zero, a, ab ..." -> left of 1000 "munitions" -> under head 200 "m'y, mystere, n ...".

**Reading.** err_2reader 4/155 = 0.026 (8 cells `?` for one pass); 12 cells settled by me from the crops (four target cells -- 1242, 1497,
1502, 1202 -- checked at full resolution: each row is empty between two written neighbours). Per cell: `key_r4386/cells_read.tsv`, `settle.tsv`.

**Result** (`python3 key_r4386/blank_test.py --score`, `key_r4386/score.txt`):

| | S (blank-cell token share) | null (100 cells, p0) | null p01 / p05 / median | control R4369 on R1953 at N=121, p95 / p99 | verdict |
|---|---|---|---|---|---|
| X as filled (primary) | 23/121 = **0.190** | 0.140 | 0.033 / 0.058 / 0.132 | 0.058 / 0.074 (**power FAIL**) | **NON-TEST** |
| X as blank (sensitivity) | 23/121 = 0.190 | 0.150 | 0.041 / 0.066 / 0.149 | 0.058 / 0.074 | NON-TEST |

**Verdict (pre-registered rule): NON-TEST at this N.** R4386's own blank rate (about 14% of random cells) is too low for 121 tokens to
separate a true key from a random sheet: the control's p99 (0.074) is above the null's p01 (0.033). Neither candidate nor retired. Not
gated, descriptive only: S 0.190 sits above the null median (P(null >= S) 0.21) and well above the control p99; 6 of the 63 target codes
are blank (1242 x8, 1497 x7, 1319 x3, 1502 x3, 1314, 1202), against about 3% U for a true key at R1953 -- this leans against R4386 but is
not a test. The names (Macartney knighted 1764, Conway) still point after 5 Jul 1763 (N7-HELDK, inference).

**Where it was not found:** R4386 does not pass the blank-cell test on the 1763 1201-2000 band (non-test, not a retirement); R4388 retired
(N7-HELBC); no holder or date on either sheet. More passes at the same 121 tokens cannot raise the power; the different instrument is a
words-level test (read the 63 target cells' words, decode the 121 tokens in context, value-shuffle control), ~$3. Requests: de-crypt.org
about 10 (1 login + RecordsView 4386 + 4 thumbnails + 4 full-size), 1.7 s apart, no challenge. Subagent calls: 2 (Sonnet). Cost: see the
lane ledger.

## Remaining gaps (N7-HEL86, 4 Oct 2026)
Read so far: 456 of 846 R1953 tokens carry a key value (H 152, S 304) plus M 16; 374 U (unchanged)
- codes 1-800 of the Hellen key (374 R1953 tokens) - blocker: not-attempted; period tables R4370/R4372 retired (rule 3); the context-fit anneal over fr18 bigrams is untestable at this N (N5-HEL7); next: transcribe Fagel 5177's clear Hellen pages (scans 5-93, two blind passes + reconciliation) as a writer- and week-matched phrase corpus, then a pre-registered phrase-crib placement in the R4369-decoded gaps with its own held-out control, ~$12
- empty cells inside 801-1796 (14 tokens) and the 16 M tokens - blocker: open-codes; scattered codes the sheet leaves blank or the readers could not settle
- the 1756 letter (R1049) - blocker: no-key-material; R4369, R4372 and R4376 do not read it (N6-HEL76), the 1756 sheets R4377-R4379 are tallies/empty or Michel's, and no record in R4381-R4408 is dated 1756 or names Hellen (N6-HEL81); no further Add MS 32276 record remains unopened
- the 1763 letters (R1045-R1048, R1060, R1061) - blocker: not-attempted; R4388 (f.79, 2001-3900) retired by the pre-registered blank-cell test (N7-HELBC); R4386 (f.75, 1201-2000, names 1764+) NON-TEST under the same instrument (S 0.190 vs null median 0.132, control p99 0.074 above null p01 0.033: the sheet's blank rate is too low at N=121; N7-HEL86); next: a words-level test of R4386 -- read the 63 target cells' words (2 blind passes + reconciliation), decode the 121 tokens in their 1763 context and score against a value-shuffle of R4386's own 1201-2000 words, pre-registered, ~$3, low prior

## Escalation (N7-HEL86, 4 Oct 2026)
- [x] siblings: Michell keys tested negative (FT4, FT4b); R4370 (f.46) and R4372 (f.48) tested negative as the first half (READ2-HEL2, NEAR3-HEL4, N4-HEL6 context check); all Add MS 32276 records looked at, up to f.56 (NEAR3-HEL3), R4381-R4408 by metadata and thumbnails (N6-HEL81), R4386 and R4388 at full size (N7-HELDK)
- [x] clear-pages: Fagel 5177's clear copies of Hellen's Oct-Dec 1751 letters looked at (N4-HEL5); context only, not a crib for R1953 itself
- [ ] known-keys: R4369 reads R1953; R4370 and R4372 retired for codes 1-800; R4376 fails on R1049 (N6-HEL76); R4388 fails the blank-cell test on the 1763 letters (N7-HELBC); R4386 blank-cell test NON-TEST at N=121 (N7-HEL86); untried instrument: words-level context test of R4386's 63 target cells, ~$3
- [x] print: Politische Correspondenz vols. 9-10 searched for the letter (check-solved sections above)
- [ ] key-rebuild: the fr18-bigram context-fit anneal is untestable at this N (N5-HEL7); untried instrument: phrase-crib placement from a transcribed Fagel 5177 writer-matched corpus, with its own held-out control
- [x] image-check: R4369, R4370, R4372 and R4376 read from the full-size images, two blind passes plus reconciliation each
- [ ] retry: an image check of R1953 itself against DECODE's transcription where decoded spans break (rule 2)
Verdict: keep going: 3 internal gaps; cheapest next: words-level context test of R4386 on the 1763 1201-2000 band, ~$3 (low prior); larger: Fagel 5177 phrase corpus for codes 1-800, ~$12

## D2-HELFAGEL (5 Oct 2026): phrase-crib pilot from Fagel 5177 clear Hellen pages, codes 1-800 of R1953 (account 1 worker for LANE-D2PUSH)

Step run: N7-HEL86's larger named next, PILOT slice. Intake gate (`python3 tools/intake_gate_check.py hellen-frederick-1752`, 18:4x UTC):
`hellen-frederick-1752: partial (line 1) -- edition/page or full-text-search citation found within 6 lines` (pass).
PREREG `key_rebuild/PREREG-HELFAGEL.md` pushed 137b2d66b (18:50 UTC) before any page was transcribed or any score run; instruments
`key_rebuild/phrase_crib.py` and `key_rebuild/reconcile_fagel.py` pushed 3049ea92a before the run.

**Corpus H.** Eight clear Hellen pages nearest 4 Jan 1752: scan 93 R (No 36, 24 Dec 1751), 94 L, 94 R, 89 R (No 37, 28 Dec 1751),
90 L (No 37 cont., the even scans 90 and 94 newly fetched), 85 L, 85 R, 87 L + 87 R tail. Images (NA `default` URLs from
`fagel5177/manifest_na5177.json`) in scratch only. Crops, one command per page (pasted):
`python3 tools/iiif_lines.py --image s<N>.jpg --region <box> --out c<N><side> --prefix s<N><side> --lines-per-crop 2 --distance 100 --prominence 40 --smooth 9 --debug`
with boxes 93R 2650,450,2250,3300; 94L 750,200,2100,3550; 94R 2500,200,2350,3550; 89R 2750,600,1950,3000; 90L 750,200,1950,2000;
85L 700,150,2050,3600; 85R 2550,200,2300,3550; 87L 800,150,2050,3600; 87R 2550,200,2300,500 (debug overlays checked for 89R, 85R,
87L, 94L; 87L/94L/85L boxes widened once after the first overlay clipped the right edge).
Passes: 2 blind Sonnet passes per page (one page's crops per call) = 16 calls + 1 re-run of 85R pass A (its first run skipped about a
third of the lines under my "skip slivers" wording; the prompt was corrected for all later calls) = 17 vision calls. Reconciliation by
script (agreement-only, `key_rebuild/fagel_agreement.tsv`): agreed share of pass A's words 0.854-1.000 per page; corpus H =
**1,861 agreed words** (`key_rebuild/fagel_corpus_H.txt`; disagreements and uncertain words are phrase breaks).
Topics read (context, not code values): the Port Franc project and its opposition by Utrecht and Gelderland (No 37), the Privy
Council protocol of the 16th on the yield of Republic offices and the Traité de Londres copy sent to Eichel (No 36), the Barrier and
the Vienna court, the Gotha subsidy, the funeral of the Prince of Orange at the Generality's charge, the regiments.

**Result** (`python3 key_rebuild/phrase_crib.py`, output `key_rebuild/phrase_crib_output.txt`, `--check` exits 0):

| | cribs | counted placements | S (codes proposed) | gate / reading |
|---|---|---|---|---|
| C1 fr18 slices x5 (1,861 words each) | 34-190 | 0 each | 0, 0, 0, 0, 0 (mean 0.00) | <= 1: PASS |
| C2 U-code shuffles x20 | 111 | 0 | all 0 (mean 0, p95 0) | -- |
| C3 known-answer, 182 keyed codes 801+ held out in 10 folds | 111 | 0 | 0 proposals, 0 correct | power: **none** |
| TARGET R1953 | 111 | 0 | **0** | -- |

**Decision (PREREG 7): no values.** Nothing was proposed by the target or by either control. The known-answer control C3 also
proposed nothing, so this is **untestable by this instrument at 1,861 words**, not a negative about codes 1-800 (rule 3). No grade
moves; R4369's reading stands (H 152 / S 304 / M 16 / U 374); `key_r4369/key.tsv` untouched; no depth change.
Diagnostic, outside the PREREG and not used for any decision (`key_rebuild/phrase_crib_diag.txt`): with the authentication-distance
gate removed, the 111 cribs (median 11 letters) give only 14 boundary-consistent placements in R1953; the best is about 6 letters
short of the gate (k=1 U token, m=3-4 keyed letters: "les etats", "la cour de", "le comte de"); only 3 of the 111 cribs occur wholly
inside a keyed letter run. The bottleneck is crib supply and the syllable-sized keyed tokens, not the gate setting.
**Is the full 5-93 corpus worth it?** Estimate: about 40 Hellen pages, 2 passes each, about 80 Sonnet calls at about $0.35 plus
crops and overhead, about $30-35. Not recommended on this evidence: five times the words gives more generic repeats ("les etats", "la
republique"), but a counted placement needs a repeated phrase of about 14+ letters lying mostly across keyed tokens next to one U,
and the pilot found 0 even before the gate in the known-answer arm. A different instrument (more ciphertext in the same code, or
the image check of R1953 itself) is the better spend.
Where it was not found: no code value for 1-800 from phrase cribs drawn from Hellen's 24-28 Dec 1751 letters (8 pages).
Requests: service.archief.nl 6 (scans 85, 87, 89, 93 and 90, 94; `default` image URLs), 2 s apart, no 403/429/challenge. Vision
calls 17 (Sonnet subagents), 0 by me on crops beyond 4 overlay checks. Cost: estimate about $8-9 total (lane reads get_session).

## Remaining gaps (D2-HELFAGEL, 5 Oct 2026)
Read so far: 456 of 846 R1953 tokens carry a key value (H 152, S 304) plus M 16; 374 U (unchanged)
- codes 1-800 of the Hellen key (374 R1953 tokens) - blocker: not-attempted; period tables R4370/R4372 retired (rule 3); context-fit anneal untestable at this N (N5-HEL7); phrase-crib placement from 8 Fagel 5177 pages untestable at 1,861 words, known-answer control 0 proposals (D2-HELFAGEL); next: image check of R1953 against DECODE's transcription where decoded spans break (rule 2), ~$6
- empty cells inside 801-1796 (14 tokens) and the 16 M tokens - blocker: open-codes; scattered codes the sheet leaves blank or the readers could not settle
- the 1756 letter (R1049) - blocker: no-key-material; R4369, R4372 and R4376 do not read it (N6-HEL76), no 1756 Hellen sheet in R4377-R4408 (N6-HEL81)
- the 1763 letters (R1045-R1048, R1060, R1061) - blocker: not-attempted; R4388 retired (N7-HELBC); R4386 blank-cell test NON-TEST at N=121 (N7-HEL86); next: a words-level test of R4386's 63 target cells on the 1763 1201-2000 band, pre-registered, ~$3, low prior

## Escalation (D2-HELFAGEL, 5 Oct 2026)
- [x] siblings: Michell keys tested negative (FT4, FT4b); R4370 (f.46) and R4372 (f.48) tested negative as the first half; all Add MS 32276 records looked at (NEAR3-HEL3, N6-HEL81, N7-HELDK)
- [x] clear-pages: Fagel 5177's clear Hellen copies looked at (N4-HEL5) and 8 pages of Dec 1751 transcribed as a phrase corpus (D2-HELFAGEL); context only, no ciphertext beside them
- [ ] known-keys: R4369 reads R1953; R4370/R4372 retired for 1-800; R4376 fails on R1049; R4388 fails on 1763; R4386 NON-TEST at N=121; untried instrument: words-level context test of R4386's 63 target cells, ~$3
- [x] print: Politische Correspondenz vols. 9-10 searched for the letter (check-solved sections above)
- [ ] key-rebuild: fr18-bigram anneal untestable (N5-HEL7); phrase-crib placement untestable at 8 pages, C3 power 0 (D2-HELFAGEL); untried: the same instrument on the full scans 5-93 corpus, ~$30-35, low prior (not recommended), or a further R4369-code letter if one is found
- [x] image-check: R4369, R4370, R4372 and R4376 read from the full-size images, two blind passes plus reconciliation each
- [ ] retry: an image check of R1953 itself against DECODE's transcription where decoded spans break (rule 2), ~$6
Verdict: keep going: 3 internal gaps; cheapest next: words-level context test of R4386 on the 1763 1201-2000 band, ~$3 (low prior); for codes 1-800: image check of R1953, ~$6

## D2-HELR (6 Oct 2026): pre-registered words-level frequency-fit test of R4386 (f.75) on the 1763 1201-2000 band (account 1 worker for LANE DEFAULT-account-1-20261005-2217)

Step run: N7-HEL86's named next (the different instrument after its NON-TEST). Intake gate (`python3 tools/intake_gate_check.py
hellen-frederick-1752`, 5 Oct 2026 23:54 UTC): `hellen-frederick-1752: partial (line 1) -- edition/page or full-text-search citation found
within 6 lines` (pass, exit 0). PREREG `key_r4386/PREREG-D2HELR.md` pushed 02115fd90 (5 Oct 23:58-23:59 UTC; its header's "about 00:00"
is corrected in the file) before the images were fetched; control run and pushed 990801f28 before any word was read. One DECODE browser login
(`--guess-fullsize`), R4386 P1-P4 full size to scratch only (P2/P3 sha1 match N7-HELDK). Tiles: N7-HEL86's `crop_cells.py` with a new
`--scale 1.0` option (same 163 cells, same attribution). Units: 2 blind Sonnet passes (one call each, 11 tiles) + 1 reconciliation.

**Reading.** 163 cells, the passes disagree on 25 (15%; mostly `?`-marks, abbreviations and null cells); 8 settled (`key_r4386/words_read.tsv`
column `settled`): 1242 (x8) BLANK -- pass A read the neighbouring row 241 "affaires", N7-HEL86 checked row 242 empty at full resolution;
1202 BLANK (N7-HEL86); 1522 "dernieres" and 1227 "a l'egard de" from the crop. Non-target disagreements took pass B.

**Statistic** (PREREG): S = token-weighted mean log10 fr18 frequency of each 1763 token's R4386 word; null = 10,000 permutations of the 163
read words over the cells. `python3 key_r4386/words_test.py --control --score` (`words_control.txt`, `words_score.txt`):

| | S | null median / p95 / p99 | P(null >= S) | control R4369 on R1953 at ~121 tokens: share S > own p99 (gate >= 0.80) | wrong key (gate <= 0.05) | verdict |
|---|---|---|---|---|---|---|
| reconciled (primary) | **-4.788** | -4.678 / -4.366 / -4.226 | **0.736** | **1.000** | 0.005 | **FAIL** |
| pass A only (sensitivity) | -4.639 | -4.714 / -4.411 / -4.285 | 0.331 | | | inconclusive |
| pass B only (sensitivity) | -4.783 | -4.674 / -4.362 / -4.218 | 0.733 | | | FAIL |

**Verdict (pre-registered rule): FAIL -- R4386 retired for the 1763 1201-2000 band (instrument: words-level frequency fit).** With power
1.000 at this N, R4386's words sit at or below a random reassignment of its own words: 58 of the 121 tokens land on a blank, "zero" or a
non-word, and the three most frequent 1763 codes read BLANK (1242 x8), "bre" (1337 x8) and BLANK (1497 x7), where a true key puts
function words. Pass A's inconclusive line comes only from its 1242 misread (the neighbour row). Caveat: the control's R1953 values are
the R4369 reading itself (152 H, 304 S tokens), so the control is partly circular for its S tokens; the wrong-key line (0.005) shows the
statistic does not pass a key of the same design by construction.

**Where it was not found:** R4386 does not carry the 1763 1201-2000 values (this test); R4388 does not carry the 2001-3900 values
(N7-HELBC); no other Add MS 32276 record R4381-R4408 is a 1763 positional candidate (N6-HEL81). Requests: de-crypt.org about 10 (1 login +
RecordsView 4386 + 4 thumbnails + 4 full-size), 1.7 s apart, no challenge. Subagent calls: 2 (Sonnet). Cost: see the lane ledger.

## Remaining gaps (D2-HELR, 6 Oct 2026)
Read so far: 456 of 846 R1953 tokens carry a key value (H 152, S 304) plus M 16; 374 U (unchanged)
- codes 1-800 of the Hellen key (374 R1953 tokens) - blocker: not-attempted; period tables R4370/R4372 retired (rule 3); context-fit anneal untestable at this N (N5-HEL7); phrase-crib placement from 8 Fagel 5177 pages untestable at 1,861 words, known-answer control 0 proposals (D2-HELFAGEL); next: image check of R1953 against DECODE's transcription where decoded spans break (rule 2), ~$6
- empty cells inside 801-1796 (14 tokens) and the 16 M tokens - blocker: open-codes; scattered codes the sheet leaves blank or the readers could not settle
- the 1756 letter (R1049) - blocker: no-key-material; R4369, R4372 and R4376 do not read it (N6-HEL76), no 1756 Hellen sheet in R4377-R4408 (N6-HEL81)
- the 1763 letters (R1045-R1048, R1060, R1061) - blocker: no-key-material; both positional candidates in Add MS 32276 retired by pre-registered tests with passed controls, R4388 for 2001-3900 (N7-HELBC) and R4386 for 1201-2000 (D2-HELR); no other 1763 sheet in R4381-R4408 (N6-HEL81); reopens only with new material (a 1763 Hellen/La Haye key sheet elsewhere)

## Escalation (D2-HELR, 6 Oct 2026)
- [x] siblings: Michell keys tested negative (FT4, FT4b); R4370 (f.46) and R4372 (f.48) tested negative as the first half; all Add MS 32276 records looked at (NEAR3-HEL3, N6-HEL81, N7-HELDK)
- [x] clear-pages: Fagel 5177's clear Hellen copies looked at (N4-HEL5) and 8 pages of Dec 1751 transcribed as a phrase corpus (D2-HELFAGEL); context only, no ciphertext beside them
- [x] known-keys: R4369 reads R1953; R4370/R4372 retired for 1-800; R4376 fails on R1049; R4388 fails on 1763 (N7-HELBC); R4386 fails on 1763 under the words-level test (D2-HELR)
- [x] print: Politische Correspondenz vols. 9-10 searched for the letter (check-solved sections above)
- [ ] key-rebuild: fr18-bigram anneal untestable (N5-HEL7); phrase-crib placement untestable at 8 pages, C3 power 0 (D2-HELFAGEL); untried: the same instrument on the full scans 5-93 corpus, ~$30-35, low prior (not recommended), or a further R4369-code letter if one is found
- [x] image-check: R4369, R4370, R4372, R4376, R4386 and R4388 read from the full-size images, two blind passes plus reconciliation each
- [ ] retry: an image check of R1953 itself against DECODE's transcription where decoded spans break (rule 2), ~$6
Verdict: keep going: 2 internal gaps; cheapest next: image check of R1953 against DECODE's transcription for codes 1-800, ~$6

## R7A-HEL53 (6 Oct 2026): image check of R1953 against DECODE's transcription (account 1 worker for LANE LANE-RUN7-account-1)

Step run: the Remaining-gaps "next" of D2-HELR (rule 2: the image, not the transcription). Intake gate passed (lane brief, 6 Oct
01:5x UTC). One DECODE browser login (`NODE_PATH=$(npm root -g) node tools/decode_browser_login.js 1953 <scratch> --guess-fullsize
--delay 1700 --max-files 8`): **full-size images were served** for all three pages, plus DECODE's own transcription document. Kept in
the scratchpad only, not committed (not public domain). sha1: IMG_R1953_I13447_P2.png 16a4504954eef2126946ae716606df895ea05e97,
IMG_R1953_I13448_P3.png 16f742a99255e05c8ebfb100efc16adac8605320, IMG_R1953_I13446_P1.png f57cf8adb3b047041038635310b29cda0fd40f67
(5472x3648, photographed sideways; reading order P2 = image 13447, P3 = 13448, P1 = 13446), DOC_R1953_D3616_3616.txt
f08e2126a78fc4b778eee5ecdc725d9b3ecc4e68 (transcriber "KL", 26 Jan 2020, 2 h, manual).

**Transcription = DOC.** `image_check_r1953/doc_tokens.py` splits the DOC by page and line: 846 groups, 0 digit mismatches with
`ciphertext_R1953.txt` (P2 22 lines, P3 23, P1 9). So any error found below is DECODE's, carried unchanged into this folder.

**Crops and reads.** Pages rotated upright; P3 and P1 levelled by 3.4 and 2.6 degrees (PIL) after `--deskew` produced duplicated
bands; then `python3 tools/iiif_lines.py --image <page> --region ... --distance 115-150 --prominence 5 --max-width 1700 --overlap 120`
(crops in the scratchpad). Three blind Sonnet calls, no transcription shown: pass A on page 2 and on pages 3+1 (first cut), pass B
re-read of the bands the first cut had garbled (P2 L18-L22, P3 L12-L22, P1 L01-L09). `image_check_r1953/compare.py` aligns each read
to the DOC per page by edit distance (`compare.tsv`, merged read `pass_merged.tsv`): 747 same, 13 same-with-doubt, 32 differ, 54 DOC
groups no read reached (P3 L07, L22, L23 and the tail of P2 L22), 18 read-only (duplicate bands). Reconciliation (this worker, one
unit): every differ/doubt token and every unreached line looked at on the levelled crops (6 review sheets + 2 hand cuts at the foot
of P3). All 846 groups were seen in the image by at least one reader.

**What the image shows.** This hand writes 8 as a loop with a slanted bar, close to its 0; almost every Sonnet-vs-DECODE split was
that pair (308/300, 1458/1450, 284/204, 848/840, 998/990, 681/601 ...), and the image upheld DECODE in all but the cases below.
The repeated three-line passage on P3 (DOC L11-L13 = L14-L16) is real ink, as Bourdeau's audit says. Underlining (single, double,
triple) is real and DECODE's `_` marks follow it.

`image_check_r1953/corrections.tsv` (12 rows; `ciphertext_R1953.txt` is not modified):

| pos | DECODE | image | conf | key effect (R4369) |
|---|---|---|---|---|
| 40 | 1114 | 414 | high | U -> U (1-800) |
| 65 | 952 | 752 | high | H "re" -> U (1-800) |
| 549 | 898 | 838 | high | H "quel" -> H "que" (the repeated line has 838 too) |
| 682 | 128?3 | 1283 | high | U -> S "obten" |
| 716 | 23?8 | 278 | high | U -> U |
| 829 / 124 / 757 | 8?09 / 668? / 28?0 | 809 / 668 / 280 | high | doubtful 8 settled; no grade change |
| 89 | 1050 | 1058 | medium | S "mi" -> S "di" |
| 136 | 806 | 886 | medium | H "avance" -> H "prince de" |
| 386 | 1426903 (one group) | 1426 . 903 | medium | U -> S "et" + H "qu'" (one ink run, no dot) |
| 671 | 42 | 43 | medium | U -> U |

Re-decode with the R4369 key unchanged (`python3 tools/decode_key.py ciphers/hellen-frederick-1752/image_check_r1953`, `--check`
exit 0, "reading up to date"; config `image_check_r1953/decode.json`, corrections applied by `apply_corrections.py`):

| version | tokens | H | S | M | U |
|---|---|---|---|---|---|
| DECODE transcription (key_r4369/reading_R1953.txt) | 846 | 152 | 304 | 16 | 374 |
| high-confidence corrections | 846 | 152 | 305 | 16 | 373 |
| high + medium corrections | 847 | 153 | 306 | 16 | 372 |

**Finding.** Codes 1-800 are not unread because of transcription. Of the 374 U tokens, the image confirms all but 8 as DECODE
transcribed them, and none of those 8 moves a code from 1-800 into R4369's range except the two settlements above (1283, the
1426/903 split). The 1-800 gap is a key gap, as the earlier tests assumed. Transcription error found: 3 high-confidence wrong groups
(1114, 952, 898) and 4 medium, out of 846 (0.4-0.8%), plus 5 doubtful digits settled. Two key-reading tokens change value (952 "re"
-> unread, 898 "quel" -> "que"). The main reading in `key_r4369/` is left as it was; adopting the corrections there is the lane
orchestrator's call (it would change a counted reading).

**Where it was not found:** no marginal key note, docket or interlinear decipherment on any of the three images (cleartext is only
the heading, the opening sentence, "Je suis" and the signature line "/: signé :/ de Hellen", which is the form of a copy). Requests: de-crypt.org 9 (1 login + RecordsView + 3 thumbnails +
3 full-size + 1 document), 1.7 s apart, no challenge. Subagent calls: 3 Sonnet reads + 1 reconciliation (this worker).

## Remaining gaps (R7A-HEL53, 6 Oct 2026)
Read so far: 456 of 846 R1953 tokens carry a key value (H 152, S 304) plus M 16; 374 U on DECODE's transcription; 459 of 847 (H 153, S 306) with the image-check corrections (image_check_r1953/)
- codes 1-800 of the Hellen key (372 R1953 tokens) - blocker: no-key-material; the image check confirms the U tokens as transcribed (R7A-HEL53), period tables R4370/R4372 retired (rule 3), no other Hellen sheet in Add MS 32276 (NEAR3-HEL3, N6-HEL81); context-fit anneal untestable at this N (N5-HEL7); phrase-crib placement untestable at 8 Fagel pages (D2-HELFAGEL)
- empty cells inside 801-1796 (14 tokens), the 16 M tokens and the 0/8 look-alike in S/H tokens - blocker: open-codes; this hand's 8 is a barred 0, and only the tokens a reader disputed were checked; next: a 0/8 pass over every 801-1796 token whose 0<->8 twin is also keyed with a different meaning, on the R7A-HEL53 crops, ~$2
- the 1756 letter (R1049) - blocker: no-key-material; R4369, R4372 and R4376 do not read it (N6-HEL76), no 1756 Hellen sheet in R4377-R4408 (N6-HEL81)
- the 1763 letters (R1045-R1048, R1060, R1061) - blocker: no-key-material; both positional candidates retired by pre-registered tests with passed controls (N7-HELBC, D2-HELR); reopens only with new material

## Escalation (R7A-HEL53, 6 Oct 2026)
- [x] siblings: Michell keys tested negative (FT4, FT4b); R4370 (f.46) and R4372 (f.48) tested negative as the first half; all Add MS 32276 records looked at (NEAR3-HEL3, N6-HEL81, N7-HELDK)
- [x] clear-pages: Fagel 5177's clear Hellen copies looked at (N4-HEL5) and 8 pages of Dec 1751 transcribed as a phrase corpus (D2-HELFAGEL); context only
- [x] known-keys: R4369 reads R1953; R4370/R4372 retired for 1-800; R4376 fails on R1049; R4388 and R4386 fail on 1763
- [x] print: Politische Correspondenz vols. 9-10 searched for the letter (check-solved sections above)
- [ ] key-rebuild: fr18-bigram anneal untestable (N5-HEL7); phrase-crib placement untestable at 8 pages (D2-HELFAGEL); untried: the same instrument on the full scans 5-93 corpus, ~$30-35, low prior, or a further R4369-code letter if one is found
- [x] image-check: R4369, R4370, R4372, R4376, R4386, R4388 read from full-size images; R1953 itself checked against DECODE's transcription (R7A-HEL53: 846/846 groups seen, 12 corrections, U unchanged in substance)
- [x] retry: the R1953 image check (R7A-HEL53)
Verdict: keep going: 1 internal gap; cheapest next: the 0/8 pass over keyed 801-1796 tokens on the R7A-HEL53 crops, ~$2 (the 1-800 key-rebuild on the full Fagel corpus stays ~$30-35, low prior)

## R8-HEL (6 Oct 2026): pre-registered 0/8 pass over keyed 801-1796 tokens of R1953 (account 1 worker for LANE LANE-RUN8-account-1)

Step run: the R7A-HEL53 Verdict's cheapest next. Pre-registered in `zero_eight/PREREG.md` (pushed b30642cca at 04:07 UTC, before
any image was fetched). The brief assumed the R7A-HEL53 crops were on disk; they had lived in that session's scratchpad and were
gone, so the three page images were re-fetched with one DECODE browser login (`tools/decode_browser_login.js 1953 <scratch>
--guess-fullsize --delay 1700 --max-files 7`; sha1 identical to R7A-HEL53's; scratchpad only, not committed), rotated upright,
P3/P1 levelled 3.4/2.6 degrees, and cut with `python3 tools/iiif_lines.py --image <page> --out <scratch> --region 150,0,3400,5472
--distance 140 --prominence 5 --max-width 1700 --overlap 120 --debug` (crop lines map to DECODE lines as P2 L(n+4), P3 L(n) by the
overlay, P1 L(n+1); the P3 reader matched by neighbours and found its file labels one further down, no effect on the answers).

Candidates (`zero_eight/candidates.py` -> `candidates.tsv`): 138 tokens in 801-1796 whose 0<->8 twin is keyed in R4369 with a
different value (39 H, 87 S, 8 M, 4 U). 17 were already settled on the image by R7A-HEL53's reconciler and were not re-read; 121
went to three blind Sonnet calls (one per page) that saw only the group with every 0/8 masked as '?', its two neighbours, and the
crops. Never the key or the meanings. Reconciliation (this worker) on every non-agreeing answer.

| page | read | agree with DECODE | reader differs | unclear |
|---|---|---|---|---|
| P2 (13447) | 54 | 51 | 2 | 1 |
| P3 (13448) | 45 | 45 | 0 | 0 |
| P1 (13446) | 22 | 22 | 0 | 0 |

`zero_eight/corrections.tsv` (ciphertext_R1953.txt not modified):

| pos | DECODE | image | conf | key effect (R4369) |
|---|---|---|---|---|
| 2 | 820 | 828 | high (reader + reconciler: the final glyph has the 8 form of 1208/578, not the oval 0 of 1208/1049) | H "soin" -> H "suis" |
| 133 | 990? | 998 | high (reader + reconciler; DECODE had marked the digit doubtful) | M "le" -> H "d" |
| 272 | 1009 | 1089? | ambiguous (reader U; second 0 is an ink blot), not applied | S "er" stays (twin 1089 = H "ves") |

Key context column, for information only (PREREG rule 4): 828 gives "ie me suis" in the opening group, which reads better than
"ie me soin"; the change was made on the image, not for that.

Re-decode (`python3 zero_eight/apply_corrections.py`, then `python3 tools/decode_key.py ciphers/hellen-frederick-1752/zero_eight`,
`--check` exit 0 "reading up to date"; key_r4369/key_decode.tsv unchanged):

| version | tokens | H | S | M | U |
|---|---|---|---|---|---|
| R7A-HEL53 high + medium (image_check_r1953/reading_R1953_all.txt) | 847 | 153 | 306 | 16 | 372 |
| + R8-HEL 0/8 corrections (zero_eight/reading_R1953_08.txt) | 847 | 154 | 306 | 15 | 372 |

**Judge** (`python3 tools/judge_plaintext.py specs/hellen-frederick-1752.json --file ciphers/hellen-frederick-1752/zero_eight/reading_R1953_08.txt`):
```
ok   length: got=1332, min=200, max=1000000000
FAIL language: score=-0.978, null_p99=-1.739, real_p05=-0.968, real_median=-0.826, mode=both, N=1332
FAIL - hellen-frederick-1752 (a PASS is a gate for a verifier, not a reading; rule 10)
```
Same place as before (-0.976 on the DECODE transcription): a FAIL near the gate, inside the calibration band where real fr18 prose
at this coverage also FAILs (judge_calib.py); the judge cannot decide.

**Finding.** The 0/8 look-alike is not a large error source in the keyed range: of 121 twin-keyed tokens that two readers had
agreed on, 2 change (1.7%), 1 is ambiguous, 118 confirmed. The 1-800 gap is untouched (the pass only reads 801-1796). The main
reading in `key_r4369/` is left as it was; adopting the image-check and 0/8 corrections there is the lane orchestrator's call.

**Where it was not found:** no marginal key note or interlinear decipherment seen on the crops (as R7A-HEL53). Requests: de-crypt.org
8 (1 login + RecordsView + 3 thumbnails + 3 full-size + 1 document), 1.7 s apart, no challenge. Subagent calls: 3 Sonnet reads + 1
reconciliation (this worker).

## Remaining gaps (R8-HEL, 6 Oct 2026)
Read so far: 460 of 847 R1953 tokens carry a key value (H 154, S 306) plus M 15, U 372, with the R7A-HEL53 and R8-HEL corrections (zero_eight/); 456 of 846 on DECODE's transcription
- codes 1-800 of the Hellen key (372 R1953 tokens) - blocker: no-key-material; the image check confirms the U tokens as transcribed (R7A-HEL53), period tables R4370/R4372 retired (rule 3), no other Hellen sheet in Add MS 32276 (NEAR3-HEL3, N6-HEL81); context-fit anneal untestable at this N (N5-HEL7); phrase-crib placement untestable at 8 Fagel pages (D2-HELFAGEL)
- empty cells inside 801-1796 (14 tokens), the 15 M tokens and one 0/8-ambiguous token (pos 272) - blocker: open-codes; the 0/8 pass is done (R8-HEL: 121 read, 2 changed, 1 ambiguous); the empty cells are blank in R4369 itself
- the 1756 letter (R1049) - blocker: no-key-material; R4369, R4372 and R4376 do not read it (N6-HEL76), no 1756 Hellen sheet in R4377-R4408 (N6-HEL81)
- the 1763 letters (R1045-R1048, R1060, R1061) - blocker: no-key-material; both positional candidates retired by pre-registered tests with passed controls (N7-HELBC, D2-HELR); reopens only with new material

## Escalation (R8-HEL, 6 Oct 2026)
- [x] siblings: Michell keys tested negative (FT4, FT4b); R4370 (f.46) and R4372 (f.48) tested negative as the first half; all Add MS 32276 records looked at (NEAR3-HEL3, N6-HEL81, N7-HELDK)
- [x] clear-pages: Fagel 5177's clear Hellen copies looked at (N4-HEL5) and 8 pages of Dec 1751 transcribed as a phrase corpus (D2-HELFAGEL); context only
- [x] known-keys: R4369 reads R1953; R4370/R4372 retired for 1-800; R4376 fails on R1049; R4388 and R4386 fail on 1763
- [x] print: Politische Correspondenz vols. 9-10 searched for the letter (check-solved sections above)
- [ ] key-rebuild: fr18-bigram anneal untestable (N5-HEL7); phrase-crib placement untestable at 8 pages (D2-HELFAGEL); untried: the same instrument on the full scans 5-93 corpus, ~$30-35, low prior, or a further R4369-code letter if one is found
- [x] image-check: R4369, R4370, R4372, R4376, R4386, R4388 read from full-size images; R1953 checked against DECODE's transcription (R7A-HEL53) and its keyed 0/8 twins read masked (R8-HEL)
- [x] retry: the R1953 image check (R7A-HEL53) and the 0/8 pass (R8-HEL)
Verdict: keep going: 1 internal gap; cheapest next: the 1-800 key-rebuild on the full Fagel scans 5-93 corpus, ~$30-35, low prior (a campaign, lane orchestrator's call), or adopting the image-check + 0/8 corrections into key_r4369/ (orchestrator's call, changes a counted reading)
