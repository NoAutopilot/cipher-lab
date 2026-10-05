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

## AUDIT 2 (DEF1-PIS, 5 Oct 2026) -- second adversarial audit of f.247r, f.275v, f.302v

Verifier DEF1-PIS (account 1, LANE DEFAULT-account-1-20261005-2039; brief .claude/briefs/runs/2026-10-05-account1-default-2039-jobs.md
"DEF1-PIS"). A fresh session: not a solver of any reading here and not VER1-PIS. Nothing decoded; no transcription, key or reading
touched. Clock by `date -u`: start 20:46 UTC, this section written 20:59 UTC.

### 0. Revisions since Audit 1
None. No NOTES.md section and no commit to the folder after VER1-PIS (git log: last folder commit before this one is 279a0920,
18:55 UTC, a Gallica manifest cache for another target). Readings, grade files and key are as Audit 1 audited them. No
SECOND-OPINIONS-QUEUE.tsv row exists for this target (class below N3), so there is nothing to propagate.

### 1. Re-checked from disk
Token counts recomputed from the grade files: f.247r C 236 / M 122 / U 7 of 365 (kp86g/grades_f247r.tsv); f.275v C 287 / M 444 /
U 15 of 746 (kp86h/grades_f275v.tsv); f.302v the file holds C 230 / M 143 / U 29 of 402 (kp87b/grades_f302v.tsv), 227 / 146 / 29
with the three T31 tokens held at M as HYPOTHESES.md and Audit 1 report. Audit 1's figures stand.

### 2. Independent search, aimed at f.302v (5 Oct 2026, 20:48-20:58 UTC)
The open question was whether the f.302v plaintext (24 Mar 1587: "Je suis le plus trompé homme du monde si l'on ne persuade au Pape
de s'entretenir avec Messieurs de Guise ... qu'eux seuls sont bastants pour faire l'entreprise d'Angleterre ... trop attaché à
approuver leur entreprise de Sedan ... qu'elle ne se fie de ce Prince sinon autant qu'elle en verra") is in print.
| family | what was searched (beyond Audit 1) | result |
|---|---|---|
| (a)/(c) documentary editions | **Desjardins, Négociations diplomatiques de la France avec la Toscane vol. IV** (IA gri_33125017127529, whole djvu text, accent-folded regex for trompé homme / bastan(t)s / fie de ce prince / entreprise de Sedan / entreprise d'Angleterre / Messieurs de Guise / Pisany); **Hübner, Sixte-Quint vol. 2** (IA sixtequint02hbne: djvu download 500, so be-api fts on the item for "trompé homme", "Pisany", "Sedan", "bastans"); Hübner 1882 edition vol. 1 (IA sixtequintdapre01hbgoog, whole text, same regexes); **L'Estoile, Journal de Henri III, 1744 ed. with Preuves** (Gallica bpt6k97695406, the only hit of a Gallica SRU exact-phrase search, then ContentSearch in the volume); Le Laboureur's 1731 Castelnau, Mémoires tome II (IA india.history.resource.100009) | Desjardins IV: none of the phrases; two Pisany mentions, both unrelated (the Navarre excommunication; a Florentine note on approaching the Pope through Pisani). Hübner 2: cites Pisany's dispatches ("Coll. Harlay 288") but none of the phrases. Hübner 1882: none. Journal de Henri III 1744: its "plus trompé homme du monde" (PAG_371) is a different sentence of 1588-89 ("Mais ou je suis le plus trompé homme du monde, ou le tems & les affaires vous enseignent maintenant"), not this dispatch; its Sedan pieces are Guise/La Châtre/Catherine papers, not Pisany. Castelnau 1731 t.II: OCR too poor to be a test (no Pisany at all): **logged as not a test** |
| (b) sender/recipient print | d'Ars 1884 re-read around 1587 (IA lepredemadamede00dargoog djvu text); Lettres de Henri III (SHF, vols 1959-2018; Google Books NO_PAGES, snippets only); Aubery 1654 relied on Audit 1's full-text 16-gram match (not re-run) | d'Ars pp.~216-217 paraphrases the Pope's mood in several 1587 audiences ("Pisany se voit forcé de l'adoucir en lui faisant observer qu'une rupture avec eux serait bien dangereuse"; footnote illegible in OCR; Google Books places "24 mars 1587" near it) -- a paraphrase of another passage, not the f.302v text. Lettres de Henri III: snippets show summaries of the King's letters to Pisani (15 Mar, 3 May [1587]; Sedan and Jametz) -- the King's side, not Pisany's dispatch text; volumes not readable here: **unreachable** |
| (e) full text | IA be-api fts, all items: "trompe homme du monde", "plus trompé homme du monde", "trompé homme du monde" Guise, "sont bastans pour faire", "bastants pour faire l", "approuver leur entreprise", "fie de ce Prince", "entretenir avec Messieurs de Guise" (one 503, not retried); Google Books API (key, country=US): 10 queries incl. "plus trompé homme du monde" Pape Guise, "bastans pour faire l'entreprise", "ne se fie de ce Prince", "s'entretenir avec Messieurs de Guise", "persuade au Pape" Guise Angleterre, "Pisany" "24 mars 1587" (one 503); Gallica SRU exact-phrase (text adj): three queries | IA: 61 hits for the trompé phrase, all other texts (Mazarin, d'Ossat, François de Sales, Dupuy correspondence, a 1835 Bulletin SHF piece on Mazarin, etc.); the three 16th-century-looking hits (bub_gb_dERgoHMqixkC "si S. S. n'aime & n'estime le Roi" = a d'Ossat-type sentence) do not carry the Guise clause. The other phrases: 0 or unrelated. Google Books: 0 exact hits; loose matches only (Hübner, L'Épinois, Revue critique 1886 review of L'Épinois citing the 24 Mar 1587 "querelles d'Allemagne" clear passage). Gallica: see row above |
| (g) scholarship | OpenAlex (Bearer key) "Vivonne Pisany Rome ambassadeur Henri III"; CORE (Bearer, v3/search/works/) "Pisany" AND Sixte-Quint/Sixtus V; HAL API "Pisany" OR "marquis de Pisani"; CrossRef bibliographic query; Semantic Scholar (x-api-key) | OpenAlex 1 (Pineau 2023, Henri IV and the papacy, not these dispatches); CORE 3 (BnF manuscript-record entries, not editions); HAL 0 relevant; CrossRef nothing on the dispatches; S2 2 unrelated |
| (f) solver repos, blogs | not re-cloned: Audit 1's grep of both repositories is from today (heads 3 Oct and 27 Sept 2026) | relied on Audit 1 |
| JSTOR | one family (ii) row appended (bare phrase "qu'elle ne se fie de ce Prince"); Audit 1's three rows (family i + two phrases) stand | queued; does not block |
| unreachable | Lettres de Henri III (SHF) page text; Anticona 2012-13 (Academia login wall, per CS-3); Hübner vol. 2 djvu download (500; fts route used instead); Castelnau 1731 OCR quality | logged |

Requests (5 Oct 2026, DEF1-PIS): be-api 14 (one 503); archive.org metadata/download 8 (one 500); Google Books 15 (two 503); Gallica
SRU 5 + ContentSearch 3; OpenAlex 2; CORE 1; HAL 1; CrossRef 1; Semantic Scholar 1. One request per host at a time, >= 1.5 s apart.

### 3. Classification per page (rule 10), key source, witness
| item | N-class | N0 holds on which witness | in print? | key | text |
|---|---|---|---|---|---|
| A f.247r (17 Sept 1586, second letter) | **N0 upheld** | the f.248r-v period "dechiffre" of this letter (manuscript, 1586) and the Colbert 16 pt II clear copy pp.54-55 (17th-c. manuscript) | about a third: one sentence in Aubery 1654 p.46 (Audit 1; not contradicted here) | published (Tomokiyo, credited) | known |
| B f.275v (4 Nov 1586) | **N0 upheld** | the leaf's own period decipherment (head of page and margin) and Colbert pp.122-123; also print | yes, whole: Aubery 1654 pp.51-52 (Audit 1) | published (Tomokiyo) | known |
| C f.302v (24 Mar 1587) | **N0 upheld** | the leaf's own 19-line margin decipherment (period) and Colbert pp.341-342 (manuscript). N0 rests on these manuscripts alone | **not located in print** after Audit 1's and this audit's searches (Aubery 1654, L'Épinois, Hübner 1-3 and 1882, Desjardins IV, d'Ars, Catherine 8-10, Journal de Henri III 1744, IA/Google Books/Gallica phrase searches); Lettres de Henri III (SHF) and Anticona unread | published (Tomokiyo) | known (in manuscript: the leaf's own decipherment and the Colbert copy) |
The answer to the brief's question: f.302v's plaintext was not located in any printed edition searched; it exists in the leaf's
own margin decipherment and the Colbert 16 pt II copy, both manuscript. That does not change the class: a period decipherment of
this very item exists, so N0 holds whether or not it was ever printed. Confidence high for all three.

### 3a. Depth (rule 4a) -- D1 confirmed on all three
| item | % H/C/S tokens | unread | depth | check |
|---|---|---|---|---|
| A f.247r | 64.7 (C 236/365) | M 122, U 7: mostly ordinary letters, not names/codes | **D1** | longest firm run 17 letters, below the authentication distance; no code value read in two contexts; firm share < 80% |
| B f.275v | 38.5 (C 287/746) | M 444, U 15 (L17-L20 all M) | **D1** | longest firm run 15 letters; as above |
| C f.302v | 56.5 (C 227/402, T31 held) | M 146, U 29 | **D1** | longest firm run 13 letters; as above |
The C grades are licensed by an aggregate known-answer alignment against the period text, with controls on file (Audit 1, 3a);
they are scattered letters, not a clause of our own reading, so D2 is not reached. No D2 content sentence is required.

### 4. Postmortem
- No over-claim found in the folder; the solvers' wording ("a known-answer confirmation of the published table ..., not a
  decipherment") and Audit 1's safe sentences stand unchanged.
- Audit 1 named Hübner vol. 2 as "not on IA (404)"; it is on IA as sixtequint02hbne (the 404 was on hubner-sixte-quint-t-2).
  Searched here through be-api: no phrase hit. Correction of fact only; Audit 1's conclusion does not change.
- PROGRESS.tsv data rows 42-44 (file lines 49-51; "Pisany 17 Sept 1586 f.247r", "... 4 Nov 1586 f.275v", "... 24 Mar 1587
  f.302v"): column `2` = x, `C` stays '.' (N0 never counts).
- No SECOND-OPINIONS-QUEUE.tsv row: class below N3.

### 5. Safe and unsafe sentences
Audit 1's sentences stand. For f.302v the safe sentence is sharpened to: "Tomokiyo's published table reads the f.302v cipher (24 Mar
1587) at letter level against the leaf's own period margin decipherment and the Colbert 16 pt II copy (known-answer PASS, about 56%
of tokens confirmed; D1); the plaintext is known from those two manuscripts and was not located in print in the editions and
full-text indexes searched on 5 Oct 2026 (two audits)." Unsafe: "an unpublished passage", "read for the first time", or any
wording implying the text was unknown before this project.

Depth check pasted (python3 tools/depth_check.py, 5 Oct 2026, DEF1-PIS): exit 0; last line "unique solves (N3+ and D2+): 16 -- D4 1, D3 2, D2 13; not counted D0/D1: 13; legacy ungraded: 0" (the three rows stay N0 / D1, not counted; status.json results[117-119] audit_status 'two audits'). tools/verify_backlog.py regenerated: "38 rows: audit2 8, both 4, counted 26".
