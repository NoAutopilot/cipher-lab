# BNF-GIEVRE-SORT sorter inputs (15 Oct 2026, account 2, LANE BNF-FOCUS)
Blind sign sorter for the cipher paragraph at the end of the Nevers-to-Gievre letter of 21 Aug 1593 (BnF fr.3985 f.89, canvas 179).
Built, not published. `sh ciphers/fr3985-gievre-1593/sorter/build.sh OUTDIR` cuts the tiles (no network) and writes
`gievre_f89_sorter.html` in default blind mode (no key, no value, no machine or reader label; starting piles are shape clusters),
then runs `tools/sorter_preflight.py`. Tiles come from the committed crops `images/f89/f89_L0N_s1/s2.jpg` (lines L01-L03 stitched
at native x=2700; L04 is clear text and is not tiled; the clear words inside L01-L02 are left out by hand-set spans in cut.py).
`focus.tsv` lists the tiles at the places where BNF-Q2-TX's two blind passes split (positions only).
What the page asks: pile each tile by shape alone, new pile for a new sign, BAD-CUT for a wrong box.
Export: publish with capabilities {"db": {}} after eyeing the preflight contact sheet, sort, export, then `tools/sign_sorter_apply.py`
turns the export into settled labels; machine passes then transcribe against those labels (TRANSCRIPTION.md).
Preflight warnings left open: R13/R15 (starting piles are shape clusters, not settled piles) and R14 (no box check done; the cut
is automatic with a hand-set span filter, so box-check before publishing if the owner's rule applies). See NOTES.md "BNF-GIEVRE-SORT".
