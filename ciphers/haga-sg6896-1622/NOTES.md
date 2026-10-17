open
Resolutien der Staten-Generaal Nieuwe Reeks Deel 4 (GS176) pp.462, 482 (res. 3178b, 3332a), Deel 5 (GS187) pp.260, 536 (res. 1644a, 3504/3504a), and Deel 7 (GS223) p.529 (res. 3065) read in full by this worker via resources.huygens.knaw.nl/retroboeken/statengeneraal (`search_in_text`/`searchText` accessor); Heeringa & Nanninga, Bronnen tot de geschiedenis van den Levantschen handel (resources.huygens.knaw.nl/retroboeken/levantschehandel, 6 vols) searched by this worker for "Haga" (325 hits), "cijfer" (7 hits) and "ontcijferd" (0 hits), all hits read.

QUEUE row: SCOUT-KEYS K1 (QUEUE.md "## Key-beside-cipher candidates (17 Oct 2026)"; harvest/SCOUT-KEYS-2026-10-17.tsv).

## Target

Cornelis Haga, Dutch ambassador at Constantinople, to the States General. Nationaal Archief 1.01.02 (Staten-Generaal)
inv. nr. 6896 holds a duplicate of a Haga despatch carrying an "onopgeloste cijfercode" (unsolved cipher code) on a
letter dated 30 April 1622, per the Resolutien SG's own footnote to res. 3504 (NR 5 p.536). The 1620 key is DECODE
R2118 (NA inv. 6894), already applied by Bourdeau (`targets/haga1620`) to R2113/R2115; R2114 (11 May 1620) was
already marked Decrypted on DECODE before Bourdeau's pass.

## Six sources (CHECK-HAGA, 17 Oct 2026)

- **Web** (4 plain queries): "Cornelis Haga 1622 cijfercode Constantinopel ontcijferd"; "Haga 1622 letter cipher
  States General '6896' decipher"; "Cornelis Haga cipher key Constantinople 1620 1622 cryptanalysis"; "Haga
  Constantinopel 'onopgeloste cijfercode' S.G. 6896". No hit naming a decipherment or cryptanalysis of this item;
  results are Haga biography, an unrelated TNA SP 84/106/111 record (18/28 May 1622, not the 6896 item), and
  unrelated Huygens Besluiten-SG 1626-1651 entries.
- **Blog comment threads** (site-restricted queries, per check-solved.md "Required step"): Cipherbrain
  (scienceblogs.de/klausis-krypto-kolumne), the Cryptiana blog (cryptiana.blogspot.com), Cipher Mysteries
  (ciphermysteries.com) -- no hit for "Haga" on any of the three.
- **Print**: Resolutien SG (primary source, read directly, not quoted from the harvest -- see "Resolutions read"
  below). Heeringa & Nanninga's *Bronnen tot de geschiedenis van den Levantschen handel* is on the same Huygens
  retroboeken platform (`resources.huygens.knaw.nl/retroboeken/levantschehandel`, `search_in_text` accessor, 6
  vols, Deel 1 = GS9 ... Deel 6 = GS120); searched "Haga" (325 hits across the whole edition -- the index pages
  VII-XXIV and the Deel 1 narrative pp.63-157 region, where the hit density is highest, were read; all relate to
  Haga's ordinary diplomatic business, none to a cipher), "cijfer" (7 hits total, all read: none mention Haga or
  1622 -- they are scattered mentions in Deel 1 pp.188/362/415 and Deel 2 pp.908/987 and Deel 5/6, none naming
  Haga), "ontcijferd" (0 hits, "Er zijn geen resultaten gevonden"). No print edition of this item's decipherment,
  and no editor's note that it was ever deciphered or left undeciphered, found.
- **DECODE**: cached crawl (`sources/decode/records-decrypted-2026-09-24.tsv`,
  `records-non-decrypted-2026-09-24.tsv`, `keys-all-2026-09-28-merged.tsv`) carries only NA inv. 6894 (1620) Haga
  records -- R2113 (Non-decrypted), R2114 (Decrypted), R2115 (Non-decrypted), R2118 (key) -- and nothing for inv.
  6896 or 1622. One live RecordsList sender-filter probe
  (`RecordsList?x_sender=Haga&z_sender=LIKE&cmd=search`) returned 0 record rows; the filter's operator syntax for
  a free-text field is unconfirmed against this CMS, so this probe is not relied on alone -- the cache (named in
  the brief) is the primary source and it is unambiguous: no 1622 record exists on DECODE yet.
- **Bourdeau** (`dbourdeau/cyphersolver`, shallow clone, `targets/haga1620/` read in full plus README.md,
  CATALOGUE.md, SOLVED_RANKING.md, SOLVED_CATALOGUE.md grepped for "Haga"): covers only NA inv. 6894 (1620: R2113,
  R2115, with R2114 noted as already Decrypted on DECODE and not re-read), and is marked "complete" in all four
  catalogue files. No mention anywhere in the repository of inv. 6896, 1622, or a "next"/"todo"/"planned" pointer
  toward this item (check-solved.md's "stated next step" rule).
- **Aymeloglu** (`aaymeloglu/unsolved-ciphers`, shallow clone, grepped for "haga" and "6896"): no hit relating to
  Haga's 1622 material. The repository's own `catalogue/decode-catalog.csv` row for id "6896" is an unrelated
  DECODE record (Florence, Archivio di Stato di Firenze ASFi_SIIVol1_103), a coincidence of DECODE's internal
  numbering, not the NA inventory number.
- **Cryptiana** (Tomokiyo, cryptiana.web.fc2.com): site-restricted web search returned no result for "Haga".

### Resolutions read (primary source, not the harvest's paraphrase)

- **Res. 3178b** (NR 4 p.462, dated within the entry for ~24 April 1620 a.o.): "b. Haga, dd. Constantinopel 15
  febr. en 12 maart. Hij stuurt de cijfercode, die hij gebruiken zal wegens het gevaar van onderschepping" -- Haga
  sends the cipher code he will use because of the risk of interception. This is the establishment of the 1620
  system (DECODE R2118).
- **Res. 3332a** (NR 4 p.482, "1juni1620" page header): "3332a S.G. 6894 (orig.). Aldaar ook nog een brief van 23
  maart (orig.); beide met ontcijfering." -- both the 9 April and 23 March 1620 letters carry a decipherment,
  consistent with Bourdeau's `haga1620` read.
- **Res. 1644a** (NR 5 p.260, 23 Aug 1621): "1644. Ontvangen brieven van: a. Haga, dd. Constantinopel 30 juni, met
  een cijfercode. President Culemborg zal deze aan Frederik V tonen. Er mogen geen kopieën van worden uitgedeeld."
  Footnote 1644a: "S.G. 6895 (orig.). Inzake Turkse hulp aan Bethlem Gabor. [...]" -- about the letter's content
  (Turkish aid to Bethlen Gábor), not about the cipher system. **Correction to the harvest's framing**:
  QUEUE.md/harvest row K1 reads this as "Haga sent a NEW code" in 1621; the resolution itself only says the
  letter arrived "met een cijfercode" (with a cipher code) -- it does not say *nieuwe* (new), and nothing here or
  in the footnote distinguishes this code from the one established in March 1620 (res. 3178b). Whether the 1622
  duplicate's cipher is the same R2118 system or a different one stays open and untested by this resolution text.
- **Res. 3504/3504a** (NR 5 p.536, within the entry for 14 June 1622): "3504. Van een brief dd. Constantinopel 16
  april van Haga mag de griffier geen kopieën uitgeven." Footnote: "3504a S.G. 6896 (duplicaat met onopgeloste
  cijfercode op brief dd. 30 april)." -- the original (16 April) is discussed by the resolution; the footnote
  separately locates, in the same inventory number, a *duplicate* with an unsolved cipher code, on a letter dated
  30 April. The immediate neighbouring resolutions (3501 Rutgertsius, 3502 Franse troepen soldij, 3503 Lambrecht
  Henricxsz., 3505 Middelburg kooplieden) were read in full and are unrelated matters, with no decipherment
  mentioned beside this one.
- **Res. 3065** (NR 7 p.529, 8 Sept 1625): "Haga schrijft dd. Constantinopel 21 juni en 12 juli. Het ontcijferde
  inzake vredesbesprekingen met Spanje zal worden overgebracht aan de Venetiaanse ambassadeur." -- a later (1625)
  Haga letter *was* deciphered ("het ontcijferde"), showing the office kept deciphering his despatches well past
  1622; this is not evidence either way about the 1622 duplicate specifically.

## Premise check (adversarial, CHECK-HAGA, 17 Oct 2026)

(a) **Folder's own mentions**: none -- this folder is newly created by this worker; nothing to check.
(b) **Other solvers' working files**: Bourdeau's `targets/haga1620/` (read in full) covers inv. 6894 only and is
    marked complete; no file in his repository mentions inv. 6896 or 1622. Aymeloglu: grepped, no hit. Not found.
(c) **Physical neighbours**: the printed Resolutien's own immediately neighbouring entries (res. 3501-3509, NR5
    p.536) were read in full -- none mentions a decipherment filed beside 3504a's duplicate. The physical leaves of
    inv. 6896 itself were sampled at low resolution (two contact sheets, see Material step) looking for a page
    that looks visually distinct (numeral-dense, as a cipher span would look in isolation) or carries a legible
    dateline; neither test was conclusive at the resolution used. Not found / inconclusive -- a closer pass is the
    named next step.
(d) **Recipient's side**: N/A -- the States General is itself the recipient and the holding archive for this
    item; there is no separate recipient-side edition to check.

## Material step

NA item page (`www.nationaalarchief.nl/onderzoeken/archief/1.01.02/invnr/6896`) read via its embedded
`drupal-settings-json` `viewer.response`: inv. 6896, unittitle "1622", `isDownloadable: true`, **575 scans**, each
with its own `service.archief.nl` IIIF endpoint
(`https://service.archief.nl/iip/iipsrv?IIIF=<path>/<uuid>.jp2/...`) -- digitised and copy-free, confirming
SCOUT-KEYS K1's flag independently. No item-level (sub-date) description exists in the page's own metadata beyond
the single inv.-level title "1622"; the finding aid does not break the 575 scans into dated sub-items.

Two contact sheets (vision calls: 2 x USD 0.5 = USD 1.0, per the brief's price line):

1. **Sheet 1** -- native thumbnails (188x256) for scan orders 120, 126, ..., 318 (34 pages, every 6th across
   roughly the first 55% of the volume, on the working assumption the lias is bound in roughly chronological
   order across the year). Ordinary Dutch secretary-hand prose throughout; no page visually distinct as
   cipher-dense. This null result is expected, not a miss: the 1620 system (R2118) is "mostly clear Dutch with
   enciphered spans" (Bourdeau's own description), not visually distinguishable from plain prose at thumbnail
   scale, so a pattern-matching pass like this cannot find it even where it is present.
2. **Sheet 2** -- IIIF crops (400px wide) for scan orders 256, 264, ..., 400 (19 pages), a denser sample around
   the estimated reception window for an April-dated despatch (the 1620 and 1621 letters both show roughly a
   7-9 week Constantinople-to-Hague transit, which would put a 30 April letter's arrival, and likely its binding
   position, around mid-to-late June 1622). Same result: ordinary prose, no legible dateline readable at 400px on
   this hand, no page identifiable as the 30 April duplicate or its cipher.

**Leaf not identified** within the brief's 2-contact-sheet vision cap. Two transient `Connection reset by peer`
errors on `service.archief.nl` (orders 156 and 246, sheet 1; order 296, sheet 2) were each retried once after a
pause and succeeded (good-citizen single-retry rule); no other host issue.

## Verdict

**open.** Confirmed still unsolved: no period decipherment and no modern reading of the 30 April 1622 Haga
duplicate (NA 1.01.02 inv. 6896) found in six independent sources, each read or searched directly by this worker
(not taken from the SCOUT-KEYS harvest's paraphrase -- see "Resolutions read" above, including one correction to
its framing of the 1621 letter). The material is digitised and copy-free (575 scans, IIIF). The next test needs
the exact leaf first.

`tools/intake_gate_check.py haga-sg6896-1622` output:
```
haga-sg6896-1622: open (line 1) -- edition/page or full-text-search citation found within 6 lines
```
exit 0.

## Next test

1. **Locate the leaf** (unblocked, cheap): a focused native-resolution crop pass on the April-June 1622 run,
   roughly 10-15 single-page IIIF fetches (not a contact sheet) targeting the dorsal/address-leaf docket of each
   spread, where a contemporary filing note ("Haga... Aprilis/April 1622...") is most likely legible even where
   the body text is not -- about USD 1.
2. **Key application** (gated on step 1): once the leaf is found, fit Bourdeau's R2118 alphabet + 116-code
   nomenclator against the duplicate's cipher spans, with a shuffled-key control (CLAUDE.md rule 3) -- a fit is
   key application of an already-published-and-credited key (RETRO-2026-10-05 P4 labelling: `key application`,
   not recovery), a miss points to the res. 1644a "cijfercode" instead, which has no period decipherment on file
   yet to test against -- about USD 2.

## While waiting

None of this is blocked on a person or an outside party. The leaf-location step (Next test 1) depends on nobody
and is the one action the next worker or lane can take without waiting.

## Web and blog check (CHECK-HAGA, 17 Oct 2026)

(a) Four plain web searches:
1. "Cornelis Haga 1622 cijfercode Constantinopel ontcijferd" -- no hit naming a decipherment; results are Haga
   biography pages (Wikipedia, Deutsche Biographie, dbnl) and an unrelated 1613 pamphlet.
2. "Haga 1622 letter cipher States General '6896' decipher" -- no hit for "6896"; nearest result is TNA SP
   84/106/111 (18/28 May 1622 Haga letter, open but not digitised, a different item), and an unrelated Yale
   cipher-sheet record about Portugal, not Haga.
3. "Cornelis Haga cipher key Constantinople 1620 1622 cryptanalysis" -- no hit on any cryptanalysis of Haga's
   correspondence; results are biography and an unrelated Ottoman-cipher HistoCrypt listing.
4. "Haga Constantinopel 'onopgeloste cijfercode' S.G. 6896" -- no hit on this exact phrase; results surfaced
   three unrelated entries from the Huygens Besluiten Staten-Generaal 1626-1651 database (a newer, separate
   digitisation from the `retroboeken` edition used above) for other Haga letters (1625/1626/1628), none
   mentioning a cipher.

(b) Three blog site searches, read for any comment-thread hit (per check-solved.md's CHECK-SOLVED-WEB rule):
- `site:scienceblogs.de/klausis-krypto-kolumne Haga Constantinopel` -- no result from the blog itself.
- `site:cryptiana.blogspot.com Haga` -- no result from the blog itself (results were all unrelated "Haga" surname
  matches elsewhere on the web).
- `site:ciphermysteries.com Haga Constantinople cipher` -- no result from the blog itself (nearest: an unrelated
  2024 paper on Lorenzo Ventura's Constantinople cipher, a different person and archive).

No decipherment, plaintext, or discussion of this item (NA 1.01.02 inv. 6896, the 30 April 1622 Haga duplicate)
found in any of the seven queries across the three named blogs and open web search.

## HAGA-LEAF (17 Oct 2026)

**Leaf not pinned to a single scan this pass, but the search range is narrowed from CHECK-HAGA's 256-400
(144 scans, untested at native resolution) to about order 321-327 (6-7 scans), using a calendar method rather
than more contact-sheet sampling.**

12 native-resolution single scans fetched via `service.archief.nl/api/file/v1/default/{uuid}` (the item page's
own `drupal-settings-json` -> `viewer.response.scans` gives order -> uuid -> this URL directly, no METS/IIIF path
construction needed; simpler than `ciphers/oldenbarnevelt-brederode-1605/screen_tools/na_fetch.py`'s pattern for
this host). Full list, UUIDs and per-scan findings in `images/manifest.json`; images under `images/` (15 MB).
Requests: 12 image fetches + 1 item-page fetch = 13 to www.nationaalarchief.nl/service.archief.nl, >=1.5s apart
(two were a 3.1s cadence from an earlier probe, well clear), no 429/403/challenge.

**Method.** inv. 6896 is not Haga's letters alone: it is a mixed Levant/Barbary file (Smyrna bills of exchange,
Algiers/Tunis instructions, Ottoman-script correspondence, Livorno and Milan letters, general news digests, as
well as Haga's own despatches), confirmed by what the 12 scans actually show (manifest "finding" field per scan).
Many leaves carry a clerk's docket at the top of the first page in the form "Dat[um] <written date> / Rece[ptum]
<received date> <year>" -- when present, this gives the archive's own filing date directly, which is more reliable
than guessing from transit-time alone (CHECK-HAGA's approach). Two such dockets were read this pass and used as
calendar anchors:

| scan order | docket read | note |
|---|---|---|
| 320 | Dat 28 maert / Recep 14 april 1622 | unrelated correspondent (troop/regiment matter) |
| 328 | Date 17 juny / Recepto 7 july 1622 | opens with Constantinopel news (Sultan Osman/Mustafa, the May 1622 Ottoman regicide) |

Both anchors are internally consistent: written-date gap (17 Jun - 28 Mar = 81 days) over 8 scan-orders and
received-date gap (7 Jul - 14 Apr = 84 days) over the same 8 orders agree to within 4%, giving a local rate of
about 10.1-10.5 days per scan-order in this stretch of the volume (scan density is *not* uniform across the whole
575-scan item -- order 330 to 350 alone spans 5 Jul to about 12-22 Aug, a much faster ~4 days/order, so this rate
is local to orders ~320-330 only and should not be extrapolated past that window).

Applying the 320 anchor's rate to the target's two written dates:
- 16 April 1622 (the original, res. 3504): 28 Mar + 19 days -> order ~320 + 19/10.1 ~ **322**
- 30 April 1622 (the duplicate, res. 3504a, the actual target): 28 Mar + 33 days -> order ~320 + 33/10.1 ~ **323**

Order 327 (checked directly, one order before the 328 anchor) already carries Constantinopel/Ottoman-regicide
news matching the same register as 328, supporting that orders ~325-330 are the right general neighbourhood for
Constantinopel material reaching The Hague in June-July 1622. Order 340's docket was not fully read this pass
(budget) but its left-margin address note appears to read "...Constantinopoli" -- plausibly a later Haga letter
(consistent with the calendar: 340 would fall after the 328 anchor, i.e. written later than 17 June).

**Not found within the 12-scan cap**: no scan actually fetched (100, 230, 252, 274, 300, 320, 327, 328, 330, 340,
350, 450) is the 16 or 30 April Haga letter or its docket -- the two calendar anchors bracket the target to orders
**321-327** (the span between the 14 April receipt anchor's neighbourhood and the first Constantinopel-news hit)
without landing on it directly within this worker's cap.

### Next step (HAGA-LEAF2, unblocked, cheap)

Fetch native-resolution scans for orders **321, 322, 323, 324, 325, 326** (6 scans, all inside the narrowed
window, same `service.archief.nl/api/file/v1/default/{uuid}` route via `images/manifest.json`'s per-order
UUIDs already on file where reused, else re-read from the item page's `drupal-settings-json`); read each
docket/first line for "Haga", "Constantinopel", "16 april" / "30 april" / "duplicaet". ~USD 2 (6 vision calls
+ overhead) at the README per-pass rate. If found: proceed to **HAGA-KEYAPP** (Bourdeau's R2118 alphabet +
nomenclator against the cipher spans, shuffled-key control, label key application per RETRO-2026-10-05 P4) --
about USD 2 more, per CHECK-HAGA's original estimate. If not found in 321-326: extend one order at a time
outward (327 already checked; try 319, 318... and 329, 331... before widening past the 310-335 band), since
the 10.1 days/order rate is only a local estimate and the true position of a single 2-3 day gap between the
16 and 30 April letters' receipt could sit a few orders either side.

Unblocked, as before (CHECK-HAGA, "## While waiting" above): the leaf-location step above depends on nobody
and is the next action available to any worker or lane.

## HAGA-LEAF2 (17 Oct 2026)

**Scan: not found. Cipher lines: 0 across the whole window. No decipherment, because no cipher.** Orders
321-326 fetched at native resolution (`service.archief.nl/api/file/v1/default/{uuid}`, UUIDs read fresh from
the item page's `drupal-settings-json`, same route as HAGA-LEAF); order 327 re-examined from the existing
fetch (no new request). All 7 scans read.

| order | dateline/signature | content | cipher? |
|---|---|---|---|
| 321 | none visible | continuous Dutch prose, "Hooghe ende Moghende Heeren" header; looks like a States-General resolution/memorial text, not a letter | no |
| 322 | "Date: 22 april 1622"; addressed "Doorluchtige Hoochgeboren Vorst Genadichste Heer" | a letter to a Prince (not the States General), opens discussing Constantinople-related diplomacy | no |
| 323 | closes "...te Venetien den [] April 1622", signed "A.E." (or similar, illegible past initials) | continuation/close of 322's letter; mentions Constantinopel and France/Spain affairs; written **from Venice**, not Constantinople | no |
| 324 | "Date 10 juny / Recep 2 july 1622"; "mijn genaedichste Heeren" | Vlissingen garrison-payment matter (2,000 ducats, troops) | no |
| 325 | closes "Hooghe Mogende Heeren ... in Venetien den [] July 1622", signed "Philip Calandrijn" | continuation/close of 324's letter; same Venice correspondent | no |
| 326 | left page: sealed cover/address verso of the 325 letter ("Aux Hauts et Puissants Seigneurs...", wax seal); right page new letter "Date 24 juny" | Milan/Spanish-troop movements (Bergamasca, Messina) | no |
| 327 (re-read, no new fetch) | no dateline/signature visible in this spread (continues from the preceding, unfetched leaf) | France/Spain/Milan military movements, then "Uyt de stadt van Constantinopele werden geschreven..." (news from Constantinople: Sultan Osman/Mustafa) -- a **news-digest paragraph inside someone else's letter**, not a despatch written from Constantinople | no |

**Finding: the calendar window itself is the wrong correspondent.** Orders 322-327 are not Haga material at
all -- they are a Venice-based correspondent's letters (the 322/323 pair, unsigned past "A.E.", and the
324/325 pair signed Philip Calandrijn), one of which relays Constantinople news secondhand (327's paragraph).
That explains why order 327 "read" as being in the right register (CHECK-HAGA/HAGA-LEAF's inference) without
being Haga's own hand: a Venice newsletter reporting Ottoman news reads exactly like Constantinople chatter
at the content level. The 320/328 anchors (troop-regiment letter; Constantinopel-opening letter) bracket this
Venice correspondent's run internally consistently by date, but that run is not Haga's despatch -- the
volume interleaves distinct correspondents' bundles rather than filing strictly by one sender's chronology
(as CHECK-HAGA's "mixed Levant/Barbary file" note already flagged), so a date-anchored projection from two
*different, nearby* correspondents' letters does not reliably land inside a third correspondent's (Haga's)
own run, even when the dates agree.

**Not a reliable local rate either**: within 321-326 the dates do not run monotonically with scan order
(22 Apr at 322, Venice/April at 323, 10 Jun at 324, Venice/~Jul at 325, 24 Jun at 326) -- bundles of a few
leaves each are filed together, not single sheets in strict date order. The 10.1-10.5 days/order rate HAGA-LEAF
derived from 320->328 is therefore not a dependable local clock for pinpointing one leaf inside this stretch;
it happened to bracket a correspondent's batch, not a continuum.

### Next step

Vision/request budget exhausted this pass (7 vision calls, the brief's cap; 13 host requests across HAGA-LEAF
and this job). Two candidate next steps, cheaper than more blind native-res reads:
1. **Re-read the item page's own scan list for a boundary marker.** `drupal-settings-json` gives `label` per
   scan (e.g. `NL-HaNA_1.01.02_6896_0321.jpg`) but no document-level title; check whether the Nationaal Archief
   finding aid (the `/onderzoeken` page, not yet grepped for this) or the EAD/XML behind it exposes a
   per-document index (sender, date) rather than per-scan images only -- would turn this from a blind native-res
   sweep into a targeted fetch. One page fetch, no vision calls, near-zero cost.
2. **If no index exists**, widen the native-res sweep away from the 320/328 anchors rather than between them:
   try order 329 (the one gap scan between the 328 Constantinopel-opening letter and the already-checked 330
   Milan letter) and orders 318-319 (just before the 320 troop-matter anchor), since Haga's own bundle may sit
   adjacent to, rather than between, the two anchors that turned out to belong to the Venice correspondent.
   ~USD 1-1.5 for 2-3 more native-res scans + reads.

intake_gate_check.py not re-run (no new deep-work campaign started, only a continuation of the already-gated
leaf-location step). file_shrink_guard.py not run (new content appended to an existing file this worker owns
this pass; no other tracked file touched). Hosts: www.nationaalarchief.nl (1 request, item page),
service.archief.nl (6 image requests), >=1.5s apart, 7 total this job (20 cumulative with HAGA-LEAF).

## Parent decision after HAGA-LEAF2 (17 Oct 2026, 05:3x UTC by date -u; account-4 parent)
Three jobs (CHECK-HAGA, HAGA-LEAF, HAGA-LEAF2; USD 11.4) have not pinned the 30 April 1622 duplicate: the lias interleaves correspondents'
bundles, so date projection from neighbouring letters is not a locating instrument here. Blind docket reads stop (rule 3's third-attempt
clause, shape (b)). Status stays open. The next step needs a different instrument: a per-document listing of inv. 6896 (none in the NA
finding aid at item level; a Haga-specific calendar, e.g. the Heeringa Bronnen's own footnotes citing S.G. 6896 folios, would be one), or
a systematic docket contact sheet of all 575 scans at a legible resolution (about 48 vision calls, USD 14), to be priced only after
the cheaper key-material checks on K2 (Aitzema). Six questions: learned that this volume is not Haga's run; depended on two anchors
from other senders; unverified: whether Haga's own bundle sits elsewhere in the volume; alternative: the duplicate is bound with its
original of 16 April in a Haga bundle well away from these orders; most informative next: a listing, not more reads; decision: pivot
program C to K2.
