# MONL-C268B blind transcription prompt (14 Oct 2026). One call per line per pass; {LINE} = c268 L06-L10, {N} = crop band 1-5.

You are transcribing ONE line of a 16th-century symbol cipher, sign by sign, against a numbered reference sheet. You are
not told what any sign means and must not guess meanings; only match shapes to sheet ids.

Files (read each with the Read tool):
- Reference sheet: /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/images/keysheet_monluc1_ids.png
  (68 cells K01-K68, each a sign shape with its id in the corner; a thick black bar at a cell's left edge is a sheet artefact).
- Segment 1 (left part of the line): /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/images/scratch268b/crops/c268b_L0{N}_s1.jpg
- Segment 2 (right part of the line): /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/images/scratch268b/crops/c268b_L0{N}_s2.jpg

The two segments OVERLAP: segment 2 starts 300 px before segment 1 ends (each is 1700 px wide), so the signs in the rightmost
~300 px of segment 1 appear again at the left edge of segment 2. Transcribe segment 1 fully, then continue with segment 2 from
the first sign that is NOT already in segment 1. Each crop may show fragments of the lines above and below at its top and
bottom edges: transcribe only the central line, the one running through the middle of the crop.

Conventions:
- each sign = its sheet id (K01 ... K68), choosing the closest shape; the hand is looser than the sheet;
- a double oblique stroke '//' = ?double_slash; an 'h' with a crossbar on its stem = ?h_bar;
- a sign matching no cell = ?x[short description], e.g. ?x[looped q];
- a run of ordinary Latin-script letters forming a word written in clear inside the cipher = W:word (as spelled, e.g. W:abc);
- do not skip signs; do not add signs for flourishes or tails that belong to a neighbour.

Answer with exactly three lines and nothing else:
LINE {LINE}: <space-separated tokens, left to right, segment 1 then the new part of segment 2>
SKIPPED_OVERLAP: <how many signs at the left of segment 2 you skipped as already in segment 1>
UNSURE: <comma-separated 1-based positions in your token list you are least sure of, or none>
