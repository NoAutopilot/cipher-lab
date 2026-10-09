"""BRANDT-TX (9 Oct 2026): cut ciphertext_0020.tsv and gloss_0020.txt into (cipher run, gloss span) pairs at the clear words
the writer left among the groups, as PREREG-BRANDT-TX.md fixes. Separators (|) and the superscript correction (sup:53) are dropped.
The cipher after the last glossed anchor ('hat' + its run, L18) -- L19-L21, about 40 groups -- has no gloss beside it and is left out.
Usage: python3 make_pairs.py [--check]   (exit 1 if pairs_0020.tsv is stale)"""
import csv, sys
toks = [r for r in csv.DictReader((l for l in open('ciphertext_0020.tsv') if not l.startswith('#')), delimiter='\t')]
seq = [(r['line'], r['token']) for r in toks if r['token'] != '|' and not r['token'].startswith('sup:')]
# anchors: (clear word(s) in the cipher stream, in order) ; gloss spans between them, in order
ANCH = ['sonderlich', 'auch', 'undt', 'undt nahmen', 'da die', 'undt', 'bis', 'der', 'hat']
GLOSS = ['der koenig ist oft masquirt dahin kommen',
         'vorgestern da die tragedie vom koenig in engelandt carl stuard agirt wurde kamen sie',
         'daher mit gueldenlew der selbst auf englische manier wollen',
         'andere cavalliern',
         'die masquen ab',
         'tragedie halb aus war',
         'blieben',
         'zum ende',
         'englische resident',
         'dieses uebel genommen']
segs, cur, lines, i = [], [], set(), 0
words = [t for _, t in seq]
k = 0
while i < len(seq):
    line, t = seq[i]
    if t.startswith('w:'):
        a = ANCH[k].split()
        got = [w[2:] for w in words[i:i + len(a)]]
        assert got == a, (i, got, a)
        segs.append((cur, sorted(lines))); cur, lines = [], set(); k += 1; i += len(a)
        if k == len(ANCH):
            # last anchor: its run is the rest of line L18 only (the gloss ends there)
            while i < len(seq) and seq[i][0] == 'L18':
                cur.append(seq[i][1]); lines.add('L18'); i += 1
            segs.append((cur, ['L18'])); break
        continue
    cur.append(t); lines.add(line); i += 1
assert len(segs) == len(GLOSS), (len(segs), len(GLOSS))
out = 'plain_line\tplain_raw\tcipher_line\tcipher_raw\n' + ''.join(
    'g%02d\t%s\tS%02d:%s\t%s\n' % (n + 1, g, n + 1, '-'.join(ls), ' '.join(c)) for n, ((c, ls), g) in enumerate(zip(segs, GLOSS)))
if '--check' in sys.argv:
    sys.exit(0 if open('pairs_0020.tsv').read() == out else 1)
open('pairs_0020.tsv', 'w').write(out)
print(out)
