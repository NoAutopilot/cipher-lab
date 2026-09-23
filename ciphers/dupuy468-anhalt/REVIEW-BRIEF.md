# Review brief: BnF Dupuy 468 f.28, a Latin cipher letter to François I

Written 23 September 2026 for an independent reviewer (a person or another model). Everything here is in the
repository https://github.com/NoAutopilot/cipher-lab under ciphers/dupuy468-anhalt/ (NOTES.md, AUDIT.md,
ciphertext.txt, key.tsv, key_from_gloss.tsv, reading.txt, check.py, images/). Nothing in this brief claims a
"first" or a "new" discovery. We want to be told where this is wrong.

## 1. The claim, in the only wording we allow ourselves

BnF Dupuy 468 f.28 is a Latin cipher letter to Francis I. The catalogue gives it to Ernest and Joachim of Anhalt,
1515/16. It is more probably from Ernest of Brunswick-Lüneburg and Joachim von Moltzan, 1518/19. It carries an
interlinear decipherment in a second hand, probably contemporary. That decipherment was transcribed and the key it
implies applied to the whole letter. Together they read 663 of the 687 cipher tokens (630 from the gloss, 33 from the
key with a synthetic control at 99.8%); 18 are uncertain and 6 unread. No printed text or printed decipherment of the
letter was found after the logged search (class N3 on our scale: no prior plaintext or decipherment located; not N4,
because JSTOR, Google Books full text, HathiTrust full text and parts of the Reichstagsakten were not reached).

So: we did not break a cipher. A chancery clerk did, around 1518/19, on the leaf. We transcribed that, extended it
with a key, and think the catalogue has the wrong sender and date. The open question is whether anyone has printed
this letter or its decipherment, under any attribution.

## 2. The document

- BnF, Collection Dupuy 468, f.28r-v with the subscription on the following leaf; Gallica ark:/12148/btv1b10035959t,
  canvases 63-65 (images free online). Catalogue: "Lettre d'Ernest et Joachim d'Anhalt à François Ier, orig., en
  latin, presque entièrement en chiffres (28)".
- Cipher: a simple substitution, one sign per letter (21 letter signs, R with a rare second form), plus word signs
  read from the gloss (K = christianissimus, F = marchio, theta = Luneburg, a lone P-shape = Mekleburg) and two
  separator signs. 687 cipher tokens; the opening and closing formulae are in clear.
- The gloss: a second hand wrote the Latin plaintext above almost every cipher word. Letters of the King and his
  officers in March 1519 say Moltzan's Latin cipher letters were sent to the Chancellor to be deciphered and
  translated, which points to a contemporary chancery decipherment. The hand was not compared letter by letter
  with any known chancery hand.

## 3. Why we think the attribution is wrong (grade I, inferred, for a historian to confirm)

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

## 4. What was searched and where it was not found

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

## 5. What would change our mind

- Any printed text, summary (Regest) or decipherment of this letter, under Anhalt, Lüneburg, Moltzan/Maltzan, or
  anonymous, in the Deutsche Reichstagsakten (Jüngere Reihe I-II), Lisch's Maltzan Urkunden-Sammlung, Le Glay,
  Mignet, Barrillon, the Catalogue des actes de François Ier, Potter's inventories, or any journal article.
- A published reading of the same cipher key from another Moltzan letter (he wrote several in cipher).
- Evidence that the gloss hand is later than the 16th century, which would change the recovery story.
- Errors in the reading itself: reading.txt below, with the key in key.tsv.

## 6. Questions for the reviewer

1. Is this letter, or its content, printed anywhere you know? Please give the edition and page.
2. Does the attribution to Ernest of Brunswick-Lüneburg and Joachim von Moltzan, and the date 1518/19, hold up
   against what you know of the 1519 election diplomacy?
3. Read the Latin below: does it read as a coherent letter? Where does it not?
4. Is there a source family we have plainly missed?

## 7. The reading (regenerated by check.py from ciphertext.txt and key.tsv)

```
# Reading of BnF Dupuy 468 f.28r-v, regenerated by check.py from ciphertext.txt and key.tsv.
# Clear words lower case; deciphered UPPER CASE (word division of cipher runs is not marked in
# the cipher and is not restored here); <WORD> = word sign; ? = unread; 'g' rows = the gloss.
# Grades: H 630, M 18, S 33, unread 6
r00  Amicissime potentissime ac christianissime rex ac domine domine obseruandissime
r01  Post humilimam atque humilimam commendationem maiestatem vestram certiorem reddi-
r02  mus nos ambos saluos ac fortunatos venisse INOPIDUM
r02g in@8-9 oppidum@10-15
r03  CERBESSETIBIERANTSIMUL? <SAXONIE> <MARCHIO>
r03g cerbes@1-6 et@8-9 ibi@10-12 erant@13-17 simul@18-22 ma?ch??@23 saxo@24 march@25
r04  <LUNEBURG> ambos <MEKLEBURG> ETMULTIALII?EGOFILIUS <MEKLEBURG> <LUNEBURG>
r04g luneburg@1 mekleburgen@3 et@4-5 multi@6-10 alij@11-14 t@15 ego@16-18 filius@19-24 dux@25 de_lune@26
r05  tractatum cum patre meo ad patrem et EGOIOCHINUT
r05g ego@8-10 joachim@11-16 ut@17-18
r06  PROPOSUI <MARCHIO> CONMISSMONEMMEAM
r06g proposui@1-8 marchio@9 commissionem@10-21 meam@22-25
r07  In presentia <LUNEBURG> vnius de <MEKLEBURG> et consortij mei quia <MARCHIO> hic placuit
r07g de_luneburg@3 mekle@6 marchion@11
r08  conclusum hic est <MARCHIO> CUMAUXILIO <LUNEBURG> ?ET
r08g marchio@4 cum@5-7 auxilio@8-14 de_luneborg@15 et@17-18
r09  <MEKLEBURG> faciant totis viribus ut FEDUSCONCLUDAT
r09g mekleburg@1 fedus@6-10 concludatur@12-20
r10  UR cum tot sint possibile est per ipsos omnibus melius et
r10g concludatur@1-2
r11  utiliter pro <CHRISTIANISSIMUS> videtur ut primo de <CHRISTIANISSIMUS> nulla fiat mencio sed
r11g chrmo@3 chro@8
r12  inter EOSETQUIINTERGERMANIEPR
r12g eos@2-4 et@5-6 qui@7-9 inter@10-14 germanie@15-22 principes@23-24
r13  INCIPESATTRAHIPOSSUNTFIAT
r13g principes@1-7 attrahi@8-14 possunt@15-21 fiat@22-25
r14  FEDUS?ETUNUSARTICULUTINP
r14g fedus@1-5 et@7-8 unus@9-12 articulus@13-21 imponetur@22-24
r15  ONETURUTNULLUSALIUSINIS
r15g imponetur@1-6 ut@7-8 nullus@9-14 alius@15-19 in_istud@20-23
r16  TUDFEDUSACCEPTARETURNISI
r16g in_istud@1-3 fedus@4-8 acceptaretur@9-20 nisi@21-24
r17  MAIOREPARTECONFEDERATORUMCON
r17g maiore@1-6 parte@7-11 confederatorum@12-25 consentiente@26-28
r18  SENSIENTEETQUEMCUMQUEMAIO
r18g consentiente@1-9 et@10-11 quem@12-15 nunq@16-18 maior@22-25
r19  RPARSADMITTERET aut quoniam ?CONSENT
r19g maior@1 pars@2-5 admitteret@6-15 consentiret@19-25
r20  IRETUTMINORPARSADMITTERE
r20g consentiret@1-4 ut@5-6 minor@7-11 pars@12-15 admittere@16-24
r21  ETCONSENTIRETENERETUR Deinde potest
r21g et@1-2 consentire@3-12 teneretur@13-21
r22  palatinus TRACTARICUMHISQUINON dum
r22g tractari@2-9 cum@10-12 his@13-15 qui@16-18 non@19-21
r23  habent speciale FEDUSAUT singulare AMICICIAMCU
r23g fedus@3-7 aut@8-10 amicitiam@12-20 cum@21-22
r24  M <CHRISTIANISSIMUS> UTSPECIALEFEDUSFIAT aut amicitia
r24g cum@1 chrmo@2 ut@3-4 speciale@5-12 fedus@13-17 fiat@18-21
r25  a tandem ubi SECURUMSIT quod LONGEMAIO
r25g securum@4-10 sit@11-13 longe@16-20 maior@21-24
r26  RPARS erit et conficiet PRO <CHRISTIANISSIMUS> tunc optimum erit ut
r26g maior@1 pars@2-5 pro@9-11 chrmo@12
r27  <CHRISTIANISSIMUS> HOCFEDUSPETATUELLEINIRE
r27g chrmus@1 hoc@2-4 fedus@5-9 petat@10-14 velle@15-19 inire@20-24
r28  hoc modo etiam si aliquem noluissent ESSEINFEDERE
r28g esse@7-10 in@11-12 federe@13-18
r29  CU? <CHRISTIANISSIMUS> hoc modo ASTRICTIERUNTESS
r29g rum@1-3 chrmo@4 astricti@7-14 erunt@15-19 esse@20-22
r30  ECONFEDERATORESES <CHRISTIANISSIMUS> vri prudenti pauca
r30g esse@1 confederatores@2-15 chrmi@18
v01  Nos omnino speramus quod firmiter ut cito faciemus MAIOREM
v01g maiorem@9-15
v02  LIGAMETCONFEDERACIONEMINFAUOR
v02g ligam@1-5 et@7-8 confederationem@9-23 infauorem@24-30
v03  EM <CHRISTIANISSIMUS> quod sit INTOTAGERMANIA sed oportet
v03g infauorem@1-2 chrmi@3 in@6-7 tota@8-11 germania@12-19
v04  omnino ut <MARCHIO> <LUNEBURG> omnino consultum ut aliquos etiam nobis necesse et consultum
v04g marchio@3 luneburg@4
v05  videtur ut huius qui non habent A <CHRISTIANISSIMUS> PENSIONEMIPS
v05g chr@8 pensionem@9-17 ipsis@20-22
v06  ISPROMITTATURQ et videtur <MARCHIO> consultum ut
v06g ipsis@1-2 promittatur@3-13 marchioni@18
v07  consortii nobis GALLUMQ <CHRISTIANISSIMUS> non mittat principaliter pro posse sed no-
v07g gallum@3-8 chrus@11
v08  bis struck duobus autoritate det privatis PRINCIPIBU
v08g principibus@7-16
v09  S promittendi donec quando FEDUSINTEREOS
v09g principibus@1 fedus@6-10 inter@12-16 nos@17-19
v10  FACTUMSIT ac tempus erit ut <CHRISTIANISSIMUS> INGREDIA
v10g factum@1-6 sit@7-9 chrmus@14 ingrediatur@15-22
v11  TUR deinde <CHRISTIANISSIMUS> poterit mittere ad placitum eius ita si pars adversa
v11g ingrediatur@1-3 chrmus@5
v12  de ista materia intelligeret aliquid impediret totis viribus ne perficeretur
v13  Nos minore suspicione faciemus et citius perficiemus quod de quibus ne longis
v14  litteris maiestati vestre fastidio simus maiestas vestra intelliget clare ex litteris
v15  quas ego Joachimus ad dominum Cancellarium et dominum admiraldum scripsi qui haud
v16  dubie maiestati vestre omnia significabunt restat nos maiestati vestre quam humilime atque
v17  humilime commendemus quam optimus maximus felicissime custodiat
v18  Datum in vigilia sancti Pauli in mane hora quinta
```

## 8. The key

```
# Key for BnF Dupuy 468 f.28r-v, 23 September 2026. token<TAB>value<TAB>source<TAB>note
# source 'gloss': value read from the later hand's interlinear gloss (key_from_gloss.py, votes in key_from_gloss.tsv).
# source 'search': value from the n-gram search only (runs.tsv). value '=word' is a word sign; '' a null.
# The gloss hand is not identified (see NOTES.md); nothing here asserts who wrote it.
token	value	source	note
q	e	gloss	78 votes; 1 minority (v09 gloss 'nos' over q Y P, cipher reads eos as in r12 where the same group is glossed eos)
V	i	gloss	67 votes
Po	t	gloss	58 votes; r14 token 21 stands where articulus has s
cc	u	gloss	49 votes (u and v)
R	r	gloss	46 votes
R2	r	gloss	2 votes (proposui r06, principibus v08); curled variant of R
P	s	gloss	44 votes; r18 token 4 stands where consentiente has t
6	a	gloss	44 votes
U	n	gloss	40 votes; the gloss writes m in commissionem (r06) and imponetur (r14) where the cipher spells n
Y	o	gloss	34 votes
D	m	gloss	31 votes; r06 token 17 stands where commissionem has i (encipherer's slip)
L	c	gloss	25 votes; the gloss writes t in confederationem (v02) and amicitiam (r23) where the cipher spells c (-cio-)
4	p	gloss	19 votes
9	l	gloss	17 votes
3	f	gloss	16 votes
T	d	gloss	16 votes
+	g	gloss	8 votes
7	b	gloss	3 votes
Z	q	gloss	3 votes (qui, qui, quemcumque); two further Z after g in v06, v07 are unglossed
Π	h	gloss	3 votes (attrahi, his, hoc)
II	x	gloss	1 vote (auxilio)
K	=christianissimus	gloss	12 votes, gloss abbreviated chrmus/chrmo/chrmi (case follows the gloss)
F	=marchio	gloss	6 votes (marchio, marchion, marchioni)
O	=Luneburg	gloss	5 votes (luneburg, de luneburg); theta
PW	=Mekleburg	gloss	3 votes (mekleburg, mekle); P-shape standing alone; r04 token 25 is glossed 'dux' instead (M there)
SX	=Saxonie	gloss	1 vote, gloss 'saxo'; value expanded from the gloss abbreviation, uncertain
g		search	null (dumbbell sign, 13 tokens, at word or clause ends, e.g. 'ligam . et', 'possunt fiat .'); no gloss; the search sets it to null in T-blind and T-glossfixed (runs.tsv)
o		search	null (small circle, 3 tokens, always next to g); no gloss; null in T-blind, 'h' in T-glossfixed: unstable, uncertain
```
