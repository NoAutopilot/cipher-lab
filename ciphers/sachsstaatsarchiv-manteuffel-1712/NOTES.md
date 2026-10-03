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

## GAPS151-sachsstaatsarchiv-manteuffel-1712 (3 Oct 2026, account-4): Krauske's key table into key.tsv

Intake gate pasted before work: `sachsstaatsarchiv-manteuffel-1712: blocked (line 1) -- already terminal, nothing to gate` (exit 0).
Scope (prompt): the table only, ff.2-5 (images/0004-0007.jpg); then apply it to the ciphertext on disk.

**Crops.** `python3 tools/iiif_lines.py --image ciphers/sachsstaatsarchiv-manteuffel-1712/images/000N.jpg --out
ciphers/sachsstaatsarchiv-manteuffel-1712/images/table_crops --region 2100,870,1680,1400 --prefix fFtop --centres
50,150,...,1350 --lines-per-crop 14` and the same with `--region 2100,2070,1680,1400 --prefix fFbot` (N=4-7, F=2-5):
one top and one bottom half per folio, overlapping by 200 px. The tool's automatic line finder missed most rows
on this sparse table, and evenly spaced 13-line bands cut through rows 49, 98 and 283, hence the two overlapping halves.

**Two blind Opus passes** (one subagent call per pass per folio pair: 4 calls) -> `table_passes/pass{A,B}_f{2-3,4-5}.tsv`.
Agreement on value: ff.2-3 78/84 codes, ff.4-5 84/91. Every value split was either an alternative written in the
value or the note column (settled by joining) or a Kurrent name: 259 Ilgen?/Flynn?, 260 Kameke?/Haacken?, 191
Stenbock?/Steenbock?, 20.12 Blaspil?/Blassil?. **Reconciliation** (`reconcile_table.py`, settlements listed in
its RECON table with reasons; one reconciler image read of three spots): 259 Ilgen (Ilgen is also written beside codes 9, 39 and 46 on f.2 in
both passes), 260 Kameke (pass A reads Kameke beside code 11 on f.2), 191 Stenbock. All of these graded M.

**key.tsv: 157 codes**, 122 grade C, 35 grade M (alternatives such as `s|ss|sa`, nulls, the reconciled names, any
'?'). Codes with no value written (75, 86, 88, 94, 98) are left out of the key. **Grade C, not H**: Krauske's table is an
1893 archivist's compilation ("Einige Chiffre-Auflösungen", f.2 head), not the 1712 key sheet; key source class
`published` (Dr. Krauske, 1893, Loc. 694/10; rule 8). The table is a homophonic letter table (codes 1-120,
several codes per letter, a few marked "non valeurs"), a nomenclator (130-401: names, titles, places) and
compound groups (f.5 right column). `python3 reconcile_table.py --check` regenerates key.tsv and compounds.tsv.

**Internal check (compounds.tsv).** Krauske's 13 compound groups spelled through his own single-letter codes
match the opening letters of the word he gives in **8/13** (1.44 fl-Flemming, 17.16.44 pol-Polonois,
35.12.55 elb-Elbing, 11.21 kn-Kniphausen, 83.44 schl-Schlippenbach, 20.12 bl-Blaspil, 45.60 kr-Kreis?, 34.27
pr-prince). They disagree in 5: 8.60 hr-Grumbkow, 60.39 ri-roi, 17.6 pu-prince, 17.27.26 prr-prince royal,
mons.110.217. So most compounds are words spelled with the letter codes, and the 5 misses are either
abbreviations or misreads; none was re-read.

**Applied** (`decode.json`, `python3 tools/decode_key.py ciphers/sachsstaatsarchiv-manteuffel-1712 --check`:
"reading up to date", exit 0) to the only ciphertext on disk, the 24 code tokens A2-SAX2 eye-read from 694/08
frames 0510 and 0580 (`ciphertext.tsv`; all conf low, as that pass graded them M; not a transcription of either leaf).
**Grades: H 0, C 0, S 0, M 6, I 0, U 18** (U = code not in Krauske's table). Frame 0580: 191 Stenbock, 187 Roi de
Suède, 157 ?, 26 r, 66 a. **Known-answer check, 1 of 1:** the leaf's own gloss writes Stenbock over 191 (A2-SAX2),
and Krauske's table gives 191 = Stenbock. That is one agreement, not a control. Frame 0510: 2 of 18 codes are keyed (155 Flemming, 77 d). Its
codes run 213-1056, above or between the table's entries ("Einige" = some solutions only), so Krauske's table does
not cover that letter's nomenclator.

**Judge** (fr18, Torcy/Villars/Maintenon/Gazette, era-matched for 1712; leave-one-file-out false-negative rate
0.18-0.19 at N=200/500, tools/data/fr18/README.md, so a FAIL on a short text is weak): decode
`STENBOCKROI DE SUÈDERA FLEMMINGD` **FAIL, score -1.394** (null_p99 -1.377, real_p05 -1.101, N=29 letters);
shuffled-key decode (key values permuted, seed 1) **FAIL, -2.146** (null_p99 -1.145, real_p05 -1.114, N=20).
The judge cannot decide here: 29 letters, almost all nomenclator names, no prose. This is not a negative on the key
(rule 3). No 'reading ready' flag.

Vision: 4 blind subagent passes (Opus) + 1 reconciler read + 5 layout reads by this worker. Requests: none (all images on disk).

## GAPS154-sachsstaatsarchiv-manteuffel-1712 (3 Oct 2026, account-4): 694/08 f.468 transcribed, decoded, checked against its glosses

Intake gate before work: `sachsstaatsarchiv-manteuffel-1712: blocked (line 1) -- already terminal, nothing to gate` (exit 0).

**Crops.** `python3 tools/iiif_lines.py --image ciphers/sachsstaatsarchiv-manteuffel-1712/images/loc694-08-09/694-08_0580.jpg
--out ciphers/sachsstaatsarchiv-manteuffel-1712/images/f468_crops --region 870,1180,1270,1660 --prefix f468L --lines-per-crop 3
--overlap 0 --debug` -> "region 1270x1660, 24 lines, 8 bands x 1 segments; pitch 63"; same with `--region 2110,1180,1250,880
--prefix f468R` -> "9 lines, 3 bands". The leaf fills only ~1240 px of the 4345 px frame, so the passes were given copies of the
11 band boxes with 45 px added above and below (the tool's band 1 edge cut the "Stenbock" gloss) and scaled to 2400 px wide
(scratch, not committed; boxes in images/f468_crops/manifest.json).

**Two blind Opus passes** (one subagent call each, 11 crops per call) + reconciliation -> `f468/passes.tsv`. 20 code groups on
the leaf (19 single codes + one 7-number spelled group), all on the left page and R01; R02-R03 (the close and a P.S. "ma fille
est fort malade") carry none. **Agreement: 19/20 groups identical, glosses identical on all 17 glossed groups.** Split: the
spelled group, element 2 (35/38) and 4 (12/"R"); reconciler image read 35 and 12, both M. The 1/7 (177/171) and 4/9 (39, 9:
a y-shaped glyph) doubts were raised by the passes and left as read. `ciphertext.tsv`: the five A2-SAX2 eye-read 0580 rows are
replaced by these 26 tokens (0510 fragments kept).

**Decode** (`python3 tools/decode_key.py ciphers/sachsstaatsarchiv-manteuffel-1712 --check`: "reading up to date", exit 0).
f.468: **26/26 tokens covered by Krauske's table; grades H 0, C 18, S 0, M 8, I 0, U 0** (M: 191 x3, the table's own M grade;
298 two values; 39 and 9 low digit confidence; two split elements of the spelled group). Whole file (with 0510 fragments):
C 18, M 10, U 17. Reading of the groups: Stenbock, Roi de Suède, R[.], I[lgen], L[ol.], le czar, Le roi de Prusse (x3),
l'Empereur, la France, R[.], A[rn], W-E-L-L-P-N-G, Stenbock, I[lgen], Roi de Suède, Stenbock, Stanislas, A[rn].
The leaf uses single-letter codes standing alone as a person's initial (39/9 glossed Ilg./Ilgen, 44 Lol., 66 Arni/Arn, 26 with
"R." in the margin); Krauske's table notes "Ilgen" beside 9 and 39 and "Angleterre" beside 66.

**Gloss vs key** (`python3 f468/gloss_check.py --check` -> f468/gloss_check.txt; match rule written in its docstring before
scoring): **17/17 glossed instances agree (11/11 distinct codes)**; shuffled-key control (key values permuted over codes, 10,000
draws) **mean 0.67, p95 3, p99 5, max 8**. Spelled group (gloss Welling): the key spells w-e-l-l-**p**-n-g, 6/7 letters by
position (control mean 0.14, p99 1); the miss is 34 = p where the gloss wants i -- 39 = i in the same table, and both passes
flagged the writer's 4/9 glyph, so a 9 read as 4 is the likely cause (M, not settled). **Caveat on independence:** the glosses'
hand was not judged. If they are Krauske's own 1893 working notes, this agreement shows his table matches his own annotations,
not that either is right; if they are a period (1712) decipherer's, it is an independent check. Judging the hand against f.1-5
of Loc. 694/10 is the cheap way to settle it.

**Judge** (fr18, ad hoc spec with `corpora` = the six tools/data/fr18 files, era-matched for 1712; fold caveat: six files,
leave-one-file-out false-negative rate 0.18-0.19, tools/data/fr18/README.md): decode (group values joined, N=129)
**FAIL, score -1.252, null_p99 -1.654, real_p05 -1.012**; shuffled-key decode (seed 1, N=49) **FAIL, -1.656, null_p99 -1.385,
real_p05 -1.101**. The decode clears the shuffled-letter null and the shuffled-key decode does not, but neither reaches real
prose: the input is a list of names and initials, not prose (the clear text around the groups is not transcribed), so the
judge cannot decide here. Not a negative on the key (rule 3). No 'reading ready' flag: the gloss check is the stronger signal and
it already depends on the hand question above.

**Status word.** Line 1 stays `blocked`. A2-SAX's "stale" flag is right that access is no longer the blocker (images and key
are online and on disk), but `tools/intake_gate_check.py` refuses `partial` here: "partial (line 1) with no standard-edition
citation ... within 6 lines -- ... must read `blocked` instead" (exit 1, tried and reverted). It moves to `partial` when a
check-solved verdict naming the edition read and a Premise check are written.

Vision: 2 blind subagent passes (Opus, one call each) + 2 reconciler crop reads + 2 layout reads by this worker. Requests: none
(image on disk). Credit: the key is Dr. (Otto) Krauske's 1893 table, Loc. 694/10 (rule 8).

## Remaining gaps (finish-or-blocker pass, 3 Oct 2026, A2-SAX)
Read so far: 1 leaf of the 1712-13 reports decoded (694/08 f.468, its 20 code groups, GAPS154 3 Oct 2026; clear text not transcribed); Krauske's key table imaged (7 frames, ff.1-5), untranscribed; 17 of 894 report frames inventoried, 2 carry code groups (694/08 0510, 0580)
- Krauske's code table ff.2-5 and its application - blocker: open-codes; DONE for the table (GAPS151, 3 Oct 2026: key.tsv 157 codes, C 122 / M 35, compounds 8/13 self-consistent) and for 694/08 f.468 (GAPS154, 3 Oct 2026: 26/26 tokens keyed, C 18 M 8; gloss agreement 17/17 vs shuffled-key p99 5; spelled 'Welling' 6/7, 34=p vs i); 694/08 f.409 (frame 0510) codes run 213-1056, past the table; open: whose hand wrote the f.468 glosses (Krauske 1893 or period) -- next: compare the gloss hand with Loc. 694/10 ff.1-5 on disk, one reader call, ~$1
- Loc. 694/08 and /09 ciphered reports, 877 of 894 frames not inventoried - blocker: not-attempted; 894 frame URLs in images/loc694-08-09/frames.tsv, 17 sampled (A2-SAX2: 2 cipher, 1 possible); next: full-size fetch in batches of <=250 frames per session with a 1000-px contact-sheet y/n pass, ~$2 per batch
- print: Haake's Flemming biography, the Wackerbarth paper's "Chiffren de S. Exc. Mgr. le C. de Flemming" citation - blocker: not-attempted; NOTES 24 Sept steps (2)-(3); next: IA/Google Books fts for Haake + read the paper, ~$1

## Escalation (3 Oct 2026)
- [ ] siblings: Loc. 694/03, /04, /06 (1706-10, same Manteuffel series) carry digitisat links; not opened
- [x] clear-pages: 694/08 f.468 glosses transcribed and scored against the key, 17/17 vs shuffled-key p99 5 (GAPS154, 3 Oct 2026); independence of the glosses from Krauske not yet judged
- [x] known-keys: Krauske's 1893 key table, Loc. 694/10, located online and fetched (A2-SAX, 3 Oct 2026); transcribed into key.tsv, 157 codes (GAPS151, 3 Oct 2026)
- [ ] print: NASG 1893-98 done, no print found; Haake and the Wackerbarth paper still to read
- [n/a] key-rebuild: a period-archive key exists; rebuild only if Krauske's table fails on the letters
- [ ] image-check: 694/10 imaged; 694/08-09: 894 frames listed, 17 sampled (2 cipher, 1 possible, A2-SAX2 3 Oct 2026), 877 to check
- [ ] retry: nothing has failed yet that needs a retry
Verdict: keep going: 3 internal gaps; cheapest next: judge the f.468 gloss hand against Krauske's own hand on Loc. 694/10 ff.1-5 (images on disk, one reader call, ~$1), which decides whether the 17/17 gloss agreement is an independent check; then the check-solved + Premise check that would let line 1 read partial (Haake, the Wackerbarth paper), ~$3

## While waiting (GAPS154, 3 Oct 2026)

- Judge the f.468 interlinear gloss hand against Krauske's own hand on Loc. 694/10 ff.1-5 (images/0003-0007.jpg on disk): one reader call, ~$1, depends on nobody; it decides whether the 17/17 gloss agreement is an independent check of the key.
