blocked

Status: blocked (needs-physical-access: BnF Français 4688 is not digitised -- the holding catalogue record
archivesetmanuscrits.bnf.fr/ark:/12148/cc57738c, read in full 2 Oct 2026, carries only "Document original :
Français 4688 Réserver" with no "Consulter le document numérisé" link and no substitute microfilm cote, and Gallica
SRU finds no copy). Check-solved: no prior decipherment found in the sender's printed Lettere (Guazzo, Lettere,
1606 edition, IA bub_gb_i5TaJCFjfM8C, full-text grep of the whole _djvu.txt for Nevers/cifra: two literary letters
to Nevers, neither a cipher dispatch), Boltanski 2006 (Google Books full-text search "Guazzo" + "chiffre"/"1572",
no hit), Tomokiyo nevers.htm (no Guazzo), DECODE, both solver repositories, three blogs (below).

# Stefano Guazzo to the Duke of Nevers, Casale, 1571-72 (BnF Français 4688)

GUAZZO-INTAKE, 2 Oct 2026 (account-2 worker under LANE-A2PUSH, for the account-3 orchestrator; brief
.claude/briefs/runs/2026-10-02-acct3-guazzo-intake.md). Intake only: no image, no transcription, no reading.

Source of the lead: ciphers/nevers-birago-fr3251-1572/BIRAGO-POOL.tsv rows 13-14 (BIRAGO-SCOUT, 2 Oct 2026).

## Volume and availability (holding catalogue, quoted)

- BnF, Département des Manuscrits, **Français 4688** (ancienne cote Anc. 9510). "Recueil de pièces originales et
  de copies concernant la maison de Nevers. De 1567 à 1574." XVIe siècle, papier.
- Record: `https://archivesetmanuscrits.bnf.fr/ark:/12148/cc57738c` (FRBNFEAD000057738), fetched 2 Oct 2026,
  snapshot `catalogue/bnf-aem-cc57738c-2026-10-02.txt`. Availability flag, quoted: "Document original : Français
  4688 Réserver" -- no "Consulter le document numérisé" link (its neighbour fr.4687, record cc577374, carries one,
  to btv1b90075058, and a substitute "MF 7338"; fr.4688's record carries neither).
- Gallica SRU, 2 Oct 2026: `gallica all "Français 4688"`, `dc.source all "4688"` (40 hits, none BnF Français 4688),
  `gallica all "Guazzo" and dc.type all "manuscrit"` (19 hits: fr.3312, 3421, 3989, 4687, 4695, 4702, 4704,
  Français 322xx, Rothschild, Chappée; not 4688). Not on Gallica.
- So step 1 of the brief (canvas/folio offset, cipher-passage layout from the page images, facing pages at native
  resolution) cannot be done: there is no image. `tools/gallica_folio.py` was not run (no ark).

## Layout (from the catalogue only; folio ranges, not seen)

| item | folio | date | sender -> recipient | catalogue words | cipher? | est. signs |
|---|---|---|---|---|---|---|
| 4 | f.9 | 12 Jul 1570 | Guazzo -> Nevers, Casale | "En italien" | not stated | ? |
| 7-8 | ff.15, 17 | 25 Mar 1571 | Guazzo -> Nevers, Casal | "Chiffres. En italien" | yes (catalogue) | ? |
| 10-12 | ff.29 et suiv. | 1-9 Apr 1571 | Guazzo -> Nevers, Casal | "En italien" | not stated | ? |
| 15-17 | ff.39 et suiv. | 30 Apr, 1 Jun 1571 | Guazzo -> Nevers and Cesare Ceppo | "En italien" | not stated | ? |
| 19 | f.47 | 14 Sep 1571 | Guazzo -> Nevers, Casal | "En italien" | not stated | ? |
| 24-33 | ff.65 et suiv. (to f.86) | 12 Dec 1571 - 28 Apr 1572 | Guazzo -> Nevers, Casal, "Lettres et notes" | "En italien. Chiffres." | yes (catalogue) | ? |
| 45, 48, 51-58 | ff.115, 126, 131 et suiv. | Aug 1572 - Jun 1573 | Guazzo -> Nevers | "En italien" | not stated | ? |

Two catalogue items say "Chiffres": nos.7-8 (two letters, one day) and nos.24-33 (ten letters and notes, ff.65-86,
about 22 leaves). Whether "Chiffres" means cipher passages in the letters, or separate key sheets, or both, the
record does not say; neither item says "déchiffrement" or "avec traduction". The est. signs column is "?" for every
row: no leaf has been seen. Which of the "not stated" letters carry cipher is unknown (BnF item lists often omit
"avec chiffre" on letters that have a few cipher words).

Related, outside this volume (catalogue hits on "Guazzo Nevers", 2 Oct 2026): fr.4687 no.18 "Fragment d'une lettre
... par un de ses agents, le Sr GUAZZO ?" and no.28 "Fragment de lettre adressée par le Sr CEPPO au Sr Guazzo,
agent du duc de Nevers à Milan. 28 aprile 1572" (cc577374, on Gallica btv1b90075058) -- a Ceppo-to-Guazzo letter of
the same day as the last fr.4688 cipher item; fr.3989 no.53 (Guazzo 1594, out of window).

## Design note (no images: inference only, grade I)

Same months and network as the Ceppo-Nevers cipher (Sept 1570 - May 1571, ciphers/ceppo-nevers-fr3251-1570s,
Tomokiyo's key from fr.4702) and the Nov 1571 numerical / 1572 Nevers-Birago keys (ciphers/birago-nevers-1571,
ciphers/nevers-birago-fr3251-1572). Guazzo was Nevers's agent in Casale (Montferrat), not Birago's office in
Saluzzo, so a shared key is a hypothesis only: an agent's cipher with his own principal is at least as likely
to be a separate table. Step 3 of the brief (one first test under Ceppo-Nevers or the 1572 key if the sign
inventory matches by eye) is not reachable: no sign inventory can be compared without an image.

## Check-solved (GUAZZO-INTAKE, 2 Oct 2026)

Order of CLAUDE.md rule 1:
1. Search engine: "Stefano Guazzo Nevers 1571 1572 lettere cifra "Français 4688"", "Guazzo duca di Nevers cifra
   Casale 1572 lettere decifrate" -- no page about these letters; hits are Wikipedia (Guazzo), the 2021 HistoCrypt
   paper on Henri IV to Nevers 1592 (dspace.ut.ee / ecp.ep.liu.se), and Biblissima notices for fr.3375 (Guazzo 1586).
   None mentions fr.4688 or a 1571-72 Guazzo cipher.
2. Sender's printed letters: Lettere del signor Stefano Guazzo (1606 edition, IA `bub_gb_i5TaJCFjfM8C`), whole
   _djvu.txt fetched once and grepped: "Nevers" twice (two letters "Al Signor Duca di Nevers", one recommending a
   Malvezzi, one congratulating on a marriage -- literary letters, no dispatch, no cipher); "cifr" once, unrelated.
   Recipient side: Les Mémoires de monsieur le duc de Nevers (Gomberville, 1665), Google Books API query
   `"Guazzo" intitle:memoires intitle:nevers` (country=US, key) -- 0 hits; Boltanski, Les ducs de Nevers et l'État
   royal (2006, Google Books dsInahmnar8C, PARTIAL): snippet "Guazzo correspond régulièrement avec le duc de Nevers
   et compose plusieurs mémoires sur le conflit d'héritage", queries `chiffre Guazzo` and `Guazzo 1572` inside
   that title: 0 hits.
3. Calendars / state papers: no state-paper calendar covers Mantua-Nevers agent letters; not applicable beyond the
   BnF catalogue (above) and Tomokiyo.
4. List-post comment threads: see "Web and blog check".
5. DECODE: the solver-repo copy of the DECODE catalogue (aaymeloglu/unsolved-ciphers catalogue/decode-catalog.csv,
   clone of 27 Sept 2026) has no Guazzo row; record id 4688 there is a Marburg key, unrelated.
6. Solver repositories: dbourdeau/cyphersolver (shallow clone, commit of 2 Oct 2026) -- "Guazzo" only in
   research/gallica_sweep (fr.3989 no.53, 1594; fr.4687 nos.18/28 notices); no fr.4688, no Guazzo target.
   aaymeloglu/unsolved-ciphers (commit of 27 Sept 2026) -- no Guazzo, no fr.4688.
Tomokiyo: sources/cryptiana/web/*.htm (local mirror) -- no "Guazzo" anywhere; nevers.htm lists no fr.4688 item.
Verdict: no prior decipherment located for fr.4688 nos.7-8 or 24-33 in the sources above, searched 2 Oct 2026;
status `blocked` because the material itself is not reachable (no image), not because an edition went unread.

## Web and blog check

2 Oct 2026, WebSearch restricted to scienceblogs.de (Cipherbrain / klausis-krypto-kolumne), cryptiana.blogspot.com
(Cryptiana blog) and ciphermysteries.com (Cipher Mysteries), query "Guazzo Nevers cifra"; and an open query
"Guazzo Nevers cipher" across the same three plus cryptiana.web.fc2.com. No post or comment about Guazzo or
fr.4688; hits were unrelated (Bellaso ciphers, Biermann posts, Top-25 list).

## Premise check (GUAZZO-INTAKE, 2 Oct 2026)

(a) Folder's own files and the source row: BIRAGO-POOL.tsv rows 13-14 say decipherment "not stated" and image
"not found on Gallica"; the catalogue record says "Chiffres" for nos.7-8 and 24-33 and never "déchiffrement",
"traduction" or "avec la traduction". Not found (no decipherment mentioned anywhere to open). Caveat: "Chiffres"
could itself mean key sheets bound with the letters; only the leaves can settle it.
(b) Other solvers' working files: none for this item in cyphersolver or unsolved-ciphers (grep "Guazzo", "4688").
Not found.
(c) Physical neighbours, facing pages, slips: unreachable -- no image of fr.4688 exists online. The neighbouring
items in the record (no.9 f.27 Nevers minute; nos.10-12 ff.29ff Guazzo letters 1-9 Apr 1571; no.34 f.87 memoriale
28 May 1572) are not described as clear copies. Clear copies elsewhere: fr.4687 no.28 (Ceppo to Guazzo, 28 Apr
1572, Gallica btv1b90075058) is the nearest same-day leaf online; not opened in this job (outside the brief).
(d) Recipient side: Gomberville's Mémoires de Nevers (1665) and Boltanski 2006 searched as in check-solved item 2:
not found. The recipient's other cipher keys (fr.4702 Ceppo-Nevers tables; the "68 cipher tables" Nevers
manuscript named by the 2021 HistoCrypt paper's abstract) are not checked for a Guazzo table in this job.

## Intake gate

```
$ python3 tools/intake_gate_check.py guazzo-nevers-fr4688-1571-72
guazzo-nevers-fr4688-1571-72: blocked (line 1) -- already terminal, nothing to gate   (exit 0)
$ python3 tools/gaps_check.py guazzo-nevers-fr4688-1571-72
SKIP guazzo-nevers-fr4688-1571-72: status blocked; sections not required   (exit 0)
```
No letter tested, so no PROGRESS.tsv row (brief: one row per letter tested).

## While waiting

The one action that depends on nobody: look through the Nevers key collections already on Gallica (fr.4702
cc57752b; the HistoCrypt "68 tables" volume) for a table captioned Guazzo / Casale / Monferrato, 1571-72; ~$2.
Done 2 Oct 2026 (GUAZZO-KEY, below): no Guazzo/Casale key found. Remaining untried sibling: the undated tables of
fr.3995 (Tomokiyo nos.32-34, 71, 73, 76) by image, ~$1; low prior (every dated fr.3995 table is 1584 or later).

## GUAZZO-KEY: key search in the digitised Nevers volumes (2 Oct 2026)

Account-2 worker for the account-3 orchestrator; brief .claude/briefs/runs/2026-10-02-acct3-guazzo-key.md.
Gallica IIIF only (one request at a time, >=1.5 s apart); images viewed at 500-1400 px, not committed.

| volume / item | what was checked | finding |
|---|---|---|
| fr.4687 no.28 (f.65), Ceppo to Guazzo, 28 Apr 1572 | catalogue cc577374 (snapshot `catalogue/bnf-aem-cc577374-fr4687-2026-10-02.txt`); Gallica btv1b90075058 canvases 73 (f.65r) and 74 (f.65v); canvases are two-page openings, f.65r is the right page of canvas 73 (offset found from canvases 43, 66, 71, 73; the manifest carries no folio labels) | **one leaf, clear Italian only, no cipher, no key.** f.65r: "Molto mag.co sig.r mio sig.r oss.mo / Hieri ho ricevuto il plico di V.S. ... trovandosi V.S. a Millano ..." -- about the jewels in the late "sig.r C.F."'s estate and an "Instrutione"; f.65v: endorsement only (Ceppo, 28 [aprile] 1572) and show-through. |
| fr.4687 no.41 (f.89), "Chiffre. Quelques lignes non chiffrées sont en italien" | canvas 97 (f.89r) | a cipher **letter** fragment, not a key table: about 8 lines of figures mixed with capital letters (A, B, D, G, R, S) and over/under marks, then clear Italian ("di modo che se questo è vero ...", "e vuole se ne vuole andare a casa ..."). Undated; its neighbours are 1589-93 (nos.38-40, 42), so probably outside the Guazzo window. Not in Tomokiyo's nevers.htm; not deciphered in this job (outside the brief). |
| fr.4702 (cc57752b, snapshot `catalogue/bnf-aem-cc57752b-fr4702-2026-10-02.txt`; Gallica btv1b530546654) | full catalogue read (49 entries, 9 name Guazzo); ff.34r and 35r (canvases 81, 83; `tools/gallica_folio.py` constant offset k=14) for the "Notes ... 1572" item 17-18 | none of the nine Guazzo items is catalogued as cipher; the only cipher of the 1570s is Ceppo's ff.36-37 (the Ceppo-Nevers key Tomokiyo rebuilt, already held in ciphers/ceppo-nevers-fr3251-1570s). ff.34-35: clear Italian notes (Mantua, Saluzzo, the jewels), no table. Other fr.4702 cipher items are 1586-1590 decipherments. |
| fr.3995 (Tomokiyo's 76-table Nevers collection) | sources/cryptiana/web/nevers.htm, catalogue text only (no images) | no table captioned or annotated Guazzo, Casale or Monferrato; every dated table is 1584-1594. Undated: nos.32-34 (Italian annotations naming Florence, Paris, "luigi"), 71, 73, 76 -- not checked by image. |

**Verdict: no Guazzo/Casale key located** in fr.4687, fr.4702 or the fr.3995 catalogue, searched 2 Oct 2026.
The keys in hand for that network and window stay the Ceppo-Nevers cipher (Sept 1570 - May 1571), the Nov 1571
Birago numerical cipher (undeciphered) and the 1572 Nevers-Birago cipher. The Ceppo leaf shows Guazzo in Milan on
Nevers's business in April 1572 with Ceppo as correspondent, which keeps the Ceppo-Nevers table the first key to
try on fr.4688 nos.7-8 (March 1571, inside its Sept 1570 - May 1571 window) once images exist (grade I, inference).

Requests: gallica.bnf.fr 15 (13 IIIF images + 1 manifest via gallica_folio.py x2); archivesetmanuscrits.bnf.fr 2.

## Suggestions (not done, Usage 7)

- Add fr.4688 ff.15-18 and ff.65-86 to the next BnF reproduction quote batch (outreach/bnf-manuscrits-arsenal-quote-batch.md, ASKS 38 pattern); REQUEST.md here.
- fr.4687 no.41 (f.89r, Gallica btv1b90075058 canvas 97): an undated cipher letter fragment (figures + capitals + marks), not in Tomokiyo; probably 1589-93 by its neighbours. A scout/intake row, not this target.
- fr.3995 undated tables nos.32-34, 71, 73, 76 by image (~$1) for a Casale/Monferrato caption.

## Re-check (CS-BATCH1, 3 Oct 2026)

Re-confirmed, no new material: WebSearch `Stefano Guazzo Nevers Casale 1571 1572 ... "Français 4688"` (3 Oct 2026) returned the Guazzo biography, BnF/Folger/Heidelberg catalogue records and the HistoCrypt Nevers papers, none carrying a decipherment of fr.4688. Local grep of `sources/cryptiana/web/codebreaking.htm` and the DECODE key lists: the "4688" hits are an unrelated Marburg key. Status stays `blocked` (needs-physical-access; the 2 Oct premise check and While-waiting entries stand, no new step).

## Next step (NO-CRACKS, 5 Oct 2026)

next: add fr.4688 ff.15-18 and ff.65-86 to the next BnF reproduction quote batch (ASKS 38 pattern, REQUEST.md here) for the owner to order, ~$0 agent cost; while waiting, read fr.3995 undated tables nos.32-34, 71, 73, 76 by image for a Casale/Monferrato caption, ~$1. Who acts: owner. Source: this file's follow-up bullets (fr.4688 not digitised); written by NO-CRACKS (account 3) because tools/next_steps.py found no next-step line in this file.
