#!/usr/bin/env python3
"""Hard-EM alignment of the reconciled cipher groups (ciphertext.tsv) against the interlinear decipherment
(dechiffre.tsv) of the two Vergier letters in Clairambault 1108 (f.253 = 26 Mar 1696; f.265 undated) (24 Sept 2026).

The EM, Viterbi and consistency code is ciphers/clair1067-brienne-poland-1646/align_1646.py's, imported unchanged.
Each SPAN is one continuous cipher run (no clear word inside it; runs flow across line ends) with the words the
decipherer wrote above it. A name written [text|sym] in a span's words is one symbol for the aligner (longer than the
7-letter cap): Milord Myddleton '#' (722, three times), Roy d'Angleterre '%' (720, where no groups spell it out),
Prince d'Orange '&' (725), Angleterre '@' (105, twice after 16 'd'). A part (leaf, row, run, start, end) takes a slice
of a run: the glosser left some groups unglossed at a run's edge (B08 start).

  python3 align_1696.py              write align_1696.tsv and key_1696.tsv, print the alignment per span
  python3 align_1696.py --control N  true pairing against N shuffled span/gloss pairings (same EM, same scoring)
"""
import csv, importlib.util, os, random, re, sys, unicodedata
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    'a1646', os.path.join(HERE, '..', 'clair1067-brienne-poland-1646', 'align_1646.py'))
A = importlib.util.module_from_spec(spec)
spec.loader.exec_module(A)

PRINT = {'#': 'Milord Myddleton', '%': "Roy d'Angleterre", '&': "Prince d'Orange", '@': 'Angleterre', '': '0'}

# (span id, [(leaf, row, run index within the row)], decipherer's words).  Read from the images (rows.tsv).
SPANS = [
    ('A01', [('f253L', 'R01', 0)], "[Milord Myddleton|#] et Jay eu une"),
    ('A02', [('f253L', 'R02', 0)], "longue conference avec luy"),
    ('A03', [('f253L', 'R03', 0)], "plus empressé que de coustume"),
    ('A04', [('f253L', 'R04', 0)], "pour l'entreprise"),
    ('A05', [('f253L', 'R06', 0)], "l'affaire est a present"),
    # A06: the gloss stands over R07 only, but the words run on into R08's first run ('281 29 / 195 .. 32' =
    # 'sur la coste de Kent' under the first key, which had left them out)
    ('A06', [('f253L', 'R07', 0), ('f253L', 'R08', 0)], "presque impraticable sur la Coste de Kent"),
    ('A08', [('f253L', 'R08', 1), ('f253L', 'R09', 0)], "forces que le [Prince d'Orange|&]"),
    ('A09', [('f253L', 'R10', 0), ('f253L', 'R11', 0), ('f253L', 'R12', 0)],
     "tenter le desbarquement dans les Province d'York ou sont presque tous les haras d'[Angleterre|@]"),
    ('A10', [('f253L', 'R13', 0), ('f253L', 'R14', 0), ('f253L', 'R15', 0)],
     "on trouveroit les chevaux necessaires pour l'armée ou bien dans une des Provinces de l'Ouest"),
    ('A11', [('f253L', 'R16', 0), ('f253L', 'R17', 0)],
     "y en a abondance ensorte que l'armée y subsisteroit aisement"),
    ('A12', [('f253L', 'R18', 0)], "faire la descente dans ces deux lieux la a la fois"),
    # f253R R01 run 0 '155 44 30.' continues A12 on the new page and carries no gloss (not aligned)
    ('A13', [('f253R', 'R01', 1), ('f253R', 'R02', 0), ('f253R', 'R03', 0), ('f253R', 'R04', 0)],
     "de faire embarquer a Brest Les Troupes destinées pour l'Ouest et a Calais celles destinées pour York"),
    ('A14', [('f253R', 'R04', 1)], "son projet"),
    ('A15', [('f253R', 'R08', 0), ('f253R', 'R09', 0)],
     "Il compte sur la fidelité de plusieurs personnes dans ce pays la"),
    ('A16', [('f253R', 'R12', 0), ('f253R', 'R13', 0), ('f253R', 'R14', 0)],
     "d'intelligence ny mesme de Correspondance car ils n'en recoivent aucune nouvelle ny par la Hollande ny d'ailleurs"),
    ('A17', [('f253R', 'R15', 0), ('f253R', 'R16', 0)], "du chevalier Giraudin"),
    ('A18', [('f253R', 'R16', 1), ('f253R', 'R17', 0)], "Irlandois estably a Dunkerque"),
    ('B01', [('f265L', 'R08', 0), ('f265L', 'R09', 0)],
     "a mon despart un tour qui n'a pas despleu au [Roy d'Angleterre|%]"),
    ('B02', [('f265L', 'R10', 0), ('f265L', 'R11', 0), ('f265L', 'R12', 0)],
     "Je luy ay fait entendre que me voyant icy inutile pour son service"),
    ('B03', [('f265L', 'R13', 0), ('f265L', 'R14', 0), ('f265L', 'R15', 0), ('f265L', 'R16', 0)],
     "a M vostre Pere la permission de m'en retourner a Dunkerque pour y ayder a avancer l'armement"),
    ('B04', [('f265L', 'R17', 0)], "inutile a Boulogne Je pourrois"),
    ('B05', [('f265L', 'R18', 0), ('f265L', 'R19', 0), ('f265L', 'R20', 0)],
     "Le Roy d'[Angleterre|@] approuvast mon despart que comme Il m'avoit"),
    ('B06', [('f265L', 'R20', 1), ('f265L', 'R21', 0)], "me mettre sous ses ordres"),
    ('B07', [('f265L', 'R22', 0), ('f265L', 'R23', 0)],
     "faire aucun mouvement sans son ordre exprés Il m'a paru fort touché de cette honnesteté de"),
    ('B08', [('f265R', 'R01', 0, 10, 99), ('f265R', 'R02', 0)], "M de Pontchartrain et de mon"),
    ('B09', [('f265R', 'R03', 0), ('f265R', 'R04', 0), ('f265R', 'R05', 0), ('f265R', 'R06', 0)],
     "Il est tres persuadé que l'armement de Dunkerque regarde la descente et doit se joindre a M"),
    ('B10', [('f265R', 'R08', 0)], "Je suis"),
    ('B11', [('f265R', 'R09', 0), ('f265R', 'R10', 0)],
     "avec [Milord Myddleton|#] et avec tout ce qu'il y a icy d'Anglois un peu"),
    ('B12', [('f265R', 'R11', 0), ('f265R', 'R12', 0)], "Eux en coterie journaliere de desbauche et de plaisir"),
    ('B13', [('f265R', 'R13', 0)], "en [Milord Myddleton|#]"),
]


def norm(s, align=True):
    s = re.sub(r'\[([^|\]]*)\|([^\]]*)\]', lambda m: m.group(2) if align else m.group(1), s).lower()
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn').replace('v', 'u').replace('j', 'i')
    return re.sub(r'[^a-z#%&@]', '', s)


def runs():
    """(leaf, row) -> list of runs, each a list of (pos, group); a clear or struck token ends a run."""
    out = defaultdict(list)
    cur = {}
    for r in csv.DictReader(open(os.path.join(HERE, 'ciphertext.tsv'), encoding='utf-8'), delimiter='\t'):
        k = (r['leaf'], r['row'] if 'row' in r else r['line'])
        if k not in cur:
            cur[k] = None
        if r['layer'] == 'cipher':
            if cur[k] is None:
                cur[k] = []
                out[k].append(cur[k])
            cur[k].append((int(r['pos']), r['token']))
        else:
            cur[k] = None
    return out


def load():
    R = runs()
    segs = []
    for sid, parts, words in SPANS:
        toks = [(leaf, row, p, g) for leaf, row, i, *sl in parts
                for p, g in (R[(leaf, row)][i][sl[0]:sl[1]] if sl else R[(leaf, row)][i])]
        segs.append((sid, toks, norm(words)))
    return segs


def check_glosses():
    """The span glosses, joined, must be the dechiffre.tsv rows, joined (struck words dropped)."""
    rows = [r['words'] for r in csv.DictReader(open(os.path.join(HERE, 'dechiffre.tsv'), encoding='utf-8'), delimiter='\t')]
    a = norm(' '.join(re.sub(r'\{[^}]*\}|\.\.\.', '', w) for w in rows), False)
    b = norm(' '.join(s[2] for s in SPANS), False)
    if a != b:
        sm = __import__('difflib').SequenceMatcher(None, a, b, autojunk=False)
        for op in sm.get_opcodes():
            if op[0] != 'equal':
                print('gloss mismatch', op, a[op[1]:op[2]], '|', b[op[3]:op[4]])
        sys.exit('span glosses differ from dechiffre.tsv')


def control(n):
    segs = [(s, [t[3] for t in toks], text) for s, toks, text in load()]
    c, _, ll = A.em(segs, restarts=2)
    print(f'true pairing      consistency {A.consistency(c):.3f}  loglik {ll:.1f}')
    rng = random.Random(1696)
    vals = []
    for k in range(n):
        texts = [s[2] for s in segs]
        while True:
            rng.shuffle(texts)
            if all(t != s[2] for t, s in zip(texts, segs)):
                break
        cc, _, l2 = A.em([(s[0], s[1], t) for s, t in zip(segs, texts)], restarts=2)
        vals.append((A.consistency(cc), l2))
        print(f'shuffled pairing {k + 1:2d} consistency {vals[-1][0]:.3f}  loglik {l2:.1f}')
    print(f'shuffled: consistency max {max(v[0] for v in vals):.3f} mean {sum(v[0] for v in vals) / n:.3f}; '
          f'loglik max {max(v[1] for v in vals):.1f}')


def main():
    check_glosses()
    if '--control' in sys.argv:
        return control(int(sys.argv[sys.argv.index('--control') + 1]))
    spans = load()
    counts, res, ll = A.em([(s, [t[3] for t in toks], text) for s, toks, text in spans])
    with open(os.path.join(HERE, 'align_1696.tsv'), 'w') as f:
        f.write('line\tpos\tgroup\tplain\tspan\n')
        for (sid, toks, text), (_, groups, al) in zip(spans, res):
            for t, a in zip(toks, al):
                f.write(f'{t[0]}_{t[1]}\t{t[2]}\t{t[3]}\t{PRINT.get(a, a)}\t{sid}\n')
            print(sid, ' '.join(f'{g}={a or "0"}' for g, a in zip(groups, al)))
    with open(os.path.join(HERE, 'key_1696.tsv'), 'w') as f:
        f.write('code\tvalue\tgrade\tevidence\toccurrences\tother_values\tnote\n')
        for g in sorted(counts, key=int):
            c = counts[g]
            v, n = c.most_common(1)[0]
            tot = sum(c.values())
            other = ','.join(f'{PRINT.get(k, k)}:{m}' for k, m in c.most_common()[1:])
            note = 'single attestation' if tot == 1 else ('conflict' if n / tot < 0.75 else ('minor conflict' if other else ''))
            f.write(f'{g}\t{PRINT.get(v, v)}\tC\t{n}\t{tot}\t{other}\t{note}\n')
    print(f'consistency {A.consistency(counts):.3f}  groups {len(counts)}  loglik {ll:.1f}')


if __name__ == '__main__':
    main()
