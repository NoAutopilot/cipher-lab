# BnF fr.20140 — Charles de Danzay to Henri II / Cardinal of Lorraine, January 1557

Status: found-solved (3 of 4 items); open (1 of 4, f.35)

Check-solved pass, 24 September 2026 (Sonnet, orchestrator brief for M13-M16). Editions-first + one-leaf pass;
a formal six-source check-solved run is still owed for the f.35 remainder before it goes on the board.

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
