# BnF fr.5160 — Loménie de Brienne (père et fils) to Abel Servien, 1653-1661

Status: open

Check-solved pass, 24 September 2026 (Sonnet, orchestrator brief for M13-M16). Editions-first + one-leaf pass;
a formal six-source check-solved run is still owed before board promotion.

## Correction to the queue row — the ciphered letters are not Le Tellier's

QUEUE.md M16 names this "Michel Le Tellier correspondence... 'en partie chiffrées, et souvent accompagnées du
déchiffrement' — about 47 letters, 10 Jan 1653 - 21 Dec 1661." Gallica's own catalogue description (via
`services/OAIRecord`) attributes the 47 partly-ciphered letters to a **different** correspondent:

> 1 Lettres originales adressées à Abel Servien par HENRI-AUGUSTE « DE LOMENIE », comte de « BRIENNE », et par
> son fils HENRI-LOUIS DE LOMENIE DE « BRIENNE », du 10 janvier 1653 au 21 décembre 1661. Ces lettres, dont
> plusieurs sont en partie chiffrées, et souvent accompagnées du déchiffrement, sont au nombre de 47 ;
> 2 Lettres originales de MICHEL « LE TELLIER », adressées au même, entre le 22 mars 1652 et le 27 août 1658...

Item 1 (the 47 ciphered letters, with contemporary decipherment) is Brienne père-et-fils to Servien. Item 2
(Le Tellier's own letters to Servien, a smaller, separately-dated set) carries **no** cipher note in the
catalogue description at all. The QUEUE row's title and the scout's "kind" (recovery, decipherment often
present) both describe item 1 correctly in substance, but mis-name the sender. Renamed correctly in this note;
QUEUE.md M16 row updated. The folder slug (`fr5160-letellier-1653`) is kept as filed by the scout to avoid a
second rename mid-pipeline, but should be corrected to something like `fr5160-brienne-servien-1653` if this is
promoted.

## Checked (24 Sept 2026)

- Fresh shallow clone of `dbourdeau/cyphersolver`: `letellier/NOTES.md` covers a **different, unrelated** item —
  "Le Tellier → Marquis de Castelnau, 12 May 1657", cryptiana transcription `LeTellier_Castelnau1657.txt`, a
  distinct cipher family ("Le Tellier-Colbert Cipher 2", tried and set aside as unsolved/skipped, too short).
  No shelfmark given in that note beyond the cryptiana transcription filename; not established whether it is
  from fr.5160 or elsewhere in the Le Tellier papers (BnF fr.4187 or SHD A1, per Bourdeau's own suggestion in
  that note). Worth checking as a possible same-key sibling once fr.5160's actual cipher is transcribed, not
  pursued this pass. No other hit on "5160", "Brienne" or "Servien" tied to this volume.
- Fresh shallow clone of `aaymeloglu/unsolved-ciphers`: no hit.
- `sources/cryptiana/web/louisxiv0.htm` (43 "Le Tellier" hits, local mirror, no fetch) is about the Louvois/Le
  Tellier war-ministry cipher family in general; not checked line-by-line against fr.5160's 47 letters this
  pass — flagged as the next step, since it is already on disk.
- Editions: "Caron 1898" (as named in the orchestrator brief) could not be identified as a specific, real
  edition of this correspondence — WebSearch surfaced only N.-L. Caron's 1881 *Michel Le Tellier, son
  administration comme intendant d'armée en Piémont, 1640-1643* (a different, earlier period of Le Tellier's
  career, and by a different given-name initial) and Pierre Caron (1875-1952), an unrelated archivist. *
  Correspondance administrative sous le règne de Louis XIV*, ed. G.B. Depping (Imprimerie nationale, 1850-1855,
  4 vols, digitised on Gallica) is real and covers Louis XIV's administrative correspondence, organised by
  subject (provincial estates; justice/police/galleys; public works/religious affairs/sciences) rather than by
  correspondent pair; whether it includes any Brienne-Servien 1653-61 letters was **not established** this
  pass — a volume-by-volume index check is the next step, not a network fetch.
- Gallica IIIF, one leaf plus two extra probes (367-canvas volume): canvas 20 = folio 7, a clear French letter
  about the 1653 siege of Bordeaux, no cipher (`images/f20.jpg`). Canvas 100 = faint, largely illegible verso
  show-through, no cipher visible (`images/f100.jpg`). Canvas 150 = blank verso (`images/f150.jpg`). **No
  ciphertext passage was located in this three-leaf sample** of 367 canvases for 47 letters — expected, since
  the ciphered passages are a minority within each letter and scattered through the volume; not a negative
  finding on the catalogue's own claim.

## Verdict

Open at stage 2. The catalogue's own claim (47 letters, several partly ciphered, often with contemporary
decipherment already in the volume) was not contradicted, but also not directly confirmed on an image this
pass — a genuine gap, flagged rather than assumed. Kind: recovery (decipherment often present), as scored,
**for Brienne père-et-fils, not Le Tellier**. No reading attempted, nothing to grade.

Cheapest next step: use archivesetmanuscrits.bnf.fr's item-level listing (if it enumerates the 47 letters
individually, as it did for fr.4687) to get folio numbers for the ciphered ones directly, instead of paging the
367-canvas manifest blind; then view two or three of those specific leaves to confirm the "often accompanied by
decipherment" claim and separate the letters that already carry one from the ones that do not.

## Sources

- Gallica: `https://gallica.bnf.fr/ark:/12148/btv1b9060495t`, OAI record via
  `https://gallica.bnf.fr/services/OAIRecord?ark=btv1b9060495t`.
- `sources/cryptiana/web/louisxiv0.htm` (S. Tomokiyo), local mirror, not yet read against this target.
- github.com/dbourdeau/cyphersolver `letellier/NOTES.md` (a different item, cite only, code MIT / text CC BY
  4.0, nothing copied); github.com/aaymeloglu/unsolved-ciphers (checked, no relevant content).

## Requests this pass

gallica.bnf.fr: 1 OAI record + 1 manifest + 3 IIIF image fetches. github.com: 2 shallow clones (shared with
M13-M15, deleted after grep). WebSearch: 2 queries.

## Census pass, 24 September 2026 (archive-lookup brief, Sonnet)

### (1) archivesetmanuscrits.bnf.fr item-level notice

Fetched `https://archivesetmanuscrits.bnf.fr/ark:/12148/cc58150z` directly (one redirect to https, one
connection reset recovered on the single allowed retry — proxy-side `ws_closed_mid_exchange`, not a site
block; confirmed via `$HTTPS_PROXY/__agentproxy/status`). **It does not enumerate the 47 letters individually.**
The only folio information is the two-item split already known:

> Fol. 1-110 • 1 Lettres originales adressées à Abel Servien par HENRI-AUGUSTE « DE LOMENIE », comte de
> « BRIENNE »... sont au nombre de 47.
> Fol. 111-182 • 2 Lettres originales de MICHEL « LE TELLIER »...

with three named sub-pieces inside item 2 only (Fol.148 "Estat des troupes... 1653"; Fol.150-151 a copy of a
Servien→Le Tellier letter of 11 Oct 1653; Fol.176 a Le Tellier order of 1 Jan 1658) — item 1 gets no such
breakdown. Also confirmed from this notice: 182 feuillets + a preliminary feuillet A, folio 127 is blank
(within item 2), old shelfmarks Anc. 9751(7) / Cangé 16. **Usable result: the search space for the 47 letters
is folios 1-110 of 182 (≈60% of the volume), not the full 367-canvas manifest** — worth stating plainly since
the brief asked whether this route would narrow the walk, and it does, just not down to individual letters.

### (2) Canvas-to-folio calibration and IIIF census walk

Two prior calibration points (this NOTES.md's earlier pass: canvas 20 = folio "7"; this pass's own corner-crop
read: canvas 107 = folio "57", `images/f107_corner.jpg`) do **not** sit on a consistent linear rate — 87
canvases for a claimed 50-folio jump (1.74 canvas/folio, physically impossible if every folio is imaged
recto+verso, i.e. ≥2 canvas/folio). A second, independently-read set of calibration points from the census walk
below is internally consistent at exactly 2.0 canvas/folio (canvas 160=folio 82, 164=84, 176=90, 180=92) and a
further point, canvas 8 = folio 1, sits close to that same rate over a longer span (152 canvases / 81 folios =
1.88/folio, plausibly explained by a handful of unfoliated or single-canvas leaves rather than a different
rate). **The canvas 107 = "57" read is flagged as probably a misread or a local irregularity and should not be
trusted without a fresh look** — not resolved this pass, following the fr16092 precedent of flagging rather
than forcing a formula (ROOM.md 24 Sept, fr16092 print-check worker).

Walked the manifest from canvas 8 to canvas 220 in steps of 4 (54 fetches, IIIF `,600` width thumbnails,
1.5 s apart, descriptive User-Agent; 3 transient connection resets, each recovered on the one allowed retry, no
403/altcha at any point) — this range covers item 1's folios 1-110 with margin. Images are in
`images/census/f{canvas}.jpg` (1.5 MB total, folder well under the 30 MB cap). A Sonnet subagent read all 54
thumbnails blind (no network access) and classified each one; full per-canvas table below.

**Result: 6 of 54 sampled canvases (11%) show cipher or mixed cipher+prose content, in two bands, not
scattered evenly:**

| band | canvases | approx. folios | approx. date (from adjacent dated leaves) |
|---|---|---|---|
| early | 8, 12, 24 (mixed), 32 (full-page cipher) | ~1, 3, 9, ~12 | January 1653 (canvas 12 dated "Paris 2 Janvier 1653") |
| late | 168, 172 (mixed) | ~86, ~88 | within the autumn/winter 1659 run (undated on the sampled leaves themselves; neighbours at canvas 156-212 run Nov-Dec 1659) |

**None of the 6 cipher/mixed canvases in this sample show a visible interlinear or marginal decipherment** —
every cipher passage reads as bare numeral/code groups with no French gloss on the same page. This does not
contradict the catalogue's "souvent accompagnées du déchiffrement": a stride-4 sample can miss a facing or
adjacent leaf that carries the decipherment (a common layout — decipherment on the verso, or on an inserted
slip), and "souvent" (often) is not "always" against 47 letters. But it means **the Dupuy-468 pattern (some
letters keyed by an attached decipherment, others not) is not yet demonstrated for any specific letter here** —
the cheapest next step (below) is to look at *every* canvas in the two identified bands, not just every fourth
one.

Two more observations, unplanned but worth recording: (a) the letters are **not in strict chronological
folio order** at fine grain — canvas 40 is dated "12 Octobre 1653" and canvas 52, only 12 canvases (6 folios)
later, is already dated "...1659"; a plausible reading is that the volume groups the father's few 1653 letters
first and the son's much larger 1659-61 run after, rather than interleaving by date, but this is **inferred,
not established** (grade I). (b) the sampled canvases never leave the Brienne-to-Servien register (no shift in
hand, salutation, or subject) all the way to canvas 220, and canvas 180 already reads folio 92 at the confirmed
2.0 canvas/folio rate — so item 1's folio-110 boundary likely falls close to canvas 216-226, not further out;
the last sampled canvases (216, 220) are blank/docket leaves consistent with a letter collection winding down,
though no 1660-1661-dated leaf was seen in this sample, so those final two years' letters are either compressed
into very few folios near the end or fell in one of the unsampled gaps.

Full per-canvas table (canvas = Gallica IIIF canvas number = `images/census/f{canvas}.jpg`; folio only given
where a digit was actually legible top-right; "-" = illegible/cropped/verso):

```
canvas	folio	content_type	decipherment	density	note
8	1	mixed	n	~1/3 page	"Monsieur" opening; ~8 lines cipher mid-page; BnF round ownership stamp
12	3	mixed	n	~1/3 page	dated Paris 2 Janvier 1653; cipher block then closing prose
16	-	clear	-	-	"Monsieur"; Mar.l de Brézé/army campaign, no cipher
20	7	clear	-	-	calibration point (prior pass): "Monsieur", Italy news, no cipher
24	9	mixed	n	most of page	"Monsieur" opening then ~10-line dense cipher block
28	-	clear	-	-	continuation prose, no numerals, verso
32	-	cipher	n	full page	~14 lines dense numeral groups, almost no prose
36	-	clear	-	-	mentions Duc de Candale, Ballaguier
40	-	clear	-	-	dated Paris 12 Octobre 1653, signed, closing
44	-	blank	-	-	near-blank, small round archival/collection stamp only
48	-	blank	-	-	blank verso, faint show-through only
52	-	clear	-	-	dated Paris ...1659, "Monsieur" closing
56	-	clear	-	-	dated Paris 1er Aoust 1659
60	-	clear	-	-	dated Paris [avril] 1659, army/campaign talk
64	-	clear	-	-	Danzig ambassadors, Poland negotiations
68	-	clear	-	-	dated Paris 2 May 1659
72	-	clear	-	-	diplomatic prose on peace, Ottomans, princes
76	-	blank	-	-	blank, faint show-through text only
80	-	clear	-	-	dated Paris 16 May 1659, signed Brienne
84	-	blank	-	-	blank, faint show-through only
88	-	clear	-	-	dated Paris 5e [month] 1659, short letter
92	-	clear	-	-	dated Paris 27 Juin 1659
96	-	blank	-	-	near-blank, faint "1659" show-through
100	-	blank	-	-	near-blank, faint show-through only (prior pass: `images/f100.jpg`)
104	-	clear	-	-	dated ...Aoust 1659, church/court matters
108	-	clear	-	-	dense prose, no date visible
112	-	clear	-	-	dated Bordeaux 1er...1659, parliament/treaty talk
116	-	clear	-	-	dated Bordeaux 18 Septembre 1659, signed Brienne
120	-	clear	-	-	dated Paris ...1659, ambassadors discussion
124	-	docket	-	-	blank folded leaf, faint sideways archival endorsement
128	-	blank	-	-	blank, fold lines visible, faint signature at bottom
132	-	clear	-	-	dense cursive prose, ink blots, no date visible
136	-	clear	-	-	dated Fontainebleau 8e[?] 1659, Duc de Parme/Infante marriage
140	-	clear	-	-	dated ...1659, Marquise/Duc de Parme
144	-	blank	-	-	near-blank, faint show-through only
148	-	blank	-	-	near-blank, faint show-through only
152	-	clear	-	-	dated Paris 7 [month] 1659, endorsed "Reims"
156	-	clear	-	-	dated Chalons 9 Novembre 1659, short letter
160	82	clear	-	-	Peace of the Pyrenees / Infante marriage discussion
164	84	clear	-	-	continues peace/marriage negotiation news
168	86	mixed	n	~1/3 page	discusses Sauvage/Ambrun; ~9-line cipher block at bottom
172	88	mixed	n	~1/2 page	Roy's orders, troops/ships; ~11-line dense cipher block
176	90	blank	-	-	blank page, foliation clearly visible top right
180	92	blank	-	-	blank page, small ink blot mid-page
184	-	clear	-	-	dated 5 Xbre (Décembre) 1659, royal family/marriage topic
188	-	clear	-	-	mariage Princesse / Espagnol match discussion
192	-	clear	-	-	dated ...Décembre 1659, frontier towns/court
196	-	clear	-	-	continuation prose, mentions "Duc de Sauvoye"
200	-	clear	-	-	dated Thoulouse 19 Décembre 1659, army/peace/marriage news
204	-	clear	-	-	discusses Angleterre, Général Monck, Écosse politics
208	-	clear	-	-	continuation, dense diplomatic prose
212	-	clear	-	-	dated Paris 26 Décembre 1659, signed Brienne, Savoie/Sénat de Turin
216	-	blank	-	-	near-blank, faint show-through, scattered ink specks
220	-	docket	-	-	near-blank leaf, faint flourish + faint "Servien" address note
```

Grade: all of the above is M (uncertain/model-read from a low-resolution thumbnail, not a transcription) — no
sign has been counted precisely and no date has been cross-checked against a second source. Content-type and
decipherment-presence calls at this resolution can be wrong, especially "blank" vs "docket" and the absence
of a faint interlinear gloss.

### (3) Print check

- `sources/cryptiana/web/servien.htm` (Tomokiyo, local mirror, no fetch): covers a **different** Servien
  item — Baluze 155, Servien to Melchior de Sabran, Oct-Dec 1632 — unrelated correspondent pair and 21 years
  earlier than fr.5160.
- `sources/cryptiana/web/louisxiv0.htm` (local mirror, no fetch): documents two ciphers used by **Henri-Auguste
  de Loménie, comte de Brienne père** in this exact office/period but with a **different** correspondent,
  D'Estrades — "Brienne's Cipher 1" (DE=46, BnF Clairambault 411, 1647) and "Brienne's Cipher 2" (DE=47, BnF
  Clairambault 579, 1651, explicitly noted there as "a large part of the letter is in numerical cipher with
  interlinear decipherment" — the same design pattern the fr.5160 catalogue note describes). No mention of
  fr.5160, Servien, or any Brienne-Servien letter 1653-61 anywhere on this page (checked by keyword count:
  15 "Brienne" hits, all D'Estrades-related; 0 "5160"). **Worth flagging as a lead for whoever eventually keys
  fr.5160's cipher**, not as a prior reading of this item: the same chancery may have reused or evolved this
  cipher design for Servien.
- Fresh shallow clone of `dbourdeau/cyphersolver` (deleted after grep): `bordeaux/NOTES.md` is a **different,
  unrelated shelfmark** — Antoine de Bordeaux (French resident in London) to Brienne, BL Add MS 4200 (Thurloe
  papers) + BnF Mélanges de Colbert 11, 1653-54, not BnF fr.5160. (The "Bordeaux" in that item's title is the
  diplomat Antoine de Bordeaux, coincidentally distinct from the city of Bordeaux mentioned in fr.5160 folio 7's
  text about the 1653 siege — two unrelated senses flagged so nobody conflates them.) That item is issued by
  the **same office** (Brienne's secretariat, per that NOTES.md's own analysis of the cipher design) and gives
  a second recovered key (George Lasry, 19 Feb 2025, for the 1654 copy) plus a design hypothesis for the whole
  1651-54 family — another candidate starting point for fr.5160's key, not a prior reading of fr.5160 itself.
  No other file in the repo matched "5160" or "brienne" (case-insensitive) beyond this and the incidental
  filename collision already logged in the prior pass.
- Fresh shallow clone of `aaymeloglu/unsolved-ciphers` (deleted after grep): `catalogue/decode-catalog.csv` has
  no row for "Brienne", "Loménie", or any BnF fr.5160 shelfmark. (DECODE record id 5160 itself is an unrelated
  Uppsala item, 1772-1809 — a coincidence of the row number, not a match.) The four Servien rows in that
  catalogue are all Baluze 155, 1632, already covered by `servien.htm` above.
- Depping, *Correspondance administrative sous le règne de Louis XIV* (Imprimerie nationale, 1850-55), 4 vols,
  checked via Internet Archive full-text search (`be-api.us.archive.org/fts/v1/search`, one query per volume,
  1.5 s apart, no login needed) for "Servien": vol.1 and vol.3, 0 hits; vol.2 and vol.4, 1 hit each, both
  incidental mentions of Servien as "ambassadeur en Piémont" / his brother, in unrelated administrative
  correspondence — **no hit connects to the Brienne-Servien 1653-61 letters or to any ciphered passage**.
  Confirms the "not by correspondent pair" description from the prior pass; this edition does not print
  fr.5160's letters. Not checked: a page-by-page browse (only full-text search was run).
- Google Books (`&key=$GOOGLE_BOOKS_KEY&country=US`, key never printed): a broad query ("Loménie de Brienne"
  Servien correspondance chiffre) returned 300 generic hits with no clear match; a narrower `intitle:` query
  (Servien Brienne 1653 lettres) returned 0. No edition specifically titled around this correspondent pair was
  found.

### Status and next step

**Status stays `open`.** This pass upgrades the evidence from "catalogue claim, unconfirmed on any image" (prior
pass) to **directly confirmed**: ciphertext is present in this volume, in at least two folio bands (~1-12 and
~86-88 of the 110), one dated January 1653. No decipherment has been found yet for any specific letter, so the
Dupuy-468 "which letters carry the key" question remains open, not answered. Kind stays recovery (decipherment
often present per catalogue, not yet confirmed present per any image).

**Cheapest next step:** dense (every-canvas, not every-fourth) sampling of just the two identified bands —
canvas 4-36 (folios ~1-14) and canvas 160-180 (folios ~82-92) — roughly 40 more thumbnail fetches total, far
cheaper than a blind full-volume walk, to (a) find the letter boundaries and exact dates for the ciphered
letters, (b) check the facing/adjacent canvases the stride-4 walk skipped for a decipherment this sample may
have missed, and (c) get a real sign-count once a specific ciphertext page is pinned down. A second, unrelated
next step already flagged in the prior pass (checking `louisxiv0.htm`'s 43 "Le Tellier" hits against item 2)
is out of scope here since item 2 carries no cipher note.

### Requests this pass

gallica.bnf.fr: ~63 (2 texteBrut probes, both redirected to an altcha challenge — stopped, not retried, and not
used again this pass; 1 manifest fetch already on disk from the prior pass; 2 single-leaf thumbnails + 1 corner
crop for calibration, one of the corner-crop attempts hit a connection reset and was retried once; 54 census
thumbnails in the canvas 8-220 walk, 3 of which hit a connection reset and were retried once each, all
recovered — no 403/altcha from any IIIF image fetch). archivesetmanuscrits.bnf.fr: 3 (1 redirect, 1 connection
reset retried once, 1 success). archive.org / be-api.us.archive.org: 6 (1 advancedsearch, 1 bad-identifier
probe, 4 full-text-search queries, one per Depping volume). googleapis.com/books: 2. github.com: 2 shallow
clones (cyphersolver, unsolved-ciphers; both cited above, nothing copied, deleted after grep). WebSearch: 0
(direct API/catalogue checks covered this pass's print-check). One Sonnet subagent (image reading only, no
network access, 56 tool uses, ~100k tokens) for the 54-thumbnail classification. Folder size: 2.3 MB, well
under the 30 MB cap.
