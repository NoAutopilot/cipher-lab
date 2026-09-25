# AUDIT: jan-van-nassau-1572-75

## V6 (LANE V2), 24 September 2026, 10:44-10:55 UTC: WVO 5200, page 1

Verifier V6 (Opus, cap $6, session_01P5vLFcEP9pQd74DHyrWW9E). I did not solve this item. I did not decode it again.
I compared the committed reading with the print.

**Claim under audit** (LANE R2 J2, 10:22 UTC): "5200 p1 read with key_1572 (a printed 1572 table), 807 cipher tokens
H680 M26 U101, real French ('EST REMISE ENTRE LES MAINS DES ESPAGNOLZ QUI ONT SACCAGE TOUT')."

### Verdict

| item | class | prior plaintext | prior decipherment | evidence | confidence |
|---|---|---|---|---|---|
| WVO 5200, William of Orange to Jan van Nassau, Zwolle, 18 Oct 1572, p.1 as read | **N1** | yes: Groen van Prinsterer, *Archives ou correspondance inédite de la maison d'Orange-Nassau*, 1re série, t.IV (Leiden 1837), no. CCCLXXXIX, pp.2-6. The whole letter is printed in roman type. The cipher passage is on pp.3-4 and is not marked as cipher. | Groen does not say so for this letter. The printed text can only come from a decipherment of this letter, most probably with the same key. That link is inferred, not stated (see below). | Groen's page (DBNL) read in full. Alignment: 454 of the 460 key-decoded letters (98.7%) land on the same letter in Groen. A shuffled control lands 161-172 of 460 (35-37%). | high |

N1 rather than N0 follows the orchestrator's test for this brief: N0 only if Groen says the text was deciphered from
this item or from a contemporary decipherment. Groen does not say that for CCCLXXXIX. The outcome for the board is
the same either way. The letter's cipher passage has been in print since 1837, so 5200 is **found-solved**. Our reading
is an independent re-decipherment of page 1, and it agrees with the print.

**Upgrade path to N0.** Any statement that names CCCLXXXIX as deciphered. Candidates: a later Konst- en Letterbode
note, Groen's t.IV "Additions", which covers t.III only (read), or van der Kemp's papers.

### Evidence

1. **Groen prints the cipher passage in clear.** In the DBNL text of t.IV no. CCCLXXXIX (`groe009arch04_01_0004.php`,
   snapshot in `sources/dbnl/groe009arch04_01_0004.html`), p.3 reads: "...a tellement étonné les villes de tous costez,
   que je voy grand changement de courages par tout, tellement que les mieux affectionnez se trouvent fort esbranlez,
   non pas tant pour estre d'autre affection que du passé, comme pour estre saisis d'une frayeur telle, que je crains
   que à la fin je me trouveray seul et abandonné de tous costez, si Dieu miraculeusement n'y pourvoit. Car depuis que
   Malines a esté remise entre les mains des Espagnolz, qui ont saccagé toute la ville l'espace de trois ou quatre
   jours, les guarnisons des autres villes ont esté tellement effrayées..." The print continues to p.6 ("Escrit à Swol,
   ce xviije d'octobre 1572. ... Guillaume de Nassau"). Pages 5-6 therefore also give the text of our unread pp.2-3.
   Groen uses no italics, brackets or "en chiffre" note, and his footnotes (savez; cassation; compte; Yselstain;
   Lauenburg; rapp. à b. esc.) do not mention cipher.
2. **Match rate, an external check on key_1572** (`align/groen_match_5200.py`, run from this folder, reproducible from
   the snapshot). The script aligns the full reading of p.1, clear words and decoded letters, to Groen's text from
   "Monsieur mon frère" to "sinon". It uses global alignment with free end gaps, and treats i/j, u/v and w/x as one.
   - Key-decoded letters (lowercase in `reading_5200_p1.txt`, 460): **454 match, 2 mismatch, 4 unaligned (98.7%)**.
   - Control: the same 460 letters shuffled in place, three seeds: 171, 161 and 172 matches (35-37%).
   - Clear-hand words transcribed by the passes (652 letters): 580 match (89%). Most of the misses are the passes'
     misreadings of the clear hand. For example, L02 "A ZOLLINGEN AVECQ" is Groen's "à solliciter ceux que savez".
     This is a transcription fault in the clear text, not a key fault. It is left for LANE R2 to correct from the image.
   - So key_1572 is confirmed by print on this letter, independently of the J1/J2 spot checks.
3. **How Groen could print it: the key was known to his circle by 1837.** The WVO PDF of sibling 5198 (pp.7-9,
   `images/05198_p7.jpg`-`p9.jpg`) is a reader's letter in the *Algemeene Konst- en Letterbode* (Haarlem), signed
   "a.". It says that t.III nos. CCCLXXXV and CCCLXXXVII contain "veel onverklaard cijferschrift" and that the writer
   "recently found the key" ("Het gelukte mij onlangs den sleutel uit te vinden"). It then prints the multiples-of-3
   table that is our key_1572, and deciphers CCCLXXXV. Groen's t.IV "Additions" (DBNL `_0002.php`, pp.CII-CIII) prints
   "le contenu des passages chiffrés" of t.III pp.503-510 and credits "ce déchiffrement à la sagacité de mon ami Mr
   C.M. van der Kemp". Under p.91 of t.IV he writes: "Nous n'avons pas même trouvé le chiffre, sans quoi nous eussions
   eu recours à l'obligeance de M. v.d. Kemp". Both statements make it likely that Groen printed t.IV's cipher letters,
   5200 among them, from van der Kemp's decipherments with this table. That is inference (grade I), not a statement
   about CCCLXXXIX.

### Families searched

| family | status | what | result |
|---|---|---|---|
| canonical edition (Groen, Archives 1re série t.IV) | searched | DBNL `groe009arch04_01`: TOC, the letter page `_0004` (pp.1-9), front matter `_0001`-`_0003` (preface, Additions); grep for chiffr/cijfer | **prints the full letter in clear**, pp.2-6; decipherment credit to van der Kemp for t.III only |
| holding archive / project (KHA via WVO) | searched (from disk) | WVO record 5200 (read by the check-solved worker: "Grotendeels in cijferschrift.", Bron Groen IV 2-6); WVO 5198 PDF pp.7-9 (Letterbode key note), read by me from `images/` | no solution word on 5200; key published by 1837 in the circle |
| Groen t.V TOC (for the lead below) | searched | DBNL `groe009arch05_01` TOC and pages `_0023`, `_0030`, `_0036`, `_0091` | lead only |
| Japikse, Gachard, Kervyn, WVO Bron beyond Groen, phrase search | not needed | the earliest print was found in the canonical edition, so a later edition cannot lower the class | - |
| JSTOR | not queued | N1 rests on the 1837 print; scholarship cannot change it | - |

Requests: www.dbnl.org 15 (TOC IV, TOC V, 4 front-matter/letter pages of IV, 3 candidate pages of IV, 4 of V; 2 s apart).
No resources.huygens.knaw.nl, Google Books, archive.org or other hosts.

### Did we first-decipher?

No. Groen printed the plaintext of this letter's cipher passage in 1837. Our page-1 reading under the printed 1572 table
is an independent re-decipherment that agrees with it on 98.7% of the decoded letters.

### Safe and unsafe sentences

- Safe: "WVO 5200 (Orange to Jan van Nassau, 18 Oct 1572): page 1 read at grade H under the multiples-of-3 table printed
  in the Algemeene Konst- en Letterbode; the whole letter, cipher passage included, is printed in clear in Groen van
  Prinsterer, Archives 1re série IV (1837), no. CCCLXXXIX, pp.2-6, and our decoded letters agree with that print at
  454 of 460 (N1, found-solved)."
- Unsafe: "5200 read for the first time", "cipher passage recovered", or any wording that implies the plaintext was
  not known.

### Lead for LANE R2: the other five letters (dates and places matched in the Groen TOC and datelines; not classed)

5213 (Delft, 26 Nov 1574) matches **Groen V no. DXXIII** (dateline "De Delft, ce xxvje jour de novembre 1574"). 5221
(Dordrecht, 30 Jul 1575) matches **Groen V no. DLXXIII** ("Escript à Dordrecht, ce pénultiesme jour de juillet 1575").
5207 (Gorinchem, 23 May 1574) was **not located**: IV CDXCII is Dordrecht, 7 May 1574, and CDLXXXIX/CDXC were not
dated by my grep. 5549 (Jan to Orange, 21 Nov 1573) is cited to GPAS, the Supplément, which I did not check.
Before any more passes on 5213 or 5221, open DXXIII and DLXXIII and see whether their cipher passages are printed in
clear. With 5200, 5218 and 5222 all printed in clear, that is the likely outcome.

### Postmortem

- The failure is the one this folder has already had twice. WVO's Bron field cited Groen IV 2-6 from the start. Two
  workers (J1, J2) and about $17 of passes and reading went into a letter whose plaintext is on DBNL. Nobody opened the
  cited page, a single fetch, before the passes began. NOTES flagged it as a "search gap" at check-solved and left it
  open. The LANE N lesson ("open every bundled page before calling a letter open") covers pages bundled in the PDF, not
  a cited print outside it.
- Lesson for the WV/NB briefs: **when WVO's Bron cites a GPA page, fetch that DBNL page and compare before any pass
  starts.** It costs one request.
- Corrections made: NOTES.md status line and a V6 section; status.json row for 5200 (grade, line, novelty). The J2
  section's "This is the first graded, reconciled reading under key_1572" is internal to this repository; it is left
  with a pointer here.

## V1 (LANE V3), 24 September 2026, 12:49-12:55 UTC: WVO 5549, postscript stretch (PS1-PS26)

Verifier V1 (Opus, cap $3, for LANE V3). I did not solve this item and did not decode it again. 5200's classes above
are unchanged.

**Claim under audit** (NOTES.md "J5S result", LANE R3 worker J5S, 24 Sept 2026 12:41 UTC): the postscript stretch
(PS1-PS26, 226 tokens, leaf pp.4-5) reads under Lodewijk's 1574 five-per-letter table, C 163, I 13, M 6, U 44, and
"agrees with Groen's clear print of the postscript (Suppl. pp.146-148)". The question was N0 against N1.

### Verdict

| item | class | prior plaintext | prior decipherment | evidence | confidence |
|---|---|---|---|---|---|
| WVO 5549, Jan van Nassau to William of Orange, Dillenburg, 21 Nov 1573, PS1-PS26 (leaf p.4 second half, p.5) | **N1** | yes: Groen van Prinsterer, *Archives ou correspondance inédite de la maison d'Orange-Nassau*, 1re série, Supplément (Leiden 1847), no. 45, pp.146*-148*, roman type, no cipher marking | Groen does not say it for this letter, and the leaf has no interlinear decipherment. The printed text can only come from a decipherment, but that link is inferred, not stated. | Groen's page (DBNL, on disk as `groen/gpas_lettre45.txt`) read in full for pp.145*-148*, with its footnotes; 23 decoded words and phrases compared, all in Groen's order (table below); leaf pp.4-5 viewed; WVO record (J5I) lists no deciphered copy | high |
| WVO 5549 body, runs 1-61 (Groen pp.141*-146*) | not classed | Groen prints these 537 groups as raw numerals, undeciphered | none located | no reading exists in this repository | -- |

N1 rather than N0 follows the test used for 5200 above (V6): N0 needs Groen, the archive or the leaf to say that
this text was deciphered, or a contemporary decipherment to survive. None does (details below). The body is unread:
it is in a second, unrecovered key, and Groen prints it as raw numbers.

### Evidence

1. **The cited Groen pages print the stretch in clear.** Groen Suppl. no. 45 ("Le Comte Jean de Nassau au Prince
   d'Orange (* ms.). Nouvelles."). The last raw group is "121. 133. 192." on p.146*. Everything after it, through the
   postscript and the close "Datum Dillenburgk, dem 21 Novembris Ao 1573. ... Johann Graff zu Nassaw" on p.148*, is
   ordinary roman German. There is no numeral, italic or "chiffre" note in it. Its footnotes are "Nom propre
   sous-entendu" (p.147*, at "[fussvolck] des") and "gefangenschaft (T. IV. p. 232)" (at "verstrickung"). Groen's own
   square brackets, "[er jener nug]", "[de]", "[fussvolck]" and "[in]", fall where the committed reading has U tokens
   or gaps. That fits an editor working from a decipherment with holes, but he does not say so.
2. **Word comparison, reading_5549_ps.txt against Groen pp.146*-147*.** All of these appear in the same order in both.
   PS2 nit / "nit"; vissen / "wissen"; zogetrad{en} / "zu getrauen"; PS3 grosser die gefa(r) / "grösser die gefar";
   PS5 den remediis / "den remediis"; PS6 hulf / "hülf"; PS7 monsieur de la noue / "Monsieur de la Noue"; PS8 strossi /
   "Strossi"; PS9 uf del. vasser / "uf dem wasser"; PS10 vii oder viii / "vii odder viiic"; PS11 gutter / "gutter";
   PS12 de / "[de]"; PS13 ahn .. der hant (haot) / "ahn der hant"; PS14 gr(en)tzen / "grentzen"; PS16 des / "des";
   PS17 gedanckt / "abgedanckt"; PS19 ligen / "ligen"; PS21 in .. zihe / "[in] zihen"; PS22 uolck / "volck"; PS23 de
   lumbres / "de Lumbres"; PS24 bey / "bey"; PS25 zuleger / "Zuleger". That makes 23 of 23. The first five PS rows sit
   *before* Groen's "PS." line (from "Die menge der geschefft und das wir nit wissen was zu getrauen"). The stretch
   therefore starts in the last paragraph of the body, as the writer's "alhie ... bisz zu ende" says, and is not
   limited to the postscript. The label "postscript stretch" is kept for continuity.
3. **No decipherment on the leaf.** I viewed images p4 (lower half) and p5. None of the cipher runs has an interlinear
   gloss. The marginal note beside the start of the stretch on p4, which J5I left unresolved, is the author's own
   postscript written in the margin: "PS. Nachdem ich mich geeilet hab ich die alte Ziffer ausz vergesz alhie widder
   angefangen und bisz zu ende gebraucht, pluribus intentus minor est ad singula sensus". It matches Groen's "PS." line
   word for word, so it is not a later archival note and not a decipherment. On p.5, between the "139.127..." and
   "67.84.51..." lines, there is faint grey writing. At 150 dpi it looks like show-through from the reverse, not a gloss
   over a run. A higher-resolution image could confirm that; it would not change the class unless it is a gloss.
4. **No deciphered copy in the archive record.** WVO `brief?nr=5549` (fetched by J5I, 24 Sept 2026) names only the
   KHA original, A 11/XIV A/5-18, and GPAS pp.140-148 no. 45 "onv.". Opmerkingen: "Gedeeltelijk in cijferschrift".
   There is no second copy, deciphered copy or minute.
5. **Groen's Supplément front matter.** The Préface (`groe009arch09_01_0001.php`) mentions ciphers only for persons
   "indiquées par des chiffres" in the Granvelle extracts. It says nothing about deciphering no. 45. The Errata page
   (`_0003.php`) has no entry for no. 45. The "Additions" page was not read.

### Principal families

| family | status | what | result |
|---|---|---|---|
| cited edition (WVO Brongegevens GPAS) | searched | Groen Suppl. no. 45 pp.140*-148* in full (on disk), Préface, Errata; DBNL, 3 requests this session | plaintext of the stretch printed in clear, 1847; no statement that it was deciphered |
| leaf | searched | images/05549_p4.jpg, p5.jpg (C1 capture) | no interlinear decipherment; marginal PS is the author's |
| holding archive / WVO record | searched (by J5I, same day, reused) | resources.huygens.knaw.nl/wvo/app/brief?nr=5549 | no deciphered copy listed |
| post-edition literature | searched (by csWV2, same day, reused) | 7 WebSearch queries, solver repositories (check-solved) | nothing on this letter's cipher; WVO literature list PDF, Kronijk and BMHG not read (a gap, irrelevant to N0/N1 because the plaintext is already printed) |
| scholarship, JSTOR | queued | one row in JSTOR-QUEUE.tsv | does not affect N1 |
| Google Books, HathiTrust, IA full text, OpenAlex | not searched | not needed: prior print is established at the cited page, and only a statement of decipherment could move the class to N0 | -- |

### Did we first-decipher?

No. The plaintext of this stretch has been in print since 1847. What this repository adds is a mapping: the leaf
ciphertext of the stretch (J5I's image pass), identified as Lodewijk's 1574 table, and a C-graded reading that agrees
with the print. Groen does not mark the stretch as cipher. Whether this repository is the first to show that it was
cipher on the leaf was not searched as a claim, so it may not be stated as a first.

### Safe and unsafe sentences

- Safe: "WVO 5549 (Jan van Nassau to Orange, Dillenburg, 21 Nov 1573): the enciphered closing stretch (leaf pp.4-5,
  226 tokens) reads under Lodewijk's 1574 five-per-letter table at C 163, I 13, M 6, U 44. Its plaintext is printed
  in clear in Groen van Prinsterer, Archives 1re série, Supplément (1847), no. 45, pp.146*-148*, and the reading agrees
  with that print (N1). The body, runs 1-61, is in another key, is unread, and is printed by Groen as raw numbers."
- Unsafe: "Groen never printed this stretch", "new cipher stretch", "postscript deciphered for the first time", or any
  wording that the stretch's text was unknown.

### Postmortem

- Nothing was over-claimed about novelty: J5S reported the prior print itself. The J5I section heading, "a new cipher
  stretch Groen never printed", is wrong at the plaintext level. Groen printed the text and did not print the
  numerals. It is corrected in place.
- J5I read the p.4 marginal note as possibly "a later archival note quoting" the postscript. It is the author's own
  marginal PS. Corrected in NOTES.md with a pointer here.
- Upgrade path to N0: a statement by Groen elsewhere (the Supplément "Additions", t.IV introduction) or a KHA
  decipherment sheet that names this letter.

## V-TX (LANE TX), 25 September 2026, 07:36-07:50 UTC: WVO 5551, check-solved + reading

Verifier TX-VER5551 (Sonnet, stall alarm $6, session_01JDfSNo5TWtb4qvw3E3Mp3j), a session separate from both
solvers. I did not decode 5551 fresh; I re-derived the committed reading and checked it against the image, and
searched independently to disprove novelty.

**Claim under audit** (NOTES.md "WVO 5551 check-solved (25 Sept 2026)" and "WVO 5551 reading (25 Sept 2026)",
workers TX-WV5551 and TX-WV5551D): WVO briefnr 5551 (Jan/Johann VI van Nassau to Willem van Oranje, Keulen, 17
April 1574, KHAG A 11/XIV A/5-20) is open (six-source check-solved, 25 Sept 2026); its two cipher lines (p3 top)
read 26/32 codes (81%) under Lodewijk van Nassau's 1574 table (`../lodewijk-van-nassau-1573-74/key.tsv`),
`reading_5551.txt` giving "DER [null] KONIG ... UINGT VAN POLEN [?] WILL" / "OFFENTLI[?] ... VFF I [?] [?] ES
[?] ... [?] [?]", grades C23 I2 M1 U6, no H, no S.

### 1. Re-derivation and image check (rule 7)

`python3 tools/decode_key.py ciphers/jan-van-nassau-1572-75 --config ciphers/jan-van-nassau-1572-75/decode_5551.json --check`
exits 0 and reports "tokens 32: C 23, I 2, M 1, U 6" against the committed `reading_5551.txt` -- matches the
NOTES.md counts exactly, confirmed a second time from a fresh instance of this tool run (not the solver's own
run).

Viewed `images/05551_p3.jpg` (the committed 150dpi original; the worker's 300dpi re-render was scratch, not on
disk) at 3-8x crop zoom on both lines, digit by digit, without looking at the committed transcription first for
the codes I spot-checked. Confirmed by eye, matching `ciphertext_5551.tsv` exactly: L1 `77.81.21.121.106.6.2.
101.92.136` then a clear word then `11.7.111.83.4.145`; L2 `8.88.89.84.5.31.112.103` then a clear word then
`104` then `146.127.85.29.140` then a clear word then `137.126`. The anomalous code `136` (keyed M, "uingt" =
French "vingt") is a genuine "1‧3‧6" in the hand -- the same looped-tail "6" the scribe uses in `106` two codes
earlier -- not a misread of a different digit; nothing in the image suggests `130`, `138` or `186`. I did not
re-verify all 32 codes myself (the two independent blind passes already agree 32/32, re-verified by their own
authors at 4-8x zoom, and a third, fresh-instance re-derivation reproduced the identical reading -- three
independent transcriptions is enough that a spot check, not a full re-transcription, is the proportionate
verifier check here). I also confirmed structurally what TX-WV5551's eye-check reported: immediately below the
two cipher lines, the same page continues in plain German ("Die conditiones und ...") with no more cipher on
p3 -- the "Twee regels in cijferschrift" claim holds; the cipher really is confined to two lines.

**Is the German sense or forced?** L1's spelled-out stretch, `D-E-R [null] K-O-N-I-G ... P-O-L-E-N ... WILL`
("DER KÖNIG ... POLEN ... WILL") is real, unforced German syntax -- "der König [von/der] Polen will..." ("the
King [of] Poland wants/will...") is a plausible clause opening, and the doubled-F letter-block in L2's
`O-F-F-E-N-T-L-I` (the codes 88 and 89 landing on the key's own predicted 86-90=f block) is an independent
structural check that the table holds on this new letter, not merely 8 lucky letters. I agree with the solver
that this is real, not noise: a shuffled-code control would not by chance produce "DER KONIG" and "OFFENTLI"
with no wrong letters in either 8-letter run. **Is "uingt" a mistranscription?** No -- the digit is correctly
read as 136 (confirmed above); the mismatch is that the *key's own* M-graded row 136 was recovered from
Lodewijk's French correspondence ("vingt" = twenty) and does not make German sense at this position ("der
könig zwanzig van polen" is not a sentence). This is a genuine anomaly in applying a French-derived
nomenclator row to a German letter, correctly left unresolved by the solver, not a reading error. The
"Henri de Valois, elected King of Poland" gloss in NOTES.md is explicitly flagged there as unconfirmed
speculation, not a claim; I did not find anything in this pass's search (below) that confirms or refutes it,
so it should stay exactly that hedged.

### 2. Independent novelty search

Building on TX-WV5551's and TX-WV5551D's own searches (WVO record, Groen IV/V/Supplement items 45-57, DECODE,
both solver repositories, general WebSearch, Gachard III full-text via be-api -- not repeated here except
where noted), I searched:

1. **Groen Supplement, full table of contents** (`www.dbnl.org/tekst/groe009arch09_01/index.php`, read directly,
   not by phrase): items 15 and 42-78 read by title and date marker. Confirms TX-WV5551D's neighbourhood check
   rather than just extending it -- items 43/44/48/53 are all Countess Julienne (not Jean), 47/49 are Louis (not
   Jean, and not to the Prince in 49's case), 45/46 are Jean-to-Prince "Nouvelles" but both fall before the
   `[1574]` marker at item 47 (so both are 1573, matching TX-WV5551's dating), 50 is 31 May 1574 (Christoph of
   *Mecklenburg*, not Wurttemberg), 52 is a joint Berghes+Nassau letter with an unrelated subject line ("Ils
   désirent pouvoir un jour le servir"). **No entry in the full TOC between items 15 and 78 is dated 17 April
   1574, from Cologne, or matches 5551's Mookerheide-report content.** This closes the search-gap style risk
   the Dupuy 468 lesson warns about (a neighbourhood read missing an out-of-sequence entry) with a full-index
   read instead.
2. **Google Books** (3 queries, `country=US` + key): `"Johann von Nassau" Mookerheide 1574 Köln` (6 hits, all
   an 1868 general encyclopedia, irrelevant); `Glawischnig Nassau-Dillenburg Johann Mookerheide 1574` (3 hits:
   *Nassauische Biographie* 1992, *BMGN* 1984, *Graf Johann VII* 1958 -- none opened full-text this pass, a
   gap, not a negative, since none is confirmed to print this letter); `"17 april 1574" Nassau Keulen
   cijferschrift` (0 hits).
3. **OpenAlex** (2 queries, keyed): `Johann von Nassau Mookerheide 1574 cijferschrift` (0 results);
   `Jan van Nassau Willem van Oranje Keulen 1574 brief` (14 results, none about this letter or its cipher --
   titles on Dutch Revolt propaganda, reconciliation attempts, a Latin-school history, a language guide, Neo-
   Latin drama).
4. **Semantic Scholar** (1 query, keyed): `Johann Nassau Mookerheide 1574 cipher letter` (0 results).
5. **Japikse's Correspondentie van Willem den Eerste** (named in my brief as a family to cover): confirmed via
   WebSearch that it exists digitised on Huygens retroboeken infrastructure
   (`resources.huygens.knaw.nl/retroboeken/willem_den_eerste/`), the same platform as this repo's Heinsius/De
   Witt/Oldenbarnevelt tools already cover, but this specific book is not yet in this repo's list of known
   accessor ids and its TOC page did not render usable content via plain curl (a JS-rendered listing, unlike
   the books this repo's tools already handle). **Not searched this pass -- a genuine gap**, flagged for a
   future session with the accessor id worked out (or the browser tool), not folded into the negative above.
   Kervyn de Lettenhove's editions and a Jacobi dissertation (also named in my brief) were checked only by the
   Google Books/WebSearch queries above, not opened directly -- also a gap, not a negative.
6. **JSTOR**: not reachable from the cloud; one row queued (`JSTOR-QUEUE.tsv`, "Johann VI" OR "Jean de Nassau"
   AND Mookerheide/Mookerheyde AND 1574 AND Koln/Cologne/Keulen), per the outreach gate -- a queued row never
   blocks a class on its own (CLAUDE.md rule 10).

Requests this pass: www.dbnl.org 2 (Supplement TOC, one retry on a bad path corrected), www.googleapis.com 3,
api.openalex.org 2, api.semanticscholar.org 1, WebSearch 2. No DECODE, no credentials beyond the three API
keys (presence tested with `test -n`, never printed), no subagents, no image or PDF refetches (used the
already-committed `images/05551_p3.jpg`).

### Verdict

| item | class | prior plaintext | prior decipherment | key source | evidence | confidence |
|---|---|---|---|---|---|---|
| WVO 5551 (Jan/Johann VI van Nassau to Willem van Oranje, Keulen, 17 Apr 1574), the two cipher lines, p3 top | **N3** | no, not located | no, not located | `ours` (Lodewijk van Nassau's 1574 table, `../lodewijk-van-nassau-1573-74/key.tsv`, rebuilt in this repo by aligning WVO 4613/4615's ciphertext to their own imaged contemporary plaintext decipherment -- confirmed directly from that folder's NOTES.md "Source" section) | WVO's own Brongegevens field carries no GPA/GPAS/JC edition code at all for this letter (unlike this circle's print-bundled siblings); full TOC reads of Groen IV, V and the Supplement (items 15, 42-78) find no matching entry; DECODE, both solver repositories and general WebSearch (TX-WV5551) plus Google Books, OpenAlex and Semantic Scholar (this pass) are all negative; JSTOR queued, not yet answered | high on the negative as searched; Japikse, Kervyn de Lettenhove and a Jacobi dissertation remain unopened (gap, not negative) |

N3, not N4: the principal cited edition for this whole correspondence circle (Groen) is now covered exhaustively
(full TOC, not a neighbourhood read), and DECODE/solver repositories/general web/Google Books/OpenAlex/S2 are all
negative -- but Japikse's Correspondentie, Kervyn de Lettenhove and the Jacobi/Glawischnig secondary literature,
all named in my brief as families to cover, were not opened directly this pass (Japikse's retroboeken page did
not render by curl; the others were only keyword-searched). A second adversarial audit should close that gap,
per the Outreach rule, before any claim above N1 goes out.

### Did we first-decipher?

Unknown, and not claimed either way. What is established: no prior print or decipherment of these two lines was
located after the search above. The key that reads 81% of the two lines is `ours` -- rebuilt in this repository
from a sibling letter's own imaged period decipherment, not a published key and not cryptanalysis from nothing.
An `ours` key at N3 is the nearest honest equivalent of a first (CLAUDE.md rule 10); it may not be called "first".

### Safe and unsafe sentences

- Safe: "WVO 5551 (Jan/Johann VI van Nassau to Willem van Oranje, Keulen, 17 April 1574): the letter's two
  cipher lines (p3 top) read 26 of 32 codes under a table this repository rebuilt from a sibling letter's own
  period decipherment (WVO 4613/4615), giving recognisable German ('DER KÖNIG ... VON POLEN ... WILL',
  'ÖFFENTLI[CH] ... ES'); no prior plaintext or decipherment of these lines has been located after a search of
  Groen's edition (full index), WVO's own catalogue, DECODE, the two solver repositories, general web search,
  Google Books, OpenAlex and Semantic Scholar (N3); key source ours; the reading is partial (6 of 32 codes
  unkeyed, both lines cut off by paper loss) and one code (136, 'uingt') does not yet make German sense in
  context."
- Unsafe: "first decipherment", "previously unread", "newly recovered", "unpublished plaintext", or any wording
  that the letter's cipher, the King-of-Poland reference, or its identification as Henri de Valois was
  established, known, or ruled out -- none of those is settled here.

### Corrections to the target's files

None needed. NOTES.md's "WVO 5551 check-solved" and "WVO 5551 reading" sections already use rule-10-compliant
language throughout ("open", "partial", grades stated, the Henri de Valois reading flagged as unconfirmed
speculation, "recovery" not "cryptanalysis", no "first"/"unpublished"/"never printed" wording found anywhere in
either section). No over-claim to correct.

### Postmortem

No process failure to report. The one improvable step: TX-WV5551's own search closed two gaps by re-fetching two
Groen Supplement pages after they failed twice (good practice), but its Groen check itself was a chronological
neighbourhood read (items 45-57 by date), which the Dupuy 468 lesson flags as a pattern that can miss an
out-of-sequence entry; a full-TOC read (done here) costs one extra request and removes that residual risk. Worth
folding into `.claude/briefs/check-solved.md`'s WVO paragraph: for a Groen-covered correspondence circle, read
the volume's full TOC once, not just the surrounding date window.

## V-TX2 second audit (LANE TX), 25 September 2026, 08:15-09:05 UTC: WVO 5551, adversarial second pass

Verifier TX-AUD5551 (Sonnet, stall alarm $6, session id per system prompt), a session separate from both solvers
and from V-TX. Per `.claude/briefs/runs/2026-09-25-lane-tx-aud5551.md`: open, not keyword-search, the five
edition families V-TX only keyword-searched (Japikse; Kervyn de Lettenhove; Jacobi/Glawischnig; Gachard III
pp.90-100; Blok/Muller and the Nassau-Dillenburg archive editions), plus a fresh open-index/Google Books pass.
I did not decode 5551 and did not re-derive the reading (V-TX's re-derivation and image check stand; nothing
here touches them).

**Claim under audit** (V-TX): WVO 5551's two cipher lines, N3, key ours, safe sentence as V-TX wrote it.

### (a) Japikse, *Correspondentie van Willem den Eerste* — opened, does not cover 1574 at all

Fetched the retroboeken app directly, not by phrase search: `resources.huygens.knaw.nl/retroboeken/willem_den_eerste/`
(TOC), its `search_in_text` accessor form (the same accessor pattern `sources/huygens/NOTES.md` documents for
Heinsius/De Witt/Oldenbarnevelt), a live search (`search_term:ustring:utf-8=Mokerheyde` and `=Mookerheide`, both
"geen resultaten gevonden"), and — the decisive check — `retroboeken/willem_den_eerste/pages.json?source=1`
(the book's actual page list) and `?source=2` (503, no second source exists). **Source 1 is 450 index rows
ending at printed page 418**; the title page (`WillemDenEerste_voorwerk_i.jpg`/`.html`) reads "CORRESPONDENTIE
VAN WILLEM DEN EERSTE PRINS VAN ORANJE". A WebSearch cross-check (American Historical Review review, 1935)
confirms this is Deel I, 1551-1561, 417pp., and that "the project ultimately only produced this first part" —
Japikse's edition never reached 1574. **This family cannot contain 5551 under any search term; it is not a gap,
it is out of range.** Corrects V-TX's framing ("not yet integrated in this repo") — the edition is reachable
and was opened, and simply stops 13 years before this letter.

### (b) Kervyn de Lettenhove — opened both named works, full text read, negative

*Relations politiques des Pays-Bas et de l'Angleterre* VII (1888, "Gouvernement de Requesens", 29 Nov 1573 - 25
Oct 1575 — the volume covering our date range, identified via WebSearch and confirmed by its own front matter).
Fetched the full OCR text directly (`archive.org/download/relationspolitiq07nethuoft/..._djvu.txt`, 1968705
bytes, not a be-api snippet search) and grepped it in full, then read every hit in context. Zero hits for
Mokerheyde/Mookerheide/Mokerheyd in any spelling (this volume's index of English-Netherlands diplomatic
correspondence never mentions the battle by name, even though the volume's date range covers it — it is about
English/Requesens relations, not the Nassau brothers). 11 "Nassau" hits are all Louis de Nassau (the volume's
one glancing mention of "les comtes Loys et Jehan de Nassau, frères" as killed at Mookerheide is a third-party
rumour report to Philip II, not a letter from or to Jan). The one 17 [month] 1574 Cologne letter in this volume
(no. MMDCCLXXVI, "Le seigneur de Lumbres au comte de Leicester", Cologne, **17 juillet** 1574 — different month,
different correspondents entirely) is a coincidental date/place match a phrase search on "Cologne 1574" could
mislead on; opening the actual letter head ruled it out.

*Les Huguenots et les Gueux* III (1884, `leshuguenotsetle03kerv`, confirmed to be the right volume: its own
Chapitre IV is titled "Le combat de Mookerheyde (novembre 1573 — novembre 1574)", exactly our window). Same
method: full djvu text fetched and grepped (1235756 bytes), not a snippet search. 19 "Mook" hits read in
context: this chapter narrates the battle and its aftermath at length (citing Mondoucet's despatches, Groen)
but never cites a letter from Jean de Nassau to the Prince dated 17 April/Cologne, and never quotes our cipher
lines' content. One hit is a different ambassador's letter *to* Jean de Nassau the day after the battle
("le lendemain de la bataille de Mookerheyde, il écrivait à Jean de Nassau pour lui promettre une prompte
revanche") — incoming, not our outgoing letter. A second hit is worth flagging for the record though it is not
about 5551: a footnote on Groen IV p.91 notes "il y a dans cette lettre une lacune représentée par un passage en
chiffres" and that the House of Orange archivist General Van Mansfeld tried and failed to find the key —
a *different*, older unsolved cipher passage in this same family archive (Groen IV p.91, dated context April
1573), not 5551 (which has no GPA citation at all, per TX-WV5551). Both works: negative, opened and read in
full, not keyword-searched.

### (c) Jacobi and Glawischnig — Glawischnig is the most important finding of this pass

**Glawischnig cites this exact letter.** Google Books full-text search inside Rolf Glawischnig, *Niederlande,
Kalvinismus und Reichsgrafenstand 1559-1584. Nassau-Dillenburg unter Graf Johann VI* (Marburg, 1973 — snippet
view only, not full view; ids `DhMBAAAAMAAJ`/`lbMrAQAAIAAJ`/`Z9vuAAAAIAAJ`, confirmed the same book via
`api.openalex.org` W... record) returned, across four overlapping phrase queries that each independently
confirmed the same footnote text: **"17.4.1574 Köln und 21.4. Wesel, JvN an WvO. KHA A XI 5, auch STAMa 4f
Nld. 165."** — a source-note entry naming exactly our correspondents (Jan van Nassau to Willem van Oranje),
exactly our date and place (17 April 1574, Köln), in a chronological run of source citations for the days
after Mookerheide (the same footnote continues: "7.5.1574 Dordrecht, WvO an JvN. GvP CDXCII. (Mai 1574)
Heidelberg, (JvN) an (WvO). STAW 170 III 1574. 19.5.1574 Köln, Stenzel von Namslo an JvN. KHA 897. 31.5.1574
Dill., JvN an WvO..."). The body-text snippet this footnote supports reads: "Johann erfuhr von der Niederlage
in Köln. Die ersten Nachrichten, die er erhielt, waren widersprüchlich. Die Niederlage war gewiß, ungewiß waren
aber das Schicksal seiner Brüder und die Zahl der geretteten Truppen..." ("Johann learned of the defeat in
Cologne. The first news he received was contradictory. The defeat was certain, but the fate of his brothers and
the number of troops saved was uncertain...") — this reads as a paraphrase of the letter's *clear* German
(pp.1-2 of the leaf, which WVO's own Inhoud already summarises as exactly this report) rather than of the two
ciphered lines, whose legible content ("DER KÖNIG ... VON POLEN ... WILL", "ÖFFENTLI[CH] ... ES") does not match
this sentence.

**What this does and does not establish, and why the class does not move.** It establishes that the letter
itself — as a dated, located archival object with a summarised content — is known to and cited by Glawischnig's
1973 monograph, the single most specific piece of secondary literature on this correspondent and this exact
period. It does *not* establish that the plaintext of the two ciphered lines is published anywhere: four further
phrase queries for this book combined with Ziffer/chiffriert/verschlüsselt/"König von Polen" all returned zero
matches (Google Books snippet-view search, a real negative signal but a weak one — snippet indexing is known in
this repository to miss real co-occurrences, and I have no full-view or library access to read Glawischnig's own
pages around this footnote directly). **This is a genuine, unresolved gap, not a negative**, and it is the
single most important next step before this target goes any further: (1) get full-text or library access to
Glawischnig 1973 around the footnote citing "KHA A XI 5" (its number is not identified from snippets — likely
in the chapter on 1574, footnote ~70-75 by the numbering visible in the snippets); (2) the footnote names a
**second copy of this letter cluster, `STAMa 4f Nld. 165`** (Staatsarchiv Marburg, Bestand 4f Niederlande, item
165) — not on file anywhere else in this repository, not checked this pass (no online finding aid located
within budget), and a real candidate for a period copy, marginal note, or even a period decipherment distinct
from WVO's KHAG original. Both are flagged for a future pass, not chased to ground here. A caution on the
shelfmark: Glawischnig's "KHA A XI 5" is not a character-for-character match to WVO's own "KHAG A 11/XIV A/5-20"
for 5551 — plausibly the same fonds/box under an older citation convention (A 11 = A XI), possibly folded
together with the companion 21 April Wesel letter under one citation, but this is not confirmed and should not
be assumed; a future pass should check whether Glawischnig's own bibliography or archive visit notes resolve it.

**Jacobi**, named in my brief alongside Glawischnig, could not be identified as a specific citable work.
WebSearch and three Google Books queries for "Jacobi" + Nassau/Dillenburg/Mookerheide/Geschichte returned only
ambiguous or unrelated hits: a "Jacobi, Wiesbaden 1913" appears in bibliographies of Nassau regional-history
volumes (`Männer aus und in Nassau`, 1961; `Neugliederung...Mittelrheingebiet`, 1965) without a recoverable
title, and a "Jacobi: Geographie des Reg.-Bez. Wiesbaden" (1899/1907) is a geography text, not a correspondence
edition. Not opened — flagged as unresolved identification, not a search failure to be counted as a negative.

### (d) Gachard III, pp.90-100 — opened page by page, and the volume has no letter in this window at all

Fetched `correspondancede03will_djvu.txt` in full (1156567 bytes) and built a page map from the volume's own
"— N —" running-head page markers (349 recovered), confirming the pp.90-100 range TX-WV5551D's be-api snippet
search could not properly page-locate. **Read pp.83-101 in full, letter by letter**: this stretch is four
William-to-Julian-Romero prisoner-exchange letters (DXXXVII-DXXXIX, 8-10 Nov 1573) and a long William-to-Marnix
letter (DXL, 28 Nov 1573, running pp.88-93) — all November 1573, not April 1574. Then, decisively, **the
volume's own printed table of contents** (read directly, lines ~21260-21300 of the OCR text) shows the volume
jumps from DXLII (11 January 1574, p.95) straight to **DXLIII, "Le prince d'Orange au colonel Mondragon. De
Bommel, le 23 avril 1574", p.96** — there is no letter dated between 11 January and 23 April 1574 anywhere in
this volume, and DXLIII itself is to a Spanish colonel about a military matter, not to Jean de Nassau. **The
entire Mookerheide-aftermath window (14 April onward) is a real gap in this volume's own letter sequence.**
This closes (d) as a hard negative, page-by-page as the brief asked, not by full-text search (be-api's search
in TX-WV5551D's pass could not have found this either way, since there is genuinely nothing there to find).

### (e) Blok/Muller and the Nassau-Dillenburg archive editions — not resolved to a specific edition, flagged

Google Books queries for "Blok" and "Muller" combined with Willem van Oranje/Jan van Nassau/1574 surfaced only
secondary citations (P.J. Blok cited in Ruth Putnam's 1897 *Willem de Zwijger*; P.L. Muller's *Stukken
betreffende de zending van Dirk van Hille*, an unrelated 1574 mission) — neither is a documentary edition of
this correspondence circle that could be opened and checked page by page within this pass's budget. One
concrete, real edition surfaced instead and is worth recording precisely because it does *not* apply: **"De
correspondentie tussen Willem van Oranje en Jan van Nassau, 1578-1584"** (1984, 134 letters, RGP-style) is an
actual printed edition of this same two brothers' correspondence — but its own title states 1578-1584, four
years after 5551 (1574), so it cannot contain it; not opened (out of date range, confirmed from its own
publisher's description). Arnoldi's *Geschichte der Oranien-Nassauischen Länder* (Google Books ids located) and
a direct Arcinsys Hessen search for HStA Wiesbaden Bestand 170 III (WebSearch only, no hit for this exact date/
item; the archive's own search interface was not queried directly with its date-range tools, a gap) were both
named in my brief and both remain unopened — genuine gaps, not negatives, and lower priority than the
Glawischnig/STAMa lead above, which is concrete and dated.

### Open-index and Google Books pass

OpenAlex (keyed, 1 query: "Glawischnig Nassau-Dillenburg Johann VI", 7 results, all either Glawischnig's own
book/its review or unrelated Nassau items — nothing new). Semantic Scholar: 429 twice (keyed), stopped after one
retry per the good-citizen rule — not searched this pass, a gap. CrossRef (1 query): 5 results, one interesting
but unconfirmed tangent ("The prince of Orange to Count John of Nassau, Dordrecht, 7 May 1574", a different date
than 5551 or Gachard's DXLIV/DXLV Mondragon letters at the same pages — not chased further, flagged only). HAL
(1 query): 0 hits. Persée: WebSearch site-restricted, no relevant hits. Google Books: 20 queries in total this
pass (Glawischnig identification and footnote reconstruction, Jacobi, Blok/Muller, "König von Polen" +
Mookerheide/Nassau, Ziffer/chiffriert/verschlüsselt negatives) — see (c) above for the one substantive result.
One incidental, unchased lead worth recording: a query for the decoded German turned up Bezold's *Briefe des
Pfalzgrafen Johann Casimir* (1882), whose footnote on the 1574 Imperial-succession/Poland question ends "...zu
Polen dem König bleibe... 2) Johann von Nassau" right at the point the snippet cuts off — plausibly relevant to
the solver's own flagged (and explicitly unconfirmed) Henri-de-Valois-as-King-of-Poland reading of L1, but not
opened or confirmed this pass; flagged, not claimed.

### Verdict

| item | class | prior plaintext | prior decipherment | key source | evidence | confidence |
|---|---|---|---|---|---|---|
| WVO 5551 (Jan/Johann VI van Nassau to Willem van Oranje, Keulen, 17 Apr 1574), the two cipher lines, p3 top | **N3 (unchanged)** | no plaintext of the two ciphered lines located | no | `ours` (as V-TX; unchanged) | Japikse (opened, out of date range), Kervyn de Lettenhove x2 (opened, full text, negative), Gachard III (opened, page-by-page, a real gap in the volume's own sequence) all now closed as genuine negatives rather than unopened gaps; Glawischnig 1973 is confirmed (via Google Books) to cite this exact letter by date/place/correspondents/shelfmark for its *clear* content, but no evidence located that he discusses or prints the ciphered lines specifically — a live, unresolved lead, not a negative; Jacobi and Blok/Muller not resolved to specific openable editions; a second copy at STAMa 4f Nld. 165 (Marburg) is newly identified and unchecked | high on the five closed families; the Glawischnig/STAMa lead is the reason this cannot go to N4 yet |

**N3 stays, explicitly not N4.** Rule 10's N4 requires "the principal editions, catalogues and project pages
covered" — five of V-TX's five named families are now genuinely opened rather than keyword-searched, and three
close clean, but the fourth (Glawischnig) surfaced a concrete, dated citation of this very letter in exactly the
kind of specialist secondary literature N4 is meant to require checking, and it is not yet read past a search
snippet. Moving to N4 before that citation and the STAMa copy are chased to ground would repeat the Eckert 1864
lesson (declaring victory on an edition search that stopped one step short of the source that actually matters).

### Did we first-decipher?

Unchanged from V-TX: unknown, not claimed either way. The new finding narrows what "unknown" covers — the
letter's existence and general content are not obscure (Glawischnig cites it in 1973), but the specific
plaintext of the two ciphered lines is still not located anywhere in print after this pass's search.

### Safe and unsafe sentences

- Safe: V-TX's safe sentence stands, with one addition: "...no prior plaintext or decipherment of these lines
  has been located after a search of Groen's edition (full index), WVO's own catalogue, DECODE, the two solver
  repositories, general web search, Google Books, OpenAlex and Semantic Scholar (N3); key source ours. Rolf
  Glawischnig's 1973 study of Johann VI of Nassau-Dillenburg cites a letter from Jan van Nassau to Willem van
  Oranje of this same date and place (17 April 1574, Köln) as a source for its general content, but no evidence
  has been found that it discusses or prints the ciphered passage itself; a second copy of this letter cluster
  at the Staatsarchiv Marburg (4f Nld. 165) has not yet been checked."
- Unsafe: everything V-TX already listed, plus: "identified in Glawischnig" or any wording implying the cipher
  passage's content, rather than the letter's existence, is confirmed in secondary literature — that is
  precisely the unresolved question this section flags, not a finding.

### Corrections to the target's files

None needed to NOTES.md (V-TX already found none, and this pass adds no new claim to correct). V-TX's own
AUDIT.md text is not corrected in place (per COMMON scope, only the sections named); this section supersedes its
"N3 not N4" reasoning with the more specific reason above (Glawischnig/STAMa, not Japikse/Kervyn/Jacobi/Gachard,
which are now closed) and should be read together with it, not in place of it.

### Postmortem

No process failure in V-TX's own work to report — its five flagged families were genuine, honestly-labelled
gaps ("only keyword-searched"), and opening them was exactly the right next step, which is what this brief
asked for. The lesson worth keeping: three of five "named edition, not yet opened" flags turned out to be true
negatives cheaply closed by opening the primary source directly (a page list, a full-text fetch, an index read)
rather than by another round of phrase search — the same method V6/V1 used for 5200/5549 elsewhere in this
folder. The fourth, Glawischnig, is the reminder that a monograph specifically about the correspondent in
question is worth more than a general edition, and a snippet-view hit that confirms a citation exists is not
the same as reading what the citation supports — the next session with library or full-text access to
Glawischnig 1973 should read the actual footnote and page before this target moves past N3.

Requests this pass: resources.huygens.knaw.nl 9 (TOC, accessor forms x2, 2 live searches, pages.json x2, title
page; >=2s apart), archive.org 7 (2 advancedsearch, 3 djvu downloads, 1 redirect retry, be-api.us.archive.org 4
fts queries counted separately), be-api.us.archive.org 4, www.googleapis.com 20 (>=1.5s apart), api.openalex.org
1, api.semanticscholar.org 2 (429 x2, stopped per good-citizen rule after one retry), api.crossref.org 1,
api.archives-ouvertes.fr 1, WebSearch 7. No DECODE, no credentials beyond the two API keys (test -n only), no
subagents (both available slots unused — every step here needed direct source reading, not a parallel pass),
no image or PDF refetches.

## Second-opinion claims not confirmed (V6-SOCHK, 25 Sept 2026)

From `second-opinions/chatgpt-2026-09-25-5551.md` (PR 12, SO-NASSAU-5551); full table in
`second-opinions/CHECK-SO-NASSAU-5551.md`. Class line above untouched: WVO 5551 stays N3.
- The Glawischnig snippet (17 Apr 1574, KHA A XI 5, STAMa 4f Nld. 165): repository-reported (V-TX2), not re-confirmed
  this pass; one Google Books phrase query returned 0 items (not a negative for a snippet-view book).
Confirmed leads for the search log: Press, *BMGN* 99 (1984), p.691 and n.44, points to Glawischnig pp.105-111 for
the 1574 campaign (the page range to read first); Janssen, *BMGN* 90 (1975), pp.293-295 (review; no cipher text);
BnF Français 3961 items 1-3 (29 Mar, 6 Apr, 18 Jun 1574, catalogue level). Correction for NOTES.md (not applied
here): the Christoph killed at Mookerheide is Pfalzgraf Christoph, son of Friedrich III (Press p.691), not "Christoph
of Wurttemberg" (the WVO summary's wording, NOTES.md lines 782-784, 806, 991).
