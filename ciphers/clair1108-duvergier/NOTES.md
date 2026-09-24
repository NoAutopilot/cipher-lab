solved

Status set to solved by LANE G2, 24 Sept 2026 09:42 UTC (N0, decipherment on the leaf; clair1067 precedent). Nine groups of letter B and fol.247v are still unread; see the follow-ups.

Novelty: **N0** for letters A (26 Mar 1696) and B (fol.261v-262r), decipherment on the leaf; nine groups of B unread. See AUDIT.md (Verifier V1, 24 Sept 2026).

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
[**Verifier V1, 24 Sept 2026:** the item is cited by folio in print: Boislisle, Saint-Simon III (1879) p.57 n.1; Mancel 1903 p.130 n.3;
La Roncière VI (1909) p.216. Its deciphered text was not found in print. See AUDIT.md.]
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
| f252 (native, this session) | 248v (left, docket/address only) / 249r (right) | New letter opens "Monseigneur", dated "a Boulogne ce 26e mars 1696" in the heading on 249r; ~~dense cipher~~ **corrected 24 Sept 2026 (see "fol.249r"): 249r is all clear French; the pale numerals on it are mirrored show-through of 249v** | No | 12 clear lines | none on 249r |
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

[**Verifier V1, 24 Sept 2026:** this paragraph is about the sender's own printed works, not the recipient's. Identification now rests on
print: Depping IV p.772 n. and Mancel 1903 pp.130-134 name Vergier as Pontchartrain's observer at Calais in 1696, and
the recipient is Jérôme de Pontchartrain, the son (letter B's gloss "M vostre Pere"; Depping IV p.773 n. "mon père et moy").]
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

[**Verifier V1, 24 Sept 2026:** "no printed edition found anywhere" below is too strong: Pontchartrain's side is printed (Depping IV
pp.772-773 n., 12 Mar 1696; Mancel 1903 pp.131-134, 25 Feb-28 Mar 1696) and the item itself is cited by folio. See AUDIT.md.]
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
  no volume covers Marine-department internal correspondence of the 1690s. [**Verifier V1, 24 Sept 2026:** wrong for this exchange: t.4
  pp.772-773 prints in a footnote Pontchartrain (the son) to Vergier, 12 Mar 1696, from the Marine dispatch register,
  found by grepping the IA full text for "Vergier".]
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

## Marine key search (24 Sept 2026)

**Verdict: open, no key found for Vergier's own correspondence specifically, but two genuine surviving
Marine-secretariat cipher artefacts of the right period were located** (neither yet confirmed as *the* key to
these leaves). Question asked (LANE G2 worker D brief): does a cipher key for the Marine secretariat's
correspondence with Dunkerque/Vergier/the commissaires of the 1690s survive or appear in print? Does not
repeat the prior "Key leads and print check" section's Cryptiana/solver-repo/DECODE/Depping/Boislisle/Google
Books-phrase-query ground.

| # | Source | Query | Result |
|---|---|---|---|
| 1a | archive.org advancedsearch | `title:(inventaire archives marine) creator:(Neuville)` | 1 volume: `inventairedesar00fragoog`, "Inventaire des Archives de la marine. Série B. Service général" (1885) |
| 1b | archive.org be-api full-text search, on that volume | "chiffre", "chiffres", "cypher", "clef du chiffre" | 0 hits, all four terms |
| 1c | HathiTrust bibliographic API, record 001596202 (same Neuville title) | brief/recordnumber | 8 NYPL/UVA/Michigan items: v.1, v.3-v.6, v.8 (x2 scans), Index (1885); v.1/v.3-v.6 full view (pdus) |
| 1d | HTRC Extracted Features API (`data.htrc.illinois.edu/ef-api/volumes/HTID/pages`), token counts, all 8 items above | "chiffre"/"chiffres"/"chiffré(e)(s)"/"cypher(s)" as a token | **v.3, seq 00000318: "chiffre" x1. Index vol, seq 00000011: "chiffres" x2; seq 00000309: "chiffres" x2; seq 00000328: "Chiffre" x1.** Text itself not retrieved -- babel.hathitrust.org is Cloudflare-challenged here (confirmed again this pass, `catalog.hathitrust.org/Search/Home` 403 `cf-mitigated: challenge`) and neither volume is on archive.org. **Not pursued further this pass** (would need a browser session with a Cloudflare-clearing route, or a HathiTrust full-view page fetched some other way); flagged for a follow-on worker, not a confirmed cipher-key sighting, only a token match in an index/inventory volume of the right title. |
| 1e | Google Books full-text ("SearchWithinVolume" JSON endpoint, `books.google.com/books?id=ID&q=TERM&jscmd=SearchWithinVolume`), on the Neuville/Buche B2 volumes found by `intitle:"Inventaire des archives de la marine"` (300 results total; ids checked: `f1oEAAAAIAAJ` B2 76-243, `m0UEAAAAIAAJ` 1885 v.1, `Br5CAAAAYAAJ` **B2 244-435**, `ki8XAQAAMAAJ` B3 561-803, `DOkIAQAAIAAJ`/`ROkIAQAAIAAJ` articles 48-75, `9BwOAQAAIAAJ`) | "chiffre", "chiffres", "chiffrée(s)", "en chiffres", "clef du chiffre", "clef", "déchiffr-", "cypher" | 0 in every volume **except `Br5CAAAAYAAJ` (B2 244-435, 1902, viewability ALL_PAGES)**: 1 hit for "chiffre" at printed p.304 -- an alphabetical index line reading **"chiffre, chiffrant et déchiffrant ... 113, 118, 120, 128, 131"** (index entry pointing to five item-description pages earlier in the same volume). A direct page fetch (`pg=PA113&output=text`) was blocked by Google's own bot check ("Sorry... automated queries") on the one attempt made; not retried (single-attempt rule). **Page numbers 113/118/120/128/131 of this specific volume, not yet read.** |
| 1f | Same volume (`Br5CAAAAYAAJ`), same endpoint | "Dunkerque", "Vergier", "Pontchartrain" | "Vergier" and "Pontchartrain": 0. "Dunkerque": 3 index hits (pp.164, 177, 212) but all in unrelated index runs (fishing/anchor disputes, defence measures, arms shipments to Scotland) with no adjacency to the "chiffre" line on p.304 -- **the chiffre index entry does not itself co-occur with Dunkerque or a named person in the retrieved snippet**, so this cannot yet be tied to Vergier's correspondence specifically; it is a Marine-B2 (outgoing correspondence) cipher item of unconfirmed date within the 244-435 article range (which per web search follows on from the 76-243 volume covering *ordres et dépêches* 1663-1790; 244-435 likely runs from shortly before or after 1700, not confirmed). |
| 2a | SHD Vincennes library, printed manuscript catalogues (PDFs, `servicehistorique.sga.defense.gouv.fr`) | fetched `.../201601_NP_DBIB_Manuscrits-MS.pdf` (MS series, 266pp) and `.../201601_NP_DBIB_Manuscrits-SH.pdf` (SH series, Dépôt des cartes et plans/Service hydrographique, 156pp), text extracted with `pypdf`, grepped for "chiffr\|déchiffr" and "vergier\|pontchartrain\|dunkerque" | MS series: 1 irrelevant hit (a 16th-c. mine-survey decipherment, unrelated). **SH series: a genuine hit.** |
| 2b | SH series catalogue, same extraction | -- | **SH 49**, "Recueil de pièces originales, ordres de Louis XIV, mémoires, etc. relatifs principalement aux galères et aux campagnes dans la Méditerranée (1680-1710)": item **35 in that recueil is "Chiffre pour la correspondance des galères"** (a cipher for the galleys' correspondence). Item 25 of the same recueil is "Mémoire du comte Brémond au ministre de Pontchartrain sur l'entretien des chiourmes", dating the recueil's Pontchartrain-era items to the 1690s window; item 36 is dated 1700, item 29 dated 1700, items 19-24 concern the 1699 Sicily campaign. **This is a genuine surviving Marine-secretariat cipher artefact from the Pontchartrain era, held at SHD Vincennes, but for the Mediterranean galley fleet (Marseille/Toulon), not the Dunkerque/Channel correspondence Vergier's letters belong to** -- a different theatre and, almost certainly, a different key, not evidence for Vergier's own cipher. Also separately: **SH 10-14** and **MS 19** are two library copies of the same digest, "Principes sur la marine, tirés des dépêches et des ordres du roi... sous les ministères de Colbert, de Seignelay, de Pontchartrain père et fils..." (Pidansat de Mairobert, 1755-57), organised by ministry then alphabetically by subject; the Pontchartrain-père chapter (1690-1700) runs MS19 fol.85-140. Whether "Chiffre" is one of its alphabetical subject headings is not established -- the catalogue description does not itemise subject headings the way SH49's recueil description does. |
| 3a | Tomokiyo Cryptiana (`sources/cryptiana/web/louisxiv.htm`, `louisxiv0.htm`, `louisxiv2.htm`), read in full (not just grepped) for 1680-1710 French ciphers and what each gives | -- | 20-odd numbered ciphers/codes catalogued for Louis XIV's reign, none captioned Marine/Pontchartrain/Dunkerque/Jean Bart/corsairs except one: **(5B) "Seignelay-Lauzun Code (1690)", broken by John Wallis** -- a code used by Jean-Baptiste Colbert, marquis de Seignelay (Secretary of State for the Navy 1683-1690, Pontchartrain's immediate predecessor) in a letter to the comte de Lauzun; alphabetical arrangement with Roman-numeral and Arabic-figure mixed entries (up to at least 816/CIX). This is a genuine Marine-secretariat cipher of 1690, but addressed to an army general (Lauzun, in exile after Ireland), several years and one minister before Vergier's 1696 letters, and structurally unlike Vergier's short numeral-group (2-3 digit) nomenclator -- a precedent that the Marine secretariat *did* use ciphers just before Pontchartrain's tenure, not a candidate key for this item. All other numbered ciphers on these three pages are diplomatic/military (ambassadors, Louvois, Catinat, Harlay/Callières, Rijswijk, Usson, Guelders/Rheinberg, Geertruidenberg), none Marine. |
| 3b | DECODE catalogue, fresh shallow clone of aaymeloglu/unsolved-ciphers, `catalogue/decode-catalog.csv` | `grep -ic marine` (broader than the prior pass's name-specific grep) | **0 hits for "marine" anywhere in the file** -- confirms no DECODE-catalogued item is described as Marine-department correspondence at all, 1680-1710 or otherwise. |
| 4 | FranceArchives (`francearchives.gouv.fr`), the two relevant finding aids named by web search: Marine B service général (`.../findingaid/f2ffbd1d85a3bb1c8589bef6efbbeb7ede139de3`) and Marine G documents divers (`.../fr/findingaid/f22395ba936c797082075c7b8bc1a94e624ad06c` and a second id `.../fr/findingaid/5e3004cc477f21951cdc2274a218f0bf40f40e67`) | direct curl, then `tools/browser_fetch.js` (headless Chromium) on the B-service-général one | **Unreachable.** curl gets a JS-redirect bot-mitigation stub (`window.location.href='/redirect_.../...'`); the headless-browser attempt (single retry, per playbook) returns a page titled "Attack detected" -- a bot-mitigation product blocking even a real browser, not the Cloudflare-interstitial kind other playbook entries describe. Neither finding aid is in the Wayback Machine (`web.archive.org/cdx/search/cdx` returns `[]` for both URLs). **Not one word of either finding aid's text was read this pass.** |
| 5 | siv.archives-nationales.culture.gouv.fr and siv.archives-nationales.fr (SIV, named in the brief) | reachability only | Both **blocked by this environment's egress policy** (`connect_rejected`, confirmed via `/__agentproxy/status`'s `recentRelayFailures`, not a site-side block) |
| 6 | archivesnationales.culture.gouv.fr (the legacy AN domain hosting the PDF finding aids `Marine_ancien.pdf`, `Marine-G.pdf`, `Marine-B4.pdf`, `Etat_des_inventaires_Marine_2007.pdf` found by web search) | reachability, then Wayback CDX for the Marine-G PDF | **Blocked by egress policy** (`connect_rejected`, confirmed in `/__agentproxy/status`); Wayback CDX for the same URL timed out twice (retried once, per playbook, then abandoned) |
| 7 | WebSearch (2 queries) for Marine G / MAR/G chiffre content, since the PDF above could not be fetched | `"Mar/G" OR "Marine G" Pontchartrain "chiffre" archives nationales`; a follow-up narrower query `"MAR/G/236" OR "Mar/G/237" OR "Mar/G/238" OR "Mar/G/239" chiffre` | First query's AI-generated summary asserted **"documents in MAR/G/236 to MAR/G/239 relate to colonial administration and include material on ciphers (chiffre)"** -- **this claim is UNVERIFIED**: it did not come with a quoted snippet or link to the actual finding-aid text (which is bot-blocked here, see row 4), and the follow-up query for those exact article numbers found nothing corroborating. Logged as an unconfirmed lead only, not a finding -- a worker who can reach francearchives.gouv.fr (a different network path, or the person) should read the Marine G finding aid directly before repeating this claim. |
| 8 | Persée (review of Henrat's B7 tome V-VI inventory) | direct fetch of the review already surfaced by the prior pass's web search | Confirms B7 = pays étrangers/commerce/consulats (Taillemite 1964-66 for articles 1-75, Henrat 1979-80 for 76-103), 1480-1755; the review text itself does not mention "chiffre". Not the right sub-series for Vergier's Dunkerque dispatches to Pontchartrain (which are Marine's own internal secretariat correspondence, B2/B3, not foreign-consular B7). |

**Candidate key locations, ranked (none confirmed as Vergier's own key):**

1. **AN Marine B2 244-435** (Google Books `Br5CAAAAYAAJ`), printed p.113/118/120/128/131 -- an index entry explicitly under "chiffre, chiffrant et déchiffrant" in a volume of the Marine secretariat's own *outgoing* correspondence register, the same B2 sub-series (`correspondance générale: ordres et dépêches`) that a prior sweep already found holds Pontchartrain's 1696 Dunkerque dispatches (article numbers ~112-113 in the *preceding* volume, B2 76-243) -- structurally the single best-fitting lead of this pass, entirely unread beyond the index line itself.
2. **HathiTrust Neuville v.3 (nyp.33433008502019) p.~318 and the 1885 Index volume (mdp.39015049755260) pp.11/309/328** -- three more index/content hits for "chiffre(s)" in the same printed inventory family, via the HTRC token-count route only; genuinely unread (no text retrieved).
3. **SHD Vincennes SH 49 item 35**, "Chiffre pour la correspondance des galères" -- a confirmed, named, surviving Marine cipher key of the right decade, but for a different correspondence circle (Mediterranean galleys, not Dunkerque); useful precedent/comparandum only.
4. **AN Marine G articles 236-239** -- unverified web-search claim, not independently confirmed, lowest confidence of the four.
5. Tomokiyo's Seignelay-Lauzun 1690 code -- a real Marine-secretariat cipher, but the wrong minister (Seignelay, d. 1690, not Pontchartrain), wrong correspondent (Lauzun, army), and a different design from Vergier's numeral-group nomenclator; a methodological precedent, not a candidate key.

No candidate here was confirmed against a page image or full page text; none should be described as "the key" to Clairambault 1108 without that check. No gallica.bnf.fr leads were found this pass (row 1e/1f is Google Books, not Gallica; nothing pointed at a Gallica ark for a Pontchartrain/Marine chiffre table).

**Requests this session:** archive.org 3, be-api.us.archive.org 4, catalog.hathitrust.org 4 (1 root reachability, 1 API test call, 1 real bibliographic-API call, 1 blocked `Search/Home`), data.htrc.illinois.edu 16 (2 passes of 8 volumes each, token-count endpoint only), francearchives.gouv.fr 3 (2 curl, 1 browser_fetch), siv.archives-nationales.culture.gouv.fr 1 (blocked), siv.archives-nationales.fr 1 (blocked), archivesnationales.culture.gouv.fr 2 (blocked), servicehistorique.sga.defense.gouv.fr 3 (1 root, 2 PDFs), www.googleapis.com 2 (Google Books volumes API, key+country=US, neither printed), books.google.com 17 (SearchWithinVolume JSON endpoint, ≥2s apart; 1 direct page fetch blocked by Google's own bot check, not retried), persee.fr 2, web.archive.org 5 (4 CDX lookups, one retried once after a tunnel reset per playbook), github.com 1 (shallow clone of aaymeloglu/unsolved-ciphers, grepped and discarded). WebSearch 5. No gallica.bnf.fr request made (out of scope for this lane). No logins, no subagents, no images fetched. Cost well under the $5 cap.

Not touched: no decoding, no key application, no novelty wording, no fetch of the actual candidate pages (Google Books p.113 etc., HathiTrust v.3 p.318) -- all four candidate-key leads above are unread and are the concrete next step for a follow-on worker or for LANE G2 (Gallica) if any of them turn out to cross-reference a Gallica ark.
## Reconciliation (24 Sept 2026)

LANE G2 worker C (Opus), disk only, no network. Settled on the native page images (`images/folio250_canvas253.jpg`,
`images/folio262_canvas265.jpg`), not on the crops: the crop "lines" cut a gloss tier and its cipher row into different
crops, which is most of passA/passB's 58.6% disagreement.

**Tiers, answered: the clear words written ABOVE the numeral groups are an interlinear decipherment, not part of the
letter.** This reverses the "gloss verdict" in "Du Vergier leaves" above, which was read at thumbnail scale. Evidence:
(1) a second hand, smaller and more cursive, each gloss ending in a long trailing flourish; on f.265 it is also a
different ink: the letter is pale brown-grey, the glosses are near-black. PassB's "fainter second layer" on f.265 is the
letter itself, and the "bold main hand" is the decipherer. (2) Each gloss stands over a run of groups, never over clear
words: f253L "i'ay veu ce matin 722 143 185 38 151 34 224" carries "Milord Myddleton et Jay eu une" over the groups
only. (3) The glosses are consistent with one another: 722 is "Milord Myddleton" three times (f253L R01, f265R R09 and
R13); 225 is "ny" four times (f253R R12, R14 twice); "10 301 14" is "avec" three times; "16 105" is "d'Angleterre"
twice. (4) The glosser corrects himself: "faict l'honneur" struck on f265L R20, "parfaitement" struck on f265R R08
because it is clear text on the next row. Every cipher run on the four pages carries a gloss, except that on f265R R01
the gloss begins at "M de Pontchartrain": the first nine groups (117 .. 289) have none. Same practice as clair1067 and
fr5160 f.87.

**Files.** `rows.tsv`: 141 physical rows (main and gloss), settled on the image, conf per token, alternatives and notes.
`reconcile.py [--check]` builds `ciphertext.tsv` (leaf, line, pos, token, conf, layer, alt, note: 668 cipher groups,
290 clear words, 1 struck group, 1 struck word), `dechiffre.tsv` (51 gloss rows), `signs.tsv` (the decode_key input), and
`pass_agreement.tsv`. Against the reconciliation, passA matches 94.4% of groups on f.253 and 86.5% on f.265; passB matches
52.2% and 64.7% (it dropped whole runs, not digits).

**Out-of-range values, checked on the image.** 722, 725, 720 and 700 are real single groups, a name series: 722 is
Milord Myddleton; 725 is Prince d'Orange (after 259 "le"); 720 is Roy d'Angleterre (f265L R09); 700 is "(d')Anglois"
(f265R R10). 601 is real and written twice in the letter's pale ink (f265L R15, R20). Both times it sits beside a
correction ("16" struck before it; "6[6]10" rewritten before it), and the alignment gives it no letters (null or slip).
Pass A's "1917" (f265R R11) is written without a gap; it is read 19 17 (M, alt 1917), since 17 is common and the alignment
gives 19 17 = "en". Also retouched in dark ink: "300" f265L R13, "30" f265R R01, and "143" f265R R12 (4 over 2).

**Structure.** 668 groups, 132 distinct values: 8-52 (dense, frequent: 30 x41, 10 x27, 17 x24, 28/29 x20), 104-303
(syllables and short words), 601/610, and 700-725 (names). The layout alternates clear connective French with cipher
runs of 4-45 groups; the sensitive nouns and the whole of each sensitive clause are in cipher. It is a syllabic code:
single letters, syllables (259 que, 133 de, 195 la, 196 le, 267 re, 289 te, 275 roi, 211 ment), words (225 ny, 298
tres, 142 est, 251 pour, 137 dans, 161 faire) and names. Repeats within and across the letters are frequent: "133 30
290 224 18 30 251" (des tinées pour) twice on f253R.

**Key.** `align_1696.py` reuses clair1067's `align_1646.py` EM unchanged (imported, not copied). It has 31 spans (one per
continuous cipher run, with its gloss), and four long names are treated as one symbol each ([text|sym] in SPANS). Result:
`key_1696.tsv` has 129 codes; 36 are single attestations and 25 are flagged conflict or minor conflict. Consistency is
0.933. Control (`control_1696.txt`, 3 shuffled span/gloss pairings, same EM): true pairing 0.926 against shuffled max
0.492 (mean 0.470); loglik -1330 against a best shuffled -2660. The control was run on the version before the A06 fix
below. `decode.json` + `python3 tools/decode_key.py ciphers/clair1108-duvergier --check` regenerates `reading_1696.txt`
and `reading_tokens_1696.tsv`: **667 tokens, C 584, M 82, U 1** (C = key value equals the aligned gloss at that
position; no H, no key source; the struck 16 is kept as a clear token). A cryptanalytic result graded from the letter's own
known plaintext.

The first key run itself caught an error in my span table. The 11 groups "281 29 / 195 119 30 289 133 42 18 50 32"
(f253L R07-R08) looked unglossed, but they decode as "sur la coste de Kent": the gloss over R07 runs on into R08. A06
was widened and the run repeated.

**Known weak spots for a solver (M rows, conflicts).** Words longer than the aligner's 7-letter cap (correspondance,
Hollande, honnesteté, recoivent) are split across neighbours. 725 prints "le&" (the aligner took "le" too); read 725 =
Prince d'Orange and 259 = le. 700 prints "angloi": a letter was dropped at the cap. 610 "m", 601 "0" and 8 "0" in "206
8 610 601 206" = "me mettre" are uncertain: the writer's slip, and only the two 206s and "32 33 267" are secure. 20 "f" /
161 "faire" (l'affaire = 195 20 161) is right as printed.

**Not done (follow-ups, one line each).** (1) ~~f.252 (fol.249r) ... is dense cipher with glosses~~ Settled 24 Sept 2026 in "fol.249r" below: no cipher on
249r; its numerals are show-through of 249v. Nothing to transcribe for the key. (2) f.251
(fol.247v, tail of an earlier letter) has not been cut either. (3) Rerun `align_1696.py --control 3` on the current spans
(about 10 minutes); the separation is not expected to change. (4) A search on the decoded plaintext (print_check, Marine
B3 inventory) was not run: this is a reconciliation, and novelty is not classified here.

## fol.249r (24 Sept 2026)

LANE G2 worker J (Opus), disk only, no network, 0 requests. Question: is fol.249r (right page of
`images/folio249_canvas252.jpg`) dense cipher with glosses (Reconciliation, "Not done" 1) or show-through of 249v
(`check_bleedthrough_f252.py`)? **Decided on the native image: show-through. 249r carries no cipher.**

Evidence. (1) Read at native scale, the pale numeral rows on 249r run right to left with mirrored glyphs: the top ghost
row reads, from the right edge leftwards, "l'ay ueu ce matin 722 143 185 38 ...", which is 249v's first row
(rows.tsv f253L R01) reversed. (2) `check_bleedthrough_f252.py` mirrors that region; the mirrored crop reads
"198 17 168 18 119 50 301 28 277 290 238 10 301 14 200." and "il m'a paru beaucoup 249 18 15 24 267 30 278 259",
digit for digit f253L R02-R03, and the glosses "longue conference avec luy" and "plus empressé ..." show through
with them (evidence crop `images/thumbs/check_f252_ghost_flipped_small.jpg`, 58 KB). (3) The show-through runs both
ways: the "faint dateline top left, partly lost" read as f253L R00 on 249v is 249r's heading, mirrored. (4) The dark
ink on 249r is all clear words; not one numeral group is written in it. The reconciler's "dense cipher with glosses"
and the thumbnail-sweep table's "dense cipher" came from the ghost rows, which at reduced scale look right-reading.

What 249r does say (clear, one hand; read from the image, grade H as transcription, not a decipherment):
"Mr Vergier a Boulogne ce 26e mars 1696 / Monseigneur / Depuis la derniere lettre que i'ay eu l'honneur de vous
ecrire i'ay esté deux iours a Dunkerque, ainsy que ie m'estois donné l'honneur de vous le marquer. et Mr De Louvigny
m'a obligé d'en rester un a Calais pour y congedier et payer la conduite de Calais a Dunkerque a l'equipage du
Lutin. et enfin i'arrivay icy hyer au soir." The letter then runs on to 249v ("i'ay veu ce matin 722 ...").
"Mr Vergier" at the head may be a clerk's docket-style heading; not settled.

Changes. rows.tsv: row f253L R00 removed (commented, with the reason); `reconcile.py` regenerated ciphertext.tsv and
signs.tsv (5 clear tokens fewer, cipher groups unchanged at 668); `tools/decode_key.py ... --check` exits 0 with the
same grades, **667 tokens: C 584, M 82, U 1**. key_1696.tsv is unchanged: 249r confirms, adds and contradicts
**0** codes, because it has none. align_1696.py was not rerun (no span or gloss changed; its control stands as before).

fol.247v (canvas 251): only `images/probe_f251.jpg` (654 x 500) and no native image are on disk, so 247v was
skipped, per the brief; its native fetch is LANE G2's to schedule. Suggestion (one line): once fetched, check 247v
at native scale for mirrored ghosts from 248r before cutting crops.

Not found / not done: no cipher on 249r to add to the key; no network; no novelty classification.
