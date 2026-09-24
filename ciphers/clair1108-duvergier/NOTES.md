open

# "Du Vergier", several original ciphered letters, BnF Clairambault 1108

QUEUE row: M19 (sources/solver-diffs — "Third pass, 24 September 2026 (M17-M21)" section of QUEUE.md).

## Source

BnF, Departement des Manuscrits, **Clairambault 1108**, part of the same composite "Clairambault 1058-1110,
Mélanges généalogiques et historiques" series as M18 (finding aid `archivesetmanuscrits.bnf.fr/ark:/12148/
cc137820/FRBNFEAD000013782_info`, same fetch reused for both targets, no extra request). This individual
volume is catalogued "L UZES-VENDOME". Gallica digitisation: `ark:/12148/btv1b90009665` (537 canvases).

**Precise catalogue entry, from the finding aid's own item list:** "**Fol. 245** • Du Vergier (Lettres orig.,
dont plusieurs avec chiffres)." The next item starts at **Fol. 265** ("Vendôme..."), so the Du Vergier item runs
roughly 20 folios -- a genuinely multi-letter item, matching the QUEUE row's "plural ciphered originals in one
place" framing. No first name or further identification given in the finding aid text itself.

## Check-solved sweep (24 September 2026)

1. **Web search.** "'Du Vergier' lettres originales chiffre BnF Clairambault XVIe XVIIe siècle" surfaced only
   the general Clairambault collection guides and the correct series page (`archivesetmanuscrits.bnf.fr/ark:/
   12148/cc137820`, used above), plus, as an unconfirmed identity hypothesis worth flagging and nothing more:
   Jean du Vergier de Hauranne, abbé de Saint-Cyran (1581-1643), the Jansenist theologian -- his dates (d. 1643)
   would fit an undated item filed in a volume otherwise ranging across the 16th-17th c., but nothing in the
   catalogue snippet or the leaf itself (below) supports or rules this out; **do not repeat as an identification
   without checking his own printed correspondence** (Lancelot's or Barbier's editions of Saint-Cyran's letters)
   first.

2. **Print/scholarship.** No Tomokiyo Cryptiana page mentions "Vergier" in any form (`sources/cryptiana/`
   grepped in full, 0 hits, both the web/ mirror and blog/). No dedicated search of a Du Vergier printed
   correspondence was completed this pass (budget) -- flagged as the concrete next edition-check step once a
   sender identity is confirmed from the leaf.

3. **Community lists.** Covered by the Cryptiana grep above (0 hits).

4. **DECODE.** `unsolved-ciphers/catalogue/decode-catalog.csv` grepped for "Clairambault 1108", "clair1108",
   "vergier": no row.

5. **Bourdeau.** Fresh shallow clone grepped for the ark (`btv1b90009665`, 0 hits) and "vergier" (0 hits
   anywhere in the repository, including its large `gallica_siblings/` HTML mirror).

6. **Aymeloglu.** Fresh shallow clone; catalogue and target folders grepped for "1108", "vergier": no hit.

Requests: gallica.bnf.fr 8 (1 IIIF manifest, recovered on the 4th attempt after three tunnel-side
`ws_closed_mid_exchange` resets -- confirmed via `/root/.ccr/README.md`'s documented pattern, not a Gallica
block, checked in `/__agentproxy/status`'s `recentRelayFailures`; 1 successful thumbnail probe at canvas f251;
3 failed attempts at canvas f248, all the same tunnel reset, not retried further this pass; 2 failed attempts
at a high-resolution crop of f251, same cause, abandoned), archivesetmanuscrits.bnf.fr 0 for this target (the
M18 fetch already covered this composite finding aid), WebSearch 1.

## What the leaf shows

**Located and confirmed this sweep, at canvas f251** (`images/probe_f251.jpg`), reached by the same +6
manuscript-folio-to-canvas offset that worked for M17 (folio 245 + 6 ≈ canvas 251; the leaf's own printed folio
stamp, visible top-right in the image, reads **"248"** -- three folios into the ~20-folio item, consistent).
This is a genuine, on-target hit, not a repeat of M18's miscalibration:

- **Left page**: numeral-group ciphertext (groups like "10 34", "587", "33 131", "708 285", "24 39 26" --
  a figure/nomenclator-style cipher, not an arbitrary-symbol one like M17's), written in lines with what
  appears to be a **partial interlinear gloss in a second, lighter hand** between several of the cipher lines --
  worth a close look by whoever transcribes this, since it may be a contemporary or later part-decipherment
  attempt rather than a clean ciphertext-only leaf. Not confirmed as a reading (too small at thumbnail
  resolution; the two follow-up crop fetches to check this closely both failed on tunnel resets, see above,
  and were not retried further this pass to stay within budget).
- **Right page**: continuous clear French, ending "...Votre très humble et très obéissant serviteur" and
  signed, legibly, **"Vergier"** -- confirms the finding aid's sender attribution directly from the leaf itself,
  independent of the catalogue.

This is a real, substantial, multi-letter ciphered item with the sender's own signature confirmed on the very
first probed leaf, and a possible existing partial gloss worth checking before any cryptanalysis is attempted
from scratch.

## Verdict

**Open.** No published plaintext, decipherment, or key found in six sources for "Du Vergier"/Clairambault 1108.
Unlike M17, no external published key was located either -- this is a genuine, unaddressed cryptanalysis (or,
if the apparent interlinear marks on f251 turn out to be a real gloss, partial-recovery) candidate. Concrete
next steps for a follow-on worker, not attempted here: (1) fetch a clean high-resolution crop of f251's left
page and determine whether the faint interlinear marks are a real gloss or a scanning/bleed-through artefact;
(2) fetch canvas f248 (folio 245, the item's actual start) and the following few canvases to establish the
letter count and total cipher extent across the ~20-folio item; (3) confirm "Vergier"'s identity (Saint-Cyran
is an unconfirmed hypothesis only) before any edition search of his printed correspondence.

Not touched: no key work, no decoding, no novelty wording.

## Du Vergier leaves, extent and gloss check (24 Sept 2026)

**Offset correction.** The prior sweep's "+6" canvas offset was a lucky near-miss. Fetching native images at
canvas252, canvas253 and canvas265 and reading the manuscript's own printed folio stamps top-right gives
**canvas = folio + 3**, exactly (252→"249", 253→"250" (faint, "2[5]0"), 265→"262"), consistent with canvas251's
already-known stamp "248". One canvas is one opening (verso of folio N on the left page, recto of folio N+1 on
the right), not one canvas per leaf. Folio245 (the finding aid's item start) is therefore **canvas248**, and
folio264 (last folio before the next catalogued item, "Vendôme..." at folio265) is **canvas267**.

**Method.** Surveyed canvas248 through canvas268 (folio245-265ish) with the IIIF `.thumbnail` endpoint (low-res,
cheap) to spot cipher by its distinctive dense numeral-group texture, then fetched full native resolution
(`/full/full/0/native.jpg`) for f251 (already on disk from the prior sweep) plus three more: f252, f253, f265 —
the "up to 3 other cipher leaves" this brief allowed. No leaf between canvas254 and canvas264 (folio251-261) or
at canvas266-267 (folio263-264) showed the numeral-group texture at thumbnail scale; ordinary flowing cursive
French throughout. A faint or short cipher passage on one of these cannot be fully excluded at thumbnail
resolution, but nothing was missed for the leaves actually fetched natively.

| Canvas | Folio (stamped) | Content | Cipher? | Rough extent | Symbol type |
|---|---|---|---|---|---|
| f251 (prior sweep) | 247v (left) / 248r (right) | Tail of a letter: cipher body on 247v, closing + signature "Vergier" on 248r | Yes, 247v | ~9 lines mixed clear/cipher, ~60-70 numeral groups, plus a short clear paragraph (Dunkerque troop-ship news) at the foot | Numeral groups, 1-3 digits, values seen from 2 to ~730 |
| f252 (native, this session) | 248v (left, docket/address only) / 249r (right) | New letter opens "Monseigneur", dated by docket "26e mars 1696"; dense cipher | Yes, 249r | ~15+ lines, dense mixed clear/cipher | Same numeral scheme |
| f253 (native, this session) | 249v (left) / 250r (right) | Continues the 26 March 1696 letter; names "Milord Myddleton" in clear; closes "Vergier" at foot of 250r | Yes, both pages | ~30+ lines across the two pages, roughly 150-250 numeral groups (rough count, not a transcription) | Same numeral scheme |
| f265 (native, this session) | 262 (stamped; both pages read as one opening) | A separate letter, not a continuation of the 26 March one; opens naming "Mde Pontchartrain" in clear, discusses Dunkerque armament, "M. de Chasteaurenault", "Milord Myddleton"; closes "Vergier" | Yes, both pages | ~20 lines, roughly 60-90 numeral groups | Same numeral scheme |

No date is legible on f251 or f265 beyond the one docket on f252 ("26e mars 1696"); the f252/253 letter is dated,
the f251 and f265 letters are not (their own datelines, if any, are on canvases not fetched this pass).

**Gloss verdict: this is not an interlinear decipherment, a later note, or bleed-through.** It is the letters'
own original composition: a **mixed clear/cipher (nomenclator) format**, where ordinary connective French words
and some proper nouns are written in clear and only sensitive nouns/names/facts are replaced by 2-3 digit
numeral codes, all in the same ink, same hand, same continuous line of writing as the surrounding clear text —
not a second, lighter hand added between the lines. At thumbnail resolution the alternating rhythm of a short
clear phrase followed by a run of numerals reads as if it were two layers; at native resolution it is plainly
one layer, one scribe, one sitting. This corrects the prior sweep's "partial interlinear gloss in a second,
lighter hand" wording, which was a thumbnail-resolution misreading, not a survives-at-full-res finding.

**Who "Du Vergier" is, from the clear text plus a web search (not from any printed edition of his own
correspondence, which was not checked this pass; grade: cryptanalytic identification, not H).** The clear
portions plus dockets give: sender signs "**Vergier**" (no "Du"), writing from **Boulogne** and **Calais**,
dated **26 March 1696** on one letter; content across all three fetched leaves concerns Dunkerque's naval
armament, troop embarkations "for the West"/"for York", Milord Middleton, the Prince of Orange, the King of
England, M. de Chasteaurenault, M. de Louvigny, and (on f265) explicitly names "M. de Pontchartrain". A web
search (WebSearch, 3 queries, 24 Sept 2026) turns up **Jacques Vergier (1657-1720)**, poet and *commissaire
ordonnateur de la marine*, posted to Dunkerque from 11 April 1695 and president of its *conseil de commerce*,
who is recorded as having addressed at least six epistles to **Jérôme Phélypeaux, comte de Pontchartrain**
(1674-1747, secretary of state for the navy) from that post, including a piece dated 1696 referencing a
campaign with Jean Bart. Place (Dunkerque/Boulogne/Calais), date (1696), correspondent's surname, and subject
matter (Dunkerque armament, addressed "Monseigneur", Pontchartrain named in the body) all line up. This
supersedes the prior sweep's Saint-Cyran hypothesis, which has nothing in the leaves to support it and is now
considered ruled out by content, not just unconfirmed. Confidence: strong circumstantial match from a general
web search, not yet cross-checked against an archival or scholarly source naming this specific ciphered
correspondence — **do not repeat as a settled identification** without that check.

**Recipient's printed material, not yet checked (next step):** "Œuvres diverses de Mr Vergier, commissaire de
la marine" (an 18th-c. printed edition of his poetic works, surfaced via web search, seen listed on a rare-book
dealer page — not yet located on Gallica/Google Books/HathiTrust) may contain some of his verse epistles to
Pontchartrain but is a different genre from these administrative cipher dispatches and is not expected to
contain them. The concrete edition-check lead is the **Pontchartrain naval correspondence** (Archives
Nationales, Marine B/2 and B/7 series per the finding aid PDFs surfaced by the same searches; a published
calendar/edition was not located this pass) and any Dunkerque-focused local history of the 1695-97 war period
(the FranceArchives finding aid "1695-1697" surfaced by the same search may be relevant and was not opened).

Requests this session: gallica.bnf.fr 26 (1 manifest reachability check, 1 manifest fetch via `gallica_folio.py`
[0 folio labels — this manifest gives every canvas label "NP", so the folio map above comes from the leaves'
own printed stamps at native resolution, not the manifest], 21 `.thumbnail` fetches canvas f248-f268 [1 failure
at f263, recovered on the single allowed retry after a pause], 3 native `/full/full/0/native.jpg` fetches
f252/f253/f265), all ≥1.5s apart, single fetcher, UA `cipher-lab research script (contact via repository)`,
`--max-time 30`. WebSearch 3. No other host, no logins, no subagents.

Not touched: no key work, no decoding beyond reading the clear-French portions directly off the images, no
novelty wording, no attempt to pin the exact folio where the Du Vergier item ends and the next item begins
(somewhere canvas265-268; canvas268 is a printed "FACTUM" title leaf, an odd insertion worth a follow-on look).
