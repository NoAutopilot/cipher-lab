# f.130r word-level reading from the repaired key (A2-DIN3, 3 Oct 2026)

Letters: `reading.txt` / `reading_decode_key.txt` in this folder (repaired key `key_repaired.tsv`), graded per token in
`tokens.tsv` / `reading_tokens.tsv` (decode_key.py, 527 cipher tokens: C 329, S 71, M 127, U 0, no H). Word divisions
below are my segmentation of those letter runs (the cipher has no word divider), so every word here is at best the grade
of its weakest letter and the division itself is an inference. `(..)` = a letter I would change to make the word (grade
I, not applied to the key); `...` = a stretch I cannot divide; `[..]` = clear words on the leaf. Only stretches where a
division is reasonably secure are glossed. This is a cryptanalytic result (period key from a sibling leaf, repaired by
hill-climb with a shuffled-key control), not a reading from a key source.

| line | segmentation (letters as decoded) | gist |
|---|---|---|
| L02 | ... qui m'a ... (d)esir enuoier a ... [bonne fortune] | "who ... desire to send ... good fortune" (weak) |
| L03 | [aussi si vous plaist Monseigneur que] ... (d)emeure seul ... aue(c) les habi(t)ans ... [que larmee Lorraine] | "remains alone ... with the inhabitants" |
| L04 | [se fortifie et a qui estoit du costé de Strasbourg] ... il me s'er... ... de (c) | (not divided) |
| L05 | (c)onseruer des ... en l'obeissan(c)e ... [Messieurs de la ville] | "to keep ... in obedience ... [the gentlemen of the town]" |
| L07 | nos ont ... oultre le ... il ne se leuer a ... | "beyond the ... he will not rise/raise ..." (weak) |
| L08 | ... d'aultre ... de dans se bien bas ... qu'il ne ... plus ... | "from inside ... very low ... that he no longer ..." |
| L09 | dehors les ... seruiront ... tant ... leur ... que a la ... | "outside, the ... will serve ... their ..." |
| L10 | la uille et le roi ... | "the town and the king ..." |
| L11 | (p)ourvoir de ... retirer d'aultant qu'il i a ... l'honneur [pour luy] | "to provide for ... withdraw, inasmuch as there is ... the honour [for him]" |

Signs whose repaired or held value these words contradict (not changed here, by the pre-registered held-out rule):
h reads u in the key (one f.128 gloss occurrence) but "pourvoir" (L11 opening) wants p (the climb chose l, which the f.128
gloss rejected); D reads a (f.128 gloss a:2 g:1 t:1) but "auec", "obeissance",
"conseruer" want c and "demeure" wants d.
