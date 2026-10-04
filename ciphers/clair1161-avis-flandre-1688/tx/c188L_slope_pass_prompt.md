You are one blind transcriber of a 16th-century French pen-sign cipher leaf. Work alone; do not open any other file in the repository than the ones named here.

1. Read the label set: /home/user/cipher-lab/ciphers/clair1161-avis-flandre-1688/tx/labels_v2.md. Use ONLY these labels (plus `s` = a small plain s, `ss` = two small s written together, `/` = light diagonal slash). If a sign fits none, write `NEW:<short description>` -- never force it into an existing label.
2. Crops, in /home/user/cipher-lab/ciphers/clair1161-avis-flandre-1688/images/ : c188L_L01_s1.jpg, c188L_L01_s2.jpg, c188L_L01_s3.jpg, ... through c188L_L27_s3.jpg (27 lines x 3 segments, all cipher). These crops FOLLOW the slope of each line, so each crop holds one line. View every crop with the Read tool, one at a time, ORDER as given below.
   - Each crop shows ONE target line: the largest, fully visible line of signs. Fragments of the line above or below at the crop edges are NOT part of it -- ignore them.
   - s1 is the left third, s2 the middle, s3 the right part. Each segment overlaps the next by ~150 px (about 1-3 signs) at its left edge. Read s1 completely, then continue in s2 AFTER the signs you already wrote, then s3; do not write the overlapped signs twice.
   - Long descenders: check whether a bowl's descender is long (q), long and crossed by a bar (qb) or short (9); look at the bottom of the crop.
   - Barred stroke groups: count the strokes (3 = iii, 2 = iib). A barred z with a small raised loop on top: write it as `tz` if the loop is there, `z` if not.
   - Clear French words written in ordinary script among the cipher: write each as PLAIN:word (use ? for unread letters).
   - Append `?` to any sign you are unsure of (e.g. `qb?`).
3. Write your result to OUTFILE as a tab-separated file: first line `row<TAB>codes`, then one line per manuscript line: `L01<TAB>sign sign sign ...` (signs separated by single spaces, left to right), through L27. Every line L01-L27 must be present.
4. Reply with only: the file path, the number of lines, the total number of signs, and any NEW: labels you used with the line where each occurs.
