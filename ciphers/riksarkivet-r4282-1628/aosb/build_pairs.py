#!/usr/bin/env python3
"""Build pairs.tsv from the reconciled footnote transcription (stream_reconciled.txt) of AOSB ser. I Band 4
(1909) letter 231, Oxenstierna to Paul Strasburg, Elbing 24 Jan 1629, pp. 341-342: each footnote's cipher
tokens beside the asterisked clear passage it covers (AOSB-PAIRS, 4 Oct 2026).
cipher_print = tokens as printed (superscript marks kept); cipher_raw = aligner input:
  @NN    a 1-2 digit number (letter class, 0-1 plain letters)
  @SIGN  a letter/Greek sign (letter class too: first alignment showed Q=i, O=l, F=t, V=e, N=m ... single letters)
  %CODE  a 3-4 digit number (base value, superscript marks dropped; word/name class, 0..n letters)
The printed correction "846 recte 1369" (p.342 fn5) is aligned as 1369.
Then: python3 tools/interlinear_align.py align pairs.tsv align.tsv align_key_raw.tsv --code-prefix @ \
      --word-code-prefix % --max-chunk 16      (tokens 553; agrees 475, conflict 34)
and   python3 aosb_crossmatch.py [--check]     (key_aosb1629.tsv, results.json; PREREG-AOSB-PAIRS.md)"""
import re, sys
HERE = __file__.rsplit('/', 1)[0] or '.'
PLAIN = {
 '341.2': 'Quas nunc cum Principis Transylvaniae Legato dedisti illae mihi recte sunt redditae',
 '341.3': 'ipsum Legatum convenire non liceat',
 '341.4': 'Quae scribis mihi de statu rerum consiliis et intentione Turcae Moschi Tartari',
 '341.5': 'Princeps sentiat de electione Poloniae Regis si hunc mori contingat aliaque',
 '341.6': 'et quantocius ad Regem meum referam',
 '341.8': 'habiturus sis prima opportunitate responsum ad Principem deferendum Ego haec magni momenti puto esse ac te in omnibus caute debere progredi Si Principem aliquo inclinare intellexeris vel ad electionem sui ipsius',
 '342.1': 'electionem Regis mei promovendam',
 '342.2': 'ut destinata ipsius foveas',
 '342.3': 'perspexeris illa propendere',
 '342.4': 'Interim sicuti',
 '342.5': 'ne intermittas directe aut indirecte Principem ipsum in Polonos concitare dum Rex Poloniae in vivis est',
 '342.6': 'ut Turca Tartarus Moschus excitetur',
 '342.7': 'res et destinata Regis mei Noris etiam Farensbachium fuisse',
 '342.8': 'servitiaque sua obtulisse',  # cipher order; the edition prints 'suaque servitia'
 '342.10': 'ad Principem Transylvaniae certis cum mandatis missum esse ut conductis Siculorum',
 '342.11': 'et adjunctis Tartaris impressionem in Poloniam faceret atque armis sibi transitum pararet',
}
def main():
    toks = [t for l in open(HERE + '/stream_reconciled.txt') if not l.startswith('#') for t in l.split()]
    page, fn, cur, out = '341', '2', [], {}
    for t in toks:
        m = re.fullmatch(r'\|fn(\d+)\|', t)
        if t == '|p342|':
            page = '342'; continue
        if m:
            if cur: out.setdefault(prev, []).extend(cur)
            fn = m.group(1); cur = []
            continue
        prev = page + '.' + fn if not cur else prev
        cur.append(t)
    if cur: out.setdefault(prev, []).extend(cur)
    # p.341 fn8 continues on p.342 before p.342 fn1: the |p342| switch happens mid-footnote
    rows = []
    for key in PLAIN:
        cp = out.get(key, [])
        cp2 = []
        i = 0
        while i < len(cp):
            if i + 2 < len(cp) and cp[i + 1] == 'recte':
                cp2.append(cp[i + 2]); i += 3; continue
            cp2.append(cp[i]); i += 1
        raw = []
        for t in cp2:
            base = re.sub(r"(\^\?|['a]+)$", '', t)
            if re.fullmatch(r'[\d?]{1,2}', base): raw.append('@' + base)
            elif re.fullmatch(r'[\d?]{3,4}', base): raw.append('%' + base)
            else: raw.append('@' + base)
        rows.append((key, PLAIN[key], ' '.join(cp), ' '.join(raw)))
    with open(HERE + '/pairs.tsv', 'w') as f:
        f.write('plain_line\tplain_raw\tcipher_line\tcipher_print\tcipher_raw\n')
        for k, p, cp, raw in rows:
            f.write('\t'.join([k, p, k, cp, raw]) + '\n')
    for k, p, cp, raw in rows:
        n_l = len(re.sub('[^a-z]', '', p.lower())); n2 = sum(1 for x in raw.split() if x.startswith('@'))
        print(k, 'letters', n_l, 'two-digit', n2, 'other', len(raw.split()) - n2)
main()
