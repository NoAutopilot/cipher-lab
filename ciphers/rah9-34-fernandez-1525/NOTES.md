found-solved
No CSP Spain edition volume opened by this worker for 1525 beyond the index (Bergenroth's CSP Spain vol.2 ends 1525; vol.3, Tyler, covers 1525-1526 -- this worker read only its index, British History Online `cal-state-papers/spain/vol3/no2/pp1041-1047`, not the calendar entries themselves); dbourdeau/cyphersolver's sessa1524 NOTES.md and key_working.md read by this worker from a fresh shallow clone (25 Sept 2026).

# Same "Luis Fernández" (Duke of Sessa) Rome-embassy hand, RAH Signatura 9/34, 1525 — QUEUE.md row D3

DECODE ids (row D3): R9896, R9899, R9901 (Non-decrypted) / R9898 (Decrypted neighbour).

## Verdict: his lane, found-solved — and the crib QUEUE.md proposed does not work as stated

QUEUE.md's own note for D3 says "try G2's key first, then read R9898's decipherment as a crib". Both halves of
that plan turn out to be wrong in a way that matters:

- **R9898 carries no decipherment**, despite DECODE's "Decrypted" tag. dbourdeau/cyphersolver's `sessa1524/`
  NOTES.md, pass 12 (his own words): "R9898, Sessa 24 Feb 1525, 9/34 ff. 150–156: same cipher, NO decipherment
  bound with it despite DECODE's 'Decrypted' status" — he read it through and got only context words (`z y`,
  `vo`, `per` all absent), not a crib pair. A worker following QUEUE.md's plan literally would open R9898
  expecting a clear-cipher pair and not find one; this is now on record so nobody repeats that trip.
- **The working key is not G2's** (RAH 9/26, Lope Hurtado 1522, `cs-recheck/lopehurtado/`) but the separate,
  later key Bourdeau built in `sessa1524/` from the 1524 Salazar A.31 siblings (ff. 138/140, 163-172, 320-324)
  and extended forward through 1523-25 material (R9834, R9893, R9897). His own notes record the key **moved**
  between 1522 and 1524 (`tef` = *paz* in 1522 but *nec-* in 1524; `L` = *i* in 1522 but *r* in 1524), so G2's
  49-value alphabet is not a safe crib for 9/34 without re-deriving it — Bourdeau already made this mistake-check
  and moved on to the 1524-25 key instead.

R9899, R9901 and R9896 are not individually named anywhere in his repository (grepped by id, no hit beyond
R9898). But R9898 (9/34 ff.150-156, 24 Feb 1525) sits in the same volume and the same active campaign — his
notes describe reading "the other 1525 letter, R9898 (14 pp.)... through as well" and cross-matching it against
R9834 (8 Sept 1523, key crib) and R9893 (24 Jul 1524, key crib) for template matches. This is the same working
key, mid-campaign, on the same shelfmark, not a separate unworked target.

## Search log (25 Sept 2026)

1. Bourdeau: same fresh shallow clone as rah9-31-fernandez-1524 (25 Sept 2026). Grepped "9/34", "A-34",
   R9896/R9898/R9899/R9901 individually. Only R9898 hits, in `sessa1524/NOTES.md`, `sessa1524/profile.json` and
   `sessa1524/key_working.md` (see quotes above); no folder named `sessa1525` or similar.
2. Aymeloglu: same fresh shallow clone. No 9/34-specific row found beyond the shared DECODE-catalogue metadata
   already cached on our own disk.
3. Editions: CSP Spain vol.3 (Tyler, 1525-1526) index (British History Online, "Index: F", `vol3/no2/pp1041-1047`)
   lists dozens of Sessa-to-Emperor letters through 1525-26 (pp. 23, 87, 88, 94, 118, 134, 135, 140, 150, 153,
   157, 172, 186, 201, 202, 210, 221, 244, 258, 260, 267, 272, 279, 285-6, 298, 300 for 1525; more in 1526) but
   the index does not carry Salazar shelfmarks, so this worker could not map R9896/R9898/R9899/R9901 to specific
   CSP entries without opening each monthly page and cross-checking folio numbers against Bourdeau's own table —
   not done this pass (cap); **this is the concrete residual print-check a next worker or campaign should do**,
   since CSP Spain vol.3 plainly covers this correspondent and year in volume.
4. Community: WebSearch for the cluster turned up nothing beyond Bourdeau's own GitHub Pages site. No Cryptiana/
   Cipherbrain hit. `sources/decode/NOTES.md` carries no mention of these ids.

## What a recovery worker would need

Nothing from this lane for the same reason as D2: this is inside an active daily-worked campaign on the same
shelfmark and key family. If the orchestrator later wants R9898 checked directly against a DECODE image (to
confirm Bourdeau's "no decipherment bound" reading rather than take it on trust), the DECODE login worker would
need R9896, R9898, R9899, R9901 — not requested here, no action taken.

Images: not fetched by this worker (no DECODE login; playbook forbids it for this role).

Hosts this pass: WebSearch 2, britishhistory.ac.uk (WebFetch) 1 (index page only), github.com 2 shallow clones
(shared with D2, grep only, not counted twice).
