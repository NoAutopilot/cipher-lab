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

## Dense band walk, native crops, passes, key trial — 24 September 2026 (Sonnet, cap $12, orchestrator wake)

Cheapest-next-step from the prior pass, executed: every-canvas (not stride-4) coverage of the two cipher bands
identified by the census (canvas 4-36 and 160-180), then native-resolution fetches and two blind transcription
passes on the most fully ciphered letter, plus a mechanical trial of Tomokiyo's two published same-office
Brienne key tables against it.

### (1) Dense walk, canvas 4-36 and 160-180

40 canvases were still missing after the stride-4 census (14 of the 54 in-range values were already on disk).
Fetched with `--max-time 30` (the default curl timeout intermittently failed under this session's concurrent
multi-worker load on gallica.bnf.fr — two connection resets on canvas 4 at the default timeout, both recovered
once `--max-time 30` was used; see Requests below). 39/40 succeeded; canvas 29 failed twice (connection reset
both times) and was left unfetched, logged rather than retried a third time (good-citizen rule). Band coverage
is now canvas 4-36 minus 29 (32/33) and canvas 160-180 (21/21), i.e. every canvas in both bands except one. A
Sonnet subagent (image-only, no network) classified all 53 on-disk canvases in the two bands; full table:

```
canvas	folio	date	content_type	decipherment	rough_sign_count	note
4	-	-	blank	n	-	Blank flyleaf recto; faint mirrored ghost bleed-through of title-page text (f6) only
5	-	-	blank	n	-	Blank leaf; faint mirrored ghost bleed-through, no independent ink
6	1	-	clear	n	-	Volume title page: "Lettres Originalles Escrittes a M.r Servien par M.r de Brienne"; archival ink note top right, inventory letter "A"
7	-	-	blank	n	-	Blank flyleaf verso; mirrored ghost of title page; partial red/circular archive stamp bleeding from facing recto
8	1	-	mixed	n	~50	Opens "Monsieur" with prose paragraph, then ~5-line cipher block (symbol+numeral hybrid); wax/lead seal impression bottom left
9	-	-	cipher	n	~90	Continuous dense cipher text, no prose; partial round seal visible mid-right
10	2	-	mixed	n	~80	Cipher block occupies most of page; two plaintext closing lines at bottom
11	-	10 [mois] 1653	mixed	n	~40	Prose before and after a short cipher block; date possibly a docket note
12	3	2 janvier 1653	mixed	n	~35	Short cipher block (~4 lines) then prose closing; dated 2 January 1653
13	-	-	blank	n	-	Blank leaf, mirrored ghost bleed-through only
14	4	-	blank	n	-	Blank leaf faintly numbered "4"; ghost bleed-through only
15	-	-	docket	n	-	Blank/verso leaf with marginal endorsement note naming sender/addressee
16	5	-	clear	n	-	New letter "Monsieur"; marechal departing to lead an army, Bordeaux/Flanders affairs; entirely plaintext
17	-	1653	clear	n	-	Continuation; Spain/England, Dunkerque; date "1653" faint bottom right
18	6	20 juin 1653	clear	n	-	Short closing paragraph and signature block, dated 20 June 1653
19	-	9e[?] 1653	docket	n	-	Verso with marginal docket noting sender/date
20	7	-	clear	n	-	New letter "l'ordinaire d'Italie n'estant pas arrive..."; Italy post, Dutch/English naval affairs
21	-	27 juin 1653	clear	n	-	Continuation and closing, dated 27 June 1653
22	8	-	blank	n	-	Blank leaf numbered 8
23	-	27 [mois] 1653	docket	n	-	Verso with marginal docket, date 27 [mois] 1653
24	9	-	mixed	n	~70	Prose opening then dense cipher block; no interlinear gloss
25	-	-	mixed	n	~80	Cipher block continues (~8 lines); ends with brief plaintext phrase
26	10	-	clear	n	-	Full prose letter; opening phrase echoes f24's ciphered letter but this copy is uncoded (possibly a plain duplicate/related letter)
27	-	-	clear	n	-	New letter re: "un marechal nomme Jean Guscar/Ducar"; entirely plaintext
28	-	-	clear	n	-	Continuation of f27; draft-like hand with cross-outs
29	-	-	-	-	-	NOT FETCHED — two connection resets, logged not retried further
30	-	-	cipher	n	~90	Dense cipher block (~9 lines), no plaintext
31	19	-	mixed	n	~60	Cipher lines, then prose re: Mantua, then cipher resumes; no gloss
32	-	-	cipher	n	~90	Dense cipher block (~9 lines); final line breaks into plaintext "le Comte Philippes" continuing onto next leaf
33	20	-	mixed	n	~60	Prose re: duc de Savoye/Montferrat, then cipher block (~6 lines); no gloss
34	-	-	clear	n	-	Prose continuation, siege of Bordeaux, Spanish troops
35	21	1 aoust 1653	clear	n	-	Closing of letter dated 1 August 1653
36	22	-	clear	n	-	Prose continuation; page ends mid-sentence
160	82	-	clear	n	-	Letter re: peace treaty with Spain and the Infanta's marriage
161	-	3 [mois] 1659(?)	clear	n	-	Short closing note and signature "Brienne"
162	83	-	blank	n	-	Blank leaf numbered 83
163	-	-	blank	n	-	Blank leaf; faint ghost of facing page only
164	84	4 [mois] 1659(?)	clear	n	-	Full prose letter re: peace treaty and royal marriage negotiations
165	-	-	blank	n	-	Blank leaf, strong mirrored ink offset plus pen-trial strokes
166	85	-	clear	n	-	Full letter, ink noticeably faint throughout; no cipher
167	-	-	blank	n	-	Blank leaf; ghost bleed-through only
168	86	-	mixed	n	~110	Prose re: Mme de Savoye, then dense NUMERAL-ONLY cipher block (~9 lines) — distinct style from band 1's symbol+numeral hybrid
169	-	-	mixed	n	~80	Numeral cipher block (~7 lines) continues, then breaks into prose
170	87	21 [mois] 1659	clear	n	-	Headed "Dechiffre de la lettre de M.r le Comte de Brienne du 21 9.bre 1659" — a full PLAINTEXT DECIPHERMENT TRANSCRIPT, on its own leaf, no cipher of its own (see flag below)
171	-	-	blank	n	-	Blank/very faint leaf; ghost bleed-through only
172	88	-	mixed	n	~110	Prose re: transport of horses/habits out of the kingdom, then dense numeral cipher block (~9 lines)
173	-	27 [mois] 1659	mixed	n	~45	Short numeral cipher block continuing, then plaintext closing and date
174	89	-	clear	n	-	Full prose letter, Madame Royale, Marquis d'Ombrun; no cipher
175	-	24 [mois] 1659	clear	n	-	Short closing paragraph, dated 24 [mois] 1659
176	90	-	blank	n	-	Blank leaf numbered 90
177	-	-	blank	n	-	Blank leaf, faint mirrored ink offset
178	91	Nouembre 1659	clear	n	-	Short letter re: ratification/marriage negotiations, dated November 1659, signed "Brienne"
179	-	-	blank	n	-	Blank leaf with faint bleed-through and pen-trial flourish marks
180	92	-	blank	n	-	Blank leaf numbered 92, last leaf of band 2; small ink dot only
```

Grade M throughout (model-read from images, not a transcription; content-type/decipherment calls can be wrong).

**Cipher/mixed canvases in dense coverage (18 of 53, canvas 29 unread):** band 1 — 8, 9, 10, 11, 12 (folios
1-3, a five-leaf cluster, dated 2 Jan 1653 on one leaf); 24, 25 (folio 9); 30, 31, 32, 33 (folios 19-20). Band
2 — 168, 169 (folio 86); 172, 173 (folio 88). **No interlinear or marginal decipherment sits on any of these
18 leaves themselves.**

**Flag — a decipherment DOES exist in this dossier, on a separate leaf, not interlined:** canvas 170 (folio 87)
is headed, in clear French in a contemporary hand, "Dechiffre de la lettre de M.r le Comte de Brienne du 21
9.bre [novembre — correction, 24 Sept 2026: "9.bre" is the standard period abbreviation for novembre (7bre =
septembre, 8bre = octobre, 9bre = novembre, Xbre = décembre); the prior pass's gloss "septembre" was wrong] 1659"
(Deciphered from the letter of the Comte de Brienne of 21 November 1659) and carries a
full plaintext transcript — but as a standalone leaf, not written over or beside the cipher. The adjacent
ciphered letter (folio 86, canvas 168-169) opens "Monsieur, La lettre qu'il vous a pleu de m'escrire du 8e ce
mois..." and is dated by its neighbours to the same autumn 1659 run; the date match (21 November) between the
decipherment's heading and the letter's likely date is suggestive but **not confirmed** this pass — the two
were not cross-read token by token, and folio 86's own leaf carries no explicit date in the portion read. This
is exactly the Dupuy-468-style pattern the catalogue's "souvent accompagnee du dechiffrement" describes, just
realised as a companion leaf rather than an interlinear gloss. **Not pursued further this pass** (out of scope:
the brief asked for a mechanical trial of Tomokiyo's published tables against a blind pass, not reconciliation
against this in-dossier crib) — flagged as the single highest-value next step for whoever works this target
next: align folio 86's cipher against folio 87's clear French token by token, which would very likely recover
fr.5160's own key directly (grade C, known-plaintext) rather than guessing from a different, same-office cipher.

### (2) Native fetches and crops

Two most-fully-ciphered letters by the dense-walk table: the folio 1-3 cluster (canvas 8-10, five leaves of
cipher/mixed content, symbol+numeral hybrid, dated 2 Jan 1653 — the densest single run) and the folio 86-88
letter (canvas 168-170, numeral-only cipher, with the companion decipherment leaf at canvas 170). Fetched
native-resolution images for 6 leaves (canvas 8, 9, 10, 168, 169, 170; `full/full/0/native.jpg`, ~3810x5342px,
2.3-2.5MB each) — at the cap named in the brief. Cut 5 crops from these (folio 1-2 body text for the passes;
the folio 86 cipher block and folio 87 decipherment heading for documentation, not transcribed this pass), all
resized to <=2400px on the long side. `images/manifest.json` updated. Folder now 21MB, under the 30MB cap.

### (3) Two blind Sonnet passes, folio 1-2 letter (canvas 8-10)

Designated the folio 1-2 letter (canvas 8, 9, 10 — the "first" of the two chosen letters, and the one with
richest interspersed clear-French camouflage phrases matching Tomokiyo's description of this cipher family's
style) as the transcription target. Two independent Sonnet subagents transcribed it blind from the crops
(`passA.tsv`, `passB.tsv`; line/position/group/confidence, overline/macron on a code recorded with a leading
"_"). See "Agreement" below.

### (4) Mechanical key trial

`key_brienne_1647.tsv` (Tomokiyo's "Brienne's Cipher 1", DE=46, Clairambault 411, reconstructed by George
Lasry) and `key_brienne_1651.tsv` (his "Brienne's Cipher 2", DE=47, Clairambault 579, same reconstructor) were
transcribed mechanically from `sources/cryptiana/web/louisxiv0_Brienne{1,2}.png` (fetched fresh this pass, not
previously mirrored) by two Sonnet subagents, code+plaintext columns only. `decode.py` applies a key to a pass
TSV and scores the output against a small embedded French word list, with a shuffled-key control at the same
seed (rule 3). See "Key trial results" below.

### Agreement, passA vs passB (canvas 8-10, folio 1-2 letter)

Two Sonnet subagents transcribed the three crops blind and independently (`passA.tsv`, `passB.tsv`; neither
saw the other's output or any existing key/reading). `agreement.py` compares them line by line: same token
count at a line, and exact string match position by position (raw group only, confidence ignored).

- 47 lines total; 35 have the same cipher-group count in both passes; only 2 lines agree on every token.
- Token-level agreement, counting only the 35 count-matched lines: **258/392 = 65.8%**.
- **A line-count divergence opens on the f9 crop**: pass A reads 16 physical lines on f9_body (ending
  `f9_L16` = the clear line "nayant pas en sorte"), pass B reads 18 (`f9_L18` = the same clear line). The two
  passes agree on every group up through `f9_L12`, then `f9_L13`/`f9_L14` have matching *counts* but **0%
  token agreement** — the clearest sign of a line boundary drawn in different places by the two readers from
  that point on (one reader likely split what the other read as one line into two, or vice versa), which then
  carries the misalignment through the rest of the leaf. Not reconciled this pass (out of scope: "no
  reconciliation beyond the agreement table" per brief) — flagged as exactly the kind of disagreement rule
  6 of Usage ("two transcription passes... unless the two disagree on more than a tenth of the rows") would
  trigger a third pass for, if this target is picked up for a real transcription campaign.
- The clear-French phrases agree closely where both passes see the same line (7/12 clear-line pairs identical
  verbatim, the rest differing only in a stray letter or apostrophe — e.g. "quitte ne prennent" vs "quils ne
  prennent", both plausible misreadings of the same cursive hand) — this cross-checks against Tomokiyo's
  description of this cipher family's camouflage style (clear French phrases interspersed with cipher
  groups), independent of any decoding.
- Overall: legible enough for a confident line-count and a real (if noisy) sense of the cipher's density and
  alternation with clear French, **not** legible enough at this crop resolution/single-pass-per-reader depth
  for a committed transcription — matches the fr20140-danzay-1557 precedent (24 Sept 2026 pass) where two
  blind reads of a dense hybrid cipher diverge substantially without a third pass or higher-resolution crops.

### Key trial results (mechanical, passA only)

`decode.py key_brienne_1647.tsv passA.tsv --check` and the same for `key_brienne_1651.tsv`, both seed 1.
passA has 506 cipher-group tokens; `--check` confirms both runs are deterministic.

| key | resolved (H) | unresolved (U) | decoded chars | French-word chars (real) | French-word chars (shuffled control) |
|---|---|---|---|---|---|
| key_brienne_1647.tsv (DE=46, 1647) | 205/506 | 301/506 | 347 | **100 (28.8%), 46 words** | 70 (20.5%), 33 words |
| key_brienne_1651.tsv (DE=47, 1651) | 216/506 | 290/506 | 272 | **45 (16.5%), 22 words** | 126 (38.4%), 55 words |

**Neither key produces more French than its own shuffled-key control** (rule 3: no negative without a matched
control). The 1647 key does marginally better than its control (46 vs 33 words) but the margin is small and
the "French words" here are almost all 1-3 letter function-word homophones (se, es, et, ta...) that a
short-token embedded wordlist will match by chance at a high base rate regardless of key — not evidence of
real decode quality. The 1651 key does **worse** than its own control (22 vs 55 words), a clean negative.
This is exactly the expected result: both keys are Tomokiyo's reconstructions for the *same office*
(Loménie de Brienne père) writing to a *different* correspondent (D'Estrades, 1647 and 1651) — same-office
leads, not fr.5160's own key, as already flagged in the prior pass. Grade: this is a mechanical trial only
(no H/C grade applies to the trial's own "reading," since nothing here is claimed as a decipherment); the
205-216 "resolved(H)" counts above mean only "this code string appears in Tomokiyo's table," not that the
resulting plaintext is correct.

### Status and next step

**Status stays `open`.** This pass: (a) completed dense coverage of both cipher bands (53/54 canvases, one
unreachable); (b) confirmed the volume does hold a contemporary decipherment for at least one letter, on a
companion leaf (canvas 170/folio 87) rather than interlined — the strongest lead yet for actually keying this
cipher; (c) ran a first blind transcription (uncommitted to a canonical reading, two passes disagree too much
past line 12 of the f9 crop to reconcile without a third pass); (d) mechanically ruled out both published
same-office Brienne keys as direct hits, with a matched control, as expected. No decipherment recovered, no
novelty wording.

**Cheapest next step:** align the folio 86 cipher (canvas 168-169) token by token against the folio 87
decipherment transcript (canvas 170) already on disk (`images/native/f168.jpg`, `f169.jpg`, `f170.jpg`,
`images/crops/f168_body.jpg`, `f170_body.jpg`) — a known-plaintext crib sitting in the same dossier, not yet
used. That is very likely to recover fr.5160's own key directly at grade C, which no amount of trying published
same-office keys from a different correspondent will do. Second, cheaper option: a third pass (or higher-
resolution crops) on the f9 leaf of the folio 1-2 letter to resolve the line-count divergence before
committing a transcription.

### Requests this pass

gallica.bnf.fr: ~56 (1 reachability check on the cached manifest.json; 3 diagnostic fetches while
troubleshooting a slow-response timeout — two `curl` connection resets at the default timeout, resolved with
`--max-time 30`, logged as a container/load note rather than a site block; 46 census-thumbnail attempts
across the two bands, 40 target canvases with 6 needing one retry each, canvas 29 failing both attempts and
left unfetched; 6 native-resolution leaf fetches, all first-try). cryptiana.web.fc2.com: 2 (the two Brienne
key-table PNGs, not previously mirrored). No other host queried this pass (no archive.org, Google Books,
GitHub, WebSearch, or logins). Three Sonnet subagents for image reading/classification (the dense-band census
table) and two for the key-table transcriptions (image-only, no network); two further Sonnet subagents for
the blind passA/passB transcription (image-only, no network). Folder size 21MB, under the 30MB cap.

## Folio 86 cipher and folio 87 decipherment, passes (24 Sept 2026)

Following on the dense-band-walk flag above. All images already on disk (`images/native/f168.jpg`,
`f169.jpg`, `f170.jpg`); no fetches this pass (another worker held this session's Gallica lane slots).

### Correction: the decipherment heading's date is 21 November, not 21 September

The prior pass's gloss of "9.bre" as "septembre" was wrong. In ancien-régime French dating, the period
abbreviation follows the Latin ordinal from March = 1: 7bre = septembre, 8bre = octobre, **9bre = novembre**,
Xbre = décembre. Both of this pass's independent blind readers of the heading (below) read the abbreviation as
"9.bre" and neither read "7.bre" — pass A additionally checked the ascender shape of the abbreviation's "b"
against the same scribe's "b" in "publiez" later on the same page and confirmed it is a "b", not a "d" (which
would give a different, implausible reading). The heading reads **"Brienne du 21 9.bre 1659"** = 21 November
1659. The "Correction to the queue row" and "Census pass" sections above have been corrected in place.

### (1) Line crops

16 single-line crops of the folio 86 cipher block (`images/crops/f86_cipher_L01.jpg`..`L16.jpg`, L01-L07 from
canvas 168, L08-L16 from canvas 169, continuous across the two canvases) and 26 single-line crops of the folio
87 decipherment leaf (`f170_H01_heading1.jpg`, `H02_heading2.jpg`, `P1L01`..`P1L12`, `P2L01`..`P2L12`), all
<=2400px on the long side. Line bands were located by manual pixel-grid inspection (overlaying a coordinate
grid on a downscaled copy and reading off line boundaries by eye) — an automatic row-darkness-projection
segmentation was tried first and rejected: this cursive secretary hand has no clean zero-valley between text
lines (ascenders/descenders of adjacent lines overlap in the row-darkness profile), so it merged most lines
into single blobs. The manual bands include deliberate generous padding, so several crops show a thin sliver
of the neighbouring line at the very top or bottom edge by design.

**Known weak spot, flagged independently by both f86 cipher passes below:** the crop bands for lines L13-L16
(the tail of the block, canvas 169) sit over a region with visible bleed-through/ghosting (from the facing
page and page-turn shadow), and the calibration used for the earlier, more widely-spaced lines (L01-L12)
undershoots there — L15 and L16 in particular are narrower crops than the actual line height, cutting content.
This should be re-cropped with tighter, individually-checked bands before any committed reading of this
region; not fixed this pass (out of scope — recropping was not part of the brief, and a second bad crop
without redoing the passes would not have helped a blind comparison).

### (2) Two blind Sonnet passes, folio 86 cipher (`passA_f86.tsv`, `passB_f86.tsv`)

Two independent Sonnet subagents transcribed the 16 line crops blind (neither saw the other's output, any
existing key, or the folio 87 text). Token counts: pass A 251 tokens, pass B 263 tokens, over the same 16
lines. Both passes independently flag the same problems, unprompted: overlines are common on both single- and
double-digit groups (recorded as a leading underscore, e.g. `_18`); digit-count is genuinely ambiguous in a
couple of spots (a token read as "115" could be one 3-digit group or two, "11"+"5", at L05 and L10 in both
passes); and lines L13-L16 have visible bleed-through/ghosting making the line boundary itself uncertain (both
passes' confidence drops sharply there, and pass B separately flags a token at L08 pos 17 as possibly cut off
at the crop's right edge).

Ten to twelve of the sixteen lines carry a clear-French token mixed in among the numerals (mostly a lone "m"
or the title abbreviation "M."/"M.r"), plus two lines with short clear-French runs: L07 "mais aussy" and L09
"et c'est ce qui donne lieu de" (six consecutive clear words) — both passes agree closely on these clear-text
spans, cross-checking independently of any digit reading.

Agreement (`line`, `pos`, `group` compared, confidence/note ignored): of 16 lines, 11 have matching token
counts between the two passes; 5 do not (L09, L12, L13, L15, L16 — the L15/L16 mismatch is large, 6-7 tokens
in pass A vs 15 in pass B, consistent with the L13-L16 crop-boundary problem above rather than a real
disagreement about the cipher). **Token-level agreement on the 11 count-matched lines: 172/188 = 91.5%** —
markedly higher than fr2980-gramont's or fr5160's own folio-1-2-letter precedent (65.8%), consistent with this
being a plainer numeral-only hand versus the symbol+numeral hybrid transcribed in the prior pass. Restricting
to the 10 lines away from the flagged L13-16 region, count-matching and token agreement are both high; the
tail of the block (L13-16) is the only real weak spot and should not be relied on without a recrop.

### (3) Two blind passes, folio 87 decipherment (`dechiffre_f87_A.txt`, `dechiffre_f87_B.txt`)

Two independent Sonnet subagents transcribed the same 26 line crops as diplomatic French text, blind to each
other and to the cipher passes. Both independently read the heading date as "21 9.bre 1659" (see date
correction above). Word count of the body (excluding the 2 heading lines): 213 words, identical for both
passes.

Diff (`diff -y`, then a normalised comparison stripping apostrophes, accents and `[?]` markers): of 26 lines,
8 are character-for-character identical; 18 of 26 are identical once apostrophe-insertion and secretary-hand
u/v spelling variants are normalised away (pass A consistently does not insert elision apostrophes not
clearly drawn in the hand — "lauoir", "quil", "cest" — while pass B does — "l'avoir", "qu'il", "c'est" — a
transcription-convention difference each pass stated up front, not a reading disagreement). The genuine
content-level disagreements, not explained by that convention difference:

- Line 7 ("celle la, mais aussi j'ay peine de croire que M.**r**" (A) vs "M.**e**" (B)): the two passes
  disagree on which title abbreviation follows — Monsieur or Madame — immediately before "de la croire
  capable". Worth a third look at the crop.
- Line 26, the closing line: pass A reads "**quoy** y pense" (cross-checked, no `[?]`); pass B reads
  "**qu'on** y pense". These are different words ("what does he/she think of it" vs "that one thinks of it")
  — the single most important disagreement between the two passes, since it is the letter's last line.
- Line 3, the name after "M.r": pass A reads "Dambrun" (no flag); pass B reads "Dambruon[?]" (flagged
  uncertain) — likely the same name, pass B just less confident of the exact letters.
- Minor: line 9 "desirer"/"désirer" (accent only), line 12/24 comma placement — cosmetic, not a reading
  disagreement.

No word was marked fully illegible by either pass. Both passes independently noted that several crops show
two overlapping manuscript lines (the deliberate-overlap-by-design padding mentioned above) and that they
resolved which text belonged to the "target" line by requiring the reconstructed multi-line sequence to read
as continuous, grammatical French — a sound blind-transcription strategy, and the reason the two passes agree
so closely despite the crop overlap.

### (4) Does the decipherment plausibly belong to folio 86's own cipher?

Read folio 86's own clear French text in full (the "Monsieur..." opening on canvas 168 before the cipher
block, and the "je ne croy pas..." closing on canvas 169 after it, down to where the leaf ends mid-sentence,
"C'est d'une lettre de M[...]"). **Folio 86 itself carries no explicit date anywhere in either its opening or
its closing prose** — only a relative reference, "La lettre qu'il vous a pleu de m'escrire du 8.e de ce
mois...", which dates the letter *received*, not this one being *written*. This confirms rather than resolves
the prior pass's flag: the pairing still rests on context, not a matching date written on the page itself.

Content match: folio 86's opening prose discusses **M. d'Ambrun** advising **Madame de Sauoye** on securing
her power (garrisoning places, controlling troops) and whether he could be held "innocent" without the King's
order — and folio 87 paragraph 1 is *entirely* about whether **M. d'Ambrun** made damaging remarks about
someone "to Monsieur son fils" and whether it reflects "justice ou... hayne" on his part. Folio 86's closing
prose discusses **M. de Mantoue**'s claims and **M. de Sauoye** needing to defend Montferrat — while folio 87
paragraph 2 discusses **M. de Savoye** possibly arranging a marriage alliance for his sister at Parme. Both
leaves circle the same small cast (d'Ambrun, M./Mme de Savoye) and the same register of content: private,
speculative political commentary on named individuals' motives — exactly the kind of material a mid-17th-
century diplomat would encipher rather than write in clear, while the surrounding narrative frame (who wrote
to whom, what is publicly known) stays in plain French. This is consistent with folio 87 being the
decipherment *of* folio 86's cipher block, but it is a topical/thematic match, not a token-by-token one.

Length check: folio 86's cipher block is ~251-263 numeral tokens (the two passes' raw counts; the true count
is uncertain in the L13-16 region flagged above); folio 87's body is 213 words. A ratio of roughly 1.2 cipher
tokens per plaintext word is unremarkable for a nomenclator system mixing letter-, syllable- and word-codes
with occasional nulls — it neither confirms nor rules out the pairing on its own.

**Net: the pairing is plausible and, on content, fairly strongly suggested, but remains unconfirmed** — no
date match, and no token-by-token alignment attempted this pass (out of scope per brief). The cheapest next
step named in the dense-band-walk section above still stands: align folio 86's cipher against folio 87's
clear French token by token as a known-plaintext crib, ideally after a recrop of the L13-16 region.

Grades: everything in this section is a transcription pass (grade M throughout, model-read from crops, no
key applied, nothing decoded). No novelty wording (rule 10) — this section describes transcriptions and a
content-based pairing hypothesis, not a claimed decipherment.

### Requests this pass

No fetches (all six source images already on disk from the prior pass; this session's Gallica lane slots were
held by another worker). Four Sonnet subagents (two blind passes of the folio 86 cipher, two blind passes of
the folio 87 decipherment leaf, image-only, no network). Folder size unchanged from the prior pass's ~21MB
plus ~2.8MB of new line-crop JPEGs, still well under the 30MB cap.

## Folio 86-88: key from the f.87 decipherment (24 Sept 2026)

Opus reconciler+solver, LANE G. Files: `reconcile_f86.py` -> `ciphertext_f86.tsv`; `dechiffre_f87.txt`;
`align_f86.py` -> `align_f86.tsv`, `key_1659.tsv`; `pair_control.py`; `ciphertext_f88.tsv`; `holdout_f88.py` ->
`holdout_f88.tsv`; `decode_1659.py` -> `reading_f86.{txt,tsv}`, `reading_f88.{txt,tsv}` (`--check` exits 1 if stale).

### (1) Reconciliation

**f.86 cipher** (`ciphertext_f86.tsv`, 268 groups + 12 clear tokens (9 words, 3 "M.r"); conf H 139, M 129). L13-L16 recropped from
`images/native/f169.jpg` (the old bands sat one line low and cut the right end) and read by eye:
`crops/f86_cipher_L13-L16_recrop.jpg`. Both passes' L13-L16 were misaligned (pass A's L15/L16 were fragments, pass
B's L15/L16 were the true L15/L16 with its L13/L14 shifted). Other settlements by eye: L01 pos 5 is a single `7`
(passes 9/4); L02 pos 5 `19` (29); L04 pos 16 `56` (86/96); L03 pos 5 `33`. The hand has a curly, 3-shaped
digit distinct from its straight `7`; it is read as 3 throughout (`_3` in "pour" = `_3 7 21`, where both passes
read `_7`; `30` where passes read `70`; `36` for their `76`). This changes only group names, not which groups are
the same. L10 pos 15: the gutter crop shows overlined 1, a space, then 7 (`_1 7`, "pe u" in "peut"); passes read
`_17`/`_7`. Every line from L09 on runs into the gutter; a further group may be hidden at each line end (M).

**f.87 decipherment** (`dechiffre_f87.txt`, pass A's diplomatic spelling, no inserted apostrophes). Line 7 is
**M.r** (the superscript matches "termes M.r" on line 9, and f.86 L08 has a clear "M.r" before the name). Line
26 reads **"quoy y pense"** diplomatically: the fourth letter has a y-descender like the following "y" (sense
would want "qu'on"; the scribe's form is kept). Pass B's unflagged "bon", "essayassions", "quavoir" adopted.

### (2) Pairing: yes

- The clear words in the cipher sit where f.87 has them, in the same order: "M.r" before the name (twice),
  "M.r son fils", "mais aussy" (f.87 "mais aussi"), "et c'est ce qui donne lieu de" (f.87 "et cest ce qui donne
  à lieu de"). f.86's prose ends "...a Monsieur son filz" and f.87 begins "Soit pour le luy avoir esté ainsi dit".
- Repeats line up: `_3 7 21` three times where "pour" is three times; `m 31 7 8 _7 24 18 19` twice (L11, L16)
  where "à ceux qui ont" is twice.
- Length: 268 groups (between the clear words) for 412 letters of f.87 paragraph 1 (1.5 letters per group; the table has letters,
  digraphs and syllables).
- Matched control (`pair_control.py`): key consistency (share of group occurrences taking their group's modal
  value) after unseeded hard-EM: real 0.321, letter-shuffled plaintext 0.265-0.287 (5 seeds), f.87 paragraph 2
  cut to the same lengths 0.276. With seeds: real 0.795, shuffled 0.362, paragraph 2 0.388 (the seeds come from
  the real pairing, so this favours it and is only supporting).

**f.87 paragraph 2 deciphers f.88, not f.86.** f.88's cipher follows the clear "peut estre que M.r" and reads
"de Savoye allant accompagner M.e sa soeur jusques à Parme ...", which is f.87 paragraph 2. f.88's cipher
stops at "celle la"; the rest of paragraph 2 ("et il seroit bon ... qu'on/quoy y pense") presumably continues on
canvas 173 (not fetched, below). So f.87 covers two ciphered passages, f.86 and f.88. Whether f.86-88 is one
letter of 21 Nov 1659 (with f.87 inserted) or f.88 is a separate letter was not settled: the census read canvas
173's date as "27 [mois] 1659", unconfirmed without the image.

### (3) Key

`key_1659.tsv`: **65 groups**, every value grade C (known plaintext from the f.87 decipherment), with evidence =
occurrences aligned to the value / total occurrences, other values seen, and a `conflict` flag where the modal
value holds under 75% of occurrences (19 groups) or `minor conflict` (6). 20 values are single attestations.
Seeds for the EM were read by hand from the repeats above and are listed in `align_f86.py`; every value is
re-estimated. Examples: `m`=a (11/11), `20`=s (18/18), `19`=t (13/13), `21`=r (15/17), `15`=oi (11/15),
`61`=le (9/9), `36`=de, `35`=da, `_0`=pa, `115`=M.e/M.r, `_3`=p, `7`=ou/u. It is a mixed table: single letters,
many digraphs/syllables (pa, da, de, le, si, ca, fi, ju, ...), overlined figures as a separate series, the
lowercase `m` as "a". Known conflicts: `7` ou 8 / u 5; `18` on 7 / n 5; `9` y 2 of 9 (spread); `24` ui 2 of 6;
`71` e 4 of 7.

Held-out checks: (a) segment hold-outs within f.86 (`align_f86.py --holdout S2|S5|S4|S1`): 22/37, 8/16, 7/11,
16/25 groups take the same value as in the full alignment; misses are mostly homophone-level (u/ou, m/mb).
(b) **f.88 against f.87 paragraph 2, key from f.86 only** (`holdout_f88.py`): 153 groups, 145 keyed; the f.86
key value equals the aligned plaintext for **114/145**; control (paragraph 2 letters shuffled, 5 seeds):
28-35/145. Misses are again mostly sub-part mismatches (on vs n, el vs l, re vs e).

### (4) Readings and grades

`decode_1659.py` writes per-token readings. Grade C where the key value is attested and the group was read at
conf H, M where the group's reading is M or its key row is `conflict`, U unkeyed, P clear in the manuscript.

- **f.86**: C 81, M 187, U 0, P 12. It is the key's own training text, and its plaintext is the f.87
  decipherment itself (paragraph 1); the reading is a regeneration check, not new text.
- **f.88** (single reader, this worker, by eye from the native crop; 153 groups, 8 lines): C 67, M 78, U 8
  (`13`=gn, `3`, `65`=mar, `26`=be, `27`=bi, `_19`=su, `70`=na, `_10`, from the alignment only, not in the key),
  P 5. The reading runs "de sa v y e a el la on t a c c m pa ? e r M. / sa s e ou r ju s qu a pa r me p ou r r oi t
  pr ...", i.e. f.87 paragraph 2 from "de Savoye" to "celle la". This is the f.87 text read back through the
  key, not a new text.

Not found / not done: canvas 173 (rest of the f.88 cipher and its date) was not fetched; f.88's own alignment
could add the 8 unkeyed groups and more evidence to the key (suggestion: extend the key from f.88 + f.87 para 2
with f.86 held out, the reverse of check (b)). The folio 1-3 (1653) letters use a different, symbol+numeral
system and are untouched by this key. No novelty wording, no novelty class; that is for a verifier.

### Requests this pass

gallica.bnf.fr: 4 (canvas 172 native: 1 reset, 1 success on retry; canvas 173 native: 2 resets, stopped at the
one-retry limit and logged). No other host. No subagents.

## Joint key from f.86 + f.88 (24 Sept 2026)

Opus solver, LANE G, disk only (no network; canvas 173 still unfetched). Files: `passC_f88.tsv` (blind second
reader), `ciphertext_f88.tsv` (settled), `joint_key.py` -> `key_1659.tsv` (joint), `align_f88.tsv`,
`holdout_f86.tsv`; `key_1659_f86only.tsv` is the previous f.86-only key, now written by `align_f86.py` (which no
longer overwrites `key_1659.tsv`) and used by `holdout_f88.py`; `decode_1659.py` unchanged, `--check` exits 0.

### (1) Second reading of f.88

One Sonnet subagent read the cipher from `images/crops/f88_cipher_{top,bottom}.jpg` without access to any
transcription, key or note. Same segmentation on all 8 lines (153 groups each, plus [mais]); **141/153 groups
agree (92.2%)**. The 12 disagreements were settled by eye on zoomed crops (conf column; note says which reader):
- second reader adopted at 3: L02 pos 8 `_6` and L04 pos 12 `_16` (overline plain on zoom), L06 pos 10 `27`
  (straight 7, like L05 pos 12; first reader had 23, now M);
- first reader kept at 9: six `36`/`31`/`_13` where the second reader wrote 26/71/_17 for the descending
  3-shaped glyph (kept as 3 under the f.86 convention: 2 in this hand is z-shaped without a descender, 7 has a
  flat top), now M; L01 pos 20 `13` (no overline; the bar to its left belongs to `_0`).
Conf after settlement: H 125, M 28.

### (2) Joint key and the mirror hold-out

Same hard-EM/Viterbi as `align_f86.py`, same hand seeds, f.86 segments S1-S6 plus f.88 split at [mais] (T1 "de
Savoye ... beaucoup de bien", T2 "lalliance ... celle la"). `key_1659.tsv` now has **74 groups** (was 65), all
grade C, with `ev_f86`/`ev_f88` columns (modal value count / occurrences in each folio).
- **Values changed (4)**: `16` el -> l (4/13; f86 1/4, f88 3/9), `18` on -> n (11/25; f86 5/14, f88 6/11),
  `24` ui -> i (3/9; f86 1/6, f88 2/3), `71` e -> ne (4/11; f86 3/7, f88 1/4). All four are sub-part splits
  (on/n, el/l, ui/i, e/ne) of the kind the aligner cannot settle; all four stay `conflict`.
- **Conflicts resolved (3)**: `_16` se 3/4, `37` di 4/5, `62` i 3/4. **Newly conflict (6)**, each from one or two
  f.88 occurrences: `_13` r 6/9, `23` pr 4/6, `_28` v 3/5, `40` fa 2/3, `41` e 1/2, `64` lu 1/2. Conflicts 19 -> 23.
- **New groups (9)**, one f.88 attestation each: `3` e, `_6` ques, `_10` st, `13` gn, `_19` su, `26` be, `27` b
  (1/2), `65` ar, `70` a. Single attestations 20 -> 22.
- **Hold-out, mirror of check (b)**: key from f.88 only, f.86 aligned to f.87 paragraph 1 under it; control =
  paragraph 1 letters shuffled per segment, seeds 0-4 (`joint_key.py --holdout`, `holdout_f86.tsv`):
  - unseeded EM (no f.86 information): 50 groups, 227/268 f.86 occurrences keyed, **47/227** match vs control
    **32-40**. Weak: 153 groups are too few for the unseeded EM to converge on the table.
  - seeded EM (the 20 seeds were read by hand from f.86, so this leaks and is supporting only): **168/227** vs
    control 48-63; on the 77 occurrences of non-seed groups, **41/77** vs control 9-18.
  - Check (b) re-run on the settled transcription (`holdout_f88.py`, f.86-only key): 114/143 vs control 28-35.

### (3) Readings

- **f.86**: C 72, M 196, U 0, P 12 (was C 81, M 187): `18` is now a conflict group (on 5 / n 5 in f.86), so its
  C tokens drop to M.
- **f.88**: C 65, M 88, U 0, P 5 (was C 67, M 78, U 8): every group is now keyed. Reading, as regenerated: "de sa v
  y e a l la n t a c c m pa gn ne r M. sa s e ou r ju s ques a pa r me p ou r r oi t pr re n e re re s lu t i n
  ... de s pr i n ne s se s ... be a ou c ou pr de b e n [mais] la l i a n ne e s t si di s b r p r t i n ne e
  ... ce l le la". It is f.87 paragraph 2 read back through a key partly estimated from it; not new text.

Not done: canvas 173 (the rest of the f.88 cipher and its date); a hand-seeded f.88-only key (seeds from f.88's
own repeats) would give a cleaner mirror than the unseeded run. No novelty wording, no class; that is for a
verifier. Requests: none (no network). One Sonnet subagent.
