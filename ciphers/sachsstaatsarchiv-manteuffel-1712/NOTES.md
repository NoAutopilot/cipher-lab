blocked

# Krauske's 1893 decipherment of Manteuffel's 1712-13 reports to Flemming — SHStA Dresden (print check only)

QUEUE row: DA4 (sources/solver-diffs/2026-09-24-lane-n2-dea.tsv, "German state archives, online finding aids
(LANE N2 scout of 24 September 2026)"). **Per brief: this target gets a print check only, not a full
check-solved campaign** — the question is whether Krauske's 1893 decipherment was ever printed.

## Source

Sächsisches Hauptstaatsarchiv Dresden, **10026 Geheimes Kabinett**:
- **Loc. 00694/10 (08/09)**: "Chiffren in Schreiben Manteuffels an Flemming (angefertigt von Dr. Krauske,
  1893)[.] Enthält u. a.: Einige Chiffre-Auflösungen zu den Berichten Manteuffels an Flemming 1712 und 1713,
  (Loc. 694/08 und Loc. 694/09)." — i.e. the underlying 1712-13 ciphered reports are Loc. 694/08 and /09; a
  set of cipher solutions ("Chiffre-Auflösungen") made by "Dr. Krauske" in 1893 is filed with them at Loc.
  694/10.

Correspondents: **Ernst Christoph von Manteuffel** (1676-1749), Saxon diplomat, close collaborator of
**Jakob Heinrich von Flemming** (1667-1728), directing Saxon-Polish cabinet minister from 1712 (both confirmed,
Sächsische Biografie/ISGV, WebSearch 24 Sept 2026). **"Dr. Krauske"** is almost certainly **Otto Krauske**
(1859-1930), a Prussian-trained historian and archivist active in this period (Wikipedia; "Historiker und
Archivar im Dienste Preußens" festschrift, 2015) — his other confirmed editorial work, *Die Briefe König
Friedrich Wilhelms I. an den Fürsten Leopold zu Anhalt-Dessau 1704-1740*, is Prussian court correspondence of
the same general era, consistent with an archivist capable of and likely to be commissioned for this kind of
deciphering/editing work at a state archive; not independently confirmed as the same Krauske who worked at
Dresden specifically.

## Print check (24 September 2026)

1. **The 1893 year itself.** *Neues Archiv für sächsische Geschichte* is the standard Saxon regional-history
   journal (named in the brief) and its volume 14 corresponds to 1893 (annual since vol. 1 in 1880). Full-text
   searched on archive.org (`neuesarchivfur14sach`, be-api fts): "Manteuffel" — **0 hits**. "Flemming" — 1 hit,
   p.394, but it is a genealogical article on Bautzen-area surnames ("Flemming, Bautzner Familie... Flemming,
   Feldmarsch.") mentioning the Flemming surname's local origin, not Ernst Christoph von Manteuffel's 1712-13
   reports or any cipher solution. **Real negative**, not just an unreached source.
2. **The five years after (1893-1898), per the check-solved brief's rule for editors who could not find a key —
   here inverted: an editor who could find and print a key sometimes published a fuller article on the
   correspondence afterward.** Not run this pass (budget) — a real gap.
3. **Biographical/secondary literature.** Sächsische Biografie (ISGV) entries for both Manteuffel and Flemming
   were found by WebSearch and read at snippet level; neither snippet cites Krauske's 1893 Chiffre-Auflösungen
   or quotes deciphered text from the 1712-13 reports. One modern secondary source (a ResearchGate paper on
   August Christoph von Wackerbarth / the "Société des antisobres", found by WebSearch) cites the archival
   fond "SächsHStAD, 10026, Geheimes Kabinett, Chiffren de S. Exc. Mgr. le C. de Flemming, Loc." — i.e. a
   *different*, French-titled sub-series within the same Geheimes Kabinett bestand, used as an archival source
   by a modern historian, not a printed edition of Krauske's 1893 work and not confirmed to be Loc. 694/08-10
   specifically. Not opened in full this pass (WebFetch on the PDF was not attempted — flagged, not run).
4. **Community lists / DECODE / solver repositories.** `sources/cryptiana/`, `sources/decode/`, and fresh
   shallow clones of both solver repos grepped for "Manteuffel", "Flemming", "Krauske": zero hits in all three
   (shared search pass with the other five targets this run; see their NOTES.md for the same negative).
5. **Haake's Flemming studies** (named in the brief) — Alfred Haake wrote a standard early-20th-c. biography of
   Jakob Heinrich von Flemming; not located/opened this pass — a real gap, flagged for a follow-up.

## Verdict

**Not found printed** in the one source checked in full (Neues Archiv für sächsische Geschichte 1893, the
publication year itself) — a real negative, not an unreached-source placeholder. The five-years-after sweep,
Haake's Flemming biography, and full reading of the Wackerbarth/Société-des-antisobres paper are not done this
pass and are the concrete next steps. **Krauske's decipherment already exists in the archive**, so this is not
a fresh cryptanalysis or recovery target regardless of the print-check outcome: if unprinted, the natural
product is a *transcription of Krauske's own 1893 reading* (a contribution, once a copy of Loc. 694/10 is in
hand), not a new solve. **Status: blocked** — no image of Loc. 694/10 resolved to a working URL (scout's
original sweep saw a `#digitalisat` anchor that did not resolve in a 4s render), and the print-check gaps above
(five-years-after journal sweep, Haake, full reading of the one secondary-source lead) are not closed. Not
nominated to the board: per the brief, this is a print check, not a check-solved campaign, and the target's own
`kind` (recovery/contribution) does not fit a cryptanalysis nomination in any case.

**Recommended next steps (not run this pass):** (1) run *Neues Archiv für sächsische Geschichte* vols. 15-19
(1894-98) through the same be-api fts for "Manteuffel"/"Chiffre"; (2) locate and read Haake's Flemming
biography; (3) read the Wackerbarth/Société-des-antisobres ResearchGate paper in full for its citation context
around "Chiffren de S. Exc. Mgr. le C. de Flemming, Loc." and check whether it resolves to Loc. 694 specifically;
(4) resolve the Sächsisches Staatsarchiv `#digitalisat` anchor on Loc. 694/10 to a working image URL or confirm
it does not serve one.

queued JSTOR rows, 26 Sept 2026, QUEUE-FILL.

## JSTOR runner, 26 Sept 2026

- `"Manteuffel" AND "Flemming" AND 1712 AND Chiffre`: no relevant hit (2 results, none about the letter).
- `"Krauske" AND "Chiffre-Auflösungen" AND Manteuffel`: no relevant hit (0 results, none about the letter).

## A2-SAX, 3 Oct 2026 (LANE-A2PUSH, account 2): NASG 1894-98 sweep and the Loc. 694/10 image

Intake gate pasted before work: `sachsstaatsarchiv-manteuffel-1712: blocked (line 1) -- already terminal, nothing to gate` (exit 0).
Note: the lane brief said this NOTES.md ends in "## A2-SAX2, 3 Oct 2026 (LANE-A2PUSH, account 2): Loc. 694/08 and /09 frames, sampled inventory

Intake gate pasted before work: `sachsstaatsarchiv-manteuffel-1712: blocked (line 1) -- already terminal, nothing to gate` (exit 0).

**Records and image counts.** Catalogue records quoted first (access playbook):
https://www.archiv.sachsen.de/archiv/bestand.jsp?guid=3a83f921-9a43-485f-874b-34653ed59b68 -- "Archivaliensignatur
Loc. 00694/08 · Datierung 1712", Digitalisat tab; Enthält u. a.: "Nachrichten vom Berliner Hofe.- Kriegsnachrichten.-
Personalien des Grafen Manteuffel.- ... Peter der Große in Berlin, 1712 ...".
https://www.archiv.sachsen.de/archiv/bestand.jsp?guid=c5158a8f-281c-49a8-985a-b0aa75400e17 -- "Loc. 00694/09 ·
Datierung 1713", Digitalisat tab; "Nachrichten vom Berliner Hof.- Graf Manteuffel Personalia.- Verlobung mit Baronne
von Wackerbarth.- Krankheit und Tod des Königs von Preußen, Friedrich I. ...".
The viewer's frame list is a plain JSON file, `https://www.archiv.sachsen.de/digitalisate/<guid>/files.json`
(found in `/js/archiv.js`): **694/08 = 592 frames, 694/09 = 302 frames** (894 in all; each a two-page microfilm
spread, ~4340x3860, ~1.5 MB). Every frame URL is in `images/loc694-08-09/frames.tsv`. The viewer's `/preview/`
images are 150x134 px, too small to tell code groups from words.

**Why a sample, not every frame.** 894 full-size frames is ~1.3 GB and 894 requests to one host, past the
good-citizen limit ("a few hundred requests per host per session") and this step's 35-minute box. So 17 frames
were fetched, evenly spread (694/08 every 70th from 0020, 694/09 every 40th from 0020, plus 0295), read on 1000-px
contact sheets, and the two with code groups re-read at 1600-px crops. Only those two are committed
(`images/loc694-08-09/694-08_0510.jpg`, `694-08_0580.jpg`, in `images/manifest.json`; folder 14 MB, under 30).
Per-frame result: `frame_inventory.tsv` (loc, frame, document, cipher y/n, interlinear decipherment y/n, clear text).

**Inventory (17 frames).** Cipher present: **2 of 17 sure (694/08 frames 0510, 0580), 1 possible (694/09 0060)**,
14 without cipher. The reports are French clear text with **cipher used for words and passages inside the clear
text** (partial encipherment, number groups underlined and separated by points), not whole-cipher letters. Other
sampled frames: Flemming's own minutes to Manteuffel (08_0160, 08_0370, 09_0295), German enclosures (08_0090, 09_0260),
an account signed by Manteuffel (09_0220).
- 694/08 frame 0510 (Manteuffel to Flemming, Berlin, Nov 1712, no.96, f.409): underlined groups, e.g. (eye read
  at 1600 px, grade M) "840.865", "403.1056.974", "344.226.213", "...272.155.583.586.351.77", "...569.403.539.237.601".
  No interlinear decipherment seen above these groups.
- 694/08 frame 0580 (f.468): groups 191, 187, 157, 26, 66 in the text; **"Stenbock" written above 191** and further
  small glosses above other groups -- an interlinear (period or archival) decipherment on this leaf, hand not judged.

**Finding that bears on the key step.** Frame 0510's codes run up to at least **1056**, while Krauske's table
(Loc. 694/10) as eye-checked by A2-SAX covers codes 1-401 plus a column of composite numbers. Either the table's
composite column covers the high codes, or 1712 letters used a larger code than Krauske tabulated, or the numbers
are misread at this resolution (M). Not settled here. Frame 0580 (codes under 200, with glosses) is the better
first test frame: its glosses act as a check on Krauske's table (if Krauske's 191 reads Stenbock, the table and
this leaf agree on one code).

**Key-application step named, not run (per brief):** (a) Krauske's table ff.2-5 (images/0004-0007.jpg): line crops
with `tools/iiif_lines.py --image`, two blind passes + one reconciliation into `key.tsv` (grade H per code, M where
the passes split), ~$5 (about 9 vision calls at the per-pass rate); (b) 694/08 frame 0580: line crops, two blind
passes of the code groups and glosses + one reconciliation into a ciphertext file, ~$2; (c) `tools/decode_key.py
ciphers/sachsstaatsarchiv-manteuffel-1712` on that frame, with the leaf's own glosses as the known-answer check
(rule 3: the gloss comparison is the control). Total ~$7.

Requests: www.archiv.sachsen.de 2 record pages + 1 archiv.js + 2 files.json + 1 preview + 17 full-size frames = 23.
Vision: 5 contact-sheet reads + 1 preview + 2 crops by this worker = 8, no subagent calls.
Not done: 877 of 894 frames not inventoried (see gaps).

## Remaining gaps"/"## Escalation"; it did not (status `blocked`,
which gaps_check skips). The sections are written below for the first time, from this step.

**(1) Neues Archiv für sächsische Geschichte vols. 15-19 (1894-98).** Instead of be-api snippet search, the full
public-domain OCR (`neuesarchivfurNNsach_djvu.txt`, archive.org, 5 downloads) was grepped, which also gives page
context. Positive controls on the same files: "Dresden" 233/208/399/177/225 hits, "Flemming" 2/0/4/4/0 (vols
15-19), so the OCR reads and a name of this shape is findable. Target terms and OCR-variant stems
(`manteu`, `anteuff`, `krausk`, `chiffr`, `dechiff`, `Loc. 694`, `Geheimes Kabinet`):
- vol. 18 (1897): "Manteuffel" x1 = a review noting a marble bust of Graf Ernst Christoph von Manteuffel
  (line 11040, art-history review), not the reports; "Krauske" x4 = footnotes citing O. Krauske, *Der Große
  Kurfürst und die protestantischen Ungarn*, HZ LVIII 465 ff. -- this confirms an O. Krauske working on
  Prussian state-archive material, but the hits are unrelated to Manteuffel or ciphers. Flemming hits there are
  military-music/regiment history (1688, 1711, 1723) and the poet Paul Fleming.
- vols. 15, 16, 17, 19: no Manteuffel, Krauske, Chiffre/dechiffr hits; "Chiffer"/"Schiffer" hits are boatmen and an
  editorial "Chiffern" (sigla) note, vol. 15 l.2802.
Result: **not printed in NASG 1893-98** (vol. 14 by the 24 Sept pass, 15-19 now). A search result, not a novelty
verdict (rule 10).

**(4) The `#digitalisat` anchor on Loc. 694/10 -- resolved.** Catalogue record (quoted first, access playbook):
https://www.archiv.sachsen.de/archiv/bestand.jsp?guid=96698908-5fa7-4fb6-ae66-bf4617f6e401 -- "Archivaliensignatur
Loc. 00694/10 · Datierung 1712 - 1713 · Benutzung im Hauptstaatsarchiv Dresden", with a "Digitalisat" tab (7 images,
"Bild herunterladen"). The viewer's images are plain files at
`https://www.archiv.sachsen.de/digitalisate/<guid>/fullsize/000N.jpg` (curl, browser UA, HTTP 200 image/jpeg,
~4339x3865, 300 dpi, grayscale microfilm scans, film 1583-1589, Archivzentrum Hubertusburg). All 7 fetched to
`images/` (11 MB, `images/manifest.json` with URLs, sizes, sha256). Route: `tools/browser_fetch.js` on the
`cps/suche.html?q=Krauske` search to get the guid, then plain curl. The 24 Sept "did not resolve in 4 s" was a
render-wait problem, not an access block.

What the images show (eye check of reduced frames only; nothing transcribed this step):
- frame 1 Beiblatt: "Dieses Archivale umfasst die Blätter 1-5"; frame 2 binding: "Chiffern in Schreiben
  Manteuffels an Flemming 1712 f." / "Locat 694/10".
- f.1: "Chiffern-Auflösungen zu Berichten Manteuffels an Flemming aus den Jahren 1712, 1713 (angefertigt von
  Dr. Krauske 1893)".
- f.2 head: "Einige Chiffre-Auflösungen zu den Berichten Manteuffels an Flemming 1712 und 1713. Hauptstaatsarchiv
  zu Dresden vol. CXLV und CXLVI, Loc. 694/8-9", then **ff.2-5 are a numbered code table**: codes 1-~120 to
  letters, doubled letters, syllables and a few names (e.g. 1 f [Flemming], 13 m [Manteuffel]; several entries
  marked "non valeurs"), codes ~150-401 to names, titles and words (le Roi de Pologne, le Czar, Roi de Suède,
  Stanislas, le Roi de Prusse, Dresden, Berlin, la paix, l'envoyé...), and a column of composite numbers. Mixed
  German/French; the plaintext language of the reports is presumably French (inferred from the table, I).
  Reading of the table to be done at grade M/I by a later pass with line crops (Usage 6); none claimed here.

**Neighbouring records (one search, not opened):** `cps/suche.html?q=Manteuffel Flemming` lists **Loc. 00694/08**
(1712, guid 3a83f921-9a43-485f-874b-34653ed59b68) and **Loc. 00694/09** (1713, guid
c5158a8f-281c-49a8-985a-b0aa75400e17), "Des Kammerherrn, Baron von Manteuffel während seiner Verschickung an den
Königlich Preußischen Hof mit dem Generalfeldmarschall Herrn Graf von Flemming geführte Korrespondenz", **both with a
`#digitalisat` link** in the result list, as are 694/03, /04, /06 (1706-10, same series). Their image counts were not
read this step.

So the target's premise changes: the key-side (Krauske's 1893 table) and, on the result-list evidence, the letters
themselves appear to be online and copy-free; the REQUEST.md copy order is likely unnecessary. Status line left
as is (brief: not this worker's to change); flagged to LANE-A2PUSH.

Requests: archive.org 5 (djvu.txt) + 1 (advancedsearch); www.archiv.sachsen.de 3 browser renders + 7 image GETs.
Vision: 2 reads of reduced frames by this worker, no subagent calls.

## Remaining gaps (finish-or-blocker pass, 3 Oct 2026, A2-SAX)
Read so far: 0 of the 1712-13 reports read; Krauske's key table imaged (7 frames, ff.1-5), untranscribed; 17 of 894 report frames inventoried, 2 carry code groups (694/08 0510, 0580)
- Krauske's code table ff.2-5 and its application - blocker: not-attempted; table images and cipher frame 694/08 0580 on disk (A2-SAX2); next: line crops with tools/iiif_lines.py --image, two blind passes + reconcile into key.tsv, then the 0580 code groups the same way and decode_key.py with the leaf's own glosses as the check, ~$7
- Loc. 694/08 and /09 ciphered reports, 877 of 894 frames not inventoried - blocker: not-attempted; 894 frame URLs in images/loc694-08-09/frames.tsv, 17 sampled (A2-SAX2: 2 cipher, 1 possible); next: full-size fetch in batches of <=250 frames per session with a 1000-px contact-sheet y/n pass, ~$2 per batch
- print: Haake's Flemming biography, the Wackerbarth paper's "Chiffren de S. Exc. Mgr. le C. de Flemming" citation - blocker: not-attempted; NOTES 24 Sept steps (2)-(3); next: IA/Google Books fts for Haake + read the paper, ~$1

## Escalation (3 Oct 2026)
- [ ] siblings: Loc. 694/03, /04, /06 (1706-10, same Manteuffel series) carry digitisat links; not opened
- [ ] clear-pages: 694/08 frame 0580 carries interlinear glosses above code groups (Stenbock over 191, A2-SAX2) -- a known-answer check for Krauske's table; not yet read
- [x] known-keys: Krauske's 1893 key table, Loc. 694/10, located online and fetched (A2-SAX, 3 Oct 2026)
- [ ] print: NASG 1893-98 done, no print found; Haake and the Wackerbarth paper still to read
- [n/a] key-rebuild: a period-archive key exists; rebuild only if Krauske's table fails on the letters
- [ ] image-check: 694/10 imaged; 694/08-09: 894 frames listed, 17 sampled (2 cipher, 1 possible, A2-SAX2 3 Oct 2026), 877 to check
- [ ] retry: nothing has failed yet that needs a retry
Verdict: keep going: 3 internal gaps; cheapest next: transcribe Krauske's table ff.2-5 into key.tsv (line crops, 2 blind passes + reconcile) and apply it to 694/08 frame 0580 with decode_key.py, its own glosses as the check, ~$7
