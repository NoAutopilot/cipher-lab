#!/usr/bin/env python3
"""Rule-4a depth statistics for one item of a graded reading (DEPTH-MH, 8 Oct 2026).

Reads a reading-tokens TSV (line, pos, sign, conf, value, grade; as written by tools/decode_key.py) and the key TSV
(code, value, grade, ...), and computes, for the depth bar in .claude/briefs/runs/2026-10-08-acct3-depth-bar.md:

  1. grade runs: longest contiguous H/C/S run in letters (primary: cipher-class tokens only, a code-class token breaks
     the run; secondary: code-class H/C/S tokens let through and counted), per line and over the item;
  2. AD = 1.5 x H(K)/R, H(K) = distinct cipher-class codes in the item x log2(V) + liberties (M: log2(max(2, alts)),
     U: log2(V)), R = log2(26) - held-out per-letter cross-entropy of an interpolated char 5-gram on the corpus;
     also AD at R = 3.4 (sensitivity);
  3. code-class codes occurring >= 2 times, contexts deduplicated by the 3 codes either side (verbatim repeat = once);
  4. control (i): longest decoded stretch that segments fully into corpus words (len >= 2, count >= 5, plus a, y);
  5. control (ii): per recurring code and context, mean log2 P per letter of an 8+value+8 letter window
     (sensitivity: the 8+8 flanks alone, the value's own letters gapped out);
  (4) and (5) on the target and on N value-shuffled keys (within classes with --shuffle classes, over all codes
  with --shuffle all). Grade runs and recurrence counts do not depend on the key and get no shuffle control.

Scope: built for nomenclator/homophonic readings whose tokens file carries one key code per row. It catches
"a stretch above AD exists / does not" and "a code reads in >= 2 contexts above shuffle"; it must NOT be used to
grade a reading (it never changes grades) or as a judge of the plaintext (no PASS/FAIL against real prose).

Usage:
  python3 tools/depth_stats.py --tokens T.tsv --key K.tsv --line-prefix PFX [--exclude-prefix X]
      --cipher-class code<=120 | len<=3  --shuffle classes|all  --seeds 8100-8299  --out DIR
      [--corpus tools/data/fr18]
Writes DIR/summary.json, DIR/runs.tsv, DIR/contexts.tsv and prints a short report.
"""
import argparse, collections, glob, gzip, json, math, os, random, sys, unicodedata


def fold(s):
    s = unicodedata.normalize('NFKD', s.lower())
    return ''.join(c for c in s if 'a' <= c <= 'z')


def first_alt(v):
    return v.split('|')[0]


def load_corpus(d):
    lines = []
    for p in sorted(glob.glob(os.path.join(d, '*.txt.gz'))):
        with gzip.open(p, 'rt', encoding='utf-8', errors='replace') as f:
            lines.extend(f.read().splitlines())
    return lines


class NGram:
    """Interpolated character n-gram (Jelinek-Mercer, fixed lambdas), a-z only."""
    def __init__(self, text, n=5):
        self.n = n
        self.c = [collections.Counter() for _ in range(n + 1)]
        for k in range(1, n + 1):
            cc = self.c[k]
            for i in range(len(text) - k + 1):
                cc[text[i:i + k]] += 1
        self.tot = sum(self.c[1].values())
        self.lam = [0, 0.05, 0.1, 0.15, 0.3, 0.4][:n + 1]

    def p(self, ctx, ch):
        pr = self.lam[1] * (self.c[1][ch] + 1) / (self.tot + 26)
        for k in range(2, self.n + 1):
            h = ctx[-(k - 1):] if k - 1 <= len(ctx) else None
            if h is None:
                pr += self.lam[k] * (self.c[1][ch] + 1) / (self.tot + 26)
                continue
            d = self.c[k - 1][h]
            pr += self.lam[k] * (self.c[k][h + ch] / d if d else (self.c[1][ch] + 1) / (self.tot + 26))
        return pr

    def logp_seq(self, s):
        """s may contain '|' gaps; context does not cross a gap. Returns (sum log2 p, n scored)."""
        tot, n, ctx = 0.0, 0, ''
        for ch in s:
            if ch == '|':
                ctx = ''
                continue
            tot += math.log2(self.p(ctx, ch)); n += 1
            ctx = (ctx + ch)[-(self.n - 1):]
        return tot, n


def longest_segmentable(s, words, maxw=20):
    """Longest substring of s (no gaps) that splits completely into words."""
    n = len(s); best = [0] * (n + 1)
    for j in range(n - 1, -1, -1):
        b = 0
        for L in range(1, min(maxw, n - j) + 1):
            if s[j:j + L] in words:
                b = max(b, L + best[j + L])
        best[j] = b
    return max(best) if n else 0


def stat_i(letters, words):
    return max((longest_segmentable(seg, words) for seg in letters.split('|')), default=0)


def build_stream(vals):
    """vals: list of letter strings or None (gap). Returns stream with '|' gaps and per-token (start, end)."""
    out, spans, pos = [], [], 0
    for v in vals:
        if v is None:
            out.append('|'); spans.append((pos, pos)); pos += 1
        else:
            out.append(v); spans.append((pos, pos + len(v))); pos += len(v)
    return ''.join(out), spans


def window(stream, span, k=8):
    a, b = span
    i, got = a, 0
    while i > 0 and got < k:
        i -= 1
        if stream[i] != '|':
            got += 1
    j, got = b, 0
    while j < len(stream) and got < k:
        if stream[j] != '|':
            got += 1
        j += 1
    return stream[i:j]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--tokens', required=True); ap.add_argument('--key', required=True)
    ap.add_argument('--line-prefix', default=''); ap.add_argument('--exclude-prefix', default=None)
    ap.add_argument('--cipher-class', required=True, help='code<=N or len<=N')
    ap.add_argument('--shuffle', choices=['classes', 'all'], required=True)
    ap.add_argument('--seeds', default='8100-8299'); ap.add_argument('--out', required=True)
    ap.add_argument('--corpus', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'fr18'))
    a = ap.parse_args(argv)

    key = {}
    for i, ln in enumerate(open(a.key, encoding='utf-8')):
        f = ln.rstrip('\n').split('\t')
        if i == 0 or len(f) < 2:
            continue
        key[f[0].strip()] = f[1]
    kind, lim = a.cipher_class.split('<=')
    lim = int(lim)

    def is_cipher(code, value):
        if kind == 'code':
            try:
                return int(code) <= lim
            except ValueError:
                return True
        return len(fold(first_alt(value))) <= lim

    toks = []
    for i, ln in enumerate(open(a.tokens, encoding='utf-8')):
        f = ln.rstrip('\n').split('\t')
        if i == 0 or len(f) < 6:
            continue
        line, pos, sign, conf, value, grade = f[:6]
        if not line.startswith(a.line_prefix):
            continue
        if a.exclude_prefix and line.startswith(a.exclude_prefix):
            continue
        sign = sign.strip().rstrip('?')
        toks.append(dict(line=line, sign=sign, value=value, grade=grade))
    for t in toks:
        t['cls'] = 'cipher' if is_cipher(t['sign'], key.get(t['sign'], t['value'])) else 'code'
        t['letters'] = None if t['grade'] == 'U' else fold(first_alt(t['value']))

    # 1. grade runs
    def runs(allow_code):
        best, cur, cur_line_best, per_line, prev_line = (0, None), 0, collections.Counter(), {}, None
        start = 0
        for idx, t in enumerate(toks):
            ok = t['grade'] in 'HCS' and t['grade'] != '' and (t['cls'] == 'cipher' or allow_code)
            if ok:
                if cur == 0:
                    start = idx
                cur += len(t['letters'] or '')
                if cur > best[0]:
                    best = (cur, (start, idx))
            else:
                cur = 0
        # per line (no crossing)
        for ln_ in dict.fromkeys(t['line'] for t in toks):
            c = b = 0
            for t in toks:
                if t['line'] != ln_:
                    continue
                if t['grade'] in 'HCS' and t['grade'] and (t['cls'] == 'cipher' or allow_code):
                    c += len(t['letters'] or ''); b = max(b, c)
                else:
                    c = 0
            per_line[ln_] = b
        return best, per_line
    (prim, prim_span), prim_lines = runs(False)
    (sec, sec_span), sec_lines = runs(True)

    def span_text(sp):
        if not sp:
            return ''
        return ' '.join(toks[k]['value'] for k in range(sp[0], sp[1] + 1))

    # 2. AD
    lines = load_corpus(a.corpus)
    train = fold(' '.join(l for i, l in enumerate(lines) if i % 10))
    held = fold(' '.join(l for i, l in enumerate(lines) if i % 10 == 0))
    model = NGram(train)
    lp, nn = model.logp_seq(held[:200000])
    H = -lp / nn; R = math.log2(26) - H
    if not train or R <= 0:
        sys.exit('depth_stats: corpus too small for a held-out R (need many lines)')
    cvals = {fold(first_alt(v)) for c, v in key.items() if is_cipher(c, v) and fold(first_alt(v))}
    V = len(cvals)
    dcodes = {t['sign'] for t in toks if t['cls'] == 'cipher' and t['grade'] != 'U'}
    Hdes = len(dcodes) * math.log2(V)
    Hlib = 0.0
    for t in toks:
        if t['grade'] == 'M':
            Hlib += math.log2(max(2, len(t['value'].split('|'))))
        elif t['grade'] == 'U':
            Hlib += math.log2(V)
    HK = Hdes + Hlib
    AD = 1.5 * HK / R; AD34 = 1.5 * HK / 3.4

    # word list
    wc = collections.Counter()
    for l in lines:
        for w in l.replace("'", ' ').replace('’', ' ').split():
            fw = fold(w)
            if fw:
                wc[fw] += 1
    words = {w for w, c in wc.items() if len(w) >= 2 and c >= 5} | {'a', 'y'}

    # 3. recurring code-class codes, dedup contexts
    occ = collections.defaultdict(list)
    for idx, t in enumerate(toks):
        if t['cls'] == 'code' and t['grade'] != 'U':
            occ[t['sign']].append(idx)
    rec = {}
    for code, idxs in occ.items():
        if len(idxs) < 2:
            continue
        seen, uniq = set(), []
        for idx in idxs:
            ctx = (tuple(toks[k]['sign'] for k in range(max(0, idx - 3), idx)),
                   tuple(toks[k]['sign'] for k in range(idx + 1, min(len(toks), idx + 4))))
            if ctx in seen:
                continue
            seen.add(ctx); uniq.append(idx)
        rec[code] = dict(n_occ=len(idxs), contexts=uniq)

    # target decode
    def decode_with(kmap):
        vals = []
        for t in toks:
            if t['grade'] == 'U':
                vals.append(None)
            elif kmap is None:
                vals.append(t['letters'])
            else:
                vals.append(fold(first_alt(kmap.get(t['sign'], t['value']))))
        return build_stream(vals)

    def ctx_scores(stream, spans):
        out = {}
        for code, r in rec.items():
            for idx in r['contexts']:
                w = window(stream, spans[idx])
                s, n = model.logp_seq(w)
                a_, b_ = spans[idx]
                fl = window(stream[:a_] + '|' * (b_ - a_) + stream[b_:], (a_, b_))
                s2, n2 = model.logp_seq(fl)
                out[(code, idx)] = (s / n if n else float('-inf'), w, s2 / n2 if n2 else float('-inf'))
        return out

    st, sp = decode_with(None)
    tgt_i = stat_i(st, words)
    tgt_ii = ctx_scores(st, sp)

    lo, hi = (int(x) for x in a.seeds.split('-'))
    codes = list(key)
    cls_of = {c: ('cipher' if is_cipher(c, v) else 'code') for c, v in key.items()}
    sh_i, sh_ii, sh_fl = [], collections.defaultdict(list), collections.defaultdict(list)
    for seed in range(lo, hi + 1):
        rng = random.Random(seed)
        km = {}
        groups = [codes] if a.shuffle == 'all' else [[c for c in codes if cls_of[c] == g] for g in ('cipher', 'code')]
        for g in groups:
            vs = [key[c] for c in g]; rng.shuffle(vs); km.update(zip(g, vs))
        s2, sp2 = decode_with(km)
        sh_i.append(stat_i(s2, words))
        for k, (v, _, fv) in ctx_scores(s2, sp2).items():
            sh_ii[k].append(v); sh_fl[k].append(fv)

    def p95(xs):
        xs = sorted(xs); return xs[int(0.95 * len(xs)) - 1]
    os.makedirs(a.out, exist_ok=True)
    rows = []
    for (code, idx), (v, w, fv) in sorted(tgt_ii.items(), key=lambda kv: (kv[0][0], kv[0][1])):
        sh = sh_ii[(code, idx)]; shf = sh_fl[(code, idx)]
        rows.append(dict(code=code, value=toks[idx]['value'], grade=toks[idx]['grade'], line=toks[idx]['line'],
                         window=w, target=round(v, 3), shuffle_p95=round(p95(sh), 3), shuffle_max=round(max(sh), 3),
                         above_p95=v > p95(sh), flanks=round(fv, 3), flanks_p95=round(p95(shf), 3),
                         flanks_above=fv > p95(shf),
                         context=' '.join(toks[k]['value'] for k in range(max(0, idx - 4), min(len(toks), idx + 5)))))
    with open(os.path.join(a.out, 'contexts.tsv'), 'w', encoding='utf-8') as f:
        f.write('code\tvalue\tgrade\tline\ttarget\tshuffle_p95\tshuffle_max\tabove_p95\tflanks\tflanks_p95\tflanks_above\twindow\tcontext\n')
        for r in rows:
            f.write('\t'.join(str(r[k]) for k in ('code', 'value', 'grade', 'line', 'target', 'shuffle_p95',
                                                     'shuffle_max', 'above_p95', 'flanks', 'flanks_p95', 'flanks_above', 'window', 'context')) + '\n')
    with open(os.path.join(a.out, 'runs.tsv'), 'w', encoding='utf-8') as f:
        f.write('line\tprimary_letters\tsecondary_letters\n')
        for ln_ in prim_lines:
            f.write(f'{ln_}\t{prim_lines[ln_]}\t{sec_lines[ln_]}\n')
    g = collections.Counter(t['grade'] for t in toks)
    summ = dict(tokens=len(toks), grades=dict(g), hcs=sum(g[x] for x in 'HCS'),
                hcs_pct=round(100 * sum(g[x] for x in 'HCS') / len(toks), 1),
                primary_run=prim, primary_run_text=span_text(prim_span),
                secondary_run=sec, secondary_run_text=span_text(sec_span),
                H_model_bits=round(H, 3), R=round(R, 3), V=V, distinct_cipher_codes=len(dcodes),
                H_design=round(Hdes, 1), H_lib=round(Hlib, 1), H_K=round(HK, 1), unicity=round(HK / R, 1),
                AD=round(AD, 1), AD_R3_4=round(AD34, 1), cipher_clause=prim > AD,
                stat_i_target=tgt_i, stat_i_p95=p95(sh_i), stat_i_max=max(sh_i), stat_i_pass=tgt_i > p95(sh_i),
                n_shuffles=len(sh_i), seeds=a.seeds, shuffle=a.shuffle, cipher_class=a.cipher_class,
                recurring_codes={c: dict(n_occ=r['n_occ'], independent_contexts=len(r['contexts']),
                                         contexts_above_p95=sum(1 for x in rows if x['code'] == c and x['above_p95']),
                                         flanks_above_p95=sum(1 for x in rows if x['code'] == c and x['flanks_above']))
                                 for c, r in rec.items()},
                wordlist_size=len(words))
    json.dump(summ, open(os.path.join(a.out, 'summary.json'), 'w'), indent=1, ensure_ascii=False)
    print(json.dumps({k: v for k, v in summ.items() if k != 'recurring_codes'}, ensure_ascii=False))
    for r in rows:
        print(f"{r['code']}\t{r['value']}\t{r['grade']}\t{r['target']}\tp95 {r['shuffle_p95']}\tmax {r['shuffle_max']}"
              f"\t{'ABOVE' if r['above_p95'] else 'below'}\tflanks {r['flanks']} p95 {r['flanks_p95']} "
              f"{'ABOVE' if r['flanks_above'] else 'below'}\t{r['context']}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
