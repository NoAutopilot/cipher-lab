#!/usr/bin/env python3
"""TXE-O (9 Oct 2026) harness: the plain lattice at lam 4 on eval_heldout for tools/tx_doubt.py signal `latt` (M14),
read-free. Same inputs and code as TXE-E's run_conf.py `base` lattice (passes A/B, passC skeleton, confusion_1572.tsv,
key_1572_sheet.tsv, it16dip LM, beam 64) with NO learnt matrix, so no truth is read. dev_tune's plain lattice is the
committed benchmark-tx/outputs/birago1572-no87/passL_lattice_dev_tune_lam4.tsv (TXE-E). Run from the repo root:
  python3 benchmark-tx/txeng/doubt/run_latt.py"""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "benchmark-tx/txeng/conf"))
import key_decode_lattice as K  # noqa: E402
import run_conf as RC  # noqa: E402
from judge_plaintext import LANG_CORPORA, NgramModel, read_corpus  # noqa: E402

RC.TMP = HERE / "work"
pages = RC.prep()
key = K.read_key(RC.H / "key_1572_sheet.tsv")
lm = K.LM(NgramModel([read_corpus(p) for p in LANG_CORPORA["it16dip"]]))
base = RC.lattice(pages, RC.EVAL)
RC.write_seq(HERE / "passL_lattice_eval_heldout_lam4.tsv", base, K.viterbi(base, key, lm, 4.0)[0])
print("positions", len(base))
