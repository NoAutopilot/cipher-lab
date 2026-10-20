#!/usr/bin/env python3
"""Decode the Cossit/Summer cypher (BL Add MS 21838 pp.345-347) from Entick, New Spelling Dictionary 1781 (SHERWOOD-READ, 18 Oct 2026).

Convention (gate: 8 anchors, NOTES.md "## Reading from Entick 1781"): a pair P-W is printed page P of Entick 1781
(archive.org 11280377bsb) and the W-th printed line of one of its two columns, counted from the top of the column; a
wrapped continuation line counts. The column is not written, so each pair has two candidates.

Sources: book/entries_image.tsv (the two candidate headwords per pair, read by eye from the scan) and
book/entick_lines.tsv (the OCR line grid for every page, from book/build_entick_lines.py; used where no image read exists,
i.e. the controls). The column is chosen per message by a Viterbi pass over a word-bigram model of the en18 corpus
(tools/data/en18), the same chooser for the reading and for every control.

Grades (rule 4): C = a period gloss written over/under the group on p.347 ("February"); H = the entry read from the book
image and the other column's line is not a headword (a wrapped line), so no choice was made; S = the entry read from the image,
column chosen by the bigram chooser with a margin >= 2.0 nats over the other column; M = margin under 2.0, or OCR only, or a
pair outside the book's range. Clear-text words written in letters in the cypher are listed as clear, not graded.

  python3 decode_entick.py            write reading.tsv and reading.txt
  python3 decode_entick.py --check    exit 1 if the committed reading.tsv/reading.txt are stale (rule 7)
  python3 decode_entick.py --chooser kn3  grade counts under the trigram chooser of mrows.py (prints only)
  python3 decode_entick.py --controls [--seeds 20]   offset W+1/W-1 and P-shuffled controls, OCR-only for all arms
"""
import argparse, csv, gzip, math, os, random, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
EN18 = os.path.join(ROOT, 'tools', 'data', 'en18')
MARGIN = 2.0


def load_tokens():
    """Ciphertext in page order p345, p346, p347, as (line, kind, value) with kind pair|clear|gloss|other."""
    out = []
    for ln in open(os.path.join(HERE, 'ciphertext.tsv'), encoding='utf-8'):
        if ln.startswith('#') or ln.startswith('line\t') or not ln.strip():
            continue
        lid, toks = ln.rstrip('\n').split('\t')
        for t in toks.split():
            m = re.fullmatch(r'(\d+)[-:=.](\d+)(\?)?', t)
            if m:
                out.append((lid, 'pair', (int(m.group(1)), int(m.group(2)), bool(m.group(3)))))
            elif t.startswith('w:'):
                out.append((lid, 'clear', t[2:]))
            elif t.startswith('g:'):
                m = re.fullmatch(r'g:([^@]+)@(\d+)-(\d+)(\?)?', t)
                if m:  # a period word written over the group: decode the group, keep the gloss beside it
                    out.append((lid, 'pair', (int(m.group(2)), int(m.group(3)), bool(m.group(4)), m.group(1))))
                else:
                    out.append((lid, 'gloss', t[2:]))
            else:
                out.append((lid, 'other', t))
    return join_breaks(out)


def join_breaks(out):
    """A bare number ending one line and a bare number opening the next line of the same page are one pair split by the
    line break (p346 L06/L07 '364' '32', L10/L11 '367' '11'). Joined here, explicitly, and graded I (repaired), never
    silently: the transcription keeps them apart."""
    res, i = [], 0
    while i < len(out):
        t = out[i]
        if (t[1] == 'other' and t[2].isdigit() and i + 1 < len(out) and out[i + 1][1] == 'other'
                and out[i + 1][2].isdigit() and out[i + 1][0] != t[0] and out[i + 1][0][:4] == t[0][:4]
                and (i + 2 == len(out) or out[i + 2][0] == out[i + 1][0]) and
                [x for x in out if x[0] == t[0]][-1] is t and [x for x in out if x[0] == out[i + 1][0]][0] is out[i + 1]):
            res.append((t[0], 'pair', (int(t[2]), int(out[i + 1][2]), False, '', True)))
            i += 2
            continue
        res.append(t)
        i += 1
    return res


def messages(tokens):
    """Messages in Sherwood's order (NOTES.md SHERWOOD-PAGES): No.1 = p346 L01-L12 (ends at the clear word read 'the',
    where the next line opens No.2 with 'Advertisement', Sherwood's 'seems to be an advertisement'), No.2 = p346 L13-L19
    (ends 'two'), No.3 = p346 L20 - p347 L01 (ends 'three'), the p347 block below it (glosses, subscription, date), No.4 = p345."""
    def which(lid):
        pg, ln = lid.split('_L')
        n = int(re.match(r'\d+', ln).group())
        if pg == 'p346':
            return 'No.1' if n <= 12 else 'No.2' if n <= 19 else 'No.3'
        if pg == 'p347':
            return 'No.3' if n <= 1 else 'p347 block'
        return 'No.4'
    names = ['No.1', 'No.2', 'No.3', 'p347 block', 'No.4']
    return [(nm, [t for t in tokens if which(t[0]) == nm]) for nm in names]


def load_image_entries():
    e = {}
    for r in csv.reader(open(os.path.join(HERE, 'book', 'entries_image.tsv'), encoding='utf-8'), delimiter='\t',
                        quoting=csv.QUOTE_NONE):
        if not r or r[0].startswith('#') or r[0] == 'page':
            continue
        e[(int(r[0]), int(r[1]))] = (r[2], r[3])
    return e


def load_ocr_grid():
    g = {}
    for r in csv.reader(open(os.path.join(HERE, 'book', 'entick_lines.tsv'), encoding='utf-8'), delimiter='\t',
                        quoting=csv.QUOTE_NONE):
        if r[0] == 'page':
            continue
        g[(int(r[0]), int(r[1]), int(r[2]))] = r[5] if len(r) > 5 else ''
    return g


def ocr_headword(txt):
    m = re.match(r"[^A-Za-z]*([A-Za-z][A-Za-z'’/\"\-]*)", txt or '')
    if not m:
        return ''
    w = re.sub(r"['’/\"]", '', m.group(1)).strip('-')
    return w if len(w) > 1 or w in ('A', 'I') else ''


def norm(w):
    w = w.lower().replace('ſ', 's')
    w = re.sub(r'[^a-z]', '', w.split(',')[0].split(' ')[0])
    return w


class Bigram:
    def __init__(self):
        uni, bi = Counter(), Counter()
        for f in sorted(os.listdir(EN18)):
            if not f.endswith('.gz'):
                continue
            prev = None
            for line in gzip.open(os.path.join(EN18, f), 'rt', encoding='utf-8', errors='ignore'):
                for w in re.findall(r"[a-z]+", line.lower()):
                    uni[w] += 1
                    if prev:
                        bi[(prev, w)] += 1
                    prev = w
        self.uni, self.bi, self.N, self.V = uni, bi, sum(uni.values()), len(uni) + 1

    def p_uni(self, w):
        return math.log((self.uni.get(w, 0) + 0.1) / (self.N + 0.1 * self.V))

    def p(self, a, b):
        # interpolated bigram, lambda 0.6
        pu = math.exp(self.p_uni(b))
        if a and self.uni.get(a):
            pb = self.bi.get((a, b), 0) / self.uni[a]
            return math.log(0.6 * pb + 0.4 * pu)
        return math.log(pu)


def choose(seq, lm):
    """seq: list of candidate lists (one list per position, each [(word, payload), ...]). Viterbi; returns
    chosen indices and the per-position margin (best path through chosen minus best path forced through the other)."""
    n = len(seq)
    if n == 0:
        return [], []
    fw = [dict() for _ in range(n)]
    for i, cands in enumerate(seq):
        for j, (w, _) in enumerate(cands):
            if i == 0:
                fw[i][j] = (lm.p(None, norm(w)), None)
            else:
                best = max(((fw[i - 1][k][0] + lm.p(norm(seq[i - 1][k][0]), norm(w)), k) for k in fw[i - 1]),
                           key=lambda x: x[0])
                fw[i][j] = best
    bw = [dict() for _ in range(n)]
    for j in range(len(seq[-1])):
        bw[-1][j] = 0.0
    for i in range(n - 2, -1, -1):
        for j, (w, _) in enumerate(seq[i]):
            bw[i][j] = max(lm.p(norm(w), norm(seq[i + 1][k][0])) + bw[i + 1][k] for k in bw[i + 1])
    pick, margin = [], []
    for i in range(n):
        tot = {j: fw[i][j][0] + bw[i][j] for j in fw[i]}
        jb = max(tot, key=tot.get)
        others = [tot[j] for j in tot if j != jb]
        pick.append(jb)
        margin.append(tot[jb] - max(others) if others else float('inf'))
    return pick, margin


def candidates(P, W, img, grid, use_image=True):
    """Two candidates for P-W (col1, col2), each (word, source) where source is image|ocr|wrap|none."""
    out = []
    if use_image and (P, W) in img:
        for c in img[(P, W)]:
            if c.startswith('+wrap'):
                out.append(('', 'wrap'))
            else:
                out.append((c, 'image'))
        return out
    for col in (1, 2):
        hw = ocr_headword(grid.get((P, col, W), ''))
        out.append((hw, 'ocr') if hw else ('', 'none'))
    return out


def decode(msgs, img, grid, lm, transform=None, use_image=True, chooser=None):
    rows = []
    for name, toks in msgs:
        pos, seq = [], []
        for t in toks:
            lid, kind, val = t
            if kind != 'pair':
                rows.append([name, lid, kind, val, '', '', '', '', '', ''])
                continue
            P, W, unsure = val[:3]
            gloss = val[3] if len(val) > 3 else ''
            joined = len(val) > 4 and val[4]
            if transform:
                P, W = transform(P, W)
            cands = candidates(P, W, img, grid, use_image)
            live = [(w, (k + 1, s)) for k, (w, s) in enumerate(cands) if w]
            r = [name, lid, 'pair', '%d-%d%s%s' % (val[0], val[1], '?' if unsure else '', ' (joined)' if joined else ''),
                 P, W, '', '', '', gloss]
            rows.append(r)
            if live:
                pos.append((r, live, cands, unsure or joined))
                seq.append(live)
            else:
                r[6], r[7], r[8] = '', '', 'M'
        pick, margin = (chooser or choose)(seq, lm)
        for (r, live, cands, unsure), j, mg in zip(pos, pick, margin):
            w, (col, src) = live[j]
            r[6], r[7] = col, w
            if src == 'ocr':
                g = 'M'
            elif len(live) == 1:
                g = 'H'
            else:
                g = 'S' if mg >= MARGIN else 'M'
            if unsure and g != 'M':
                g = 'M'
            if ' (joined)' in r[3]:
                g = 'I'
            if r[9] and norm(r[9]) == norm(w):
                g = 'C'  # the period interlinear gloss on p.347 reads the same word
            r[8] = g
    # the period gloss on p.347: 138-28 is glossed "February" (C)
    for r in rows:
        if r[2] == 'pair' and r[3].startswith('138-28') and transform is None:
            r[8] = 'C'  # glossed 'February' in the period hand on p.347; the same group closes p.345
    return rows


def lm_score(rows, lm):
    """Mean bigram log-prob per decoded word (en18), within messages: the controls' statistic."""
    tot, n = 0.0, 0
    for name in dict.fromkeys(r[0] for r in rows):
        ws = [norm(r[7]) for r in rows if r[0] == name and r[2] == 'pair' and r[7]]
        for a, b in zip([None] + ws, ws):
            tot += lm.p(a, b)
            n += 1
    return tot / n if n else float('-inf')


def render(rows):
    tsv = ['message\tline\tkind\tgroup\tpage\tW\tcol\tentry\tgrade\tperiod_gloss']
    for r in rows:
        tsv.append('\t'.join(str(x) for x in r))
    txt = []
    for name in dict.fromkeys(r[0] for r in rows):
        ws = []
        for r in rows:
            if r[0] != name:
                continue
            if r[2] == 'pair':
                w = ('%s[%s]' % (r[7], r[8])) if r[7] else '<%s>' % r[3]
                ws.append(w + ('{gloss:%s}' % r[9] if r[9] else ''))
            elif r[2] in ('clear', 'gloss'):
                ws.append('"%s"' % r[3])
            else:
                ws.append(r[3])
        txt.append('%s: %s' % (name, ' '.join(ws)))
    counts = Counter(r[8] for r in rows if r[2] == 'pair')
    txt.append('grades (pairs): ' + ' '.join('%s %d' % (g, counts.get(g, 0)) for g in 'HCSMI'))
    return '\n'.join(tsv) + '\n', '\n'.join(txt) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--controls', action='store_true')
    ap.add_argument('--seeds', type=int, default=20)
    ap.add_argument('--chooser', choices=['bigram', 'kn3'], default='bigram',
                    help='kn3: the Kneser-Ney trigram of mrows.py (SHERWOOD-MROWS, 20 Oct 2026); prints grade counts only, never writes')
    a = ap.parse_args()
    lm = Bigram()
    toks = load_tokens()
    msgs = messages(toks)
    img, grid = load_image_entries(), load_ocr_grid()
    if a.controls:
        out = []
        def arm(label, tf=None, ms=msgs):
            rows = decode(ms, img, grid, lm, tf, use_image=False)
            ws = [r[7] for r in rows if r[2] == 'pair']
            cov = sum(1 for w in ws if w) / len(ws)
            txt = ' '.join(norm(w) for w in ws if w)
            out.append((label, lm_score(rows, lm), cov, txt))
        arm('reading (OCR only)')
        arm('W plus 1', lambda P, W: (P, W + 1))
        arm('W minus 1', lambda P, W: (P, max(W - 1, 1)))
        pairs = [t[2] for t in toks if t[1] == 'pair']
        for s in range(a.seeds):
            rng = random.Random(1000 + s)
            Ps = [p[0] for p in pairs]
            rng.shuffle(Ps)
            mp = {}
            k = 0
            new = []
            for name, tl in msgs:
                nl = []
                for t in tl:
                    if t[1] == 'pair':
                        nl.append((t[0], 'pair', (Ps[k],) + tuple(t[2][1:])))
                        k += 1
                    else:
                        nl.append(t)
                new.append((name, nl))
            # the shuffle is applied by position, so pass the shuffled messages with no transform
            arm('P-shuffle seed %d' % s, None, new)
        os.makedirs(os.path.join(HERE, 'controls'), exist_ok=True)
        with open(os.path.join(HERE, 'controls', 'controls.tsv'), 'w') as f:
            f.write('arm\tmean_bigram_logp\tdecoded_share\n')
            for lab, sc, cov, txt in out:
                f.write('%s\t%.4f\t%.3f\n' % (lab, sc, cov))
                fn = re.sub(r'[^a-z0-9]+', '_', lab.lower()).strip('_') + '.txt'
                open(os.path.join(HERE, 'controls', fn), 'w').write(txt + '\n')
        # the image reading as one lower-case word stream, the judge's input (rule 7; SHERWOOD-FIX, 18 Oct 2026)
        img_rows = decode(msgs, img, grid, lm)
        open(os.path.join(HERE, 'controls', 'reading_image.txt'), 'w').write(
            ' '.join(r[7].lower() for r in img_rows if r[2] == 'pair' and r[7]) + '\n')
        for lab, sc, cov, _ in out:
            print('%-22s %.4f  %.3f' % (lab, sc, cov))
        return
    if a.chooser == 'kn3':
        import mrows
        lm3 = mrows.KN3()
        def ch(seq, _lm):
            return mrows.choose3([[norm(w) for w, _ in c] for c in seq], lm3)
        rows = decode(msgs, img, grid, lm, chooser=ch)
        print(render(rows)[1].splitlines()[-1] + '  (kn3 chooser; committed reading unchanged)')
        return
    rows = decode(msgs, img, grid, lm)
    tsv, txt = render(rows)
    if a.check:
        ok = open(os.path.join(HERE, 'reading.tsv')).read() == tsv and open(os.path.join(HERE, 'reading.txt')).read() == txt
        print('reading current' if ok else 'STALE: reading.tsv/reading.txt differ from a fresh decode')
        sys.exit(0 if ok else 1)
    open(os.path.join(HERE, 'reading.tsv'), 'w').write(tsv)
    open(os.path.join(HERE, 'reading.txt'), 'w').write(txt)
    print(txt)


if __name__ == '__main__':
    main()
