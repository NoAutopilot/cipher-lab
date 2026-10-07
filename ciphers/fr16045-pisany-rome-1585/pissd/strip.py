"""Stitch an f.302v line strip from the committed images/f302v_L<NN>_s1/s2 crops,
the same way D07-PIST40 did (s2 pasted at x=1600 from its own x=656)."""
import sys
from PIL import Image
H = 'ciphers/fr16045-pisany-rome-1585/images'
def strip(line):
    a = Image.open(f'{H}/f302v_{line}_s1.jpg').convert('L'); b = Image.open(f'{H}/f302v_{line}_s2.jpg').convert('L')
    h = max(a.size[1], b.size[1]); W = 1600 + b.size[0] - 656
    s = Image.new('L', (W, h), 255); s.paste(a, (0, 0)); s.paste(b.crop((656, 0, b.size[0], b.size[1])), (1600, 0))
    return s
if __name__ == '__main__':
    print(strip(sys.argv[1]).size)
