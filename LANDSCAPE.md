# The landscape on 19 September 2026: who is working, what is left, where to play

## Who

| Who | Role | Where to watch |
|---|---|---|
| Satoshi Tomokiyo | Keeps the list at cryptiana.web.fc2.com/code/unsolved.htm and the Cryptiana blog. Records solutions sent to him, with lag. | The page itself; blog feed cryptiana.blogspot.com/feeds/posts/default |
| George Lasry, Norbert Biermann, Thomas Bosbach, Matthew Brown | The veterans. Lasry's homophonic and syllable-cipher solvers have cleared most of the French, Spanish and Italian nomenclators since 2020. They post on Cipherbrain comments, DECODE, Cryptologia and HistoCrypt. | Cipherbrain (Klaus Schmeh), HistoCrypt proceedings on LiU E-Press, DECODE records |
| Daniel Bourdeau | cyphersolver: 99 target folders, about 45 solved, read or partly read between 14 and 19 September 2026, AI-driven with a human checking, formal write-ups, a catalogue of 194 further open targets harvested from DECODE, BnF and PARES. | github.com/dbourdeau/cyphersolver and dbourdeau.github.io/cyphersolver |
| Andrew Aymeloglu | unsolved-ciphers: 8 targets, cipherkit, a catalogue sweep of DECODE, BNE and PARES with 1,187 DECODE records ranked. Same AI-plus-human method, stricter conventions. | github.com/aaymeloglu/unsolved-ciphers and aaymeloglu.github.io/unsolved-ciphers |
| Robert Pitt | Forster 1644 and Charles I-Boswell 1643 keys. | github.com/robertpitt |
| Arya Sanketbhai Patel | Contributor to cyphersolver (Lorraine 1592, Sormano). | via cyphersolver |
| Richard Bean | Milroy 1862 telegrams with Claude Opus 5. | Cryptiana civilwar1b_milroy.htm |
| offgramercy | Barney 1863 dictionary code, on r/codes. | reddit.com/r/codes |

Both AI-driven projects started in the second week of September 2026 after Vals AI reported Claude Fable 5.1 reading Urquhart's Cyphral Distich. Bourdeau's rate is roughly ten targets a day. Tomokiyo's 18 September notice says he cannot keep up with the solutions arriving.

## What this does to our catalogue

Every one of the eleven working folders in `ciphers/` has been attempted by Bourdeau, Aymeloglu or both. Corrected statuses:

| Our folder | Status on 19 Sept 2026 | Source |
|---|---|---|
| sp53-16-78, sp53-16-79 | Closed-negative by both. Symbol ciphers, not numeric. A solver that reads matched 507-token controls finds no language basin in five languages. Needs page images (State Papers Online, paywalled) and the SP53/22 keys. | cyphersolver/sp53, unsolved-ciphers TARGETS row 13 |
| sp53-22-f52 | Closed-negative by both. 84 tokens is below unicity; matched controls solve, the target does not. All 61 SP53/22 key images tried by Aymeloglu. | cyphersolver/sp53, unsolved-ciphers TARGETS row 14 |
| moray-wood-1568 | Substantially read by Aymeloglu from the DECODE page image (119 of 134 glyphs graded S, key-shuffle z = 17). Ending of seven signs unresolved. Bourdeau's attempt on Tomokiyo's transcription was undetermined. | unsolved-ciphers/moray-1568 |
| birago-nevers-1571 | Closed-negative by Bourdeau after glyph-level re-transcription from Gallica: the only consistent design (two-digit letters plus marked code groups, 228 tokens over 62 symbols) is beyond what the annealer reads on matched controls. Needs a sibling letter or crib. | cyphersolver/birago |
| ormond-arran-1678 | Not attempted by either beyond noting "20 groups, written as a test". Below unicity. | cyphersolver TARGETS |
| maurice-rupert-1645 | Offline-only. Known Rupert keys do not fit; the key would be in BL Add MS 18980-82 or 72438, digitised but offline since 2023. | cyphersolver/rupert |
| intercepted-royalist-1646 | Partial by Aymeloglu: f.10 (the 13 May letter to Charles I) is Digby's captured key no. 129, about 45 values fixed from the surviving key page and Evelyn's printed decipherments. Our f.9 opening is the other letter, which uses a smaller key in which 226 = London. Full reading needs the rest of key 129 or the contemporary decipher (Add MS 72438 f.11, Tanner 59-60, SP 16/514). | unsolved-ciphers/royalist-1646 |
| stepney-manchester-1702 | Offline-only. Bourdeau located and transcribed the manuscript at Yale (OSB MSS fc37 box 8 folder 40), rejected the THE=454 key, and placed the real key in TNA SP 105/106 or BL Add MSS 7058-78. | cyphersolver/stepney |
| destaing-gerard-1779 | Skipped by Bourdeau: 217 tokens of a 600-entry code with no key material. The deciphered copy would be in AAE Correspondance politique, États-Unis suppléments t.1. | cyphersolver/destaing |
| berthier-napoleon-1812 | Blocked on one article: the full ciphertext exists only in Vilcoq 1969, not digitised. Chuquet 1912 prints Berthier's December 1812 letters in clear from the same carton, two dated 22 December, so a crib exists once the ciphertext does. Our two Cryptiana pages disagree on one group (356 vs 656). | cyphersolver/napoleon |

Other catalogue rows that moved:

| Item | Status | Source |
|---|---|---|
| Charles I-Boswell 1643 | Solved (Pitt; verified and extended by Bourdeau, z = 9.6) | cyphersolver/boswell |
| Davison to Walsingham 1584 | Found in print, CSP Scotland VII no. 222 | unsolved-ciphers TARGETS row 18 |
| Dutch ciphers 1653, Beverning and Vande Perre to Boreel | Closed-negative by both. Separately, Aymeloglu recovered the alphabet of Vande Perre's own letters to de Bruyne in Thurloe vol. 1, an item not on Tomokiyo's list. | unsolved-ciphers/vande-perre-1653, cyphersolver/thurloe |
| Henry III to Ségur 1583-86 | Three of four read by Bourdeau. The sender is Henry of Navarre, not Henry III. f.143 is another key, open. | cyphersolver/segur |
| Starhemberg 1758 | Substantial partial by Aymeloglu with the 1752 Prima/Secunda key from DECODE. | unsolved-ciphers/starhemberg-1758 |
| Ferdinand III to Cardinal-Infante, R1887 (1634) | Open, assessed by Aymeloglu: a different graphic and code repertoire from R1889/R1890. All four images available. | unsolved-ciphers/ferdinand-1635-1640/1634-ASSESSMENT.md |
| Charles I Isle of Wight 1648 | Two letters still unread; the published 2021 key and the Titus key both excluded numerically. | cyphersolver/charlesi |
| Colbert passages 1665-75 | Charost and Gravel are one key (Maulevrier's), Charost is 1675 not 1673; closed-negative against controls. | cyphersolver/colbert |
| Chaulnes 1690 | Closed-negative; ciphertext verified from images, Croissy-table design established, 300 groups too few. Needs the minute in AE Rome Corr. 331-332. | cyphersolver/chaulnes |
| Torcy and Villars 1710 | No ciphertext online: Tomokiyo's two transcription links are dead and were never archived. | cyphersolver/geertruidenberg |
| Cocquet 1616, Joyeuse 1594, du Croc 1567, Blancmesnil | Attempted or gated by Bourdeau; Blancmesnil has no ciphertext online (fr. 3633 not digitised). | cyphersolver folders of the same names |
| Vatican Challenge 5 (1542) | Seven sessions by Bourdeau; identified as an Elio-family polyphonic syllabic cipher; excluded against controls. | cyphersolver/vatican5 |
| Armstrong to Madison, 20 Feb 1808 | The AFIO claimed solution adjudicated and rejected. Still unsolved. | cyphersolver/armstrong |
| BLUME SALAMANCA 1937 | In progress: transposition of telegraphic Spanish; single and short double columnar excluded. | cyphersolver/blume |
| Enigma 1945 | In progress: exhaustive UKW-B pass running. | cyphersolver/enigma |
| Hyde superscriptions | Not a cipher (nulls). | cyphersolver/hyde |
| Charles II to Hamilton 1650 | Offline-only, but the key is located and catalogued open: NRS GD406/1/2197, "Keys for ciphers used in the correspondence of the Duke of Hamilton", 5 items. Needs a copy order to Edinburgh. | cyphersolver/hamilton |

Net effect: after two AI-driven sweeps in one week, what remains on Tomokiyo's list is either below unicity, a large nomenclator with one letter, or blocked on something only a person with archive access can do.

## Where the open ground is

For one person without institutional archive access, the ground is not Tomokiyo's list any more. It is in three places.

### 1. The archive-request lane (recommended first)
Both AI projects park items as "offline-only" the moment the next step is a copy order, a reader's ticket, or an email. Nobody is racing on these, the cryptanalysis is already done or trivial once the material arrives, and Tomokiyo records the result. Ranked by how cheaply one request finishes the job:

| Item | The one request | What is already prepared |
|---|---|---|
| Charles II to Hamilton 1650 | Copy order to National Records of Scotland for GD406/1/2197 (5 key items, open) and the letters GD406/1/10573-10576 | Bourdeau's `hamilton/` has all 102 groups transcribed and the printed sources collated. With the key it reads immediately. |
| Berthier to Napoleon 1812 and the Marmont 1807 letter | Interlibrary loan or a French library scan of J. Vilcoq, "Le Chiffre sous le Premier Empire", Revue Historique de l'Armée no. 4 (1969) | Chuquet 1912 prints Berthier's clear letters of the same date from the same carton (AF/IV/1643). Bourdeau's `napoleon/` has the plan. Marmont's 1811 code had about 150 entries, so it should fall to cribs. |
| Torcy and Villars 1710 | An email to Tomokiyo asking for the two transcription files his page links to (dead links), or a DECODE login for R8755 and R8756 | Bourdeau's `geertruidenberg/` notes say what to do once the text exists. |
| Stepney 1702 | Request to TNA for SP 105/106 or to BL for Add MSS 7058-78 ("Mr. Stepney's cipher", asked for August 1701) | Manuscript transcribed by Bourdeau from Yale's IIIF; 24 groups waiting. |
| Blancmesnil to Nevers | Reader's copy of BnF fr. 3633 f. 24 | The Potier-Nevers key of 1589 is the candidate, in Tomokiyo's nevers.htm. |
| d'Estaing 1779 | AAE Correspondance politique, États-Unis suppléments t.1 for the deciphered copy | 217 groups ready. |
| Maurice to Rupert 1645, the 1646 intercepts | Wait for the British Library viewer, or a DECODE login plus BL permission for Add MS 72438 | Aymeloglu has 45 values of key 129 already. The volume holds 49 captured Digby keys. |

The first row is the best single target in this whole document. One copy order, a known price, and a solve that has resisted since 1650.

#### If you read only English

The archive lane, ranked again with the plaintext language as a hard filter:

| Rank | Item | Plaintext | Request | Folder |
|---|---|---|---|---|
| 1 | Charles II to Hamilton 1650 | English | NRS copy order for GD406/1/2197 | ciphers/hamilton-1650 |
| 2 | Stepney to Manchester 1702 | English | TNA copy of the letter-book entry in SP 105 (gives the plaintext without a key) | ciphers/stepney-manchester-1702 |
| 3 | Maurice to Rupert 1645 and the 1646 intercepts | English | Wait for the British Library viewer, or a DECODE login plus BL permission | ciphers/maurice-rupert-1645, ciphers/intercepted-royalist-1646 |
| 4 | Torcy and Villars 1710 | French | Email Tomokiyo for the two dead transcription files | none yet |
| 5 | Berthier 1812 | French | Interlibrary loan of Vilcoq 1969 | ciphers/berthier-napoleon-1812 |

Rows 4 and 5 are still doable without French, because the AI does the reading and the crib for Berthier is
already in print; but checking a French reading for sense is harder when you cannot read it, so they come after
the English items.

### 2. Series with images online and keys nearby, in a language you read
Aymeloglu's CATALOGUE.md and Bourdeau's catalogue of 194 open targets both point at the same untouched bodies:
- **AGS Estado, Génova legajos 1383-1430 (1553-1600).** Dozens of ciphered letters a year from the Genoa embassy to Philip II, every one with images on PARES. Simancas keeps the Estado ciphers as a separate series, and a key found for one 1581 letter reads the forty-four beside it. Aymeloglu: "the largest homogeneous body of undeciphered-as-catalogued cipher in the sweep." Bourdeau has taken one PARES item (Toledo 1565) and nothing from this run.
- **AHNOB Santa Cruz 1632-35.** Philip IV's ciphered letters to the Marqués de Santa Cruz, three bundles that the archivist's own summary marks "[Sin descifrar]", 21 of 22 units with images.
- **BNE Granvelle correspondence 1548-54 (MSS/7900s).** Coherent run of diplomatic cipher; keys of the circle exist in Van Durme and Besançon.
- **Brussels SEG inv. 2559.** 45 records, transcriptions attached to 44. Bourdeau read Carpio and Balbases from it; the rest of the fonds is open.
- **Riksarkivet 1600-1646.** 16 records, images public, and R4332 carries both a decipherment and a key.
- **Brulart de Sillery 1615 and 1617 (BnF fr. 18043-18044 on Gallica).** Key attached, inline plaintext, DECODE says "partially decrypted". Nobody has taken it.

All of these need Spanish, French or German and the willingness to transcribe from images. That is where the AI helps most and where both projects say their bottleneck is (single-pass transcription leaves 20-45% garbled on the Kurtz letters).

### 3. English-language material neither project has touched
Both repos are thin on American material beyond the Madison and Adams letters. The Civil War telegraph collections (the Eckert papers at the Huntington, state archives such as Indiana Memory where the Milroy telegrams came from) are English, digitised, and use route transposition and dictionary codes that fall to modest tooling. The Milroy solve this year shows the approach works. The trade-off is that the historical stakes are lower and the pieces are less catalogued, so the first job is finding them.

### What to avoid
Anything Bourdeau lists as closed-negative with a control. Anything a Lasry solver will reach first: French and Spanish syllabic nomenclators with a transcription already online. The famous ciphers. Telegraphic-age codebook messages.

## Staying current

The wave is happening on GitHub and two blogs. Enough to see everything:

1. **Watch on GitHub** (Watch button, then email): `dbourdeau/cyphersolver`, `aaymeloglu/unsolved-ciphers`, `robertpitt/forster-cipher`. Bourdeau's README "Recent findings" line and both TARGETS.md files are the live state.
2. **Cryptiana blog feed:** `https://cryptiana.blogspot.com/feeds/posts/default` in any RSS reader. Tomokiyo posts new open items there before they reach the list (Mirabeau 1787, Wellington's Peninsular War code, September 2026).
3. **Cipherbrain** (Klaus Schmeh): where challenges are posted and where Biermann, Bosbach and Brown announce solutions in the comments.
4. **DECODE** at de-crypt.org: register (free) for images and to see when a record's status changes. Both projects say the status field is unreliable, so read the attached files.
5. **Weekly diff of the list.** Run `tools/refresh-sources.ps1` on your PC. It re-downloads unsolved.htm and shows what changed. Bourdeau keeps a copy of the same page in his repo for the same reason.
6. **HistoCrypt** (annual, open access at ecp.ep.liu.se) and Cryptologia for the methods papers. Lasry's papal-ciphers paper (2020) and the 2023 syllable-cipher work describe the solvers that are clearing the lists.
