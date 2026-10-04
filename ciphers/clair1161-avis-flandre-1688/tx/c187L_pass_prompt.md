You are one blind transcriber of a 16th-century French pen-sign cipher leaf. Work alone; do not open any other file in the repository than the ones named here.

1. Read the label set: /home/user/cipher-lab/ciphers/clair1161-avis-flandre-1688/tx/labels_v2.md. Use ONLY these labels (plus `s` = a small plain s, `ss` = two small s written together, `/` = light diagonal slash). If a sign fits none, write `NEW:<short description>` -- never force it into an existing label.
2. Crops, in /home/user/cipher-lab/ciphers/clair1161-avis-flandre-1688/images/ : c187L_L02_s1.jpg, c187L_L02_s2.jpg, ... through c187L_L27_s1.jpg, c187L_L27_s2.jpg (26 lines x 2 segments; L01 is a clear heading "Autres advis": skip it). View every crop with the Read tool, one at a time.
   - Each crop shows ONE target line: the largest, fully visible line of signs. Fragments of the line above (cut at the top edge) or the line below (cut at the bottom edge) are NOT part of it -- ignore them.
   - s1 is the left part of the line and s2 the right part. The last ~150 px of s1 are the same ink as the first ~150 px of s2 (about 1-3 signs). Read s1 completely, then continue in s2 AFTER the signs you already wrote from s1; do not write the overlapped signs twice.
   - Long descenders: check whether a bowl's descender is long (q), long and crossed by a bar (qb) or short (9); look at the bottom of the crop.
   - Clear French words written in ordinary script among the cipher (e.g. a word like "pour"): write each as PLAIN:word (use ? for unread letters). A large decorative initial letter: PLAIN:<letter>.
   - Append `?` to any sign you are unsure of (e.g. `qb?`).
3. Write your result to OUTFILE as a tab-separated file: first line `row<TAB>codes`, then one line per manuscript line: `L02<TAB>sign sign sign ...` (signs separated by single spaces, left to right), through L27. Every line L02-L27 must be present.
4. Reply with only: the file path, the number of lines, the total number of signs, and any NEW: labels you used with the line where each occurs.
