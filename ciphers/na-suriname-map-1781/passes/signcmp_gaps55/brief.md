You are looking at 8 small image tiles, T1.jpg to T8.jpg, each cut from handwritten 18th-century sheets (some tiles are
enlarged). Each tile is centred on one handwritten sign; strokes from neighbouring signs (above, below or beside) may
intrude at the edges. Look at each tile carefully at full resolution. Do not guess what the signs mean; describe shapes only.

For each tile report one TSV row:
tile  main_sign_shape (short words)  mark_above (none | dots:<count> | loop | stroke_from_line_above | unclear)  mark_conf (0-1)  notes
"mark_above" is a mark that sits directly above the main sign's body and belongs to it, not a stroke that is part of a
different sign coming down from the line above (call that stroke_from_line_above).
Then one line: groups: which tiles show the same sign (e.g. "T1=T4; others distinct").
Output only the TSV rows and the groups line.
