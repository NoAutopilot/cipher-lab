# AUDIT -- fr16045-pisany-rome-1585

## AUDIT 1 (VER1-PIS, 5 Oct 2026) -- three known-answer pages: f.247r, f.275v, f.302v

Verifier session VER1-PIS (LANE-VER1, account 2), brief .claude/briefs/runs/2026-10-05-ytbiz-ver1-jobs.md "VER1-PIS".
A fresh session, not the solver of any reading here; nothing decoded, no transcription or key touched. Clock read by
`date -u` at start (18:17 UTC) and before every dated line.

### Claim under audit
The repository says (NOTES.md, PIS1-247 / PIS1-275V / RUN6-PIS / RUN6-PISFIN / PIS1-302, 4-5 Oct 2026): Tomokiyo's published
1586-87 table (key86.tsv) passes a known-answer test on three more pages of Jean de Vivonne, marquis de Pisany, to Henri III
from Rome, scored against the clear copy in BnF Mélanges de Colbert 16 part II; "a known-answer confirmation of the published
table ..., not a decipherment; no claim of a new reading." This audit checks that wording and classes each page.

### 1. Extract (per item)
| item | leaf (Gallica btv1b9060906j) | date, sender -> recipient, place | plaintext as the repo has it | period decipherment on/near the leaf | clear copy | solver's search |
|---|---|---|---|---|---|---|
| A | fr.16045 f.247r (c506), 9 cipher lines, 365 tokens (tx86g) | 17 Sept 1586 (second letter of that day), Pisany -> Henri III, Rome | "licence a Sa Saincteté de me le donner par escrit ... J'ay les mains liées de ce costé, de peur d'alterer rien ... par le moyen du Cardinal de Saincte Croix" (kp86g/colbert_f247r.txt) | yes: f.248r-v "dechiffre" of the letter; its f.248v lines 10-20 run the f.247r passage (kp86g/dechiffre_f248.txt) | Colbert 16 pt II pp.54-55 (btv1b100341061 c446) | CS-3/PIS-M (4 Oct): d'Ars 1884, Catherine de Médicis 8-10, web/blog, solver repos, IA be-api |
| B | fr.16045 f.275v (c563), 20 cipher lines in two blocks, 746 sign tokens (tx86h) | 4 Nov 1586, Pisany -> Henri III, Rome | "ne le me communiquer a moy; de peur que le faisant entendre a V. M. par lettres ... envoyé vers elle pour assister, deffendre, et recommander ... ladite Royne d'Escosse ... elle s'y efforceroit tant plus volontiers" (kp86i/colbert_f275v.txt) | yes: second hand, 4 lines at the head of the page (decipherment of block A) and a long left-margin decipherment beside block B | Colbert pp.122-123 (c480) | as A |
| C | fr.16045 f.302v (c617), 11 cipher lines, 402 sign tokens (tx87b) | 24 Mar 1587, Pisany -> Henri III, Rome | "Je suis le plus trompé homme du monde si l'on ne persuade au Pape de s'entretenir avec Messieurs de Guise ... leur entreprise de Sedan ... si je ne l'en advisois" (kp87b/colbert_p341_342.txt) | yes: second hand, 19-line left-margin decipherment (kp87b/gloss_f302v.txt; gloss vs copy nw 0.944) | Colbert pp.341-342 (c589-c590) | as A |

Verifier's own image check (5 Oct 2026, 18:2x UTC; Gallica c509, c563, c617 at 1000 px, 3 requests, all 200): the period
decipherments are on the leaves as the solvers describe. f.275v: four lines in a smaller hand above block A ("... me le
communiquer a moy de peur que le faisant entendre a V. Ma.te par lettres ...") and a decipherment column in the left margin
the full height of block B, plus small interlinear letters; f.302v: a 19-line marginal column opening "Je suis le plus trompé
homme du monde si l'on ne persuade au Pape ..."; f.248v: a faint full page in a clear hand ending "... Cardinal S.te Croix.
Nous sommes prestz d'aller a l'audiance ...", the passage the f.247r cipher carries.

### 2. Independent search (5 Oct 2026, 18:19-18:40 UTC)
Phrases searched (ciphers/fr16045-pisany-rome-1585/phrases.txt, eight, from the Colbert copy and the leaves' glosses) plus
names/date keyword queries. `tools/print_check.py` -> print-check.tsv / print-check-hosts.tsv (72 rows).
| family | what was searched | result |
|---|---|---|
| (a) canonical series | Lettres de Catherine de Médicis 8-10 (IA lettresdecatheri08/09/10cathuoft, phrases via be-api); Hauser, *Sources de l'histoire de France XVIe s.* (Google Books snippet only, NO_PAGES) | no phrase hit; Hauser lists Pisany's Rome embassy, entry not readable |
| (b) sender/recipient-specific print | d'Ars 1884 (IA lepredemadamede00dargoog, phrases); **Antoine Aubery, *L'histoire du cardinal duc de Joyeuse ... plusieurs memoires, lettres, dépesches ... non encore imprimées* (Paris 1654), IA bub_gb_Vw5mDnRMjIcC, whole djvu text and hOCR, normalised 16-gram match against the three passages** -- found via Hübner's footnotes (below); Lettres de Henri III (SHF, 2012 vol.) surfaced by Google Books on a loose match only | **Aubery: f.275v passage printed whole; one f.247r sentence printed; f.302v passage not found** (details below). d'Ars: no hit. |
| (c) documentary/narrative editions of the period | Hübner, *Sixte-Quint* (1870) vols 1 and 3 (IA sixtequint01hbne, sixtequint03hbne; vol.2 not on IA, 404 on hubner-sixte-quint-t-2); L'Épinois, *La Ligue et les papes* (1886, IA laligueetlespap00lepgoog); Chéruel, *Marie Stuart et Catherine de Médicis* (1858, IA mariestuartetca02chgoog) | Hübner vol.1 cites Pisany to Henri III 17 Sept 1586, 4 Nov 1586 and 24 Mar 1587 ("Coll. Harlay 288") and says of the last two "extrait/une partie ... publiée dans la Vie du cardinal de Joyeuse, Paris 1654"; his own quotations are other passages (no 16-gram cluster with any of the three). L'Épinois cites the 24 Mar 1587 dispatch at fr.16045 ff.297, 298, 301 (clear parts: "querelles d'Allemagne", "le Pape me loua l'entreprise de Sedan"), not the f.302v cipher passage. Chéruel: no cluster. |
| (d) holding archive / project pages | BnF catalogue of Colbert 16 pt II (cc954664, read by CS-3, 4 Oct); Gallica leaves c509, c563, c617 viewed by this verifier; de Witte, "Notes sur les ambassadeurs de France à Rome et leurs correspondances sous les derniers Valois (1556-1589)", MEFR 83 (1971) pp.89-121 (Persée, search snippets only: lists manuscript copies incl. Colbert and Dupuy 29 for Vivonne; the PDF answered 403, not retried) | the survey treats the dispatches as manuscript copies; no edition of the 1586-87 dispatches named in the snippets read |
| (e) full text IA / HathiTrust / Google Books | IA be-api fts, all items, eight phrases (16 requests); IA advancedsearch for the editions above; Google Books API with key and country=US, eight phrases + 5 title/keyword queries | Google Books "phrase" queries return loose matches (Mercure 1703, Bayle, d'Aubigné, etc.): none carries the passages; Anticona title query 0. HathiTrust EF not used (the IA copies were full text). |
| (f) solver repositories, blogs | shallow clones of dbourdeau/cyphersolver (head 3 Oct 2026) and aaymeloglu/unsolved-ciphers (head 27 Sept 2026), grep pisany/pisani/vivonne/16045/saint-gouard | Bourdeau: Pisany only as recipient in the 1593 Nevers target and Tomokiyo mirrors; no fr.16045 target or reading. Aymeloglu: no hit. Cryptiana henryiii page (sources/) is the key's source (Tomokiyo), reports Anticona 2012-13 p.105 for 17 Sept 1586 f.244 |
| (g) scholarship | OpenAlex (Bearer key, 10 requests), CrossRef (4), Semantic Scholar (3 keyword queries by hand: 0 relevant; print_check's phrase query hit 429 once, not retried), HAL API (4 queries: 0 relevant), Persée search (5 queries) | nothing on these pages beyond de Witte 1971 |
| JSTOR | three rows appended to JSTOR-QUEUE.tsv (5 Oct 2026): family (i) names+years+cipher keyword; family (ii) bare phrases "le plus trompé homme du monde", "leur entreprise de Sedan" | queued; does not block the class |
| unreachable | Anticona 2012-13 mémoire (Academia.edu login wall, CS-3 4 Oct; not retried); Hübner vol.2 on IA (404); Persée PDF of de Witte (403); Hauser (Google Books NO_PAGES) | logged |

**Aubery 1654, what it prints (IA bub_gb_Vw5mDnRMjIcC; page numbers from the item's page_numbers.json, cross-checked against
the running heads).** The "Memoires pour l'histoire du cardinal de Joyeuse" section prints extracts of Pisany's dispatches,
each headed "Au Roy" with a marginal date, in clear (quotations below are from the OCR with long s, u/v and accents normalised by this verifier):
- **f.275v (4 Nov 1586): printed whole, pp.51-52.** "... desirant que cela fust si secret, qu'il ne l'avoit pas seulement voulu
  écrire à son Nonce, ne me le communiquer à moy, de peur que le faisant entendre à V. M. par lettres elles ne fussent veues de
  personne qui découvrist cét affaire ... le soupçon perpetuel où je suis que je ne la sers qu'à demy, combien que j'employasse
  & misse cent fois l'heure ma vie en hazard pour son service ... à laquelle elle porte toute affection, amour & bienveillance,
  qu'encore entendant V. M. que Sa Sainteté en recevroit plaisir, elle s'y efforceroit tant plus volontiers." Every clause of
  kp86i/colbert_f275v.txt is there in order (384 shared 16-grams in one cluster after normalisation); "sers" where Colbert reads
  "sors". The plaintext of both f.275v cipher blocks has been in print since 1654.
- **f.247r (17 Sept 1586, second letter): one sentence printed, p.46.** "J'ay les mains liées de ce costé, de peur d'alterer rien,
  & d'en communiquer avec Monsieur le Cardinal d'Est, qui est tres-resolu d'envoyer un courrier exprès pour donner à V. M. les
  advis qu'il a." Aubery's extract is abridged and joined to a Geneva paragraph; the rest of the f.247r span ("licence a Sa
  Saincteté de me le donner par escrit ... Et ainsy nous nous sommes separez"; "que ie crois aussy n'estre a mespriser ... par le
  moyen du Cardinal de Saincte Croix") was not found in Aubery. About a third of the f.247r plaintext is in print.
- **f.302v (24 Mar 1587): not found in Aubery.** Aubery prints clear paragraphs of a later dispatch (pp.56-57; its date not legible in the OCR read; L'Épinois places the Sedan remark in the 24 Mar 1587 dispatch, f.298: "Le Pape me
  dit que si V. M. eust permis à Monsieur de Guyse de prendre Sedan ...", "Nous avons obtenu l'Indult ...") but no form of
  "Je suis le plus trompé homme du monde si l'on ne persuade au Pape ...", "bastans", "ne se fie de ce Prince"; normalised
  16-gram match: no cluster above 8 grams, all generic. Not found in L'Épinois, Hübner 1 and 3, d'Ars, Catherine 8-10 or by the
  phrase searches either. Its plaintext is known from the leaf's own margin decipherment and the Colbert copy, both manuscript.

### 3. Classification (rule 10) and key source
| item | N-class | prior plaintext | prior decipherment | key | text | evidence, confidence |
|---|---|---|---|---|---|---|
| A f.247r | **N0** | yes: f.248r-v period decipherment (manuscript, 1586); Colbert 16 pt II pp.54-55 (17th-c. copy); one sentence printed, Aubery 1654 p.46 | yes: the f.248r-v "dechiffre", and the clear copy | published (Tomokiyo's 1586-87 table, credited; key86.tsv) | known | leaf viewed; Aubery read in full text; high |
| B f.275v | **N0** | yes: printed whole, Aubery 1654 pp.51-52; Colbert pp.122-123; head-of-page and margin decipherment on the leaf | yes: the leaf's own period decipherment; the printed 1654 text is the deciphered passage | published (Tomokiyo) | known | leaf viewed; Aubery text matched clause by clause; high |
| C f.302v | **N0** | yes, in manuscript: the leaf's 19-line margin decipherment and Colbert pp.341-342; not located in print (Aubery, L'Épinois, Hübner 1/3, d'Ars, Catherine 8-10, phrase searches, 5 Oct 2026) | yes: the margin decipherment on the leaf | published (Tomokiyo) | known | leaf viewed; high for N0 (the decipherment of this very item exists from the period) |

N0 on all three rests on the period decipherment of each passage (on or beside the leaf) and the key's being Tomokiyo's
published table; the print found here (Aubery 1654) adds a printed witness for B and part of A. Nothing here is an independent
re-decipherment of an unknown text: the solvers' own wording ("a known-answer confirmation of the published table ..., not a
decipherment; no claim of a new reading") is correct and stands.

### 3a. Depth (rule 4a)
| item | sign tokens | C / M / U (rule-4 grades file) | firm % | longest C run | depth | check |
|---|---|---|---|---|---|---|
| A f.247r | 365 | 236 / 122 / 7 (kp86g/grades_f247r.tsv) | 64.7 | 17 letters | **D1** | known-answer PASS kp86g (0.639 vs key-shuffle p99 0.431 / order p99 0.494, control 5/5 at e 0.268) |
| B f.275v | 746 | 287 / 444 / 15 (kp86h/grades_f275v.tsv; L17-L20 all M after kp86h/kp86i local FAIL) | 38.5 | 15 letters | **D1** | full page PASS kp86h (0.514 vs 0.391 / 0.469, control 5/5 at e 0.190); L17-L20 FAIL twice |
| C f.302v | 402 | 227 / 146 / 29 (kp87b/grades_f302v.tsv holds the script's 230 / 143; the 3 T31 tokens held at M per HYPOTHESES.md, as NOTES.md reports) | 56.5 | 13 letters | **D1** | known-answer PASS kp87b (0.590 vs 0.389 / 0.464, control 5/5 at e 0.335) |
D1, "fragments read", on all three: the firm (C) tokens are letters scattered between M tokens, the longest unbroken firm
stretch is 13-17 letters, and for a 73-cell homophonic table at two-reader transcription error 0.18-0.34 the authentication
distance is of the order of 10^2 letters before liberties; no firm stretch comes near it, and no code value is read in two
contexts. The PASS is an aggregate alignment test of the published table against a known text (rule 3 control on file), which
licenses the C grades but not a clause-level reading of our own. Not D3: firm share 38-65%, far below 80%. Judge (rule 7) FAILs
on all three (-1.271, -1.215, -1.405, as NOTES.md records; letter-for-letter output with many M tokens), not a gate here.
No D2 content sentence is required; for orientation only, from the period texts (not our reading): on f.275v Pisany reports
that he learnt, without anything in writing, that Sixtus V had secretly charged the duc de Luxembourg to ask Henri III to act
for the safety of Mary Queen of Scots, and that he then told the Pope the King had already sent to defend her.

Depth check pasted (python3 tools/depth_check.py, 5 Oct 2026): exit 0; last line "unique solves (N3+ and D2+): 16 -- D4 1, D3 2, D2 13; not counted D0/D1: 13; legacy ungraded: 0" (the three rows added here are N0 / D1, not counted, so they add three to "not counted D0/D1" and fail nothing).

### 4. Postmortem
- No over-claim found in the folder: every section calls these pages a known-answer confirmation of a published key against a
  period copy, "not a decipherment", and no file uses novelty wording.
- Gap in the solvers' print search (not an over-claim): the CS-3 premise check (4 Oct) concluded "no printed edition of
  Pisany's Rome dispatches found" from d'Ars and Catherine de Médicis 8-10; Aubery's 1654 *Histoire du cardinal de Joyeuse*
  prints extracts of these very dispatches, including the whole f.275v cipher passage, and Hübner (1870) says so in his
  footnotes. NOTES.md Findings item 3 is corrected by a dated note (VER1-PIS, 5 Oct 2026) rather than rewritten. Any later
  page of these letters (f.276r-f.279r of 4 Nov 1586, f.246r-v of 17 Sept 1586, the 9 Sept 1586 letter, 1587-88 letters) should
  be checked against Aubery's Mémoires (pp.40-60 and following) before work on it is described.
- PROGRESS.tsv: three rows added (one per leaf), `1` = x, `2` = '.', `C` = '.' (N0 never counts).
- No SECOND-OPINIONS-QUEUE.tsv row: the class is below N3.

### 5. Safe and unsafe sentences
| item | safe sentence | unsafe sentence |
|---|---|---|
| A f.247r | "Tomokiyo's published 1586-87 table reads the f.247r cipher of Pisany's second letter of 17 Sept 1586 at letter level against the period decipherment on f.248v and the Colbert copy (known-answer PASS, about 65% of tokens confirmed; fragments read, D1); the text is known from those period sources and one sentence of it was printed by Aubery in 1654." | "We deciphered Pisany's letter of 17 Sept 1586." / any "first", "unpublished" or "previously unread" |
| B f.275v | "Tomokiyo's published table reads the f.275v cipher (4 Nov 1586) at letter level against the leaf's own period decipherment and the Colbert copy (known-answer PASS on the page, about 39% of tokens confirmed; D1); the passage has been in print since Aubery's *Histoire du cardinal de Joyeuse* (1654), pp.51-52." | "A hidden passage about Mary Queen of Scots recovered from cipher." |
| C f.302v | "Tomokiyo's published table reads the f.302v cipher (24 Mar 1587) at letter level against the leaf's own margin decipherment and the Colbert copy (known-answer PASS, about 56% of tokens confirmed; D1); the text is known from those period manuscripts; it was not located in print in the editions searched on 5 Oct 2026." | "An unpublished passage of Pisany's dispatch read for the first time." |

Requests (5 Oct 2026): Gallica 3; archive.org 3 + 12 downloads/metadata (Hübner 1-3, L'Épinois, Chéruel, Aubery djvu, hOCR,
page numbers, metadata, advancedsearch 6); be-api 16; Google Books 13; OpenAlex 10; CrossRef 4; Semantic Scholar 4 (one 429);
HAL 4; Persée 7 (one 403); GitHub 2 shallow clones. One request per host at a time, >= 1.5 s apart.
