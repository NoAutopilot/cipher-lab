open

INTAKE-3251, 27 Sept 2026: solver-ready intake only (Layout, no reading, no decoding, no class). Built from
KEY-ADJACENT.tsv row 2 (SCOUT-OWN-6, 27 Sept 2026) and `sources/cryptiana/web/nevers.htm` (local mirror,
read in full by this worker, not re-fetched, section id=BnFfr3251). Tomokiyo, verbatim:

> "BnF fr.3251 contains letters partially in cipher from Lodovico Birago to Duke of Nevers (1570-1572)."
> "From September 1570 to May 1571, they used the Ceppo-Nevers Cipher below (reconstructed from BnF fr.4702)."

# Ceppo-Nevers Cipher letters (BnF fr.3251), Lodovico Birago to Duke of Nevers, Sept 1570-May 1571

All from Saluzzo. Digits, per Tomokiyo (KEY-ADJACENT.tsv row 2, `token_shape` column).

## Undeciphered (this folder's targets, no "(with decipherment)" marking on nevers.htm)

| folio | no. | date |
|---|---|---|
| f.11 | no.6 | 14 September 1570 |
| f.21v | no.11 | 12 October 1570 |
| f.35 | no.18 | 15 November 1570 |
| f.87 | no.45 | 9 May 1571 |

(f.87 no.45 is not in KEY-ADJACENT.tsv row 2's own three-folio summary or the SCOUT-OWN-6 ROOM line, but the
brief for this job named it explicitly as a fourth target: nevers.htm lists the whole September 1570-May 1571
run as ff.11, 21v, 27, 35, 39, 82, 87, and only 27/39/82 carry "(with decipherment)" -- f.87 is not one of them.)

## Witnesses (known-plaintext siblings -- carry a period decipherment, the calibration set per the fr7129 lesson)

| folio | no. | date |
|---|---|---|
| f.27 | no.14 | 6 November 1570 (with decipherment) |
| f.39 | no.20 | 30 November 1570 (with decipherment) |
| f.82 | no.42 | 20 March 1571 (with decipherment) |

## Excepted (already in this repository, a DIFFERENT cipher, not part of this folder)

f.119 no.63, Saluzzo, 13 November 1571: nevers.htm says "In November 1571, they used a numerical cipher (not
deciphered)" -- a distinct, third cipher from the Ceppo-Nevers one above, already covered by
`ciphers/birago-nevers-1571` (status: open, no key found). Not duplicated here.

## The key

> "In 1572, the year of Birago's death, they used a new cipher, which can be reconstructed from the
> decipherment attached to no.87 is called the Nevers-Birago Cipher (1572) herein."

(That sentence names the OTHER cipher, covered by the sibling folder `ciphers/nevers-birago-fr3251-1572`.) This
folder's own key, the Ceppo-Nevers Cipher, is reconstructed by Tomokiyo from a different volume, BnF fr.4702:

> "(BnF fr.4702) Fols.36-37 are letters from Cesare Ceppo to the Duke of Nevers. One has interlined
> deciphering, which allows reconstruction of the cipher as follows (called "Ceppo-Nevers Cipher" herein).
> This in turn allows reading of the undeciphered letter "io sono avisato via di Milano et ..." but not quite."

The printed table itself is the image `nevers_add1.png`, embedded in nevers.htm immediately after that
paragraph -- see "Key blocker" below; it was not transcribed this session.

## Check-solved header (not a formal check-solved pass -- see "What remains" below)

What has been checked, by whom, when:
- **Community list.** Tomokiyo's `nevers.htm` names all four target folios above and does not mark any of them
  "(with decipherment)" -- read in full by this worker, 27 Sept 2026, local mirror, not re-fetched.
- **Sibling correspondence, same shelfmark.** `ciphers/birago-nevers-1571/NOTES.md` (LANE CX, 25 Sept 2026) ran a
  full six-source check-solved sweep on this exact sender-recipient pair (Birago to Nevers) and its finding on
  point 1 applies here without change: *"no published edition of Birago's letters to Nevers exists"*, confirmed
  by two web searches, not merely assumed. That file also confirms DECODE has no record for fr.3251 at all
  (`records-non-decrypted-2026-09-24.tsv` and Aymeloglu's DECODE mirror grepped for "birago"/"3251", zero hits),
  and that Bourdeau's own `birago/NOTES.md` and `profile.json` (`prior_solution.exists: "no"`) found no sibling
  solution either, after sweeping all 118 remaining fr.3251 openings for a matching cipher design.
- **Solver-repository cross-check.** `sources/cryptiana/READABLE.tsv`'s own row for `unsolved.htm` quotes
  Bourdeau's `SOLVED_CATALOGUE.md` directly: *"Birago and Ceppo to Nevers (about 13 letters)... catalogue
  318... Read in part... ff. 11, 21v, 35, 87, 138-174, 184... have no published reading"* -- Bourdeau
  independently lists this exact set of folios (both this folder's four and the sibling folder's seven) as his
  own open, unread work, which corroborates Tomokiyo's own "not deciphered" wording rather than merely repeating
  it (a second, independent source naming the identical folio list as unsolved).

What remains before any class (rule 10) or any deep-work brief:
- A formal `.claude/briefs/check-solved.md` pass proper (this intake job is Layout only, not check-solved) --
  `tools/intake_gate_check.py ceppo-nevers-fr3251-1570s` should be run before any deep-work brief; the citation
  above (full-text read of nevers.htm, no printed edition to open) is written to satisfy that gate's shape, not
  as a substitute for the formal pass.
- The catalogue's own record for BnF fr.3251 (`archivesetmanuscrits.bnf.fr/ark:/12148/cc49712p`) has not been
  read by this worker for a fuller description or availability flag beyond the ark already used by
  `ciphers/birago-nevers-1571`.
- Once a reading exists: `tools/print_check.py` on the decoded phrases (rule 10; CLAUDE.md README common tail).

## Key blocker (not reached this session)

`keys/key_ceppo_nevers.tsv` (header only, no rows -- see that file) could not be transcribed. Tomokiyo's printed
table for this cipher is the hand-drawn image `nevers_add1.png`, embedded in `nevers.htm` directly after the
BnF fr.4702 paragraph quoted above. It is **not** present in this repository's local mirror
(`sources/cryptiana/web/`; confirmed absent by `ls`/`find`, only `nevers_no55.png`, `nevers_no57.png` and
`nevers_no58.png` were ever cached from this page) and it is hosted on `cryptiana.web.fc2.com`, a host outside
this job's stated network allowance ("Gallica IIIF and the BnF catalogue" only). `sources/cryptiana/keys/IMAGE-QUEUE.tsv`
already lists it (row for `nevers.htm` / `nevers_add1.png`, flagged `looks_like_key: no` by the automated pass --
wrong for this image specifically, given the surrounding text; a human/model glance would catch it) but it has
never been fetched.

**Next step:** a worker with `cryptiana.web.fc2.com` in its network allowance fetches `nevers_add1.png` (this
folder) and `NeversBirago.png` (the sibling folder), transcribes each into `keys/key_<name>.tsv` (columns sign,
value, kind, source, unclear) with a second blind transcription pass and disagreements listed, per
CLAUDE.md's own image-key pricing note (Usage item 6: no recorded rate yet for this shape, price it like
CRYPT-KEYS-B and confirm on the first table before committing to both). Only then do `KEY-OFFICES.tsv` and
`KEY-DESIGN.tsv` gain rows for these keys and `tools/key_design.py --check` pass with real data; registering an
empty or fabricated key now would misrepresent the state. Priced conservatively, this is its own job, not a
top-up of INTAKE-3251's cap.

**Next step:** transcribe the cipher passages of the listed folios (two blind passes) and apply
keys/key_<name>.tsv with a 20-shuffled-key control; reading to a verifier. (Blocked on the key-table fetch
above until then.)
