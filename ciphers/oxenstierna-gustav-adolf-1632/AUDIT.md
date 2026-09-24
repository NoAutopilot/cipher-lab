# AUDIT: novelty of the reading of Gustav II Adolf to Axel Oxenstierna, Nürnberg 23 July 1632 (letter 602)

Verifier session, 24 Sept 2026 (LANE W worker C, started 06:14 UTC, written 06:25-06:40 UTC). This is an adversarial audit of
LANE R worker R3's reading (NOTES.md section "Image check, design, control and reading", commit 6979c96). The
verifier did not take part in the solving. Levels N0-N5 are those of CLAUDE.md rule 10.

## 1. Executive verdict

| item | prior plaintext | prior decipherment of this ciphertext | level |
|---|---|---|---|
| Letter 602, Gustav II Adolf to Axel Oxenstierna, "Aff lägret vidh Nürnberg den 23 Julij, Åhr 1632" | **yes**: R. Torpadie, "Några ord om chifferskrift", *Historisk tidskrift* 8 (1888), Strödda meddelanden och aktstycken, pp. 376-383; full plaintext pp. 382-383 | **yes**: the same article. Torpadie recovered the key by frequency analysis from this very printed ciphertext, printed the two-digit key table (p. 382 note), read some codes, and printed the whole letter deciphered | **N0** |

**Letter 602 was solved in print in 1888, the year the edition came out.** Torpadie opens: "Uti det nyss utkomna
första bandet af andra afdelningen utaf Axel Oxenstiernas Skrifter ... meddelas under N:o 602 ett chifferbref,
hvilket på grund af felande nyckel, när bandet trycktes, måst lemnas olöst. Då förf. ... lyckats finna denna
nyckel, har han trott det kunna vara af intresse att meddela lösningen" (in the recently published first volume of
the second section of Axel Oxenstierna's Skrifter, no. 602 is a cipher letter that had to be left unsolved for
lack of a key when the volume was printed. The author found the key and thought it worth publishing the solution),
p. 376. The journal's editors add in a note on p. 381 that the two-digit cipher was since found deciphered in
several other letters, and that this "fully confirmed" the author's solution.

R3's reading is an **independent re-decipherment** of a letter whose plaintext and key have been in print for 138
years. It adds nothing to Torpadie on the letter layer. Torpadie is ahead on the codes and signs that R3 left
unread (U) and on every stretch R3 graded M. Examples, R3 against Torpadie: "hvardera ett [code] complett" /
"hvardera et regemente complett" (2923 = regemente); "anhålla hos [code] omlopalath" / "anholla hoos
Chur-Brandenburg om löp-platz för 4 regementen"; "mistaboetium" / "mista Boetium"; "som droged [code] tneder" /
"som droge dit neder"; "befruell r stutta" / "befrukta eller stutza"; "Stee.. [code] Bielke" / "Steen Bielke"
(96, 99 and 205 are nulls, p. 381); r = I, rr = och, ll = äro (the printed letter-signs R3 left unread); 1328 and
3328 = tusen, 3927 = ryttare (hedged "?"), 2162 = lägret (hedged). Torpadie also states the design: three
consecutive numbers stand for each letter (p. 381). R3's key (24-26 = e, 27-29 = l, 49-50 = c ...) follows the
same pattern, which independently confirms both readings.

**Safe sentence:** "Letter 602 (Gustav II Adolf to Oxenstierna, 23 July 1632) was deciphered and printed by R.
Torpadie in Historisk tidskrift 8 (1888), pp. 376-383. Our cryptanalytic re-reading of the letter layer (grades H0
C0 S665 M29 I0 U77, with a matched control at 98.0%) agrees with his, but it is not a new result."

**Unsafe sentence (do not use):** "The only unsolved cipher letter in Gustav II Adolf's printed letters to
Oxenstierna, now read for the first time", or any wording that says the letter was unsolved, unread or open after
1888.

**Status consequence:** `found-solved` (CLAUDE.md rule 5): the solution already existed and was found by search.
The check-solved verdict "open" (NOTES.md, 24 Sept 2026) was wrong. The status line of NOTES.md is corrected in this
commit. status.json, STATUS.md and QUEUE.md row W1 are for the orchestrator to change; they are not touched here.

## 2. Item extracted from the repo

- Date and place: "Aff lägret vidh Nürnberg den 23 Julij, Åhr 1632" (dateline, printed p. 823). The heading OCR
  "1682" is a digit slip.
- Sender and recipient: Gustav II Adolf to Rikskansler Axel Oxenstierna. The editor's note on p. 823 describes the
  original as a "tripplet" on a quarto leaf, with a "duplett" and a "triplett" of the same day to Gustaf Horn.
- Edition: *Rikskansleren Axel Oxenstiernas skrifter och brefvexling*, senare afdelningen, första bandet, *Konung
  Gustaf II Adolfs bref och instruktioner* (Stockholm 1888), letter 602, pp. 821-823. **Edited by Per Sondén**, who
  signs the preface ("Redaktionen af detta band har ombesörjts af undertecknad. Per Sondén", djvu text of
  `rikskanslerenax00styfgoog`, around line 140). The repo's "Styffe's edition" / "Styffe no. 602" is a
  misattribution: C. G. Styffe edited *Konung Gustaf II Adolfs skrifter* (1861), not this volume. Corrected in
  NOTES.md.
- Editor's footnote, checked verbatim against the djvu text (line 39890): "Nyckeln till ofvanstående chifferbref
  har af utgifvaren icke i riksarkivet kunnat återfinnas, men då intet tvifvel är om, att det är ett Konungens bref
  till Rikskansleren, hvartill möjligen en lösning sedermera kan finnas, har det här blifvit meddeladt." The repo
  quotes it correctly. The gloss "[unsolved]" is correct only for the moment of printing.
- The reading, grades and phrases: NOTES.md, R3 section. Phrases R3 gave for the search: "bakefter oss i ett godt
  positeur", "vid Mitou", "höglar bevuxen", "retranchera eder allestädes rundt omkring", "en deel under Holcken".
- What R3 and the earlier workers searched: the edition's own footnote; Styffe 1861 (*Konung Gustaf II Adolfs
  skrifter*, does not print the letter); Irmer 1888 (one unrelated hit); WebSearch; Cryptiana, CATALOG.md,
  LANDSCAPE.md; both solver repositories; DECODE through Aymeloglu's cached sweep; the Riksarkivet Sök-API.
  Unreachable for them: sok.riksarkivet.se/oxenstierna (captcha), OpenAlex, Semantic Scholar, DiVA, the
  Waldispühl paper. **No full-text phrase search on the decoded text was run before this audit.** Historisk
  tidskrift, the national historical journal, was not searched at all.

## 3. Search log (this session, 24 Sept 2026)

| family | what was searched | result |
|---|---|---|
| (a) the edition itself | djvu text of `rikskanslerenax00styfgoog`, fetched once: every "chiffer/chiffr/nyckel/dechiff" hit, the preface, the footnote, the note on p. 823, the register and the errata ("Rättelser") at the end | Footnote verified verbatim. Preface by Per Sondén: cipher letters are printed with the solution in brackets "efter någon af de i riksarkivet ännu förvarade klaverna" (from one of the keys still in the Riksarkivet); 602 had none. Errata and register: no correction or solution for 602. |
| (b) the King's printed letters | Styffe, *Konung Gustaf II Adolfs skrifter* (1861), `konunggustafiia01gustgoog`; *Arkiv till upplysning om svenska krigens ... historia* vols 1-2 (`arkivtillupplys00mankgoog`, `arkivtillupplys01mankgoog`, 1854-1861); *Handlingar rörande Skandinaviens historia*, the four chronological-register volumes (`handlingarrrand00/01/02/04scangoog`) | No 23 July 1632 letter to Oxenstierna in any of them (grep for "23 Jul" dates and the phrases). *Sverges traktater* not searched (a treaty series, not a natural home for a field letter). |
| (c) Oxenstierna series | Ser. II vols 2-12 on IA (`rikskanslerenax00akadgoog`, `02akadgoog`, `03akadgoog`, `00palagoog`, `01palagoog`, `01styfgoog`; `01akadgoog` returned an empty text file) grepped for the phrases and the date. Ser. I vol 7 (*Brev 1632*, 1926), HathiTrust `mdp.39015026707094`, full view: read through the HTRC Extracted Features API (per-page word bags; the HathiTrust page text is Cloudflare-blocked, 403 on one request, not retried) | Ser. II: no hit. Ser. I vol 7: seq 549-550 and 559 cite "Skrifter ... 821/823" in the notes to Oxenstierna's letters of late July 1632 (cross-references to letters 602 and 603); no cipher vocabulary on those pages, so the 1926 editors do not print a solution there (word bags only, not read as text). Seq 627-629: Oxenstierna to the King, October 1632, partly in cipher with codes 1538-3760, decoded by the 1926 editors from "klaverna" (the keys), with "duplett" notes: a key of this large nomenclator was known in 1926. A lead for the codes, not a prior print of 602. |
| (d) holding archive | Riksarkivet Sök-API (`data.riksarkivet.se`): "dechiffrering" (2 hits, 1710-1791, irrelevant), "dechiffrering" 1620-1640 (1: SE/RA/202), "chiffer" 1632 (4: SE/RA/202, SE/RA/202/1 and two irrelevant), "chifferbrev" (0 relevant); two further attempts failed with the host's known SSL_ERROR_SYSCALL. E 614 not re-queried (R5 did it the same day: no item-level note, not digitised). `sok.riksarkivet.se/oxenstierna?Fritext=chiffer`: 302 to captcha, one request, not retried | No catalogue note of a decipherment. The online Oxenstierna database is **unreachable** (captcha). |
| (e) scholarship | CrossRef: "Gustav Adolf cipher", "Oxenstierna cipher", "Swedish chancery cipher seventeenth century", "chiffer Gustav II Adolf" (nothing relevant). HAL: "Oxenstierna AND (chiffre OR cipher OR chiffrement)" (0). OpenAlex: 429 twice ("temporarily rate-limited"), **unreachable**. Semantic Scholar: 429 twice, **unreachable**. DiVA and historisktidskrift.se not queried (the IA full-text hit below settled the class) | CrossRef and HAL index no nineteenth-century Swedish journal content; the decisive item was found through IA full text instead. |
| (f) full text | Internet Archive full-text search across all items (`be-api.us.archive.org/fts/v1/search`), eight queries: "höglar bevuxen" (0), "Nyckeln till ofvanstående chifferbref" (1, the edition), "vid Mitou" (0), **"godt positeur" (1: `historisktidskriftsv8`)**, "under Holcken" (2, a Danish topography, irrelevant), "Nürnberg den 23 Julij" (0), "23 Julii 1632" Oxenstierna (0), Gustaf Adolf chifferbref 1632 Oxenstierna (17, none relevant except the edition). Then `historisktidskriftsv8` djvu text and page map, fetched once, read pp. 376-384. HathiTrust: the Bibliographic API for record 001245720 (the volume list of both series) | **Hit: Torpadie 1888.** The phrase search on R3's decoded text found it on the fourth query. Note that R3's phrases are in R3's normalised spelling and several missed ("höglar" is "hyglar" in Torpadie, "Mitou" is "Mitov"); "godt positeur" matched because the spelling agreed. |
| (g) solver repositories and DECODE | Fresh shallow clones of dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers, grepped for Torpadie, Oxenstierna, Gustav Adolf, Styffe, Sondén, Nürnberg + 1632 | Neither has this letter or cites Torpadie. Bourdeau's `riksarkivet1628/` and `baner1640/` are other items. DECODE public pages not re-queried (login is out of scope; the cached sweeps show no row for this letter). |
| Google Books | Not this session's: queries handed to LANE V in ROOM.md, marked optional because the class is decided | none |
| JSTOR | One row appended to JSTOR-QUEUE.tsv (later scholarship citing Torpadie) | queued; does not affect the class |

Requests this session: archive.org 26 (1 djvu text of the edition, 13 djvu texts of editions, 1 journal djvu text,
1 page map, 1 metadata, 5 advancedsearch, 8 be-api fts; one request at a time, at least 2 s apart);
data.htrc.illinois.edu 2; catalog.hathitrust.org 1; babel.hathitrust.org 1 (403 Cloudflare, stopped);
data.riksarkivet.se 6 (4 × 200, 2 × SSL_ERROR_SYSCALL); sok.riksarkivet.se 1 (302 captcha, stopped);
api.openalex.org 2 (429, stopped); api.crossref.org 4; api.semanticscholar.org 2 (429, stopped);
api.archives-ouvertes.fr 1; github.com 2 shallow clones; WebSearch 1.

## 4. Did we first-decipher?

No. Torpadie printed the plaintext, the method and the key table of the letter layer in 1888, and read or guessed
about ten of the codes. The editors of *Historisk tidskrift* confirmed his key from other letters in which the same
two-digit cipher had since been found deciphered. R3's contribution is a modern, controlled, reproducible re-reading
(`tools/decode_key.py --check`), useful as a check on Torpadie. It is not a discovery. Where the two differ,
Torpadie had the whole context and is probably right. A collation of the two per token is a possible small
contribution (a dataset: the key table, the codes, the discrepancies). It would be class N0 and must say so.

Evidence quality: high. The article names letter 602, quotes the incipit, prints the full plaintext with the
dateline, and prints a key table (garbled in the OCR; the page images were not viewed this session). IA page map: p. 376 =
leaf 385, p. 382 = leaf 391, p. 383 = leaf 392; https://archive.org/details/historisktidskriftsv8/page/382.
Confidence in N0: very high.

## 5. Postmortem

**Failure:** a printed cipher was declared "open" because the edition's own footnote said the key was lost, and
nobody asked whether anyone had solved it after the volume came out. The footnote itself invites a later solution
("hvartill möjligen en lösning sedermera kan finnas"). The obvious place for such a solution, the national
historical journal in the year of publication, was never searched. Three workers (check-solved, key hunt, original
hunt) and the solver treated the footnote as the current state instead of the state in 1888. No phrase search on
the decoded text was run until this audit. One run in normalised spelling found it in minutes.

**Contributing causes:** (1) the check-solved brief lists editions of the sender and recipient but not the period
journals that review a new edition (Historisk tidskrift, Svensk historisk tidskrift, the Scandia/Karolinska
förbundets årsbok equivalents); (2) IA full-text search across all of IA ("unasked" in `tools/print_check.py`) was
not run on the plaintext before the solver's result was reported; (3) the misattribution to Styffe could have sent a
search for reviews of the edition to the wrong editor.

**Proposed brief change (for the retrospective):** in check-solved and in the solver's search log, for any cipher
printed "unsolved" in an edition, search the national historical journal(s) for the five years after the edition's
date for the edition's title and the letter number, and run `tools/print_check.py` on the decoded phrases in both
normalised and period spelling before reporting.

**Corrections made in this commit:**
- NOTES.md: status line changed from `partial` to `found-solved`, with the Torpadie citation; a correction block
  added at the top; "Styffe's second series" corrected to Per Sondén's volume (1888); the check-solved "Verdict:
  open" marked wrong in place; the "[unsolved]" gloss qualified as "at the time of printing".
- REQUEST.md: a note at the top that the letter layer and part of the codes were solved in 1888, so the requests no
  longer serve a decipherment of letter 602. E 614 and the Horn letters may still settle Torpadie's hedged codes.
  The owner decides whether any request stays.
- reading.txt heading ("Styffe no. 602") is generated by `decode.json` / `tools/decode_key.py`; not edited here, to
  keep `--check` green. Flagged in ROOM.md for LANE R.
- Left for the orchestrator (not this session's files): status.json, STATUS.md, QUEUE.md row W1 ("Styffe ed.",
  "No [decipherment]"), `.claude/briefs/runs/*W1*`, and any board card that calls this target open or partial.

## 6. Second-opinion claims not confirmed

None filed. No second-opinion prompt written: the class is N0, and CLAUDE.md asks for one only at N3 or above.

## Google Books queries (LANE V runner), 24 Sept 2026

LANE V worker (Sonnet), running the 5 queries LANE W worker C marked **optional** in ROOM.md 06:26 UTC ("class
already N0 from IA full text"). Run last, after the P4 and rah-canada-1869 queries, since the cap allowed. This
session only ran the queries and records what came back; it does not decode and does not assign or change a class.

**Queries (5, verbatim from ROOM.md):** "Torpadie" chifferskrift; "godt positeur" "här oppe"; "hyglar bevuxen"; "vid
Mitov"; "Några ord om chifferskrift". Full results: `google-books-2026-09-24.tsv`.

**Hit counts:** all 5 queries returned hits. "Torpadie" chifferskrift and "Några ord om chifferskrift" each returned
300 items (a bibliography-name/title match, capped by the API's totalItems estimate, 4 and 2 respectively after
`filter=full`); "godt positeur" "här oppe", "hyglar bevuxen" and "vid Mitov" each returned 2 items (1 each after
`filter=full`).

**Hits whose snippet contains the quoted phrase (selected -- these directly corroborate the N0 finding already on
record; the bibliography-citation hits for "Torpadie"/"Några ord om chifferskrift" are omitted here as duplicative
of section 3's IA finding):**

1. `"godt positeur" "här oppe"` -- volume `W38LAAAAIAAJ`, *Historisk tidskrift* (1887 -- catalogued a year off from
   the 1888 volume already cited in section 1/3; likely a bound-volume or scan-metadata year, not a second
   printing): "...godt positeur än här oppe; så är fördenskuld vår nådigeste vilie, dett I correspondere medh her
   Steen Bielke..."; and volume `WQHKWzqiA2wC`, *Hemlig skrift* (Henning Stålhane, 1934), same wording verbatim --
   a **later secondary source reprinting Torpadie's plaintext**, corroborating it independently of the 1888 journal.
2. `"hyglar bevuxen"` -- same two volumes, `W38LAAAAIAAJ` and `WQHKWzqiA2wC` (Stålhane 1934): "...hyglar bevuxen, så
   att I ej behöfve till att retranchera eder allestädes rund omkring, uthan bruka samma hyglar eder till fordeel
   och retranchement. Corresponderer och flitigt med her Jahan Baner..."
3. `"vid Mitov"` -- same two volumes: "...vid Mitov, nembligen, att I ej gå uhr det ena retrancherede lägret för än
   I veta, hvar I kunne antreffa en ort..."
4. `"Torpadie" chifferskrift` -- volume `xoqSF8GzYrMC`, *Historisk tidskrift* (1889, a bibliography/register volume
   citing the 1888 article): "...chifferskrift. Af R. Torpadie. Utg. sid. 376-383 af Historisk Tidskrift 1888.
   Inneh. bl. a. upplösning af ett chifferbref från k. Gustaf II Adolf till A. Oxenstierna af d. 23 Juli 1632."; and
   volume `3fAtAAAAIAAJ`, *Svensk historisk bibliografi* (1907), same citation. Also volume `3S8rhOEmDIIC`, *The
   Codebreakers* (David Kahn, 1996): "...Torpadie solution: 'Några ord om chifferskrift,'..." in Kahn's endnotes.
5. `"Några ord om chifferskrift"` -- same *Historisk tidskrift* 1889 bibliography hit and the Kahn citation, plus
   volume `dDkiAQAAIAAJ`, *Nordisk familjebok* (1906): "...'Några ord om chifferskrift' (i Hist. tidskr. VIII, s.
   376)."

**Effect on the class:** none needed -- already N0. These hits are useful corroboration, not new information: two
independent secondary sources (Stålhane 1934, a Swedish cryptology history; Kahn 1996, *The Codebreakers*) confirm
Torpadie's 1888 plaintext and cite his article by name, and several bibliographies (1889, 1891, 1907) index the
article under Oxenstierna/Gustav II Adolf. No hit suggests a decipherment of this letter earlier or independent of
Torpadie.

Requests this session: www.googleapis.com 10 (5 base queries + 5 `filter=full` re-runs, since all 5 had hits), one
at a time, at least 3 s apart, key never printed. No other host.
