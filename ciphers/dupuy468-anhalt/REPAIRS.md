status: partial

# Proposed repairs to ciphertext.txt (not applied)

Rule: "ciphertext.txt (as transcribed, never silently repaired)" (CLAUDE.md, Layout). This file records a
transcription correction the solver believes is right, without editing ciphertext.txt itself. Written 23
September 2026 by the ASSIGNMENTS row 25 worker, following the second, adversarial audit's finding (AUDIT.md,
"Second, adversarial audit", corrections item 2), not by decoding.

## r22, token 1 ([PLAIN:palatinus])

**Transcribed as:** `palatinus` (a clear Latin word, not a cipher token; ciphertext.txt line r22, `[PLAIN:palatinus]`).

**Proposed repair:** `paulatim` ("peu à peu" -- little by little).

**Basis.** The letter's plaintext is printed in Deutsche Reichstagsakten, Jüngere Reihe II (Wrede 1896),
Beilagen zur Einleitung IV no. 1, p. 122, in a contemporary French translation (AUDIT.md, "Second, adversarial
audit"). At the point corresponding to reading.txt r22, the French reads "Puys l'on pourra **peu à peu**
traicter avec ceulx qui n'ont encores specialle alliance..." -- "then one may gradually deal with those who do
not yet have a special alliance...". There is no Count Palatine (*comes palatinus*, or similarly a bare
*palatinus* meaning "the Palatine") anywhere else in the letter or in the printed French, and no Rhenish or
other Palatine elector is named among the princes gathered at Zerbst (Saxony, Brandenburg, Lüneburg,
Mecklenburg). *Paulatim* is a common classical adverb and fits both the French translation and the sentence's
grammar ("Deinde potest [paulatim] tractari cum his qui non dum habent speciale fedus..." -- "then [little by
little] one may deal with those who do not yet have a special alliance..."), where "palatinus" as a bare
adjective/noun has no clear grammatical role in the sentence as transcribed.

**Why this is a repair proposal, not an applied fix.** The word was read from the image as a clear (non-cipher)
Latin word, not decoded from a key -- rule 2 ("Image over transcription") and the ciphertext.txt convention
("never silently repaired") both apply. *Palatinus* and *paulatim* differ by two letters in an 8-9 letter word,
which is plausible either as a transcription misreading of a clear secretary hand or, less probably, as the
17th-century-or-earlier scribe's own slip; neither has been checked against the image at native resolution
since the second audit's finding (AUDIT.md: "The line should be re-read on the image (canvas 63, r22). This
session does not edit reading.txt or ciphertext.txt (no decoding)."). This worker (ASSIGNMENTS row 25) did not
fetch or re-view the image either -- no network beyond git was in its brief.

**What would apply it.** A worker with image access should re-crop and re-read canvas 63 at r22 at native
resolution, confirm *paulatim* against the letterforms, and only then edit ciphertext.txt's `[PLAIN:palatinus]`
to `[PLAIN:paulatim]` with a NOTES.md note of the correction and the re-read image reference. Until then,
reading.txt and NOTES.md's paraphrase keep the transcribed "palatinus", flagged as probably wrong (already
noted at reading.txt's paraphrase and in AUDIT.md).

**Grade impact if applied.** `[PLAIN:palatinus]`/`[PLAIN:paulatim]` is a clear word, not a cipher token, so it
is outside check.py's grading (rule 4 grades cipher tokens only; NOTES.md's grading table already excludes the
242 clear words). Applying this repair would not change any H/S/M/unread count.
