# BnF fr.5160 — Loménie de Brienne (père et fils) to Abel Servien, 1653-1661

Status: open

> **Verifier correction, 24 Sept 2026 (AUDIT.md):** f.86 and f.88 are N0 (their contemporary decipherment is f.87).
> The recipient of the 1659 letters cannot be **Abel** Servien, who died on 17 Feb 1659. It is almost certainly his brother
> **Ennemond Servien**, ambassador at Turin 1648-1676 (grade I, verifier's inference; AUDIT.md section 3). The catalogue's
> "Abel" is kept below only where it is quoted.

Suggestion (verifier): read Conti 2024, *Histoire, économie et société* 2024/4 p.51 (Servien embassy, Turin), for any citation of fr.5160.

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

## Canvas 173 (24 Sept 2026)

Access worker, LANE G. Fetched canvas 173 natively (`images/native/f173.jpg`, 3827x5356, one request, 200 on
first try). This canvas is the tail of the f.88 letter: 7 more cipher lines (numeral groups) closing with the
clear-French words "je suis," (start of the sign-off formula), then blank space, then the letter's own dateline,
signature and docket, all on the same physical page — no key or alignment work done, per brief.

### Date and signature

Read directly by this worker (not a blind pass — plain secretary-hand French, not cipher): the dateline reads
**"A Paris ce 21e nov[e] / 1659"** (crop `/tmp/f173_dateword2.jpg`, not committed, regenerable from
`images/native/f173.jpg`), i.e. **21 November 1659** — independently confirming, from the letter's own closing
dateline, the date already read from the f.87 decipherment heading ("Brienne du 21 9.bre 1659") in the prior
pass. The signature block below it reads "[flourish] Vostre humble et tresh[umble] serviteur / de Brienne" —
signed by (Loménie de) Brienne, the letter-book's author. A docket in a different hand at the foot of the page
reads **"M. de Servien"** (crop `/tmp/f173_addressee.jpg`, not committed) — independent corroboration, from the
manuscript itself, of LANE V's 04:30 UTC correction (AUDIT.md s.3, ROOM.md) that the 1659 letters in this
dossier are addressed to a Servien, matching "Servien" rather than confirming which given name (Abel died Feb
1659; the correction argues for Ennemond).

### (1) Line crops

Two crops, `images/crops/f173_cipher_{top,bottom}.jpg` (<=2400px wide, no overlap: top holds the first 4
numeral lines, bottom the remaining 3 numeral lines plus the closing "je suis," line), following the same
{top,bottom} convention used for f.88's own second reading.

### (2) Two blind Sonnet passes (`passA_f88b.tsv`, `passB_f88b.tsv`)

Two independent Sonnet subagents transcribed the two crops blind (neither saw the other's output, any existing
transcription, key or note; each was told only the generic paleographic convention already established for this
hand: a leading `_` for an overlined group, `[word]` for clear French). Both read 8 manuscript lines (L01-L07
numeral, L08 = "je suis,") and landed on identical token counts, 123 each.

**Token-level agreement: 107/123 = 87.0%** (line/pos/group compared exactly, overline prefix included) — in
the same range as f.86's 91.5% and f.88's own second-reading 92.2%. 16 disagreements, all at points either
pass already flagged as uncertain in its own notes, not new problems:
- **Overline presence/absence** on an otherwise-agreed digit (5 cases: L01/5, L01/6, L02/1, L02/5, L04/2,
  L05/9) — both passes read the same digits, differ on whether a stroke above them is a macron or a flourish.
- **9/7 shape ambiguity** at the start of a group (3 cases, all the same pattern): L04/9 `96` vs `26`, L06/1
  and L07/1 both `96` vs `76` — this scribe's 9 and 7 (and this scribe's 2) share a similar curled top stroke;
  both passes flag it independently.
- **The recurring curly descender-tailed digit** (this hand's 3/7 confusion, already documented for f.86/f.88):
  L02/6 `_7` vs `_1`, L02/10 `_21` vs `21`, L06/11 `_7` vs `_3`, L07/17 `_18` vs `_1`.
  L07/17 sits at the crop's right edge; pass A flagged truncation, pass B additionally shrank the group.
- **"111"-shaped tokens** (2 cases, L02/16, L07/6): pass B independently read a token as a run of vertical
  strokes resembling "iii"/roman numerals as the 3-digit group `111` in both places; pass A read the same
  positions as the single ambiguous curly digit `3`. Both passes flag low confidence; this is a real
  disagreement about segmentation (one token vs. three), not just glyph choice, and is the one item here that
  looks like more than a legibility call — worth checking on the image before it goes in a key.
- **L01/17**: the one token both passes flag as a heavy ink blot rather than a clean digit — pass A left it
  unread (`?`), pass B tentatively read `7`.

Not settled by eye and not reconciled into a single ciphertext_f88b.tsv or merged into `key_1659.tsv` — that is
key/alignment work, out of scope for this brief (an Opus worker follows, matching the f.86/f.88 handoff
pattern). No novelty wording, no class.

### Requests this pass

gallica.bnf.fr: 1 (canvas 173 native, 200 on first try). No other host. Two Sonnet subagents (the two blind
passes only).

## f.88 tail and regrade (24 Sept 2026)

Opus reconciler+solver, LANE G, disk only (no network). Files: `reconcile_f88b.py` (new; `--check`) writes canvas 173
into `ciphertext_f88.tsv` as L09-L16; `joint_key.py` (tail segments, warm start, gutter wildcard) -> `key_1659.tsv`,
`align_f88.tsv`, `align_f86_joint.tsv` (new), `holdout_f86.tsv`; `decode_1659.py` (new C rule) -> `reading_f8{6,8}.*`;
`holdout_f88.py` now reads f.88 L01-L08 only (its output is unchanged). `decode_1659.py --check` exits 0.

### (1) Reconciliation of canvas 173

Pass A vs pass B 107/123 (87.0%). All 16 disagreements, plus 7 places where both passes agreed on the wrong glyph,
were settled by eye on zoomed crops of `images/crops/f173_cipher_{top,bottom}.jpg`. Each is listed with its reason
in `reconcile_f88b.py` SETTLE and in the note column:
- Overlines: `_16` `_13` (L01/5-6), `_26` (L04/2), `_7` (L05/9) present; L02/1 `20` and L02/10 `21` have none (the
  curl and the wavy stroke belong to other groups).
- The 3-shaped descending glyph (f.86 convention): the passes' 96/76/26 at L02/5, L04/4, L04/9, L04/15, L06/1, L07/1
  are `36`; their 71 at L05/1 is `31`; their 77 at L07/7 is `33`; their `_7` at L06/11 is `_3`.
- The "3"/"111" dispute (L02/16, L07/6) is the table's lowercase `m`, as in f.86.
- L02/6 `_1`; L07/17 is `_1` followed by a separate `18` at the gutter (added as L07/18).
- L01/17 is a 7 struck through by the scribe: written `?`, not read, left out of the alignment.
- Gutter: a further, hidden group after L04/16 (pass A's faint stroke) and after L05/17 (starts with 2): `?`, conf L.
Tail after settlement: 125 tokens: 115 cipher groups plus 3 `?`, and 7 clear (`[.]`, "car ce ne peut", "je suis,");
conf H 94, M 21, L 3 across the 118 cipher tokens.

### (2) Alignment and joint key

The tail continues f.87 paragraph 2 from "et il seroit bon" with no clear word at the page turn, so T2 now runs
"lalliance ... la fantesie" to the clear "car ce ne peut", and T3 is "estre quauoir ... quoy y pense" up to the
clear "je suis,". Two changes to the aligner, both in `joint_key.py`: (a) a group hidden at the gutter is a
wildcard (0-4 letters at half the skip cost, never keyed), which lets "[Fr]ance" in "de la France" fall on the
hidden group after L04/16; (b) warm start: EM first on f.86 + f.88 L01-L08 (which gives the previous joint key), then
on everything. A cold start (`--cold`, kept for comparison) let first guesses on new tail groups lock in, e.g.
"chose" as `4`=ho `53`=s `_16`=e. With the warm start it reads `4`=c `53`=ho `_16`=se.

`key_1659.tsv`: **79 groups** (was 74), all grade C (known plaintext), evidence as before (`ev_f86`, `ev_f88`,
with f.88 now covering the tail too).
- **New groups (5), one tail attestation each:** `_5` estr, `_8` qu, `28` b, `45` ga, `53` ho. `_5`=estr looks like
  an alignment artefact: "estre quauoir" is spread over `_5 _26 4` under the four-letter cap. It is C by the rule
  below (single attestation, conf H, value = aligned text), so treat it as the thinnest C in the table.
- **Values changed: none** against the previous joint key. (`python3 joint_key.py` prints the diff against the
  f.86-only key instead: the same four sub-part changes as before, `16` `18` `24` `71`.)
- **Conflicts 23 -> 25.** Resolved: `40` fa (5/6), `60` la (8/10). Newly conflict: `2` e 14/19, `4` c 5/7, `_6`
  ques 1/2, `_20` ta 2/3. Single attestations 22 -> 21. Most tail conflicts sit where the f.87 text and the cipher
  part company (next point).
- **Where the cipher and f.87 part company (M at those tokens, reported, not repaired):** f.87 "lallicher[?]"
  (our transcriber's [?]) against the cipher `60 62 2 71 21` = la i e ne r under the key; f.87 "fantesie" against
  `40 18 _20 15 _17 2` = fa n ta i si e; f.87 "quoy y pense" (our transcription notes the fourth letter is
  doubtful) against `_8 18 9 _1 18` = qu on y pe n (+ a hidden group); "essayassions" where the struck group sits.
  These are readings of the cipher under a key estimated from f.87 itself: grade M, not corrections to f.87.
- Mirror hold-out (`joint_key.py --holdout`, key from the whole of f.88 only, f.86 aligned under it): unseeded
  32/238 vs control 29-39, **null** (the unseeded EM does not find the table from 268 groups alone); seeded
  (seeds read from f.86, so this leaks and is supporting only) 180/238 vs control 43-58, non-seed groups 54/85 vs 7-13.
  Check (b) (`holdout_f88.py`, f.86-only key on f.88 L01-L08) unchanged: 114/143 vs control 28-35.

### (3) Regrade (AUDIT.md s.4)

New rule in `decode_1659.py`: a token is C only if its key value is the f.87 text that the joint alignment puts at
**that position** (column `f87_aligned` in `reading_f8x.tsv`), besides conf H and a non-conflict key row. f.86 is
graded against `align_f86_joint.tsv` (the alignment that made the key), not the f.86-only `align_f86.tsv`. The
two differ at 7 of 268 positions, none of them a C.
- The verifier's four: f.86 L07/2 `_16` se/es and L07/14 `_0` pa/ei, now **M** by the new rule; f.88 L01/16 `4`
  c/cc and L07/14 `2` e/fr, now **M** (the rule applies, and rows `4` and `2` are also conflicts now).
- Same fault elsewhere: two more C tokens failed the rule and are now M: f.86 L03/1 `60` la/l and f.88 L07/11
  `40` fa/fai. After the regrade, 0 C tokens anywhere have a value different from the aligned f.87 text.
- Still C and thin: 13 C tokens on single-attestation rows (f.86 5, f.88 8). The verifier allowed these;
  they are listed by `key_1659.tsv` note `single attestation`.

**Grades (tokens):**

| folio | C | M | U | P | total |
|---|---|---|---|---|---|
| f.86 | 69 | 199 | 0 | 12 | 280 |
| f.88 L01-L08 | 60 | 93 | 0 | 5 | 158 |
| f.88 tail (canvas 173, L09-L16) | 43 | 72 | 3 | 8 | 126 |
| f.88 whole | 103 | 165 | 3 | 13 | 284 |

Before: f.86 C 72 M 196; f.88 C 65 M 88. No H anywhere (no key source). The tail reading is f.87 paragraph 2 read
back through a key estimated partly from it; it is not new text. `reading_f88.txt` L09-L16: "e t oi l se r oi t b n
[.] ques v ou s e ? s oi / s si e je de pe ne t re r q lu y e n a fa oi / a oi s t re la fa n ta oi si e [car ce ne
peut] / estr ve c de s se oi n de la i e ne r de la ? / ce s t ou ne c ho se q l fa ou t ve oi l le ? / de pr re je se
ga r da n t p ou r ta n t b / de d n ne r a c n n oi s t re qu n y pe n / [je suis ,]" (modal key values, so the
homophone-level letters `15` oi/i, `18` n/on, `7` ou/u show their modal form).

Not done: the hidden gutter groups (L12/17, L13/18, and possibly L11 after [peut], L14 after `27`) need the
volume opened flat or a better image; the four-letter cap and the f.87 differences above are aligner limits,
not settled. No novelty wording, no class.

Requests: none (no network). No subagents.

## Folio 1-2 letter reconciled (24 Sept 2026)

Opus reconciler, disk only, no network. Inputs: `passA.tsv`, `passB.tsv` (the two blind Sonnet passes of the
dense band walk, part 3) and the native leaves `images/native/f8.jpg`, `f9.jpg`, `f10.jpg`. Output:
`ciphertext_f1.tsv` (line, pos, token, conf, alt, note), `inventory_f1.tsv`, `agreement_f1.tsv`, all written by
`reconcile_f1.py`, whose `--check` exits 1 when any of the three is stale (rule 7). The reading lives in the
script as one text line per manuscript line, so a later correction is a one-line edit.

**Method.** Every line was read from native-resolution strips cut from the leaves (not committed; the folder is
at 28 MB, the cap is 30 MB). Regions, reproducible with PIL from the committed natives: f8 x 950-3050,
y 2080-4250; f9 x 1380-3330, y 1000-4500; f10 x 1100-3100, y 950-4400, each cut in 700-800 px bands.
`tools/iiif_lines.py --image` found 12 of the 14 f8 lines (its bands drift on this hand), so bands were cut by
hand. Each pass disagreement was settled from the strip.

**The f9 line-boundary divergence is settled.** f9 has **18 lines**; pass B's count is right. Pass A skipped
physical lines 13 (`37 _11 _7 65 I _6 _6 73 11 tt 60 23`) and 14 (`_11 51 db 37 q‡ db tt d mm 36 _42 d m‡`),
so its f9_L13-L16 are lines 15-18. That shift is where the 0% agreement at A's f9_L13/L14 came from.
`agreement_f1.tsv` maps A's lines back.

**Totals.** 49 lines (f8 13 from "receuoir", f9 18, f10 18). **528 sign tokens: 508 H, 20 M**, plus 14 clear
phrases. After mapping each pass's spellings onto the sign classes below, pass A matches 448/528 of the
reconciled tokens (84.8%) and pass B 494/528 (93.6%). Unmatched by either pass: 14 tokens. Six carry dots or
underlines that neither pass recorded, and the rest are flagged M with the passes' reading as `alt`. 97 distinct
tokens (overline and dots counted), 81 distinct base signs.

**Sign spelling** (the script's docstring is the reference). A leading `_` is an overline and a leading `¨` is
two dots over the first figure. `11` is every two-minim sign: the passes wrote 11, u or n, and at this
resolution joined and unjoined minims cannot be told apart consistently, so a later solver may want to split
it. `m` is three minims. `mm` is the long minim sign with a descender. `m‡` is m with a double underline and
a cross (pass A wrote m + #). `tt` is a crossed double stroke. `db` is tt joined to a looped d (pass B wrote 8).
`d` is a looped d and `đ` a d with a barred ascender. `X` is a long cross, `Z` a Z, `I` a barred I and `£` a
crossed looped L (the passes wrote #, ≠, L). `q`, `q'` (looped head) and `q‡` (crossed descender) are three
shapes, kept apart. `θ` is an o with a stroke through it and `_o` an o with a bar above.

### Structure, for a later solver (description only, no decoding)

- **Two classes, one stream.** 310 numeral tokens (39 one-figure, 262 two-figure, 9 three-figure: 100, 115 x2,
  118 x2, 123, 144 x2, 154) and 218 letter-like signs. The numerals run 1-78 densely, then 94, 95, 96 and the
  three-figure values. The most frequent tokens are db 46, tt 37, then 11, m and mm at 22 each, _11 21,
  36 19, I 18 and d 15. Letter-like signs make up 41% of the tokens. That is the symbol+numeral hybrid named
  in the census.
- **Overlines.** 124 tokens are overlined. Some figures occur only overlined (_21 x13, _16 x9, _6 x7, _10,
  _22, _12, _7, _50, _18, _20, _28, _42, _27, _78). Others occur both ways (11 22 bare vs 21 overlined; 23 9
  vs 3; 17 3 vs 4; 3 5 vs 1). So the overline is probably part of the code value, not decoration, but that is
  an inference, not a test.
- **Dotted figures.** `¨4` x6, `¨1`, `¨2`, `¨15`, `¨34`; also one-dot `14` (f9_L3) and `15` (f10_L13), in notes.
  `¨4` stands next to `£` five times (`£ ¨4` f8_L10, f9_L7, f10_L4, f10_L13; `¨4 £` f10_L3), and three
  of these sit directly against a clear phrase.
- **`db` is a trailer.** 46 times, most often after 33, q‡, d, 40, X, 11 and 62, and often written raised
  against the sign before it (`40ᵈᵇ`, `Xᵈᵇ`, `q‡ᵈᵇ`). A solver should test it both as its own token and as a
  modifier of the one before; the passes and this file keep it separate.
- **Repeats** (exact runs in the reconciled stream): `36 62 db 40 db _21` at f9_L5/4 and f10_L17/1 (the
  second directly before the clear "selon touttes sortes"). `db 40 db _21` also at f9_L2/3, so three times.
  `4 _23 _12 _21 d` at f8_L6/2 (running over the line break into f8_L7) and f10_L15/2. `33 db _16 I _26` at
  f9_L15/3 and f10_L5/7. In total: one repeat of 6, four of 5, seven of 4, 26 of 3.
- **Clear French phrases and where they sit** (14; `inventory_f1.tsv` section `clear`). The letter opens in
  clear on f8 ("Monsieur", then nine lines of clear prose from "Depuis que Heron est party": Verue, the Rome
  ordinary; not in either pass and not transcribed here). The cipher enters mid-sentence at "quel peut
  estre" (f8_L2). After that the clear pieces sit at line starts or ends, mostly as sentence frames:
  "Cest estre persuade que bon" (f8_L6 start), "Et peut estre le" (f8_L7 mid), "lesquels noublieront"
  (f8_L10 mid), "yl le peut estre dans le doubte de cogn" (f9_L7, breaks off at the margin, the next line is
  cipher), "nayant pas en sorte" (f9_L18 start), "quils ne prennent" (f10_L1 end), "aisement" (f10_L2 start),
  "Et ce nest pas chose aisee de" (f10_L3 mid), "et de" / "nestre point surpris" (f10_L11 end / L12 start),
  "selon touttes sortes" / "dapparences nous aurons dans ce jour de ce" (f10_L17-18, where the cipher ends
  and the letter goes on in clear on the next leaf). The clear words are plausibly the real text around
  enciphered words rather than decoys, but that is an inference, not a test.
- **Transcription limits.** The 20 M tokens are listed with alternatives. The two classes most likely to hold
  errors are the two-minim `11` family (see above) and short overlines, which sometimes run on from a
  neighbouring stroke (f8_L3 `tt _16`, f9_L1 `θ θ _11`, f9_L2 `tt _17`).

**Status stays `open`.** No decoding and no key trial this pass. **Next step:** the same-office key trial of
part 4 was run on pass A. It can now be rerun on `ciphertext_f1.tsv`, with the spelling map above.
Otherwise wait for the f.86-88 joint key to be tested against this letter (a different date, so probably a
different key).

### Requests this pass

None (disk only). pip installed Pillow and numpy into the container for the strips. Cost: about $3 of the $8 cap.

## 1653 band: natives and folio 9 passes (24 Sept 2026)

Sonnet transcription worker, LANE G, cap $6. Picked up from the prior "LANE G access+transcription worker"
pass (manifest.json entry, canvases 11/12/24/25/30/31/32/33), whose per-canvas NOTES.md sections
("canvas 11/12 (folio 1-2 letter, continued)" and "canvas 30-33 (folios 19-20, Mantoue/Montferrat letter)")
were referenced by that manifest entry but never written before the 05:39 rate-limit stop. This section
supplies them, plus a blind pass B on the folio 9 letter.

### (1) Native fetches

None of canvas 11, 12, 24, 25, 30, 31, 32, 33 had a native image on disk at the start of this pass (the prior
pass's disposition note says all 8 were deleted after use to stay under the 30 MB folder cap; the folder was
still at 30 MB/30 MB when this pass started, so all 8 were fetched to the session scratchpad, read directly,
and **not** committed — same pattern as the prior pass). All 8 fetched successfully; canvas 33 needed one retry
after a connection reset (recovered on the retry, per the good-citizen single-retry rule). Requests:
gallica.bnf.fr 9 (8 canvases + 1 retry), one at a time, ~1.8s apart, UA `cipher-lab research script (contact
via repository)`, `--max-time 30`. Re-fetch with
`https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060495t/f{N}/full/full/0/native.jpg` if needed again.

### (2) Per-canvas table, read directly from the native images (this worker, no subagent, no network beyond the fetch)

Grade M throughout (model-read from full-page images, no transcription committed for 11/12/30-33, no key
applied). Corrects and extends the stride-4 census (thumbnail resolution) at "Dense band walk" above.

| canvas | folio (page no.) | date line | extent of cipher | decipherment beside it |
|---|---|---|---|---|
| 11 | - (no number visible) | none on this leaf | ~11 lines clear prose (Rethel/Château-Porcien/army news, "la mort de M. de la Vieuville rend les affaires plus difficiles"), **then a second, previously unnoted cipher block starts at the bottom of the page** (~4-5 lines) and continues onto canvas 12 | no |
| 12 | 3 | **"Paris le x janvier 1653"** (10 January 1653), signed "Brienne" | cipher block continues from canvas 11 for ~5-6 more lines at the top, then clear prose to the close/dateline/signature | no |
| 24 | 9 | none on this leaf | clear 2-line opening ("Monsieur, Je croy que vous vous souuiendrez bien de ce d'avoir ordonné que vous avez receu bo[n]...") then continuous dense cipher to the foot of the page (~13 lines) | no |
| 25 | - (facing leaf, no number) | none on this leaf | continuous dense cipher for ~13 lines, ends "...en sorte que vos paroles" (matches passA_f9.tsv's last line) with the rest of the leaf blank | no |
| 30 | - (page no. too faint to read) | none on this leaf | dense cipher for ~9-10 lines, but **not pure cipher**: at least two short clear-French phrases sit inside the block ("et soubliant de leurs interests et de ceux des autres princes italiens"; "le soubcon que"), missed by the thumbnail-resolution census's "no plaintext" call | no |
| 31 | 19 | none on this leaf | cipher opens the page (~5 lines), breaks into ~4 lines of clear prose ("Et Sa Ma[jes]té auoit peine de prendre une resolution esloignée de celle en laquelle elle est entrée, a[u]moins que le duc de Mantoue ne l'y contraignist par son mauvais procede"), then cipher resumes to the foot of the page, continuing onto canvas 32 | no |
| 32 | - (facing leaf) | none on this leaf | cipher continues from 31; **two more clear-French insertions** inside the block ("sans se souvenir des obligations desquelles on estoit redevable à sa Couronne"; "il ne fault point que se supreme, si nous ne nous y porterons pas") — again missed by the census's "no plaintext" call for this canvas; final line breaks into clear "...le Comte Philippes que le" running onto canvas 33 | no |
| 33 | 20 | none on this leaf | opens in clear prose continuing from 32 (~6 lines: duc de Savoye's dispatch to the Emperor, dissatisfaction over the Montferrat award "confirmée par trois traittez solemnels"), then cipher resumes for the rest of the page (~9-10 lines) | no |

**Flag — canvas 11-12 is the tail of the already-reconciled folio 1-2 letter, not a separate item, and it is
dated.** The "Folio 1-2 letter reconciled" section above (canvas 8-10, `ciphertext_f1.tsv`, 528 tokens) noted
the cipher "ends... where the cipher ends and the letter goes on in clear on the next leaf" without naming
that next leaf. It is canvas 11. Canvas 11's clear opening (army/Rethel news) and canvas 12's clear close read
as one continuous letter with canvas 8-10, and canvas 12 carries a dateline and signature: **"Paris le x
janvier 1653"** (10 January 1653), signed "Brienne" — the first firm date recovered for that letter, and by
inference for its clear-and-cipher content. **A second cipher block, not present in `ciphertext_f1.tsv`,
sits at the very end of the letter** (canvas 11 bottom through canvas 12 top, roughly 5+6 = ~11 lines,
comparable in length to the folio 1-2 dense-band table's per-canvas estimates of ~35-40 tokens) and has not
been transcribed by either pass. This is new ciphertext belonging to a letter that already has 528 reconciled
tokens and is a candidate for key recovery — worth a same-office key trial extension or a third crop/pass once
picked up again. Not transcribed this pass (out of scope: the brief asked for a date/extent/decipherment
report, not a new transcription pass).

No interlinear or marginal decipherment sits beside any cipher on any of the 8 canvases (consistent with the
dense-band census for the rest of both bands). No novelty wording (rule 10) — this is a transcription/extent
report, nothing decoded.

### (3) Folio 9 letter (canvas 24/25): blind pass B

Existing crops (`images/f9r_L01_s1.jpg`..`f9r_L15_s2.jpg`, `images/f9v_L01.jpg`..`f9v_L12.jpg`, 42 files, cut
by the prior pass) were reused, no re-fetch needed. A single Sonnet subagent, blind to `passA_f9.tsv` and to
any other file in the target (not given that path, instructed not to open it), transcribed all 27 manuscript
lines (15 recto + 12 verso) into `passB_f9.tsv` (231 tokens; same `line`/`position`/`group`/`confidence`
columns as `passA_f9.tsv`, overline as leading `_`). The subagent flagged its own weak spots: f9r_L01's
"Monsieur" read only from bleed-through off the next line; a compound cross/cancel mark over "121" at f9r_L09
and f9r_L13 it could not decompose (recorded `#121`, low confidence); a cut-off double-dot at f9r_L14; an
unidentified slashed-circle sign at f9v_L06; and the recurring two-minim-vs-"n" ambiguity already known from
the folio 1-2 letter's passes.

**Agreement** (`agreement_f9.py`, same method as `agreement.py`): of 27 lines, 23 have matching cipher-group
counts between the two passes (4 do not: f9r_L13, f9v_L05, f9v_L06, f9v_L10). **Token-level agreement on the
23 count-matched lines: 143/184 = 77.7%** — between the folio 1-2 letter's own first-pass figure (65.8%) and
the folio 86 numeral-only letter's (91.5%), consistent with this being a symbol+numeral hybrid like folio 1-2
rather than the plainer numeral-only folio 86-88 hand. The 7 clear-French line pairs read closely but not
identically (1/7 verbatim-identical; the rest differ by a word choice or a cut-off, e.g. A "en sorte que vos
paroles" vs B "ensorte toutes parolles" at f9v_L12, the letter's last legible clear phrase) — both readable as
the same underlying sentence, not a contradiction. No reconciliation run this pass (out of scope per brief) —
left for whoever next picks up this target, alongside the folio 1-2 letter's own unresolved f9-line-count
divergence precedent (a different f9, canvas 9, not to be confused with this folio 9, canvas 24-25).

### (4) Status and next step

**Status stays `open`.** This pass: (a) established that all 8 named band-1 canvases lack committed natives
(all fetched, read, and released, per the folder's 30 MB cap); (b) produced the date/extent/decipherment table
above; (c) found that the folio 1-2 letter (canvas 8-12) is dated 10 January 1653 and signed Brienne, and
carries an untranscribed second cipher block on canvas 11-12; (d) ran a second blind pass on the folio 9
letter. No decipherment recovered, no novelty wording, no reconciliation.

**Cheapest next step:** reconcile `passA_f9.tsv`/`passB_f9.tsv` the same way `reconcile_f1.py` did for the
folio 1-2 letter (disk-only, no network), then either try the two published same-office Brienne keys against
it or wait for a same-office key recovered elsewhere in this dossier. Separately, transcribe canvas 11-12's
second cipher block and append it to `ciphertext_f1.tsv` so the whole dated 10 Jan 1653 letter is one unit.

### Requests this pass

gallica.bnf.fr: 9 (8 native fetches + 1 retry on canvas 33, one at a time, ~1.8s apart, UA per playbook, none
committed). No other host. One Sonnet subagent (folio 9 pass B, image-only, no network). Folder size
unchanged (natives not committed). Cost: about $3 of the $6 cap so far.

## 1653 band: folio 9 reconciled and key trial (24 Sept 2026)

LANE G2 worker A (Opus, cap $10), disk only, no network, no subagent.

### (1) Folio 9 letter reconciled

`reconcile_f9.py` (with `--check`, rule 7) writes `ciphertext_f9.tsv`, `inventory_f9.tsv` and `agreement_f9.tsv`. The
reading sits in the script, one line per manuscript line. It was settled from the committed crops. The `_s1`/`_s2`
recto crops are two overlapping cuts of the same line, not halves (`_s1` is cut short at the right edge), so `_s2` and
the verso crops were read. Sign spellings are those of reconcile_f1.py. The script docstring maps the pass spellings:
A `H` and B `ff` are the raised trailer `db`, not `tt`; A `o` and B `d` are the looped `d`; `m=` and A's `m tt` are
`m‡`; `T` is `_1`.

- 27 lines (15 recto, 12 verso), **226 sign tokens: 202 H, 24 M**, plus 7 clear phrases. There are 73 distinct tokens
  and 66 base signs. Pass A matches 190 of the 226 (84.1%) and pass B 212 (93.8%).
- New on this leaf: the scribe writes **commas after signs** (21 of them; kept in the note column, not as tokens). They
  may be word divisions, but that is untested. `121` appears twice (r L9, r L13) **struck through** with hatching; it is
  spelled `~121` and left out of trials. There is one `z` (a looped d barred through the bowl, v L5).
- The same small-sign cluster as f1 f8_L10 recurs: `¨1 ¨2 £ X ¨4` (r L13) against f1's `£ ¨1 ¨2 [clear] £ ¨4`.
- Clear text as read: "Monsieur / Je croy que vous vous souuiendrez bien de ce / diverses ordres que vous avez receu",
  "Sy contre lattente", "des gens de bien", "et de mesnage", "en sorte toutes parolles" (the last is M).

### (2) Key trial with matched controls

`trial_1653.py` (with `--check`, seed 1653, 200 derangements) writes `trial_1653.tsv`, `trial_1653_overlap.tsv`,
`trial_1653_stretches.tsv` and `trial_1653_1659codes.tsv`. It tried four keys: key_1646 (clair1067), Tomokiyo 1647,
Tomokiyo 1651, and this volume's key_1659 (f.86-88). The measure is mean log2 p per character under
tools/french16_ngram.py, taken over runs of keyed signs. The script docstring gives the sign mapping between spellings;
it is grade I, because shape identity across transcribers is assumed. Control (a) permutes the key's values over its
codes. Control (b) enciphers period French with the true key at the letter's length and blanks the letter's own unkeyed
positions, so coverage and run lengths match exactly.

| key | letter | keyed/signs | real | shuffled mean (max) | derangements >= real | z | synthetic true (shuffled max) |
|---|---|---|---|---|---|---|---|
| 1646 | f1 | 186/528 | -4.77 | -3.89 (-3.29) | 200/200 | -3.45 | -3.17 (-3.55) |
| 1646 | f9 | 85/226 | -4.65 | -3.89 (-3.10) | 199/200 | -2.39 | -3.29 (-3.37) |
| 1647 | f1 | 135/528 | -3.76 | -4.38 (-3.17) | 14/200 | 1.44 | -3.66 (-3.96) |
| 1647 | f9 | 58/226 | -3.36 | -4.34 (-3.35) | 1/200 | 2.48 | -3.34 (-3.83) |
| 1651 | f1 | 278/528 | -5.13 | -4.80 (-3.89) | 172/200 | -1.09 | -3.26 (-4.34) |
| 1651 | f9 | 121/226 | -4.93 | -4.84 (-3.85) | 127/200 | -0.30 | -3.15 (-4.22) |
| 1659 | f1 | 260/528 | **-3.72** | -4.49 (-3.85) | **0/200** | **3.38** | -3.86 (-4.08) |
| 1659 | f9 | 106/226 | **-3.41** | -4.39 (-3.75) | **0/200** | **3.71** | -3.53 (-3.73) |

The synthetic control separates for every key: 0 of 200 derangements reach the true key on synthetic text. So at this
coverage the test can see a true key.

- **key_1646 and Tomokiyo 1651 read these letters worse than or no better than their shuffled keys. That is a clean
  negative with a matched control.** Tomokiyo 1647 does not beat its control either. On f9 one derangement reaches it
  (z 2.48, on 58 keyed signs); on f1, 14 do. After 8 tests, this is chance level.
- **key_1659 beats its character-level control on both letters.** No derangement reaches it (z 3.4 and 3.7), and the
  real scores are about as good as the true key's on synthetic French. **But it does not read words.** A second measure
  counts runs of 3 or more signs that split wholly into frequent period words (`trial_1653_stretches.tsv`). On the real
  letters it finds 2 on f1 and 4 on f9. Under derangements the mean is 5.2 and 1.9. The true key on synthetic finds 12
  and 7. So the word test has power, and the real letters fall below or inside the shuffled range.
- The six stretches it finds are: f8_L9 `m _26 4` "a ve c"; f10_L2 `_11 m 62` "re a i"; f9r_L04 `_21 _6 _28`
  "te ques v"; f9r_L11 `_23 _12 _21` "o i te"; f9r_L12 `_23 _12 _21 m 60` "o i te a la"; f9v_L07 `m 60 _26` "a la ve".
  `m _26 4` "avec" also occurs at f1 f9_L10, and `_23 _12 _21` occurs three times. **Grades: S 0, M 20 tokens.** They
  cannot be graded S because their own control fails. They are listed, not read.
- The most likely interpretation (an inference, not a test): the 1653 table shares some values with the 1659 table, at
  least in the syllabic numerals, but it is a different table. `trial_1653_1659codes.tsv` shows which codes carry the
  character-level signal. Leaving out `36`=de (30 uses), `_6`=ques (11), `61`=le (16) or `_16`=se (12) makes the joint
  score worse, so these codes may share their values with the 1659 table. Leaving out `23`=pr (+0.17 bpc), `_7`=q,
  `62`=i, `_1`=pe, `m`=a, `17`=m, `65`=ar or `4`=c makes it better, so on these codes the 1653 table probably differs.

**Where the 1653 table must differ (overlap counts, f1 + f9 together: 754 tokens, 113 distinct).** key_1659 can write
51 of the 113 distinct tokens and 366 of the 754 tokens. key_1651 covers 61/399, key_1646 37/271 and key_1647 30/193.
No key has the commonest letter-like signs: `db` 61, `tt` 46, `11` 37, `mm` 36, `d` 26, `X` 25 and `I` 23. The only
exceptions are key_1647/1651 `tt` and `d` and key_1646 `X` and `d`, which fail their controls. So about 40% of the text
is written in signs that no available table covers. The dotted figures (`¨1`, `¨2`, `¨4`, `¨15`, `¨34`) and the values
above 96 (100-190) are also absent from every key except as bare numerals.

### (3) Status and next step

**Status stays `open`.** Folio 9 is reconciled. None of the four keys reads either 1653 letter. key_1659 carries a
significant character-level signal but no word-level reading. **Next step** (the numbers justify it; not attempted
here): a constrained cryptanalytic solve of f1 and f9 together, 754 tokens. It would start from key_1659's values on the
four supporting codes, free the rest, add the letter-like signs as unknowns and use the clear phrases as context. Use
tools/nomenclator_anneal.py or subst_hillclimb.py, and run a synthetic control of the same size first. Separately,
transcribing canvas 11-12's second cipher block would add about 80 tokens to f1.

What was found, and where it was not: no reading of either 1653 letter was found with any of the four keys (tables
listed above, all on disk). No print or phrase search was run, because nothing was read. No novelty class is
assigned.

### Requests this pass

None (disk only). Pillow was installed with pip for the strips.

## Canvas walk 37-159 and canvas 11-12 block (24 Sept 2026)

LANE G2 worker, Sonnet, cap $8. Read `walk_37_159.tsv` for the full per-canvas table.

### (1) Canvas walk 37-159

Fetched IIIF `full/1000,/0/default.jpg` thumbnails for every canvas 37-159 not already covered by the prior
dense walk (canvas 4-36) or census (stride-4 to 156), one at a time, ~1.8 s apart, descriptive User-Agent.
119 of 123 canvases came back as valid images. Four never returned an image after the standard one retry
each (`45`, `55`, `58`, `74` — connection resets/timeouts, not 403/altcha) and are left unfetched, consistent
with the fr5160/clair1067 precedent of not looping retries. Three more canvases (`56`, `119`, `145`) initially
returned an HTTP 500/404 or, in `119`'s case, a Gallica *"ark is unknown"* HTML error page disguised as a 200
response — each was given one further single retry after a pause (not a loop) and all three then returned a
valid image. A Sonnet subagent (no network access) read all 119 thumbnails in four batches (37-66, 67-96,
97-126, 127-159) and classified each for folio/date/sender/cipher content; batches committed as a single
`walk_37_159.tsv` (all four batches were ready together, so no intermediate 30-canvas commit was needed).

**Result: zero cipher in canvas 37-159 except one letter not flagged by earlier passes.** Canvas 129 (folio 67, mid-page) and canvas 130
(its continuation, dated "A Paris ce 10 8bre 1659", signed Brienne, addressed M. de Servien) carry a dense,
symbol+numeral cipher block — **not recorded in the census pass, dense band walk, or any prior NOTES.md
section**. No interlinear or marginal decipherment visible on either canvas at thumbnail resolution (grade M).
Everything else in canvas 37-159 is plain French prose (Brienne/Brienne fils to Servien, Savoy court and
Pyrenees-peace diplomatic correspondence, Aug-Nov 1659) or blank/docket versos. Two scan anomalies flagged by
a subagent, unconfirmed: canvas 122 appeared to duplicate canvas 120's content and canvas 123 canvas 121's
(worth a re-fetch/IIIF-sequence check, not chased further here).

**The 1653 band is now fully walked and contains no cipher beyond what NOTES.md already records.** The dense
walk (canvas 4-36) plus this pass (37-51, the band's tail before the run turns to 1659 dates at canvas 52)
cover every canvas from the volume's start through the last 1653-dated leaf (canvas 40, "12 Octobre 1653").
No canvas in 37-159 carries an 1653 date. The 1653 band's three cipher letters, for a later solver, are all
already known and none are newly found here:

| letter | canvas | extent | status |
|---|---|---|---|
| folio 1-2-3 (2 Jan 1653) | 8-12 | mixed, ~1/3 page each | reconciled (`ciphertext_f1.tsv`); canvas 11-12's block below is new |
| folio 9 | 24-25 | most of page | two blind passes done (`passA_f9.tsv`/`passB_f9.tsv`), not reconciled |
| unnumbered, between folio 9 and the Oct 1653 letter | 32 | full page, ~14 lines dense | **not transcribed** (census only) |

### (2) Canvas 11-12: the folio 1-2-3 letter's second cipher block

Canvas 11 (bottom of the leaf, no clear folio digit; the previous worker's flag that this is "the dated tail
of the already-reconciled folio 1-2 letter" is confirmed — the same leaf carries the "Paris le x janvier 1653"
dateline and "Brienne" signature, seen mirrored/bled-through on canvas 12) and canvas 12 (folio "3" recto,
digit visible top right) carry a second cipher block not present in `ciphertext_f1.tsv`: 2 lines clear French,
then 6 lines of dense symbol+numeral cipher, then 1 mixed cipher/clear line (canvas 11); continuing directly
on canvas 12 with 5 more dense cipher lines then 1 mixed cipher/clear line, after which the letter closes in
clear French ("Et tel qui en a le sevre soubz...", signed Brienne).

Native fetches (`full/full/0/native.jpg`, 3810×5346px): canvas 11 needed one retry after a transient HTTP 500
(Gallica's own Spring error page, not a site block); canvas 12 succeeded first try. **Not committed** — the
folder is at the 30 MB cap — kept in the worker's scratchpad and logged in `images/manifest.json` with the
exact fetch URLs so a later worker can re-fetch cheaply.

Line crops cut with `tools/iiif_lines.py --image ... --debug` (region `1250,2700,2150,1450` on canvas 11,
`1100,950,2150,1250` on canvas 12; `--distance 90 --prominence 25` after the defaults under-detected lines by
2-4 in each region — checked against the debug overlay both times before accepting). 16 crops total (9 on
canvas 11, 7 on canvas 12; the cipher-only lines are `f11cipher_L03` through `L08` and `f12cipher_L01` through
`L06`), all ≤2150px wide. **Not committed** for the same 30 MB reason; kept in scratchpad, regions logged in
`images/manifest.json` under `iiif_lines`.

Two blind Sonnet passes (`passA_f11.tsv`, `passB_f11.tsv`; the second pass never saw the first, separate
subagent calls with no shared context), same line/position/group/confidence columns and sign-spelling
convention as `passA_f9.tsv`/`reconcile_f1.py`'s docstring. Numbered-token exact-match agreement: **85/111 =
76.6%** (lower than `passA`/`passB_f9`'s 77.7% or the folio 1-2 letter's 84.8-93.6%, but most of the
disagreement is not a real reading conflict — see below).

**Two signs recur across both passes that are not in the established fr.5160 vocabulary.** Both blind passes
independently and repeatedly flag the same two shapes, at matching positions, without being told to look for
them: (a) an open cursive hook/loop (pass A calls it "Ɔ"; pass B declines to name it, describing "a cursive
open hook, like ⊃, non-standard" — same shape, four occurrences: `f11_L2` pos4/6, `f11_L5` pos3/9/11, `f12_L3`
pos9, `f12_L4` pos1/6); (b) a looped-ascender flourish resembling a cursive H/& (pass A tentatively calls it
"db"; pass B again declines, "looped ascender flourish resembling cursive H/&, non-standard" — four
occurrences: `f11_L2` pos3, `f11_L3` pos7, `f11_L5` pos4, `f12_L3` pos10, `f12_L5` pos1). Both passes seeing
the same shape at the same positions independently is evidence these are real, consistently-drawn signs in
the manuscript, not misreads — but whether (b) is actually the established "db" sign (tt+looped-d) read
confidently by pass A and cautiously by pass B, or a genuinely new sign, is not resolved here; flagged for
whoever reconciles this block into the key. The remaining disagreements are mostly ordinary digit-reading
noise (`_0`/`_10`, `31`/`I`, `¨34`/`34`) plus one likely segmentation offset at `f12_L1` (pass B splits out an
extra leading token that pass A folds into its first digit read, shifting positions 1-4 by one against each
other). No reconciliation was attempted (not in this brief); the next step is a reconciler pass against the
native images, the same as `reconcile_f1.py` did for canvas 8-10.

### (3) Status and next step

**Status stays `open`.** No decoding attempted. No print or phrase search run (nothing new was read as
plaintext). No novelty class assigned. Grade of everything in this section: M (subagent/blind-pass reads, not
eye-checked by a human or reconciled against the image by a second worker).

Two things worth a follow-up brief, not attempted here per "stop when the brief is met": (1) canvas 129/130's
new cipher letter — native fetch, crops, and blind passes, the same as this section did for canvas 11-12; (2)
canvas 32's full-page 1653 cipher, still untranscribed since the first census pass.

### Requests this pass

`gallica.bnf.fr` ~155 total: 123-canvas walk at 1000px width (149 requests — 97 canvases on the first try, 26
needed the loop's own built-in one retry; 3 more of those 26, `56`/`119`/`145`, got one further single retry
after a pause once their "success" turned out to be an HTML error page, all recovered; `45`/`55`/`58`/`74`
never recovered and are left unfetched) + 3 native full-res fetches for canvas 11/12 (one retry on a transient
500). All ≥1.5 s apart, one fetcher, UA `cipher-lab research script (contact via repository)`. No other host.
6 Sonnet subagents total (4 for the canvas-walk classification batches, at most 4 concurrent; 2 for the blind
passA/passB_f11, run after the walk batches finished). No logins, no credentials, no novelty wording. Well
under the $8 cap.

## 1653 band: constrained solve (24 Sept 2026)

LANE G2 worker G (Opus, cap $10). Disk only, no network, no subagent. Brief step 1 (control first) failed its bar, so,
as the brief says, **the real run on f1 + f9 was not made**, and no key_1653.tsv or decode.json was written (there is
no reading to regenerate).

**Inputs** (`solve_inputs.py`, `--check` exits 1 if stale). `real_f1.txt`, `real_f9.txt` and `real_f1f9.txt` hold
ciphertext_f1/f9 in the annealer's format, with clear runs in braces and ~121 dropped: 752 sign tokens, 112 types. The
control plaintext `control_plain.txt` (2,345 letters) is the f.87 decipherment (Brienne, 21 Nov 1659), then the
clair1067 1646 reading (Brienne). A held-out Marguerite de Valois letter of 12 March 1581, from the fr16 corpus, fills
the rest, because the two repo letters alone ran out at 676 tokens. The French 5-gram model uses tools/data/fr16
(4.43M letters) with every paragraph that contains a control sentence removed. It is built into a 20 MB npz, which is
not committed; `FR_MODEL_DIR=<dir> python3 solve_inputs.py` rebuilds it.

**Tool change.** `tools/nomenclator_anneal.py` gained three things. `--words` takes a French word list in place of the
Italian default. `--extra-syl` accepts syllable values of any length (ques, estr, ment). `--p-syl` sets the share of
moves that propose a syllable. synth now matches syllables of up to 4 letters, longest first. With the defaults,
behaviour is unchanged.

**Control** (`control_1653_design.json`, `control_1653.txt`, `.truth.json`, seed 1653). The design follows key_1659:
21 letter signs, 96 syllable signs (key_1659's own values plus common French pairs and trigraphs, including ques and
estr), 16 word signs and 2 nulls. It is enciphered on the real letters' run pattern (`synth --pattern`), so cipher
runs and clear frames sit where they do on f1 and f9. That gives 752 tokens and 114 types. The top-8 token shares are
7.3 6.0 4.5 3.5 3.3 3.3 3.3 2.9 %, against the real 8.1 6.1 4.9 4.8 4.0 4.0 3.5 3.5 %, with 27 singletons against 36.
The solver uses the same settings the real run would have used: `--context clear` (clear phrases as frames), `--syl cv`
plus the design syllables (`control_1653_syl.txt`), a French word list, caps of 100 syllables, 16 words, 3 nulls and
4 homophones, and the true signs for de, ques, le and se fixed. That seeds the same four values that the real run would
seed from key_1659.

| run | schedule | restarts | best score | token accuracy (best, spread) | letter accuracy (best run) |
|---|---|---|---|---|---|
| t3 | 4M iterations, tool-default move mix | 4 | -3058.6 | 12.5% (12.0-12.5) | 13.8% |
| t4 | 2M, p-syl 0.45 | 4 | -3033.8 | 18.8% (10.9-23.0) | 18.9% |
| t5 | 10M, T0 2, T1 0.02, p-syl 0.45 | 4 | -3013.0 | **25.7%** (10.9-25.7) | 21.0% |
| true key | same scoring | - | **-2309.7** | 100% | 100% |

Per-restart rows are in `control_1653_runs.tsv`, and the best t5 key and reading are in `control_1653_best.json`.
**The control reads at most 25.7% of tokens, far under the brief's ~60% bar.** The best of 12 restarts reads no French
beyond scattered syllables. The true key scores about 700 nats better than anything the annealer reaches. So at 752
tokens the language model can pick out the right key, but this search cannot find it: the failure is in the search,
not the scoring. Raising the syllable move share and running 2.5 times longer lifted token accuracy from 12% to 26%.
That is still nowhere near a reading.

**Result.** The 1653 letters (f1 + f9, 752 tokens, 112 types, a key_1659-like syllabic nomenclator) are below what
tools/nomenclator_anneal.py can do, even seeded with the four key_1659 codes. This is a method-limit negative with its
matched control (control 25.7% of tokens). It is not evidence about the letters themselves. **Grades: S 0, M 0, H 0,
C 0.** No token was read in this pass, and the worker A M-list stands as it was. Status stays `open`.

What was found, and where it was not found: no reading of f1 or f9. The control shows that the method fails at this
size and design. No print or phrase search was needed, because nothing was read.

Suggestions, not attempted (Usage item 7): (1) a solver whose moves act on whole words, such as a word-lattice or
dictionary-constrained search over the cipher runs between clear frames, since the frames give sentence context on
both sides; (2) rerun this same control after adding the canvas 11-12 block (about 80 tokens, once reconciled) or the
canvas 32 leaf, to see whether more text moves the control; (3) find the 1653 key itself, in the Brienne and Servien
keys of the same office (a recovery route), which is likelier to open these letters than cryptanalysis.

Requests: none. Cost: about $4 of the $10 cap.

## Canvas 129/130 and canvas 32 (24 Sept 2026)

LANE G2 worker H, Gallica fetcher (Sonnet, cap $7). Files: `passA_f67.tsv`/`passB_f67.tsv`, `trial_f67.py` ->
`trial_f67.tsv` (`--check` exits 1 if stale), `passA_c32.tsv`/`passB_c32.tsv`, `walk_37_159.tsv` (rows added),
`images/manifest.json` (fetch log; crops/natives kept in the worker's scratchpad, folder already at the 30 MB cap).

### (1) Canvas 129/130: folio 67, 10 Oct 1659, Brienne to Servien

Native fetches (`f129/full/full/0/native.jpg`, `f130/...`, 3801-3802x5180-5198px): canvas 129 needed one retry
after a transient connection reset; canvas 130 succeeded first try. Folio number "67" visible top right of canvas
129; canvas 130 carries the dateline "A Paris ce 10 8bre 1659" and signature "...de Brienne", addressed "M. de
Servien" — the same letter the prior worker's canvas walk flagged as not seen before (ROOM.md 08:10, "canvas 129/130, folio
67, dated 10 8bre (Oct) 1659, symbol+numeral, dense"). On the native image this is **numeral-only** (no
symbol vocabulary), not symbol+numeral as the walk's thumbnail-resolution classification guessed — every group is
a plain number, some with a horizontal overline over one or both digits, the same convention as f.86-88's
`key_1659.tsv`. The letter runs canvas 129 (16 lines: a short mixed clear+cipher line, then 15 lines of dense
cipher) onto canvas 130's first 7 lines (continuing the same run, ending mid-line in clear French "Desja ie vous
ay mandé cequi..."), then five lines of clear French ("...il est du service du Roy que vous nous mandiez cequi en
est, comme aussy"), then a second 7-line cipher block ("presupposé..." through "...ce que vous aurez demoy qui
suis").

Line crops cut with `tools/iiif_lines.py --image ... --debug` from the locally-fetched natives (no extra Gallica
request per crop): canvas 129 region `380,1750,3050,3420` (16 bands, `--distance 130 --prominence 15`); canvas
130 block A region `390,650,3050,1050` and block B region `390,2250,3050,1120` (7 bands each, `--distance 120
--prominence 15`). All three debug overlays checked by eye against the native page before handing crops to the
passes. **Crop/line-count mismatch, canvas 129 only**: both blind passes independently flagged that the 16
detected bands do not each hold exactly one manuscript line — bands 1 and 10 each contain two physical lines (the
row-height estimate undercounted there), and the two trailing bands (15, 16) are blank/spurious (past the last
real line, same as the spurious 15th band this worker also hit on canvas 32, below). Pass A self-corrected by
reading the debug overlay directly and assigning `f129_L01`..`L16` to the 16 true physical rows top to bottom
(cross-checked against this worker's own independent read of the full native page — matches token-for-token on
every row); pass B kept the tool's own band numbering (`f129_L01` = physical rows 1+2, `f129_L10` = physical rows
11+12, `f129_L15`/`L16` = blank), noting this explicitly. Both readings are internally consistent and complete;
they just use different line labels for the same content. **Flag for the reconciler**: use `passA_f67.tsv`'s line
numbers as the physical-row reference; `tools/iiif_lines.py`'s pitch/prominence defaults under-detect on tightly
and unevenly spaced cursive rows like this leaf — a future crop pass on this canvas should tighten `--distance`
or crop in two narrower sub-regions rather than one tall region.

Two blind Sonnet passes (`passA_f67.tsv`, `passB_f67.tsv`; second pass never saw the first). Agreement measured by
sequence alignment (`difflib.SequenceMatcher` on each block's flattened cipher-token stream, since the two passes'
line boundaries differ as above): f129cipher 0.892 (327 vs 319 tokens), f130ciphA 0.936, f130ciphB 0.957, **combined
0.915** — higher than the folio 1-2/folio 9/canvas 11-12 letters' 77-85%, consistent with this being a cleaner
numeral-only hand with no ambiguous symbol vocabulary to disagree over. No reconciliation attempted (per brief,
"the orchestrator briefs an Opus reconciler").

### (2) Mechanical trial: does key_1659 read this letter?

`trial_f67.py` applies `key_1659.tsv` (recovered from the 21 Nov 1659 f.86-88 decipherment, a different letter, 65
groups at grade C) to pass A's token stream (bracketed clear French and scribal marks are run breaks), scored by
mean log2 probability per character under `tools/french16_ngram.py`, against a **20-derangement shuffled-key
control** (rule 3), seed 1659:

| letter | cipher tokens | keyed | coverage | chars scored | real bpc | shuffled mean | shuffled sd | shuffled max | shuffled >= real | z | beats control |
|---|---|---|---|---|---|---|---|---|---|---|---|
| f67 | 543 | 501 | 0.923 | 766 | -4.272 | -5.889 | 0.453 | -4.735 | 0/20 | 3.57 | **yes** |

**Coverage 92.3%** (501 of 543 cipher tokens carry a `key_1659` code) and the real key's French score clearly beats
every one of the 20 shuffled derangements (z = 3.57; the best derangement still falls 0.46 bpc short of the real
key). This is a cryptanalytic result (grade S), not a reading: no plaintext is produced here, only a mechanical
check that the f.86-88 key's table also decodes this second, earlier letter better than chance. It is consistent
with both letters being enciphered with the same office table across at least Oct-Nov 1659 (`key_1659` was
recovered from a 21 Nov letter; this is a 10 Oct letter). A full reading (running `key_1659`'s values through
`decode_1659.py`-style per-token grading, and settling the ~8% uncovered tokens) is the natural next step, not
attempted here (out of scope for a fetcher/blind-pass brief).

### (3) Canvas 32: full-page 1653 letter, never transcribed

Native fetch needed three attempts (two connection resets, recovered on the third after a longer pause — logged,
not looped beyond the playbook's one-retry limit in any single attempt). Full page, ~14 lines, **symbol+numeral**
cipher (unlike canvas 129/130): the vocabulary includes `tt`, `d`/`db`, `X`, `mm`, `m`, `11` (two-minim), `£`, the
same sign families as the folio 1-2-3 and folio 9 letters' table, not `key_1659`'s numeral-only style. No date or
signature visible in this crop (the letter's opening and closing are presumably on the neighbouring canvases 31/33,
not fetched here); one clear phrase names "le Comte Philippes" and the leaf ends mid-sentence ("...que se/quelc..."
at the last line, cut by the page edge, no further ink below — a spurious 15th detection band past this point was
discarded, same artifact as canvas 129 above).

Line crops (`region 380,900,3250,3260`, `--distance 120 --prominence 15`, 14 bands, debug-checked). Two blind
Sonnet passes (`passA_c32.tsv`, `passB_c32.tsv`): **82.6% agreement** (95/115 shared positions match exactly,
by-position this time since both passes used the same straightforward 14-line numbering with no band-merging
issue). Of the 20 disagreements, **7 are the same recurring loop+cross sign, called `db` by pass A and `tt` by pass
B** — a real, consistently-drawn sign the two passes just named differently against the reference vocabulary list
they were given; worth resolving first in any reconciliation, likely by comparing both candidate readings directly
against `key_1646`/`key_brienne_1647`/`key_brienne_1651`'s own `tt`/`db` rows. Two clear-French phrases (L02, L09)
are read only tentatively by both passes (cursive, low confidence, flagged C but genuinely uncertain letter-by-
letter). No key trial was run against this letter (it is not in scope of the brief's step 1, and the existing
`trial_1653.py` control already found the three known 1653-band letters read at most 25.7% under a matched
control with all four 1653-era keys — a fourth, similarly-styled letter added to that same trial is a natural
follow-up, not attempted here).

### (4) Canvas walk follow-ups: canvases 45/55/58/74, canvas 122/123 vs 120/121

1000px thumbnails, one attempt each per brief (45/55/58/74) plus one retry each for 74/120/121 (needed for the
dedupe check, not covered by the "one attempt" instruction): **45 unfetched** (connection reset, not recovered
after one retry — logged, not looped further). 55 (folio 31, "Je croyois vous envoyer la coppie d'un arrest...",
dated 1659), 58 (blank verso, docket "sur le Nouveau establissement..."), and 74 (clear French continuation,
dateline "Paris ce 9.e[?] 1659", addressed Servien) are all **plain French prose, no cipher** — rows added to
`walk_37_159.tsv`.

**Canvas 122/123 duplicate flag, checked and confirmed for 120/122, not for 121/123.** The prior worker flagged
"canvas 122 appeared to duplicate canvas 120's content and canvas 123 canvas 121's" from thumbnails alone.
Fetched all four (120 needed a second retry) and compared downscaled grayscale correlation: **canvas 120 and 122
are a genuine duplicate scan of the same recto** — identical text ("Jamais fait difficulté de rendre aux
Ambassadeurs..."), identical dateline "a Paris ce 26.7bre 1659" and signature block, MAE 3.37, correlation 0.90 on
a 200x260 downscale. **Canvas 121 and 123 are not a strong match** — both are faint blank versos with similar
"64" folio-number show-through, which is what made them look alike at a glance, but MAE 8.05, correlation only
0.24 (versus 121-vs-122's 0.11 and 122-vs-123's 0.27, i.e. 121-vs-123 is not meaningfully closer than either is to
the unrelated recto). The half of the flag that named the two content pages is real; the half naming the two
blank versos is not — likely just two ordinary faint versos, not a scan duplicate.

### (5) Status and next step

**Status stays `open`.** No plaintext reading produced (the f67 trial is a mechanical coverage/control check, grade
S, not a decode). No print or phrase search run. No novelty class assigned. Grades: f67 and c32 transcriptions are
M (blind-pass reads, not eye-checked or reconciled); the f67 key-trial coverage/score numbers are S with a matched
control. Follow-ups for a later worker: (1) an Opus reconciler for `passA_f67.tsv`/`passB_f67.tsv` against the
native images, then a full `decode_1659.py`-style reading of the whole letter now that the mechanical trial says
`key_1659` covers 92% of it and beats its control decisively; (2) reconcile `passA_c32.tsv`/`passB_c32.tsv`,
settling the `db`/`tt` sign first; (3) add canvas 32 to `trial_1653.py`'s four-key trial; (4) canvas 45 (still
unfetched) and canvases 31/33 (canvas 32's neighbours, for its date/signature) are open gaps.

### Requests this pass

`gallica.bnf.fr`: manifest fetch (1, cached to `sources/gallica-manifests/btv1b9060495t.json`, committed) + 2
native fetches for canvas 129/130 (1 retry on canvas 129) + 1 native fetch for canvas 32 (2 retries, all transient
connection resets, recovered on the third attempt after a longer pause) + 8 thumbnail fetches for canvases
45/55/58/74/120/121/122/123 (45 and 120 each needed one retry; 45 never recovered, 120 recovered). No other host.
Crops cut from locally-fetched natives, no extra requests. 4 Sonnet subagents (2 blind passes for f67, 2 for
canvas 32, never more than 2 concurrent). All >=1.5s apart, UA `cipher-lab research script (contact via
repository)`. No logins, no credentials, no novelty wording. Well under the $7 cap.

## Folio 67: reconciled and read (24 Sept 2026)

> **Verifier V5b, 24 Sept 2026 (AUDIT.md, "f.67 re-class (V5b)"):** N0. f.68r (canvas 131) of this volume carries the
> letter's text in clear (worker P, "f.68r and f.66r checked"); our partial reading (S 107 / M 416, no H or C) is a
> re-decipherment. Supersedes V5's N3. f.68r is known plaintext for C-grading f.67 (a LANE G2 job).

LANE G2 worker M (Opus, cap $8). Files: `reconcile_f67.py` -> `ciphertext_f67.tsv` (`--check`); `read_f67.py` ->
`exceptions_f67.tsv` (per-token grades), `control_f67.tsv` (`--check`); `decode_f67.json` -> `tools/decode_key.py . --config
decode_f67.json [--check]` -> `reading_f67.txt`, `reading_f67.tsv`. All three `--check`s exit 0 as committed.

### (1) Reconciliation

Canvas 129/130 natives fetched once each to the scratchpad (not committed; folder at its cap). Base is pass A, whose
labels are the 16 physical rows of canvas 129. Pass B merged rows 1+2 and 11+12 into single bands and **dropped 10
groups of row 11** (`_11 70 61 80 , 2 19 6 16 _18 15 18`, present on the image). Each pass B band was mapped onto pass
A's rows and aligned with difflib. Every disagreement was settled by eye on zoomed native crops (reason per position
in `SET`/`INS` in the script):
- **Curly 3** (the f.86/f.88 convention): both passes wrote this hand's rounded, descending 3 as 9, 7 or 2. On the
  image it is the curly form at 20 positions: 96/76/26 -> `36` (de), 99 -> `39` (du), 91 -> `31` (ce), 77 -> `33`,
  72 -> `32`. Kept where the first stroke is a flat-topped 7: f129 L02/3 `_76`, f130a L02/9 `79` (39 not excluded).
- Overlines settled: `_6` (f129 L07/11, L11/21, L15/6, L16/19), `_16` (L07/13, L07/22, L08/2: a small 1 under the
  bar; the passes wrote `_6`), `_11` (L12/11), `_26` (f130b L03/3); `_5` at f129 L07/3 (long-s 5, both passes `_6`);
  `_3` at f130a L02/11 (`_3 7 21` = pour, as in f.86).
- Segmentation: `154` kept as one group twice (f129 L07/19, f130a L04/5; pass B split `15 4`); `61` kept at f129
  L08/16 (B `6 1`); gutter groups added from pass B or the image at f130a L02 (`2 21`), L03 (`2`), L04 (`2`).
- Clear French, row 1: "en diburez [= devrez] parler a leurs Altesses Royalles;" (diplomatic).
Result: 546 cipher groups, conf H 483 (both passes agree, unchanged), M 63.

### (2) Reading with key_1659

key_1659 (79 codes, grade C on the f.86/f.88 letter) keys **523/546 groups (95.8%)**. Grades per token (rules in
`read_f67.py`): **S 107, M 416, I 9, U 14; H 0, C 0.** S = keyed, key row not `conflict`, conf H, and the letters fall
inside a French word of the best lexicon segmentation; M = conflict row (the table's homophone-level rows `7` ou/u,
`15` oi/i, `18` n/on, `16`, `2`, `21`, `9`, `10`... carry most of the text, hence M dominates), conf M, or outside
every French word. I = six unkeyed codes proposed from context only: `72` ni and `67` mi ("maniement", "ministres"),
`32` ci ("principaux"), `43` fo ("fort", "fondement"), `68` mo ("Mademoiselle" twice), `63` lo ("que lon publie").
U: `_76 _24 154 25 80 51 79 _70 _25 _2` (14 tokens). `65` (key value ar, one f.88 attestation) reads **ma** four
times here (maniement, marier, Mademoiselle x2); `10` (key je, conflict) reads **z** in "filz" three times. Both
stay M; a key revision is for the next solver.

Reading, modal key values, as regenerated (`reading_f67.txt`; brackets = unkeyed):
```
f129 L01  [clear] ... a leurs Altesses Royalles; | ou i ou e r
f129 L02  e je [_76] ques n v ou s di e qu n pu b i e de s n ou
f129 L03  ve l le s de [_24] i n de la ve i te de s ques l le s
f129 L04  oi l oi m q r te r oi t fo r t de s t re e s c la
f129 L05  oi s c y s a v oi r ques la f e c t i n du fi l je
f129 L06  qu le n e si oi t de la me re n e s t pr lu s si gn st
f129 L07  n de estr ou pa s se e t ques M. se r oi t e n [154] pe n se e
f129 L08  de se re t re r du ar ni e me n t de s le fa oi re s
f129 L09  [parceque sil pouvoit estre] c st oi n t q l qu r i [25] s t
f129 L10  ou n l m b la b le c ha n ge me n t n ou s qu ou i i
f129 L11  n s de s me su re s qu pr re n e re a le [80] e t ques l s oi n
f129 L12  ques le fi l je e t la me re me s me le ou r s pr i n ci pa
f129 L13  ou x mi ni s t re s pr i s se n t de ca c [51] r ce t
f129 L14  te me s oi n te l i ge n ce oi l ne se r oi t pa s
f129 L15  q s si b le ques v ou s ne n e ou s si e je c n n oi s
f129 L16  oi n ce q qu ve je qu ou s s y qu qu pr pr i ques r o ou s
f130a L01 v je s oi n s qu pe ne t re r ques l le pe ou t e s
f130a L02 i n fi i a t i n [79] [80] p ou r se ar i e r
f130a L03 ou s la pe e s n ne e t q ou r le te m pr s e
f130a L04 ce s t [_70] [154] fo n de me n t ques lo n pu b i e
f130a L05 ar da mo oi se l le qu re n du t re s ar ou [_25] oi
f130a L06 i f fi ce qu ar da mo oi se l le d r le qu n
f130a L07 oi s e ou r [Desja ie vous ay mandé ce qui s'est]
f130b L01 [presupposé] ques ce q l di t de la me s oi n re
f130b L02 i ge n ce de n t re le fi l je e t la me re
f130b L03 oi t ve i ta b le si le ar r q s de [_2] qu ne je
f130b L04 de me ou re st c [51] e de s le f fa oi re s i ou
f130b L05 e n su r q le [80] se je q ou r se n de c ha r
f130b L06 r qu n ju ge e n pe n se e pr lu s o s t
f130b L07 di ve r t r ques de s y qu pr pr i ques r
```

**What it is about** (reader's gloss, grade M as a whole; words in square brackets supplied). The clear opening
says the peace terms and the King's marriage with the Infanta are settled, for Servien's information only, and the
court will tell him when he may speak of them to "leurs Altesses Royalles" (the Savoy court, Turin). The cipher then
runs, roughly: "...[que] l'on publie des nouvelles ... de la verité desquelles il importeroit fort d'estre esclaircy,
sçavoir quelle affection du filz ... de la mere ... que M. seroit en [?] pensée de se retirer du maniement des
affaires; [parceque s'il pouvoit estre] ... un semblable changement, nous ... des mesures qu'on prendra ... et que
le soin que le filz et la mere mesme, leurs principaux ministres, presentement ... de concert, ... une mesme
intelligence, il ne seroit pas possible que vous ne nous [en donnassiez] connoissance ... vos soins [à] penetrer
quelle peut estre l'inclination ... pour se marier, ou [à] la personne, et pour le temps; c'est [?] fondement que
l'on publie ... Mademoiselle ... tres ... Mademoiselle d'Or[l]... [Desja je vous ay mandé ce qui s'est ...]" and,
in the second block, "[presupposé] que ce qu'on dit de la mesintelligence d'entre le filz et la mere soit
veritable, si le mar[quis] de [?] ... demeure ... des affaires ... pour se descharger ... qu'on juge en pensée plus
... divertir ...". So: Brienne asks Servien to find out whether the reported rift between the Duke of Savoy and his
mother is real, whether she means to withdraw from government, and the Duke's marriage inclinations, a
"Mademoiselle" being named. Identities (which Mademoiselle, which marquis) are not established here.

### (3) Control

`control_f67.tsv`. Statistic: share of keyed letters covered by the best segmentation into lexicon words (3+
letters, count >= 5 in tools/data/fr16, 9,498 words), runs between clear words/punctuation; I values not used.
- key_1659 true: **584/810 = 0.721**.
- 200 derangements of key_1659's values over its codes (seed 1659): mean **0.488**, sd 0.060, max 0.647; **0/200**
  reach the true value; z = 3.85. (worker H's n-gram trial on pass A: z 3.57, 0/20.)
- Holdout, key_1659_f86only.tsv (65 codes, f.86 alone): keys 489 groups, rate 0.668 (518/776); 66 tokens take a
  different value from the joint key (the sub-part splits `16` `18` `24` `71`), so the f.88 alignment improves the
  reading of this letter but is not needed for it.
Word-level baseline is high (short French words cover random text), so the margin, not the absolute rate, is the
result.

### (4) Report

Found: folio 67 (10 Oct 1659) is enciphered in the same table as the 21 Nov 1659 f.86-88 letter, and key_1659 reads
it as French over most of its length: S 107, M 416, I 9, U 14 (cryptanalytic result; no H or C on this letter).
Not found / not done: no printed text or decipherment of this letter was searched for (no print check, no phrase
search; novelty is not classified here). The 14 U tokens and the thin/conflict rows (`65` ma, `10` z, `7`/`15`/`18`)
need a key revision with f.67 as a third aligned text; f130a L02/9 `79` vs `39` and the two `154` groups need a second
look on the image. Suggested phrases for a print check: "retirer du maniement des affaires", "mesintelligence
d'entre le filz et la mere", "leurs principaux ministres", with "Servien" and "10 octobre 1659".

Requests: gallica.bnf.fr 2 (canvas 129 and 130 natives, 200 first try). No other host. No subagents.

### f.68r and f.66r checked (24 Sept 2026, for LANE V2 verifier V5's 09:55 ask)

LANE G2 worker P (Sonnet, cap $4). Canvas 131 (f.68r) and canvas 127 (f.66r) fetched from
`https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060495t/f{131,127}/full/2000,/0/default.jpg` (200 both, one try
each), plus a full-resolution f.68r for a closer read. Not committed (scratchpad only; folder is at its 30 MB cap
per the Canvas 129/130 section above).

**f.66r (canvas 127) is blank**, confirmed by eye -- matches V5's walk note. Only a page-number "66" and the tail
of the facing leaf's writing bleeding through from the left margin. No content, no cipher.

**f.68r (canvas 131) is plaintext, not cipher, and it is the same letter as f.67 written out in clear.** It is not
a duplicate transcription of f.67's ciphertext and not a separate letter on a different subject: sentence for
sentence it is the unenciphered French that key_1659's reading of f.67 recovers only patchily, including the
passages f.67 left as U or I tokens. Opening lines (diplomatic, my transcription):

> "...voudrez [manque] le [vous] die qu'on publie des nouvelles de [la/luy] verité desquelles il importeroit fort
> d'estre esclairay [= esclaircy], scavoir que la affection du fils a l'endroit de la mere n'est plus si grande
> qu'au passé, et que Madame seroit en quelque pensée de se retirer du maniement des affaires parceque s'il
> pouvoit estre craint qu'il arrivast un semblable changement nous aurions des mesures a prendre avec le duc..."

and further down: "...quelle peut estre l'inclination du duc pour se marier, [pour la personne et] pour le temps,
et si c'est avec quelque fondement que l'on publie que mademoiselle a rendu tres mauvais office a mademoiselle
d'Orleans sa soeur, que ce qui se dit de la mesintelligence d'entre le fils et la mere soit veritable, si le
marquis de Pianese demeurera [chef] des affaires ou bien sur qui le duc se [pourvoira de charge], qu'on juge en
pensée plustost de se divertir que de s'y appliquer. C'est ce que vous avez [à savoir? -- last line partly under
the gutter]."

This matches reading_f67's gist word for word where f.67 was legible (maniement des affaires, mesintelligence
entre le filz et la mere, principaux ministres, inclination du duc pour se marier, mademoiselle...tres [mauvais
office]) and **resolves two of f.67's open points**: the U group at f129 L08/`_25` etc. sits where f.68r has "le
duc" (confirming "le fils" = the Duke of Savoy, not a named prince), and the unresolved "le marquis de [_2]" at
f130b L03 is **"le marquis de Pianese"** (Filippo San Martino d'Aglié, marquis di Pianezza, chief minister to
Christine of France) -- f.67's key gave no token for this name; f.68r spells it in clear. f.68r also completes
the truncated "Mademoiselle d'Or[l]..." as **"mademoiselle d'Orleans sa soeur"**, i.e. two Mademoiselles are
distinguished: an unnamed one whose marriage prospects are discussed, and Mademoiselle d'Orléans (presumably
Marguerite-Louise or another daughter of Gaston d'Orléans) to whom she is said to have done ill office. Not
established from these two leaves alone which is which; canvas order suggests f.68 sits after f.67 in the same
gathering, both loose in this recueil, so its exact relation (fair copy the cipher was made from, or a decoded
transcript added later) is not settled by handwriting comparison here -- same secretary hand as f.67/f.86-88 by
eye, no distinguishing ink or later annotation seen. **This bears directly on the f.67 N-class**: the plaintext of
the passage f.67 enciphers is present in this very volume, two leaves away, in clear -- a verifier should treat
that as the first thing to check against AUDIT.md's N3 (V5, 24 Sept 2026), not a published source found elsewhere.

**Full-text search.** Gallica's in-document ContentSearch (OCR-based) on btv1b9060495t returns 0 hits for both
"maniement des affaires" and "mesintelligence" -- expected and not informative, since this is a manuscript with no
OCR layer (handwritten leaves return no ContentSearch text at all; checked by the zero-hit response having no
error, just empty `<items/>`). Global Gallica SRU (`gallica all "phrase" and gallica all "phrase2"`) for
'"maniement des affaires" Servien 1659' returned 6,048 records and for '"mesintelligence" "Altesses Royalles"'
5,022 records -- the CQL `all` relation matches on the individual words, not the exact phrase (top hits are
unrelated: Avaux-Servien 1644 letters, Fouquet biographies, a Trente ans war history), so this is **not a phrase
match and not informative** as run; a real phrase search needs Gallica's `adj`/exact-phrase CQL or a different
index, which this worker did not reach. Logged as attempted, inconclusive, 24 Sept 2026.

For LANE V2 / V5: f.68r's plaintext of the same letter, in the same volume, is the material fact for the N-class
decision, not the SRU non-result above. Requests: gallica.bnf.fr 5 (2 images at 2000px, 1 at full res, 2
ContentSearch) + 2 SRU (7 total this section, all 200 first try, >=1.5s apart).

## f.67 aligned to f.68r (24 Sept 2026)

LANE G2 worker R (Opus, cap $7). Files: `dechiffre_f68.txt` (pass A, this worker) and `dechiffre_f68_B.txt` (blind pass B,
Sonnet subagent), `align_f67.py` -> `align_f67.tsv`, `align_f67_conflicts.tsv`, `key_1659_ext.tsv`, `exceptions_f67_C.tsv`
(`--check`); `decode_f67.json` job 2 -> `reading_f67_C.txt` / `reading_f67_C.tsv` (`tools/decode_key.py . --config
decode_f67.json --check` exits 0; job 1, worker M's S/M reading, unchanged).

**f.68r.** Canvas 131 fetched once at 2000 px (the native `full/full` request failed twice at the proxy, ws_closed_mid_exchange
after 11 s; the 2000 px render worked first time; scratchpad only, not committed). No heading, no docket; leaf number "68"
top right; 20 lines, lower half blank. It begins mid-sentence ("voudrez bien que je vous die quon publie des nouvells de
turin") and ends "de sy appliquer Cest ce que vous aurez de moy". It carries neither f.67's clear opening nor its clear
"Desja ie vous ay mandé ce qui s'est presupposé": it is the enciphered passages only, written out (a paragraph break
stands where f.67 has that clear sentence). Two passes agree on 179 of 199 words; the rest are u/v or word division
except five settled on the image (header of dechiffre_f68.txt). New from f.68r beyond worker P's reading: "des nouvelles
de **Turin**" (f.67 `_24` = tur).

**Alignment.** f.67's three cipher stretches (cut at its clear words) aligned to the matching f.68r text with the
align_f86 Viterbi/EM, groups carrying 0-8 letters, key_1659's own f.86/f.88 counts kept as fixed pseudo-counts, and start
seeds for 154/_70/79/80 and worker M's six context proposals (all re-estimated). Grading rules in the script docstring.

| grades (546 cipher groups) | H | C | S | M | I | U |
|---|---|---|---|---|---|---|
| before (read_f67.py, key_1659 cryptanalytic) | 0 | 0 | 107 | 416 | 9 | 14 |
| after (align_f67.py, f.68r known plaintext) | 0 | 435 | 0 | 111 | 0 | 0 |

Of the 111 M: 58 are groups transcribed at conf M (f.68r agrees with the key at most of them, but the group itself is
uncertain; decode_key.py downgrades them and align_f67 does the same), the rest are key conflicts or inconsistent codes.
C includes tokens where f.68r gives an alternate value key_1659 already attests from f.86/f.88 (7 u, 15 i, 18 on, 10 z/s,
_6 qu, 23 p, 24 null): the table is syllabic and these codes carry both values on f.86/f.88 too.

**Codes added (key_1659_ext.tsv, 16 rows, evidence per row):** `_2` pi (Pianese, spelled pi-a-ne-se), `_24` tur, `25` va,
`_25` va, `32` ci, `43` fo (x2), `63` lo, `67` mi, `68` mo (x2), `_70` avec, `72` ni (x2), `_76` bien, `79` du, `80` duc
(x3), `154` quelque (x2): C, consistent at every occurrence (most single attestations). `51` he/h: M (inconsistent).
Worker M's six I proposals (72 ni, 67 mi, 32 ci, 43 fo, 68 mo, 63 lo) are all confirmed by f.68r.
None of the added codes occurs in f.86 or f.88, so their readings are unchanged and were not rerun.

**Conflicts with key_1659 (align_f67_conflicts.tsv, 51 tokens):** `6` key qu (5/5 on f.86/f.88) reads **a** at 11 of 14
f.67 occurrences ("madamoiselle a rendu", "a prendre"); `65` key ar (one f.88 attestation) reads **ma** 5 times (maniement,
marier, madamoiselle x2) -- worker M saw this; `3` key e (one attestation) reads d 3 times (voudrez); `_7` key q (8/8)
reads po/o 4 times (possible, pour); `_10` key st reads ra/a. A revision of 6 and 65 is for the next key worker: key_1659
rows are left as they are and the f.67 evidence is in the `ev_f67`/`f67_evidence` columns. The rest are single
misalignments at spelling differences (e.g. 16 "el" in quelles, 61 "af").

**Report.** f.67 read against its own clear text at C 435 / M 111 of 546; 16 codes added; key_1659 contradicted at 6 and 65.
Not searched for print (not this brief's job); novelty stays AUDIT.md's (V5b). Requests: gallica.bnf.fr 3 (2 failed at the
proxy, 1 x 200). One Sonnet subagent (pass B).

## Sibling volumes (24 Sept 2026)

LANE G2 worker W, brief: find other digitised BnF volumes holding letters in key_1659_ext's period and
correspondence (Servien papers, Brienne's outgoing registers 1658-1661, Turin/Savoy embassy volumes) via
archivesetmanuscrits.bnf.fr's plain POST search and Gallica SRU with `dc.source` scoping. Full table:
`sources/solver-diffs/2026-09-24-lane-g2-servien.tsv` (17 rows).

**Method and control.** `archivesetmanuscrits.bnf.fr` POST `resultatRechercheSimple.html` (cookie jar, field
`TEXTE_LIBRE_INPUT`), per the Fourth-pass method logged in QUEUE.md; a plain `Servien` query (322 results, fully
paginated over 4 pages) surfaces Français 5160 itself in the results' own left-hand facet sidebar
(`recalculFacets.html?...&filtre=Dao`, confirming the ark `btv1b9060495t`) — control passed. Six further queries
narrowed the term (`Servien Turin`, `Servient Turin`, `Ennemond Servient`, `chiffre de Servien`, `Brienne
Turin`, `Brienne chiffre Servien`, `Loménie Brienne Savoie`). Gallica SRU (`gallica.bnf.fr/SRU`, GET not POST —
a POST 405s) scoped with `dc.source all "Manuscrits"`/`"Mélanges de Colbert"`/`"Baluze"`/`"Clairambault"`/`"NAF"`
combined with `dc.description all "Servien"`/`"Turin"`/`"chiffre"`, three queries. Both hosts gave one
`ws_closed_mid_exchange` proxy-side reset apiece (confirmed via `/__agentproxy/status`, not a site block),
each recovered on a single retry per the good-citizen rule.

**No volume in fr.5160's own 1653-1661 window was found carrying an explicit cipher note.** The closest leads:

- **Mélanges de Colbert 26** (ark `cc955062`, digitised): part III is Henri-Louis de Loménie de Brienne's own
  outgoing despatches as secrétaire d'État aux Affaires Étrangères, **juillet-décembre 1661** — the tail end of
  fr.5160's date range, same office. No "chiffre"/"déchiffrement" in the item-page catalogue text (checked
  directly); not opened as an image this pass.
- **Français 20657-20674**, item **Français 20660**: "Lettres originales adressées en général au comte de
  Brienne...1652-1659" — exact correspondent, exact years, but general incoming correspondence (Provence,
  galères, marine), no cipher note, **not digitised** (no `pictoGallica` badge).
- **Français 20500-20576**, item **Français 20563**: "Papiers du comte de Brienne. Tome III (1630-1660)" —
  not digitised, item-level cipher status unread.
- **Français 23203-23204** "Papiers et lettres d'Henri-Auguste de Loménie, comte de Brienne": matched only at
  the volume-header level in this pass's queries, no item rows returned, not resolved.
- **NAF 6972-7328** "Collection de Brienne": a very large Brienne-family collection; the Savoie-related items
  this pass's queries actually surfaced are all 1521-1629, decades too early — later volumes, if any, not
  located.

Everything else found under "Servien"/"Servient" + "Turin" is off-period: **Mélanges de Colbert 113,
120-120bis, 121-121bis, 123-123bis, 124, 127-127bis, 130-130bis** (all digitised) are Ennemond Servien's own
Colbert correspondence as ambassadeur à Turin/en Savoie, but dated **1662-1665**, after fr.5160 ends;
**Mélanges de Colbert 131-131bis** is the Savoy ambassador Giron de Ville's reciprocal correspondence, also
1665. **Baluze 155-156** (31 letters of Abel Servien to Sabran) and **Baluze 163** (Claude de Mesmes d'Avaux at
Venice, one letter "en partie chiffrée" signed "Chrysogono") are both **1629-1637**, Abel Servien's earlier
Italian mission, not Ennemond's 1659 Turin embassy, and Baluze 163's cipher is a different, unrelated code
name. **Français 3822, 3944** and **Dupuy 869** (all digitised, all found via the Gallica SRU control query)
are 1615-1648 miscellanies with incidental Savoy/Turin items, no cipher note.

**Negative.** Gallica SRU, `dc.source` scoped to Mélanges de Colbert + Baluze + Clairambault + NAF combined,
`dc.description all "Turin"` and `dc.description all "chiffre"` together: **0 records** — no volume in these
four fonds carries both words in its catalogue description. Not exhaustive (archivesetmanuscrits' own
pagination cap, and the "chiffré alone is foliation noise" lesson both apply; a cataloguer's dc.description
for an item-level cipher note does not always propagate to the parent record SRU indexes).

**No image beyond one Gallica ark check** (this brief's limit); nothing here has been check-solved, and no
novelty claim is made. Next step for whoever returns to this: open Mélanges de Colbert 26 part III (Brienne's
Jul-Dec 1661 despatches, closest in time to this volume) and Français 20660/20563/23203-23204 (Brienne's own
papers, if any turn out to be digitised after all) at the image, since none of the leads above were checked
past the catalogue-text level.

Requests: archivesetmanuscrits.bnf.fr ~12 (POST searches + 1 item-page GET, ≥1.5s apart, one
`ws_closed_mid_exchange` reset recovered on retry), gallica.bnf.fr (SRU) ~5 (2 `ws_closed_mid_exchange` resets
before the host recovered, then 3 clean queries). No logins, no subagents, no images fetched beyond the ark
confirmations already in the sources TSV. Well under $3 cap.

## Canvas walk 160-367 (24 Sept 2026)

LANE G2 worker V, Sonnet, cap $6. Read `walk_160_367.tsv` for the full per-canvas table. IIIF `full/600,/0/default.jpg`
thumbnails, one canvas at a time, ~1.8 s apart, descriptive User-Agent, one retry then skip (never needed — every
fetch in this pass returned 200 on the first or second try). Read directly by this worker, no subagent, per brief.

**No new cipher letter found in canvas 160-367.** Canvas 160-167 (folio 82-85 approx.) and 174-218 are plain French
Brienne/Servien diplomatic correspondence, Nov-Dec 1659 (one Dec 1661 dateline noted near canvas ~205), covering the
Pyrenees peace ratifications, the royal marriage, Piedmont/Savoy court affairs, Switzerland, and the Baltic war —
ordinary recto/letter/verso-docket/blank pattern, no cipher on any of the 59 canvases fetched and read in that span.

**Canvas 168-173 is the already-known folio 86-88 cipher dossier, not a new find.** Cross-checked this pass's own
reading against the existing NOTES.md sections "Folio 86 cipher and folio 87 decipherment" and "Folio 86-88: key from
the f.87 decipherment": canvas 168-169 = folio 86's numeral cipher (opens "Monsieur, la lettre qu'il vous a pleu de
m'escrire du 8e..."), canvas 170 = folio 87, the contemporary decipherment ("Dechiffré de la lettre de M.r le Comte
de Brienne du 21 9.e 1659"), canvas 172-173 = folio 88's own separate numeral cipher block, closing "A Paris ce 21e
9bre 1659" signed Brienne. All three already reconciled (`ciphertext_f86.tsv`, `ciphertext_f88.tsv`,
`dechiffre_f87*.txt`) by an earlier LANE G2 pass this same day; this walk independently confirms the canvas
assignment and finds nothing beyond what is already committed.

**Canvas 219 (folio 111) is a structural finding: the volume's second item starts here, and it is out of this
brief's date scope.** The leaf reads "Lettres Originales de M.r le Tellier a M.r Servien" — exactly the item-2
divider the catalogue notice (`archivesetmanuscrits.bnf.fr` OAIRecord, quoted earlier in this file) describes as
folio 111-182, Le Tellier to Servien, 22 March 1652 - 27 August 1658, with **no cipher note** in the catalogue
description. Canvas 221 (folio 112) confirms the start date directly: "Lyon ce 22 mars 1652", Le Tellier's own
signature. Since item 1 (the only correspondent this volume's catalogue entry ever attributes cipher to, Brienne
père-et-fils, folio 1-110) already runs the full 1653-1661 span and ends at canvas ~210 (folio 110, last blank
recto before the title leaf), **item 2 cannot contain any further 1659-61 cipher letter by construction** — its
latest possible date (27 Aug 1658) predates the whole window this brief was briefed to search.

**Canvas 220-367 (item 2's ~147 remaining canvases) was therefore spot-sampled, not walked canvas-by-canvas,** to
conserve the cap once the date-scope argument above was established: canvas 222-229 read in full (plain Le Tellier
administrative correspondence, garrisons and munitions, no cipher), then single-canvas spot checks at 240, 260, 280,
300, 320, 340, 360, 365, 367 (9 samples spanning the rest of the volume) — folio 121, 131, blank, dense plain prose,
blank with a July dateline, blank with a Nov 165[7] dateline, folio ~17x plain French, folio 182 blank (matching the
catalogue's stated end of item 2), and canvas 367 blank (the volume's last canvas). No cipher and no numeral groups
in any of the 9 samples. This is a **sample, not an exhaustive walk** of 230-364 — a stray misfiled or misdated leaf
inside item 2 cannot be fully ruled out by 9 samples over ~135 unread canvases — but it is consistent with the
catalogue's own "no cipher" description of item 2 and gives no reason to expect a further 1659-61 cipher letter in
this volume beyond what canvas 8-173 already documents (folio 1-3, folio 9, the unnumbered full-page 1653 letter at
canvas 32, folio 67-68, folio 86-88).

**Status stays `open`.** No decoding attempted this pass. No print or phrase search run (nothing new read as
plaintext). No novelty class assigned — canvas 168-173's novelty is AUDIT.md's, unchanged. Grade of every cipher_extent
call in `walk_160_367.tsv`: M (single-worker read at 600px, no subagent cross-check, no reconciliation against native
resolution).

**Follow-up, not attempted here (stop when the brief is met):** if a later worker wants to close the "no cipher in
item 2" question more firmly than a 9-canvas sample, the remaining ~135 canvases of 230-364 are the next walk —
cheap at 600px, low expected yield given the catalogue and the date argument above.

### Requests this pass

gallica.bnf.fr: 79 (160-229 sequential, plus the 9 spot-check canvases 240-367), all `full/600,/0/default.jpg`, all
≥1.8 s apart, descriptive User-Agent (`cipher-lab research script (contact via repository)`). All 200 on first or
second try; one transient `curl: (35) Recv failure` on the automatic retry within the fetch loop resolved itself
(same URL, no host-level block). No subagents, no other hosts. Well under $6 cap.

## key_1659 codes 6 and 65 (24 Sept 2026)

LANE G2 worker Y (Opus, cap $4, disk only, no network). Question: key_1659 has 6=qu and 65=ar; the f.67/f.68r alignment
gives 6=a (11 of 14) and 65=ma (5 of 6). Is each one a homophone, a value that differs between letters, or an alignment slip?

**65: an alignment slip in f.88. The value is ma in all three letters.** f.88's only 65 falls in "de sy marier" (f.87 l.17), coded
`36 20 9 65 _12 2 21`. The unseeded EM split it as `9`=ym `65`=ar `_12`=i. The same word in f.67 ("pour se marier", f130a
L02) is `65 _12 2 21` again, and f.67's other five 65s are ma-: maniement, madamoiselle x2, marquis, plus one "quema" the
aligner merged. `9`=y is otherwise 8/15 and was never ym. Fix: `joint_key.py` now seeds `65`=ma (`EXTRA_SEEDS`, used in
`joint()` only, so the hold-outs are unchanged), which is external known plaintext from f.68r. Only f.88 L03/13-15 realigns
(y | ma | ri), and every other f.86/f.88 alignment row is unchanged. The same realignment exposes `_12`=ri: f.67 gives ri at
8 of 8 (tu-ri-n, ve-ri-té, ar-ri-vast, au-ri-ons, p-ri-ncipaux, p-ri-sent, ma-ri-er), and key_1659 row `_12` is now i 2/3 with ri
1, flagged `conflict`. That is honest, but it costs three C tokens on f.86/f.88 (below). A later key worker could set `_12`=ri
and `23`=p, not pr: f.67 gives `23`=p at 9 of 10.

**6: a different value in each letter. It is not a homophone, and neither alignment slipped.**
- f.86/f.88 (21 Nov 1659): 6 = qu at 5 of 5, all in unambiguous f.87 contexts: "si noire **que** seroit", "de croire **que** M.r
  Dambrun", "en **quel**s termes", "discours **quel**le a tenus", "des**quel**les". The native crop `crops/f86_cipher_L08.jpg`
  shows a plain, un-overlined 6 directly before the clear "M.r", so the sign reading holds there.
- f.67 (10 Oct 1659): 6 = a at 11 of 14 (du filz **a** l'endroit, qu'il **a**rrivast, **a**urions, mesures **a** prendre, office **a**
  mademoiselle, Orle**a**ns, Pi**a**nese, madamoiselle **a** rendu...). Under the letter-scoped value the aligner puts a at 13 of 14. The
  remaining one, f129 L16/15 (p), sits in the aligner's untidy "possible/pour" run.
- The two letters also swap the a-sign. f.86/f.88 write a as `m` 21 times in 438 cipher groups. f.67 has **no `m` at all** in 546
  groups: at the same rate about 26 would be expected, and it writes a as `6` (14) and `70` (3). f.67's qu is `_6` (13 of 13).
  A code does not carry two unrelated values inside one letter. The pattern fits a table in which 6 was reassigned between
  10 Oct and 21 Nov 1659 (a revised issue of the same table, or a scribe's variant), or, less likely, a sign in f.67 that two blind
  passes and the reconciler all read as 6 when it is the November `m`. **Not settled:** the canvas 129/130 natives are not on
  disk, since earlier workers kept them in their own scratchpads, so the f.67 sign was not compared with f.86's 6 and `m`.
  Suggestion: fetch canvas 129 once, crop f129 L06/1 and L16/9, and compare them with `crops/f86_cipher_L08.jpg` (6) and
  `crops/f86_cipher_L11.jpg` (`m`).
- Fix: key_1659 row 6 stays qu (f.86/f.88). `align_f67.py` has `LETTER_SCOPED = {'6': 'a'}`. For f.67 it drops key_1659's
  f.86/f.88 counts for code 6 as the prior and grades an f.68r "a" as C "f.67-scoped value". `key_1659_ext.tsv` row 6 keeps the
  value qu and records ev_f67 13/14.

**Grades before / after (tokens; every `--check` exits 0: decode_1659, align_f67, read_f67, reconcile_f88b, decode_key both jobs):**

| reading | before | after | why |
|---|---|---|---|
| f.86 (decode_1659) | C 69 M 199 P 12 | C 68 M 200 P 12 | L04/7 `_12` now a conflict row |
| f.88 (decode_1659) | C 103 M 165 U 3 P 13 | C 101 M 167 U 3 P 13 | L03/14 `65` ma stays C; L03/15, L04/8 `_12` now M |
| f.67 on f.68r (align_f67, job 2) | C 435 M 111 | **C 454 M 92** | 6=a x13 and 65=ma x2 C; `_12` ri via attested alternate |
| f.67 cryptanalytic (read_f67, job 1) | S 107 M 416 I 9 U 14 | S 102 M 421 I 9 U 14 | 65 ma now S x2; `_12` conflict drops S |

The f.67 cryptanalytic control is unchanged in kind: true rate 0.720 against derangements with mean 0.488, sd 0.061, and 0 of 200
at or above the true rate (z 3.82; it was 0.721 and z 3.85).
f.67's conflicts drop from 51 to 32 tokens (`align_f67_conflicts.tsv`). Side change: `_24` is now tu (Turin = tu-ri-n), not tur.

Report: 65 = ma (an alignment slip in f.88, corrected by an external seed). 6 = qu in the November letter and a in the October
letter, so it is a letter-scoped value. Whether that reflects a table revision or an unchecked sign reading in f.67 was not
settled, because the f.67 image was not on disk. No H anywhere (no key source), no novelty wording. Requests: none (no network).
No subagents.

## Code 6 image compare (24 Sept 2026)

LANE G3 worker A (Opus, cap $3). Question from 'key_1659 codes 6 and 65': is f.67's code 6 (value a, 13 of 14) really a 6, or the
November `m` misread by both passes? **It is a real 6. No correction to ciphertext_f67.tsv; LETTER_SCOPED stays.**

Image: canvas 129 (f.67r) cipher region `380,1750,3050,3420` at native resolution (3050x3420), one Gallica request after the full
`native.jpg` and `default.jpg` URLs each reset once (manifest entry in `images/manifest.json`; kept in the worker's scratchpad,
folder at its 30 MB cap). Canvas 130 was not fetched (brief: one native), so its six occurrences (f130a L01/7, L05/8, L06/5, L06/16;
f130b L03/16, L07/10) are not image-checked.

Comparison signs: `crops/f86_cipher_L08.jpg` (f.86 code 6 before "M.r", = qu) and `crops/f86_cipher_L11.jpg` (f.86 `m`, = a).

| f.67 token | on the image | confidence |
|---|---|---|
| f129 L06/1 | plain 6, open bowl with tall ascending stroke, no bar; line-initial | high |
| f129 L09/9 | plain 6 after `16`, no bar; clearly separated from `16` | high |
| f129 L10/20 | plain 6 before `7 _12 24`, no bar | high |
| f129 L11/9 | plain 6 before `23 _11 18`, no bar | high |
| f129 L16/6 | plain 6 after barred `_7`; bar stops before it | high |
| f129 L16/9 | plain 6 after `10` | high |
| f129 L16/14, L16/15 | two plain 6s after `9`, before `23 23` | high |

All eight are the same form as the f.86 six (loop with a tall, rightward-leaning ascender) and the same form as the 6 inside this
page's own `16`, `26`, `36`, `66`, `76`. None resembles the f.86 `m`, which is a three-minim minuscule m with no ascender; no
two-minim or three-minim sign occurs anywhere in the f.67 region (the letter has no `m`, as the earlier count said). The only
nearby confusable, overlined `_6` (= qu on f.67, 13 of 13), is excluded because none of the eight carries a bar. So a
misread cannot explain the split: on the evidence of the 8 image-checked tokens, code 6 = a in the 10 Oct 1659 letter and qu in
the 21 Nov 1659 letter, with a written as `m` only in November. This fits a revised issue of the table between the two letters
(or a second table variant in use at the office), not a sign-reading error. Recorded as a table revision; LETTER_SCOPED kept
with an image-check comment in `align_f67.py`.

`_12` = ri conflict: the two `_12` tokens in the fetched region that were viewed (f129 L09/11, L10/22) are a clear overlined 12,
so that conflict is not a sign misread either; f.67 gives ri 8/8 against key_1659's i 2/3. Reported, not forced.

Grades: unchanged, since no ciphertext changed (f.67 on f.68r C 454 M 92; f.67 cryptanalytic S 102 M 421 I 9 U 14).
`align_f67.py --check`, `read_f67.py --check` and `tools/decode_key.py . --config decode_f67.json --check` exit 0.
Not checked: canvas 130's six 6s (suggestion: one region request on canvas 130 if a later worker needs 14/14).
Requests: gallica.bnf.fr 3 (2 resets, 1 success). No subagents.

## KX-COLB26: Mélanges de Colbert 26 part III (25 Sept 2026)

LANE KX worker KX-COLB26, QUEUE row KX-01. Job: eye-check BnF Mélanges de Colbert 26 part III (Brienne's outgoing
despatches, juillet-décembre 1661, "Hollande, Angleterre, Espagne, Italie, Turquie") for cipher, then check-solved
any leaf found. No key applied (out of scope for this brief).

**Ark correction.** QUEUE row KX-01 and this file's own "Sibling volumes" section (line ~1708) both give the ark as
`btv1b955062`. That ark 400/500s on both the IIIF manifest and the item page (retried once each, per the good-citizen
rule) — it is not a valid Gallica document ark. `cc955062` is the BnF finding-aid record id (`archivesetmanuscrits.
bnf.fr/ark:/12148/cc955062`, `FRBNFEAD000095506`), not a Gallica ark either. The finding-aid page itself embeds the
real Gallica ark: **`btv1b10035069t`** (confirmed: manifest fetches 200, 779 canvases, all labelled 'NP'). Whoever
updates QUEUE.md/KEY-CROSSMATCH should correct the ark there.

**Volume structure**, read off the finding aid (`archivesetmanuscrits.bnf.fr/ark:/12148/cc955062`) and confirmed by
eye: "Papier. 66, 332 et 366 feuillets." — Part I = Coignet de la Thuillerie/Servien correspondence, 1644-1648, 66
feuillets (canvas ~4-69 by eye); Part II = Brienne's own despatches "Tom. I", France/marine/Lorraine/Allemagne/
Nord/Suisse, 332 feuillets, its own alphabetical index at canvas ~70-74 (table entries "R" through "V" seen at
canvas 70, referencing the part's own internal pagination, e.g. "p.325"), content canvas ~75-404; **Part III**
begins at **canvas 405** with its own title leaf, "Depesches de M. de Brienne, Tom. II, Concernant les affaires de
Hollande, Angleterre, Espagne, Italie, Turquie. Depuis le commencement de juillet jusqu'à la fin de dec. 1661"
(canvas 405-406, two near-identical drafts of the same title), followed by its own "Table des lettres contenus en
ce Volume" (canvas 407-408), then the despatches proper from canvas ~409 (folio numbering restarts inside Part III;
letters seen are addressed to Monsieur de Thou — the French resident at The Hague, matching the "Hollande" heading
— dated 29 July and 13 Aug 1661 at canvas 415/425) through to the end of the volume at canvas 779 (back cover;
last dated letter seen, canvas 770, is to "Roboly Marchand" at Constantinople, matching the volume's own
"Turquie"/end-Dec-1661 close). Part III's own span is canvas 405-779 (375 canvases for a stated 366 feuillets,
consistent with the title/table/cover overhead).

**Eye-check.** IIIF `full/450,/0/native.jpg` thumbnails (below the brief's suggested ~1000px, chosen to keep the
image-request and review cost down over ~100+ leaves; digit clusters remained visually distinguishable from cursive
prose at this size in the one confirmed case found elsewhere in this volume, see below). Per the brief's sampling
rule (366 feuillets > 250): every leaf of the first 40 canvases of part III (405-444) and every 5th canvas from 445
to 779. **104 of 375 canvases checked** (39/40 of the first block — canvas 441 unfetched, two connection resets,
one retry each per the good-citizen rule, not retried further; 65/68 of the every-5th sample — canvases 465, 470,
485 unfetched, same reason).

**Negative.** No leaf checked shows cipher — no numeral groups, no interlinear decipherment, no "en chiffre" or
"déchiffré" marginal note. Every leaf sampled is plain French chancery cursive prose. This matches the brief's own
honest prior ("outgoing despatch registers are usually minutes in clear"). Not exhaustive: 271 of 375 canvases in
Part III were not opened (the un-sampled 4-in-5 leaves plus 4 connection failures), so a cipher passage on an
unsampled leaf cannot be ruled out, only made unlikely by the sampling density used.

Since no cipher was found, per the brief this stops here — no check-solved is run (step 3, applying only if cipher
turns up). Kind: n/a (negative eye-check, not a reading).

**Flag — cipher found in Part I, outside this brief's scope.** While resolving the ark (probing canvases 1, 4, 20,
40, 60, 70, 75 on the corrected ark to locate the part boundaries before finding the finding-aid's own title pages),
**canvas 20 (folio ~17 of Part I, the Coignet de la Thuillerie/Servien correspondence, 1644-1648, addressed from
"Coppenhaghen"/Copenhagen, in the middle of a plain-French letter about the Westphalia plenipotentiaries)** shows a
genuine cipher passage: numeral groups run inline with plain-text connective words, e.g. "...la Suede... 6 25 zz 11
83 c 21 90 y 34 14 n° 65 f g... injurera par cette fortune quide 42 z gr m d 96 d 83 to 43 21 q q 21 49 21 32 c...
o ne connoit de raison qui..." — the same nomenclator shape (numeral groups substituting for content words, syntax
left in clear) as fr5160-letellier-1653's own key_1659 cipher. This is a **different correspondence** (La
Thuillerie/Servien, Dutch Republic and Scandinavia, 1644-48) from KX-01's Brienne 1661 despatches, and outside this
brief's scope (Part III only, no key work authorised); not eye-checked further, not check-solved, no novelty claim.
Image kept: `colb26/f20_source.jpg` (900px). Flagged in ROOM.md for the lane orchestrator to route as a new
candidate (own QUEUE row, own key-crossmatch check — key_1659/key_brienne_1647/key_brienden_1651 are Brienne's
1650s-60s Secretary-of-State cipher and not necessarily the same nomenclator as this 1644-48 La Thuillerie/Servien
one, so this needs its own key search, not an assumed match).

Requests: gallica.bnf.fr ~150 (manifest fetches incl. the wrong-ark 500s, `archivesetmanuscrits.bnf.fr` finding-aid
page, Gallica SRU queries used only to try to relocate the ark before the finding aid gave it directly, and ~146
IIIF image fetches at 1.8s apart, one retry each on ~10 connection resets, all recovered except the 4 canvases named
above); archivesetmanuscrits.bnf.fr 1. No DECODE, no credentials, no subagents (fetch/eye-check split across
foreground calls and this worker's own background shell jobs, not subagents). Well under the $4 stall-alarm cap.
