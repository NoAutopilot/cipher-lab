"""UNA-PISA: stitch a line strip from the committed images/<prefix>_L<NN>_s1/s2 crops (s2 pasted at its manifest box x
offset, as D07-PIST40/R9-PIS2 did) and parse the page's transcription line into tokens (1-based, '/' not counted)."""
from PIL import Image
D = 'ciphers/fr16045-pisany-rome-1585'
PAGES = {  # page: (crop prefix, s2 x offset in the strip, transcription file)
    'f275r': ('f275rL', 1250, 'tx86e/ciphertext_f275r.tsv'),
    'f301v': ('f301v', 1000, 'tx87/ciphertext_f301v_preT32.tsv'),
    'f302v': ('f302v', 944, 'tx87b/ciphertext_f302v_preT32.tsv'),
}
def strip(page, line):
    pre, off, _ = PAGES[page]
    a = Image.open(f'{D}/images/{pre}_{line}_s1.jpg').convert('L'); b = Image.open(f'{D}/images/{pre}_{line}_s2.jpg').convert('L')
    h = max(a.size[1], b.size[1]); W = off + b.size[0]
    s = Image.new('L', (W, h), 255); s.paste(a, (0, 0)); s.paste(b.crop((a.size[0] - off, 0, b.size[0], b.size[1])), (a.size[0], 0))
    return s
def tokens(page, line):
    """Signs of one line from reading_<page>_tokens.tsv as [(pos, sign)], pos as that file counts it ('/' included in
    the count, dropped from the list)."""
    out = []
    for row in open(f'{D}/reading_{page}_tokens.tsv'):
        f = row.rstrip('\n').split('\t')
        if f[0] == line and f[2] != '/':
            out.append((int(f[1]), f[2]))
    return out
