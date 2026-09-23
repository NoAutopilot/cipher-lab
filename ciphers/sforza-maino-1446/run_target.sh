#!/bin/sh
# Target runs, 23 Sept 2026, with exactly the control settings (SET). Usage: sh run_target.sh MODEL.npz CORPUS.txt
# CORPUS is the '#'-word-divided corpus used for --unit vocabulary (tools/italian_ngram.py corpus output).
M=$1; V=$2
SET="--restarts 16 --iters 300000"
A="ciphertext.txt ciphertext_f70.txt"
U="--vocab $V --unit 'F p B H c d S p' --unit '8 z B p r J F p' --unit 'x J p g' --unit 'F E p S' --unit 'F p B H c'"
python3 campaign.py T-joint-mapA --model $M -- $A --map signs_mapA.tsv $SET
python3 campaign.py T-joint-mapB --model $M -- $A --map signs_mapB.tsv $SET
python3 campaign.py T-f68-alone --model $M -- ciphertext.txt $SET
python3 campaign.py T-f70-alone --model $M -- ciphertext_f70.txt --map signs_mapA.tsv $SET
python3 campaign.py T-joint-mapA-clearctx --model $M -- $A --map signs_mapA.tsv $SET --context clear
python3 campaign.py T-joint-mapA-V=de --model $M -- $A --map signs_mapA.tsv $SET --fix V=de
python3 campaign.py T-joint-mapA-V=de-clearctx --model $M -- $A --map signs_mapA.tsv $SET --fix V=de --context clear
python3 campaign.py T-joint-mapA-V=che-clearctx --model $M -- $A --map signs_mapA.tsv $SET --fix V=che --context clear
python3 campaign.py T-joint-mapA-V=et-clearctx --model $M -- $A --map signs_mapA.tsv $SET --fix V=et --context clear
eval python3 campaign.py T-joint-mapA-units --model $M -- $A --map signs_mapA.tsv $SET $U
eval python3 campaign.py T-joint-mapA-units-V=de-clearctx --model $M -- $A --map signs_mapA.tsv $SET $U --fix V=de --context clear
python3 campaign.py T-joint-mapA-shuffled1 --model $M -- $A --map signs_mapA.tsv $SET --shuffle 1
python3 campaign.py T-joint-mapA-shuffled2 --model $M -- $A --map signs_mapA.tsv $SET --shuffle 2
python3 campaign.py T-joint-mapA-clearctx-shuffled1 --model $M -- $A --map signs_mapA.tsv $SET --context clear --shuffle 1
