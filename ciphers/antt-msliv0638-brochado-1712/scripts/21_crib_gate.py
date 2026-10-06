"""R11A-BRO (6 Oct 2026): the pre-registered paraphrase-crib gate of PREREG-R11A-BRO.md, nothing more.
T(text) = number of distinct 5-grams of the letter-134 candidate's C-graded runs (reading_body_tokens.tsv) found in the
folded text. Target = each neighbouring leaf's transcription (crib_m0272.txt, crib_m0277.txt, crib_m0278.txt; one Sonnet
pass each, grade M); control = length-matched windows (stride 25) of the appendix's period Deciffrada prose
(plaintext_appendix.tsv deciffrada_line, Cartas 13-123). Leaf PASS: T > control p(1-0.05/3) and T >= 3.
Writes crib_gate.tsv; exit 0 always (a FAIL is a result). `--check` exits 1 if crib_gate.tsv is stale."""
import csv, random, re, sys, unicodedata
ROOT = '/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712'
K, ALPHA = 5, 0.05 / 3


def fold(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if 'a' <= c <= 'z')
    return s.translate(str.maketrans('vjy', 'uii'))


def runs():
    rows = [r for r in csv.DictReader(open(f'{ROOT}/reading_body_tokens.tsv'), delimiter='\t')
            if r['line'] in ('m0275-r1', 'm0276-r1', 'm0276-r2')]
    out = {'A': [[]], 'B': [[]]}
    for r in rows:
        span = 'B' if r['line'] == 'm0276-r2' else 'A'
        if r['grade'] == 'C' and fold(r['value']):
            out[span][-1].append(fold(r['value']))
        elif out[span][-1]:
            out[span].append([])
    return [''.join(x) for v in out.values() for x in v if len(x) >= K], rows


def grams(strings):
    return {s[i:i + K] for s in strings for i in range(len(s) - K + 1)}


def T(g, text):
    return sorted(x for x in g if x in text)


def quantile(xs, q):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(q * len(xs)))]


def main():
    cruns, rows = runs()
    g = grams(cruns)
    letters = ''.join(fold(r['value']) for r in rows if fold(r['value']))
    rnd = random.Random(7); sh = list(letters); rnd.shuffle(sh)
    gsh = grams([''.join(sh)])
    ctrl = fold(' '.join(r['deciffrada_line'] for r in csv.DictReader(open(f'{ROOT}/plaintext_appendix.tsv'), delimiter='\t')))
    out = [['leaf', 'L', 'T', 'hits', 'ctrl_windows', 'ctrl_len', 'ctrl_repeated', 'ctrl_median', 'ctrl_q', 'ctrl_max',
            'T_shuffled_candidate', 'ctrl_q_shuffled', 'verdict']]
    out.insert(0, [f'# candidate C-runs (>= {K}): ' + ' '.join(cruns) + f'; distinct {K}-grams: {len(g)}'])
    anyp = False
    for leaf in ('m0272', 'm0277', 'm0278'):
        text = fold(''.join(l for l in open(f'{ROOT}/crib_{leaf}.txt') if not l.startswith('#')))
        L = len(text)
        src, rep = ctrl, 'no'
        if L > len(ctrl):
            src, rep = ctrl + ctrl, 'yes'
        wins = [src[i:i + L] for i in range(0, len(src) - L + 1, 25)] or [src[:L]]
        cv = [len(T(g, w)) for w in wins]
        cvs = [len(T(gsh, w)) for w in wins]
        t = T(g, text)
        q = quantile(cv, 1 - ALPHA)
        ok = len(t) > q and len(t) >= 3
        anyp |= ok
        out.append([leaf, L, len(t), ' '.join(t), len(wins), len(ctrl), rep, quantile(cv, 0.5), q, max(cv),
                    len(T(gsh, text)), quantile(cvs, 1 - ALPHA), 'PASS' if ok else 'FAIL'])
    out.append([f'# gate: {"PASS" if anyp else "FAIL"} (any leaf T > control p{100 * (1 - ALPHA):.2f} and T >= 3)'])
    txt = '\n'.join('\t'.join(map(str, r)) for r in out) + '\n'
    p = f'{ROOT}/crib_gate.tsv'
    if '--check' in sys.argv:
        stale = open(p).read() != txt
        print('crib_gate.tsv stale' if stale else 'crib_gate.tsv up to date'); sys.exit(1 if stale else 0)
    open(p, 'w').write(txt); print(txt)


if __name__ == '__main__':
    main()
