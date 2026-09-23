#!/bin/sh
# Second target batch, 23 Sept 2026: search baselines for the single-letter and map-B runs, and a looser
# hypothesis space (CV and VC syllables, more nulls and word signs). Same SET as the controls.
M=$1
SET="--restarts 16 --iters 300000"
A="ciphertext.txt ciphertext_f70.txt"
python3 campaign.py T-f68-alone-shuffled1 --model $M -- ciphertext.txt $SET --shuffle 1
python3 campaign.py T-f70-alone-shuffled1 --model $M -- ciphertext_f70.txt --map signs_mapA.tsv $SET --shuffle 1
python3 campaign.py T-joint-mapB-shuffled1 --model $M -- $A --map signs_mapB.tsv $SET --shuffle 1
python3 campaign.py T-joint-mapB-clearctx --model $M -- $A --map signs_mapB.tsv $SET --context clear
python3 campaign.py T-joint-mapA-loose --model $M -- $A --map signs_mapA.tsv $SET --syl both --max-syl 10 --max-null 4 --max-word 6
python3 campaign.py T-joint-mapA-loose-shuffled1 --model $M -- $A --map signs_mapA.tsv $SET --syl both --max-syl 10 --max-null 4 --max-word 6 --shuffle 1
python3 campaign.py T-joint-mapA-lettersonly --model $M -- $A --map signs_mapA.tsv $SET --syl none --max-word 0 --max-null 2
python3 campaign.py T-joint-mapA-lettersonly-shuffled1 --model $M -- $A --map signs_mapA.tsv $SET --syl none --max-word 0 --max-null 2 --shuffle 1
