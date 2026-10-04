#!/usr/bin/env python3
"""KEY1629-XMATCH step 1 (4 Oct 2026): list every ciphertext file on disk under ciphers/ and flag it
(a) Swedish/Riksarkivet/Oxenstierna/Transylvania/Gustav Adolf/Bethlen-related (folder NOTES.md keyword),
(b) dated 1620-1640 (a year in the folder name, or the first 15 NOTES.md lines' first year),
(c) numeric with most 2-digit values in 12-91 plus some 3-4 digit codes.
Writes inventory.tsv (every file) beside this script. Deterministic, disk only."""
import os, re, glob, collections
H = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(os.path.join(H, '../../../..'))
KW = re.compile(r'oxenstierna|riksarkivet|transylvan|siebenb|bethlen|gustav ?adolf|gustavus adolphus|strasburg|r[aá]k[oó]czi|swed|svensk|sverige', re.I)
pat = ['ciphertext*.txt', 'ciphertext*.tsv', '*/ciphertext*.txt', '*/ciphertext*.tsv', '*_ciphertext.tsv', '*/*_ciphertext.tsv']
def tokens(path):
    txt = open(path, encoding='utf-8', errors='replace').read()
    if path.endswith('.tsv'):
        lines = txt.splitlines(); hdr = lines[0].split('\t') if lines else []
        col = next((i for i, h in enumerate(hdr) if h in ('sign', 'token', 'cipher', 'value', 'ciphertext', 'code', 'tokens', 'text', 'line_text')), None)
        if col is not None:
            out = []
            for l in lines[1:]:
                f = l.split('\t')
                if len(f) > col: out += f[col].split()
            return out
    return re.findall(r'\S+', re.sub(r'#.*', '', txt))
rows = []
for d in sorted(glob.glob(os.path.join(REPO, 'ciphers/*/'))):
    name = os.path.basename(d.rstrip('/'))
    notes = os.path.join(d, 'NOTES.md'); nt = open(notes, encoding='utf-8', errors='replace').read() if os.path.exists(notes) else ''
    a = bool(KW.search(nt[:20000])) or bool(KW.search(name))
    yrs = [int(y) for y in re.findall(r'(?<!\d)(1[4-9]\d\d)(?!\d)', name)]
    if not yrs: yrs = [int(y) for y in re.findall(r'(?<!\d)(1[4-9]\d\d)(?!\d)', '\n'.join(nt.splitlines()[:15]))][:1]
    b = any(1620 <= y <= 1640 for y in yrs)
    files = sorted({f for p in pat for f in glob.glob(os.path.join(d, p))})
    for f in files:
        t = tokens(f); n = len(t)
        num = [x.strip('?.,;:()[]') for x in t]; num = [x for x in num if x.isdigit()]
        two = [x for x in num if len(x) <= 2]; big = [x for x in num if 3 <= len(x) <= 4]
        in_r = sum(1 for x in two if 12 <= int(x) <= 91)
        c = n > 0 and len(num) / n >= 0.6 and len(two) >= 20 and in_r / max(1, len(two)) >= 0.8 and len(big) >= 3
        rows.append((name, os.path.relpath(f, REPO), n, len(num), len(two), in_r, len(big), int(a), ','.join(map(str, yrs)), int(b), int(c)))
with open(os.path.join(H, 'inventory.tsv'), 'w') as o:
    o.write('folder\tfile\ttokens\tnumeric\ttwo_digit\tin_12_91\tcodes_3_4\ta_kw\tyears\tb_1620_40\tc_numeric\n')
    for r in rows: o.write('\t'.join(map(str, r)) + '\n')
if __name__ == '__main__':
  sel = [r for r in rows if r[7] or r[9] or r[10]]
  print(len(rows), 'files;', len(sel), 'flagged')
  for r in sel: print('\t'.join(map(str, r)))
