#!/usr/bin/env python3
"""Pre-registered test kp86f (kp86f/PREREG_kp86f.md, PIS1-275V): kp86d/kp86d.py run UNCHANGED (same statistic, nulls,
seeds, arms A/B, positive control, gate) on the per-line passes of f.275v (tx86f/) against the Colbert copy of f.275v
(kp86f/colbert_f275v.txt). kp86d.main() reads its copy text as HERE/colbert_p121_123.txt and writes HERE/kp86d_result.json;
this wrapper (as kp86e.py did) saves the committed kp86d result first, points kp86d's module-level `open` at
kp86f/colbert_f275v.txt for that one filename only, sets kp86d.CLEAR_IN_MS to the in-clear phrase on f.275v (empty if
none, given with --inms), runs kp86d.main(), moves the output to kp86h/kp86i_result.json and restores kp86d's file.
    python3 kp86i/kp86i.py --err E [--inms "phrase"]   (tokens tx86h/ciphertext_f275v.tsv, extra tx86h/passA/passB)
    --local: tokens tx86h/local_ciphertext.tsv, extra tx86h/local_passA/B.tsv (lines L17-L20 only) -> kp86h/kp86i_local_result.json
RUN6-PIS (5 Oct 2026): kp86f.py with paths changed and the --local switch added; nothing else.
RUN6-PISFIN (5 Oct 2026): kp86h.py with output names kp86i_*; COPY = kp86i/colbert_f275v.txt (span extended); nothing else.
D2-PIS275 (6 Oct 2026, PREREG kp86j): kp86i.py with --local tokens tx86i/local_ciphertext.tsv, extra local passes A, B (tx86h) + C (tx86i),
output names kp86j_*; COPY still kp86i/colbert_f275v.txt; nothing else."""
import builtins, os, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(T, 'kp86d'))
import kp86d
args = sys.argv[1:]; inms = ''
LOCAL = '--local' in args
if LOCAL:
    args.remove('--local')
PFX = 'tx86h/local_' if LOCAL else 'tx86h/'
if '--inms' in args:
    i = args.index('--inms'); inms = args[i + 1]; del args[i:i + 2]
COPY = os.path.join(T, 'kp86i', 'colbert_f275v.txt')


def _open(path, *a, **k):
    if os.path.basename(str(path)) == 'colbert_p121_123.txt':
        path = COPY
    return builtins.open(path, *a, **k)


kp86d.open = _open
kp86d.CLEAR_IN_MS = inms if inms else '\x00'   # '\x00' never occurs in the copy: nothing removed
D = os.path.join(T, 'kp86d', 'kp86d_result.json'); SAVE = D + '.save'
shutil.copyfile(D, SAVE)
try:
    assert LOCAL, 'kp86j is registered for --local only'
    sys.argv = [sys.argv[0]] + args + ['--tokens', 'tx86i/local_ciphertext.tsv',
                                       '--extra', 'tx86h/local_passA.tsv', 'tx86h/local_passB.tsv', 'tx86i/local_passC.tsv']
    kp86d.main()
    shutil.move(D, os.path.join(HERE, 'kp86j_local_result.json'))
finally:
    shutil.move(SAVE, D)
