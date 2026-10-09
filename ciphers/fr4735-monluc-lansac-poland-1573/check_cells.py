#!/usr/bin/env python3
"""MONLUC-KEY step 1 (7 Oct 2026): per-cell check of Tomokiyo's Monluc Cipher 1 table (key.tsv) against the f.86
(c172) marginal decipherment, with a held-out-line control.

  python3 check_cells.py [--gloss gloss_c172_withline1.txt] [--draws 200] [--seed 1] [--check]

1. Token-level semi-global alignment (score_c172.py's scoring: match +2, mismatch -1, gap -2, free end gaps on the gloss)
   of the decoded tokens against the gloss, with traceback, so every cipher token gets the gloss letter it faces (or a gap).
2. Per cell: n tokens, n aligned, the gloss letters faced, the majority letter and its share. Verdict per cell:
   confirm   majority == table letter, >=2 aligned, share >= 2/3
   contradict majority != table letter, >=2 aligned, share >= 2/3 (a candidate correction)
   once      exactly 1 aligned instance (agrees / disagrees noted, never a correction)
   mixed     >=2 aligned, no letter at 2/3
   unexercised  the cell is not in the f.86 transcription (or never aligned)
3. Control A (shuffle): the same per-cell procedure on 200 token-shuffled decodes; reports how many cells reach
   'confirm' and 'contradict' by chance (rule 3: the shuffle changes which token faces which letter, so it can differ).
4. Control B (held-out line, the gain gate): corrections are learned from two of the three cipher lines and the
   third is scored with the table key and with the corrected key, both against the gloss; the gain must exceed the
   shuffled-token gain on the held-out line (same corrections, shuffled held-out tokens).
Writes cells_c172.tsv, results_cells_c172.json, ciphertext_c172.tsv (per position: sign, conf M where the passes split,
pass A/B, table letter, gloss letter faced) and votes_c172.tsv (for decode.json); --check exits 1 if either is stale (rule 7).
"""
import argparse, json, random, sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from score_c172 import norm, load_key  # noqa: E402

M, X, G = 2, -1, -2

# MONLUC-K38 (9 Oct 2026): the 10 f.86 K07 tokens a value-blind binary sort answered curl-present (MONLUC-CURL, f86_curl_answers.tsv;
# gate PASS p 0.0086) are written K38 (the key sheet's C-curl z, table t) in ciphertext_c172.tsv only, as a transcription
# correction. passA/passB keep the old label; relabel = curl-sort. The alignment, cells_c172.tsv, results_cells_c172.json and
# the gloss letter each token faces are computed on the transcription before this relabel, so the relabel never feeds back into
# which gloss letter a token faces. Grades then follow decode.json's votes: C where the faced gloss letter is t, M otherwise.
RELABEL = {(L, i): ('K07', 'K38') for L, i in [('L02', 1), ('L02', 20), ('L02', 31), ('L03', 6), ('L03', 19), ('L03', 22),
                                               ('L03', 30), ('L03', 39), ('L03', 45), ('L04', 22)]}


def load_lines(name='ciphertext.txt'):
    lines = {}
    for ln in (HERE / name).read_text().splitlines():
        if ln.startswith('L') and '\t' in ln:
            lab, rest = ln.split('\t', 1)
            lines[lab] = [t for t in rest.split() if t not in ('END_CUT', '-')]
    return lines


def tok_letters(toks, key):
    """one normalised letter (or '') per token"""
    return [norm(key.get(t, '')) for t in toks]


def align_tb(letters, gloss):
    """letters: list of '' or one char per token. Returns (matched, faced) where faced[i] is the gloss letter token i
    faces (None for a token with no letter or a gap)."""
    idx = [i for i, c in enumerate(letters) if c]
    a = [letters[i] for i in idx]
    n, m = len(a), len(gloss)
    S = [[0] * (m + 1) for _ in range(n + 1)]
    T = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        S[i][0] = S[i - 1][0] + G
        T[i][0] = 1
        for j in range(1, m + 1):
            d = S[i - 1][j - 1] + (M if a[i - 1] == gloss[j - 1] else X)
            u = S[i - 1][j] + G
            l = S[i][j - 1] + G
            best = max(d, u, l)
            S[i][j] = best
            T[i][j] = 0 if best == d else (1 if best == u else 2)
    j = max(range(m + 1), key=lambda k: S[n][k])
    i = n
    faced_a = [None] * n
    matched = 0
    while i > 0:
        if j == 0:
            i -= 1
            continue
        t = T[i][j]
        if t == 0:
            faced_a[i - 1] = gloss[j - 1]
            matched += a[i - 1] == gloss[j - 1]
            i, j = i - 1, j - 1
        elif t == 1:
            i -= 1
        else:
            j -= 1
    faced = [None] * len(letters)
    for k, i0 in enumerate(idx):
        faced[i0] = faced_a[k]
    return matched, faced


def cell_table(toks, faced, key):
    by = defaultdict(list)
    for t, f in zip(toks, faced):
        by[t].append(f)
    rows = {}
    for cid in sorted(key):
        fs = by.get(cid, [])
        al = [f for f in fs if f]
        c = Counter(al)
        maj, mc = (c.most_common(1)[0] if c else ('', 0))
        share = mc / len(al) if al else 0.0
        tab = norm(key[cid])
        if not fs or not al:
            v = 'unexercised'
        elif len(al) == 1:
            v = 'once-agree' if maj == tab else 'once-disagree'
        elif share >= 2 / 3:
            v = 'confirm' if maj == tab else 'contradict'
        else:
            v = 'mixed'
        rows[cid] = dict(n=len(fs), aligned=len(al), faced=''.join(sorted(al)), majority=maj,
                         share=round(share, 3), table=tab, verdict=v)
    return rows


def corrections(rows):
    return {c: r['majority'] for c, r in rows.items() if r['verdict'] == 'contradict'}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--gloss', default='gloss_c172_withline1.txt')
    ap.add_argument('--draws', type=int, default=200)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    key = load_key()
    lines = load_lines()
    gloss = norm((HERE / a.gloss).read_text().split('\n#', 1)[0])
    toks = [t for L in sorted(lines) for t in lines[L]]
    matched, faced = align_tb(tok_letters(toks, key), gloss)
    rows = cell_table(toks, faced, key)
    vc = Counter(r['verdict'] for r in rows.values())

    rng = random.Random(a.seed)
    sh_conf, sh_contra = [], []
    for _ in range(a.draws):
        t = toks[:]
        rng.shuffle(t)
        _, f = align_tb(tok_letters(t, key), gloss)
        c = Counter(r['verdict'] for r in cell_table(t, f, key).values())
        sh_conf.append(c['confirm'])
        sh_contra.append(c['contradict'])
    sh_conf.sort(); sh_contra.sort()
    p95 = lambda v: v[int(0.95 * len(v)) - 1]

    # held-out line gain
    held = {}
    for L in sorted(lines):
        train = [t for K in sorted(lines) if K != L for t in lines[K]]
        _, ftr = align_tb(tok_letters(train, key), gloss)
        corr = corrections(cell_table(train, ftr, key))
        key2 = dict(key); key2.update(corr)
        test = lines[L]
        nlet = sum(1 for c in tok_letters(test, key) if c)
        base, _ = align_tb(tok_letters(test, key), gloss)
        new, _ = align_tb(tok_letters(test, key2), gloss)
        gains = []
        for _ in range(a.draws):
            t = test[:]
            rng.shuffle(t)
            b0, _ = align_tb(tok_letters(t, key), gloss)
            b1, _ = align_tb(tok_letters(t, key2), gloss)
            gains.append(b1 - b0)
        gains.sort()
        held[L] = dict(corrections=corr, letters=nlet, table_matched=base, corrected_matched=new, gain=new - base,
                       shuffle_gain_mean=round(sum(gains) / len(gains), 2), shuffle_gain_p95=p95(gains))

    allcorr = corrections(rows)
    key2 = dict(key); key2.update(allcorr)
    m2, _ = align_tb(tok_letters(toks, key2), gloss)
    nlet = sum(1 for c in tok_letters(toks, key) if c)
    res = dict(gloss=a.gloss, tokens=len(toks), letters=nlet, table_matched=matched,
               table_rate=round(matched / nlet, 4), verdicts=dict(sorted(vc.items())),
               shuffle_confirm_mean=round(sum(sh_conf) / len(sh_conf), 2), shuffle_confirm_p95=p95(sh_conf),
               shuffle_contradict_mean=round(sum(sh_contra) / len(sh_contra), 2),
               shuffle_contradict_p95=p95(sh_contra), corrections_all_lines=allcorr,
               corrected_matched_in_sample=m2, corrected_rate_in_sample=round(m2 / nlet, 4),
               held_out=held, draws=a.draws, seed=a.seed)
    tsv = 'cell\ttable\tn\taligned\tfaced\tmajority\tshare\tverdict\n' + ''.join(
        f"{c}\t{r['table']}\t{r['n']}\t{r['aligned']}\t{r['faced']}\t{r['majority']}\t{r['share']}\t{r['verdict']}\n"
        for c, r in rows.items())
    # per-position file (feeds decode.json: conf M where the two blind passes split; vote = gloss letter faced)
    settled = {}
    for ln in (HERE / 'passes' / 'settled.tsv').read_text().splitlines()[1:]:
        f = ln.split('\t')
        settled[(f[0], int(f[1]))] = (f[2], f[3])
    pos_rows, vote_rows, k = [], [], 0
    for L in sorted(lines):
        for i, t in enumerate(lines[L], 1):
            ab = settled.get((L, i))
            conf = 'M' if ab or t.startswith('?') else 'H'
            rl = ''
            if (L, i) in RELABEL:  # transcription correction after the alignment: the faced letter is not re-derived from it
                old, new = RELABEL[(L, i)]
                assert t == old, (L, i, t, old)
                t, rl = new, 'curl-sort'
            pos_rows.append(f"{L}\t{i}\t{t}\t{conf}\t{ab[0] if ab else lines[L][i - 1]}\t{ab[1] if ab else lines[L][i - 1]}\t{norm(key.get(t, ''))}\t{faced[k] or ''}\t{rl}\n")
            if faced[k]:
                vote_rows.append(f"{L}\t{i}\t{faced[k]}\n")
            k += 1
    ctsv = 'line\tpos\tsign\tconf\tpassA\tpassB\ttable_value\tgloss_faced\trelabel\n' + ''.join(pos_rows)
    vtsv = 'line\tpos\tvalue\n' + ''.join(vote_rows)
    js = json.dumps(res, indent=1) + '\n'
    outs = {HERE / 'cells_c172.tsv': tsv, HERE / 'results_cells_c172.json': js,
            HERE / 'ciphertext_c172.tsv': ctsv, HERE / 'votes_c172.tsv': vtsv}
    if a.check:
        bad = [p.name for p, t in outs.items() if not p.exists() or p.read_text() != t]
        print('STALE ' + ' '.join(bad) if bad else 'OK ' + ' '.join(p.name for p in outs) + ' current')
        sys.exit(1 if bad else 0)
    for p, t in outs.items():
        p.write_text(t)
    print(js)


if __name__ == '__main__':
    main()
