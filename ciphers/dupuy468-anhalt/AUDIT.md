# AUDIT: the Dupuy 468 f.28 reading (novelty class)

Verifier session, 23 September 2026, 21:34-22:10 UTC (Opus, no subagents). Audits NOTES.md, reading.txt,
key.tsv, key_from_gloss.tsv, runs.tsv and check.py as of commit 1820fe5, and the sentences about them in
status.json, LEDGER.md and ROOM.md. This session did not take part in the transcription or the solving. It did no
decoding and does not protect the solver's conclusions. Classes are those of CLAUDE.md rule 10.

> **Superseded, 23 September 2026:** the second, adversarial audit at the end of this file found the letter printed
> (French translation) in Deutsche Reichstagsakten, Jüngere Reihe II (1896), p. 122, dated [1520] Jan. 24. The class is
> **N1**. Sections 1-9 are kept as the first audit's record. Their N3, their safe sentence and their 1518/19 date no longer hold.

## 1. Verdict

| item | prior plaintext | prior decipherment of this item | class |
|---|---|---|---|
| BnF Dupuy 468 f.28r-v (subscription on the next leaf, canvas 65), Latin letter to Francis I, 687 cipher tokens | **not located.** No printed text, extract or summary of this letter was found in the editions of section 4. Its subject is in print: Kluckhohn (Deutsche Reichstagsakten, Jüngere Reihe I, 1893, Einleitung pp. 55-57) summarises a plan, reported by Joachim von Moltzan, for a "hartes Verbündnis" of Saxony, Brandenburg, Lüneburg and neighbouring princes, Mecklenburg and Pomerania among them. | **yes, on the document.** 659 of the 687 cipher tokens have an interlinear decipherment above them. It is written by a second hand after the main text, and is most probably the French chancery's decipherment made on receipt (section 5). It is not mentioned in Dorez (1899) or the BnF notice, and it has not been found in print. | **N3** |

**Class N3**: no printed plaintext or printed decipherment was found after the logged search. It is not N4.
JSTOR, Google Books full text, HathiTrust full text, Reichstagsakten JR II, Mignet vol. II, Potter's 1515 and 1517
inventories and the Paris and Wolfenbüttel archive catalogues were not reached (section 4). Rule 10 does not
put the letter at N0, because the decipherment that exists is a manuscript gloss that nobody has printed or
described. But the answer to "did we first-decipher?" is **no.** The letter was deciphered about five hundred years
ago on the leaf itself. The solver's H 630 tokens are a transcription of that decipherment. Only the S 33 tokens,
which the gloss skipped, were read with a key the solver took from the gloss. So even at N4 or N5, wording such as "first
decipherment", "previously unread" or "newly recovered" would be false here. The most that can be said is
"no prior printed decipherment located".

**Sender and date: the catalogue's attribution is probably wrong** (the verifier's inference, grade I, for a
historian to confirm; section 3). The letter is most probably from **Ernest of Brunswick-Lüneburg** (later "the
Confessor", 1497-1546, son of Duke Henry the Middle) **and Joachim von Moltzan (Maltzan)**, Francis I's German
agent. It was not written by Ernest of Anhalt and "Joachim his brother". It most probably dates from the 1518-19
campaign for the imperial election. "Vigil of St Paul" then means 28 June 1518 or 24 January 1519, not 1515/16.

**Safe sentence.** "BnF Dupuy 468 f.28 is a Latin cipher letter to Francis I. The catalogue gives it to Ernest and
Joachim of Anhalt, 1515/16. It is more probably from Ernest of Brunswick-Lüneburg and Joachim von Moltzan, 1518/19.
It carries an interlinear decipherment in a second hand, probably contemporary. That decipherment was transcribed,
and the key it implies was applied to the whole letter. Together they read 663 of the 687 cipher tokens (H 630
from the gloss, S 33 from the key, control 99.8%); 18 are M and 6 unread. No printed text or printed decipherment
of the letter was found in the editions listed in AUDIT.md (N3)."

**Unsafe sentences.** "The Anhalt cipher letter deciphered for the first time"; "a previously unread letter to
Francis I"; "read in full by cryptanalysis"; "the princes of Anhalt proposed a league" (as established fact);
"a new source for the 1519 election" (it may be new to print, but nobody has searched the archives, and it was
read in 1518/19).

## 2. What the repo claims (extracted)

| field | value in the repo | source of the value |
|---|---|---|
| shelfmark | BnF Dupuy 468 f.28 (Gallica ark:/12148/btv1b10035959t, canvases 63 recto, 64 verso, 65 subscription) | NOTES.md, images/manifest.json |
| sender, recipient | "Ernest, [prince d'Anhalt-Zerbst-Dessau], et Joachim, son frère" to Francis I | finding aid = Dorez, Catalogue de la collection Dupuy I (1899) p.440, no. 468, verbatim; the bracket is the cataloguer's |
| date, place | "s. l., veille de la saint Paul, s. d. [1515 ou 1516]"; place in the text "opidum Cerbess" (Zerbst) | Dorez; reading.txt r02-r03 |
| cipher | simple substitution, 21 letter signs, word signs K = christianissimus, F = marchio, theta = Luneburg, PW = Mekleburg (SX = Saxonie, uncertain), nulls g and o | key.tsv |
| plaintext | reading.txt (49 rows, regenerated by check.py). Distinctive phrases: "ut primo de christianissimo nulla fiat mencio"; "inter Germanie principes attrahi possunt"; "nisi maiore parte confederatorum consentiente"; "palatinus tractari"; "a christianissimo pensionem"; "maiorem ligam et confederacionem in fauorem christianissimi ... in tota Germania"; clear text "quas ego Joachimus ad dominum Cancellarium et dominum admiraldum scripsi"; opening "Post humilimam atque humilimam commendationem" | reading.txt, NOTES.md |
| grades | H 630, S 33, M 18, unread 6; 242 clear words ungraded; no C | check.py, reading_tokens.tsv |
| gloss hand | "a lighter, later-looking humanist cursive in grey ink"; not compared with Godefroy's notes at ff.8-9; "not identified" | NOTES.md "The gloss hand" |
| solver's search | cyphersolver (head 763a3b9) and unsolved-ciphers (head 2495c45) grepped for anhalt, Dupuy 468, btv1b10035959t, zerbst, cerbes and the finding-aid phrases; one WebSearch on "nisi maiore parte confederatorum consentiente"; Beckmann, Champollion-Figeac, the editions of Francis I's German diplomacy, Gallica full text, HathiTrust and Google Books **not searched** (stated honestly) | NOTES.md "Where it was not found" |
| check-solved's search | 2 WebSearches; cryptiana, DECODE cache, both solver catalogues grepped for "anhalt"; Beckmann not located | NOTES.md "Check-solved sweep" |

## 3. The attribution and the date (why "Anhalt, 1515/16" is doubtful)

The evidence below comes from the plaintext as read and from printed sources. It is the verifier's inference (grade I).

1. **The subscription is "Ernestus dux etc. / Joachimus etc."** (canvas 65, viewed at 700 px). The Anhalt princes
   styled themselves Fürst / princeps, not dux. Ernest of Anhalt-Dessau (d. 2 July 1516) had no brother Joachim
   who could have written this. His son Joachim was born in 1509.
2. **The text says "EGO FILIUS [dux] <LUNEBURG> tractatum cum patre meo"**: one writer is the son of the Duke of
   Lüneburg. The gloss at r04:25-26 reads "dux de lune[burg]". Ernest, son of Henry the Middle of Lüneburg, was at
   Francis I's court from 1518 (NDB, "Ernst der Bekenner"; Lisch V p.26f. quoting Heimbürger 1839 and Chytraeus:
   "Henricus dux Lunaeburg. in Francisci Galliae regis amicitiam, in cuius aulam filium Ernestum aliquanto ante
   miserat"). He travelled with Moltzan after Easter 1518 (RTA JR I p.57 n.: "Kurz nach Ostern war Moltzan zusammen
   mit Herzog Ernst von Celle aufgebrochen").
3. **"EGO IOCHIN" and "quas ego Joachimus ad dominum Cancellarium et dominum admiraldum scripsi"**: Joachim von
   Moltzan corresponded with Chancellor Duprat and Admiral Bonnivet in 1518-19 (Lisch V pp.326-344; Potter's
   1519 inventory nos. 18, 55, 80, 96, 130, 175).
4. **The opening formula matches Moltzan's own letter** of 12 March 1519 to Francis I (Dupuy 264, printed by
   Le Glay, Négociations II p.329). That letter opens "Invictissime, potentissime ac cristianissime rex ac domine
   clementissime. Post humilimam atque humilimam commendacionem". f.28 opens "Amicissime potentissime ac
   christianissime rex ac domine domine observandissime. Post humilimam atque humilimam commendationem". Both
   use "totis viribus" and "admiraldo/admiraldum".
5. **The content fits 1518-19.** Moltzan reported Duke Henry's plan for a hard alliance of Saxony, Brandenburg,
   Lüneburg, Mecklenburg and others (RTA JR I pp.55-57). Duke Henry proposed meeting Elector Frederick "in
   Zerbst oder Allstädt" in February 1519 (Weicker 1901, section on February 1519). Francis promised pensions
   to "quelques ducz de la basse Allemaigne" through Brandenburg or Lüneburg (Potter 1519).

So the letter is most probably from Ernest of Lüneburg and Joachim von Moltzan. "In vigilia sancti Pauli" is
most probably 28 June 1518 (the vigil of Peter and Paul) or 24 January 1519 (the vigil of the Conversion).
A historian should settle it. The letter's own mention of "Saxonie <Marchio> <Luneburg> ambo <Mekleburg>" at
Zerbst is the best anchor. This matters for novelty, because the sender-specific editions to search are those of Moltzan
and Lüneburg, not Anhalt.

## 4. Search log (23 September 2026)

| family | searched | result |
|---|---|---|
| (a) Beckmann, Historie des Fürstenthums Anhalt (1710-16) | IA 11054796bsb, 11054797bsb, 11054798bsb (3 volumes, djvu text) grepped for Franciscus/Franz/Franckreich with 1515-19, Ernst with 1516, Zerbst with 1515-19 | no mention of a letter or dealings with Francis I; Fraktur OCR is poor (long s), so conditional. The Urkunden part was not identified separately |
| (a) Codex diplomaticus Anhaltinus | not searched | stops at 1400 (von Heinemann, 6 vols); cannot contain a 1515-19 letter |
| (a) Deutsche Reichstagsakten, Jüngere Reihe I (Kluckhohn 1893) | IA bub_gb_0gFoAAAAMAAJ, full djvu text; grep for Dupuy, Zerbst variants, Cerbes, the Latin phrases (confederatorum, attrahi, acceptaretur, nulla fiat men[c]io, admiraldum, humilimam, vri prudenti), Ernestus, Anhalt, chiffr | letter not printed or cited. Only Dupuy 263 is cited (via Le Glay). The Einleitung summarises Moltzan's alliance plan and the chancery's deciphering of his Latin cipher letters (see section 5). Control: the phrase "christianissimus rex" and "Moltzan" are found, so the OCR is searchable |
| (a) Deutsche Reichstagsakten, Jüngere Reihe II (1896, Worms 1521) | not searched | relevant only if the letter is of 1520-21; suggested |
| (a) Lisch, Joachim Maltzan (Urkunden-Sammlung Maltzan V, 1853) | IA bub_gb_uRA6AAAAcAAJ (and bub_gb_Y5NAAAAAcAAJ, same text) full djvu text; grep for Zerbst variants, Cerbes, vigilia Pauli, confoederat-, Ernestus, Anhalt, pension, admiral | letter not printed. Lisch prints letters **to** Moltzan (Wolfenbüttel, Schwerin), not his letters to the King in Paris |
| (a) Le Glay, Négociations diplomatiques entre la France et l'Autriche I-II (1845) | IA negociationsdipl01legluoft, negociationsdipl02legluoft; grep Zerbst, Cerbes, confederator-, humilimam, Dupuy, Ernestus, Moltzan | not printed. II p.329 prints Moltzan to Francis I, 12 Mar 1519 (Dupuy 264), the formula comparison of section 3; the table has Moltzan only at II 329 |
| (a) Mignet, Rivalité de François Ier et de Charles-Quint I (1886) | IA rivalitdefranois01mign; grep Dupuy, 468, Zerbst, Lunebourg, Moltzan | not cited; cites Dupuy 263, 264, 486, 745 for Moltzan. p.161-162 n.4: "L'original avec le déchiffrement des mots chiffrés écrit dessus. Mss. Dupuy, vol. 263" (same practice as f.28). Vol. II and the 1854 Revue des deux Mondes articles not searched |
| (a) Weicker, Die Stellung der Kurfürsten zur Wahl Karls V. (1901) | IA bub_gb_RncRAAAAYAAJ; grep Dupuy, Zerbst, Anhalt, Ernst, Chiffr | not cited; gives Zerbst as a proposed Lüneburg-Saxony meeting place, Feb 1519 |
| (a) Hasenclever, Die kurpfälzische Politik ... Ottheinrichs | not searched | it covers the 1550s, not 1515-19; not relevant |
| (a) Bauer (named in the brief) | not identified, not searched | a session should name the work |
| (a) Journal de Jean Barrillon, secrétaire de Duprat II (1897) | IA journaldejeanbar02barruoft; grep Zerbst, Cerbes, confederator-, Ernestus, Lunebourg, Moltzan | Moltzan's mission described; letter not printed ("confederatorum" hits are treaty texts) |
| (a) Catalogue des actes de François Ier I (1887) | IA collectiondesord01acad; grep Zerbst, Lunebourg, Moltzan, Ernest, Dupuy 468 | no hit (it catalogues the King's acts, not letters received) |
| (a)(b) Potter, Inventaire des lettres missives de François Ier, 1516, 1518, 1519 (cour-de-france.fr PDFs) | cour-de-france.fr refused (403, Cloudflare challenge, stopped); the 1516, 1518 and 1519 PDFs fetched from Wayback captures of 20 Jan 2025, text extracted, grep Anhalt, Lunebourg, Zerbst, Mecklenburg, Moltzan, Ernest, Dupuy 468, chiffr | outgoing letters only; no reply to or mention of f.28. 1519 no. 21 cites Dupuy 468 fo.49-51 (Suffolk instructions), not f.28. Evidence on deciphering practice in section 5. The index of recipients could not be fetched (web.archive.org SSL errors twice) |
| (b) Ernest of Lüneburg | Heimbürger, Ernst der Bekenner (1839) IA ernstderbekenner00heim; Wrede (1888) IA ernstderbekenne00wredgoog; grep Dupuy, Zerbst, Moltzan, Anhalt, Chiffr | nothing on this letter |
| (b) Francis I's printed correspondence | Potter's inventories above; Champollion-Figeac not searched this session | |
| (c) Dorez, Catalogue de la collection Dupuy I (1899) p.439-440 | IA cataloguedelaco01dupugoog | entry = the BnF notice verbatim; says "presque entièrement en chiffres", **no mention of a decipherment**, although Dorez notes "déchiffrement interlinéaire" for other items. Also lists "A François Ier, par Joachim de Moltzain (?), 12 mars s. a., en latin (47)" in Dupuy 264 |
| (c) BnF Archives et manuscrits cc88606j | fetched once (HTTP 200) | same text; index entries "ANHALT-ZERBST-DESSAU (Ernest, prince D')" and "(Joachim, prince D'), frère d'Ernest". No decipherment note |
| (c) who annotated the volume | Dorez: Théodore Godefroy's signed notes at ff.8-9 | the gloss hand was not compared with them (no image of ff.8-9 fetched). See section 5 for why a 17th-century gloss is unlikely |
| (d) Internet Archive full text | be-api fts, whole collection: "Dupuy 468" / "Dupuy, 468" (51 items, all snippets read: Suffolk instructions, Cleves treaty f.41, Colin f.43-48, Rincon, Corsini f.156, Raumer's 1630s excerpts; none f.28), "Dupuy, vol. 468" (12), "confederatorum consentiente" (0), "in opidum Cerbes" (0), "nulla fiat mencio" (30, all legal texts), "Moltzan" "Zerbst" (372 genealogical/secondary, none about this letter in the first page) | no hit for this letter |
| (d) Gallica full text (SRU) | text adj "Dupuy 468" (6 unrelated), text adj "confederatorum consentiente" (0), text adj "nulla fiat mencio" (4 unrelated), Moltzan + Lunebourg + Dupuy (6: Mignet, Barrillon, Le Glay, RDM 1829, Acad. sc. morales), Moltzan + Zerbst (0) | no hit. Gallica texteBrut answered with an altcha challenge; stopped |
| (d) HathiTrust | not run: full-text search is behind Cloudflare, and the brief allows only the APIs, which cannot phrase-search. The same editions were read in IA copies instead | unreachable for phrase search |
| (d) Google Books | WebSearch only, 8 queries (sender, recipient, Latin phrases, Moltzan and Ernest with Zerbst, Dupuy 468 with Anhalt/Lüneburg) | no page on this letter |
| (e) solver repositories | fresh shallow clones 23 Sept 2026: dbourdeau/cyphersolver 763a3b9, aaymeloglu/unsolved-ciphers 2495c45; grep -ri anhalt, dupuy ?468, btv1b10035959t, zerbst, moltzan, maltzan, lüneburg, lunebourg | no hit for this letter. cyphersolver's hits are other Anhalt/Lüneburg items (gallica_sweep, vanreede1787, riksarkivet1628). caprile1519 mentions "Joachim [Moltzan?] at the Polish court" in another context |
| (e) Cryptiana (sources/cryptiana/, mirror) | grep anhalt, dupuy 468, moltzan, maltzan, zerbst, lüneburg; francis.htm for 1515-19 | no hit (two unrelated Lüneburg mentions, habsburg.htm, charlesii2.htm) |
| (e) Cipherbrain | WebSearch | no page |
| (f) scholarship | WebSearch: Desenclos on Francis I's ciphers; Moltzan 1518 Kaiserwahl Chiffre; Ernst von Lüneburg 1518 | no study of this letter found |
| (f) JSTOR, Google Scholar full text, dissertations | **unreachable** (no credentials in this session) | queries for a session with credentials: JSTOR `"Dupuy 468"`; `Moltzan AND "François Ier" AND 1518`; `"Ernest de Lunebourg" OR "Ernst von Lüneburg" AND 1518 AND Zerbst`; `"Joachim von Maltzan" Kaiserwahl`. Google Books full text: `"Dupuy 468" 28`, `"confederatorum consentiente"`, `"in opidum Cerbes"`, `"Moltzan" "Zerbst" 1518`, `"Ernestus dux" "Joachimus" "christianissime rex"` |
| DECODE | unreachable (no credentials); the check-solved sweep's cached-catalogue grep for "anhalt" was negative, and "moltzan", "lüneburg", "dupuy 468" were not run | a session with the cache should grep them |

## 5. The gloss: contemporary or later, and what it implies

What the images show (7 crops viewed: r03_s1, r13_s1, r17_s2, v02_s1, r27_s1, v05_s2, legend, and canvas 65). The
gloss is a smaller, lighter humanist cursive in grey ink. It is written over every cipher group and is not
confined to hard words. It abbreviates in the chancery way (chrmus, chrmo), keeps the medieval spelling
(fedus), and makes a working decipherer's slips (nos for eos). A 17th-century antiquarian such as Godefroy would
be unlikely to decipher a whole letter interlinearly without a key, and Dorez does not mention a decipherment.

Printed evidence that such letters were deciphered at the French court on receipt:
- Robertet to Bonnivet, 4 March 1519 (RTA JR I no. 126, n.1, citing BnF fr.5756): Moltzan's letters "kamen
  am 3. März abends in Paris an und wurden sofort dem Kanzler geschickt, pour translater et deschiffrer ce qui
  estoit en latin et chiffre".
- Francis I to Bonnivet and Guillart, 5 March 1519 (Potter 1519 no. 55, BnF fr.5761 fo.63v-64v, DRA I no.126):
  "J'ay ordonné au chancellier de vous envoier les dechiffremens et translatz qu'il a faiz de ce que Joachin
  Moltzan a icy escript ... Aussi vous envoira la chiffre d'icelluy Joachin."
- Bonnivet and Guillart to Francis I, 1519 (RTA JR I): a courier from Moltzan came "mit einem chiffrierten Briefe
  für den König, den sie nicht auflösen können".
- Mignet I p.161-162 n.4, of Moltzan's Brandenburg articles in Dupuy 263: "L'original avec le déchiffrement des mots chiffrés
  écrit dessus".

**Conclusion (probable, not established).** The gloss is most probably the decipherment made in Duprat's chancery
in 1518-19. It was not compared letter by letter with any chancery hand, and Dupuy 263 and 264 were not viewed.
**Implication:** the letter was read by its recipient. The repo's H grade (a reading "from a key source") is
correct, but the key source is the original decipherment, so the reading is a transcription of it. "Later hand"
in the repo means "a second hand, written after the text", not "a later century".

## 6. Tests of the reading

| test | result |
|---|---|
| `python3 check.py --check` | exit 0, "reading.txt and reading_tokens.tsv are current" |
| key.tsv applied independently to ciphertext.txt (the verifier's own script, scratch) | 49 of 49 rows identical to reading.txt's reading rows; 687 cipher tokens, 6 with no key value (= the 6 unread). Grade counts in reading_tokens.tsv: H 630, S 33, M 18, unread 6, matching NOTES.md |
| 13 glossed words against the crops | r03 cerbes / et / ibi over L q R 7 q P, q Po, V 7 V; r13 principes over V U L V 4 q P, attrahi over 6 Po Po R 6 Π V; r17 confederatorum; v02 ligam over 9 V + 6 D, et over q Po, confederationem; r27 chrmus over K, hoc over Π Y L, fedus over 3 q T cc P, petat over 4 q Po 6 Po; v05 pensionem over 4 q U P V Y U q D, chr over K. In every case the gloss word stands over the signs that key_from_gloss.tsv aligns with it, letter for letter |
| control (rule 3) | present (runs.tsv, 99.8% and 100% blind); not re-run |

The reading is reproducible and matches the page where sampled. The transcription is still conditional on one
reconciler's reading (the passes agreed on 60%). Nothing found here contradicts it.

## 7. Postmortem

**Failure:** there was no novelty over-claim. The folder never says new, unread or first, and it says plainly that
the editions were not searched. But the target's identity came from the catalogue's bracketed guess, "Anhalt,
1515/16", and nobody tested that guess against the plaintext after decoding. The subscription "Ernestus dux",
"ego filius ... Luneburg" and "ego Joachimus" point elsewhere, so the solver's search list (Anhalt editions,
the negotiations of 1515-16) pointed at the wrong sender and year. The word "later" for the gloss hand was also
read as meaning "centuries later", although the evidence points to the recipient's own decipherment.

Corrections made in this commit:
- NOTES.md: a verifier block under the status line (class, attribution, gloss); the title line annotated.
- status.json: the target's note gets the class and the attribution doubt; name, stage and holder are left to the
  orchestrator (rule 10: stage 9 is set from this file).
- Not changed: reading.txt, key.tsv (check.py regenerates reading.txt; their wording "later hand" is literally
  true); LEDGER.md and ROOM.md (no over-claim found); QUEUE.md M7 still carries the catalogue attribution and is
  outside this brief, so the orchestrator should correct it.

## 8. Suggested follow-ups (not done)

1. A historian's check of sender and date against Moltzan's letters in Dupuy 263 and 264 (same volume series,
   Gallica). If the hand, the cipher and the formula match, the attribution becomes established.
2. Compare the gloss hand with the decipherment on Dupuy 263 (Mignet's "déchiffrement ... écrit dessus").
3. Search RTA JR II, Mignet II, Mignet's 1854 Revue des deux Mondes articles, Potter's 1517 inventory and index,
   and JSTOR/Google Books with the queries of section 4, before any N4 claim.
4. The same key may read Moltzan's other cipher letters in Dupuy 263-264 (Francis I sent "la chiffre d'icelluy
   Joachin" to his envoys in March 1519).

## 9. Requests this session

archive.org 41 (12 advancedsearch, 6 metadata, 23 djvu downloads incl. 6 range reads), be-api.us.archive.org 8,
gallica.bnf.fr 14 (10 SRU, one connection reset retried once; 4 texteBrut/HEAD, ending in an altcha challenge,
stopped), web.archive.org 6 (1 CDX, 3 PDFs, 2 SSL failures), cour-de-france.fr 1 (403 Cloudflare, stopped),
archivesetmanuscrits.bnf.fr 1, github.com 2 clones, WebSearch 8. All 1.5 s or more apart, one host at a time,
with a descriptive User-Agent.

## Second, adversarial audit (23 September 2026)

Second verifier session, 23 September 2026, 22:08-22:16 UTC (Opus, no subagents). This session did not take part in
the transcription, the solving or the first audit. Its mandate was to assume that the letter is already in print and
to find it. **It found it.**

### Verdict: N1. The plaintext has been in print since 1896.

**The finding.** *Deutsche Reichstagsakten, Jüngere Reihe*, **Band II** (ed. Adolf Wrede, Gotha: F. A. Perthes, 1896),
*Beilagen zur Einleitung* IV, no. 1, **p. 122**. The heading reads: "IV. Verhandlungen von Ernst v. Lüneburg und Joachim v. Moltzan
in Zerbst. 1. Ernst v. Lüneburg und Joachim v. Moltzan an Franz I. über Verhandlungen mit Brandenburg, Lüneburg und
Mecklenburg in Zerbst. — [1520] Januar 24." Source note: "Aus Paris Bibl. nat. f. fr. 3897 fol. 146. Franz.
Übersetzung. Dazu fol. 149b die Indorsalnotiz: Translat des lettres du filz du duc de Lunembourg et Joachin au roy."
The whole letter is printed there in this contemporary French translation, from "Sire, apres tres-humbles
recommandations" to "Dat. (s. l.) la veille de sainct Pol au matin à cinq heures". The Einleitung summarises it at
pp. 28-29 ("Vgl. Beil. nr. IV"). No. 4 of the same Beilage (pp. 125-126) is Ernest's covering letter to Chancellor
Duprat, "A Celles, le 28e de janvier" [1520]. It is also from fr. 3897 (fol. 147f.) and refers to "le Brief Joachims von
Moltzan". Read in two independent scans: IA `bub_gb_yAQQAAAAYAAJ` (lines 8011-8060 of the djvu text) and IA
`deutschereichst07kommgoog` (lines 8226-8275). The two scans agree word for word apart from OCR noise.

**Earlier still: a catalogue entry since 1881.** *Catalogue des manuscrits français*, t. III, *Ancien fonds* (Paris:
Firmin-Didot, 1881), fr. 3897, item 73: "Lettre d'«Ernest, duc de Lunembourg» et «Joachin» de Brandebourg à
François Ier. «Escript la veille de Sainct Pol, au matin à cinq heures». Copie. (Fol. 146.)". Item 74 is the Celle letter
of 28 January (IA `p1cataloguegnr03bibluoft`, lines 19016-19022).

**It is this letter.** Every sentence of reading.txt has its counterpart in the printed French, in the same order:

| reading.txt | RTA JR II p.122 (French translation, 1520) |
|---|---|
| r01-r03 Post humilimam atque humilimam commendationem ... nos ambos saluos ... venisse in opidum Cerbes | apres tres-humbles recommandations ... mon compaignon et moy sommes arrivés en la ville de **Cerbes** |
| r03-r04 et ibi erant simul **?** Saxonie, Marchio, Luneburg, ambos Mekleburg, et multi alii | et là estoient ensemble **l'arcevesque de Magance**, le duc de Saxe, le marquis de Brandebourg, le duc de Lunembourg, les deux ducz de Meklembourg et plusieurs autres princes |
| r04-r05 ego filius [ducis] Luneburg tractatum cum patre meo | Et moy, filz du duc de Lunembourg, tirey mon père à part pour parler de notre affaire |
| r05-r07 ego Iochin ut proposui Marchio[ni] commissionem meam in presentia Luneburg vnius de Mekleburg | et moy, Joachin, en communiquey audit marquis en luy monstrant en la présence du duc de Lunembourg et l'ung des Meklembourg ma commission |
| r08-r10 conclusum ... Marchio cum auxilio Luneburg et Mekleburg faciant totis viribus ut fedus concludatur | La conclusion fut que ledit marquis avec la bonne aide de Lunembourg et Meklembourg mectra peine de traicter icelle alliance |
| r11 ut primo de christianissimo nulla fiat mencio | que de vous au commancement ne soit faicte aucune mencion |
| r12-r14 inter eos et qui inter Germanie principes attrahi possunt fiat fedus | que entre eulx et le plus de princes de la Germanie, qu'ilz y pourront actrayre, se face icelle alliance |
| r14-r21 articulus ... nullus alius in istud fedus acceptaretur nisi maiore parte confederatorum consentiente ... minor pars ... consentire teneretur | articles exprès que nul ne puisse entrer en icelle sinon du consentement de la plus grant part des alliés et confedérés ... la meindre partie sera tenue le ratiffier |
| r22-r24 Deinde potest **palatinus** tractari cum his qui non dum habent speciale fedus aut singulare amiciciam cum christianissimo | Puys l'on pourra **peu à peu** traicter avec ceulx qui n'ont encores specialle alliance ou singulière amytie avecques vous |
| r25-r27 ubi securum sit quod longe maior pars erit pro christianissimo, tunc optimum erit ut christianissimus hoc fedus petat velle inire | quant l'on sera asseuré que la plus grant partye sera pour vous, lors sera bon que requeriez entrer en icelle ligue |
| r28-r30 etiam si aliquem noluissent esse in federe cum christianissimo ... astricti erunt esse confederatores | si aucuns d'iceulx princes ne voulloient avoir alliance avecques vous, seront toutesfois contraintz estre voz alliez |
| v01-v03 maiorem ligam et confederacionem in fauorem christianissimi quod sit in tota Germania | la plus grant ligue et confedération en votre faveur, qui soit en toute la Germanye |
| v04-v06 Marchio, Luneburg ... qui non habent a christianissimo pensionem ipsis promittatur | comme le marquis et le duc de Lunembourg conseillent, promectre pensions à ceulx, qui de vous n'en ont aucune |
| v06-v07 videtur Marchioni consultum ut consortii nobis Gallum christianissimus non mittat principaliter | si est d'avis ledit marquis que ne debvez envoyer par-deçà ung Françoys pour notre compaignon, ou au moins qui ne tienne grant estat |
| v07-v10 sed nobis duobus autoritate det ... promittendi donec ... fedus inter eos factum sit ac tempus erit ut christianissimus ingrediatur | mais debvez donner à nous deux puissance de povoir promectre icelles pensions jusques à ce que ladite ligue sera conclute ... et que sera temps que entriez en icelle |
| v11-v12 si pars adversa de ista materia intelligeret aliquid impediret totis viribus | si partie adverse povoit entendre quelque chose de cest affère, elle mectroit peine de le rompre |
| v13 Nos minore suspicione faciemus et citius perficiemus | Nous conduyrons ledit affaire en moindre danger et suspeçons et plustost l'acheverons |
| v13-v15 ne longis litteris maiestati vestre fastidio simus ... quas ego Joachimus ad dominum Cancellarium et dominum admiraldum scripsi | La reste pour crainte de vous ennuyer moy, Joachin, l'escrips à mess. voz chancellier et admiral |
| v18 Datum in vigilia sancti Pauli in mane hora quinta | Dat. (s. l.) la veille de sainct Pol au matin à cinq heures |

**Classification (rule 10).**
- Prior plaintext: **yes.** The full text is printed in the contemporary French translation, RTA JR II p.122 (1896).
  The letter is also listed in the 1881 BnF catalogue.
- Prior decipherment: the letter was deciphered on receipt in 1520. The French "translat" was made from the
  deciphered Latin, and the interlinear gloss on f.28 is most probably that decipherment. The first audit's
  section 5 inference is now strongly supported: the printed text is the output of the chancery's decipherment.
- Prior mapping in print of *this ciphertext* (Dupuy 468 f.28) to that text: **not found.** RTA JR II cites only the
  translation in fr. 3897. It does not mention the Latin cipher original in Dupuy 468. Dorez (1899) and the BnF
  notice give the Dupuy leaf to "Anhalt, 1515 ou 1516" and do not link it to fr. 3897.
- The Latin wording itself: not found in print. What is printed is a translation.
- **Class N1.** Our reading is an independent re-reading of a letter whose plaintext has been published since
  1896. N0 could be argued in substance, because the printed text comes from the 1520 decipherment of this very item. It is
  not assigned only because no print links the Dupuy 468 cipher leaf to it. N2 does not apply, because the text
  is published and not merely known elsewhere.
- Evidence quality: direct. The printed page was read in two scans and compared sentence by sentence. Confidence:
  very high.

**Safe sentence.** "BnF Dupuy 468 f.28 is the Latin cipher original of the letter of Ernest of Brunswick-Lüneburg
and Joachim von Moltzan to Francis I, Zerbst, [24 January 1520]. Its French translation (BnF fr. 3897 fol. 146) was
printed in Deutsche Reichstagsakten, Jüngere Reihe II (1896), p. 122 (N1). The leaf carries a contemporary interlinear
decipherment. Transcribing it gives the Latin that the printed translation renders. The catalogue's 'Anhalt, 1515
ou 1516' is wrong, and no printed link between the Dupuy leaf and the RTA text was found."

**Unsafe sentences.** Anything that calls the letter unread, unknown, newly recovered, first deciphered or unpublished;
"new evidence for German politics in 1518/19"; "the princes proposed approaching the Count Palatine"; "N3"/"N4";
"solved" as a result of this project. At most it is a contribution: the Latin original identified, the catalogue's
attribution and date corrected, and the reading checked against the printed translation.

### Corrections this finding forces

1. **Date.** The date is **24 January 1520**, the vigil of the Conversion of St Paul. The catalogue's 1515/16 is wrong,
   and so is the first audit's 1518/19. Wrede dates it by the Zerbst Tag, the Zerbster Vertrag of "Dinstag nach
   Vincentii" (24 Jan.) 1520, and by Ernest's letter from Celle of 28 January. The first audit's senders were right.
2. **"palatinus" (r22) is very probably a misreading of *paulatim*.** The French has "peu à peu" in that place,
   and there is no Count Palatine in the printed text. It is a clear word, so it is ungraded, and it was misread in
   transcription. NOTES.md's paraphrase "The Count Palatine could be approached" is therefore wrong. The line should be
   re-read on the image (canvas 63, r22). This session does not edit reading.txt or ciphertext.txt (no decoding).
3. **The unread token in r03** stands where the French names "l'arcevesque de Magance". It is probably a word sign
   for Mainz. This is left to the solver: a hint, not a reading.
4. **The first audit's N3 was a search-coverage failure, not a reading error.** It read RTA JR I and listed JR II as "not searched ...
   relevant only if the letter is of 1520-21". That was the volume. The Eckert lesson again: the edition that
   prints the sender's own negotiations was one volume further on. Its N3 and its safe sentence are superseded by this
   section.

### Search log, this session (read pages, not only hit counts)

| family | read | hits | judgement |
|---|---|---|---|
| 1. RTA JR I (Kluckhohn 1893), IA `bub_gb_0gFoAAAAMAAJ` (copies `bub_gb_6gcQAAAAYAAJ`, `deutschereichst08kommgoog`, `deutschereichst10kommgoog` identified) | Einleitung pp. 52-57 (Moltzan's 1518 alliance plan, Ernst's journey), pp. 131-139 (Moltzan's instruction of 23 Oct 1518: "capitula et articuli federis fiant"), p. 146-147 n. (Moltzan in Berlin end 1518), the chronological register (1519) for Moltzan/Lüneburg/Franz, the index entries Lüneburg ("Sohn Ernst"), Moltzan; grep of all Paris source notes (Dupuy only 263, via Le Glay), Chiffr-, Zerbst variants ("Zerbst 262" only) | Moltzan to Francis I, 12 Mar 1519, nos. 416-419 (= Le Glay II 329, Dupuy 264), not this letter | not in JR I. JR I points forward: Ernst was still in France in Nov 1518 |
| 1. RTA JR II (Wrede 1896), IA `bub_gb_yAQQAAAAYAAJ`, `deutschereichst07kommgoog` | Einleitung pp. 28-30 (Zerbst Tag, Jan 1520, notes); Beilagen zur Einleitung IV nos. 1-4, pp. 122-126 | **IV no. 1, p. 122: this letter, in full, French translation; no. 4 pp. 125-126: Ernest to Duprat, Celle, 28 Jan [1520]** | **found** |
| 1. RTA Nachträge | not needed after the finding | | |
| 2. Lisch, Maltzan Urkunden I-IV, Jahrbücher; Havemann; ADB/NDB | not read. Could only add a second printing | | not needed for the class |
| 3. Mignet II, Champollion-Figeac, Potter 1515/1517, Ulmann, Bauer, Weiss, CAF index | not read (same reason) | | not needed for the class |
| 4. BnF catalogue history | *Catalogue des manuscrits français* III (1881), fr. 3897 items 73-74, IA `p1cataloguegnr03bibluoft` | the translation catalogued, with the date formula | the letter's existence and date formula in print since 1881. Dorez's Dupuy 468 entry was read by the first audit (no link) |
| 5. Full text | IA fts `"ville de Cerbes"` (2 hits: the two RTA II scans); `"duc de Lunembourg et Joachin"` (2: RTA II, the 1881 catalogue); `"Moltzan" "Cerbes"` (8: RTA II ×2, the rest unrelated). HTRC not used: the page was read in two IA scans | as listed | no printing of the Latin, and no link of Dupuy 468 to the text found |
| 5. WebSearch (Google Books/JSTOR snippets) | `"Dupuy 468" Zerbst OR Cerbes OR Lunebourg OR Moltzan 1520`; `"Moltzan" "Zerbst" 1520 Franz I. Ernst Lüneburg Bündnis Brief chiffriert` | nothing on the letter | for a credential session (only to test for N0, a printed link of the Dupuy leaf): Google Books `"Dupuy 468" 1520 Lunebourg`, `"fr. 3897" Moltzan`, `"Cerbes" Moltzan`; JSTOR `"Ernst von Lüneburg" Zerbst 1520 Moltzan` |
| 6. Cryptologic literature, DECODE cache | not re-run (first audit: negative). A cryptologic study would matter only for N0 | | |

**Requests this session:** archive.org 9 (2 advancedsearch, 6 RTA djvu texts, 1 catalogue djvu text),
be-api.us.archive.org 3 (fts), WebSearch 2. One host at a time, at least 1.6 s apart, descriptive User-Agent. No credentials used.

**Postmortem (one line).** The first audit searched the right edition series but stopped one volume short, because its
date inference (1518/19) ruled out JR II. The catalogue had already listed the translation, under its date formula,
in 1881.
