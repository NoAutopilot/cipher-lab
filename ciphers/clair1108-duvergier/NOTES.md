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

## Key leads and print check (24 Sept 2026)

**Verdict: open, no key lead.** No published key, decipherment, or printed edition found anywhere for the
Marine/Pontchartrain/Dunkerque nomenclator correspondence of the 1690s, and specifically none for Vergier's
letters. This is a cryptanalytic-only target for now: no external key to warm-start against.

**(a) Key/decipherment leads.**

- *Cryptiana* (`sources/cryptiana/`, grepped in full for "vergier", "pontchartrain", "phelypeaux", "dunkerque",
  "clairambault 1108"/"clair1108", "marine"): no page addresses this item or this correspondence. One
  near-miss, not a match: `web/louisxiii.htm` ("Council of Béarn — Hesperien's Cipher") covers BnF Clair 373,
  two 1612 cipher letters of Théophile Hesperien to **Paul Phélypeaux, seigneur de Pontchartrain**, secretary
  of state for Protestant affairs — the addressee's great-grandfather, 84 years earlier, a different office
  (Protestant affairs, not the Navy) and a different cipher (3-digit nomenclature reconstructed by Tomokiyo).
  Worth noting as a methodological precedent (Tomokiyo has worked Phélypeaux-addressed nomenclator ciphers
  before) but not a key or lead for this item.
- **Both solver repositories**, fresh shallow clones, grepped for "vergier", the ark (`btv1b90009665`),
  "clair1108"/"clairambault 1108", "pontchartrain", "dunkerque"/"dunkirk": no hit on this target. Two
  unrelated homonyms surfaced and are ruled out: (1) `cyphersolver/gallica_sweep/sru_chiffre_desc.json`, a
  generic Gallica SRU catalogue-search dump, has one snippet naming a 1574 municipal letter from "Seveste" and
  "**Du Vergier**" (Bordeaux jurats) to Matignon — wrong century, wrong place, wrong genre; (2)
  `cyphersolver/yard1699/` is an unrelated English diplomatic nomenclator (1699) whose key has an entry
  `2280: *Pontchartrain` alongside `*Pomponne`/`*Privy Seal` — Pontchartrain there is a subject name to be
  encoded in an English key, not a decipherment of any French correspondence, let alone this one.
- **DECODE catalogue.** No cached DECODE catalogue CSV exists yet in this repo (`sources/decode/` holds only
  an unrelated login-form capture from another lane, dated today); the aaymeloglu mirror's
  `catalogue/decode-catalog.csv` was grepped instead for "pontchartrain", "dunkerque"/"dunkirk", "vergier",
  "clairambault 110": no row.
- **Lasry/Tomokiyo papers.** Web search for their joint and individual work turned up the Mary Stuart
  1578-1584 decipherment (Cryptologia, with Tomokiyo and John Chris Miller) and a separate credit to Lasry for
  a 1684 letter to Louis XIV from his ambassador to the United Provinces — no paper by either author on a
  Marine/Pontchartrain/Dunkerque nomenclator of the 1690s, and no mention of Vergier or Clairambault 1108
  anywhere in the search results.

**(b) Printed edition of Vergier's administrative letters.** Not found. Two named editions checked by web
search, both organized by a different axis than the Marine department's own internal correspondence:
- **Depping, *Correspondance administrative sous le règne de Louis XIV*** (4 vols, 1850-55): organized by
  topic — provincial/municipal affairs (t.1), justice/police/galleys (t.2), religious affairs/Protestants/
  sciences (t.4) — and by intendants and provincial governors' correspondence with the king's cabinet and
  secretaries of state. Dunkerque appears only via its admiralty lieutenant-general (Nacquart) and the
  intendant of maritime Flanders (Robert) writing to Colbert in the 1660s-70s, a generation before Vergier;
  no volume covers Marine-department internal correspondence of the 1690s.
- **Boislisle, *Correspondance des contrôleurs généraux des finances avec les intendants des provinces*** (3
  vols, 1874-97): scoped to the Contrôle général/intendants of finance, not the Marine secretariat; one
  incidental 1715 Dunkerque reference (Chamillart) turned up, two decades after and unrelated to Vergier.
  Neither edition is the right series for a Marine commissioner's dispatches to the secretary of state for
  the Navy.
- Vergier's only located printed correspondence is his own literary *Œuvres diverses* (poetic epistles,
  including pieces addressed to Pontchartrain such as "La Couche," 1696) — already flagged in the prior sweep
  as a different genre from these administrative cipher dispatches, and confirmed again here: nothing in the
  search results ties that volume to the ciphered administrative letters in Clairambault 1108.
- Google Books (key + country=US, 7 calls, ≥2s apart): `"du Vergier" Dunkerque marine chiffre` (2 hits, both
  irrelevant: *Carnet de la sabretache* 1895, and Darsel & Le Bouëdec's *L'Amirauté en Bretagne* 2012 — Brittany,
  not Dunkerque); `"clef du chiffre" marine Pontchartrain` (5 hits, all Michaud's *Biographie universelle*
  editions — the three query terms matching as unrelated words in a huge biographical dictionary, not a real
  edition); `Vergier "commissaire" Dunkerque Pontchartrain déchiffrement` (0 hits); `"correspondance chiffrée"
  marine Louis XIV Pontchartrain` (4 hits, all unrelated — a Saintonge/Aunis historical bulletin and a Mazarin-
  Nevers biography). No genuine hit for a printed key or decipherment in any query.

**(c) Archive series holding the Pontchartrain side, and whether a cipher key sits there.** AN (Archives
nationales) **Marine B2** is *correspondance générale* — orders and dispatches sent out by the secretariat
(the Pontchartrain side going out); **Marine B3** is *lettres reçues* — incoming letters, where Vergier's own
originals or ministry copies would be filed if the department kept them (our BnF Clairambault 1108 leaves may
be a private/genealogical-collection copy rather than the ministry's own filed copy — not established either
way this pass). FranceArchives finding-aid snippets surfaced dispatches specifically dated 1695-1697 and 1699
under Pontchartrain, consistent with the window of these letters, but nothing describing a cipher key held
in either sub-series. One specific and load-bearing fact: the Marine's own **central archive service was
established by Pontchartrain only in 1699** (a pavilion by the Discalced Augustinians' convent, place des
Victoires, Paris) — three years *after* the 26 March 1696 letter — so if a cipher key for this correspondence
was ever formally filed as an artifact of the ministry's own record-keeping, it would postdate the letters
themselves; nothing in the finding-aid text located this pass says such a key exists in B2/B3 at all. Not
checked this pass: the Marine B2/B3 series' own detailed inventory beyond finding-aid abstracts (would need a
Gallica/SIV fetch, out of scope — other lanes own those hosts) and the Service historique de la Défense
(Vincennes) manuscript catalogue (one PDF fetched turned out to be an unrelated 1733-35 ship's log, not a
chiffre/key inventory; not retried).

Requests this session: WebSearch 7, googleapis.com (Google Books) 7 (all ≥2s apart, `country=US` +
`key=$GOOGLE_BOOKS_KEY`, neither printed), 2 shallow git clones (github.com, dbourdeau/cyphersolver and
aaymeloglu/unsolved-ciphers, grepped and discarded), 1 servicehistorique.sga.defense.gouv.fr PDF fetch (dead
end, wrong manuscript). No gallica.bnf.fr, no archive.org. Cost well under the $5 cap.

Not touched: no decoding, no novelty wording, no fetch of BnF Marine B2/B3 finding aids or Gallica/SIV records
(other lanes' hosts).

## Passes (24 Sept 2026)

Two transcription passes over all 61 cropped cipher lines (f253L L01-L12, f253R L01-L14, f265L L01-L16, f265R
L01-L19; 2 crops each, s1/s2 overlapping horizontal halves), both disk-only, both continuing/repeating the
prior sweep's crop set (see "Du Vergier leaves, extent and gloss check" above) with no new fetches.

**passA.tsv** (1210 token rows + header). A prior worker (interrupted by the rate limit at 05:40) had
transcribed f253L L02-L08 before this session; a Sonnet subagent completed the remainder this session
(f253L L01/L09-L12, all of f253R, f265L, f265R), continuing the same schema and note vocabulary
(`leaf\tline\tpos\ttoken\tconf\tnote`; conf H/M/L; note values like "cipher", "clear, main row", "clear,
caption above row", "cipher, digit ambiguous X/Y"). All 61 leaf/line pairs present, 6 fields per row (checked
with awk). Notable additions to the convention, flagged by the completing agent: (1) several rows tagged
"bottom/top edge cut, reconstructed via L0X bleed" where the automatic line-splitting crop cut a row's text at
a boundary and content from the neighbouring line's own crop was used to complete it — not covered by the
original s1/s2 (horizontal-overlap) merge instructions, worth documenting in the crop-cutting tool's own notes
for the next target; (2) five genuinely blank margin crops (f253L L01, f253R L01, f265L L01/L16, f265R L01) got
a single `[no legible text]` placeholder row at conf L rather than a forced reading; (3) a handful of
illegible/cancelled fragments got single low-confidence placeholder rows (`[illegible fragment]`, `[cancelled
word/phrase]`, `[bleed fragment, unresolved]`); (4) f253R L08's top bleed did not clearly reconcile with f253R
L07's own bottom row and was left unmerged, flagged for review; (5) a few unusually large cipher values (601,
700, 1917, 722) outside the ~1-310 range seen elsewhere are flagged as likely misreadings rather than trusted.

**passB.tsv** (794 token rows + header), a fresh Sonnet subagent, genuinely blind: it did not read passA.tsv,
this NOTES.md, or anything but the crop images themselves, and built its own note/confidence vocabulary
independently (converging on similar terms — "clear, main row", "clear, caption above/below row", "cipher,
digit ambiguous X/Y" — without having seen passA's). All 61 leaf/line pairs present. Observations from that
agent, useful for a future reconciler: adjacent line IDs on a leaf are not always physically adjacent
manuscript lines (a curated subset, not every consecutive row), so it transcribed each line from its own
crop pair rather than assuming continuity except where a cross-line sentence join was directly legible (e.g.
f265L L04->L05->L06). On f265L/f265R specifically it reports two overlapping layers — a bold main-hand
cipher letter and a fainter second (pencil?) layer, possibly a later paraphrase or archivist gloss — and
transcribed the bold main-hand text as primary, substituting the faint layer only where it was the sole
content present (f265R L07/L08/L10/L11). This second-layer observation was not mentioned by passA's completing
agent and is a candidate for a dedicated look at those specific crops before any reconciliation.

**Token counts and agreement.** passA: 1210 tokens. passB: 794 tokens (passA has roughly 50% more tokens
overall). Per-line token counts differ substantially in many places (e.g. f253L L02: 36 vs 11; f265L L14: 46
vs 10), which is a segmentation difference, not necessarily a reading disagreement: passA's completing agent
read every caption/gloss tier as its own token stream per line (stacking multiple caption rows plus the main
row into one flat per-position list), while passB's agent more often collapsed a line to its single dominant
text layer. A same-position, shorter-list-basis comparison (`compare_passes.py`, committed alongside; not a
reconciler — no merged output is produced) gives **462/788 = 58.6% overall token agreement**, with wide
per-line spread: several lines at or near 90-100% (f253L L11 92%, f253R L07 96%, f265L L10 100%, f253R L14
100%) where segmentation happened to line up, and several at or near 0% (f253L L02/L03/L05/L06/L08/L09, f253R
L04/L11, f265L L01/L13/L14/L16, f265R L01/L04/L11) where it did not — the low-agreement lines are dominated by
the segmentation mismatch described above rather than by the two passes disagreeing digit-for-digit. Full
per-line table is `compare_passes.py`'s stdout (rerun to regenerate; not committed as a separate report file).

No reconciliation was attempted (out of scope for this pass): before any reconciliation pass, the aligner
should expect to normalize segmentation (decide whether caption/gloss tiers count as separate tokens) rather
than diff the two files positionally as-is. No key work, no decoding, no novelty wording. Disk only, no
network requests by either subagent.
