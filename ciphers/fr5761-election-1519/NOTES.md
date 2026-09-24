open

# 1519 imperial-election embassy cipher key -- BnF Français 5761, no. 3

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
