#!/usr/bin/env python3
"""Read the 2894 key cells against the 1778 title page itself: GAPS4-pro3055-clinton-1779, 2 Oct 2026.

The key of the Clinton-Haldimand book cipher is the title page of A List of the General and Field Officers (1778), a
figure pair (line, letter) naming a letter, counting characters only (no spaces or punctuation). GAPS3 read the still-open
cells from the 1761 EDITION (title_1761_check.py, grade I, line numbers remapped by the fixed cells). This script reads
them from the 1778 printing (archive.org listofgeneralfie00grea, leaf page/n12, passes/title1778_reading.txt), the key
book itself: a 1778 key line L is printed line L of that page, no remapping -- but the mapping is still TESTED, not
assumed: every fixed cell (key_2894.tsv from the f.186 decipherment; S. Tomokiyo's independent cells where f.186 has
none) is compared with the same-numbered printed line, with two controls on the statistic's own axis (the line's letters
shuffled in place, 20 seeds; every other printed line).

Character convention: letters a-z AND the ampersand. Two of Tomokiyo's cells fix this: 27-9 is '&' in his table (line 27
'Clothing, &c.' is c-l-o-t-h-i-n-g-&-c) and 22-39 is 'm' (line 22 '... Governors, &c. of his Majesty's' puts m at 39 only
when & is counted). No 2894 token falls on line 27 or beyond the & of line 22, so the convention changes no token; the
script reports the agreement under both conventions.

Grades (rule 4): a letter read from the 1778 page is **H** (read from the key source itself). H and C tokens keep their
grade, with the 1778 letter written beside them as a check; an I token (GAPS3, from the 1761 page) becomes H when the 1778
page gives a letter at that cell; an M token becomes H when it does, else stays M.

Outputs: title_1778_map.json (per-line agreement, controls, grades, clause), tokens_2894_1778.tsv (all 315 tokens with
the 1778 letter and the grade now), clause_2894_1778.tsv (the clause f.186 omits). The 1761 outputs are left as they
are (title_1761_check.py --check still passes). --check re-derives and exits 1 when any committed output differs (rule 7).
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

def chars(s, amp=True):
    return re.sub(r'[^a-z&]' if amp else r'[^a-z]', '', s.lower())

def load_title(path):
    return [l.rstrip('\n') for l in open(path, encoding='utf-8') if l.strip() and not l.startswith('#')]

def agreement(cells, text):
    return sum(1 for p, l in cells.items() if p <= len(text) and text[p - 1] == l), len(cells)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--seeds', type=int, default=20)
    a = ap.parse_args()
    title = load_title(P('title1778_reading.txt'))
    tl = [chars(t) for t in title]
    tl_noamp = [chars(t, amp=False) for t in title]
    fixed = defaultdict(dict); src = {}
    for r in read_tsv(P('key_2894.tsv')):
        fixed[int(r['line'])][int(r['pos'])] = r['letter']; src[(int(r['line']), int(r['pos']))] = 'f186'
    for r in read_tsv(P('tomokiyo_key_pairs.tsv')):
        if r['flag'] == 'counting-error':
            continue
        L, p = int(r['line']), int(r['pos'])
        if p not in fixed[L]:
            fixed[L][p] = r['letter']; src[(L, p)] = 'tomokiyo'
    LOGGED = {(16, 7): "f.186 'Terney' vs the clerk's 'Ternay' (GAPS2); Tomokiyo, the 1761 and the 1778 page all give 'a'",
              (13, 11): "i/j are one letter in this key (GAPS2: 'Johns'/'Island' share 17-4); Tomokiyo writes j",
              (23, 25): "f.186 'u' where the page has 'w' (GAPS3); the decipherer's u for w",
              (1, 37): "Tomokiyo's cell beyond the 32 characters of line 1 (GAPS3: beyond the line); a miscount",
              (25, 19): "Tomokiyo's 's' where the page has 'e' at 19 ('A Succession of Colonels': s is at 21); a miscount of two"}
    rows = []; total = Counter(); per_conv = Counter()
    for L in sorted(fixed):
        cells = fixed[L]; n = len(cells)
        text = tl[L - 1] if L - 1 < len(tl) else ''
        ag, _ = agreement(cells, text)
        ag_noamp, _ = agreement(cells, tl_noamp[L - 1] if L - 1 < len(tl_noamp) else '')
        per_conv['amp'] += ag; per_conv['noamp'] += ag_noamp
        shuf = []
        for seed in range(a.seeds):
            ls = list(text); random.Random(seed).shuffle(ls)
            shuf.append(agreement(cells, ''.join(ls))[0] / n)
        others = [agreement(cells, t)[0] / n for i, t in enumerate(tl) if i != L - 1]
        dis = [(p, cells[p], src[(L, p)], text[p - 1] if p <= len(text) else '>end') for p in sorted(cells)
               if not (p <= len(text) and text[p - 1] == cells[p])]
        unlogged = [d for d in dis if (L, d[0]) not in LOGGED]
        status = 'full' if ag == n else ('full-logged' if not unlogged else 'disagree')
        total['cells'] += n; total['agree'] += ag; total['f186'] += sum(1 for p in cells if src[(L, p)] == 'f186')
        rows.append(dict(line=L, printed=title[L - 1] if L - 1 < len(title) else '', n_chars=len(text), n_cells=n,
                         f186_cells=sum(1 for p in cells if src[(L, p)] == 'f186'),
                         tomokiyo_cells=sum(1 for p in cells if src[(L, p)] == 'tomokiyo'),
                         agree=ag, agree_frac=round(ag / n, 3), status=status,
                         disagreeing_cells=[f"{L}-{p} key={l} ({s}) page={t}" + (f" [logged: {LOGGED[(L, p)]}]" if (L, p) in LOGGED else '') for p, l, s, t in dis],
                         control_shuffled_mean=round(sum(shuf) / len(shuf), 3), control_shuffled_max=round(max(shuf), 3),
                         control_other_lines_mean=round(sum(others) / len(others), 3), control_other_lines_max=round(max(others), 3)))
    # the lines the 1761 page did not confirm (GAPS3): 9, 14, 15, 17, 18, 22, 24-27, plus line 21 and the tails of 16 and 23
    m61 = json.load(open(P('title_1761_map.json')))
    not61 = set(m61['lines_not_read'])
    unconfirmed_1761 = dict(lines=sorted(not61), cells=sum(r['n_cells'] for r in rows if r['line'] in not61),
                            agree=sum(r['agree'] for r in rows if r['line'] in not61))
    def read_cell(L, p):
        t = tl[L - 1] if L - 1 < len(tl) else ''
        return t[p - 1] if p <= len(t) else ''
    g61 = {r['n']: r['grade_now'] for r in read_tsv(P('m_tokens_1761.tsv'))}
    l61 = {r['n']: r['letter_1761'] for r in read_tsv(P('m_tokens_1761.tsv'))}
    for r in read_tsv(P('clause_2894.tsv')):      # the 1761 check letter beside the clause's C and H tokens too
        l61.setdefault(r['n'], r['letter_1761'])
    toks = read_tsv(P('tokens_2894.tsv'))
    out_rows = ['n\tref\tline\tpos\tword\tletter_gaps2\tgrade_gaps2\tgrade_gaps3\tletter_1761\tletter_1778\tgrade_now\tnote']
    clause = ['n\tref\tline\tpos\tletter_f186\tletter_tomokiyo\tletter_1761\tletter_1778\tgrade\tsource']
    grades = Counter(); clause_grades = Counter(); checks = Counter(); changes = Counter(); clause_text = []
    for t in toks:
        L, p = t['line'], t['pos']
        l78 = read_cell(int(L), int(p)) if (L.isdigit() and p.isdigit()) else ''
        g2 = t['grade']; g3 = g61.get(t['n'], g2); note = ''
        if g3 in ('M', 'I'):
            gnow = 'H' if l78 else 'M'
            if g3 == 'I' and l78 and l61.get(t['n'], '') and l61[t['n']] != l78:
                note = f"1761 gave {l61[t['n']]}, 1778 gives {l78}"
            if g3 == 'M' and not l78:
                note = 'cell beyond the printed line'
            changes[f'{g3}->{gnow}'] += 1
        else:
            gnow = g3
            if l78:
                ok = l78 == t['letter']
                checks['agree' if ok else 'disagree'] += 1
                if not ok:
                    note = f"page {l78} vs token {t['letter']}" + (' [logged]' if (int(L), int(p)) in LOGGED else '')
            else:
                checks['beyond'] += 1; note = 'cell beyond the printed line'
        grades[gnow] += 1
        out_rows.append('\t'.join([t['n'], t['ref'], L, p, t['word'], t['letter'], g2, g3, l61.get(t['n'], ''), l78 or '-', gnow, note]))
        if t['how'] == 'skip':
            tomo = t['tomokiyo']; f186 = t['letter'] if g2 == 'C' else ''
            letter = l78 or f186 or (tomo if g2 == 'H' else '')
            srcname = 'f186' if gnow == 'C' else ('1778' if l78 else ('tomokiyo' if g2 == 'H' and tomo else ''))
            clause.append('\t'.join([t['n'], t['ref'], L, p, f186, tomo, l61.get(t['n'], '-') or '-', l78 or '-', gnow, srcname]))
            clause_grades[gnow] += 1; clause_text.append(letter or '.')
    out = dict(title_source='archive.org listofgeneralfie00grea, page/n12 (scandata leaf 13, Title), 1778 printing (imprint MDCCLXXVIII) -- the key book itself',
               convention='letters a-z and the ampersand count as characters; spaces and punctuation do not',
               fixed_cells=dict(total=total['cells'], f186=total['f186'], tomokiyo=total['cells'] - total['f186'], agree=total['agree'],
                                agree_letters_only=per_conv['noamp'], agree_with_ampersand=per_conv['amp']),
               lines=rows, status_by_line={str(r['line']): r['status'] for r in rows},
               lines_unconfirmed_by_1761=unconfirmed_1761,
               line21=dict(printed=title[20], cells_9_10=tl[20][8:10], note="the 1778 page reads 'CORPS and in the ARMY': 21-9 21-10 = 'in'; Tomokiyo's 21-17 y agrees (y is the 17th character)"),
               token_grade_changes=dict(changes), fixed_token_checks=dict(checks), grades_now=dict(grades),
               clause_grades=dict(clause_grades), clause_letters=''.join(clause_text))
    new = {'title_1778_map.json': json.dumps(out, indent=1) + '\n',
           'tokens_2894_1778.tsv': '\n'.join(out_rows) + '\n',
           'clause_2894_1778.tsv': '\n'.join(clause) + '\n'}
    if a.check:
        bad = [k for k, v in new.items() if not os.path.exists(P(k)) or open(P(k)).read() != v]
        print('STALE: ' + ', '.join(bad) if bad else 'check ok: title_1778_map.json, tokens_2894_1778.tsv, clause_2894_1778.tsv regenerate identically')
        sys.exit(1 if bad else 0)
    for k, v in new.items():
        open(P(k), 'w').write(v)
    for r in rows:
        print(f"line {r['line']:>2} ({r['n_chars']:>2} chars): {r['n_cells']:>2} cells agree {r['agree']:>2} [{r['status']}] shuffled {r['control_shuffled_mean']} (max {r['control_shuffled_max']}) other-lines {r['control_other_lines_mean']} (max {r['control_other_lines_max']}) | {r['printed']}  {'; '.join(r['disagreeing_cells'])}")
    print(json.dumps({k: v for k, v in out.items() if k != 'lines'}, indent=1))
    print('\n'.join(clause))

if __name__ == '__main__':
    main()
