# della-torre-olanda-1690

Status: blocked

No printed Savoy edition of the Della Torre Hague correspondence could be opened or identified by this worker, and the ASTo inventory PDF (LETTERE MINISTRI_Vol.II.pdf) did not open from this container (connection reset twice, 2 Oct 2026), so no edition or page was read. The 24 Sept 2026 sweep below stands as a negative search result only.

## What this is

Cipher-book ("CIFRARIO al Conte e Presidente Della Torre") filed in the same mazzo as the decade of
correspondence (1690-1700) of Savoy envoy extraordinary Conte e Presidente Della Torre at the Hague, negotiating
Dutch subsidies for the League of Augsburg war against France. Archivio di Stato di Torino, "Lettere Ministri —
Carteggio diplomatico" (Inv. 151/B), Lettere Ministri Olanda, mazzo 2. Box also holds letters to/from Lord
Nottingham, Milord Monquille, Cav. Giuseppe Terne (London), Conte Caraffa, Prelà Doria and the Marchese di Prié
(Vienna). QUEUE.md row IR1 (section "Italian regional state archives, Mantua Modena Turin Genoa Naples", LANE N
scout IT3 of 24 Sept 2026); source PDF `LETTERE MINISTRI_Vol.II.pdf`, ASTo.

No image or transcription has been seen by anyone in this project; the box-level finding aid gives no item-level
content note beyond the cipher-book's title, so it is not established from the finding aid alone that any letter
in the mazzo is itself ciphertext rather than clear correspondence about the cipher's issue — only that the box
holds both a keybook and the envoy's own decade of letters (CLAUDE.md "Confirm the key and the letters are in the
same unit and that the letters are ciphered" — partially met: same unit confirmed, letters-are-ciphered not yet
confirmed without opening the box). `ciphertext.txt` is not created (rule 2: no invented transcription).

## Check-solved sweep, 24 September 2026

1. **Web.** WebSearch `"Della Torre" ambasciatore Aia Olanda cifra 1690 1700 Savoia` and `Della Torre inviato
   Savoia Olanda "Lettere Ministri" cifrario Torino archivio` and `"Della Torre" negoziato Aia 1690 sussidi guerra
   Lega Augusta Savoia carteggio pubblicato`. Hits: the ASTo inventory PDF itself, Wikipedia pages for unrelated
   Della Torre namesakes (Filippo, Oberto, Giovanni Maria, Leonardo — all different people/centuries), and general
   background on the War of the League of Augsburg and Vittorio Amedeo II. No hit names this envoy's cipher, this
   mazzo, or a printed decipherment. Not found.
2. **Print.** No printed Savoy diplomatic edition or "Biblioteca di storia italiana" volume for the Della Torre
   Hague mission located by WebSearch this pass (queried against opac.sbn.it and generally); Vittorio Amedeo II's
   published *Lettere e relazioni diplomatiche* series was not checked volume-by-volume (out of scope for one
   worker's budget) — recorded as not located, not as a confirmed absence at N3/N4 level. This is a check-solved
   pass, not a verifier's edition sweep.
3. **Lists.** `sources/cryptiana/` grepped locally for `della torre|dellatorre`: no hits.
4. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` (1187 rows) grepped for `della torre|olanda|
   torino`: no matching envoy/shelfmark. Live de-crypt.org not queried (this lane's rule: only the DECODE worker
   logs in).
5. **Bourdeau.** Fresh shallow clone `github.com/dbourdeau/cyphersolver`. `grep -ril "Della Torre"` across the
   whole tree: 3 hits, none this item — `buda1489/vestigia/search_rows.json` (unrelated search-index noise),
   `vatican5/lit/elio.txt` line 405 ("Dandino, Della Torre et Trivultio (1546-...)", a different, earlier Della
   Torre, papal nuncio context), `pallotto1629/ed/pallotto_bd2_1629.txt` (unrelated edition text). Not found.
6. **Aymeloglu.** Same clone/grep pass against `github.com/aaymeloglu/unsolved-ciphers`: 0 hits for "Della Torre".
   Not found.

## Verdict

**Open.** No source located a solution, key, plaintext or documented attempt for this item. Not yet confirmed
whether the mazzo's letters are themselves ciphered (finding-aid text alone does not say), and no printed Savoy
diplomatic edition has been checked page-by-page — both gate items for promotion past stage 2, left for the next
worker (access/print-check pass) rather than closed here.

Copy-order: no digitised image of ASTo Lettere Ministri Olanda mazzo 2 found this pass (the PDF is an inventory,
not a viewer). REQUEST.md below.

Requests this pass: WebSearch 3 (shared with general Turin/Della Torre queries), opac.sbn.it via WebSearch
`allowed_domains` 1, github.com 2 shallow clones (shared across all six IR targets, grepped, kept for reuse),
archiviodistatotorino.beniculturali.it 0 direct fetches this pass (inventory PDF already fetched and quoted by
the 24 Sept scout; not re-fetched). No SIAS, no Google Books, no DECODE login, no promotion, no decoding.

## Web and blog check (CS-A2-B, 2 Oct 2026)

WebSearch (standard) on the envoy/secretary, place, year and "cifra/cifrario" in Italian (see below per target); results were the holding archives' own inventory PDFs, unrelated namesakes and general background, none naming a decipherment. Cryptiana blog, Cipherbrain and Cipher Mysteries: the Waldegrave-run site searches the same day (same three hosts) cover only that name; for this target the three blogs were searched through WebSearch and `sources/cryptiana/` only, no post found, comment threads not separately opened. DECODE: login-free `tools/decode_list.py --status non-decrypted` crawl of 2 Oct 2026 (801 rows): 0 rows matching della ?torre|olanda|savoia for this item (the 54 "Hague/Aia" matches in the crawl are Dutch royal-archive items of 1789-1804, not this mazzo). Solver repos, shallow clones grepped 2 Oct 2026: dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers: no hit for this item (only namesake or place-name noise). Unreachable this pass: archiviodistatogenova.cultura.gov.it and archiviodistatotorino.beniculturali.it (curl, connection reset, one retry), so the holding finding aid was not re-opened.

## Premise check (CS-A2-B, 2 Oct 2026)

(a) Folder's own NOTES.md/REQUEST.md: no decipherment, gloss, clear copy or attachment mentioned. Not found. (b) Solver working files: no file for this item in either repository. Not found. (c) Physical neighbours / facing page: no image exists or was reachable (copy-order). Unreachable. (d) Recipient-side editions: not located by this worker's searches. Not found (not an edition read).

Hosts this pass: de-crypt.org 17 (no login, shared run), github.com 2 clones (shared), archiviodistatogenova/torino 2 attempts each failed, WebSearch 1 for this target.

## CS-BATCH4 pass (3 Oct 2026, 15:3x-15:4x UTC)

- Holding finding aid opened this time (the 2 Oct connection resets did not recur; one request, HTTP 200, 20.1 MB): ASTo `upload/LETTERE MINISTRI_Vol.II.pdf`, "Lettere Ministri Olanda" listing read with pdftotext. Mazzo 2 line reads "CIFRARIO ... Lettere di Milord Monquille, dirette al Conte e Presidente Della Torre 1690 e 1691", then Terne (London, 1690-97), Conte Caraffa (1691), Nottingham, Doria, Prie (Vienna 1691-1700); mazzo 1 is the Court's instruction and letters to Della Torre. The aid is box-level: it does not say any letter is in cipher, and it carries no availability flag (it is an inventory, not a catalogue record or viewer). Grade I for "the cipher-book sits with the letters" (same box line, OCR-noisy).
- Edition: Carutti, Storia della diplomazia della corte di Savoia vol. 3 (1880), IA `carutti-storia-della-diplomazia-della-corte-di-savoia-v-3`, whole-volume djvu (957 KB, 24,732 lines) grepped by this worker for "della torre", "cifr", "Car[a]ffa": Della Torre's mission to The Hague and London in autumn 1690 is narrated (treaties of 20 Oct 1690, text near line 7093), the only "in cifra" citation is a 1686 Ferrero despatch (line 5225); no cipher text, key or decipherment of Della Torre's papers printed. This is a narrative history, not an edition of the correspondence; no edition of the Della Torre Hague letters was identified. Not found.
- Not done: Italian-side printed editions of the despatches (none identified), ASTo holding record flag, images (none online per the 24 Sept sweep).

Intake gate (python3 tools/intake_gate_check.py della-torre-olanda-1690): "blocked (line 3) -- already terminal, nothing to gate", exit 0.

Verdict: stays `blocked` (no edition of the letters exists to open; whether the letters are enciphered is unknown). Next: the ASTo reading-room/copy enquiry of REQUEST.md, ~USD 0 agent cost, owner-side; or a Dutch-side search of Hague records for the same envoy (Nationaal Archief, Staten-Generaal lias Savoije 1690, ~USD 1.5).

## While waiting

[done 6 Oct 2026, D22-FTS: Staten-Generaal retroboek stops at 1625 and cannot cover 1690; one lead in Willem III-Bentinck KS 24 p.800, unread] One action that depends on nobody: search Dutch printed sources for Della Torre's 1690 mission (Resolutien der Staten-Generaal, Huygens retroboeken Staten-Generaal 1690) for a clear copy of his despatches; ~USD 1.

## D22-FTS (6 Oct 2026)

Item 4 of D22-FTS (Sonnet worker, 6 Oct 2026), search only. Grade I.
Huygens retroboeken full-text search (accessor `searchText`, whole-edition, >=2.2 s apart): the *Staten-Generaal* retroboek covers only the 1576-1625 Besluiten (volume labels "Deel 13 (1604-1606, GS 101)"), so it cannot hold 1690 resolutions: `Della Torre` 0, `Torre` 2 (both a 1604-06 Antwerp merchant, Paulo de la Torre), `Savoye` 205 (not read). *Correspondentie van Willem III en Bentinck* (retroboek willemiii, KS 23-28): `Della Torre` 0, `Torre` 0, `Torre Savoye` 0, `Savoyse gesant` 0, `President de la Tour` 3 (noise), `Savoye` 69, `gezant van Savoye` 19. The 19 include the letter-writer list of Eerste gedeelte deel 2, KS 24, p.800: "De la Tour(?), buitengewoon gezant van den hertog van Savoye (geschreven met Blancard ...)" followed by dates "... September, ... October" -- i.e. a Savoy extraordinary envoy appears as a correspondent in the Willem III-Bentinck edition (the OCR spelling is garbled, not confirmed as Della Torre, no year read). Heinsius (`search_in_text`) `Della Torre` 0. Not reached: the page itself (`pages.json?source=` for KS 24, p.800 and the letter pages).
Result: no clear copy of a Della Torre despatch found; one lead for a page read (KS 24 alphabetical letter list p.800 and the letters it indexes), ~USD 0.5. Not a novelty verdict. Requests: resources.huygens.knaw.nl 17 (search pages), no pages.json fetched.
