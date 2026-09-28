# Desk pack for ASKS row 92 (campaign armstrong-madison-1808, H59, 28 Sept 2026)

What is asked: label the shorthand signs on four lines of Armstrong to Madison, Paris, 20 February 1808 (NARA RG 59 M34
roll 14 frames 0030-0031), by shape only, against Satoshi Tomokiyo's 38-type sheet (`tomokiyo_38_types.png`). Two
model readers could not agree on these types (B35: 80 percent disagreement; H54: no smaller sign list fixes it; H55: a
reader disagrees with itself on the same line), so a person's labels are the known answer every further glyph test
needs. Nothing here asks for a reading of the cipher; three of the four lines are enough.

Sheets: `S1a`/`S1b` .. `S4a`/`S4b` -- each line at 2x in two overlapping halves, with a blue ruler under it (the numbers
are the position in the original crop, every 50 px). `sheets.tsv` names the source crop of each line.

How to answer -- one row per sign, left to right, into `ciphers/armstrong-madison-1808/h59/person_labels.tsv`,
tab-separated, header exactly as below: `x` is the ruler number nearest the sign's LEFT edge; `type` is the number of
the closest shape on Tomokiyo's sheet, or `?` if none fits (describe it in `note`); a numeral group on the line is one
row with type `digits` and the number in `note`; a dot or tick that belongs to the sign before it goes in that sign's
`note`, not its own row.

    sheet	x	type	note
    S3	235	?	short horizontal bar
    S3	320	20	
    S3	1000	digits	13

Then push, or paste the rows into ASKS.md row 92.
