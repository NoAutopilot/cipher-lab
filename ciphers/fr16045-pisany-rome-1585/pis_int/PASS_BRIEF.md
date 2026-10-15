# Blind interlinear-gloss pass, fr16045 canvas 252 (PIS-INT, 15 Oct 2026)

You are one of two independent readers. Do not read any file in ciphers/fr16045-pisany-rome-1585 except the two named here;
never read key.tsv, key86.tsv, any reading, decode, NOTES or gloss file (this pass is value-blind and key-blind).

Inputs:
- Reference sheet: ciphers/fr16045-pisany-rome-1585/tx/SIGNSHEET.png (cells S01-S67) and tx/SIGNS.md. S07 = S04, S08 = S05: use S04 / S05.
- Six crops <CROPDIR>/pair_A.jpg ... pair_F.jpg. Each shows a line of a 1585 French letter that mixes plain handwriting with cipher signs, and
  one or more SMALL glosses written in a later/smaller hand squeezed ABOVE a run of cipher signs (an interlinear decipherment).

Task, for each crop A..F, for EACH small interlinear gloss in it:
1. Read the gloss letter by letter as written (French, 16th-c. hand; keep abbreviations as written; an unreadable letter = '?').
2. Identify the run of cipher signs that the gloss sits over (from the first cipher sign under its start to the last under its end;
   stop at plain handwriting on either side) and transcribe it left to right with the closest Sxx label; unsure: best label + '?' (S41?);
   no match: ?[shape]. Prefer compound labels (S25, S26, S57, S59-S67) when strokes sit together as in the cell.
Read one crop per Read call, write its rows before opening the next crop; never open the full page.

Output: one TSV file (path given in your instructions), header `crop	gloss_no	gloss	group	note`, one row per gloss (gloss_no 1,2 left to right),
note = short (e.g. "gloss cut at crop edge", "group extent unsure"). A crop with no gloss: one row with gloss '-' and group '-'.
Reply only: the file path, the number of rows, and the two rows you are least sure of.
