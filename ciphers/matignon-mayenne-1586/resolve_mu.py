#!/usr/bin/env python3
"""Job bMAT2 (LANE B5, 26 Sept 2026): matignon-mayenne-1586 NEAR step (1).

1. spans.tsv: split ciphertext.txt into 'read'/'unread' line-spans. Bourdeau's own measure.py rule
   (a keyed token is READ if every plaintext letter it produces falls inside a sense run of >= 3
   lexical words / >= 10 letters) needs his lm.pkl + corpus_words.txt, both .gitignored in his
   repository and absent from the shallow clone at fc0c9e8 (confirmed: neither file, nor
   measure_cache/, is present) -- so this script reimplements the SAME rule (MINWORDS=3,
   MINLETTERS=10, a token graded H, M or U all break a run the way his '+' does since we have no
   LM to disambiguate an M candidate or fill a U gap) using tools/judge_plaintext.py's NgramModel
   built from this target's own fr16 corpus (lettresdecatheri01). This is a materially different
   word list from his (his corpus, size and MINCOUNT=20 threshold are unknown to us) and a
   materially stricter decoder (no LM fills M/U tokens here, so an H-run can be broken by a single
   ambiguous code where his beam search would not break it) -- reported as a proxy split, not a
   reproduction of his own numbers. Per-leaf comparison: this rule reads far less of each leaf as
   'read' than his measure.json (10.8% of all tokens here vs his 26-33%), consistent with being a
   stricter proxy, not a contradiction of his figures.

2. Two-context rule: for each M code (test only its own 2-3 key.tsv candidates) and each U code (an
   unkeyed sign: open search over a-z, since no candidate list exists), for every occurrence of that
   code on the unread spans, splice a candidate letter between the immediately adjacent H-chunks (up
   to the next M/U token or line end each side) and greedy-segment the result with the SAME NgramModel;
   the candidate is 'confirmed' by that occurrence if the spliced letter lands inside a recognised
   word. A code reaches grade S if the SAME candidate is confirmed in >= 2 distinct occurrences, M if
   in exactly 1. Control: identical procedure on the same lines with tokens shuffled within each line
   (3 seeds) -- the count of S values the control also produces is the false-positive rate of the
   rule itself, not of any candidate value (CLAUDE.md rule 3: no negative -- and, symmetrically, no
   gain claim -- without a matched control; here the control result IS the finding, see NOTES.md).

3. Re-judge (fr16) the unread spans alone, real order vs the same shuffled-order control used by the
   previous job (specs/matignon-mayenne-1586.json), scoped to just the unread-only H-token letters.

Run from the repository root: python3 ciphers/matignon-mayenne-1586/resolve_mu.py
Outputs (committed): spans.tsv, mu_resolve_results.json, unread_only_reading.txt
"""
import sys, os, csv, random, json

sys.path.insert(0, 'tools')
from judge_plaintext import NgramModel, read_corpus, fold, judge

TARGET = 'ciphers/matignon-mayenne-1586'
MINWORDS, MINLETTERS = 3, 10
ALPHA = 'abcdefghijklmnopqrstuvwxyz'


def load_tokens(path):
    lines, order = {}, []
    with open(path, encoding='utf-8') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            ln = row['line']
            if ln not in lines:
                lines[ln] = []
                order.append(ln)
            lines[ln].append({'pos': int(row['pos']), 'sign': row['sign'], 'value': row['value'], 'grade': row['grade']})
    for ln in lines:
        lines[ln].sort(key=lambda t: t['pos'])
    return order, lines


def chunk_of(text):
    """Greedy longest-word segmentation -> list of (start, end, word, is_lexical)."""
    out, i = [], 0
    while i < len(text):
        best = 0
        for L in range(min(MODEL.maxw, len(text) - i), 0, -1):
            if text[i:i + L] in MODEL.words:
                best = L
                break
        if best:
            out.append((i, i + best, text[i:i + best], True))
            i += best
        else:
            out.append((i, i + 1, text[i:i + 1], text[i:i + 1] in ('a', 'i')))
            i += 1
    return out


def sense_mask(text):
    spans = chunk_of(text)
    mask = [False] * len(text)
    i = 0
    while i < len(spans):
        if not spans[i][3]:
            i += 1
            continue
        j = i
        while j < len(spans) and spans[j][3]:
            j += 1
        nlet = spans[j - 1][1] - spans[i][0]
        if j - i >= MINWORDS and nlet >= MINLETTERS:
            for k in range(spans[i][0], spans[j - 1][1]):
                mask[k] = True
        i = j
    return mask


def line_spans(toks):
    """Per-token 'read'/'unread' using the sense-run rule on maximal H-runs (M/U break a run)."""
    status = ['unread'] * len(toks)

    def flush(run):
        if not run:
            return
        text = ''.join(fold(toks[i]['value']) for i in run)
        mask = sense_mask(text)
        p = 0
        for i in run:
            L = len(fold(toks[i]['value']))
            if L and all(mask[p:p + L]):
                status[i] = 'read'
            p += L

    run = []
    for idx, t in enumerate(toks):
        if t['grade'] == 'H':
            run.append(idx)
        else:
            flush(run)
            run = []
    flush(run)
    return status


def spans_to_rows(folio_line, toks, status):
    rows, i = [], 0
    while i < len(toks):
        j = i
        while j < len(toks) and status[j] == status[i]:
            j += 1
        rows.append((folio_line, toks[i]['pos'], toks[j - 1]['pos'], status[i]))
        i = j
    return rows


def local_ctx(toks, i):
    """Immediate H-chunk text before/after position i in the line, stopped by any non-H token."""
    left = []
    k = i - 1
    while k >= 0 and toks[k]['grade'] == 'H':
        left.append(fold(toks[k]['value']))
        k -= 1
    left.reverse()
    right = []
    k = i + 1
    while k < len(toks) and toks[k]['grade'] == 'H':
        right.append(fold(toks[k]['value']))
        k += 1
    return ''.join(left), ''.join(right)


def confirms(left, c, right):
    if not c:
        return False
    local = left + c + right
    p = len(left)
    for (s, e, w, lex) in chunk_of(local):
        if s <= p < e:
            return lex and (e - s) >= 2
    return False


def resolve_codes(order, lines, key_candidates):
    occ = {}
    for ln in order:
        toks = lines[ln]
        for i, t in enumerate(toks):
            if t['grade'] in ('M', 'U'):
                left, right = local_ctx(toks, i)
                occ.setdefault(t['sign'], []).append((ln, t['pos'], left, right))
    result = {}
    for sign, occs in occ.items():
        cands = key_candidates.get(sign)
        test_cands = cands if cands else list(ALPHA)
        support = {c: [] for c in test_cands}
        for (ln, pos, left, right) in occs:
            for c in test_cands:
                if confirms(left, c, right):
                    support[c].append((ln, pos))
        best_c, best_n = None, 0
        for c, hits in support.items():
            if len(hits) > best_n:
                best_c, best_n = c, len(hits)
        result[sign] = dict(occurrences=len(occs), best=best_c, n_confirmed=best_n,
                             support={c: h for c, h in support.items() if h})
    return result


def shuffled_lines(order, lines, seed):
    rng = random.Random(seed)
    out = {}
    for ln in order:
        toks = [dict(t) for t in lines[ln]]
        vals = [(t['sign'], t['value'], t['grade']) for t in toks]
        rng.shuffle(vals)
        for t, (sign, value, grade) in zip(toks, vals):
            t['sign'], t['value'], t['grade'] = sign, value, grade
        out[ln] = toks
    return out


def count_S(res):
    return sum(1 for d in res.values() if d['n_confirmed'] >= 2)


def count_M1(res):
    return sum(1 for d in res.values() if d['n_confirmed'] == 1)


if __name__ == '__main__':
    corpora = ["tools/data/fr16/lettresdecatheri01cathuoft_djvu.txt.gz"]
    MODEL = NgramModel([read_corpus(p) for p in corpora])

    order, lines = load_tokens(os.path.join(TARGET, 'reading_tokens.tsv'))

    key_cands = {}
    with open(os.path.join(TARGET, 'key.tsv'), encoding='utf-8') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            if '|' in row['value']:
                key_cands[row['code']] = [c for c in row['value'].split('|') if len(c) == 1]

    # 1. spans.tsv
    span_rows, tot_read, tot_unread = [], 0, 0
    status_by_line = {}
    for ln in order:
        toks = lines[ln]
        status = line_spans(toks)
        status_by_line[ln] = status
        for s in status:
            tot_read += (s == 'read')
            tot_unread += (s == 'unread')
        span_rows.extend(spans_to_rows(ln, toks, status))
    with open(os.path.join(TARGET, 'spans.tsv'), 'w', encoding='utf-8') as f:
        f.write('folio_line\tpos_start\tpos_end\tstatus\tsource\n')
        for (fl, ps, pe, st) in span_rows:
            f.write(f'{fl}\t{ps}\t{pe}\t{st}\tthis job, sense-run rule (MINWORDS=3,MINLETTERS=10) on '
                    f'fr16 lettresdecatheri01, proxy for Bourdeau measure.py (his lm.pkl/corpus_words.txt '
                    f'gitignored, unavailable in the shallow clone)\n')
    print(f'spans.tsv: {len(span_rows)} rows, tokens read={tot_read} unread={tot_unread} (of {tot_read + tot_unread})')

    # 2. resolve M/U codes: real order vs 3 shuffled-line-order controls
    real = resolve_codes(order, lines, key_cands)
    ctrl_results = [resolve_codes(order, shuffled_lines(order, lines, seed), key_cands) for seed in (1, 2, 3)]

    print(f'real: codes tested={len(real)}, S(>=2 contexts)={count_S(real)}, M(1 context)={count_M1(real)}')
    for i, r in enumerate(ctrl_results, 1):
        print(f'control seed {i}: codes tested={len(r)}, S={count_S(r)}, M={count_M1(r)}')

    with open(os.path.join(TARGET, 'mu_resolve_results.json'), 'w', encoding='utf-8') as f:
        json.dump(dict(real=real, controls=ctrl_results,
                        summary=dict(real_S=count_S(real), real_M=count_M1(real),
                                     control_S=[count_S(r) for r in ctrl_results],
                                     control_M=[count_M1(r) for r in ctrl_results])),
                  f, indent=1, ensure_ascii=False)

    # 3. re-judge the unread spans alone: real order vs shuffled-order control, same subset
    spec = json.load(open('specs/matignon-mayenne-1586.json', encoding='utf-8'))

    def unread_text(seed=None):
        out = []
        for ln in order:
            toks = lines[ln]
            st = status_by_line[ln]
            letters = [fold(t['value']) for t, s in zip(toks, st) if s == 'unread' and t['grade'] == 'H']
            if seed is not None:
                random.Random(seed).shuffle(letters)
            out.append(''.join(letters))
        return '\n'.join(out)

    real_text = unread_text()
    with open(os.path.join(TARGET, 'unread_only_reading.txt'), 'w', encoding='utf-8') as f:
        f.write(real_text)
    j_real = judge(spec, real_text)
    print(f"unread-only judge (real order): {j_real['checks']['language']}, words={j_real['checks'].get('words')}")
    for seed in (1, 2, 3):
        j_ctrl = judge(spec, unread_text(seed))
        print(f"unread-only judge (shuffled seed {seed}): {j_ctrl['checks']['language']}, words={j_ctrl['checks'].get('words')}")
