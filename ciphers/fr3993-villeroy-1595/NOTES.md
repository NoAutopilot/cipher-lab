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
