# BnF fr.20140 — Charles de Danzay to Henri II / Cardinal of Lorraine, January 1557

Status: found-solved (3 of 4 items); open (1 of 4, f.35)

Check-solved pass, 24 September 2026 (Sonnet, orchestrator brief for M13-M16). Editions-first + one-leaf pass;
a formal six-source check-solved run is still owed for the f.35 remainder before it goes on the board.

## Check-solved (24 Sept 2026, formal pass for f.35)

Second pass, same day, dedicated to the one remaining item, f.35 (27 Jan 1557, Danzay to the Cardinal of
Lorraine, "not deciphered" per Tomokiyo — quoted verbatim above). No reading or key application attempted;
this only asks whether the plaintext or a decipherment already exists somewhere in print. Every source below
checked 24 Sept 2026.

1. **Tomokiyo's page** (`sources/cryptiana/web/danzay.htm`, local mirror, already quoted above): the only
   source that names this exact folio and date. States f.35 is the one item of the four "not deciphered" and
   that he has "not seen (images of)" either printed edition below. No stronger claim available from this page.
2. **Correspondance de Charles Dantzai / Bricka (1901)** — checked what this edition actually covers, since the
   brief that opened this pass named it "the standard edition of exactly this correspondence." That is not
   correct and is corrected here: WebSearch confirms the 1901 volume's own title is *Indberetninger fra Charles
   de Dançay til det franske Hof om Forholdene i Norden 1567–1573* (Bricka, Copenhagen, C.A. Reitzel) — its
   subtitle states the span 1567–1573. It cannot contain a 1557 letter; ten years before its earliest despatch.
   Not chased further (HathiTrust `hvd.hnnfqp` catalog page itself 403'd to curl, Cloudflare-gated per the
   playbook; moot given the date mismatch already rules it out).
3. **Correspondance de Charles Dantzai (1824), Handlingar rörande Skandinaviens Historia vol. IX, Stockholm,
   Elmén et Granberg** — this is the actual candidate for 1557 material (from Swedish, not Danish, archives;
   Fryxell was the series' general editor across its run, hence "Fryxell's Handlingar" in the brief). Found a
   same-numbered volume on Internet Archive, `handlingarrrand06unkngoog` (Google-scan metadata: "volume": "9",
   "date": "1821" — the date field on these old Google-metadata records is frequently wrong/approximate and is
   not itself disqualifying). Fetched its full djvu text directly (no login, 447 KB, single request) and grepped
   locally: **zero** hits for "Danzay", "Dantzai", "Dançay" (any case) and **zero** hits for "1557" anywhere in
   the volume. Also checked archive.org's global full-text index (`be-api.us.archive.org/fts/v1/search`, no
   login needed) for "Dantzai" scoped to this identifier: 0 hits; and unscoped: 133 hits across the whole
   archive, none of them this identifier or an obvious sibling volume (top hits are an unrelated 1910 Danzay
   biography `undiplomatepoite00richuoft`, already known from Tomokiyo's own bibliography, and unrelated
   periodicals). Conclusion: either this Google-scan copy is a different volume that happens to share Google's
   internal "volume: 9" tag (the Handlingar series was rescanned/renumbered inconsistently across different
   Google Books projects — this is plausible, not confirmed), or the true 1824 volume IX is not on Internet
   Archive under a name this search surfaced. Google Books: no full-view edition found under the title
   "Correspondance de Charles Dantzai" or under "Handlingar rörande Skandinaviens historia" + "Dantzai" (0 hits
   both queries, `&country=US&key=$GOOGLE_BOOKS_KEY`, key never printed). **Not located; genuinely unreached,
   not searched-and-cleared** — this is the one source in this pass that stays an open gap, not a checked
   negative.
4. **Calendar of State Papers Foreign, Mary 1553–1558** (Turnbull, 1861) — a WebSearch hit surfaced a "Danzay,
   —, letter from, 290" index entry, but tracing it (British History Online, `cal-state-papers/foreign/vol16`)
   showed it belongs to volume 16 of the CSP Foreign series (context: "States' army", "Leicester's footman" —
   1580s Dutch Revolt material), not the Mary 1553-1558 volume. No Danzay entry located in the actual
   1553-1558 volume's own index by this method. Not chased further by direct page-by-page read (an English
   calendar of state papers is not where a French ambassador's outgoing despatch to a French cardinal would be
   calendared unless intercepted; low prior, and the brief's own source list treats it as a formality check).
5. **Internet Archive full text / general search**: covered under item 3 above; also ran a bare
   `archive.org/advancedsearch.php?q=Dantzai` title search — 0 hits.
6. **Solver repositories** — not re-cloned this pass; citing the M13-M16 check-solved worker's fresh shallow
   clones of both `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers` from earlier the same day (24 Sept
   2026, this file's first section above), which found no hit on "20140" or "Danzay" in either. Re-cloning
   twice in one day for the same volume would be wasted cost against the same result; if this is later
   contested, redo it.

**Verdict: still open.** No source in this pass — the two printed editions, the English calendar, Internet
Archive, Google Books, or the solver repositories — produces a decipherment or plaintext for f.35 specifically.
The 1901 edition is ruled out on internal evidence (date range). The 1824 edition, the one edition that could
plausibly cover it, was not successfully located in full-text-searchable form this pass; this is a gap, not a
clearance, and should not be read as "checked, absent." Status stays open for f.35; the key is already
published (Tomokiyo) from the sibling decipherments, so this remains a recovery job, not cryptanalysis, per the
verdict already on record above.

## Images

Folio offset calibrated this pass directly from the primary ark's own IIIF manifest (`../manifest.json`, already
on disk, no fetch needed) rather than by probing: its canvas `label` fields carry the manuscript's own
foliation (e.g. canvas id `f69` → label `35r`), not just sequence position. Single-folio canvases run from
index 17 (`9r`); recto canvas index = `2×folio − 1`. Checked against three folios Tomokiyo names and confirmed
exact: `16r`→canvas 31, `24r`→canvas 47, `30r`→canvas 59. Folio 35: recto = canvas index 69 (`f69`, label
`35r`), verso = canvas index 70 (`f70`, label `35v`). This resolves the previous pass's "canvas-to-folio offset
uncalibrated" note — no probing needed once the manifest's own labels are read.

Fetched (gallica.bnf.fr, browser User-Agent, 1.5 s apart, 4 requests total this leg): a 1200px preview of each
canvas first (confirmed by eye — folio headed "35", margin dated "27 Jan. 1557", matching Tomokiyo's entry
exactly), then the native-resolution image for each (`f69` 4800×7062, `f70` 4791×7091). Also fetched, from
`cryptiana.web.fc2.com` (1 request), the key-table image `danzay_1557.png` that Tomokiyo's page embeds but that
was not previously mirrored (only the HTML was) — saved to `sources/cryptiana/web/danzay_1557.png`, needed as
the legend for the passes below.

f.35 recto is mostly clear French (Tomokiyo's letters do open in clear, per his page); the cipher is confined to
~7 lines at the foot of the page, beginning mid-sentence after "...Monseigneur je vous puis asseurer que".
f.35 verso is cipher from the first line to the last, no contemporary decipherment visible in the margin on
either leaf — consistent with Tomokiyo's "not deciphered." Cut three crops (local, from the native images, no
extra network fetch): `f69_cipher.jpg` (the recto cipher block, 2400×960), `f70_cipher_top.jpg` and
`f70_cipher_bot.jpg` (the verso cipher block split in two with a ~4-5 line overlap so no line falls on a crop
boundary, each 2400×~1515). Full provenance, pixel boxes and the offset derivation are in `images/manifest.json`.
Folder size 8.9 MB (native_f69.jpg 3.2 MB, native_f70.jpg 3.0 MB, three crops ~2.2 MB combined, two previews
~0.5 MB, plus the pre-existing 115 KB `alt_f40.jpg`) — well under the 30 MB cap.

## Passes

Two independent Sonnet subagents (`passA.tsv`, `passB.tsv`), neither shown the other's output or told what the
other found, transcribed the cipher signs on the three crops line by line (R1... for the recto, V1... for the
verso) against Tomokiyo's sign legend (`danzay_1557.png`: a–z minus j/k/v/w, a nulls column, and word-signs for
"dict/et/le/luy/quel?/son?" and "Dannemarch"/"le Roy de Dannemarch"), naming each sign by its legend letter,
"null", a "word:" gloss, or an "unkN" label for shapes matching nothing in the legend. Format: `line  position
sign  confidence` (H/M/L). No reconciliation, no key application, no decoding attempted — that is explicitly
out of scope for this pass.

## What the target is

Gallica ark `btv1b52521512h` (alt. digitisation `btv1b10782904z`), a recueil "Pièces relatives à la Suède et au
Danemark (1557-1706)". `services/OAIRecord` confirms: *"Correspondance, originale et en partie chiffrée, de
Charles de Danzay, ambassadeur en Danemark, 1557-1567 (fol. 16)."* — matches QUEUE.md M15 exactly.

## Checked (24 Sept 2026) — this is the found-solved finding

`sources/cryptiana/web/danzay.htm`, already mirrored locally (no fetch needed), S. Tomokiyo, "Danzay's Ciphers:
Ciphers of a French Diplomat with a Long Tenure" (first posted 22 Feb 2026). Per rule 10, quoted verbatim rather
than paraphrased, because it names this exact shelfmark and folios:

> BnF fr.20140 includes ciphertext in four letters from Danzay in the reign of Henry II:
> f.16 10 January 1557 (to Henry II, deciphered in separate sheets)
> f.24 10 January 1557 (to Cardinal of Lorraine, deciphered in the margin)
> f.30 27 January 1557 (to Henry II, deciphered in the margin)
> f.35 27 January 1557 (to Cardinal of Lorraine, not deciphered)
> The reconstructed cipher is as follows. It can be seen most double letters are represented by the letter
> itself with a diacritic sign above or below... many nulls are used...

Tomokiyo reconstructed the full substitution/diacritic key **from the contemporary decipherments already
present** on f.16, f.24 and f.30 (one "in separate sheets", two "in the margin") — i.e. three of the four
ciphered items are already deciphered in the manuscript itself and their plaintext is in hand; only f.35 lacks
a contemporary decipherment. He states he has not seen a fifth item beyond these four, and separately (same
page) that Ryabov (2025) independently reconstructed a *different*, later Danzay cipher (1574-1578, BnF fr.4736
and fr.2812) from similar marginal decipherments — a different volume, not this one.

- Fresh shallow clone of `dbourdeau/cyphersolver`: no hit on "20140" or "Danzay" tied to this volume.
- Fresh shallow clone of `aaymeloglu/unsolved-ciphers`: no hit.
- Printed editions Tomokiyo cites but has not seen images of: *Correspondance de Charles Dantzai, ministre de
  France à la Cour de Danemarck* (1824, from Swedish archives) and C.F. Bricka (ed. 1901, from Danish archives,
  HathiTrust `hvd.hnnfqp`) — both post-date 1557 material differently (Bricka's volume title says 1567-1573);
  neither confirmed or ruled out as covering the four January 1557 letters specifically. Not chased further this
  pass (Tomokiyo's manuscript-internal decipherment finding already settles the status for f.16/f.24/f.30
  regardless of print).
- Gallica IIIF: one connection reset on the primary ark fetching a canvas near the expected f.35 location,
  retried once per the good-citizen rule, failed again — stood down on that ark per the rule (one retry only)
  and switched to the alternate digitisation ark named in QUEUE.md. That ark's canvas 40 (`images/alt_f40.jpg`)
  showed two clear-French leaves, one headed with a leaf number "30" and a marginal date "1558" — **not
  confirmed as Tomokiyo's f.30** (canvas-to-folio offset uncalibrated for either ark, and no cipher or
  interlinear decipherment was visible on this particular canvas) — inconclusive, not a contradiction of
  Tomokiyo's report.

## Verdict

**Found-solved for f.16, f.24, f.30**: plaintext already exists in the manuscript via contemporary decipherment,
and Tomokiyo has already published the reconstructed key from it. No new cryptanalysis is possible or needed on
these three. **Open for f.35 alone**: the one item without a contemporary decipherment, but the key is already
published and this letter is written the same day (27 Jan 1557) by the same hand to the same correspondent type
as the deciphered f.30 — a cheap recovery/transcription job, not cryptanalysis. QUEUE.md M15's "kind" (currently
"cryptanalysis") should be corrected to **recovery (published key via sibling decipherment)**, matching the
Dupuy 468 / M15 pattern already established as precedent in LESSONS.md. Grade: no reading attempted by this
worker; f.16/f.24/f.30's grade is Tomokiyo's own H (contemporary decipherment) once transcribed, f.35 would
grade S (cryptanalytic, but with a key derived from H sources — closer to a recovery than a blind attack).

Cheapest next step: transcribe f.35 (one leaf) against Tomokiyo's published key and check it decodes to
coherent French; no image-hunting beyond that single leaf is needed.

## Sources

- Gallica: `https://gallica.bnf.fr/ark:/12148/btv1b52521512h` (primary), `https://gallica.bnf.fr/ark:/12148/btv1b10782904z` (alternate).
- S. Tomokiyo, "Danzay's Ciphers: Ciphers of a French Diplomat with a Long Tenure", cryptiana.web.fc2.com,
  mirrored locally at `sources/cryptiana/web/danzay.htm` — credit Tomokiyo for the key reconstruction and the
  identification of the three contemporary decipherments; this worker did no cryptanalysis.
- github.com/dbourdeau/cyphersolver, github.com/aaymeloglu/unsolved-ciphers (both checked, no relevant content).

## Requests this pass

gallica.bnf.fr: 1 OAI record + 1 manifest + 2 IIIF image attempts on the primary ark (1 connection reset,
retried once per rule, failed again, stood down) + 1 IIIF image fetch on the alternate ark (succeeded).
github.com: 2 shallow clones (shared with M13/M14, deleted after grep).
