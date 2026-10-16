#!/bin/bash
# HEID-NA-SCREEN (16 Oct 2026): re-derive the inv. 6022 700 px scans and the 36 composites. Run from the repository root.
# 140 service.archief.nl requests at >= 3.1 s (take/release lines in ROOM.md first); images stay outside git;
# compare with heidnascreen/scans_sha1.txt; the composite key is heidnascreen/compkey.json (seed 16230).
set -e; O=${1:-scratch_heidnascreen}; M=412b1414-afa2-42fe-b56d-2b5f705e5005; T=ciphers/oldenbarnevelt-brederode-1605
python3 $T/screen_tools/na_fetch.py $M $O/i6022 700 166 181 $(seq 186 3 595)
I=$T/images
python3 ciphers/brederode-heidelberg-1621/heidnascreen/composites.py $O/i6022 $O/comp $O/key.json 16230 \
  POS166=$O/i6022/s0166_700.jpg POS181=$O/i6022/s0181_700.jpg POS181=$O/i6022/s0181_700.jpg \
  CTRL-CIPHER=$I/na_301_14_2016_p0031.jpg NEG-PLAIN=$I/na_101_02_6016_p0261.jpg -- $(seq 186 3 595)
cmp $O/key.json ciphers/brederode-heidelberg-1621/heidnascreen/compkey.json && echo "key MATCH"
