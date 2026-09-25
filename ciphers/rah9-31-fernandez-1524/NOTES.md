found-solved
CSP Spain vol.2 (Bergenroth 1866) read by this worker at britishhistory.ac.uk/cal-state-papers/spain/vol2/pp614-626 (April 1524, entries 633-643); dbourdeau/cyphersolver's own sessa1524 NOTES.md and key_working.md read by this worker from a fresh shallow clone (25 Sept 2026).

# Rome embassy correspondence (Lope Hurtado de Mendoza's circle; letters signed "Luis Fernández"/Duke of Sessa), RAH Signatura 9/31, 1524 — QUEUE.md row D2

DECODE ids (row D2): R9872, R9875, R9879, R9880, R9882, R9883, R9885-R9889, R9891, R9892, R9894 (Non-decrypted) /
R9872, R9881, R9884, R9890, R9893, R9895 (their own Decrypted neighbours, one per sub-cluster).

## Verdict: his lane, found-solved

dbourdeau/cyphersolver's `sessa1524/` (title: "Duke of Sessa (Luis Fernández de Córdoba) → Charles V, Rome, 18
April 1524 — RAH Salazar A-31 (9/31) ff. 128–131", status "read in part") is a live, working-key campaign on
**this exact shelfmark**, RAH Colección Salazar y Castro A-31 = Signatura 9/31. DECODE's catalogue date "1424" is
a typo for 1524 (confirmed independently below); the sender is not a separate "Luis Fernández" but Luis Fernández
de Córdoba, 2nd Duke of Sessa, imperial ambassador at Rome 1522-26, working alongside Lope Hurtado de Mendoza.

His own table of the volume (sessa1524/NOTES.md), cross-checked by this worker against CSP Spain vol.2 directly
(British History Online, `cal-state-papers/spain/vol2/pp614-626`, entries 633-643, read 25 Sept 2026):

| CSP no. | date | letter | Salazar A.31 | DECODE | this worker's read of CSP |
|---|---|---|---|---|---|
| 633/635 | 13 Apr | Lope Hurtado -> Emperor / -> Gattinara | ff. 61-67 | R9871, R9872 **Decrypted** | confirmed: "M. Re. Ac. d. Hist. Salazar. A. 31. ff. 61-63" / "ff. 65-67" |
| 639 | 17 Apr | Sessa -> Emperor | ff. 138-140 | R9881 **Decrypted** | confirmed: "Salazar. A. 31. ff. 138-140" |
| — | 18 Apr | Sessa -> Emperor + duplicate (Bourdeau's own target) | ff. 128-131 | R9877, R9878 | **not calendared** — CSP entry 642 for 18 Apr is a different letter (Lope Hurtado, Salazar **A.33** f.172), confirming Bourdeau's "Bergenroth skipped this letter" |
| 643 | 22 Apr | Sessa -> Emperor | ff. 163-172 | R9883, R9884 **Decrypted** | confirmed: "Salazar. A. 31. ff. 163-172" |

R9883 and R9895 (both on D2's own Non-decrypted/neighbour list above) are named by Bourdeau's notes as part of
this same run (R9883 in the CSP-643 sibling pair table; R9895 as a mostly-clear 29 Jul 1524 letter he read in
pass 14 for template matches). The remaining D2 ids (R9875, R9879, R9880, R9882, R9885-R9889, R9891, R9892,
R9894) are not individually named in his repository files, but they fall inside the R9877-R9895 id span his
working key (`key_working.md`, ~50 secure code values plus the letter alphabet, built from the ff.138/140,
163-172, 320-324 crib pairs) already covers, and he is actively extending it forward (his pass 10-14 log runs
through R9897, R9898, R9834, R9893 in the same document sequence, into 9/33 and 9/34 — see rah9-34-fernandez-1525
for the sibling verdict).

**D6** (QUEUE.md: R9659 / R9652, RAH Signatura 9/26, extension of row G2/Lope Hurtado) is not a separate target:
QUEUE.md itself says to fold it into G2's existing `cs-recheck/lopehurtado/` work rather than opening a folder.
No action taken here beyond this note, per the job brief.

## Search log (25 Sept 2026)

1. Bourdeau: fresh shallow clone of dbourdeau/cyphersolver (25 Sept 2026, this worker's own clone, not a cached
   digest). Grepped for "9/31", "A-31", "Luis Fernández", "Lope Hurtado", "sessa1524", and every individual D2
   DECODE id. Result: `sessa1524/` matches the shelfmark and id range exactly (see above); no per-id hit for
   R9875/9879/9880/9882/9885-9889/9891/9892/9894 beyond the id range they sit in.
2. Aymeloglu: fresh shallow clone of aaymeloglu/unsolved-ciphers (25 Sept 2026). No folder or catalogue row
   specific to 9/31 beyond the same DECODE-catalogue metadata already on our own disk
   (`sources/solver-diffs/2026-09-23-decode-neighbours-annotated.tsv`).
3. Editions: CSP Spain vol.2 (Bergenroth), April 1524, read directly by this worker at British History Online
   (`cal-state-papers/spain/vol2/pp614-626`) — see table above. CODOIN and the RAH Colección Salazar y Castro
   printed catalogue were not opened this pass (time/cap); flagged as unchecked, not as absent.
4. Community: WebSearch for "Luis Fernández" / "Duke of Sessa" Rome cipher 1523-1525 solved — turned up only
   Bourdeau's own GitHub Pages site (dbourdeau.github.io/cyphersolver), no independent announcement. No Cryptiana
   or Cipherbrain post found for this cluster. DECODE comments on disk (`sources/decode/NOTES.md`) carry no
   mention of these ids.

## What a recovery worker would need

Nothing from this lane: duplicating dbourdeau/cyphersolver's `sessa1524/` campaign on the same shelfmark with
the same working key would be the disallowed case CLAUDE.md flags ("a catalogue a daily-active project also
reads is not a lane"). If the orchestrator wants independent verification of his readings, the DECODE login
worker would need R9877, R9878 (his stated target) plus the Decrypted siblings R9871/R9872/R9881/R9883/R9884/
R9890/R9893/R9895 to check image quality against his transcriptions — not requested here, no action taken.

Images: not fetched by this worker (no DECODE login; playbook forbids it for this role). Page images are behind
DECODE's login wall; not checked for a no-login route this pass.

Hosts this pass: WebSearch 4, britishhistory.ac.uk (WebFetch) 1, github.com 2 shallow clones (grep only).
