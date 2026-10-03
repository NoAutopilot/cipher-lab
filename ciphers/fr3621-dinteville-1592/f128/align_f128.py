#!/usr/bin/env python3
"""f.128r (BnF fr.3621 no.114) interlinear gloss -> period key, with a rotated-gloss control (rule 3).

    python3 ciphers/fr3621-dinteville-1592/f128/align_f128.py [--syl] [--check]

--syl: variant 2, declared before it was run (3 Oct 2026): each sign may take 0-3 gloss letters (numeral codes >=
floor, --max-chunk 3, --seg-bonus 0, --len-prior 1.0, --null-cost -1.0; with --null-cost 0 every sign went null and
the plain letters were all skipped, a degenerate run with no counts); writes the *_syl.tsv files.

Reads gloss_pairs.tsv (the reconciled sign-by-sign transcription: one row per gloss word with the cipher signs
under it), builds PAIRS for tools/interlinear_align.py in --code-prefix mode (every sign is one code taking 0 or 1
gloss letters; --null-cost 0 so dots and nulls are free; f and s kept apart), runs the hard-EM alignment, and writes
pairs.tsv, align.tsv, key.tsv (value -> meaning, counts) and control.tsv.

Statistic: consistency = sum over sign types seen aligned >= 2 times of (count of the type's top letter) / (number
of those aligned occurrences). Control: the gloss letters of all aligned words are concatenated and rotated by k
(k = 1..len-1, every rotation, deterministic), then re-split into the original words, so every gloss word keeps
its length and place and the passage keeps its letter frequencies; only the sign/letter correspondence is broken. The
control CAN differ from the target on this statistic (it changes which letter each sign sits under).

Grades per token (rule 4): C = the sign's aligned letter agrees with its type's top letter seen >= 2 times
(read from the period gloss); M = singleton type, or conflict with the type's top letter, or null/unaligned;
'?' signs are excluded. --check: exit 1 if key.tsv / align.tsv on disk differ from a fresh run (rule 7).
"""
import csv, io, os, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import interlinear_align as ia  # noqa: E402

ia.FOLD_FS = False  # manuscript gloss read by eye: keep f and s apart (--keep-fs)
PFX = '@'


def load_rows():
    with open(os.path.join(HERE, 'gloss_pairs.tsv'), encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter='\t'))


SYL = '--syl' in sys.argv  # variant 2 (declared before running it): a sign may take 0-3 gloss letters
CODES = {}


def tok(sign):
    if not SYL:
        return PFX + sign
    return str(CODES.setdefault(sign, 100 + len(CODES)))  # numeral >= floor 100: a chunk of 0..max_chunk letters


def build_pairs(rows, glosses=None):
    pairs = []
    k = 0
    for r in rows:
        g = r['gloss'].strip()
        if not g or g == '-' or g.startswith('CLEAR:') or not r['signs'].strip():
            continue
        plain = glosses[k] if glosses is not None else g
        k += 1
        pairs.append({'plain_line': r['line'], 'plain_raw': plain, 'cipher_line': '%s.%s' % (r['line'], r['order']),
                      'cipher_raw': ' '.join(tok(s) for s in r['signs'].split())})
    return pairs


def run(pairs):
    if SYL:
        prepared, results, counts, shown = ia.run_align(pairs, floor=100, null_cost=-1.0, wildcard='+', max_chunk=3,
                                                        seg_bonus=0.0, len_prior=1.0)
        return prepared, results, counts, shown
    prepared, results, counts, shown = ia.run_align(pairs, code_prefix=PFX, null_cost=0.0, wildcard='+')
    return prepared, results, counts, shown


def consistency(counts):
    tot = top = 0
    for v, cnt in counts.items():
        if name(v) == '?':
            continue
        n = sum(cnt.values())
        if n >= 2:
            tot += n
            top += max(cnt.values())
    return (top / tot if tot else 0.0), tot


def name(v):
    if not SYL:
        return v
    inv = {str(c): k for k, c in CODES.items()}
    return inv.get(str(v), str(v))


def letters_of(g):
    return ia.plain_letters(g, '+')[0]


def outputs():
    rows = load_rows()
    pairs = build_pairs(rows)
    prepared, results, counts, shown = run(pairs)
    trows = ia.token_rows(prepared, results, counts, shown)
    real_c, real_n = consistency(counts)
    # grades
    out_align = io.StringIO()
    w = csv.writer(out_align, delimiter='\t', lineterminator='\n')
    w.writerow(['cipher_line', 'idx', 'sign', 'plain_chunk', 'status', 'grade'])
    grades = Counter()
    for cl, idx, raw, kind, value, repair, chunk, status in trows:
        value = name(value) if value != '' else value
        if value == '?':
            g = '-'
        elif status == 'agrees':
            g = 'C'
        else:
            g = 'M'
        grades[g] += 1
        w.writerow([cl, idx, value, chunk, status, g])
    out_key = io.StringIO()
    w = csv.writer(out_key, delimiter='\t', lineterminator='\n')
    w.writerow(['sign', 'meaning', 'n', 'agree', 'others'])
    for v in sorted(counts):
        cnt = counts[v]
        top, topn = ia.top_of(cnt)
        rest = sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))[1:]
        w.writerow([name(v), top, sum(cnt.values()), topn, ','.join('%s:%d' % (m, c) for m, c in rest)])
    # control: every rotation of the concatenated gloss letters, re-split into the original word lengths
    # word structure kept: every gloss word keeps its length and place (the aligner's word-boundary bonus is
    # unchanged); only the letters move
    words = [[letters_of(w) for w in p['plain_raw'].split()] for p in pairs]
    cat = ''.join(''.join(ws) for ws in words)
    null = []
    for k in range(1, len(cat)):
        rot = cat[k:] + cat[:k]
        gl, pos = [], 0
        for ws in words:
            out = []
            for w in ws:
                out.append(rot[pos:pos + len(w)])
                pos += len(w)
            gl.append(' '.join(out))
        c, _ = consistency(run(build_pairs(rows, gl))[2])
        null.append(c)
    null.sort()
    mean = sum(null) / len(null)
    p95 = null[int(0.95 * (len(null) - 1))]
    ge = sum(1 for x in null if x >= real_c)
    out_ctl = io.StringIO()
    w = csv.writer(out_ctl, delimiter='\t', lineterminator='\n')
    w.writerow(['statistic', 'real', 'real_n_occ', 'null_rotations', 'null_mean', 'null_p95', 'null_max', 'null_ge_real'])
    w.writerow(['consistency', '%.3f' % real_c, real_n, len(null), '%.3f' % mean, '%.3f' % p95, '%.3f' % null[-1], ge])
    out_pairs = io.StringIO()
    w = csv.writer(out_pairs, delimiter='\t', lineterminator='\n')
    w.writerow(['plain_line', 'plain_raw', 'cipher_line', 'cipher_raw'])
    for p in pairs:
        w.writerow([p['plain_line'], p['plain_raw'], p['cipher_line'], p['cipher_raw']])
    summary = ('pairs %d; aligned tokens %d; grades %s; sign types %d; consistency real %.3f on %d occ vs rotated-gloss '
               'null mean %.3f p95 %.3f max %.3f (%d rotations, %d >= real)'
               % (len(pairs), len(trows), dict(grades), len(counts), real_c, real_n, mean, p95, null[-1], len(null), ge))
    sfx = '_syl' if SYL else ''
    summary = ('variant %s: ' % ('syllabic (0-3 letters per sign)' if SYL else 'letter (0-1 letter per sign)')) + summary
    return {'pairs%s.tsv' % sfx: out_pairs.getvalue(), 'align%s.tsv' % sfx: out_align.getvalue(),
            'key%s.tsv' % sfx: out_key.getvalue(), 'control%s.tsv' % sfx: out_ctl.getvalue()}, summary


def main():
    files, summary = outputs()
    if '--check' in sys.argv:
        stale = [n for n, t in files.items()
                 if not os.path.exists(os.path.join(HERE, n)) or open(os.path.join(HERE, n), encoding='utf-8').read() != t]
        print(summary)
        if stale:
            print('STALE: %s' % ', '.join(stale))
            sys.exit(1)
        print('check: committed outputs match')
        return
    for n, t in files.items():
        with open(os.path.join(HERE, n), 'w', encoding='utf-8') as f:
            f.write(t)
    print(summary)


if __name__ == '__main__':
    main()
