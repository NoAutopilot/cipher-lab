# UNA-GRAM blind sort prompt (one Sonnet call; R12D-GRAZB2's own prompt text was not saved, so this follows PREREG-R12D-GRAZB.md's
# instrument description word for word: "sort ... into classes (as many as it sees, max 8) by visible stroke features, describe each
# class, mark OFF where the [tile] misses a clear sign")

You are sorting handwritten signs by shape. Read these three image files (and nothing else):
<SHEETS>
Each sheet shows numbered tiles (#N in red). Each tile is meant to hold one handwritten sign from a 16th-century manuscript cipher.
Sort the signs into classes (as many as you see, max 8) by visible stroke features only. Describe each class in one line (its
distinguishing strokes). Mark a tile OFF if it does not hold one clear sign (empty, a fragment, two signs, illegible).
Ignore ink darkness, paper colour and scan quality; sort by the shape of the strokes. There is no right number of classes.
Do not open any other file. Do not guess what the signs mean.
Answer with: the class descriptions (C1 ... C8: description), then one line per tile, "id<TAB>class" (class = C1..C8 or OFF),
for every tile id on the sheets, in numeric order.
