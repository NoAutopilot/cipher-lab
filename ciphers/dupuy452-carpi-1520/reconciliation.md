# Reconciliation, f.20 (Alberto Pio de Carpi to Madame [Louise de Savoie]), 23 September 2026

## Method actually used (and why it differs from the brief)

The brief asked for two independent Sonnet-subagent passes over native-resolution line crops,
reconciled row by row, for a cipher passage estimated at ~70-90 tokens on one leaf. No subagent
tool was available in this session's tool set (checked: no Task/agent-spawning tool was present
alongside Bash/Read/Edit/Write/Artifact/ToolSearch and the Claude_Code_Remote MCP tools). Per the
brief's fallback ("run the passes as your own two independent readings if subagents are
unavailable, say which"), the intended fallback was a single agent doing two independent
readings of its own.

That fallback was only partly executed. Full-resolution imaging (done to satisfy the brief's own
"check the verso" instruction) showed the passage is roughly six times longer than estimated --
~44 cipher lines across three page-sides (folio 20 recto tail, folio 20 verso, folio 21 recto),
not ~8-9 lines on one leaf -- and is a symbol/glyph substitution alphabet, not the numeral-group
cipher the check-solved sweep's low-resolution thumbnail suggested. Given that six-fold scope
change and the session's cost cap, a genuine second independent pass over the full ~500-token
extent was not attempted. What is in ciphertext.txt is a SINGLE careful reading of only the
originally-scoped portion (the recto's own cipher tail, 9 lines, 86 tokens by this reading).

## Evidence that this single pass has not converged

The 86 tokens transcribed contain zero repeats -- no token-string occurs twice. For ~86 tokens of
enciphered French prose (rows 4-11 read as continuous narrative text, not a list of distinct
names or numbers), some repetition of common short words (et, de, la, que, ...) would ordinarily
be expected once a transcription is stable and self-consistent. Zero repeats across this many
tokens is itself diagnostic: it means the same underlying glyph is most likely being rendered
with a slightly different code in different places (a stroke read as "τ" in one spot and "τ'" or
"δ" in another, a "Δ" vs "Λ" inconsistency, etc.), i.e. this transcription has not yet reached the
self-consistency a real second pass (or a first pass re-checked against itself token-by-token
with a fixed glyph inventory decided in advance, ideally with an OCR-assisted tool rather than
prose description) would produce. This is flagged rather than hidden, per rule 4 (grade every
token; M throughout, none escalated to S or higher) and rule 7 (a reproducible reading needs a
script or a second reader to regenerate it; neither exists yet for this file).

## What a genuine second pass needs to do

1. Fix the glyph inventory FIRST, from clean single-glyph exemplars (e.g. crop each distinct
   shape once, in isolation, and agree a code), rather than assigning codes ad hoc while reading
   running text -- the likely source of this pass's self-consistency problem.
2. Re-read every row against that fixed inventory, independently of this pass's specific choices
   (do not read this file's tokens as a starting point; read the crops).
3. Do the same for the verso (folio 20v, images/crops/f24_folio20v_top_L.jpg /
   _top_R.jpg / _bot_L.jpg / _bot_R.jpg) and folio 21 recto (images/crops/f24_folio21r_*.jpg),
   which are not transcribed at all yet -- crops are saved and native-resolution page images are
   in images/img/ (btv1b10036146c_f24_folio20r_full.jpg covers both).
4. Reconcile the two readings row by row, as the brief originally asked, and only then compute
   token count / distinct tokens / length distribution / repeats as a claim rather than a
   provisional single-pass count.
5. Check token-for-token against Nicolas Raince's published 1526 key (Tomokiyo, francis.htm, BnF
   fr.2984 -- see NOTES.md "Key-family leads") once a stable glyph inventory exists; that
   comparison is not meaningful against an unstable single pass.

## Crops produced this session

`images/crops/f23_folio20r_cipherblock_{L,R}.jpg` -- the recto's cipher tail (transcribed above).
`images/crops/f24_folio20v_{top,bot}_{L,R}.jpg` -- the verso, full cipher run + 2 plain
paragraphs (not transcribed).
`images/crops/f24_folio21r_{top,bot}_{L,R}.jpg` -- folio 21 recto, cipher run + plain closing +
date + signature (not transcribed).
All are native-resolution JPEG crops under 2400 px wide, cut from the two full-page IIIF fetches
in `images/img/` (btv1b10036146c_f23_folio20r_full.jpg, 8315x6214; btv1b10036146c_f24_folio20r_full.jpg,
8299x6214, which is actually [folio 20 verso | folio 21 recto] as one photographed opening).
Folder size check: `du -sh images/` well under the 30 MB cap (see report).
