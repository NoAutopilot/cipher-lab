# PREREG-ECK62-QP (AM-ECK62Q, 7 Oct 2026, written and pushed before any image is fetched or looked at)

Target: the 25 mssEC 18 entries decided `?p` by print_q under split2 (`s2/print_q.tsv`, decision `?p`: a dated OR match exists
under both books but the 5-gram margin is < 2), all with zero marker words in the volunteer transcription (`book()` = '?').
Question: does the page image carry a book marker the volunteer text dropped or normalised?

Instrument: the Huntington IIIF page image (`hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/<w>,/0/default.jpg`),
cropped with `tools/iiif_lines.py --image FILE --out DIR` (command pasted in NOTES.md); one eye (this worker), crop by crop.

1. Marker, as `ec18.book()` defines it: a legible word of N1 {unity, zebra, zodiac, walrus, webster, yoke, youth} or N2 {tulip,
   pike, yacht, yawl, yard, yardstick} written inside the entry's own block (from its heading to the next heading), absent from
   the volunteer transcription; or a written book annotation in or beside the block ("No 1", "No 2", "No 3", "Cipher No n").
   Illegible or doubtful readings do not count. A clear-text word ("period", "sig") is not a marker.
2. Move: an entry moves from '?' to book k only if it shows >= 1 marker of set k (or annotation k) and none of the other set.
   Grade of the move: S (image marker, the same rule as the marker-known class whose known-answer precision is 0.948,
   print_q_summary.tsv). A move is a decision about the book only; no reading or key.md row changes in this job.
3. Control (rule 3, same eye, same crops, same look): 8 marker-known entries that sit on the same page images as `?p` entries,
   chosen before any image is seen -- book 1: 9676.22, 9731.91, 9735.98, 9980.557b; book 2: 9672.12, 9764.138, 9873.340,
   9962.534. Statistics: (a) recall = marker tokens of the transcription found legibly on the image / marker tokens in the
   transcription, gate >= 0.80; (b) cross-set false markers reported on the control entries, gate = 0. The control can fail
   on both: the hand may be too faint at the crop resolution (a), and the eye may misread a word as a marker (b).
   Disclosed limit: the control is not blind -- the worker printed the control entries' marker lists before writing this
   file. It measures legibility of marker words at this crop resolution and the eye's cross-set error, not blind recall.
4. Gate: if (a) < 0.80 or (b) > 0, no target entry is moved; the result is logged "untested-by-this-tool at this resolution".
   If the gate passes and 0 target entries show a marker, the result is logged as a search result (image checked, no marker
   dropped by the volunteer text), never as a book decision.
5. Units: one crop look per entry; stop before 80% of cap 4.5 or of the box (10:19-11:19 UTC, stop line 11:07). Entries not
   looked at by the stop line are listed as not attempted.
