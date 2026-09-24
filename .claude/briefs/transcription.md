# Transcription (Fable for reconciliation, Sonnet passes, cap $30)
Read CLAUDE.md (rules 2, 7, Usage 4 and 6). Target: <folder>. Fetch images once to images/ with
manifest.json. Two independent passes by Sonnet subagents from the images, never from an existing
transcription; reconcile row by row against the image; a third pass only where the two disagree on more than
a tenth of rows. Output ciphertext.txt in the repo's group format and a reconciliation log. + common tail.
Symbol alphabets (RETRO-2026-09-24 proposal 4, applied in part): on a page of invented signs, segment the glyphs
from the images and cluster them by shape into one shared atlas first (see ciphers/dupuy452-carpi-1520/glyphs/),
then give both passes the atlas's codes; two passes that each invent their own code book cannot be reconciled
row by row (Raince, 23-24 Sept: 124 codes against 25). Report token count and type count against any gate the
orchestrator names in the brief; if it fails, say so in NOTES.md and stop rather than start another full pass.
