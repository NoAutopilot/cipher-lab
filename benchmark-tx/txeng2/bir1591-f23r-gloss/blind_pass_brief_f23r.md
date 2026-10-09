# Blind transcription pass, fr.3623 f.23r cipher lines (TXP-B23, 9 Oct 2026)

You are one of two independent readers of the cipher signs on crops of a late-16th-century letter (BnF fr.3623 f.23r).
The pass is VALUE-BLIND: you label each hand-drawn sign by its SHAPE only, from the label list below. You do not know, and
must not look up, what any sign means.

Read ONLY the 8 crop files named in your task and this brief. Do not open any other file in this repository (no NOTES.md,
no key, no other pass, no other image of this page); the pass is void if you do.

## The crops

8 crops, one per cipher line, top to bottom of the page; each crop is the whole line (no segments, no overlap):

| passage | crop file |
|---|---|
| L01 | f23r_L03.jpg |
| L02 | f23r_L05.jpg |
| L03 | f23r_L07.jpg |
| L04 | f23r_L09.jpg |
| L05 | f23r_L11.jpg |
| L06 | f23r_L13.jpg |
| L07 | f23r_L15.jpg |
| L08 | f23r_L17.jpg |

The crops are small (about 1200 px wide, signs about 20-25 px): enlarge them (e.g. 3x with PIL into your own scratch
directory, never into the repository) and read in short stretches. Each crop holds its cipher line along the middle; the
page also carries small ordinary handwriting between the cipher lines, and pieces of it may remain in a crop above or below
the signs, sometimes touching them: that writing is NOT cipher, ignore it. In L07 and L08 the right part of the crop is
ordinary handwriting (a closing formula and a signature): skip it; transcribe the cipher run only.

## Labels (shape only; use these exact labels)

    PSI    psi / trident (a cup or Y with a vertical stem through it)
    TRI    upright triangle (delta) standing alone
    TRIS   upright triangle on a vertical stem or flag, figure-4-like
    TRIX   upright triangle sitting above a small cross or bar (stacked)
    DTRI   downward triangle (nabla) alone
    DTRIS  downward triangle with a vertical stroke rising from it or through it
    HASH   double-barred cross, # or H-with-two-bars
    SQ     small square / box
    O      small round o
    OS     o with a stem or hook rising from it (delta-like)
    Q      loop with a descending tail (q- or c-cedilla-like)
    THREE  figure 3
    TWO    figure 2
    Z      plain z
    XI     z or 3 with an extra cross-bar or a third stroke (xi-like)
    INVT   inverted T (a horizontal bar with a vertical stroke rising from its middle)
    MPLUS  a short bar above a cross (minus-plus)
    PLUS   a plain cross
    NEQ    a long slanted stroke crossed by two short bars (crossed f / not-equal)
    CENT   c with a vertical stroke through it
    C      plain c
    X      x / cross-saltire
    ALPHA  alpha / a with a tail
    CUP    u / v cup, open at the top, rounded
    OMEGA  double loop (w / omega shape), with or without a bar over it
    M      m-like run of humps, often with a tail
    DIV    division sign (a bar with a dot above and below)
    DOT    a single dot written between signs
    I      a single short vertical stroke

A sign that fits none: `NEW:<short description>` (e.g. `NEW:h-shaped hook`), and use the same description every time you
meet that shape. Unreadable mark: `?`. A sign struck through by the writer: still give it a row, and write `struck` in note.

## Output

Write exactly one TSV file at the path your task names, header exactly:

    passage	pos	sign_id	alt	conf	note

- `passage`: L01..L08 as in the table; `pos`: 1-based position within the passage.
- `sign_id`: a label above, or `NEW:...`, or `?`. `alt`: a second label if two fit, else blank.
- `conf`: H (clear), M (plausible, one look-alike), L (guess). `note`: a few words on the shape when useful.

No other output file in the repository. When done, report in a short paragraph: sign count per passage, how many NEW: and ?
rows, which labels you found hardest to tell apart. Do not decode, do not guess at meanings, do not describe the content.
