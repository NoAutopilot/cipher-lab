# Blind transcription pass, BnF fr.2980 f.30r-v (cipher letter, 1530)

You transcribe invented cipher signs from images into codes. You do not decode; there is no plaintext to find.

Files (all in this folder):
- atlas_f29.png: the shared atlas. Each row = one code (left) with up to 3 exemplars cut from the same scribe's f.29r.
- atlas_f30add.png: extra codes for shapes that occur on f.30 (FL, HASH, BOX, ss2 arch, INF, TRI, QQ, ST, A2, CROSS, Rt).
- sheet01.jpg ... sheet19.jpg: each sheet has 6 rows; each row is labelled on the left (e.g. f30r_L01a). Every
  manuscript line is split into an 'a' (left) and 'b' (right) row that do not overlap. Other lines' ascenders and
  descenders intrude at the top and bottom of a row; transcribe only the signs sitting on the row's own middle line.

Rules:
1. Read each row left to right and write one code per sign, separated by single spaces, using ONLY codes from the two
   atlas images. Codes are case-sensitive (e.g. 'H' and 'h' differ, 'T' and 'Tb', 'g' and 'g2' and '9' and 'q').
2. A sign you cannot match to any atlas code: write NEW:<3-6 word shape description>, e.g. NEW:circle-with-cross.
3. A sign you can see but whose identity you doubt: append '?' to your best code, e.g. 'g?'.
4. A free-standing small dot between signs: write '.'. Ignore flourishes/underlines that are parts of signs.
5. Two long strokes joined at the top like an arch is ss2. Two SEPARATE long strokes side by side are 'sl sl'.
6. Do not skip signs and do not guess from context: you are recording shapes only.
7. Output: a TSV file with header 'row<TAB>codes' and one line per row id (f30r_L01a ... f30v_L20b), 110 rows.
Zoom: open each sheet image with the Read tool; if a row is hard, re-read that sheet and look again.
