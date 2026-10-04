# TX-SHEET (4 Oct 2026, account 3): secure exemplar positions for the per-hand sign sheet
# (tools/glyph_atlas.py atlas --from-truth). No no.87 leaf (f178r, f178v, f179r) is read: no.87 is the eval item.
# Rule (PREREG benchmark-tx/PREREG-txsheet.md): a box is a secure exemplar of code T when three instruments agree --
#   the two independent blind line-read passes A and B (harvest/<leaf>/passC_agreement.tsv status 'agree', idA == idB,
#   neither conf L) and the family atlas's kNN code for that box with every no.87 box held out of the vote
#   (classify --holdout f178r_ --holdout f178v_ --holdout f179r_). The box <-> token match is an LCS over each page's
#   reading order (agreement rows in file order vs non-'_' boxes by line, x) on equal codes; a matched pair counts only
#   inside a run of >= 2 consecutive matches (both neighbours' box and token matched in step), which keeps chance
#   matches out. No C/H-graded sign positions exist outside no.87 in this family (the clerk sheet is no.87's), so every
#   exemplar is S-grade by this rule. Limit: the atlas cluster names were partly set on no.87 tune lines (README.md);
#   that is why the atlas only filters what the two blind readers already agree on and never supplies a label alone.
# Run from the repo root:
#   python3 tools/glyph_atlas.py classify --out A --labels A/labels.json --page all --tsv HO87 \
#       --holdout f178r_ --holdout f178v_ --holdout f179r_
#   python3 ciphers/nevers-birago-fr3251-1572/atlas/secure_tokens.py HO87 > ciphers/nevers-birago-fr3251-1572/atlas/secure_tokens.tsv
import csv, collections, os, sys
R = os.path.dirname(os.path.abspath(__file__)); H = os.path.join(R, '..', 'harvest')
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
NO87 = ('f178r', 'f178v', 'f179r')
LEAVES = [('f139v', 'f139v/passC_agreement.tsv'), ('f144r', 'f144r/passC_agreement.tsv'),
          ('f152r', 'f152r/passC_agreement.tsv'), ('f162r', 'f162r/passC_agreement.tsv'),
          ('f174r', 'f174r/passC_agreement.tsv'), ('f174v', 'f174v/passC_agreement.tsv'),
          ('f174vB', 'f174vB/passC_agreement.tsv'), ('f175v', 'f175v/passC_agreement.tsv'),
          ('f184r', 'f184r/passC_agreement.tsv'), ('f185r', 'f185r/passC_rest90_agreement.tsv')]


def lcs(a, b):
    n, m = len(a), len(b)
    T = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            T[i][j] = T[i + 1][j + 1] + 1 if a[i] == b[j] else max(T[i + 1][j], T[i][j + 1])
    i = j = 0; out = []
    while i < n and j < m:
        if a[i] == b[j]: out.append((i, j)); i += 1; j += 1
        elif T[i + 1][j] >= T[i][j + 1]: i += 1
        else: j += 1
    return out


def main(ho87):
    boxes = collections.defaultdict(list)
    for r in rd(ho87):
        if r['page'] not in NO87 and r['code'] != '_':
            boxes[r['page']].append(r)
    print('sid\tcode\tpage\tgrade\tpassage\tpos')
    for leaf, fn in LEAVES:
        toks = []
        for r in rd(os.path.join(H, fn)):
            page = r['passage'].split('_')[0] if '_' in r['passage'] else leaf
            sign = r['merged'] or r['idA'] or r['idB']
            ok = (r['status'] == 'agree' and r['idA'] == r['idB'] and sign.startswith('T')
                  and 'L' not in (r['confA'], r['confB']))
            toks.append(dict(page=page, sign=sign, ok=ok, passage=r['passage'], pos=r['posA']))
        for page in sorted({t['page'] for t in toks}):
            if page in NO87:
                continue
            tk = [t for t in toks if t['page'] == page]
            bx = sorted(boxes.get(page, []), key=lambda r: (int(r['line']), int(r['x'])))
            m = lcs([t['sign'] for t in tk], [b['code'] for b in bx])
            ms = set(m)
            for i, j in m:
                run = ((i - 1, j - 1) in ms) or ((i + 1, j + 1) in ms)
                if run and tk[i]['ok']:
                    print(f"{bx[j]['box']}\t{tk[i]['sign']}\t{page}\tS\t{tk[i]['passage']}\t{tk[i]['pos']}")


if __name__ == '__main__':
    main(sys.argv[1])
