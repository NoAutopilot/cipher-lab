# belmesseri-napoli-1627

Status: blocked
No standard edition identified or opened for the Este envoy's Naples dispatches on the Stigliano marriage of 1627-28; archive.org full-text search for Belmesseri+Napoli+Stigliano returned 35 hits and Belmessieri+Napoli 316, all noise (Neapolitan directories, newspapers, indexes), none naming this envoy.

## What this is

Cipher attached to Este envoy Angelo Belmesseri's Naples dispatches on the Stigliano marriage negotiation, 16
May 1627 – Jan 1628. Archivio Segreto Estense, Cancelleria, Carteggio ambasciatori — Napoli, b.20 fasc.1
(shelfmark given directly by the finding aid). Finding-aid note (verbatim): "Evvi congiunta una cifra" ("there
is attached a cipher"), on a nine-month run of dispatches about negotiating a marriage between the prince and
princess of Stigliano. The same run's earlier fascicle, b.19, carries an unciphered mission by the same envoy,
so the finding aid itself localises the cipher use to b.20 fasc.1 specifically. QUEUE.md row IR3 (LANE N scout
IT3 of 24 Sept 2026); source PDF `ASE_Cancelleria_ambasciatori_napoli.pdf`, ASMo/Este archive.

Same-unit and ciphered-letters are both stated directly by the finding aid's own wording ("evvi congiunta" = a
cipher is attached to this fascicle), the strongest form of confirmation available from a text-only source —
still short of having seen the item itself. `ciphertext.txt` is not created.

## Check-solved sweep, 24 September 2026

1. **Web.** WebSearch `"Belmesseri" OR "Belmessieri" Napoli Stigliano matrimonio ambasciatore estense 1627`.
   Hits: Treccani entries for Marzio Mastrilli and unrelated figures, a 21st-century Parma family news item
   (different "Belmessieri"), Tommaso Stigliani (poet, different spelling/person), general Stigliano/Colonna
   pages. No hit names this envoy, negotiation or cipher. Not found.
2. **Print.** No printed Este diplomatic edition for the Naples 1627-28 Stigliano marriage negotiation located
   this pass (Venturi/Balan/Pastor appendices and the "Carteggio degli oratori" series not checked
   volume-by-volume — out of one worker's budget). Not confirmed absent at verifier level.
3. **Lists.** `sources/cryptiana/` grepped locally for `belmesseri|belmessieri|stigliano`: no hits.
4. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` grepped for `belmesseri|napoli|stigliano`:
   the file's "Modena" rows are all Ambasciatori Ungheria (Ferrara envoy reports, 1482-1504, boxes Amb. Ung.
   b.2/... and Carteggio Principi Esteri) — a different fondo and box entirely from Carteggio ambasciatori
   Napoli b.20; no row matches this envoy or shelfmark. Live de-crypt.org not queried.
5. **Bourdeau.** Fresh shallow clone `github.com/dbourdeau/cyphersolver`, `grep -ril "Belmesseri"`: 0 hits.
6. **Aymeloglu.** Same clone/grep pass against `github.com/aaymeloglu/unsolved-ciphers`: 0 hits.

## Verdict

**Open.** No source located a solution, key, plaintext or documented attempt for this item. "Evvi congiunta una
cifra" is ambiguous by itself between "a cipher key is attached" (the IR1/IR2/IR4/IR5 recovery pattern) and "a
ciphered letter is included" (cryptanalysis) — Italian archival usage of "cifra" covers both the table and the
enciphered text, and the finding aid does not disambiguate. Kept as recovery per the scout's row pending
inspection; a worker who opens the fascicle should confirm which reading is right before any solver attempt.

Copy-order: no digitised image of ASMo Carteggio ambasciatori Napoli b.20 fasc.1 found this pass. REQUEST.md
below.

Requests this pass: WebSearch 1, github.com 0 (reused shared clone). No SIAS, no Google Books, no DECODE login,
no promotion, no decoding.


## Web and blog check (CS-A2-C, 2 Oct 2026)

WebSearch queries (standard) and what they returned:
- Belmesseri Napoli 1627 Stigliano matrimonio Este cifra dispacci (Anna Carafa/Stigliano marriage pages, RAH and Spanish studies; envoy and cipher not named)

Blogs: Cipherbrain, Cryptiana blog and Cipher Mysteries were covered by the restricted web searches above and a local grep of `sources/cryptiana` and `sources/ciphermysteries`; 0 hits for the sender, recipient or shelfmark; no comment thread opened because no hit was relevant.

archive.org full-text (be-api, one request at a time, 2 s apart, unquoted-token behaviour so counts are upper bounds):
- Belmesseri Napoli Stigliano (35, noise)
- Belmessieri Napoli (316, noise)

Solver repositories (shallow clones, grep only, 2 Oct 2026): belmesseri/belmessieri: 0 / 0; 'stigliano' appears in Bourdeau pallotto1629 and esp318 (different targets, not this letter). Aymeloglu cited, no code used.

DECODE: local grep of sources/decode (records-non-decrypted 24 Sept 2026 and later key lists) for the sender/recipient names: 0 rows; the 2 Oct 2026 login-free crawl (801 rows) by CS-A2-B is the same list. Live de-crypt.org not queried by this worker.

## Premise check (CS-A2-C, 2 Oct 2026)

- (a) not found as a decipherment; the finding aid's "Evvi congiunta una cifra" is ambiguous between a key and a ciphered letter.
- (b) not found: no Belmesseri file in either solver repo.
- (c) unreachable: no image of ASMo Napoli b.20 fasc.1.
- (d) not found/unreachable: the Spanish-side literature on the Carafa-Stigliano marriage (Sabbioneta/Gonzaga) was not opened; a search of Simancas/Sabbioneta studies for Este dispatches is the next step.

Verdict: blocked. No solution, key, plaintext or documented attempt was found in anything searched, but no edition could be opened, so this is a search result for the log and not a statement that none exists. Status was `open` before this pass and failed the intake gate.

## While waiting (RUN4-WAITBF, 4 Oct 2026)

- [done 6 Oct 2026, D22-FTS2: Negri's Modena footnotes read -- series: Cancelleria Ducale agenti e residenti a Roma 1627 busta 180 (Testi, partly cifrato, printed in clear in appendices), Torino/Napoli 1625-27 no busta; Belmesseri's own dispatches not printed] [done 6 Oct 2026, D22-FTS: no printed decipherment found; secondary hit Negri in Archivio Soc. rom. di storia patria 34 (1911), `archivio34sociuoft`, uses Testi's "cifrato" Rome dispatches on the Stigliano affair] Action that depends on nobody: the step this folder's own pass (d) names -- a full-text search (archive.org be-api/advancedsearch, Google Books API with key and country=US) of the Spanish-side literature on the Carafa-Stigliano marriage (Sabbioneta/Gonzaga studies, Simancas) for Belmesseri's Este dispatches of 1627-28 and any printed decipherment of their cipher; one Sonnet worker, ~$1.5 (estimate). The image itself stays an archive request.

## D22-FTS (6 Oct 2026)

Item 2 of D22-FTS (Sonnet worker, 6 Oct 2026), search only. Grade I.
Queries (be-api fts, whole archive.org): `"Belmesseri" Stigliano` 35 (same 35 as the earlier sweep; the useful one is `archivio34sociuoft`); `"Belmessieri" Stigliano Napoli` 77 (noise); `"Belmesseri" Napoli 1627 Este` 153 (noise); `"Stigliano" "Carafa" Sabbioneta cifra 1627` 275 (Carrasco, *La nobleza y los reinos*, on Sabbioneta and Stigliano; Quazza, *Mantova e Monferrato*; no cipher text). Google Books API (key, country=US) `"Belmesseri" Stigliano` 5 volumes, all copies of *Archivio della Società romana di storia patria* 1911 (vol. 34), snippets "unione Este - Stigliano ... Belmesseri, Giambattista Zampolocca".
Read: `archivio34sociuoft` (IA, public), P. Negri's article on the Este marriage negotiations, full text `_djvu.txt` downloaded once and grepped: "Belmesseri" occurs once (footnote 2, a list of Naples/Este intermediaries: "padre Ippolito Guidi, Angelo Belmesseri, Giambattista Zampolocca ..."); the narrative rests on Francesco Testi's Rome dispatches, cited "Disp. F. Testi, Roma, 20 sett. 1627, cifrato" (twice) and two "(in parte cifrata)" notes; no decipherment of Belmesseri's cipher is printed and Belmesseri's own dispatches are not cited by shelfmark. `codicesvrbinates0003vari` lists a "Belmesseri Francesco: lett. 1628" (a different person, Urbinate MSS).
Result: no printed decipherment of the b.20 cipher found; one secondary article (Negri, Archivio Soc. rom. 34) uses ciphered Este dispatches of the same marriage affair and could name where Este dispatches were read -- its footnotes citing Modena are the next page-level check if wanted. Not a novelty verdict. Requests: be-api 6 (incl. 3 identifier-restricted), archive.org download 1, Google Books 1.

## D22-FTS2 (6 Oct 2026)

Item 4 of D22-FTS2 (Sonnet worker, 22:5x-23:0x UTC, for LANE DEFAULT-account-2-20261006-2209), page reading only. Grade I.
Source: P. Negri, article on the Este-Stigliano marriage negotiations of 1627 (Testi's two months at Rome), *Archivio della Societa romana di storia patria* 34 (1911), IA `archivio34sociuoft`, `_djvu.txt` (1.3 MB, downloaded once, grepped; footnotes and appendices of the article read at djvu lines 19500-21000).
**Modena series cited** (all "R. Arch. di Stato di Modena"): (1) *Cancelleria Ducale, agenti e residenti estensi a Roma, 1627*, **busta 180**, "come tutti i documenti citati qui appresso senz'altra indicazione" (line 19505): this is Francesco Testi's Rome correspondence, cited as "Disp. F. Testi, Roma, <date> 1627" throughout, incl. 20 Sept 1627 "cifrato" (twice, lines 20222-20223); (2) *Cancelleria Ducale, Carteggio restituito, Agenti e residenti estensi a Torino e a Napoli*, 1625-27, no busta given (footnote at lines 20178-20182, with Turin's Carteggio Principi Este-Savoia); (3) a "sommario di lettere relativo al matrimonio" in the *Carteggio agenti e residenti estensi a Roma* of **1634**; also Reggio Emilia, Carteggio Bolognesi (1635) and Turin. Not the finding aid's "Carteggio ambasciatori, Napoli, b.20": the Naples series is cited under the older name "Agenti e residenti estensi a Napoli", with no busta, so whether it is the same unit as b.20 fasc. 1 is unconfirmed.
**Printed deciphered passages.** The article's Appendices I-XI print passages of Testi's Rome dispatches (e.g. Appendix I "(*) In parte cifrata", line 20594, and another at 20797), so some Este cipher dispatches are printed, with the cipher parts rendered in clear and not marked as deciphered by whom. All are Testi's, from Rome (busta 180). **Belmesseri's own Naples dispatches are not cited or printed**: his name occurs once, in a footnote list of intermediaries ("padre Ippolito Guidi, Angelo Belmesseri, Giambattista Zampolocca ...", line 20257). So nothing printed could be the b.20 letter's text; the Stigliano marriage dates the b.20 run (16 May 1627 - Jan 1628), and Negri's Rome appendices (Sept-Nov 1627) fall inside it but come from another envoy.
Result: no printed passage that can be the b.20 fasc. 1 text; the one transferable fact is that Negri read the Este Rome cipher dispatches for the same affair in Modena busta 180 (Testi, 1627, partly "in parte cifrata", printed in clear in his appendices), a possible crib source for the same affair's vocabulary if a cipher design is ever shared (not tested). Not a novelty verdict (rule 10). Requests: archive.org 1 (`_djvu.txt`).
