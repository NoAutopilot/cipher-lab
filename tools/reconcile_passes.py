#!/usr/bin/env python3
"""Align two or three blind transcription passes line by line and hand the reconciler only the disagreements.

  python3 tools/reconcile_passes.py passA.tsv passB.tsv [passC.tsv] [--out-dir DIR] [--crops DIR]
          [--method nw|difflib] [--halves] [--line-sub PAT REPL] [--split-chars] [--keep-dots] [--keep-plain] [--rows]

Lesson answered (LEDGER.md, 23-24 Sept 2026): every reconciler (Raince, Gramont, Paleologue) spent its first dollars
recomputing the same alignment before it could look at a single disagreement. Scripts read, models judge: this does
the alignment, the reconciler settles only the listed positions from the image.

Pass formats (detected per file):
  wide  'row<TAB>codes' (or no header): a line id, then the line's signs separated by spaces (fr2980-gramont passes).
  long  header 'line  pos|position  sign|token|group  conf|confidence ...': one sign per row (Danzay, Paleologue,
        Anhalt passes, and any ciphertext.tsv, so a reconciled file can be the third pass). An optional 'gloss'
        column (interlinear plaintext glossed above a token, clair349-style) rides along with its token through
        alignment; if any pass has one, ciphertext_draft.tsv gains a 'gloss' column (majority value per aligned
        column, blank where none) and the printed summary adds a gloss-agreement figure over aligned columns
        where every pass with a token there also wrote a non-blank gloss.
Normalising: a trailing '?' on a sign marks it uncertain (the pass flagged it); confidences M, L, l, low count as
flagged too (lower-case m, 'medium' in the Anhalt and Gramont passes, does not;
--flag-conf sets the list). '.' dots and [PLAIN:...] / w: clear words are dropped unless --keep-dots / --keep-plain. --split-chars
splits each group into single characters (unsegmented digit ciphers). --halves joins 'f30r_L01a' + 'f30r_L01b' into
line 'f30r_L01' (half-line crops).

Alignment: per line, pass B (and C) aligned to pass A, the reference, by Needleman-Wunsch over signs (match +1,
mismatch -1, gap -1), or by difflib's matching blocks with --method difflib (the measure fr2980-gramont
reconcile_f30.py printed). Agreement = aligned columns where every pass has the same sign / columns.

Outputs in --out-dir (default: the folder of the first pass), nothing else is written:
  disagreements.tsv   line, col, A, B[, C], flagged, crop: every column where the passes differ, for the reconciler
  ciphertext_draft.tsv  line, position, sign, confidence, alt, why: the agreed sign with H; where the passes differ,
                      the majority sign (or A's) with M and the others in alt; agreed but flagged by a pass -> M
  agreement.tsv       line, signs per pass, agreeing columns, columns, share
Prints the per-line table with --rows, always the overall figure. Exit 0.

Test: python3 tools/tests/test_reconcile_passes.py (Gramont f.30 passes reproduce reconcile_f30.py's 1195/2010; the
Danzay f.36 passes against the reconciled line reproduce the reconciler's 9/25 and 13/25).
"""
import argparse, collections, difflib, os, re, sys

FLAG_CONF = {'M', 'L', 'l', 'low', '?'}


def norm_sign(t, a):
    """(sign, flagged) or None when the token is dropped."""
    if t.startswith('[PLAIN:') or t.startswith('w:'):
        return (t, False) if a.keep_plain else None
    if t == '.' and not a.keep_dots:
        return None
    if t in ('', '-'):
        return None
    flagged = t.endswith('?') and t != '[?]'
    return t.rstrip('?') if flagged else t, flagged


def load_pass(path, a):
    """OrderedDict line -> list of (sign, flagged, gloss); gloss is '' where the pass has no gloss column."""
    rows = [l.rstrip('\n').split('\t') for l in open(path, encoding='utf-8') if l.strip() and not l.startswith('#')]
    out = collections.OrderedDict()
    head = rows[0] if rows else []
    long_fmt = head and head[0] == 'line' and len(head) >= 3
    has_gloss = False
    if long_fmt:
        ci = head.index('line')
        pi = next(head.index(n) for n in ('pos', 'position', 'index') if n in head)
        si = next(head.index(n) for n in ('sign', 'token', 'group', 'code') if n in head)
        ki = next((head.index(n) for n in ('conf', 'confidence') if n in head), None)
        gi = head.index('gloss') if 'gloss' in head else None
        has_gloss = gi is not None
        body = sorted(((r[ci], int(r[pi]), i, r) for i, r in enumerate(rows[1:]) if len(r) > si),
                      key=lambda x: x[2])
        for ln, _, _, r in body:
            conf = r[ki] if ki is not None and ki < len(r) else ''
            gloss = r[gi].strip() if gi is not None and gi < len(r) else ''
            toks = list(r[si]) if a.split_chars and not r[si].startswith('[') else [r[si]]
            for t in toks:
                s = norm_sign(t, a)
                if s:
                    out.setdefault(line_key(ln, a), []).append((s[0], s[1] or conf in a.flag, gloss))
    else:
        for r in rows:
            if r[0] in ('row', 'line'):
                continue
            out.setdefault(line_key(r[0], a), [])
            for t in (r[1].split() if len(r) > 1 else []):
                for c in (list(t.rstrip('?')) if a.split_chars else [t]):
                    s = norm_sign(c if not a.split_chars else c + ('?' if t.endswith('?') else ''), a)
                    if s:
                        out[line_key(r[0], a)].append((s[0], s[1], ''))
    return out, has_gloss


def line_key(ln, a):
    for pat, rep in a.line_sub or []:
        ln = re.sub(pat, rep, ln)
    return re.sub(r'(\d)[ab]$', r'\1', ln) if a.halves else ln


def nw(x, y):
    """Needleman-Wunsch: list of (i, j) index pairs, None for a gap."""
    n, m = len(x), len(y)
    S = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        S[i][0] = -i
    for j in range(1, m + 1):
        S[0][j] = -j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            S[i][j] = max(S[i - 1][j - 1] + (1 if x[i - 1] == y[j - 1] else -1), S[i - 1][j] - 1, S[i][j - 1] - 1)
    i, j, path = n, m, []
    while i or j:
        if i and j and S[i][j] == S[i - 1][j - 1] + (1 if x[i - 1] == y[j - 1] else -1):
            path.append((i - 1, j - 1)); i -= 1; j -= 1
        elif i and S[i][j] == S[i - 1][j] - 1:
            path.append((i - 1, None)); i -= 1
        else:
            path.append((None, j - 1)); j -= 1
    return path[::-1]


def dl(x, y):
    """difflib alignment as (i, j) pairs: matching blocks and replace runs paired, the rest as gaps."""
    pairs = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, x, y, autojunk=False).get_opcodes():
        k = min(i2 - i1, j2 - j1) if tag in ('equal', 'replace') else 0
        pairs += [(i1 + t, j1 + t) for t in range(k)]
        pairs += [(i, None) for i in range(i1 + k, i2)] + [(None, j) for j in range(j1 + k, j2)]
    return pairs


def columns(seqs, method):
    """Star alignment on seqs[0]: list of columns, each a list (one entry per pass) of (sign, flagged) or None."""
    ref = seqs[0]
    cols = [[r] + [None] * (len(seqs) - 1) for r in ref]
    extra = collections.defaultdict(list)          # insertions relative to ref, keyed by the ref index they follow
    for p, s in enumerate(seqs[1:], 1):
        f = nw if method == 'nw' else dl
        last = -1
        for i, j in f([c[0] for c in ref], [c[0] for c in s]):
            if i is not None:
                cols[i][p] = s[j] if j is not None else None; last = i
            else:
                col = [None] * len(seqs); col[p] = s[j]; extra[last].append(col)
    out = extra.get(-1, [])
    for i, c in enumerate(cols):
        out.append(c); out += extra.get(i, [])
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('passes', nargs='+', help='two or three pass files; the first is the reference')
    ap.add_argument('--out-dir'); ap.add_argument('--crops', help='folder of line crops, matched by line id prefix')
    ap.add_argument('--method', choices=('nw', 'difflib'), default='nw')
    ap.add_argument('--halves', action='store_true'); ap.add_argument('--split-chars', action='store_true')
    ap.add_argument('--keep-dots', action='store_true'); ap.add_argument('--keep-plain', action='store_true')
    ap.add_argument('--line-sub', nargs=2, action='append', metavar=('PATTERN', 'REPL'),
                    help="regex applied to every line id, e.g. --line-sub '^36' '' (repeatable)")
    ap.add_argument('--flag-conf', default=','.join(sorted(FLAG_CONF)), help='confidences that flag a sign')
    ap.add_argument('--rows', action='store_true', help='print one line per manuscript line')
    ap.add_argument('--no-write', action='store_true', help='print only (used by the test)')
    a = ap.parse_args(argv)
    a.flag = set(a.flag_conf.split(','))
    if not 2 <= len(a.passes) <= 3:
        ap.error('give two or three pass files')
    loaded = [load_pass(p, a) for p in a.passes]
    P = [d for d, _ in loaded]
    any_gloss = any(hg for _, hg in loaded)
    names = 'ABC'[:len(P)]
    lines = list(P[0]) + [l for p in P[1:] for l in p if l not in P[0]]
    lines = list(dict.fromkeys(lines))
    crops = sorted(os.listdir(a.crops)) if a.crops and os.path.isdir(a.crops) else []
    dis, draft, agr_rows = [], [], []
    tot_agree = tot_cols = 0
    tot_gloss_agree = tot_gloss_cols = 0
    for ln in lines:
        seqs = [p.get(ln, []) for p in P]
        cols = columns(seqs, a.method)
        agree = sum(1 for c in cols if all(x is not None for x in c) and len({x[0] for x in c}) == 1)
        if a.method == 'difflib' and len(P) == 2:
            n = max(len(seqs[0]), len(seqs[1]))        # the measure reconcile_f30.py printed
        else:
            n = len(cols)
        tot_agree += agree; tot_cols += n
        agr_rows.append((ln, [len(s) for s in seqs], agree, n))
        crop = ','.join(os.path.join(a.crops, f) for f in crops if f.startswith(ln)) if crops else ''
        pos = 0
        for k, c in enumerate(cols, 1):
            signs = [x[0] if x else '-' for x in c]
            flagged = [n_ for n_, x in zip(names, c) if x and x[1]]
            present = [s for s in signs if s != '-']
            same = len(set(signs)) == 1
            if not same:
                dis.append([ln, str(k)] + signs + [''.join(flagged), crop])
            if not present:
                continue
            best = collections.Counter(present).most_common()
            sign = best[0][0] if len(best) == 1 or best[0][1] > best[1][1] else (signs[0] if signs[0] != '-' else best[0][0])
            pos += 1
            why = ('agree' if not flagged else 'agree-flagged') if same else ('gap' if '-' in signs else 'differ')
            conf = 'H' if why == 'agree' else 'M'
            alt = '/'.join(f'{n_}:{s}' for n_, s in zip(names, signs) if s != sign) if not same else ''
            if any_gloss:
                glosses = [x[2] if x else None for x in c]     # None = no token here in that pass, '' = token, no gloss
                non_gap = [g for g in glosses if g is not None]
                if len(non_gap) == len(c) and all(non_gap):     # every pass has a token here AND wrote a gloss
                    tot_gloss_cols += 1
                    if len(set(non_gap)) == 1:
                        tot_gloss_agree += 1
                present_g = [g for g in glosses if g]
                if present_g:
                    gbest = collections.Counter(present_g).most_common()
                    gloss = gbest[0][0] if len(gbest) == 1 or gbest[0][1] > gbest[1][1] else present_g[0]
                else:
                    gloss = ''
                draft.append([ln, str(pos), sign, gloss, conf, alt, why])
            else:
                draft.append([ln, str(pos), sign, conf, alt, why])
    share = tot_agree / tot_cols if tot_cols else 1
    if a.rows:
        for ln, ns, ag, n in agr_rows:
            print(ln, *ns, ag, n, f'{ag / n:.2f}' if n else '1.00', sep='\t')
    print(f"lines {len(lines)}  signs " + '  '.join(f'{n_} {sum(r[1][i] for r in agr_rows)}' for i, n_ in enumerate(names))
          + f"  agree {tot_agree}/{tot_cols} = {share:.1%}  ({a.method})")
    print(f"disagreement columns {len(dis)}; draft signs {len(draft)}, of which M {sum(1 for d in draft if d[-3] == 'M')}")
    if any_gloss:
        gshare = tot_gloss_agree / tot_gloss_cols if tot_gloss_cols else 1
        print(f"gloss agreement (aligned columns where every pass wrote a gloss): "
              f"{tot_gloss_agree}/{tot_gloss_cols} = {gshare:.1%}")
    if a.no_write:
        return dict(agree=tot_agree, cols=tot_cols, rows=agr_rows, dis=dis, draft=draft,
                     gloss_agree=tot_gloss_agree, gloss_cols=tot_gloss_cols)
    out = a.out_dir or os.path.dirname(os.path.abspath(a.passes[0]))
    os.makedirs(out, exist_ok=True)
    def w(name, head, rows):
        with open(os.path.join(out, name), 'w', encoding='utf-8') as f:
            f.write('\t'.join(head) + '\n' + ''.join('\t'.join(r) + '\n' for r in rows))
    w('disagreements.tsv', ['line', 'col'] + list(names) + ['flagged', 'crop'], dis)
    draft_head = ['line', 'position', 'sign', 'gloss', 'confidence', 'alt', 'why'] if any_gloss else \
                 ['line', 'position', 'sign', 'confidence', 'alt', 'why']
    w('ciphertext_draft.tsv', draft_head, draft)
    w('agreement.tsv', ['line'] + [f'signs_{n_}' for n_ in names] + ['agree', 'columns', 'share'],
      [[ln] + [str(x) for x in ns] + [str(ag), str(n), f'{ag / n:.3f}' if n else '1.000'] for ln, ns, ag, n in agr_rows])
    print('wrote', ', '.join(os.path.join(out, f) for f in ('disagreements.tsv', 'ciphertext_draft.tsv', 'agreement.tsv')))
    return 0


if __name__ == '__main__':
    r = main()
    sys.exit(r if isinstance(r, int) else 0)
