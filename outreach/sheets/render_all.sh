#!/bin/sh
# Regenerates every sheet in outreach/sheets/ (MQS-SHEETS-R, 9 Oct 2026). Run from the repository root:
#   sh outreach/sheets/render_all.sh [--check]     (--check exits 1 for any sheet that is stale, rule 7)
# The Birago 1572 family sheets are HELD and are not here (see README.md).
set -e
C="$1"; S=outreach/sheets; T=tools/decipher_sheet.py
python3 $S/eckert_e4_inputs.py $C
python3 $T key ciphers/fr2980-gramont --config tools/tests/decode_configs/fr2980-gramont.json --job ciphertext.txt --out $S/gramont-key.html $C
python3 $T reading ciphers/fr2980-gramont --config tools/tests/decode_configs/fr2980-gramont.json --job ciphertext.txt --result 'BnF fr.2980 f.29r' --out $S/gramont-f29r-reading.html $C
python3 $T key ciphers/fr20140-danzay-1557 --config tools/tests/decode_configs/fr20140-danzay-1557.json --job ciphertext.txt --out $S/danzay-f35-key.html $C
python3 $T reading ciphers/fr20140-danzay-1557 --config tools/tests/decode_configs/fr20140-danzay-1557.json --job ciphertext.txt --result 'fr.20140 f.35' --line-images $S/danzay-f35-lines.tsv --out $S/danzay-f35-reading.html $C
python3 $T key ciphers/eckert-1864 --tokens-tsv $S/eckert-e4-tokens.tsv --key-tsv $S/eckert-e4-key.tsv --title 'Huntington E4: the code words this telegram uses' --out $S/eckert-e4-key.html $C
python3 $T reading ciphers/eckert-1864 --tokens-tsv $S/eckert-e4-tokens.tsv --key-tsv $S/eckert-e4-key.tsv --line-images $S/eckert-e4-lines.tsv --result 'Huntington mssEC 19 p.49' --title 'Huntington mssEC 19 p.49, E4: Fox to Butler, 21 Apr 1864' --leaf-url 'https://hdl.huntington.org/digital/collection/p16003coll11/id/8941' --key-credit 'Key: Cipher No. 1 (Huntington mssEC 41), the cipher book, read page by page (ciphers/eckert-1864/key.md)' --image-credit 'Thomas T. Eckert Papers, mssEC 19, The Huntington Library, San Marino, California' --out $S/eckert-e4-reading.html $C
