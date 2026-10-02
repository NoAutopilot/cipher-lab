#!/usr/bin/env python3
"""Read the 2894 key cells against a printed title page of the key book: GAPS3-pro3055-clinton-1779, 2 Oct 2026.

The key of the Clinton-Haldimand book cipher is the title page of A List of the General and Field Officers (1778):
a figure pair (line, letter) names a letter, counting letters only (no spaces or punctuation) -- the f.186 cells of
GAPS2 (passes/key_2894.tsv, 166 cells) already read lines 1-2 as "By Permission of the Right Honourable / the
Secretary at War". The only copy on archive.org (listofgeneralfie00grea_0, leaf n4, images/armylist/n4.jpg) is the
1761 EDITION, so its lines are a DIFFERENT PRINTING of the same title: some lines keep their wording and others do
not, and the line numbers shift from line 9. This script therefore never trusts a 1761 line number; it maps each
1778 key line to a 1761 printed line by the cells already fixed on it (key_2894.tsv from the f.186 decipherment,
plus S. Tomokiyo's independent cells, passes/tomokiyo_key_pairs.tsv), accepts a 1761 line only where every fixed
cell agrees with it (or every cell up to a prefix length, for a line whose tail wording changed), and then reads
the still-unread cells (grade M in tokens_2894.tsv) from the accepted 1761 text.

Grades (rule 4): a letter read this way is **I** (inferred: the wording of the 1778 line is inferred from a 1761
printing that agrees with every cell fixed on that line), never H -- H needs the 1778 page itself. C and H tokens
of tokens_2894.tsv keep their grades; the 1761 letter is written beside them as a check.

Control (rule 3): for each accepted mapping, the same agreement statistic against (a) the letters of that 1761 line
shuffled in place (20 seeds) and (b) every other 1761 line -- both vary on the statistic's own axis (which letter
sits at which position).

Outputs: title_1761_map.json (mapping table, controls, clause reading), m_tokens_1761.tsv (every M token with its
1761 letter or '-'), clause_2894.tsv (the tokens of the clause f.186 omits, with every source letter and grade).
--check re-derives and exits 1 when any committed output differs (rule 7).
"""
import argparse, json, os, random, re, sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(ROOT, *a)

def read_tsv(path):
    rows, hdr = [], None
    for line in open(path, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line or line.startswith('#'):
            continue
        parts = line.split('\t')
        if hdr is None:
            hdr = parts; continue
        parts += [''] * (len(hdr) - len(parts))
        rows.append(dict(zip(hdr, parts)))
    return rows

def letters(s):
    return re.sub(r'[^a-z]', '', s.lower())

def load_title(path):
    out = []
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        out.append(line.rstrip('\n'))
    return out

def agreement(cells, text):
    """cells: {pos: letter}; -> (agree, total). A position beyond the line's length is a disagreement."""
    a = sum(1 for p, l in cells.items() if p <= len(text) and text[p - 1] == l)
    return a, len(cells)

def prefix_len(cells, text):
    """longest p such that every cell with pos <= p agrees (0 if the first cell disagrees)."""
    best = 0
    for p in sorted(cells):
        if p <= len(text) and text[p - 1] == cells[p]:
            best = p
        else:
            break
    return best

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--seeds', type=int, default=20)
    a = ap.parse_args()
    title = load_title(P('title1761_reading.txt'))
    tl = [letters(t) for t in title]
    # fixed 1778 cells: f.186 majority cells first, Tomokiyo's where f.186 has none (counting-error rows excluded)
    fixed = defaultdict(dict); src = {}
    for r in read_tsv(P('key_2894.tsv')):
        fixed[int(r['line'])][int(r['pos'])] = r['letter']; src[(int(r['line']), int(r['pos']))] = 'f186'
    for r in read_tsv(P('tomokiyo_key_pairs.tsv')):
        if r['flag'] == 'counting-error':
            continue
        L, p = int(r['line']), int(r['pos'])
        if p not in fixed[L]:
            fixed[L][p] = r['letter']; src[(L, p)] = 'tomokiyo'
    # cells whose disagreement with the 1761 text is a conflict already logged, not a wording difference
    ALLOW = {(16, 7): "f.186 'Terney' vs the clerk's 'Ternay' (GAPS2): Tomokiyo and the 1761 page both give 'a'",
             (13, 11): "i/j are one letter in this key (GAPS2: 'Johns'/'Island' share 17-4); Tomokiyo writes j"}
    MIN_PREFIX_AGREE = 8      # a prefix read needs this many agreeing cells: with fewer, a competing wording of the
                              # same title can fit the same cells (1778 line 21: 5 agreeing cells fit both
                              # 'Corps, and as they Rank in the Army' and 'Corps, and in the Army', which differ at 9-10)
    rng_rows = []
    mapping = {}
    for L in sorted(fixed):
        cells = fixed[L]
        n = len(cells)
        scores = []
        for i, text in enumerate(tl):
            ag, _n = agreement(cells, text)
            scores.append((ag, prefix_len(cells, text), i))
        scores.sort(key=lambda x: (-x[0], -x[1]))
        ag, pre, i = scores[0]
        text = tl[i]
        others = [s[0] / n for s in scores[1:]]
        shuf = []
        for seed in range(a.seeds):
            ls = list(text); random.Random(seed).shuffle(ls)
            shuf.append(agreement(cells, ''.join(ls))[0] / n)
        dis = [(p, cells[p], src[(L, p)], text[p - 1] if p <= len(text) else '>end')
               for p in sorted(cells) if not (p <= len(text) and text[p - 1] == cells[p])]
        # readable prefix K: up to the first disagreeing cell that is neither beyond the 1761 line's end nor an
        # allowed logged conflict; a disagreement beyond the end does not shorten K (the 1778 line may be longer,
        # or the cell a miscount), but K never exceeds the 1761 line's length
        K = len(text)
        for p, l78, sname, l61 in dis:
            if l61 == '>end' or (L, p) in ALLOW:
                continue
            K = min(K, p - 1); break
        if ag == n:
            status = 'full'
        elif n >= 4 and ag >= 0.8 * n and all(l61 == '>end' or (L, p) in ALLOW for p, l78, sname, l61 in dis):
            status = 'full-allowed'      # every disagreement is beyond the line's end or a logged conflict
        elif K >= 10 and ag >= MIN_PREFIX_AGREE:
            status = f'prefix-{K}'       # read only positions <= K
        elif n >= 10 and ag >= 0.9 * n:
            status = 'near'              # reported, not used for reading
        else:
            status = 'none'
        row = dict(line_1778=L, n_cells=n, f186_cells=sum(1 for p in cells if src[(L, p)] == 'f186'),
                   tomokiyo_cells=sum(1 for p in cells if src[(L, p)] == 'tomokiyo'),
                   best_1761_line=i + 1, best_1761_text=title[i], agree=ag, agree_frac=round(ag / n, 3),
                   disagreeing_cells=[f"{L}-{p} 1778={l78} ({sname}) 1761={l61}" for p, l78, sname, l61 in dis],
                   status=status, readable_upto=(K if status.startswith(('full', 'prefix')) else 0),
                   control_shuffled_mean=round(sum(shuf) / len(shuf), 3), control_shuffled_max=round(max(shuf), 3),
                   control_other_lines_mean=round(sum(others) / len(others), 3), control_other_lines_max=round(max(others), 3))
        rng_rows.append(row)
        if row['readable_upto']:
            mapping[L] = (i, row['readable_upto'])
    def read_cell(L, p):
        if L not in mapping:
            return ''
        i, upto = mapping[L]
        return tl[i][p - 1] if p <= upto and p <= len(tl[i]) else ''
    # tokens
    toks = read_tsv(P('tokens_2894.tsv'))
    m_rows = ['n\tref\tline\tpos\tword\tgrade_gaps2\tletter_gaps2\tletter_1761\tgrade_now']
    clause = ['n\tref\tline\tpos\tletter_f186\tletter_tomokiyo\tletter_1761\tgrade\tsource']
    grades_now = Counter(); clause_grades = Counter(); resolved = 0; agree_check = Counter()
    clause_text = []
    for t in toks:
        L, p = t['line'], t['pos']
        if not (L.isdigit() and p.isdigit()):
            l61 = ''
        else:
            l61 = read_cell(int(L), int(p))
        g = t['grade']
        if g == 'M':
            gnow = 'I' if l61 else 'M'
            resolved += bool(l61)
            m_rows.append('\t'.join([t['n'], t['ref'], L, p, t['word'], g, t['letter'], l61 or '-', gnow]))
        else:
            gnow = g
            if l61:
                agree_check['agree' if l61 == t['letter'] else 'disagree'] += 1
        grades_now[gnow] += 1
        if t['how'] == 'skip':
            tomo = t['tomokiyo']
            f186 = t['letter'] if g == 'C' else ''
            letter = f186 or (tomo if g == 'H' else '') or l61
            srcname = 'f186' if f186 else ('tomokiyo' if g == 'H' and tomo else ('1761' if l61 else ''))
            clause.append('\t'.join([t['n'], t['ref'], L, p, f186, tomo, l61 or '-', gnow, srcname]))
            clause_grades[gnow] += 1
            clause_text.append((t['ref'], letter or '.'))
    LINE21 = ("1778 line 21 is not read from the 1761 page: its best 1761 line, 'CORPS, and as they Rank in the ARMY.', "
              "disagrees with Tomokiyo's 21-17 y (1761: n). Under that wording 21-9 21-10 read 'as'; the wording "
              "'Corps, and in the Army' (c1 p4 h12 e13 r15 y17) fits all six of Tomokiyo's line-21 cells and reads 'in'. "
              "The cells fixed on this line cannot separate the two at positions 9-10, so the pair stays M with 'in' "
              "the better-supported candidate; the 1778 page itself decides.")
    out = dict(title_source='archive.org listofgeneralfie00grea_0 leaf n4, 1761 edition (NOT the 1778 key book)',
               n_1778_lines_with_cells=len(fixed), mapping=rng_rows,
               status_by_line={str(r['line_1778']): r['status'] for r in rng_rows},
               lines_read_from=sorted(mapping), lines_not_read=[r['line_1778'] for r in rng_rows if not r['readable_upto']],
               fixed_cells_on_read_lines=dict(agree_check),
               fixed_cells_all_best_lines=dict(agree=sum(r['agree'] for r in rng_rows), total=sum(r['n_cells'] for r in rng_rows)),
               line21_note=LINE21,
               m_tokens_total=sum(1 for t in toks if t['grade'] == 'M'), m_tokens_resolved_to_I=resolved,
               grades_now=dict(grades_now), clause_grades=dict(clause_grades),
               clause_letters=''.join(ch for _, ch in clause_text))
    new = {'title_1761_map.json': json.dumps(out, indent=1) + '\n',
           'm_tokens_1761.tsv': '\n'.join(m_rows) + '\n',
           'clause_2894.tsv': '\n'.join(clause) + '\n'}
    if a.check:
        bad = [k for k, v in new.items() if not os.path.exists(P(k)) or open(P(k)).read() != v]
        print('STALE: ' + ', '.join(bad) if bad else 'check ok: title_1761_map.json, m_tokens_1761.tsv, clause_2894.tsv regenerate identically')
        sys.exit(1 if bad else 0)
    for k, v in new.items():
        open(P(k), 'w').write(v)
    for r in rng_rows:
        print(f"1778 line {r['line_1778']:>2}: {r['n_cells']:>2} cells -> 1761 line {r['best_1761_line']:>2} agree {r['agree']}/{r['n_cells']} [{r['status']}] read<= {r['readable_upto']:>2}  shuffled {r['control_shuffled_mean']} other-lines {r['control_other_lines_mean']}  | {r['best_1761_text']}  {'; '.join(r['disagreeing_cells'])}")
    print(json.dumps({k: v for k, v in out.items() if k != 'mapping'}, indent=1))
    print('\n'.join(m_rows)); print(); print('\n'.join(clause))

if __name__ == '__main__':
    main()
