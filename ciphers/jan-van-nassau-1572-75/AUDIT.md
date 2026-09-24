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
