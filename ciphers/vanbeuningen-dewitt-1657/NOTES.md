partial

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

[to be filled in: subagent running, sees only `ciphertext.tsv`, `plaintext_print.txt` and the system
description in its brief, not this session's `key.tsv`/`key_align.tsv`/`conflicts.tsv`/`align.py`]
