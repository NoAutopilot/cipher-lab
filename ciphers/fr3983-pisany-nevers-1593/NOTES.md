# fr.3983 f.169 (Pisany -> Nevers, 23 Mar 1593) — Marquis de Pisany (Jean de Vyvonne) to the Duke of Nevers

Status: **found-solved**

Checked by LANE N4 csKSa (check-solved), 24 Sept 2026, following `.claude/briefs/check-solved.md` and
`.claude/briefs/runs/2026-09-24-lane-n4-csKSa.md`. Row KS-04 from
`sources/solver-diffs/2026-09-24-keys-vs-siblings.tsv`, originally scored `copy-free`, `kind recovery`.
**This session's leaf check overturns that framing before any nomination: the letter already carries a period
office decipherment written on the page.**

## 1. What is established

- BnF fr.3983, "Collection Mémoires de la Ligue". Gallica ark `btv1b9059406b` (481 canvases, all "NP").
- Sender: Marquis de Pisany (Jean de Vyvonne). Recipient: Louis de Gonzague, duc de Nevers.
- Key: Tomokiyo's no.46 (fr.3995 f.86-87, "the place name on the endorsement reads 'Chelles'"; two-digit
  figures with homophones and nulls; figures with an overbar, figures, figures with two dots above represent
  names/words). Table transcribed by Daniel Bourdeau (CC BY 4.0, `key46.txt`).

## 2. Leaf confirmation and the found-solved finding (this session)

Canvas estimate (297, from a first-pass ~1.7-2x-folio guess, unconfirmed -- this volume was never opened by
Bourdeau's session) fetched and checked directly:

- Canvas 297 (`images/f169_canvas297_try.jpg`,
  `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9059406b/f297/full/,1000/0/native.jpg`) shows folio **"169"**
  stamped top right and **"23 de Mars 1593"** dated top left, salutation "Monseigneur" -- confirms canvas 297 =
  folio 169, matching KS-04 exactly on both folio and date.
- The body is dense two-digit-figure cipher (key no.46 style), but a high-resolution crop of the opening lines
  (`images/f169_crop_top.jpg`, native region `.../f297/0,1700,4948,1800/2200/0/native.jpg`) shows **clear French
  words written interlinearly above (and below) most of the cipher figure-groups, in a lighter/thinner hand than
  the cipher itself**: readable glosses include "premierement", "de ce qu'il", "davantage", "faict ... apres
  pour", "la courrier", "d'autre", "ma lettre", "en sçachant", "tenvoir"/"renvoyer", "savoir", "faut monstrer ...
  de l'inquisiteur", "de la presente", "moyen", "qui en entreprendra", "point", "discontenu", "que pour cela je
  ne vous ...", "ma femme". This is a **contemporary interlinear decipherment**, not a modern annotation -- same
  pattern as the fr.3986 f.64-65v Gondi-to-Pisany letter already excluded elsewhere in this queue section for
  the identical reason ("carries the office's own contemporary interlinear decipherment, already transcribed in
  full by Bourdeau; not an open cipher").
- **This matches Tomokiyo's own listing pattern, read closely**: his no.46 section (`sources/cryptiana/web/
  nevers.htm`, lines 441-452) lists five letters under this key and explicitly tags two of them
  "**undeciphered**" (fr.3985 f.209 and fr.3986 f.168) -- but does *not* tag this letter, fr.3983 f.169, that
  way. He simply lists it plain: "Pisany to Duke of Nevers, Padova, 23 March 1593 (BnF fr.3983 fol.169)". The
  one other untagged letter in that same list, fr.3986 f.64 (Gondy to Pisany), is the one already confirmed
  elsewhere to carry an interlinear decipherment. The pattern (tagged = genuinely undeciphered, untagged = not)
  is consistent, not proof on its own -- but it corroborates the direct leaf read rather than contradicting it.

## 3. Six-source sweep (partial -- superseded by the leaf finding)

Web, DECODE (`sources/decode/`), Bourdeau (`nevers1593/` -- this volume, fr.3983, is not in his README's scope
at all: "not in Bourdeau's nevers1593/ folder (which only covers the reverse-direction Nevers->Pisany letters in
fr.3985/3986)", per the TSV note) and Aymeloglu (grepped, no fr.3983 f.169 hit) were checked and found nothing
that names this letter as already read by a modern solver. Gomberville seconde partie (Google Books
`H2eV4wAmIr0C`) search-within for "Pisany" (5 hits) and "Mars 1593" (not separately queried) turned up only
narrative mentions of Pisany as a person, not this letter's text. None of that matters for the verdict: a
modern-solver search is the wrong test here. The leaf itself already carries the answer, put there by the
Duke of Nevers' own office in 1593.

## Verdict

KS-04: **found-solved -- the leaf (BnF fr.3983 f.169, Gallica canvas 297) carries a contemporary interlinear
decipherment over most of the cipher text, in the same hand pattern as the already-excluded fr.3986 f.64-65v
Gondi letter; not an unread cipher.** No nomination posted. Not scored `open`; QUEUE.md's KS-04 row updated to
this status rather than promoted.

This is **not** a claim of a modern first reading (rule 10) -- it is the opposite: the plaintext has been on
the page since 1593. Per the found-solved convention (README F0/F1/F2), what this session did *not* know until
the leaf check: that a reading already exists in the archive for this letter. What it hands on: a transcription
task (read the existing interlinear gloss off the image), not a recovery or cryptanalysis task. Per this
brief's scope, this session does not transcribe the gloss -- that is a job for whichever lane picks this up
next (flagged in ROOM.md).

## Credit

Key no.46: Satoshi Tomokiyo (`nevers.htm`), Daniel Bourdeau (CC BY 4.0, `key46.txt`). The interlinear
decipherment itself is the unnamed period office's, not any modern solver's.

## Next step (one line)

Transcribe the interlinear gloss directly from the image (no key application needed, no annealer) -- a short,
disk-only pass; cross-check any faint word against `key46.txt` where the gloss is illegible.
