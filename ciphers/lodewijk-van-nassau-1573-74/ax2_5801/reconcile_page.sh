#!/bin/sh
# AX2-5801: reconcile passA/passB for page $1, print per-line + overall agreement.
set -e
cd "$(dirname "$0")/.."
python3 ../../tools/reconcile_passes.py ax2_5801/passA_5801_p"$1".tsv ax2_5801/passB_5801_p"$1".tsv \
    --out-dir ax2_5801/recon_p"$1" --crops images_wv2/crops_comp --rows
