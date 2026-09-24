# BnF Français 2980, ff.29-30: two cipher letters of Gabriel de Gramont, bishop of Tarbes (cardinal from 8 June 1530)

partial

Check-solved sweep, 23 September 2026 (started ~23:19 UTC, this section written ~23:40 UTC; `date -u` read before
writing). QUEUE row M8. Worker: check-solved M8-M11 (Sonnet, cap $8 across all four targets).

## What the BnF finding aid and Gallica leaf show

BnF finding aid (`archivesetmanuscrits.bnf.fr/ark:/12148/cc494342`, fetched 23 Sept 2026, one retry after a
connection reset):

- Fol. 29, item 21: "Lettre, avec chiffre, du cardinal Gabriel DE GRAMONT, evesque de Tarbe... à monseigneur...
  de Villandry, conseiller du roy et secretaire de ses commandemens et finances... A Rome, le XXme jour de may."
  No year given in the finding-aid snippet.
- Fol. 30, item 22: "Lettre en chiffre du cardinal Gabriel DE GRAMONT, evesque de Tarbe... Faict à Rome, le XXme
  jour de may M.D.XXX" — dated **20 May 1530**.

Both leaves viewed via Gallica IIIF (`images/f29_item21.jpg` = canvas f31, `images/f30_item22.jpg` = canvas f32,
`images/f31_item23_context.jpg` = canvas f33). Canvas-to-folio offset for this volume found by direct probing
(f41/f53/f75 misleading, f33 gave the first firm anchor via item 23's plain Latin text matching folio 31
exactly; see `images/manifest.json`).

**Both items are genuinely and heavily ciphered, confirmed by image, no key or gloss on the leaf itself:**

- **Fol. 29 (item 21):** mixed letter — ~7 lines plain French salutation, a wax seal, then **~13 lines of dense
  cipher** (numeral and symbol tokens, roughly 15-20 tokens/line, so very roughly 150-200 cipher tokens), signed
  in clear "De Gramont E. de Tarbe". No interlinear or marginal decipherment visible.
- **Fol. 30 (item 22):** **entirely ciphered**, ~25 lines filling the whole recto densely (roughly 20-25
  tokens/line, so **very roughly 500-600 cipher tokens**), continuing onto the verso where it closes and is
  again signed "De Gramont E. de Tarbe" (canvas f33, left page). No plaintext, gloss or key anywhere on either
  leaf or its facing pages.

Total extent across both items: roughly 650-800 cipher tokens, well above the M6/M7 "short letter" scale (rule
3/size caveat in QUEUE.md no longer applies at this size).

## Editions and prior art

- **Cryptiana (Tomokiyo, `sources/cryptiana/web/francis.htm`), section "BnF fr.2980 (1530)":** explicitly names
  both items — "f.29 (no.21) is a letter dated Rome, 20 May [1530], from Cardinal Gabriel de Gramont, Bishop of
  Tarbe, to Jean Breton, seigneur de Villandry... f.30 (no.22) is a letter dated Rome, 20 May 1530 from Cardinal
  Gabriel de Gramont, Bishop of Tarbe... **These undeciphered letters can be read with Gramont's cipher (1530)
  below.**" Tomokiyo gives no plaintext or transcription for either item — only the observation that the key
  applies.
- **The key itself is already published and cross-validated**, but not on this manuscript. "Gramont's Cipher
  (1530)" was reconstructed by Tomokiyo from BnF fr.3019 f.20 (a different Gramont-to-Grand-Master letter), then
  the same key was independently rediscovered by George Lasry's codebreaking in 2023 and confirmed to also read
  BnF fr.3071 f.17 (no.7) and two letters in BnF fr.3040 (f.12 no.4, f.18 no.6, "both deciphered"). None of
  those source volumes is fr.2980.
- **dbourdeau/cyphersolver** (fresh shallow clone, 23 Sept 2026) has a `gramont1529/` folder (catalogue item 6:
  Gramont, Mâcon and Langeac to Montmorency, 1529-1537) that read **fr.3071 no.7 with this exact "Gramont's
  cipher (1530)"** to ~85%, plus fr.3091 no.23 ("Gramont's cipher (1529)", a different key, read in full) and
  two other letters. His NOTES.md is explicit that "Neither site gives any plaintext... the task here was
  reading the letters, not breaking the ciphers" — i.e. he applied Tomokiyo/Lasry's published keys by hand.
  **fr.2980 does not appear anywhere in his repository** (grepped the full clone for "2980" and "gramont",
  checked every hit; none is this manuscript). *[Verifier correction, 24 Sept 2026: wrong. A fresh clone (head
  763a3b9) lists both items in `CATALOGUE.md` line 76, "Gramont to Villandry, Rome (BnF fr. 2980 nos. 21–22,
  ff. 29–30; catalogue 328): Gramont 1530 key held (gramont1529)", in its 22 Sept 2026 sweep of letters "a key
  already in hand reads", and in `gallica_sweep/bnf_candidates.txt` line 302. Bourdeau had catalogued them as
  readable with the key; he had not read them. See AUDIT.md.]*
- **aaymeloglu/unsolved-ciphers** (fresh shallow clone, 23 Sept 2026): no hit for "2980" or "gramont" anywhere
  in the repository.
- **DECODE cached catalogue** (`sources/decode/`): empty, nothing to grep (no cached catalogue file present
  this session).
- No web search run this pass beyond the Cryptiana/solver-repo checks above (in-budget triage; a full
  Gramont-correspondence edition search, e.g. Wirtz-Daviau on the 1529-30 Rome embassy noted as unchecked prior
  art in Bourdeau's own NOTES.md, is left to the solver/verifier stage).

## Verdict

**Open, verified unsolved by this sweep** (not found-solved): no source checked gives a plaintext or a
transcription of fr.2980 ff.29-30 specifically, and the only two projects that read letters in this key
(Bourdeau, and Tomokiyo/Lasry themselves) have not read this manuscript. *[Verifier correction, 24 Sept 2026: Tomokiyo names both letters as readable with the key, and Bourdeau lists them as his catalogue 328; neither gives a reading. See AUDIT.md.]*

**Reclassify kind: recovery, not cryptanalysis.** The QUEUE row scored this as "cryptanalysis" on the
assumption no key existed. A key does exist, is published, and is independently cross-validated on three other
manuscripts (fr.3019, fr.3071, fr.3040) by two different methods (Tomokiyo's reconstruction and Lasry's
codebreaking) — applying it to fr.2980 is transcription-and-substitution, not fresh cryptanalysis. Per
README's metric this is a key-based reading: a published key applied to a ciphertext for which no prior reading
has been located, in different boxes. *[Verifier correction, 24 Sept 2026: "unique solve" and "unread" removed (rule 10).]* Rule 10 still applies in full: nothing here may be called new, unpublished, first or unread
until a verifier searches for the plaintext in print (Gramont's own printed correspondence/embassy papers,
etc.) and classifies N0-N5.

Stage: **2, verified unsolved.** No copy order needed (Gallica image in hand).

## For the next worker (not done this pass — check-solved does not decode)

1. Fetch the full-resolution IIIF crops of fr.2980 f.29r (cipher portion only), f.30r-v, transcribe against the
   published "Gramont's Cipher (1530)" table (image at `cryptiana.web.fc2.com/code/francisGramont.png`, copy
   should be pulled into `img/` before transcribing, cited not copied).
2. Check Bourdeau's `gramont1529/decode.py` and alias table for the 1530 key's exact symbol-to-letter mapping
   before re-deriving it from the picture by eye.
3. Verifier must search Gramont's own printed embassy correspondence circa Rome, May 1530 (Wirtz-Daviau on
   Chabot's 1529 embassy, flagged unchecked in Bourdeau's own notes; Le Glay; Ribier; Négociations diplomatiques
   de la France series) before any "unread"/"new" wording, per rule 10 and the Dupuy 468 lesson (verifier's own
   re-dating/re-attribution widens the search, never narrows it).

## Requests this pass

gallica.bnf.fr: 1 IIIF manifest.json, 1 Pagination service call (all-"NP", unused), 1 ContentSearch (0 results,
manuscript not OCR'd), ~9 IIIF image fetches at 900px/1400px width for canvas-to-folio calibration and the two
item leaves (2 connection resets, each retried once after a pause, per the good-citizen single-retry rule).
archivesetmanuscrits.bnf.fr: 1 finding-aid page fetch (1 connection reset, retried once). github.com: 2 shallow
clones (dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers). No logins, no credentials used.

## Print check, class gate — 23 September 2026 (started ~23:44 UTC, this section written ~23:58 UTC; `date -u`
read before writing). QUEUE row M8. Worker: print-check M8 (Sonnet, cap $5).

Question: is the plaintext of either fr.2980 f.29 (no.21, Gramont to Villandry, Rome, 20 May 1530, partly in
cipher) or f.30 (no.22, entirely in cipher, same date) already in print or online, from any source. No
decoding, transcription or key-fetch attempted this pass; this is a class gate only.

**Verdict for both letters: not found in print or online after the searches below. Best-case class N3** (no
prior plaintext or decipherment located after the logged search below) for each. Status stays `open` (not
`found-solved`) — rule 5 vocabulary. This is a search result, not a claim of absence (rule 10); "unread" or
"new" wording is not used here or anywhere else until a verifier session runs the full rule-10 sweep.

### What was searched, and what it turned up

- **LP Henry VIII vol. 4 pt. 3, the exact 1530 calendar** (Gairdner; IA `11332111bsb`, Bavarian State Library
  scan of vol. "4,3", not access-restricted, full djvu.txt downloaded and grepped directly rather than via the
  fts-api snippet-only route, so this is a complete check of that volume's OCR, not a sample). Searched by
  date ("20 May 1530", "20May" item headers around item numbers 6390-6441, which bracket 8 June 1530), by
  recipient ("Villandry"), and by sender ("Gramont", "Tarpe"/"Tarbe", OCR renders "Tarbes" both ways).
  - No item dated Rome, 20 May 1530 from Gramont/Tarbe to Villandry or anyone else. The May 1530 Rome-dated
    items found (26 May, 29 May) are Miçer Mai-to-Charles-V and Salviati-to-Casale despatches, not Gramont's.
  - LP *does* calendar two other Gramont-Villandry-circle cipher letters from the same embassy, dated a few
    months earlier: **item 6244**, "G. de Gramont, Bishop of Tarbe, to Brion", Bologna, 25 Feb. [1530],
    sourced in the margin as **"Le Grand, ii. 386"** and noted "the original is endorsed 'Copie de la lettre
    escripte par Monsieur de Tarbe en chiffre a Monsieur l'Admiral'" — i.e. Le Grand's 1688 edition prints this
    Gramont cipher letter deciphered, at vol. 2 (ii), p. 386. And **item 6245**, "Bishop of Tarbe to Mons. de
    Villandry", Bologna, 27 Feb., "French. The original was in cipher.", with no Le Grand citation (a
    manuscript-only source, likely the same BM Additional MS. 28,581 series cited elsewhere in this volume for
    Gramont/Tarbes items). Neither is our target (wrong date, wrong place — Bologna not Rome), but both show
    (a) Le Grand's edition does print some of Gramont's deciphered ciphers from this exact embassy and period,
    and (b) LP separately calendars Gramont-Villandry cipher correspondence from manuscript when it exists —
    strengthening rather than weakening the negative result for our two items specifically, since the editors
    plainly had material to calendar from this correspondent/recipient pair and did not include our two.
- **Le Grand, *Histoire du divorce de Henry VIII*, 1688** (the volume LP cites above for a neighbouring
  letter). Two full-view scans located on Google Books (`t2dUAAAAcAAJ`, `rclrXxrYEwcC`); the "Preuves" volume
  specifically may be a separate bibliographic record (`TgPrvgEACAAJ`, no preview). Google Books API full-text
  queries combining `intitle:"histoire du divorce"` with "Villandry", "Tarbe" and "Villandri" each returned
  zero hits, but this method is unreliable (title-metadata filter, not a true within-book search). Direct
  inside-book search (`books.google.com/books?id=...&q=Villandry`) was attempted by curl and once more via
  `tools/browser_fetch.js` (the real-Chromium route) — both were redirected to Google's `/sorry/` bot-challenge
  page. One retry each, per the good-citizen rule; stopped, not retried further. **Gap**: Le Grand's actual
  page content for May 1530 (as opposed to the Feb. 1530 letter LP already locates there) was not directly
  verified; a future pass should try a library proxy, a different Google Books mirror, or read the physical
  volume via HathiTrust/IA if a copy surfaces. *[Second audit, 24 Sept 2026: closed. Le Grand III pp.394-542 read page by page from the
  MDZ scan bsb10280117 OCR; no Rome letter between 28 March and 20 October 1530. See AUDIT.md, second audit.]*
- **English 1690 translation** of Le Grand (IA `bim_early-english-books-1641-1700_...le-grand-joachim_1690`)
  located but not searched this pass (English translations of this work are known to abridge the "Preuves"
  documents; lower priority than the French original, not reached under the cap).
- **Decrue (de Stoutz), *Anne de Montmorency, grand maître et connétable de France*** (1885/1889 scholarly
  biography, editions on IA as `annedemontmoren00decr`, `annedemontmoren00stougoog`, `anneducdemontmor00decruoft`,
  `annedemontmoren00decr`) — a strong candidate since it cites BnF fr.2980 directly and repeatedly by item
  number for *other* letters in the same recueil (items 7, 25, 26, 27, 57, 80, all Montmorency/royal
  correspondence, none in the 20-22 range). Searched by exact phrase `"2980, 21"` / `"2980, 22"` and by
  folio form `"2980, f. 29"` / `"2980, f. 30"` in all three IA copies: **zero hits**. Decrue plainly worked
  through this volume item-by-item and did not cite ours — consistent with (not proof of) his not having
  read them. *[Wording corrected by the verifier, 24 Sept 2026, rule 10.]*
- **PUR OpenEdition**, Thierry Rentet's chapter on Jean Breton (Villandry) in *Conseils et conseillers sous
  François Ier* (`books.openedition.org/pur/120024`, fetched directly, full chapter read) — biographical detail
  on Breton/Villandry's 1530 role as Montmorency's relay at court (citing Rentet's own 2008 conference paper on
  Montmorency's 1530 correspondence, a different, Montmorency-addressed corpus at Chantilly) but **no mention
  of fr.2980, of Gramont's 20 May letters, or of their content** — this is the source Tomokiyo cites only for
  identifying who Villandry was, not for the letters themselves.
- **Bourrilly & Vindry, *Ambassades en Angleterre de Jean Du Bellay*** — only "La Première Ambassade"
  (Sept. 1527-Feb. 1529) found on IA (`ambassadesenang00bourgoog`); out of date range for a 20 May 1530 letter,
  not applicable, not searched further.
- **Internet Archive full-text search** (`be-api.us.archive.org/fts/v1/search`, no login) for `"Gramont"
  "Villandry"` together (2,479 raw hits, all titles inspected in the top page): the only period-relevant hits
  are the Decrue volumes above (already covered) and the Montmorency biography under its alternate title/
  scan (`annedemontmoren00decr` again); nothing else surfaces this specific letter pair.
- **Pocock, *Records of the Reformation* (1870); State Papers Henry VIII vol. 7; Camusat/Ribier, *Lettres et
  mémoires d'estat*; Molini, *Documenti di storia italiana*** — not reached this pass (budget cap); flagged
  below for a future pass or the verifier if the gate needs tightening beyond N3.
- **Tomokiyo/Lasry own pages** (`sources/cryptiana/web/francis.htm`, `GL.htm`, both cached, greped directly):
  confirms francis.htm's own wording — "These undeciphered letters can be read with Gramont's cipher (1530)
  below" — with no plaintext or transcription given for either item; GL.htm documents the same key's
  provenance (BnF fr.3019, cross-validated on fr.3071 and fr.3040) with no mention of fr.2980 anywhere.
  cryptiana.web.fc2.com not re-fetched (mirror of francis.htm, another worker using it per ROOM.md; the local
  cache is current as of the same-day check-solved pass).
- **Lasry's Cryptologia/other publications**: one WebSearch pass (`Lasry Tomokiyo Gramont cipher 1530
  Cryptologia fr.2980`) surfaced his Mary-Stuart-cipher work and the general Gramont-cipher-key background
  already known from GL.htm, nothing naming fr.2980.
- **General WebSearch** for the letter itself (`Gramont "Villandry" Rome 1530 lettre chiffre fr.2980`;
  `"Gabriel de Gramont" cardinal Rome mai 1530 lettre chiffrée Villandry`) returned only the BnF finding aid
  itself, Wikipedia biographical pages, and a cardinals-of-the-Church consistory list (confirms Gramont was
  created cardinal 9 March 1530, promoted 8 June 1530 — so as of 20 May 1530 he already held the cardinal's
  hat, though the manuscript signs him "E. de Tarbe"); no independent hit on the letters' content. *[Second-audit correction, 24 Sept 2026: over-claim. He was created cardinal in the consistory of
  8 June 1530 (LP iv.3 6441-6443); a March reservation is not established by the sources read, and on 20 May 1530
  he signs as bishop. See AUDIT.md, second audit.]*
- **Solver repositories**: not re-cloned this pass (the check-solved M8-M11 worker cloned both fresh the same
  day, 23 Sept 2026, and grepped for "2980"/"gramont" with no hits in either — reused rather than repeated per
  the usage rule against duplicate fetches; see that worker's ROOM.md/NOTES.md entry above).
- **DECODE cache** (`sources/decode/`): directory does not exist in this checkout, nothing to grep.

### Best-case class and status

| Item | Printed deciphered | Printed as cipher | Calendared | Best-case class |
|---|---|---|---|---|
| f.29 no.21 (Gramont to Villandry, partly cipher) | not found | not found | not found (LP vol.4 pt.3 checked directly, absent) | **N3** |
| f.30 no.22 (entirely cipher) | not found | not found | not found | **N3** |

Status: **open** (unchanged from the check-solved verdict). Gate passed for a solver to proceed to
transcription/key application — no print or online decipherment stands in the way — but the gaps above
(Le Grand's own page content unverified due to a bot-block; Pocock/SP7/Ribier-Camusat/Molini unreached) mean a
verifier must close them before any N-class above N3 or any "unread"/"first" wording is used, per rule 10 and
the Eckert 1864 lesson (absence from the calendar series is not absence from the sender-specific editions).

### Requests this pass

books.openedition.org: 1 page fetch. archive.org/be-api: ~10 (1 djvu.txt full download of `11332111bsb`,
~9 be-api fts-api queries). googleapis.com (Google Books, `&key=$GOOGLE_BOOKS_KEY&country=US`): 4 queries, key
never printed. books.google.com: 1 curl + 1 browser_fetch.js attempt, both bot-blocked, one retry each, then
stopped (good-citizen rule). gallica.bnf.fr: 1 SRU query (irrelevant results, not pursued further). WebSearch:
4 queries. No logins, no credentials, no subagents, no images fetched, no decoding or transcription attempted.

## Transcription and key application, f.29r — 24 September 2026 (00:05-00:45 UTC, `date -u` read)

Worker: transcription + key (Opus reconciler, two Sonnet passes), orchestrator session_01SepNMpYrr6L2EwqL43aTnm,
cap $20. Stopped after f.29r; f.30r-v (item 22) not transcribed.

**Credit (rule 8).** The key is S. Tomokiyo's reconstruction "Gramont's Cipher (1530)" from BnF fr.3019 f.20
(Cryptiana, francis.htm, `sources/cryptiana/web/francisGramont.png`) and George Lasry's independent recovery of
the same cipher from BnF fr.3071 f.17 (table dated 04/11/2023, `sources/cryptiana/web/GL/BnF_fr3071_f17.png`).
Tomokiyo identified these two fr.2980 letters as readable with it. Bourdeau (dbourdeau/cyphersolver,
`gramont1529/fr3071_no7_gramont.md`, MIT/CC BY 4.0) read fr.3071 no.7 with it; his notes on g serving V/E/B and
on the ss-on-a-stem null were used. Nothing is copied from aaymeloglu/unsolved-ciphers.

**Files.** `ciphertext.txt` (f.29r, 14 lines, 569 signs, descriptive codes), `key.tsv` (code, value, grade, which
table), `decode.py` (writes `reading.txt` and `reading_tokens.tsv`; `--check` exits 1 when stale, verified both
ways), `reconciliation.md`, `legend.py`/`legend.tsv`/`legend_sheet.png`, `tomokiyo_columns.py`/`.tsv`,
`crop.py`, `sheets.py`, `sheets/`, `passA.tsv`, `passB.tsv`, `PASS-BRIEF.md`, `key_draft.tsv` (legend codes to
table values, used only to test the passes).

**Grades (per token, f.29r, from decode.py):** 569 tokens: H 538, C 0, S 0, M 26, I 0, U 5. The H count means
"value taken from the Lasry or Tomokiyo table"; it does not grade my identification of each sign on the leaf,
which rests on one reader (the blind passes failed, reconciliation.md) and on the French coming out. No
cryptanalytic extension of the key was made, so no matched control was needed or run. This is a key-based
reading of f.29r, with word division and the modern rendering below mine (grade I where marked).

**Reading, f.29r cipher (letters as decoded, my word division; `·` = sign not in the key, `?` = I cannot yet
divide or read the letters; `g` read E where the word needs it):**

    L01 il y baille a ce porteur ...? article que j'ay mis
    L02 a part, et i[l?] faict l'adresse de dessus a vous, combien que ce soit
    L03 au roy, et si ledict porteur com...? ...? a vous
    L04 ...ie (artillerie?) vous prie le luy demander, car c'est le total
    L05 ...? et ... faict d'aultant que nous tres ...
    L06 ...? faict ... de instance ...
    L07 contenu ... grande ... du vingtiesme et pour
    L08 ...? faire ... faict et luy ay monstre tout
    L09 re[com]tenu pour le contenter et oster ... de suspecon
    L10 qui est cause que j'ay faict ledit article a part
    L11 pour vous do[nn]er cognoissance de tout, mais je vous
    L12 prie advertissement(?) ... ledict seigneur et tous
    L13 aultres que ... que le ... voulsist
    L14 favoriser(?) soit mene ... secretement [nulls]

Lines 10-11 and parts of 2, 8, 9 and 12 read as continuous French directly from the table values; the rest has
letters I have not yet divided, and some sign identifications in L01, L03-L07 and L13 are probably wrong. The
decoded "du vingtiesme" (L07) fits the letter's own date (20 May) or a reference to an earlier letter of the 20th.

**Clear text, f.29r (draft, read by eye from the image, grade M throughout, for context only):** "Monsr, pensant
que ce courrier pourra estre plustost a vous que le pacquet que j'ay envoye au Roy du xxi[?]e [verifier note, grade I: a packet of the 21st cannot precede a letter of the 20th; 20 May 1530 (Julian) was a Friday and 'lundi' was 16 May, so 'xvi' is likelier; re-read against the image] de ce moys, je vous ay
bien voulu envoyer ung double des lettres que j'escriptz lundi ... et demeurant voz ... La venue ... et la depesche
dudit porteur ... pour la satisfaction de nostre Sainct Pere et assez tost ... des affaires du Roy par deca ...
Je m'escriptz pour ... messeigneurs ... d'Ancone(?) que j'ay ... par la depesche dudit xxie ... qui sera la fin,
apres de bien bon coeur me recommande a vostre bonne grace, priant Dieu vous donner ... A Rome le xxme de may."
Then cipher; then "Vostre ... serviteur, De Gramont E. de Tarbe". f.30v ends in clear "faict a Rome le xxme jour
de may M D XXX" and the same signature.

**Where the reading was not found (searched 24 Sept 2026, ~00:35 UTC):**
- Internet Archive full text (be-api fts, no login): `"faict ledict article a part"` 0 hits;
  `"pour le contenter et oster"` 0 hits; `"Gramont" "Villandry" "article a part"` (words, not a phrase) 10 hits,
  all general (Journal des guerres / du Bellay volumes, `documents10sociuoft`, `grandsecrivainsd0000dema`), none
  checked further.
- Google Books API (keyed, country=US): `"ledict article a part" Gramont` 0; `"baille a ce porteur" Villandry` 0;
  `"Tarbe" "Villandry" 1530 chiffre` 3 (Letters and Papers Henry VIII (1965 reprint) x2, Calendar of State Papers
  1876): LP vol.4 pt.3 was already checked by the print-check pass (no item of 20 May 1530); the CSP volume was not opened.
- Also see the print-check section above (Le Grand gap, Pocock, SP7, Ribier/Camusat, Molini unreached).
No novelty class is given here (rule 10); the verifier follows.

**Requests this pass.** gallica.bnf.fr 6 (3 info.json, 1 reset not retried; 3 full-resolution regions, f32 reset
twice then fetched on a third attempt after a 20 s pause, one attempt beyond the single-retry rule).
cryptiana.web.fc2.com 2 (the two key images; the key is not in the mirror as an image). github.com 1 shallow clone
(dbourdeau/cyphersolver, read only gramont1529/). archive.org be-api 3. googleapis.com 3. No logins.

**For the next worker (one line each):** transcribe f.30r and f.30v by the reconciler method (reconciliation.md),
reusing key.tsv codes; re-read f.29r L01, L03-L07, L13 against the image with the decoded letters in hand; add
exceptions.tsv for g-as-E and 9-as-B positions so reading.txt carries the context values with their grade.

## Verifier audit, 24 September 2026

AUDIT.md: item 21 (f.29r) is **N3**. No prior printed plaintext or decipherment was located. Tomokiyo had
identified the letter as readable with the key, and Bourdeau catalogued it (catalogue 328); neither read it.
The reading is partial and rests on one reader. Item 22 has no class until it is read. The safe sentence and
the gaps (Le Grand pages seen only as token counts, Camusat as snippets, JSTOR, HathiTrust full text) are in
AUDIT.md. Suggestion: a second adversarial audit (outreach gate 2) before any message to Tomokiyo or Bourdeau.

## Second reader (24 Sept 2026)

Worker: second reader (Opus), 02:04-02:25 UTC by `date -u`. Brief: blind transcription of the f.29r cipher passage,
then reconciliation with the first reader. No images fetched: the work used the pass sheets on disk
(`sheets/sheet01-05.jpg`, native-resolution line crops cut from the full-resolution IIIF region), enlarged 1.5x and 2x.

**Blind pass C.** `passC_f29.tsv`: 567 signs, 31 marked uncertain, 9 shapes given new codes (N1-N9, defined in
the file footer). It was made from the crops and `atlas/atlas_f29.png` before any of the first reader's files
were opened. Caveat: the atlas exemplars were cut by aligning the first reader's codes (`atlas/dp.py`). Pass C is
blind to the first reader's transcription but uses the same sign inventory, and it was made by the same model
family. It is a second reading, not an independent sign census. `key.tsv` applied to pass C through a scratch
copy of decode.py gives `reading_passC.txt`: H 509, M 44, U 14. Blind, it already read as continuous French in
L01, L02, L04, L08-L12 and most of L03, L05 and L13.

**Agreement with the first reader** (LCS alignment of sign codes, dots excluded): 523 of 569 = **91.9%**. Counting
same-shape pairs that carry different names (N5 = Hb twice, N4 = E twice) and T/Th (both SS) as agreement, it is
529 of 569 = **93.0%**. By line (raw): L01 90, L02 85, L03 93, L04 93, L05 90, L06 87, L07 82, L08 98, L09 93,
L10 92, L11 98, L12 92, L13 95, L14 94. Compare the two Sonnet passes on the redrawn legend: 29% (reconciliation.md).

**The one systematic confusion is 9 (E) against g (V).** Pass C and the first reader split on it 10 times. On a
2x zoom the shapes do separate. 9 has a long descender that swings down-left or out to the right under the next
sign. g has a closed bowl with a tail that hooks back to the left. Where the image is clear, context agrees with
it: PORTEVR and BIEN take 9, SEIGNEVR takes g. Pass C was wrong on 7 of the 10 (L02 idx18, L06 idx5, L07 idx30
and 33 in VINGTIESME, L09 idx32, L12 idx31, L13 idx17) and the first reader on 3 (L01 idx17, L02 idx34, L03
idx40).

**Changes: proposed, not applied.** `passC_proposed_changes.tsv` has 19 rows. 14 are sign changes where the image
supports pass C (15 rows, because one change merges two signs): L01 x3, L02 x2, L03 x2, L04 x2 deletions, L05 x2,
L06 x1, L08 x1 (also marked uncertain), L09 x1. The other 4 mark a first-reader sign uncertain without changing it
(L03 idx34, L04 idx0, L06 idx6, L09 idx0). Each row gives the image basis. The worker's attempt to write them into `ciphertext.txt` was refused by
the session's permission policy (a shared transcription file). The committed ciphertext, reading.txt and
reading_tokens.tsv are therefore **unchanged**, and `decode.py --check` passes on them. If the orchestrator or
the owner accepts the table, applying it to ciphertext.txt and running `python3 decode.py` gives the preview
below (made in a scratch copy).

| | tokens | H | M | U |
|---|---|---|---|---|
| committed (first reader) | 569 | 538 | 26 | 5 |
| after the proposed changes (preview) | 568 | 533 | 30 | 5 |
| pass C alone, blind | 567 | 509 | 44 | 14 |

H falls by 5 because five signs become uncertain (M), not because any reading gets worse. The proposed changes
repair these words in the preview: IAY (was ILY), PORTEVR (was PORTVVR), VNG ARTICLE (was VNGAERTICLE), ET AI
FAICT (was ET I FAICT), BIEN (was BIVN), AVENDVRE (was LVENDVRE), BAILLER less its first sign (EAILLER, was
EAISLLER), LE LVY DEMANDER (was LVTIDEMANDER), FONDEMENT less its first sign (TONDEMENT, was TONDEPETT), DV
SCRI.. (was DG), LVI (was OVI), ORS DE SVSPECON (was ORADE). None of the first reader's readings in L07, L10, L12
or L13 is changed. There, pass C's alternatives read worse; the key example is L10's final APART, where pass C's
null_o is wrong and the sign is q9 (P).

**Preview, lines as they read after the proposed changes** (grade H except where marked; word division by eye):
L01 continuous (IAY [B]AILLE A CE PORTEVR VNG ARTICLE QVE IAY MIS). L02 continuous except QVV for QVE. L03 mostly
continuous, one wrong sign in D'AVENTVRE. L04 continuous except the first sign (E for B). L05 continuous except
the first sign (T for F). L08 continuous (SATASFAIRE for satisfaire). L09 continuous. L10 continuous except N
for Q. L11 continuous. L14 largely continuous (BAVORISER for favoriser; EXSECRETEM·NT).

**Lines that still do not read as French:** L06 (CTPEREDAFAICT·RAB...), L07 (AVLEGRANDESCEPVS), L12
(ADVERTISSEMEIETN), and L13 in part (LACPOVSVENCAS..., LERPIVOVLSIST). Their disputed signs (L07 idx7-8, 16,
18-19; L12 idx13, 17; L06 idx5-6) are the ones to look at next, on the full-resolution region rather than the
sheets. Suggestion, not done: a third look at those six spots at full resolution would settle whether they are
sign misreadings or encipherer's errors.

Requests: none to any host (no fetch). Files: passC_f29.tsv, reading_passC.txt, passC_proposed_changes.tsv, this
section. AUDIT.md, ciphertext.txt, reading.txt, reading_tokens.tsv and f.30 files are not touched.

## Second reader: changes applied (24 Sept 2026)

Applied per ASKS.md row 25 (orchestrator decision, 24 Sept 2026, by `date -u`). Every row of
`passC_proposed_changes.tsv` whose `basis` column reports image support was written into `ciphertext.txt`: 14
sign changes (15 rows, one change merges two signs: L01 idx24-25 `sl r3` -> `rs`) plus L02 idx5 (`4t` gains a
following `z`, a genuine 4th-token insertion) and L04 idx3/idx21 (two deletions: a double-counted `2` folded into
`ll`, and a spurious `yt` with no sign in the image). L08 idx0 (`Rt` -> `L2`) is a sign change whose new code is
itself uncertain, so it was written as `L2?`. The 4 rows the table marks as uncertain-without-changing (L03
idx34 `eh`, L04 idx0 `sl`, L06 idx6 `fh`, L09 idx0 `r3`) were left at their existing value and given a trailing
`?` only. Nothing the table calls uncertain or unsupported was applied otherwise.

`python3 decode.py` regenerated `reading.txt` and `reading_tokens.tsv` from these inputs; `python3 decode.py
--check` passes (reading matches the committed inputs, rule 7).

**Grade counts, before -> after** (of all graded tokens; U = sign not covered by the key):

| | tokens | H | M | U |
|---|---|---|---|---|
| before (first reader, committed) | 569 | 538 | 26 | 5 |
| after (passC changes applied) | 568 | 533 | 30 | 5 |

The token count drops by 1 (one deletion net of one insertion and one 2-for-1 split minus one merge: L01
2-for-1 +1, L01 merge -1, L02 insertion +1, L04 two deletions -2). H falls by 5 only because five signs (the
four newly uncertain plus L08's changed-and-uncertain `L2?`) can no longer carry a firm grade under decode.py's
rule that an uncertain sign is capped at M -- no reading got worse.

**Words that changed** (grade H unless noted): IAY (was ILY, L01), PORTEVR (was PORTVVR, L01/L03), VNG ARTICLE
(was VNGAERTICLE, L01), BIEN (was BIVN, L02), LE LVY DEMANDER (was LVTIDEMANDER, L04), FONDEMENT less its first
sign, still reading T for F and unresolved by this pass (was TONDEPETT, L05), ORS DE (was ORADE, L09).

**Lines that now read as continuous French** (word division by eye, decoded from `reading.txt`): L01 `IAY EAILLE
A CE PORTEVR VNG ARTICLE QVE IAY MIS` (bracketed digraphs as decode.py renders them: `IAYEAI[LL]EACEPORTEVRVNGARTICLEQVEIAYMIS`).
L02 `A PART [ET] AI FAICT LA DRE[SS]E DE DE[SS]VS A VOVS [COM]BIEN QVV CE SOIT`. L03 `A ROY [ET] SI LE DICT
PORTEVR [COM]VELIOIT D'AVENDVRE AYE VOVS`. L04 `EAILLERIE VOVS PRIE LE LVI DEMANDER CAR CEST LE TOTAL`. L05
`TONDEMENT [ET] I AI CE FAICT D'AVLTANT QVE NOVS TRE SAIB` (T for F at the first sign is a separate, unresolved
issue, not touched by this pass). L08 `LVI SATASFAIRE I AI CE FAICT [ET] LVY AI MONSTRE TOVT`. L09 `RE[COM]TENV POVR LE [COM]TENTER
[ET] OVSTER · ORS DE SVSPECON`. This matches the preview above; L06, L07, L12 and part of L13 are unchanged and
still do not read as French (their disputed signs are unaffected by this pass; see the preview note above for
where to look next).

Files touched: ciphertext.txt, reading.txt, reading_tokens.tsv, this section, ASKS.md (row 25 set to done).
AUDIT.md, key.tsv and f.30 files not touched. No novelty wording used or implied.

## f.30 passes (24 Sept 2026)

Image work and two blind Sonnet passes only, per brief -- no reconciliation, no key application, no decoding.
Retries the 01:32 claim on this same job (commit 229570d), which stalled without producing any output.

**Images.** Re-fetched the f.30r (canvas f32) and f.30v (canvas f33) native-resolution IIIF regions named in
`images/manifest.json` (4004x5566 and 4050x5567, matching the byte counts already recorded there); not
committed, per the existing convention (re-fetchable from the same URLs). Cut 110 per-line-half crops (55
manuscript lines x a/b halves, all under 2500px wide) reusing the box coordinates already computed in
`crops/crops.json`/`crops/splits.json`, and packed them into `atlas/sheet01.jpg`-`sheet19.jpg` (6 rows per
sheet, last sheet 2 rows) for the pass brief `atlas/PASS-BRIEF-f30.md`. Crop list recorded in
`images/manifest.json` under `f30_line_crops_2026-09-24`. Folder now ~17MB, under the 30MB cap.

**Passes.** Two independent Sonnet subagents, each given only `atlas/PASS-BRIEF-f30.md`, the two atlas images
(`atlas_f29.png`, `atlas_f30add.png`) and the 19 sheets; neither saw the other's file, ciphertext.txt,
reading.txt, key.tsv or NOTES.md. `passA_f30.tsv` and `passB_f30.tsv`, 110 rows each (f30r_L01a-f30v_L20b),
header `row<TAB>codes`. Pass A: 1987 tokens, 257 `?` (12.9%), 0 invented/NEW codes. Pass B: 1926 tokens, 734 `?`
(38.1%, self-reported lower confidence -- it read each sheet once without re-zooming individual rows), 0
invented/NEW codes -- both passes matched every sign to the existing atlas.

**Agreement** (difflib alignment per row on base codes, trailing `?` stripped, aggregated per manuscript line;
a comparison count, not a reconciled reading): overall 1195/2004 = **59.6%**, well below f.29r's second-reader
91.9% (higher-quality f.29r crops, established codebook by then) but far above the 29% an earlier shape-only
attempt got on f.30 before this atlas existed (see "For the next worker" above). Worst-agreeing lines: f30v_L19
(39%), f30r_L26 (46%), f30r_L25 (49%), f30r_L09 (49%), f30r_L11 (50%), f30r_L13 (50%), f30v_L17 (50%). Full
per-line table is reproducible from `passA_f30.tsv`/`passB_f30.tsv` (script not committed this pass; the next
worker can regenerate it with difflib the same way).

**Hard crops**, flagged independently by both passes: a dark ink blot/smudge affecting f30r_L02a (sheet01) and
again across f30r_L07a-L09a (sheet03) and f30r_L23a/L25a (sheets 08-09) -- this smudge region overlaps three of
the seven worst-agreeing lines above, so it looks like the main driver of disagreement rather than scribal
ambiguity alone. Also flagged: f30r_L16b (bleed-through from the adjacent line), f30v_L05a-L06a (pass A could
not decide dot vs. a small "v"/lam sign), f30v_L14a (pass B: an unfamiliar boxed/stacked glyph, marked `BOX?`),
and the right-hand (`b`) halves on sheets 12-19 generally, where pass B reports the crop running into the page's
gray margin and cutting off the last sign or two.

No decoding attempted, no key applied, no novelty wording. Status unchanged (partial: f.29r read, f.30 still
unread). Requests this pass: gallica.bnf.fr 2 (both IIIF region fetches, 1.5s apart, 200 on first attempt, no
retries needed). No other hosts, no logins, no subagents beyond the two pass workers (Sonnet, at most two at
once). Cost well under the $10 cap.

**For the next worker:** reconcile passA_f30/passB_f30 against the crops (same method as `reconciliation.md`
used for f.29r), giving weight to the higher-confidence pass on rows where one used far fewer `?` than the
other; re-crop or re-fetch the f30r_L02/L07-L09/L23/L25 blot region at higher zoom if the reconciler still can't
resolve it; only then map codes to key.tsv values and decode.
