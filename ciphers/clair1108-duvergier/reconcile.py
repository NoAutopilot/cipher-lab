#!/usr/bin/env python3
"""Build ciphertext.tsv and dechiffre.tsv for clair1108-duvergier from rows.tsv (the reconciled physical rows,
settled on the native page images) and score passA.tsv / passB.tsv against it.

rows.tsv: leaf, row, layer (main|gloss), text, conf, note. In `text` a numeral is a cipher group, anything else a
clear word; a trailing '?' marks conf M for that token; {..} marks a struck word or group; 192|142 gives an
alternative reading (first preferred).

  python3 reconcile.py           write ciphertext.tsv, dechiffre.tsv, pass_agreement.tsv, signs.tsv (decode_key input)
  python3 reconcile.py --check   regenerate in memory, exit 1 if any committed file differs (rule 7)
"""
import csv, difflib, io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = ['ciphertext.tsv', 'dechiffre.tsv', 'pass_agreement.tsv', 'signs.tsv']


def load_rows():
    rows = []
    for line in open(os.path.join(HERE, 'rows.tsv'), encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        f = line.rstrip('\n').split('\t')
        f += [''] * (6 - len(f))
        rows.append(dict(leaf=f[0], row=f[1], layer=f[2], text=f[3], conf=f[4], note=f[5]))
    return rows


def tokens(text):
    """Split a row into tokens; {a b} is one struck unit."""
    out = []
    for m in re.finditer(r'\{[^}]*\}|\S+', text):
        out.append(m.group(0))
    return out


def classify(tok, rowconf):
    """Return (token, conf, kind, alt)."""
    if tok.startswith('{'):
        return tok.strip('{}'), 'M', 'struck', ''
    core = tok.rstrip('.,;—-')
    conf = rowconf or 'H'
    if core.startswith('='):
        return core[1:], conf, 'clear', ''
    if core.endswith('?'):
        core, conf = core[:-1], 'M'
    alt = ''
    if '|' in core:
        core, alt = core.split('|', 1)
    if core == '':
        return None
    if re.fullmatch(r'\d+', core):
        return core, conf, 'cipher', alt
    return core, conf, 'clear', alt


def build():
    rows = load_rows()
    ct = io.StringIO()
    w = csv.writer(ct, delimiter='\t', lineterminator='\n')
    w.writerow(['leaf', 'line', 'pos', 'token', 'conf', 'layer', 'alt', 'note'])
    sg = io.StringIO()
    ws = csv.writer(sg, delimiter='\t', lineterminator='\n')
    ws.writerow(['line', 'pos', 'token', 'conf'])
    dc = io.StringIO()
    wd = csv.writer(dc, delimiter='\t', lineterminator='\n')
    wd.writerow(['leaf', 'line', 'words', 'conf', 'note'])
    for r in rows:
        if r['layer'] == 'gloss':
            wd.writerow([r['leaf'], r['row'], r['text'], r['conf'] or 'H', r['note']])
            continue
        pos = 0
        for t in tokens(r['text']):
            c = classify(t, r['conf'] if r['conf'] == 'M' else '')
            if c is None:
                continue
            tok, conf, kind, alt = c
            if kind == 'struck' and re.fullmatch(r'\d+', tok):
                kind = 'cipher-struck'
            pos += 1
            note = r['note'] if pos == 1 else ''
            w.writerow([r['leaf'], r['row'], pos, tok, conf, kind, alt, note])
            ws.writerow([r['leaf'] + '_' + r['row'], pos, tok if kind == 'cipher' else 'w:' + tok.replace(' ', '_'), conf])
    return ct.getvalue(), dc.getvalue(), rows, sg.getvalue()


def cipher_stream(ct_text):
    out = {}
    for r in csv.DictReader(io.StringIO(ct_text), delimiter='\t'):
        if r['layer'] == 'cipher':
            out.setdefault(r['leaf'][:4], []).append(r['token'])
    return out


def pass_stream(path):
    out = {}
    for r in csv.DictReader(open(path, encoding='utf-8'), delimiter='\t'):
        t = r['token'].strip().rstrip('.,')
        if re.fullmatch(r'\d+', t):
            out.setdefault(r['leaf'][:4], []).append(t)
    return out


def agreement(ct_text):
    ref = cipher_stream(ct_text)
    s = io.StringIO()
    w = csv.writer(s, delimiter='\t', lineterminator='\n')
    w.writerow(['pass', 'folio', 'recon_groups', 'pass_groups', 'matched', 'pct_of_recon'])
    for p in ('passA', 'passB'):
        ps = pass_stream(os.path.join(HERE, p + '.tsv'))
        for fol in sorted(ref):
            a, b = ref[fol], ps.get(fol, [])
            sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
            m = sum(x.size for x in sm.get_matching_blocks())
            w.writerow([p, fol, len(a), len(b), m, f'{100 * m / len(a):.1f}'])
    return s.getvalue()


def main():
    ct, dc, _, sg = build()
    ag = agreement(ct)
    new = dict(zip(OUT, [ct, dc, ag, sg]))
    if '--check' in sys.argv:
        bad = [f for f in OUT if not os.path.exists(os.path.join(HERE, f))
               or open(os.path.join(HERE, f), encoding='utf-8').read() != new[f]]
        if bad:
            print('STALE:', ', '.join(bad))
            sys.exit(1)
        print('ok: ' + ', '.join(OUT) + ' match rows.tsv')
        return
    for f, t in new.items():
        open(os.path.join(HERE, f), 'w', encoding='utf-8').write(t)
    print(ag)


if __name__ == '__main__':
    main()
