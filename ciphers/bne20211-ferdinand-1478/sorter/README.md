# Ferdinand 1478 sign sorter (FER1478-SORTER, 5 Oct 2026, account-4 standing session)

Text inputs only; the tiles and page images are BNE images and stay in the private repository / a scratchpad (never here).

Rebuild (needs the private clone at /home/user/cipher-lab-private):
1. Line strips: `tools/iiif_lines.py --image images-123-shots/set1-4.png --out <scratch>/full --prefix s4 --region 180,0,1384,736 --centres 515,557,598,640 --top-margin 14 --bottom-margin 14`; set1-5 `--prefix s5 --region 180,0,1180,802 --centres 15,60,100,138,185,238,285,333,380,428,480,527,572,621,670,726,778 --follow-slope 300 --top-margin 14 --bottom-margin 14`; set1-6 `--prefix s6c --region 230,0,1150,110 --centres 70 --top-margin 14 --bottom-margin 14`.
2. `tools/glyph_atlas.py segment $(cat segment_pages.txt) --out <scratch>/seg` (default mode; pages C01-C22, C01 starts after the clear "soy maravillado", C22 stops before "Exmo señor"), then `tools/glyph_atlas.py cluster --out <scratch>/seg --k 40 --k-marks 6`. signs.tsv here keeps only boxes crossing the strip's centre band (923 of 1170; 247 neighbour-line fragments dropped); labels.tsv names the 40 shape clusters by the letter they resemble (piles starting "?" are mixed or badly cut).
3. `tools/sign_sorter.py --signs signs.tsv --labels labels.tsv --marks <scratch>/seg/marks.tsv --pages <scratch>/seg/crops --focus focus.tsv --rank rank.tsv --title "Ferdinand 1478 Sign Sorter" --out <scratch>/ferdinand1478-sorter.html` -> 28 piles, 923 tiles, 2.3 MB.

Status: built 5 Oct 2026 23:3x UTC; publishing it as a private artifact was refused by this session's auto-mode classifier
(the page embeds BNE images from the private repository). Waiting on the owner to allow the publish or to publish the page
from a session that may (ASKS 143). Focus box: 25 tiles from the tt / crossed-t / e / e: / c / d / d. piles.
