#!/usr/bin/env python3
"""RUN2-NXDUP: build the Dupuy 521 221R-226R clear text (the 6/7 July 1574 letter to the King) from the reconciled pages.

usage: build_texts.py [--check]
Reads reconciled/<page>.txt (one manuscript line per text line, diplomatic: abbreviations as written, ^ = superscript,
':' = the copyist's line-end hyphen, [?] = uncertain, CATCH:/HEAD: = catchword/heading, {DITTO: ...} = a copyist's
repetition) and writes:
  dupuy221_226_diplomatic.txt  page and line markers, text as reconciled;
  dupuy221_226_norm.txt        rule 3 (PX-BRODEC) normalisation, one line per manuscript page:
     - HEAD lines, catchwords, {DITTO} repetitions, '&c.' (the copyist's truncation mark) and [?] marks dropped;
     - line-end ':' joins the two halves of a word; other line ends are word breaks;
     - abbreviations expanded (table ABBR below), '&' -> 'et';
     - lower case; apostrophes become word breaks (j'ay -> j ay); every other non-letter dropped; diacritics
       stripped (é -> e, ç -> c); u/v and i/j KEPT AS WRITTEN in the reconciled text (no u/v or i/j mapping applied);
       digits kept (the date '1574').
--check exits 1 if either committed output differs from what the reconciled pages produce (rule 7).
"""
import os, re, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = ['221R', '222L', '222R', '223L', '223R', '224L', '224R', '225L', '225R', '226L', '226R']
ABBR = [(r'Ma\^te', 'maieste'), (r'dupp\^tas', 'duplicatas')]

def diplomatic():
    out = ['# Dupuy 521 (Gallica btv1b100339270) canvases 221R-226R: Acqs (Noailles) to the King, Pera, vj Juillet 1574.',
           '# Reconciled diplomatic text, RUN2-NXDUP (4 Oct 2026). Format: see build_texts.py docstring.']
    for p in PAGES:
        out.append(f'== {p}')
        for i, l in enumerate(open(os.path.join(HERE, 'reconciled', p + '.txt'), encoding='utf-8').read().splitlines(), 1):
            out.append(f'{p}.{i:02d}\t{l}')
    return '\n'.join(out) + '\n'

def norm_page(lines):
    buf = ''
    for l in lines:
        if l.startswith(('HEAD:', 'CATCH:')):
            continue
        l = re.sub(r'\{DITTO:[^}]*\}', ' ', l).replace('[?]', '').replace('&c.', ' ').replace('—', ' ')
        l = l.replace('[', '').replace(']', '')
        for a, b in ABBR:
            l = re.sub(a, b, l)
        l = l.replace('&', ' et ').strip()
        if buf.endswith(':'):
            buf = buf[:-1] + l
        else:
            buf = (buf + ' ' + l) if buf else l
    buf = buf.rstrip(':')
    s = unicodedata.normalize('NFD', buf.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[’']", ' ', s)
    s = re.sub(r'[^a-z0-9 ]', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()

def normalised():
    out = ['# Dupuy 521 221R-226R normalised (rule 3 PX-BRODEC convention; see build_texts.py). One line per manuscript page.']
    for p in PAGES:
        out.append(f'{p}\t' + norm_page(open(os.path.join(HERE, 'reconciled', p + '.txt'), encoding='utf-8').read().splitlines()))
    return '\n'.join(out) + '\n'

def main():
    want = {'dupuy221_226_diplomatic.txt': diplomatic(), 'dupuy221_226_norm.txt': normalised()}
    if '--check' in sys.argv:
        bad = [f for f, t in want.items() if not os.path.exists(os.path.join(HERE, f)) or open(os.path.join(HERE, f), encoding='utf-8').read() != t]
        print('stale: ' + ', '.join(bad) if bad else 'OK: committed texts match reconciled/')
        sys.exit(1 if bad else 0)
    for f, t in want.items():
        open(os.path.join(HERE, f), 'w', encoding='utf-8').write(t)
    n = sum(len(l.split('\t', 1)[1].split()) for l in want['dupuy221_226_norm.txt'].splitlines()[1:])
    print(f'wrote {len(want)} files; normalised words {n}, letters {sum(c.isalpha() for c in want["dupuy221_226_norm.txt"].split(chr(10),1)[1])}')

if __name__ == '__main__':
    main()
