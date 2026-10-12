#!/usr/bin/env python3
"""Build keys/hmc6_gualterio.tsv and keys/hmc6_sicily.tsv from the printed keys in HMC, Calendar of the Stuart
Papers vol. VI (1916), introduction pp. lxxvi-lxxxiii (archive.org calendarofstuart06grea, leaves n81-n88).

Input: hmc6_rows_ocr.tsv (the item's own _djvu.xml words grouped into rows by y-centre and split into the term
column and the cant-name column by x; GUALT-HMC, 12 Oct 2026). Pairing is by printed row; a cant name on a row
with no term belongs to the brace of the nearest term above or below (the print braces 2-3 cant names to one term,
image-checked on leaves 81 and 83). FIXES holds every correction made by eye on the strip crops in
../images/hmc6/ (leaves 81, 83, 86, 88) or by an evident OCR substitution (Due->Duc, Koy->Roy, on->ou).

Grade: H = row on an image-checked leaf (81, 83, 86, 88); M = row on a leaf not image-checked (82, 84, 85, 87),
OCR only, or a row whose pairing rests on a brace not seen. No ciphertext is on disk; nothing here is tested.
Usage: build_hmc6_keys.py [--check]   (--check exits 1 if the committed TSVs differ from a rebuild)
"""
import csv, re, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
CHECKED = {81, 83, 86, 88}
PAGE = {81: 'lxxvi', 82: 'lxxvii', 83: 'lxxviii', 84: 'lxxix', 85: 'lxxx', 86: 'lxxxi', 87: 'lxxxii', 88: 'lxxxiii'}
# (leaf, y) -> (term, cant) replacing the OCR row; None drops the row. Eye-read on the crops unless marked.
FIXES = {
    (86, 528): ("Les Irlandois", "Mr. Jenkins."), (86, 601): ("Les Jacobites", "Mr. Janson."),
    (86, 683): ("Les Jesuites", "Mr. Jolly."), (86, 911): ("La Lorraine", "Liége."),
    (86, 1052): ("Le Duc de Lauzun", "Mr. Launois."), (86, 1072): None,
    (86, 1125): ("Londres", "Limbourg."), (86, 1198): ("Chevalier Lily", "Mr. Lister."), (86, 1219): None,
    (86, 1449): ("Madame de Maintenon", "Mr. Menar."),
    (86, 2174): ("Mariage", "Mr. Maronis."), (86, 2193): None,
    (86, 2245): ("Duc de Modene", "Mr. Maurois."), (86, 2266): None,
    (86, 2497): ("Le Cardinal de Noailles", "Mr. de Neuville ou Nettancour."), (86, 2580): None,
    (86, 2798): ("Negotiation", "Mr. Nollan."), (86, 2870): ("Mr. Nairne", "Mr. Neutton."),
    (86, 2934): ("Le Nord", "Mr. Panetier."),
    (86, 3390): ("Les officiers de sa Sainteté en Avignon", "Mr. Offin."), (86, 3462): None,
    (83, 1114): ("M. Le Regent de France", "M. Ranucci ou M. Ricanati."), (83, 1152): None, (83, 1188): None,
    (83, 1375): ("Le Roy de Sicile", "M. Stella."), (83, 1449): ("Le Roy de Sicile", "M. Sansome, ou M. Salvador."),
    (83, 1523): None, (83, 1598): ("Le Roy de Suede", "M. Stampa."), (83, 1672): ("La Reine de Sicile", "MM. Santochi."),
    (81, 1505): ("Le Roy d'Angleterre", "Mr. Alba."), (81, 1653): ("Le Roy d'Angleterre", "Mr. Aquino."),
    (81, 1949): ("Cardinal Aquaviva", "Mr. Alpiggi."),
    (82, 1012): ("La guerre", "M. Goddar."), (82, 1031): None, (86, 4197): None,
    # OCR-only leaves (not image-checked): multi-line cells joined by row geometry; graded M
    (84, 765): None, (84, 837): ("Les Amis du Roy d'Angleterre", "Mr. Alexandre."),
    (84, 2675): ("Le frere de Mr. Bufalini demeurant a Rome", "Mr. Bulau."), (84, 2711): None,
    (84, 2749): None, (84, 2765): None,
    (87, 3918): None, (87, 3990): ("L'union d'Angleterre et d'Ecosse", "Mr. Urbin."),
}
OCR_SUBS = [(r'\bDue\b', 'Duc'), (r'\bKoy\b', 'Roy'), (r'\bon\b', 'ou'), (r'Expr6s', 'Exprès'), (r"L'ltalie", "L'Italie"),
            (r'SteUa', 'Stella'), (r'-Stampa', 'Stampa'), (r"d' ", "d'"), (r'\s+', ' '), (r'Ac qua viva', 'Acqua viva'),
            (r'Mr\. \.Lambert', 'Mr. Lambert'), (r'Par me', 'Parme'), (r'Savoy e', 'Savoye'), (r'Cavaillon\.', 'Cavaillon')]
SKIP = re.compile(r'^(?:[A-Z0]|l?x+[ivxl]*|I[xv]+[ivxl]*|lxx\w*|Ixx\w*)$')
NAMEY = re.compile(r"^(?:Le |La |Les |L'|Mr|M\.|Milord|Cardinal|Comte|Duc|Duca|Abbe|Monsieur|P\.|Pere|Principessa|Prince|Princesse|Roy|Marechal|Madame|Chevalier|Agent|Alberoni|Daubanton|Douglas|Bar )")
WORDS = {"Argent", "Armee", "Armes", "Armee Navalle", "Adresse", "Ennemis", "Entreprise", "Exprès", "Mariage", "Pension",
         "Religion", "Retablissement", "Retablessement", "Succession", "Voiage", "Vaisseaux", "Catholique", "Cardinal",
         "Congregation", "Consistoire", "Cour", "Courrier", "Eloignement", "Ecclesiastique", "Electeur", "Flotte",
         "Negotiation", "Passeports", "Pontificat", "Promotion", "Propaganda", "Seurete", "Secretaire", "Des Troupes"}

def clean(s):
    for a, b in OCR_SUBS: s = re.sub(a, b, s)
    return s.strip()

def kind(term):
    if term in WORDS or term.lower().startswith(('la guerre', 'la paix', 'la mission', 'la mort', 'la nomination',
                                                   'le parlement', 'le protectorat', 'les ', 'la flote', 'la flotte',
                                                   'le clerge', 'la chambre', 'parti ', 'passe ', 'douaire', "l'union")):
        return 'word'
    return 'name'

def build():
    rows = list(csv.DictReader(open(os.path.join(HERE, 'hmc6_rows_ocr.tsv')), delimiter='\t'))
    keys = {'sicily': [], 'gualterio': [], 'gualterio_figure': [], 'sicily_alphabet': []}
    cur = None
    for r in rows:
        leaf, y = int(r['leaf']), int(r['y'])
        if leaf == 88 and y > 700: break  # figure key and the Noailles cipher follow; figure key handled below
        full = clean(r['left'] + ' ' + r['right'])
        if 'King of Sicily' in full: cur = 'sicily'; continue
        if 'cipher used with Cardinal Gualterio' in full: cur = 'gualterio'; continue
        if 'Alphabet' in r['left'] or (leaf == 83 and y >= 3600): continue
        if cur is None: continue
        fix = FIXES.get((leaf, y), False)
        if fix is None: continue
        if fix is False:
            term, cant = clean(r['left']), clean(r['right'])
            if not term or not cant or SKIP.match(term) or SKIP.match(cant): continue
            eye = False
        else:
            term, cant = fix; eye = leaf in CHECKED
        grade = 'H' if leaf in CHECKED else 'M'
        note = 'eye-corrected on crop' if eye else ('OCR row joined by geometry' if fix is not False else 'OCR')
        for c in re.split(r',? ou ', cant.rstrip('.,')):
            c = c.strip().rstrip('.,')
            keys[cur].append((c, term, kind(term), grade, f'n{leaf}', PAGE[leaf], note))
    for L, a, b in zip('ABCDEFGHILM', [74, 72, 70, 68, 66, 65, 62, 61, 59, 57, 55], [24, 22, 71, 23, 20, 18, 19, 17, 14, 16, 15]):
        keys['gualterio'] += [(str(a), L, 'letter', 'H', 'n88', 'lxxxiii', 'figure key, eye-checked'),
                              (str(b), L, 'letter', 'H', 'n88', 'lxxxiii', 'figure key, eye-checked')]
    for L, a, b in zip('NOPQRSTVXYZ', [53, 50, 49, 47, 45, 42, 39, 33, 30, 28, 25], [10, 12, 11, 13, 26, 27, 29, 31, 32, 38, 37]):
        keys['gualterio'] += [(str(a), L, 'letter', 'H', 'n88', 'lxxxiii', 'figure key, eye-checked'),
                              (str(b), L, 'letter', 'H', 'n88', 'lxxxiii', 'figure key, eye-checked')]
    for L, a, b in zip('abcdefghiklm', range(48, 36, -1), range(49, 61)):
        keys['sicily'] += [(str(a), L, 'letter', 'H', 'n83', 'lxxviii', 'alphabet a double chiffres, eye-checked'),
                           (str(b), L, 'letter', 'H', 'n83', 'lxxviii', 'alphabet a double chiffres, eye-checked')]
    for L, a, b in zip('nopqrstuwxyz', range(36, 24, -1), range(61, 73)):
        keys['sicily'] += [(str(a), L, 'letter', 'H', 'n83', 'lxxviii', 'alphabet a double chiffres, eye-checked'),
                           (str(b), L, 'letter', 'H', 'n83', 'lxxviii', 'alphabet a double chiffres, eye-checked')]
    out = {}
    for name in ('gualterio', 'sicily'):
        lines = ['code\tmeaning\tkind\tgrade\tleaf\tpage\tnote']
        lines += ['\t'.join(t) for t in keys[name]]
        out[f'hmc6_{name}.tsv'] = '\n'.join(lines) + '\n'
    return out

if __name__ == '__main__':
    out = build(); stale = []
    for fn, text in out.items():
        p = os.path.join(HERE, fn)
        if '--check' in sys.argv:
            if not os.path.exists(p) or open(p).read() != text: stale.append(fn)
        else:
            open(p, 'w').write(text)
        print(fn, text.count('\n') - 1, 'rows')
    if stale: print('STALE:', ' '.join(stale)); sys.exit(1)
