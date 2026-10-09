found-solved
Source of the prior plaintext: R. Fruin / N. Japikse (ed.), Brieven aan Johan de Witt I (1919), pp.405-406, printed from the plain copy NA 3.01.17 inv.1538 ff.208-209 of this same letter (editor's footnote 1: "Dezelfde brief ook in onopgelost cijfer") -- the plaintext of this very item is in print (AUDIT.md item 1, N1); no prior key or decipherment of the cipher copy ff.210-211 located (AUDIT.md item 2, N3, key ours). Status set found-solved by GF4-BATCH6, 3 Oct 2026, by the brief's rule (premise check below); was partial.
Brieven aan Johan de Witt I (Fruin/Japikse 1919) p.405 read directly by the check-solved worker csHU on 24 Sept 2026 from the Huygens retroboeken page image (images/dewitt_01_405.jpg; footnote 1 "onopgelost cijfer" quoted in the sweep below), and pp.405-406 is the plaintext in plaintext_print.txt; the citation sat at line 9 until 2 Oct 2026, when GAPS-vanbeuningen-dewitt-1657 moved it here per check-solved.md's line-2 placement rule (RETRO-2026-09-24f).

# Van Beuningen circle to Johan de Witt: the same letter survives as a plain copy and an unsolved cipher copy, 19/29 September 1657

QUEUE row: HU8 (`QUEUE.md`, "Huygens and Nationaal Archief correspondence editions: letters noted in cipher
(LANE N harvest of 24 September 2026)"). Brief `.claude/briefs/runs/2026-09-24-lane-n-csHU.md`.

## Source

Johan de Witt correspondence, printed in R. Fruin / N. Japikse (ed.), *Brieven aan Johan de Witt*, Deel 1,
p.405, via the Huygens `retroboeken/dewitt` viewer (no login, `resources.huygens.knaw.nl`). No H.A.-style
archive number is used by this edition; the manuscript's archive location was not resolved this pass (see
below).

## Check-solved sweep, 24 September 2026

Run directly by this worker (Sonnet, no Workflow tool, no subagents).

1. **Editions first -- decisive, re-fetched and read directly this pass** (`images/dewitt_01_405.jpg`, page
   text also read as OCR): the printed letter itself (dated 19/29 September 1657 by internal content, no
   explicit heading on this page beyond the date) is a report from Copenhagen on Danish court affairs and
   English/Danish diplomacy. The editor's footnote 1, quoted verbatim:
   > "1) Niet van de hand van Van Beuningen. **Dezelfde brief ook in onopgelost cijfer, van een andere hand.**
   > - Op dezen brief schreef De Witt: 'beantwoort den 19en October 1657'. - Brieven van Van Beuningen van 7 en
   > 13 September, die De Witt 5 October beantwoordde (Brieven van De Witt, I, blz. 437), werden niet
   > aangetroffen."
   Translation: "Not in Van Beuningen's own hand. **The same letter also [survives] in unsolved cipher, in
   another hand.** De Witt wrote on this letter: 'answered 19 October 1657'. Letters from Van Beuningen of 7
   and 13 September, which De Witt's 5 October reply answered (Letters from De Witt, I, p.437), were not
   found."
   This confirms, directly from the primary edition and not merely from the harvest's paraphrase, that: (a)
   the text printed here is itself a copy, not Van Beuningen's autograph; (b) a **separate cipher copy of the
   identical letter, in a different hand, is stated to survive** -- a genuine known-plaintext pairing if both
   copies are still extant, the strongest class of lead in LESSONS.md's own ranking; (c) De Witt's 19 October
   1657 reply is referenced but its own text/archive location is not given on this page; (d) two earlier Van
   Beuningen letters (7 and 13 Sept 1657) that De Witt's 5 Oct reply answered were explicitly **not found**
   ("niet aangetroffen") by Japikse's own editorial search -- unrelated to this cipher, logged for
   completeness only, not a target.
2. **Post-edition literature search (check-solved.md's Oxenstierna/Torpadie lesson).** Located and read two
   modern secondary works specifically about this exact correspondence circle (De Witt-Van Beuningen, Northern
   War 1655-1660):
   - **M. Postma, *Johan de Witt en Coenraad van Beuningen: correspondentie tijdens de Noordse oorlog
     (1655-1660)*** -- the standard modern study of this exact correspondence (cited repeatedly by the second
     source below). Its own Academia.edu copy returned HTTP 403 (blocked to WebFetch) this pass; not read
     directly. Flagged unreachable, not scored negative on that basis alone.
   - A related scriptie/paper, "Macht en daadkracht tijdens de Noordse Oorlog" (vriendenvandewitt.nl PDF,
     fetched and OCR'd with `pdftotext` this pass since WebFetch could not parse the raw PDF stream): cites
     Postma's book about 20 times, including footnote 88, **"Van Beuningen aan De Witt, 15 maart 1656, Brieven
     aan Johan de Witt I, 328"** -- the same printed-edition page as this batch's HU7 (a different row, not one
     of this worker's assigned targets, but the same correspondence circle) -- confirming Postma's book cites
     this correspondence at the letter level. Grepped the full extracted text (1122 lines) for "cijfer" and
     "geheimschrift": **zero hits anywhere in the document.** Neither this scriptie nor, by extension, its main
     source (Postma) discusses the cipher content of any Van Beuningen-De Witt letter in the material actually
     read -- a real secondary-literature search, not merely "unreachable and skipped", even though it does not
     positively confirm Postma's book is silent on the cipher specifically (only this citing paper's own text
     was searched, not Postma's book itself, which could not be fetched).
3. **Community lists.** `sources/cryptiana/web/dutch.htm` re-read: mentions Coenraad van Beuningen only via an
   unrelated Petkum/Blencowe 1709 interception discussed on `blencowe2.htm` (a different correspondent, a
   different decade); no mention of this 1657 letter or its cipher.
4. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` grepped for "beuningen"/"de witt"/
   "nieuwpoort": zero hits.
5. **Solver repositories.** Fresh shallow clones this pass grepped for "beuningen", "de witt", "nieuwpoort",
   "3.01.17": no hit in either repository. (A distinct DECODE catalogue entry for "Rechteren tot
   **Borg**beuningen" -- a different person, a different century, NA 1.01.02/1.10.29, already solved -- is a
   surname false-positive worth recording so a later worker does not confuse it with Coenraad van Beuningen.)

## Verdict

**Status: open.** The editor's own footnote, read directly from the primary edition this pass, states plainly
that a separate cipher copy of this exact letter survives; no decipherment, key, or later print of that cipher
copy was found in the (partial, one source unreachable) secondary-literature search, community lists, DECODE,
or either solver repository.

**Copy status: archive confirmed, specific inv.nr NOT resolved.** LANE N2 worker csHU2 (24 Sept 2026) confirmed
**NA 3.01.17** ("Inventaris van het archief van Johan de Witt, raadpensionaris van Holland, 1653-1672") is the
correct archive, two independent ways: (1) the printed edition's own front matter (Deel 1, p.XVI) states "de
brieven aan De Witt alle eigenhandige originelen zijn" (the letters to De Witt are all autograph originals),
collated by Fruin against the originals, with Van Beuningen's Copenhagen letters named as the volume's single
most important chapter (p.XV); (2) EMLO's "Correspondence of Johan de Witt" project page (fetched via
`tools/browser_fetch.js`, curl alone returns HTTP 503 for both nationaalarchief.nl's own client-rendered search
API and emlo-portal.bodleian.ox.ac.uk, both logged as unreachable by curl and not retried a second time, per the
good-citizen one-retry rule) states plainly: "National Archive: inventory Raadpensionaris De Witt, 3.01.17" and
that EMLO indexes ~7,465 of the ~35,000-letter archive online (the "diplomatic correspondence" category, which
Sauniere-style diplomatic dispatches like Van Beuningen's would fall under) with links to digitised images
where available (EMLO's own caveat: "the manuscript images available at present are provisional... lower-
quality"). **The specific inv.nr for the 19/29 Sept 1657 letter, and separately for the "unsolved cipher copy,
van een andere hand" the footnote states survives, was NOT resolved this pass.** EMLO's advanced-search form
(`emlo.bodleian.ox.ac.uk/forms/advanced`) is a React app; a browser-rendered fetch with guessed URL query
parameters (`sender=Beuningen&date=1657`) did not actually filter the result set (it returned the full 16,736-
row catalogue unfiltered, confirming those aren't the real parameter names) -- finding the exact record needs
either interactive form-filling (`--type`/`--selector` in `tools/browser_fetch.js`) or NA's own `zvt.
nationaalarchief.nl` / `hub3.nationaalarchief.nl` search API, whose real endpoint path was not found by
guessing (both returned 503/404). No REQUEST.md written; the next worker should either drive EMLO's search form
interactively or find NA's real search API before ordering a copy -- and note the separate cipher copy "van een
andere hand" may not even be catalogued in EMLO the same way as the plain copy, since it is a different
physical item in a different hand.

**Kind: recovery.** A plain copy and a separately-surviving unsolved cipher copy of the identical letter is
exactly the known-plaintext pairing pattern LESSONS.md ranks as the strongest lead class -- stronger than a
mere sibling, since the plaintext itself (not just a related letter) is already in hand via this edition's own
print.

Search log (rule 10): reported above, per source. Not classified for novelty. Requests this pass:
`resources.huygens.knaw.nl` ~3 (book_data.js, 1 pages.json, 1 html_url OCR fetch, 1 image fetch), WebFetch 2
(Academia.edu, blocked 403; vriendenvandewitt.nl PDF, fetched and locally OCR'd with `pdftotext`, not a network
re-fetch), WebSearch 2, `github.com` 0 (reused clones already on disk this session). No subagents.

## Archive location pinned, 25 September 2026 (LANE OX worker OX-VB, session_017rmJ1jFJvbnXj6nrcb223x)

**NA 3.01.17, inv.nr 1538** (the yearly bundle "Missiven van Coenraed van Beuningen, extraordinaris gedeputeerde
naar Denemarken", 1657) is the exact inventory number. Found by fetching the archive's own full EAD inventory
(`www.nationaalarchief.nl/onderzoeken/archief/3.01.17/download/xml`, 3.1 MB, 41k lines, one curl request) and
grepping for "Beuningen" -- the subseries A.2.7.1.2 "Bijzondere gezantschappen" lists yearly bundles 1536-1541
for 1656-1658, with 1538 dated exactly "1657" (cover leaf confirms: "Denemarken / Ambassadeur Van Beuningen aan
den Raadpensionaris / 1657", image order 1 of the bundle). Its METS (`service.archief.nl/gaf/api/mets/v1/
dfa4b121-2476-41cf-8a1c-d784ec6f2050`, resolved from the EAD's own `<dao>` handle) shows the bundle is digitised
end to end: 289 leaf-images (two-page spreads), rightsMD `RIGHTSCATEGORY="PUBLIC DOMAIN"`, no login, served at
`service.archief.nl/api/file/v1/default/<uuid>` (no IIIF; full-resolution JPEG only, ~1-6 MB each).

Calibrated the bundle's chronological order by sampling images at roughly every 30th position and reading
datelines (p.1 cover "1657"; p.30 "27 January 1657"; p.60 "25 martij 1657"; p.180 "Coppenhagen 15en Julij
1657"), then narrowed in around the September/October area. Both copies of the 19/29 September 1657 letter
are in this same bundle, four leaf-images apart:

- **Plain copy: ff.208-209** (`NL-HaNA_3.01.17_1538_0208.jpg`, `_0209.jpg`). f.208's docket reads (abbreviated,
  another hand, top left) "...de 19en Octob. 1657" -- matching the printed edition's footnote quote of De
  Witt's own endorsement, "beantwoort den 19en October 1657", verbatim. The body opens "Mijn Heer, Hier wert
  van dag tot dag met groot impatientie verlangt na [...] Rosewinge..." which matches Brieven aan Johan de Witt
  I p.405's printed text from its first line, word for word (checked directly against `images/dewitt_01_405.jpg`).
  f.209 ends with the signature "UEd: ootmoedigen [en] verplichten dienaer, [signed] Van Beuningen" over the
  dateline "Coppenhagen de 19/29 [Septem]bris 1657" -- the same double Julian/Gregorian date the printed
  edition cites as "(19/29 September 1657)".
- **Cipher copy, "van een andere hand": ff.210-211** (`NL-HaNA_3.01.17_1538_0210.jpg`, `_0211.jpg`). Visibly a
  different, more cramped hand than ff.208-209, matching the footnote's own description. Opens "Hier voort van
  dag tot dag met groot impatientie verlangt na U [cipher numbers]..." -- the identical opening, with content
  words replaced by comma-separated two-digit numeric groups and colons apparently marking word boundaries;
  plain Dutch function words (mijn, heer, met, over, onder, daer, ...) are left uncoded. Ends with the same
  closing formula and the identical double date, "Coppenhaghen den 19/29 [Septem]bris 1657", confirming this
  is the cipher copy of *this* letter and not of the other same-day dispatch below.

**Not the target, kept for context:** ff.206-207 carry the end of one Van Beuningen dispatch and the whole of
another, both also dated 19/29 September 1657 but on different subject matter (a Brandenburg/Poland/Sweden
report) -- Van Beuningen evidently sent more than one letter to De Witt on the same courier date. Recorded here
so a later worker does not confuse it with the target or re-spend a pass identifying it.

Images fetched and committed: `images/NL-HaNA_3.01.17_1538_020{6,7,8,9}.jpg`, `_021{0,1}.jpg`, plus single-page
crops of the two cipher leaves at `images/cipher_crops/0210_right.jpg` and `0211_left.jpg` for the transcription
pass. `images/manifest.json` records the inventory/METS URLs and per-image content. Folder size 9.5 MB, well
under the 30 MB budget. Requests this pass: `www.nationaalarchief.nl` 2 (archive landing page, EAD XML download),
`service.archief.nl` 1 (inv.nr 1538 METS) + 15 leaf-image fetches (calibration samples + the four target leaves
+ two context leaves), all >=1.5s apart, single host, well under the good-citizen per-session cap. No EMLO fetch
was needed this pass (the EAD route alone resolved the inv.nr; EMLO's advanced-search API remains unresolved,
see below, but is now moot for this target).

**Kind confirmed: recovery by known plaintext.** Both copies of the same letter are now in hand as images, not
merely inferred from the printed edition's footnote. Key/alignment recovery is explicitly NOT attempted this
pass (out of this worker's brief); a two-pass blind transcription of the cipher leaves follows below for the
next solver.

## Cipher transcription, 25 September 2026 (LANE OX worker OX-VB)

Two independent blind transcription passes were run against `images/cipher_crops/0210_right.jpg` and
`0211_left.jpg` (Sonnet subagents, per `.claude/briefs/transcription.md`), each numbering the manuscript's 73
lines L01-L73 continuously across both leaves, neither shown the other's output or the plaintext. Raw passes:
`passA.tsv`, `passB.tsv`. Both agents self-reported (correctly) that they had no true pixel-zoom/crop tool
beyond re-reading the same full-leaf JPEG, and flagged low confidence on most of the connecting plain-Dutch
prose while reporting moderate-to-good confidence on the numeric cipher clusters.

Reconciled with `tools/reconcile_passes.py` (wide format). First run scored only 23.6% agreement, which turned
out to be a tokenisation artefact, not a real reading gap: pass A wrote unbroken runs like `51,32,61,10,57,51:`
as fewer, larger tokens, while pass B split every comma onto its own space-separated token -- the aligner was
comparing token counts, not signs. Normalised both passes (a space forced after every comma/colon;
`reconciliation/passA_normalized.tsv`, `passB_normalized.tsv`) and re-ran: **78.0% overall agreement (672/862
aligned columns)**, above the 60% gate in transcription.md. Per-line agreement is bimodal exactly as both
passes predicted: most number-only lines score 0.85-1.00, most prose-heavy lines score 0.35-0.65.
`reconciliation/disagreements.tsv` (191 rows), `agreement.tsv`, and the auto-generated `ciphertext_draft.tsv`
(H for agreement, M + alternate for disagreement) are kept for audit.

**Settled from the image against the disagreement list** (this worker, not a third blind pass): of 191
disagreement rows, only 7 were disagreements between two actual digit values (the rest were spelling variants
of the same word -- dagh/dag, maer/maar -- or one pass mis-tokenising a plain word as a number or vice versa).
Checked all 7 against tight crops of the manuscript:
- L04 pos.7 "bij" (a plain word, not a digit -- pass B misread it as "6?,"), L04 pos.10 "25," (pass A had
  "23,"), L55 pos.1 "26," (pass A had "28,"), L58 pos.7 "10," (pass A had "19,") -- all confirmed and upgraded
  to H.
- L37 pos.10: the manuscript shows a cramped, unseparated-looking cluster where both passes guessed different
  2-digit numbers ("20," vs "50,"); close inspection suggests it may actually be a 3-digit run "250" with no
  visible internal comma. Left at M with the ambiguity noted rather than silently resolved (rule 2) -- **this
  position needs a fresh look at a proper high-resolution crop, not a screen-rendered read, before any decode
  attempt relies on it.**

Also settled the closing formula and dateline (L68-L73) directly from a tight crop, since both passes had
marked most of it [ILLEGIBLE] or guessed inconsistent structure: confirmed "Mijn Heer" (L69), "UEd:" (L70,
matching pass B), and critically **"Coppenhagen" as the place in the dateline (L73), not pass A's "'s
Gravenhaghe"** -- consistent with the letter's known place of writing and with the plain copy's own dateline on
f.209. The signature (L72) remains illegible (a flourish, not readable text) and the month abbreviation before
"1657" (L73 pos.4) is still unresolved at M; for context only (not read off this leaf), the plain copy's own
dateline on f.209 gives "de 19/29 [Septem]bris 1657" for the same letter. The opening word of the closing
formula (L68) is likewise still M -- neither pass's guess ("Ick blijf" / "Blijft") matches what the image
appears to show, tentatively closer to a "Godt blijft/blijve" formula, not confirmed.

**Final tally, `ciphertext.tsv` (862 tokens):** 666 H (77.3%), 196 M (22.7%), 0 C, 0 S, 0 I -- no key or known
plaintext was used to produce this transcription (grade C would require that); the H tokens are grade H only
in the rule-4 sense of "read directly from a source image with confidence", not from a key. The M tokens are
concentrated in the connecting Dutch prose between cipher-number runs (mede, over, onder, daer, and similar
short function words used inconsistently by 17th-century secretary hand); **every numeric cipher token that
could be checked against the image has now been checked**, with only the single L37 pos.10 cluster left
genuinely ambiguous. Reconciling the remaining ~190 M-graded prose tokens to a higher grade would need either a
third independent pass or per-line crops sharper than the two-page spreads fetched this pass (see Access
playbook note above: `service.archief.nl` serves full-resolution JPEG only, no IIIF zoom) -- left as the clear
next step for whoever takes this to key recovery, not attempted further this pass (out of this worker's brief).

**Key recovery was not attempted**, per this worker's brief -- the next step is a solver session using
`ciphertext.tsv`, `plaintext_print.txt` (the known plaintext, pp.405-406 of the printed edition), and an
alignment/EM approach per LESSONS.md's "look for the sibling" method, since this is exactly that pattern: a
cipher copy with its plaintext already in hand, not a blind cryptanalysis problem.

## HU8: archive location, 24 September 2026 (LANE N2 worker csHU2)

Confirmed NA 3.01.17 (see Copy status above, revised). Requests this pass: `www.nationaalarchief.nl` ~3
(3.01.17 collection landing page, the "Briefwisseling van Johan de Witt" research-guide page and index search
page, all >=2s apart), `resources.huygens.knaw.nl` ~9 (De Witt book_data.js, pages.json source=1, 6 front-
matter OCR fetches [pages X-XVI] read for the "eigenhandige originelen" line, `retroboeken/heinsius` book's own
search form reused from the same-session HU1/HU2 work), 2 attempted `zvt.nationaalarchief.nl`/`hub3.
nationaalarchief.nl` API-endpoint guesses (503/404, abandoned, not retried), `emlo-portal.bodleian.ox.ac.uk` 1
curl attempt (503/connection timeout, logged unreachable, not retried per the one-retry rule) + 2 browser_fetch
(worked: the project overview page, and one advanced-search attempt whose guessed query params did not
actually filter). No subagents.

## Key recovery, 25 Sept 2026 (LANE OX solver OX-VBS)

No host fetches this pass; worked entirely from `ciphertext.tsv` and `plaintext_print.txt` already on disk.
`key.tsv`, `decode.json`, `reading.txt`, `reading_tokens.tsv` added/regenerated;
`tools/decode_key.py ciphers/vanbeuningen-dewitt-1657 --check` exits 0.

**Status stays `partial`.** This is a genuine but incomplete key recovery: the system is identified with strong
evidence, a 9-entry nomenclator is recovered, and 25 code-values covering 13 distinct letters are recovered
(12 letters cross-validated in 2+ independent words -- several by an independent fresh-instance subagent, see
below -- 1 from a single word only). The rest of the alphabet, and one real conflict, are unresolved and listed
below rather than guessed.

### System

The cipher copy interleaves two things:
1. **Plain, uncoded Dutch** for function/connective words (de, van, met, op, dat, sal, niet, ...) and some
   content words the copyist evidently didn't bother to encode -- these are simply the ciphertext's own
   transcribed signs, passed through unchanged (`key.tsv` grade `clear`, excluded from the H/C/S/M/I cipher
   tally per rule 4, since they are not a decoded cipher token).
2. **Coded runs of 1-3 digit numbers**, comma-separated within a "word" and colon-terminated at its end, of
   two kinds:
   - **A small closed nomenclator**: a handful of distinct codes (mostly 100-225) that each recur a few times
     through the letter and always at a position matching the same recurring name or set phrase. Established
     by *count* matching (a code's occurrence count against a term's occurrence count in `plaintext_print.txt`)
     **and** direct context matching at 2+ of each code's occurrences (not just the first).
   - **A homophonic letter-substitution alphabet**: the far more common 1-2 digit codes (values roughly 4-65)
     each stand for one Dutch letter; several distinct codes can stand for the same very frequent letter
     (homophones -- 'e' alone has at least three: 50, 51, 52). Evidence: a 9-code run lines up exactly with the
     9-letter proper name "Rosewinge" (see below), with the letter 'e' -- which recurs at positions 4 and 9 of
     that name -- getting the *same* code (51) both times; several other code-runs line up letter-for-letter
     with plaintext words of the identical length (agent=5, wil/versoeck partial=3+8, met=3). u and v (and
     probably i/j) are evidently not distinguished, consistent with this period's orthography (LESSONS.md).

Applying the 13 recovered letter-codes globally (not just at the words used to derive them) reproduces
recognisable Dutch fragments throughout the letter with no forcing -- `reading.txt` L03-04 gives `r o s / e w
i n g e` for "Rosewinge" itself; L06 gives `u/v e r s o e [k]` for "versoeck"; L37 and L48 both give `e e n`
("een") from the identical 3-code run `51,52,10:`; L39 gives `n i e t` ("niet"); L26/L34 line up
"Coningh van Denemarcken"; L19/27/40/50/61 line up "Vereenichde Nederlanden"; L24/26/31/38 line up "Engelandt".
This cross-context consistency, not asserted anywhere in advance, is the strongest evidence the system
identification and the specific codes below are right.

### Nomenclator table (grade C; `key.tsv` rows tagged "nomenclator entry")

Occurrence counts below are `grep`-verified against `plaintext_print.txt` (my first pass hand-counted these and
got several wrong -- corrected here): Vereenichde Nederlanden 4, Haer Hoog Mog. 4, Engelandt 4, Sweden(+Sweedtsch) 6,
Coningh 3, Denemarcken/Denemarken 3. Since three of these tie at 4, the count alone cannot disambiguate 143 vs
144 vs 213 -- the assignments below rest on direct sequential context (adjacent plain words matching on both
sides), not on occurrence count; see the disagreement note beneath the table.

| code | value | evidence |
|---|---|---|
| 143: | Vereenichde Nederlanden | L27: "de [143] 't selve met [CODE6=andere][CODE13=danckbaerheyt] soud wordt erkant, maer" against print "...voor de Vereenichde Nederlanden, 't selve met andere danckbaerheyt soude werden erkent, maer..." -- "andere" (6 letters) and "danckbaerheyt" (13 letters) match the two code-run lengths exactly, either side of the nomenclator code |
| 144: | Haer Hoog Mog. | L20: "om [144] de vruntschap van dese Croon" against print "...om Haer Hoog Mog. de vruntschap van dese Croon te doen verliesen" -- vruntschap(10)/van(3)/dese(4)/Croon(5) all match their code-run lengths exactly on both sides of 144 |
| 213: | Engelandt | L24 ("van [213] tot [104=Elseneur]" ~ "van Engelandt tot Elseneur") and, in the same 4-item list as 105/225 below, the last slot before "bekendt sijn" |
| 105: | Sweden (Zweden) | L31, a sequential match with nothing else in between: "gelijck sij bij [105] [225] [CODE4=ende] [213] [CODE6] [CODE3=sijn]" against print "gelijk sy by **Sweden**, **Vranckrijk** ende **Engelandt** bekendt sijn" -- "ende" (4 letters) matches its code-run length exactly, and "sijn" (3 letters, though sijn is elsewhere usually left plain -- possibly coded here to avoid ambiguity beside "bekendt"). This is the cleanest alignment found this pass (every word in a 9-word stretch matches in order) and is why 105/213 are assigned to Sweden/Engelandt rather than the reverse |
| 225: | Vranckrijk | same L31 sequence as above |
| 104: | Elseneur (Helsingor) | L24, same context as 213 above |
| 222: | Londen | L34 and L41 (both followed immediately by "geeft geschreven"/"over de..." matching "heeft geschreven"/"over de commercie") |
| 172: | Denemarcken / Denemarken | L29 (near "in Denemarken de heren Staeten Generael") and L46 ("van de tractaten met [172] wil ..." ~ "van de tractaten met Denemarcken wil uytsluyten") |
| 173: | Coningh van Denemarcken (collocation) | matches the 2x this exact collocation recurs (S3, S4); context at L26 ("de [173] sal doen soo veel" ~ "de Coningh van Denemarcken het derde soo veel had gedaen") |

**Disagreement with the fresh-instance re-derivation subagent (see below):** working from occurrence counts
alone (before this pass's grep correction), it proposed swapping two pairs -- 143=Haer Hoog Mog./144=Vereenichde
Nederlanden, and 213=Sweden/105=Engelandt -- and said explicitly it had not checked which of 172/173/222 is
which. I kept the assignments above because they rest on direct multi-word sequential context (the L31
four-item list and the exact code-run-length chains either side of 143 and 144 in L20/L27), which the
count-only pass did not have. **Not fully resolved between two independent passes; flagged for a third check**,
ideally against the manuscript image rather than either printed alignment alone.

### Letter alphabet, partial (grade C = 2+ independent consistent word-contexts, several confirmed by an
independent fresh-instance re-derivation subagent this pass; grade M = 1 context, tentative)

| letter | code(s) | grade | contexts |
|---|---|---|---|
| e | 50, 51, 52 | C | Rosewinge (pos 4 & 9, both 51); agent (pos 3, 50); vande/met (pos 5, 51); versoeck (pos 2, 52); geobtineert (pos 8=50, pos 9=52); "een" = 51,52,10 recurring twice unambiguously (L37, L48) |
| n | 10 | C | Rosewinge (pos 7); agent (pos 4); geobtineert (pos 7); "een"/"niet" |
| t | 25, 26 | C | 25: agent (pos 5); met (pos 3); "niet" (L39). 26: geobtineert (pos 5 AND pos 11, internally self-consistent doubled 't') |
| s | 23 | C | Rosewinge (pos 3); versoeck (pos 4); ambassadeur-candidate (pos 5) |
| g | 57 | C | Rosewinge (pos 8); agent (pos 2); geobtineert (pos 1) |
| r | 22 | C | Rosewinge (pos 1); versoeck (pos 3); geobtineert (pos 10) |
| o | 12, 13 | C | 12: Rosewinge (pos 2); versoeck (pos 5). 13: geobtineert (pos 3) |
| w | 32 | C | Rosewinge (pos 5); wil (pos 1) |
| i | 61, 62 | C | 61: Rosewinge (pos 6); wil (pos 2). 62: geobtineert (pos 6) |
| u/v | 27 | C | vande (pos 1, as v); versoeck (pos 1, as v) -- treated as one letter, period orthography does not reliably distinguish u/v |
| m | 11 | C | met (pos 1); ambassadeur-candidate (pos 2) |
| b | 44 | C | geobtineert (pos 4) -- single word, but that word independently cross-checks on 5 other already-fixed letters (g,e,n,e,e,r), so treated as solid despite one context |
| d | 49 | C | isolated 2-letter word "de" (d + already-fixed e=51) directly after "bij"/"by", found independently by both this session and the re-derivation subagent |
| l | 6 | M | wil (pos 3) only |

14 letters recovered (13 at grade C across 25 distinct code-values, 1 at grade M). Roughly 15 more distinct
2-digit codes are still unkeyed and render as `[code]` in `reading.txt`. Applying the "geobtineert" letters
decodes that entire 11-letter word without a single gap (`reading.txt` L05: `g e o b t i n e e r t`) --
the strongest single confirmation of the alphabet found this pass.

### Fresh-instance re-derivation (rule 7)

A subagent that saw only `ciphertext.tsv`, `plaintext_print.txt` and a description of the system above (not
this session's key.tsv) independently rebuilt a code table. It found the identical Rosewinge alignment and the
identical three 'e' homophones (50, 51, 52) unprompted, plus the "geobtineert" alignment (g,e,o,b,t,i,n,e,e,r,t)
that supplied b=44, the t=26 homophone, and the o=13/i=62 homophones folded into the table above -- all now
merged into `key.tsv`. It also independently found the "de"=49,51 alignment. Net new letters/homophones from
the subagent, adopted here: b, d, and homophones o:13, i:62, t:26 (5 of the 14 recovered letters' code-values
came from its pass, not this session's own alignment work).

**Real conflict it caught, confirmed here:** a candidate 5-letter word right after "de" (49,51), read as
"Staet" (S-t-a-e-t against codes 25,25,40,51,25), would need code 25 to mean both 'S' (position 1) and 't'
(positions 2 and 5) -- impossible for a single code in this system, and 't' is independently pinned at 25 from
three clean contexts elsewhere (agent, met, niet). This means the "Staet" identification for this specific
5-code run is wrong (some other word, not yet identified, sits there) -- not that letter t=25 is wrong. Left
unresolved and not corrected in `key.tsv`; the position itself (`ciphertext.tsv` L04.10-14) is a candidate for
a fresh look at the image.

**Disagreement it raised, addressed above:** its nomenclator mapping swapped 143<->144 and 213<->105 from
count evidence alone; kept this session's context-anchored mapping instead (see the nomenclator table's
disagreement note) but flagged, not silently overridden.

**Still-open conflict, not caught by the subagent, not resolved:** code 40. One candidate word ("agent",
5 letters a-g-e-n-t against codes 40,57,50,10,25) would fix it as 'a'; a different candidate ("van de", read as
one 5-letter run against codes 27,39,10,40,51) would fix it as 'd'. Both otherwise check out (g,e,n,t
position-match cleanly in the first; v,n,e position-match in the second) but they cannot both be right for a
single code. 'van' is usually left plain elsewhere in this letter (6 uncoded occurrences), so encoding it here
would be inconsistent -- the "agent" reading is probably right and the "van de" segmentation probably wrong --
but not certain enough to commit to the key.

### Flagged: plain-word signs that are probably mistranscribed cipher, not real Dutch

Of the 187 distinct non-numeric signs in `ciphertext.tsv`, most are recognisable (if archaically spelled)
Dutch words and are passed through as `clear` in `key.tsv`. A visible minority do not parse as Dutch at all and
do not fit grammatically at their position against `plaintext_print.txt`; these are left as `clear` pass-through
in `key.tsv` too (rule 2: the transcription is not silently repaired here), but are flagged here as the
likeliest next win for a re-transcription/re-crop pass, since several sit immediately next to a coded run and
may really be part of it: `stiptgesantwoort` (L23.4), `couromen` (L24.13), `godag` (L26.8), `goederhijzeerd`
(L43.4), `cristien` (L65.1), `indagijt` (L66.2), `gebal` (L67.1, already flagged `agree-flagged` by the
reconciler), `hierm` (L67.6), `verwehr-` (L49.9), `aansier` (L49.1), `Willemsmaker` (L20.4), `gepersiadeeren`
(L52.2), `dubelijck` (L56.5, `agree-flagged`), `sonell` (L20.2, L28.9, L29.13, L36.6, L53.9 -- recurs 5 times,
always immediately before a verb like "soud", suspiciously regular for a genuine word), `oindsighte` (L29.2),
`versaeckeren` (L17.10), `vereenigt` (L10.11), `bedelckt` (L13.4), `datums` (L18.1, L29.1, L38.9, L52.3 --
recurs 4 times, always as if standing in for "dat" plus something else), `fredberg?,` (L50.11), `vercke`
(L43.7), `stt` (L51.5), `luv.` (L63.2). None of these were re-read from the image this pass (out of the
no-host-fetch scope of this brief); a worker with `service.archief.nl`'s full-resolution JPEG and a proper
crop tool could very plausibly turn several of them into more coded digit-runs, which would materially help
resolve the code-40 conflict and the L04 "Staet" mismatch above.

### Other letters in the same key (brief item 6)

Not chased this pass (no host fetch attempted, per brief scope). `ff.206-207` of the same bundle (a second,
same-day Van Beuningen dispatch on Brandenburg/Poland/Sweden, already imaged by OX-VB) has not been
characterised as plain or cipher -- worth a quick look before any wider sweep of the 1657 bundle.

### Grades (rule 4)

Per `tools/decode_key.py`'s own tally: cipher tokens 862, of which C 329 (nomenclator + recovered letters,
applied globally), M 26 (the tentative letter `l`=6, plus the 13 `[MARK]`/`[ILLEGIBLE]` transcription gaps),
U 162 (unresolved codes, shown as `[code]`), H 0, S 0, I 0; 345 further tokens are plain uncoded Dutch text
(grade `clear`, not part of the cipher tally). `tools/decode_key.py ciphers/vanbeuningen-dewitt-1657 --check`
exits 0. No spec exists for this target (`specs/vanbeuningen-dewitt-1657.json` not present; Dutch) --
`tools/judge_plaintext.py` was not run, per this brief's step 5.

## Key recovery round 2, 25 Sept 2026 (LANE OX solver OX-VBS2)

No host fetches this pass; worked entirely from `ciphertext.tsv` and `plaintext_print.txt` already on disk, per
`.claude/briefs/runs/2026-09-25-lane-ox-vbs2.md`. Job: key every code the known plaintext can fix -- round 1
(OX-VBS, above) had keyed 13 letters / 25 codes by hand; this pass automates the alignment and extends it.

**Status stays `partial`.** Every coded token now has *some* grade (516 of 517 coded tokens, 99.8%) but not
every one is grade C (rule 5's condition for `solved`): 446 C, 70 M, 1 U. Two codes are a genuine, unresolved
conflict between two well-supported values, kept honest (grade M, `a|b` ambiguous value) rather than guessed.

### Method: `align.py` (committed in the folder)

A global (Needleman-Wunsch) word alignment between `ciphertext.tsv`'s word sequence (clear Dutch words +
coded runs, `[MARK]`/`[ILLEGIBLE]` dropped) and `plaintext_print.txt`'s word sequence (known multi-word
nomenclator phrases pre-collapsed into single tokens so an already-recovered nomenclator code aligns 1:1
against its phrase). A clear cipher word scores high against an identical plaintext word; a coded word scores
by letter-count match against the plaintext word's length, plus a consistency bonus/penalty against codes
already keyed (bootstrapped from round 1's grade-C rows), so the DP's own scoring improves as more codes are
locked in. Insertions/deletions are allowed throughout (rule 2: the two copies are in different hands and do
not agree word for word -- this is confirmed by the diff table below, not assumed).

`python3 align.py --debug` prints the full alignment (cipher word / plaintext word, one pair per line) for
inspection. `--votes` prints one row per accepted code position. `--build` writes `key_align.tsv` (voted,
one row per code, with support count and the words behind it) and `conflicts.tsv` (every code with more than
one voted value). Two Python bugs were caught and fixed while writing it, both worth flagging for reuse
elsewhere: `str.split()` treats U+00A0 (non-breaking space) as whitespace, so joining a collapsed multi-word
phrase on a non-breaking space silently re-splits it back apart on the very next `.split()` -- and, less
obviously, it also treats the ASCII "information separator" controls U+001C-U+001F as whitespace, so that
workaround fails too; the fix used here collapses phrases on the already-split word list instead of the raw
text, sidestepping the whitespace question entirely.

**Voting rule** (job step 2): for each code, the plaintext letter most of its aligned instances agree on, if
any two or more agree (grade C); a code with only one supporting word, or where a second value also has two
or more independent supporting words (a genuine conflict, not noise), grades M. A single dissenting word
against an otherwise strong majority is treated as noise (segmentation/alignment error at that one position),
not a conflict -- e.g. code 10=n has 35 supporting words against a single stray "p" (from "prompte", almost
certainly a misalignment at that position, see the diff table below), and is graded C, not M.

### Result: 21 letters recovered (53 code-values), up from 13 letters (25 code-values)

Applying the bootstrap (round 1's 13 letters + 9 nomenclator codes) as anchors, the aligner independently
**reconstructed every one of round 1's 25 code-values with the same letter** (including upgrading `l`=6 from
round 1's single-context M to a script-verified C, 11/11 independent words), and added 7 entirely new letters
(k, p, a, c, y, h, f) plus new homophones for several already-known letters (a second `u/v`=20 alongside 27,
a second `r`=21 alongside 22, a second `s`=24 alongside 23, a second `l`=7 alongside 6, and a contested second
`m`=9). Coverage: coded tokens 862-345(clear)=517; keyed 516/517 (99.8%), of which 446 grade C (86.3% of all
coded tokens) and 70 grade M; 1 token (code 106, a single occurrence) stays fully unkeyed. 53 of 53 distinct
codes appearing in the ciphertext now have a key.tsv row (52 with a value, 1 without).

Letters recovered, C-grade code-values (M-grade in parentheses): a=39,41,42 (43); b=44; c=46,47; d=49; e=50,
51,52; f=55,56; g=57; h=59; i=61,62 (65); k=4 (5); l=6,7; n=10; o=12,13 (14); p=17; r=21,22; s=23,24; t=25,26;
u/v=20,27; w=32; y=36 (37). Not yet recovered: j and v are not distinguished from i and u/v respectively
(consistent with round 1's period-orthography note); q, x (3 occurrences in the print) and z (5 occurrences)
have no recovered code -- either genuinely rare/absent from the coded portions, or hiding among the still-
unkeyed/conflicted codes.

### Two genuine conflicts, not resolved (`conflicts.tsv`)

**Code 40 (d vs a), the same code round 1 flagged unresolved** (there: "agent" vs "van de", a single-word
disagreement). This pass's systematic vote across many more contexts confirms it is a real, unresolved
conflict rather than round 1's one-off ambiguity: 14 independent words vote `d` (dese, goede, verscheyde, de,
andere, danckbaerheyt, ende, ambassadeur, gehandelt,, sonder, dese, staende, and 2 more) against 10 words that
vote `a` (Staet, assisteren,, andere, danckbaerheyt, agent, ambassadeur, realiteyten, affectie, Staet,
staende). Note that four word-*types* (andere, danckbaerheyt, ambassadeur, staende, dese) appear on **both**
sides at different occurrences in the letter -- since a homophonic code has one fixed meaning, this means at
least one alignment instance for each of those word-types is wrong (a misaligned coded run, not a real second
meaning for code 40), and the diff table below independently confirms `a` is very often the better semantic
fit (dfcectie/affectie, redliteiten/realiteyten, stdet/Staet, stdende/staende) even though the raw vote count
narrowly favours `d`. Left as `40 = d|a`, grade M, rather than picked -- CLAUDE.md rule 10/3 both counsel
against silently choosing when the evidence itself disagrees; a future pass with the manuscript image (round
1's plain-word-that-may-be-cipher list, or a sharper crop) is the way to actually settle this, not more
alignment against the same print.

**Code 11 (m vs n), not caught by round 1** (which graded `m`=11 grade C from 2 contexts: "met", and an
uncertain "ambassadeur-candidate" reading). This pass's votes: 7 words vote `m` (om, somme, ambassadeur,
commercie, met, met, prompte) vs 5 words vote `n` (van, penningen, penningen, kennen,, sonder). The diff table
below shows two contexts where `n` is clearly the better fit (kenmen/kennen,, somder/sonder), i.e. round 1's
C grade for this code should be treated as **downgraded to M** by this pass's evidence, not confirmed. Left
as `11 = m|n`, grade M.

### Diff table (job step 3: "the words where the decoded cipher copy differs from the print, not corrections")

`python3 align.py --diff` compares every fully-keyed coded word's decoding against its aligned plaintext word
and lists the 34 (of ~140 fully-keyed multi-letter coded words) that differ:

| line | decoded | print word | likely cause |
|---|---|---|---|
| L03 | de | 't | misalignment (short function words either side of a gap) |
| L03 | heer | geen | misalignment |
| L04 | ttdet | Staet | code 40 conflict (position 3) -- round 1's own flagged "Staet" issue, unaffected by this pass |
| L07 | uerstreckinge | verstreckinghe | orthography: print's silent -gh- |
| L08 | uam | van | code 11 conflict (m/n) manifesting as an extra letter, or a length-mismatch misalignment |
| L08 | eoede | goede | misalignment (g not yet decodable at that position) |
| L09 | penmingem | penningen | code 11 conflict, both occurrences in this one word |
| L09 | dssisteren | assisteren, | code 40 conflict |
| L12 | recreutes | recrutes, | orthography (extra e) or a length-mismatch misalignment |
| L27 | dndere | andere | code 40 conflict |
| L27 | ddnckbaerheyt | danckbaerheyt | code 40 conflict |
| L29 | heeren | Staeten | misalignment (wrong word paired) |
| L30 | kenmen | kennen, | code 11 conflict -- context clearly wants `n` here |
| L31 | bekent | bekendt | orthography (silent -d-) |
| L31 | syn | sijn. | orthography (i/j not distinguished, per round 1's note) |
| L33 | dgent | agent | code 40 conflict |
| L34 | uande | van | misalignment (length mismatch) |
| L35 | ambdssadeur | ambassadeur | code 40 conflict |
| L37 | allianuie | alliantie | one position not yet resolved cleanly |
| L39 | goets | goedts | orthography (silent -d-) |
| L45 | ho / m | van / Sweden | misalignment (DP filler, low-value nomenclator-range slot) |
| L46 | uytslugten | uytsluyten, | code 57 minor homophone noise (g/y), see conflicts.tsv |
| L47 | dat | omdat | partial match (segmentation) |
| L48 | sweets | aensiet, | misalignment (wrong word paired) |
| L52 | conditiem | conditiën | code 11 conflict + diacritic normalised away |
| L53 | somder | sonder | code 11 conflict -- context clearly wants `n` here |
| L58 | promnte | prompte | misalignment at one position (code 10=n is otherwise rock solid, 35 contexts) |
| L58 | redliteiten | realiteyten | code 40 conflict |
| L59 | credyt | credijt | orthography (ij/y) |
| L60 | dfcectie | affectie | code 40 conflict + one further position not yet resolved |
| L61 | stdet | Staet | code 40 conflict |
| L62 | stdende | staende | code 40 conflict |

Reading left to right: roughly half the "differences" are the two known code conflicts showing through (not
new information), a third are ordinary period-orthography variation between two independently written copies
(rule 2 -- this was never assumed to be a byte-identical duplicate), and the rest are alignment misses at
short/ambiguous stretches (flagged, not silently corrected in `key.tsv` or `ciphertext.tsv`).

### Fresh-instance re-derivation (rule 7)

A subagent that saw only `ciphertext.tsv` and `plaintext_print.txt` (not this session's `key.tsv`,
`key_align.tsv`, `conflicts.tsv` or `align.py`) independently tokenised, anchored on identical clear words
(its own script, `difflib`-based LCS anchoring rather than this session's full DP), and proposed a letter or
nomenclator meaning per code with its own support counts, explicitly declining to guess where its evidence
was thin or contradictory.

**Full agreement, 40 of 40 codes where it found any evidence** (35 letter codes + 5 nomenclator codes),
once u/v and case are normalised (its "v" is this key's "u/v" merged letter; its "sweden"/"vranckrijk"/etc.
are this key's "Sweden"/"Vranckrijk"/etc. -- the same values, not a real difference): every letter it proposed
matches this key's value exactly, including both new-this-pass homophones it re-derived independently (20=u/v,
alongside 27; and its low-support "9=m" matching this key's second `m` homophone). No code got a *different*
letter from the two independent passes -- the rule-7 bar ("a difference larger than the M-graded codes sends
the key back") is not met, so the key stands.

**Both genuine conflicts independently reproduced, same direction:** it found the exact same 11=m/n split
("too close to call... not reporting a preferred letter" -- its words) and the exact same 40=d/a split
(majority d, "a real minority a that is not obviously noise... reported as d but flagged as contested" -- its
words), from a different anchoring method and, where the two methods' word lists overlap, mostly different
supporting contexts. Two independent methods landing on the same two live conflicts, not resolving them, is
itself evidence the conflicts are real (a genuine two-value ambiguity in the cipher's own design at those two
codes, most plausibly a second Staat-related homophone group not yet disentangled) rather than an artifact of
either alignment script.

**No evidence either way** for codes 37, 41, 43, 56, 65 -- it reports these as unreachable from its more
conservative anchor-only method, concentrated (its words) in "the middle stretch (~120-350)... where the
print copy's wording diverges too much from the cipher copy's to anchor reliably", not as containing
contradicting evidence. This session's key already grades 37, 43, 65 M (single-context, already flagged
weak). **41 (a) and 56 (f) are graded C here** (3/3 and 2/2 independent words respectively) but were not
independently confirmed -- flagged for a future pass as the two C-grade codes resting on this session's
alignment alone; nothing found by either pass contradicts them, so they are not downgraded, but a third
check (ideally against the manuscript image) would be worth doing before treating them as fully settled.
**Nomenclator 172/173** (Denemarcken/Coningh van Denemarcken): the subagent found the same phrases
contextually plausible but could not position-verify them and declined to report them resolved; this
session's C grade for both rests on round 1's direct sequential-context reading (L26/34, L29/46), not
independently reproduced this pass -- also worth a third check.

## NX-UNBLOCK (26 Sept 2026): flag, not an unblock -- NEXT-STEPS.tsv's "needs-edition" reads stale

Before trying a free route, read this row's actual current state: `key.tsv` (53 code-values, 446/517 coded
tokens grade C), `reading.txt`, and `AUDIT.md` (verifier OX-VBV, LANE OX, 25 Sept 2026, class N3 for the key/
decipherment, N1 for the plaintext) all already exist, and `status.json` already records `key: "ours"`,
`text: "known"` for this target. `NEXT-STEPS.tsv`'s extracted "next step" text ("Key recovery was not
attempted... the next step is a solver session using ciphertext.tsv, plaintext_print.txt...") is from an
*earlier* paragraph in this same NOTES.md, written before key recovery happened (OX-VB/OX-VBS/OX-VBS2), and
this file's own top status line still reads `partial` even though the verifier's own AUDIT.md table above
already shows the key at N3. `tools/next_steps.py`'s "last paragraph naming a next step" extraction picked
up that stale paragraph rather than the file's true current state (there is no later "next step" bullet after
the rule-7 re-derivation section, so it fell back to the last match by that phrase).

**Not an image/edition/person blocker at all** -- this is a `next_steps.py` extraction miss on a target whose
own status line has not been updated to match its AUDIT.md, not something a free-route pass can unblock. Per
this brief's own scope (never touch status.json or another folder's reading files), left unchanged here;
flagged in ROOM.md for whoever owns this target's status line and the NEXT-STEPS.tsv regeneration to fix
(either bump the status line/status.json's own status field to match AUDIT.md, or teach next_steps.py to
prefer a next-step paragraph that comes after the file's newest dated section).

## GAPS-vanbeuningen-dewitt-1657 (2 Oct 2026, account-4): alphabetic-order bracketing with an order-shuffle control

Written 2 Oct 2026 02:0x UTC (clock read), BEFORE the script existed or ran, as the pre-registered prediction the
Remaining-gaps Verdict line asks for. Nothing here changes key.tsv or reading.txt (rule 4: a structural prior names
what to check, it does not grade a token).

### What the C-graded letter codes already show (read from key.tsv, no computation)

35 letter codes at grade C, sorted by code number, read: 4 k, 6 l, 7 l, 9 m, 10 n, 12 o, 13 o, 17 p, 20 u/v, 21 r,
22 r, 23 s, 24 s, 25 t, 26 t, 27 u, 32 w, 36 y | 39 a, 41 a, 42 a, 44 b, 46 c, 47 c, 50-54 e, 55 f, 56 f, 57 g, 59 h,
61 i, 62 i. Up to one cyclic wrap (y at 36 -> a at 39) the letters run in alphabetical order with one exception,
code 20 (u/v; all seven contexts are v-words: van x3, verscheyde, vruntschap, verliesen, one t-outlier), which sits
between p 17 and r 21 where q would be expected. i/j and u/v are one letter each in a 17th-century alphabet.

### The two statistics, and the control

1. **Descents.** Sort the C codes by number; count the consecutive pairs whose letters go backwards in the alphabet,
   taking the best of the 26 cyclic rotations of the alphabet (so the single k..y / a..i wrap costs nothing).
   Read-off prediction: real = 1 (20 u/v -> 21 r). Control: the same count on 1,000 random re-assignments of the
   same 35 letter labels to the same 35 code numbers (the shuffle varies exactly the statistic's own axis, the
   letter-to-code order, so it can fail differently from the target -- rule 3's bCAS/AX-5799 test).
2. **Leave-one-out bracket accuracy (the known-answer control for the prediction rule itself).** For each C code,
   hide it, take the nearest C codes below and above by number, and predict the letter interval between their two
   letters (cyclic). A hit is the hidden code's own letter inside that interval. Report hits/35 and the mean interval
   width, real and under the same 1,000 shuffles. Read-off prediction: real about 34/35 (20 u/v is the predicted
   miss: bracket p..r) at a width of 1-3 letters; shuffled near chance at a wide width.

### Pre-registered predictions for the eight codes, from their C-graded brackets (cyclic)

| code | votes on file | lower C neighbour | upper C neighbour | bracket | bracket says |
|---|---|---|---|---|---|
| 40 | d 14 / a 10 (conflict) | 39 a | 41 a | {a} | **a**; d lies 8 codes away (48-49) |
| 11 | m 7 / n 5 (conflict) | 10 n | 12 o | {n, o} | **n**; m lies at 9 |
| 5 | k 1/1 | 4 k | 6 l | {k, l} | k consistent |
| 14 | o 1/1 | 13 o | 17 p | {o, p} | o consistent |
| 37 | y 1/1 | 36 y | 39 a | {y, z, a} | y consistent |
| 43 | a 1/1 | 42 a | 44 b | {a, b} | a consistent |
| 49 | d 1/1 | 47 c | 50 e | {c, d, e} | d consistent, and 49 is the only d slot on file (48 absent from the ciphertext, 40's d-votes aside) |
| 65 | i 1/1 | 62 i | 4 k (wrap) | {i, j, k} | i consistent |

### What result supports which value (written before the run)

- **Order model supported** = real descents at or below the minimum of the 1,000 shuffles (p < 0.001) AND
  leave-one-out accuracy >= 90% (>= 32/35) with the shuffled accuracy clearly lower at a wider mean bracket. Then the
  brackets are a usable prior and the registered predictions for the native-resolution crop pass are: **40 = a** and
  **11 = n** (both against the current majority vote), and the six single-context values are consistent with their
  brackets (which does not raise any of them above M, rule 4). key.tsv stays 'd|a' and 'm|n' until the crop pass.
- **Order model not supported** = accuracy under 90%, or the shuffles reaching the real descent count, or the shuffled
  accuracy within 10 points of the real one. Then the bracketing prior has no discriminating power at this K and no
  prediction for 40 or 11 is registered; the crop pass runs blind to both, and this instrument is logged
  "untested-by-this-tool" for the two conflicts (rule 3's third-attempt clause does not apply: one attempt).
- **For 40 under a supported model, two outcomes are written down for the crop pass:** (i) the 14 d-sense "40"
  positions read 48 or 49 at native resolution (0 vs 8/9 confusion; then 40 = a and the model holds everywhere), or
  (ii) they read 40 (then 40 is a genuine d|a polyphone or clerk slip, the model's prediction for 40 FAILS, and the
  d-votes stand -- the prior does not override the image). OX-VBV's three screen-crop samples (one d-sense) all read
  "40", which already leans to (ii) for that one position; the native crops decide.
- **For 11 under a supported model:** the 7 m-sense positions have no digit-confusion route to 9, so if the crops
  confirm "11" at met/om/somme, 11 is a genuine m|n polyphone (or n with alignment slips at those words) and the
  bracket prediction for 11 FAILS; it is logged as such, and m|n stays.
- Whatever the result, no code's grade changes in this step and reading.txt is not regenerated.

### Run (filled in after the script ran, 2 Oct 2026 02:0x UTC)

Script: `tools/key_order_test.py` (written for this step, shared under tools/ per Usage 8; offline test
`tools/tests/test_key_order_test.py`, 15/15 pass). Command and output, verbatim:

```
$ python3 tools/key_order_test.py ciphers/vanbeuningen-dewitt-1657/key.tsv --grades C --query 40 11 5 14 37 43 49 65 --shuffles 1000 --seed 1
key ciphers/vanbeuningen-dewitt-1657/key.tsv: 35 attested codes at grade C; alphabet read as starting at 'k' (best rotation)
descents: real 1 [20 u -> 21 r] | shuffle mean 15.868 min 10 p05 13 (N=1000) | P(shuffle <= real) = 0.0
leave-one-out bracket: real 34/35 = 0.971 at mean width 3.06 letters [misses: 20 u (bracket 17 p .. 21 r = pqr)] | shuffle hits mean 18.163 p95 25 max 29 at mean width 12.54 | P(shuffle >= real) = 0.0
bracket 40 (on file d|a, grade M): 39 a .. 41 a -> {a}
bracket 11 (on file m|n, grade M): 10 n .. 12 o -> {n,o}
bracket 5 (on file k, grade M): 4 k .. 6 l -> {k,l}
bracket 14 (on file o, grade M): 13 o .. 17 p -> {o,p}
bracket 37 (on file y, grade M): 36 y .. 39 a -> {y,z,a}
bracket 43 (on file a, grade M): 42 a .. 44 b -> {a,b}
bracket 49 (on file d, grade M): 47 c .. 50 e -> {c,d,e}
bracket 65 (on file i, grade M): 62 i .. 4 k -> {i,k}
```

Seed 2 (1,000 shuffles): descents shuffle mean 15.9, min 10; leave-one-out shuffle hits mean 17.9/35, max 30 at
mean width 12.5; the real numbers do not change. `--no-merge` (i/j and u/v kept apart, 300 shuffles): real 1
descent, 34/35, same miss; shuffle mean 16.0 descents, 17.8/35 hits. 0 network requests; 0 vision calls.

**Result against the pre-registered reading.** Every number landed where the prediction put it: real descents 1
(the one named exception, 20 u/v -> 21 r) against a shuffle minimum of 10 over 1,000 draws (P = 0.0); leave-one-out
34/35 = 97.1% at a mean bracket width of 3.06 letters, the one miss being the predicted one (20, bracket p..r),
against a shuffle mean of 18.2/35 (52%) at a mean width of 12.5 letters, shuffle maximum 29/35 (P = 0.0). This is
the "order model supported" outcome as written above, so the registered predictions for the native-resolution
crop pass stand: **40 = a** (bracket {a}, 39 a .. 41 a) and **11 = n** (bracket {n, o}, 10 n .. 12 o), both
against the current majority vote, with the two written-down ways each prediction can fail on the image (the 14
d-sense "40" positions reading 40 rather than 48/49; the 7 m-sense "11" positions confirmed as 11). The six
single-context values (5 k, 14 o, 37 y, 43 a, 49 d, 65 i) all lie inside their brackets ({k,l}, {o,p}, {y,z,a},
{a,b}, {c,d,e}, {i,k}; with i/j merged the last bracket has no j), which is consistency, not a second context:
all six stay M (rule 4). key.tsv, reading.txt and reading_tokens.tsv are unchanged by this step;
`tools/decode_key.py ciphers/vanbeuningen-dewitt-1657 --check` was not re-run because no reading input changed.

Control adequacy (rule 3): the shuffle re-assigns the 35 letter labels over the 35 code numbers, which is the
axis both statistics measure, so it could have matched the real key and did not (10-30 descents, 9-29 hits across
draws, never 1 or 34); a known-answer check is built in (leave-one-out on the C codes themselves), so the bracket
rule's own reliability is measured on this key, not assumed. What it does not test: whether the clerk kept the
order at the specific codes 40 and 11 -- that is exactly what the crop pass decides, and this prior only names
which outcome to look for first.

## Remaining gaps (finish-or-blocker pass, 2 Oct 2026)
Read so far: 491 of 517 coded tokens at grade C (95.0%), 26 M, 0 U, after the 5 Oct 2026 native re-read (A4-RFVB, section "Native-resolution re-read of codes 40 and 11" below; `tools/decode_key.py ciphers/vanbeuningen-dewitt-1657 --check`: "tokens 862: C 491, M 26, clear 345", up to date). Codes 40 and 11 are settled there and removed from this list (40 = a, 48 = d, 11 = n, 8 = m, 28 = u/v). Earlier figure, kept for the record: 446 of 517 coded tokens at grade C (86.3%); 516 of 517 carry a value (70 M, 1 U = code 106). Source: `tools/decode_key.py ciphers/vanbeuningen-dewitt-1657 --check` re-run 2 Oct 2026 01:02 UTC ("tokens 862: C 446, M 70, U 1, clear 345", reading up to date), M/U tally by sign from reading_tokens.tsv: code 40 x31, code 11 x17, [MARK] x9, [ILLEGIBLE] x2, 43 x2, 37 x2, 5/14/49/65 x1 each, transcription-M 50/20/23 x1 each, 106 x1. Below Bourdeau's 95% read bar (sources/cyphersolver/2026-10-01/writeup-SKILL.md section 0a). The plaintext is in print (AUDIT.md item 1, N1), so what remains is grading the key, not recovering unknown text.
- transcription gaps: 9 [MARK] (L05, L12, L15, L19, L23, L38, L51, L55, L66), [ILLEGIBLE] L63.4, L37 pos.10 cluster ("20"/"50"/"250"), transcription-M 50@L18, 20@L37, 23@L48 - blocker: not-attempted; OX-VB's two passes read full-leaf JPEGs with no crop tool and NOTES "Cipher transcription" says L37 pos.10 "needs a fresh look at a proper high-resolution crop"; never re-read on line crops; next: same line-crop pass as code 40, ~$1 marginal
- about 24 suspect "clear" word types inside the 345 clear tokens (sonell x5, datums x4, stiptgesantwoort, couromen, godag, goederhijzeerd, cristien, indagijt, gebal, hierm, verwehr-, aansier, Willemsmaker, gepersiadeeren, dubelijck, oindsighte, versaeckeren, vereenigt, bedelckt, fredberg?, vercke, stt, luv.) - blocker: not-attempted; NOTES "Flagged: plain-word signs that are probably mistranscribed cipher" says none were re-read from the image; if any are digit runs they change the 517 coded-token total and may add contexts for codes 40, 11 and the single-context codes; next: add their lines to the same crop list, re-tokenise any digit runs in ciphertext.tsv, re-run align.py --build and decode_key.py --check, ~$2
- code 186 (formerly read 106; 1 token, grade M 'Coningh van Sweden', L45.8) - blocker: open-codes; the 5 Oct 2026 native re-read (A4-RFVB) reads 1, open 8, 6 and the position against print L27 gives "de Coningh van Sweden" beside 185 Sweden, a single context; a second occurrence (the Amsterdam sibling or other Van Beuningen letters) is what would raise it
- single-context homophones 5 (k), 14 (o), 37 (y, x2), 43 (a, x2), 49 (d), 65 (i): 8 tokens graded M on one supporting word each - blocker: open-codes (VB-0086, 9 Oct 2026: on the 1656 letter 0086 code 58 (g) and nomenclator 186 gained a second agreeing context; code 14 stands where the print has n in "misgunnen", image reads "1(", an n-code shape, flagged, not settled; none of 5, 37, 43, 49, 65 occurs on 0086; bracketing done 2 Oct 2026, GAPS-vanbeuningen-dewitt-1657: all six inside their C-graded brackets, order model 34/35 leave-one-out vs 18/35 shuffled, section above; a second context each still needed, rule 4); was: not-attempted; reclassified from open-codes: key.tsv shows "align.py vote 1/1" for each, but two internal steps narrow them and neither has run: (i) all six values fall inside the alphabetic blocks the C-graded codes form (k 4-5, o 12-14, y 36-37, a 39-43, d 48-49, i 61-65), testable against an order-shuffle null, and (ii) re-tokenised suspect words and the Amsterdam sibling (next gap) can supply second contexts; a structural prior alone does not upgrade a grade (rule 4), it names which ones to check first; done 2 Oct 2026: `tools/key_order_test.py` (35 C-graded letter codes, 1,000 shuffles, descents 1 vs shuffle min 10, brackets printed above); next: second contexts from the re-tokenised suspect words and the Amsterdam sibling, in the crop pass, ~$1 marginal
- Van Beuningen's cipher letters to the Burgomasters of Amsterdam, Copenhagen 28 Oct 1657 (Fruin/Kernkamp, Brieven van Johan de Witt I, 1906, pp.440-441, IA werken28nethgoog) - blocker: not-attempted; missed by the classifier: AUDIT.md (second-audit list, item 2, the Fruin/Kernkamp 1906 entry) records that Kernkamp deciphered three of these letters "omdat de sleutel van het geheimschrift voor in de portefeuille ligt" and quotes the plaintext, but the key table is not printed and nobody has looked for the portfolio or its key in the Amsterdam city archive; same writer, same place, nine days later, so it may be the same key and would give period (grade H) values or second contexts for codes 40, 11 and the single-context codes; next: search the Stadsarchief Amsterdam catalogue for the burgomasters' "missiven" portfolio of 1657 and record its availability flag and shelfmark (catalogue record first, per the access playbook), ~$2
- inv.1537 cipher passages found by VB-SCREEN (9 Oct 2026): scans 0029, 0038, 0048, 0079, 0086, 0088 (about 230 groups) - blocker: not-attempted (for 0029, 0038, 0048, 0079, 0088 and the 0086 continuation leaf, scan 0087); 0086 done 9 Oct 2026 (VB-0086, section below): the 1656 letter shares the 1657 key at the scored positions (S 216/225 = 0.96 vs permutation p99 0.249, PREREG-VB0086.md, gate PASS); all six are printed in clear (VB-1537), so they add key evidence, not text; next: the same pipeline (native fetch, align_0086.py pattern, PREREG) on 0088 (~40 groups, 17 Dec 1656, pp.366-367) and 0087 (the rest of the 10 Dec letter, p.366), ~$4 each
- other Van Beuningen letters of 1656-1658 in NA 3.01.17 inv.1536-1541, including QUEUE HU7 (15 Mar 1656, Brieven aan Johan de Witt I p.328, groups 154/250/254/264 Fruin left unread with "het cyfer van de heer Nieupoort") - blocker: not-attempted; none opened (NOTES "Other letters in the same key"; HU7 never got a folder); only ff.206-211 of inv.1538's 289 images are on disk; next: full-text search the Fruin/Japikse Deel 1 OCR (Huygens retroboeken dewitt) for "cijfer"/"cyfer" footnotes on Van Beuningen letters 1656-1658 to list which are in cipher, then fetch only those leaves through the inv.1538 METS, ~$3 (VB-SCREEN2, 9 Oct 2026: inv.1541 screened in full at 400 px, 51 scans; its letters are endorsed answered 29 Mar to 2 Aug 1658 and the last two are dated 3 Aug and 13-or-7 Aug 1658, so no letter after mid-Aug 1658 is in 1541; inv.1540 sampled every 7th scan, official missives endorsed 24 Apr to 6 Aug 1658; cipher in 1541 at 0043 (3 Aug 1658, printed, glossed) and at least 0001 (400 px only); siblings_screen_1541.tsv)
- L72 signature (1 [ILLEGIBLE] token) - blocker: illegible; a flourish, not readable text (NOTES "Cipher transcription"); the plain copy f.209 gives the signer as Van Beuningen, so no information is lost

## Escalation (2 Oct 2026)
- [ ] siblings: same-day dispatch ff.206-207 (images/NL-HaNA_3.01.17_1538_0206.jpg, 0207.jpg, on disk) viewed 2 Oct 2026 at a 1500 px downscale: running plain Dutch prose on both leaves (Brandenburg/Poland/Sweden report, signed, dated Coppenhagen 19/29 September 1657), no comma-separated digit runs, so not a cipher sibling; DECODE grep for beuningen/de witt/nieuwpoort returned zero hits (check-solved, 24 Sept 2026). Not yet opened: the Amsterdam burgomasters' portfolio of 28 Oct 1657 (Kernkamp pp.440-441, deciphered, key "voor in de portefeuille"), HU7 (15 Mar 1656), the rest of inv.1538 and bundles 1536-1541; planned: Stadsarchief Amsterdam catalogue record (~$2), then the Fruin Deel 1 "cijfer" footnote search (~$3)
- [x] clear-pages: the plain copy ff.208-209, printed as Brieven aan Johan de Witt I pp.405-406 (plaintext_print.txt), is the decipherment itself; rounds 1 and 2 aligned it word for word (align.py), 446 of 517 coded tokens at C
- [ ] known-keys: done: Fruin/Kernkamp 1906 pp.71-72 prints De Witt's own February 1653 key for his letters TO Van Beuningen, compared value by value with key.tsv in AUDIT.md (AUD2): does not match (Fruin 50-51=s against our 50-52=e, 24-25=h against 25-26=t, 44-45=p against 44=b); KEY-OFFICES.tsv row 50 and KEY-DESIGN.tsv rows 171-172 hold only this target's own key; sources/decode/keys-all-2026-09-28-merged.tsv has no De Witt, Van Beuningen or Nieupoort key. Not tried: the Amsterdam portfolio key of autumn 1657 (Kernkamp p.440), Nieupoort's key named by Fruin (HU7), the NA 3.01.17 EAD grepped for cijfer/sleutel/chiffre items 1655-1660 (OX-VB grepped it only for "Beuningen"), Tomokiyo; planned: re-fetch the EAD (one request) and grep it, ~$2
- [x] print: Fruin/Japikse 1919 pp.405-406 (plaintext, footnote "onopgelost cijfer"); Fruin/Kernkamp 1906 read in full from IA OCR (pp.71-72 key, pp.440-441 footnote, no cipher note on the 19/29 Sept letter); Rowen 1978 via IA full-text search; JSTOR-QUEUE row 73 (done); OpenAlex, Semantic Scholar, CrossRef; print_check.py. No prior key or decipherment located (AUDIT.md item 2, N3); Postma 2006/2007 unread limits the novelty class, not the reading
- [ ] key-rebuild: round 1 hand alignment (13 letters / 25 codes), round 2 align.py NW voting (21 letters / 53 codes), difflib re-derivation (40 of 40 codes agree, both conflicts reproduced). Print alignment is retired for codes 40 and 11 (three passes, same split each time; no fourth). Different instrument tried 2 Oct 2026: alphabetic bracketing with an order-shuffle control (`tools/key_order_test.py`: 35 C codes, 1 descent vs shuffle min 10, leave-one-out 34/35 vs 18/35), predicting 40 = a and 11 = n, written down as the prediction before the image pass and not used to change key.tsv; what remains for this bullet is the image pass itself
- [ ] image-check: done 5 Oct 2026 (A4-RFVB): all 31 code-40 and 17 code-11 positions, the 7 code-20 and L37.10 re-read on native strips, the open-8 glyph found (C 446 -> 491 of 517); still not re-read: 9 [MARK], L63.4, L44-L46 beyond three tokens, the suspect clear words, ~$3. Earlier: done in part: OX-VB settled 7 digit-vs-digit disagreements and the closing formula on tight crops; OX-VBV sampled L03-L05 and one 0211 code-40 position on the screen-rendered cipher_crops (three code-40 readings, one d-sense and two a-sense, all "40"). Never re-read on native-resolution line crops: the 31 code-40 and 17 code-11 positions, 9 [MARK], L63, L37 pos.10, L44-L46, about 24 suspect clear words. Planned: tools/iiif_lines.py --image on the local 0210/0211 leaves, 2 blind passes per leaf plus 1 reconciliation, ~$12
- [x] retry: round 2 re-ran all 517 coded tokens with the extended key and regraded them (446 C / 70 M / 1 U); decode_key.py --check re-run 2 Oct 2026 exits 0. A further retry (align.py --build, then decode_key.py --check) follows the image pass and should include a third check on C-codes 41 (a), 56 (f) and nomenclator 172/173, which rest on one pass only (NOTES round-2 re-derivation section)
Verdict: keep going: 7 internal gaps; cheapest next (VB-0086, 9 Oct 2026): 0086 (10 Dec 1656) reads with the 1657 key (gate PASS, 216/225 vs p99 0.249), so the 1656 letters are a second witness for this key: run the same alignment on 0088 and 0087 (~$4 each) for further second contexts (codes 5, 37, 43, 49, 65 still single-context; 58 and 186 gained one on 0086; 14 conflicts, image flag) and an image re-check of the two 0086 flags (code "9" in saken, "14" in misgunnen, ~$1); the inv.1539/1541 edition check is done (edition_check_1539_1541.tsv: 72 Van Beuningen letters of 1657 to 7 Aug 1658 printed in Deel 1 pp.369-447, none after 7 Aug 1658), so a screen of those bundles looks for unprinted letters only after the per-letter dates are matched; cheapest next (VB-1537, 9 Oct 2026): the six inv.1537 cipher letters are printed in clear (Deel 1 pp.330-367), so they add key evidence, not text: align 0086 against pp.365-366 on native crops, ~$5; the edition check of inv.1539/1541 dates against Deel 1-2 (same Huygens route, ~10 requests) before any screen of those bundles; earlier (VB-SCREEN): the glossed inv.1537 passages, 0086 first, ~$6; then screen inv.1539 (102 scans) and 1541 (51 scans) the same way, ~$3 each; earlier list: 6 internal gaps (codes 40 and 11 settled 5 Oct 2026 by the native re-read, A4-RFVB: 491 of 517 coded tokens at C); cheapest next: the NA 3.01.17 EAD re-fetch (one request) grepped for cijfer/sleutel/chiffre items 1655-1660, ~$2; then the Stadsarchief Amsterdam catalogue record for the burgomasters' 1657 missiven portfolio (lead: www.amsterdam.nl/stadsarchief/stukken/macht/geheimschrift/, 403 to the fetcher on 2 Oct 2026), ~$2; then the remaining image items (9 [MARK], L63.4, L44-L46, suspect clear words) on the same strips, ~$3

## Web and blog check (GAPS-vanbeuningen-dewitt-1657, 2 Oct 2026)

Run 2 Oct 2026 02:0x UTC (clock read) by GAPS-vanbeuningen-dewitt-1657 (account-4): the ten WebSearch queries and two page opens by a Sonnet subagent, the three blogs' own search pages by the worker. Status word unchanged (a search result, not a novelty verdict, rule 10).

```
disk grep: sources/cryptiana: grep -rli "beuningen" returned no file at all (sources/cryptiana/web/dutch.htm does not contain "beuningen" either) -- 0 requests
query: "Van Beuningen" "De Witt" 1657 cipher -- WebSearch -- 10 results, 3 plausible
query: "Van Beuningen" "De Witt" 1657 cijfer geheimschrift Kopenhagen -- WebSearch -- 10 results, 2 plausible
query: "3.01.17" 1538 cijfer OR cipher -- WebSearch -- 9 results, 0 plausible
query: "onopgelost cijfer" "Van Beuningen" -- WebSearch -- 9 results, 0 plausible
query: "Rosewinge" 1657 -- WebSearch -- 9 results, 0 plausible (Thurloe State Papers snippets about Rosewinge as Danish envoy; no cipher)
query: Van Beuningen De Witt 1657 cipher copy -- WebSearch -- 10 results, 1 plausible (our own repo PR #11)
query: "Van Beuningen" cipher solves Claude OR GPT -- WebSearch -- 9 results, 0 plausible (Claude/"Cyphral Distich" 1653 stories, not this letter; read from snippets only, not opened)
query: site:scienceblogs.de/klausis-krypto-kolumne Beuningen OR "De Witt" cipher -- WebSearch -- 10 results, 0 plausible (engine did not apply site filter; no Beuningen/De Witt hit)
query: site:cryptiana.blogspot.com Beuningen OR "de Witt" -- WebSearch -- 9 results, 0 plausible (only Wikipedia; no blog hit)
query: site:ciphermysteries.com Beuningen OR "De Witt" -- WebSearch -- 9 results, 0 plausible (only Wikipedia; no blog hit)
hit: https://github.com/NoAutopilot/cipher-lab/pull/11 -- this repository's own second-opinion PR "[SO-VANBEUNINGEN-1657]" (our ChatGPT runner loop, verified by V6-SOCHK 25 Sept 2026), not an independent source; no external decipherment cited -- comment thread: read (2 comments, both repo-internal)
hit: https://www.amsterdam.nl/stadsarchief/stukken/macht/geheimschrift/ -- WebFetch 403 Forbidden, not retried; search snippet concerns a different letter (Van Beuningen to the Amsterdam burgomasters, Copenhagen 6 Sept 1656, cipher key preserved in the burgomasters' archive), not this letter -- comment thread: not reachable
hit: https://www.vriendenvandewitt.nl/assets/files/macht-en-daadkracht.pdf -- snippet only (not opened): general article on the Northern War; no mention of this cipher copy seen -- comment thread: none
hit: https://www.nationaalarchief.nl/onderzoeken/archief/3.01.17/download/pdf -- snippet only (not opened): the 3.01.17 finding aid; does not mention a decipherment in snippet -- comment thread: none
no decipherment or plaintext of this item located by these queries on 2 Oct 2026
requests: WebSearch: 10, github.com: 1, www.amsterdam.nl: 1 (403)
Direct searches on each blog's own search page by the parent worker (the engine ignored the site: filter above), 2 Oct 2026 02:0x UTC:
query: scienceblogs.de/klausis-krypto-kolumne/?s=Beuningen -- Cipherbrain's own search -- "Wir konnten leider keine Beiträge finden" (0 posts); ?s="de Witt" -- 0 posts
query: cryptiana.blogspot.com/search?q=Beuningen -- the Cryptiana blog's own search -- "No posts matching the query" (0 posts); search?q="de Witt" -- 0 posts
query: ciphermysteries.com/?s=Beuningen -- Cipher Mysteries' own search -- first request answered HTTP 406 (Mod_Security) to a browser UA; the one permitted retry with the descriptive UA answered 200: "Nothing Found" (0 posts). Not searched for "de Witt" on this host (stopped after the 406, good-citizen rule).
With 0 posts on all three blogs there is no comment thread to read; the blog step is covered by the blogs' own search, not by the engine.
Lead for the Remaining-gaps "Amsterdam portfolio" bullet, not this step: the Stadsarchief Amsterdam page www.amsterdam.nl/stadsarchief/stukken/macht/geheimschrift/ (403 to the fetcher) is about a Van Beuningen cipher letter to the burgomasters of 6 Sept 1656 with its key preserved in the burgomasters' archive -- same writer, same post, a year earlier.
requests (this worker): scienceblogs.de: 2, cryptiana.blogspot.com: 2, ciphermysteries.com: 2 (one 406, one retry 200)
Gate re-run output follows.
```

```
$ python3 tools/intake_gate_check.py vanbeuningen-dewitt-1657
vanbeuningen-dewitt-1657: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
exit=0
```

## Premise check (GF4-BATCH6, 3 Oct 2026)

Worker GF4-BATCH6 (account-4), 01:46-01:5x UTC 3 Oct 2026 by the clock. The adversarial pass of `.claude/briefs/check-solved.md`
"## Premise check". No cryptanalysis, no transcription, no vision subagent call (the worker viewed three downscaled spreads itself).

- **(a) Decipherments and plaintexts the folder already mentions -- FOUND (plaintext of this very item; no decipherment of the
  cipher copy).** Opened each: (1) the plain copy ff.208-209 = Brieven aan Johan de Witt I pp.405-406 (`plaintext_print.txt`,
  `images/dewitt_01_405.jpg`, `_406.jpg`), the same letter word for word, footnote 1 calling the cipher copy "onopgelost cijfer"
  -- the folder was built on it (known-plaintext key recovery). (2) Fruin/Kernkamp 1906, Brieven van Johan de Witt I pp.440-441:
  Kernkamp deciphered three Van Beuningen letters to the Amsterdam burgomasters of 28 Oct 1657 with the key in the portfolio --
  different items, a sibling-key lead (Remaining gaps). (3) Fruin/Kernkamp pp.71-72, De Witt's Feb 1653 key: does not match
  key.tsv (AUDIT.md AUD2). (4) The Stadsarchief Amsterdam page www.amsterdam.nl/stadsarchief/stukken/macht/geheimschrift/: curl
  with a browser UA answered 403 today (1 request, not retried); the WebSearch snippet "Van Beuningen geheimschrift 1656 sleutel
  burgemeesters Amsterdam stadsarchief" says the 6 Sept 1656 Copenhagen letter to the burgomasters carries a decipherment written
  above it and its key is kept in the burgomasters' archive -- a different letter, but same writer and post: if that key is the
  one used here it would be a period key for codes 40 and 11 (lead for the sibling step, not a decipherment of this item).
- **(b) Other solvers' working files -- not found.** Fresh shallow clones 3 Oct 2026 (dbourdeau/cyphersolver a4292cb;
  aaymeloglu/unsolved-ciphers d2800bb), `grep -ril beuningen`: only Rechteren tot Borgbeuningen 1785-86 (Bourdeau
  `targets/rechteren1785`, DECODE R1039/R2032/R2052), a different writer; nothing on Coenraad van Beuningen, De Witt 1657 or NA
  3.01.17 inv.1538.
- **(c) Physical neighbours -- not found.** NA 3.01.17 inv.1538 spreads viewed by the worker at 1400 px: 0206-0207 (the other
  same-day Brandenburg/Poland dispatch, plain), 0208-0209 (the plain copy), 0210 (left page blank but for show-through; right page
  the cipher f.210, no interlinear above the digit groups), 0211 (left page the cipher f.211 ending with the date and signature;
  right page blank, no slip, no decipherment), and 0212, fetched today from the bundle's METS (1 METS + 1 image request,
  service.archief.nl, not committed): left page blank verso with show-through, right page a new plain letter opening "Mijn Heer, De
  heer ... Ambassadeur ...", no decipherment of the cipher copy. The cipher's own spread therefore carries no gloss or laid-in
  slip at this scale; native resolution of the facing pages was not checked (the downscale is enough to see they are blank).
- **(d) Recipient's side -- found the plaintext only (= (a)(1)).** De Witt is the recipient, and Brieven aan Johan de Witt is the
  recipient-side edition: it prints the plaintext and states the cipher copy unsolved. Sender's side: Fruin/Kernkamp's Brieven van
  Johan de Witt read in full from IA OCR (AUDIT.md), no decipherment of this letter. Postma 2006 (the standard study) still unread
  (AUDIT.md gaps). Danish side not searched (no Danish edition of an intercept of this letter is known to the folder).

**Verdict:** (a)/(d) found the plaintext of this very item in print (Fruin/Japikse 1919, N1), already known since intake; no prior
decipherment or key of the cipher copy found by this pass (AUDIT.md's N3 for the key stands). Per this job's brief ("a hit carrying
a decipherment or plaintext of this very item: status word -> found-solved"), the status word is set to `found-solved` with the
source on line 2. Flagged to the account-4 parent: this folder's open work is key recovery (codes 40 and 11, the transcription
gaps), which `found-solved` does not close; "Remaining gaps" and "Escalation" above are left as the record. Rule 10 wording.

Requests this job (this target): www.amsterdam.nl 1 (403), service.archief.nl 2, WebSearch 1; github.com clones shared with the
batch. No credentials.

```
$ python3 tools/intake_gate_check.py vanbeuningen-dewitt-1657   # before: exit 1, no Premise check section
vanbeuningen-dewitt-1657: found-solved (line 1) -- edition/page or full-text-search citation found within 6 lines
exit=0
```

## Native-resolution re-read of codes 40 and 11 (A4-RFVB, 5 Oct 2026, account-4)

Worker A4-RFVB for LANE DEFAULT-account-4-20261005-2253, 23:40-00:0x UTC 5 Oct 2026 by date -u. Images: the native
crops already on disk (`images/cipher_crops/0210_right.jpg` 2540x3730, `0211_left.jpg` 2485x3720); no fetch, no
request to any host. Crop step: `tools/iiif_lines.py` could not run (numpy/Pillow not installed in this container and the
pip install did not finish), so line strips were cut with ImageMagick instead (`convert <crop> -crop 1960x430+580+Y`,
8 strips per leaf, 370 px step, about 5 lines each, under 2500 px wide); the strips and zooms were read by the worker
itself (no subagent call). One pass, as the brief asked.

**Finding.** What OX-VB's passes transcribed "0" after a digit and "11" when standing alone is, at native resolution,
one distinct glyph: the clerk's open-topped **8** (a small bowl with a rising stroke, ɑ/δ-shaped), clearly different from
his round 0 and his two-stroke 11. No token containing the digit 8 had been transcribed anywhere in the 517 coded tokens.
Pre-registration (written 23:48 UTC after viewing only L03-L07, kept in this section's numbers): "transcribed 40" is two
signs, 4+round-0 and 4+open-8; the form read from the image agrees with the print sense (a vs d); failure if Fisher
p >= 0.05 or more than 3 positions disagree. Caveat: conflicts.tsv's word/line list had been printed to the session
before the read, so the read is form-first but not strictly sense-blind. Per-position labels:
`reconciliation/rfvb_form_labels.tsv` (line, pos, transcribed, form, image reading).

| transcribed | form on the image | n | print sense after re-alignment | reading |
|---|---|---|---|---|
| 40 | round 0 | 10 | a 10/10 | **40 = a** (the bracket prediction of 2 Oct 2026, confirmed) |
| 40 | open 8 | 21 | d 14/15 (15th = the L03 't artefact) | **48 = d** |
| 11 | clean 11 | 5 | n 5/5 | **11 = n** (the bracket prediction, confirmed) |
| 11 | open 8 alone | 12 | m 7/7 | **8 = m** |
| 20 | open 8 | 6 | u/v 6/6 | **28 = u/v** |
| 20 (L37.10) | 2 + 5 written over another stroke, one cluster, not 250 | 1 | t | 25 = t, kept M (correction on the page) |
| 50 (L08.7) | open 8 | 1 | g (goede) | 58 = g, M (one context) |
| 10 (L58.7) | open 8 | 1 | p (prompte) | 18 = p, M (one context) |
| 104 / 105 / 106 | 1 + open 8 + digit | 1 / 3 / 1 | Elseneur / Sweden / position of "de Coningh van Sweden" | 184 / 185 C / **186 = Coningh van Sweden, M** (was U) |

Form vs sense, 2x2: 40 vs 48 10/0 and 0/14, one-sided Fisher p = 5.1e-7; 11 vs 8 5/0 and 0/7, p = 0.0013; 0 positions
disagree. The pre-registered failure condition is not met. Structural check: every new code lands inside its alphabetic
block (8 m between 7 l and 9 m; 18 p beside 17 p; 28 u/v between 27 u and 32 w, which removes the only descent the 2 Oct
order test found, code 20; 48 d beside 49 d; 58 g beside 57 g), and 185/186 sit beside 172/173 (Denemarcken / Coningh van
Denemarcken) the same way. Positions of 40 and 11 not read beyond those listed: none (all 31 + 17 labelled). Not
re-read: the other 50 and 10 tokens (the two found here were incidental; re-alignment shows no further outliers on 50/10,
e 34/35 and n 35/35), the 9 [MARK], L63.4 [ILLEGIBLE], L44-L46 apart from L45.8/12 and L46.4, and the suspect clear words.

Applied: 45 tokens corrected in `ciphertext.tsv` (alt column "was <old>", why "A4-RFVB native re-read"); `align.py`
NOMENCLATOR Sweden 185, Elseneur 184; `key.tsv` rows 40 a C, 48 d C, 11 n C, 8 m C, 28 u C, 58 g M, 18 p M, 184 C,
185 C, 186 M (old 20, 104, 105 rows removed). `python3 align.py --build`: 9 conflicting codes, all `genuine False`
(single stray votes); codes 40 and 11 no longer conflict. `tools/decode_key.py ciphers/vanbeuningen-dewitt-1657 --check`:
"ciphertext.tsv: tokens 862: C 491, M 26, clear 345 / reading up to date", exit 0. Coded tokens at C: 491 of 517 (95.0%;
was 446, 86.3%); U 0 (was 1). Grades per rule 4: C 491, M 26, H 0, S 0, I 0 -- a known-plaintext result. Side
observation, not applied: L47.3 transcribed 57 looks like 37 on the strip; L45.13 "B" likely 13 (o, "Haer ho: mo:").

## VB-EAD (9 Oct 2026, LANE FAMILY-A2g, account 2): sibling cipher letters from the 3.01.17 EAD
Prior work: `prior_work.py --step-type lookup --fetch` exit 0 (plaintext KNOWN for the 19/29 Sept 1657 letter, AUDIT.md; residue = the whole sibling question; 3-tomokiyo/3-solver/4-editions UNCHECKED, folio-less unit). Check 1 (own work): NOTES "Remaining gaps" bullet and Verdict name this EAD re-fetch as cheapest next; no earlier grep of the EAD for cipher terms beyond AUDIT (c) (done 2 Oct, same terms, whole-archive, no key item).
Route: 1 request, www.nationaalarchief.nl/onderzoeken/archief/3.01.17/download/xml, HTTP 200, 3,099,376 bytes, saved unmodified to sources/na-3.01.17/2026-10-09/ (README, sha256 55288e16...). Script `siblings_ead.py` (--check) writes `siblings_ead.tsv` (24 rows).
Found: the EAD contains zero occurrences of cijfer, cyfer, cypher, cipher, gecijferd, sleutel, chiffre, geheimschrift, ontcijfer anywhere in the archive (grep counts all 0); the inventory does not flag cipher letters at item level, so sibling cipher letters cannot be found from the finding aid. Van Beuningen items 1655-1660 (yearly bundles, all digitised `<dao>` METS except the series headings): inv.1535 (1656), 1536 (1656), 1537 (1656, "Eigenhandig"), 1538 (1657; ff.206-211 read, of 289 images), 1539 (1657, Eigenhandig), 1540 (1658), 1541 (1658, Eigenhandig); a second numbered run 1532-1534 (1656, 1657, 1658; "extraordinaris ambassadeur naar Denemarken") and the France 1660-62 bundles 1868, 1870, 1872, 1875 (Boreel/Van Gent co-ambassadors; other cipher family, not this key). No printed-edition pointer is given by the EAD for any bundle.
Ranked (unread + digitised + Van Beuningen as sender; none opened this job): 1. inv.1537 and 1539 and 1541 ("Eigenhandig", autograph; likeliest private-key letters to De Witt) 2. inv.1536, 1540 3. inv.1535, 1532-1534 (joint missives with Reede/Vierssen, other hands) 4. rest of inv.1538 (ff.1-205, 212-289). Known/printed: the 28 Oct 1657 letters to the Amsterdam burgomasters (Kernkamp 1906) are in the Amsterdam city archive, not this series.
Next step per row (all: ~$2 each at one METS request on service.archief.nl + a numeral-density page screen of the leaf list, no model read until a page shows digit runs; then the matched-control/crop rules): 1537/1539/1541 first; QUEUE HU7 (15 Mar 1656, Fruin p.328) falls in 1536 or 1537 by date, check both.
Not found: any cipher marker in the finding aid (all terms, whole file). Not checked: images, METS, printed editions. Requests: www.nationaalarchief.nl 1 (200). No credentials.

## VB-SCREEN (9 Oct 2026, LANE FAMILY-A2g, account 2): inv.1537 screened for cipher passages
Prior work: `prior_work.py --item-spec 'shelfmark=NA 3.01.17 inv.<n>;sender=Van Beuningen;recipient=De Witt' --step-type lookup --fetch` for 1537, 1539, 1541: exit 4 each, the only owed LEAD was this job's own claim (recorded CLEAR in prior-work.tsv); KNOWN row = the 19/29 Sept 1657 letter in inv.1538, not these bundles. Check 1 (own work): grep of the repository for inv.1537/1539/1541 finds only VB-EAD (no images ever opened). Check 2 (neighbours): n/a, bundle-level screen. Check 3 (holder): EAD carries no cipher flag (VB-EAD). Check 4 (editions): sources/huygens/cipher-letters-2026-09-24.tsv (Fruin/Japikse Deel 1 footnote sweep, 24 Sept) lists only HU7 (15 Mar 1656) and HU8 (19/29 Sept 1657) as Van Beuningen cipher letters; whether the 1656 letters below are printed (deciphered) in Deel 1 was not checked -- unchecked.
Route: METS service.archief.nl/gaf/api/mets/v1/aeb68de6-b638-42c9-bceb-0fb8aca6464c (93 scans); IIIF path = the METS uuid split into 2-character directories + scan id (`service.archief.nl/iip/iipsrv?IIIF=<path>/<id>.jp2/full/400,/0/default.jpg`), confirmed against the item page's drupal-settings-json; every scan at 400 px, 1.6 s apart (`screen_vb/fetch_small.py`).
Screen: 12 contact sheets (`screen_vb/sheets.py`), 8 targets + 4 planted controls per sheet in shuffled positions (cipher 1538_0210, 0211; clear 1538_0206, 0207 -- the brief named 0208/0209 as cipher, but those are the plain copy, NOTES above), tile key kept in a file read only after all calls were written (`screen_vb/calls_1537_blind.tsv`, `sheetkey_1537.json`). Controls: cipher 24/24 flagged, clear 24/24 called clear. Caveat: the controls are whole-cipher pages, so they show recall only for full cipher pages, not for a few groups inside prose (HU7's shape); the same control repeating on every sheet is recognisable, so they are not blind after sheet 1.
Result (`siblings_screen.tsv`, 93 rows): no all-cipher page in inv.1537. Blind calls: 75 clear, 12 blank/cover, 1 partial (0086), 5 maybe. All 6 eye-checked at 1500 px (`images/screen_1537/`): every one carries comma-separated number groups closed by colons, the layout of this key: 0029 (Coppenhagen 5 April 1656, ~20 groups, interlinear gloss), 0038 (4 July 1656, ~10, gloss), 0048 (August 1656, name codes 192/193, gloss), 0079 (1656, Coppenhagen, ~30 words and name codes 172, 185, 193, 149, 173, 225, 213, no interlinear gloss seen), 0086 (29 December 1656, ~15 lines mostly cipher, ~120 groups, interlinear gloss over most groups; address leaf "Mijn Heer Johan de Witt, Raetpensionaris van Hollandt ende Westvrieslandt, inden Hage"), 0088 (December 1656, ~40 groups, gloss, e.g. 114 = Keur-Brandenb., 257 = Amb.). Glossed group values seen in passing (50, 51, 23, 48, 25, 39, 10) are in the range of this folder's key; no decode, no comparison run.
Not found: HU7 (15 Mar 1656, four groups) was not identified at 400 px -- four groups inside prose are below what this screen can show; not checked: inv.1539 (102 scans) and 1541 (51 scans), METS fetched only (scratchpad), the 120-request budget of this job did not reach them; no transcription.
Requests: service.archief.nl 102 (2 METS beyond 1537 included: 1 METS 1537, 1 thumbnail, 93 + 6 scans, 2 METS 1539/1541), www.nationaalarchief.nl 1 (item page 1537); all 200. No credentials.


## VB-1537 (9 Oct 2026, LANE FAMILY-A2g, account 2): edition check of the six inv.1537 cipher scans
Prior work: `prior_work.py vanbeuningen-dewitt-1657 --item-spec 'shelfmark=NA 3.01.17 inv.1537;sender=Van Beuningen;recipient=De Witt' --step-type transcribe --fetch` exit 2 (KNOWN = the 19/29 Sept 1657 letter in inv.1538, recorded CLEAR as not this bundle; LEAD = this job's own claim, recorded CLEAR; 3-tomokiyo/3-solver/4-editions UNCHECKED, folio-less unit -- check 4 below is this job). Check 1 (own work): VB-SCREEN and VB-EAD only; no earlier edition check of these dates.
Check 4 (edition by date, run before any transcription per the Wave 4 lesson). Route: Huygens retroboeken `dewitt`, "Brievenlijst" accessor `toc/index_html` (the `toc1` path used for willemiii 404s here) with `correspondent=Beuningen`, `van_aan=van`, date ranges 1656-1657 (the list shows 20 rows per call and ignores `batch_start`, so it was queried by date windows); `pages.json?source=1` for the OCR page URLs; pages 330-332, 337-345, 363-368 and the control p.405 read as OCR text. Positive control: the 19/29 Sept 1657 letter is found on p.405 with its footnote "Dezelfde brief ook in onopgelost cijfer, van een andere hand" -- PASS.
Result: every Van Beuningen letter to De Witt of 1656 appears in the list (Brieven aan Johan de Witt I, 1919, pp.320-368; 8 Jan to 20 Dec 1656 plus undated ones), and all six scans are printed: 0029 = 5 Apr 1656 pp.330-332; 0038 = 25 Jun 1656 pp.337-338 (the "4 July" VB-SCREEN read is De Witt's endorsement "beantw. 4 July"); 0048 (left page) = 6 Aug 1656 pp.340-342; 0079 = 22 Nov 1656 pp.363-364 (date line "Desen 22 November 1656 in Coppenhagen"); 0086 = 10 Dec 1656 pp.365-366 (the "29 December" is the endorsement, print fn. p.365); 0088 = 17 Dec 1656 pp.366-367. Per scan: `edition_check_1537.tsv` (date, pages, how the cipher passage is printed, the match evidence).
How the print gives the cipher: in clear, letter-spaced. The editor's note on p.104 (N. v. d. U.) says names in cipher in these letters are printed spaced ("gespatieerd gedrukt"), and the spaced stretches on pp.332, 338, 341-342, 363-364, 365-367 sit where the leaves carry number groups (0086's opening "'t is seer te geloven dat Ambr van Churf: Brandenb hier meer is om de saken van sijn meester te doen..." is p.365 word for word). For 0079, which has no interlinear gloss, the print still gives the passage in clear ("tusschen Denemarcken ende Sweden een alliantie"); p.344 fn.1 (23 Aug 1656) says "Deze woorden in cijferschrift waren in den brief onopgelost gelaten", so the editor deciphered unglossed groups himself in at least two 1656 letters. None of the six is printed as "onopgelost cijfer". The letters are partly summarised in modern Dutch with quoted extracts; whether every cipher group falls inside a quoted extract was not checked group by group.
Fruin/Kernkamp 1906 (IA werken28nethgoog `_djvu.txt`, 1 request): its "cijfer" hits concern the 1653 key (pp.71-72, already in AUDIT.md), Van Beverningh 1653-54, and later years; nothing on Van Beuningen's 1656 letters. The toc list shows that volume (source 3) carries De Witt's replies to Van Beuningen of 1656, not these letters.
Ungated observation (a lookup, not the step-2 test, which did not run): on 0079 the groups 172, 185, 225, 213 stand where p.363 prints Denemarcken, Sweden, Francrijck, Engelant, the same values key.tsv holds from the 1657 letter (172 Denemarcken, 185 Sweden, 225 Vranckrijk, 213 Engelandt); 186 stands at "Sweden" in the "Francrijck, Engelant ende Sweden" list where key.tsv has 186 = Coningh van Sweden (M, single context). Read at 1500 px, positions not verified on crops.
Stop: the brief's step 2 needs "the smallest glossed leaf not in print"; all six are in print, so steps 2 and 3 did not run. No crops, no vision subagent, no PREREG, no decode.
Next step (for the lane): the 1656 letters are known plaintext for this key family, with a third witness (the period gloss) beside the print. A print alignment of 0086 (10 Dec 1656, ~120 groups) against pp.365-366 with tools/interlinear_align.py on native line crops would test whether the 1656 letters share the 1657 key and give second contexts for the single-context codes (5, 14, 37, 43, 49, 65, 186); the text is known (N0-N1 territory for any reading of these leaves), so the value is the key, not the content. ~$5 (crops + two blind code passes + alignment).
Not found: any 1656 Van Beuningen letter marked "onopgelost" in Deel 1. Not checked: inv.1539/1541 letters of 1657-1658 against Deel 1-2 (same route, ~10 requests); the group-by-group coverage of the print.
Requests: resources.huygens.knaw.nl 32 (31 x 200, 1 x 404 on the toc1 path; the ROOM release line's "24" undercounted), archive.org 1 (200). No credentials.

## VB-0086 (9 Oct 2026, LANE FAMILY-A2h, account 2): does the 1656 letter 0086 share the 1657 key?
Known-text work: inv.1537 scan 0086 (Van Beuningen to De Witt, Coppenhagen 10 Dec 1656) is printed in clear in Brieven aan Johan de Witt I (1919) pp.365-366; the print was used only as a key source, not read as new text.
Prior work: `prior_work.py vanbeuningen-dewitt-1657 --item-spec 'shelfmark=NA 3.01.17 inv.1537 scan 0086;sender=Van Beuningen;recipient=De Witt;date=1656-12-10' --step-type align --fetch` exit 4 (plaintext KNOWN; four LEAD rows = VB-SCREEN, VB-1537 and this job's own claim, all recorded CLEAR in prior-work.tsv: VB-1537 ran an edition check only, no alignment). Check 1 (own work): VB-1537's ungated 0079 observation only, no alignment of 0086 before. Check 2 (neighbours): 0079 (ungated lookup, 172/185/225/213), 0088 not read. Check 3 (holder): the EAD has no cipher flag (VB-EAD). Check 4 (editions): pp.365-366, read this job. Check 5 (after the score): the code values used are this folder's own key.tsv; no published key for this family is on file (AUDIT.md AUD2).
Step 0 (edition check, huygens): Brievenlijst `toc/index_html?correspondent=Beuningen&van_aan=van` by four-month windows: 45 Van Beuningen letters to De Witt of 1657 (7 Jan-18 Dec, pp.369-418) and 27 of 1658 (6 Jan-7 Aug, pp.419-447), all in Deel 1; none from 1 Sep to 31 Dec 1658. `edition_check_1539_1541.tsv` lists them; which bundle (1538/1539, 1540/1541) holds each letter was not resolved (no per-scan dates on disk, no screen, no NA request spent on it).
Step 1 (transcription): pp.365-366 page images and OCR html (images/dewitt_01_365.jpg, _366.jpg; print_0086/), print text from the opening to "Ende hebbe ik niettemin" in `print_0086.txt` (OCR corrected against the page images). One native fetch of 0086's right page (images/native_0086/, IIIF pct region, 2570x3729). Crop command, pasted:
`python3 ../../tools/iiif_lines.py --image images/native_0086/NL-HaNA_3.01.17_1537_0086_right.jpg --out images/crops_0086 --region 330,850,2240,2500 --prefix c0086 --centres 115,206,296,384,477,570,663,762,855,948,1037,1125,1217,1314,1410,1502,1596,1690,1785,2225,2362 --top-margin 30 --lines-per-crop 1 --debug`
(21 cipher-bearing lines, centres set by eye from the debug overlay because the detector split gloss and main lines). Two blind Sonnet passes per half page (L01-L10, L11-L21; pass B read in reverse order), digits and the interlinear gloss in separate columns, key and print not shown (reconciliation/0086/). Pass A's line labels match the page; pass B's bands caught neighbouring lines, but its digit sequences agree with A's. 70 C items: 64 identical in both passes; 6 settled from the crop image (L03 48,12,51,10 and 27,40,10; L06 46; L11 "4:" not "41>"; L16 10; L07 61,10,48,50 a word end at the margin, gloss "inde"); 1 left M (L08 nakomen, 4th code 10 or 40), excluded from the statistic. `ciphertext_0086.tsv`.
Step 2 (PREREG-VB0086.md pushed first, e27f1be17 10:31 UTC; inputs and key-free pairs pushed 66c54d1fe before the score). `align_0086.py --pairs` (DP, key.tsv not read) then `--score` (`--check`: up to date).
Result: S = 216/225 = 0.960 (letter class 212/220, name class 4/5); null (1,000 permutations of key.tsv's values among its codes, seed 0) mean 0.048, p99 0.249, max 0.369. **Gate PASS**: the 1656 letter reads with the 1657 key at the scored positions. 2 C items unscored (code count different from the paired word).
The 9 disagreeing tokens, read after the score (not changing it): 5 come from one pairing artefact (L20 32,50,36,8,39 paired with "ons te" instead of Weyman, its gloss "Wetijnse"); code 23 at "zijn" (print spelling z, the cipher s); 144 (key "Haer Hoog Mog.") at "Staten-Generael", glossed "de Staet gent" by pass B -- the same body under another style, a mismatch under the registered similarity rule; code 9 (key m) at the k of "saken" -- in this hand 4 and 9 are close and 4 = k, image flag; code 14 (key o, M) at the n of "misgunnen" -- the image shows "1(", an n-code shape (10/11), image flag. Neither flag was used to change a reading.
Single-context (M) codes of key.tsv gaining a second agreeing context on 0086: 58 (g), 186 (Coningh van Sweden: print "den Coning van Sweden"). 5, 37, 43, 49, 65 do not occur on 0086. `codes_0086.tsv` has the per-code table.
Codes absent from key.tsv, with their print pairing (grade C from print; `key_1656_candidates.tsv`, never written into key.tsv): 29 = u/v (souverainiteit); 114 = Churvorst (van) Brandenburgh (3 contexts, gloss "Churf. Brandenb."); 119 = den Churvorst Brandenburgh (1; a second name code for the Elector, or a variant: unsettled); 192 = Pruyssen (DP run took two extra words); 198 = Polen (run "met Polen"); 257 = ambassadeur (3 contexts, gloss "Ambr"). The name runs are DP runs; the head words are named here by eye.
Gloss: read blind in both passes, not used in S; where legible it matches the print (Ambr, Churf. Brandenb., Denemarcks, de Con: van Sweden, souverainiteit, Weyman), so the 1656 decipherer used the same values.
Not done: 0087 (the rest of the 10 Dec letter, p.366 "Denemarcken ... Coning van Denemarcken"), 0088, 0029, 0038, 0048, 0079; the two image flags; per-letter inv. for 1539/1541.
Requests: resources.huygens.knaw.nl 12 (all 200), service.archief.nl 1 (200). Vision calls: 4 Sonnet passes + image checks in this session. No credentials.

## VB-SCREEN2 (9 Oct 2026, LANE FAMILY-A2h, account 2): inv.1541 (and an inv.1540 sample) for letters after 7 Aug 1658
Question: the edition (Brieven aan Johan de Witt I) prints no Van Beuningen letter to De Witt after 7 Aug 1658 (edition_check_1539_1541.tsv); do inv.1540/1541 hold letters from that window, and do they carry cipher?
Prior work: `prior_work.py vanbeuningen-dewitt-1657 --item-spec 'shelfmark=NA 3.01.17 inv.1541;sender=Van Beuningen;recipient=De Witt' --step-type lookup --fetch` exit 4 (plaintext KNOWN = the 1657 letter's audit, not this bundle; two owed LEADs = VB-1537's and this job's own claims, recorded CLEAR in prior-work.tsv; 3-tomokiyo/3-solver/4-editions UNCHECKED, folio-less unit). Check 1 (own work): VB-SCREEN fetched the 1539/1541 METS only (scratch), no 1540/1541 image opened before. Check 2 (neighbours): n/a, bundle screen. Check 3 (holder): EAD (sources/na-3.01.17/2026-10-09/3.01.17.xml) gives 1540 "1658" and 1541 "1658, Eigenhandig", no cipher flag. Check 4 (editions): edition_check_1539_1541.tsv (VB-0086's Brievenlijst windows), not re-queried.
Route: METS from the EAD's dao hrefs (1541 df3198b2-978f-47d6-9675-4ef62501bdcf, 51 scans; 1540 442ce4c5-2316-4890-aed8-3759c5e3bae6, 141 scans); IIIF via screen_vb/fetch_small.py at 400 px.
Step 1+2 (one pass, cheaper than two): 5 contact sheets of 10-11 inv.1541 scans plus planted controls (cipher 1538_0210, clear 1538_0206, shuffled; tile key `screen_vb/1541/sheetkey_1541.json` read only after all five calls were saved, `calls_1541_blind.tsv`), one Sonnet call per sheet asking page type, legible date, cipher y/partial/n, groups, gloss. Controls: cipher 5/5 called y; clear 3/4 called n, 1 called partial (a false positive, so a "partial" call on a target is weak). No date was legible at 400 px (all 51 "-"), so dates came from a second route: the top 17% strip of each of the 23 letter-start/cover scans at 1400 px (23 requests; `endorsements_1541_a.jpg`, `_b.jpg`), read by eye.
Dates (inv.1541, De Witt's endorsements "Beantw. den ..."): 0003 29 Mar, 0007 19 Apr, 0011 10 May, 0013 17 May, 0016 24 May, 0020 7 Jun, 0022-0032 12 Jul (six letters), 0034/0036 10 or 19 Jul, 0041 2 Aug 1658. The bundle is in date order. The three letters after 0041 carry no endorsement; eye checks at 1500 px: 0043 dateline "Desen 3 Augustij 1658 in Coppenhagen", signed Van Beuningen, cipher in the lower half, comma groups closed by colons with an interlinear gloss (Engelandt, Sweden, Denemarcken, augusto legible; the 400 px call missed the gloss), printed (3 Aug 1658, p.445 or p.446); 0047 (last letter, prose, no number groups seen) dateline "Dese 13. Augustij 1658 in Coppenhagen" with a "7" written above the day (`eye_1541_0047_dateline.jpg`, native crop): either 13 Aug (outside the printed list) or a correction to 7 Aug (= the p.447 letter) -- M, unsettled; a comparison with p.447's text would decide it (huygens, not run). 0001 (the first letter, undated at this size) shows comma-separated number groups in its lower third at 400 px, not eye-checked.
Cipher calls on inv.1541 targets: 0 y, 9 partial (0001, 0010, 0020, 0022, 0032, 0034, 0038, 0043, 0044), 42 n/blank/cover; of the partials only 0043 (eye) and 0001 (visible at 400 px) are confirmed; the other seven are unconfirmed (one in four clear controls drew the same call). All dated cipher-bearing letters fall inside the printed range (Jan-7 Aug 1658).
inv.1540 sample (every 7th scan + the last, top 20% strip at 1000 px, 21 requests, `endorsements_1540_sample.jpg`): cover "Denemarken"; endorsements "Missive ... van Beuningen ... Coppenhage 24 April 1658" (0064), "19 July 1658" (0120), "6 Aug 1658" (0134 of 141); one French piece (0043, copy/enclosure); number groups visible at the top of 0036's right page. These read as missives in the official series (addressee not read), spanning to 6 Aug 1658 -- no later date seen in the sample.
Result: neither bundle shows a Van Beuningen letter dated after mid-August 1658 in what was read (1541 in full by endorsement/dateline; 1540 by a 1-in-7 sample). The edition's silence after 7 Aug 1658 matches the bundles ending there, not an unprinted run; the one open case is 0047's day (13 or 7 Aug). No 1657-58 letter absent from the edition list was identified (per-letter matching of the twelve 1541 reply dates to the list's letter dates not done: a reply date is not the letter's date).
Not done: 1540 scans between the sample points; eye checks of 0001 and the seven unconfirmed partials; per-letter matching to the edition list; no transcription, no decode.
Requests: service.archief.nl 99 (METS 2, 1541 scans at 400 px 51, 1541 top strips 23, 1500 px eye fetches 2, native dateline crop 1, 1540 top strips 21 (incl. one repeat of 0141)), all 200. Vision: 5 Sonnet sheet calls + own reads of 4 composites and 3 eye crops. No credentials.

## VB-1540 (9 Oct 2026, LANE FAMILY-A2l, account 2): inv.1540 per-letter edition match, partial (26 of 141 scans looked at)
Prior work: check 1 = VB-SCREEN2 section above (1-in-7 sample; no per-letter match), edition_check_1539_1541.tsv (Brievenlijst, 27 letters 6 Jan-7 Aug 1658). Check 2-4 not re-run (bundle job).
Route: NA METS for inv.1540 (1 request) + 7 scans at 700-1400 px (0035 0036 0037 0085 0092 0099 0113; 0035/0037 fetched, not read); huygens edition page images pp.423, 430, 439 (3 requests, only 423 read). Totals: NA 8 requests, huygens 3, all 200. The brief's <= 30 NA requests cannot cover 141 scans; the sweep needs about 115 further 400-px requests (a second job, ~$2).
Found: inv.1540 holds Van Beuningen letters from Copenhagen 1658 whose datelines match printed letters (0036 13 Mar = p.423; 0085 12 May = p.430; 0113 2 Jul = p.439). Of the five letters read, only 0036 carries cipher (interlinear gloss on the right page). The edition's p.423 prints the same-date letter and its footnote 2 gives the gist of the cipher letter in clear (cited as R.A. S.G. 7270, "to the griffier"): so 0036's cipher is covered by the edition in paraphrase (M; no gloss-vs-print comparison made) and is a key test at most, not unread material.
Not found: any unprinted cipher-bearing letter. Two sample endorsements (0120 19 Jul, 0134 6 Aug) have no edition list entry of that date (list 10, 20, 24 Jul; 3, 7 Aug), so those two letters, or the edition's dates, are an open per-letter question; cipher on them not looked at. Other 100+ scans unread. No transcription, no decode.
Next: sweep 1540 scans at 400 px with the sheet method (VB-SCREEN2) in two sessions, then match; eye check 0120 and 0134 first (~$0.5).

## VB-EYE (9 Oct 2026, LANE FAMILY-A2m, account 2): eye check of inv.1540 scans 0120 and 0134
Prior work: `tools/prior_work.py vanbeuningen-dewitt-1657 --item-spec ... --step-type read --fetch` exit 2 (plaintext KNOWN, own audit; LOOK 2-leaf and UNCHECKED rows are generic, the leaf checked by eye here); check 1 = VB-1540 and VB-SCREEN2 above (these two scans were "cipher not seen, strip only"); checks 2-4 not re-run (single-leaf eye job).
Route: huygens retroboeken OCR pages of Brieven aan Johan de Witt I (aandewitt_01 html pp.439, 440, 441, 442-447; 10 requests incl. pages.json, all 200); NA 3.01.17 inv.1540 scans 0120 and 0134 at 1500 px (2) plus three native region crops (3), 5 NA requests, all 200 (mets.xml read from disk). Crops committed in screen_vb/1540/ (w1500_*, dl_*, en_*). Positive control: 0036 (13 Mar 1658) already matched to p.423 by dateline in VB-1540; the same dateline-to-printed-date method is used here.
Found: both scans are single-sheet Van Beuningen letters in clear prose, no cipher groups, no interlinear gloss, no continuation on the facing page (0120 left page = blank cover with the endorsement; 0134 likewise). 0120: dateline "6/16 Julij 1658 in Coppenhagen", endorsed "Missive ... van Beuningen van Coppenhage 13 July 1658": the printed edition has "(6 Juli 1658)" on p.440 (date match; its summary and quoted text concern the Swedish ambassadors, as does the letter; wording not compared). The VB-SCREEN2 and VB-1540 reading of this endorsement as "19 July" was wrong; so the "no printed entry for 19 Jul" question is closed: 19 Jul was never the letter date. 0134: endorsement "6 aug 1658" is the receipt date; dateline "Coppenhagen 10/20 ... 1658 n.st." with the month hard to read (M); the letter opens "my letter of the 6th of this month", so it follows 0120's letter, which fits printed 10/20 Juli (p.442-444) better than any August entry. Neither letter carries cipher, so neither is a key test or an unread candidate.
Not found: any cipher passage on either scan; a content-level match (neither letter transcribed, per the brief); the dateline month of 0134 settled.
Next (not run): a native-res crop of the 0134 dateline month, then read the 0134 body against pp.442-444 if the edition match matters (~$0.5).
Counts: NA 5, huygens 10, no other host. Rule 10: search results only, no class assigned.
