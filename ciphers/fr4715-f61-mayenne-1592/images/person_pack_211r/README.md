# Desk pack for ASKS row 93 (campaign fr4715-f61-mayenne-1592, H96, 28 Sept 2026)

What is asked: read the small clear words written ABOVE the one cipher run of BnF fr.3983 f.211r (Mayenne to de Diou,
"Du camp de Han, ce premier jour d'apvril 1593", line 2, after "arrivee" and before "qui n'y avoit"): about 18 cipher
signs with a sparse period gloss above them (words that look like "forbley", "comm...", "elle", "...se" at a glance --
not read). This run was used in no fit, so a person's reading of its gloss is a held-out period known answer for the
cells our campaign fitted on f.61 and f.108r.

Sheet: `f211r_run.jpg` -- the run at 2x from the native Gallica image, a blue ruler under it (one tick per 100 px of the
sheet, numbered 0, 1, 2 ...). Gallica: https://gallica.bnf.fr/ark:/12148/btv1b9059406b/f362.item at full zoom.

How to answer -- one row per gloss word, and one row per cipher sign, into
`ciphers/fr4715-f61-mayenne-1592/scripts/gloss211r_person.tsv`, tab-separated, header exactly as below; `from_tick` and
`to_tick` are the ruler numbers the word (or sign) spans; kind is `gloss` or `sign`; for a sign, describe its shape in a
few words (no letters needed); keep the gloss spelling as written.

    kind	text	from_tick	to_tick	note
    gloss	forbley	3	8	
    sign	two loops side by side on a stem	4	5	

Then push, or paste the rows into ASKS.md row 93. Nothing here asks for a reading of the cipher itself.


## Added 29 Sept 2026 by the campaign (H315/H316, runner 12) -- a frame to fill, not a reading

Two blind model sign passes agree on 16 of 18 signs (H315). Their positions in ruler ticks (sheet px / 100) and atlas codes (two codes where the
passes differ); a person's sign rows can simply confirm or correct these:

| # | tick | atlas code |
|---|---|---|
| 1 | 2.8 | VBAR_A |
| 2 | 4.4 | SBS |
| 3 | 5.9 | HASH4 |
| 4 | 7.9 | SBS |
| 5 | 9.2 | EBR_B |
| 6 | 10.6 | DBL |
| 7 | 12.2 | 4STEM |
| 8 | 13.9 | SBS |
| 9 | 15.5 | OTHER |
| 10 | 16.7 | OTHER |
| 11 | 18.3 | DBL |
| 12 | 19.9 | DBL |
| 13 | 21.1 | EBR_A / EBR_B |
| 14 | 22.3 | EBR_B |
| 15 | 23.6 | DBL |
| 16 | 25.1 | DBL |
| 17 | 26.4 | VBAR_A / EBR_B |
| 18 | 27.7 | VBAR_A |

Two blind model reads of the gloss (H316) put four small words at the same places but could read only one fully -- **ticks 4.7-9.8 'forb...'
(forble? / forbe?z), 13.2-17.0 'comm...', 21.1-23.5 'elle', 25.9-28.0 'v?l'**. They failed their own gate, so the gloss is unread: a person's
reading of these four words (and any the models missed) is what ASKS 93 asks for, with from/to ticks as in the template above.
