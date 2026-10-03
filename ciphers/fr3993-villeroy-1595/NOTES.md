open
Gomberville, *Mémoires du duc de Nevers* (1665) seconde partie (Google Books H2eV4wAmIr0C) full-text searched by this worker (GF4-BATCH9, 3 Oct 2026): pregnant, "noz affaires", intelligiblement 0 hits; Doullens 6 hits pp.717-719 (the different letter to "Messieurs") -- letter absent.

**Hold lifted, LANE N4 scGOM2, 24 Sept 2026:** the genuine seconde partie is Google Books `H2eV4wAmIr0C` (title
page confirmed); full-text searched for this letter's own terms (Villeroy, Cambray, Doullens, Fuentes,
S. Quentin, 16 Aoust, the cipher-explaining clear sentence) -- letter absent; see the dated section below.

# Nevers to Villeroy, Saint-Quentin, 16 August 1595 — BnF fr. 3993 no. 102 (ff. 148r–149r)

QUEUE row: CS2-26 (`sources/solver-diffs/2026-09-24-cyphersolver-site.tsv`, LANE N3 scout scCS2, 24 September
2026 — catalogue item 277 at dbourdeau.github.io/cyphersolver/catalogue.html). Check-solved run 24 September
2026 by LANE N3 csCS2b (session_01711qcbvcwvGDsSAtVXwfJB), brief `.claude/briefs/runs/2026-09-24-lane-n3-csCS2b.md`.

## What it is

Nevers's file copy (secretary's hand) of a letter to Villeroy, dated "16 d'aoust 1595" / "De St Quentin ce 16
aoust 1595," about the relief of Cambrai (besieged by Fuentes) and the loss of Doullens. Clear French with 17
inserted cipher runs (753 signs total: mostly 1–4-digit figures — `1 2 o 3 7 4 9 ...` — plus about 45 non-figure
signs `ↄ T λ π θ ∞ ‡ ϖ Δ ∩ Ⱡ`). The letter itself explains why cipher is used: "ce qui est de plus pregnant seroit
bon d'estre en chiffre ... affin que 72 ne puissent prendre cognoissance de noz affaires" (72 = code number for
the enemy). D. Bourdeau's own working folder (`nevers1595/`, session of 22 September 2026) transcribed both
cipher blocks (`ct_f148r.txt`, `ct_f148v_149r.txt`) and tried six Nevers keys from fr. 3995 (nos. 60, 65, 66,
68–76, including the Court cipher of 1593 and the Balagny–Nevers alphabet reconstructed by Tomokiyo from the
same volume, fr. 3993 f. 130) — none fits. Six unit-segmentation models were run through a letter-level solver
(`hsolve.py`) and a syllabic-unit solver (`hsyl.py`), each validated against a matched control built from Henri
IV's letters enciphered with the letter's own run-length profile: **the homophonic control solves cleanly
(−1.84/char, all restarts agree) and every target run scores far worse (−2.5 to −3.1, no restart agreement, no
French)**; the syllabic-unit control itself fails to solve at this length, so that design cannot even be tested
here. This satisfies rule 3 (no negative without a matched control) directly.

## Six-source search log (24 September 2026)

1. **Tomokiyo (sources/cryptiana/ on disk).** No sentence in the local snapshot names fr. 3993 no. 102
   specifically (grep for "3993" hits only two unrelated 1595 items, f.71 and f.254, in `nevers.htm`). Bourdeau
   cites Tomokiyo's *League* page directly (not in the local snapshot, so not independently re-verified here):
   *"Portions in cipher. Undeciphered. The cipher uses figures and other symbols ... It seems none of the Nevers
   collection decodes these."* No later publication cited.
2. **Standard printed edition — actually read.** Gomberville, *Mémoires du duc de Nevers* (1665), tome 2,
   **searched by Bourdeau via Gallica's own full-text search** against this letter's exact clear phrases (e.g.
   "assez intelligiblement," the Cambrai/Doullens/Fuentes context): **no hit**. This is the strongest edition
   check of this batch — a genuine full-text search of the correct tome for the correct date and content, not
   an index lookup. This worker did not have Gallica full-text search access this pass (IIIF-only grant) and so
   did not independently re-run it, but the search terms, tome and method are named, matching this lane's rule
   (LANE N3 addition, 24 Sept 2026).
3. **DECODE (sources/decode/) + both solver-repo clones.** No DECODE record found for fr. 3993 no. 102 in the
   local snapshot (grep for "3993": no hit in `records-non-decrypted-2026-09-24.tsv` or
   `records-decrypted-2026-09-24.tsv`). dbourdeau/cyphersolver (shallow clone, 24 Sept 2026):
   `nevers1595/NOTES.md` gives the fullest account (above); verdict "attempted, closed from the evidence (not
   read)... the runs are not a plain homophonic cipher"; full escalation checklist [x] on siblings, clear-pages,
   known-keys, print, key-rebuild; sibling fr. 3993 no. 133 (18 Aug 1595, next letter to Villeroy) checked and
   confirmed all-clear, no cipher. aaymeloglu/unsolved-ciphers: fresh shallow clone, no hit for "3993" or
   "Villeroy" + "1595".
4. **Web search** (Nevers Villeroy Saint-Quentin 16 août 1595 chiffre fr.3993): only BnF/Wikipedia catalogue-type
   results surface (the manuscript series record, Louis de Gonzague's Wikipedia page); no solution or key found.
5. **Ciphertext confirmed present on the Gallica leaf.** IIIF fetch, gallica.bnf.fr, 24 Sept 2026, 1 request:
   `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9059229n/f161/full/500,/0/native.jpg` (canvas 161, f.148r, right
   half of the two-page spread). Image shows clear French prose with a block of cipher figures at the foot of
   the page, matching Bourdeau's description and layout (a two-page-spread volume, *Collection Mémoires de la
   Ligue*). Leaf: https://gallica.bnf.fr/ark:/12148/btv1b9059229n/f161.item

## Verdict

**Stage 2, open.** No source of the six claims a decipherment of BnF fr. 3993 no. 102. Bourdeau's own attempt —
the deepest single source, and the only one of this batch to run an actual full-text search of the correct
Gomberville tome against the letter's own clear phrases — closes it as a genuine ciphertext-resistant target: a
753-sign mixed nomenclator that fails every tested unit-segmentation model under a rigorously matched
homophonic control (rule 3 satisfied), and is not any of eleven candidate Nevers keys checked against the image.
What would move it, per Bourdeau: the as-sent letter to Villeroy (Nevers's copy is what survives here), or a
key among the unexamined portions of fr. 3995 beyond nos. 60/65/66/68–76.
**Update, VILL-147, 3 Oct 2026:** ff.147v/149v viewed native (no gloss; f.149v docket names the packet the original went in);
fr.3995 nos.48-51 not testable (symbol-only, max coverage 0.409). Next: fr.3995 nos.39/40/43/58; Nevers to Henri IV, July-Aug 1595, as siblings.
**Update, A1B-VILL-PAIR, 3 Oct 2026:** figure-pair homophone design (Bourdeau 1x/2x, K null) is a control-backed negative (control 0.733, target judge FAIL -1.263 = shuffle -1.261). Next: no.57's table (j), no.44 symbol column (k), as-sent packet (d), second transcription pass (e').

Credit: D. Bourdeau, cyphersolver, https://dbourdeau.github.io/cyphersolver/ (catalogue item 277; `nevers1595/`
working folder — full transcription, matched-control solver ladder across six unit models, Gomberville tome-2
full-text search), CC BY 4.0 — prior attempt (not a solution). S. Tomokiyo, cryptiana *League* page (cited via
Bourdeau; not independently re-verified from the local snapshot this pass).

Not decoded, not transcribed here (out of scope for check-solved; Bourdeau's `nevers1595/` already has a full
transcription and solver ladder if a solver picks this up). Rule 10: no novelty claim made; this is a search
result, not a verifier's classification.

## Control-first cryptanalysis (24 Sept 2026, LANE R4 N)

Brief `.claude/briefs/runs/2026-09-24-lane-r4-n-villeroy-garbino.md` (Opus, cap $7, session_018cVYFykz1TpBPHHHgWqHuN).
Transcription: D. Bourdeau's first pass (`bourdeau/`, copied unchanged with attribution, MIT / CC BY 4.0); not
re-checked on the image, so everything here is conditional on it (rule 2).

**What Bourdeau had not tested.** His ladder assigns one letter (or one CV syllable) per unit. The design not yet
tried is a mixed nomenclator: letters with homophones, plus syllable signs, plus word codes, plus nulls, solved
jointly. Segmented 1x/2x as in his `seg.py` (`solver/target_pairs.txt`), the runs give **607 units, 69 types**.

**Matched control first (rule 3).** `solver/design_nomen69.json`: 45 letter signs (e 5, a/i/s/u 3, ...), 12
syllables, 8 French word codes (from de que le la les et pour roi nous vous qui est ennemi dessein), 4 nulls at 5%,
syllables used 80% of the time; enciphered on held-out French 16th-c. letter prose (every 10th paragraph of
`tools/data/fr16`, Catherine de Médicis t.1-2 and Marguerite de Valois, never seen by the model) in the target's own
17-run pattern: 607 tokens, 61-62 types. Solved blind with `tools/nomenclator_anneal.py solve` (French order-5
model built by `solver/fr_corpus.py` + `tools/italian_ngram.py build`; `--syl both --max-syl 12 --max-word 8
--max-null 4`, 12 restarts x 1.5 M iterations). Reproduce: `solver/run_controls.sh`.

| control | token accuracy | letter accuracy | sign accuracy | reading |
|---|---|---|---|---|
| nomenclator, seed 1 | **2.0%** | 21.5% | 1.6% | gibberish |
| nomenclator, seed 2 | **5.9%** | 12.5% | 4.9% | gibberish |
| sanity: pure homophonic, 45 signs + 3 nulls, same length and pattern | 61.1% | 56.2% | 53.3% | partly readable ("medicis elle ua de...") |

**Target: not run.** The brief says run the target only if the control reads; it does not, so a target run could
say nothing either way. Result: **the mixed-nomenclator design has no working control at 607 units with this
solver** (2.0% / 5.9%, against 61% for a homophonic control of the same size through the same solver; Bourdeau's
`hsolve.py` reads the homophonic control fully). With Bourdeau's six negatives this closes ciphertext-only attack on
the transcription as it stands: every design that could be controlled has been, and the remaining one cannot be.

**Keys on file.** No key in `ciphers/*/key.tsv` dates from 1593-96 or belongs to Nevers's circle (the 14 keys on
file are 1446-1869, none French 1590s), so none was applied. Bourdeau's Court cipher of 1593 (fr. 3995 no. 60)
and nos. 65, 66, 68-76 are already ruled out above.

Grade counts: H 0, C 0, S 0, M 0, I 0 (nothing read). Status stays `open`.

Suggestions (not done, outside this brief): read the fr. 3995 keys other than nos. 60/65/66/68-76 on the image for
the sign family `λ π θ Δ ϖ ∞` with 1x/2x figures (no. 76 is the nearest family); look for the as-sent letter in
Villeroy's papers (fr. 15xxx / Cinq Cents de Colbert). No request was made to any host in this step.

## Edition check, LANE N4 scGOM2, 24 September 2026 (Google Books, genuine seconde partie found)

Brief `.claude/briefs/runs/2026-09-24-lane-n4-scGOM2.md`. Job: find Gomberville's *seconde partie* as readable
text, since csGOM (18:02) showed both known Gallica arks are copies of the *Première partie* (content ends
before 1591) and flagged that Bourdeau's own "t.2, no hit" search most likely ran against one of those by
mistake.

**Found: Google Books `H2eV4wAmIr0C` is the genuine seconde partie**, distinct from `ztkvMWA_yO0C` (a second
Google Books scan of the same Première partie already ruled out on Gallica). Confirmed by title page, read via
the `jscmd=SearchWithinVolume` snippet API (`books.google.com/books?id=<id>&q=<term>&jscmd=SearchWithinVolume`,
per this lane's accessInfo/searchInfo-only route): `ztkvMWA_yO0C` page PP7 = "PREMIERE PARTIE... A PARIS, LES
ARTSA LYGA Chez THOMAS IOLLY"; `H2eV4wAmIr0C` page PP5 = "SECONDE PARTIE... A PARIS, Chez THOMAS IOLLY", page
PP6 = "TABLE GENERALE DES MATIERES CONTENVES DANS CETTE SECONDE PARTIE". Both volumes are `FULL_PUBLIC_DOMAIN`,
`ALL_PAGES` viewable (Google Books API `volumes/<id>?country=US&key=$GOOGLE_BOOKS_KEY`).

**Full-text search of `H2eV4wAmIr0C` for this letter's own terms, all via the same snippet API:**
- "Villeroy": 10+ hits. One letter is headed to Villeroy directly, p. 391 ("VILLEROY. MONSIEVR de Villeroy. I'ay
  veu par le contenu de vostre lettre, la sommation que vous m'auez faite de vouloir m'empescher la cheute de ce
  ..."), grouped in the table of contents with several other short letters on consecutive pages (391-393, to
  La Grange, Servieres, Blancmesnil) — a different, unrelated cluster, nowhere near the Cambrai/Fuentes/Doullens
  subject matter or "16 Aoust" (no "16. Aoust" hit anywhere near p. 391; the two "16. Aoust" hits in the whole
  volume, pp. 16 and 625, are unrelated 1572- and undated-context passages).
- "Doullens" / "Fuentes" / "Cambray" / "Balagny": dense cluster at pp. 710-732, matching this letter's own
  subject (relief of Cambrai, besieged by Fuentes, loss of Doullens, Cambrai's governor Balagny) almost exactly.
  But this is a **different letter**: it closes "... comme prouenant de celuy qui est, MESSIEVRS, Vostre
  tres-humble..." (p. 732) — addressed to a plural "Messieurs" (a council or deputies), not to Villeroy alone,
  and searches for "S. Quentin" (this letter's own dateline place) return 10 hits, none in the 700s page range,
  and "mesprendre" (from that same Aoust-1595 passage, "de peur de me mesprendre") independently confirms the
  content but not the address. Not this letter.
- The letter's own clear-text sentence explaining why cipher is used ("... ce qui est de plus pregnant seroit bon
  d'estre en chiffre ... affin que 72 ne puissent prendre cognoissance de noz affaires"): searched as "pregnant"
  (0 hits) and "cognoissance de noz affaires" (0 hits) verbatim. Absent.

**Verdict: `open -- Gomberville 1665 seconde partie (Google Books H2eV4wAmIr0C), full-text searched (Villeroy,
Cambray, Doullens, Fuentes, Balagny, S. Quentin, 16 Aoust, the letter's own cipher-explaining sentence), letter
absent.`** The edition does print a different, non-cipher letter about the same Cambrai crisis (pp. ~710-732,
addressed to "Messieurs") and a different, unrelated Villeroy letter (p. 391) — neither is this letter. Hold
lifted; re-nominated (see ROOM.md and QUEUE.md CS2-26).

Credit: unchanged (D. Bourdeau, cyphersolver; his own "t.2, no hit" search is now independently corroborated
against the correct tome, resolving csGOM's flag that it may have run against the wrong ark). Rule 10: no
novelty claim made; this is a search result, not a verifier's classification.

Requests this section: www.googleapis.com 2 (volume metadata for both ids), books.google.com ~15
(`jscmd=SearchWithinVolume`, >=2s apart, `cipher-lab research script (contact via repository)` User-Agent). No
gallica.bnf.fr, HathiTrust, BSB, ONB or archive.org used (Google Books gave readable text at the first routing
step).

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/targets/nevers1595/NOTES.md
- Their extent, in their words: attempted, closed from the evidence, not read; key not among surviving Nevers keys
- Their date: 22 Sept 2026
- Note: already cited in our NOTES.md
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## Web and blog check (GF4-BATCH9, account-4, 3 Oct 2026)

Plain web searches (WebSearch, 3 Oct 2026):
1. `Nevers Villeroy Saint-Quentin 16 août 1595 lettre chiffre Cambrai Doullens` returned the BnF fr.3974-3995 finding aid,
   historyofwar.org's siege of Cambrai, Wikipedia pages (Nevers, Doullens, Villeroy) and a Gallica Leuridan volume.
   There was no decipherment and no transcription of this letter.
2. `"français 3993" OR "fr. 3993" Nevers chiffre 1595` returned only number-spelling and Wikipedia noise.
3. The letter's own clear phrase, `"ne puissent prendre cognoissance de noz affaires" OR "seroit bon d'estre en chiffre"`,
   returned no exact hit (DMF, Montaigne and Gutenberg noise only).
4. For the folder title and the BnF record, the live fr.3993 finding aid (archivesetmanuscrits.bnf.fr/ark:/12148/cc504266/cd0e37708)
   was fetched by curl; see Premise check (c).
Blogs: `Nevers 1595 cipher Villeroy site:scienceblogs.de OR site:ciphermysteries.com OR site:cryptiana.blogspot.com`.
- Cryptiana blog, 2018 archive page (cryptiana.blogspot.com/2018), opened and read with its comment text. It names
  Tomokiyo's fr.3995 Nevers catalogue and the fr.4715 post, with no mention of fr.3993, Villeroy or 1595.
- Cipherbrain hits (Biermann's 17th-century letters; the German conquistador cryptogram) are unrelated.
- No Cipher Mysteries hit.
Tomokiyo's League page, as cited by Bourdeau above, says "Undeciphered". Nothing found.

## Premise check (GF4-BATCH9, account-4, 3 Oct 2026)

(a) **Decipherments the folder mentions: none of this item.** The folder names no gloss or clear copy of no.102. The
live BnF record reads "102 Lettre, avec chiffre, de LOUIS DE GONZAGUE, duc DE NEVERS, à monseigneur de Villeroy,...
De St Quentin, ce 16 aoust 1595. Copie." It says "avec chiffre", without the "et déchiffrement" the catalogue uses
elsewhere. The leaf is Nevers's file copy, so the as-sent letter (Villeroy's side) is the one place a decipherment
could sit. Not found.
(b) **Other solvers' working files: not found.** Checked dbourdeau/cyphersolver `targets/nevers1595/` (shallow clone,
HEAD 4aedb40, 2 Oct 2026). It holds the transcriptions, hsolve.py/hsyl.py with control logs and anneal.py. There are no
plaintext outputs, and no key renders French. Its NOTES.md still reads "attempted, closed from the evidence (not read)".
aaymeloglu/unsolved-ciphers (shallow clone, HEAD d2800bb) has no "3993" or Villeroy-1595 file.
(c) **Physical neighbours: no clear copy found in the catalogue.** The live finding aid lists:
- f.145 no.100, d'Auchi to Nevers, St Quentin, 14 Aug 1595;
- f.146 no.101, Longueville, 15 Aug;
- f.148 no.102, this letter;
- f.150 no.103, Charles de Gonzague-Clèves, 16 Aug, copy;
- f.151 no.104, Trumelet, Cambrai, 16 Aug, copy;
- f.152 no.105, Petit, Cambrai, 16 Aug, copy.
None is marked "chiffre" or "déchiffrement". Bourdeau checked sibling no.133 (18 Aug, to Villeroy) and found it all
clear. This worker did not view ff.147v/149v at native resolution, so that view is still to do (cheap, depends on
nobody).
(d) **Recipient side: not found.** Villeroy, *Mémoires d'Estat* (1622, archive.org memoiresdestat01vill, 02vill and
03vill) was searched in full in the OCR text. There were 4 and 6 "Cambray" hits in vols 1 and 3, and 0 hits for
Doullens, Fuentes, Quentin or "aoust 1595". Nevers appears only in other contexts (vol. 3 l.8045 "receus de feu M. de
Neuers qui me conuioit de me haster pour le secours" is a later narrative, not this letter). These are long-s OCR
texts, so this is a conditional negative. The 1665 "Second volume ... recueillis de diuers manuscrits" was not
searched.

Verdict after this pass: `open` stands. Next steps per the sections above: the fr.3995 keys outside nos.60/65/66/68-76,
the as-sent letter in Villeroy's papers, and the ff.147v/149v native view. All of these depend on nobody, so no
"While waiting" section is needed.
Requests this pass: archivesetmanuscrits.bnf.fr 1, books.google.com 4, archive.org 4 (1 advancedsearch, 3 djvu.txt),
cryptiana.blogspot.com 1. Rule 10: no novelty claim; these are search results.

## ff.147v/149v native view and fr.3995 nos.48-51 (VILL-147, account 1, 3 Oct 2026)

Brief `.claude/briefs/runs/2026-10-03-acct1-vill-147.md`. Intake gate 09:44 UTC: "open (line 1) -- edition/page or
full-text-search citation found within 6 lines", exit 0. Gallica canvases placed from a 700 px contact sheet of canvases
160-163 (the volume is shot as two-page spreads: 160 = f.146v|147r, 161 = f.147v|148r, 162 = f.148v|149r, 163 =
f.149v|150r). Crop step (native, then rotated by hand because both versos are written sideways/upside down):

    python3 tools/iiif_lines.py --ark btv1b9059229n --canvas 161 --region 1500,3000,1900,1000 \
        --out ciphers/fr3993-villeroy-1595/images --prefix f147v --debug     # -> f147v_rot180.jpg
    python3 tools/iiif_lines.py --ark btv1b9059229n --canvas 163 --region 1900,2600,1800,2300 \
        --out ciphers/fr3993-villeroy-1595/images --prefix f149v --debug     # -> f149v_rot_ccw.jpg, read_f149v_docket.jpg

**(1) ff.147v and 149v: no decipherment, no gloss, no cipher.**
- f.147v (the blank verso closing the preceding letter, no.101) carries only an address: "A Monsieur / Monsieur de
  nevers". It belongs to no.101 (Longueville to Nevers), not to this letter.
- f.149v (the verso of this letter) carries a secretary's docket, read at about 1x native, every word M:
  "[Coppie de la lettre de Monseig]neur / a Monsieur de Villeroy / l'original de laquelle a / este envoyee par
  [struck: un laquais du Roy; interlined: a word read 'Bagne'/'Loris', not settled] / ensemble une coppie / de
  plus[ieu]rs l[ett]res que / Monseig[neu]r a escrit a sa Ma[jes]te / des 23 et 25 Juillet / 3. 6. 13[?], et dern[ier] /
  Aoust 1595 avec un / extraict de no[uve]lles / venues de Doncheri. / [two lines not read, one ending '77', the last
  '... le Roy']". It describes the packet; it holds no key, gloss or clear rendering of the cipher runs. The '77' in the
  unread line is noted only: it may be a date, a count or a code number, and nothing here settles which.
- What it adds: the original went to Villeroy in a packet with copies of Nevers's letters to the King of 23 and 25 July
  and 3, 6, 13[?] and the last of August 1595, plus news from Donchery. So the as-sent copy, if it survives, sits with
  that packet on Villeroy's side, and Nevers's letters to Henri IV of those dates (his own file copies are likely in this
  same volume or fr.3992-3994) may share the cipher. These are candidate siblings for pooling, not yet looked at.

**(2) fr.3995 nos.48-51 (f.90-91v, canvases 175-178, `btv1b525085665`): not testable against this letter.** One
1100 px contact sheet (`images/fr3995/sheet_f175_178.jpg`). f.90r is a cover, "Chiffres de lettres interceptees" (Mayenne
with Aumale, with Villars, ...); f.90v and f.91r are Mayenne-Aumale symbol alphabets (a-z each with one or two symbols,
pi-like and Delta-like forms among them, double-letter and small-word signs); f.91v is Mayenne-Villars, a shifted-letter
alphabet with symbols for some words and names. None of the four uses figures as substitutes. The target's own
transcription (Bourdeau, `bourdeau/ct_*.txt`) is 753 signs, of which 445 are figures (1-9 and o) and 308 are other signs,
so a symbol-only table can cover at most 308/753 = 0.409 of it, under the brief's pre-registered 0.5 coverage floor
(brief, committed before this run): **not testable**, not a negative. No table was transcribed, no score run, no control
needed. These are also League (Mayenne) intercept keys, a poor design and party match for a royalist Nevers to
Villeroy letter. Tomokiyo's descriptions of the remaining fr.3995 keys that mix figures and symbols in 1591-93 and are not
in Bourdeau's checked set (no.39 f.72, 1591, intercepted, symbols and figures; no.40 f.74, Aug 1591; no.43 f.80, 1591;
no.58 f.104, Jul 1593) are the ones with the target's shape; none was viewed here.

Grade counts: H 0, C 0, S 0, M 0, I 0 (nothing read in the cipher). Requests: gallica.bnf.fr 12 (4 + 4 overview images,
2 native regions, 1 info.json, 1 from iiif_lines), about 1.6 s apart, no block. Vision calls 4 (one over the planned 3:
the first rotation of f.149v was upside down). Rule 10: no novelty claim; search and view results only.

Verdict after this pass: `open`. Next steps, cheapest first: (a) [done, VILL-KEYS below] fr.3995 nos.39, 40, 43 and 58
viewed for the figure+symbol family; (b) Nevers's
letters to Henri IV of 23 and 25 July and 3-31 Aug 1595 located in fr.3992-3994 (finding aid, disk/one host, ~$2) and
checked for the same cipher, to pool signs; (c) the as-sent packet on Villeroy's side (Villeroy papers). All depend on
nobody.

## fr.3995 nos.39, 40, 43, 58 for the figure+symbol family (VILL-KEYS, 3 Oct 2026)

Pre-registered before any image was viewed: `fr3995/PREREG-VILL-KEYS.md` (commit 76fb0713): a table is family-bearing
only if it shows figure codes AND at least 3 of lambda, pi, theta, Delta, varpi, infinity as cipher values; score
(judge + 200 value-shuffled keys, rank and z) only for a family-bearing table at coverage >= 0.5.

Canvases (`tools/gallica_folio.py btv1b525085665`): f.72r f143, f.72v f144, f.74r f147, f.80r f158, f.104r f202, all from
the manifest's own labels. Crops (iiif_lines.py, regions native, then 2 contact sheets, 2 vision calls):

    python3 tools/iiif_lines.py --ark btv1b525085665 --canvas {143,147,158,202} --region 0,0,4000,3000 --out <scratch> \
        --prefix c<N> --lines-per-crop 200 --max-width 2400 --debug           # -> images/fr3995/vk_sheet1_f143_147_158_202_top.jpg
    python3 tools/iiif_lines.py --ark btv1b525085665 --canvas N --region R --out <scratch> --lines-per-crop 200 --max-width 2400
        # 143 1000,3000,3000,3000; 144 0,1200,4100,3000; 147 1300,2600,2700,3000; 158 1800,2600,2200,3000;
        # 202 1700,0,2400,3000; 202 1700,3000,2400,3000                      -> images/fr3995/vk_sheet2_bodies.jpg

What the sheets show (all at about 0.37x native, every observation M):
- **f.72 (no.39)**: a small slip mounted low on the guard; f.72r shows "1591" and a vertical endorsement on the left edge
  (an "extraict"/"coppie" docket, not read), f.72v a vertical endorsement beginning "Chiffre ...". No table in either
  region viewed. The 1591 "symbols and figures" table Tomokiyo describes was not seen here.
- **f.74r (no.40)**: heading "Doncheri 1591 20 Aoust", "Chiffre". A letter strip across the top with one- and two-figure
  codes under the letters, then a two-column nomenclator of names with two- and three-figure numbers. No lambda/pi/theta/
  Delta/varpi/infinity identifiable at this resolution. Donchery is the place of the "extraict de nouvelles venues de
  Doncheri" in the target's own f.149v docket.
- **f.80r (no.43)**: heading "... 22 Novem 1591", "Chiffre"; the rest of the slip in the region viewed is blank (table
  presumably on the verso, f.80v, canvas f159, not viewed).
- **f.104r (no.58)**: heading "...tangi 1593 23 Juillet", "Chiffre". A letter strip at top with figure codes (11, 12, 13
  ... legible) and one or two non-figure signs (an x-like and a Delta-like mark under the right-hand columns, M), then a
  nomenclator of persons (Montpensier, Rosny, Baron de ..., D. de Parme ...) with two-figure numbers about 60-99.

**Result: no table is family-bearing by the pre-registered rule 1** (none shows 3 of the 6 family signs), so no score was
run and no control was needed: **not testable** for these four tables, not a negative. Caveat: the resolution cannot
exclude small symbols in the f.74r and f.104r letter strips. Those two are figure tables; under rule 2 alone their figures
would cover 445/753 = 0.591 of the target, so a figure-only test is possible, but only after their letter strips are read.

Grade counts: H 0, C 0, S 0, M 0, I 0 (nothing read in the cipher). Requests: gallica.bnf.fr 10 region fetches + 1
cached manifest read, about 2 s apart, no block. Vision calls 2 (as planned). Rule 10: no novelty claim.

Verdict after VILL-KEYS: `open`. Next steps, cheapest first: (a) native read of the f.74r (Doncheri, 20 Aug 1591) and
f.104r (23 Jul 1593) letter strips, two crops each (~$3), checking for the family signs at native resolution and, if
coverage >= 0.5 holds, scoring them under PREREG-VILL-KEYS rule 3 with the value-shuffled control; (b) f.80v (canvas f159)
viewed for no.43's table (~$1.5); (c) [done, VILL-SIBS 3 Oct 2026: the six digitised Nevers-to-King letters,
fr.3993 ff.40/46/82/99/204/235, are clear; fr.3994 ff.6/44 not digitised; no pool. One same-sender cipher
letter found instead: fr.3994 f.134, Nevers to his son, 17 Sept 1595, not digitised, needs a reproduction]; (d) the as-sent packet on Villeroy's side
(Villeroy papers finding aids, ~$3). All depend on nobody.

## Nevers to Henri IV, 23 Jul - 31 Aug 1595: located, none in cipher (VILL-SIBS, account 1, 3 Oct 2026)

Brief `.claude/briefs/runs/2026-10-03-acct1-vill-sibs.md`. Intake gate 10:04 UTC: "open (line 1) -- edition/page or
full-text-search citation found within 6 lines", exit 0. Job: find the letters VILL-147's f.149v docket names (copies of
Nevers to the King of 23 and 25 Jul and 3, 6, 13[?] and last of Aug 1595, sent in the packet with the original of no.102),
and say which carry cipher.

**Source.** BnF archivesetmanuscrits finding aid for Français 3974-3995 (ark:/12148/cc504266; the page serves the whole
dépouillement), fetched by curl 3 Oct 2026, grepped for Nevers letters "au roi/au roy" dated 20 Jul - 31 Aug 1595.
Availability flags read on the volume records: fr.3993 (cd0e33226) "Version numérisée ... gallica.bnf.fr/ark:/12148/
btv1b9059229n"; **fr.3994 (cd0e35499) carries no "Version numérisée" line, i.e. not digitised** (Tomokiyo's League page,
`sources/cryptiana/web/league.htm` l.646-649, also says "Images not available online"). fr.3992 ends 30 Jun 1595 (its
last Nevers items are June), so it holds none of these dates.

**Canvases.** The fr.3993 manifest has no folio labels (279 canvases, all "NP"), so `tools/gallica_folio.py` cannot map
folios; canvases were placed by reading the folio number and date on 808 px thumbnails. The canvas-folio offset drifts
(+7 at f.46, +9 at f.82-104, +13 at f.204, +14 at f.235), so VILL-147's +13 anchor at f.148 does not carry back.

| date (docket) | catalogue entry | shelfmark, folio | Gallica canvas | catalogue flag | seen at 808 px |
|---|---|---|---|---|---|
| 23 Jul 1595 | no.21, Nesle, minute | fr.3993 f.40 | 47 (right) | none | clear French prose, heavy deletions; no cipher run |
| 25 Jul 1595 | no.26, Amiens "mardy 25 juillet au soir", minute | fr.3993 f.46 | 53 (right) | none | clear; no cipher run |
| 3 Aug 1595 | no.47, Amiens, minute | fr.3993 f.82 | 91 (right) | none | clear ("Sire, Je ne diray point..."); no cipher run |
| 6 Aug 1595 | no.63, Corbie, copie | fr.3993 f.99 | 108 (right) | none | clear, short; no cipher run |
| "13[?]" Aug | no letter to the King dated 13 Aug in the catalogue; nearest is no.134, St Quentin 18 Aug, copie (the docket's "13" may be "18", not settled) | fr.3993 f.204 | 217 (right) | none | clear; no cipher run |
| (not in docket) | no.157, St Quentin 23 Aug, copie | fr.3993 f.235 | 249 (right) | none | clear, dense; no cipher run |
| (not in docket) | no.5, St Quentin 26 Aug, copie | fr.3994 f.6 | not digitised | none | not seen |
| last of Aug 1595 | no.34, St Quentin "ce dernier d'aougst 1595", copie | fr.3994 f.44 | not digitised | none | not seen |

Contact sheets (committed): `images/sheet_sibs_c53-249.jpg` (canvases 53, 54, 59, 60, 95, 96, 112, 113, 217, 218, 248, 249;
the first pass, which found the offset drift) and `images/sheet_sibs2_c47-108.jpg` (47, 89, 90, 91, 108). Every 808 px
thumbnail was fetched as `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9059229n/f<N>/full/808,/0/native.jpg`.

**Result.** All six digitised letters (ff.40, 46, 82, 99, 204, 235) are clear prose at contact-sheet resolution, and the
catalogue marks none of the eight "avec chiffre" (it does mark no.102 itself, and every Balagny/Petit/Charles cipher
letter in the same weeks). So Nevers's own file copies of his letters to the King in July-August 1595 do not supply a
pool of the no.102 cipher: **pooling from this set: none found** (conditional on 808 px, where a short cipher run inside a
line could be missed; a foot-of-page block like no.102's is visible at 500 px, per the check-solved section above). The two
fr.3994 letters (26 and 31 Aug) were not seen; the catalogue does not flag them either. Inferred, not checked: the docket's
packet copies were probably clear, and the cipher in no.102 was for Villeroy alone (the letter's "affin que 72 ne
puissent prendre cognoissance de noz affaires").

Grade counts: H 0, C 0, S 0, M 0, I 0 (nothing read in the cipher). Vision calls: 2 contact sheets (1 over the planned 1:
the first sheet's +13 offset guess missed ff.40, 82, 99). Requests: archivesetmanuscrits.bnf.fr 4 (1 reset, retried once
after 20 s), gallica.bnf.fr 18 (12 + 5 thumbnails + 1 retry after a connection reset; 1 SRU query, 0 records), 1.6 s apart.
Rule 10: no novelty claim; search and view results only.

**Pooling next step, priced.** Not within Nevers-to-King. The remaining pool candidates are: (i) other Nevers outgoing
letters "avec chiffre" in fr.3993-3994 (grep of the whole dépouillement of both volumes for "chiffre" in a Nevers-sender
entry): exactly one besides this letter, **fr.3994 f.134 no.102, Nevers "à son filz [the son is presumably Charles, duc de Rethelois; inferred]...  De St Quentin,
ce XVIIe septembre 1595", avec chiffre (no déchiffrement), original not marked copie** -- same sender, same place, one
month later, the only same-sender pool candidate found. fr.3994 is not digitised, so it needs a BnF reproduction
(owner step; a quote request for one leaf, f.134r-v); worth it only if the sign family matches, which cannot be judged
without the image. Charles's own letters to Nevers in these weeks (fr.3993 f.71, f.254; fr.3994 f.1, f.41) use cipher
no.70 per Tomokiyo, a different direction and a key already ruled out for no.102 by Bourdeau; (ii) the as-sent packet
on Villeroy's side (Villeroy papers, BnF fr.15xxx / Cinq Cents de Colbert), a catalogue search, one host, ~USD 3 for a
finding-aid worker; (iii) fr.3994 ff.6/44 seen only by a BnF reproduction order (owner, low value given the catalogue's
silence; not filed).

## fr.3995 nos.40 and 58 letter strips read and scored (VILL-STRIPS, account 1, 3 Oct 2026)

Brief `.claude/briefs/runs/2026-10-03-acct1-vill-strips.md`. Intake gate: "open (line 1) -- edition/page or full-text-search
citation found within 6 lines", exit 0. Pre-registered before any strip was read: `fr3995/PREREG-VILL-STRIPS.md` (commit c93ea117).

**Correction to VILL-KEYS.** The faint "letter strips" seen on f.74r (canvas f147) and f.104r (canvas f202) are show-through:
at native resolution the figures on f.74r read mirror-image (`images/fr3995/f74r_lines_debug.jpg`), and the dark recto ink is
only the heading ("Doncheri 1591 20 Aoust" / "...tangi 1593 23 Juillet", "Chiffre"). The tables themselves are on the versos:
**f.74v = canvas f148** (5440x3646, landscape: alphabet strip, Nulles box, then Noms generaux / Provinces / Noms propres /
Villes nomenclator) and **f.104v = canvas f203** (5054x3635: alphabet strip, Nulles, nomenclator of persons and Villes).
The step was run on the verso strips.

Crops (pasted):

    python3 tools/iiif_lines.py --ark btv1b525085665 --canvas 148 --region 200,30,4600,620 --out <scratch> --prefix f74v_strip \
        --centres 150,300,450 --lines-per-crop 200 --max-width 1200 --overlap 100      # 5 segments
    python3 tools/iiif_lines.py --ark btv1b525085665 --canvas 203 --region 500,180,4000,700 --out <scratch> --prefix f104v_strip \
        --centres 150,300,450 --lines-per-crop 200 --max-width 1100 --overlap 100      # 4 segments
    # committed: images/fr3995/f74v_strip_L01_s1-5.jpg, f104v_strip_L01_s1-4.jpg (manifest.json "iiif_lines")

Keys (one blind read per strip, every cell M; nulls of f.104v I, read only at 700 px):
- **f.74v (no.40, Doncheri 20 Aug 1591)** `keys/key_f74r_letters.tsv`: a-z (23 letters) = even 10-52 (a 10, b 12, ... z 52),
  plus odd homophones 11-37 (a 21, c 11, e 23, f 13, h 15, i 31, m 17, n 33, p 19, r 35, s 25, u 37, x 27, z 29) and symbol
  homophones (theta-barred, phi, upsilon, x-bar, #, R, alpha, beta, hatched x, triangle, T, square, reversed c, I, double-barred =,
  triple #, gamma, epsilon, A); Nulles 39 41 45 47 49 51, infinity, double-barred H, Z, open bracket.
- **f.104v (no.58, 23 Jul 1593)** `keys/key_f104r_letters.tsv`: mixed one- and two-figure codes: a 6 5, b 2, c 3 4, d 8 7, e 11 12,
  f 15 16, g 17, h 18, i 19 20, l 9, m 22 23, n 24 25, o 27 28, p 13, q 14, r 30 31, s 33 34, t 36, u 38 39, x 42, y 44, z 46;
  symbols: Delta with cross (a), double-barred x (e), open diamond (i), square (o), circle with cross (u). Nulles (I): 32 35 37 40 41 43 45.

Family signs: the f.74v strip carries infinity (as a null) and theta-like and reversed-c signs; f.104v carries a Delta-like
sign. Neither carries lambda, pi or varpi, the target's commonest symbols (L 17, P 13, V 12). No target sign was certified
identical (no target image viewed in this job), so per PREREG rule 2 only figures count.

**Gates and score** (`strips_score.py`, regenerates `strips_score.tsv`, `--check` exits 1 if stale; fr16 4-gram model of
`tools/judge_plaintext.py`; figure tokens segmented two-figure-first when the pair is a key code, 'o' = 0, signs dropped):

| strip | coverage | reader err | power (rank 1 of 201, 20 synthetic French texts, same length/coverage/segmentation) | target letters | target score | rank / 201 | z | verdict |
|---|---|---|---|---|---|---|---|---|
| f.74v no.40 | 0.591 | 0.015 | 20/20 | 146 | -2.201 | 107 | -0.13 | FAIL |
| f.104v no.58 | 0.591 | 0.152 | 18/20 | 217 | -2.107 | 41 | 0.83 | FAIL |

Both strips clear the coverage gate (0.591 >= 0.5) and the power gate (>= 16/20), so both are **control-backed negatives
for the figure part of the target under these two alphabets** (the real key scores no better than value-shuffled keys).
Conditional on: Bourdeau's transcription (no image check of the target's figures in this job); the two-figure-first
segmentation; and signs dropped (41% of tokens unread). Decodes by eye show no French either (f.104v begins
"ipbemeidqgafbdeaog..."). No reading committed; judge_plaintext.py not run because there is no reading to report
(nothing passed). Grade counts: H 0, C 0, S 0, M 0, I 0 in the cipher.

Requests: gallica.bnf.fr 4 info.json + 2 thumbnails (700 px) + 4 native regions, about 2 s apart, no block. Vision reads: 6
(1 earlier contact sheet, 2 debug overlays, the f.74r show-through stack, 1 verso thumbnail pair, 2 verso strip stacks).
Rule 10: no novelty claim.

Verdict after VILL-STRIPS: `open`. Next steps, cheapest first: (b) f.80v (canvas f159) for no.43's table, and check whether
f.72v (canvas f144) carries no.39's "symbols and figures" table on the facing side, as nos.40 and 58 did (~$2, one thumbnail
sheet then a strip read; same script, new key file); (e) a target-image pass on the f.148r-149r cipher runs, settling which
target signs are figures vs symbols and whether 'o' is a 0 or a sign, before any further figure-key test (~$5); (d) the as-sent
packet on Villeroy's side (finding aids, ~$3). All depend on nobody.

## fr.3995 f.72v and the no.43 table (canvas f159) (VILL-7280, account 1, 3 Oct 2026)

Brief `.claude/briefs/runs/2026-10-03-acct1-vill-7280.md`. Intake gate: "open (line 1) -- edition/page or full-text-search
citation found within 6 lines", exit 0. Pre-registered before any image was viewed: `fr3995/PREREG-VILL-7280.md` (commit 7252c082),
rules unchanged from PREREG-VILL-STRIPS.

**f.72v (canvas f144, no.39): no table.** The verso of the small 1591 slip carries only a docket written sideways, "+ 1591 /
Chiffre extraict d'une lettre ... escrite ... pour son secretaire" (thumbnail at 900 px, not read further); the rest is blank,
and there is no mirrored ink suggesting a table on f.72r either (VILL-KEYS saw only "1591" and the endorsement there). Whatever
"symbols and figures" Bourdeau's checked set lists for no.39 is not a table on f.72. Canvas f143 answered 503 once (not retried).

**f.80 (no.43).** f.80r (canvas f158) is a small slip mounted on a guard: "... + 22 Novem 1591 / Chiffre", foliated "80", with a
ruled-table show-through. The next canvas, **f159, is a full leaf foliated "81" in ink** (manifest: f158 = 80r, f160 = 81v; no
separate 80v canvas was found), carrying a complete table written sideways: alphabet strip down the right edge, a "Nulles" box
(about six symbols), and a nomenclator of Picardy places (Abbeville, Rue, Amiens, Corbie, S Quentin, Moreuil, Compiegne) and
persons (Mr de Longueville, Mr de Humieres, ...) with two-figure codes 20-80. The ink reads the right way round (not show-through).
Its attribution to no.43 is likely (heading on f.80r, show-through of a ruled table) but not certified.

Crops (pasted):

    python3 tools/iiif_lines.py --ark btv1b525085665 --canvas 159 --region 4060,220,520,3460 --out <scratch> --prefix f159_strip \
        --centres 430,1290,2150,3010 --lines-per-crop 1 --max-width 2400 --overlap 100 --debug      # 4 bands
    # committed: images/fr3995/f159_strip_L01-4.jpg + f159_strip_rotated_stack.jpg (bands rotated 90 deg CCW for reading)

Key (one blind read, `keys/key_f159_letters.tsv`): figures cover only eight letters -- a 19 18, b 16, c 15 14, d 13 12, e 11 10,
i 7 8 6, l 5 4, o 3 2 1 (8 and 1 graded I) -- and every other letter is a symbol: f epsilon-like, g N-with-flourish, h alpha/cross
loop, m omega, n psi, p curly phi/varsigma, q overbarred zigzag, **r lambda**, s two cross-hatched stars, t v, u a thick pi-like p,
x +, y square; the z column is cut off at the leaf edge (not read).

**Family signs: this table carries lambda (= r), a pi-like sign (u) and an infinity-free Nulles box** -- the first fr.3995 table
seen in this folder with the target's commonest symbol (lambda, 17 in the target). Not certified identical to the target's
lambda (no target image viewed in this job).

**Gates** (`strips_score.py`, now three rows; `--check` exits 0):

| table | coverage | reader err | power (rank 1 of 201, 20 synthetic French texts) | target letters | score | rank | z | verdict |
|---|---|---|---|---|---|---|---|---|
| f159 (no.43?) | 0.591 | 0.065 | **8/20** | 282 | -- | -- | -- | **non-test** (power < 16/20, stop before scoring) |

Rule 3, both numbers: control power 8/20 against the pre-registered 16/20, so the target was not scored. Why: the figures here
spell only a b c d e i l o, so a figure-only decode is an eight-letter text whose 4-grams cannot separate the real key from value
shuffles. This is not a negative for the table. By eye the figure-only decode is dominated by 'o' (the target's 1/2/3 figures):
"alododoodaicoooillocoloidioi...". Grade counts in the cipher: H 0, C 0, S 0, M 0, I 0 (nothing read).

Requests: gallica.bnf.fr 4 thumbnails (900 px; one 503) + 1 manifest pass (tools/gallica_folio.py, twice) + 1 info.json + 1
native region, about 2 s apart. Vision reads: 4 (thumbnails f159+f144 together, f158, the rotated strip stack). Rule 10: no novelty claim.

Verdict after VILL-7280: `open`. Next steps, cheapest first: (e') a target-image sign pass on the f.148r-149r cipher runs that
settles which target signs match this table's symbols (lambda, the pi-like u, omega, psi, v, +, square, stars), then rescore with
figures + certified signs -- with lambda = r and the symbols counted, the f159 key would cover nearly every token and the power
control would no longer be an eight-letter text (~$5 image pass + ~$1 rescore, power gate first); (f) read the f159 Nulles box and
the nomenclator codes 20-80 (the target's two-figure groups such as 72 for the Spanish may be nomenclator codes, cf. "72 ne
puissent" in the clear) (~$2); (d) the as-sent packet on Villeroy's side (~$3). All depend on nobody.

## Target signs vs the f159 table, power gate (VILL-SIGNS, account 1, 3 Oct 2026)

Brief `.claude/briefs/runs/2026-10-03-acct1-vill-signs.md`. Intake gate 10:59 UTC: "open (line 1) -- edition/page or
full-text-search citation found within 6 lines". Target crops (pasted; the seven f.148r cipher lines, canvas 161 = f.147v|148r):

    python3 tools/iiif_lines.py --ark btv1b9059229n --canvas 161 --region 4300,4450,3300,900 --out <scratch>/t148 \
        --prefix f148r_ct --max-width 2400 --overlap 150 --debug      # 7 lines x 2 segments; committed as images/f148r_ct_stack.jpg

Table side: the committed `images/fr3995/f159_strip_rotated_stack.jpg` (VILL-7280's native crops). Vision calls: 3 (contact
sheet to place the block, the target stack, the table stack) + 1 blind Sonnet second reader given both stacks.

**Sign certification** (both readers SAME = certified; `keys/key_f159_full.tsv`):

| table letter / sign | reader A (worker) | reader B (subagent) | status |
|---|---|---|---|
| r LAMBDA | same (Bourdeau L, 16 in the target) | SAME, ~7 on f.148r | **certified** L = r |
| m OMEGA | same/like (Bourdeau w, 2) | SAME | **certified** w = m |
| x PLUS | same (Bourdeau +, 1) | SAME | **certified** + = x |
| f EPS, p VARPHI, u PTHICK, t V | like (target 3/e-like, y, crossed p, cup) | LIKE / LIKE / LIKE / NO | not certified |
| g NFL, h AX, n PSI, q ZBAR, s stars, y SQX | no | NO (g, y LIKE weak) | not in target |

The target's frequent signs pi (P 12), varpi (V 11), theta (Q 14), infinity (W 13), reversed c (R 25), T (23), double-cross
(K 13) are **not in the f159 alphabet strip** (both readers); they may sit in the table's Nulles box or nomenclator, not read.

**Power gate** (pre-registered `fr3995/PREREG-VILL-SIGNS.md`, commit 54a9a65a, before the run; `signs_score.py` -> `signs_score.tsv`,
`--check` exits 0):

| key | coverage | reader err | power (rank 1 of 201, 20 synthetic French texts) | target letters | verdict |
|---|---|---|---|---|---|
| f159 figures + certified signs | 0.616 | 0.100 | **5/20** | 301 | **non-test** (power < 16/20; target not scored, no judge run) |

Rule 3, both numbers: control power 5/20 against the gate 16/20. The certified signs add only r, m, x (19 tokens), so the decode is
still an eleven-letter text. Not a gate result, an observation: under this key 'o' (figures 1, 2, 3) is 41.2% of the decoded
letters and i 15.9% -- no French letter reaches 20% -- so the table's figure values look implausible for the target's figures
whatever the signs read. Grade counts in the cipher: H 0, C 0, S 0, M 0, I 0 (nothing read).

**Nomenclator 20-80 vs the target's code groups: not done (not on disk).** VILL-7280 read only the alphabet strip; no crop or
transcription of the f159 nomenclator exists in the folder, and the brief limited this check to disk. Named as step (f) below.

Requests: gallica.bnf.fr 1 info.json + 1 native region. Rule 10: no novelty claim.

Verdict after VILL-SIGNS: `open`. Next steps, cheapest first: (f) read the f159 nomenclator and Nulles box (native crops of the
rest of canvas f159, one blind read + check) and match codes 20-80 and the Nulles signs against the target's two-figure groups and
its pi/varpi/theta/infinity/T/reversed-c signs (~$3); if the Nulles box carries those signs, the target's symbol share is nulls and
the figure stream alone is the text -- but the 41% 'o' share already argues against the f159 figure values; (d) the as-sent packet
on Villeroy's side (~$3); (g) [done, VILL-SIBS above: the Nevers-to-King letters of 23 Jul - 31 Aug 1595
are located and none is in cipher -- no pool]. Corrected by VILL-NOMEN, 3 Oct 2026.

## f159 nomenclator and Nulles box vs the target (VILL-NOMEN, account 1, 3 Oct 2026)

Brief `.claude/briefs/runs/2026-10-03-acct1-vill-nomen.md`. Intake gate 11:17 UTC: "open (line 1) -- edition/page or
full-text-search citation found within 6 lines", exit 0. Pre-registered before any crop was viewed: `fr3995/PREREG-VILL-NOMEN.md`
(commit 657d9a39). Crops (pasted; the nomenclator is written sideways, read with the four bands rotated 90 deg CCW):

    python3 tools/iiif_lines.py --ark btv1b525085665 --canvas 159 --region 1650,250,2300,3310 --out <scratch>/nom \
        --prefix f159_nom --centres 379,1147,1938,2776 --lines-per-crop 1 --max-width 2400 --overlap 100 --debug   # 4 bands
    # committed: images/fr3995/f159_nomen_rotated_sheet.jpg (4 bands side by side), images/fr3995/f159_nulles.jpg (Nulles box, 2x)

Reads: reader A (worker, Opus) one read of the sheet and one of the Nulles box stacked over `images/f148r_ct_stack.jpg`; reader B
(blind Sonnet subagent, the same two images, no answers given). Key `keys/key_f159_nomen.tsv`: 52 two-figure codes agreed by both
readers (12-19 places of Picardy, 19-38 persons -- Longueville, la Boissiere, Vitermont, Crevecoeur, Mailly, le Roy, Guise, Aumale,
the comte de Saint-Pol --, 39-49 Rosne, Saint-Pol, Villeroy, Evesque, Lieutenant, Gouverneur, ..., 52-71 common nouns soldat,
Monsieur, Madame, cardinal, ville, village, charrette, bateau, filz, fille, femme, messager, gentilhomme, argent); no 20, 30, 40 or 70
is written; two codes disputed (capitaine 50/51, village 60/61) and left out. Grades as key values: 45 M (code and meaning agreed,
incl. the six Nulles), 15 I (meaning or code disputed). The table carries no code 72 (cf. "72 ne puissent" in the target's clear text).

**Nulles box: six symbols** -- N1 downward triangle, N2 circle with a cross above, N3 double-barred cross, N4 square on a cross stem,
N5 epsilon, N6 lozenge on a curved stem.

| target sign (Bourdeau code, count) | reader A | reader B | status |
|---|---|---|---|
| K double-crossed dagger (13) | SAME N3 | SAME N3 (~8 seen on f.148r) | **certified null** (not in the pre-registered list) |
| D Delta (1) | LIKE N1 (upright vs inverted) | LIKE N1 | not certified |
| R reversed c (25) | NO (N5 is epsilon, opens right, barred) | LIKE N5 | not certified |
| P pi, V varpi, Q theta, W infinity, T tau | NO | NO | not in the Nulles box |

**Pre-registered decision: none of P V Q W T R is a certified null**, so the power re-run was not done: **f159 nomenclator/nulles do
not explain the target's symbols** (pi 12, varpi 11, theta 14, infinity 13, T 23, reversed c 25 stay unexplained by this table).
One observation outside the pre-registered list: the target's K (13 tokens) is the table's null N3 by both readers -- a fourth shared
design element after L = r, w = m, + = x (VILL-SIGNS); removing 13 tokens would not lift the power control (5/20) because the decode
alphabet is unchanged, so no re-run was made.

**Nomenclator codes vs the target's figure pairs** (`nomen_match.py` -> `nomen_match.tsv`, `--check` exits 0; an observation, no
reading): of the target's 324 adjacent figure pairs, 199 form one of the 52 agreed codes, against 87 for random code sets disjoint
from it (200 draws, mean 87.0, p95 87). The null is confounded and says nothing: 52 of the 90 values 10-99 are codes, the disjoint
remainder is forced to the same 38 values each draw (10, 11, 20, 30, 40, ...72-99), and the target's figures are mostly 1 and 2, so any
code set rich in the teens and twenties wins. The target shows no overline on its figures in Bourdeau's transcription or on the
f.148r crops seen here; nothing on disk separates nomenclator codes from letter figures. Grade counts in the cipher: H 0, C 0, S 0,
M 0, I 0 (nothing read).

Requests: gallica.bnf.fr 1 info.json + 1 thumbnail (1000 px) + 1 native region, about 2 s apart. Vision reads: 2 by the worker,
1 subagent call (2 images). Rule 10: no novelty claim.

Verdict after VILL-NOMEN: `open`. Next steps, cheapest first: (h) a key-family check: four sign designs shared with f159 (L, w, +, K)
but the commonest target symbols (pi, varpi, theta, infinity, T, reversed c) absent from both the f159 alphabet and its Nulles, and
f159's figure values give 41% 'o' -- look in fr.3995 for a later (1592-95) Nevers table of the same family carrying pi/theta/infinity
(thumbnail sheet of the remaining canvases, ~$3); (i) homophonic cryptanalysis treating all target signs and figures as unknown
codes with K as a null, matched control first (tools/family_run.py homophonic at the target's N, ~$3; at 753 tokens expect a weak
control); (d) the as-sent packet on Villeroy's side (~$3). All depend on nobody.

## fr.3995 nos.44, 45, 52, 57 located for a later pi/theta/infinity table (A1-VILL-TABLE, account 1, 3 Oct 2026)

Brief `.claude/briefs/runs/2026-10-03-acct3-a1-wave7.md` job 3 (VILL-NOMEN step (h)). Intake gate 11:31 UTC: "open (line 1)
-- edition/page or full-text-search citation found within 6 lines", exit 0. Pre-registered before any canvas was viewed:
`fr3995/PREREG-VILL-TABLE.md` (commit 63d04072). Candidates chosen from Tomokiyo's catalogue (sources/cryptiana/web/nevers.htm):
the French 1592-93 tables mixing figures and symbols outside Bourdeau's checked set and outside VILL-KEYS/STRIPS/7280/NOMEN.
Canvases from the manifest labels (`tools/gallica_folio.py btv1b525085665 --list`). Crop/overview step (pasted; outputs in the
worker's scratchpad only, nothing committed):

    for c in 161 162 165 166 179 180 196 197; do
      python3 tools/iiif_lines.py --ark btv1b525085665 --canvas $c --out <scratch>/ov --prefix c$c \
          --lines-per-crop 200 --max-width 2400 --debug; done
    # the eight 1600 px reference copies tiled 4x2 at 620 px -> <scratch>/ov/sheet.jpg (2480x1890), one vision call

What the sheet shows (about 0.15x native, every observation M):
- **no.44 (f.82r cover "Janvier 1592"; table on f.82v, canvas f162):** a figure alphabet (a-z header, two- and three-figure
  homophones in rows) and a long nomenclator of names/titles with two-figure codes; a narrow right-hand column of symbols beside
  some entries and a few symbols in the lower names block. No pi, varpi, theta or infinity identifiable at this resolution.
- **no.45 (f.84r cover "Aoust 1592"; table on the f.84v-85r spread, canvas f166):** a dense grid of figure columns (the
  intercalary-null table Tomokiyo describes); no symbol alphabet seen.
- **no.52 (f.92r, canvas f179; f.92v, canvas f180):** an **Italian** table ("Provincie, Alamagna, Fiandra ... soldati, citta,
  ambasciatore ..."): a symbol-only alphabet (each letter two or three symbols) and symbols for words and names; no figure
  alphabet. Out of the pre-registered family (figures in the alphabet), and Italian.
- **no.57 (f.102r cover "fevrier 1593", f.102v endorsement "Mons. de Laveriere" ... "Chartres"):** canvases f196-f197 carry only
  the cover and the endorsement; **the table itself was not on the sheet** (it is presumably on the preceding opening, f.100v-101r
  canvas f194 or f.101v canvas f195, not viewed).

**Pre-registered decision: no family candidate** (figure codes in the alphabet AND at least 2 of pi/varpi/theta/infinity) among the
seven canvases viewed, so no native crops were cut and no blind reads were made: **"no 1592-93 French figure+symbol table among
nos.44/45/52 carries the target's pi/varpi/theta/infinity at overview resolution"** -- a search result at M, not a negative on the
key family, since (i) overview resolution cannot exclude a pi/theta among no.44's few symbols and (ii) no.57's table page was not
on the sheet. No sign was certified; no key written; grade counts in the cipher H 0, C 0, S 0, M 0, I 0 (nothing read).

Requests: gallica.bnf.fr 10 native/info fetches by iiif_lines (about 2 s apart) + 0 for the manifest (cached), no block.
Vision calls: see below. Rule 10: no novelty claim.

**Second locate call (no.57's table, still within the registered candidate list; no crop read, certification rule untouched):**
canvases f194 (f.100v-101r) and f195 (f.101v), same iiif_lines command with `--canvas 194` / `195`, tiled at 1250 px high
(`<scratch>/ov/sheet57.jpg`), vision call 2 of 3. f194 is **not no.57 but no.56** (fol.100, Italian): an Italian nomenclator
(Accordo, Ambasciatore, Cardinale di, Re di Spagna, Re di Francia, ...) with Italian instructions, and an alphabet header of
figures in broken squares plus a few symbols (one infinity-like sign in the header row) -- Tomokiyo's "figures in a square broken
at both sides", out of scope (Italian, square-framed figures, no figure+symbol letter of the target's shape). f195 (f.101v) is a dense
figure grid with a short docket, no symbol alphabet seen. **No.57's table was not found on ff.100v-102v**; the manifest labels
canvases f198, f199 and f200 all '103r' (duplicate labels, `gallica_folio.py`), so it is presumably there. Vision calls: 2 of 3; the
third was not spent because a found candidate would still need two blind reads (2 calls) to certify anything.

Next steps from this pass, cheapest first: (j) view no.57's table, presumably canvases f198-f200 (all labelled '103r'), the one 1593
candidate whose description (symbol homophones, figures 1-72 for two-letter syllables) fits a figure+symbol letter, one overview
plus, if it carries pi/theta/infinity, the two blind row reads PREREG-VILL-TABLE.md sets out (~$5); (k) a native crop of no.44's right-hand
symbol column on f.82v (canvas f162) to settle whether any of its few symbols is a target sign (~$3). Both depend on nobody.

## Homophonic family_run with K as null (A1-VILL-HOMO, account 1, 3 Oct 2026)

Pre-registered in `fr3995/PREREG-VILL-HOMO.md` (commit 5b97baef, pushed before any run). Every sign and figure in
Bourdeau's one-token-per-sign first pass (`bourdeau/ct_*.txt`) is treated as an unknown homophone for one letter;
K (13 tokens, = f159 null N3 by two readers, VILL-NOMEN) is removed. Cipher `homo/cipher_noK.txt`: 25 lines,
N = 740, 53 types. Spec `specs/fr3993-villeroy-1595.json` (new, written by this job). Tool: `tools/family_run.py
--family homophonic --param profile=target --restarts 8 --corpus tools/data/fr16` (homophonic_anneal, French order-3).

| run | control (fr16, N=740, K=53 allotted, target's own sign-count profile) | target best anneal score | judge (fr16, real_p05 -0.873, null_p99 -1.868) |
|---|---|---|---|
| real target, seed 1 | mean 0.764 over 3 seeds (0.981 / 0.358 / 0.953; scores -1548 / -1865 / -1622) -- gate 0.6 met | -1919.1 (8 restarts -1919 to -2000, no agreement) | **FAIL** -1.35, word cover 0.842 |
| shuffled target (floor), seed 1 | 0.981 (one seed, the same seed-1 control) | -2000.4 | FAIL -1.404 |

Reading the numbers: the control reads its own design at this N in 2 of 3 seeds, and when it reads, it scores
-1548 to -1622; the one control seed that failed scored -1865. The real target's best (-1919) sits below even the
failed control and only 81 points above the order-destroyed shuffle (-2000), and the decode shows no French by eye
("laasenoteresedeleieis..."). Per the prereg: **control-backed negative for one-sign-one-letter homophonic substitution
over Bourdeau's transcription with K as null** -- 0.764 control vs a FAIL target, both numbers above. Conditional on
(a) Bourdeau's single unmeasured transcription pass (rule 2) and (b) the token model (one sign = one letter); it says
nothing against a nomenclator with figure pairs as codes (LANE R4 N's ladder) or against a mixed letter/code table of the
f159 kind. It agrees with LANE R4 N's hsolve result (homophonic control solves, target does not) with a different
solver and with K removed. Grades: H 0, C 0, S 0, M 0, I 0 (nothing read).

Caveats: the first run's judge step crashed (spec `judge.corpora` pointed at a directory; removed, the default fr = fr16
file applies); the FAIL above is `tools/judge_plaintext.py specs/fr3993-villeroy-1595.json --file` on the same decode,
run by hand. The control realised 45-48 distinct signs because singleton homophones are not always drawn (53 allotted;
the target has 12 singletons). The shuffle floor ran with one control seed instead of three to stay inside the box
(disclosed deviation; the gate was already met). Seed 2 at 0.358 shows the control is not near ceiling at this N, so a
FAIL is informative but not overwhelming. Vision calls 0; network requests 0.

Next (one line, for the lane): (j) the same family with figure pairs segmented as codes (Bourdeau seg 1x/2x) and the
VILL-SIGNS certified signs pinned (L=r, w=m, +=x) via `--param pins` is the remaining untried variant of this instrument;
otherwise (h) and (d) above stand.

## Figure-pair homophonic family_run, K as null (A1B-VILL-PAIR, LANE-A1B, account 1, 3 Oct 2026)

Brief `.claude/briefs/runs/2026-10-03-acct1-a1b-vill-pair.md`. Intake gate 16:40 UTC: "fr3993-villeroy-1595: open (line 1) --
edition/page or full-text-search citation found within 6 lines". Pre-registered in `fr3995/PREREG-VILL-PAIR.md` (commit
cf962165, pushed before any run). Cipher `pair/cipher_pairs_noK.txt` = Bourdeau's 1x/2x segmentation already on disk
(`solver/target_pairs.txt`, nevers1595/seg.py) with the header and every K dropped:

    grep -v '^#' solver/target_pairs.txt | sed -E 's/(^| )K( |$)/\1\2/g; s/(^| )K( |$)/\1\2/g; s/  +/ /g; s/^ //; s/ $//' \
        > pair/cipher_pairs_noK.txt          # 25 runs, N = 594 tokens, K = 68 types, 146 two-figure groups

Family `homophonic` (same solver, corpus fr16 and profile=target as A1-VILL-HOMO; only the token unit changes: one figure group =
one homophone). Not pinned: the homophonic family takes no pins parameter, so L=r, w=m, +=x were not applied (disclosed deviation).

| run | control (fr16, N=594, K=68 allotted, target profile) | target best anneal score | judge (fr16, real_p05 -0.900, null_p99 -1.857) |
|---|---|---|---|
| real target, seed 1 | mean **0.733** over 3 seeds (0.860 / 0.941 / 0.399; scores -1256 / -1271 / -1459) -- gate 0.6 met | -1460.8 (8 restarts -1461 to -1500, no agreement) | **FAIL** -1.263 |
| shuffled target (floor), seed 1 | 0.860 (one seed, the same seed-1 control) | -1495.8 | FAIL -1.261 |

Reading the numbers: the control reads its own design in 2 of 3 seeds (and is not at ceiling, 0.733 < 0.95, so it can fail -- seed 3
did); when it reads it scores -1256 to -1271. The real target's best (-1461) sits at the failed control seed (-1459), only 35 points
above the order-destroyed shuffle, and its judge score (-1.263) is indistinguishable from the shuffle's (-1.261). Per the prereg:
**control-backed negative for the figure-pair homophone design (Bourdeau 1x/2x groups, one group or sign = one letter) with K as
null** -- control 0.733 vs a target judge FAIL, both numbers above. Decodes `pair/decode_target.txt`, `pair/decode_shuffle1.txt`
(the tool writes to `families/` under the same names as A1-VILL-HOMO's run; those two files were restored from git). Conditional
on (a) Bourdeau's single unmeasured transcription pass (rule 2), (b) his 1x/2x segmentation being the true unit cut, and (c) no
word codes: it says nothing about a mixed nomenclator (LANE R4 N's design, whose control reads 2-6% at this N -- untestable, not
refuted). Grades: H 0, C 0, S 0, M 0, I 0 (nothing read). Vision calls 0; network requests 0. Rule 10: no novelty claim.

Verdict after A1B-VILL-PAIR: `open`. Both controllable letter-homophone token models (one sign, one figure group) are now
control-backed negatives on the transcription as it stands; the next steps are not further solver variants on the same text but new
material or a better text, cheapest first: (j) view no.57's table (canvases f198-f200, ~$5); (k) no.44's right-hand symbol column
(canvas f162, ~$3); (d) the as-sent packet on Villeroy's side (~$3); (e') a measured second transcription pass of the f.148r-149r runs
so negatives stop resting on one unmeasured pass (~$4). All depend on nobody.
