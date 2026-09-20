# Transcription (Fable for reconciliation, Sonnet passes, cap $30)
Read CLAUDE.md (rules 2, 7, Usage 4 and 6). Target: <folder>. Fetch images once to images/ with
manifest.json. Two independent passes by Sonnet subagents from the images, never from an existing
transcription; reconcile row by row against the image; a third pass only where the two disagree on more than
a tenth of rows. Output ciphertext.txt in the repo's group format and a reconciliation log. + common tail.
