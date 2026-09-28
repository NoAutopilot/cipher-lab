# Desk pack for ASKS row 88 (campaign fr4715-f61-mayenne-1592, H50/H60, 28 Sept 2026)

What is asked: read the small clear words written ABOVE the cipher signs on three rows of BnF fr.3983 f.108r (Mayenne to
de Diou, 1593), rows L04, L05 and L06 -- about 25 words in all. Model readers score 11/32 exact words on the two rows whose
gloss is already known (H34), so a person's reading is the instrument. Ten minutes at the Gallica viewer
(https://gallica.bnf.fr/ark:/12148/btv1b9059406b/f195.item, full zoom; the block starts a third down the page, row L03 is
the clear line "Et pour cela je vous laisse a juger quel contentement je doibs auoir") or on the contact sheets here.

Sheets: `f108r_L01.jpg` (a worked example: its gloss is "satisfaire ung seul au preiudice de plusieurs"), `f108r_L04.jpg`,
`f108r_L05.jpg`, `f108r_L06.jpg` (this last row is cut through its lower half by the scan region; its gloss is whole).
Each sheet stacks the row's four crops; the blue numbers under each crop are the cipher signs in order (pass A's numbering),
and `PLAIN` marks a clear word written inside the row itself (not a gloss word).

How to answer -- write one row per gloss word into `ciphers/fr4715-f61-mayenne-1592/scripts/gloss108_person.tsv`, tab-separated,
header exactly as below; `first_sign`/`last_sign` are the blue numbers the word sits above (its left and right ends); a
stroke with no letters is a `-` row; an illegible word is `?` with any letters you can make out; keep 16th-century spelling
as written (no modernising), abbreviations expanded in square brackets, e.g. `Mons[ieu]r`.

    line	word	first_sign	last_sign	note
    L04	La	1	2	
    L04	misere	3	7	
    L04	-	8	9	a dash, no letters

Then push, or paste the rows into ASKS.md row 88. The runner does the rest (CAMPAIGN.md row H50: `scripts/f61gloss.py
--tag h50`, the same x-placement scorer as H34). Nothing here asks for a reading of the cipher itself.
