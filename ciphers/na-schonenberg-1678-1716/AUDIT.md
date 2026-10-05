# AUDIT -- na-schonenberg-1678-1716 (NA 1.02.04 invnr 63)

Verifier: VERIFY-SCHONENBERG (account-4), 2 Oct 2026, 23:17-23:4x UTC (container clock). This session did no solving and
did not decode beyond the rule-7 re-derivation. Brief: the account-4 parent's VERIFY-SCHONENBERG instruction (rule 10 template
plus rule 7). No earlier AUDIT.md existed.

Claim under audit: "the leaf's body read from its own interlinear gloss (grade C), leaf C 270 / M 11, body C 243 / M 10
(7 illegible + 3 NULL), target parked; code 36 = c by a gloss-hand letterform test (known answer 10/10, narrow: the c class
rests on 2 tiles)."

## 1. Extract

| field | value |
|---|---|
| Archive | Nationaal Archief, toegang 1.02.04 (Archief van F. van Schonenberg, gezant in Spanje en Portugal, 1678-1716), invnr 63, 1 leaf, 1 scan |
| Catalogue entry (re-read this session, item page drupal-settings-json `unittitle`) | "Aan dona Antonya de Albanylla, z.d." -- finding aid adds "In cijferschrift"; section "Minuten van uitgaande brieven aan overige correspondenten, 1702-1716 en z.d." |
| Image | https://www.nationaalarchief.nl/onderzoeken/archief/1.02.04/invnr/63 ; file https://service.archief.nl/api/file/v1/default/fc3a8d42-b89e-4715-9753-0320355365c7 (native 1946x2618) |
| Date | undated (z.d.); the section covers 1702-1716 (Lisbon years); a possible "23 de Nobe[mbre]" in the L01 gloss was not confirmed by the readings (L01 reads "no abyendo nobe-") |
| Sender | Francisco van Schonenberg's chancery (retained draft/minute of an outgoing letter), by the finding aid's placement; no signature on the leaf |
| Recipient | Doña Antonia (Antonya / Antonija) de Albanylla, per the catalogue and the clear address on the leaf |
| Place | not stated on the leaf; Lisbon by the section's date range (inference) |
| Language | Spanish |
| Plaintext as read (reading.txt letters, one /-separated run per line L01-L14, L18, L19; NULLs omitted) | "noabyendonobe/dadenestaspartesque/ladeabermudadoeste/gouyernoconlaszyrcun/stanzyasqueaysesabra/nmexoresperoconansya/lasqueybyeredelnor/teydeytalyapuesesau/andeocasyonarlasque/puedanocuryrz/parayasseguradadde/lalorespondenzyase/pondrasolamenteyn/sobrescrytoenesta/forma/adoñaantonyadealbanylla" -- word segmentation and expansion ("No aviendo novedad en estas partes que la de aver mudado este govierno con las circunstancias ... para mas seguridad de la correspondencia ... pondra solamente en sobrescrito en esta forma: A Doña Antonya de Albanylla") is M/I-grade sense, body/reading_body.txt, not part of the graded token reading |
| Distinctive phrases | "no abyendo novedad en estas partes", "aver mudado este gouyerno", "las que ubiere del norte y de ytalya", "para mas seguridad de la corespondenzya", "pondra solamente en sobre escrito en esta forma", "dona antonya de albanylla" |
| Ciphertext | ciphertext.tsv, 281 tokens (2-digit numbers with tick modifiers and a few symbols), homophonic, 87 codes |
| What the solvers searched | check-solved 25 Sept 2026 (6 sources: web, IA full text, Heinsius Briefwisseling on Huygens retroboeken, Cryptiana/Cipherbrain, DECODE dumps, both solver repositories); web and blog check 2 Oct 2026 (10 queries, three blogs, two Utrecht theses 403); Premise check 2 Oct 2026 (solver repos re-cloned, NA neighbours invnr 58-64, Willem III-Bentinck, Staten-Generaal, Heinsius, Google Books) |

## 2. Rule-7 re-derivation (fresh session, committed key and ciphertext only)

- `python3 tools/decode_key.py ciphers/na-schonenberg-1678-1716 --check` -> "ciphertext.tsv: tokens 281: C 270, M 11 / reading up to date", exit 0.
- Independent re-application by this session (a 20-line script reading only key.tsv, exceptions.tsv, ciphertext.tsv; not
  decode_key.py): every one of the 281 token values agrees with reading_tokens.tsv. The only differences are (a) NULL
  tokens, which decode_key.py omits from reading.txt and the script printed (L10 pos0-2, L14 pos3, L01 blot) -- display only;
  (b) two grades (L04 pos19 code 45, L08 pos15 code 26) that decode_key.py caps at M because the transcription confidence of
  the group is M -- by design. Differences beyond the M-graded tokens: **0**. The reading is not sent back.
- Grade counts confirmed from reading_tokens.tsv: body L01-L14 C 243 / M 10; L18 C 5; L19 C 22 / M 1; leaf C 270 / M 11, H 0.
- Note for readers of the files (not an error): ciphertext.tsv's `gloss` column is passB's raw positional gloss before the
  2 Oct re-sync, so against the key it agrees at only 143 of 246 glossed positions; the drift is a column offset in whole
  runs (e.g. L02, L08, L12, L13 shift by one), which align/ (tools/interlinear_align.py) corrects. The C grades rest on the
  aligner plus five image passes, not on that column as written.
- Code 36 = c (GAPS14): the 4 tokens change no letter (36 was c at M before); the test is narrow (2 c reference tiles,
  1 of 20 shuffle seeds reaches the target, tile boxes placed by a label-aware worker). Accepted at C as registered; if a
  later reader disputes it, the cost is 4 tokens C -> M, no text change.

## 3. Independent search log (this session, 2 Oct 2026)

| family | searched | result |
|---|---|---|
| (a) canonical series / state papers | Huygens retroboeken *Briefwisseling Heinsius 1702-1720* `search_in_text`: Albanilla, Albanylla, Albanila, Albanija -> 0 each; positive control Schonenberg -> 413 (works). *Correspondentie Willem III en Bentinck* `searchText`: same four -> 0 each; control Schonenberg -> 11. Staten-Generaal edition ends 1625 (out of range; Premise check) | no hit |
| (b) sender/recipient printed correspondence | none exists on IA (check-solved); Heinsius and Willem III editions above carry Schonenberg's official letters only | no hit |
| (c) documentary editions | print_check.py ia-global (IA full text, all items) on 9 phrases (phrases.txt): 0 hits each | no hit |
| (d) holding archive | NA item page invnr 63 re-read (unittitle as above, "cijferschrift"); finding aid read in full by check-solved; no decipherment or transcription mentioned | catalogue flags cipher only |
| (e) IA / HathiTrust / Google Books | print_check.py: IA fts 0/9; Google Books (key, country=US) returns loose word matches for the long phrases (legal codes, 19th-c. gazettes, blazon books for the surname Albanilla) -- none is this letter, the API does not enforce the quote; HathiTrust full text unreachable from the cloud (CLAUDE.md hosts table) | no hit |
| (f) solver repos, blogs | fresh shallow clones of dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers, grep albanil/albanyl/schonenberg/1.02.04: only the roell1809 aside (wrong-archive-number note), not this item. WebSearch: 3 queries ("Albanylla" OR "Albanilla" Schonenberg carta cifra; the "seguridad de la correspondencia" + sobrescrito phrase; Herrero Sánchez Conectores sefarditas cifrada) -> nothing on this letter | no hit |
| (g) scholarship | OpenAlex (key): 2 keyword searches -> Herrero Sánchez, "Conectores sefarditas ... El caso Belmonte/Schonenberg", *Hispania* 76/253 (2016) 445-472, doi 10.3989/hispania.2016.014, and the UU thesis "Diplomatie eind zeventiende eeuw ... De casus Francisco van Schonenberg" (2016). CORE (key): "Schonenberg AND (cifra OR cijferschrift OR cipher)" 0; "Albanilla OR Albanylla" 4 (geology/zoology place-name hits); "Schonenberg AND Belmonte" 0. Semantic Scholar: mostly 429, 2 answered (0 relevant). CrossRef: 1 answered (noise), 3 429. JSTOR: rows appended to JSTOR-QUEUE.tsv, families (i) and (ii) | no hit |
| unreachable | Herrero Sánchez 2016 full text: hispania.revistas.csic.es fails TLS from the cloud (curl 000, browser 502 x3), ResearchGate 403; Wayback CDX connection reset. UU thesis: 403 (2 Oct, earlier pass). These are the two studies of Schonenberg himself; neither has been read by anyone in this repo | unreachable |

Requests this session: resources.huygens.knaw.nl 12 (>=2.1 s apart); www.nationaalarchief.nl 1; github.com 2 clones;
be-api.us.archive.org 9, www.googleapis.com 9, api.openalex.org 12, api.semanticscholar.org 9, api.crossref.org 2,
api.core.ac.uk 4; hispania.revistas.csic.es 2 (+ browser 3 attempts), researchgate.net 1, dialnet.unirioja.es 1,
web.archive.org 1; WebSearch 3. One retry at most per host after a block.

## 4. Classification

| item | tokens | N-class | prior plaintext | prior decipherment | key source | evidence | confidence |
|---|---|---|---|---|---|---|---|
| A. Body L01-L14 | 253 | **N0** | yes, in manuscript: the contemporary interlinear Spanish gloss over every body line of this very leaf; not found in print | **yes:** that gloss is the period decipherment of this item, letter over group | `period` | gloss over all 14 lines; aligner agreement 0.699 vs shuffled-gloss control max 0.301 (n=300); five image passes | high |
| B. L18 (5 groups) | 5 | **N0** | yes, in manuscript: its own gloss "forma." on the leaf | yes, the gloss | `period` | layout image check (GAPS) | high |
| C. L19 (23 groups) | 23 | **N2** | yes, in clear on the same leaf: the address "A Doña Antonija de Albanylla" | no: the leaf carries no gloss over L19, and no mapping of these groups to the address was located | `ours` (the crib alignment, crib_align.py, 15/16 resolved positions vs slid-window max 0.286 and shuffled-crib max 0.438; letter values themselves come from the period-gloss key) | moderate-high (1 M token, the blotted ?9) |
| Leaf as a whole | 281 | **N0** | -- | the leaf is a deciphered cipher letter; our work is a transcription and code-alignment of a decipherment already written on it | `period` (body), `ours` (L19 alignment only) | -- | high |

Why `period` and not `ours` for the body: every plaintext letter of L01-L14 and L18 is written on the leaf in the gloss
hand; the repo's alignment (tools/interlinear_align.py) and image passes only decide which gloss letter belongs to which
group and so recover the code table. The plaintext was not produced by us. Precedents: clair1067-brienne-poland-1646 and
clair1108-duvergier AUDIT.md (an interlinear decipherment on the leaf is N0 without print), fr5160-letellier-1653; the
Dupuy 468 counter-precedent (an undescribed manuscript gloss) is noted -- here the catalogue says only "In cijferschrift"
and does not describe the gloss, which is exactly the clair1067 situation, ruled N0 there.

No item is N3 or better, so no SECOND-OPINIONS-QUEUE.tsv row is filed (the brief's "at N3 or better" condition).

**Safe sentence:** "NA 1.02.04 invnr 63, a cipher letter from Schonenberg's chancery to Doña Antonia de Albanylla, carries a
contemporary interlinear decipherment on the leaf; we transcribed it, aligned it with the 87 cipher codes (key rebuilt from the
period gloss, grade C 270 / M 11 of 281 tokens), and read the unglossed address line from the clear address on the same leaf.
No printed edition or published transcription of the letter was located (search log in AUDIT.md, 2 Oct 2026)."

**Unsafe sentence:** "We deciphered / first read a previously unsolved Schonenberg cipher letter" -- the leaf was deciphered
in the period; our contribution is transcription, key table and the L19 mapping.

## 5. Postmortem and corrections

No over-claim found: NOTES.md, HYPOTHESES.md and reading.txt contain no "new / first / unpublished" wording, and the
status word `partial` with Verdict "parked" stands. Two stale sentences in early sections, superseded by later ones in the
same file, are flagged in a correction line added to NOTES.md (no text deleted): VX-RD01's "L18 and L19 ... no gloss on the
leaf at all" (L18 carries "forma.", GAPS 2 Oct) and its L18-L19 judge "PASS" on 19 letters (superseded by the GAPS/GAPS2
FAIL on the full 28-letter string); and reading.txt's header still says "U = code never seen in the gloss" and
"L18-L19 carry NO gloss" (decode.json header text; 0 U tokens remain, L18 is glossed) -- left for the target's owner to
regenerate, since editing decode.json is a solver change. Result kind for the board: **recovery** (period key), text
`known` in manuscript, key `period`.

Open, not blocking: Herrero Sánchez 2016 (*Hispania*, OA but unreachable from the cloud) and the 2016 Utrecht thesis are
the only studies of Schonenberg's correspondence; a person's browser read of either for "Albanilla" or "cifra" would close
the one family this audit could not reach. It cannot lower the class below N0 for the body.

## Register note (VER1-REG, 5 Oct 2026; no new audit)

A separate verifier session (VER1-REG, account 2, for LANE-VER1) set the registers from section 4 above, without re-searching:
PROGRESS.tsv column `1` = x (source: this AUDIT.md); status.json target row `novelty` N0, `audit_status` 'one audit'.
Depth (rule 4a), set from section 2's counts: **D3**, 96.1% of tokens C (270 of 281; H 0, S 0), residue 11 M = 7 illegible,
3 NULL, 1 blot (no name codes); external check = the period gloss over L01-L14 and L18 (aligner 0.699 vs shuffled-gloss max
0.301, n=300); not D4 because the M residue is not limited to name/code groups. Outward words: "largely deciphered (about 96%)"
-- here by the period gloss on the leaf, so the safe sentence in section 4 still governs: the text is the period's decipherment,
the code table is ours. Depth sentence (true, from the gloss): the letter tells Doña Antonia de Albanylla that, for greater
security of the correspondence, only a cover address in the form "A Doña Antonya de Albanylla" will be used.

## AUDIT 2 (D2B-SCHON, 5 Oct 2026)

Verifier: D2B-SCHON (account 2, LANE DEFAULT-account-2-20261005-2217), 5 Oct 2026, 23:35-23:4x UTC by `date -u`. A fresh
session: not the solver (VX-RD01, GAPS-GAPS14) and not Audit 1's author (VERIFY-SCHONENBERG, account-4). Brief: the lane's
D2B-SCHON job, under the "Verifier jobs" rules of .claude/briefs/runs/2026-10-05-account1-default-2217-jobs.md. No decoding;
the reading, key.tsv and decode.json are untouched. Aim: break Audit 1's N0 for the body and, above all, L19's N2.

**Revisions since Audit 1:** none. The folder has no commits after Audit 1 beyond the VER1-REG register note and RUN4-WAITBF's
"While waiting" line. The reading is still C 270 / M 11 of 281 and `decode_key.py --check` exits 0 (Audit 1 section 2). This
target has no SECOND-OPINIONS-QUEUE.tsv row, so nothing needs to be carried into one.

### A2.1 Search log (5 Oct 2026; every family searched or unreachable)

| family | searched | result |
|---|---|---|
| holding archive | NA item page 1.02.04 invnr 63, re-read (drupal-settings-json): unittitle "Aan dona Antonya de Albanylla", odd ["In cijferschrift"], availability DIGITALIZED + PHYSICAL; scope, physdesc and acqinfo are empty | unchanged since 2 Oct; no transcription, decipherment or gloss described |
| studies of Schonenberg (Audit 1's unreached family) | **Utrecht student theses, now reachable** (studenttheses.uu.nl DSpace 7 API `server/api/discover/search/objects?query=Schonenberg`): three theses, all downloaded and read in full by script. (1) W. Steketee, "Franciscus van Schonenberg: diplomaat en spin in het web tussen Portugal en de Republiek" (2012, .doc, ~15,500 words; this is the record behind the handle 20.500.12932/20077 that answered 403 on 2 Oct). It covers his Lisbon years, cites NA 1.02.04 only as "toegangsnummer 45-47" and once generically, and has no Albanilla/Albanylla, no cijfer/cifra/chiffre/geheimschrift. (2) M. van Weede, "Schonenberg, netwerker of pion? Diplomatieke netwerken in 17de-eeuws Spanje" (2015, .docx, 7,147 words): cites 1.02.04 "(Archief van Schonenberg, 1676-1702)" only; no Albanilla, no cipher. (3) M. Verbraak, "Diplomatie eind zeventiende eeuw: theorie en praktijk. De casus Francisco van Schonenberg, gezant in Madrid" (2016, PDF 34 pp., 11,321 words; the old dspace.library.uu.nl/handle/1874/334523 now answers 404): cites 1.02.04 inv. 6 (3 Dec 1699); its one cipher mention is a Heinsius letter "in geheimschrift" to Schonenberg in Madrid, c.1700, which is another letter and another office; no Albanilla | no hit; family closed for the theses |
| studies of Schonenberg, continued | Herrero Sánchez, "Conectores sefarditas ...", *Hispania* 76/253 (2016) 445-472, doi 10.3989/hispania.2016.014 (OA, CC BY). OpenAlex and Semantic Scholar both give only the publisher PDF (hispania.revistas.csic.es/.../download/494/488): curl fails with "unable to get local issuer certificate" (the origin's chain, not the proxy's CA), and tools/browser_fetch.js --binary got 502 three times. Dialnet record 5604165 was read: it has the abstract only, and its "Texto completo" link points to the same host. The abstract places the article on Belmonte/Schonenberg's network, Madrid and Amsterdam, second half of the 17th century, and does not mention Lisbon-era private correspondents. CORE has no full-text copy (title search: 5 "Conectores" records, all fullText 0). Wayback CDX: connection reset | **unreachable** (full text), abstract read |
| canonical / state series | not re-run; Audit 1 section 3 covered Heinsius Briefwisseling, Willem III-Bentinck and Staten-Generaal on 2 Oct, all with 0 Albanilla hits | carried from Audit 1 |
| IA full text (be-api fts) | "Albanylla" 0; "Antonia de Albanilla" 0; "Albanilla" + Schonenberg 4, all atlas/gazetteer place-name indexes | no hit |
| Google Books API (key, country=US) | "Antonia de Albanilla": 182 loose matches (1822 Cortes diaries, blazon books for "Abanilla"), none this letter; "Antonya de Albanylla": HTTP 503, not retried (the same query 503'd twice on 2 Oct): unreachable; Schonenberg Albanilla: 3 (1956 Journal officiel place-name hits); "pondra solamente en sobre escrito": 349 loose legal-code matches (the API does not enforce the quote), none this letter; Schonenberg cifra Lisboa Belmonte: 0 | no hit |
| CrossRef | Schonenberg Albanilla: 3 noise records | no hit |
| HAL | Schonenberg AND (cifra OR chiffre OR Albanilla): numFound 0 | no hit |
| CORE | fullText Schonenberg AND (Albanilla OR Albanylla OR cifra): HTTP 500, not retried; Audit 1's CORE queries (2 Oct) stand | unreachable this pass |
| solver repositories | fresh shallow clones on 5 Oct (cyphersolver head 5 Oct 2026, unsolved-ciphers head 27 Sept 2026), grep albanil/albanyl/schonenberg: the only hit is cyphersolver targets/roell1809/NOTES.md (the 1.02.04 wrong-archive-number note), not this item | no hit |
| JSTOR | the 2 Oct rows (164-166 and 163 in JSTOR-QUEUE.tsv, answered 4 Oct, no relevant hit) already cover both families. Three more appended: (i) "Schonenberg" AND (Lisboa OR Lisbon OR Portugal) AND (cifra OR ... cipher); (ii) bare phrases "Albanylla" and "de aver mudado este govierno" | queued; never blocks the class |
| not repeated | Persée, OpenAlex keyword sweeps, Semantic Scholar keyword sweeps, blogs (Cipherbrain, Cryptiana, Cipher Mysteries) and DECODE dumps: covered by Audit 1, the GAPS web check and the Premise check on 2 Oct; nothing has changed since | carried |

Requests this session: studenttheses.uu.nl 6, dspace.library.uu.nl 1 (404), api.openalex.org 2, api.semanticscholar.org 1,
dialnet.unirioja.es 2, hispania.revistas.csic.es 1 curl + 3 browser attempts, api.core.ac.uk 3, web.archive.org 1 (reset),
be-api.us.archive.org 3, www.googleapis.com 5 (one 503), api.crossref.org 1, api.archives-ouvertes.fr 1,
www.nationaalarchief.nl 1, github.com 2 clones. Each host was paced at 1.5 s or more between requests, and no host was retried
after a block.

### A2.2 Attempts to break the classes

- **Body N0: is the gloss really period?** One look at images/crop_top.jpg (L01-L02, Audit 1's crop): the interlinear letters
  ("n o a b y e [n] d o N o b e", "d a d e n e s t a s p a r t e s q u e") are spaced one over each code group, in the same
  brown ink and a comparable pen to the codes and the clear "Amigo". The orthography is period: "abyendo", "gouyerno", "ubiere",
  y for i, z for c. A modern archivist's decipherment would not be written that way, and the finding aid does not mention one.
  The gloss is period. **One wording correction (not a class change):** the leaf is a retained *minute of an outgoing letter*,
  so the interlinear plaintext is as likely the writer's own encipherment layout (plaintext written first, codes set under it)
  as a decipherment made on receipt. Audit 1's "contemporary interlinear decipherment" should read "contemporary interlinear
  plaintext". Either way the plaintext and its letter-by-group mapping are on the leaf in the period, so the body stays **N0**,
  key `period`.
- **Body N0: is the plaintext in print?** No print located (A2.1). That does not lower N0, which rests on the leaf itself.
- **L19 N2: is there a prior mapping or a print of the address-line groups?** The three Schonenberg theses, the abstract of the
  Hispania study, IA, Google Books, CrossRef, HAL, the NA record and both solver repositories show no transcription of the leaf's
  cipher groups. None of them names the recipient. Not reached: the Hispania full text (TLS) and one Google Books phrase query
  (503). **L19 stays N2**: the plaintext is the clear address on the same leaf, and no prior mapping of the 23 groups was located.
  The values come from the period key, and the identification of L19 with the address is `ours` (crib_align.py).
- **Leaf N0** stands.

### A2.3 Depth (rule 4a), recounted from reading_tokens.tsv

The standard (research/DECIPHERMENT-STANDARDS-2026-10-04.md item 2) counts cipher tokens *excluding nulls*. Four tokens carry
the NULL value: L10 pos0-2 (M) and the L14 pos3 blot (C). On the remaining **277**: **C 269, M 8, H 0, S 0 = 97.1% C**.
VER1-REG's 96.1% (270/281) included the nulls in the denominator. **Corrected to 97.1%.** Body L01-L14 non-null: C 242 / M 7.
L18-L19: C 27 / M 1.

The residue is 8 M tokens, every one valued: L04 pos19 45 n, L05 pos1 )3 t, L07 pos15 6) n, L08 pos15 26 e, L09 pos0 [L] a,
L10 pos12 2) r, L12 pos2 58 l, L19 pos9 ?9 n. These are uncertain letters inside read words at the native image's limit. None
is an unread name or code group. Unread tokens: 0 name/code, 0 other.

**Depth D3**, kept. More than 80% of tokens are C, and the external check is the period plaintext over L01-L14 and L18 (aligner
0.699 vs shuffled-gloss max 0.301, n=300). D3's "gaps mostly names/codes" is met in substance because nothing is unread; the 8
uncertain letters are not gaps. **Not D4**, because 8 cipher-letter tokens are M, not H/C/S. The fresh-session re-derivation was
done in Audit 1 section 2.

Outward words: "largely deciphered (about 97%)". The safe sentence governs: the text is on the leaf in a period hand.

Depth sentence (true, from the leaf's own plaintext): the letter tells Doña Antonia de Albanylla that, for greater security of
the correspondence, only a cover address in the form "A Doña Antonya de Albanylla" will be used.

`python3 tools/depth_check.py` (5 Oct 2026, after this audit): "unique solves (N3+ and D2+): 16 -- D4 1, D3 2, D2 13; not counted
D0/D1: 13; legacy ungraded: 0". This target has a status.json `targets` row and no `results` row, and it is N0, so the tool does
not count it. The depth fields are set on the targets row.

### A2.4 Classification (Audit 2)

| item | N-class | key source | text known | depth |
|---|---|---|---|---|
| A. Body L01-L14 | **N0** (confirmed) | period | known (in manuscript, on the leaf) | part of the leaf's D3 |
| B. L18 | **N0** (confirmed) | period | known (gloss "forma.") | part of the leaf's D3 |
| C. L19 | **N2** (confirmed) | period values; L19-to-address mapping ours | known (the clear address on the leaf) | 22 C / 1 M |
| Leaf | **N0** | period (body), ours (L19 alignment) | known | **D3, 97.1% C** (269/277 non-null) |

Below N3, so no SECOND-OPINIONS-QUEUE.tsv row is filed.

**Safe sentence:** "NA 1.02.04 invnr 63, a cipher minute from Schonenberg's chancery to Doña Antonia de Albanylla, carries its
own contemporary interlinear plaintext. We transcribed the leaf and rebuilt its 87-code table from that plaintext (grade C on
269 of 277 cipher tokens, about 97%). We also matched the unglossed address line to the clear address on the same leaf. No
printed edition or published transcription of the letter was located (search logs in AUDIT.md, 2 and 5 Oct 2026)."

**Unsafe sentence:** "We deciphered a previously unread Schonenberg cipher letter." The plaintext is on the leaf in a period
hand, and our work is the transcription, the code table and the L19 mapping.

### A2.5 Postmortem

No over-claim found in NOTES.md, HYPOTHESES.md, reading.txt or status.json.

Two corrections, recorded here without deleting earlier text:
- (a) The depth percentage is 97.1%, not 96.1%, because nulls are excluded from the denominator. Applied to status.json `depth_pct`.
- (b) "Interlinear decipherment" becomes "interlinear plaintext" in the safe sentence, because the leaf is a retained outgoing
  minute.

Audit 1's one open family (the Schonenberg studies) is now closed for the three Utrecht theses. Only the Hispania 2016 full
text remains unread. It is a person's-browser read for "Albanilla" or "cifra", and it cannot lower the body below N0.
