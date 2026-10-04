#!/usr/bin/env python3
"""A2-HAR5 (2 Oct 2026): align the R8491 f.84r / R8494 f.90r interlinear glosses to their cipher signs with
tools/interlinear_align.py (--code-prefix mode: every sign takes 0 or 1 gloss letters), then a shuffled-alignment
control (rule 3): the same run with each cipher line paired to another line's gloss (derangement, 20 seeds).
A2-HAR6 added a second, length-preserving control: each pair keeps its own gloss with the letters shuffled (20 seeds).

Input: gloss_pairs.tsv (reconciled two-pass transcription; committed before this script was run).
Statistic: key consistency = sum over signs with n>=2 of (count of its majority letter) / sum of n.
           known-answer concordance = share of signs (n>=3) whose majority letter is one of the values
           Bourdeau's cobham1588/signs.tsv gives that shape on other glossed leaves (SIGNS_TSV below).
The control can differ from the target on both: re-pairing changes which letters sit over which signs.

    python3 run_align.py [--check]     # --check: exit 1 if the committed key_f84_f90.tsv / control.tsv are stale
RUN1-HAR (4 Oct 2026): --pairs FILE (default gloss_pairs.tsv), --page f84r (keep only that page's rows) and --suffix S
(write control{S}.tsv, key{S}.tsv, align{S}.tsv instead of the committed A2-HAR7 names), for the gloss-masked control
(PREREG_masked.md). With none of the three the run is identical to A2-HAR7's.
"""
import csv, os, random, subprocess, sys, tempfile
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
TOOL = os.path.join(ROOT, 'tools', 'interlinear_align.py')
PAIRS = os.path.join(HERE, 'gloss_pairs.tsv')
SEEDS = 20
# shape code -> letters Bourdeau gives that shape (cobham1588 runs.txt legend / signs.tsv, cyphersolver)
# A2-HAR6 (3 Oct 2026): replaced A2-HAR5's undocumented shape code with Bourdeau's documented ASCII code (the legend of
# solver/runs_bourdeau.txt, l.3-10), the code PASS_PROMPT.md gives the transcription passes.
SIGNS_TSV = {'U': 'a', 'A': 'sta', '+': 'b', '8': 'c', 'D': 'd', 'T': 'dt', '7': 'e', 'H': 'f', 'G': 'g', 'h': 'h',
             'I': 'iay', 'k': 'k', 'l': 'lt', 'm': 'm', '#': 'mn', 'n': 'n', 'z': 'o', 'd': 'o', 'c': 'oae', 'p': 'p',
             'V': 'r', 'y': 'ry', ':': 'uv', 'w': 'w', 'X': 'i', 'Q': 'ar', 'L': 'e'}
ALIGN_ARGS = ['--code-prefix', '@', '--wildcard', '?', '--null-cost', '-1.5', '--keep-fs']


def opt(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


def load():
    with open(opt('--pairs', PAIRS), encoding='utf-8') as f:
        rows = [r for r in csv.DictReader(f, delimiter='\t') if r['gloss'] not in ('', '-')]
    page = opt('--page')
    return [r for r in rows if r['page'] == page] if page else rows


UNK = [0]


def cipher_raw(s):
    out = []
    for t in s.split():
        if t in ('/', '.'):
            continue
        if t.startswith('{clear:'):
            out.append(t[7:-1])
        elif t == '?':
            UNK[0] += 1
            out.append('@?%d' % UNK[0])  # singleton code: takes a letter, never counted as evidence
        else:
            out.append('@' + t)
    return ' '.join(out)


def run(rows, glosses, tag):
    UNK[0] = 0
    d = tempfile.mkdtemp()
    p = os.path.join(d, 'pairs.tsv')
    with open(p, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['plain_line', 'plain_raw', 'cipher_line', 'cipher_raw'])
        for r, g in zip(rows, glosses):
            lid = '%s_%s_%s' % (r['page'], r['band'], r['pair'])
            w.writerow([lid, g, lid, cipher_raw(r['cipher'])])
    ka, kk = os.path.join(d, 'align.tsv'), os.path.join(d, 'key.tsv')
    subprocess.run([sys.executable, TOOL, 'align', p, ka, kk] + ALIGN_ARGS, check=True, capture_output=True)
    with open(kk, encoding='utf-8') as f:
        key = [r for r in csv.DictReader(f, delimiter='\t') if not r['value'].startswith('?')]
    return key, ka


def stats(key):
    multi = [r for r in key if int(r['n']) >= 2]
    n = sum(int(r['n']) for r in multi)
    agree = sum(int(r['agree']) for r in multi)
    ka = [r for r in key if int(r['n']) >= 3 and r['value'] in SIGNS_TSV]
    conc = sum(1 for r in ka if r['meaning'].lower()[:1] in SIGNS_TSV[r['value']] and len(r['meaning']) == 1)
    return (agree / n if n else 0.0), (conc / len(ka) if ka else 0.0), len(ka)


def derange(n, rng):
    while True:
        idx = list(range(n))
        rng.shuffle(idx)
        if all(i != j for i, j in enumerate(idx)):
            return idx


def main():
    rows = load()
    key, ka = run(rows, [r['gloss'] for r in rows], 'real')
    cons, conc, nka = stats(key)
    out = ['run\tseed\tconsistency\tconcordance\tn_signs_ge3']
    out.append('real\t-\t%.3f\t%.3f\t%d' % (cons, conc, nka))
    ctl = []
    for s in range(SEEDS):
        idx = derange(len(rows), random.Random(s))
        k2, _ = run(rows, [rows[i]['gloss'] for i in idx], 'shuf')
        c2 = stats(k2)
        ctl.append(c2)
        out.append('shuffled\t%d\t%.3f\t%.3f\t%d' % (s, c2[0], c2[1], c2[2]))
    ctl2 = []  # A2-HAR6: length-preserving null -- each pair keeps its own gloss, letters shuffled within it
    for s in range(SEEDS):
        rng = random.Random(1000 + s)
        g2 = []
        for r in rows:
            letters = [ch for ch in r['gloss'] if ch != ' ']
            rng.shuffle(letters)
            g2.append(''.join(letters))
        k3, _ = run(rows, g2, 'lshuf')
        c3 = stats(k3)
        ctl2.append(c3)
        out.append('letter_shuffled\t%d\t%.3f\t%.3f\t%d' % (s, c3[0], c3[1], c3[2]))
    keylines = ['value\tmeaning\tn\tagree\tothers\tsigns_tsv'] + [
        '\t'.join([r['value'], r['meaning'], r['n'], r['agree'], r['others'], SIGNS_TSV.get(r['value'], '-')])
        for r in key]
    with open(ka, encoding='utf-8') as f:
        aligntxt = f.read()
    files = {'control.tsv': '\n'.join(out) + '\n', 'key_f84_f90.tsv': '\n'.join(keylines) + '\n',
             'align_f84_f90.tsv': aligntxt}
    suf = opt('--suffix')
    if suf:
        files = {'control%s.tsv' % suf: files['control.tsv'], 'key%s.tsv' % suf: files['key_f84_f90.tsv'],
                 'align%s.tsv' % suf: files['align_f84_f90.tsv']}
    if '--check' in sys.argv:
        stale = [n for n, t in files.items() if open(os.path.join(HERE, n), encoding='utf-8').read() != t]
        print('stale: %s' % stale if stale else 'check ok')
        sys.exit(1 if stale else 0)
    for n, t in files.items():
        with open(os.path.join(HERE, n), 'w', encoding='utf-8') as f:
            f.write(t)
    cs = sorted(c[0] for c in ctl); cc = sorted(c[1] for c in ctl)
    print('real consistency %.3f concordance %.3f (%d signs n>=3)' % (cons, conc, nka))
    print('shuffled consistency mean %.3f p95 %.3f; concordance mean %.3f p95 %.3f' % (
        sum(cs) / len(cs), cs[int(0.95 * len(cs)) - 1], sum(cc) / len(cc), cc[int(0.95 * len(cc)) - 1]))
    ls = sorted(c[0] for c in ctl2); lc = sorted(c[1] for c in ctl2)
    print('letter-shuffled consistency mean %.3f max %.3f; concordance mean %.3f max %.3f' % (
        sum(ls) / len(ls), ls[-1], sum(lc) / len(lc), lc[-1]))
    print('pair-shuffled max consistency %.3f concordance %.3f' % (cs[-1], cc[-1]))


if __name__ == '__main__':
    main()
