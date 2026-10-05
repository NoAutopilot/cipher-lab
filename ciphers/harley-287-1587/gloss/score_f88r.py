#!/usr/bin/env python3
"""Score the two blind f.88r sign-by-sign passes (A4-RFHAR, 5 Oct 2026), as pre-registered in PREREG_f88r.md.

  python3 gloss/score_f88r.py [--check]

Reads gloss/passA_f88r.tsv and gloss/passB_f88r.tsv (columns band, pair, before, cipher, after, notes; cipher = one
token per sign, " / " between cipher words). Writes gloss/f88r_recon.tsv (mechanical reconciliation, no eye
arbitration: agreed tokens kept, every split or gap -> ?) and gloss/score_f88r.txt. --check exits 1 if the committed
outputs differ from a fresh run (rule 7).

Statistics (all pre-registered):
  err_2reader  token disagreements / aligned tokens, A vs B, per band (difflib on tokens).
  L            share of eligible cipher words (3-10 signs, >= half of them core signs) whose core-letter pattern
               (non-core signs and ? as one-letter wildcards) matches >= 1 word of the same length among the 30,000
               most frequent of solver/wordfreq.tsv (Bourdeau's word list).
  control      L under 1000 random permutations of the letter sets among the 12 core signs (seed 88); the control can
               differ from the target because it changes which letter each core sign carries, which is exactly what
               the pattern test reads.
  bourdeau     reported, not gated: for each of Bourdeau's f88 runs (solver/runs_bourdeau.txt), the share of its signs
               matched in the reconciled page string by difflib, against the same with each run's tokens shuffled.
"""
import difflib, random, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CORE = {'#': 'n', '+': 'b', '7': 'e', '8': 'c', 'A': 'st', 'D': 'd', 'G': 'g', 'H': 'f', 'U': 'a', 'z': 'o', 'd': 'o',
        'y': 'ry'}


def read_pass(p):
    rows = []
    for ln in Path(p).read_text().splitlines()[1:]:
        f = ln.split('\t')
        if len(f) < 4:
            continue
        rows.append((f[0].strip(), f[3].strip()))
    bands = {}
    for band, cipher in rows:
        if cipher in ('', '-'):
            continue
        bands.setdefault(band, []).append(cipher)
    return {b: ' / '.join(v) for b, v in bands.items()}


def toks(s):
    return s.split()


def reconcile(a, b):
    ta, tb = toks(a), toks(b)
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    out, dis, n = [], 0, 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            out += ta[i1:i2]
            n += i2 - i1
        else:
            k = max(i2 - i1, j2 - j1)
            n += k
            seg_a = [t for t in ta[i1:i2] if t != '/']
            seg_b = [t for t in tb[j1:j2] if t != '/']
            dis += k
            out += ['?'] * max(len(seg_a), len(seg_b))
            if '/' in ta[i1:i2] and '/' in tb[j1:j2]:
                out.append('/')
    return ' '.join(out), dis, n


def words(s):
    return [w.split() for w in s.split('/') if w.split()]


def lexicon():
    by_len = {}
    for i, ln in enumerate((ROOT / 'solver/wordfreq.tsv').read_text().splitlines()):
        if i >= 30000:
            break
        w = ln.split('\t')[0].lower()
        if w.isalpha():
            by_len.setdefault(len(w), set()).add(w)
    return by_len


def eligible(ws):
    return [w for w in ws if 3 <= len(w) <= 10 and sum(t in CORE for t in w) * 2 >= len(w)]


def pattern(w, key):
    return re.compile('^' + ''.join('[%s]' % key[t] if t in key else '.' for t in w) + '$')


def score_L(ws, key, lex):
    hits = 0
    for w in ws:
        rx = pattern(w, key)
        if any(rx.match(x) for x in lex.get(len(w), ())):
            hits += 1
    return hits / len(ws) if ws else 0.0


def main():
    A = read_pass(HERE / 'passA_f88r.tsv')
    B = read_pass(HERE / 'passB_f88r.tsv')
    lex = lexicon()
    lines, recon, dis_t, n_t = [], {}, 0, 0
    for band in sorted(set(A) | set(B)):
        r, d, n = reconcile(A.get(band, ''), B.get(band, ''))
        recon[band] = r
        dis_t += d
        n_t += n
    rec_tsv = 'band\tcipher\n' + ''.join('%s\t%s\n' % (b, recon[b]) for b in sorted(recon))
    err = dis_t / n_t if n_t else 1.0
    lines.append('err_2reader = %d / %d = %.3f' % (dis_t, n_t, err))
    ws = eligible([w for b in sorted(recon) for w in words(recon[b])])
    L = score_L(ws, CORE, lex)
    LA = score_L(eligible([w for b in sorted(A) for w in words(A[b])]), CORE, lex)
    LB = score_L(eligible([w for b in sorted(B) for w in words(B[b])]), CORE, lex)
    rng = random.Random(88)
    signs, vals = list(CORE), list(CORE.values())
    ctrl = []
    for _ in range(1000):
        v = vals[:]
        rng.shuffle(v)
        ctrl.append(score_L(ws, dict(zip(signs, v)), lex))
    ctrl.sort()
    p95 = ctrl[949]
    p = sum(c >= L for c in ctrl) / len(ctrl)
    lines.append('eligible words (reconciled) = %d; L = %.3f; control mean %.3f p95 %.3f max %.3f; p = %.3f'
                 % (len(ws), L, sum(ctrl) / len(ctrl), p95, ctrl[-1], p))
    lines.append('per pass L: A %.3f, B %.3f' % (LA, LB))
    lines.append('G1 (err_2reader <= 0.30): %s' % ('PASS' if err <= 0.30 else 'FAIL'))
    lines.append('G2 (L > control p95): %s' % ('PASS' if L > p95 else 'FAIL'))
    # Bourdeau comparison, reported only
    page = ' '.join(recon[b] for b in sorted(recon)).replace('/', ' ').split()
    tot = m = mc = 0
    rng2 = random.Random(7)
    for ln in (ROOT / 'solver/runs_bourdeau.txt').read_text().splitlines():
        if not ln.startswith('f88'):
            continue
        run = ln.split('|')[2].split()
        run = [t for w in run for t in (re.findall(r'\[[^\]]*\]|.', w))]
        tot += len(run)
        m += sum(x.size for x in difflib.SequenceMatcher(None, run, page, autojunk=False).get_matching_blocks())
        acc = 0
        for _ in range(20):
            s = run[:]
            rng2.shuffle(s)
            acc += sum(x.size for x in difflib.SequenceMatcher(None, s, page, autojunk=False).get_matching_blocks())
        mc += acc / 20
    lines.append('bourdeau f88 runs: %d signs; matched in reconciled page %d (%.3f); shuffled-run control %.1f (%.3f)'
                 % (tot, m, m / tot if tot else 0, mc, mc / tot if tot else 0))
    uniq = []
    for w in ws:
        rx = pattern(w, CORE)
        c = [x for x in lex.get(len(w), ()) if rx.match(x)]
        if len(c) == 1:
            uniq.append('%s=%s' % (''.join(w), c[0]))
    lines.append('words with exactly one lexicon match (grade M candidates, not readings): ' + ', '.join(uniq))
    txt = '\n'.join(lines) + '\n'
    if '--check' in sys.argv:
        ok = (HERE / 'f88r_recon.tsv').read_text() == rec_tsv and (HERE / 'score_f88r.txt').read_text() == txt
        print('check ok' if ok else 'STALE')
        sys.exit(0 if ok else 1)
    (HERE / 'f88r_recon.tsv').write_text(rec_tsv)
    (HERE / 'score_f88r.txt').write_text(txt)
    print(txt, end='')


if __name__ == '__main__':
    main()
