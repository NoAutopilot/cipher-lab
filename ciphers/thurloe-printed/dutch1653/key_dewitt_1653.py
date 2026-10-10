#!/usr/bin/env python3
"""Build key_dewitt_1653.tsv from the printed table, Brieven van Johan de Witt dl 1 (ed. Japikse, after Fruin) p.72.

Ranges read by eye from img/VAN_DEWITT_01_072.jpg (sha1 39c9a23b...) and checked against the edition's own OCR
(edition/VAN_DEWITT_01_072.html): 24 ranges, 1-66 contiguous, both reads agree.
  python3 key_dewitt_1653.py          write key_dewitt_1653.tsv
  python3 key_dewitt_1653.py --check  exit 1 if the committed TSV is stale, or the ranges are not 1-66 contiguous,
                                      or a range is missing from the OCR text
"""
import sys, os, re
H = os.path.dirname(os.path.abspath(__file__))
RANGES = [(1,8,'a'),(9,10,'b'),(11,12,'c'),(13,14,'d'),(15,19,'e'),(20,21,'f'),(22,23,'g'),(24,25,'h'),
          (26,30,'i'),(31,32,'k'),(33,34,'l'),(35,36,'m'),(37,38,'n'),(39,43,'o'),(44,45,'p'),(46,47,'q'),
          (48,49,'r'),(50,51,'s'),(52,53,'t'),(54,58,'u'),(59,60,'w'),(61,62,'x'),(63,64,'y'),(65,66,'z')]
def rows():
    out = ['code\tletter\tsource\tgrade']
    for a, b, l in RANGES:
        for c in range(a, b + 1):
            out.append(f'{c}\t{l}\tBrieven van Johan de Witt I (Japikse) p.72\tH')
    return '\n'.join(out) + '\n'
def main():
    t = rows(); p = os.path.join(H, 'key_dewitt_1653.tsv')
    codes = [c for a, b, _ in RANGES for c in range(a, b + 1)]
    ok = codes == list(range(1, 67))
    ocr = open(os.path.join(H, 'edition', 'VAN_DEWITT_01_072.html'), encoding='utf-8', errors='ignore').read()
    ocr = re.sub(r'<[^>]+>', ' ', ocr)
    for a, b, l in RANGES:  # each range's low bound appears in the OCR beside its letter (u written 'u, V', o as '0', l as 'I', s as '8')
        if not re.search(r"\b%d[\"']?\s*[-,]" % a, ocr): print('range start not in OCR:', a); ok = False
    if '--check' in sys.argv:
        cur = open(p).read() if os.path.exists(p) else ''
        if cur != t: print('STALE', p); ok = False
        print('OK' if ok else 'FAIL'); sys.exit(0 if ok else 1)
    open(p, 'w').write(t); print('wrote', p, len(codes), 'codes'); sys.exit(0 if ok else 1)
if __name__ == '__main__':
    main()
