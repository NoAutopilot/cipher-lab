R9-OBRED4, 6 Oct 2026. Image check of ciphertext.txt (print) against NL-HaNA 3.01.14 inv. 1490 scans 1-2 (the letter; scans 3-7 are the
endorsement and the money-account annex, no cipher groups). passA_*.tsv: one blind Sonnet pass per page on line crops (only the
lines with numerals are kept here). printed_numerals.py regenerates printed_numerals.txt from ciphertext.txt. corrections.tsv: the
image's readings where it differs from the print or cannot confirm it. summary.tsv: the counts.
Crops: python3 tools/iiif_lines.py --image images/na_301_14_1490_p0001.jpg --out <dir> --prefix s1 --region 90,120,2390,3450 --debug
       ... --image images/na_301_14_1490_p0002.jpg --prefix s2L --region 60,60,2380,3500 ; --prefix s2R --region 2480,60,2400,3500
