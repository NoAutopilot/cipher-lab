#!/usr/bin/env python3
"""Regenerate the three reconciliation-agreement metrics for clair349-este-guise-1556's passA.tsv/passB.tsv
(YX-TR349B, 25 Sept 2026). The two blind passes used independent, unshared vocabularies for non-digit signs
(no ciphertext-side glyph atlas was built before the passes -- a known gap, see NOTES.md), so the raw
tools/reconcile_passes.py agreement (39.9%) mostly measures label-vocabulary mismatch, not real disagreement
on what mark is on the page (Symbol alphabets lesson, transcription.md). This script regenerates the two
fairer metrics quoted in NOTES.md:
  1. sign-normalized: every 'sign'-kind token's value replaced with the placeholder 'SIGN' before reconciling
     (passA_norm.tsv / passB_norm.tsv), so two different sign labels at the same position count as agreement
     -- measures "did both passes agree a sign (of some kind) belongs here", not which one.
  2. digit-only: 'sign'-kind rows dropped entirely, only 'digit' rows kept and renumbered per line
     (passA_digitsonly.tsv / passB_digitsonly.tsv) -- measures agreement on the (decode-critical, vocabulary-
     unambiguous) digit stream alone.
Run: python3 ciphers/clair349-este-guise-1556/reconcile_metrics.py
"""
import csv, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))


def write_norm(src, dst):
    with open(src) as f, open(dst, 'w', newline='') as g:
        r = csv.reader(f, delimiter='\t'); w = csv.writer(g, delimiter='\t')
        w.writerow(next(r))
        for line, pos, token, kind, grade, *rest in r:
            w.writerow([line, pos, 'SIGN' if kind == 'sign' else token, kind, grade, rest[0] if rest else ''])


CANON = {
    'z-flourish': 'C1-tieflourish', 'tie-flourish': 'C1-tieflourish',
    'Ao-ligature': 'C2-Ao', 'Ao-lig': 'C2-Ao',
    'ff-ligature': 'C3-ff', 'ff-lig': 'C3-ff',
    'hash-mark': 'C4-hash', 'hash': 'C4-hash',
    'tc-ligature': 'C5-tc', 'tc-sign': 'C5-tc',
    'uu-ligature': 'C6-uu', 'uu-sign': 'C6-uu',
    'loop-Y': 'C7-Y', 'Y-mark': 'C7-Y',
    'to-ligature': 'C8-to', 'to': 'C8-to',
}  # the 8 sign-shape correspondences this worker is confident of (matching descriptions in both passes'
   # own notes, AND the NW aligner independently placing them at the same column repeatedly before any
   # remapping) -- everything else keeps its own pass-specific label, i.e. is NOT credited as agreement


def write_atlas(src, dst):
    with open(src) as f, open(dst, 'w', newline='') as g:
        r = csv.reader(f, delimiter='\t'); w = csv.writer(g, delimiter='\t')
        w.writerow(next(r))
        for line, pos, token, kind, grade, *rest in r:
            if kind == 'sign':
                token = CANON.get(token, token)
            w.writerow([line, pos, token, kind, grade, rest[0] if rest else ''])


def write_digitsonly(src, dst):
    with open(src) as f, open(dst, 'w', newline='') as g:
        r = csv.reader(f, delimiter='\t'); w = csv.writer(g, delimiter='\t')
        w.writerow(next(r))
        counters = {}
        for line, pos, token, kind, grade, *rest in r:
            if kind != 'digit':
                continue
            counters[line] = counters.get(line, 0) + 1
            w.writerow([line, counters[line], token, kind, grade, rest[0] if rest else ''])


def reconcile(a, b, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    return subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'reconcile_passes.py'), a, b,
                           '--out-dir', out_dir], capture_output=True, text=True).stdout.strip()


if __name__ == '__main__':
    a, b = os.path.join(HERE, 'passA.tsv'), os.path.join(HERE, 'passB.tsv')
    print('raw (as committed):')
    print(reconcile(a, b, HERE))

    an, bn = os.path.join(HERE, 'passA_norm.tsv'), os.path.join(HERE, 'passB_norm.tsv')
    write_norm(a, an); write_norm(b, bn)
    print('\nsign-normalized (sign tokens -> placeholder "SIGN"):')
    print(reconcile(an, bn, os.path.join(HERE, '_scratch_norm')))

    aa, ba = os.path.join(HERE, 'passA_atlas.tsv'), os.path.join(HERE, 'passB_atlas.tsv')
    write_atlas(a, aa); write_atlas(b, ba)
    print('\npartial cross-pass sign atlas (8 confident shape correspondences only, everything else unmapped):')
    print(reconcile(aa, ba, os.path.join(HERE, '_scratch_atlas')))

    ad, bd = os.path.join(HERE, 'passA_digitsonly.tsv'), os.path.join(HERE, 'passB_digitsonly.tsv')
    write_digitsonly(a, ad); write_digitsonly(b, bd)
    print('\ndigit-only (sign rows dropped, digit rows renumbered per line):')
    print(reconcile(ad, bd, os.path.join(HERE, '_scratch_digits')))
