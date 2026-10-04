# BnF Français 2980, ff.29-30: two cipher letters of Gabriel de Gramont, bishop of Tarbes (cardinal from 8 June 1530)

partial
Letters and Papers Henry VIII vol. 4 pt. 3 (IA 11332111bsb) full OCR text read and grepped for 20 May 1530, Villandry and Tarbe by print-check M8 (23 Sept 2026), and Le Grand, Histoire du divorce III pp.394-542 read page by page from the MDZ scan bsb10280117 by the second audit (24 Sept 2026, AUDIT.md): neither prints either letter.

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

Question: is the plaintext of either fr.2980 f.29 (no.21, Gramont to Villandry, Rome, 20 May [1530], partly in
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
- **PUR OpenEdition**, Philippe Hamon, "Jean Breton (v. 1490-1542)", in Cédric Michon (ed.), *Les conseillers de
  François Ier* (PUR 2011), pp.335-342 [author and title corrected by verifier V2, 24 Sept 2026: not Thierry Rentet,
  whom the chapter thanks and cites (n.22)] (`books.openedition.org/pur/120024`, fetched directly, full chapter read) — biographical detail
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

**Files.** `ciphertext.txt` (f.29r, 14 lines, 568 signs after the second reader, 569 before; descriptive codes), `key.tsv` (code, value, grade, which
table), `decode.py` (writes `reading.txt` and `reading_tokens.tsv`; `--check` exits 1 when stale, verified both
ways), `reconciliation.md`, `legend.py`/`legend.tsv`/`legend_sheet.png`, `tomokiyo_columns.py`/`.tsv`,
`crop.py`, `sheets.py`, `sheets/`, `passA.tsv`, `passB.tsv`, `PASS-BRIEF.md`, `key_draft.tsv` (legend codes to
table values, used only to test the passes).

**Grades (per token, f.29r, from decode.py):** 569 tokens: H 538, C 0, S 0, M 26, I 0, U 5 (first reader; current, after the second reader: 568 tokens, H 533, M 30, U 5 -- see "Second reader: changes applied"; verifier V2, 24 Sept 2026). The H count means
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

## f.30 reading (24 Sept 2026)

Worker: reconciler + key application (Opus, cap $15), 02:55-03:20 UTC by `date -u`, orchestrator session
session_01EFmUvFAifLKGdBSsW9mjEG. Work from the crops on disk; no image fetched and no host contacted.

**Files.** `passR_f30.tsv` is the reconciler's sign-by-sign reading of the 110 crops. `build_ciphertext_f30.py`
(with `--check`) turns it into `ciphertext_f30.tsv` (line, position, sign, confidence h/m/l),
`reconciliation_f30_lines.tsv` and `reconciliation_f30_signs.tsv`. `reconciliation_f30.md` has the method,
agreement per line and how the disagreements were settled. `decode.py` now also writes `reading_f30.txt` and
`reading_f30_tokens.tsv` from `ciphertext_f30.tsv` and the unchanged `key.tsv`. `--check` covers both leaves,
and the f.29r outputs are byte-identical. `contexts_f30.py` writes `unkeyed_f30.tsv`.

**Transcription.** 1973 signs on 55 lines (f.30r 35, f.30v 20). Confidence: h 1333, m 474, l 166. The
reconciled signs agree with blind pass A on 63.5% and with pass B on 55.3%, and the passes agree with each
other on 60.8%. As on f.29r, the transcription rests mainly on one reader.

**Grades (per token, from decode.py):** 1973 tokens: **H 1500, C 0, S 0, M 241, I 0, U 232.** H means "value
taken from the Lasry/Tomokiyo table" (key.tsv). It does not grade the identification of the sign, which rests
on the reconciler. M means a sign read with doubt. U means a sign key.tsv does not cover. No value was added to
key.tsv and no cryptanalytic extension was made, so this is a key-based reading with unread signs, not a
cryptanalytic result, and no control was needed.
*[Verifier note, f.30 audit, 24 Sept 2026: only `l` signs are demoted to M (decode.py). 331 of the 1502 H tokens
are on signs read at medium confidence (`m`); H on a high-confidence identification is 1171. 43 H tokens fall on the
flagged signs eh (19), Tb (16) and H (8). "M means a sign read with doubt" should read "M means a sign read with
low confidence (`l`) or a key value graded M". See AUDIT.md, section "f.30".]*

**Lines that read as continuous French** (word division possible by eye with at most one or two unread signs,
22 of 55): f.30r L13, L14, L19, L20, L21, L26, L27, L31, L32, L33; f.30v L02, L03, L04, L07, L08, L09, L10,
L12, L13, L15, L17, L18.
**French with gaps** (words readable, runs broken by unkeyed or doubtful signs, 25): f.30r L05, L06, L09,
L10, L15, L16, L17, L18, L22, L23, L24, L25, L28, L29, L30, L34, L35; f.30v L01, L05, L06, L11, L14, L16,
L19, L20.
**Not French, still unread** (8): f.30r L01, L02, L03, L04, L07, L08, L11, L12. This is the top of f.30r,
dense with the unkeyed arch/FL/box/III/HASH signs. Either the signs there are misidentified, or the passage
uses nomenclator signs outside both tables. It needs a second reader on the crops before anything else.

**Plain sense, provisional** (from the decoded runs only; unread signs shown as `·`; modern sense mine, grade I):
1. The cipher speaks of a "declaration" of "la liberte de Florence" (f.30v L02-L03, L10: DECLARADION DE LA
   LIBERTE DE FLORENCE; LA DECLARATION DE LA ·IBERTE).
2. Someone "a s'estre ja declare" and "qu'il ve·lt aller en Avi·non" (f.30r L32). There is talk "pour
   recouvrer" something (f.30r L33) and of someone who "·yont perdu" (f.30r L34).
3. Formulas addressed to "Sire" occur (f.30v L05-L06 "TRES ·VMBL / ·ENTSIRE"), with
   "vostre commandement" (f.30v L17). So the cipher is addressed at least in part to the king. The addressee
   of item 22 is not established here. *[Verifier note, 24 Sept 2026: the cipher addresses the king ("Sire", "vostre
   commandement"; grade I). It is probably the "article mis a part" that f.29r says was addressed on the outside to
   Villandry although meant for the king (inference). See AUDIT.md, section "f.30".]*
4. The letter names "l'ambassadeur ... et aultres ses ·ini·res" (f.30v L12), "il est impossible" (f.30r L31),
   "il est rayson" (f.30r L14), "a craindre" (f.30v L15), "neantmoins qu'il ait maulvayse fan·asie" (f.30v L18).
5. Closing matter on f.30v L19-L20 (DE·ESPPIR, ...), before the clear-text date and signature.

**Distinctive decoded phrases for the verifier** (as decode.py prints them; `·` = unread): DECLARADIONDELA /
LIBERTEDEFLORENCE (f.30v L02-03); ASE·TREIADECLAREQ·ILVE·LTA[LL]E·ENAVI·NON (f.30r L32); PPVRRECOVVRER
(f.30r L33); QVIL E·T IMPO[SS]IBLE (f.30r L31); ILESTRAYSON (f.30r L14); AVCVNEMENT (f.30r L19);
ENTIEREMENT (f.30r L20); SELON ... MAINTENIR (f.30r L21); PEVVENTFAIRE (f.30r L22); DESIBONPIED (f.30r L30);
MONADVIS (f.30v L07); POVR[COM]MANDER (f.30v L08); LAVI[LL]E ... LAFORC· ENTRE VO· MAINS (f.30v L09);
LAMEA[SS]ADEVR (key q=E, read B, f.30v L12); [ET]QVENEANTMOINSQ·ILAIT·AVLVAYSEFAN (f.30v L18);
CRAINDRE (f.30v L15); VOVSTRE[COM]MANDE (f.30v L17).

**Unkeyed signs that recur** (listed with their decoded contexts in `unkeyed_f30.tsv`; no values proposed):
FL 35, BOX 27, n 26, ST 18, A2 17, HASH 13, III 13, B8 13, Mx 11, v 11, QQ 8, re 7, Sx 7, CROSS 4, lz 4,
[?] 4, INF 3, TRI 2, ev 2, Hb 2, Zs 2; single occurrences nn, ff, tb. Sample contexts:
- `n` after nq, before I/E: SIREQ{n}ILVOVS, VSQ{n}ES, APVSEQ{n}IL (f.30r L17, L24, L12).
- `re` after Q or in a word: DECLAREQ{re}ILVE·LT, AVC{re}NE (f.30r L32, f.30v L01).
- `Sx` before V: DSVRAY{Sx}EV, SELON·E{Sx}VVIL, CEN·ST{Sx}VE (f.30r L06, L21, f.30v L02).
- `BOX`: ICEN{BOX}ST, IL D{BOX}SIRE, S{BOX}RVICE (f.30v L02, f.30r L21, L23).
- `FL`: IL E{FL}T IMPO[SS]IBLE, VOVS {FL}AVRIE (f.30r L31, f.30v L08).
- `ST`: DELA{ST}IBERTE, Q·E{ST}EMIEVL (f.30v L10, L07).
- `A2`: LAFORC{A2}ENTRE, [COM]MANDE{v}{A2}NT (f.30v L09, L17).
- `v`: ·VMBL{v}ENT SIRE, PARLE{v}OIEN (f.30v L05-06, L14).
- `lz`: TRES{lz}VMBL (f.30v L05).
**Key-valued signs whose contexts deserve a second look** (graded H because the table gives the value; the
contexts are listed, not corrected): `Tb` (table P) in P{Tb}VR RECOVVRER, COGN{Tb}ISSE, DESESP{Tb}IR;
`eh` (table D) in DECLARA{eh}ION, REPVTA{eh}ION; `H` (table I; Tomokiyo also links it to z) in
SAVRIE{H}, BRA{H}; `q` (table E; key note: reads B on f.29r) in LAM{q}ASSADEVR, OV {q}IEN.

**Still unread:** f.30r L01-L04, L07, L08, L11, L12 in full; the gaps in the 25 partial lines; every U sign above.

**Where the reading was not searched:** no print or phrase search was run in this pass (brief: reconcile and
decode only). Novelty is not classified here (rule 10); the verifier follows.

**Suggestions (not done):** a second blind reader on the f.30r L01-L12 crops; a 2x-zoom check of the 166 `l`
signs; a key-table check of the recurring unkeyed shapes (FL, BOX, n, Sx, re, v, A2, ST) against the Lasry
and Tomokiyo images, which is a key-identification job, not a guess from context.

Requests this pass: none to any host. Subagents: none.

## f.30 unkeyed signs (24 Sept 2026)

Worker: solver (Opus, cap $12), 03:26-03:45 UTC by `date -u`, LANE G orchestrator session_014zWyan51u9qMn9gnHpm1Aq.
No image fetched; archive.org only, 4 requests (one search, three `_djvu.txt` downloads) for the corpus.

**Model.** `tools/french16_ngram.py`: a character 5-gram model (Witten-Bell), folded as the cipher tables are
(upper case, no accents, J->I, U->V). Corpus: Internet Archive OCR of *Lettres inédites de Marguerite de Valois*
(1886) and *Lettres de Catherine de Médicis* t.1-2 (1880), 939,272 words, listed in `tools/data/fr16/MANIFEST.tsv`
(gzipped text committed; the pickled model is a rebuildable cache). Held-out 2.70 bits/char. These are 1530s-1600
letters, which is close to Gramont's period and spelling but later. No edition that could hold Gramont's own letters
was used as corpus.

**Procedure** (`infer_unkeyed.py`, deterministic): every sign key.tsv values is decoded as decode.py reads it
(M values included). Each hidden sign is tried at each candidate value: 23 letters, NULL, and the table's word signs
ET/COM/SS/LL. Every occurrence on both leaves is scored in a window of +-8 signs under the model. Each letter is
charged at the model's mean bits/char so that deleting letters earns nothing, and a word sign pays 3 bits.
Neighbouring signs with no value are filled with the model's likeliest letter. The procedure greedily fixes the
sign whose best value leads its runner-up by the largest margin (bits), then repeats.

**Matched control first (rule 3), `control_f30.tsv`.** Ten draws. Each draw hid 20 keyed H signs, one per unkeyed
target sign (the 20 that occur twice or more). Each hidden sign was chosen at random from the 5 keyed signs whose
total count was nearest the target's. The real unkeyed signs stayed unvalued throughout. Excluded from the pool:
M-graded key entries, and the four keyed signs the reconciler flagged (Tb, eh, H, q), whose true value here is in
doubt. Settings and the acceptance rule were chosen on draws 0-4 only; draws 5-9 were held out.
- All proposals: 155/200 correct (tuning 77/100, held-out 78/100). By frequency band: n>=10 91/101, 5-9 36/36,
  2-4 8/24.
- **Acceptance rule** (fixed on draws 0-4): the value is not NULL, the sign occurs 5+ times, and the margin is at
  least 10 bits. Under the rule: tuning 46/50, **held-out 50/53**, all draws 96/103 (93%). The seven misses are
  aq Y->I six times (a period spelling twin) and Af M->R once. NULL proposals were right about half the time,
  which is why NULL is never accepted. The word sign COM (bb) was always proposed as NULL.
- What did not help on the tuning draws: a dictionary-coverage bonus for word segmentation (0.5 and 1 bit per
  char), a larger set of candidate word signs, and a null penalty. The control score fell each time, so all three
  were left out. The brief asked for a segmentation bonus; the control says it hurts with this corpus.
- Limitation: only 25 distinct keyed signs could fill the pool, so the draws repeat signs, and the 103 accepted
  control proposals are not 103 independent trials.

**Values accepted** (`key_extension_f30.tsv`, grade S; `infer_f30.tsv` has every proposal):

| sign | n | value | margin (bits) | runner-up | sample context (extended reading) |
|---|---|---|---|---|---|
| n | 26 | V | 351 | N | SIREQ**v**ILVOVS, QvIL throughout |
| BOX | 27 | E | 124 | I | S**e**RVICE, CEN**e**ST |
| FL | 35 | S | 109 | NULL | QVILE**s**TIMPOSSIBLE, VOVS**s**AVRIE |
| re | 7 | V | 69 | N | AVC**v**NE DESLIBERATION |
| A2 | 17 | E | 68 | I | LAFORC**e** ENTRE |
| III | 14 | E | 53 | I | (f.30r L01-L04 mostly) |
| lz | 5 | H | 31 | L | TRES**h**VMBL, TOVDES C**h**OVSES QVI VOVS TOVC**h**VNT |
| ST | 18 | L | 25 | NULL | DE LA **l**IBERTE, DES**l**IBERATION |
| QQ | 8 | D | 17 | NULL | |
| Mx | 12 | L | 13 | N | |
| Sx | 7 | Q | 11 | I | SELON·E**q**VVIL |

Not accepted: B8 (NULL, 49 bits; NULL is never accepted), v (M, 5.4 bits), HASH (I, 4.8 bits), and every sign
seen fewer than 5 times (Zs, Hb, INF, TRI, ev, CROSS, nn, ff, tb, [?]). Mx, III, lz and Hb also occur on f.29r.
Those occurrences were scored, but reading.txt (f.29r) is not extended.

**Information only, not applied:** the same procedure, hiding the four flagged keyed signs (`infer_unkeyed.py
doubtful`), gives eh -> T (47.6 bits; DECLARA*t*ION, REPVTA*t*ION), H -> I (as in the table), q -> B (8.7 bits,
below the rule) and Tb -> E (1.2 bits, no decision). key.tsv is untouched. eh = T contradicts the table's D, and a
key-image check should settle it.

**Readings.** `decode.py` now also writes `reading_f30_extended.txt` / `reading_f30_extended_tokens.tsv`: key.tsv
plus key_extension_f30.tsv, which fills only the signs key.tsv leaves unvalued. S values are printed in lower
case. `--check` covers all six outputs, and `--extended` prints the extended reading. The published-key reading is
unchanged. Grades, f.30, 1973 tokens:
- published key: H 1500, C 0, S 0, M 241, I 0, U 232
- extended: **H 1500, C 0, S 158, M 256, I 0, U 59**. The 15 extra M are S values on signs read with doubt (l).
There is no C, so the extension is a cryptanalytic result resting on a key-based reading.

**Lines that read as continuous French**, by eye on the extended reading, in the reconciler's classes (sense
grade I): **32 of 55** (was 22). Newly continuous: f.30r L15, L16, L28, L29, L30; f.30v L01, L05, L14, L16, L19.
The rest are French with gaps (18) or not French (f.30r L01, L02, L04, L08, L11). f.30r L03, L07 and L12 move
from not French to gaps. Samples: f.30r L30 TOVDES CHOVSES QVI VOVS TOVCHVNT DE SI BON PIED; f.30r L29 FOY QVE IE
VOVS DOIBS ... ALLER EN; f.30v L01 ... QVIL NA AVCVNE DESLIBERATION; f.30v L05 ET A VOVS ... ET VOVS ... TRES
HVMBL-. The top of f.30r (L01-L04, L08, L11) stays unread with the new values. That supports the reconciler's
view that signs there are misidentified or belong to a nomenclator outside both tables.

**Where not searched:** no phrase or print search on the new text (not in the brief); novelty is not classified
(rule 10).

**Suggestions (not done):** check eh = T and the accepted shapes (FL, BOX, n, ST, lz) against the Lasry and
Tomokiyo key images; a second reader on f.30r L01-L12; test v as EM or M, and B8 as a null, on the crops.

Requests this pass: archive.org 4. No other host, no subagents, no logins.

**Suggestions from the f.30 audit (24 Sept 2026, not done):** grep *Archivio storico italiano* Appendice II-IX and Sanuto *Diarii* 52-53 for Gramont, May-June 1530 (the two gaps between f.30 and N4); for the solver, Dupuy 452 f.48 (Gramont to Du Prat, 15 May 1530) and fr.3019 f.84 (to the grand maître, 15 May) are context letters in clear, and the printed April 1530 letter to the king (ASI App. I pp.473-481) is a period word list for the same negotiation.

## Second reader f.30, 24 Sept 2026

Worker: blind second reader (LANE V, Opus), 04:21-04:29 UTC by `date -u`. Disk only (images/crops_f30, atlas
images); no Gallica. `passC_f30.tsv` (1977 signs + 54 dots; 212 marked uncertain, 4 illegible, 113 NEW shape codes)
was made by three Opus subagents (f30r L01-18, f30r L19-35, f30v L01-20). They saw only the atlas, the pass brief and
the crops. It was committed (936b4ef) before any f.30 transcription, pass or reading was opened. Caveat, as on f.29r:
same atlas and same model family, so this is a second reading, not an independent sign census.

**Agreement with ciphertext_f30.tsv** (`tools/reconcile_passes.py ciphertext_f30.tsv passC_f30.tsv`, NW, dots
dropped): raw 1649/1987 columns = **83.0%**. 86 of the 338 differences are names only: pass C gave NEW codes to
shapes the reconciler had already coded outside the atlas (nr, nq, n, v, re, B8, Sx, ev). Counting those as
agreement gives **1735/1987 = 87.3%**. Per line (raw), the lowest are f30r L34 71%, f30v L14 73%, f30r L06 74%,
f30v L07 74%, f30r L24 75%, f30v L16 77%; the highest are f30v L04 95%, f30v L10-L11 94%, f30r L10 and L18 92%.

**Systematic classes, 88 columns, committed upheld on sample crops:** nr>2 (29) and n>2 (6): pass C merged the
dotted r (nr) into 2, but the crops show the two apart (f30r L04a idx0, L13b idx24/32). 9>g (23, 22 of them on the
verso) and g>9 (3): the verso subagent used the inverse of the f.29r rule, so a long descender sweeping down-left
is 9 (f30v L05a idx9, L07b idx18/24/29). eh>c (17), with low resolution, so the least sure of the four. nq>xr (10):
the cursive N with a hook sits next to a distinct x-with-r (f30r L12a/b).

**Changes proposed: 2** (`passC_proposed_changes_f30.tsv`, 338 rows, `proposed` column): f30r L06 idx9 and idx21,
committed `2` → `zb`. The crops show a barred 2 at both places (reconciliation class 3). Applied, 24 Sept 2026
(below). Of the other 164 one-off differences, 14 are pass C insertions, mostly `mx x` for the committed single
`mx`, which is a segmentation choice (f30r L02b checked). The rest were not re-checked on the crop and are
proposed `no`. The unflagged ones are the ones worth a look: lam/lz (f30r L12 idx1), bb/br (f30r L06 idx0), 4t/d
(f30v L05 idx1, L16, f30r L25), and 2/zb at f30r L11 idx28.

**Inventory:** pass C found no shape the reconciled code set lacks. Every recurring NEW shape maps to a code that
reconciliation_f30.md already created. Suggestion: add nr, nq, n, v, re, B8, Sx and ev to `atlas_f30add.png` so
that a future blind pass has names for them.

**Applied, 24 Sept 2026.** Apply worker (LANE V, Sonnet), checked both crops itself before applying
(`images/crops_f30/f30r_L06a.jpg` idx9, `f30r_L06b.jpg` idx21): both show the curl-with-horizontal-stroke shape
described in `reconciliation_f30.md` class 3 (barred 2, distinct from the plain 2's tick-above at e.g. L06 idx2,
and from the separate `z` letterform at L06 idx23). `ciphertext_f30.tsv` L06 idx9 and idx21 changed `2` → `zb`;
`passR_f30.tsv` L06a/L06b updated to match and `build_ciphertext_f30.py` rerun, which also dropped both positions'
confidence from `h` to `m` (neither blind pass wrote `zb` there). `decode.py` rerun; `decode.py --check` and
`build_ciphertext_f30.py --check` both exit 0. `zb` keys to NULL (M), so both positions drop from the reading
rather than substitute a letter:
- L06 before: `[COM]ESILE·DSVRAY·EV·LE[COM]SMA·FAICTDPSSCE·`
- L06 after: `[COM]ESILE·DVRAY·EV·LE[COM]MA·FAICTDPSSCE·`

Grade counts (f.30, 1973 tokens) move from H 1502/M 239/U 232 to **H 1500/M 241/U 232**; extended from
H 1502/S 158/M 254/U 59 to **H 1500/S 158/M 256/U 59** (updated above, in AUDIT.md and status.json). No other
row of `passC_proposed_changes_f30.tsv` was touched.

## f.30r top lines re-read (24 Sept 2026)

Worker: solver (LANE G child, Opus, cap $8), 05:18-05:35 UTC by `date -u`. Disk only: no host contacted, no subagents.
Scope: f.30r L01-L04, L07, L08, L11, L12, the eight lines still unread after the published key and the 11 grade-S values.

**Images.** No native region is on disk, but the committed line-half crops are native resolution and overlap their
neighbours, so `recrop_f30r_top.py` pastes them back at page coordinates (crops.json; b halves start at splits.json - 8)
into one mosaic of L01-L13 and cuts the evidence crops from it at 2-5x (`crops/f30r_top/`, 17 files, 0.8 MB). Every sign
in the eight lines was re-read at 2x against legend_sheet.png and the two atlases, with the M/L signs and the a/b seams
at 4-5x. The ink blot on L02 and L07-L09 lies across the paper, but on these crops the signs under it can be read.
It left no sign on these lines unreadable.

**Corrections** (`fixes_f30r_top.tsv`, 21 rows: 16 applied, 5 not applied). What they show:
- **Seam double counts (3).** A sign cut by the a/b split was counted once in each half: L02 `Mx o` -> one sign
  (B8), L12 `mx x` -> `mx`. On L08, three signs under the blot are really two (`sl [?] o` -> `ST 9`).
- **Shape corrections (11):** L01 rs->z3; L02 [?]->INF; L03 lt->CROSS; L04 bb->br and D->br; L07 lt->CROSS;
  L08 HASH->CROSS and yt->B8; L11 Mx->CROSS and 2->zb; L12 lam->lz.
- **L07:** one reading deleted: `nq`, which was the exit stroke of A2.
- Two cross shapes are both coded CROSS: a cross pattee (L03 pos36, L12 pos0) and a double-barred cross (L07 pos3,
  L08 pos29, L11 pos2). A later key check may need to split them.
- **Not applied** (the image does not decide): L07 q (not atlas q; q9, g2 or 9), the faint loop at L07 lam's foot,
  L01 eh/c, L04 Af/Tb, L11 Af/4t, L12 lt vs T/Th.

Applied through `passR_f30.tsv` -> `build_ciphertext_f30.py` -> `decode.py`. Both `--check` pass. Only the eight
target lines changed. The other f.30 lines and all f.29r outputs are byte-identical. f.30 now has 1969 signs (was
1973). Grades: published key **H 1502, C 0, S 0, M 231, I 0, U 236**. Extended **H 1502, C 0, S 159, M 245, I 0, U 63**.
The eight lines alone (extended): H 183, S 44, M 52, U 19 of 298 (before: H 181, S 43, M 63, U 15 of 302). U rose
because four signs moved from a keyed misreading to unkeyed CROSS/INF/B8.

**Lines, extended reading after the fixes** (sense by eye, grade I):
- **Now French with gaps (were not French): L04, L08.**
  - L04 `NesTOIDPOVRM[SS]TeNDERA·LTRVY·EsPeRAND·VE`: POVR (was POV[COM]) and ESPERAN- (was ESPEQAN-) both come from
    the two br fixes. ·LTRVY is AVLTRVY if the unkeyed `nn` is V.
  - L08 `·TENVeSENMeSDICDESLEEReSNRA·SOlANT·PAR`: TENVES EN MES DIC-DES.
- **Still French with gaps: L03, L07.**
  - L07 `DIS·OVRS·QveNOVSNAVeONSEVleSEARO[LL]ES`: DIS-OVRS QVE NOVS ... EV LES -AROLLES.
- **Still not French: L01, L02, L11, L12.** The signs are not the cause: each one is identified at 2-5x, and the
  three passes and this re-read agree on them. What remains is the key, in one of three ways:
  - L01-L02 are dense with the arch ss2 (6 on L01) and the barred zb. Both are read as nulls from f.29r's closing run.
  - The unkeyed signs are HASH, TRI, INF, B8, CROSS and ev.
  - L11 BAIMER and L12 hPVSE rest on Af=M, E=B and Tb=P, which are doubtful here.

  Whether these lines hold nomenclator words or a different value for ss2/zb is not established.

**Inferred from sense only, grade I, not applied** (for a key-image check, not for key.tsv): eh = T (NESTOIT and
ESPERANT on L04, DICTES on L08; infer_unkeyed.py's hidden-sign test gave eh -> T at 47.6 bits). CROSS = C
(DISCOVRS, L07). L07 q = P (LES PAROLLES). nn = V (AVLTRVY, L04). A2 as null or I on L07 (N'AVONS / AVIONS). These
five would make L04, L07 and L08 continuous French. None of them has an image reading or a control behind it.

**Where not searched:** no phrase or print search on the new text. Novelty is not classified (rule 10).
Suggestion (not done): check eh, CROSS (both shapes), nn and the arch ss2 against the Lasry and Tomokiyo key images.

Requests this pass: none to any host.

## f.30r L01, L02, L11, L12 (24 Sept 2026)

Worker: LANE G2 worker E (Opus, cap $6), 07:47-07:56 UTC by `date -u`, parent session_015NqJ9uu5Ef3Bo6QaRiGcGp. Disk only:
no host contacted, no subagents. Brief: `.claude/briefs/runs/2026-09-24-lane-g2-e-gramont-f30r.md`.

**Method.** `test_f30r_top.py` (with `--help`; `--round1` reproduces the first round) uses infer_unkeyed.py's model,
window and costs. The base is the extended reading (key.tsv + key_extension_f30.tsv). For each sign under test it scores
every candidate value over **all** occurrences on f.29r and f.30. The candidates are 23 letters, NULL and 24 word signs
(ET, COM, CON, SS, LL, PAR, POVR, QVE, DE, ... ROY, SIRE, PAPE, EMPEREVR), which covers the nomenclator hypothesis. The
statistic is the score of the best value minus the score of the current value. The control is the same test on
shuffled positions, 100 draws, matched on n:
- n positions of the sign's current value, taken from high-confidence keyed tokens of other signs outside the four
  lines ('matched'). When that value has too few positions, the positions come from any letter ('any').
- For NULL signs, n pseudo-signs inserted at random gaps ('gaps').

p is the share of draws with a statistic at least as large. Recovery is the share of draws in which the proposed
letter comes out best at the same n, on positions whose true value it is. The acceptance rule was fixed before the
run: best differs from current, margin >= 10 bits, p <= 0.01, recovery >= 0.9, n >= 5, and no breakage elsewhere
(the change summed over occurrences outside the four lines >= 0, and at most a quarter of those occurrences lose
more than 3 bits). Results: `test_f30r_top_round1.tsv` (round 1), `test_f30r_top.tsv` (round 2, the accepted values
in the base), `linescore_f30r_top.tsv` (bits/char per f.30 line, before and after).

**Hypotheses tested (round 1; d = bits gained on f.29r / f.30 / the four lines):**

| hypothesis | n | result | decision |
|---|---|---|---|
| arch ss2 not a null (letter or nomenclator word) | 47 | NULL is best over every letter and word sign (margin 0) | rejected: ss2 stays NULL |
| barred zb not a null | 43 | NULL is best (margin 0) | rejected: zb stays NULL |
| nomenclator words for HASH, B8, INF, TRI, ev | 12/15/4/2/2 | HASH best EMPEREVR 10.8 bits but p=0.99 and -71 bits outside; the rest best NULL or below 10 bits | rejected |
| Af = M doubtful | 39 | M is best (margin 0) | table M kept |
| E = B doubtful | 27 | I best by 71.8 bits, p=0.01, but 7/26 outside occurrences lose >3 bits (IMPOSSIBLE, LIBERTE, SEMBLE, HVMBLE need B) | rejected by the breakage rule: B kept |
| **Tb = P doubtful** | 22 | **O best by 283.4 bits**, p=0.010 ('any'), recovery 1.00, d +18.1/+247.9/+17.4, 4/21 lose >3 bits | **accepted, grade S** |
| eh = T (sense only) | 32 | T best by 110.4 bits on the whole, p=0.010, but d **-57.1** on f.29r / +157.1 on f.30, and 10/31 lose >3 bits | rejected by the breakage rule |
| CROSS = C (sense only) | 8 | NULL 0.7 bits ahead of C; round 2: C ahead by 4.4 bits, p=0.97 | rejected (not decided) |
| L07 q = P (sense only) | 1 | P best by 14.9 bits, p=0.02, recovery 0.78, n=1 | rejected (n < 5; stays grade I) |
| nn = V (sense only) | 1 | V best by 2.7 bits, p=0.44 | rejected (n=1) |
| A2 null or I (sense only) | 17 | E stays best; NULL -112.5 bits | rejected: A2 = E kept |
| q = B (key note: reads B on f.29r) | 9 | B best by 50.0 bits, p=0.010 (matched), recovery 1.00 ('any'), d +9.2/+40.8/0, 0/9 lose | **accepted, grade S** |

Round 2 (Tb = O and q = B in the base) accepts nothing else, so the procedure has converged.

**Tb = O, per occurrence.** The gain is on POVR RECOVVRER (L33, +31), COGNOISSE (v L14, +34), DESESPOIR (v L20),
MONSTRE (L18), EN VOZ MAINS (v L03), C(H)OVSE (L12), and LE ROI VOVLSIST on f.29r L13 (+18). Four occurrences lose: f.30r
L13 (-3.4, m), L19 (-15.3, l), L20 pos5 (-7.8, l), L21 (-4.5, l). Three of the four are low-confidence identifications,
and every high-confidence Tb gains. The likeliest reading is that Tb is the O sign and that these few `l` positions are
misread P signs (dl or q9). That is an inference for a crop check, not a correction.
**eh splits by leaf.** It reads D on f.29r (LE DICT, GRANDES, ADVERTISSE, DEMANDER) and T on much of f.30 (NESTOIT,
ESPERANT, TOVTES, REPVTATION, DECLARATION). One value cannot serve both leaves. This looks like two shapes merged under
one code (the second reader's eh>c class), and it is a shape question for the crops and the key images, not a value.
**q at f.30r L07** now reads B (LES BAROLLES). The previous re-read noted that this sign is "not atlas q; q9, g2 or 9".
As q9 (= P, keyed) it would give PAROLLES. Suggestion: re-check that one sign on `crops/f30r_top/L07_q.jpg`.

**Output.** `key_extension_f30.tsv` gains two rows, Tb = O and q = B, each grade S and marked `OVERRIDE`. decode.py now
lets an OVERRIDE row replace the key.tsv value, **in the extended f.30 reading only**. key.tsv, reading.txt (f.29r) and
reading_f30.txt are unchanged. infer_unkeyed.py keeps OVERRIDE rows if it is rerun, and now has `--help`: any other
argument used to run target mode and overwrite key_extension_f30.tsv. This worker's first probe did exactly that, and the
two files were restored from git before any work. `decode.py --check` exits 0.

**Grades, f.30, 1969 tokens:** published key unchanged, H 1502, C 0, S 0, M 231, I 0, U 236. Extended before: H 1502,
C 0, S 159, M 245, I 0, U 63. **Extended after: H 1486, C 0, S 181, M 239, I 0, U 63.** No C, so this is a cryptanalytic
result on top of a key-based reading.

**The four lines** (extended reading after; bits/char under the model, before -> after; the 32 continuous lines have
median 3.00 and 90th percentile 3.51):
- **L01** `·sIMReIEAEeNsEIVeVDVSEsDIMeREI` (4.46 -> 4.46). **Still not French.** None of its signs changed value. Its
  six ss2 and three zb are nulls on the evidence of both leaves, so they cannot be letters here unless the line uses a
  different key. The line is the densest in nulls on the leaf. That fits a padded opening, or a nomenclator passage
  whose signs have been coded as known shapes. No word sign tested fits.
- **L02** `·Qve·eNSVIs·sISDTdEVOVSesCRPRE` (4.20 -> 4.20). **Still not French.** Fragments only (VOVS). INF, TRI and B8
  stay unread: none has a value that passes the control, and B8 as NULL is the best score but NULL is never accepted.
- **L11** `lE·BAIMERLESOVSTDELANOI··QVEl[COM]Ve` (3.58 -> 3.58). **Still not French** as a line, though it sits inside
  the range of the continuous lines. BAIMER rests on E = B and Af = M, and both tables survive the test on the whole
  text, so the doubt is not in those values. The reading `LE · B AIMER LES OVST DE LA NOI` does not give words. Either a
  sign is misidentified here or the passage is nomenclator.
- **L12** `·hOVSEQvILlSYseMOLASTQVENDeV[SS]IEI` (4.47 -> 4.09). **French with gaps.** Tb = O turns hPVSE into hOVSE:
  with the unkeyed cross pattee as C (grade I, not applied) it reads CHOVSE QV'IL ... The rest after QVIL is not yet
  words.

**Not established:** whether L01, L02 and L11 hold nomenclator words, and what CROSS (both shapes), HASH, INF, TRI, B8
and ev stand for. The two cross shapes (pattee on L03 and L12, double-barred on L07, L08 and L11; checked on
`crops/f30r_top/L12_lz.jpg` and `L11_CROSS.jpg`) should be split before any further test. A key-image check against
the Lasry and Tomokiyo tables is the next step for eh, Tb and the crosses.

**Suggestions (not done):** apply Tb = O to f.29r as well (+18.1 bits there; reading.txt is not extended, by
convention); split eh into its two shapes on the crops; re-check L07 q against q9.

**Where not searched:** no phrase or print search on the new text. Novelty is not classified (rule 10).
Requests this pass: none to any host.

**Suggestion (verifier V2, 24 Sept 2026, not done; for a solver):** the L01 word division "il y baille" does not fit
the letters, which read I A Y [q] A I LL E; with q as B (key.tsv's own note) the opening is "j'ay baille(e) a ce
porteur". Re-divide L01 in the gloss; reading.txt itself is unaffected. Also noted by the ChatGPT second opinion
(second-opinions/chatgpt-2026-09-24.md, section 3), with its unverified conjectures on L04-L05 "tondement"/"fondement",
L10 "cavsenve" and L11 "do[nn]er".
- Suggestion (V3b, 24 Sept 2026, from second opinion SO-GRAMONT-F30): f30r L32 reads AVILNON, which the prompt glossed as Avignon; check the L/G sign against the image and the key before any paraphrase says "Avignon" (same pass as eh T/D and the two crosses).

## Web and blog check (GF-A2-3, account 2, 2 Oct 2026)

Queries run (plain web search), hit lists read, plausible hits opened:
1. `Gramont évêque de Tarbes Villandry Rome 20 mai 1530 lettre chiffre` (sender + recipient + date) -- Wikipedia, FIU
   cardinals list, catholic-hierarchy, BL catalogue rows; nothing on these letters or their cipher.
2. `"fr. 2980" OR "français 2980" Gramont chiffre` (shelfmark) -- only unrelated Gramonts (later dukes, a linguist).
3. `Gramont cipher 1530 Lasry Tomokiyo deciphered letters Villandry` (the folder's own key route) -- HistoCrypt papers
   (article 402, Sennecey; article 699), Lasry's Wikipedia page, and Cipherbrain's "21 previously unsolved encryptions solved"
   (opened: Lasry's 2022 list, the only example quoted is Marillac 1550; no Gramont/Tarbes item).
4. `Gabriel de Gramont cardinal 1530 encrypted letter deciphered Claude OR GPT solves` (model-solve family) -- no
   announcement on Gramont; only other 16th-century decipherment news (Charles V 1547, Sennecey).
Blog site searches: `site:scienceblogs.de Gramont cipher Tarbes` (no Cipherbrain page returned);
`site:ciphermysteries.com Gramont OR Tarbes cipher` (Cipher Mysteries pages returned are Jabron, Valcros, La Buse --
unrelated); `site:cryptiana.blogspot.com Gramont` (no Cryptiana blog page returned; Tomokiyo's francis.htm on disk
names both letters as readable with Gramont's 1530 key and gives no reading, as already recorded above). No comment
thread found discussing fr.2980 ff.29-30.

## Premise check (GF-A2-3, account 2, 2 Oct 2026)

(a) Decipherments the folder already mentions -- **not found for this item.** No gloss on the leaf (check-solved,
image viewed); the decipherment the folder mentions is of a neighbouring letter (LP iv(3) 6244, Gramont to Brion,
Bologna 25 Feb 1530, printed deciphered at Le Grand ii.386) and LP 6245 (to Villandry, Bologna 27 Feb, "the original
was in cipher") -- different dates and place; the second audit read Le Grand III pp.394-542 without a Rome letter of
20 May. Tomokiyo's francis.htm statement that the letters "can be read" with the key is a key attribution, not a
reading.
(b) Other solvers' working files -- **not found.** Fresh clone of dbourdeau/cyphersolver (head 2341682, 2 Oct 2026):
CATALOGUE.md line 76 still lists "Gramont to Villandry, Rome (BnF fr. 2980 nos. 21-22, ff. 29-30; catalogue 328):
Gramont 1530 key held (gramont1529)"; targets/gramont1529/ holds readings of fr.3091 no.23 (ff.45r-47v), fr.3071
no.4/no.7, fr.3083 no.8 and Macon -- no transcription, alias file or decode run of fr.2980. aaymeloglu/unsolved-
ciphers (head d2800bb): "2980"/"Villandry" hits are digit runs in unrelated files; no Gramont folder.
(c) Physical neighbours -- **not found.** Canvases f31 (f.29), f32 (f.30) and f33 (f.31, item 23 plain Latin) were
viewed by the check-solved worker (images/); no clear copy or decipherment bound beside them was recorded; this worker
did not re-view at native resolution (unreached in this job's box).
(d) Recipient's side -- **not found.** Villandry (Jean Breton) was secretary of finances at the French court: the
recipient-side calendars and editions checked by the print-check and audits (LP iv(3), Le Grand, Decrue, the Catalogue
des actes de Francois Ier IX [411], Hamon's Breton chapter) cite the letter's existence and date only, no content.

## Key-image check: eh, Tb and the two crosses against the Lasry and Tomokiyo tables (A2-GRA, account 2, 2 Oct 2026)

The step named at the end of the Tb/eh test section ("A key-image check against the Lasry and Tomokiyo tables is the
next step for eh, Tb and the crosses"). Disk only, no network: Tomokiyo's table `sources/cryptiana/web/francisGramont.png`
(reconstructed from fr.3019), Lasry's table `sources/cryptiana/web/GL/BnF_fr3071_f17.png` (fr.3071, 4 Nov 2023),
the leaf exemplars in `atlas/atlas_f29.png`, the f.30 line crops `images/crops_f30/f30r_L04a.jpg`/`L04b.jpg` and the
cross crops in `crops/f30r_top/`. Comparison sheets: `keyimage_check/sheet.png` (`build_sheet.py`) and
`keyimage_check/zoom.png` (`build_zoom.py`), both regenerate from those files. One reader (this worker, by eye):
a shape comparison, not a value test, and no control is claimed for it (rule 3 applies to the value test named below).
Nothing in key.tsv, key_extension_f30.tsv, decode.py or the readings was changed; `decode.py --check` is unaffected.

| Sign | Leaf shape(s) seen | Lasry table | Tomokiyo table | Result |
|---|---|---|---|---|
| eh, f.29r (3 atlas exemplars) | small closed C/G-bowl with a filled inner curl | D, row 1 (k19, the filled e-hook) | d, row 2 (same filled curl) | **D confirmed by both tables.** No T-column shape (Lasry T: m, a 2-hook; Tomokiyo t: a curled l, a 2-hook, m) resembles it. |
| eh, f.30r (3 of its 22 occurrences viewed: L04 pos 6, 16, 36) | open c-bowl with a separate slanted (pos 6, 36) or crossed (pos 16) stroke above it; not filled | no shape like it in any column | nearest is the row-5 sign under m (a crossed stroke over a c-bowl), in Tomokiyo's row of doubled letters (LL, RR, SS ...); no T shape like it | **A different sign from f.29r's eh**, coded together by the passes. It is in neither T column, so the tables do not give it T; they do not give it D either. Value unestablished. This explains the earlier split (D on f.29r, T by sense on f.30, breakage d -57.1 on f.29r): it is a shape split, not one sign with two values. |
| Tb (2 atlas exemplars, f.29r L05, L13) | (1) p-bowl on a stem with a crossbar on the stem; (2) tall hooked stroke over a b/8 bowl | key.tsv cites P k33, a heavy T-bar over an E: **not like either exemplar**. O column: k16 (b with a stroke through it) is close to exemplar 2; k13 (l with a stroke) has the same crossbar idea as exemplar 1 | o, row 2 (a stemmed sign with a crossbar) is close to exemplar 1; o row 1 is b | **The shapes sit with O in both tables, not with P k33.** This agrees with the grade-S override Tb = O (key_extension_f30.tsv, 283.4 bits, p = 0.010). key.tsv's source note "Lasry P (E with a bar, k33)" is a mismatch of shape, not a table value. Grade not raised here (one reader's shape call); see the next step. |
| CROSS, pattee (f.30r L03 pos 36, L12 pos 0) | equal-armed cross with splayed ends | none (Unknown row: hash, barred z, 8, double s, keyed T) | none | **In neither table.** CROSS = C (sense, L12 CHOVSE) stays grade I, unapplied. |
| CROSS, double-barred (f.30r L07 pos 3, L08 pos 29, L11 pos 2) | upright with two crossbars and a short foot | none | row-5 sign under l: an upright with two crossbars and a curled tail, in the doubled-letter row (so LL?) | **Nearest table shape is Tomokiyo's row-5 sign under l**, whose value Tomokiyo's layout implies is LL. On L07 it would give DIS-LL-OVRS where sense wants C (DISCOVRS), so the shape match and the sense disagree; not decided. The two cross shapes are distinct in the tables' terms too and should be coded apart (CROSSp, CROSS2). |

Grades: no token's grade changes (H/C/S/M/I/U counts as in the Tb/eh test section). What the check settles: f.29r eh = D
is table-backed; f.30 "eh" is a separate shape the tables do not key; Tb's shape points at O, not at the cited P k33;
the pattee cross is unkeyed in both tables; the double-barred cross has one candidate table shape (Tomokiyo row 5, l).
Not established: the value of the f.30 c-with-stroke sign and of either cross.
Where not looked: Tomokiyo's and Lasry's tables for other Gramont manuscripts (only fr.3019 and fr.3071 tables are on
disk); the remaining 19 f.30 occurrences of "eh" were not each viewed, so the split count per shape is not yet known.
Requests this pass: none to any host. Vision calls: 4 (atlas_f29, two halves of sheet.png, zoom.png) plus the two table
images and the legend sheet read once each.

## Key.tsv Tb row corrected to O (A2-GRA2, account 2, 2 Oct 2026)

Intake gate before work (`python3 tools/intake_gate_check.py fr2980-gramont`):
`fr2980-gramont: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`, exit 0.

The retry step named in the Escalation list. key.tsv's `Tb` row read `P / H / Lasry P (E with a bar, k33)`; the key-image
check above found that the cited k33 shape does not match the leaf's Tb exemplars, which sit with O in both tables
(Lasry O k16, k13; Tomokiyo o row 2), and the 24 Sept 2026 hidden-sign test already preferred O by 283.4 bits
(p = 0.010, shuffled-position control). The row now reads `Tb / O / S` with both citations. Grade S, not H: the value
rests on the control-backed test, and the table match is one reader's shape call, so it does not license H (rule 4).
No new test was run and no image was read in this step; nothing else in key.tsv changed.

`python3 decode.py --check` before regenerating: STALE, exit 1 (as expected). After `python3 decode.py`: `reading up to
date`, exit 0. Counts:

| Reading | before | after |
|---|---|---|
| f.29r reading.txt (568 tokens) | H 533, S 0, M 30, U 5 | H 532, S 1, M 30, U 5 |
| f.30 reading_f30.txt (1969 tokens) | H 1502, S 0, M 231, U 236 | H 1486, S 16, M 231, U 236 |
| f.30 extended (1969 tokens) | H 1486, S 181, M 239, U 63 | unchanged (the OVERRIDE row in key_extension_f30.tsv already gave Tb = O there) |

Reading changes, f.29r: L13 `...QVELERPIVOVLSIST` -> `...QVELEROIVOVLSIST` (sense: "que le roi voulsist"; the earlier
"Suggestions (not done): apply Tb = O to f.29r as well" is now done). f.30 base reading: 21 Tb positions now O (16 S, 5 M
from l-confidence signs), e.g. L33 POVR RECOVVRER, v L14 COGNOISSE, v L20 ESPOIR, v L03 ENVOI, L18 VOS LOIRE ... OMONSTRE.
The key_extension_f30.tsv OVERRIDE row for Tb is now redundant with key.tsv but left in place (the extended reading
regenerates identically either way). test_f30r_top.py's base is the extended reading, so its committed results are
unaffected. No spec for this target (specs/ has no gramont file), so no judge run. Vision calls 0; requests: none.

## f.30 eh and CROSS split by shape, hidden-sign test rerun (A2-GRA3, account 2, 3 Oct 2026)

Brief `.claude/briefs/runs/2026-10-03-acct2-a2-gra3.md` (the Verdict's cheapest next step). Intake gate before work
(`python3 tools/intake_gate_check.py fr2980-gramont`): `fr2980-gramont: partial (line 3) -- edition/page or full-text-search
citation found within 6 lines`, exit 0. Disk only: no host contacted, no subagents.

**Images (rule 2).** `split_shapes_crops.py` cuts one strip per f.30 `eh` (22) and `CROSS` (8) occurrence from the committed
native line-half crops (`images/crops_f30/`), and `split_shapes_zoom.py` zooms each glyph 3x into `crops/f30_split/zoom_eh.jpg`
and `zoom_cross.jpg` (glyph centres read by eye on the strips, listed in the script). One reader (this worker), 6 image views
(4 strip sheets, 2 zoom sheets) plus one re-view of L04 pos 6. The calls are in `split_f30.tsv` (line, position, old, new,
confidence, shape).

| Code | Shape | Occurrences | Note |
|---|---|---|---|
| `ehx` (was eh) | open c-bowl with a crossed (sometimes slanted or flat T-bar) stroke above | 20 (ciphertext confidence 17 h, 1 m, 2 l; shape call m for L08 pos 15, under the blot, and L04 pos 6, at a strip edge) | the 2 Oct "slanted" vs "crossed" variants are one sign: the stroke angle varies continuously across the 20 |
| `c` (was eh) | plain c, no stroke | 2: f30r L17 pos 21 (l), L31 pos 25 (m) | the atlas c sign (key L); a transcription correction, not a new code |
| `CROSSp` | equal-armed cross, splayed ends | 5: L03 pos 36, L07 pos 3 (m), L12 pos 0, L21 pos 12, L33 pos 15 | L07 pos 3 was called double-barred on 2 Oct; at 3x its upper bar is a short cap, like the other pattee tops |
| `CROSS2` | upright with two full crossbars | 2: L08 pos 28, L11 pos 2 | |
| `CROSSo` | cross over a circle, with a triangular flag | 1: L03 pos 30 | a third cross shape, not seen before |

Applied through `passR_f30.tsv` (30 signs recoded) -> `build_ciphertext_f30.py` (new `SPLITOF`: a split code agrees with the
pass code it was split from, for alignment and confidence; ciphertext_f30.tsv changes only at the 30 positions, L31 pos 25
drops h -> m) -> `decode.py`. Both `--check` exit 0.

**Test (rule 3).** `test_f30r_top.py --split split_f30.tsv` (new option: recodes in memory, tests eh on f.29r, ehx and the three
cross shapes only, writes `test_f30r_split.tsv`; `ehx` is tested against D, the eh table value, as its current value). Same
model, candidates (23 letters, NULL, 24 word signs), shuffled-position control (100 draws, matched on n) and acceptance rule as
the 24 Sept run, fixed before running. The control can differ from the target on this statistic: it rescans the margin at n
other positions of the current value, so a margin depends on where the positions fall.

| Code | n | best | margin (bits) | control p | recovery | outside delta / lose>3 | named value | decision |
|---|---|---|---|---|---|---|---|---|
| eh (f.29r) | 10 | D (current) | 0.0 | 1.000 | 0.88 | 0.0 / 0 of 10 | T: -57.1 | D kept |
| **ehx** | 20 | **T** | **152.1** over D | **0.010** (matched) | **1.00** | +141.7 / 3 of 19 | T | **accept, grade S** |
| CROSSp | 5 | C | 17.4 over T (no current value) | 0.762 (gaps) | 0.94 | -2.4 / 0 of 4 | C: 27.6, p 0.535 | reject: C is not separated from random positions |
| CROSS2 | 2 | EMPEREVR | 0.9 | 0.891 | -- | -3.6 / 1 of 1 | LL (Tomokiyo row 5): -34.4 | reject; n < 5; LL disfavoured |
| CROSSo | 1 | P | 0.1 | 0.960 | 0.70 | 0.1 / 0 of 1 | C: -3.5 | reject; n = 1 |

`key_extension_f30.tsv` gains `ehx T S` (key.tsv unchanged: neither table keys the shape, so the published-key reading now
leaves ehx unkeyed). Grades, f.30, 1969 tokens: published key **H 1468, C 0, S 16, M 229, I 0, U 256** (was H 1486, U 236:
the 20 ehx leave the H column, as the tables do not give them D; 2 c gain H L); extended **H 1468, C 0, S 199, M 239, I 0,
U 63** (was H 1486, S 181, M 239, U 63). f.29r unchanged (H 532, S 1, M 30, U 5). No C, so a cryptanalytic result.

Extended-reading changes (sense by eye, grade I): L04 NESTOIT POVR ... TENTERA ... ESPERANT; L03 LA SORTE QVE; L06 EST VRAY;
L08 DICTES; L14 DE SORTE; L30 TOVTES; L35 REPVTATION; f30v L02 DECLARATION; L13 TRAIRE (was DRAIRE). Not improved or worse:
L05 NINTPOVR, L10 IOTPEIL, L17 VELIET, L26 ·CT·, L01 (still not French); the c recodes give L17 DBLE and L31 IEEVL (were
DBDE, IEEVD), neither yet words. Which three outside occurrences lose >3 bits is in the per-occurrence scores, not listed here.

**Not established:** a value for any cross shape. CROSS = C has now been tested three times with this hidden-sign test (round 1,
round 2, and split as CROSSp here) and never passed its control; the instrument is retired for it (rule 3, third attempt), and
the three shapes have only 5, 2 and 1 occurrences.
**Suggestions (not done):** on the L10 strip (`crops/f30_split/f30r_L10_7_eh.jpg`) the sign coded `lt` before ehx looks like
the double-barred cross; the 24 Sept re-read already moved two `lt` to CROSS (L03, L07), so lt/CROSS2 may be confused
elsewhere. The default `test_f30r_top.py` run (L01, L02, L11, L12 hypotheses) has not been rerun with ehx = T in the base.
**Where not searched:** no phrase or print search on the changed text. Novelty is not classified (rule 10).
Requests this pass: none to any host. Vision calls: 7 (by this worker; no subagents).

## Round 3 of the f.30r hidden-sign test, ehx = T in the base (A2-GRA4, account 2, 3 Oct 2026)

Brief `.claude/briefs/runs/2026-10-03-acct2-a2-gra4.md` (the Verdict's cheapest next step). Intake gate before work
(`python3 tools/intake_gate_check.py fr2980-gramont`): `fr2980-gramont: partial (line 3) -- edition/page or full-text-search
citation found within 6 lines`, exit 0.

**Pre-registered, 04:36 UTC 3 Oct 2026, before running.** `test_f30r_top.py --round3` runs the default sign list (ss2, zb, Af, E,
Tb, eh, CROSS, A2, HASH, B8, INF, TRI, ev, nn, q, q@L07) on the current base (key.tsv + key_extension_f30.tsv, which now carries
ehx = T and the two c recodes through ciphertext_f30.tsv), skipping any code with no occurrences left after the split, plus
ehx itself at its current value T. Same model, candidates, shuffled-position control (100 draws, matched on n), seed and
acceptance rule as the 24 Sept and A2-GRA3 runs, unchanged: best differs from current, margin >= 10 bits, p <= 0.01,
recovery >= 0.9, n >= 5, outside delta >= 0 and at most a quarter of outside occurrences lose > 3 bits. A sign enters the
base only if it clears that rule; nothing else changes the key. Output to `test_f30r_top_round3.tsv` (round 2's
`test_f30r_top.tsv` is kept as is), and the per-occurrence T-minus-D scores for ehx to `ehx_occ_round3.tsv`, whose three
outside occurrences losing > 3 bits are then checked by eye on their committed crops (`crops/f30_split/`).

**Result (run 04:37 UTC, 45 s, `test_f30r_top_round3.tsv`).** Nothing is accepted, so the key is unchanged (key.tsv and
key_extension_f30.tsv untouched; no reading regenerated). CROSS has no occurrences left after the split and was skipped.

| sign | n | current | best | margin | p | recovery | outside delta / lose>3 | decision (round 2 for comparison) |
|---|---|---|---|---|---|---|---|---|
| E | 27 | B | I | 61.5 | 0.010 | 1.00 | +43.6 / 8 of 26 | reject by the breakage rule (round 2: I by 70.2, 7 of 26) |
| eh (f.29r only) | 10 | D | D | 0.0 | 1.000 | 0.94 | 0 / 0 of 10 | D kept; T -57.1 |
| ehx | 20 | T | T | 0.0 | 1.000 | 1.00 | 0 / 0 of 19 | T kept; D -152.1 |
| B8 | 15 | -- | NULL | 79.8 | 0.614 | -- | -25.2 / 7 of 13 | reject (round 2: 81.9, p 0.634) |
| HASH | 12 | -- | EMPEREVR | 3.3 | 1.000 | -- | -75.7 / 7 of 11 | reject (round 2: 10.8, p 0.970) |
| q@L07 | 1 | B | P | 7.5 | 0.059 | 0.70 | +7.5 / 0 of 1 | reject, n = 1 (round 2: p 0.099) |
| ss2, zb, Af, Tb, A2, q | 47, 43, 39, 22, 17, 9 | NULL, NULL, M, O, E, B | current | 0.0 | 1.000 | -- | -- | current kept |
| INF, TRI, ev, nn | 4, 2, 2, 1 | -- | NULL, I, EMPEREVR, V | <= 8.3 | >= 0.465 | -- | -- | reject (n < 5, p) |

Putting ehx = T in the base moved no other sign across the gate: the round-2 numbers shift by a few bits only (E 70.2 -> 61.5,
HASH 10.8 -> 3.3) and every decision is the same. This is the third run of this instrument on the default sign list (round 1,
round 2, round 3) with only the base changed between runs; the non-words in L01, L02, L11, L12 and L05, L10, L17, L26 are not
reached by a single-sign value change it can detect (rule 3, third-attempt clause: retired for these hypotheses, not refuted).

**The three losing ehx occurrences, by eye** (`ehx_occ_round3.tsv`; this worker, 3 image views of the committed strips, no subagent):

| occurrence | conf | T - D (bits) | crop | shape | why T loses |
|---|---|---|---|---|---|
| f30r L26 pos 34 | h | -19.3 | `crops/f30_split/f30r_L26_34_eh.jpg` | c-bowl with crossed stroke, left of the HASH sign: ehx (m: the strip's red marker falls on blank paper right of the line end, so the glyph is identified by its neighbour order 5, ehx, HASH) | line end, right window empty, left neighbour unkeyed (·CT·) |
| f30v L17 pos 18 | l | -18.1 | `crops/f30_split/f30v_L17_18_eh.jpg` | flat T-bar over a c-bowl: ehx (h) | follows m = T, so T gives TT |
| f30r L06 pos 32 | h | -10.2 | `crops/f30_split/f30r_L06_32_eh.jpg` | small c-bowl with crossed stroke after the long-s ss2: ehx (h) | follows ...CT + null ss2, so T gives FAICT T OSS CES (cf. "faict tous ces"); D gives FAICT DOSS |

All three are the ehx shape, not misread D signs; the losses come from T-T adjacency and a truncated window, which the n-gram
model charges whether or not the T is right. Nothing here argues against ehx = T, and the key is not changed (grade S as before).

`decode.py --check`: "reading up to date", exit 0. Grades unchanged from the A2-GRA3 section (f.30 extended H 1468, C 0, S 199, M 239, I 0, U 63;
published key H 1468, S 16, M 229, U 256; f.29r H 532, S 1, M 30, U 5). No C, so a cryptanalytic result. No verifier flag:
no reading changed. Requests this pass: none to any host. Vision calls: 3 image views by this worker, no subagents.

## Clear-pages crib alignment of LP iv(3) 6244/6245 against f.30: non-test (A2-GRA5, account 2, 3 Oct 2026)

Brief `.claude/briefs/runs/2026-10-03-acct2-a2-gra5.md` (the Verdict's cheapest next step; disk only, no images). Intake gate
before work (`python3 tools/intake_gate_check.py fr2980-gramont`): `fr2980-gramont: partial (line 3) -- edition/page or
full-text-search citation found within 6 lines`, exit 0.

**Pre-registration (04:56 UTC), and why it could not be run as briefed.** The planned step was: take the LP iv(3) 6244 (Gramont to
Brion, Bologna 25 Feb 1530) and 6245 (Gramont to Villandry, Bologna 27 Feb 1530) calendar summaries, list their names, places and
dates, align them against `reading_f30_extended.txt`, and raise a token to C only where a summary phrase matches a decoded span
beyond the p95 of a control (the same phrases against f.29r `reading.txt`, and against line-shuffled f.30). Two findings stop it
before any alignment:
1. **The crib text is not on disk.** The LP iv(3) OCR (IA `11332111bsb`) and Le Grand III (MDZ `bsb10280117`) were read by the
   print-check M8 and the second audit but never committed (`find` for `11332111`, `bsb10280117`, `*djvu*` in this folder and
   `sources/`; `grep -rIl "Bishop of Tarbe"` finds only this NOTES.md and the cached Cryptiana pages). What the repo holds of 6244/6245
   is their headers only (sender, recipient, place, date, LP's endorsement and "The original was in cipher", print-check section above).
   Fetching it would break the brief's disk-only rule, so this worker did not.
2. **By construction it cannot give C.** C means read from known plaintext *of this item* (rule 4). 6244 and 6245 are two other letters,
   three months earlier and from Bologna, and LP's summaries are English paraphrases, so no summary phrase is plaintext of the 20 May
   Rome letter; an aligned match could at most suggest a value for a nomenclator code, which is the open-codes question the hidden-sign
   test already tried and was retired on (A2-GRA4). A control on the same summaries would not change that: the step is a non-test
   for C-grading, whatever its numbers, not a negative on the reading.

**Header check (disk only, done before this section was written, so not pre-registered; reported as a search result).** The names,
places and months the 6244/6245 headers carry, spelled as words in the decoded text (spaces and line breaks removed): ADMIRAL/AMIRAL,
BRION, BOVLOGN/BOLOGN, VILLANDRY, FEVRIER/FEBVRIER, plus EMPEREVR, PAPE, ANGLETERRE -- 0 hits each in the f.30 extended reading and in
f.29r (ROY: 0 in f.30, 1 in f.29r). Names and titles in this cipher go to nomenclator codes (the [COM], [ET] brackets; HASH tested as
EMPEREVR in round 3 and rejected), so header words have nothing spelled out to align with; this is consistent with point 2.

**Result.** No token grade changed; key.tsv, key_extension_f30.tsv and the readings untouched. `decode.py --check`: "reading up to date", exit 0. Grades
as in the A2-GRA4 section (f.30 extended H 1468, C 0, S 199, M 239, I 0, U 63; f.29r H 532, S 1, M 30, U 5). No C, so still a
cryptanalytic result. No VERIFIER WANTED (no reading changed).
**What would give C instead (different material, not run):** (a) fr.3019 no.31, Gramont to the grand maitre, "A Rome, le XVe jour de
may" [1530], in clear by its BnF description (second audit, AUDIT.md) -- same sender, same place, five days earlier, the nearest
topic and name source; one Gallica leaf read, ~$3. (b) fr.3038 no.19, the period decipherment of the 27 Feb Villandry letter (printed
Le Grand III pp.391-393): if its cipher original is located, the pair is known plaintext in the same key family and would give C to the
codes they share (key values, not this letter's tokens). Neither was opened; (a) is the cheaper.
**Where not searched:** LP iv(3) and Le Grand III texts not re-fetched (disk-only brief). Novelty not classified (rule 10).
Requests this pass: none to any host. Vision calls: 0.

## fr.3019 no.31 (f.84) as a name and topic source for the f.30 open codes (A2-GRA6, account 2, 3 Oct 2026)

Brief `.claude/briefs/runs/2026-10-03-acct2-a2-gra6.md` (the Verdict's cheapest next step). Intake gate before work
(`python3 tools/intake_gate_check.py fr2980-gramont`): `fr2980-gramont: partial (line 3) -- edition/page or full-text-search
citation found within 6 lines`, exit 0.

**Crops (mandatory step, pasted).** Leaf: BnF fr.3019 no.31 = f.84 = Gallica `btv1b9059994n` canvas 86 (offset canvas = folio + 2,
second audit, AUDIT.md "Gap (4)"); native 4189x5985 (info.json).
```
python3 tools/iiif_lines.py --ark btv1b9059994n --canvas 86 --region 984,387,3166,4692 --prefix f84m --out ciphers/fr2980-gramont/images/fr3019_f84 --debug
  region 3166x4692, 27 lines, 27 bands x 2 segments; pitch 162 distance 113 prominence 220.0   (L01-L22 = letter body; L23-L27 = postscript, clipped on the left)
python3 tools/iiif_lines.py --ark btv1b9059994n --canvas 86 --region 448,4230,3700,800 --prefix f84ps --out ciphers/fr2980-gramont/images/fr3019_f84 --debug
  region 3700x800, 7 lines, 7 bands x 2 segments; pitch 114 distance 79 prominence 197.1   (postscript, full width)
```
(Two earlier calls failed: a doubled `ark:/12148/` prefix gave HTTP 500 twice, my error; one mis-placed postscript region was cut and deleted.)

**Pre-registration (written before any line of f.84 was read; committed before scoring).**
- Candidate list N: every person, place and title-as-name read on f.84 (body + postscript), normalized to the cipher's spelling
  (upper case, U/V -> V, J -> I, Y kept), each at most two spellings. Built from the reconciled reading of two blind passes.
- Codes tested: the f.30 open (U) signs with >= 4 occurrences in `reading_f30_extended_tokens.tsv`: B8 (15), HASH (12), v (11),
  CROSSp (5), INF (4). Signs with 2-3 occurrences are too short for this test and are not scored.
- Statistic: f.30 extended reading as one upper-case string, other U signs and `[..]` brackets kept as they are. For code c and
  name w, every occurrence of c is replaced by w; boundary fit B(c,w) = mean over occurrences of [LL(window with w) - LL(window
  with c deleted) - LL(w alone)], window = 6 characters each side, LL from an add-0.5 character 4-gram model trained on
  `tools/data/fr16` (all three files, upper-cased, U->V, J->I, letters only). Subtracting LL(w alone) removes the name's own
  internal likelihood, so B measures how the name's edges fit the cipher context.
- Control (shuffled names; it CAN differ from the target because B depends on the order of w's letters, its first and last
  letters above all): 1000 replicates, each letter-shuffles every name in N (same lengths, same letters), and takes
  max over names of B(c, shuffled w). Gate per code: real max_w B(c,w) above the replicate's 99th percentile (p <= 0.01,
  Bonferroni for 5 codes at alpha 0.05).
- Power control (known answer, run first): for each of the frequent decoded words VOVS, QVIL, POVR, mask 5 occurrences
  (seed 0, chosen at random from all occurrences) as a pseudo-code, add the word to N, and run the identical statistic and gate.
  If fewer than 2 of 3 pass with the masked word as the top candidate, the test has no power at this N and the target result
  is a non-test (licenses nothing), whatever its numbers.
- Outcome rule: a code passing the gate gets the name as a grade-S candidate value in this section only, with VERIFIER WANTED;
  no token in key files changes from this step unless the code passes and the power control passes. Otherwise no grade moves.
- Script: `f84_names_test.py` (this folder).

**Reading of f.84 (05:13-05:18 UTC).** Two blind Sonnet passes over the 29 crop lines (one call each, both segments of every line),
returned as text and written by this worker to `f84_passes.md`; both readers rate their own reading low-to-medium, with B01, B04-B05,
B13, B16-B17 and B20-B21 the firmest. Not reconciled word by word (not needed for a name list; rule 2: image read, but the reading is
a machine pass of a hard secretary hand, context only, never plaintext of fr.2980). **Topic, where the passes agree:** field news
from northern Italy -- the count Claude Rangon (Claudio Rangone) with light horse and foot went out from Plaisance (Piacenza) toward the
Trebbia and the Po, the enemy were "bien frottez", Claude took a captain (Brandon?) with his own hand, a Burgundian named Hauser? is
mentioned; a count "de Gayace" (Gaiazzo/Caiazzo?) has left the Empire's service for the pope's (B16-B17); the closing recommends
the writer to the recipient's good grace. The postscript names a marquis "de Vigesme" (Vigevano?), a count Jehan, "paule" (Paolo, cf.
the second audit's "Paule Camille"), Rome, and the king. Nothing on f.84 matches the f.30 subject (a courier, an article, an address
to the king through his secretary), consistent with the second audit's description.

**Names list N** (`f84_names.tsv`, 19 forms, only names both passes read on the same line): CLAVDE, RANGON, PLAISANCE, TREBYA, LONGRES,
DIAVOLLARA, MARQVIS, BRANDON, HAVSER, GAYACE, EMPIRE, PAPE, VIGESME, IEHAN, CONTE, PAVLE, ROME, ROY, FRANCE. Pass-only forms not
used: Loys, Pau, Rimini, bourguignon, Piemonte/Tremonte, Sorbi, Pizav, lanz (lansquenets?).

**Registered test (`python3 f84_names_test.py --reps 1000`, output `f84_names_test.tsv`):**

| kind | code/word | n | top name | B top | control p99 | p | gate |
|---|---|---|---|---|---|---|---|
| power | VOVS | 5 | VOVS | -4.141 | -4.141 | 0.096 | FAIL |
| power | QVIL | 5 | QVIL | -5.223 | -5.223 | 0.046 | FAIL |
| power | POVR | 5 | POVR | -4.327 | -4.327 | 0.044 | FAIL |
| power | summary | | | | | | 0/3: **non-test** |
| code | B8 | 15 | TREBYA | -8.518 | -8.580 | 0.009 | (PASS) non-test |
| code | HASH | 12 | TREBYA | -6.029 | -6.470 | 0.005 | (PASS) non-test |
| code | v | 11 | MARQVIS | -4.845 | -3.896 | 0.084 | FAIL |
| code | CROSSp | 5 | MARQVIS | -6.309 | -4.607 | 0.152 | FAIL |
| code | INF | 4 | TREBYA | -5.615 | -5.154 | 0.019 | FAIL |

The power control fails 0/3, so by the pre-registered rule the target rows license nothing. Cause (seen in the dry run before the
name list existed): a letter-shuffle of a short word with repeated letters often reproduces the word itself (VOVS, POVR), so the
control's 99th percentile equals the true word's score -- the control *can* differ from the target in general but ties it exactly
whenever an identity shuffle is drawn, a design flaw of this brief's test as written, not of the data.

**Post-hoc diagnostic, declared after the dry run, licenses no grade** (`--no-identity`: shuffles equal to the word rejected; output
`f84_names_test_noidentity.tsv`): power 3/3 PASS (VOVS p 0.000, QVIL 0.006, POVR 0.000); codes: HASH -> TREBYA p 0.008 PASS, B8 ->
TREBYA 0.016, INF -> TREBYA 0.023, v -> MARQVIS 0.060, CROSSp -> MARQVIS 0.147, all FAIL. The one pass is not a lead: TREBYA (a river
near Piacenza) is the top name for three unrelated codes, which marks an edge-letter bias of the statistic (T- and -A fit French
word boundaries) rather than a fit; a river name standing for a 12-occurrence code in a letter about a courier and an address to the
king has no historical support; and HASH was already tested as EMPEREVR in rounds 2 and 3 and rejected (p 0.97, 1.00).

**Result.** No token grade changed; key.tsv, key_extension_f30.tsv and the readings untouched (`decode.py --check`: "reading up to date", exit 0). Grades as
in the A2-GRA4 section (f.30 extended H 1468, C 0, S 199, M 239, I 0, U 63; f.29r H 532, S 1, M 30, U 5). No C, so still a cryptanalytic
result. No VERIFIER WANTED (no reading changed). f.84 is a name and topic list, not plaintext of either fr.2980 letter, so this
clear-pages step cannot give C either (same reason as A2-GRA5 point 2); the clear-pages escalation is now exhausted for the clear
companions known (LP summaries: A2-GRA5; fr.3019 no.31: this step).
**Where not searched:** Dupuy 452 f.48 (Gramont to Du Prat, 15 May 1530, in clear) not opened; fr.3038 no.19 (period decipherment of
the 27 Feb Villandry letter) not located. Novelty not classified (rule 10).
Requests this pass: gallica.bnf.fr 5 (1 info.json; 2 region fetches with a doubled ark prefix, HTTP 500, my error; 2 region fetches,
200), 1.5 s+ apart, no challenge. Vision calls: 2 (Sonnet, one per pass, line crops only).

## fr.3038 no.19 (period decipherment of the 27 Feb 1530 Villandry letter) and its cipher original: located / not located (N8-GRA, account 2, 4 Oct 2026)

Brief `.claude/briefs/runs/2026-10-04-ytbiz-near8-wave1.md`, job N8-GRA (the Verdict's cheapest next step; A2-GRA7 left no commit,
checked `git log origin/main` before work). Intake gate pasted by LANE-NEAR8: `fr2980-gramont: partial (line 3) -- edition/page or
full-text-search citation found within 6 lines`. The brief's branch: if the cipher original is not on Gallica or not this key family,
stop and record where it was looked; PREREG, crops and transcription only if both exist.

**The decipherment: located.** BnF finding aid `archivesetmanuscrits.bnf.fr/ark:/12148/cc494971` (Français 3038), fetched 4 Oct 2026:
"Fol. 42 - 19 Déchiffrement de la lettre de G[abriel] de Granmont, evesque de Tarbe... à monseigneur de Villandry,... A Boulongne, le
XXVIIe jour de febvrier" (component `cd0e363`). Gallica `ark:/12148/btv1b9060036k` (193 canvases, every label 'NP', so
`tools/gallica_folio.py` cannot map folios; anchors found by eye): canvas 74 = f.46r (no.21, Brion to Madame, Suze, folio number "46"
visible), canvas 66 = f.41v (address "Monsr le grant maistre", back of no.18), **canvas 68 = f.42r**, the decipherment, about 30 lines
of clear French in one hand, clause breaks marked with "(", signed "Vre ... serviteur G. de Gramont, ev. de Tarbe", margin "Chiffre"
and a later archival heading "Italie"; canvas 69 = f.42v, endorsement "Dechiffrement de la lettre ... Monsr de Villandry"; canvas 70 =
f.43r, blank. **No cipher sign on either side of the leaf** (f.42r top half viewed at about 2x, rest at sheet scale): it is a clean
fair copy of the plaintext, not an interlinear decipherment.

**The cipher original: not located.** Where looked, 4 Oct 2026:
- BnF archivesetmanuscrits full-text search (headless Chromium, the home-page box, because the result list is JavaScript-loaded; the
  `champSimple=` GET form returns "Aucun résultat" for anything): "Granmont febvrier" 1 hit (no.19 itself); "Tarbe Villandry" 3 (fr.2980
  nos.21, 22 and fr.3038 no.19); "Tarbe chiffre" 7 (fr.2980 nos.21, 22; fr.3040 nos.5, 6; fr.3091 no.23; plus name facets) -- no letter in
  cipher dated Boulogne 27 Feb; "Boulongne febvrier chiffre" and "Granmont chiffre" 0. The second audit's own queries (AUDIT.md, Raince
  test: "Gramont Tarbe chiffre", "Tarbe déchiffrement", "evesque de Tarbe" 41 hits) also found none.
- Tomokiyo's and Lasry's lists of Gramont cipher letters (`sources/cryptiana/web/francis.htm`, `GL.htm`, cached): fr.3040 nos.4-6,
  fr.3091 no.23, fr.3071 no.7, Clair.330 f.53, fr.3019 f.20, fr.2980 nos.21-22. None is dated 27 Feb 1530.
- DECODE non-decrypted list on disk (`sources/decode/records-non-decrypted-2026-09-24-diff.tsv`): Gramont-tagged BnF records are
  fr.3071 f.17, fr.3053 ff.77/85, fr.3045 ff.28/42, fr.3040 ff.16/18/68 -- none of them this letter by the catalogue dates above.
- LP iv(3) 6245 calendars the letter with "The original was in cipher" (print-check section above); it gives no shelfmark for a cipher
  original. The decipherment leaf is the only witness the catalogues hold.
So the pair the brief needed does not exist in any catalogue reached, and no key-family check, PREREG, crop or transcription was run
(brief's stop branch). This is a search result about where the cipher original is, not a negative on the reading: no grade, key row or
reading changed; `decode.py --check` untouched.

**Named for the Verdict (not run, one line):** the same pair shape exists for the 28 March 1530 Boulogne letter: fr.3040 f.18 no.6,
"Lettre, en chiffre, de G. de Gramont ... au grant maistre ... A Boulongne, le XXVIIIme jour de mars" (Tomokiyo: Gramont's Cipher
(1530), this folder's key family; on Gallica), and Le Grand III p.399, which Ehses cites for Gramont, Bologna, 27 March 1530
(AUDIT.md, documentary editions). If Le Grand III p.399 prints that same letter (date and recipient to be checked on the MDZ scan
bsb10280117 first, one page), the two are known plaintext in the same key and could give C to codes they share with f.30.

**Where not searched:** archives outside the BnF (the cipher original could have stayed with Villandry's papers; none located);
BnF Dupuy and NAF series beyond the finding-aid full-text search. Novelty not classified (rule 10).
Requests this pass: archivesetmanuscrits.bnf.fr 7 (1 curl ark page, 1 curl GET search, 5 browser searches; one browser run failed
mid-navigation, not retried for that query); gallica.bnf.fr 25 (1 manifest via gallica_folio.py; 19 IIIF Image API requests, of which f74 served twice, one info.json
answered 500 and the other 16 answered 404 "ark is unknown" -- the IIIF host refused this ark's other canvases throughout; then 5
`.highres` fetches, all 200),
at least 1.6 s apart, no challenge. Vision calls: 3 image views by this worker, no subagents.

## fr.3040 f.18r no.6 vs Le Grand III pp.454-455 as known plaintext: PASS (N8-GRA2, account 2, 4 Oct 2026)

Brief `.claude/briefs/runs/2026-10-04-ytbiz-near8-wave2.md`, job N8-GRA2. Intake gate pasted by LANE-NEAR8: `fr2980-gramont: partial
(line 3) -- edition/page or full-text-search citation found within 6 lines`. PREREG-N8-GRA2.md pushed (b2161680) before any read or score.

**The pair.** Le Grand III **p.399 is not this letter**: it sits in "Dechiffrement des Lettres de Monsieur de Tarbe" (pp.394-40x, Béthune
vol. 866 pag. 68, to the king, Bologna, after the emperor's departure; MDZ OCR scans 400-408). The 28 March letter to the grand maître is
printed at **pp.454-457** ("Lettre de Mr. de Gramont Evesque de Tarbe à Mr. de Montmorency. De Boulongne le 23. Mars", subscribed "A
Boulongne ce 28. jour de Mars", Béthune vol. 8565; scans 460-463), as the second audit's dateline list already had it. Its original, fr.3040
no.6, is Gallica `ark:/12148/btv1b9059870w` (all canvas labels 'NP'; anchors by eye: canvas 32 = f.18r with folio "18", 33 = f.18v, 34 =
f.19r with folio "19"). The leaf is **mixed**: clear passages that read as the print's words (f.18r top "vous m'escripvistes a vostre
partement de la court ... entretenir Mons. de Rochefort"; f.19r "je presuppose que messeigneurs seront en France ... A Boulongne ce
28. jour de mars", the Corfou postscript), cipher blocks between them, and marginal notes beside the cipher blocks (not read here). The
print runs on continuously, so it gives the plaintext of the cipher blocks. Signs: the same family as atlas_f29 by eye (lam, h, aq, fh, H,
5, m, D, g, x, c, T, 2, z, dl, 4t, oi on line 1), with "/" between groups.

**Run.** f.18r cipher block, first 11 lines cut with `tools/iiif_lines.py --ark btv1b9059870w --canvas 32 --region 560,1680,3300,1420
--follow-slope 400` (22 half-line crops, `images/fr3040_f18/`); 2 blind Sonnet passes against atlas_f29/atlas_f30add (`n8gra2/passA.tsv`,
`passB.tsv`); raw pass agreement 314/420 = **0.748**. Reconciliation (`n8gra2/reconcile.py`, worker by eye on crops L04_s1, L07_s1): where
the passes split, circled B = br (not BOX), δ = n6 (not d), barred z = rs (not lz), the barred J = r3, u = zu; every other split '?'
(69/421 = 0.164, unscored). Print span `n8gra2/print_span.txt` (OCR, long-s slips hand-fixed). Scorer `n8gra2/score.py`.

| | agree | N1 shuffled print p99 | N2 shuffled key p99 | gate |
|---|---|---|---|---|
| planted control, 13% error (registered), N=308, 20 seeds | 0.872 mean | 0.347 | 0.305 | >= 0.497: pass |
| planted control, 25% error (post-hoc bracket at the raw pass disagreement), 10 seeds | 0.764 mean | 0.344 | 0.305 | >= 0.494: pass |
| **target f.18r L01-L10, 308 keyed tokens** | **0.838** | 0.347 | 0.309 | >= 0.50 and > p99: **PASS** |

So key.tsv reads the f.18r block against the printed plaintext at about the planted control's level: independent known-plaintext support for
the key family's values (x A, H I, h V, m T, n6 N, oi E, sl E, rs R, lt O, dl P, p M, c L, b O, 2 S, D Q, r3 R, br R all agree in nearly every
occurrence). This is a check of key.tsv, not a reading of f.30.

**Key changes: none.** Open codes in the span: HASH -> L, L, E, gap (conflict); A2 -> E, D, E (conflict); ST -> L (once); BOX -> R, R, gap,
but the agreed "BOX" at L08 is a circled B by eye (the br shape, not f.30's open box), so it is a reader label error and BOX is not keyed.
Under the PREREG no open code qualifies for C. Keyed codes with >= 2 disagreements (listed, not changed, rule 4): z A -> R x3; g V -> E x5
(9/g reader confusion likely, 9 = E); q E -> P x2 (q/q9 confusion likely); yt T -> P x2; 4t ET aligns badly because the registered
normalisation drops the print's "&". `decode.py --check` not needed (key.tsv untouched).

**Next (one line, not run):** the f.18v blocks and the f.19r top two lines are the same pair (about 30 more cipher lines); a targeted pass on
the open codes (HASH, A2, INF, TRI, ST, the v-shape) with eye checks per occurrence could give them C; the marginal notes beside the blocks
are a third witness not read here.
Requests this pass: api.digitale-sammlungen.de 13 (OCR, all 200); archivesetmanuscrits.bnf.fr 1 (200); gallica.bnf.fr 12 (1 manifest via
gallica_folio.py, 1 info.json, 9 IIIF region/thumbnail fetches, 1 native region via iiif_lines.py; all 200), >= 1.5 s apart, no challenge.
Subagent calls: 2 (Sonnet blind passes); reconciliation by this worker. Novelty not classified (rule 10).

## fr.3040 no.6 f.18v + f.19r top vs Le Grand III pp.455-456 as known plaintext: PASS; ST keyed L at C (N8-GRA3, account 2, 4 Oct 2026)

Brief `.claude/briefs/runs/2026-10-04-ytbiz-near8-wave3.md`, job N8-GRA3. PREREG-N8-GRA3.md (addendum to PREREG-N8-GRA2; new lines, print
segments, units, open-code rule) pushed ec93af5a before any crop was read or any score computed.

**Lines and print.** f.18v (canvas 33): L01-L03 at the top (end of the f.18r block; print S1 = N8-GRA2's span, free ends), L04-L07 (the
addendum estimated 5 lines; the block has 4) after "selon le project et desseing qu'ilz font" (print S2 = p.455 "car puisque luy qui est
Pere" .. p.456 "depuis fait entendre"), L08-L23 after "plus proffitable pour le service du ..." (16 lines, the first mixed clear+cipher)
and f.19r (canvas 34) L01-L02 (print S3 = p.456 "dudit Seigneur. Monsieur l'Evesque de Vvigorne" .. "pour s'en valloir de luy ailleurs").
Print from MDZ OCR scans 461-463, long-s slips hand-fixed (`n8gra3/print_S2.txt`, `print_S3.txt`). Crops: `tools/iiif_lines.py --ark
btv1b9059870w --canvas 33 --region 1000,270,2860,360 | 1000,1040,2900,640 | 1000,2230,2880,2200 --prefix f18vA|f18vB|f18vC` and `--canvas
34 --region 1080,200,2700,300 --prefix f19r`, all `--follow-slope 400 --overlap 0` (f18vC band L17 is clear text, dropped). The tool's s1/s2
segments overlap by about 1,900 px when the region is a little wider than --max-width (N8-GRA2's f.18r crops have the same overlap), so
`n8gra3/halves.py` cut non-overlapping _a/_b halves at the emptiest column near mid-line; only those are committed (manifest marks the s1/s2
entries uncommitted). In this job's numbering f18vC_L01-L16 = f.18v L08-L23.

**Run.** 4 Sonnet blind calls (2 units x 2 passes, `n8gra3/PASS-BRIEF.md`, `passA_u1/u2.tsv`, `passB_u1/u2.tsv`); raw agreement
730/869 = **0.840** (`splits.py`). Reconciliation (`reconcile.py`): agreements kept, reader-label aliases (a -> A2, O -> null_o, n -> n6, the
v shape both readers saw -> v, unkeyed), two splits settled by this worker's eye without the print (HASH on f.19r L02: '#' with two bars;
zb vs mx on f.19r L02); every other split '?' (129/869 = 0.148, unscored; the largest split class, lz vs g2 x12, left unsettled).
Scorer `n8gra3/score3.py` (imports N8-GRA2's registered functions; three alignments, pooled).

| | agree | N1 shuffled print p99 | N2 shuffled key p99 | gate |
|---|---|---|---|---|
| planted control, 13% error, per-block N 83/120/504, 20 seeds | 0.878 mean (min 0.857) | 0.318 | 0.274 | >= 0.468: pass |
| **target f.18v L01-L23 + f.19r L01-L02, 707 keyed tokens** | **0.871** | 0.328 | 0.299 | >= 0.50 and > p99: **PASS** |

Pooled with N8-GRA2's f.18r L01-L10 (0.838 on 308), key.tsv reads the cipher of fr.3040 no.6 against the printed plaintext at about the
planted-control level. This is a check of key.tsv, not a reading of f.30.

**Open codes (registered rule, this job + N8-GRA2 f.18r L01-L10).**
- **ST: 4 occurrences (f.18r L01, f.18v L01, L03, L23), all aligned to L, per-code shuffled-print null 0.000; eye check on each crop: all
  four are the long-s joined to t shape of atlas_f30add, none rejected -> key.tsv `ST L C`.** key_extension_f30.tsv already had ST = L at
  grade S (infer_unkeyed.py, 24 Sept 2026, 18 f.30 occurrences); the known-plaintext value agrees with it. `decode.py` regenerated, f.30
  grades now H 1468, C 18, S 16, M 230, U 237 (was C 0, U 256; f.30r L05 now reads "POVRLA"); `decode.py --check` exit 0.
- HASH: 6 occurrences -> L, L, L, L, E, gap: not all the same, not keyed (4/6 L, like ST; a variant of the same value is possible, untested).
- A2: 10 -> I x5, E x3, L, D: not keyed (the label may cover two shapes).
- Mx (key '?'): 2 -> N, N, per-code null 0.04 > 0.01: listed, not keyed. BOX: 3 -> R, R, gap: not keyed. QQ 1 (gap), v 1 (M): seen once.
- INF, TRI, B8, ev: no occurrence read in these lines.

**Keyed-code conflicts (>= 2 disagreements, rule 4: listed, not changed).** **z A -> R in 20 of 23** aligned occurrences (N8-GRA2 had
3 of 3 on f.18r): on this letter the sign the readers label z reads R almost everywhere, against Tomokiyo/Lasry's A; either z is R in this
letter's key, or the readers' 'z' is another R sign (rs, r3) -- an image check of z against both key tables is the next step, not run.
q E -> B x6 of 14 (q/9 reader confusion likely); dl P -> H x3 of 18; g V -> E x5 of 51 (9/g); h V -> S x2; 2 S -> L x2; 4t ET aligns
badly because the registered normalisation drops the print's "&"; 5 C falls on gaps x7 (cedilla/c?).

Requests this pass: gallica.bnf.fr 9 (3 x 1000 px canvas thumbnails, 1 info.json, 5 native-region fetches via iiif_lines.py; all 200);
api.digitale-sammlungen.de 3 (OCR scans 461-463, all 200); >= 1.5 s apart, no challenge. Subagent calls: 4 (Sonnet blind passes);
reconciliation and eye checks by this worker. Novelty not classified (rule 10).

## Remaining gaps (finish-or-blocker pass, A2-GRA, 2 Oct 2026; updated A2-GRA3, A2-GRA4, A2-GRA5 and A2-GRA6, 3 Oct 2026, and N8-GRA and N8-GRA3, 4 Oct 2026)
Read so far: 1906 of 1969 f.30 signs keyed in the extended reading (H 1468, C 18, S 181, M 239; U 63 -- ST moved S -> C by N8-GRA3, 4 Oct 2026; after the ehx split; unchanged by round 3, A2-GRA4), from the eh/CROSS split section above; f.29r reading.txt per its own section.
- the three cross shapes (CROSSp 5, CROSS2 2, CROSSo 1 occurrence) - blocker: too-short; split by shape and tested 3 Oct 2026 (eh/CROSS split section, test_f30r_split.tsv): C for the pattee fails its control (p 0.762), CROSS2 and CROSSo are below the test's n >= 5, and neither key table keys any of them
- f.30r L01, L02, L11, L12 (not French) - blocker: open-codes; dense ss2/zb and unkeyed HASH, TRI, INF, B8, ev, which neither table keys (HASH aligns L in 4 of 6 fr.3040 no.6 occurrences, not keyed, N8-GRA3) (f30r_top section); the hidden-sign tests there predate ehx = T in the base; a names test against the clear companion fr.3019 no.31 (A2-GRA6, 3 Oct 2026, f84_names_test.tsv) is a non-test (power control 0/3) and its post-hoc no-identity variant gives no credible name (HASH -> TREBYA only, an edge-letter bias)
- f.30r L05, L10, L17, L26 positions where ehx = T does not give words (NINTPOVR, IOTPEIL, VELIET, ·CT·) - blocker: open-codes; round 3 of the hidden-sign test with ehx = T in the base accepts no sign change (A2-GRA4, 3 Oct 2026, test_f30r_top_round3.tsv) and the instrument is retired for these hypotheses (third run); the 3 losing ehx occurrences are ehx by shape on their crops

## Escalation (A2-GRA, 2 Oct 2026)
- [n/a] siblings: Tomokiyo and Lasry tables already come from the sibling letters fr.3019 and fr.3071; fr.3038 no.19 (period decipherment of the 27 Feb 1530 Villandry letter) located on Gallica (btv1b9060036k canvas 68 = f.42r, clear only) but its cipher original is in no catalogue reached (N8-GRA, 4 Oct 2026), so that pair cannot be aligned; the 28 March pair is fr.3040 f.18-19 no.6 vs Le Grand III pp.454-457 (not p.399): f.18r L01-L10 PASS 0.838 vs p99 0.347 (N8-GRA2, 4 Oct 2026); f.18v L01-L23 + f.19r L01-L02 PASS 0.871 vs p99 0.328, ST keyed L at C (N8-GRA3, 4 Oct 2026); f.18r L11-L26 unread
- [x] clear-pages: no clear text of these letters known; the LP iv(3) 6244/6245 summaries are other letters (Bologna, Feb 1530, English paraphrase), cannot give C by construction and are not on disk (A2-GRA5, 3 Oct 2026, non-test); fr.3019 no.31 (Gramont, Rome 15 May 1530, in clear) read from Gallica by two blind passes (A2-GRA6, 3 Oct 2026, f84_passes.md): Italian field news (Rangone at Piacenza, the count of Gaiazzo? to the pope), no topic overlap with f.30; its 19-name list fits no open code (registered test non-test, power 0/3; post-hoc variant only HASH -> TREBYA, rejected as bias)
- [x] known-keys: Tomokiyo and Lasry keys applied (key.tsv), Bourdeau's gramont1529 compared (Premise check)
- [x] print: LP iv(3), Le Grand III, Decrue and the Catalogue des actes checked, no print of either letter
- [x] key-rebuild: eh and CROSS split by shape and the hidden-sign test rerun with its control (A2-GRA3, 3 Oct 2026): ehx = T accepted (grade S, 152.1 bits, p 0.010, recovery 1.00); no cross value passed; round 3 of test_f30r_top.py with ehx = T in the base accepts nothing (A2-GRA4, 3 Oct 2026), third run with only the base changed, so that instrument is retired for the default sign list (rule 3)
- [x] image-check: this section, eh/Tb/crosses against both key images on 2 Oct 2026
- [x] retry: Tb row corrected to O (grade S, table citation) in key.tsv and readings regenerated, decode.py --check exit 0 (A2-GRA2, 2 Oct 2026)
Verdict: keep going: 2 internal gaps; cheapest next: image-check, the z sign against the Tomokiyo and Lasry key images and f.30's z occurrences, since fr.3040 no.6 aligns z to R in 23 of 26 occurrences against the key's A (N8-GRA2/N8-GRA3, 4 Oct 2026), ~$1; then siblings, fr.3040 f.18r L11-L26 (16 lines, unread) against Le Grand III pp.454-455 for more HASH/A2/Mx occurrences under PREREG-N8-GRA3, ~$3

## Interrupted (account 2 usage limit, 3 Oct 2026)

- Role: A2-GRA7 (account 2, LANE-A2PUSH2, session_01Bdx5XaXVGRvDF8zAqG9EH7), spawned 05:30 UTC 3 Oct 2026; brief
  .claude/briefs/runs/2026-10-03-acct2-a2-gra7.md (2d73ce47). No claim or done line in ROOM.md.
- Committed: none (no commit in this folder after A2-GRA6's 95dbb432, checked 09:25 UTC); no orphaned pre-registration.
- Unfinished step: locate fr.3038 no.19 (period decipherment of the 27 Feb 1530 Villandry letter) and its cipher
  original on Gallica, check key family, align as known plaintext -- the Verdict line above is still this step.
- May still push if account 2's session resumes; check git (`git log origin/main -- <this folder>`) and ROOM.md before re-running. Recorded by CLOSEOUT-A2 (account-3 in-session worker) from git and ROOM.md only; no reading, grade, status line or key was changed.
