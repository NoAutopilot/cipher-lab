# H13: dots and colons attached to numeral groups (28 Sept 2026, campaign runner account 2)

Method: every cipher line band of both canvases (manifest bands, r_n = band n+1) thresholded, connected components
labelled (scipy.ndimage), components 6-90 px in area and at most 16 px square inside the band's text zone kept
(237), then re-measured at a darker threshold for roundness, with ink to the left within 55 px and blank to the
right for 18 px, margins excluded (50). The 50 were checked by eye on contact sheets; `marks.tsv` lists the 16
marks after cipher groups that are real (15 dots, 1 colon; one r06 dot after 8 before 5 could not be resolved to a
position and is left out), `verified_marks_*.jpg` shows them plus the three plain-text full stops that precede a
cipher run (r08 "materia.", r13 "della.", v11 "tiempo."). The detector missed the r16:10 dot both blind reads saw
in H10/H11 (added by hand): its recall is not complete, so the count is a floor.
