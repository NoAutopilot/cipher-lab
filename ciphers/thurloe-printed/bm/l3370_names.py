#!/usr/bin/env python3
"""THUR-3370: l.3370's word/name codes (and 481, 733 from l.83274 / l.86815) paired against the period key sheet.

python3 l3370_names.py [--check]
Reads bm/passes/<letter>_B1.tsv and _B2.tsv (two blind passes of Birch's printed gloss, no key shown) and bm/key_period_f117.tsv
(BL Add MS 4166 f.117, names 102-139). For every occurrence of a code in 100-195, 481 or 733 it takes the printed gloss word on that group
('^' continuation of a 'A, B' gloss gives the next coded group the next part), compares it with the sheet's value and writes
bm/l3370_names.tsv: code, birch_gloss (B1 | B2 with counts), sheet_value, verdict, n_occ, note.
Verdicts: agree (normalised equal, contained, or alias), agree-referent (alias table below: same person, different text), disagree,
sheet-silent (code not on the sheet). Disagreements are rule-4 data conflicts: logged, never settled by count. Does not touch
key_blankmarshall_7.tsv. Must NOT block: a gloss differing only by long-s read as f, a title expansion ("Duke of"), or a sheet value that
qualifies the name ("Ships belonging to Dunkirk" vs "Dunkirk"). Scoring is on glosses only, not on the ciphertext.
--check exits 1 if bm/l3370_names.tsv is stale.
"""
import csv, difflib, os, re, sys, collections
H = os.path.dirname(os.path.abspath(__file__))
LETTERS = ['l3370', 'l83274', 'l86815']
ALIAS = {  # code -> regex on the normalised gloss; same person/place, text differs (reported as agree-referent)
    104: r'chst',                   # "Ch. Stew(art)/St." = the sheet's K. Charles (Charles Stuart): referent, not text
    106: r'dyork', 123: r'd(of)?glouc',
    118: r'newburgh',               # sheet spells Newbrugh
}
def norm(s):
    s = s.lower().replace('ſ', 's')
    s = ''.join(c for c in s if c.isalpha())
    return s.replace('j', 'i').replace('v', 'u')
def nf(s):  # B1 reads long-s as f in these glosses
    n = norm(s).replace('f', 's')
    return n[3:] if n.startswith('the') and len(n) > 6 else n
def want(t): return t.isdigit() and (100 <= int(t) <= 195 or int(t) in (481, 733))
sheet = {}
for r in csv.DictReader(open(os.path.join(H, 'key_period_f117.tsv')), delimiter='\t'):
    sheet[int(r['value'])] = r['meaning']
occ = collections.defaultdict(list)   # code -> [(letter, pass, gloss)]
for L in LETTERS:
    for k in ('B1', 'B2'):
        rows = [r for r in csv.DictReader(open(os.path.join(H, 'passes', f'{L}_{k}.tsv')), delimiter='\t') if r['kind'] == 'N']
        for i, r in enumerate(rows):
            t = r['token'].strip().rstrip('.|')
            if not want(t): continue
            g = r['gloss'].strip().rstrip('~')
            if g == '^':
                # continuation: look back for the head and split 'A, B' by coded-group order
                j = i
                while j > 0 and rows[j]['gloss'].strip() == '^': j -= 1
                parts = [p.strip() for p in re.split(r',|\band\b', rows[j]['gloss']) if p.strip()]
                coded = [x for x in rows[j:i + 1] if want(x['token'].strip().rstrip('.|'))]
                g = parts[len(coded) - 1] if len(parts) >= len(coded) and len(coded) > 1 else '^(span interior)'
            else:
                g = re.sub(r'^and\s+', '', g)
            occ[int(t)].append((L, k, g))
# scope: l.3370's own occurrences; a code with none there (131, 173, 481, 733) falls back to the letters that carry it, said in the note
for c in list(occ):
    own = [x for x in occ[c] if x[0] == 'l3370']
    if own: occ[c] = own
SPANS = {169: ([169, 48, 18, 73], 'arms'), 191: ([27, 69, 191, 77], 'great')}  # l3370 rows 1 and 25, both passes: a word printed over a run
def span_note(c):
    codes, word = SPANS[c]
    pre = ''.join(sheet[x] for x in codes[:codes.index(c)]); suf = ''.join(sheet[x] for x in codes[codes.index(c) + 1:])
    w = norm(word)
    if w.startswith(pre) and w.endswith(suf) and len(w) > len(pre) + len(suf):
        return f"span '{word}' with the sheet's letters {pre or '-'} + [{c}] + {suf or '-'}: {c} = '{w[len(pre):len(w) - len(suf)]}' (M, single span)"
    return f"span '{word}' with the sheet's letters {pre or '-'} + [{c}] + {suf or '-'} does not fit exactly (period spelling 'armes' would give {c} = 'ar'; M)"
XREF = {733: "733 is not on the sheet; the sheet's 133 = Sr Mar: Langdale is the same referent as Birch's 'Sir Mar. Lang.' one digit apart (lead, M: a printed 7 for 1, or two codes)",
        173: "173 not on the sheet; the sheet's 113 = Ormond is the same referent (HYPOTHESES.md FIX-THURBM2 item b)",
        481: "481 not on the sheet; gloss 'Mar' is a fragment before 71 (l.83274 row 2)"}
out = ['code\tbirch_gloss\tsheet_value\tverdict\tn_occ\tnote']
for c in sorted(occ):
    lst = occ[c]
    cnt = collections.Counter(f'{k}:{g}' for _, k, g in lst)
    gl = ' | '.join(f'{g} x{n}' for g, n in sorted(cnt.items()))
    sv = sheet.get(c)
    letters = sorted({L for L, _, _ in lst})
    note = 'in ' + ','.join(letters)
    if sv is None:
        verdict = 'sheet-silent'
    else:
        vs = []
        for _, _, g in lst:
            n, s = nf(g.rstrip('?')), nf(sv)
            if g.startswith('^'): v = 'span'
            elif n == s or (len(n) > 2 and (n in s or s in n)): v = 'agree'
            elif c in ALIAS and re.match(ALIAS[c], n): v = 'agree-referent'
            elif difflib.SequenceMatcher(None, n, s).ratio() >= 0.75: v = 'agree-fuzzy'
            else: v = 'disagree'
            vs.append(v)
        u = set(vs) - {'span'}
        verdict = 'disagree' if 'disagree' in u else ('agree-referent' if 'agree-referent' in u else ('agree' if u else 'span-only'))
        if 'agree-fuzzy' in u and verdict == 'agree': note += '; includes a misread spelling within 0.75 similarity (M)'
    if c in SPANS: note += '; ' + span_note(c)
    if c in XREF: note += '; ' + XREF[c]
    if c == 115: note += "; both passes read 'Don John' over 115 (crop l3370_p31_L01.jpg, row 'Loven. Don John quarters'), the sheet has 105 = Don John and 115 = Rochester: rule-4 data conflict"
    out.append('\t'.join([str(c), gl, sv or '', verdict, str(len(lst)), note]))
text = '\n'.join(out) + '\n'
path = os.path.join(H, 'l3370_names.tsv')
if '--check' in sys.argv:
    cur = open(path).read() if os.path.exists(path) else ''
    if cur != text: print('STALE: l3370_names.tsv'); sys.exit(1)
    print('ok'); sys.exit(0)
open(path, 'w').write(text); print(text)
