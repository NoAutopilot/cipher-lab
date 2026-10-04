partial
Read by this worker (3 Oct 2026): Gachard, La Bibliothèque nationale à Paris vol.1 (1875) notice 130 = Espagnol 132, pp.415-421 (IA labibliothque01gach, whole-volume grep for Vargas/Mexia/chiffre; vol.2 also grepped, 0 Mexia hits); Teulet, Relations politiques ... Ecosse vol.5 (1862) (IA relationspolitiq05teul, whole-volume grep, "Ambassade de D. Juan de Vargas Mexia" section, all 36 dated item headings listed); Mignet, Antonio Perez et Philippe II (1846) (IA antonioperezetph00mign, whole-volume grep, 4 Mexia hits); and the solver repository el-descifrador/cabinet-noir es132-vargas-mexia/ (shallow clone, README and folder list), 3 Oct 2026.

- Target: BnF Espagnol 132 (Gallica btv1b10032556x), Philip II / Antonio Perez to Juan de Vargas Mexia, Paris, 1577-80 (QUEUE.md "LANE-POOLS scout, 3 Oct 2026", rows P1-01 Cipher 3 and P1-03 Cipher 4; sources/pools-scout/2026-10-03/P1.md/.tsv). Checked by CS-1, LANE-POOLS, account 1.
- Verdict in one line: the pool is **already partly read by another team**. Another AI solver repository published readings of 30 of its letters on 2 Oct 2026 using published keys; roughly 30-37 letters remain with no reading found. Keys are all published (Alcocer 1921, Devos 1950, Tomokiyo 2020). Status `partial`, not `open`, because most of what the scout scored as open is taken.

## Per-letter table of the pool (distinct letters; duplicates grouped)

Folio numbers are Tomokiyo's TOC numbers (spanish3D.htm, sources/cryptiana/web/spanish3D.htm); "CN" = cabinet-noir reading (README table, result n°); "TE" = Teulet 1862 prints a decipherment of the letter's date.
| Group | Folios (first folio of letter) | Status |
|---|---|---|
| Solver read (CN, published keys, grades A/B/C are CN's own, not ours) | 11-12, 17-25, 32, 34, 44, 46, 58, 71, 73, 81, 105, 113, 123, 134, 138, 142, 154, 161, 165(+167), 195, 198, 200, 211, 215, 220, 222, 228, 233, 245, 255 (30 letters, n°6-7, 14-21, 23-36, 39-44; n°33 f.255 minute printed in Teulet per CN, not verified by me) | solver read |
| Read by Tomokiyo | f.3-4 (Cipher 1, 16 Dec 1577; Spanish text by D. Martin Vilela, DECODE record 1960 doc D3482) | period/solver read |
| Contemporary clear copy in the volume | f.169 (no.78, 22 Jan 1579) and f.177 (no.81, Farnese 25 Jan 1579): plain Spanish decipherments, viewed by me at canvases 166 and 174 (see Premise check c); the ciphered originals they answer are not identified | clear copy on leaf |
| Printed decipherment (recipient side) | f.89/93 (19 Sept 1578) and f.119 (15 Oct 1578): Teulet vol.5 prints Philip II to Vargas of 19 Sept 1578 and 15 Oct 1578 from "Archives de l'Empire, Fonds de Simancas, liasse B 47, n.8 / n.6 -- Déchiffr. officiel". Tomokiyo (2024 note) says contents "seem to be different" from the f.89/f.119 letters; I did **not** compare texts | needs comparison (cheap) |
| Open, Cipher 3 (no reading found) | 37, 39, 41 (transcribed, Cipher 3 pool test 1 PASS, ES132-C3 4 Oct 2026: `ciphertext_f41r.tsv`, `reading_f41r.txt`), 50, 54, 62, 79, 85, 89*, 119*, 129, 146, 150, 171, 181, 185, 202, 206, 208, 213, 218, 235, 237, 251, 253, 257, 267, 269, 271, 275 (* = TE candidates) | open (30; my count from the TOC, duplicates folded) |
| Open, Cipher 4 (Perez) | 87, 157, 179 ("En partie chiffrée" in the BnF record; cabinet-noir has no lecture.md for them but its `cle/cipher4_codes_perez.tsv` quotes decoded contexts from f.87r/v, f.157r, f.179v-180r, so they have been partly worked there -- A3V2-ES132C4, 4 Oct 2026). f.136 and f.148 (Perez, 5 and 21 Nov 1578, money to Flanders) carry no "chiffre" in the BnF record and no cipher label in the TOC: probably clear, image unchecked | open (3; 136/148 probably not cipher) |
| Open, Cipher 2 / other | 273 (no.124), 26-27 (CN: extent doubtful) | open (1-2) |
| Not cipher | clear letters, Italian/French pieces, f.1, 48, 56, 66, 68, 70, 77, 97, 107-111, 121, 183, 191, 193, 204, 217, 243, 249, 277-287 | out of scope |

Totals: open letters about 34 (range 30-37) of about 70 distinct cipher letters. Open signs: cabinet-noir's own measure is about 15,000 groups for its 32 Spanish letters (README), about 470 per letter, so the open remainder is **about 16,000 groups (range 12,000-20,000)**, not the scout's ~70,000 (which counted the whole volume from one sampled canvas). Not measured by me.

## Why DECODE marks records 1960-2025 "Decrypted" (brief question)
Opened with one browser login (tools/decode_browser_login.js, 3 Oct 2026): record 1960 (f.3-4) carries two documents: "Vargas Mexia's Cipher 1 [key]" (Tomokiyo's table, image) and "Reading an Undeciphered Letter of Philip II to Juan de Vargas Mexia (1577) [pub]" (Tomokiyo, Academia.edu ver.21, with Spanish text by D. Martin Vilela). Records 1979 (f.87) and 2025 (f.275) each carry one document: "Vargas Mexia's Cipher 4 [key]" and "Cp30 (Vargas Mexia's Cipher 3) [key]". So "Decrypted" is key-attached status; the only plaintext attached is the one Cipher 1 letter. Authors/language fields on 1979 and 2025 are blank. Other records not opened (one login per session).

## Web and blog check (CS-1, 3 Oct 2026)
Queries (WebSearch, 9): "Felipe II Juan de Vargas Mexía embajador París 1578 carta cifra descifrada"; "Vargas Mexia" "Espagnol 132" Philip II cipher letters BnF; "Vargas Mexia" Antonio Pérez cipher letters 1578 Escobedo decipherment f.198; Tomokiyo Cryptiana Vargas Mexia es.132 comments solved; Rubino "Secrets of Antonio Pérez Decoded"; ciphermysteries.com Philip II Vargas Mexia Espagnol 132; Klausis Krypto Kolumne Philipp II Vargas Mexia; cryptiana.blogspot.com Vargas Mexia ... Alcocer Cp.30; "Vargas Mexia" 1578 Philippe II lettre chiffrée ... déchiffrement publié; Alcocer Criptografía española 1921.
Hits: Tomokiyo spanish3D.htm and Academia.edu paper (read locally from sources/cryptiana/web; "undeciphered ... keys identified"; the Academia page itself is 403 per CLAUDE.md, not opened); **github.com/el-descifrador/cabinet-noir (hit, read)**; Rubino 2012 OSU thesis (not opened, cited by Tomokiyo for f.198); BnF finding aid archivesetmanuscrits.bnf.fr/ark:/12148/cc34747q (WebFetch 403; search snippet only: letters "en partie chiffrées"; availability flag NOT quoted); Cipherbrain 2016-05-17 "Wer löst diesen verschlüsselten Brief aus dem französischen Nationalarchiv" (title only, not opened; likely another letter); Cryptiana blog 2018 and Sept 2025 pages (listed in results, not opened). Blog comment threads: not opened, unreachable-by-effort; no hit text naming Espagnol 132 outside the above.
Quote (cabinet-noir README, es132-vargas-mexia): "30 premières lectures avec clés publiées ... aucune de ces lettres n'est une découverte cryptologique ... première lecture (à notre connaissance) avec clé publiée". Quote (Gachard 1875 p.416): "à toutes celles qui sont chiffrées (sauf une seule) le déchiffrement manque."

## Premise check (CS-1, 3 Oct 2026)
- (a) folder's own mentions: no folder existed. Cryptiana's TOC marks no.78 (f.169) and no.81 (f.177) "(decipherment)". Found: both are clear-Spanish decipherments (see c). DECODE: key tables attached, one article attached to record 1960. found.
- (b) other solvers' working files: **found.** cabinet-noir es132-vargas-mexia/ has per-letter chiffre.txt + lecture.md for 30 letters (list above), `cle/cp30_complements.tsv`, `cle/cipher4_codes_perez.tsv`, added in one commit, 2 Oct 2026 14:15 UTC (v1.2.1). Its stated grades: 23 "A" (no clear found), 6 "B", 1 "C"; rates 79.9-97.2 % by its verifier. Not independently checked by me. Bourdeau cyphersolver: only research/gallica_sweep/bnf_candidates.txt line 51 ("Espagnol 132 | 24 items"), no target folder; Aymeloglu: DECODE catalogue rows only. Not found there.
- (c) physical neighbours: viewed canvases 166 (f.169 right, docket verso "Resumen de despachos") and 174 (f.177) at 1000 px: f.169 and f.177 are plain-Spanish clerk's decipherments of cipher letters, so at least two letters of the volume carry a contemporary clear copy. I did not view the other cipher letters' facing pages (not in the box); Gachard says the others have none ("sauf une seule"). Found (2), others not found at Gachard's word, unviewed by me.
- (d) recipient side: **found.** Teulet vol.5 prints "Déchiffr. officiel" texts (Archives de l'Empire, Simancas fonds, liasse B 47) of Philip II to Vargas of 19 Sept 1578 (n.8) and 15 Oct 1578 (n.6), dates of f.89 and f.119 (both Cipher 3, neither read by cabinet-noir); 27 Oct 1578 is a minute. Gachard: Archives nationales hold "toute la correspondance de Vargas avec Philippe II" (Simancas fonds, Vargas to the King, deciphered); AGS Estado K minutes not consultable online. CODOIN, BL Add MS 28421 (7 Vargas letters 1579-80 per Tomokiyo), Alcocer 1921 (Cervantes Virtual/HathiTrust, key facsimile) and Devos 1950: not opened by me, so unreachable/unread, cited from cabinet-noir and Tomokiyo.
- Mignet 1846: whole-volume grep, Vargas/Mexia hits at lines 2144 (appendix E reference to Vargas and the king's reply), 3952, 4106 (denunciation by Vargas), 4185, 6234; I did not locate the ~80 words of f.17-25 that cabinet-noir attributes to Mignet.

## Cheap gaps 4-6 (A3V2-ES132C4, account 3, 4 Oct 2026, 05:16-05:2x UTC by the container clock)
Brief: `.claude/briefs/runs/2026-10-04-acct3-a3v2-wave2.md` section A3V2-ES132C4. No decoding, no Cipher 3 letter touched.

**(a) Cipher 4 (Perez) table source.** Two sources now on disk or cited:
- Tomokiyo's table `spanish3vargas4.png` ("Vargas-Mexias' Cipher 4 (1578-1579)", spanish3D.htm section "Vargas Mexia's Cipher 4"), fetched 4 Oct 2026 from cryptiana.web.fc2.com (HTTP 200, image/png, 851x371, 23,406 B, sha256 f4884bf580bfef4712a14870549d4f068f5bbb0a8ba62a048680ae64235047a8), saved unmodified as `sources/cryptiana/web/spanish3vargas4.png` beside the page; row added to `sources/cryptiana/keys/IMAGE-PICK.tsv`. Content, read by eye from the image: a 23-letter alphabet a-z (no k, w) over numerals 12 11 10 9 8 7 6 5 4 3 2 1 23 22 21 20 19 18 17 16 15 14 (a=12 ... u=17, z=14), with extra signs y (under a), d (under d), o and v (under o), a (under u); a second row of double consonants bl cl fl gl pl br cr fr gr pr tr = B C [F] [G] [P] [b] [c] f g p t (brackets = Tomokiyo's conjectures); vowel marks: dot-right -a, plus -e, dot-below -i, "6"-like hook -o, dot-above -u, caret = null(?). Prose on the page: reconstructed by Devos (1950) p.422 from Vargas Mexia's letter of 16 May 1579; code words known: "vo" = Vra. Magd., "o" = hu (Devos), "co" = carta (Tomokiyo, f.123). No code-word list beyond these three.
- el-descifrador/cabinet-noir `es132-vargas-mexia/cle/cipher4_codes_perez.tsv` (commit 47b6db9, 2 Oct 2026; data licence CC BY 4.0 per its LICENSE-DONNEES.md, code MIT -- read and cited, nothing copied): 33 rows of code hypotheses with contexts, 18 distinct codes: vo = S.M. (6 contexts, 0.8-0.9), xe = V.m. (5, 0.6-0.9), ra = oficio (5, 0.6-0.75), xi = a person (don Juan de Austria or Alencon, 4, 0.5), plus single-context guesses (tu, mo, no, Ta, H?, P?, pff, a-with-point = vi, "ARCAUTI" spelled). Its contexts come from f.198 (15), **f.87 (7), f.157 (6), f.179 (3), f.180 (2)** -- that is, cabinet-noir has transcribed and partly read the three open Cipher 4 letters even though it publishes no lecture.md for them (its README table lists only f.123, f.154-155, f.198-199 under Cipher 4).
- Coverage: Tomokiyo's table (alphabet + syllables + three code words) covers the whole alphabetic part of f.87 (Perez, 13 Sept 1578, "En partie chiffrée"), f.157 (8 Dec 1578, "En partie chiffrée") and f.179 (26 Jan 1579, "En partie chiffrée"); the cabinet-noir hypotheses would add the recurring codes vo/xe/ra/xi at their stated confidence (grade M at best, their judgement not ours). f.136 and f.148 (Perez, 5 and 21 Nov 1578, "envoi d'argent en Flandre") are described by the BnF record with no "chiffre" at all and carry no cipher label in Tomokiyo's TOC, so they are probably clear letters; not image-checked.
- Not done: no transcription, no key.tsv for Cipher 4, no application to any letter.

**(b) Holding catalogue record.** archivesetmanuscrits.bnf.fr/ark:/12148/cc34747q answers plain curl with a browser User-Agent (HTTP 200, text/html, 58,116 B, 4 Oct 2026; the 3 Oct WebFetch 403 was the fetcher, not the host; `tools/browser_fetch.js` failed here only because this container's Chromium NSS cert fix was not applied -- same as A3V2-SANG's flag). Record: "Espagnol 132 • Regius 9999 [FRBNFEAD000034747]", Département des Manuscrits > Espagnol. Availability flags quoted verbatim: "Version numérisée : Consulter le document numérisé [http://gallica.bnf.fr/ark:/12148/btv1b10032556x]"; "Document de substitution : MF 8506"; "Document original : Espagnol 132 Réserver ... Veuillez réserver/consulter en priorité un exemplaire de substitution. La consultation du document original doit être motivée et est soumise à validation." So: digitised (Gallica ark confirmed from the holding record itself), microfilm MF 8506, original on justified request only. The record's per-item descriptions also fix which letters the BnF itself calls ciphered: f.87, 157, 179 "En partie chiffrée"; f.89 and 93, 119, 123, 154 "En chiffre"; f.169 and f.177 "Déchiffrement"; f.273 and 275 "Deux chiffres de Philippe II pour Juan de Vargas Mexia" (the two key sheets); f.136, 148 no cipher mention.

**(c) Blog comment threads** (one search page per host plus the post pages named; descriptive UA; all HTTP 200):
- Cipherbrain / Klausis Krypto Kolumne, 17 May 2016, "Wer löst diesen verschlüsselten Brief aus dem französischen Nationalarchiv" (scienceblogs.de/klausis-krypto-kolumne/2016/05/17/...): about Gallica btv1b9059908w (a Ranzo letter from the "Knox list"), **not Espagnol 132**; 21 comments (Thomas, Mamie Juliette, Lercherl, Torbjörn Andersson, Norbert), all about that letter and its nomenclator, no Vargas Mexia / es.132 mention. No reading claim relevant here.
- Cryptiana blog (cryptiana.blogspot.com, search "Vargas Mexia", 8 posts listed). "Will Anyone Decipher Philip II's Secret Letters?" (Aug 2020, and its Spanish twin): 3 comments, all by Tomokiyo himself -- preliminary reading of the 16 Dec 1577 letter (Academia.edu), its update with Demetrio Martín Vilela's help (31 Oct 2020), and the DECODE upload (4 Jan 2021); no third-party reading claim. "Some Updates on Correspondence between Philip II and Vargas Mexia" (23 June 2024): no comments; body says he compared Teulet (1862) by dates and correspondents and "confirmed the letters in BnF es. 132 are not printed in Teulet", and that further undeciphered Vargas Mexia letters are catalogued in **BL Add MS 28421** (a sibling pool, not on our board). The two 2026/10 posts in the list (Fran VI polyphonic cipher; Enigma messages solved by AI) matched the query only through the sidebar; not opened. The Sept 2025 page CS-1 listed was not identified in the search result; the "2018" page is the Guise post (sources/cryptiana/blog), no Vargas mention.
- Cipher Mysteries (ciphermysteries.com/?s=Vargas+Mexia): "Nothing Found", 0 posts.
Result: no reading claim for any Espagnol 132 letter found in any comment thread; the only readings known remain Tomokiyo's f.3-4 and cabinet-noir's 30 letters (plus its working contexts on f.87/157/179-180). Search result, not a novelty verdict (rule 10).

Requests by host: cryptiana.web.fc2.com 1; archivesetmanuscrits.bnf.fr 2 (one browser-tool attempt failed on the cert, one curl 200); scienceblogs.de 2; cryptiana.blogspot.com 3; ciphermysteries.com 1; github.com 1 shallow clone; WebSearch 3 (all off-target). Subagent calls 0. No credentials used.

## Remaining gaps (finish-or-blocker pass, 3 Oct 2026, refreshed 4 Oct 2026 A3V2-ES132C4)
Read so far: 31 of about 70 distinct cipher letters read by others (30 cabinet-noir + 1 Tomokiyo), about 44%, counted from the TOC and cabinet-noir's README; 2 more have a clear copy on the leaf.
- The two Teulet letters' unprinted text is through gate (b) on every page (f.89 letter: f.89r, f.89v, f.90r, f.90v, f.91r; f.119 letter: f.119r, f.119v, f.120r), rule-7 SAME 2842/2842 (A3V2-ES7) and print-checked; **AUDIT 1 done (A3V2-ES132A1, 4 Oct 2026, `AUDIT.md`): printed paragraphs N0 (Teulet 1860/1862, period decipherment), unprinted paragraphs N3, depth D2 on the C text only (about 11% / 16%), D1 on the N3 text; not a unique solve, AUDIT 2 not due**. The duplicate copy f.93r-f.95r is transcribed and aligned (A3V3-ES9396) and **43 of the 113 '?' tokens are settled from it** (A3V3-ES132S, 4 Oct 2026, PREREG_dupsettle.md, section below: 25 flags removed where both duplicate blind reads confirm, 18 tokens replaced by the duplicate's isolated 1:1 token; control 48/50 firm tokens unchanged); **70 '?' remain**; a fresh rule-7 re-derivation of the settled f.89 pages is owed (not done by the settling worker) - blocker: not-attempted; next: rule-7 re-derivation after A3V3-ES132S (fresh session, spec + key + test2.py/settle_dup.py --check), ~$2; then the 30 non-isolated and 10 non-agreed candidates in dup_settled.tsv by a two-crop look (f.89 crop vs duplicate crop), ~$3
- Cp.30 nomenclature (cursive word codes, numbers >= 38: 14 of 75 tokens in the unprinted paragraph) - blocker: not-attempted; not on disk; next: Alcocer 1921 facsimile (Cervantes Virtual: cloud-blocked, LOCAL-QUEUE row) or cabinet-noir attested values cited, ~$1
- About 29 open Cipher 3 letters (list in the table), about 16,000 groups - blocker: not-attempted; f.41r and f.41v (letter of 29 April 1578), f.50r, f.50v and f.51r (letter f.50, June 1578; RUN4-ES50R, RUN4-ES41V, RUN4-ES50) done: gate (b) PASS on both blind passes with the control passing in the same run (err_2reader 30.6% / 33.0% / 40.0% / 12.7% / 18.2%, '?' 105/526, 162/546, 179/456, 72/516, 83/473; f.50r pass B wrote no '.' vowel signs and passed by 0.003 only); the f.41r crop settlement failed its own control by one item and was not applied; cabinet-noir still at 47b6db9 (4 Oct 2026 11:41 UTC); next: f.51v if it continues the letter (not viewed; canvas 49 left page, same route, ~$4.5); one replacement blind pass B on f.50r with the dot sign called out in the prompt, scored against the same PREREG (~$1.5); then if it continues the letter (not viewed); lookalike pass (`tools/lookalike_pass.py`) on f.41r/f.41v before any further machine settlement there (~$3)
- 3 open Cipher 4 (Perez) letters f.87, 157, 179 (f.136/148 probably clear per the BnF record) - blocker: not-attempted; table now on disk (sources/cryptiana/web/spanish3vargas4.png, A3V2-ES132C4 4 Oct 2026) and cabinet-noir's code hypotheses cited, but cabinet-noir's own cle/ file shows it has already transcribed and partly read all three (contexts from f.87r/v, f.157r, f.179v-180r), so a reading here would likely duplicate theirs; next: re-check cabinet-noir's git log for f087/f157/f179 folders before any work, then (only if still absent) build key.tsv from the PNG and read f.87 (2 blind passes + reconciliation on line crops), ~$4
- Sibling pool BL Add MS 28421 (further undeciphered Vargas Mexia letters, Tomokiyo blog 23 June 2024) - blocker: not-attempted; outside this target's volume, for the scout (QUEUE.md), not this folder; next: one BL catalogue lookup (searcharchives.bl.uk JSON) to size it, ~$0.5

## Escalation (3 Oct 2026, refreshed 4 Oct 2026)
- [x] siblings: cabinet-noir es132-vargas-mexia read (30 letters, cle/ files); Bourdeau and Aymeloglu have no folder
- [x] clear-pages: f.169 and f.177 viewed (canvases 166, 174), clerk's decipherments; other facing pages not viewed
- [x] known-keys: Cp.30 (Alcocer 1921, Devos 1950), Cipher 2 and Cipher 4 (Tomokiyo, Devos) recorded, not applied
- [x] print: Teulet 15 Oct 1578 = f.119v lower paragraph running on to f.120r L01-L04 (N4-ES132: blind S_a 0.917/0.923 vs null p99 <= 0.646) (test 0, known answer 0.90-0.92 blind); 19 Sept paragraph = f.90v L10-L26 (test 1, 4 Oct 2026: blind S_a 0.925/0.918 vs null p99 <= 0.395); Mignet appendix E and CODOIN not located
- [n/a] key-rebuild: keys are already published and rebuilt by others
- [x] image-check: Gallica canvases 166, 167, 174, 175 fetched at 1000 px
- [x] retry: catalogue record fetched (curl + browser UA, 200; digitised, Gallica btv1b10032556x, MF 8506) and the three blog threads opened (A3V2-ES132C4, 4 Oct 2026): no reading claim found
Verdict: keep going: 5 internal gaps; Cipher 3 pool f.41r, f.41v, f.50r, f.50v and f.51r gate (b) PASS on file (ES132-C3, RUN3-ES41, RUN4-ES50R, RUN4-ES41V, RUN4-ES50, 4 Oct 2026; f.41r settlement control FAIL, not applied); cheapest next: the cabinet-noir git-log re-check before any Cipher 4 or Cipher 3 work (~$0.3), then the BL Add MS 28421 catalogue lookup for the scout (~$0.5); for the two Teulet letters, AUDIT 1 is on file (A3V2-ES132A1, 4 Oct 2026: N0/N3, D2/D1, no unique solve); the f.93-95 duplicate is transcribed and aligned (A3V3-ES9396: letter-level disagreement 8.1% across both readings) and 43/113 '?' tokens are settled from it (A3V3-ES132S, control 48/50 unchanged); next the rule-7 re-derivation owed after A3V3-ES132S (~$2), then a two-crop look at the 40 unsettled candidates (~$3)

## While waiting
Nothing waits on a person: the f.89 '?' settlement from the duplicate is applied (A3V3-ES132S, 4 Oct 2026); the action that depends on nobody is now the fresh rule-7 re-derivation of the settled f.89 pages, then the next open Cipher 3 letters outside cabinet-noir's list.

## Requests by host (CS-1)
gallica.bnf.fr 4 images; archive.org 6 advancedsearch + 4 djvu downloads; github.com 3 shallow clones (2 solver repos earlier + cabinet-noir; one WebFetch); de-crypt.org 1 browser login + 12 fetches; WebSearch 9; archivesetmanuscrits.bnf.fr 1 (403, not retried). No credentials printed. Report only; no novelty classification made.

## Gate output (3 Oct 2026)
`python3 tools/intake_gate_check.py es132-vargas-mexia-1578` -> "partial (line 1) -- edition/page or full-text-search citation found within 6 lines", exit 0.
`python3 tools/gaps_check.py es132-vargas-mexia-1578` -> "OK keep-going: 5 internal gap(s), 2 step(s) untried".
`python3 tools/next_steps.py --wait-only | grep es132` -> no line.

## Test 0 (LANE-POOLS FT-B, account 1, 3 Oct 2026, 22:25-22:4x UTC by the container clock)
Gate: `python3 tools/intake_gate_check.py es132-vargas-mexia-1578` -> "partial (line 1) -- edition/page or full-text-search citation found within 6 lines", exit 0.
Tool shelf: `tools/tool_shelf.py "transcribe one cipher page from Gallica, decode with a published code key, compare with printed decipherment, shuffled-key null"` offered htrc_numeral_pages, key_decode_lattice [weak], cipher_page_detector [weak], interlinear_align, decode_neighbours: none composes a vowel-indicator syllabic key, so a target script `test0.py` was written (tools/decode_key.py does per-token lookup only). Crops: `tools/iiif_lines.py` (pasted run below).
Third party re-checked: el-descifrador/cabinet-noir git log (fresh clone 3 Oct 2026): last commit 47b6db9, 2 Oct 2026 14:15 UTC; es132 folder still the same 30 letters; f.89 and f.119 not among them. Credit: cabinet-noir's `cle/cp30_complements.tsv` (CC BY 4.0) for 35 = pr.
Key: `key.tsv`, Tomokiyo's Cp.30 table image (cryptiana.web.fc2.com/code/cp30.png, fetched 3 Oct 2026; Tomokiyo cites Devos 1950, Alcocer 1921) + the cabinet-noir 35=pr correction. No nomenclature on disk.

**Which letter Teulet prints.** Teulet vol.5 pp.167-168 (Simancas B.47 n.6, "Déchiffr. officiel", 15 Oct 1578) is ONE paragraph, the Scotland paragraph, of the three-page f.119 letter: f.119v lower paragraph decodes "a lo que pa-sas-tes con el [Bul] de [Dul] no a y que [29σ@r] [Val] que me res-pon-da-is a lo que os es-cri-ui ..." = Teulet "A lo que passastes con el embaxador de Escocia, no ay que dezir hasta que me respondais a lo que os escrivi ...". Tomokiyo's "contents seem to be different" holds for the letter's opening (f.119r opens "A ocho del passado se recibieron juntas vras cartas de 17, 19, 20 del mismo ...", not printed), not for this paragraph. So Teulet's B.47 n.6 is an extract (or the Scotland part deciphered separately); f.119's other paragraphs are not in Teulet. The 19 Sept text (B.47 n.8, "De consideracion es lo que passastes con el embaxador de Escocia ...") was not located in f.89 in this job.

Crops: `python3 tools/iiif_lines.py --ark btv1b10032556x --canvas 117 --region 1050,2700,2300,2150 --out ciphers/es132-vargas-mexia-1578/images --prefix f119v --follow-slope 300 --slope-margin 40 --debug` -> 13 lines (L01 = cut tail of the previous paragraph, not used). Debug overlay checked. Defect: with --follow-slope, band L12 was fitted onto L11's line (both blind passes flagged the duplicate); L12 was re-cut with `--centres 1270,1396,1516,1652,1777,1939` (no slope) and read by this worker alone (single read, the slope cuts its first tokens; read with the 1600 px region view). A first run without --follow-slope clipped the start of the sloping lines. Worth a fix in iiif_lines.py (flagged, not done: write scope).
Transcription: 2 blind Sonnet passes on L02-L13 (`passes/passA.tsv`, `passes/passB.tsv`; neither saw Teulet or the key), reconciled by this worker into `ciphertext.tsv` (header lists every change). The reconciler HAD read Teulet, so the reconciled number is not blind; the blind passes are the known-answer figures.

| statistic | real | 200 shuffled keys (mean / p95 / max) | N |
|---|---|---|---|
| known answer, blind pass A (token agreement with Teulet) | 75/82 = 0.915 | 0.183 / 0.293 / 0.341 | 82 key tokens |
| known answer, blind pass B | 75/83 = 0.904 | 0.182 / 0.277 / 0.325 | 83 |
| known answer, reconciled (not blind) | 95/99 = 0.960 | 0.170 / 0.265 / 0.327 | 99 |
| target L02-L06, Spanish word-cover (es17 vocabulary) | 0.983 | 0.919 / 0.971 / 0.993 (rank 6/201) | 121 letters, 14 code tokens |

Both sides normalised to one convention before the diff (lower case, accents/cedilla dropped, v->u, j->i, double letters collapsed; rule 3 notation paragraph). Code tokens are excluded from both numerator and denominator. Known-answer gate (>= 0.80 on a blind pass) met, far above the null: Cp.30 as on disk opens this hand at this transcription error.
Target: word-cover is **at ceiling** for syllabic decodes (any key gives 2-letter syllables that are mostly words; null mean 0.92), so it cannot discriminate (rule 3's ceiling clause): a non-test, neither a pass nor a negative.
Judge (`python3 tools/judge_plaintext.py specs/es132-vargas-mexia-1578.json --file <f>`; es = es17, Cervantes/Quevedo c.1605-26, ~30-50 years late and literary, not decisive):
```
cand_target.txt (L02-L06 decode, codes dropped):  FAIL language: score=-1.149, null_p99=-1.761, real_p05=-0.944, real_median=-0.82, mode=both, N=121 ; ok words: cover=0.917
cand_known.txt (L07-L13 decode, codes dropped):   FAIL language: score=-1.077, null_p99=-1.798, real_p05=-0.908, real_median=-0.818, mode=both, N=221 ; ok words: cover=0.882
cand_teulet_span.txt (Teulet's printed text, same span): FAIL language: score=-0.962, null_p99=-1.809, real_p05=-0.902, N=305
cand_teulet_full.txt (Teulet's whole paragraph):  FAIL language: score=-0.956, null_p99=-1.857, real_p05=-0.888, N=518
cand_target_shufkey.txt (target decoded with one shuffled key): FAIL language: score=-1.814, null_p99=-1.74, real_p05=-0.92, N=128
```
Teulet's own printed 1578 Spanish fails this judge, so es17 false-negatives real text of this era/register: "judge cannot decide". The target decode (-1.149) sits beside the known-answer decode (-1.077) and far from the shuffled-key floor (-1.814).

Target reading (L02-L06, key letters only, per token; bracketed = nomenclature, unread):
`en [79+] [{nel}] fu e ro la [91@s] que el [66@c] es cri ui o a lo can | nes y a ba y li o de uer man do is so br la [{dom}] de | [76@s] co de la ma ca y [65+] re is de [100@c] y si no h u | re si do [{de}] se pre te de tor na re is a ha zer | [{bim}] [{rum}+] [{Val}] que con [{bel}] se [58.@c]`
Interpretation, not graded as a reading: phrases such as "si no hu[bie]re sido", "tornareis a hazer", "escriuio" look like Spanish; [65+] is "avisa-" per cabinet-noir's complements (avis-), [{Val}] = "hasta" by the known-answer paragraph (C-grade there only).
Grades (rule 4), target L02-L06, 75 cipher tokens (+1 "/"): H 0, C 0, S 0 (no control-backed statistic for the target; the known-answer control backs the key and transcription, not this paragraph's sense), M 61 (key-decoded tokens), I 0, unread 14 (codes). Known-answer L07-L13: C-supported 75/82 (pass A) tokens agree with the printed period decipherment. No H or C on the target: cryptanalytic/key-applied result only.
Reproduce: `python3 ciphers/es132-vargas-mexia-1578/test0.py` (writes reading_*.txt, test0_result.json); `--check` exits 1 if stale.
Requests: gallica.bnf.fr 7 (4 low-res canvases/regions + 1 region 500 on a malformed ark, 1 native region, 1 info.json); cryptiana.web.fc2.com 2; archive.org 4 (2 x 500 on /download, 1 metadata, 1 datanode djvu); github.com 1 clone. No credentials used.

## cabinet-noir map (VG-CN)
Read 3 Oct 2026 (fresh shallow clone, depth 50, 12 commits total). Credit: github.com/el-descifrador/cabinet-noir (es132-vargas-mexia/, README + folder list + git log); scripts MIT, data and readings CC BY 4.0 (LICENSE, LICENSE-DONNEES.md in its repo); no code copied. Map: `cabinet_noir_map.tsv` (70 rows).
- Repo history: first commit 29 Sept 2026; es132 folder added 29 Sept (ac199aa), touched again 1 Oct (d620371, v1.2.0). Last commit of the whole repo 47b6db9, 2 Oct 2026 14:15 UTC (v1.2.1); none after it seen on 3 Oct, and none touches es132 after 1 Oct.
- Read there: 30 letters (result n°6-7, 14-21, 23-36, 39-44; folios 11, 17, 32, 34, 44, 46, 58, 71, 73, 81, 105, 113, 123, 134, 138, 142, 154, 161, 165(+167), 195, 198, 200, 211, 215, 220, 222, 228, 233, 245, 255). All 30 folders exist in the clone with chiffre.txt + lecture.md; the list equals this folder's "solver read" row exactly. Keys: Cipher 2 (3: f.11, 34, 17), Cipher 4 (3: f.198, 123, 154), Cp.30 (24). Their own grades: A 23 / B 6 / C 1 (f.255 minute printed in Teulet); their rates 79.9-97.2% by their verifier, not re-measured by me. They are solver readings with published keys (Tomokiyo, Alcocer 1921, Devos 1950), none a key they cracked.
- Not read there (open in our table): 30 Cipher 3 folios (incl. f.89 and f.119, the two Teulet "Déchiffr. officiel" candidates, neither in their list), 3-5 Cipher 4 (87, 157, 179, 136?, 148?), f.273, f.26-27 (they also leave f.26r uncounted). f.3-4 is Tomokiyo's, f.169/f.177 are clerk clear copies.
- Consequence: the 30 CN letters are found-solved candidates for those letters (a verifier classifies, rule 10); only the 30+5+2 open folios stay targets. Dates of the open letters are not in this folder's table, so the TSV leaves them blank (next: read dates from Tomokiyo's TOC, no cost beyond disk).
- Note: "n°39" in CN's table is a result number (f.71), unrelated to our open folio 39.

## Test 1 (LANE-RUN1 RUN1-ES132, account 1, 4 Oct 2026, 00:47-01:0x UTC by the container clock)
Gate: `python3 tools/intake_gate_check.py es132-vargas-mexia-1578` -> "es132-vargas-mexia-1578: partial (line 1) -- edition/page or full-text-search citation found within 6 lines", exit 0.
Scope: `cabinet_noir_map.tsv` rows 89 and 119 both `cn_read = no`; neither page dropped. Pre-registration `PREREG_test1.md` committed and pushed (e8c71b2a) before any f.90v/f.119r decode.
**Where Teulet's 19 Sept 1578 text is.** The f.89 letter runs f.89r-f.91r (canvases 86-88; signed "De Madrid a xix de Sept.e MDLXXVIII"); Teulet vol.5 pp.161-162 (Simancas B.47 n.8, "Déchiffr. officiel"; `teulet_19sep1578.txt`, IA relationspolitiq05teul djvu lines 7922-7943) prints ONE paragraph of it, the Scotland paragraph, which is f.90v L10-L26 ("de [ho] es lo que pa-sa-tes con el [Bul] de [Dul] y se-ña-la..." = "De consideracion es lo que passastes con el embaxador de Escocia, y señaladamente ..."). As with f.119, the rest of the letter is not in Teulet. [ho] = "consideracion" by position only (C-context, one occurrence).
es16 corpus: `es16/build_es16.py` keeps Teulet vol.5 Spanish paragraphs (844 of 3,936 OCR paragraphs, 695,390 chars), cuts the known-answer window (19 Sept-27 Oct 1578), 5 chronological folds. Leave-one-file-out (`tools/judge_plaintext.py --holdout`): N=300 blended false-negative 60.7% (folds 48.5-66.5%); N=600 70.3% (65.5-76.5%). The standard judge line (real_p05) is therefore unusable with this corpus (its in-sample real_p05 sits far above held-out prose); as pre-registered it is reported, not gated. One source volume, 5 folds: reliability of any real_p05 verdict here is unknown (rule 3 es17c lesson). The gate (b) statistic is relative to decode-level nulls instead.
Crops (pasted):
```
python3 tools/iiif_lines.py --ark btv1b10032556x --canvas 88 --region 280,850,3000,3950 --out ciphers/es132-vargas-mexia-1578/images --prefix f90v --follow-slope 300 --slope-margin 40 --debug
 -> region 3000x3950, 27 lines, 27 bands x 2 segments; pitch 134; slopes -0.008..-0.036; wrote 54 crops
python3 tools/iiif_lines.py --ark btv1b10032556x --canvas 116 --region 3350,1850,2950,2850 --out ciphers/es132-vargas-mexia-1578/images --prefix f119r --follow-slope 300 --slope-margin 40 --debug
 -> region 2950x2850, 20 lines, 20 bands x 2 segments; pitch 134; wrote 40 crops
```
Both overlays checked by eye (f90v 27 = 9 + 17 Teulet lines + 1; f119r L01 = "Qual ..." to L20; L09 = short paragraph end). No duplicated band this time.
Transcription: 2 blind Sonnet passes per page (crop paths only, no key, no text). Notation normalised mechanically by `passnorm.py` for both passes alike ('e'->ρ, 'ι'->⊣, trailing '6' on base+6 >= 38 -> σ, mark order). The ι map was first ι->σ and was revised to ι->⊣ after the first scoring run, from the glyph (test 0's reconciled 2⊣); the numbers below are all from the revised map, and pass A has no ι so its numbers did not move.
err_2reader (token level after normalisation): **f.90v 62/457 = 13.6%**; **f.119r 82/366 = 22.4%** (mostly ρ vs σ on one tail shape).
Reconciliation: f.90v unprinted lines L01-L09, L27 settled by this worker from the crops; f.90v Teulet lines L10-L26: A/B agreement kept, every disagreement kept as pass A's token marked '?', never settled by eye (this worker had read Teulet). f.119r: all 62 disagreements settled by a third blind Sonnet call from the crops only (`passes/f119r_arbitration.tsv`: 44 B, 13 A, 5 own, 9 still '?'), so neither the decode's Spanish-ness nor this worker chose between readings.

Results (`python3 test1.py`; `--check` exits 1 if stale; `test1_result.json`). Nulls computed before the target in each run.
| page / part | text | statistic | real | null 1 (p99) | null 2 (p99) | gate |
|---|---|---|---|---|---|---|
| f.90v Teulet lines (a) | blind pass A | S_a char-align | 0.925 (tokens 217/249 = 0.871) | key shuffles 0.391 | wrong-Teulet windows 0.347 (501) | PASS |
| f.90v Teulet lines (a) | blind pass B | S_a | 0.918 (218/250 = 0.872) | 0.395 | 0.352 | PASS |
| f.90v unprinted L01-L09, L27 (b) | blind pass A | S_b es16 4-gram | -1.064 (318 letters) | token-order shuffles -1.419 | key shuffles -1.837 | PASS |
| f.90v unprinted (b) | blind pass B | S_b | -1.112 (320) | -1.418 | -1.797 | PASS |
| f.90v unprinted (b) | reconciled | S_b | -1.048 (322) | -1.396 | -1.801 | PASS |
| f.90v Teulet lines, calibration (b) | pass A / B | S_b | -1.229 / -1.277 | -1.432 / -1.428 | -1.910 / -1.896 | PASS (gate (b) has power at this N) |
| f.119r all 20 lines (b) | blind pass A | S_b | -1.268 (708) | -1.427 | -1.861 | PASS |
| f.119r (b) | blind pass B | S_b | -1.228 (700) | -1.446 | -1.867 | PASS |
| f.119r (b) | reconciled | S_b | -1.158 (703) | -1.435 | -1.861 | PASS |
| f.119v (supplementary, not pre-registered: test 0's page re-scored) | pass A / B (a) | S_a | 0.941 / 0.932 | 0.485 / 0.483 | 0.532 / 0.524 | PASS |
| f.119v unprinted L02-L06 (b) | pass A / B | S_b | -1.376 / -1.239 (120 letters) | -1.463 / -1.358 | -1.748 / -1.731 | PASS (narrow on pass A) |
ARM-C1: the median token-order-shuffled decode FAILs the standard judge on every page and pass (it sits near -1.50 against a judge null_p99 near -1.95 and real_p05 near -0.78), so the judge is not voided by the shuffled target. But the standard judge FAILs every real decode too, including the known-answer decode and (per the holdout) most real held-out Teulet prose, so judge PASS/FAIL says nothing here; only the pre-registered decode-level gate is read.
Orthogonality (rule 3): token-order shuffles change the 4-gram contexts across syllable joins, key shuffles change the letters, wrong-Teulet windows change the reference; each can and does move its statistic (the shuffled values above differ from the real ones). The order shuffle keeps within-token syllables, so it is the closer null, as stated in the PREREG.
Grades (rule 4, reconciled text, `test1_result.json` grades_reconciled): f.90v H 0, C 217 (key tokens agreeing with Teulet's printed decipherment), S 0, M 188, I 0, U 48 (codes, cursive words, unreadable). f.119r H 0, C 0, S 0, M 330, I 0, U 33. No H or C on the unprinted text: key-applied, cryptanalytic result only. Code values: none assigned beyond test 0's C-context [Bul]/[Dul]/[Val]; cabinet-noir complements not consulted in this job.
Readings: `reading_f90v.txt`, `reading_f119r.txt` (bracketed = unread code). Sense, not graded, by eye: f.90v L09 "lo que toca a la naue-ga-cion de las indias", L27 "... haueis hecho en lo del trigo"; f.119r L10-L20 "me pesa del principio que dezis se ha dado en esa villa a las predicas ... y resistir a esta tempestad ... que el [Rey?] hiziese rostro y severo en los que se han atrevido a introduzir una tan grave ... con la [code] que la materia requiere". Reported as found; not searched in print in this job beyond Teulet vol.5 (not in Teulet: these lines are outside both printed paragraphs).
Not done (pacing, Usage 7): f.89r, f.89v, f.90r, f.91r, f.119v upper paragraph, f.120r; the spec's `cheap_test_done` (specs/ is outside this job's write scope: suggestion for the lane orchestrator to copy the table above).
Requests: archive.org 3 (1 download 500, 1 metadata, 1 datanode djvu); gallica.bnf.fr 11 (7 x 1000 px canvases, 2 info.json, 2 native regions). No credentials used. Subagent calls: 5 Sonnet (4 blind passes + 1 arbitration).

## Test 2 (LANE-RUN2 RUN2-ES132, account 1, 4 Oct 2026, 02:46-02:5x UTC by the container clock)
Gate: `python3 tools/intake_gate_check.py es132-vargas-mexia-1578` -> "es132-vargas-mexia-1578: partial (line 1) -- edition/page or full-text-search citation found within 6 lines", exit 0.
Scope: `cabinet_noir_map.tsv` rows 89/119 `cn_read = no`; fresh cabinet-noir clone 4 Oct 2026 ~02:48 UTC: last commit still 47b6db9 (2 Oct), no f.89/f.119 folder. Nothing dropped. `PREREG_test2.md` committed (57afba26) and `test2.py` committed (797275bb) before any f.89r/f.89v decode.
Pages done: **f.89r** (canvas 86 right, 23 lines: clear opening + cipher) and **f.89v** (canvas 87 left, 26 bands, three paragraphs). Neither is printed by Teulet, so only gate (b) ran. f.119v upper not started (pacing, below).
Crops (pasted):
```
python3 tools/iiif_lines.py --ark btv1b10032556x --canvas 86 --region 3450,1580,2950,3200 --out ciphers/es132-vargas-mexia-1578/images --prefix f89r --follow-slope 300 --slope-margin 40 --debug
 -> 23 bands x 2 segments, pitch 135; wrote 46 crops
python3 tools/iiif_lines.py --ark btv1b10032556x --canvas 87 --region 520,880,2720,3980 --out ciphers/es132-vargas-mexia-1578/images --prefix f89v --follow-slope 300 --slope-margin 40 --debug
 -> 26 bands x 2 segments, pitch 132; wrote 52 crops (first run with h=3850 clipped the last line; re-cut, first run's files deleted)
```
Both overlays checked by eye; no duplicated band; f.89v's right edge is the gutter (last characters of some lines may be in the binding).
Notation change from test 1: blind passes wrote above-marks by SHAPE (`run2/pass_prompt_f89r.md`, `_f89v.md`), mapped by `test2.py` before decode: hat->@n, bar->@s, acute->@l, tilde->@m, small r-shaped mark->@r, two dots->@2, from test 1's f.90v Teulet lines (L10: bar 4 = "es", hat 7ρ = "con", acute 4 = "el"; L05 tilde 17σ@m, r-mark 24.@r). The f.89r passes first got one shape "@tilde" for both ~ and the r-mark; the split was sent to both passes mid-run (logged in the prompt file); pass B then used @rmark throughout, so f.89r's @m/@r may be under-separated. cross-above and other marks are dropped (no letter).
err_2reader (token level, after normalisation): **f.89r 88/445 = 19.8%**; **f.89v 47/433 = 10.9%**. err_true not measurable (no benchmark item of this hand).
Reconciliation (`run2/reconcile_f89r.py`, `run2/reconcile_f89v.py`; disagreement lists `run2/*_disagreements.tsv`): this worker, from the crops/overlays by shape; no printed text exists for these lines and the key was not consulted per span. Systematic: looped e-tail = ρ (pass A wrote σ), "2ι3" = 2⊣ 3, "1ı" without top bar = 11. Spans not settled by eye kept and flagged '?': 44 tokens on f.89r, 36 on f.89v.

Results (`python3 test2.py`; `--check` exits 1 if stale; `test2_result.json`). Nulls first in each run.
| page | text | key letters | S_b | order-shuffle p99 | key-shuffle p99 | gate (b) |
|---|---|---|---|---|---|---|
| f.89r | blind pass A | 853 | -1.203 | -1.439 | -1.870 | PASS |
| f.89r | blind pass B | 817 | -1.183 | -1.396 | -1.831 | PASS |
| f.89r | reconciled | 863 | -1.116 | -1.436 | -1.854 | PASS |
| f.89v | blind pass A | 810 | -1.205 | -1.422 | -1.848 | PASS |
| f.89v | blind pass B | 820 | -1.177 | -1.404 | -1.853 | PASS |
| f.89v | reconciled | 820 | -1.176 | -1.412 | -1.855 | PASS |
All pages are over 250 key letters, so the pre-registered f.90v-prefix calibration was not triggered; test 1's f.90v known-answer lines (504 letters) remain the power demonstration. ARM-C1: the median order-shuffled decode fails the standard judge on every page and pass (not voided); the standard judge also fails every real decode (judge_real_p05 about -0.77) -- es16 held-out false negative 60.7-70.3%, one volume, 5 folds: judge PASS/FAIL says nothing here. Gate (b) PASS = weak support that the key-applied text is Spanish-like beyond its own syllable inventory, nothing more.
Grades (rule 4, reconciled): f.89r H 0, C 0, S 0, M 410, I 0, U 35; f.89v H 0, C 0, S 0, M 386, I 0, U 42. No H or C: key-applied, cryptanalytic result only. No nomenclature value assigned.
Readings: `reading_f89r.txt`, `reading_f89v.txt`. Sense, not graded, by eye: f.89r L01-L03 "... [cartas] todas contienen [cal?]idades que fue bien escriuirmelas, y señaladas las que tocan a [{Ja}] de Alanzon ..." (Alençon), L10-L11 "... prohibir de ueras y castigar con rigor lo que ...", L17 "con comunicacion y aprobacion del ...", L18 "lo que me embiastes", L22-L23 "os hazer saber ... al monesterio"; f.89v L08-L09 "con las palabras que me parescio conuenir", L13 "todo lo que ha hecho el de Alanzon", L22-L23 "lo primero de la uisita satisfazer ... lo segundo le dixe". Reported as found; not searched in print in this job beyond Teulet vol.5 (Teulet prints only f.90v's paragraph of this letter).
Not done (pacing: session cost not visible to this worker; two pages = 4 Sonnet passes + 2 reconciliations, estimated near the 80% line of the USD 8 cap): f.119v upper, f.120r, f.90r, f.91r.
Requests: gallica.bnf.fr 6 (2 x 1000 px canvases, 1 info.json, 3 native regions incl. one re-cut); github.com 1 shallow clone. Subagent calls: 4 Sonnet (blind passes). No credentials used.

## Test 2 continued (LANE-NEAR4 N4-ES132, account 2, 4 Oct 2026, 04:17-04:3x UTC by the container clock)
Brief: `.claude/briefs/runs/2026-10-04-ytbiz-near4-wave1.md` job N4-ES132. Intake gate pasted by the lane at 04:13 UTC ("partial (line 1) -- edition/page or full-text-search citation found within 6 lines", exit 0).
Scope: `cabinet_noir_map.tsv` row 119 `cn_read = no`; fresh depth-5 clone of el-descifrador/cabinet-noir 4 Oct 2026: last commit still 47b6db9 (2 Oct 2026), no f119/f120 folder. Nothing dropped.
Pre-registration: `PREREG_test2.md` amendment 1 (pushed f42c7d6e before any crop or decode): pages f.119v upper (`f119vU`) and f.120r, same statistic/nulls/gate, plus an overlap clause for f.120r. `test2.py` gained `f120r` in PAGES and, after the overlap was seen, the `gate_a` function (PREREG_test1 (a) unchanged: S_a, N1 200 key shuffles, N2 501 wrong-Teulet windows).
Crops (pasted):
```
python3 tools/iiif_lines.py --ark btv1b10032556x --canvas 117 --region 900,1020,2500,1780 --out ciphers/es132-vargas-mexia-1578/images --prefix f119vU --follow-slope 300 --slope-margin 40 --debug
 -> 12 bands x 2 segments, pitch 143; wrote 24 crops
python3 tools/iiif_lines.py --ark btv1b10032556x --canvas 117 --region 3600,1000,2600,1390 --out ciphers/es132-vargas-mexia-1578/images --prefix f120r --follow-slope 300 --slope-margin 40 --debug
 -> 8 bands x 2 segments, pitch 142; wrote 16 crops (a first cut with h=1320 risked clipping L08's lower half; re-cut, first run's files deleted)
```
Both overlays checked by eye: f119vU 12 lines ("12. 25σ 24ρ 15ρ ..." to "... 24. 1 /", ending just above test 0's L01); f120r 4 + 4 lines, the clear dating line "De Madrid a xv de Octubre ..." left out. Canvas 117 is the f.119v/f.120r opening (6673 x 5452). f.119v's right edge is the binding; show-through from the verso on both pages.
Transcription: 2 blind Sonnet passes per page (`run2/pass_prompt_f119vU.md`, `_f120r.md` = the f.89v prompt with page/line count changed, plus one sentence for both passes alike on show-through and the binding edge). err_2reader (token level after test2's shape map + passnorm): **f.119v upper 39/212 = 18.4%** (mostly ρ vs σ on the looped e-tail, and '+' vs u-hook on '20-1'-shaped groups); **f.120r 15/145 = 10.3%**. err_true not measurable.
Reconciliation (`run2/reconcile_f119vU.py`, `run2/reconcile_f120r.py`; spans `run2/*_disagreements.tsv`): this worker from the crops (2400 px) by shape, before reading any Teulet text; looped e-tail = ρ (as f.89r/v), a group closed by a horizontal stroke ending in a down-tick = ⊣, distinct from the crossed '+'. f.119v upper: 12 tokens left '?'. **Overlap found:** the first decode showed that f.120r L01-L04 continue Teulet's printed 15 Oct 1578 paragraph (test 0's f.119v lower paragraph runs on overleaf), so per the amendment's clause those four lines were re-reconciled by A/B agreement only (5 disagreement spans set to pass A, flagged '?') and scored under (a); L05-L08 (the second paragraph) stay under (b).

Results (`python3 test2.py`; `--check` exits 1 if stale; `test2_result.json`). Nulls first in each run. f.89r/f.89v numbers unchanged by this job.
| page / part | text | statistic | real | null 1 (p99) | null 2 (p99) | gate |
|---|---|---|---|---|---|---|
| f.120r L01-L04, printed (a) | blind pass A | S_a char-align | 0.917 (tokens 51/62 = 0.823) | key shuffles 0.590 | wrong-Teulet windows 0.617 (501) | PASS |
| f.120r L01-L04 (a) | blind pass B | S_a | 0.923 (52/62 = 0.839) | 0.588 | 0.646 | PASS |
| f.120r L01-L04 (a) | reconciled (A/B agreement, A on splits) | S_a | 0.917 (51/62) | 0.590 | 0.617 | PASS |
| f.119v upper L01-L12 (b) | blind pass A | S_b es16 4-gram | -1.260 (373 letters) | token-order shuffles -1.409 | key shuffles -1.825 | PASS |
| f.119v upper (b) | blind pass B | S_b | -1.385 (374) | -1.442 | -1.884 | PASS (narrow) |
| f.119v upper (b) | reconciled | S_b | -1.171 (375) | -1.422 | -1.848 | PASS |
| f.120r L05-L08 (b) | blind pass A | S_b | -1.118 (139) | -1.315 | -1.698 | PASS |
| f.120r L05-L08 (b) | blind pass B | S_b | -0.994 (141) | -1.374 | -1.756 | PASS |
| f.120r L05-L08 (b) | reconciled | S_b | -0.992 (143) | -1.367 | -1.740 | PASS |
| f.120r L05-L08 calibration (< 250 letters: same-length prefix of f.90v known-answer lines) | pass A / B / reconciled | S_b | -1.156 / -1.236 / -1.142 | -1.377 / -1.367 / -1.341 | -1.787 / -1.793 / -1.777 | PASS (gate (b) has power at this N) |
The (a) nulls are high (0.59-0.65) because the f.120r decode (about 130 letters) is matched against the whole 531-letter paragraph; the blind passes still clear both p99s by 0.27-0.33 and test 0's 0.80 known-answer bar. ARM-C1: the median order-shuffled decode fails the standard judge on both pages and all passes (not voided); the standard judge also fails every real decode (es16 held-out false negative 60.7-70.3%, one volume, 5 folds): judge PASS/FAIL says nothing here. Gate (b) PASS = weak support that the key-applied text is Spanish-like beyond its own syllable inventory, nothing more.
Grades (rule 4, reconciled): f.119v upper H 0, C 0, S 0, M 187, I 0, U 25. f.120r L05-L08 H 0, C 0, S 0, M 67, I 0, U 3. f.120r L01-L04 (printed) H 0, C 51 (key tokens agreeing with Teulet's printed period decipherment), S 0, M 11, I 0, U 11. No H; C only on the printed lines; the unprinted text is a key-applied, cryptanalytic result. No nomenclature value assigned.
Readings: `reading_f119vU.txt`, `reading_f120r.txt`. Sense, not graded, by eye: f.119v upper L01 "he uisto lo que e[scri]uio ... y os comunico", L02 "... al [{Ja}] de Alanson y ...", L03 "tienen aparencia de bien", L05-L06 "no le iueis dando a entende[r] que yo lo entienda sino que lo creo", L07 "que procure el [58] quitandole de ... todas", L09-L10 "... de que se a sufficiente y ... de lo que os respondiere", L11 "la [{bum}] que el [{Ja}] de Guisa ha tray[do]"; f.120r L06-L08 (unprinted) "que se hazen sobre lo de las piraterias, todauia las yreis continuando, siquiera [por]que no puedan dezir que no se haze caso de las ...", L05 "se puede tener poca [{gal}] de sacar fruto de la [{Ra}]". f.120r L01-L04 = Teulet "... en que parte y a que tiempo havrian de servir ... ganan los [capitanes] ... en aquel [reyno]. Y embiareys relacion de todo para que tanto mejor se pueda mirar y resolver lo que convenga". Reported as found; the unprinted lines were not searched in print in this job beyond Teulet vol.5.
Consequence for the letter: f.119 (15 Oct 1578) now has every page through gate (a) or (b): f.119r (test 1), f.119v upper (this job), f.119v lower (test 0, printed), f.120r (this job). The f.89 letter still lacks f.90r and f.91r.
Requests: gallica.bnf.fr 5 (1 x 1400 px canvas, 1 info.json, 3 native regions incl. one re-cut); github.com 1 shallow clone. Subagent calls: 4 Sonnet (blind passes). No credentials used.

## Test 2 continued (LANE-NEAR4 N4-ES132B, account 2, 4 Oct 2026, 04:35-04:4x UTC by the container clock)
Brief: `.claude/briefs/runs/2026-10-04-ytbiz-near4-wave2.md` job N4-ES132B. Intake gate pasted by the lane at 04:13 UTC ("partial (line 1) -- edition/page or full-text-search citation found within 6 lines", exit 0).
Scope: `cabinet_noir_map.tsv` row 89 `cn_read = no`; fresh depth-5 clone of el-descifrador/cabinet-noir 4 Oct 2026 04:36 UTC: last commit still 47b6db9 (2 Oct 2026), es132-vargas-mexia/ (32 entries) has no f089/f090/f091 folder. Nothing dropped.
Pre-registration: `PREREG_test2.md` amendment 2 (pushed f4a2c483 before any crop or decode): pages f.90r and f.91r, same statistic/nulls/seeds/gate (b)/calibration rule, overlap clause as amendment 1. `test2.py` gained `f90r`, `f91r` in PAGES, nothing else.
Crops (pasted):
```
python3 tools/iiif_lines.py --ark btv1b10032556x --canvas 87 --region 3580,900,2680,3900 --out ciphers/es132-vargas-mexia-1578/images --prefix f90r --follow-slope 300 --slope-margin 40 --debug
 -> 27 bands x 2 segments, pitch 137; wrote 54 crops (a first cut at x=3740, w=2510 clipped the second paragraph's line starts; re-cut, first run's files and manifest entries deleted)
python3 tools/iiif_lines.py --ark btv1b10032556x --canvas 88 --region 3650,860,2650,1020 --out ciphers/es132-vargas-mexia-1578/images --prefix f91r --follow-slope 300 --slope-margin 40 --debug
 -> 7 bands x 2 segments, pitch 128; wrote 14 crops (a first cut at y=940 clipped L01's above-marks; re-cut, first run's files and manifest entries deleted)
```
Both overlays checked by eye: f90r 21 + 6 lines ("12+ 29σ 4 6ρ quam ..." to "... 6. 15+ /"), left edges intact; f91r 3 + 4 lines, the clear dating line "De Madrid a xix de Sept.e MDLXXVIII" and the signatures left out. Canvas 87 is 6614 x 5452, canvas 88 6598 x 5452 (info.json).
Transcription: 2 blind Sonnet passes per page (`run2/pass_prompt_f90r.md`, `_f91r.md` = the f.120r prompt with page/line count changed, plus one sentence for both passes alike: leave out marginal numerals standing alone in the far right margin). err_2reader (token level after test2's shape map + passnorm): **f.90r 67/495 = 13.5%** (12 of the 58 spans are notation only: pass A wrote the letter y as `{y}`, which the prompt allows and test2's err2 counts; the rest are mostly ρ vs σ on the looped e-tail and above-marks present in one pass only); **f.91r 12/122 = 9.8%** (8 spans: pass A read the '1' + long-s digit + tail as 12ρ, pass B as 15ρ). err_true not measurable.
Reconciliation (`run2/reconcile_f90r.py`, `run2/reconcile_f91r.py`; spans `run2/f90r_disagreements.tsv`, `run2/f91r_disagreements.tsv`): this worker, before reading `teulet_19sep1578.txt` or `reading_f90v.txt`, by three kinds of decision written in each script's docstring: by eye from the 2400 px crops (f.90r L01, L10, L12; f.91r L01, L04); by the earlier pages' systematic rules ('1fe' = 15ρ, as f.89r/v and f.90v: 15ρ 42 times, 12ρ never; looped e-tail = ρ; '20-1' = ⊣; `{y}` = y); everything else (marks seen by one pass only, digit splits not checked by eye) kept and flagged '?': **31 tokens on f.90r, 2 on f.91r**. The rules were applied without the key being consulted per span.
Overlap: after both reconciliations, the decodes were compared with Teulet's printed 19 Sept 1578 paragraph (Scotland, Guaras, Mendoza). No line of f.90r or f.91r continues it, so gate (a) does not apply; both pages are scored under (b) only, as pre-registered.

Results (`python3 test2.py`; `--check` exits 0 on the committed outputs; `test2_result.json`). Nulls first in each run. f.89r/f.89v/f.119vU/f.120r numbers unchanged by this job.
| page | text | key letters | S_b | order-shuffle p99 | key-shuffle p99 | gate (b) |
|---|---|---|---|---|---|---|
| f.90r | blind pass A | 863 | -1.131 | -1.393 | -1.832 | PASS |
| f.90r | blind pass B | 891 | -1.121 | -1.384 | -1.825 | PASS |
| f.90r | reconciled | 899 | -1.080 | -1.367 | -1.825 | PASS |
| f.91r | blind pass A | 218 | -1.222 | -1.396 | -1.759 | PASS |
| f.91r | blind pass B | 218 | -1.211 | -1.325 | -1.725 | PASS |
| f.91r | reconciled | 222 | -1.212 | -1.344 | -1.767 | PASS |
| f.91r calibration (< 250 letters: same-length prefix of f.90v known-answer lines) | pass A / B / reconciled | | -1.189 / -1.257 / -1.191 | -1.321 / -1.393 / -1.374 | -1.804 / -1.811 / -1.821 | PASS (gate (b) has power at this N) |
Margins over the stricter (order-shuffle) null: f.90r 0.26-0.29, f.91r 0.11-0.17 (pass B narrowest at 0.114). ARM-C1: the median order-shuffled decode fails the standard judge on both pages and all passes (medians -1.43 to -1.51 vs judge null_p99 about -1.9 to -2.0 and real_p05 about -0.77 to -0.81): not voided. The standard judge also fails every real decode (es16 held-out false negative 60.7-70.3%, one volume, 5 folds): judge PASS/FAIL says nothing here. Gate (b) PASS = weak support that the key-applied text is Spanish-like beyond its own syllable inventory, nothing more.
Grades (rule 4, reconciled): f.90r H 0, C 0, S 0, M 429, I 0, U 65. f.91r H 0, C 0, S 0, M 113, I 0, U 7. No H or C: key-applied, cryptanalytic result only. No nomenclature value assigned.
Readings: `reading_f90r.txt`, `reading_f91r.txt`. Sense, not graded, by eye (Spanish): f.90r L08-L10 "lo que uoles habra ... y esto aunque quede abierta la puerta ... que segun el [100] de las ... con que ay se procediere", L13-L16 "y a uos os hauemo querido [..] de lo que es con el se passo ... lo tengais entendido y que me ha parescido proceder por esta uia por lo que importa no dar [{Vum}] a que se dexe de ...", L22-L25 "si hauieredes hauido alguna de las [..] falsa[s] ... en esa uilla ... el de Alanzon y el de Bearne que dezis contienen que le offrescia yo fauor ... que se apoderen de ..."; f.91r L01-L03 "... si se huuiere de [V]sar de la licencia ... y de lo que mas se huuiere de hazer", L04-L07 "... de lo que mas entendieredes de los andamientos y pretension de [..] Bearne, y a don Sancho de Leyua de lo que uieredes conuenir ...". Reported as found; not searched in print in this job beyond Teulet vol.5 (Teulet prints only f.90v's paragraph of this letter).
Consequence for the letter: the f.89 letter (19 Sept 1578, f.89r-f.91r) now has every page through gate (a) or (b): f.89r, f.89v (test 2), f.90r (this job), f.90v (test 1: Teulet lines (a), the rest (b)), f.91r (this job). With N4-ES132, both Teulet "Déchiffr. officiel" letters (f.89 and f.119) are through on every page.
Requests: gallica.bnf.fr 8 (2 x 1200 px canvases, 2 info.json, 4 native regions incl. two re-cuts), >= 2 s apart; github.com 1 shallow clone. Subagent calls: 4 Sonnet (blind passes). No credentials used.

## RD7 + print check (4 Oct 2026)
Worker A3V2-ES7 (account 3, for LANE-A3V2; brief `.claude/briefs/runs/2026-10-04-acct3-a3v2-wave1.md`), 04:56-05:0x UTC by `date -u`. A fresh session: nothing in this folder had been seen before, and NOTES.md, `reading_*.txt` and `test*_result.json` were not opened until the re-derivation was done.
**Rule 7 (full write-up: `RD7-2026-10-04.md`).** The folder was copied to the scratchpad without NOTES.md, the readings and the result JSONs; `test0.py`, `test1.py`, `test2.py` were run there from `key.tsv` and the committed `ciphertext_*.tsv` alone, then `--check` on each in the real folder (all three: `OK: committed outputs match`, exit 0). Token-by-token diff of the fresh readings against the committed ones, per line:
| page | tokens | identical | differing | M (committed) | U (committed) | verdict |
|---|---|---|---|---|---|---|
| f.89r | 445 | 445 | 0 | 410 | 35 | SAME |
| f.89v | 428 | 428 | 0 | 386 | 42 | SAME |
| f.90r | 494 | 494 | 0 | 429 | 65 | SAME |
| f.90v | 453 | 453 | 0 | 405 | 48 | SAME |
| f.91r | 120 | 120 | 0 | 113 | 7 | SAME |
| f.119r | 363 | 363 | 0 | 330 | 33 | SAME |
| f.119v upper | 212 | 212 | 0 | 187 | 25 | SAME |
| f.119v lower | 184 | 184 | 0 | 160 | 24 | SAME |
| f.120r | 143 | 143 | 0 | 129 | 14 | SAME |
**rule-7 SAME 2842 of 2842**; every page differs by 0 tokens against an M count of 113-429, so none goes back. The three result JSONs and `reading_known.txt`/`reading_target.txt` are byte-identical as well. (The M column counts every key-decoded token; on the Teulet-printed lines the agreeing tokens are C in the result JSONs.) This says the committed readings are what the committed key and transcriptions produce; it says nothing about transcription accuracy (err_2reader 9.8-18.4% per page), the nomenclature (U) or novelty (rule 10).
**Print check.** `phrases.txt`: one positive control printed by Teulet ("no conviene determinarnos sin mucho fundamento", f.119v lower) and 11 phrases from the unprinted paragraphs, joined into words by this worker from the M-graded syllables. `sources.tsv`: IA relationspolitiq05teul (Teulet vol.5), labibliothque01gach (Gachard 1875), antonioperezetph00mign (Mignet 1846). `python3 tools/print_check.py ciphers/es132-vargas-mexia-1578 --max-requests 150`, 04:59-05:0x UTC, summary pasted:
```
12 phrases, 3 listed sources: 96 rows, 30 with hits -> ciphers/es132-vargas-mexia-1578/print-check.tsv
requests: archive.org 3, be-api.us.archive.org 24, www.googleapis.com 12, api.openalex.org 12, api.semanticscholar.org 3, api.crossref.org 12
  api.semanticscholar.org: blocked: HTTP 429 on .../graph/v1/paper/search?...query="andamientos y pretension"
```
What the 30 hit rows are (`print-check.tsv`, read row by row; 3 further be-api snippet calls by this worker):
- Control: "no conviene determinarnos sin mucho fundamento" found in Teulet (ia-global relationspoliti04teulgoog; Google Books 7 copies of Relations politiques 1862). The listed Teulet djvu itself answered HTTP 500 on archive.org/download (as on 3-4 Oct), so the ia-global route is what found it.
- "el de Alanzon y el de Bearne": 1 IA item + 2 Google Books copies, Cabrera de Cordoba, Don Filipe el prudente (1625): narrative prose ("El de Alanzon, y el de Bearne estuvieron ... a lo menos mirados"), not a letter text.
- "tan injusta y de tan mal nombre": 9 IA items + 30 Google Books, all CODOIN/Semanario erudito copies of one passage ("una novedad tan injusta y de tan mal nombre y estimacion, como seria dexar ...", CODOIN vol. 103 Correspondencia de los principes de Alemania): a stock chancery phrase in another document, not this letter.
- "sobre lo de las piraterias" (Bibliografia militar de Espana 1876; "Anos 1568-1571" 1952), "lo que toca a la navegacion de las indias" (CODOIN, 7 items), "don Sancho de Leyva" (362 items: a person's name), "circunstancias que a esto tocan" / "se ha dado en esa villa a las predicas" / "se han atrevido a introduzir" / "prohibir de veras y castigar con rigor" (Google Books only, 13-351 volumes each, common phrases): none names Vargas Mexia, Espagnol 132 or a 1578 letter in its snippet or title.
- ia-global no hits: "andamientos y pretension", "circunstancias que a esto tocan", "prohibir de veras y castigar con rigor", "se ha dado en esa villa a las predicas", "se han atrevido a introduzir", "con las palabras que me parescio convenir". Gachard and Mignet djvu texts: no hits on any phrase. OpenAlex: only "don Sancho de Leyva" (18 works about the person). CrossRef: relevance noise only. Semantic Scholar: 2 phrases answered (noise), then 429 (keyed; its 1 request/s pool), 10 phrases not searched. Google Books: "lo que toca a la navegacion de las indias" not searched (HTTP 503).
These are search results on this date by this method, not a novelty verdict (rule 10); the verifier's families (b)-(g) are still owed. Not found: any print of the unprinted paragraphs' wording by this method.
Requests: archive.org 3 (djvu downloads; Teulet 500), be-api.us.archive.org 27 (24 by the tool + 3 snippet calls), www.googleapis.com 12 (keyed, country=US), api.openalex.org 12 (keyed), api.semanticscholar.org 3 (keyed, 429 after 2), api.crossref.org 12; gallica.bnf.fr 0. Subagent calls: 0. No credentials printed.

## Duplicate copy f.93r-f.95r (A3V3-ES9396, account 3, 4 Oct 2026, 06:12-06:2x UTC by the container clock)
Brief: `.claude/briefs/runs/2026-10-04-acct3-a3v3-wave1.md` section A3V3-ES9396. Reading and key unchanged.

**Where it is.** `tools/gallica_folio.py btv1b10032556x --anchor 86=89r --anchor 116=119r --anchor 166=169r --anchor 174=177r` (all
labels 'NP'; fit canvas = folio - 3, residuals 0); canvases 90-93 viewed at 1200 px. The duplicate is f.93r (canvas 90 right, headed
"El Rey" / "Juan de Vargas Mexia"), f.93v (91 left), f.94r (91 right), f.94v (92 left), f.95r (92 right, ends "De Madrid a XIX de
Septiembre 1578" with the king's and Çayas's signatures); f.95v/f.96r carry only show-through and the seal, f.96v blank, f.92v is the
f.89 letter's address leaf. 5 cipher pages, 113 lines. Unlike f.89r, the duplicate enciphers the clear opening: f.93r L01-L03 (about
30 tokens) are a cipher text of f.89r L01's clear "de 26, y a los 15 deste las de cinco y seis del mismo" (a known-plaintext stretch,
not used here).

**Crops (pasted commands; overlays checked, every red centre on its line; crops kept in the session scratchpad, not committed, to keep
images/ under 30 MB -- regenerate with the same commands; overlays and crop manifest in images/dup93/):**
```
python3 tools/iiif_lines.py --ark btv1b10032556x --canvas 90 --region 3300,1200,3100,3600 --out <dir> --prefix f93r --follow-slope 300 --slope-margin 40 --debug   # 23 lines
python3 tools/iiif_lines.py --ark btv1b10032556x --canvas 91 --region 550,880,2750,3950 --out <dir> --prefix f93v --follow-slope 300 --slope-margin 40 --debug    # 25 lines, right edge at the gutter
python3 tools/iiif_lines.py --ark btv1b10032556x --canvas 91 --region 3450,850,2900,3900 --out <dir> --prefix f94r --follow-slope 300 --slope-margin 40 --debug   # 25 lines
python3 tools/iiif_lines.py --ark btv1b10032556x --canvas 92 --region 550,850,2750,3900 --out <dir> --prefix f94v --follow-slope 300 --slope-margin 40 --debug    # 25 lines, gutter
python3 tools/iiif_lines.py --ark btv1b10032556x --canvas 92 --region 3650,280,2800,2200 --out <dir> --prefix f95r --follow-slope 300 --slope-margin 40 --debug   # 15 lines (L15 = clear date)
```
**Passes.** Two blind Sonnet passes per page (10 calls; prompts `run2/pass_prompt_f9*.md` = the f.89r prompt with its tilde/rmark
amendment folded in; `passes/f9*_passA/B.tsv`). Two-reader disagreement after `test2.load_pass` (`run2/dup_spans.py`): f.93r 45/436
(10.3%), f.93v 54/442 (12.2%), f.94r 63/446 (14.1%), f.94v 63/428 (14.7%), f.95r 44/311 (14.1%). Reconciled by `run2/reconcile_dup.py
<page>` with `run2/decisions_<page>.tsv` (span decisions from the overlays and crops f93r_L13_s1, f93v_L01_s1, f94r_L21_s1, made without
looking at the f.89 tokens for the span; rules: looped tail = ρ, the small r-shaped hook = @r, a cross read as a digit = '+', and one
declared mechanical rule <n>0ρ -> <n>ρ when <n>0 is not a Cp.30 base, 12 tokens). Output `ciphertext_f93r/f93v/f94r/f94v/f95r.tsv`:
2,046 tokens, 159 flagged '?'.

**Alignment** (`align_dup.py`, `--check` exits 1 if stale; outputs `dup_align.tsv`, `dup_settlements.tsv`, `dup_align_summary.json`).
Needleman-Wunsch over tokens (exact 4, same decoded text 2, same number 1, else -2, gap -3), free end gaps on the f.89 side. The whole
duplicate aligns to the whole f.89 letter, f.89r L01 tok 15 (after the clear opening) to f.91r L07 tok 14: matched span = the entire
letter, 1,927 f.89 tokens vs 2,039 duplicate tokens; 1,836 aligned pairs, 292 one-sided (203 duplicate-only, 89 f.89-only).
On the 1,578 pairs with neither token flagged '?':

| class | n | share |
|---|---|---|
| same token | 1,177 | 74.6% |
| copy variant (different token, same decoded text) | 68 | 4.3% |
| notation (declared reading convention: dup 14/14+/14. = f.89 12+/12.; 0 = 18; Q/R cursive capitals) | 34 | 2.2% |
| differ, marks only | 76 | 4.8% |
| differ, vowel sign | 53 | 3.4% |
| differ, number/word | 170 | 10.8% |

Token-level disagreement 299/1,578 = 18.9% (marks excluded: 223/1,578 = 14.1%). This is NOT err_true: it sums the f.89 reading's
errors, the duplicate reading's errors, and the clerk's own copy variants that do not decode identically token by token. The image
sample (one window, f.89v L15 vs f.93v L19, both crops viewed): every one of its 5 'differ' pairs is supported by its own image -- f.89
has 12(cross above) 8 where the duplicate spells 35_+ 24σ 7+@s, and 28+ where the duplicate has y 10 (same letters, split
differently) -- i.e. clerk re-encipherment, not reader error. So the token rate is an upper bound.
**Letter-level estimate.** Between anchor pairs (same/variant/notation), the decoded letters of both sides were compared (387 windows;
247 skipped because a side holds a code word, a '?' or an undecodable token): 139 windows differ, 252 letter edits over 2,697 + 401
letters = **8.1% letter disagreement (N = 3,098 letters)**, both readings and clerk spelling together; if the two readings are equally
reliable, about **4% per reading (err_true, this hand, letter level, upper bound)**. The token-level per-reading equivalents are 9.5%
(all) and 7.1% (number+vowel), also upper bounds. The skipped code-bearing windows are not measured.

**The 113 '?' tokens** (unprinted pages f.89r, f.89v, f.90r, f.91r; all inside the matched span): 83 meet an unflagged duplicate token,
30 do not (dup token also flagged, or a gap). Of the 83: 29 confirm the f.89 '?' token exactly; 54 differ (14 marks only, 12 vowel
sign, 28 number/word) and are written as proposals in `dup_settlements.tsv` (plus 36 rows for f.90v, Teulet's page, marked
'teulet-f90v'). Given the image sample above, a proposal is a pointer to two crops to compare, not a settlement: the rule-7 job applies
one only where the f.89 image itself supports the duplicate's token.

Requests: gallica.bnf.fr 11 (6 x 1200 px canvases 89-94, 5 native regions). Subagent calls: 10 Sonnet (blind passes); reconciliation
and alignment by this worker. No credentials used. Report only; no novelty classification.

## Duplicate settlement of the f.89 '?' tokens (A3V3-ES132S, account 3, 4 Oct 2026, 06:35-06:4x UTC by `date -u`)
Brief: `.claude/briefs/runs/2026-10-04-acct3-a3v3-wave2.md` section A3V3-ES132S. Rule pre-registered and pushed before any settlement was
computed: `PREREG_dupsettle.md` (commit 7c98044a, with frozen copies `dup_settlements_pre.tsv` / `dup_align_pre.tsv` of A3V3-ES9396's
alignment). Script `settle_dup.py` (`--check` exit 0); per-candidate decisions in `dup_settled.tsv` (old token, duplicate token, decision,
new token), summary `dup_settle_result.json`.

**Rule** (summary; the PREREG is the text): R1 the duplicate token was written by both blind readers (an `equal` opcode of passes A/B, no
reconciler decision); R2 same token / same decoded text (align_dup's clerk-variant and notation classes) + R1 -> the '?' flag is removed, the
f.89 token is kept; R3 a differing token + R1 + (a) the pair is an isolated 1:1 substitution (both neighbouring aligned pairs are anchors) +
(b) the duplicate token is not one of its notation-side forms (14, 0, R) -> the f.89 token is replaced. Only the unprinted pages f.89r, f.89v,
f.90r, f.91r; the 36 f.90v (Teulet known-answer) candidates are not applied, so test 1's calibration is untouched.

**Control** (rule 3; replacements depend on token identity, R1 and isolation, so the control can differ): 50 firm (unflagged) f.89 tokens
aligned to an unflagged duplicate token (seed 1578), run through R1-R3 as if flagged: **48/50 unchanged = 96.0% (gate >= 95%: PASS)**.
Beside it, the whole firm population: **1,143/1,218 unchanged = 93.8%** -- below 95%: the 50-token sample passes only narrowly and the
population rate says the rule would replace about 6% of tokens that were already firm. Read the 18 replacements accordingly: they move a
'?' token toward the duplicate where both copies' readers agree on the duplicate side, but about one in sixteen such moves on firm tokens
would be a clerk variant or a duplicate-side misreading, not a correction. No image look was made (not in the brief).

**Result on the 83 unprinted candidates:** 25 flag-removed (R2), 18 replaced (R3), 30 kept (R3a not isolated: re-segmented windows), 10
kept (R1: the duplicate token was a reconciler decision). **'?' tokens 113 -> 70** (f.89r 44 -> 24, f.89v 36 -> 26, f.90r 31 -> 18, f.91r
2 -> 2); of the 43 settled, 35 are key-decodable syllables and 8 are code/unreadable (U). Replacements (f.89 -> duplicate): 6.@s->6.,
17+@2->17+@l, 6ρ->{a}, 13+->131, 13->13@l, 28->26 (x2), 7σ->7+, 16σ->16+, 11σ->16+@n, 12σ->12, 17ρ@n->17ρ, {pam}+@s->{pam}+, 7ρ->7ρ@n,
60->10@s, 13@n->13@l, 15+@n->15+, 25+->15+.

**Grades** (rule 4; settled tokens M, never above the pages' own grade; test2_result.json):
| page | before M / U / '?' | after M / U / '?' | S_b reconciled before -> after (gate (b)) |
|---|---|---|---|
| f.89r | 410 / 35 / 44 | 408 / 37 / 24 | -1.116 -> -1.109 (PASS) |
| f.89v | 386 / 42 / 36 | 386 / 42 / 26 | -1.176 -> -1.177 (PASS) |
| f.90r | 429 / 65 / 31 | 430 / 64 / 18 | -1.080 -> -1.073 (PASS) |
| f.91r | 113 / 7 / 2 | 113 / 7 / 2 | -1.212 -> -1.212 (PASS) |
H 0, C 0, S 0 on these pages before and after (cryptanalytic, key-applied result). After the settlement `align_dup.py` was re-run (its
`dup_settlements.tsv` now lists only the remaining candidates; the pre-settlement state is in the `_pre` files), `test2.py` regenerated
`reading_f89r/f89v/f90r.txt`; `settle_dup.py --check`, `align_dup.py --check`, `test2.py --check`, `test1.py --check`, `test0.py --check`
all exit 0. **A fresh rule-7 re-derivation of the f.89 pages is owed after A3V3-ES132S; this worker did not do it.**
Requests: none (no network). Subagent calls: 0. Report only; no novelty classification.

## Cipher 3 pool test 1 (ES132-C3, LANE-POOLS2 account 1, 4 Oct 2026, 06:23-06:3x UTC by the container clock)
Brief `.claude/briefs/runs/2026-10-04-acct1-pools2-es132c3.md`. f.89/f.119/f.93-96 files and AUDIT.md untouched.
Step 0. `python3 tools/intake_gate_check.py es132-vargas-mexia-1578` -> "es132-vargas-mexia-1578: partial (line 1) -- edition/page or full-text-search citation found within 6 lines", exit 0.
Fresh shallow clone of el-descifrador/cabinet-noir (06:2x UTC): `git log -5` top = `47b6db9 2026-10-02 14:15:15 +0000 Version 1.2.1 ...` (unchanged since 2 Oct); `ls es132-vargas-mexia/` = README.md, cle, and the same 30 folders (f011-012 ... f255). No open Cipher 3 folio has a lecture.md there; nothing dropped from `cabinet_noir_map.tsv`.
Step 1. Six 900 px looks (canvases 34, 38, 76, 147, 178, 182 = f.37r, 41r, 79r, 150r, 181r, 185r). Chosen: **f.41r**, canvas 38 right; Tomokiyo TOC no.21 (no.21-23 = f.41, 44, 46: Philip II to Juan de Vargas Mexia, Madrid, 29 April 1578, Cipher 3, undersigned by Antonio Perez). Why: 30 full cipher lines after the clear address "Juan de Vargas Mexia |" -- the most cipher on one page of the six (f.150r and f.185r carry ~4-5 clear lines first; f.37r and f.79r are half clear). Caveat: cabinet-noir reads f.44 and f.46 of the same date; f.41 was not compared with their readings (not opened).
Step 2. Crops (pasted):
```
python3 tools/iiif_lines.py --ark btv1b10032556x --canvas 38 --region 3500,1300,3150,3800 --out ciphers/es132-vargas-mexia-1578/images --prefix f41r --follow-slope 300 --slope-margin 40 --debug
 -> 30 bands x 2 segments, pitch 121; slopes about -0.010..-0.017; wrote 60 crops (2400 px wide)
```
Overlay and an s1 contact sheet checked by eye: 30 bands = 30 text lines one-to-one (L01 = clear address + cipher, L30 = last line); no duplicated or skipped band.
2 blind Sonnet passes (`run2/pass_prompt_f41r.md` = test 2's shape notation verbatim, crop paths only) -> `passes/f41r_passA.tsv`, `_passB.tsv`. `python3 tools/reconcile_passes.py` on the load_pass-normalised passes: "lines 30 signs A 526 B 529 agree 375/534 = 70.2% (nw); disagree 159".
**err_2reader (test2.err2, token level after normalisation): 163/533 = 30.6%** -- above test 1/2's 10.9-22.4% and above TRANSCRIPTION.md's one-tenth line; per TRANSCRIPTION.md a third machine pass was not run (lookalike/owner sorter is the route for this hand if the rate is to be cut).
Reconciliation (third unit, this worker, `run2/reconcile_f41r.py`, header lists rules): from crops L02 and L07 viewed at 2400 px plus this hand's f.89-f.91 reconciled convention, rules R1 21. not 11. (u-shaped group; f.89r-91r reconciled hold 21. x83, 11. x0) 14; R2 looped tail on 7 = 7ρ (A read 77) 16; R3 6σ/64ρ -> 6ρ 11; R4 'v24' ligature = 12+ 5; R5 16 vs 161 -> 16⊣? 3; R6 15+ vs 158+ 1; R7 mark/dot seen by one reader -> marked reading, flagged 32; default (A's token, flagged) 81. Result `ciphertext_f41r.tsv`: 30 lines, 526 tokens, 105 flagged '?'. The key was not consulted per span (R1 is a shape convention carried from f.89; it is also the most frequent syllable 'que', said so).
Step 3. design_prior (pasted):
```
python3 tools/design_prior.py --no-write ciphers/es132-vargas-mexia-1578/ciphertext_f41r.tsv
 526 tokens, 189 distinct, inventory mixed; multi-sign d=0.51 (envelope 0.4, null_p05 0.79) plausible; letter-for-letter d=1.60 excluded;
 mixed d=2.14 plausible; code d=2.38 plausible; shuffled-input FP 0.070; ranking nomenclator 0.51, homophonic 1.20, syllabary 1.40;
 nearest keys: orange-nassau-1572/key_nepveu.tsv d=0.25 || es132-vargas-mexia-1578/key.tsv d=0.30 || vanbeuningen-dewitt-1657 d=0.45
python3 tools/design_prior.py --no-write ciphers/es132-vargas-mexia-1578/ciphertext_f90v.tsv   (calibration, Cp.30)
 454 tokens, 185 distinct, inventory mixed; multi-sign d=0.35 plausible; letter-for-letter d=1.75 excluded; mixed d=2.18; code d=2.55;
 shuffled-input FP 0.065; ranking nomenclator 0.35 ...; nearest keys: es132 key.tsv d=0.12 || vanbeuningen-dewitt d=0.28 || key_nepveu d=0.48
```
Same family as the calibration (multi-sign/nomenclator first, letter-for-letter excluded). Difference: Cp.30's own key is second-nearest (0.30) behind Nepveu (0.25) on f.41r, first (0.12) on f.90v; plausibly the higher transcription error (30.6% vs 13.6%) spreads the inventory -- not read as a different cipher, since the decode gate below passes.
Step 4. `PREREG_c3_test1.md` committed and pushed (6c85d400) before any f.41r decode (passes were still running).
Step 5. `test2.py --page f41r` (new option; `test2.py --check` on the old pages still "OK"; `test1.py --check` "OK"). One bug fixed before the reported run: the first run loaded the f.90v blind passes with test2's shape loader, which dropped their test-1 notation marks (control pass A -1.327); the reported run loads them with test 1's own loader and reproduces test 1 exactly. Results (`c3_test1_f41r_result.json`, nulls first):
| text | letters | S_b | order-shuffle p99 | key-shuffle p99 | gate (b) |
|---|---|---|---|---|---|
| f.41r blind pass A | 909 | -1.375 | -1.533 | -1.838 | PASS |
| f.41r blind pass B | 924 | -1.388 | -1.548 | -1.839 | PASS |
| f.41r reconciled | 973 | -1.266 | -1.483 | -1.832 | PASS |
| positive control f.90v unprinted, pass A | 318 | -1.064 | -1.419 | -1.837 | PASS |
| positive control, pass B | 320 | -1.112 | -1.418 | -1.797 | PASS |
| positive control, reconciled | 322 | -1.048 | -1.396 | -1.801 | PASS |
Margins on f.41r (0.14-0.16 over the order null on the blind passes) are narrower than on f.90v (0.31-0.35): consistent with the higher transcription error. Key-shuffle null far below real (no overlap). ARM-C1: median order-shuffled decode fails the standard judge on target and control (not voided); the standard judge (real_p05 about -0.77) fails every real decode here, as in tests 1-2, so it is reported, not gated.
Grades (rule 4, per PREREG: S where the page gate passes on both blind passes and the control passes, '?' tokens M): H 0, C 0, **S 393, M 95**, I 0, U 35 (codes / brace words / numbers >= 38, unread). Page-level gate, not per-token verification. No H or C: cryptanalytic (key-applied) result. Rule 7: `python3 test2.py --page f41r --check` -> "OK: committed outputs match".
Reading `reading_f41r.txt`. Sense by eye, not graded (decode quoted literally, syllables spaced): L11 "[158] [258] [238] ta do a e ba xa dor de fra ci a que a qui" (embaxador de Francia que aqui), L13 "de fran ci a y fran de [5]" (Francia y Flandes?), L16 "pa t el cos ti go de los re be de [5]" (castigo de los rebeldes?), L21 "ti ni o pe re f pa t e tra tar de ta ma ie ri a" ([Anto]nio Perez ... tratar de ta[l] ma[t]eria?), L23 "y el di co el ba xa dor tor no a fro po ner la mi [5] ma", L28 "dar io bre la re y na de yn gra te ra" (la reyna de Ynglaterra). Reported as found; not searched in print in this job; f.44/f.46 (same date, cabinet-noir) not compared.
Not done: f.41v (continuation, if cipher; not viewed); settlement of the 81 default-flagged spans.
Requests: gallica.bnf.fr 8 (6 x 900 px canvases, 1 info.json, 1 native region); github.com 1 shallow clone. Subagent calls: 2 Sonnet (blind passes). No credentials used. Report only; no novelty classification made.

## f.41r settlement + f.41v (RUN3-ES41, LANE-RUN3 account 1, 4 Oct 2026, 08:47-09:xx UTC by the container clock)
Brief `.claude/briefs/runs/2026-10-04-acct1-run3-wave1.md` section RUN3-ES41. f.89/f.119/f.93-96 files and AUDIT.md untouched.
Step 1. cabinet-noir fresh shallow clone (08:4x UTC): `git log -1` = `47b6db9 2026-10-02 14:15:15 +0000 Version 1.2.1` (unchanged); es132 folder list
unchanged (30 folders; no f037, f041, f079). Nothing dropped from `cabinet_noir_map.tsv`.
Step 2. f.41r default-flag settlement. Rule pre-registered and pushed before any read: `PREREG_f41r_settle.md` (367f3428; a clarification
restricting decoys to digit tokens pushed with the items, d915332b, before the read). The 81 default tokens = 56 units (44 one-to-one A/B
pairs + 12 unequal spans; `run2/f41r_units.tsv`, written by `run2/reconcile_f41r.py`, which now writes `ciphertext_f41r_pre.tsv`, byte-identical
to the ES132-C3 stream). One blind Opus subagent read `run2/settle_f41r_items.tsv` (76 items: the 56 units + 20 decoys, shuffled, options in
random order, crops only, no key) -> `run2/settle_f41r_reads.tsv`; `settle_f41r.py --apply` -> `f41r_settle_result.json`, `run2/f41r_settled.tsv`.
**Control (20 firm tokens vs a look-alike decoy): firm picked at high confidence 17/20, at low 3/20; decoy picked 0/20 at any confidence.
Gate (>= 18/20 firm-high AND <= 1/20 decoy-high): FAIL (by one item).** Per the PREREG nothing is applied: `ciphertext_f41r.tsv` = the _pre
stream plus one header line saying so; the 56 reads stay as image-check pointers in `run2/f41r_settled.tsv` (S1 high-confidence 11 units, S2
low 36, S3 "other" 9; side A 23 / B 24 / other 9). Not re-gated after the fact (the reader never chose a decoy, but the gate counts confidence
too, and was fixed before the read).
Scoring before/after (test2.py --page f41r, unchanged): identical, since nothing was applied: reconciled S_b -1.266 vs order p99 -1.483 /
key p99 -1.832 (PASS); blind A -1.375 / B -1.388 (PASS); positive control f.90v reconciled -1.048 vs -1.396 / -1.801 (PASS).
`c3_test1_f41r_result_pre.json` = the committed result; `test2.py --page f41r --check` and `settle_f41r.py --check` "OK". Grades unchanged:
H 0, C 0, S 393, M 95, I 0, U 35. '?' tokens stay 105.
Step 3. Next page: **f.41v** (the brief's first choice; canvas 39 left, 31 full cipher lines, verso of f.41r, same letter of 29 April 1578;
`PREREG_c3_f41v.md` pushed c8384ba4 before any decode, statistic/nulls/gate/control/grades = PREREG_c3_test1.md unchanged). Crops (pasted):
```
python3 tools/iiif_lines.py --ark btv1b10032556x --canvas 39 --region 650,850,2700,4300 --out ciphers/es132-vargas-mexia-1578/images --prefix f41v --follow-slope 300 --slope-margin 40 --max-width 1450 --centres 241,365,495,609,731,869,985,1100,1226,1358,1499,1644,1775,1913,2064,2190,2334,2462,2597,2732,2856,3012,3143,3269,3405,3547,3679,3803,3929,4055,4177 --debug
 -> 31 lines, 31 bands x 2 segments; wrote 62 crops (1450 px wide)
```
Automatic detection first gave 29 bands with a duplicate (L28/L29 at the same y; the lines slope about -0.05, ~150 px drift over the
region); the centres are the 31 row-ink peaks of the region's left 500 px (script), checked by eye on a contact sheet (L01/02/10/11/20/21/
30/31) and L15 full width. Side effect logged: the tool's 30 MB guard deleted nine committed `src_*` reference images in the working tree
(restored from git before committing; the native f.39 source is not committed, re-fetchable from the region URL).
2 blind Sonnet passes (`run2/pass_prompt_f41v.md`) -> `passes/f41v_passA.tsv` (546 tokens), `_passB.tsv` (517). **err_2reader 183/554 = 33.0%**
(f.41r 30.6%; above one tenth: per TRANSCRIPTION.md the next transcription step for this hand is the lookalike pass / owner sorter, not a
third machine pass). Pass A's reader flagged L17 (short line) and L30 as least reliable. Reconciliation (third unit): `run2/reconcile_f41r.py
--page f41v`, f.41r's rules applied mechanically: R1-R6 fired 0 times, R7 17, default 166 -> `ciphertext_f41v.tsv` 31 lines, 546 tokens,
162 flagged '?'. (f.41r's shape rules do not transfer: the two readers' confusions on this page are different ones.)
Decode (`test2.py --page f41v`, `c3_test1_f41v_result.json`, nulls first, positive control in the same run):
| text | letters | S_b | order-shuffle p99 | key-shuffle p99 | gate (b) |
|---|---|---|---|---|---|
| f.41v blind pass A | 872 | -1.456 | -1.647 | -1.896 | PASS |
| f.41v blind pass B | 804 | -1.407 | -1.630 | -1.908 | PASS |
| f.41v reconciled | 877 | -1.446 | -1.623 | -1.886 | PASS |
| positive control f.90v unprinted, A / B / reconciled | 318 / 320 / 322 | -1.064 / -1.112 / -1.048 | -1.419 / -1.418 / -1.396 | -1.837 / -1.797 / -1.801 | PASS |
Margins over the order null 0.19 / 0.22 on the blind passes (f.41r 0.16 / 0.16). Standard judge fails every real decode and the ARM-C1
shuffled-median check is False on target and control (reported, not gated, as in tests 1-2).
Grades (rule 4, per PREREG): H 0, C 0, **S 359, M 125**, I 0, U 62. Page-level gate, not per-token verification; no H or C: cryptanalytic
(key-applied) result. Rule 7: `test2.py --page f41v --check`, `test2.py --check`, `test1.py --check` all "OK: committed outputs match".
Reading `reading_f41v.txt`. Sense by eye, not graded (decode quoted literally): L03 "y a don e ba xa dor le res a ce" (embaxador), L04 "an ti ni o
pe re c" (Antonio Perez), L06 "de di os y bi en", L14 "con es to an to ni o p pe re c me di a", L16 "le res pon di e", L23 "ne go ci o",
L26-27 "pa ra cas ti go de ... re be [l]de[s]" (cf. f.41r L16 "castigo de los rebeldes"), L29 "el ba xa dor", L31 "an xo ni o pe re c el o tro
di a". Not searched in print in this job; f.44/f.46 (same date, cabinet-noir) not compared.
Requests: gallica.bnf.fr 5 (one 900 px canvas 39, one info.json, three native-region fetches of the same region: the tool re-fetched after
its own 30 MB downscale); github.com 1 shallow clone. Subagent calls: 1 Opus (settle read), 2 Sonnet (blind passes). No credentials used.
Report only; no novelty classification made.

## Images under 30 MB (RUN3-ESSHR, LANE-RUN3 account 1, 4 Oct 2026, 09:42-09:5x UTC by `date -u`)
- images/ was 33.4 MB (464 files: 435 line crops 20.2 MB, 16 debug overlays 6.4 MB, 11 src_* regions 6.3 MB, 2 manifests). Shrunk the
  AX2-SHRINK way: `images_manifest_full.tsv` lists every file (path, bytes, sha1, kind, Gallica source or regen command, cited_by from a
  filename/stem grep of every text file in this folder, status). 325 files (17.9 MB) were deleted: only files with no filename citation
  **and** a byte-identical re-cut from the committed native src_* region (`tools/iiif_lines.py --image <src> --follow-slope 300
  --slope-margin 40 --debug`, the NOTES commands above minus the fetch): 382 of 383 files across 10 pages re-cut identically; the one
  that did not (f119v_L12, the separate --centres re-cut) is kept. Kept: every filename-cited crop (51 f41r crops cited by
  run2/settle_f41r_items.tsv, f119v_L02 etc.), all f41v crops (their src is a 1600 px reference copy, so no local re-cut), dup93/, all
  src_* and both manifests. Folder now about 17 MB. Nothing fetched. Originals in git history at 351e2659.
- `./regen_images.sh local [PREFIX]` restores crops offline in seconds (tested on f91r: sha1 match, then removed again);
  `./regen_images.sh check` re-verifies every page (expected one DIFF, f119v_L12); `fetch f41v|f93r..f95r` refetches a Gallica region.
  Cited full pages were already JPEG, so no conversion was needed. Note the passes TSVs name lines (L01) rather than crop files, so a
  transcription re-check of a deleted line runs `local` first.
- images/manifest.json repaired: 389 entries named `*_ref1600.jpg` reference copies that were not on disk (the native copies had been
  restored after the iiif_lines 30 MB guard downscaled them in RUN3-ES41's worktree) while f41v named a native file that was not on disk;
  each `source_file` now names the file present, with `source_file_downscaled` set to match.
- tools/iiif_lines.py guard bug (RUN3-ES41's report) reproduced offline and fixed: the guard now skips any src_*.jpg tracked by git
  (tools/tests/test_iiif_lines.py item 7 fails before the fix, passes after).

## f.50v, next Cipher 3 letter (RUN4-ES41V, LANE-RUN4 account 1, 4 Oct 2026, 10:48-11:0x UTC by `date -u`)
Brief `.claude/briefs/runs/2026-10-04-acct1-run4-wave1.md` section RUN4-ES41V. f.41, f.89/f.119/f.93-96 files and AUDIT.md untouched.
Step 1. cabinet-noir fresh shallow clone (10:4x UTC): `git log -1` = `47b6db9 2026-10-02 14:15:15 +0000 Version 1.2.1` (unchanged); es132
folders the same 30 (no f050, f054, f062). Nothing dropped from `cabinet_noir_map.tsv`.
Step 2. Letter and page: the next open Cipher 3 letter after f.41 in Tomokiyo's TOC order (f.44, f.46 are cabinet-noir's) is **f.50**, TOC
no.25 (no.25-29 = f.50, 54, 58, 60, 62, Philip II to Vargas Mexia, Bosque de Segovia, 7 and 14 June 1578; which date f.50 carries was not read).
Two 900 px looks after RUN4-PIS1's Gallica line (canvases 47, 48): f.50r = clear address + ~3 clear lines, then ~23 cipher lines; f.51r ~33
lines with two paragraph breaks; **f.50v (canvas 48 left) = 27 full cipher lines, no clear text** -> chosen as the most cipher on one page.
`PREREG_c3_f50v.md` pushed 15bb2ab4 before either pass or any decode (statistic/nulls/gate/control/grades = PREREG_c3_test1.md unchanged).
Crops (pasted):
```
python3 tools/iiif_lines.py --ark btv1b10032556x --canvas 48 --region 800,850,2750,3450 --out ciphers/es132-vargas-mexia-1578/images --prefix f50v --follow-slope 300 --slope-margin 40 --max-width 1450 --debug
 -> 27 bands x 2 segments, pitch 121, slopes about -0.015..-0.032; wrote 54 crops (1450 px wide)
```
Debug overlay and a contact sheet (L01, L14, L27, both halves) checked by eye: 27 bands = 27 lines, each centred; automatic detection was
right first time (no --centres needed). Line ends at the gutter may be partial (physical). images/ 18 MB after the crops (under 30 MB).
Step 3. 2 blind Sonnet passes (`run2/pass_prompt_f50v.md`, f41v's prompt with paths/line count changed) -> `passes/f50v_passA.tsv`
(4a53fefa), `_passB.tsv` (0b26859b). Reader A named L11 and L13 as weakest; reader B named 1/2/6/7/12/24 and 7ρ/y as its usual doubts.
**err_2reader 66/518 = 12.7%** (f.41r 30.6%, f.41v 33.0%; the f.89-f.91 pages 10.9-22.4%) -- still just above one tenth, so per
TRANSCRIPTION.md the next transcription step is the lookalike pass / owner sorter, not a third machine pass. Reconciliation (third unit,
mechanical, as pre-registered): `run2/reconcile_f41r.py --page f50v` (f.41r's R1-R7): R1-R6 fired 0, R7 15, default 51 ->
`ciphertext_f50v.tsv` 27 lines, 516 tokens, **72 flagged '?'**.
Decode (`test2.py --page f50v`, `c3_test1_f50v_result.json`, nulls first, positive control in the same run):
| text | letters | S_b | order-shuffle p99 | key-shuffle p99 | gate (b) |
|---|---|---|---|---|---|
| f.50v blind pass A | 932 | -1.197 | -1.439 | -1.866 | PASS |
| f.50v blind pass B | 969 | -1.228 | -1.459 | -1.863 | PASS |
| f.50v reconciled | 945 | -1.175 | -1.425 | -1.854 | PASS |
| positive control f.90v unprinted, A / B / reconciled | 318 / 320 / 322 | -1.064 / -1.112 / -1.048 | -1.419 / -1.418 / -1.396 | -1.837 / -1.797 / -1.801 | PASS |
Margins over the order null 0.24 / 0.23 on the blind passes (f.41r 0.16, f.41v 0.19-0.22; the f.90v control 0.31-0.36): the lower reader
error shows in the margin. Standard judge fails every real decode; ARM-C1 shuffled-median check False on target and control (reported, not
gated, as in tests 1-2).
Grades (rule 4, per PREREG): H 0, C 0, **S 421, M 57**, I 0, U 33 (codes/braces/numbers >= 38). Page-level gate, not per-token verification;
no H or C: cryptanalytic (key-applied) result. Rule 7: `test2.py --page f50v --check`, `--page f41r --check`, `--page f41v --check`,
`test2.py --check`, `test1.py --check` all "OK: committed outputs match".
Reading `reading_f50v.txt`. Sense by eye, not graded (decode quoted literally; t/r and u/b swaps are the decode's own, left as they are): L02 "de la car ta que
ha ui an te ci bi do de l de o ran ges" (la carta que havian recibido del de Oranges), L03 "es tan can sa dos", L11 "de l de o tan ges con
el se cre ta u o ui l to y" (del de Oranges con el secretario Villeroy?), L13 "mi her ma to", L20-21 "que se co nos ci e s por las o bras",
L21 and L26 "de a lan son" (de Alanson), L22 "mi her ma no no po di a de xar de o po n se le", L27 "un pa ca mas a pre ta do". Not searched in
print in this job; f.50r (same letter) not read.
Requests: gallica.bnf.fr 4 (2 x 900 px canvases 47/48, 1 info.json, 1 native region), after RUN4-PIS1's fetch line; github.com 1 shallow
clone. Subagent calls: 2 Sonnet (blind passes). No credentials used. Report only; no novelty classification made.

## f.51r, rest of the June 1578 letter (RUN4-ES50, LANE-RUN4 account 1, 4 Oct 2026, 11:16-11:3x UTC by `date -u`)
Brief `.claude/briefs/runs/2026-10-04-acct1-run4-wave3.md` section RUN4-ES50. f.41, f.50v, f.89/f.119/f.93-96 files and AUDIT.md untouched.
Step 1. cabinet-noir fresh shallow clone (11:16 UTC): `git log -1` = `47b6db9 2026-10-02 14:15:15 +0000 Version 1.2.1` (unchanged); es132
folders the same 30 (no f050, f051). Nothing dropped from `cabinet_noir_map.tsv`.
Step 2. One page, not two: 3 units x ~USD 1.5 per page = ~4.5 per page, two pages would cross 80% of the USD 6 cap. One 1200 px look at
canvas 48 after RUN4-PIS2's Gallica line (11:23 UTC): **f.51r (right page) = 26 cipher lines in three paragraphs (7 + 9 + 10), no clear
text**; chosen over f.50r (clear address and ~3 clear lines, ~23 cipher) as the more cipher and the page that follows f.50v.
`PREREG_c3_f50r51r.md` pushed ff236258 before either pass or any decode (statistic/nulls/gate/control/grades = PREREG_c3_test1.md unchanged;
C3_PAGES gained f51r/f50r in b0ec0d99, old pages `--check` OK).
Crops (pasted; the first native-region fetch answered HTTP 500, one retry after 25 s succeeded):
```
python3 tools/iiif_lines.py --ark btv1b10032556x --canvas 48 --region 3450,650,3050,3700 --out ciphers/es132-vargas-mexia-1578/images --prefix f51r --follow-slope 300 --slope-margin 40 --max-width 1450 --debug
 -> 26 bands x 3 segments, pitch 134, slopes about -0.007..+0.008; wrote 78 crops (1450 px wide)
```
Debug overlay and a contact sheet (L01, L07, L08, L16, L17, L26, s1) checked by eye: 26 bands = 26 text lines, each centred, paragraph
breaks after L07 and L16 fall between bands (no empty band). The native src region is committed (images/ 21 MB, under 30 MB).
Step 3. 2 blind Sonnet passes (`run2/pass_prompt_f51r.md`, f50v's prompt with paths, three segments and line count changed) ->
`passes/f51r_passA.tsv` (19421eb1; reader named L01 and L22 weakest), `_passB.tsv` (636d6eda; usual doubts 2/x, ρ/σ/+, 1/7//, 6/G/8, 5/S,
hat/rmark/acute, n/m/u). **err_2reader 87/477 = 18.2%** (f.50v 12.7%, f.41r 30.6%, f.41v 33.0%) -- above one tenth, so per TRANSCRIPTION.md
the next transcription step is the lookalike pass / owner sorter, not a third machine pass. Reconciliation (third unit, mechanical, as
pre-registered): `run2/reconcile_f41r.py --page f51r`: R1-R6 fired 0, R7 12, default 75 -> `ciphertext_f51r.tsv` 26 lines, 473 tokens,
**83 flagged '?'**.
Decode (`test2.py --page f51r`, `c3_test1_f51r_result.json`, nulls first, positive control in the same run):
| text | letters | S_b | order-shuffle p99 | key-shuffle p99 | gate (b) |
|---|---|---|---|---|---|
| f.51r blind pass A | 838 | -1.198 | -1.468 | -1.842 | PASS |
| f.51r blind pass B | 829 | -1.188 | -1.467 | -1.820 | PASS |
| f.51r reconciled | 852 | -1.174 | -1.463 | -1.814 | PASS |
| positive control f.90v unprinted, A / B / reconciled | 318 / 320 / 322 | -1.064 / -1.112 / -1.048 | -1.419 / -1.418 / -1.396 | -1.837 / -1.797 / -1.801 | PASS |
Margins over the order null 0.27 / 0.28 on the blind passes (f.50v 0.24 / 0.23; control 0.31-0.36). Standard judge fails every real decode
(real_p05 about -0.77); ARM-C1 shuffled-median check False on target and control (reported, not gated, as in tests 1-2).
Grades (rule 4, per PREREG): H 0, C 0, **S 366, M 65**, I 0, U 42 (codes/braces/numbers >= 38). Page-level gate, not per-token verification;
no H or C: cryptanalytic (key-applied) result. Rule 7: `test2.py --page f51r --check`, `--page f50v/f41v/f41r --check`, `test2.py --check`,
`test1.py --check` all "OK: committed outputs match".
Reading `reading_f51r.txt`. Sense by eye, not graded (decode quoted literally; x/r and t/r swaps are the decode's own): L08 "en lo de ma de l
de o ran ge s le man de xe s por der que" (del de Oranges le mandase poder?), L10-11 "lo pa sa y lo de mas que a es te pro po si to me a d uer
ti a y o fre ci a", L12 "que el de o xan ges to ma se", L17-18 "xe pri co el di ca [bul] ... di zi en do a lo [358?] me ro de lo de a lan son
que le pa xe ci a" (replicó ... diziendo a lo primero de lo de Alanson que le parecía?), L19 "es ta ya tan de ter mi ha do", L21 "pa a par tar a
[231] her ma no del yn ten to", L23-24 "que yo le o fre ci e se que le a y da x", L26 "ne ce si da d ... por es ta ca u sa". Code 231 occurs
9 times (7 firm, 2 flagged '?'), outside the key, unread; not resolved here. Not searched in print in this job; f.50r (same letter) not read.
Requests: gallica.bnf.fr 5 (2 x 1200 px canvases 47/48, of which 47 was not viewed; 1 info.json; the native region twice: HTTP 500,
then one retry 200); github.com 1 shallow clone. Subagent calls: 2 Sonnet (blind passes). No credentials used. Report only;
no novelty classification made.

## f.50r, opening of the June 1578 letter (RUN4-ES50R, LANE-RUN4 account 1, 4 Oct 2026, 11:40-11:4x UTC by `date -u`)
Brief `.claude/briefs/runs/2026-10-04-acct1-run4-wave3.md` section RUN4-ES50R. Pages read earlier, the f.89/f.119/f.93-96 files and AUDIT.md were not touched.
Step 1. cabinet-noir fresh shallow clone (11:41 UTC): `git log -1` = `47b6db9 2026-10-02 14:15:15 +0000 Version 1.2.1` (unchanged); es132
folders the same 30 (no f050). Nothing dropped from `cabinet_noir_map.tsv`.
Step 2. One 1200 px look at canvas 47: f.50r = "El Rey" + clear opening ("Juan de Vargas Mexia. Despues que ultimamente se os aviso del recibo de
vuestras cartas, han llegado las de xvj. xvij. xx. xxj, xxv. y xxvij del passado"), cipher from mid line 3 to the end. `PREREG_c3_f50r.md`
(addendum to PREREG_c3_f50r51r.md, page changed only) pushed 97faca4a before either pass or any decode.
Crops (pasted):
```
python3 tools/iiif_lines.py --ark btv1b10032556x --canvas 47 --region 3600,1340,2850,3060 --out ciphers/es132-vargas-mexia-1578/images --prefix f50r --follow-slope 300 --slope-margin 40 --max-width 1450 --debug
 -> 24 bands x 3 segments, pitch 120; wrote 72 crops
```
I checked the debug overlay by eye: 24 bands = 24 text lines (L01 clear, L02 clear then cipher, L03-L24 cipher), each band centred on its line.
images/ 24 MB (under 30 MB).
Step 3. 2 blind Sonnet passes (`run2/pass_prompt_f50r.md`) -> `passes/f50r_passA.tsv` (a7170464; reader named L02 L10 L13 L17 L20 L24 as
weakest), `_passB.tsv` (6670c7bb). **Pass B wrote no '.' vowel sign at all** (0 of 450 tokens; pass A 103/458; every earlier pass on this
hand 99-122): a reader notation lapse, not a reading of the page (the dots are visible in the overlay). Because of it, **err_2reader
184/460 = 40.0%** (f.51r 18.2%, f.50v 12.7%). No rule was added: the reconciliation was run as pre-registered (`run2/reconcile_f41r.py --page f50r`,
HDR1/LETTER entries for f50r added, no rule changed): R4 2, R7 89 (mostly A's dots, flagged '?'), default 93 -> `ciphertext_f50r.tsv`
24 lines, 456 tokens, **179 flagged '?'**.
Decode (`test2.py --page f50r`, `c3_test1_f50r_result.json`, nulls first, positive control in the same run):
| text | letters | S_b | order-shuffle p99 | key-shuffle p99 | gate (b) |
|---|---|---|---|---|---|
| f.50r blind pass A | 864 | -1.219 | -1.443 | -1.844 | PASS |
| f.50r blind pass B | 679 | -1.770 | -1.773 | -1.950 | PASS (margin 0.003) |
| f.50r reconciled | 865 | -1.227 | -1.445 | -1.842 | PASS |
| positive control f.90v unprinted, A / B / reconciled | 318 / 320 / 322 | -1.064 / -1.112 / -1.048 | -1.419 / -1.418 / -1.396 | -1.837 / -1.797 / -1.801 | PASS |
Gate (b) passes on both blind passes as pre-registered, but pass B only by 0.003 (a dotless decode loses its vowels); pass A's margin over
the order null is 0.22, which matches f.50v (0.24) and f.51r (0.27). Standard judge fails every real decode (real_p05 -0.778); ARM-C1 shuffled-median
check False on target and control (reported, not gated).
Grades (rule 4, per PREREG): H 0, C 0, **S 255, M 167**, I 0, U 30. Page-level gate, not per-token verification; no H or C:
cryptanalytic (key-applied) result. Rule 7: `test2.py --page f50r --check`, `--page f51r/f50v/f41v/f41r --check`, `test2.py --check`,
`test1.py --check` all "OK: committed outputs match".
Reading `reading_f50r.txt`. Sense by eye, not graded (decode quoted literally; t/r swaps are the decode's own): L04 "pra ti ca con la d ma ee so
bre lo de [61?] que de a lan son", L05 "con el se cre ta u o ui le fo y" (el secretario Villeroy?), L05-06 "a que la car ta de de tan ge s que os
mos tro" (aquella carta del de Oranges que os mostró?), L07 "a es te pro po si to tra to con uos", L13 "a ma s de a lan son", L18 "di zi en do
que de tal ma h ta", L21 "de la de tr mi ha ci on en que es ta", L22 "de la q er za" (de la fuerza?). Same names as f.50v/f.51r (Oranges,
Alanson, Villeroy). Not searched in print in this job.
Requests: gallica.bnf.fr 3 (1 x 1200 px canvas 47, 1 info.json, 1 native region; all 200, >= 2 s apart); github.com 1 shallow clone.
Subagent calls: 2 Sonnet (blind passes). No credentials used. Report only; no novelty classification made.
