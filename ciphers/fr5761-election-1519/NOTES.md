open

# 1519 imperial-election embassy cipher key -- BnF Français 5761, no. 3

Edition check (25 Sept 2026, LANE R8, intake-gate repair, re-verified from 24 Sept): Mignet, *Rivalité de
François Ier et de Charles-Quint* (1886, Internet Archive `rivalitdefranois01mign`), be-api full-text
search "Cordier" -> 1 hit, p.554 (printed p.193): cites the Feb 1519 instruction from a different archive
(AN J 952), no cipher named; 0 hits for "chiffre"/"Motheaugroing"/"5761"/"Salviati" in the volume. Le Glay,
*Négociations diplomatiques entre la France et l'Autriche* (1845, IA `negociationsdipl01legluoft`):
"Cordier"/"Motheaugroing" 0 hits; "chiffre" 1 hit p.836 (a different embassy, Rogendorf/da Burgo
postscript); "Salviati" 1 hit p.836 (a different legate, unrelated to this key's own "Salviati" line).
Desjardins, *Négociations diplomatiques de la France avec la Toscane*, confirmed by title and by web
search to cover Franco-Tuscan (Italian) relations only, not the German/imperial-election embassy -- out
of scope for this target, not a gap. Tomokiyo (`sources/cryptiana/web/*.htm`, all 104 cached pages
grepped): no hit for this shelfmark, these names or this embassy; `habsburg.htm`'s 1519 section covers a
different cipher (Nassau to Margaret of Austria). Both solver repositories (fresh shallow clones, grepped
for "5761", "motheaugroing", "cordier", "voiage.*allemagne", "conte palatin", "deppartiz", "bourdeaulx",
"moltzau"/"moltzan"): no genuine hit -- every apparent match is a coincidence: `cyphersolver`'s
`gallica_sweep/sru_chiffre_desc.json` "Bourdeaulx" hits are the city of Bordeaux (a title, "second
président de Bordeaux", and place-name uses), not the person "[Jehan] de Bourdeaulx" of this key's f110
block; its `caprile1519/NOTES.md` names "Joachim [Moltzan?]" once, in an unrelated Ferrarese-to-Hungary
dispatch that mentions the same 1519 imperial election in passing -- real historical corroboration that
Moltzan/Moltzau was active in this exact election, not a ciphertext or key match. Full six-source
check-solved log (web, print/calendars, cryptiana/cipherbrain, DECODE, Bourdeau, Aymeloglu) below is
unchanged from 24 Sept 2026 and still supports `open`.

`python3 tools/intake_gate_check.py fr5761-election-1519` (25 Sept 2026, after this rewrite):
`fr5761-election-1519: open (line 1) -- edition/page or full-text-search citation found within 6 lines`
(exit 0).

QUEUE row: M36 (`sources/solver-diffs/2026-09-24-lane-g3-gallica6.tsv`, "Sixth pass (LANE G3), 24 September 2026").

## Source

BnF, Département des Manuscrits, **Français 5761** ("Anc. 10332(3)", "Recueil de copies de lettres et de
pièces concernant"), item 3: "Recueil des négociations « pour le faict de l'empire » recherché par
François Ier contre Charles, roi d'Espagne, le futur Charles-Quint, après la mort de l'empereur Maximilien
Ier," subdivided (finding aid `archivesetmanuscrits.bnf.fr/ark:/12148/cc587094/cd0e296`, fetched via
browser, 24 Sept 2026):
- Fol. 46-50: "Instruction... à ceulx qui vont devers le conte palatin. Messieurs Cordier, conseiller du
  roy en son grant conseil, et le Sr de La Motheaugroing,... envoye[s] par devers... le conte palatin du
  Rin, prince et electeur de l'empire..."
- **Fol. 50-53: "Chiffres desquelz l'on a usé durant le voiage d'Allemagne, faict pour l'empire, deppartiz
  ainsi qu'i s'ensuit"** -- the M36 target itself, a cipher-assignment key list naming: Cordier & La
  Motheaugroing; Langjac; La Vernade (to Trèves); Lorraine, Orval, Bazoges, Savonnières, Chasteaubriant and
  **Salviati**; treasurer Robertet; La Guiche; Joachin de Moltzau (to the marquis de Brandebourg); Tavannes
  and de Surie (to the duke of Saxony); the grand archdeacon of Sens (to the legate in Germany); François de
  Bordeaux (to the marquis de Brandebourg).
- Fol. 54-102: "Lectres du roy durant ledict voiage" -- the king's own letters to the negotiators (Jean
  d'Albret Sr d'Orval, Guillaume Gouffier Sr de Bonnyvet amiral de France, président Guillard), 7 Feb - 5 Jul
  1519, from Paris, Port de Marly, Saint-Germain-en-Laye, Vincennes, l'Isle-Adam, Melun (one, fol.77v, to
  Pope Leo X).
- Fol. 104-172: "Responces au roy durant ledict voyage" -- the negotiators' replies, 10 Feb - 18 Jul 1519,
  from Lunéville, Trèves-Sierck, Nancy, Dieuse, Coblentz.
- Fol. 173-179: further individual letters "Voiage d'Allemaigne pour l'empire. A plusieurs Srs
  particuliers" (to captaine Francisque, the Palatine elector's brother, Louise de Savoie, "monseigneur
  Cordier," duke Frederic of Bavaria, the Palatine elector twice more, his chancellor), before Easter 1520
  through 15 Jul 1519 (sic, dates as catalogued span both years across subsections).

**Key finding for a recovery worker**: the catalogue text for Fol. 54-102 and Fol. 104-172 (the actual
letters exchanged during this embassy, by the same negotiators the key list names) **does not use the word
"chiffre" anywhere** -- per the finding aid's own wording, no ciphertext is stated to survive among the
volume's own letters. This is a catalogue-text check only (per brief: "catalogue only, no canvas walk");
it does not rule out an unremarked cipher passage within any of those ~170 folios of correspondence, only
that the cataloguer did not flag one. A companion ciphertext letter using this exact key, if one exists,
was not located in this volume by catalogue wording alone.

One correspondent named in the key list, **"Salviati,"** is not identified further by the catalogue (a
Frenchified surname spelling consistent with the era's cipher-key lists, which often garble names). Given
the Salviati banking family's established presence in Lyon and French royal finance in this period, this
is plausibly an unrelated Salviati agent/banker in French service, not the Medici-circle Cardinal Giovanni
Salviati of M35 (BnF fr.2933 no.11, dated 1525, a different volume, different date, different context --
Cardinal Salviati was not part of a 1519 French embassy to the Palatine elector). Flagged as a naming echo
worth a follow-up worker's attention, not concluded as the same person.

## Check-solved sweep (24 September 2026)

1. **Web search.** `"Français 5761" chiffres 1519 Cordier Motheaugroing`, `1519 élection impériale chiffre
   clé Cordier La Motheaugroing François Ier`: surfaced only the manuscript's own finding-aid page and
   general 1519-imperial-election historiography (Wikipedia, Wikisource, Cairn.info, Herodote.net) -- none
   ties this cipher key to a prior transcription, print or decipherment. Wikisource's "Une Election à
   l'Empire en 1519" (Mignet, checked directly below) was the one lead worth following through.
2. **Print / calendars.** Mignet, *Rivalité de François Ier et de Charles-Quint* (1886 ed., Perrin;
   Internet Archive `rivalitdefranois01mign`, vol.1) is the standard calendar/narrative history of exactly
   this 1519 election and its embassies. Full-text search (`be-api.us.archive.org/fts`) against this volume:
   - "Motheaugroing": 0 hits. "Salviati": 0 hits. "5761": 0 hits. "chiffre": 0 hits anywhere in the volume.
   - **"Cordier": 1 hit, page 554** -- "Instruction de février 1519 pour Cordier (conseiller du roi en son
     grand conseil) et La [Motheaugroing]..." and again on p.193, "maître des requêtes Cordier, de l'autre
     Armerstorff, le comte de Nassau..." The footnote for the first passage cites **"Moitzan. Carton J.,
     952, page 8"** -- an Archives Nationales Trésor des Chartes series reference (J 952), **not** BnF
     fr.5761. Mignet therefore knew of and used this same February 1519 instruction, from a different
     archival copy, and at no point in the volume mentions a cipher for it. This is a real, checked negative
     for one major calendar/narrative source: the instruction is in print (Mignet cites and paraphrases it),
     but its accompanying cipher key is not, at least not in this volume.
   - "Palatin"/"électeur palatin": 5 hits, all on the same page 554 spread, general narrative about the
     Palatine electorate's grievances -- no cipher content.
3. Duplicate of item 2 (Mignet is this period's standard narrative/calendar; Desjardins Toscane and the
   Catalogue des Actes de François Ier, used for other 1519-1525 BnF fr. targets this pass and last, cover
   different theatres -- Italy/Tuscany and royal acts respectively -- not the German/imperial-election
   embassy; not separately queried this pass, a gap for a follow-up if Mignet's coverage is judged
   insufficient).
4. **Cryptiana / Cipherbrain.** Grepped all 104 cached `sources/cryptiana/web/*.htm` pages for "5761",
   "motheaugroing", "cordier", "voiage.*allemagne", "conte palatin", "cardinalis": no relevant hit (the two
   files matching "5761" as a bare substring, `codebreaking.htm` and `spanish3.htm`, are unrelated numeral
   coincidences in cipher-figure examples, checked directly). `habsburg.htm`'s "Margaret of Austria (1519)"
   section covers a different 1519 cipher entirely (Nassau-to-Margaret, Achembourg, 13 April 1519, already
   in `spanish2.htm`) -- no mention of the French embassy to the Palatine elector or this key. No
   Cipherbrain page found by web search.
5. **DECODE.** `unsolved-ciphers/catalogue/decode-catalog.csv` grepped for "5761" (the numeral is an
   unrelated DECODE record id, a Florence ASFi 1504 item) and for "Cordier"/"Motheaugroing"/"palatin": no
   hit under any of these terms tied to a French 1519 item.
6. **Solver repositories.** Fresh shallow clones of `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers`
   grepped for "5761", "motheaugroing", "cordier", "cardinalis", "voiage.*allemagne", "conte palatin" (all
   matches inspected): every hit is a coincidental filename/id/numeral (`labbe1582/segment_sweep.tsv`,
   `bethune/em_model_v2.json`, `sunyatsen/*.csv`, etc.) -- no shelfmark or content match to BnF fr.5761 in
   either repository.

Requests: WebSearch 4 queries. archive.org 6 be-api fts queries (Cordier, Motheaugroing, Salviati, "5761",
chiffre, Palatin/électeur palatin), ≥1.5s apart. github.com 2 shallow clones (shared with M35 above). No
credentials, no logins.

## Digitisation and key-leaf check (24 Sept 2026)

**Digitised: yes.** ark `btv1b52510561g`, found by a Gallica SRU query (`gallica adj "Français 5761"`,
after one transient reset and one retry) matching the exact catalogue title "Recueil de copies de lettres
et de pièces concernant." `tools/gallica_folio.py btv1b52510561g --folio 50` resolved the manifest cleanly
(460 canvases, 448 with folio labels; **canvas f103 = folio 50r, canvas f104 = folio 50v**; the manifest
flags an inconsistent offset and a duplicate label later in the volume around canvas f435-f438/folio
216r-v -- not relevant to folio 50).

**Key leaf confirmed by direct inspection: canvas f104 (folio 50v).** The image
(`images/canvas104_folio50v_key.jpg`) shows the heading "Chiffres des[quel]z l'on a [us]é durant [le]
voiage d'Allemagne, [faict] pour l'empire, deppartiz ainsi qu'i s'ensuit," matching the catalogue text
verbatim, followed by "A monsieur Cordier et [Sr] de la Motheaugroing," a substitution alphabet (symbols
for each letter, a-t or so), and the start of the per-correspondent code list (comte palatin, Trèves,
Brandebourg, and further names cut off at the image's bottom edge, continuing onto later leaves toward
folio 53 per the catalogue's stated span). Folio 50r (canvas f103, checked first) is still the tail end of
the Instruction (fol.46-50), in continuous prose, not yet the key -- consistent with the catalogue's
"Instruction... (Fol. 46-50)" / "Chiffres... (Fol. 50-53)" boundary falling mid-folio 50.

This item is a **plaintext key document**, not ciphertext -- "ciphertext present" does not apply to it the
way it does to M35. What was checked (per catalogue wording only, no canvas walk) is whether a companion
ciphered letter using this key survives in the same volume: **no letter in Fol. 54-172 is catalogued with
the word "chiffre"** (see Source section above) -- a catalogue-level negative, not a leaf-by-leaf one.

Requests this section: gallica.bnf.fr 1 SRU query (1 reset + 1 retry) + 1 manifest.json fetch + 2 image
fetches (f103, f104), all ≥2s apart, UA `cipher-lab research script (contact via repository)`. No
403/429/challenge seen.

## Verdict

**Open**, 24 Sept 2026. Six sources checked (web, print/calendars, cryptiana/cipherbrain, DECODE,
Bourdeau, Aymeloglu): no found-solved claim, no prior transcription or decipherment of this key list located
under this shelfmark, these names, or this embassy in any of them. Mignet's standard narrative (1886 ed.)
cites and paraphrases the same February 1519 instruction from a *different* archival copy (Archives
Nationales J 952) and never mentions a cipher for it -- real evidence the key itself has not been printed
by the one calendar source checked, not proof for every source. Not scored closed-negative: no cryptanalytic
attempt was made (this is a plaintext key-recovery target, not a ciphertext to break), so rule 3's
matched-control requirement does not apply. Confirmed digitised (ark `btv1b52510561g`) with the key leaf
pinned by manifest label (canvas f104 = folio 50v) and content-matched by direct inspection. The volume's own
Fol. 54-172 correspondence is a real, catalogue-level gap for finding a companion ciphertext (no "chiffre"
word in the finding aid for those items, but no leaf was opened to check for an unremarked cipher passage);
Desjardins Toscane and the Catalogue des Actes de François Ier were not queried this pass (a further gap,
shared with M35).

Stage-2 eligible on this verdict (`open`, six sources checked, per check-solved.md).

Update 15 Oct 2026 (ELEC-END): fr.5761 ff.172r-179v now read on both sides at 600 px. No copy with names in cipher, and Kluckhohn nr. 357/383 are not there (the versos of ff.165-171 and 180-182 are still unread). Next step: the fr.5756 census (ark btv1b60010927, still to be confirmed); see "## ELEC-END".

Update 15 Oct 2026 (ELEC-SRC): Kluckhohn's source lines read on the page image: nr. 357 is BnF **fr. 3897** (item 56 of its contents list, ark btv1b90096539, folio not given), nr. 383 is **fr. 5761** after all (folio not given; ff.165-182 already read without it). See "## ELEC-SRC".

## Key transcription, progress (24 Sept 2026, 14:00 UTC, written by the LANE G3 orchestrator)

Worker G (session_01VqKFDYvBPedSfydmRjbFWq, Sonnet) was interrupted at 13:59 UTC at about 1.9x its $4 cap, under the account's seven-day
rate-limit warning (no new workers anywhere). On disk: natives of the whole key, folio 50v-53v (canvases f104-f110, 1500 px,
images/manifest.json), and ONE blind pass, key_passB.tsv (319 rows: f104 38, f105 74, f106 43, f107 45, f108 39, f109 41, f110 39; sign
shapes described in words, no glyph atlas). Pass A was running in a subagent and was lost. No key.tsv, no grades: a single pass is grade M
throughout and is not a reading. Next (for a successor): build a glyph atlas for the alphabet signs first (.claude/briefs/transcription.md;
tools/glyph_atlas.py from the Salviati worker), then two atlas-coded passes of f104 only before the rest; reuse the natives on disk.

## Atlas and key f.104 (24 Sept 2026, LANE R4 D)

Built a shared glyph atlas over all seven key leaves (canvas104-110, folio 50v-53v) with `tools/glyph_atlas.py`
(segment/cluster/atlas), disk only, no fetches, reusing the natives worker G left on disk. `glyphs/segment_args.txt`
crops each page to its sign-bearing region (the alphabet row, the "Nulle" row and the correspondent/code list),
skipping only the ornate opening flourish some leaves carry. `mark-h 0.8`; k=60 signs / 16 marks with a deliberate
over-split, then targeted `--split` on the clusters whose f104 members visibly mixed more than one shape
(alphabet-row signs cluster tightly with each other by HOG features regardless of which letter they are) --
`s19,s2,s32,s47,s50,s49,s35` and a second round on the sub-clusters that were still mixed after the first split.
Verified reproducibility: `glyphs/build.sh` regenerates `clusters.tsv` byte-identical from the images on disk
(fixed seed).

**Labelling method.** Rather than judge each of the 89 post-split sign clusters from the pooled 7-leaf contact
sheets alone (name/word cursive and invented signs cluster together there in a way that is hard to eyeball), I
built a page-specific montage of f104's own members per cluster (crops cut from `glyphs/crops/f104.png` by
`signs.tsv` coordinates, not committed, regenerated by build.sh) and judged each of f104's ~57 distinct cluster
memberships directly against the leaf image. 35 clusters were coded K1-K35; the rest are plain script (names,
the a-z equivalence row, word fragments) or segmentation noise (underlines, serifs, split letter strokes) and
carry `_`. Clusters belonging to the families I confirmed as genuine invented signs on f104 (prefixes of
clusters 19, 2, 32, 47, 49, 50, 35, plus standalone clusters 13/48/51/58) were coded even where their only f104
member was a singleton after splitting; clusters where the f104 crop showed cursive letters or word blobs
(29, 44, 22, 1, 9, etc.) were left `_` even though some are large across the whole corpus.

**Known limitation, not resolved this pass**: `atlas.png`'s full-corpus exemplar list shows that some coded
clusters are not perfectly pure once exemplars from the other six leaves are pulled in -- K1 (cluster 13), K13
(2.0), K15 (2.2) in particular mix a plain-script word blob in among otherwise consistent invented-sign
exemplars, and K28 (49.1) reads mostly as a plain cursive "b" once its 11 members are seen together, though its
single f104 member matches a hook-shaped code sign on the image. This is a hazard of clustering across all
seven leaves by shape alone: a simple invented mark on one page and a common letter's cursive stroke on another
can land in the same HOG cluster. Every code used below was checked against f104's own crop directly, not
against the pooled atlas.png legend alone; a future pass extending the atlas to f105-f110 should re-split these
four before trusting them on another leaf. No merge pass was run to unify duplicate codes for the same real
shape (e.g. K3 and K12 are both "P"): harmless for reconciliation (each code still maps to one consistent
shape), just not tidy.

Files: `glyphs/{segment_args.txt,pages.json,signs.tsv,marks.tsv,clusters.tsv,bitmaps.npz,labels.json,atlas.tsv,
atlas.png,atlas_part1.png,atlas_part2.png,sheet_signs_00..04.png,sheet_marks.png,build.sh}`. `glyphs/crops/` and
`glyphs/debug_*.jpg` are regenerated by build.sh and not committed. Requests: 0 hosts (disk only, per brief).

LANE R4 orchestrator, 24 Sept 2026 15:47 UTC: worker D (session_01KvtMK21Ab1rzhyobtgTdv7) was interrupted at 15:45 at $8.69 against a $5 cap,
after the atlas and blind atlas pass A of f.104 (key_passA_atlas.tsv, 38 rows) were pushed; its pass B ran in a subagent and was lost.
Next: brief lane-r4-h (pass B with the atlas, reconcile, key.tsv).

## Pass B and key f.104 (24 Sept 2026, LANE R4 H)

Pass B (`key_passB_atlas.tsv`, 38 rows: 23 alphabet letters a-x plus an unresolved y/z, 4 Nulle marks, 10
correspondent-code lines), written blind (key_passA_atlas.tsv and the old key_passB.tsv were not opened until
after this file was committed and pushed), from the f104 line crops (`images/f104_L01..L14.jpg`) plus the leaf
overview (`images/f104_lines_debug.jpg`) and the shared atlas legend (`glyphs/atlas_part1.png`,
`atlas_part2.png`, `glyphs/atlas.tsv`). Method differs from a from-scratch-by-eye pass: for each f104 sign
position, `glyphs/signs.tsv` + `glyphs/clusters.tsv` + `glyphs/labels.json` (the atlas's own per-position
cluster-to-K-code mapping, already built and verified against f104 by worker D) was read to get the mechanical
K-code at that position, then checked by eye against the crop and the atlas legend image before being written to
the row; a handful of positions were re-judged by eye where the mechanical code looked wrong (e.g. Nulle mark 2,
flagged low-confidence against K1's known contamination). Correspondent names were read fresh from the crops
without reference to the catalogue's correspondent list, except where noted as a plausibility cross-check against
NOTES.md's Source section (Trèves, Brandebourg, Saxe -- duke of Saxony, Francisque). Two correspondent names
(lines 10 and 12) were not confidently read and are flagged `[name unclear]`.

**Reconciliation** (`recon_key/reconcile_key.py key_passA_atlas.tsv key_passB_atlas.tsv --out-dir recon_key`,
joins by (line, plain) with a positional fallback for the four same-labelled Nulle rows and a line-number
fallback for correspondent rows whose plain-text reading differs letter-for-letter between the two passes):
**36 rows paired, 1 agreeing on a non-blank sign_code (2.8%). Gate (>=80%) FAILS.** `recon_key/agreement.tsv`,
`recon_key/disagreements.tsv` committed.

**Confusion pairs / what actually happened**: this was not primarily a disagreement about which sign sits at a
position -- both passes read essentially the same line structure (23-ish alphabet letters, a 4-mark Nulle row,
10 correspondent-code lines, "Le conte palatin" / Brandebourg / Hongrie / Trèves-Treues / Poulongne-Poulougne /
Maguence-Mugance / a line-12 entry with three small repeated comma/loop marks that pass A reads as "&c." after
"Catholicque" and this pass reads as two of three loops partially matching cluster-19-family K-codes). The
disagreement is almost entirely in the **sign_code column**: pass A assigned codes from a careful per-position
by-eye judgement against the atlas legend and very often concluded no acceptable match ("UNLISTED", used for
about half the alphabet row and several correspondent codes, e.g. Trèves, France/Lempereur, Catholicque), while
this pass mostly took the mechanical K-code already sitting in `glyphs/labels.json` for that sign position,
which frequently disagreed with pass A's independent visual read even where both passes agree a sign is present
(e.g. plain `a`: A=UNLISTED/"asymmetric cross" vs B=K25; `e`: A=K24/"thin plus" vs B=K35; `x`: A=K23 vs B=K31;
Brandebourg: A=K19 vs B=K22; Hongrie: A=K17 vs B=K20). Where both passes independently found no atlas code at
all the row still counts as a disagreement here (differing empty/near-empty judgements are not a confirmed
match), which is conservative but appropriate given the gate is meant to catch exactly this kind of code-level
uncertainty. **Lesson for a successor**: reading the K-code straight from `labels.json` at a signs.tsv position
is not an independent check of the atlas -- it just re-states the atlas's own (admittedly imperfect, per worker
D's "Known limitation" section above) mechanical cluster labelling, and diverges sharply from a careful
per-position by-eye read. A real pass B/C on this leaf's alphabet row needs to judge each of the ~21-23 sign
shapes fresh against the crop, the way pass A did, not consult signs.tsv/clusters.tsv/labels.json at all except
as a legend of named shapes to choose among.

Per brief: gate fails, so no key.tsv and no settling pass this round. Files: `key_passB_atlas.tsv`,
`recon_key/reconcile_key.py`, `recon_key/agreement.tsv`, `recon_key/disagreements.tsv`. Requests: 0 hosts (disk
only). Cost: see ROOM.md done line / session metadata.

## Pass C and key f.104 (24 Sept 2026, LANE R4 L)

**Coverage (`recon_key/coverage.py`, disk only).** Scoped "the f104 sign boxes" to `glyphs/signs.tsv` line 1,
the alphabet cipher-sign row -- the one row of f104 that is unambiguously all invented signs with no plain
script mixed in (every other line pairs a cursive name with a single code sign, and signs.tsv has no per-box
flag separating the two, so a literal all-174-box coverage figure would mostly measure how much of the page
is cursive prose, not atlas coverage of the cipher). Of the 21 alphabet-row positions, 17 map through
`glyphs/clusters.tsv` + `glyphs/labels.json` to a named K-code: **81.0%, gate (>=70%) passes.** No atlas
expansion done this pass; this is a scoping choice, not a proof that every other cipher-relevant sign box is
covered (see the Mugance finding below for a case where a sign box is missing from signs.tsv entirely, which
no coverage-by-cluster figure can catch).

**Pass C** (`key_passC_atlas.tsv`, 37 rows: 23 alphabet letters a-x plus unresolved y/z, 4 Nulle marks, 10
correspondent lines), read independently against the shared atlas legend (`glyphs/atlas_part1.png`,
`atlas_part2.png`) and fresh high-resolution crops cut directly from `images/canvas104_folio50v.jpg` for this
pass (not the pre-cut `images/f104_L01..L14.jpg` line crops alone, which were too compressed for several
close calls). Caveat on "blind": per the common brief, NOTES.md itself (this file) was read before this pass,
and its "Pass B and key f.104" section above quotes several of pass A's and pass B's specific sign_code calls
(e.g. e=K24 vs K35, Brandebourg=K19 vs K22) -- true blindness to those specific comparisons was not possible
once this file was read as required. Where this pass's own crop-vs-atlas-legend judgement agreed with a
quoted call, that is noted as independent confirmation, not assumed; the sign_code column throughout was
written from the image and the atlas legend, never copied from either prior pass's tsv.

Two findings from working the image directly, beyond the per-row calls:
- **The Trèves code sign sits under signs.tsv line 4, not line 5.** `glyphs/signs.tsv` row `f104_04_010`
  (x=555,y=428) is the loop-stem-loop sign belonging to the "Treues" line (crop confirms it against K10's
  atlas exemplars closely); both prior passes filed the Trèves row under line 5 by hand-copying the key list's
  own layout, which is fine for the key.tsv output (matched by line number via `recon_key/majority_key.py`,
  not by signs.tsv row), but worth recording for anyone re-deriving positions mechanically from signs.tsv.
- **The Mugance code sign has no box in signs.tsv at all.** The actual sign (a vertical stem with a small
  rectangular box partway up and a curling foot, matching K34) sits at roughly x=555-620,y=495-560 on the
  f104 crop coordinates -- between the end of the "Muganro" name (positions 1-11) and signs.tsv line5 pos12
  (x=692), which is a separate small cursive loop/flourish immediately to the sign's right, not the code sign
  itself. The segmenter (`tools/glyph_atlas.py segment`) missed the sign as its own connected component; it
  was read here directly from the page image with a targeted crop, not through signs.tsv/clusters.tsv at all.
  This is a segmentation gap, not a labelling gap, and the line-1 coverage figure above cannot detect it (it
  only measures boxes that exist). A future extension of the atlas to f105-f110 should re-run `segment` with
  tighter connected-component parameters around similarly dense name+sign lines before trusting per-box
  coverage figures on those leaves.

**Majority key** (`recon_key/majority_key.py key_passA_atlas.tsv key_passB_atlas.tsv key_passC_atlas.tsv` ->
`key.tsv`; alphabet rows matched by letter, Nulle rows matched positionally within their line, correspondent
rows matched by line number since spelling of the cursive names differs pass to pass): **37 rows, grade H
(>=2 of 3 passes agree on the same sign_code, UNLISTED counting as an agreeing value) on 30, grade M
(no majority) on 7 -- h, q, r, v, y, z, and line 10's unclear-name correspondent.** Of the 37, 21 carry a
named K-code by majority (not UNLISTED/blank): a-h positions b,c,e,f,g,h(no majority),l,m,p,x on the alphabet
row, all 4 correspondent-line signs with 3-pass or 2-pass K-code agreement (Le conte palatin=K27, Treves=K10,
Mugance=K34, Brandebourg=K19, Saxe=K15, Poulougne=K14, Hongrie=K17, Francisque=K14), and 3 of 4 Nulle marks
(K26, K13, K31; the third Nulle mark's crop is too small/faint to read confidently and stays UNLISTED by
2-pass agreement). This closes the f104 dataset per the brief regardless of grade mix: every row has a
majority-backed sign_code (H or M) and a full three-pass audit trail (`note` column cites all three passes'
readings). No plaintext decode was attempted this pass (a substitution alphabet with roughly half its letters
still UNLISTED is not decodable text yet; that is a follow-up for a worker with the correspondent-list context
and, ideally, f105-f110 atlas coverage to cross-check the K-codes that recur across leaves).

Files: `key_passC_atlas.tsv`, `recon_key/coverage.py`, `recon_key/majority_key.py`, `key.tsv`. Requests: 0
hosts (disk only, per brief). Cost: see ROOM.md done line / session metadata.

## Key f.105-f.110 and letters to try (24 Sept 2026, LANE R5 D)

**Container note first.** A fresh `pip install numpy opencv-python-headless scikit-image scikit-learn Pillow`
in this container does **not** reproduce `glyphs/clusters.tsv`/`signs.tsv`/`atlas.tsv` byte-identically from
`glyphs/build.sh` (174 vs 184 f104 sign boxes, 26 vs 37 coded clusters) -- the same library-version hazard
LANE R5 worker A flagged for the Salviati atlas. Restored the seven committed files (`clusters.tsv`,
`signs.tsv`, `atlas.tsv`, `marks.tsv`, `atlas.png`, `atlas_part1/2.png`, `sheet_signs_00-04.png`,
`sheet_marks.png`, `bitmaps.npz`, `pages.json`) via `git checkout --`, keeping only the regenerated
`glyphs/crops/*.png` (grey per-page working copies, uncommitted, used for cropping exemplars below) and
`glyphs/debug_*.jpg`. All work below is against the **committed** atlas/clustering, unchanged; no reclustering
was attempted this pass, so `--split` boundaries are exactly as LANE R4 D left them.

**Atlas extension (box-level coverage, no reclustering).** The segmentation/clustering already spans all
seven leaves (`glyphs/segment_args.txt` always did); K1-K35 are cluster-family codes, not page-specific, so
most of "extending the atlas to f105-f110" turned out to already exist mechanically. Box-level coverage
(share of each leaf's sign boxes -- plain script and invented signs together -- already carrying a non-`_`
K-code via `clusters.tsv`+`labels.json`, computed from committed files only, no new labels):
f104 34/174 (19.5%, 28 distinct codes), f105 52/369 (14.1%, 26), f106 32/189 (16.9%, 17), f107 43/224
(19.2%, 18), f108 27/217 (12.4%, 18), f109 20/172 (11.6%, 10), f110 31/165 (18.8%, 18). Per worker L's f104
scoping note, this is a page-wide box figure (cursive prose and invented signs mixed, no per-box flag to
separate them), not a per-code-position figure -- useful as "does the shared codebook recur on this leaf at
all" (yes, on every leaf), not as "is every code sign on this leaf labelled."

**New-code search.** Listed every uncoded cluster (`signs_lab.get(cluster,'_')=='_'`) with >=3 members outside
f104 (52 clusters) and inspected all five contact sheets (`glyphs/sheet_signs_00..04.png`) plus a 2x zoom crop
of the strongest single candidate (cluster 45, 19 members, present on 6 of 7 leaves, `/tmp/cluster45_zoom.png`,
not committed). Every large uncoded cluster is spread near-evenly across all seven leaves in a pattern matching
ordinary cursive prose (repeated "m"/"n"/"L"/"S"/"o" letterforms, minim strokes, underlines, abbreviation
flourishes), consistent with worker D's own f104 judgment that these families are plain script, not invented
signs. Cluster 45's zoomed crop, the best candidate by shape and by leaf-spread, resolved on close inspection
to a cursive secretary-hand "h" ligature (fluid connected strokes, not the isolated geometric strokes the
confirmed K-codes show), not a new sign. **No new code minted this pass** -- a conservative call under budget
(each candidate needs page-context to confirm, i.e. is it standing alone at a code position or is it mid-word;
that check was not done for all 52, only the visually strongest ones). Left as a follow-up: clusters 29 (mixed
plain/possible-sign blob, already flagged ambiguous on f104) and 35.0/56 (modest, fairly uniform round shapes,
not clearly script but not confidently a sign either) are the next candidates for a worker with more budget to
crop and check in page context. The contamination already flagged for K1/K13/K15 (cluster 13/2.0/2.2 mixing a
plain-script blob into an otherwise consistent invented-sign cluster) is unresolved and unchanged; it was not
re-split (would require reclustering, unsafe in this container per the note above).

**Two atlas-coded passes, one leaf (f110, folio 53v, 39 rows in the existing `key_passB.tsv`).** Budget did not
allow more than one leaf at real per-row quality (see "what's left" below); f110 was chosen over the larger
f105-f109 for tractability, not leaf order. `key_passA2_atlas.tsv` and `key_passC2_atlas.tsv` (both new,
leaf-scoped, columns `leaf,line,section,plain,sign_code,note`) read the correspondent-name rows and the
alphabet row fresh from native crops cut directly from `images/canvas110_folio53v.jpg` (PIL crops of the
segmented region, not committed, `/tmp/f110_*.png`), checked against the atlas legend exemplars in
`glyphs/sheet_signs_00-04.png` already viewed for the new-code search above. **Caveat on "blind"**: both
passes were written in this one session with the same crops already in view, so true independence (as
between separate worker sessions) was not achieved -- pass C was written without opening
`key_passA2_atlas.tsv`, re-deriving each call from the images directly, but is not a fully independent
re-fetch. Flagged per the common brief's honesty requirement rather than presented as equivalent to LANE R4's
cross-session f104 passes.

f110's correspondent block is headed "Maistre [Jehan] de Bourdeaulx devers le marquis de Brandebourg" (read
directly off the page and confirmed against `key_passB.tsv`'s own independent free-text read of the same
name, and against NOTES.md's Source section, which already lists "François de Bordeaux (to the marquis de
Brandebourg)" among the key's correspondents) -- this is a **different correspondent's own alphabet+code
list** from f104's Cordier/Motheaugroing block, confirming the document assigns each negotiator their own
sign set rather than one shared alphabet (the same referent, e.g. "Saxe", gets a visually different sign on
f110 than whatever f104's block would assign it, so K-codes were matched by this leaf's own shape against the
atlas legend, never carried over by name from f104's rows).

`key_passB.tsv` (free-text, predates the atlas, no `sign_code` column) could not itself cast a majority vote,
so it is not the third voter the common brief's 2-of-3 language assumes: `recon_key/majority_key_leaf.py`
(new script) folds it in as a non-voting cross-check (its `cipher_desc` text carried into the `note` column)
and grades H where A and C's atlas codes agree (UNLISTED counting as agreeing, the same convention
`recon_key/majority_key.py` used for f104), M otherwise. Result: **38 rows appended to key.tsv, all grade H**
(34 on UNLISTED agreement, 4 on a named K-code: alphabet-row `h`=K27, Maguence=K34, Saxe=K20, Null4=K27) --
`key.tsv` now carries a `leaf` column (f104 rows backfilled to `leaf=f104`, unchanged otherwise) and 76 rows
total. The four named agreements are a real, if narrow, majority-backed reading: both passes independently
matched f110's Maguence sign to the same H-box shape as f104's Mugance=K34 (cluster 51), and f110's Saxe sign
to K20 (cluster 32.1, a small-circle-on-a-bar shape distinct from f104's Saxe=K15) -- i.e. the same referent
name gets a *different* code across correspondents' blocks, as expected. This is a real dataset result (rule
7: `recon_key/majority_key_leaf.py f110` regenerates these 38 rows deterministically from the two pass files
and `key_passB.tsv`, no key stage-checker script written this pass since there is no ciphertext to `--check`
against yet). Most of the leaf (34/38 rows) stayed UNLISTED by honest agreement, not by a forced code --
grade H here documents "both readers found no confident atlas match," not "the sign is unread."

Two names on f110 are worth a flag for a solving pass: line 12 "Roy [d'Angleterre]" (most likely Henry VIII
of England, plausible for a 1519 embassy with wide diplomatic reach) and line 13 "Madame Marguerite" (most
likely Margaret of Austria, governor of the Habsburg Netherlands) -- both read from the image directly, not
inferred from the catalogue's correspondent list (which does not name either). Lines 7-9's correspondent
names are lost to a torn top-left corner of the leaf (page damage, not a transcription failure); `plain` is
left `[name torn]` per rule 2 rather than guessed.

**What's left** (per brief, stopping before adding more leaves so this section can be written): f105
(74 rows, largest), f106 (43), f107 (45), f108 (39), f109 (41) still need their own pass-A2/C2 pair and a
`majority_key_leaf.py <leaf>` run -- each is the same shape of work as f110 above, at roughly the same
per-leaf cost. `recon_key/majority_key_leaf.py` is written generally (any leaf name) so a successor only
needs to write that leaf's two pass files and run it with `--migrate-header` omitted (already done once).

Files: `key_passA2_atlas.tsv`, `key_passC2_atlas.tsv`, `recon_key/majority_key_leaf.py`, `key.tsv` (migrated
to add a `leaf` column + 38 new f110 rows). Requests: 0 hosts (disk only, per brief). No subagents. Cost: see
ROOM.md done line / session metadata.

### Candidate companion-letter search (disk only, no fetches)

Grepped `QUEUE.md`, `CATALOG.md`, `sources/solver-diffs/*.tsv` and `sources/` directory listings for the
embassy's named correspondents (Bonnivet/Gouffier, Jean d'Albret d'Orval, président Guillart/Guillard, Louise
de Savoie, Joachim de Moltzau, François Ier to the electors) and fr.5761's neighbouring shelfmarks
(Français 2994, 3005, 3060; Dupuy; Clairambault volumes dated 1519-20). No captures, listing only.

**Real candidate: `ciphers/dupuy468-anhalt/` (QUEUE row M7, already on the board, not a new find).** BnF Dupuy
468, item 28 (canvas 64), a Latin letter to François Ier catalogued "orig., en latin, presque entièrement en
chiffres," dated 1515 or 1516 by the catalogue but re-attributed by a 23 Sept 2026 verifier pass to "more
probably Ernest of Brunswick-Lüneburg and **Joachim von Moltzan**, 1518/19" -- Moltzau/Moltzan is named
verbatim in M36's own key list ("Joachin de Moltzau, devers le marquis de Brandebourg," per the Source
section above and `sources/solver-diffs/2026-09-24-lane-g3-gallica6.tsv`). QUEUE.md already flags this cross-
reference (line ~452, M7's row) but as a lead for dupuy468-anhalt's own workers, not yet checked against M36's
key. A worker on that target could try M36's f104 or f110 K-codes against Dupuy 468 f.28's ciphertext once
enough of the key is coded. Status per QUEUE.md: `dupuy468-anhalt` is **partial**, not open -- a later hand
already glossed ~15-20 tokens interlinearly with Latin plaintext, so this is a transcription/collation job, not
blind cryptanalysis.

**Corroborating, not a fresh target:** `QUEUE.md`'s "Dropped this sweep" table (Archives Nationales pass) and
`sources/solver-diffs/2026-09-24-lane-n-fr-an.tsv` (row 27) both record "27 février 1519, Lettre en partie
chiffrée (et déchiffrée) de Joachim de Moltzan au chancelier de France Antoine Duprat..." (AN, Pièce n57) --
same correspondent, three days before the earliest king's-letter date in this volume's own Fol. 54 span (7 Feb
1519), catalogued as **already deciphered** ("et déchiffrée" in the finding aid itself), so not a solving
target, but real corroboration that Moltzau was actively sending ciphered correspondence in exactly this
embassy's window.

**Checked, no hit on disk:** Français 3005 (and the whole Français 3005-3993 "Recueil de lettres et pièces
originales" cluster) is on the board only as a wholesale-excluded noise cluster (`bourdeau-named:fr.3xxx`,
`sources/solver-diffs/2026-09-23-digitised-excluded.tsv`), not date- or correspondent-matched to this embassy.
Français 2994 and Français 3060 do not appear anywhere in `QUEUE.md`, `CATALOG.md`, `sources/solver-diffs/` or
any other cached file on disk -- nothing to report for either without a fresh catalogue fetch (out of this
brief's scope). No Dupuy or Clairambault volume on disk is dated or titled for 1519-20 specifically (Dupuy
452/468 are the two 1519-era Dupuy items already on the board, both covered above or already scored M6/M7;
no Clairambault volume in QUEUE.md carries an 1519-20 heading). Bonnivet/Gouffier, Jean d'Albret d'Orval,
président Guillart and Louise de Savoie produced no shelfmark hits anywhere searched -- the one "Gouffier" hit
on disk (`sources/solver-diffs/2026-09-23-non-decode-hits-excluded.tsv`, `2026-09-24-lane-g2-gallica5.tsv`) is
Claude Gouffier's own psalter (Ms-5095), an unrelated 16th-c. Gouffier, already dropped as a false positive by
the pass that found it.

**Tangential, same year, different embassy:** `ciphers/nla-heinrich-braunschweig-1519/` (QUEUE row DA7,
Niedersächsisches Landesarchiv L1 Nr.548/562, Duke Heinrich the Younger of Brunswick-Lüneburg, 1519 and 1522,
German) shares only the year, not a correspondent or the imperial-election context -- flagged for
completeness, not a real candidate.

No new QUEUE rows added (per brief: list only, do not capture or promote).

## Sign inventory (25 Sept 2026, LANE R8)

`sign_inventory.py` (disk only, regenerates `sign_inventory.tsv`) counts alphabet/code-name/null rows per
correspondent block from `key_passB.tsv` (the one free-text blind pass that covers all seven key leaves,
319 rows) and cross-checks which sign_code recurs for the same referent across the two atlas-coded,
3-pass-reconciled blocks in `key.tsv` (f104, f110 -- the only leaves with a majority-voted `sign_code`
column to compare).

**The document is not six correspondent blocks, it is eight.** f105 (folio 51v) is not one block: it
carries two full correspondent lists back to back, "A monsieur de Langsac" (23 alphabet + 7 names + 5
nulls = 35 rows) and immediately after it "A monsieur de la Boulade devers monsieur de Trèves" (23 + 11 +
4 = 38 rows) -- both already distinguished in `key_passB.tsv`'s own `correspondent` column, matching
NOTES.md's Source section, which separately names "Langjac" and "La Vernade (to Trèves)" among the key's
correspondents. So the leaf-to-block mapping is f104=1 block, f105=2 blocks, f106-f110=1 block each, eight
in total, not seven leaves = seven blocks.

| leaf | correspondent | alphabet | code/name | nulls | total | grade |
|---|---|---|---|---|---|---|
| f104 | Cordier & La Motheaugroing | 23 | 10 | 4 | 37 | H (key.tsv, 3-pass atlas-coded) |
| f105a | Langsac | 23 | 7 | 5 | 35 | M (single blind pass, not atlas-coded) |
| f105b | La Boulade / Trèves | 23 | 11 | 4 | 38 | M (single blind pass, not atlas-coded) |
| f106 | Lagnisay | 21 | 17 | 5 | 43 | M (single blind pass, not atlas-coded) |
| f107 | Joachim de Moltzan / Brandebourg | 23 | 18 | 4 | 45 | M (single blind pass, not atlas-coded) |
| f108 | duc de Saxe | 23 | 11 | 4 | 38(+1 heading) | M (single blind pass, not atlas-coded) |
| f109 | grand archidiacre / legate in Germany | 23 | 14 | 4 | 41 | M (single blind pass, not atlas-coded) |
| f110 | Bourdeaulx / Brandebourg | 23 | 12 | 4 | 39 | H (key.tsv, 3-pass atlas-coded) |

Full table with per-block notes: `sign_inventory.tsv`. Every block's alphabet row is close to 23 letters
(a-x/y, skipping j/u/w per the era's convention) -- f106's single blind pass counts only 21, a gap not yet
checked against the image (M grade, unreconciled). Every block also carries 4-5 null signs and its own
list of code-names for foreign electors/places/persons, so the design class is confirmed as **one
per-correspondent substitution alphabet plus a small nomenclator (code-names, not syllables or words),
repeated independently for each of the eight blocks** -- not a single shared cipher for the whole
document, and not a homophonic or polyalphabetic design at the letter level (no evidence of multiple
signs per letter in either atlas-coded block).

**Do blocks share signs?** Mixed, on the only two blocks with atlas-coded majority readings (f104,
f110): the code-name lists in both blocks name almost exactly the same referents (the Palatine elector,
Trier/Treves, Mainz, Brandenburg, Saxony, plus a "Francisque"/"Francisme" and a "Catholicque"/
"Catholicquer" line) -- expected, since every negotiator needed to refer to the same handful of German
electors and princes back to Paris -- but the **sign assigned to a given referent is not fixed across
blocks**: Mainz (f104 "Mugance."=K34, f110 "Maguence"=K34) happens to share the same sign, while Saxony
(f104 "Saxe"=K15, f110 "Saxe"=K20) does not. One match and one mismatch out of the two referents both
blocks resolved to a named K-code is not enough to call this "shared" or "independent" in general; the
other five shared referents (Palatine elector, Treves, Brandenburg, Francisque/Francisme, Catholicque)
are UNLISTED on f110's side and cannot be compared yet. This needs f105-f109 atlas-coded before it can be
answered for the document as a whole -- flagged as the next step for a worker extending the atlas past
f104/f110, not concluded here either way. This is consistent with, and adds one data point to, worker
D's 24 Sept finding (f110 section, above) that "the same referent name gets a different code across
correspondents' blocks."

Requests: 0 hosts for this section (disk only, `key_passB.tsv`/`key.tsv` already on disk). Files:
`sign_inventory.py`, `sign_inventory.tsv`.

## Pool search (25 Sept 2026, LANE R8, disk only)

Re-grepped `QUEUE.md`, `CATALOG.md`, `sources/solver-diffs/*.tsv` and `ciphers/*/NOTES.md` for each named
correspondent (Bonnivet, d'Orval, Guillart, Cordier, La Motheaugroing/Motheaugroing, Bourdeaulx, Joachim de
Moltzau/Moltzan), a superset of the 24 Sept sweep (adds Bonnivet, d'Orval, Guillart, not separately queried
then). One new hit not previously logged: `ciphers/fr2967-duprat/NOTES.md` names "Bonnivet" once, among a
list of clear-copy (not ciphered) letters to François Ier bound in the same recueil as that volume's Duprat
decipherments -- checked directly, not a ciphertext, not date-matched to this embassy, and that target is
itself `closed-negative`; excluded as a coincidental match, not a candidate.

The one real candidate is unchanged from 24 Sept: **`ciphers/dupuy468-anhalt/`** (QUEUE row M7, BnF Dupuy
468 item 28, ark `btv1b10035959t` canvas 64) -- a Latin cipher letter a 23 Sept 2026 verifier re-attributed
to "more probably Ernest of Brunswick-Lüneburg and Joachim von Moltzan, 1518/19," and Joachim de Moltzau is
named verbatim in this key's own f107 block ("Joachim de Moltzan tenant le marquis de Brandebourg"). Status
has changed since 24 Sept: `ciphers/dupuy468-anhalt/NOTES.md` line 1 now reads **`found-solved`** (23 Sept
2026), via the leaf's own pre-existing interlinear gloss, not via any key from this document -- so it is no
longer an open target this key could unlock, only a corroborating catalogue link (the same Moltzan was
active in exactly this embassy's window, and dupuy468-anhalt's cipher long predates fr5761's own key list,
which is undated internally but bound with 7 Feb - 18 Jul 1519 correspondence). No other 1519-1520
ciphertext under any of the seven named correspondents was found on disk or in the catalogues searched.

for the parent: fr5761 key 317 signs (8 correspondent blocks, sign_inventory.tsv); candidate letter
dupuy468-anhalt (BnF Dupuy 468 item 28, Joachim von Moltzan) -- already found-solved 23 Sept 2026 via its
own gloss, not via this key; no new candidate this pass.

## Web and blog check (GF-A2-3, account 2, 2 Oct 2026)

Queries run (plain web search), hit lists read, plausible hits opened:
1. `"Chiffres desquelz l'on a usé durant le voiage d'Allemagne"` (the key's own heading, quoted) -- no hit on the
   phrase (only modern tourism/statistics pages).
2. `"français 5761" chiffres élection impériale 1519` (shelfmark) -- Wikipedia and DHM pages on the 1519 election; no
   hit on the shelfmark or the key.
3. `François Ier élection impériale 1519 chiffre Bonnivet Orval Guillart lettres chiffrées ambassadeurs` (sender side
   + date) -- David Potter's calendar "Lettres de François Ier" on cour-de-france.fr (per-year PDFs and an index of
   recipients). Plausible (a calendar of the king's 1519 letters, the volume's Fol. 54-102). The 1519 PDF
   (`cour-de-france.fr/IMG/pdf/d._potter_-_lettres_de_francois_ier_-_1519.pdf`) answered HTTP 403 to a descriptive
   UA and to one retry with a browser UA after a pause; stopped (good-citizen rule). **Unreached** -- next: read it
   from a local browser (LOCAL-QUEUE) and grep for "5761" and "chiffre".
4. `1519 imperial election French cipher key nomenclator Cordier Motheaugroing Moltzan Bonnivet` (names in the key;
   also model-solve family) -- Rossignols, Charles V 1547 decipherment news, Cipherbrain's "The unsolved ciphers of
   Emperor Maximilian I" and a "Reading Maximilian's Mail" post (Habsburg side, not this French key); no page on this
   key.
Blog site searches: `site:cryptiana.blogspot.com 1519 election OR Bonnivet OR "Francis I"` (no Cryptiana blog page
returned; the 104 cached Tomokiyo pages were grepped earlier, see the top of this file); `site:scienceblogs.de
klausis-krypto-kolumne 1519 Franz I. Kaiserwahl Chiffre` (Cipherbrain pages returned: a 15th-century encryption,
Maximilian I's unsolved ciphers, Thomas Ernst / Ferdinand III -- none is this key); `site:ciphermysteries.com 1519
election cipher Francis` (one Cipher Mysteries page, ?p=9800, on 15th-century cryptography -- not this key). No
comment thread found discussing fr.5761 or this key list.

## Premise check (GF-A2-3, account 2, 2 Oct 2026)

The item is a plaintext key list (fol. 50v-53), so "already done" here means a prior transcription or printing of
the key, or a period decipherment that already applies it.
(a) Decipherments the folder already mentions -- **found (mentioned), unreachable.** The Pool search names an Archives
nationales piece, "27 fevrier 1519, Lettre en partie chiffree (et dechiffree) de Joachim de Moltzan au chancelier
... Duprat" (AN, piece n57; `sources/solver-diffs/2026-09-24-lane-n-fr-an.tsv` row 27). Moltzan holds one of this
key's blocks, so that period decipherment may be a known-plaintext check on the f107 Moltzan block. It is an AN
original, not viewed by this worker (archivesnationales/francearchives do not load from the cloud). It is not a
transcription of the key itself. Dupuy 468 item 28 (Moltzan, already `found-solved` via its own gloss) is the
other mentioned decipherment; it was read without this key.
(b) Other solvers' working files -- **not found.** Fresh clones of dbourdeau/cyphersolver (head 2341682) and
aaymeloglu/unsolved-ciphers (head d2800bb) grepped for "motheaugroing", "moltzau", "btv1b52510561g", "fr. 5761"/
"français 5761": no hit; the bare "5761" hits are image ids and digit runs (hcportal media 5761, Hessen key 19).
(c) Physical neighbours -- **partly found, nothing beside the key.** Canvases f103-f110 (fol. 50r-53v) are on disk
(images/); f103 is the end of the Instruction in prose. The volume's letters (Fol. 54-172) were checked by catalogue
wording only (no "chiffre"); no leaf walk of those folios for an unremarked cipher passage or a clear copy using the
key -- not done by this worker either.
(d) Recipient's side -- **not found / unreached.** The recipients are the German electors (Palatine, Trier,
Brandenburg, Saxony): no German edition (Deutsche Reichstagsakten, Jungere Reihe vol. 1, the 1519 election volume)
was opened by this worker; Mignet and Le Glay (French side) were read by full-text search (top of this file) without
the key. Next: a full-text search of Deutsche Reichstagsakten J.R. I for "chiffre"/"Ziffer" + Moltzan/Cordier, ~$1.

## While waiting (RUN4-WAITBF, 4 Oct 2026)

- Action that depends on nobody: the step pass (d) names -- a full-text search (archive.org be-api, Google Books API with country=US) of Deutsche Reichstagsakten, Juengere Reihe vol. 1 (the 1519 election volume) for 'chiffre'/'Ziffer' with Moltzan/Cordier, ~$1.

## R9-ELEC: Deutsche Reichstagsakten J.R. I full-text search (worker R9-ELEC, 6 Oct 2026, 06:25-06:35 UTC)

Search results only (rule 10); OCR text, not page images (rule 2: any negative is conditional on Google's OCR).
Volume: Deutsche Reichstagsakten unter Kaiser Karl V., J.R. Bd. I (Kluckhohn, Gotha 1893), archive.org
`bub_gb_0gFoAAAAMAAJ` (`_djvu.txt`, 3.16 MB; copies `bub_gb_6gcQAAAAYAAJ` and `deutschereichst10kommgoog` give
the same counts). Requests: archive.org 14 (advancedsearch 2, metadata 3, djvu downloads 6 incl. other-year volumes),
be-api 3, googleapis books 3; no 403/429.
Counts in vol. I OCR: "Moltz*" 241, "Cordier" 28, "chiffr*" 26, "Ziffer" 2, "Geheimschrift" 0, "Schluessel" 1 (unrelated:
Minute's key, Charles V's Lille letter), "5761" 50 (Kluckhohn prints many BnF F. fr. 5761 copies: "Aus Paris Bibl. nat. F. fr. 5761
(frueher de la Mure) Cop.").
Hits that matter (OCR offsets in the djvu text):
- 183024: Moltzan to Joachim, March 1518, "Orig. zum Teil chiffriert" (Berlin) -- Moltzan used a cipher.
- 1082557: Joachim's envoy with a "chiffrierten Briefe" for the king that the French cannot resolve.
- 2429009: Joachim to Francis I (June 1519), copy with "die Stichworte in Chiffren mit ueber-geschriebener Aufloesung"
  (Dresden) -- cipher words with interlinear solution, a possible plain-copy for a Joachim/Moltzan block.
- 2685183 and 2827217: BnF F. fr. copies (shelfmark OCR-garbled "Vom."/"VGL", probably 5761 or 5756; check on image)
  "die Namen in (den bekannten) Chiffren" -- the editor says names are cipher groups in the BnF copy, i.e. the
  fr.5761 key list is the key to them; Bonnivet/Guillart/Orval to Francis I, June 1519 (Wahl Karls).
- 1145143: Robertet to Bonnivet 4 Mar 1519, letters sent to the chancellor "pour translater et deschiffrer".
Not found: any printed edition or transcription of the key list itself ("Chiffres desquelz", "voiage d'Allemagne": 0 hits);
no "Ziffer" tied to Moltzan/Cordier (be-api "Ziffer Moltzan": 0 hits in this volume). Cordier appears only as a name.
be-api: "chiffre Cordier" 1 volume hit (this one); "Ziffer Moltzan" 0. Google Books (country=US, key): "Reichstagsakten Moltzan
Chiffre" 8 items, snippets all this volume (several reprints, 1962); "Ziffer Cordier Moltzan 1519" 0; "Chiffres desquelz"
3 items, none relevant (arithmetic 1670; BnF Catalogue general des mss francais 1902, no snippet).
Next steps (not run): (1) read the printed letters at offsets 2685183 and 2827217 on the page image and see whether the
BnF copy carries code groups that match key.tsv names (a plain-copy known-plaintext check, C grade); (2) the printed
fr.5761 letters of vol. I as cipher-group witnesses; (3) volume II/III (1520-21) not searched. Vol. I is a Kluckhohn
"Cop." for each BnF item, so the groups may be only partly retained.

## Keyhunt 7 Oct 2026 (KH2-A, LANE KH-2)

Unread fetchable siblings for key.tsv: 0. The fr.3092 "Memoire chiffre" leaves (f.101, f.103-104, f.107; Gallica btv1b10720612s
canvas 105, 107-108, 111), full-page symbol cipher near Langeac/d'Orval items of 1521, are already read by Lasry and Biermann
(2023; Tomokiyo GL.htm "De la Tremoille's(?) cipher"), and their signs look unlike the eight blocks here at sheet scale. The
fr.5761 ff.54-172 copies with names in cipher are printed with names resolved in RTA J.R. I (Kluckhohn 1893), so they are a
possible C-grade check of the name codes (no leaf walk yet), not unread text. Rows: `keyhunt/2026-10-07-KH2A.tsv`.

## D1A-SRCH2: context quotes for the R9-ELEC hits (8 Oct 2026, 06:15 UTC by date -u)

The search itself was done by R9-ELEC (6 Oct, above); not repeated. This pass re-fetched the same OCR (archive.org `bub_gb_0gFoAAAAMAAJ` `_djvu.txt`, 3,161,610 bytes, 1 request) to quote the hits in context. OCR text, not page images (rule 2); search results only (rule 10).
- 183024: "Moltzan an Joachim, d. d. ... die jovis post letare anno etc XVIII (Maerz 18). Orig. zum Teil chiffriert. Berlin."
- 1082557: "Soeben kommt ein Bote von Joachim zu Moltzan mit einem chiffrierten Briefe fuer den Koenig, den sie nicht aufloesen koennen."
- 2429009: "Kurfuerst Joachim an Koenig Franz ... Aus Dresden ... Cop. (die Stichworte in Chiffren mit ueber-geschriebener Aufloesung)" -- Joachim's own copy, no Moltzan/Cordier named in the passage.
- 2685183: "Aus Paris Bibl. nat. F. fr. [shelfmark OCR-garbled 'Von.'], die Namen in (den bekannten) Chiffren" -- Bonnivet's 18 June 1519 letter to Moltzan (header OCR garbled). 2827217: "Aus Paris Bibl. nat. F. fr. [garbled 'VGL'] Cop., die Namen im Chiffren" -- Orval, Bonnivet, Guillart to Francis I. Neither shelfmark reads 5761 in the OCR; to be checked on the page image.
- 1145143: Robertet to Bonnivet 4 Mar 1519: letters sent to the chancellor "pour translater et deschiffrer ce qui estoit en latin et chiffre"; note cites "F. fr. 5756".
Not found: the key list or any printed code-group table; no "Ziffer"/"Chiffre" next to Cordier. Vol. II/III not searched. Requests: archive.org 1 (first attempt returned 0 bytes with the descriptive UA, one retry with a browser UA succeeded). Status unchanged.

## D1A-SRCH2: further print search (8 Oct 2026, 06:15 UTC)

D2-VIEU (5 Oct) and R9-VIEU (6 Oct) already ran print_check.py on the named phrases and variants; not repeated. This pass tried the next step they named, Google Books API (country=US, key) and be-api, on the two catalogue volumes and the Nevers volume: HQo4AQAAMAAJ, JUgMAQAAMAAJ, GP9eAAAAcAAJ are ALL_PAGES (full view) but the API returns no snippet inside them (the "30 septembre 1587 Vieuville" query lists HQo4AQAAMAAJ and JUgMAQAAMAAJ with an empty snippet); dsInahmnar8C (Les ducs de Nevers et l'Etat royal, 2006) is PARTIAL. Query "Vieuville Saint-Aignan 1587 Nevers": 18 volumes, top 5 are 1842 encyclopedia lists of dukes (noise); be-api same terms: 10 volumes, genealogical/Breton armorial noise. Not found: any printed text of the 30 Sept 1587 letter. Not done: page reading of the full-view catalogue volumes (books.google page view is blocked from the cloud; needs the owner's machine or an IA copy). Requests: googleapis 6, be-api 1. Status stays blocked.

## ELEC-WALK: name-code plain-copy walk, census (worker ELEC-WALK, LANE DEFAULT-A4-0235-15, account 4, 15 Oct 2026, 03:06-03:12 UTC by date -u)

Brief: walk the fr.5761 copies whose names are in cipher, pair (group, printed name) against Kluckhohn, RTA J.R. I. Result: **0 pairs; key.tsv
unchanged.** No score was computed, so no PREREG file was written. Rows: `namewalk_elecwalk.tsv` (12 census canvases). Images stay in the
session scratchpad; the regen URL is in the TSV header.
- Kluckhohn (IA `bub_gb_0gFoAAAAMAAJ` djvu, 1 archive.org request) flags only **two** copies "die Namen in (den bekannten) Chiffren": nr. 357
  (Joachim of Brandenburg, signed "Capitaine Josyn", to Bonnivet and Moltzan, 18 June 1519, printed names Couloigne, Saxe, Boheme, Mayence,
  Palatin, Hessen) and nr. 383 (Orval, Bonnivet, Guillart to Francis I from Coblenz, late June 1519, printed names Brandebourg, Treves, conte
  Palatin). Their shelfmark OCR reads "F. fr. Von." and "F. fr. VGL", not 5761. All the other ~45 "F. fr. 5761 Cop." source lines in vol. I
  carry no cipher note. So the brief's premise that ff.54-172 hold many name-cipher copies does not hold as stated. Kluckhohn names two letters.
- Census (openapi.bnf.fr, 12 requests at 600 px): f.172r ends "Escript a Nancy le x.. jour de juing", so the late-June 1519 letters lie
  **after** f.172. ff.172-179 are copies of the admiral's letters (to Madame, to the Palatine's chancellor, Brandenburg's letters "translatez en
  francoys"). ff.180r and 182r are blank, and ff.184 onward are later Italian matters. On all 9 written leaves the names are in clear
  (Brandebourg, Mayence, Saxe, Boheme, Poulongne, Treves, conte palatin, Joachim de Moltzan, Francisque, La Poussiniere). Two native line crops
  (f.174r, f.178r; 2 more requests, 14 in total) confirm the names are in letters, so a single cipher sign in place of a name would show at this scale.
- Not found: any leaf with a cipher name group on the 12 canvases checked; nr. 357 or nr. 383 on those canvases.
- Not checked: canvases f348-f350, f352-f356, f358, f360-f362 (ff.172v-179v, the unsampled sides of the June run, about 13 canvases),
  and ff.54-164 apart from the 4 sampled leaves. Possibly the two Kluckhohn letters are not in fr.5761 at all ("Von."/"VGL"; fr.5756 is the
  other BnF volume he cites for this embassy, e.g. Robertet 4 Mar 1519).
- Next: (1) read the remaining ff.172v-179v canvases at 600 px (about 13 requests, ~$1) for nr. 357/383. If they are absent, (2) the same census
  on fr.5756 (Gallica ark not yet looked up), ~$1.5. A match then needs >= 2 occurrences per sign before any C grade (brief rule). Status unchanged (open).

## ELEC-END: ff.172v-179v and the fr.5756 ark (worker ELEC-END, LANE DEFAULT-A1-0447-15, account 1, 15 Oct 2026, 05:01-05:12 UTC by date -u)

Brief: ELEC-WALK's next (1), reading the unsampled sides of ff.172v-179v at 600 px for Kluckhohn nr. 357 / nr. 383. If both are missing, look up the
fr.5756 ark only. Result: **0 cipher name groups; nr. 357 and nr. 383 are not on these leaves; key.tsv unchanged; status unchanged (open).**
- Read 12 canvases (f348-f350, f352-f356, f358, f360-f362; ELEC-WALK's "about 13" was 12 by its own list), openapi.bnf.fr 600 px, 12 requests,
  all 200. Images are in the session scratchpad only; rows are appended to `namewalk_elecwalk.tsv`, whose header holds the regen URL.
- ff.172v and 179v are blank. ff.173r-179r copy the admiral's own letters: to "Cappitaine Francisque" (173r, headed "Voiage d'Allemaigne pour
  l'empire"), the end of the letter to Madame (174v), to duc Federic de Baviere (175r), to the conte palatin (175v, 176v, 178v), and to the
  Palatine's chancellor (178v-179r). The run ends on 179r with "... jour de Juillet 1519". Every name on these pages is written in letters:
  Francisque, conte palatin, Robert de la Marche, la Motheaugroing, Baviere, Brandenbourg, roy catholique, bailly de Caen.
- Nr. 357 (Joachim of Brandenburg, signed "Capitaine Josyn", 18 June) and nr. 383 (Orval, Bonnivet and Guillart to Francis I, from Coblenz)
  do not match any letter here. None of these letters is from Joachim, and none is addressed to the king. With ELEC-WALK's canvases, ff.172r-179v are
  now read on both sides. ff.165-171 and 180-182 are read on the rectos only (ELEC-WALK). None of these pages has a cipher sign standing for a name.
- fr.5756 ark (1 request, Europeana Search API, quoted query "Français 5756"; the brief allowed one SRU or catalogue request, and
  gallica.bnf.fr is excluded this wave): the only hit is **ark:/12148/btv1b60010927** (gallica.bnf.fr/ark:/12148/btv1b60010927),
  "Recueil de plusieurs pièces concernant la pretension du roy François Ier à l'empire. Copies de la main de Florimond Robertet ? 1519".
  The contents in its description include letters from Orval, Bonnivet and Guillard "au roi", Bonnivet to Robertet ("datée de Coblentz,
  8 juillet") and Francis I to Brandenburg. That is the right group of correspondents for nr. 383. The response does not show the shelfmark
  itself, so the ark rests on Europeana's match to the quoted phrase. Confirm it on the BnF record before the census. The fr.5756 census was
  not started (per the brief).
- Not checked: the versos of ff.165-171 and 180-182 and f.181r; ff.54-164 of fr.5761 apart from ELEC-WALK's 4 sampled leaves; fr.5756 itself.

**Verdict (ELEC-END, 15 Oct 2026):** open, unchanged. No copy with names in cipher on fr.5761 ff.172r-179v (both sides) or on the rectos ELEC-WALK read in ff.165-182. Next:
(1) confirm that btv1b60010927 is fr.5756 from its manifest or BnF record (1 request), then census it at 600 px for nr. 357 / nr. 383 (about
15-25 requests, ~1.5). A pair needs >= 2 occurrences per sign before any C grade.

## ELEC-5756: fr.5756 census for Kluckhohn nr. 357 / nr. 383 (worker ELEC-5756, LANE DEFAULT-A1-0447-15, account 1, 15 Oct 2026, 05:35-05:4x UTC by date -u)

Brief: ELEC-END's next step. Confirm that ark btv1b60010927 is BnF Français 5756, then census it at 600 px for Kluckhohn nr. 357 and nr. 383 (names in
cipher). Result: **the ark is fr.5756. Neither letter is in it by the catalogue's contents list, and none of the 16 canvases read has a cipher name
group. 0 pairs; key.tsv unchanged; status unchanged (open).**
- Shelfmark (1 request, openapi.bnf.fr IIIF Presentation v3 manifest, 200): label "BnF. Département des Manuscrits. Français 5756"; Cote the same;
  title "« Recueil de plusieurs pièces concernant la pretension du roy François Ier à l'empire ». Copies de la main de Florimond Robertet ? 1519";
  "Papier. - 44 feuillets écrits"; catalogue record archivesetmanuscrits.bnf.fr/ark:/12148/cc58704x. 118 canvases; ff.1r-45v are canvases f15-f104
  (canvas = 2 x folio + 13 for rectos). Europeana was not needed (0 requests).
- Contents (the manifest's Description, 90 items): items 1-35 are letters of Francis I, Orval, Bonnivet and Guillart (Feb-July 1519), items 36-84
  Robertet to Bonnivet (Feb-July 1519), items 85-90 the Latin and French powers. The list has **no letter from Joachim of Brandenburg or
  "Capitaine Josyn" (nr. 357, 18 June)**. It also has **no Orval-Bonnivet-Guillart letter to the king from Coblenz (nr. 383)**. Their only
  joint letter to the king is item 8, from Nancy, 14 April. The Coblenz piece (item 31, 8 July) is Bonnivet alone to Robertet.
- Census (openapi.bnf.fr, 16 canvases at 600 px, all 200; rows in `census_elec5756.tsv`, images in the session scratchpad, regen URL in its header):
  ff.1r, 3r, 5r, 7r, 9r, 9v, 10r, 10v, 11r, 11v, 12r, 12v, 13r, 15r, 17r, 19r. These cover items 3-35 at least in part and the first Robertet leaves. Every
  name on them is in letters: bailly de Caen, marquis de Bade, roy de Poulongne, Boheme, conte palatin, duc Guillaume de Baviere, Marigny,
  Strasbourg, roy catholique, Gueldres, Magence/Mayence, Brandebourg, Treves, Couloigne, Francisque, Bazoges. No cipher sign stands for a name
  on these pages. Items 29-31 (f.10v, the Coblenz letter) and 34-35 (f.11v, Francis I to Brandenburg, 18 March, and a letter to an elector) were
  read in full at sheet scale. None of them matches nr. 357 or nr. 383.
- Not checked: ff.1v-2v, 3v-4v, 5v-6v, 7v-8v, 13v-14v, 15v-16v, 17v-18v, 19v and ff.20r-45v (the remaining Robertet letters and the powers), which
  is about 70 canvases. They are not where the catalogue places either letter. Prior-work tool (`prior_work.py --item-spec ... --step-type read
  --offline`, exit 4): its LEAD is this job's own claim, and the rest are generic UNCHECKED rows (Tomokiyo and solver caches by unit, editions)
  that a shelfmark census does not reach.
- Kluckhohn's shelfmark OCR "F. fr. Von." / "F. fr. VGL" now fits neither fr.5761 (ELEC-WALK, ELEC-END) nor fr.5756 (this census) for these two
  letters. Requests: openapi.bnf.fr 17, api.europeana.eu 0.

**Verdict (ELEC-5756, 15 Oct 2026):** open, unchanged. fr.5756 = btv1b60010927, confirmed from the manifest. Nr. 357 and nr. 383 are not in its
contents list, and no cipher name group was seen on 16 canvases. Next: (1) read Kluckhohn's own source line for nr. 357 and nr. 383 on the RTA
J.R. I page image, not the OCR (archive.org `bub_gb_0gFoAAAAMAAJ`, 1-2 page requests, ~0.5), to get the real shelfmark. "Von."/"VGL" may be
another fonds, such as Dupuy, Clairambault or a nouv. acq. volume. Census that volume only once the shelfmark reads from the page.

## ELEC-SRC: Kluckhohn's own source lines for nr. 357 and nr. 383 (worker ELEC-SRC, LANE DEFAULT-A1-0740-15, account 1, 15 Oct 2026, 08:02-08:1x UTC by date -u)

Brief: ELEC-5756's next (1), read the source line on the RTA J.R. I page image, not the OCR. Result: **both shelfmarks now read from the page;
0 pairs; key.tsv unchanged; status unchanged (open).** Page images, not OCR (rule 2); search results only (rule 10).
- Pages: archive.org `bub_gb_0gFoAAAAMAAJ`, `_page_numbers.json` gives leaf = printed page + 8. Nr. 357 heads on p.813 (leaf n821), nr. 383 on
  p.855 (leaf n863); a first try at n822/n864 landed one page late (pp.814, 856, the letter bodies).
- **Nr. 357** (Joachim of Brandenburg to Bonnivet and Moltzan, 18 June 1519), read by eye at 1800 px: "Aus Paris Bibl. nat. F. fr. **3897**. Cop.,
  die Namen in (den bekannten) Chiffren, in verso: Double des lectres du marquis de Brandebourg à monsr. l'admiral, 18e juing." The OCR's
  "Von." is 3897. Not fr.5761 or fr.5756, which is why ELEC-WALK, ELEC-END and ELEC-5756 did not find it.
- **Nr. 383** (Orval, Bonnivet and Guillart to Francis I, Wahl Karls, 29 June 1519): "Aus Paris Bibl. nat. F. fr. **5761**. Cop., die Namen in
  Chiffren." The OCR's "VGL" is 5761. So nr. 383 is in fr.5761 after all, but not on ff.165-182 (rectos, ELEC-WALK) or ff.172-179 (both sides,
  ELEC-END). Kluckhohn gives no folio for either letter.
- fr.3897: ark **btv1b90096539** was already on file (KEYHUNT-2026-10-07.tsv: fr.3897 f.222 = c263, f.236 = c279, f.238 = c281-283; Dupuy 468
  translation at f.146-147), so no SRU or catalogue lookup was needed. One request to the openapi.bnf.fr IIIF v3 manifest (200; label
  "BnF. Département des Manuscrits. Français 3897"; 314 canvases, every canvas label "NP"; "Numérisation effectuée à partir d'un document
  de substitution", i.e. from a substitute copy such as microfilm). Its Description lists **item 56: "Double des lettres d[e JOACHIM], marquis DE
  BRANDEBOURG, à monseigneur l'admiral de Bonnivet. XVIIIe jung 1519"**, which matches Kluckhohn's "in verso" line. Item 39 (Joachim to Bonnivet,
  "Vendredi, une heure apres midi, 1519") is Kluckhohn's nr. 356 (Josyn), printed just before it on p.813. Other Joachim pieces: items 36-38, 62,
  64-65, 73. The Description gives no folios. Item 73 is f.146 (Dupuy 468 work), so item 56 lies before f.146.
- No canvas of fr.3897 was read: Kluckhohn cites no folio, the canvas labels give none, and the brief forbids a census.
- Not done: locating item 56's canvas; the fr.5761 manifest Description (does it list nr. 383 with a position?); ff.54-164 of fr.5761.
- Requests: archive.org 6 (`_djvu.txt` 1, `_page_numbers.json` 1, page images n822, n864, n821, n863 at w1800), openapi.bnf.fr 1 (manifest),
  no 403/429. Images in the session scratchpad only, none in git. Regen: `https://archive.org/download/bub_gb_0gFoAAAAMAAJ/page/n821_w1800.jpg`
  (and n863); the source lines lie at about y 1940 (n821) and y 1820 (n863) of the 2500 px wide image.

**Verdict (ELEC-SRC, 15 Oct 2026):** open, unchanged. Nr. 357 = BnF fr.3897 (item 56, digitised, btv1b90096539); nr. 383 = BnF fr.5761 (digitised,
btv1b52510561g), outside the leaves read so far. Next: (1) locate fr.3897 item 56 by bisection from the f.146 anchor (item 73) and the
c263/f.222 offset, about 3-4 canvases at 600 px, then read the name groups against Kluckhohn's printed names (Couloigne, Saxe, Boheme,
Mayence, Palatin, Hessen; p.813-814), ~2; (2) read the fr.5761 manifest Description (1 request, no image) for the position of nr. 383, then
read that leaf, ~1.5. A pair needs >= 2 occurrences per sign before any C grade.

## ELEC-357: fr.3897 item 56 located and read for name signs; fr.5761 position of nr. 383 (worker ELEC-357, LANE DEFAULT-A1-0740-15, account 1, 15 Oct 2026, 08:37-08:4x UTC by date -u)

Brief: ELEC-SRC's next (1) and (2). Result: **nr. 357 found at BnF fr.3897 ff.116r-117r (canvases f142 right page, f143). It carries
non-letter signs in place of names. 0 pairs, because Kluckhohn's printed text was not available to this job (archive.org was not in its
host list). key.tsv unchanged; status unchanged (open).** Page images, not a transcription (rule 2). Search results only (rule 10).
- Prior work: `prior_work.py fr5761-election-1519 --item-spec 'BnF fr.3897 ff.116r-117r item 56 (Kluckhohn RTA J.R. I nr. 357)'
  --step-type read --offline`, exit 4. These are generic rows: LOOK 2-leaf (look.tsv crops owed for fr.5761, not this leaf), UNCHECKED
  3-tomokiyo/3-solver (the unit had no folio when the spec was written), UNCHECKED-NET 3-solver/4-editions. No specific hold.
  The edition for this letter is Kluckhohn RTA J.R. I nr. 357 itself (p.813-814, ELEC-SRC).
- Locating the item (fr.3897 = btv1b90096539, every canvas label "NP"). The canvases are openings (verso left, recto right), and the folio
  numbers are on the rectos. Anchors read by eye: c128 = f.103 (German original with an address leaf; item 51, Berne), c136 = f.112 (the Calais
  ambassadors, item 54: "roy catholique", "la fille du roy d'Angleterre", "monsr le dauphin"), c140 = f.115, c143 = f.117, c150 = f.123 (the
  left page heads "Coppie de la promesse ...", the Mayence items 58-61). The canvas-folio offset grows from 25 (c128) to 26 (c142) and 27 (c150),
  and it is 41 by f.222 (KH1A).
- **Item 56 = ff.116r-117r.** f.116r (c142 right) opens "Treschiers bons amys Capitaine Jacob et Hans ...". f.117r (c143 right) ends
  "... adieu. Datt. la veille de [saint day, not read] ... 1519" and is signed "Capitaine Jos[yn]", which matches Kluckhohn's "Capitaine Josyn"
  for nr. 357. f.117v (the endorsement "Double des lectres du marquis de Brandebourg ...") was not fetched, since it was not needed for the identification.
- **Name signs (eye inventory at 2400 px per opening, about 1100 px per page; one reader, grade M, no C or H).** These are isolated non-letter
  signs set into the French prose. The common "que" abbreviation sign is excluded.
  W-like sign: f.116r about 3 times, f.116v about 3 times (>= 6 in all). Double loop "δδ": f.116r 2, f.116v 2 (>= 4). "Z": f.116r 1,
  f.116v 2 (>= 3). Barred I "‡": f.116r 3. Triple-barred "#": f.116r 2, f.116v 1 (3). "4"-like sign: f.116r 2. "II": f.116r 1. A filled loop
  at the end of f.116v line 1: 1. That makes about 7-8 distinct signs. Kluckhohn prints six resolved names for this letter (Couloigne, Saxe,
  Boheme, Mayence, Palatin, Hessen; ELEC-WALK), so the counts are of the same order. On f.117r there is no name sign (the strokes before "1519"
  belong to the date).
  Shape check against key.tsv (descriptions only, not scored): the fr.5761 f.110 key describes Palatin as "#" with a hook, Maguence as a double
  hash "HH", Brandebourg as "Λ" and Saxe as a circle on a dash. The f.116 set (W, δδ, Z, ‡, triple #, 4, II) does not visibly reuse the
  Λ or the circle-on-dash signs. Whether "den bekannten Chiffren" means the fr.5761 key cannot be settled until the signs are paired with the printed names.
- Not done: the pairing itself, which needs Kluckhohn p.813-814 page images (archive.org `bub_gb_0gFoAAAAMAAJ` leaves n821-n822,
  2 requests). A pair is a sign at a position whose printed word is a name. A C grade needs >= 2 occurrences per sign (brief rule), and on
  these counts W, δδ, Z, ‡ and # could reach it. No crops were cut and no PREREG was written, because no score was computed.
- **fr.5761, nr. 383 (1 request, IIIF v3 manifest of btv1b52510561g, 200).** The Description places section 3 as follows: the key "Chiffres
  desquelz ..." at fol. 50-53. (a) The king's letters to Orval, Bonnivet and Guillart (7 Feb - 5 Jul 1519; f.77v named). (b) "Responces au
  roy durant ledict voyage", dated "... de Coblentz, du 14 mai au 29 juin ; de Nancy, du 4 au 18 juillet 1519". (c) "Voiage d'Allemaigne
  pour l'empire. A plusieurs Srs particuliers", which begins at f.173r (ELEC-END). So nr. 383 (Orval, Bonnivet and Guillart to the king,
  Coblenz, 29 June) is **the last Coblenz reply in run (b)**. It comes just before the Nancy July replies, which end on f.172r (ELEC-WALK). The
  Description gives no folio for it. It lies before the Nancy run, inside ff.54-172, and most likely in the f.150s-160s. ELEC-WALK read only
  the rectos of ff.165-171 and saw names in clear there. No canvas was read (brief: no census).
- Requests: openapi.bnf.fr 9 (fr.3897: c150, c136, c128, c140, c143 at 600 px; c143 and c142 at 2400 px; manifest 1; fr.5761 manifest 1),
  all 200, no 403/429. Images are in the session scratchpad only, none in git. Regen:
  `https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b90096539/f142/full/2400,/0/default.jpg` (and f143).

**Verdict (ELEC-357, 15 Oct 2026):** open, unchanged. Nr. 357 = fr.3897 ff.116r-117r, with about 7-8 name signs (M, by eye). Nr. 383 =
fr.5761 section 3(b), the last Coblenz reply (29 June) before the Nancy July run that ends on f.172r. Next: (1) fetch Kluckhohn p.813-814
(archive.org n821-n822, 2 requests) and pair the f.116r-v signs with the printed names, using two blind passes on line crops of c142 and c143
(about 4 units plus 1 reconciliation, ~3.5). (2) Find nr. 383 by bisection from f.172r backwards (canvas = 2 x folio + offset; read the
fr.5761 offset from ELEC-WALK's census rows), about 3-4 canvases at 600 px, ~2. A pair needs >= 2 occurrences per sign before any C grade.

## ELEC-PAIR: nr. 357 name signs vs Kluckhohn's print (worker ELEC-PAIR, LANE DEFAULT-A1-0740-15, account 1, 15 Oct 2026, from 09:1x UTC by date -u)

**Pre-registered pairing rule (written and pushed before any sign-to-name pairing was made; Kluckhohn pp.813-814 page images fetched
but not yet read against the manuscript).**
1. Unit: one isolated non-letter sign in the French prose of fr.3897 ff.116r-117r (canvases f142 right page, f143), the "que"
   abbreviation excluded (ELEC-357's inventory). Signs are named by shape label only (W, dd, Z, barI, hash3, 4, II, loop); no key value
   is shown on any crop or attached to a label before pairing (value-free).
2. A sign occurrence pairs with a printed name only where the clear French context on BOTH sides of the sign (at least one full clear
   word left and one full clear word right, read on the manuscript) matches the words on both sides of a name in Kluckhohn's printed text
   of nr. 357 (spelling-normalised: case, u/v, i/j, accents, abbreviations expanded). One-sided matches are recorded as "one-sided", not pairs.
3. A sign gets grade C (rule 4) only if >= 2 of its occurrences pair, all with the same printed name, and none pairs with a different
   name. One paired occurrence = M. Conflicting pairings = logged as a conflict, no grade.
4. Control (shuffled names): the printed names at the paired slots are permuted 1000 times over those slots; report the share of
   permutations under which every C-graded sign would still read one name consistently across its occurrences (the chance that rule 3
   passes with names assigned at random). A sign whose consistency the shuffle reproduces at >= 5% is held at M.
5. Comparison with key.tsv (fr.5761 ff.50-53 key) is made only after rules 1-4 are applied and written down.

**Result (ELEC-PAIR, after the rule above was pushed in 23615ec36).** Sources: Kluckhohn RTA J.R. I nr. 357, pp.813-815 page images (the letter
runs onto p.815, ending "Capitaine Josyn"; archive.org `bub_gb_0gFoAAAAMAAJ` n821, n822, n823 at w1800), against fr.3897 ff.116r, 116v
(btv1b90096539 f142 right half, f143 left half, 2400 px), read by one reader (this worker) on the page images and on value-free strip crops;
f.117r not re-read (ELEC-357: no name sign there). The French copy follows Kluckhohn's print word for word except at the signs.
- **17 both-sided pairs, 0 conflicts** (`elecpair/pairs.tsv`, one row per sign slot with the manuscript words either side and the print line).
  Grades (`elecpair/name_signs_fr3897.tsv`): **W = le roy tres-chrestien, C (6 pairs; shuffle 0/1000)**; **dd = le roy catholique, C
  (4 pairs, two of them the Latin "rege catholico" / "rex catholicus"; shuffle 8/1000)**; barI = Boheme, M (2 pairs, but shuffle 167/1000
  >= 5%, held at M by rule 4); 4 = Palatin, M (2 pairs, shuffle 176/1000); II = Couloigne, Zheavy = Saxe, flag = Mayence, M (1 pair each).
  Joint control: all four >= 2-pair signs consistent in 0/1000 shuffles (`python3 elecpair/pair_control.py --check`, seed 357, exit 0).
- Unprinted slots (a sign where Kluckhohn prints no word): hash3 x3 (f.116r l.5 "persuasion # luy ay"; l.6 "promission pro # fre de castro";
  f.116v l.2 "quatuor # pro"), a filled loop (f.116v l.1 "seur pour [loop] quatuor"), one barI (f.116r l.27 "prouchain, barI je besoigne")
  and a struck hash-like sign at the head of f.116v's last line ("car en verite [sign] je y mets"). So hash3 is not a name sign on this
  evidence (abbreviation, null or a word Kluckhohn left out: not settled).
- Corrections to ELEC-357's eye inventory: its f.116v "Z" x2 are the light cursive par-abbreviation ("me l'envoyez par ce porteur", "non
  moins que par avant"; Kluckhohn prints "par" at both), not the heavy Z (Saxe, f.116r only). Hessen and Meance are written in clear on
  f.116v, as Kluckhohn prints them; the six names ELEC-WALK listed are not all ciphered here, and the two kings are.
- Rule 5 comparison with key.tsv (fr.5761 ff.104/110 key), by description only (no key image re-read): Saxe there is a circle on a dash
  (here a heavy Z), Maguence a double hash HH (here a flag), Catholicque a cross with a small circle (here a double loop), Palatin a hash
  with a hook (here a 4-like sign with a cross-bar, the nearest of the four). On these descriptions the fr.3897 nr. 357 name signs are not
  the fr.5761 key's; "den bekannten Chiffren" in Kluckhohn's source line then points to signs he knew from other letters, not to that key.
  This is M (descriptions against one reader's eye), not an image-to-image comparison.
- Requests: archive.org 3 (n821, n822, n823 w1800), openapi.bnf.fr 2 (f142, f143 full/2400), all 200. Images and crops in the session
  scratchpad only, none in git. sha1: n821 a58ed4a8..., n822 719e2ed8..., f142 b1d18f00..., f143 52d1ec7c.... Regen:
  `https://archive.org/download/bub_gb_0gFoAAAAMAAJ/page/n82{1,2,3}_w1800.jpg`;
  `https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b90096539/f14{2,3}/full/2400,/0/default.jpg`; f.116r = right half of f142, f.116v =
  left half of f143 (crop x 0-1200 / 1200-2400).

**Verdict (ELEC-PAIR, 15 Oct 2026):** open, unchanged. Two name signs of nr. 357 read at C from Kluckhohn's print with a shuffled-name
control (W = le roy tres-chrestien, dd = le roy catholique), five more at M; none is the fr.5761 key's sign on the descriptions on file.
Next: (1) an image-to-image check of the f.116 signs against the fr.5761 f.110 key crops (disk, if look.tsv crops exist; ~1); (2) find
nr. 383 by bisection from fr.5761 f.172r backwards (ELEC-357's next 2, ~2), whose names Kluckhohn also prints, as a second witness for
the M signs; (3) other fr.3897 Joachim items (36-38, 62, 64-65, 73) for more occurrences of barI, 4, II, Zheavy, flag.

## ELEC-383: nr. 383 bisection back from fr.5761 f.172r (worker ELEC-383, LANE DEFAULT-A4-1035-15, account 4, 15 Oct 2026, 11:08-11:2x UTC by date -u)

Brief: ELEC-357's next (2), bisection from f.172r backwards for Kluckhohn nr. 383 (Orval, Bonnivet and Guillart to Francis I, 29 June 1519,
"Wahl Karls"; RTA J.R. I p.855, "Aus Paris Bibl. nat. F. fr. 5761. Cop., die Namen in Chiffren"). Result: **a likely end of nr. 383 is
found on f.166v (canvas f336), with one non-letter sign where the elected king's name stands. The letter's start was not read, and it was
not paired against the print. key.tsv unchanged; status unchanged (open).** Page images, not a transcription (rule 2). Search results only (rule 10).
- Canvas map: the fr.5761 IIIF v3 manifest's canvas labels give the folio directly (canvas = 2 x folio + 3 for rectos, e.g. f.160r = c323,
  f.166v = c336). These are the new foliation. The red ink numbers on the leaves are 5 lower (f.169 = "164"), which is ELEC-WALK's old_folio.
- Bracket (8 canvases at 1000 px, rows in `namewalk_elecwalk.tsv`). f.164v has a heading "Du [x]vij may", so it is May and before nr. 383.
  f.169r-v is a joint letter with personal paragraphs ("moy d'Orval", "moy admiral ... je partiray demain", "moy president Guillard"), dated
  "De Nanssy le x[v]iij Juill[et]" (day not settled), and is followed by the heading "Du iiij[me] Juillet". So the Nancy July run has begun by
  f.169r. It is also not in date order (18 July before 4 July, if the day is read right). ff.168r and 168v are mid-letter Coblenz-period text
  ("Bazoges est arrive icy", Treves, the conte palatin, la Motheaugroing) with every name in letters.
- **f.166v, lines 1-5**: "... a quelle heure que [SIGN] fut esleu et publie Roy des Rommains ...". Line 5 has "en ce lieu de Co[blence?]".
  Then the letter's closing paragraphs: "nous vous supplions tres humblement ...", "le peu de foy que avons trouve a ceulx a qui nous avions
  a faire ... les trahisons qui sont en ceste compaignie la", and advice to seek alliance with the Suisses, against Espaigne, the Pape and the roy
  d'Angleterre. Those names are in letters. The sign is a cross with small circle(s), "oXo"-like. The f.110 key describes Catholicque(r) as "a
  cross with a small circle attached at an angle". So the shape is close to the key's description, read by one reader at 1000 px (grade M, a
  description match, not image-to-image). This is the election news, consistent with Kluckhohn's "Wahl Karls" for 29 June and with the
  Description's last Coblenz reply. It is a candidate, not an identification: the dateline of this letter was not seen, since it ends at the
  top of f.166v without one in view.
- Kluckhohn says the names are in cipher, but this copy writes most names in letters (Suisses, Pape, roy d'Angleterre). Only the king of
  Spain/the elected king seems ciphered on the lines read. Not settled until f.165v-166r and Kluckhohn p.855-856 are read.
- `prior_work.py fr5761-election-1519 --item-spec 'BnF fr.5761 ff.165v-166v (Kluckhohn RTA J.R. I nr. 383)' --step-type read --offline`,
  exit 4. It was run after the fetches, not before the first one as the common rules require. Its holds are generic (LOOK 2-leaf, UNCHECKED
  3-tomokiyo/3-solver, UNCHECKED-NET 3-solver/4-editions). No specific hold. No PREREG, because no score was computed.
- Not read: ff.165v, 166r, 167r, 167v (the letter's start, and any other sign on it); f.166v at 2400 px; Kluckhohn pp.855-856 page images
  (archive.org was not in this job's host list).
- Requests: openapi.bnf.fr 10 (manifest 1; c323, c332, c340, c346, c342, c341, c339, c336 at full/1000; one c342 pct region), all 200, no
  403/429. Images in the session scratchpad only, none in git. Regen:
  `https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b52510561g/f336/full/1000,/0/default.jpg` (sign at about x 160-230, y 95-130 of the
  1000 px image).

**Verdict (ELEC-383, 15 Oct 2026):** open, unchanged. Nr. 383 most likely ends on fr.5761 f.166v (c336), with one cross-and-circle sign
for the elected king (M), close to the f.110 key's Catholicque description. Next: (1) read ff.165v-166r (c334-c335) at 1000 px for the letter's
start and any other signs, and f.166v at 2400 px (3 requests, ~1); (2) fetch Kluckhohn p.855-856 (archive.org `bub_gb_0gFoAAAAMAAJ` n863-n864,
2 requests) and pair the signs under the ELEC-PAIR rule, with its shuffled-name control (~1.5). A pair needs >= 2 occurrences per sign before
any C grade. Also (3): compare this sign image-to-image with nr. 357's dd ("le roy catholique", C) on fr.3897 f.116.

## ELEC-KLU: nr. 383 start and print pairing (worker ELEC-KLU, LANE DEFAULT-A4-1035-15, account 4, 15 Oct 2026, 11:37-11:5x UTC by date -u)

Brief: ELEC-383's next (1) and (2). PREREG `elecpair383/PREREG-ELEC-KLU.md` (pushed db037a72c before any fetch): ELEC-PAIR's rule
unchanged, shuffle seed 383. Page images, not a transcription (rule 2). Search results only (rule 10). key.tsv unchanged; status open.
- **Identification confirmed.** Kluckhohn RTA J.R. I nr. 383 (p.855 l.21 - p.856, continuing on p.857) opens "Sire, depuis les lectres
  que moy, admiral, vous ay escriptes hier, par lesquelles vous faisoye savoir la conclusion ..."; the same words open a new letter in the
  lower third of **f.166r (c335)**, after a blank space. So nr. 383 runs f.166r (last 4 lines) - f.166v, not from f.165v.
- Correction to ELEC-383: f.165v (c334) carries the heading "Au Roy 23 may" and begins a 23 May letter ("Suivant ce que vous escripvismes
  par noz autres lettres ... le chancelier du conte palatin est arrive en ce lieu de Coblence ..."), with names in letters, ending in the
  upper half of f.166r. ELEC-383's f.166v l.1 "a quelle heure que [SIGN]" reads at native size "que hyer ledit [SIGN] fut esleu", as printed.
- **5 both-sided pairs, 0 conflicts** (`elecpair383/pairs.tsv`): oXo = roy catholicque x2 (f.166r "deslire le _ Roy des Rommains";
  f.166v l.1 "hyer ledit _ fut esleu"); Phi (circle on a vertical stroke) = Brandebourg; Hbar (H-like with bar and superscript) = Treves;
  Lfo (L/f-like stroke with small o above) = conte Palatin (f.166v l.12 "mesmement au _ a ruyne"). "nre Sr" (nostre seigneur, f.166v l.8)
  is an ordinary abbreviation, not counted. The 7-like mark after Hbar is read as the par abbreviation ("par lesquelles"), M.
- **Grades** (`elecpair383/name_signs_fr5761_383.tsv`): all four signs M. oXo meets rule 3 (2 pairs, same name) but the shuffled-name
  control reproduces its consistency in 100/1000 permutations (10% >= 5%; `python3 elecpair383/pair_control.py --check`, exit 0), so rule 4
  holds it at M. At 5 slots with 2 of one name the control cannot fall below 5% for any 2-pair sign (2/5 x 1/4 = 0.10): a C grade from this
  letter alone is a non-test at this N (rule 3), not a negative. It needs a third oXo occurrence or a second letter pooled under a PREREG.
- Rule 5 comparisons (after 1-4; descriptions, one reader, M): oXo matches the f.110 key's Catholicquer description ("cross with a small
  circle attached at an angle"). Phi does not match the f.110 Brandebourg (Λ); it is nearer the f.110 Saxe description (circle on a
  horizontal dash) but the stroke here is vertical. Hbar is loosely like the f.110 Treves description (box divided by a bar). Lfo does not
  match the f.110 Palatin (hash with hook). Against nr. 357 (fr.3897): oXo is not dd (double loop, roy catholique) and Lfo is not "4"
  (Palatin). So nr. 383's copy shares at most one name sign (oXo) with the f.110 key and none with nr. 357, on descriptions.
- Not read: f.166v below l.12 against Kluckhohn p.857 (archive.org n865, not fetched); ELEC-383 saw Suisses, Pape, roy d'Angleterre in
  letters there, so further signs are possible but not expected.
- Requests: openapi.bnf.fr 4 (c334, c335 full/1000 200; c336 full/2400 HTTP 400, above native 2232 px; c336 full/max 200); archive.org 2
  (`bub_gb_0gFoAAAAMAAJ` n863, n864 w1800, 200). Images in the session scratchpad only, none in git. Regen:
  `https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b52510561g/f33{4,5}/full/1000,/0/default.jpg`, `.../f336/full/max/0/default.jpg`;
  `https://archive.org/download/bub_gb_0gFoAAAAMAAJ/page/n86{3,4}_w1800.jpg`. Signs: c335 1000 px x 100-500, y 1240-1290 (letter l.3-4);
  c336 max x 330-560 y 50-110 (oXo), x 1100-1200 y 1600-1680 (Lfo).

**Verdict (ELEC-KLU, 15 Oct 2026):** open, unchanged. Nr. 383 = fr.5761 f.166r (last lines) - f.166v, confirmed against Kluckhohn's print;
four name signs paired with the print (oXo = roy catholicque twice, Phi = Brandebourg, Hbar = Treves, Lfo = conte Palatin), all M: the
shuffled-name control cannot license C at 5 slots. Next: (1) Kluckhohn p.857 (n865, 1 request) against f.166v l.12-end for further signs
(~0.5); (2) a PREREG'd pooled pairing across the Coblenz-period fr.5761 letters Kluckhohn prints "die Namen in Chiffren" (find them by his
source lines, archive.org full-text "5761"), to bring oXo, Phi, Hbar, Lfo to >= 3 occurrences each (~2.5); (3) image-to-image check of
oXo against the f.110 Catholicquer crop if look.tsv has it on disk (~0.5).

## ELEC-POOL: nr. 383 end, the Kluckhohn pool, and the four signs against the f.53v key (worker ELEC-POOL, LANE DEFAULT-A4-1236-15, account 4, 15 Oct 2026, 12:45-12:5x UTC by date -u)

Brief: ELEC-KLU's next (1)-(3). PREREG `elecpool/PREREG-ELEC-POOL.md` (pushed 0164877ec before the step (3) comparison). Page images, not a
transcription (rule 2); search results only (rule 10). key.tsv unchanged; elecpair383/ grades unchanged; status open.
- **(1) Kluckhohn p.857 against f.166v l.12-end and f.167r: no further name sign.** p.857 (archive.org n865) prints the close: Suisses,
  pape, roy d'Angleterre (twice), le trésorier Babou, "A Convalence, le 29e jour de juing". On the manuscript f.166v (c336, native) runs to
  "sommes d'aviz que devez" with "Souisses", "pappe", "roy d'angl[eterre]" in letters; the letter ends at the head of **f.167r (c337)**:
  "entretenir ledit roy d'angleterre ... le tresorier babou ung de ses jours ... De Convalence le [xxix?] jour de juing. Signe d'Albret,
  Bonnyvet, Guillart" (old foliation 162), all in letters. So nr. 383 runs f.166r (last 4 lines) - f.167r (6 lines) and its name signs are
  the five ELEC-KLU slots only (oXo x2, Phi, Hbar, Lfo). Also seen: the 7-like mark stands before "lesquelles" twice on f.166r (end of letter
  l.1 "hier [7]" / l.2 "lesquelles", and l.4 after Hbar), both printed "par lesquelles", which supports ELEC-KLU's par-abbreviation reading (M).
- **(2) Pooled pairing: not run; the pool is empty on Kluckhohn's own source lines.** The volume's full text (`_djvu.txt`, 1 request) has 46
  fr.5761 source references; "die Namen in Chiffren" (or any Chiffre/Namen remark) stands on **exactly one**, nr. 383 (OCR "VGL"). The other
  fr.5761 letters of May-July 1519 are marked "Cop." only (e.g. nr. 290, 12 May; the 24 May royal reply; nr. 377, Bonnivet to the Palatine,
  "Cop. der Übersetzung"). One p.812 remark (Francis I to Orval and Guillart, 17 June) says they are to send the admiral "eine chiffrierte Copie
  dieses Briefes": that ciphered copy is not cited as being in fr.5761. Searched variants: chiff, chiffr, iffren, iffern, Namen, OCR "Xamen".
  This is OCR (the two shelfmarks OCR mangled were "Von." and "VGL", but the remark beside them survived), so it is a search result on the
  print, not an image census of fr.5761. With nr. 383 the only member, a pooled control would re-score ELEC-KLU's 5 slots and could not differ
  from it (rule 3 non-test), so no score was computed. oXo, Phi, Hbar, Lfo stay at 2/1/1/1 occurrences, M.
- **(3) Image-to-image against the f.53v key (images/canvas110_folio53v.jpg, on disk; "Maistre [Jehan] de Bourdeaulx devers le marquis de
  Brandebourg"), under the PREREG's five-feature rule** (stroke count, closed loops, crossings, orientation, detached marks), target crops at
  native size from c335/c336 (scratch only):
  | nr. 383 sign (printed name) | features | key row of the same name | result | other rows >= 4/5 |
  |---|---|---|---|---|
  | oXo (roy catholicque) x2 | horizontal stroke, closed circle at each end, crossed by an X; 3 strokes, 2 attached loops, crossing, horizontal, no detached mark | 11 Catholicquer: vertical cross with a closed circle at the foot and two small detached circles above the bar | **no match** (1/5: crossing) | 7 [Coulo]nne (horizontal stroke, circle at one end, crossed anchor at the other): partial 4/5 |
  | Phi (Brandebourg) | closed circle on a vertical stroke that passes through it; 2 strokes, 1 loop, crossing, vertical, none detached | 5 Brandebourg: "4"-shape, closed triangle on a vertical stroke | **match** on the five features (5/5); the head is round here, angular in the key, which the rule does not score | 6 Saxe (circle on a horizontal dash): partial 4/5 (orientation) |
  | Hbar (Treves) | two verticals, cross-bar, descending hook, small superscript marks; ~4 strokes, 0 loops, crossing, vertical, detached marks | 3 Treves: "6"-bowl joined to an f/long-s with a flourish | **no match** (2/5) | 4 Maguence (barred H): partial 4/5; 10 Francisme (H with small circles above): partial 4/5 |
  | Lfo (conte Palatin) | tall stroke with a foot, f-like stroke with cross-bar and a hook, small detached circle above; 3 strokes, 1 loop, crossing, vertical, detached mark | 2 Palatin: looped d/ampersand-like sign | **no match** (2/5) | none |
  So on the f.53v key one of four nr. 383 signs agrees with its own name's row on the rule's features (Phi ~ Brandebourg), three do not, and
  oXo is not the f.53v Catholicquer sign. ELEC-KLU's "oXo matches the f.110 Catholicquer description" was a description match only; image to
  image it fails. All M (one reader, the key at 1500 px, copy and key possibly in different hands); no conflict under rule 3 (no other row is a
  full match). Post hoc, outside the PREREG, not graded: the f.50v key (Cordier, crops f104_L03/04/06/12 on disk) has Palatin #, Treves a small
  loop on a hooked stem, Brandebourg a Z-like sign, Catholicque a row of small loops; none of the four nr. 383 signs is one of these by eye.
  The nr. 383 copy's name signs therefore do not follow one fr.5761 ff.50-53 key as a set (eight keys on file, none addressed to Orval, Bonnivet
  and Guillart; ff.51r-53r keys not compared).
- prior_work.py: not re-run; ELEC-KLU's run for this unit (exit 4, generic holds only) covers the same leaves, and no new leaf beyond f.167r
  was read.
- Requests: archive.org 2 (`_djvu.txt`, n865 w1800), openapi.bnf.fr 3 (c336, c335, c337 full/max), all 200, no 403/429. Images in the session
  scratchpad only, none in git. Regen: `https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b52510561g/f33{5,6,7}/full/max/0/default.jpg`,
  `https://archive.org/download/bub_gb_0gFoAAAAMAAJ/page/n865_w1800.jpg`. Crops (native px): c336 oXo x 650-950 y 180-320, Lfo x 1850-2150
  y 1560-1760; c335 Phi and Hbar x 860-1260 y 2780-2950.

**Verdict (ELEC-POOL, 15 Oct 2026):** open, unchanged. Nr. 383 is f.166r-f.167r and has exactly five name-sign slots; Kluckhohn flags no other
fr.5761 letter as having names in cipher, so the pooled pairing has no second member and C for oXo, Phi, Hbar, Lfo is not reachable from the
print. Image to image, only Phi agrees with its row on the f.53v Brandebourg key; oXo is not that key's Catholicquer. Next: (1) image check of
the other section 3(b) Coblenz replies (14 May-29 June, before f.166r; ELEC-WALK read rectos only) for name signs Kluckhohn did not flag,
starting with the versos of ff.160-165 at 1000 px (~6 canvases, ~1.5); (2) compare the four signs with the f.51r-53r keys (c105-c109 on
disk, ~1); (3) fr.3897's other Joachim items (36-38, 62, 64-65, 73) for second witnesses of nr. 357's M signs (ELEC-PAIR next 3).

## ELEC-VERSO: versos of ff.160-163 and the four nr. 383 signs against the f.51r-53r keys (worker ELEC-VERSO, LANE DEFAULT-A4-1236-15, account 4, 15 Oct 2026, 13:12-13:2x UTC by date -u)

Brief: ELEC-POOL's next (1)-(2). PREREG `elecverso/PREREG-ELEC-VERSO.md` (pushed e73f2874b before any fetch). Page images, not a
transcription (rule 2); search results only (rule 10). key.tsv unchanged; elecpair383/ grades unchanged; status open.
- prior_work.py (`--item-spec 'BnF fr.5761 ff.160v-163v versos ...' --step-type read --offline`), exit 4, generic holds only (LOOK 2-leaf,
  UNCHECKED 3-tomokiyo/3-solver, UNCHECKED-NET 3-solver/4-editions), as for ELEC-383/ELEC-KLU; run before the first fetch.
- **(1) Versos: no name sign.** f.164v (c332, ELEC-383) and f.165v (c334, ELEC-KLU) were already read, so four canvases were fetched at
  1000 px: f.160v (c324), f.161v (c326), f.162v (c328), f.163v (c330). All four are mid-letter Coblenz-period text with every name in
  letters: c324 a first-person report ("ce jour je parlay ..."; no name legible as a sign); c326 "led. conte Jehan", "l'eslection";
  c328 Bohesme, Francfort, Langraff de Hesse, Coulongne, Magence, conte palatin, marquis de Brandebourg; c330 marquis de Brandebourg
  (twice), Magence, "monseigneur vostre second filz", Strasbourg, Allemaigne, Franckfort, a heading "Sauvé" between two letters. No isolated
  non-letter sign in a word slot at this scale (the oXo of f.166v shows plainly at 1000 px, so a name sign would have been visible), so no
  native crop was fetched. With ELEC-383/KLU the versos ff.160-165 are now all read; rectos ff.161r-164r (c325, c327, c329, c331) are not.
- **(2) The f.51r lower key block carries all four nr. 383 signs under their own names** (`elecverso/key_compare_f51r-53r.tsv`). The block
  headed "A monsr de la Vernade devers monsr de Treves" (f.51r, c105, lower half; reading of "Vernade" M) gives Palatin = an L/f stroke
  with a small circle above (Lfo), Treves = an R/H-like sign with a bar and superscript (Hbar), Brandebourg = a loop on a vertical stroke
  (Phi), and, below the rule, Le Roy catholicque = a horizontal stroke with a small circle at each end and an X across it (oXo). Under the
  PREREG's five-feature rule each is a 5/5 match to its own name's row. Distractors: the rule is coarse for two of the four. oXo also scores
  5/5 against f.51v Cleves (o+o, upright cross) and f.52v Treverien (circle-bar-bar-circle), and Phi 5/5 against f.51v Saxe (phi), so those
  are logged as conflicts under the rule; Hbar's best other row is 4/5 (f.51r upper block Coulongne), and Lfo has no other row at >= 4/5 on
  ff.51r-53r. Only the f.51r Vernade block matches all four signs, each to its own printed name; no other block on ff.50v-53v matches more
  than one (f.53v Brandebourg, ELEC-POOL; f.51v two, both under other names). Post hoc, not scored: by eye the X of nr. 383's oXo is the
  diagonal cross of the f.51r Roy catholicque, not the upright + of Cleves or the double bar of Treverien.
- **Who shares the key (M, one reader).** Beside the lower block's rows a note reads "[Sem]blable a monsr de Lorraine, monsr d'Orval, monsr
  de Bazoges, [l'aumosnier?] Chambrehain, Salviati, a monsr le tresorier Robertet". If "semblable" is right and the note belongs to this block
  (it sits inside it, right of the Brandebourg-Magence rows), Orval, one of nr. 383's three signers, was given this same name list, which
  would explain why the copy's name signs follow this block. The first word and the attachment are not settled; Bonnivet and Guillart are not
  named in the note.
- All M (one reader; key image 1500 px; the copy and the key in different hands). key.tsv does not yet carry f.51r rows (R5 D's "what's
  left"), so nothing was entered; no grade in elecpair383/ changed. This is the second line of evidence ELEC-KLU's rule 3 note asked for
  (a period key row for the same name), not a second ciphertext occurrence: the shuffled-name control's 10% for oXo is unchanged.
- Step (3) (fr.3897 items 36-38) not run: under 30% of cap left after (1)-(2).
- Requests: openapi.bnf.fr 6 (c324, c326, c328, c330 full/1000; c336 region 0,0,2232,1800; c335 region 0,2650,2232,400), all 200, no
  403/429. Images in the session scratchpad only, none in git. Regen:
  `https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b52510561g/f32{4,6,8}/full/1000,/0/default.jpg`, `.../f330/full/1000,/0/default.jpg`,
  `.../f336/0,0,2232,1800/max/0/default.jpg`, `.../f335/0,2650,2232,400/max/0/default.jpg`. Key crops from images/canvas105_folio51r.jpg
  (1500x2199): lower block x 0-700 y 1270-2000; note x 620-1500 y 1560-1860.

**Verdict (ELEC-VERSO, 15 Oct 2026):** open, unchanged. The versos of ff.160-165 carry no name sign. The four nr. 383 name signs are, as a
set, the f.51r "la Vernade devers Treves" block's Palatin, Treves, Brandebourg and Roy catholicque signs (each 5/5 on the PREREG rule, M), and
a note on that block appears to extend the same list to Orval. Next: (1) a second reader (blind Sonnet pass on the f.51r lower block and the
four target crops, ~0.6) to confirm the four matches and read the note's first word, before any f.51r rows go into key.tsv (~0.6 with a
majority_key_leaf.py run); (2) with the f.51r block as the key, search fr.5761 rectos ff.161r-164r (c325-c331, 4 canvases at 1000 px, ~1.5)
and the other Orval/Bonnivet/Guillart copies for further occurrences of its signs, which a third oXo would need for C; (3) fr.3897 items 36-38
(ELEC-PAIR next 3).

## ELEC-R2: blind second reader on the f.51r lower block and its side note (worker ELEC-R2, LANE DEFAULT-A4-1236-15, account 4, 15 Oct 2026, 13:35-13:4x UTC by date -u)

Brief: ELEC-VERSO's next (1). PREREG addendum `elecr2/PREREG-ELEC-R2.md` (pushed 585a6a34d before the fetch and the reader call). One blind
Sonnet subagent call, crop paths only (no sign names, no ELEC-VERSO matches, no print): six shuffled targets (the four nr. 383 signs cut
from c335/c336 native, plus two decoys from the f.53r key: Colonien circle-bar-circle, palatinus pi-sign) against panel A (f.51r lower part,
canvas105 y 1250-2050) and panel B (f.51v whole leaf). Result `elecr2/reader2_result.tsv`.
- **Registered rule: FAIL, 2 of 4 real targets** to their own panel-A row (need >= 3). oXo -> A "Le Roy catholique" (conf 3) and Lfo -> A
  "Palatin" (conf 3) agree with ELEC-VERSO. Phi -> B (a phi sign on f.51v the reader read "Cerye", ELEC-VERSO's "Saxe" conflict row), with A
  Brandebourg named only as a "weaker look-alike"; Hbar -> none (conf 1; reader listed A Treves as "R/Rf with a flourish").
- **Decoy control clean, 0 of 2** on any panel-A row (Colonien -> "B Cleves weak, treat as none"; palatinus -> none). The control could
  vary on the matching axis and did not fire, so the two agreements are not the reader matching anything to panel A; the two misses are
  the reader's, not noise in the control.
- **Side note, first word.** The reader gives "Baille a mons[r] de Lorraine mons[r] / Arnal[?] mons[r] de Bazoges ... / [C]hambreham[?]
  [S]almiati[?] a mons[r] / Le tresorier Hobertet [R?]" -- "Baille a" (handed to), not "[Sem]blable". So the note lists who was given this
  name list, which still includes the persons ELEC-VERSO read (Lorraine, Bazoges, Chambrehain, Salviati, Robertet); the second name is read
  "Arnal" here and "d'Orval" by ELEC-VERSO -- unsettled, two readers disagree. Orval's presence on the list is therefore M, one reader for,
  one reading a different name.
- Grades: all M, unchanged (as registered). key.tsv unchanged; no --try run (no f.51r rows in key.tsv). elecpair383/ grades unchanged.
- Requests: openapi.bnf.fr 3 (c336 650,180,300,140 and 1850,1560,300,200; c335 860,2780,400,170; all /max/), all 200. Images in the
  session scratchpad only, none in git.

**Verdict (ELEC-R2, 15 Oct 2026):** open, unchanged. A blind second reader confirms two of the four nr. 383 signs against the f.51r
"la Vernade devers Treves" block (Roy catholicque, Palatin), puts Phi on f.51v's phi row and finds no row for Hbar; the registered >= 3/4 rule
fails with a clean decoy control. The side note opens "Baille a" (a recipients list), and its second name (Orval vs "Arnal") is unsettled.
Next: (1) native-resolution crops of the f.51r Brandebourg/Treves rows and the note's second line (openapi.bnf.fr c105 regions, 2 requests,
~0.8) for a third reader on Phi, Hbar and "Orval"; (2) ELEC-VERSO next (2) rectos ff.161r-164r; (3) fr.3897 items 36-38.

## ELEC-R3: third blind reader on native-resolution crops (worker ELEC-R3, LANE DEFAULT-A1-1426-15, account 1, 15 Oct 2026, 14:40-14:4x UTC by date -u)

Brief: ELEC-R2's next (1). PREREG addendum `elecr3/PREREG-ELEC-R3.md` (pushed 21e2ea4ad before the fetch and the reader call): ELEC-R2's
rule, targets, decoys, shuffle and task unchanged; only the crops changed to native resolution (panel A f.51r lower part, c105 native 2276 px
wide, plus block and note zooms cut from the same fetch; nr. 383 targets re-cut from native c335/c336). One blind Sonnet subagent call,
crop paths only. Result `elecr3/reader3_result.tsv`.
- **Registered rule: real targets 3 of 4 to their own panel-A row** (oXo -> Roy catholique conf 3, Lfo -> Palatin conf 3, Hbar -> Treves
  conf 2; Phi -> B phi row "Garye/Cerye" conf 2, A Brandebourg named only as alternative) **but the decoy control FIRES**: the f.53r palatinus
  decoy (pi-sign) was assigned to a panel-A row (the first sign of the "Nulle" row, conf 2). Under the registered rule a decoy on a panel-A
  row is a control FAIL, so the 3/4 licenses nothing: at native resolution, with more of panel A visible, the reader matches a decoy into
  panel A, and Hbar's conf-2 Treves match is not distinguishable from that decoy's conf-2 match. The Colonien decoy went to B Cleves (clean).
- **Per target against R1 (ELEC-VERSO) and R2 (ELEC-R2):** oXo and Lfo agree with both (three readers, all conf 3 for R2/R3); Phi agrees with
  R2 (f.51v phi row), disagrees with R1 (A Brandebourg); Hbar agrees with R1 (A Treves), disagrees with R2 (none); decoys: Colonien agrees
  with R2 (not panel A), palatinus disagrees (R2 none, R3 panel-A "Nulle").
- **Side note.** First word "Baille [?] a" (agrees with R2, against R1's "[Sem]blable"). The second person is read "Arnal" (agrees with R2;
  R1 "d'Orval"), so two of three readers give "Arnal": no reader after R1 gives an O-initial -rval form, and Orval's presence on the list
  is not supported by the blind readers (M at most, leaning against). Lorraine, Bazoges ("Bazogis"), Salviati ("Salmiati[?]"), Robertet
  again legible; Chambrehain read only as "rgambregam[?]".
- Grades all M (registered). key.tsv unchanged; elecpair383/ grades unchanged; status open.
- Requests: openapi.bnf.fr 3 (c105 `pct:0,56.84,100,36.38/max`, c336 `650,180,1500,1580/max`, c335 `860,2780,400,170/max`), all 200.
  Decoys cut from images/canvas109_folio53r.jpg (Colonien 290,660,140,80; palatinus 290,740,130,100); panel B images/canvas106. Images in
  the session scratchpad only, none in git.

**Verdict (ELEC-R3, 15 Oct 2026):** open, unchanged. oXo -> f.51r Roy catholicque and Lfo -> f.51r Palatin now have three readers in
agreement (M); Phi and Hbar stay split (each 2 of 3 readers, in different directions), and this pass's 3/4 is void because a decoy landed on a
panel-A row. The side note is a recipients list ("Baille a ..."); its second name is "Arnal" for two blind readers, not "Orval". Next:
(1) ELEC-VERSO next (2): rectos ff.161r-164r (c325-c331, 4 canvases at 1000 px, ~1.5) for further occurrences of the f.51r signs, which a
second ciphertext occurrence needs; (2) fr.3897 items 36-38 (ELEC-PAIR next 3); (3) no fourth reader on Phi/Hbar on the same two images
(rule 3's third-attempt clause: same instrument, same material) unless new material (a further occurrence) comes in.

## ELEC-REC: rectos ff.161r-164r searched for the f.51r-block signs (worker ELEC-REC, LANE DEFAULT-A1-1426-15, account 1, 15 Oct 2026, 15:22-15:3x UTC by date -u)

Brief: ELEC-VERSO next (2), repeated by ELEC-R2 and ELEC-R3. PREREG `elecrec/PREREG-ELEC-REC.md` (pushed 88e730ee1 before any fetch):
the occurrence rule (word slot; not a letter or a standard abbreviation; 5/5 on ELEC-POOL's five-feature rule against one f.51r lower-block
name row), with nulles not searched; and the decoy rule. ELEC-R3's decoy fired because a reader made a forced choice of a key-panel row for a
given target. This pass avoids that because the search is open (candidates are listed per canvas before any key comparison), every 5/5
candidate is re-scored against the f.53r rows as a decoy panel (5/5 there = conflict, not counted), and the surrounding clear words must admit
the row's name. One non-blind reader (this worker, Opus, own eye). Page images, not a transcription (rule 2). Result `elecrec/rectos_result.tsv`.
- prior_work.py (`--item-spec 'BnF fr.5761 ff.161r-164r rectos ...' --step-type read --offline`): exit 4, generic holds only (LOOK 2-leaf,
  UNCHECKED 3-tomokiyo/3-solver, UNCHECKED-NET 3-solver/4-editions), the same as the earlier ELEC passes on these leaves.
- **Zero candidates on all four rectos, so zero counted occurrences.** f.161r (c325): mid-letter, monsr de Coulongne twice in letters; two
  filled ink blots (l.7, l.13) are not signs. f.162r (c327): the close of a letter "De Convallence le xxvij jour de may, Signe dalbret", then
  "Sire hier monsr de Treves alla veoir monsr le legat", Francfort and Coulongne, all in letters. f.163r (c329): the close of a letter signed
  "Dalbret Bonnyvet et Guillart" (Convallance, 26 May), the same three signers as nr. 383. It writes duc de Saxe, Treves, Magence, conte
  palatin, Coulongne and the legate in letters, with no sign in any slot. A copy headed "Double" in another hand follows. f.164r (c331): that
  copy goes on, with Wirtemberg, Treves, Lorraine, Bazoges, Joachim de Moltzan, Brandebourg and Magence in letters. A 7-like mark before
  "lesquelles" (l.20) is the par abbreviation (ELEC-KLU), excluded under (b).
  So the decoy panel and the context check were never reached. No native region was fetched (no candidate). At 1000 px an oXo-sized sign
  shows plainly (ELEC-VERSO on f.166v), so this is a search result at that scale, not a native-resolution census.
- Observation, not graded: the 26 May letter of Albret, Bonnivet and Guillart (f.163r) writes in letters the names that nr. 383 (late June,
  same three signers) puts in signs. On ff.160-167 the name signs stand only in nr. 383. The f.51r list may have reached these signers
  after 26 May, or only that copy was ciphered. This is not tested here.
- Grades: none changed (no occurrence). The third oXo that C would need was not found on these leaves. key.tsv unchanged; elecpair383/
  unchanged; status open.
- Requests: openapi.bnf.fr 4 (c325, c327, c329, c331 `full/1000,`), all 200, no 403/429. Images in the session scratchpad only, none in
  git. Regen: `https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b52510561g/f3{25,27,29,31}/full/1000,/0/default.jpg` (sha1 in the TSV).

**Verdict (ELEC-REC, 15 Oct 2026):** open, unchanged. The rectos ff.161r-164r carry no f.51r-block sign at 1000 px. With ELEC-VERSO, ELEC-383
and ELEC-KLU, every leaf of ff.160-167 has now been read, and nr. 383 is the only copy there with name signs. A 26 May letter of the same three
signers (f.163r) writes all the electors' names in letters. Next: (1) fr.3897 items 36-38, 62, 64-65, 73 (ELEC-PAIR next 3) for second
witnesses; (2) other Orval/Bonnivet/Guillart copies after 26 May outside ff.160-167 (Kluckhohn's fr.5761 source list, 46 references, gives the
leaves; the June letters first, ~1.5 for 4-6 canvases at 1000 px), the only place left in this volume where a further oXo could stand;
(3) no fourth reader on Phi/Hbar on the same f.51r images (ELEC-R3 next 3).

## ELEC-3897: fr.3897 Joachim items 36-38, 62, 64-65, 73 for second witnesses (worker ELEC-3897, LANE DEFAULT-A1-1426-15, account 1, 15 Oct 2026, 15:48-16:0x UTC by date -u)

Brief: ELEC-REC next (1) = ELEC-PAIR next (3). PREREG `elec3897/PREREG-ELEC-3897.md` (pushed fac82ca3c before any fetch). It uses ELEC-REC's
occurrence rule (a word slot; not a letter form or a standard abbreviation; 5/5 features against one row) and decoy rule (an open list
before any comparison, the f.53r decoy panel, a context check), extended to set A, the nr. 357 name signs (ELEC-PAIR: W, dd, barI, 4, II,
Zheavy, flag). One non-blind reader (this worker, Opus, own eye). Page images, not a transcription (rule 2). Result: `elec3897/items_result.tsv`.
- Locating the items. The v3 manifest Description (1 request) gives the item titles. 36: first marriage treaty, Renée and Joachim's eldest son,
  Latin. 37: second treaty, 26 Mar 1519, Latin copy. 38: Joachim's letters promising his vote, Cölln an der Spree, 8 Apr 1519. 62: copy of
  Joachim's letters for the king, deferring part of the payment. 63: Joachim promises to elect the king if two co-electors do. 64: Francis I
  names Joachim his lieutenant in Germany, copy. 65: copy of the king's pension promise. The canvases are openings with the folio number on
  the recto. `gallica_folio.py` on the cached v2 manifest has every label "NP", so its anchor fit (c128=103, c142=116, c150=123, c263=222)
  was only a starting point. The folio numbers read on the rectos give a canvas offset of 21 at f.74 (c95), 22 at f.82 (c104) and 27 at
  ff.125-128 (c152-155). The offset changes between f.82 and f.103 (25 there, ELEC-357).
- **No name sign and no f.51r-block sign on any page read (0 candidates under (a)+(b), so 0 counted in set A or set B).** The decoy panel and
  the context check were never reached. Per item:
  - 36 (c95, f.73v-74r, mid-treaty; 36 rather than 37 by position only): Latin. Renata, the marquis of Brandenburg and the Regis
    christianissimi are written in letters.
  - 38 (c104, f.81v-82r, headed "Copia lre electionis"): Latin. "Nos Joachim dei gra Marchio Brandemburgen ... Franciscum ... Francorum Regem,
    Mediolani ducem" are in letters. Above the heading is the dated close of the preceding piece ("in castro nro Colonie ad Spream ... mensis
    Aprilis"). The two dots in the top margin are outside the text.
  - 62 (c152, f.124v-125r): French copy. It is signed "Joachim" in letters, with an interlinear "Joachim" correction on f.124v l.1.
    "Roy des Rommains" is also in letters. 63 starts on f.125r in the same opening: "marquis Joach[im]" and Mayence in letters.
  - 64 (c154, f.126v-127r): French. "nre cousin le marquis de Brandebourg" and "son second filz Jehan de Brandebourg" are in letters. A
    contemporary note in the f.126v margin is outside the text. Under the item-65 docket at the foot of f.127r there is a flourish group.
    It is a docket/heading flourish under rule (a), so it is not counted (not fetched natively).
  - 65 (c154 docket, c155 f.127v-128r): French. "Nous Francoys par la grace de dieu Roy de France ... Joachim marquis de Brandebourg ... nre filz
    aisne daulphin" are in letters. The item runs onto f.128r, one leaf past the catalogue's ff.72-127.
  - 37: not located. It lies between f.74r and f.81v, and no request was left (6/6 used).
  - 73: not fetched. It is f.146, a 1520 French translation of a Lüneburg/Joachin letter, which KH1-A viewed on 7 Oct 2026 as a clear translation
    (KEYHUNT-2026-10-07.tsv). It falls outside the 1519 election run.
- Reading: in this volume the formal instruments of the Brandenburg negotiation write every name in letters. These are the treaties, the vote
  promise and the king's promises, in Latin and in French. In fr.3897 the name signs stand, so far, only in the two letters to Bonnivet (items 39
  and 56; item 39, Kluckhohn nr. 356, has not been read for signs). This is an observation and is not graded.
- Grades: none changed. key.tsv and elecpair/ are unchanged, and the status stays open. This is a search result at ~1000 px per page, not a
  native census.
- Requests: openapi.bnf.fr 6 (the presentation v3 manifest; btv1b90096539 f95, f104, f152, f154, f155 at `full/2000,`), all 200, no 403/429. The
  images are in the session scratchpad only, none in git. Regen: `https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b90096539/f{95,104,152,
  154,155}/full/2000,/0/default.jpg` (sha1 in the TSV).

**Verdict (ELEC-3897, 15 Oct 2026):** open, unchanged. fr.3897 items 36, 38, 62-65 write every name in letters, and none carries a nr. 357 or
f.51r-block sign at ~1000 px per page. Item 37 was not located (between f.74 and f.81v). Item 73 is a clear 1520 translation (KH1-A). No second
witness was found here for barI, 4, II, Zheavy or flag. Next: (1) fr.3897 item 39 (Joachim to Bonnivet, "Vendredi", Kluckhohn nr. 356, printed
p.813). It is the one remaining Joachim letter to the admiral, which the name signs would favour. It lies between f.82 and f.103 (offset 22-25);
locate it in 2-3 openings at 2000 px and pair it against the print under ELEC-PAIR's rule, ~2. (2) Other Orval/Bonnivet/Guillart copies after
26 May in fr.5761 (ELEC-REC next 2), ~1.5. (3) Item 37 only if (1) shows that the Brandenburg pieces carry signs, ~0.5.
