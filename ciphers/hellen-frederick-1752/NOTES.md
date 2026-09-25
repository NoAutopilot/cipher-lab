open

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
