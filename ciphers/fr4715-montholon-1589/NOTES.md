open

INTAKE-4715 unit B, 27 Sept 2026: solver-ready intake only (Layout, no reading, no decoding, no class), on the
`ciphers/nevers-birago-fr3251-1572` pattern. Built from KEY-ADJACENT.tsv row 19 and
`sources/cryptiana/web/bnf4715.htm` (local mirror, section id=no58, read in full this session; not re-fetched).

# BnF fr.4715, no.58 (f.81), Sieur de Montholon to an unnamed recipient, Tours, 8 November 1589

Francois II de Montholon, Keeper of the Seals for the Catholic League. Digits, per bnf4715.htm.

Tomokiyo, verbatim (bnf4715.htm section id=no58):

> "no.58 (f.81) Letter of Montholon, Tours, 8 November 1589. This can be read with the Vieuville-Nevers
> cipher (for which see another article). The decipherment of the beginning is given below."

The BnF catalogue itself independently confirms this item is undeciphered: archivesetmanuscrits.bnf.fr
full-text search "non dechiffre", checked 27 Sept 2026 (ark:/12148/cc577658/cd0e811), "Lettre du Sr DE
MONTHOLON. Chiffre non dechiffre. Tours, 8 nov. 1589" -- matching sender, place and date exactly.

## The gate (this job's first step)

Fetched the page's own image for no.58 (`BnFfr4715f81.png`, into `sources/cryptiana/web/img/`, manifest not
yet written for this single file -- see "Requests" below) and looked at it directly: it is a plain manuscript
scan (dense cipher digit groups with a handful of interspersed plain-French words and a two-line clear
salutation/close top and bottom), not an interlinear or annotated reading like the mantua.htm case
(INTAKE-3979). The page's own prose confirms this independently: "The decipherment of the beginning is given
below" -- only the beginning, and the printed passage itself ends "...." (an explicit ellipsis in the source,
not this worker's truncation). **Gate verdict: only the opening is deciphered, the expected case** -- this is
a genuine open target with a partial known plaintext, not a found-solved retirement.

## What's on disk

- `known_plaintext.txt`: Tomokiyo's own printed prose decipherment of the letter's opening (grade H, rule 4 --
  his reading, not ours), transcribed verbatim from the local mirror.
- `aligned_dump.txt`: the SAME opening passage, but as Tomokiyo's own group-by-group cipher/plaintext
  alignment (his page's "DUMP" block, immediately after the prose) -- also grade H. Extracted by decoding the
  page's raw bytes as cp932 (it declares `charset=SHIFT_JIS`; a plain utf-8 read replaces several of the
  page's own printed glyphs with the mojibake replacement character, U+FFFD, losing real data -- flagged here
  since a later worker re-fetching or re-reading this page should decode it the same way).
- `keys/key_vieuville_nevers.tsv`: the letter-homophone substitution table from `nevers.htm` (section
  id=BnFfr3641, image `phelippes8.png`, a clean printed/digital table, not a hand-drawn one) -- 34 sign rows,
  21 plaintext-letter values (a-z minus j, k, v, w; French convention, i covers j, u covers v), transcribed by
  direct inspection plus one independent blind Sonnet subagent read as a cross-check (agreed on every cell
  except whether "64" sits under column h or i, settled by this worker with a zoomed pixel crop -- it is
  under i). Two cells hold a non-numeric printed glyph instead of a digit (the table's own s and x columns'
  extra homophones); both were **cross-validated**, not just visually re-checked, against `aligned_dump.txt`'s
  running text, which uses the identical characters for s and x in ordinary decoded words ("hasard",
  "excomunie") -- graded AB, not left at the initial M. `tools/key_design.py` reads it `usable=yes`,
  design_family `homophonic` (accurate for the letter table alone; see the word-code caveat below).
  `tools/key_design.py --check` passes; KEY-OFFICES.tsv and KEY-DESIGN.tsv both carry rows for this key.
- `images/manifest.json`: f.81r (canvas 177) and f.81v (canvas 178), Gallica ark btv1b52509819x, fetched at
  1000px. The ark's IIIF manifest carries its own folio labels for this span ('81r'/'81v' directly, not a
  formula-derived offset -- the manifest has two INCONSISTENT offset runs elsewhere in the volume per
  `tools/gallica_folio.py`'s own warning, so the label is what was used, not either offset). Eye-checked: a
  600px fetch of canvas f177 matches Tomokiyo's own page image (same wax-seal-shaped stamp top-left, same
  text-block shape, folio number "81" visible top-right) -- confirms the labelled canvas independently of the
  label itself.

## An important caveat for any future decode: a second, undocumented code table

nevers.htm's own prose on this cipher says: "Figures with a dot over the first digit are code numbers
representing common words" -- illustrated there only for a *different* letter (Governor of Sy to Nevers, BnF
fr.3633 f.22: 16=de, 19=et, 20=est, 24=il, 25=la, 26=le, 35=ne, 36=na, 40=ou, 42=pour, 43=plus, 46=que,
48=quil?, and two-dot forms 11=villes, 76=gens de pied, 88=duc, 93=monsieur). `aligned_dump.txt` (this
letter's own alignment) uses the SAME apostrophe/dot notation extensively -- roughly a third of its tokens are
dotted -- and glosses several of them directly: '47=qui, '30=ma, '41=par, '65=comme, '16=de, '11=au, '20=est,
'48=quil, '42=pour, '19=et, '46=que, '25=la, '35=ne, '50=se, '99=vous, '28=luy, '64=catholique, '75=faire,
'52=si, '22=je, '31=me, '40=ou, '27=les, '14=ce, plus a few left unglossed by Tomokiyo himself ('97, '94,
'51, '36, '15, '13, '7, '84). Some values agree with the fr.3633 list above (16=de, 19=et, 20=est, 40=ou,
42=pour, 46=que), others do not appear there at all -- this may be a partially overlapping but not identical
table, or the fr.3633 list may itself be incomplete. **Not built into a second key TSV this session** (out of
this job's scope); a future decode pass against the rest of f.81r/f.81v will hit these dotted codes constantly
(they cover very common short words) and should not assume every unmatched digit group is a transcription
error before checking whether it is dotted in the original image.

## Requests (network log)

cryptiana.web.fc2.com: 2 requests this unit (`BnFfr4715f81.png`, `phelippes8.png`), 2 s apart, descriptive
User-Agent (out of this job's 5-request allowance across both units; unit A used 0). gallica.bnf.fr: 3 requests
(canvas f177 at 600px for the eye check, then f177 and f178 at 1000px for the manifest), through
`tools/gallica_folio.py` for the label lookup plus direct IIIF fetches, 1.5 s apart. No archive.org requests
this unit (not needed -- no printed-volume page to confirm, unlike unit A). No credentials, no AskUserQuestion.

## What remains before any class (rule 10) or any deep-work brief

- `tools/intake_gate_check.py fr4715-montholon-1589` (run before any deep-work brief, per the intake gate rule).
- Transcribe f.81r's cipher passage from the image (two blind passes), decode with
  `keys/key_vieuville_nevers.tsv`, calibrated against `known_plaintext.txt`/`aligned_dump.txt`'s printed
  opening -- this is the aligned-letters advantage the fr.3251 lane's own targets lacked (per this job's own
  brief). The dotted word-code table above is the likely main source of undecoded tokens; a future worker
  should first check whether an unmatched group is dotted in the image before treating it as an error.
  A 20-shuffled-key control (rule 3) before any claimed reading; reading to a verifier.
- f.81v and beyond: unexamined this session; the letter's full extent (how many folios) is not established.
- A full check-solved pass proper (`.claude/briefs/check-solved.md`) has not been run; this job only confirmed
  the found-solved gate (no) and the BnF catalogue's own "non dechiffre" flag, per KEY-ADJACENT.tsv row 19's
  digitised cell and this NOTES.md's own citation above.
- Once a reading exists: `tools/print_check.py` on the decoded phrases (rule 10).
