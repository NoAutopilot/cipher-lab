#!/bin/sh
# Reproduces the LANE R4 N controls of 24 Sept 2026 (NOTES.md "Control-first cryptanalysis").
# Builds the French order-5 model from tools/data/fr16 (held-out tenth kept apart), synthesises the matched
# nomenclator controls on the target's own run pattern, solves them blind and scores them.
set -e
cd "$(dirname "$0")/../../.."
W=ciphers/fr3993-villeroy-1595/solver; TMP=${TMPDIR:-/tmp}/villeroy-ctl; mkdir -p $TMP
python3 $W/fr_corpus.py $TMP
python3 tools/italian_ngram.py build $TMP/fr16_train.txt --out $TMP/fr16_o5.npz
for s in 1 2; do
  python3 tools/nomenclator_anneal.py synth $TMP/fr16_heldout.txt --design $W/design_nomen69.json --pattern $W/target_pairs.txt --seed $s --out $W/control_s$s.txt --truth $W/control_s$s.truth.json
  python3 tools/nomenclator_anneal.py solve $W/control_s$s.txt --model $TMP/fr16_o5.npz --words "$(cat $W/words.txt)" --max-syl 12 --max-word 8 --max-null 4 --syl both --restarts 12 --iters 1500000 --procs 4 --out $W/control_s$s.result.json
  python3 tools/nomenclator_anneal.py eval $W/control_s$s.result.json $W/control_s$s.truth.json
done
python3 tools/nomenclator_anneal.py synth $TMP/fr16_heldout.txt --design $W/design_homo.json --pattern $W/target_pairs.txt --seed 1 --out $W/control_homo_s1.txt --truth $W/control_homo_s1.truth.json
python3 tools/nomenclator_anneal.py solve $W/control_homo_s1.txt --model $TMP/fr16_o5.npz --syl none --max-syl 0 --max-word 0 --max-null 3 --restarts 12 --iters 1500000 --procs 4 --out $W/control_homo_s1.result.json
python3 tools/nomenclator_anneal.py eval $W/control_homo_s1.result.json $W/control_homo_s1.truth.json
