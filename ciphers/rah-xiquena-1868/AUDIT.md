# AUDIT: rah-xiquena-1868, "Copia del telegrama cifrado al Ministro de la Reina en Munich" (RAH 9/6963, Leg. XXIV nº 158)

Verifier: V6-XIQ (LANE V6 worker, Opus), 25 Sept 2026, 19:05-19:20 UTC. Parent: LANE V6 orchestrator
session_01V2BHwhVh1k72qSYuBFCyGd. This session did not capture or transcribe the item and does not defend the
capture worker's conclusions. Nothing was decoded (there is nothing to decode).

Claim under audit (LANE R6 worker Y10, ROOM 18:27 UTC 25 Sept 2026; NOTES.md "Y10" section): the item is, in the
archive's file copy, entirely plaintext (8 leaves, certified and signed), with no cipher signs anywhere; status
`found-solved`.

## Verdict

| Item | Class | key | Prior plaintext | Prior decipherment | Evidence | Confidence |
|---|---|---|---|---|---|---|
| Telegram, Ministro de Estado to the Spanish minister in Munich, Madrid 3 May 1868 ("1350 Grupos") | **N0** | **n/a** (no ciphertext survives in the item, no key was applied or recovered; the plaintext is the archive's own clear copy) | **Yes, the item itself.** RAH holds only the clear text, a certified copy "Es copia conforme", signed by the Conde de Xiquena as Subsecretario de Estado, public-domain and online at bibliotecadigital.rah.es (registro 15711). | Not applicable: there is no ciphertext on the item, so no decipherment of it by anyone, us included. The clear text of the message sent in cipher has been on file since 1868. | Strong: all 8 leaves eye-checked on disk by this verifier (below). | High |

**Status word: `found-solved`** (confirmed, NOTES.md first line agrees). Reason: CLAUDE.md's vocabulary has no
"not a cipher" word. `closed-negative` is wrong: it means a solver ladder failed with controls, and nothing was
attempted or needed. `solved` is wrong: it implies a reading of ours. `found-solved` is the right word because the
cipher telegram as transmitted (1350 groups) is the target, and its plaintext already exists in the holding archive,
with nothing left to read. On the board: **retire it as found-solved, kind `contribution` at most (a correction of
our own queue row, not a catch)**, and never count it as a solve or a found-solved "catch" of note. In the README
F-grades, this is **F0-equivalent**: the holding archive's own title already calls the item a *copia* of the
telegram, so no catalogue is wrong and nobody outside this repository needs telling. The only error was our scout's
reading of "telegrama cifrado" as a surviving ciphertext (QUEUE row E1). Same pattern as rah-canada-1869 (catalogue
title names a cipher, what survives is the clear text), but weaker: that item at least carries ciphertext.

**Safe sentence:** "RAH 9/6963 (Leg. XXIV nº 158) holds only the certified clear-text copy of a telegram sent in cipher
(1350 groups) from Madrid to the Spanish minister in Munich on 3 May 1868. The item carries no ciphertext, so there is
nothing to decipher; the plaintext is the archive's own (N0)."

**Unsafe sentence:** "We deciphered / solved / read the Conde de Xiquena's cipher telegram." Also unsafe: "unsolved",
"open cipher", "cryptanalysis candidate", "recovered the plaintext", or any wording that the plaintext is newly known.
The transcription in `plaintext.txt` is a transcription of a clear document, not a reading.

## 1. Item extract

- **Date / place:** Madrid, 3 May 1868 (heading on p2).
- **Sender:** "El Ministro de Estado" (not identified by name here; not needed for the class). **Certifier:** the Conde de Xiquena, Subsecretario
  de Estado, who signs the copy (p8). He is the sender of the copy to the Queen's archive, not the author of the telegram.
- **Recipient:** "Ministro de S.M. en Munich", instructed to go to Vienna or wherever Franz Joseph is.
- **Content:** (1) transmit Isabel II and Francisco's French telegram to the Austrian Emperor and Empress announcing
  the betrothal of Infanta Isabel to the Conde de Girgenti; (2) discreetly get the Emperor to relieve Girgenti of his
  Austrian captaincy by telegram and wish to see him in Vienna already married, so that Girgenti does not insist on
  going to Vienna first and does not suspect the Spanish court's hand.
- **Heading:** "Telegrama cifrado. 1350 Grupos." -- the transmission form, recorded on the copy.
- **Identifiers:** RAH Sig. 9/6963; Leg. XXIV nº 158; registro 15711; oai:bibliotecadigital.rah.es:15711; idImagen
  10141611-10141618; viewer path 1008498.
- **What the capture side searched:** RAH OAI DIDL record (no description, no "Publicado" note); Google Books 3-6
  queries on Xiquena/telegrama/cifrado (6 unconfirmed hits); earlier CX2 sweep (Europeana, BOE Gaceta, BNE Hemeroteca
  403, cryptiana, DECODE cache, both solver repositories).

## 2. Task 1: is there any ciphertext in the item?

**No.** This verifier opened all 8 images on disk (`images/p1.jpg`-`p8.jpg`, 3300-3560 px wide) one by one:

| Leaf | What is on it | Cipher signs? |
|---|---|---|
| p1 | Wrapper. Top: "Leg. XXIV, nº 158" in a **modern** pencil/ink archival hand (NOTES.md called it "period hand"; corrected below); red "1" top left; a small marginal pencil mark, left edge, mid-leaf (an archivist's tick or numeral, not a cipher group); ribbon at left. | No |
| p2 | Heading "Telegrama cifrado. / 1350 Grupos. / Madrid 3 de Mayo de 1868. / El Ministro de Estado / al / Ministro de S.M. en Munich", rule, then clear Spanish "S.M. la Reina, Nuestra Señora manda se traslade V.E. inmediatamente a Viena..." | No (the only digits are "1350" and the date) |
| p3 | Clear Spanish then the French telegram "A LL. Majestés Apostoliques les Empereurs d'Autriche / Nous avons la douce satisfaction d'annoncer..." | No |
| p4 | French close "(Signé: Isabel. = Francisco. =)", "Segundo: Es la voluntad de S.M. la Reina que el casamiento..." | No |
| p5 | Clear Spanish; red-and-gold ribbon at right edge (binding). | No |
| p6 | Clear Spanish "con la mayor reserva una misión delicadísima..." | No |
| p7 | Clear Spanish "...grama de Nuestros Reyes participándole el convenido enlace..." | No |
| p8 | Close; "Es copia conforme: / El Sub. Secretario de Estado: / El Conde de Xiquena" with paraph. Lower half blank. | No |

One hand throughout p2-p8, a formal chancery copperplate, no interlinear writing, no numbers groups, no marginal key,
no pen marks of the kind in rah-canada-1869. **What the leaves are:** a fair certified copy of the despatch text, made
in the Ministerio de Estado and sent up to the Queen (the item sits in the Archivo de Isabel II, the Queen's papers,
not the ministry's). Whether it was copied from the minute before encipherment or from a decipherment is not
decidable from the leaves, and does not change the class: either way the clear text of the transmitted cipher
telegram is the item. The brief's phrase "a deciphered file copy" is therefore slightly too specific; "the clear-text
copy of a telegram sent in cipher" is what the leaves support.

## 3. Task 3: short print check (is this telegram's text in print?)

Not needed for N0 (the plaintext is on the item regardless of print), run as the brief asks, to see whether the
wording has an editor. Hosts: Google Books (`&key` and `&country=US`, >=3 s apart) and IA be-api full text (2 s apart).

| Family | Query | Result |
|---|---|---|
| Google Books | `"Conde de Girgenti" "relevara de su cargo"` | 0 |
| Google Books | `"mariage arrêté entre notre fille" Girgenti` | 0 |
| Google Books | `"douce satisfaction d'annoncer" Girgenti` | 0 |
| Google Books | `"1350 grupos"` | 3, all noise (Veracruz history 1975, Chilean catalogue 1970, statistics 1950) |
| Google Books | `"Girgenti" "Munich" telegrama 1868 Viena` | 0 |
| Google Books | `"Xiquena" Girgenti telegrama` | 0 |
| Google Books | `"le relevara de su cargo de capitán"` | 0 |
| Google Books | `"verlo en Viena ya casado"` | 0 |
| Google Books | `Girgenti Viena escuadrón licencia casamiento Infanta 1868` | 0 |
| Google Books (control: the topic is in print, so the mechanism finds it) | `"Conde de Girgenti" Infanta Isabel 1868` | 300: Pineda y Cevallos Escalera, *Casamientos régios de la Casa de Borbón* (1881, full view: "En Abril del año de 1868 se concertó el matrimonio..."), Pirala *Historia de la interinidad* (1876), others |
| Google Books (control, French) | `"Comte de Girgenti" "Infante Isabelle" mariage 1868 Autriche` | 7: *Le Mémorial diplomatique* 1868 (full view; snippet on the marriage and Girgenti's Austrian service), *Messager de la semaine* 1868, *L'Echo de la France* 1868 -- none snippets the telegram's wording |
| IA fts | `"Conde de Girgenti" "Munich"` | 107 hits, top 6 are biographies and 1868 press (none the telegram) |
| IA fts | `"Comte de Girgenti" "douce satisfaction"` | 3: Rohrbacher *Histoire universelle* (two copies), *Le Monde illustré* 1868 -- the phrase is not joined to the telegram in any snippet |
| IA fts | `"mariage arrêté entre notre fille"` | 0 |
| IA fts | `"verlo en Viena"` | 3, all unrelated (20th-century novel, Napoleonic anecdote) |
| IA fts | `"sin abordar la cuestión de frente"` | 1, unrelated (Uruguay 1921) |
| IA fts | `Xiquena Girgenti` | 203, noise (1880s-90s press; Xiquena as minister of Fomento) |

**Result:** the betrothal and Girgenti's Austrian service are well documented in 1868-1881 print (the controls), but no
phrase of this telegram, French or Spanish, was found in Google Books or IA full text. Not searched this pass: the
full text of *Le Mémorial diplomatique* 1868 and Pineda y Cevallos 1881 page by page (both full view; the French
announcement telegram to the Emperors is the kind of text the *Mémorial* printed), Hemeroteca Digital BNE (403 to
CX2), the Gaceta de Madrid body text, Spanish diplomatic editions, open-index scholarship. None of these can move the
class, which rests on the item itself.

## 4. Did we first-decipher?

No. There was no ciphertext to decipher. The repository transcribed a clear document. Nothing about this item may be
described as read, deciphered, recovered or new.

## 5. Postmortem

Failure: the catalogue title "Copia del telegrama cifrado" was read by the scout (QUEUE row E1, 24 Sept) and by
check-solved (CX2, "a genuine cryptanalysis candidate if pursued") as promising a surviving ciphertext, when
"Copia" already said it was a copy. Cost: one scout row, one check-solved pass, one capture worker (14 RAH requests).
Lesson for scouts: a catalogue title of the form "Copia del telegrama/despacho cifrado" names a clear copy until a
leaf shows cipher; fetch one text leaf (not the wrapper) before giving it a queue score. Y10 caught it at the first
look at the text leaves and set the status correctly.

## 6. Corrections made in the folder

- NOTES.md first line `found-solved` kept (agrees with the status-correction paragraph); a one-line verifier note
  added under the correction paragraph with the class and the board instruction.
- NOTES.md "Verdict" section (CX2, `open`, "a genuine cryptanalysis candidate if pursued") marked superseded in place.
- NOTES.md CX2 and Y10 descriptions of p1 ("in period hand") corrected: the "Leg. XXIV, nº 158" mark is a modern
  archival hand.
- `images/manifest.json` has the same "period hand" wording; not edited (outside this brief's files), noted here.

## 7. Requests

`www.googleapis.com/books` 11, `be-api.us.archive.org` 6. No other host. No subagents.
