#!/usr/bin/env python3
"""Build a per-holder contribution dataset (TSV) from the repository's own records.

One row per verifier-classified reading (status.json `results` entries with a `document_id`) and one row per
target folder held by the institution, so a library can ingest what this project has read, audited or found
already read in its holdings.  Built for the BnF (BNF-FOCUS lane, 7 Oct 2026, BNF-VALUE.md); the holder is a
set of shelfmark patterns, so another holder is one more entry in HOLDERS.

Reads only: ciphers/*/NOTES.md (status word on the first lines, shelfmark, Gallica arks), ciphers/*/AUDIT.md
(presence), status.json results (N-class, depth, key source, text known).  Writes nothing but --out.

Scope (Usage 8a):
  catches  a folder whose NOTES.md heading or first 3000 characters name a fonds of the holder ("BnF fr.3251",
           "Clairambault 1067", "Arsenal Ms-6314", "Espagnol 142") -- including folders whose heading never says
           "BnF" (espagnol142-mercy-1648, clair571-estrades-1645);
  does NOT a folder that only mentions the holder in passing (a BnF copy of a NARA letter, "BnF holdings were not
  catch    checked"): the shelfmark must be a holder fonds + number, not the word "BnF" alone.

Usage:
  python3 tools/holder_dataset.py --holder bnf --out BNF-VALUE.tsv
  python3 tools/holder_dataset.py --holder bnf --check BNF-VALUE.tsv    # exit 1 if the committed TSV is stale
"""
import argparse, glob, json, os, re, sys

HOLDERS = {
    'bnf': re.compile(
        r"(?<![A-Za-z])(Fran[cç]ais|fr\.|Clairambault|Dupuy|Baluze|M[ée]langes de Colbert|"
        r"Cinq[ -]cents de Colbert|500 \(Cinq cents\) de Colbert|Espagnol|Portugais|italien|NAF|Lorraine|"
        r"Arsenal,? Ms-?|Arsenal Ms\.?|Ms-)\s?(\d{1,5}[A-Za-z]?)"),
}
STATUS = re.compile(r"\b(open|partial|solved|closed-negative|found-solved|blocked|offline-only|key-only)\b")
ARK = re.compile(r"(btv1b[0-9a-z]{8,12}|bpt6k[0-9a-z]{6,12})")
LINK = re.compile(r"ciphers/([^/ )#]+)")
COLS = ['row_kind', 'folder', 'shelfmark', 'item', 'status', 'n_class', 'depth', 'depth_pct', 'key_source',
        'text_known', 'gallica_ark', 'audit', 'title', 'repo_path']


# BnF: the folder name usually carries the shelfmark; it wins over the first fonds+number the prose mentions
# (a key sheet, a sibling volume, a printed edition's own numbering).
SLUG = {'bnf': [(r'^fr(\d+)', 'fr.%s'), (r'^clair(?:ambault)?(\d+)', 'Clairambault %s'), (r'^dupuy(\d+)', 'Dupuy %s'),
                (r'^baluze(\d+)', 'Baluze %s'), (r'^colbert(\d+)', 'Colbert %s'), (r'^espagnol(\d+)', 'Espagnol %s'),
                (r'^es(?:p)?(\d+)', 'Espagnol %s'), (r'^portugais(\d+)', 'Portugais %s'), (r'^arsenal(\d+)', 'Arsenal Ms-%s'),
                (r'^naf(\d+)', 'NAF %s'), (r'^lorraine(\d+)', 'Lorraine %s'), (r'-fr(\d+)', 'fr.%s'),
                (r'-baluze(\d+)', 'Baluze %s'), (r'-colbert(\d+)', 'Mélanges de Colbert %s')]}
# Hand-checked against each NOTES.md heading (BNF-FOCUS, 7 Oct 2026).
OVERRIDE = {'bnf': {'colbert369-maisse': 'Cinq cents de Colbert 369', 'colbert401-henri3-segur-1586': 'Cinq cents de Colbert 401',
                    'colbert155-beziers-1670': 'Mélanges de Colbert 155', 'colbert26-lathuillerie-1644': 'Mélanges de Colbert 26',
                    'colbert-croissy-london-1668-74': 'Mélanges de Colbert 149-167, 176bis',
                    'baluze167-davaux-1637': 'Baluze 167-171', 'matignon-mayenne-1586': 'fr.15572 (+ fr.15571)',
                    'fr16147-sancy-constantinople-1611-18': 'fr.16145-16149', 'sforza-maino-1446': 'italien 1583-1584',
                    'espagnol142-mercy-1648': 'Espagnol 142-144', 'davaux-1633': 'Baluze 188',
                    'decode-4450-bnf-fr20506-1525': 'fr.20506 (copy of fr.2988)', 'bl-farnese-cipher': 'Baluze 156',
                    'fr3625-lauriere-1593': 'fr.3625 (key: fr.3995)', 'fr3984-sega-1593': 'fr.3984-3985'}}
EXCLUDE = {'bnf': {'addms33531-oysell-guise-1559', 'moray-wood-1568'}}


def shelfmark(text, pat):
    head = '\n'.join(text.split('\n')[:12])
    for zone in (head, text[:3000]):
        m = pat.search(zone)
        if m:
            fonds = m.group(1).replace('Français', 'fr.').replace('Francais', 'fr.')
            if fonds.startswith('Ms-') or fonds.startswith('Arsenal'):
                fonds = 'Arsenal Ms-'
            sep = '' if fonds.endswith(('.', '-')) else ' '
            return fonds + sep + m.group(2)
    return ''


def build(root, holder):
    pat = HOLDERS[holder]
    results = json.load(open(os.path.join(root, 'status.json')))['results']
    rows = []
    for nf in sorted(glob.glob(os.path.join(root, 'ciphers', '*', 'NOTES.md'))):
        folder = os.path.basename(os.path.dirname(nf))
        text = open(nf, errors='ignore').read()
        if folder in EXCLUDE.get(holder, ()):
            continue
        sm = shelfmark(text, pat)
        if not sm and folder not in OVERRIDE.get(holder, {}):
            continue
        for rx, fmt in SLUG.get(holder, []):
            m = re.search(rx, folder)
            if m:
                sm = fmt % m.group(1)
                break
        sm = OVERRIDE.get(holder, {}).get(folder, sm)
        st = STATUS.search(text[:800])
        arks = ARK.findall(text)
        audit = 'yes' if os.path.exists(os.path.join(os.path.dirname(nf), 'AUDIT.md')) else ''
        title = next((l.lstrip('# ').strip() for l in text.split('\n') if l.startswith('# ')), '')
        base = dict(folder=folder, shelfmark=sm, status=st.group(1) if st else '', audit=audit,
                    gallica_ark=arks[0] if arks else '', repo_path='ciphers/%s/' % folder)
        for r in results:
            m = LINK.search(r.get('link', ''))
            if not m or m.group(1) != folder:
                continue
            if not r.get('document_id') or r.get('superseded_by'):
                continue
            ark = ARK.search(r['document_id'])
            rows.append(dict(base, row_kind='reading', item=r['document_id'],
                             n_class=r.get('plaintext_novelty') or r.get('novelty') or '',
                             depth=r.get('depth') or '', depth_pct=r.get('depth_pct') if r.get('depth_pct') is not None else '',
                             key_source=r.get('key') or '', text_known=r.get('text') or '',
                             gallica_ark=ark.group(1) if ark else base['gallica_ark'], title=r['title']))
        rows.append(dict(base, row_kind='folder', item='', n_class='', depth='', depth_pct='', key_source='',
                         text_known='', title=title))
    return rows


def render(rows):
    out = ['\t'.join(COLS)]
    for r in rows:
        out.append('\t'.join(str(r.get(c, '')).replace('\t', ' ').replace('\n', ' ') for c in COLS))
    return '\n'.join(out) + '\n'


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--holder', default='bnf', choices=sorted(HOLDERS))
    ap.add_argument('--root', default='.')
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--out')
    g.add_argument('--check')
    a = ap.parse_args()
    txt = render(build(a.root, a.holder))
    if a.out:
        open(a.out, 'w').write(txt)
        n = txt.count('\n') - 1
        print('%s: %d rows (%d readings, %d folders)' % (a.out, n, txt.count('\nreading\t'), txt.count('\nfolder\t')))
        return 0
    cur = open(a.check).read() if os.path.exists(a.check) else ''
    if cur != txt:
        print('%s is stale: re-run with --out' % a.check)
        return 1
    print('%s current' % a.check)
    return 0


if __name__ == '__main__':
    sys.exit(main())
