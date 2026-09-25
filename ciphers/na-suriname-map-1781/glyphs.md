# Glyph atlas, NA 4.VEL Suriname fortification-survey cipher (Wollant, 1781)

RD03, 25 Sept 2026. Built from three independent transcription passes: this worker's own pixel-level reading
of 2007A's title block (images/2007a_titletext.jpg) and "Remarque" heading (images/2007a_aanmerkinge.jpg),
cross-checked against 2007B's plain twin title (images/2007b_title_crop.jpg); a Sonnet subagent's independent
blind reading of the same three 2007A crops (titletext, nota, aanmerkinge); a second Sonnet subagent's
independent blind reading of 2061's title/battery-header block (images/2061_title_gloss.jpg,
images/2061_title_topleft.jpg). See key.tsv for the 13 signs that reached grade C, conflicts.tsv for every
place two passes disagreed.

The system (evidence so far): a **homophonic monoalphabetic substitution** over Dutch. Several frequent
letters (N, E, A confirmed) each have two or more distinct cipher signs. The sign set mixes Latin-letter-
shaped glyphs (drawn in an elaborate chancery display script for titles, a plainer running hand elsewhere),
digits used as letters (5, 7 confirmed), and invented shapes (a reversed/mirrored-3 "ezh" often carrying a
dot, a closed-triangle "delta", a "hash/ladder" mark noted by one reader in the nota/aanmerkinge captions but
not yet tied to a letter). Place-name and province/bastion labels (Paramaribo, Bastion Holland, Bastion
Gelderland, Redout Purmerent, Redout Leyden, ...) are left in plain Dutch throughout on every sheet checked;
only the descriptive/explanatory clauses are enciphered. This matches the design LESSONS.md calls the
genuinely-breakable kind (a short homophonic system, not a large nomenclator) IF enough labelled crib material
exists to pin every sign -- which this pass only partly achieves (13 of a needed ~20+ signs).

## Confirmed signs (key.tsv -- >=2 independent passes/sheets agree, position unambiguous)

| sign (code) | shape | value | occurrences |
|---|---|---|---|
| `[h-loop]` | lowercase h, looped ascender | n | 2007A Generaal/Plan/Defensie (2 readers) + 2061 Plan -- most robust sign found |
| `[l-bare]` | bare vertical stroke, no crossbar | n | 2007A van + 2061 en (2nd N homophone, 2 sheets) |
| `c` | plain lowercase c | l | 2007A Plan (1 of 2 readers; other called it e-shaped) + 2061 Plan |
| `[delta]` | hollow wedge/closed triangle, no crossbar | a | 2007A van + 2061 van/Plan + 2007A Remarque (4 word-instances, 3 crops, 2 readers) -- 2nd most robust |
| `5` | digit 5 | v | 2007A van + 2061 van (2 sheets); one conflicting instance elsewhere not trusted, see conflicts.tsv |
| `7` | digit 7 | e | 2007A Defensie + 2061 de (2nd E homophone, 2 sheets) |
| `[s-loop]` | S/s chancery loop | p | 2007A Plan + 2061 Plan (2 sheets) |
| `G` | capital G, Latin-shaped | g | 2007A Generaal (2 readers, 1 sheet) |
| `[ezh-dot]` | reversed-3/ezh shape, usually with a dot | e | 2007A Generaal + Defensie (2 readers) + Remarque (3rd E homophone) |
| `[o-plain]` | plain circular o | r | 2007A Generaal (2 readers, 1 word-instance) |
| `[a-plain]` | plain round-bowl a, no accent | e | 2007A Generaal (4th E homophone; 2 readers, 1 word-instance, lower confidence) |
| `[v-tall]` | tall looped V/J ascender (title-cartouche scale) | d | 2007A Defensie (2 readers); tentatively merged with 2061's plain-v "de" instance, see conflicts.tsv |
| `y` | plain lowercase y | s | 2007A Defensie (2 readers, 1 word-instance) |
| `[hash]` | invented 2-3-stroke "ladder"/tally mark | o | RD03B 25 Sept: the word directly below the plain "Nota" heading is itself an enciphered echo of "NOTA" (same self-duplicating-heading pattern as "Remarque", see below) -- 2 independent readers (this worker + a subagent), rule-7 fresh re-derivation agrees |
| `λ` | open/hooked stroke (previously the unresolved "lambda" candidate in conflicts.tsv, now resolved as a sign DISTINCT from `[delta]`) | t | RD03B 25 Sept: same NOTA self-echo, AND independently in "Signatuure" (Remarque paragraph) at the position flanked by already-confirmed N and A with no compression needed -- 2 independent word-contexts, 2 independent readers, rule-7 fresh re-derivation agrees |

E now has four candidate signs (7, [ezh-dot], [a-plain], and a disputed [3-caret] from 2061 not carried into
key.tsv) -- plausible for the most frequent Dutch vowel, but only the two cross-sheet ones (7, [ezh-dot]) are
on strong footing; [a-plain] rests on one word read twice by the same... no, two different readers, but only
one word-instance.

## Unresolved / rejected candidates

See conflicts.tsv for the full row-by-row log. Summary: `[x-dot]` and `[g-loop]` (Generaal's disputed
AA-compression, positions 6-7) are NOT in the key; `[defensie-i-cand]`/`[defensie-e-cand]` (Defensie's last
two positions) are NOT in the key; five of Remarque's eight positions are NOT in the key
(`[remarque-r1-cand]`, `[remarque-m-cand]`, `[remarque-r2-cand]`, `[remarque-q-cand]`, `[remarque-u-cand]`,
`[remarque-e2-cand]`); `[v-plain]` (2061's "de" D-position) is cited as probably the same sign as `[v-tall]`
but not merged outright.

**Update after the rule-7 fresh-instance re-derivation (NOTES.md "Reading"):** a fourth, independent pass
(given only glyph codes + gloss words + images, not this file or key.tsv) reproduced all 13 confirmed signs
above at 100% agreement with zero contradictions, and independently reached the same AA-compression and
F-drop hypotheses used here. It additionally proposed values for the still-unkeyed candidates, all consistent
with this worker's own working hypotheses (not contradicting anything in the confirmed table), but each still
resting on one word-instance only, so kept OUT of key.tsv:
`[x-dot]`->a (its own confidence: low-medium, "could be a doubling mark rather than literally A"),
`[g-loop]`->l (medium-high), `y`->s (medium, matches key.tsv's own `y`->s exactly),
`[defensie-i-cand]`->i (medium-high), `[defensie-e-cand]`->e (medium-high),
`[remarque-r1-cand]`->r, `[remarque-m-cand]`->m, `[remarque-r2-cand]`->r (2nd R homophone),
`[remarque-q-cand]`->q, `[remarque-u-cand]`->u, `[remarque-e2-cand]`->e (all high confidence, direct 1:1
position in an unambiguous 8-glyph/8-letter word, but still single-instance).

Other shapes seen but not yet tied to any word in the key (noted by the 2007A-pass subagent while reading
nota.jpg/aanmerkinge.jpg, not used here): `[hash]` (an invented two-or-three-stroke "ladder"/tally mark,
recurs often), `ÿ` (y with two dots), `Ö` (O with two dots), `[2dot]` (a floating two-dot mark, possibly a
diacritic rather than its own letter), `λ` (an open/hooked stroke the same reader thought might be a second
form of `[delta]`), `d~` (a "d" with an elaborate looping tail, seen word-finally).

## RD03B, 25 Sept 2026: two more signs, from the Nota-heading self-echo and "Signatuure"

`[hash]`=o and `λ`=t were added from (a) the cipher word directly below the plain "Nota" heading on 2007A,
which independent readers agree is itself an enciphered echo of "NOTA" (the same self-duplicating-heading
pattern already established for "Remarque" -- see the Remarque row above and NOTES.md), and (b) the word
"Signatuure" in the Remarque paragraph's second gloss line, where the flanking positions land exactly on the
already-confirmed `[h-loop]`(N) and `[delta]`(A) with no compression needed, independently forcing `λ`=T a
second time. Both signs passed a rule-7 fresh-instance re-derivation (a subagent given only the glyph codes,
the two target words, and the three anchor values, not this file or key.tsv) at 100% agreement. That same
re-derivation also surfaced a genuine unresolved contradiction, not asserted anywhere in key.tsv: the code `з`
(used by the Remarque-pass transcriber for a reversed-3/z-like shape, tentatively distinct from `[ezh-dot]`)
is forced to two different letters (U and E) at two positions within "Signatuure" alone -- almost certainly a
transcription/segmentation slip (two similar shapes conflated under one code, or the doubled "UU" handled by
one glyph rather than two), not evidence that a single glyph carries two values. Left unresolved and OUT of
key.tsv; a follow-on worker should re-crop "Signatuure" at high zoom to settle it before trusting `з` for
anything.

## What this key can and cannot do

Fifteen signs confirmed across four independent passes and two sheets (13 from RD03, +2 from RD03B) is real,
controlled evidence (grade C throughout: known plaintext via the on-sheet interlinear gloss on 2007A and
2061, 2007B's twin for 2007A's title, and the "NOTA"/"Signatuure" self-echo and gloss words for the two new
signs). Applied back to its own ten source words it decodes 33 of 52 token positions to grade C (tools/
decode_key.py's output, reading_tokens.tsv) -- a legitimate self-consistency control, though a tautological
one for the words each sign was built from (the key was built from exactly this material); the two new signs'
values were independently re-derived by a fresh instance (rule 7) as an extra check beyond this.

It is still NOT enough coverage for Dutch prose: continuous text needs roughly 20+ distinct letters before
more than scattered fragments decode. 2039, 2046 and 2077 -- the three target sheets with no gloss or twin of
their own -- were NOT transcribed against this key this pass (RD03B); a spot check of 2039's title cartouche
("Specxl [sign]Ah sf[?]r F," / "y[?]lambda wab[?]ge[psi] 6[?][?]v[delta]plmg[?]h [psi]lambda[delta]pr...")
found the new `λ` sign appears once in the second line but the rest of the line's glyphs are either plain
Latin-looking letters not yet matched to a confirmed code at this resolution, or unconfirmed shapes -- still
too sparse for anything beyond a single-sign spot-check, not a reading. See NOTES.md for the honest state of
play and what a follow-on worker should do next.
