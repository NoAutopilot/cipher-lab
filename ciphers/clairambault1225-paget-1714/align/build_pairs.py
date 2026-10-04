#!/usr/bin/env python3
"""Build (gloss, cipher run) pairs for tools/interlinear_align.py from ../ciphertext.tsv (NEXT-PAG, 2 Oct 2026).

Each pair names the cipher runs it covers by (page, start position): a run is the contiguous stretch of
cipher tokens (kind cipher or cipher/insertion-clear) starting there; several starts chain one gloss that
continues across a manuscript line. The gloss text is what is written ABOVE those runs, read off
images/<page>.jpg by NEXT-PAG (rule 2: image over transcription) -- it often differs from the
insertion-clear rows of ciphertext.tsv, because both transcription passes merged many above-line
decipherment lines into the running clear text. Digit overrides (image reading over ciphertext.tsv) and
cipher numerals that repeat the gloss's own numeral (marked clear, grade I) are listed per pair.
Writes pairs.tsv (all pairs) and the held-out set is named in HELD_OUT.
    python3 build_pairs.py            # writes pairs.tsv
"""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__))
# id, page, starts, gloss as read above the runs, {pos: image digit}, numerals kept clear
PAIRS = [
    ('P01', 'f60R', [30], "Labbe Lomeliny", {}, []),
    ('P02', 'f60R', [44], "Venise", {}, []),
    ('P03', 'f60R', [69], "Lisle de", {}, []),
    ('P04', 'f60R', [75], "Labarque", {}, []),
    ('P05', 'f61L', [34, 47], "on verra quelques personnes a Genes", {}, []),
    ('P06', 'f61L', [56], "venue d'une procuration", {58: '90'}, []),
    ('P07', 'f61L', [70], "pour traitter avec eux", {}, []),
    ('P08', 'f61L', [80], "tiennent", {}, []),
    ('P09', 'f61L', [87], "de Lisle", {}, []),
    ('P10', 'f61L', [104], "Labbe", {}, []),
    ('P11', 'f61L', [121], "une portion", {}, []),
    ('P12', 'f61L', [146], "Labbe", {}, []),
    ('P13', 'f61L', [165], "Lisle", {}, []),
    ('P14', 'f61L', [199], "Labbe", {}, []),
    ('P15', 'f61R', [29], "a la vente de cette isle", {32: '233'}, []),
    ('P16', 'f65L', [38], "penetrer ce qui", {38: '192'}, []),
    ('P17', 'f65L', [48], "en secret", {}, []),
    ('P18', 'f65R', [45], "la Princesse de Parme et ses 2 oncles", {}, [55]),
    ('P19', 'f65R', [65], "de cette Princesse qu'on", {65: '87'}, []),
    ('P20', 'f65R', [80], "pour Reyne d'Espagne a toutes les belles", {}, []),
    ('P21', 'f66L', [1], "qualites qu'on", {}, []),
    ('P22', 'f66L', [7, 25], "Elle achevera sa 22e annee le 25 Octobre prochain", {}, [25, 31]),
    ('P23', 'f66L', [44, 77, 96], "nee le meme mois en mil six cens quatre vingt douze Elle est bien faite blonde "
                                   "Le Visage Rond Les traits fins et", {51: '97'}, []),
    ('P24', 'f66L', [112], "la taille belle", {}, []),
    ('P25', 'f66L', [121, 124], "Moyenne beaucoup", {125: '33'}, []),
    ('P26', 'f66L', [132], "d'Esprit et un air", {}, []),
    ('P27', 'f66L', [143, 149], "modeste", {}, []),
    ('P28', 'f66L', [181, 197, 202], "Madame la Duchesse sa Mere qui l'a toujours tenue sous les yeux", {189: '220'}, []),
    ('P29', 'f66L', [223], "luy donnent une", {}, []),
    ('P30', 'f66L', [232], "belle Education", {}, []),
    ('P31', 'f66L', [257], "cette mere", {}, []),
    ('P32', 'f66L', [266], "M le Duc de Parme son Mari epousa", {273: '223'}, []),
    ('P33', 'f66L', [288], "en 2e Nopces le Prince Francois Farnese", {}, [290]),
    ('P34', 'f66L', [311, 332], "le Duc de Parme Regnant frere du deffunct", {}, []),
    ('P35', 'f66L', [341, 352], "Elle n'a pas eu d'Infans", {}, []),
    ('P36', 'f66L', [360], "en avoir se", {}, []),
    ('P37', 'f66L', [367], "agee de 44 ans", {}, [371]),
    ('P38', 'f66R', [9], "quoyque ce Dernier Duc n'ait que 36", {}, [23]),
    ('P39', 'f66R', [33], "le Prince Antoine de Parme", {}, []),
    ('P40', 'f66R', [55], "frere du Duc de Parme qui n'a que 35 ans Mais", {59: '32', 61: '174'}, [63]),
    ('P41', 'f66R', [80], "Il n'est pas marie et n'a", {}, []),
    ('P42', 'f66R', [96], "pour le Mariage", {}, []),
    ('P43', 'f66R', [106], "la Jeune Princesse", {}, []),
    ('P44', 'f66R', [127, 140], "tous les biens de sa Maison", {}, []),
    ('P45', 'f66R', [145], "unique", {}, []),
    ('P46', 'f66R', [158, 161, 162], "lie et adoree de ses deux Princes qui", {}, []),
    ('P47', 'f66R', [181], "sont charmes de la voir epouser", {183: '223'}, []),
    ('P48', 'f66R', [201], "le Roy d'Espagne", {}, []),
    ('P49', 'f66R', [210], "issu", {}, []),
    ('P50', 'f66R', [217], "de France", {}, []),
    ('P51', 'f66R', [231], "une grande Partialite", {}, []),
    ('P52', 'f66R', [250], "Madame la Duchesse qui en de la Maison", {}, []),
    ('P53', 'f66R', [272, 292], "a toujours este de genie Allemand", {}, []),
    ('P54', 'f66R', [303, 309], "Jeune Princesse", {}, []),
    ('P55', 'f66R', [319, 326], "ses oncles", {}, []),
    ('P56', 'f66R', [337], "Made sa Mere", {}, []),
]
HELD_OUT = ['P10', 'P12', 'P14', 'P39']   # the three l'abbe pairs and the f66R 'de Parme' recurrence
CIPHER_KINDS = {'cipher', 'cipher/insertion-clear'}


def load():
    rows = list(csv.DictReader(open(os.path.join(HERE, '..', 'ciphertext.tsv'), encoding='utf-8'), delimiter='\t'))
    by = {}
    for r in rows:
        by.setdefault(r['line'], []).append(r)
    return by


def run_from(page_rows, start):
    """the run starting at position start; a single non-cipher token at start (an inline clear word,
    P46's 'le') is taken alone as clear."""
    out = []
    idx = [int(r['position']) for r in page_rows].index(start)
    if page_rows[idx]['kind'] not in CIPHER_KINDS:
        return [page_rows[idx]]
    for r in page_rows[idx:]:
        if r['kind'] not in CIPHER_KINDS:
            break
        out.append(r)
    return out


def main():
    by = load()
    with open(os.path.join(HERE, 'pairs.tsv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['plain_line', 'plain_raw', 'cipher_line', 'cipher_raw', 'page', 'positions', 'overrides', 'held_out'])
        for pid, page, starts, gloss, over, numerals in PAIRS:
            toks, poss, ov = [], [], []
            for s in starts:
                for r in run_from(by[page], s):
                    p = int(r['position'])
                    t = r['token']
                    if r['kind'] not in CIPHER_KINDS:
                        t = '[%s]' % t                       # inline clear word: classify_token -> clear
                    elif t == 'ILLEGIBLE':
                        t = '0?'                             # doubtful: may take a chunk, never a key entry
                    if p in over:
                        ov.append('%d:%s->%s' % (p, t, over[p]))
                        t = over[p]
                    if p in numerals:
                        t = '(%s)' % t                       # numeral repeated in the gloss: clear, grade I
                    toks.append(t)
                    poss.append(str(p))
            w.writerow([pid, gloss, pid, ' '.join(toks), page, ','.join(poss), ';'.join(ov),
                        'yes' if pid in HELD_OUT else ''])
    print('%d pairs' % len(PAIRS))


if __name__ == '__main__':
    main()
