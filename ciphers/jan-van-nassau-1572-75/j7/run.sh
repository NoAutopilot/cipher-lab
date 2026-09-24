#!/bin/sh
# J7 (24 Sept 2026): regenerate the whole 5549-body experiment from committed inputs (run from ciphers/jan-van-nassau-1572-75).
set -e
G=../../tools/german_ngram.py; N=../../tools/nomenclator_anneal.py
python3 j7/clean_sources.py && python3 j7/make_target.py && python3 j7/make_control.py
python3 $G corpus j7/src_5549_clear.txt ../../tools/data/de16/composed_enhg.txt ../august-van-saksen-1561-64/plaintext_74.txt ../august-van-saksen-1561-64/plaintext_98.txt --out j7/corpus_T.txt
python3 $G build j7/corpus_T.txt --out j7/model_T.npz --order 4
python3 $N synth j7/control_plain.txt --lang de --design j7/control_design.json --pattern j7/body_5549.txt --out j7/control_cipher.txt --truth j7/control_truth.json --seed 7
python3 $N synth j7/control_plain.txt --lang de --design j7/control2_design.json --pattern j7/body_5549.txt --out j7/control2_cipher.txt --truth j7/control2_truth.json --seed 7
python3 -c "
import re,sys; sys.path.insert(0,'../../tools'); import german_ngram as g
fr=[g.norm(x).strip('#') for x in re.findall(r'\{(.*?)\}',open('j7/control_cipher.txt').read())]
open('j7/control_frames.txt','w').write('\n'.join(f for f in fr if f)+'\n')"
cat j7/corpus_T.txt j7/control_frames.txt > j7/corpus_C.txt && python3 $G build j7/corpus_C.txt --out j7/model_C.npz --order 4
j7/solve.sh j7/control_cipher.txt j7/model_C.npz j7/control_result.json --restarts 16 --iters 400000 | head -1
j7/solve.sh j7/control_cipher.txt j7/model_C.npz j7/control_shuffle.json --restarts 16 --iters 400000 --shuffle 1 | head -1
j7/solve.sh j7/control2_cipher.txt j7/model_C.npz j7/control2_result.json --restarts 16 --iters 400000 | head -1
j7/solve.sh j7/body_5549.txt j7/model_T.npz j7/body_result.json --restarts 16 --iters 400000 | head -1
j7/solve.sh j7/body_5549.txt j7/model_T.npz j7/body_shuffle.json --restarts 16 --iters 400000 --shuffle 1 | head -1
python3 $N eval j7/control_result.json j7/control_truth.json
python3 $N eval j7/control2_result.json j7/control2_truth.json
python3 j7/truth_score.py j7/control_result.json j7/control_truth.json j7/model_C.npz j7/control_cipher.txt
