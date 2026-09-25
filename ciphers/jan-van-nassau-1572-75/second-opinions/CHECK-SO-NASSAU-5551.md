# CHECK: SO-NASSAU-5551 (PR 12, `chatgpt-2026-09-25-5551.md`)

Citation check by V6-SOCHK (LANE V6), 25 Sept 2026, 16:55-17:10 UTC. Every citation in the answer was traced
to the source itself where it could be reached. Repository-file claims checked against `main` at a05e018.

| # | Claim in the answer | Result | What was read |
|---|---|---|---|
| 1 | Glawischnig, *Niederlande, Kalvinismus und Reichsgrafenstand 1559-1584* (Marburg 1973), Google Books `DhMBAAAAMAAJ` | confirmed (bibliographic) | Google Books API: title, Rolf Glawischnig, Hessisches Landesamt für geschichtliche Landeskunde, 1973, 274 pp. |
| 2 | Glawischnig's snippet: 17 Apr 1574, Cologne, Jan to Willem, with 21 Apr Wesel, KHA A XI 5 and STAMa 4f Nld. 165 | repository-reported, not re-confirmed | the answer attributes this to AUDIT.md V-TX2 and marks it unverified; one Google Books phrase query ("17. April 1574" Glawischnig) returned 0 items, which is not a negative for a snippet-view book |
| 3 | A.E.M. Janssen, review of Glawischnig, *BMGN* 90 (1975), pp.293-295, DBNL; book grew from a 1971 Frankfurt dissertation | confirmed | DBNL page: [p.293] heading with the full Glawischnig citation (274 blz.), [p.294] "zijn in 1971 te Frankfort/Main verdedigde dissertatie", [p.295]; no cipher lines reproduced |
| 4 | Japikse, *Correspondentie van Willem den Eerste* I covers 1551-1561; Hyma's review, *AHR* 40(2) 1935, pp.324-325, DOI 10.1086/ahr/40.2.324 | confirmed | CrossRef record: Hyma, *AHR* vol.40 no.2, pp.324-325, title "... Deel I, 1551-1561 ... 1934" |
| 5 | Nicolas Du Mont, *Les obsèques et funérailles de Sigismond Auguste ... Plus l'Entrée, sacre & couronnement de Henry ...* (Paris, Denis du Pré, 1574), BnF cb303760672, privilege 15 Apr 1574 | confirmed | BnF catalogue record: title, author, publisher as stated; "Privilège du 15 avril 1574 octroyé à Denis Du Pré" |
| 6 | BnF Français 3961, items 1-3: 29 Mar 1574 objection of the Polish clergy; Henri's address to the senate, 6 Apr 1574; his declaration on leaving Poland, 18 Jun 1574; Gallica `btv1b9059409k`, Biblissima manifest | confirmed (catalogue level) | Gallica IIIF manifest: shelfmark Français 3961, "Recueil de lettres originales et de copies...", 1501-1700; Biblissima page: items 1-3 with those dates verbatim. Folios not read (the answer says so) |
| 7 | Volker Press, *BMGN* 99 (1984), p.691: the Christoph killed in 1574 was Pfalzgraf Christoph, son of Friedrich III; n.44 cites Glawischnig pp.105-111 | confirmed | DBNL page: [p.691] "unter Beteiligung von Friedrichs III. Sohn, Pfalzgraf Christoph, und der nassauischen Brüder Ludwig und Heinrich ... Mookerheide am 13./14. April 1574"; footnote 44 "Glawischnig, Niederlande, 105-111" |
| 8 | the prompt calls him a Württemberg prince | confirmed (an error in our files) | PROMPT-chatgpt-5551.md line 14 and NOTES.md lines 782-784, 806, 991 say "Christoph(ff) of/van Wurttemberg", following the WVO summary's wording; Christoph of Württemberg died in 1568 |
| 9 | reading_5551_tokens.tsv grades C 23, I 2, M 1, U 6; 106=k and 89=f are I, "not observed in 4613/4615"; 136 = uingt with the following 1 unaccounted for | confirmed | token file counted by script; `../lodewijk-van-nassau-1573-74/key.tsv` rows 89, 106, 136 verbatim |
| 10 | ciphertext_5551.tsv notes disagreement on VAN/VON and VFF | confirmed | ciphertext_5551.tsv header lines 6-8, row L2 9 "=vff ?" |
| 11 | web-index search log (11 queries) | not re-run | a search-engine silence, not a source |

Counts: 9 confirmed (1, 3, 4, 5, 6, 7, 8, 9, 10), 1 repository-reported and not re-confirmed (2), 1 not re-run
(11). Nothing invented.

**Does any confirmed lead move the class?** No. Glawischnig and STAMa were already in AUDIT.md (V-TX2) as the
reason the item is not at N4; Janssen confirms the book's identity but reproduces no cipher text; Press gives a
page range (105-111) to read in Glawischnig, a narrower lead, not a print of the two lines. N3 stands. No flag.

**Correction the answer raises (not applied here; for the lane that owns NOTES.md):** the dead Christoph of
Mookerheide is Pfalzgraf Christoph (son of Elector Friedrich III of the Palatinate), not a Württemberg prince
(Press 1984, p.691). The WVO summary's wording should be quoted as WVO's, with the correction beside it.

**Verdict: merge.** A faithful answer; its external citations are real and say what it says; the one unconfirmed
item is a repository report it marked unverified itself.

Requests: www.googleapis.com 3 (the volume record twice, one call repeated by mistake, and one phrase query; the last two under 3 s apart, noted), www.dbnl.org 2,
api.crossref.org 1, catalogue.bnf.fr 1, gallica.bnf.fr 1 (IIIF manifest), iiif.biblissima.fr 1.
