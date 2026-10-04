# AUDIT -- fr3416-nevers-fils-1589, f.35r figure runs under key no.25

Verifier: VERIFY-NV02 (account 3, for the account-3 orchestrator), 3 Oct 2026, 05:10-05:17 UTC. I'm not the solver.
Claim under audit (NOTES.md, NV02-READ, commit 0214a626): the figure runs at the foot of BnF fr.3416 f.35r (the duc de
Nevers to his son Charles, duc de Rethelois; undated, c. Oct-Dec 1589) decode under key no.25 (BnF fr.3995 canvas f104,
label 51r) as 102 tokens, H 62 / M 40, rank 1/201, z 5.04 against shuffled keys.

## 1. Extract

- Item: BnF Français 3416 f.35r, Gallica ark:/12148/btv1b9058240c canvas f43; BnF catalogue item 30 "Lettre, avec
  chiffre, du duc DE NEVERS a son fils". No contemporary decipherment on the leaf (contrast f.38, item 32 "avec chiffre
  et dechiffrement").
- Key: Tomokiyo, nevers.htm, "no.25 (fol.50) (October 1589)": "This appears to be used in ... BnF fr.3416: no.30
  (fol.35) Duke of Nevers to his son". Tomokiyo published the key's image and gave this attribution. He printed no
  decode of f.35. NV02-READ transcribed the alphabet and nulls from the period key sheet into keys/key_no25.tsv.
- Reading (f35r_reading.txt): 8 short runs of letter fragments, e.g. ".aisi.nlesauroit[ciiij].e", "s.es.auoir[0]"
  (followed by clear "bons deniers"), "b.onnefaSUN.as.". There are no continuous sentences. The clear text around the
  runs isn't transcribed, and the nomenclator codes (Roman numerals, overbar figures) are not read.
- Solver's search: Gomberville 1665 *Mémoires* (4 copies, Books API full text), Tomokiyo pages and hidden comments,
  Cabinet Noir / Bourdeau / Aymeloglu clones, DECODE snapshots, web and blog queries (NV-INTAKE and NV02-READ, 3 Oct 2026).

## 2. Re-derivation and statistics (script verify/verify_nv02.py, output verify/verify_nv02_out.txt)

- `python3 decode_f35.py --check`: `check: OK`, exit 0 (rule 7).
- Fresh seeds 2 and 3 (seed 1 was the solver's):

| text | seed 2 rank / z | seed 3 rank / z |
|---|---|---|
| target, all tokens (72 letters, -1.150) | 1/201, 4.87 | 1/201, 4.56 |
| target, H only (51 letters, -0.938) | 1/201, 5.14 | 1/201, 4.85 |
| positive control NV-03 f.38v (34 letters, -0.769) | 1/201, 5.80 | 1/201, 5.60 |
| shuffled token order, true key | 0/200 >= real (max -1.377) | 0/200 >= real (max -1.330) |

- **The four key-coverage choices the solver disclosed** were each flipped (seed 2). None of them changes the rank:
  - L03 pairing offset 0 instead of dropping the stray 1: rank 1, z 3.58.
  - L03 '59' read as 52, 53 or 54: rank 1, z 5.03, 4.89 and 4.88.
  - L05 dropped: rank 1, z 4.91.
  - L10 dropped: rank 1, z 5.28.
  - Offset 0 with L05 and L10 dropped: rank 1, z 3.87.
  - Runs 2, 4 and 8 removed entirely (41 letters): rank 1, z 4.67.
- **Key-blind check.** These are the two blind Sonnet passes as written, paired naively from each line's first digit,
  with no reconciliation:
  - Pass B as read: rank 1, z 2.54.
  - Pass B with the 0->8 convention: rank 1, z 2.97.
  - Pass A with 0->8: rank 1, z 3.25.
  - Pass A as read: rank 32/201, z 1.19.

  Both passes give a rank-1 signal before anyone looked at the key; pass B does so even without the glyph convention.
  So the reconciliation did not create the signal.
- **Error figure.** The 0.239 per digit is the raw blind passes measured against the reconciled transcription, and most
  of it is one systematic confusion (the looped 8 read as 0). That was settled from the key sheet's own hand. The
  residual error of the reconciled transcription has not been measured: there is no third independent read. So 0.239
  is an upper bracket, not the honest current figure.
- **Power** at N=72 letters, 20 synthetic fr16 windows enciphered with no.25:
  - 0.239 error: 11/20 rank 1.
  - 0.10 error: 20/20.
  - 0.05 error: 20/20.
  - H-only size (51 letters) at 0.10 error: 19/20.

  The noise model is uniform digit substitution only, with no pairing slips.
- Verdict on the statistic: the solver's numbers reproduce, and the rank-1 result survives every disclosed choice and
  the key-blind passes. The reading is still fragmentary. What it establishes is that key no.25 enciphers these runs.
  It does not give a plaintext of the letter.

Grades per token, unchanged: H 62, M 40, C 0, S 0, I 0. No C grade, so the H grade rests on the key sheet, not on a
known plaintext of this letter.

## 3. Novelty search (3 Oct 2026, this session; requests: googleapis 11, be-api.us.archive.org 3, api.openalex.org 2,
api.semanticscholar.org 2, api.core.ac.uk 2, cryptiana.web.fc2.com 1, github.com 3 shallow clones)

| family | searched | result |
|---|---|---|
| (a) canonical series / catalogue | BnF *Catalogue des manuscrits français* entries surfaced by Books API (HQo4AQAAMAAJ, aG1oAAAAcAAJ, gHu4hDItOvMC, T0cMAQAAMAAJ) | catalogue description only ("avec chiffre"); no decipherment |
| (b) sender's / recipient's printed correspondence | Gomberville 1665 (NV-INTAKE, 4 copies); Books API `"a mon fils le duc de Rethelois"`, `"duc de Rethelois" 1589 Nevers lettre`, `"duc de Rethelois" chiffre`; IA fts same phrases | no printing of f.35 found; *Histoires de vies* (1996, owPi1a0vLgsC) cites fr.3416 fol.49 and 47, not 35; *Répertoire des ressources généalogiques...* (2003, pxPgAAAAMAAJ) matches "Fr. 3416" + "fol. 35" with no snippet -- a catalogue repertory, unread |
| (c) documentary editions / monographs | Boltanski, *Les ducs de Nevers et l'État royal* (2006, dsInahmnar8C) surfaced; inauthor search for 3416 / chiffre returned 0 | not read in full (gap to N4) |
| (d) holding archive | BnF catalogue item 30 (as quoted by NEVERS-VEIN scout) | "avec chiffre", no déchiffrement |
| (e) full text IA / Google Books / HathiTrust | IA be-api fts 3 queries; Books API 9 queries (incl. `"Fr. 3416" "fol. 35"`, `"fr. 3416" Rethelois`, `"bons deniers" Nevers Rethelois`); HathiTrust unreachable from cloud | nothing about this letter |
| (f) solver repos and blogs | fresh shallow clones 3 Oct 2026: el-descifrador/cabinet-noir 47b6db9, dbourdeau/cyphersolver e8b4287, aaymeloglu/unsolved-ciphers d2800bb, grep 3416 / btv1b9058240c / Rethelois / no.25; Tomokiyo nevers.htm live fetch, identical to sources/cryptiana mirror after CR strip, all 72 HTML comments read (Shift-JIS) | Bourdeau: sweep listings only (ark_shelfmarks.json, bnf_candidates.txt line 215, raw nevers.htm copy); Cabinet Noir and Aymeloglu: no relevant hit. Tomokiyo's comments on fr.3416 hold only the catalogue lines for no.30/no.32 and a note on how he spotted the key ("found while checking codes with large numbers in the Index"); no decode of f.35. Blogs: NV-INTAKE site searches |
| (g) scholarship | OpenAlex (2 queries), Semantic Scholar (2), CORE (2): "duc de Nevers chiffre 1589", "Nevers cipher Gonzaga sixteenth century letters" | only Desenclos & Lasry (1592 Henri IV letter to Nevers) and general Nevers scholarship; nothing on f.35. JSTOR: 2 rows queued, families (i) and (ii) |
| DECODE | sources/decode snapshots grepped for Français 3416 | no record (not re-queried live) |

## 4. Classification

| item | class | key | prior plaintext | prior decipherment | evidence / confidence |
|---|---|---|---|---|---|
| fr.3416 f.35r figure runs, key no.25 | **N3** | published (Tomokiyo's attribution of key no.25 to this letter, nevers.htm; the alphabet read by us from the period key sheet fr.3995 f.51r) | no, located nowhere | no, located nowhere | statistic robust (above); reading fragmentary; medium confidence in the class |

Why N3 and not N4: Boltanski 2006 (the principal modern study of the Nevers papers) has not been read for fr.3416 f.35. The
2003 *Répertoire* hit is unread. The JSTOR rows are unanswered (they do not block N3).
Next to reach N4: a full-text search of Boltanski 2006 for "3416" and "Rethelois" (owner's desk or library copy), plus one
look at the *Répertoire* page.

**Safe sentence:** "Under key no.25, which Tomokiyo identified for this letter, the figure runs at the foot of BnF
fr.3416 f.35r (the duc de Nevers to his son, c. late 1589) read as French letter fragments, graded 62 of 102 tokens H,
that outscore 200 shuffled keys at three seeds. No prior decipherment was located in the catalogue, Gomberville's 1665
*Mémoires*, Tomokiyo's pages, three solver repositories or the open scholarship indexes (searched 3 Oct 2026)."

**Unsafe sentence:** "We deciphered a previously unread letter from Nevers to his son", or any wording that presents
the runs as a readable plaintext or calls the result unread, new or first. The runs are fragments, 40 tokens are M,
and the clear text and nomenclator are unread.

## 5. Postmortem

The solver's NOTES.md already disclosed the four key-assisted choices and the look-before-control order, and it does not
over-claim. One sentence needs a qualifier: "Power at the measured 0.239 digit error" should say that 0.239 is the raw
blind-reader error against the reconciliation, an upper bracket, and that the residual error is unmeasured. I corrected
this in NOTES.md. No other file over-claims. The SECOND-OPINIONS-QUEUE row SO-NV02-F35 is filed in this session.

## Second audit (VERIFY-FILS-N4, 3 Oct 2026)

Verifier VERIFY-FILS-N4 (account 1, for LANE-A1), 3 Oct 2026, 09:24-09:35 UTC. I'm separate from both the solver and
VERIFY-NV02. I did no decoding and read no images. The question was whether the two gaps that section 4 named between
N3 and N4 can be closed. Requests: www.googleapis.com 62 (Books API, `country=US` + key; about 10 answered 503 and were
retried once at 4 s spacing), archive.org advancedsearch 3, be-api.us.archive.org 2, api.openalex.org 3,
api.semanticscholar.org 2, api.core.ac.uk 3, api.archives-ouvertes.fr 3, persee.fr 1, scienceblogs.de 2,
klausschmeh.net 1, ciphermysteries.com 1.

### Gap 1: Boltanski 2006 (*Les ducs de Nevers et l'État royal*, Droz, ISBN 9782600010221)

The book is on Google Books as dsInahmnar8C (PARTIAL view). A second id, UAloAAAAMAAJ, is the same ISBN with NO_PAGES.
It is not on Internet Archive (advancedsearch by title and by creator). I searched inside it through the Books API
(`q=<phrase> isbn:9782600010221`).

**How the search behaves.** A single unquoted word returns 0 even for words certainly in the book ("Nevers",
"Gonzague"). Quoted phrases do work. So every query below that counts was quoted.

**Positive control.** The book cites fr.3416 in the form "Mss. Fr. 3416 , f ° NN". I tested that exact form:

| query | result |
|---|---|
| "3416 , f ° 59" | hit (4 Sept 1580, to Brulart) |
| "3416 , f ° 60" | hit (3 Sept 1580, Nevers to the king) |
| "3416 , f ° 66" | hit (31 Oct 1589) |
| "3416 , f ° 80" | hit (14 Dec 1580, to Crillon) |
| **"3416 , f ° 35"** | **0** |
| "3416 , fol . 35" | 0 |
| "3416 , f ° 35 v" | 0 |

The control found 4 of 4 known citations, so the search can find a citation of this form. Matching is if anything
loose: "3416 , f ° 38" returned a passage showing only f ° 59, and a loose matcher should over-report, not under-report.

**Other quoted queries:**

- "Fr. 3416" Rethelois: 0
- "Fr. 3416" "fils": 0
- "Fr. 3416" "son fils": 0
- "Fr. 3416" chiffre: 0
- "Rethelois" "1589": 0
- "déchiffrement": 0
- "déchiffré": 0
- "chiffrée": 0
- "chiffres": 0
- "son fils" "chiffre": 0

**The queries that hit are not about this letter:**

- "lettres chiffrées": Henriette de Clèves to Louis de Gonzague, April 1585.
- "chiffre" Nevers: a sum of money (marriage of Catherine de Gonzague).
- "en chiffre": an army's numbers, 1577.
- "duc de Rethelois", and "Rethelois" Nevers: lordship and revenues.

**Result.** No citation of fr.3416 f.35 and no decipherment of it is located in Boltanski 2006. Searched by
positive-controlled phrase search, 3 Oct 2026.

This is a search-inside, not a page-by-page read. The API shows one snippet per query, so it rules out a citation in
the forms tested, not a paraphrase that never gives the folio.

### Gap 2: the 2003 *Répertoire* hit

The hit is Jean-Philippe Gérard, *Répertoire des ressources généalogiques et héraldiques du Département des manuscrits
de la BnF* (Mémoire & documents, 2003, ISBN 9782914611145, 394 pp.). It is on Google Books as pxPgAAAAMAAJ and
2L0WAQAAIAAJ, both NO_PAGES, and it is not on Internet Archive.

Search-inside results:

- "Fr. 3416": matches (2L0WAQAAIAAJ), no snippet.
- "Fr. 3416" "fol. 35": matches, no snippet.
- "Rethelois": 0
- "chiffre": 0
- "Nevers": 0
- "Gonzague": 0
- "Clèves": 0
- "Fr. 3417" (control): 0
- "zzqqxx" (null): 0

That "Nevers" and "Gonzague" both return 0 suggests the entry cites f.35 for a genealogical or heraldic item, not for
the letter as such. That is an inference (grade I).

**Result: the page stays unread.** It cannot be reached from the cloud: NO_PAGES, no IA copy, and the
books.google.com page view is bot-blocked (Access playbook table). ASKS row 110.

### Gap 3: the remaining rule-10 families

This pass added these families. Section 3's own entries stand.

| family | searched (3 Oct 2026) | result |
|---|---|---|
| OpenAlex (key) | "Nevers Rethelois 1589"; "Gonzague Nevers lettres chiffrées"; "duc de Nevers correspondance chiffre" | 3 / 0 / 959 results; none on fr.3416 or a Nevers decipherment |
| Semantic Scholar (key) | "Nevers Rethelois"; "Gonzague Nevers chiffre 1589" | noise / 0 |
| CORE (key) | "Nevers Rethelois chiffre"; "Boltanski Nevers" | one relevant-looking hit, the Gallica record of BnF fr.4715 ("Recueil de pièces ... la plupart en chiffre", ark btv1b52509819x), a different manuscript; Boltanski 1999 on Nevers 1614-17, wrong generation |
| HAL | Rethelois AND chiffre; Nevers AND Rethelois AND 1589; "fr. 3416" | 0 / 0 / 0 |
| Persée | "Rethelois chiffre Nevers" (first page) | lordship and Ligue context only; nothing on a cipher letter to the son |
| IA full text (be-api) | "duc de Rethelois" chiffre; "Rethelois" "déchiffrement" | 432 / 690 hits, first pages: poetry, BnF catalogue volumes ("Lettre, avec chiffre et déchiffrement" entries for other manuscripts), local history; nothing on f.35 |
| Cipherbrain (scienceblogs.de and klausschmeh.net) | ?s=Nevers, ?s=Rethelois | Nothing Found |
| Cipher Mysteries | ?s=Nevers | Nothing Found |
| JSTOR | family (i) and (ii) rows already queued (JSTOR-QUEUE.tsv rows 177-178) | unanswered; does not block |

The decoded runs have no phrase distinctive enough to quote. Their longest stretches are ".aisi.nlesauroit" and
"b.onnefaSUN.as.", so a phrase search on the decode is not meaningful. "bons deniers" (clear text beside run 3) was
searched in Boltanski (0) and by VERIFY-NV02 in the Books API at large (nothing about this letter).

### Classification

| item | class | key | prior plaintext | prior decipherment |
|---|---|---|---|---|
| fr.3416 f.35r figure runs, key no.25 | **N3 (kept)** | published (Tomokiyo's attribution of key no.25 to this letter; the alphabet was read by us from the period key sheet fr.3995 f.51r) | none located | none located |

Why N3 is kept: gap 1 is closed within the limits of a search-inside. Gap 2, the one page that section 4 itself named
as a condition for N4, is still unread and cannot be read from the cloud. I don't promote on an inference about what an
unread page says.

What would make it N4: one look at the Gérard 2003 *Répertoire* entry for "Fr. 3416 fol. 35" (ASKS row 110). If the
entry is genealogical or heraldic, or a catalogue line without a decipherment, N4 follows with no further search.

**Safe sentence:** "Under key no.25, which Tomokiyo identified for this letter, the figure runs at the foot of BnF
fr.3416 f.35r (the duc de Nevers to his son, c. late 1589) read as French letter fragments, graded 62 of 102 tokens H,
that outscore 200 shuffled keys at three seeds. No prior decipherment was located in the BnF catalogue, Gomberville's
1665 *Mémoires*, Boltanski's *Les ducs de Nevers et l'État royal* (2006, phrase search with a positive control),
Tomokiyo's pages, three solver repositories, the cipher blogs or the open scholarship indexes (searched 3 Oct 2026)."

**Unsafe sentence:** "No prior decipherment located in the principal editions and catalogues". That is the N4 wording,
and the *Répertoire* entry is unread. Also unsafe: any wording that calls the runs a plaintext of the letter, or calls
the result new, unread or first.

**Postmortem.** Nothing in the target's files over-claims beyond what section 5 already corrected. Section 4 called
the Boltanski step a job for the owner's desk or a library copy; it needed only the Books API with quoted phrases,
because unquoted single words silently return 0. I recorded that behaviour above for the next verifier. The
SECOND-OPINIONS-QUEUE row SO-NV02-F35 already exists, and the class did not change, so no new row was added.

Propagation (FILS-NOMEN, 3 Oct 2026, rule 10): token grades on f.35r are now H 74 / M 28 of 102 (the safe sentence above says 62 H; FILS-CLEAR moved 9, FILS-NOMEN 3; no decoded letter changed); code words xiiij = Seigneur and 28 = Ml de Biron added at M via keys/key_no25_nomenclator.tsv.

## Gérard 2003 *Répertoire* entry, cloud route (A1B-FILS-LQ, account 1 for LANE-A1B, 3 Oct 2026, 16:4x UTC)

Search log only, no class change (a worker, not a verifier). ASKS 110 asked for one look at the "Fr. 3416 fol. 35" entry
in Jean-Philippe Gérard's *Répertoire des ressources généalogiques et héraldiques du Département des manuscrits de la BnF* (2003, ISBN 9782914611145).
Routes tried, one request each, 3 Oct 2026: archive.org advancedsearch (title) 0 items; Google Books volume 2L0WAQAAIAAJ
`NO_PAGES` (confirmed again with key + `country=US`), `"3416" inauthor:Gérard répertoire` 0 items; Gallica SRU, the title phrase
returns only unrelated heraldry books, so the *Répertoire* is not in Gallica. **HathiTrust bibliographic API (ISBN): record 004336226, htid
`mdp.39015059979289`, "Limited (search-only)".** **HTRC Extracted Features API** for that htid (406 pages, per-page token
counts, no word order): the token `3416` occurs on one page only, seq 00000176 (501 tokens, 38 lines). That page's vocabulary is
the index section on princely and royal **households**: *maison* x12, *officiers* x5, *Rôle(s)*, *gages*, *pensions*,
*pensionnaires*, *domestiques*, *gentilshommes*, *Comptes*, *État(s)*, *dépense(s)*, *Clairambault* x3, *Fr* x15, *fol* x13,
with *Nevers* x3, *Mantoue* x1 (no *Gonzague*), *duc*/*duchesse*, and the tokens `3416` and `35` once each. The page carries **no** token
containing *chiffr* (no *chiffre*, *chiffré*, *déchiffrement*), nor *lettre(s)*; the only *chiffr* tokens in the volume are on
seq 20, 21, 41, 44, 46, 47, 65 (front matter and early sections, none with 3416).
Reading of that evidence (inference, grade I: bag of words, the entry's own sentence is not quoted): fr.3416 fol.35 is
indexed by Gérard as a source for a Nevers household (officers, rolls, wages), a catalogue line of the genealogical kind,
and nothing on that page mentions a cipher or decipherment. This is the "genealogical or heraldic, or a catalogue line
without a decipherment" case the second audit named; whether it is enough for N4 without the sentence itself quoted is the
next verifier's call, not this worker's. No LOCAL-QUEUE row filed; if a verifier wants the exact wording quoted, the route
is a LOCAL-QUEUE `hathitrust-page` row on full-text search inside mdp.39015059979289 for "3416" (snippet only, search-only volume).
Requests: archive.org 1, be-api.us.archive.org 1, www.googleapis.com 3, catalog.hathitrust.org 3, data.htrc.illinois.edu 1, gallica.bnf.fr 1.

Propagation (A1B-FILS-L10, 3 Oct 2026, rule 10): the code word 28 = Ml de Biron (added at M by FILS-NOMEN, line above) is
withdrawn -- two blind reads put the stroke taken for its overbar with line 11's writing (NOTES.md "A1B-FILS-L10 results").
Token grades on f.35r are unchanged (H 74 / M 28 of 102); the only code word left is xiiij = Seigneur (M). Class unchanged.

## Third audit: Gérard 2003 *Répertoire* weighed for N4 (A1B-VERIFY-FILS-N4b, account 1 for LANE-A1B, 3 Oct 2026, 17:01-17:10 UTC)

Verifier, separate from the solver sessions and from A1B-FILS-LQ. The rule I apply was fixed in advance by the second
audit's own text (committed before this pass): "If the entry is genealogical or heraldic, or a catalogue line without a
decipherment, N4 follows with no further search."

**Independent re-check (script, scratchpad only).** HTRC Extracted Features API, mdp.39015059979289, all 406 pages,
header+body+footer token counts, one request:
- `3416` occurs once in the volume, on seq 00000176 only. `3415`, `3417`, `3418`: 0 in the volume.
- Seq 176 (505 tokens, 39 lines): *maison* x12, *État* x6, *officiers* x5, *Rôle* x3, *gentilshommes* x3, *Comptes* x3,
  *Clairambault* x3, *gages* x2, *domestiques* x2, *Nevers* x3, *Mantoue* x1, *Lorraine*, *Bourbon*, *Montpensier*,
  *Navarre*; 47 distinct numerals (manuscript and folio numbers of other entries), `35` among them. No token containing
  *chiffr* or *déchiffr*, no *lettre(s)*, no *Gonzague*, *Rethel*, *Clèves* or *Biron*. This matches A1B-FILS-LQ exactly.
- The volume's only *chiffr*/*déchiffr* tokens (7) are on seq 20, 21, 41, 44, 46, 47, 65: front matter and early
  sections, none with 3416. *Gonzague* is on seq 307 and 363, *Rethel* on 331 and 380, all away from 3416.
- HathiTrust full-text search-only (babel.hathitrust.org, `pt/search?q1=3416`): HTTP 403 Cloudflare "Just a moment",
  logged unreachable, not retried.
- Google Books API (key + `country=US`): volume 2L0WAQAAIAAJ still `NO_PAGES`; `"Fr. 3416"` (315 items) and
  `"Fr. 3416" chiffre` (26) return only "fr. 3,416" sums and federal regulations; `"3416" Nevers maison` (82) lists the
  *Répertoire* (pxPgAAAAMAAJ, no snippet) and, independently, Viennot's *Femmes en fleurs, femmes en corps* describing
  "Ms. fr. 3416 : Pièces et lettres diverses (maison de Nevers)" -- the same household/family framing as Gérard's page.

**Weighing.** The question for N4 was never what Gérard's sentence says word for word, but whether the *Répertoire*
carries a decipherment of f.35. It is a source index for genealogy and heraldry; the page that cites fr.3416 is a
household-rolls index; and a full per-page token count, not a single search snippet, shows no cipher or decipherment
word on that page and none anywhere near it. A printed decipherment cannot sit in an entry with no word for cipher,
decipherment or letter. That is the "catalogue line without a decipherment" case the second audit pre-registered. What
stays inference (grade I) is only the entry's exact wording and whether its "fol. 35" refers to the letter or to a
household item on the same folio range; neither changes the answer. One caveat: OCR could drop a token, but a 2003
printed book's OCR losing *chiffre* on exactly that page is not a reason to withhold N4 by itself.

The remaining families: Boltanski 2006 closed within search-inside limits (second audit, gap 1); open indexes, cipher
blogs, solver repositories, Tomokiyo, Gomberville and the BnF catalogue covered (sections 3 and Gap 3); JSTOR rows
177-178 unanswered, which do not block N4 (Verifier brief 2(g)).

### Classification

| item | class | key | prior plaintext | prior decipherment |
|---|---|---|---|---|
| fr.3416 f.35r figure runs, key no.25 | **N4** (from N3) | published (unchanged: Tomokiyo's attribution of key no.25 to this letter; the alphabet read by us from the period key sheet fr.3995 f.51r) | none located | none located |

**Safe sentence:** "Under key no.25, which Tomokiyo identified for this letter, the figure runs at the foot of BnF
fr.3416 f.35r (the duc de Nevers to his son, c. late 1589) read as French letter fragments, graded 75 of 102 tokens H,
that outscore 200 shuffled keys at three seeds. No prior decipherment located in the principal editions and catalogues:
the BnF catalogue, Gomberville's 1665 *Mémoires*, Boltanski's *Les ducs de Nevers et l'État royal* (2006, phrase
search), Gérard's 2003 *Répertoire* (per-page word counts), Tomokiyo's pages, three solver repositories, the cipher
blogs and the open scholarship indexes (searched 3 Oct 2026); internal or unpublished work not excluded."

**Unsafe sentence:** "First decipherment" or "previously unread letter" without the qualifier; "no prior decipherment
exists"; any wording that calls the runs a plaintext of the letter (they are fragments, 28 tokens M, clear text and
nomenclator only partly read). The key is `published`, so "our key" is unsafe too.

**Postmortem.** No over-claim found in the target's files. Propagation: SECOND-OPINIONS-QUEUE row SO-NV02-F35 carries no
class field and its prompt states no class, so nothing to change there; status.json `fields_source` still says "N3
kept" (the parent's file, flagged in ROOM.md). NOTES.md's N3->N4 gap removed. Requests: data.htrc.illinois.edu 1,
babel.hathitrust.org 1 (403), www.googleapis.com 4.

Propagation (A1B-FILS-XIIIJ2, 3 Oct 2026, rule 10): a third blind read on a wider crop (lead-in visible) met the
pre-registered G1 (NOTES.md "A1B-FILS-XIIIJ2"), so the L02 code word moves M -> H as **xiiij = Seigneur** (key no.25
nomenclator row H). Token grades on f.35r are now H 75 / M 27 of 102; the safe sentence above is updated from 74 to 75.
No decoded letter and no score changed (the code word is not a letter token). SO-NV02-F35's prompt carries the change. Class N4 unchanged.

Desenclos check, 4 Oct 2026 (DESENCLOS-PREMISE, account 3): no hit. Searched 17 open full texts of the 36 items in sources/desenclos/2026-10-04/bibliography.tsv (HAL PDFs, DSpace Tartu HistoCrypt 2024/2025 PDFs, OpenEdition HTML; built from HAL, theses.fr, OpenAlex, Semantic Scholar, CrossRef, Google Books) for this item's shelfmark, sender/recipient, place and date (terms.tsv, search-log.tsv, search.py); none names this item, its key or its plaintext. Not read: her 2014 thesis (theses.fr: not online) and 2017/2021 cryptography chapters (not open; JSTOR-QUEUE rows of 4 Oct 2026).
