#!/usr/bin/env python3
"""Align two or more blind transcription passes line by line and hand the reconciler only the disagreements.

  python3 tools/reconcile_passes.py passA.tsv passB.tsv [passC.tsv] [--out-dir DIR] [--crops DIR]
          [--method nw|difflib] [--halves] [--line-sub PAT REPL] [--split-chars] [--keep-dots] [--keep-plain] [--rows]
          [--sign-map FILE] [--vote] [--err-truth TRUTH.tsv]

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
Confidence (REC-CONF, 27 Sept 2026, after an outside review of this pipeline found lower-case 'm' and 'medium'
passed through unflagged and every agreed sign was written H whatever the passes actually said): every pass's raw
confidence label is normalised to H/M/L before use -- case-insensitive high/h -> H, medium/med/m -> M, low/l -> L;
a blank label -> M and is counted in the summary; any other non-empty label is a fatal error naming the file, the
manuscript line and the label, and exits non-zero (never silently treated as confident). A pass with no confidence
column at all (the Gramont wide format) defaults every sign to H, unchanged from before. A trailing '?' on a sign
still marks it uncertain and caps its normalised confidence at M (it can only lower a level, never raise one).
--flag-conf (default M,L) sets which of the normalised H/M/L levels count as "flagged" for the
disagreements/uncertain 'flagged' column and the 'agree'/'agree-flagged' why value; it no longer takes raw labels.
An agreed sign's confidence in ciphertext_draft.tsv is the LOWER of the passes' normalised confidences (H > M > L),
not always H; an agreed sign whose lower confidence is M or L also lands in uncertain.tsv (disagreements.tsv's
columns plus both_conf), so the reconciler's review queue is disagreements.tsv PLUS uncertain.tsv, not
disagreements.tsv alone. '.' dots and [PLAIN:...] / w: clear words are dropped unless --keep-dots / --keep-plain.
--split-chars splits each group into single characters (unsegmented digit ciphers). --halves joins 'f30r_L01a' +
'f30r_L01b' into line 'f30r_L01' (half-line crops). --sign-map FILE reads a glyph-convention table (header
pass_reading, canonical, plus any other columns, e.g. evidence/count/grade -- ignored here) and substitutes each
pass token's exact reading for its canonical value before alignment, applied to every pass equally
(malsburg-hessen-1636's bMALG glyph_map.tsv: a reading pass calling the same stroke 'i' in one line and '1' in
another stops looking like a disagreement).

Alignment: per line, pass B (and C) aligned to pass A, the reference, by Needleman-Wunsch over signs (match +1,
mismatch -1, gap -1), or by difflib's matching blocks with --method difflib (the measure fr2980-gramont
reconcile_f30.py printed). Agreement = aligned columns where every pass has the same sign / columns.

Outputs in --out-dir (default: the folder of the first pass), nothing else is written:
  disagreements.tsv   line, col, A, B[, C], flagged, crop: every column where the passes differ, for the reconciler
  uncertain.tsv        line, col, A, B[, C], flagged, crop, both_conf: agreed columns whose lower confidence is M
                      or L -- part of the review queue alongside disagreements.tsv, never folded into a silent H
  ciphertext_draft.tsv  line, position, sign, confidence, alt, why: the agreed sign at the lower pass confidence
                      (H only when every pass genuinely read it H); where the passes differ, the majority sign
                      (or A's) with M and the others in alt
  agreement.tsv       line, signs per pass, agreeing columns, columns, share
Prints the per-line table with --rows, always the overall figure and an agreed-H / agreed-uncertain / disagree
line. Exit 0 (a bad confidence label exits non-zero before any output is written).

N passes and voting (TX-VIEWS, 4 Oct 2026; research/TRANSCRIPTION-PRACTICE-2026-10-04.md #1, #10): any number of passes
(two or more; more than three are named A, B, C, D ... in the outputs), typically one blind read per view written by
tools/iiif_lines.py --views. --vote also writes vote.tsv (line, pos, sign, vote_share, votes, n_passes): per aligned
column the plurality sign, emitted only when more passes have a sign there than a gap (a gap is a vote for "no sign"),
a sign tie going to the earliest pass; vote_share = passes reading the emitted sign / all passes, so a 3-of-5 sign reads
0.60. vote.tsv is in tools/tx_bench.py's format. The star alignment is on pass A, so put the strongest plain read first.
--err-truth TRUTH.tsv (a benchmark truth file: line, pos, ref_sign, truth, status) scores every pass (and the vote) per
scored truth position with tools/tx_bench.py's position_errors and writes err_corr.tsv, one row per pair of passes:
errors of each, errors shared, shared with the SAME wrong sign, phi (the correlation of the two 0/1 error indicators
over the positions both cover) and repeat = shared / errors of the first; low phi marks the pass pairs whose errors
cancel in a vote (arXiv 2509.09722: the least-correlated views helped most). Without a truth file no correlation is
reported: agreement with the consensus is not accuracy (LESSONS.md "Look-alike pass").

Test: python3 tools/tests/test_reconcile_passes.py (N-pass vote and err_corr: tools/tests/test_reconcile_vote.py) (Gramont f.30 passes reproduce reconcile_f30.py's 1195/2010; the
Danzay f.36 passes against the reconciled line reproduce the reconciler's 9/25 and 13/25; medium/m/unknown-label
and an agreed M/M sign landing in uncertain.tsv are covered by the REC-CONF cases).
"""
import argparse, collections, difflib, os, re, sys

FLAG_CONF = {'M', 'L'}
CONF_ALIASES = {'h': 'H', 'high': 'H', 'm': 'M', 'med': 'M', 'medium': 'M', 'l': 'L', 'low': 'L'}
CONF_RANK = {'H': 3, 'M': 2, 'L': 1}


def norm_conf(label, path, line_id):
    """Normalise a raw confidence label to H/M/L. Blank -> M. Anything else not in CONF_ALIASES is a fatal error
    (never silently treated as confident) naming the file, the manuscript line and the label."""
    if label == '':
        return 'M'
    key = label.strip().lower()
    if key in CONF_ALIASES:
        return CONF_ALIASES[key]
    sys.exit(f"reconcile_passes.py: {path}: line {line_id}: unrecognised confidence label {label!r} "
             f"(expected high/h, medium/med/m, low/l, or blank)")


def norm_sign(t, a):
    """(sign, flagged) or None when the token is dropped."""
    if t.startswith('[PLAIN:') or t.startswith('w:'):
        return (t, False) if a.keep_plain else None
    if t == '.' and not a.keep_dots:
        return None
    if t in ('', '-'):
        return None
    flagged = t.endswith('?') and t != '[?]'
    sign = t.rstrip('?') if flagged else t
    sign_map = getattr(a, 'sign_map', None)
    if sign_map:
        sign = sign_map.get(sign, sign)
    return sign, flagged


def load_sign_map(path):
    """pass_reading -> canonical, from a TSV with header pass_reading, canonical, ... (extra columns ignored)."""
    rows = [l.rstrip('\n').split('\t') for l in open(path, encoding='utf-8') if l.strip() and not l.startswith('#')]
    head = rows[0]
    pi, ci = head.index('pass_reading'), head.index('canonical')
    return {r[pi]: r[ci] for r in rows[1:] if len(r) > max(pi, ci) and r[ci]}


def load_pass(path, a):
    """OrderedDict line -> list of (sign, level, gloss), level one of H/M/L (norm_conf); gloss is '' where the
    pass has no gloss column."""
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
            raw_conf = r[ki] if ki is not None and ki < len(r) else None
            level = norm_conf(raw_conf, path, ln) if raw_conf is not None else 'H'
            gloss = r[gi].strip() if gi is not None and gi < len(r) else ''
            toks = list(r[si]) if a.split_chars and not r[si].startswith('[') else [r[si]]
            for t in toks:
                s = norm_sign(t, a)
                if s:
                    sign, sign_flagged = s
                    lv = 'M' if sign_flagged and level == 'H' else level
                    out.setdefault(line_key(ln, a), []).append((sign, lv, gloss))
    else:
        for r in rows:
            if r[0] in ('row', 'line'):
                continue
            out.setdefault(line_key(r[0], a), [])
            for t in (r[1].split() if len(r) > 1 else []):
                for c in (list(t.rstrip('?')) if a.split_chars else [t]):
                    s = norm_sign(c if not a.split_chars else c + ('?' if t.endswith('?') else ''), a)
                    if s:
                        sign, sign_flagged = s
                        out[line_key(r[0], a)].append((sign, 'M' if sign_flagged else 'H', ''))
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
    """Star alignment on seqs[0]: list of columns, each a list (one entry per pass) of (sign, level, gloss) or None."""
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


CORR_HEAD = ['pass_i', 'pass_j', 'positions', 'err_i', 'err_j', 'both', 'same_wrong', 'phi', 'repeat_i_in_j']


def err_corr(a, P, names, vote_rows=None):
    """Pairwise error correlation of the passes (and the vote) on the scored positions of a benchmark truth file."""
    import math
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import tx_bench
    truth = tx_bench.read_tsv(a.err_truth)
    seqs = {n_: {ln: [x[0] for x in v] for ln, v in p.items()} for n_, p in zip(names, P)}
    if vote_rows is not None:
        vl = collections.OrderedDict()
        for ln, _, sg, *_ in vote_rows:
            vl.setdefault(ln, []).append(sg)
        seqs['vote'] = vl
    errs, reads = {}, {}
    for n_, lines in seqs.items():
        errs[n_] = tx_bench.position_errors(truth, lines)
        # the sign each pass put on each truth position (for "same wrong sign")
        by_line = collections.defaultdict(list)
        for r in truth:
            by_line[r['line']].append(r)
        rd_ = {}
        for ln, rows in by_line.items():
            if ln not in lines:
                continue
            rows.sort(key=lambda r: float(r['pos']))
            ts = [set(filter(None, r['truth'].split('|'))) for r in rows]
            for ri, osg in tx_bench.align([r['ref_sign'] for r in rows], ts, lines[ln]):
                if ri is not None:
                    rd_[(ln, rows[ri]['pos'])] = osg
        reads[n_] = rd_
    out, keys = [], list(seqs)
    for i, p in enumerate(keys):
        e = errs[p]
        print(f"err_truth {p} ({a.passes[i] if i < len(a.passes) else 'vote'}): {sum(e.values())}/{len(e)} scored positions wrong")
    for i, p in enumerate(keys):
        for q in keys[i + 1:]:
            common = sorted(set(errs[p]) & set(errs[q]))
            x = [errs[p][k] for k in common]; y = [errs[q][k] for k in common]
            n = len(common); ex, ey = sum(x), sum(y)
            both = sum(1 for u, v in zip(x, y) if u and v)
            same = sum(1 for k in common if errs[p][k] and errs[q][k] and reads[p].get(k) == reads[q].get(k))
            den = math.sqrt(ex * (n - ex) * ey * (n - ey)) if n else 0
            phi = (n * both - ex * ey) / den if den else float('nan')
            out.append([p, q, n, ex, ey, both, same, round(phi, 3), round(both / ex, 3) if ex else float('nan')])
    print('err_corr (pass_i pass_j positions err_i err_j both same_wrong phi repeat_i_in_j):')
    for r in out:
        print('  ' + '\t'.join(map(str, r)))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('passes', nargs='+', help='two or more pass files; the first is the reference')
    ap.add_argument('--out-dir'); ap.add_argument('--crops', help='folder of line crops, matched by line id prefix')
    ap.add_argument('--method', choices=('nw', 'difflib'), default='nw')
    ap.add_argument('--halves', action='store_true'); ap.add_argument('--split-chars', action='store_true')
    ap.add_argument('--keep-dots', action='store_true'); ap.add_argument('--keep-plain', action='store_true')
    ap.add_argument('--line-sub', nargs=2, action='append', metavar=('PATTERN', 'REPL'),
                    help="regex applied to every line id, e.g. --line-sub '^36' '' (repeatable)")
    ap.add_argument('--flag-conf', default=','.join(sorted(FLAG_CONF)),
                     help='normalised confidence levels (subset of H,M,L) that mark a sign flagged')
    ap.add_argument('--rows', action='store_true', help='print one line per manuscript line')
    ap.add_argument('--no-write', action='store_true', help='print only (used by the test)')
    ap.add_argument('--sign-map', dest='sign_map_file',
                     help='TSV pass_reading<TAB>canonical[...]; substitutes each raw pass token before alignment')
    ap.add_argument('--vote', action='store_true', help='also write vote.tsv: plurality sign and vote share per column')
    ap.add_argument('--err-truth', help='benchmark truth TSV: write err_corr.tsv (pairwise error correlation of passes)')
    a = ap.parse_args(argv)
    a.flag = set(a.flag_conf.split(','))
    a.sign_map = load_sign_map(a.sign_map_file) if a.sign_map_file else {}
    if len(a.passes) < 2:
        ap.error('give two or more pass files')
    if len(a.passes) > 26:
        ap.error('at most 26 passes')
    loaded = [load_pass(p, a) for p in a.passes]
    P = [d for d, _ in loaded]
    any_gloss = any(hg for _, hg in loaded)
    names = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:len(P)]
    votes = []
    lines = list(P[0]) + [l for p in P[1:] for l in p if l not in P[0]]
    lines = list(dict.fromkeys(lines))
    crops = sorted(os.listdir(a.crops)) if a.crops and os.path.isdir(a.crops) else []
    dis, draft, uncertain, agr_rows = [], [], [], []
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
            levels = [x[1] if x else None for x in c]
            if a.vote:
                pres = [s_ for s_ in signs if s_ != '-']
                if len(pres) > len(signs) - len(pres):
                    cnt = collections.Counter(pres)
                    top = max(cnt.values())
                    vs = next(s_ for s_ in signs if s_ != '-' and cnt[s_] == top)
                    votes.append([ln, vs, top, len(signs)])
            flagged = [n_ for n_, lv in zip(names, levels) if lv in a.flag]
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
            conf = min(levels, key=lambda lv: CONF_RANK[lv]) if same else 'M'
            alt = '/'.join(f'{n_}:{s}' for n_, s in zip(names, signs) if s != sign) if not same else ''
            if same and conf != 'H':
                both_conf = '/'.join(f'{n_}:{lv}' for n_, lv in zip(names, levels))
                uncertain.append([ln, str(k)] + signs + [''.join(flagged), crop, both_conf])
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
    agreed_h = sum(1 for d in draft if d[-1] in ('agree', 'agree-flagged') and d[-3] == 'H')
    print(f"disagreement columns {len(dis)}; draft signs {len(draft)}")
    print(f"agreed-H {agreed_h}  agreed-uncertain {len(uncertain)}  disagree {len(dis)}")
    if any_gloss:
        gshare = tot_gloss_agree / tot_gloss_cols if tot_gloss_cols else 1
        print(f"gloss agreement (aligned columns where every pass wrote a gloss): "
              f"{tot_gloss_agree}/{tot_gloss_cols} = {gshare:.1%}")
    vote_rows, pos_by_line = [], collections.Counter()
    for ln, vs, top, n_ in votes:
        pos_by_line[ln] += 1
        vote_rows.append([ln, str(pos_by_line[ln]), vs, f'{top / n_:.2f}', str(top), str(n_)])
    if a.vote:
        low = sum(1 for r in vote_rows if int(r[4]) * 2 <= int(r[5]))
        print(f"vote: {len(vote_rows)} signs from {len(P)} passes; mean vote share "
              f"{(sum(float(r[3]) for r in vote_rows) / len(vote_rows)) if vote_rows else 0:.3f}; "
              f"{low} signs at or below half the passes")
    corr_rows = []
    if a.err_truth:
        corr_rows = err_corr(a, P, names, vote_rows if a.vote else None)
    if a.no_write:
        return dict(votes=vote_rows, err_corr=corr_rows, agree=tot_agree, cols=tot_cols, rows=agr_rows, dis=dis, draft=draft, uncertain=uncertain,
                     agreed_h=agreed_h, gloss_agree=tot_gloss_agree, gloss_cols=tot_gloss_cols)
    out = a.out_dir or os.path.dirname(os.path.abspath(a.passes[0]))
    os.makedirs(out, exist_ok=True)
    def w(name, head, rows):
        with open(os.path.join(out, name), 'w', encoding='utf-8') as f:
            f.write('\t'.join(head) + '\n' + ''.join('\t'.join(r) + '\n' for r in rows))
    w('disagreements.tsv', ['line', 'col'] + list(names) + ['flagged', 'crop'], dis)
    w('uncertain.tsv', ['line', 'col'] + list(names) + ['flagged', 'crop', 'both_conf'], uncertain)
    draft_head = ['line', 'position', 'sign', 'gloss', 'confidence', 'alt', 'why'] if any_gloss else \
                 ['line', 'position', 'sign', 'confidence', 'alt', 'why']
    w('ciphertext_draft.tsv', draft_head, draft)
    w('agreement.tsv', ['line'] + [f'signs_{n_}' for n_ in names] + ['agree', 'columns', 'share'],
      [[ln] + [str(x) for x in ns] + [str(ag), str(n), f'{ag / n:.3f}' if n else '1.000'] for ln, ns, ag, n in agr_rows])
    written = ['disagreements.tsv', 'uncertain.tsv', 'ciphertext_draft.tsv', 'agreement.tsv']
    if a.vote:
        w('vote.tsv', ['line', 'pos', 'sign', 'vote_share', 'votes', 'n_passes'], vote_rows); written.append('vote.tsv')
    if a.err_truth:
        w('err_corr.tsv', CORR_HEAD, [[str(x) for x in r] for r in corr_rows]); written.append('err_corr.tsv')
    print('wrote', ', '.join(os.path.join(out, f) for f in written))
    return 0


if __name__ == '__main__':
    r = main()
    sys.exit(r if isinstance(r, int) else 0)
