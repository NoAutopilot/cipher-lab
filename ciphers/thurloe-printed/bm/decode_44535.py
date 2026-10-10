#!/usr/bin/env python3
"""THUR-BM step 3 (PREREG-THURBM.md): full Blank-Marshall key from the four glossed vol 6 letters, decode of l.44535.

python3 decode_44535.py [DJVU] [--check]
- key per blind pass (B1, B2) = tools/interlinear_align.py align on all four letters' bm/<line>_pairs_B<k>.tsv (written by
  bm_gate.py); bm/key_blankmarshall.tsv = codes whose B1 and B2 meanings agree (grade C, print gloss), disagreements listed (M).
- decode bm/l44535_ciphertext.tsv -> bm/reading_l44535.tsv (per token, grade) and bm/reading_l44535.txt.
- control (needs DJVU, the bim_ vol 6 djvu text): English 4-gram score of the decode's letter stream vs 200 shuffled-key decodes;
  corpus = vol 6 OCR lines with no digit, outside the Blank-Marshall windows (bm/bm_letters.tsv). Writes bm/control_l44535.tsv.
- FIX-THURBM (10 Oct 2026): LABELS relabels key codes after the alignment (123 = D. Gloucester, both glossed witnesses); slips.tsv
  regrades single groups of this letter to M (row, pos, grade, note, intended word shown in brackets after word_end); clear_rows.tsv
  restores the clear-text rows that carry no group (after_row, after_pos, text), taken from the page by V-THURBM's eye check.
--check: recompute and exit 1 if any committed output differs (the control is skipped and not compared when DJVU is absent).
"""
import csv, math, os, random, subprocess, sys, tempfile, collections
H = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(H, '..', '..', '..'))
LABELS = {123: 'D. Gloucester'}
LETTERS = ['l40469', 'l65889', 'l77385', 'l89881']
sys.path.insert(0, H)
def norm(s):
    s = s.lower().replace('ſ', 's'); s = ''.join(c for c in s if c.isalpha()); return s.replace('j', 'i').replace('v', 'u')

def train(k):
    with tempfile.TemporaryDirectory() as d:
        cat = os.path.join(d, 'p.tsv')
        with open(cat, 'w') as f:
            f.write('plain_line\tplain_raw\tcipher_line\tcipher_raw\n')
            for L in LETTERS:
                f.writelines(open(os.path.join(H, f'{L}_pairs_{k}.tsv')).readlines()[1:])
        ky = os.path.join(d, 'k.tsv')
        subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'interlinear_align.py'), 'align', cat, os.path.join(d, 'a.tsv'), ky], check=True, capture_output=True)
        return {int(r['value']): (r['meaning'], int(r['n'])) for r in csv.DictReader(open(ky), delimiter='\t') if r['value'].isdigit() and r['meaning']}

def build():
    k1, k2 = train('B1'), train('B2'); key, rows = {}, ['value\tmeaning\tkind\tn_B1\tn_B2\tgrade\tnote']
    for v in sorted(set(k1) | set(k2)):
        m1, m2 = k1.get(v, ('', 0)), k2.get(v, ('', 0))
        kind = 'letter' if v < 100 else 'code'
        if m1[0] and norm(m1[0]) == norm(m2[0]):
            key[v] = (m1[0], 'C'); rows.append(f'{v}\t{m1[0]}\t{kind}\t{m1[1]}\t{m2[1]}\tC\tBirch 1742 vol 6 printed gloss, both blind passes agree')
        else:
            key[v] = (m1[0] or m2[0], 'M'); rows.append(f'{v}\t{m1[0]}|{m2[0]}\t{kind}\t{m1[1]}\t{m2[1]}\tM\tB1|B2 meanings differ or one pass lacks the code')
    for v, lab in LABELS.items():
        if v in key:
            key[v] = (lab, key[v][1]); rows = [('\t'.join([r.split('\t')[0], lab] + r.split('\t')[2:]) if r.split('\t')[0] == str(v) else r) for r in rows]
    return key, '\n'.join(rows) + '\n'

def tsv_rows(name):
    p = os.path.join(H, name)
    return list(csv.DictReader(open(p), delimiter='\t')) if os.path.exists(p) else []

def decode(key, toks):
    slips = {(r['row'], r['pos']): r for r in tsv_rows('slips.tsv')}
    after = {}
    for r in tsv_rows('clear_rows.tsv'): after.setdefault((r['after_row'], r['after_pos']), []).append(r['text'])
    ends = {(r['word_end_row'], r['word_end_pos']): r['intended'] for r in slips.values() if r.get('intended')}
    out, tsv = [], ['row\tpos\ttoken\tmeaning\tgrade']
    for r in toks:
        if r['kind'] != 'N':
            out.append(r['token']); out.extend(after.get((r['row'], r['pos']), [])); continue
        v = int(r['token']) if r['token'].isdigit() else None
        m, g = key.get(v, ('[' + r['token'] + ']', 'unread'))
        sl = slips.get((r['row'], r['pos']))
        if sl: g = sl['grade']
        tsv.append(f"{r['row']}\t{r['pos']}\t{r['token']}\t{m}\t{g}")
        out.append(m.upper() if v is not None and v < 100 and g not in ('unread', 'M') else (m if g == 'M' and v is not None and v < 100 else '<' + m + '>'))
        if (r['row'], r['pos']) in ends: out.append('[' + ends[(r['row'], r['pos'])] + ']')
        out.extend(after.get((r['row'], r['pos']), []))
    return '\n'.join(tsv) + '\n', out

def stream(key, toks):
    s = []
    for r in toks:
        if r['kind'] == 'N' and r['token'].isdigit() and int(r['token']) < 100 and int(r['token']) in key:
            s.append(norm(key[int(r['token'])][0]))
        else:
            s.append(' ')
    return ''.join(s)

def ngram_model(djvu):
    L = open(djvu, encoding='utf-8', errors='ignore').read().split('\n'); skip = set()
    for r in csv.DictReader(open(os.path.join(H, 'bm_letters.tsv')), delimiter='\t'):
        skip.update(range(int(r['heading_line']) - 1, int(r['window_end'])))
    txt = ' '.join(norm(w) for i, l in enumerate(L) if i not in skip and not any(c.isdigit() for c in l) for w in l.split())
    c4, c3 = collections.Counter(), collections.Counter()
    for w in txt.split(' '):
        pass
    t = txt.replace(' ', '')
    for i in range(len(t) - 3):
        c4[t[i:i + 4]] += 1; c3[t[i:i + 3]] += 1
    return c4, c3, len(t)

def score(s, m):
    c4, c3, _ = m; tot, n = 0.0, 0
    for seg in s.split(' '):
        for i in range(len(seg) - 3):
            tot += math.log10((c4[seg[i:i + 4]] + 0.1) / (c3[seg[i:i + 3]] + 2.6)); n += 1
    return tot / n if n else float('nan')

def main():
    check = '--check' in sys.argv; args = [a for a in sys.argv[1:] if a != '--check']
    key, keytxt = build()
    toks = list(csv.DictReader(open(os.path.join(H, 'l44535_ciphertext.tsv')), delimiter='\t'))
    tsv, out = decode(key, toks)
    N = [r for r in toks if r['kind'] == 'N']
    sg = {(r['row'], r['pos']): r['grade'] for r in tsv_rows('slips.tsv')}
    g = collections.Counter(sg.get((r['row'], r['pos'])) or key.get(int(r['token']), ('', 'unread'))[1] for r in N)
    summ = f"groups {len(N)}; C {g['C']}; M {g['M']}; unread {g['unread']}; coverage {(g['C']+g['M'])/len(N):.3f}\n"
    txt = ' '.join(out) + '\n\n' + summ
    outs = {'key_blankmarshall.tsv': keytxt, 'reading_l44535.tsv': tsv, 'reading_l44535.txt': txt}
    if args and os.path.exists(args[0]):
        m = ngram_model(args[0]); ckey = {v: mg for v, mg in key.items()}
        real = score(stream(ckey, toks), m); vals = list(ckey.values()); codes = list(ckey); sh = []
        for s in range(200):
            vv = vals[:]; random.Random(s).shuffle(vv); sh.append(score(stream(dict(zip(codes, vv)), toks), m))
        sh.sort(); p95 = sh[int(.95 * 200)]
        outs['control_l44535.tsv'] = f"statistic\treal\tshuffle_mean\tshuffle_p95\tshuffle_max\tabove_p95\tcorpus_letters\nmean_log10_4gram\t{real:.4f}\t{sum(sh)/200:.4f}\t{p95:.4f}\t{sh[-1]:.4f}\t{real > p95}\t{m[2]}\n"
    bad = 0
    for f, t in outs.items():
        p = os.path.join(H, f)
        if check:
            if not os.path.exists(p) or open(p).read() != t: print('STALE', f); bad = 1
        else:
            open(p, 'w').write(t)
    if not check: print(txt); print(outs.get('control_l44535.tsv', 'control skipped (no DJVU)'))
    sys.exit(bad)
main()
