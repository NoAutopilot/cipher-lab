# Transcription (Fable for reconciliation, Sonnet passes, cap $30)
Read CLAUDE.md (rules 2, 7, Usage 4 and 6). Target: <folder>. Fetch images once to images/ with
manifest.json. Two independent passes by Sonnet subagents from the images, never from an existing
transcription; reconcile row by row against the image; a third pass only where the two disagree on more than
a tenth of rows. Output ciphertext.txt in the repo's group format and a reconciliation log. + common tail.
Commit and push after each pass lands (passA.tsv, then passB.tsv, then any atlas file), not once at the end --
every F row in RETRO-2026-09-24b's window lost at least one already-finished pass to an interruption at cap
because nothing was pushed until reconciliation. Use `tools/iiif_lines.py` to cut crops and
`tools/reconcile_passes.py passA.tsv passB.tsv --crops <crop dir>` to reconcile once both passes exist, rather
than an Opus reconciler reasoning over the whole leaf in one sitting: a scripted reconciler cannot silently run
past a dollar cap the way an Opus reconciler did twice in that window (line 96, $15.30 against a stated cap of
about $10-12; line 99, $35.50 against $25) -- Opus's own F-row cost that window is 44% of all Opus spend, and
every F row in the bucket shares the same shape (ran past cap mid-job, partial or no commit).
Symbol alphabets (RETRO-2026-09-24 proposal 4, applied in part): on a page of invented signs, segment the glyphs
from the images and cluster them by shape into one shared atlas first (see ciphers/dupuy452-carpi-1520/glyphs/),
then give both passes the atlas's codes; two passes that each invent their own code book cannot be reconciled
row by row (Raince, 23-24 Sept: 124 codes against 25). Report token count and type count against any gate the
orchestrator names in the brief; if it fails, say so in NOTES.md and stop rather than start another full pass.
Scripts (24 Sept 2026; CLAUDE.md Usage 8): find the leaf with `tools/gallica_folio.py ARK --folio N` (use the label;
it reports offset changes), cut crops with `tools/iiif_lines.py` and check its `--debug` overlay before the passes
start, and reconcile from `tools/reconcile_passes.py passA.tsv passB.tsv --crops <crop dir>`: settle only the rows
of disagreements.tsv from the image, then write ciphertext.tsv from ciphertext_draft.tsv. Do not write a new
crop.py or reconcile.py; add an option to the tool if it lacks one.
