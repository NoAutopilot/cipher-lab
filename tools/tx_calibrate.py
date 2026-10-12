#!/usr/bin/env python3
"""Reader calibration on known-answer pages of the same hand (TXE4-9 CALIB, 12 Oct 2026).

A reader first transcribes calibration pages whose truth is known, is shown ONLY which of its own signs were wrong (labels,
never a letter or key value), then reads a target page in a fresh call. The truth of the calibration items is a tool input
here and is never scored; the target's truth is opened by tools/tx_bench.py alone. Three subcommands:

  build    --out DIR --label-brief BRIEF.md --crop GLOB [--crop GLOB ...] [--notes NOTES.md] [--passages TEXT]
           copies the calibration crops into DIR/calib/, writes DIR/task.txt (the brief's general rules and label table, the
           crop notes, the output format) and DIR/files.txt. The reader is told to write DIR/read.tsv.
  feedback --read READ.tsv --truth ITEM=TRUTH.tsv[:PREFIX] [--truth ...] --out feedback.tsv [--context 3]
           aligns the read to each calibration item's truth with tx_bench.align (G 0.75, truth sets: the scorer's own
           alignment) and writes one row per wrong UNFLAGGED scored position: item, line, the reader's own label sequence with
           --context neighbours each side (the position in brackets), and `[your label -> allowed labels]`. A deleted scored
           position is `a sign missed here`, an output sign aligned to no reference position is `extra sign here`. Flagged
           positions (truth `flag` column, tx_bench.is_flagged) and excluded positions give no row. CLEAR rows are dropped
           from the read first. Prints counts only (scored, unflagged, wrong, missed, extra per item), never the truth.
  target   --out DIR --brief BRIEF.md --calib-dir DIR1 --calib-read READ.tsv [--feedback feedback.tsv] --crop GLOB [...]
           assembles the target call: DIR/calib/ (the calibration crops), DIR/calib_read.tsv, DIR/feedback.tsv (arm F only),
           DIR/target/ (the target crops) and DIR/task.txt = one preamble paragraph (F: study feedback.tsv against calib/
           before reading; C: the same paragraph with no mention of corrections) + the brief verbatim. The reader writes
           DIR/out.tsv.

Nothing here reads the target item's truth, writes a key, a reading or a grade, or edits any truth or flag. Offline test:
tools/tests/test_tx_calibrate.py (a substitution, a deletion and an insertion each give one row; a flagged and an excluded
position give none; no row carries a plain-text letter; CLEAR rows are dropped; the task files name no truth path).
Why (brief .claude/briefs/runs/2026-10-11-acct3-txe4-9.md): TXE3-4 showed the agreed-wrong rate is a property of the hand that
no second reader sees; TXE3-3 that the real misreads are one reader's own; TXE-H that hints from tile statistics miss the
reader's actual confusions. The owner's rule: a known answer may score a result but is never the tool's input on the scored
item -- so the calibration comes from OTHER benchmark items of the same hand.
"""
import argparse, csv, glob, os, re, shutil, sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tx_bench  # noqa: E402

HDR = ['passage', 'pos', 'sign_id', 'alt', 'conf', 'note']


def read_tsv(path):
    with open(path, newline='') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def label_table(brief_path):
    """The label-table block of a blind-pass brief: from the 'Sign labels' line to the line before 'Output'."""
    lines = open(brief_path).read().split('\n')
    start = next(i for i, l in enumerate(lines) if 'Sign labels' in l)
    end = next(i for i in range(start + 1, len(lines)) if re.match(r'\s*(##\s*)?Output', lines[i]))
    return '\n'.join(lines[start:end]).rstrip() + '\n'


def copy_crops(globs, dest):
    os.makedirs(dest, exist_ok=True)
    out = []
    for g in globs:
        fs = sorted(glob.glob(g))
        if not fs:
            sys.exit('tx_calibrate: no file matches %s' % g)
        for f in fs:
            shutil.copy(f, os.path.join(dest, os.path.basename(f)))
            out.append(os.path.basename(f))
    return out


CALIB_RULES = """You transcribe the cipher signs of French letters of 1591, line by line, from line crops in the folder calib/ next to
this file. You open ONLY this task file and the crop files listed below; nothing else, no other file, no web. You do not know
and must not guess what the signs mean: label each sign by its SHAPE with the labels below. You may make enlarged copies of a
crop (e.g. PIL resize 3x LANCZOS, cut into halves) inside this folder only, and read those. Small writing above or below the
main line of a crop is not part of the line: transcribe only the signs on the main line. Skip ordinary French prose words
(do not write rows for them; mention the word in the note of the neighbouring sign). Read every sign once, in order, without
skipping; a sign you cannot identify is a row with ?, never left out.
"""

OUTPUT_FMT = """Output: write exactly one TSV file, %s, header exactly
passage	pos	sign_id	alt	conf	note
  passage: the line id given above for each crop; pos: 1, 2, 3 ... left to right within the passage; sign_id: a label above,
  NEW:<short description> or ?; alt: a second-choice label if you hesitate, else empty; conf: H (sure), M (probable), L (guess);
  note: anything uncertain. Write nothing but your output file, then reply in one short paragraph with the sign count per
  passage. Do not decode, do not guess at meanings, do not describe the letters' content.
"""


def cmd_build(a):
    os.makedirs(a.out, exist_ok=True)
    files = copy_crops(a.crop, os.path.join(a.out, 'calib'))
    notes = open(a.notes).read() if a.notes else ''
    task = ('# Calibration read: known pages of one hand\n\n' + CALIB_RULES + '\nCrops (folder calib/):\n'
            + ''.join('  calib/%s\n' % f for f in files) + '\n' + notes + '\n' + label_table(a.label_brief) + '\n'
            + OUTPUT_FMT % os.path.join(a.out, 'read.tsv'))
    open(os.path.join(a.out, 'task.txt'), 'w').write(task)
    open(os.path.join(a.out, 'files.txt'), 'w').write('\n'.join(files) + '\n')
    print('build: %d crops, task %s' % (len(files), os.path.join(a.out, 'task.txt')))


def load_read(path, prefix_for=None):
    """{line: [labels]} from a reader TSV; CLEAR rows dropped; a bare L## passage gets the prefix its item needs."""
    lines = defaultdict(list)
    for r in read_tsv(path):
        ln = (r.get('passage') or r.get('line') or '').strip()
        sg = (r.get('sign_id') if r.get('sign_id') is not None else r.get('sign', '')).strip()
        if not ln or not sg or sg == 'CLEAR':
            continue
        if prefix_for and '_' not in ln:
            ln = prefix_for(ln)
        lines[ln].append((float(r['pos']), sg))
    return {k: [s for _, s in sorted(v, key=lambda t: t[0])] for k, v in lines.items()}


def cmd_feedback(a):
    specs = []
    for t in a.truth:
        item, rest = t.split('=', 1)
        path, _, prefix = rest.partition(':')
        specs.append((item, path, prefix))
    pre = {}
    for item, path, prefix in specs:
        if prefix:
            pre[prefix] = item
    def prefix_for(ln):
        # a bare passage id belongs to the one item that declares a prefix (several: ambiguous, keep bare)
        return '%s_%s' % (list(pre)[0], ln) if len(pre) == 1 else ln
    read = load_read(a.read, prefix_for)
    rows_out, counts = [], {}
    k = a.context
    for item, path, prefix in specs:
        truth = read_tsv(path)
        by = defaultdict(list)
        for r in truth:
            by[r['line']].append(r)
        c = dict(scored=0, unflagged=0, wrong=0, missed=0, extra=0, lines_read=0)
        for ln, trows in sorted(by.items()):
            trows.sort(key=lambda r: float(r['pos']))
            out = read.get(ln)
            if not out:
                continue
            c['lines_read'] += 1
            ref = [r['ref_sign'] for r in trows]
            ts = [set(filter(None, r['truth'].split('|'))) for r in trows]
            path_ = tx_bench.align(ref, ts, out)
            j = 0  # index into out
            for ri, osg in path_:
                if ri is None:
                    ctx = out[max(0, j - k):j] + ['[%s]' % osg] + out[j + 1:j + 1 + k]
                    rows_out.append((item, ln, ' '.join(ctx), 'extra sign here [your label %s]' % osg))
                    c['extra'] += 1; j += 1
                    continue
                r = trows[ri]
                if r['status'] != 'scored':
                    j += osg is not None
                    continue
                c['scored'] += 1
                if tx_bench.is_flagged(r):
                    j += osg is not None
                    continue
                c['unflagged'] += 1
                allowed = ' | '.join(sorted(ts[ri] | {r['ref_sign']}))
                if osg is None:
                    ctx = out[max(0, j - k):j] + ['[_]'] + out[j:j + k]
                    rows_out.append((item, ln, ' '.join(ctx), 'a sign missed here [allowed labels %s]' % allowed))
                    c['missed'] += 1
                    continue
                if osg not in ts[ri] and osg != r['ref_sign']:
                    ctx = out[max(0, j - k):j] + ['[%s]' % osg] + out[j + 1:j + 1 + k]
                    rows_out.append((item, ln, ' '.join(ctx), '[your label %s -> allowed labels %s]' % (osg, allowed)))
                    c['wrong'] += 1
                j += 1
        counts[item] = c
    with open(a.out, 'w') as f:
        f.write('item\tline\tyour_sequence\tfeedback\n')
        for row in rows_out:
            f.write('\t'.join(row) + '\n')
    for item, c in counts.items():
        print('feedback %s: lines read %d, scored %d, unflagged %d, wrong %d, missed %d, extra %d'
              % (item, c['lines_read'], c['scored'], c['unflagged'], c['wrong'], c['missed'], c['extra']))
    print('feedback rows %d -> %s' % (len(rows_out), a.out))


PRE_F = """Before this page you read two other pages of the SAME hand (the same writer, the same sign shapes). Their crops are in
calib/ and your own transcription of them is calib_read.tsv. The file feedback.tsv lists every position where your label was
wrong: your own label sequence around it, your label, and the labels that were allowed there. Study each feedback row against
the crop it comes from in calib/ before you start, so that you recognise those shapes correctly on the new page. Positions
not listed were right or were not checked. Then read the new page below exactly as the brief says.

"""
PRE_C = """Before this page you read two other pages of the SAME hand (the same writer, the same sign shapes). Their crops are in
calib/ and your own transcription of them is calib_read.tsv. Look over them again before you start, so that you recognise
the shapes of this hand on the new page. Then read the new page below exactly as the brief says.

"""


def cmd_target(a):
    os.makedirs(a.out, exist_ok=True)
    cal = os.path.join(a.out, 'calib')
    if os.path.isdir(cal):
        shutil.rmtree(cal)
    shutil.copytree(os.path.join(a.calib_dir, 'calib'), cal)
    shutil.copy(a.calib_read, os.path.join(a.out, 'calib_read.tsv'))
    if a.feedback:
        shutil.copy(a.feedback, os.path.join(a.out, 'feedback.tsv'))
    files = copy_crops(a.crop, os.path.join(a.out, 'target'))
    brief = open(a.brief).read()
    task = ('# Target read\n\n' + (PRE_F if a.feedback else PRE_C)
            + 'The crops of the new page are in target/ (%s). Enlarged copies go inside this folder only. '
              'Open nothing outside this folder. Write your output to %s.\n\n---\n\n' % (', '.join(files), os.path.join(a.out, 'out.tsv'))
            + brief)
    open(os.path.join(a.out, 'task.txt'), 'w').write(task)
    print('target: arm %s, %d target crops, task %s' % ('F' if a.feedback else 'C', len(files), os.path.join(a.out, 'task.txt')))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    sp = ap.add_subparsers(dest='cmd', required=True)
    b = sp.add_parser('build'); b.add_argument('--out', required=True); b.add_argument('--label-brief', required=True)
    b.add_argument('--crop', action='append', required=True); b.add_argument('--notes')
    f = sp.add_parser('feedback'); f.add_argument('--read', required=True); f.add_argument('--truth', action='append', required=True)
    f.add_argument('--out', required=True); f.add_argument('--context', type=int, default=3)
    t = sp.add_parser('target'); t.add_argument('--out', required=True); t.add_argument('--brief', required=True)
    t.add_argument('--calib-dir', required=True); t.add_argument('--calib-read', required=True); t.add_argument('--feedback')
    t.add_argument('--crop', action='append', required=True)
    a = ap.parse_args(argv)
    {'build': cmd_build, 'feedback': cmd_feedback, 'target': cmd_target}[a.cmd](a)
    return 0


if __name__ == '__main__':
    sys.exit(main())
