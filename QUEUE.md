# Queue of targets to attempt

Scout run of 19 Sept 2026 (first real run; stages of `.claude/workflows/scout.js` executed as ordinary agent work: five
harvesters, one filter, batched scorers, this file). Harvested from the two solver repositories
(github.com/dbourdeau/cyphersolver, github.com/aaymeloglu/unsolved-ciphers, both cloned 19 Sept 2026), the Cryptiana
snapshot in `sources/cryptiana/` and this repository's CATALOG.md and LANDSCAPE.md, the community blogs and
forums, and the archive catalogues. Re-run weekly.

Reader profile: English only, no institutional archive access, can send copy requests and pay small fees, works
with AI agents for transcription and solving.

Score = language_fit x3 + material x2 + key_lead x3 + size x2 + competition x2 + weight (max 39). Axes: language_fit
3 = English plaintext, 1 = other language readable with AI help, 0 = unknown; material 3 = images or full
transcription online free, 2 = printed figures, 1 = login needed, 0 = nothing online; key_lead 3 = key or
decipherment located, 2 = sibling with decipherment, 1 = design known, 0 = nothing; size 3 = enough text or a key
for a checkable reading, 0 = below unicity with no key lead; competition 3 = on nobody's tracker, 1 = open on a
solver-repository tracker, 0 = active work reported; weight = historical interest, 3 = decision of state.

Per-axis scores and each scorer's rationale are in `QUEUE-scores.json` beside this file. A row whose next step
is `blocked` is open but waits on something a person must do; rows marked closed-negative by a solver repository
are kept, as CLAUDE.md rule 3 says a negative without our own matched control is not a closure for us.

## Tier A: start now

| Rank | Target | Year | Lang | Next step | Detail | Total | Sources |
|---|---|---|---|---|---|---|---|
| 1 | Thomas T. Eckert Papers, US Military Telegraph: ledgers of telegrams sent 'still in code', 1862-67 (Huntington mssEC 1-76) | 1862-1867 | en | transcription | On hdl.huntington.org collection p16003coll11 pull one 1862 'telegrams sent' ledger (mssEC 1) and its Cipher Book (EC 36) and read ten messages against the code book. | 38 | archives |
| 2 | Charles Whitworth (Moscow) to Harley, partly undeciphered despatches and an undeciphered duplicate, 1707-08 (TNA SP 91/5) | 1707-1708 | en | archive-request | Order TNA copies of SP 91/5 items 108, 163, 294, 298 and 300 (Discovery search 'undeciphered', SP 91/5) to recover the key from the 294/298 pair. | 34 | archives |
| 3 | [Intercepted royalist letters to Charles I and 'My Lord', 13 and 21 May 1646 (BL Add MS 72438 ff.9-10)](ciphers/intercepted-royalist-1646/) | 1646 | en | archive-request | Order BL copies of Add MS 72438 f.11 and check Bodleian Tanner MSS 59-60 and TNA SP 16/514 for the contemporary decipher of f.10. | 34 | aymeloglu, tomokiyo |
| 4 | Wellington to General Maitland, Villa Castin, 2 Sept 1812 (Peninsular War dictionary code and strip cipher) | 1808-1814 | en | transcription | Save the lot 1184 images from live.spink.com before the 23 Sept 2026 sale and transcribe every 5b429-style group to identify the pocket-dictionary edition. | 34 | aymeloglu, tomokiyo |
| 5 | [Charles II to the Duke of Hamilton, 6 Aug - 27 Sept 1650 (four letters, passages in cipher)](ciphers/hamilton-1650/) | 1650 | en | archive-request | Copy request for NRS GD406/1/2197 (5 cipher-key items) and GD406/1/10573-10576 sent 19 Sept 2026; wait for the reply, then apply the sheet to the 102 groups. | 33 | aymeloglu, bourdeau, tomokiyo |
| 6 | Charles I to William Boswell, 1628 (TNA SP 106/5, DECODE R413) | 1628; 1758 | en | cryptanalysis | With a DECODE login, download R413 (TNA SP 106/5) with its attached key and cryptanalysis files and apply the key to the ten lines; compare against the SP 84/157 alphabet in cyphersolver boswell/. | 30 | archives, aymeloglu, bourdeau |
| 7 | Cornwallis Papers, American campaign: Rawdon, Craig, Tarleton, Balfour and others to Cornwallis, 1780-81 (TNA PRO 30/11) | 1780-1781 | en | search-print | Check Saberton, The Cornwallis Papers (2010) for the six items Discovery marks undeciphered (PRO 30/11/6/23-26, 3/207-209, 69/18-24, 68/32-35) against his printed Common, Balfour and Ninety Six cipher keys. | 30 | archives |
| 8 | Other Add MS 4136 correspondents to Cecil, 1559-67: Henry Percy, Thomas Smith (7), Norreys, Middelmore, Lomer, 'Amiral to D. Angle' (DECODE R9235-R9256) | 1559 | en | transcription | Register on DECODE (free), download key records R9260, R9261, R9262 and pages R9235-R9256, and apply Tomokiyo's Throckmorton and Smith alphabets line by line. | 30 | bourdeau |
| 9 | Scottish state letters of the Moray regency, Jan 1568 and 26 July 1569 to the 'Lorde Regent' (BL Add MS 33531 ff.73-74, 79-80; DECODE R8347-R8348) | 1568; 1569 | en | search-print | Check Labanoff, Lettres de Marie Stuart ii p.175 and CSP Scotland ii no. 1103 (Bain) for printed decipherments of ff.73-74 and ff.79-80 before any DECODE work. | 30 | aymeloglu, bourdeau |
| 10 | Sir Nicholas Throckmorton (Paris, Edinburgh) to Cecil, the Queen and the Council, 1559-63, 20 ciphertexts (BL Add MS 4136, DECODE R9220-R9255, R3026) | 1559-1560 | en | search-print | Match the 20 DECODE record dates (R9220-R9234, R9242-R9245, R9255) against CSP Foreign 1558-63 and Forbes 1740-41 to list which despatches are printed from deciphered SP 70 copies. | 30 | archives, bourdeau |
| 11 | Sir Ralph Sadler (Edinburgh) to Henry VIII, 22 April 1543 (BL Add MS 32650 ff.214-216, DECODE R4924) | 1543 | en | search-print | Read Clifford, State Papers and Letters of Sir Ralph Sadler vol. I (Google Books GMc_AAAAcAAJ) for the Edinburgh letter of 22 April 1543 and compare with Tomokiyo's reconstructed key. | 30 | bourdeau, archives |
| 12 | Walsingham and Edward Wotton (ambassador to Scotland), seven letters 28 July - 10 Sept 1585 (BL Add MS 32657, DECODE R4838-R4844) | 1585 | en | search-print | Check CSP Scotland vol. VIII (Boyd, 1914) for the 28 July-10 Sept 1585 letters in clear, then apply Tomokiyo's Walsingham-Wotton key (elizabeth.htm) to DECODE R4838-R4844. | 30 | bourdeau |
| 13 | George W. Erving to Madison, Madrid, 10 Aug 1807 (Pinckney legation code, no decode on the NARA copy) | 1807 | en | transcription | Transcribe the code groups from NARA M31 reel 12 frames 0362-0366 (naId 188605361 manifest) and apply the Pinckney pairs in cyphersolver/erving1807/pinckney_chain.tsv. | 29 | bourdeau |
| 14 | Thomas Randolph (Edinburgh) to the Earl of Sussex, 1569 (BL Cotton Caligula C II f.277, DECODE R4931) | 1569 | en | transcription | Fetch f. 277r-v tiles from https://bl.digirati.io/iiif/ark:/81055/vdc_100162985756.0x000001 (as in cyphersolver/norfolk1570/fetch.py), transcribe, and match against CSP Scotland II-III. | 29 | bourdeau |
| 15 | Charles I (Oxford) to Prince Rupert, 29 April 1645 (BL Add MS 18983 f.14, DECODE R4921) | 1645; 1648 | en | search-print | Check Warburton, Memoirs of Prince Rupert vol. 3 (1849) and CSP Domestic 1644-45 for a deciphered print of the 29 April 1645 letter before requesting DECODE R4921 and its attached key. | 28 | archives, aymeloglu, bourdeau |

## Tier B: next

| Rank | Target | Year | Lang | Next step | Detail | Total | Sources |
|---|---|---|---|---|---|---|---|
| 16 | BL Harley MS 287 cipher letters 1587-88: Cobham to Walsingham (4), Needham, unsigned (7) (DECODE R8477-R8496) | 1588 | en | search-print | Check CSP Foreign 1588 (vols 21.4 and 22) for Cobham's Bourbourg despatches of the DECODE dates, then fetch DECODE key R8497 and R8477-R8496 images. | 27 | bourdeau |
| 17 | [George Stepney to the Earl of Manchester, Vienna, 23 March 1702 (short ciphertext)](ciphers/stepney-manchester-1702/) | 1702 | en | archive-request | Tier B at 27, one under the line: only 24 groups (size 1) and no key located yet (key_lead 2); still the cheapest English finish. TNA page-check order for SP 105/65 (Discovery C3609655, the 23 March 1702 letter-book entry) was started 19 Sept 2026 but not completed, pending the account confirmation email; finish it per ciphers/stepney-manchester-1702/REQUEST.md. | 27 | bourdeau, tomokiyo |
| 18 | Robert Bowes to Walsingham, 7 April and 31 July 1583, and short Caligula B VIII ciphertexts 1580-83 (BL Cotton Caligula C VII, B VIII) | 1583 | en | search-print | Check CSP Scotland vol. 6 (Boyd 1910, 1581-83) on archive.org for Bowes's letters of 7 April and 31 July 1583 and whether the cipher words are printed deciphered. | 26 | bourdeau, tomokiyo |
| 19 | BL Harley MS 1582 cipher letters: Sir Edward Stafford 1586, N. Wotton? 1554, and unsigned (DECODE R8499-R8505) | 1586 | en | search-print | Check CSP Foreign Elizabeth vol. XXI pt 1 (british-history.ac.uk) for Stafford's letters of 19 Sept and 9 Nov 1586 in clear, then use R8503's inline plaintext as key source. | 25 | bourdeau |
| 20 | BL Harley MS 260 cipher letters 1571-72: Elizabeth R., Burghley, Walsingham and unsigned (DECODE R8356-R8364) | 1572 | en | search-print | Match the nine DECODE dates (R8356-R8364) against Digges, Compleat Ambassador (1655) on the Internet Archive, where the deciphered Walsingham-Burghley letters of 1571-72 are printed. | 25 | bourdeau |
| 21 | Nicholas Throckmorton to Elizabeth I, 10 July 1559, marginal ciphertext in an unknown cipher (BL Add MS 4136, DECRYPT 2988-2989) | 1559 | en | search-print | Check CSP Foreign Elizabeth 1558-59 (SP 70/5, Throckmorton to the Queen, 10 July 1559) for the deciphered marginal passage before requesting DECODE R2988 images. | 25 | bourdeau, tomokiyo |
| 22 | [Prince Maurice to Prince Rupert, Worcester, 7 July 1645 (Warburton, Memoirs of Prince Rupert iii.133)](ciphers/maurice-rupert-1645/) | 1645 | en | archive-request | Register on DECODE (free) and ask for the R8429-R8454 images (BL Add MS 18980-82, 1645 letters with interlinear decipherments) to look for the Rupert-Maurice cipher. | 25 | tomokiyo, bourdeau |
| 23 | Unknown (York) to Lord Goring, 5 June 1645 (TNA SP 106/10, DECODE R932) | 1645 | en | cryptanalysis | Get the DECODE login, fetch R932 (TNA SP 106/10) and test Lasry's four reconstructed SP 106/10 keys (cyphersolver hm1645/ notes) before a fresh homophonic attack. | 25 | bourdeau |
| 24 | William Cecil to Sir Ralph Sadler and Sir James Croft, 11 Sept - 30 Oct 1559 (BL Add MS 33591, DECODE R4847-R4860) | 1559 | en | search-print | Read the 11 Sept and 30 Oct 1559 letters in Clifford, Sadler State Papers vol. I (Google Books GMc_AAAAcAAJ) for the cipher phrases in clear. | 25 | bourdeau |
| 25 | Gelett Burgess, The Master of Mysteries (1912), third hidden message | 1912 | en | cryptanalysis | Score paragraph-first-word acrostics and printed-line units from the Cornell scan (archive.org cu31924022342871), the families Aymeloglu's README lists as untested. | 24 | aymeloglu |
| 26 | Intercepted letter of Edward Hyde, 1 Nov 1659, f.93 full of undecoded code numbers (BL Add MS 4166 ff.92-93, DECODE R4886) | 1659 | en | search-print | Search the Calendar of Clarendon State Papers vol. 4 (1932) for a Hyde cipher of late 1659 with numbers to about 966, then order the Bodleian Clarendon MS key by copy request. | 24 | bourdeau, tomokiyo |
| 27 | [Regent Moray to John Wood, Edinburgh, 13 July 1568 (cipher postscript, BL Add MS 32091 f.213)](ciphers/moray-wood-1568/) | 1568 | sco | blocked | Leave to Aymeloglu; only a BL copy of Add MS 32091 f.213v or a sibling letter in the same alphabet could settle the seven-sign ending. | 24 | aymeloglu, bourdeau, tomokiyo |
| 28 | Catokwacopa advertisements, Evening Standard, 8 and 20 May 1875 | 1875 | en | cryptanalysis | Run a phrase-level language-model search on line 23 (48 letters) with Bourdeau's positional prior, using cyphersolver/catokwacopa/search.py (MIT). | 23 | bourdeau, web |
| 29 | Queen Anne to Charles Mordaunt, Earl of Peterborough, 22 Feb 1711 (BL Add MS 4107 f.184, DECODE R4878) | 1711 | en | search-print | Search the printed instructions to Peterborough of 22 Feb 1710/11 (Lords' committee report 1712, Lords Journals vol. 19, Boyer's Political State) before viewing DECODE R4878. | 22 | bourdeau |
| 30 | Charles I to Henrietta Maria, 8 April 1645, one sentence in their private cipher (The King's Cabinet Opened, 1645) | 1645 | en | search-print | Check Green, Letters of Queen Henrietta Maria (1857) p.299 and locate the ciphered original of her 2 April 1645 letter, the only sibling in this private cipher. | 21 | bourdeau, tomokiyo |
| 31 | John Armstrong to James Madison, Paris, 20 Feb 1808 (unique code, 369 groups) | 1808 | en | cryptanalysis | Place Krajcovic's crib from Armstrong's 15 Feb 1808 letter to Jefferson against the opening groups in cyphersolver/armstrong/feb20_ciphertext.txt and score it with a shuffled control. | 21 | bourdeau, tomokiyo, web |
| 32 | Sir Francis Walsingham, autograph letter partly in cipher to an unknown recipient, 26 May 1574 (Folger V.b.264) | 1574 | en | archive-request | Email Folger reference for a digital image or LUNA link of the Walsingham letter of 26 May 1574 in V.b.264 and its folio number. | 21 | archives |
| 33 | Charles I in the Isle of Wight: to Worsley 22 May 1648 and to Prince Charles 1 Aug 1648 (BL Harley MS 6988 f.208; Worsley/Hillier prints) | 1648 | en | blocked | No key is located; the two unread letters need the Worsley and 'noble frend' keys themselves, whose shelfmarks nobody has identified (DECODE R8342 image is login-only). | 20 | bourdeau, aymeloglu, tomokiyo |
| 34 | John Wood to Secretary Cecil, 6 Sept 1568, 'Wool letter' on the sheet of DECRYPT 2989 (BL Add MS 4136) | 1568 | en | search-print | Check CSP Scotland vol. 2 (1563-69) and SP 52/15 for Wood to Cecil, 6 Sept 1568, with a deciphered copy, before requesting DECODE R2989. | 20 | bourdeau, tomokiyo |

## Tier C: watch

| Rank | Target | Year | Lang | Next step | Detail | Total | Sources |
|---|---|---|---|---|---|---|---|
| 35 | [Ormond to Arran, 24 Jan 1678, short undeciphered segments (HMC Ormonde iv.93)](ciphers/ormond-arran-1678/) | 1678 | en | search-print | Search HMC Ormonde vols. 4-5 and the Carte calendar for another 1678 Ormond-Arran letter with numbers up to 732 and a decipherment. | 19 | bourdeau, tomokiyo |
| 36 | Thurloe State Papers intercepts with undeciphered portions: vol. 5 (1656, du Gard to White etc.) and vol. 7 (c.1659) | 1656 | en | search-print | Search the Calendar of Clarendon State Papers vol. 3 (1655-57, archive.org) for 1656 letters of Waddall, Copinger and White that mention a cipher or key. | 19 | tomokiyo, bourdeau |
| 37 | William, Baron Craven to Prince Rupert, The Hague, 6 Nov 1648 (BL Add MS 18982 ff.134-135, DECODE R8447) | 1648 | en | transcription | Register for DECODE, obtain the R8447 images of Add MS 18982 ff.134-135, transcribe the cipher and count tokens before anything else. | 19 | bourdeau, tomokiyo |
| 38 | Unsigned letter from Paris, 19 April 1641 (BL Harley MS 7001 ff.148-149, DECODE R7766) | 1641 | en | transcription | Register for a DECODE account, download the R7766 images (Harley MS 7001 ff.148-149) and transcribe the numerical groups with the surrounding cleartext. | 18 | bourdeau |
| 39 | Gun Wa advertisement cipher, 1889 (77 letters) | 1889 | en | search-print | Search Chronicling America 1889-90 for further Gun Wa advertisements carrying cipher text, since only a sibling ciphertext would lift 77 letters above unicity. | 17 | aymeloglu |
| 40 | 'Mr. Conley's hand', Paris, 28 Dec 1652 and 3 May 1653 (BL Harley MS 7003, DECODE R7768-R7769) | 1652 | en | transcription | With a DECODE login, download R7768-R7769 (Harley MS 7003), read the cleartext and count the nomenclator groups before deciding whether an attack is possible. | 14 | bourdeau |

## Kept, not scored this sweep

163 further kept candidates were left unscored by the 40-candidate cap (by plaintext language: fr 57, es 34, unknown 19, it 17, de 14, la 10). They are listed with the harvesters' evidence under `unscored_kept` in `QUEUE-scores.json`, in the filter's order, so the next run scores them first if the top forty move. Those with a working folder already, all closed-negative or blocked in LANDSCAPE.md: [Anonymous letters to Mr Tempest (Paris) and Dr Barret (Rheims), c. Dec 1585, endorsed by Phelippes (TNA SP 53/16 nos. 78-79)](ciphers/sp53-16-78/); ['Cifer with Spanish Spye', short ciphertext c.1586 (TNA SP 53/22 f.52, and the verso of f.40)](ciphers/sp53-22-f52/); [Lodovico Birago to the Duke of Nevers, Saluzzo, 13 Nov 1571, paragraph in numerical cipher (BnF fr. 3251 f.119)](ciphers/birago-nevers-1571/); [Admiral d'Estaing to Gerard, French minister in Philadelphia, 30 April 1779, intercepted (Clements Library, Clinton Papers 64:14)](ciphers/destaing-gerard-1779/); [Berthier to Napoleon, Koenigsberg, 22 Dec 1812 (AN AF/IV/1643) and the encoded letter to Marshal Marmont, 1807 (Vilcoq 1969)](ciphers/berthier-napoleon-1812/).

## Dropped this sweep

| Candidate | Reason |
|---|---|
| William Perwich to Lord Arlington, Paris, 9 April 1670 (TNA SP 78/129 f.180) | found-solved: broken Oct 2025 by Matthew Brown and by Lasry, Biermann and Tomokiyo (cyphersolver README 'Found already solved by others') |
| Jean Du Bellay, ambassador in England, letters 1529 (BnF Clairambault 329) | plaintext known: Du Bellay 1528-29 found already solved (Le Grand 1688, Bourrilly 1905, Lasry 2022) per cyphersolver SOLVED_CATALOGUE §4; Scheurer 1969 prints the 1529 letters from deciphered copies |
| Roosevelt cryptogram, April 1935 | explained by Bourdeau 16 Sept 2026: the number block is a permutation of 1-52 padded with zeros, not a cipher; famous list |
| Fair Game end-credits code, 2010 | modern film-credits puzzle, not a historical cipher; Bourdeau top50 'open but not settleable by cryptanalysis' |
| Doge Cicogna / Marco Ottobon to Giovanni Mocenigo, 27 April 1589 (BNE Mss/994 ff.34-38) | solved by Aymeloglu 16 Sept 2026 (ottobon-1589, key Ziffra prima R1789); Bourdeau's attempt was closed before that |
| Scorpion letters S1 and S5, 1991 | famous/excluded list (Aymeloglu SHORTLIST §6: hoax risk); modern |
| Le Tellier to Castelnau, 12 May 1657 | solved by Robert Pitt, reported on Tomokiyo's page 15 Sept 2026 ('Le Tellier-Castelnau Cipher (1657) Solved') |
| Voynich manuscript | famous/excluded list; adjudicated by Bourdeau as not a cipher of a European language |
| John Quincy Adams to the Secretary of State, No. 88, 25 June 1812 | read by Bourdeau 18 Sept 2026: premise refuted, code rebuilt, the nine 'undecyphered' lines read |
| Japanese diplomatic code telegram printed by Yardley (c.1920) | plaintext known: Yardley printed the plaintext (American Black Chamber p.251); Tomokiyo says it was probably solved by the Cipher Bureau; a reconstruction exercise, not an unsolved cipher |
| Davison to Walsingham, 27 July 1584 | found-solved by Aymeloglu 16 Sept 2026: printed in Boyd, CSP Scotland VII no. 222 (LANDSCAPE 'rows that moved') |
| Chinese gold bar ciphers, Shanghai 1933 | explained by Bourdeau 15 Sept 2026 (letter counts flat, no real text); famous/excluded list |
| D'Agapeyeff cipher, 1939 | famous/excluded list; Bourdeau: not enciphered English |
| Dorabella cipher, 1897 | famous/excluded list |
| Kryptos K4 | famous/excluded list; plaintext recovered from Sanborn's archive 2025 |
| WWII pigeon cipher | famous/excluded list; one-time pad per GCHQ |
| ADFGVX residue, 1918 (Childs corpus) | found-solved: keys published by Lasry, Niebel, Kopal and Wacker; the unread residue is transmission garble (cyphersolver README 'Found already solved by others') |
| Lima, Ohio robbery note, 1916 | modern true-crime note; Bourdeau odds low, variant transcriptions |
| Rubin cryptogram, 1953 | modern true-crime slip; not a historical cipher |
| Rayburn note, 2004 | modern; plausibly a password list, not a cipher (Bourdeau) |
| SS radio message, 1944 | probable forgery (Bourdeau: wrong typography and rank abbreviations) |
| Erba murder note, 2006 | modern true-crime note |
| Sufi Fiddle | unidentified script with no published transcription; provenance rests on a novel's afterword; not established as a cipher |
| Zodiac ciphers | famous/excluded list |
| Somerton Man code | famous/excluded list; not a cipher |
| Rohonc Codex | famous/excluded list |
| McCormick notes | famous/excluded list; modern true crime |
| Cylob, Blitz, Untersberg (Schmeh Top 50 nos. 50, 41, 11) | famous/excluded list (Blitz, Cylob) and modern; Bourdeau 'not settleable by cryptanalysis' |
| Shugborough, Fair Game, Powers (Schmeh Top 50 nos. 37, 36, 22) | famous/modern puzzles; Bourdeau 'not settleable by cryptanalysis' |
| World Record and Double Column Reloaded challenges (Schmeh Top 50 nos. 45, 13) | artificial compute challenges, not historical ciphers |
| Intercepted League letters summarised for Nevers' office, Sept-Oct 1589 (BnF fr. 3977 no. 96) | not a ciphertext: only the contemporary 'Recueil sommaire' of interpreted letters is described; the intercepts are not located |
| Frederick II to Louis Michell, Berlin, 28 Dec 1751 (KHA Prins Willem V inv. 198, DECODE R1957) | found-solved: printed in Politische Correspondenz Friedrichs des Grossen 8 (1882) no. 5263 (cyphersolver README) |
| Henry IV to Savary de Breves, Paris, 5 Jan 1610 (BnF fr. 3541 ff.4-7) | marked 'Solved' on Tomokiyo's page (Lasry solved a significant part in 2021; key reportedly preserved in BnF per Desenclos) |
| Vatican Challenge Part 4: manuscript of 1535/36, Segr. Stato Portogallo | solved Aug 2019 by Thomas Bosbach (Lasry et al., Cryptologia 2020), per Tomokiyo 'New Vatican Challenges'; MysteryTwister records 2 solves |
| Spanish Strip Cipher telegram, MysteryTwister Level X | MysteryTwister challenge with no locatable archival source; no new solutions accepted since July 2026 |
| Dataset of cryptographic postcards, 21 'unidentified' items (Slovak paper) | paper's dataset only; individual items neither identified nor accessible; not a ciphertext |
| Cylob cryptogram, c.1995-96 | famous/excluded list; modern |
| Madsen cryptogram (printed book, 2016) | modern book puzzle, not a historical cipher |
| Townshend chalkboard cryptogram, c.1980 | modern video clip, possibly meaningless (Schmeh); not a historical cipher |

Sources unreachable: archives: PARES (pares.mcu.es and pares.cultura.gob.es) was unreachable from this environment on 19 Sept 2026: curl got 'Connection reset by peer' and a TLS 'unable to get local issuer certificate' through the agent proxy, WebFetch got 503; PARES candidates therefore rest on search-engine snippets and on the unsolved-ciphers repository's PARES cache (/tmp/unsolved-ciphers/catalogue/pares-*.jsonl, harvested by aaymeloglu), cited as such. TNA Discovery's JSON API answered one query then returned 403 'Restricted' for every further query; the beta catalogue search (beta.nationalarchives.gov.uk) worked and was used instead. archivesetmanuscrits.bnf.fr and gallica.bnf.fr return 403 to WebFetch but 200 to curl with a browser user agent; two Gallica OAI calls were reset once and succeeded on retry. searcharchives.bl.uk returns its landing page for search URLs (single record pages load). folgerpedia.folger.edu gave 503 and catalog.folger.edu 403/202, so Folger call numbers come from search snippets. huntington.org gave 429; the OAC finding aid loaded. DECODE record pages and the record list load without login, but every DECODE image at TNA/BL is 'Authentication required' (free DECODE account).; tomokiyo: Nothing unreachable. Cryptiana web and blog were live on 19 Sept 2026 (HTTP 200). Tomokiyo's two 1710 transcription links (blencowe_geertruidenberg.txt, blencowe_polignac.txt) redirect (HTTP 302) and are dead, as LANDSCAPE.md says; maitland.htm and mirabeau.htm are not in the snapshot and were fetched live.; web: cipherbrain.de (Klaus Schmeh's 2023-mid-2026 blog) returned HTTP 503 on every path tried, and web.archive.org and reddit.com are not fetchable by the tool, so Cipherbrain posts from Jan 2023 to Jul 2026 and r/codes threads could only be seen through search snippets. boingboing.net (403), clements.umich.edu (403) and historum.com (paywalled 402) were unreadable; worked from snippets. The HistoCrypt 2026 Vichy-telegrams PDF downloaded but its text could not be extracted (no pdftotext, pypdf's crypto backend broken), so only its abstract is used; the Jacobite paper PDF link was 404. ciphermysteries.com monthly archive URLs for May-Sept 2026 are 404; the homepage shows no cipher-document posts after 5 Apr 2026.
