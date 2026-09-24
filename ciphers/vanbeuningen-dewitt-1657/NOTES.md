open

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

**Copy status: not resolved this pass.** Japikse's edition uses no H.A.-style archive number for this letter
(unlike the Heinsius edition); its manuscript home -- most likely Johan de Witt's own archive, Nationaal
Archief **3.01.17** (per this worker's brief, which names 3.01.17 for De Witt), but not confirmed -- was not
looked up this pass (budget). No REQUEST.md written; this is a gap for the next worker to close with one more
page fetch (Japikse's own list of abbreviations/sources) or an NA 3.01.17 inventory search, not a copy-order
determination yet.

**Kind: recovery.** A plain copy and a separately-surviving unsolved cipher copy of the identical letter is
exactly the known-plaintext pairing pattern LESSONS.md ranks as the strongest lead class -- stronger than a
mere sibling, since the plaintext itself (not just a related letter) is already in hand via this edition's own
print.

Search log (rule 10): reported above, per source. Not classified for novelty. Requests this pass:
`resources.huygens.knaw.nl` ~3 (book_data.js, 1 pages.json, 1 html_url OCR fetch, 1 image fetch), WebFetch 2
(Academia.edu, blocked 403; vriendenvandewitt.nl PDF, fetched and locally OCR'd with `pdftotext`, not a network
re-fetch), WebSearch 2, `github.com` 0 (reused clones already on disk this session). No subagents.
