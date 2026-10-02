"""NEXT-BRO (2 Oct 2026): regenerate reading_body_letter134.txt (+ _spanA / _spanB) from reading_body.txt, the
file tools/decode_key.py writes from body_ciphertext.tsv + key.tsv (decode.json job 2), so the letter-134 judge
input is reproducible from the key (rule 7) instead of hand-cut. Layout as YX-BRO79 built it by hand: Span A =
m0275-r1 + m0276-r1 (one run, page break only), a space, Span B = m0276-r2; the unkeyed marker '·' becomes '_'
(stripped by the judge's fold() either way). `--check` exits 1 if the committed files are stale."""
import sys
ROOT = '/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712'
runs = {}
for ln in open(f'{ROOT}/reading_body.txt'):
    if ln.startswith('#') or '|' not in ln: continue
    head, text = ln.split('|', 1)
    runs[head.split()[1]] = text.strip().replace('·', '_')
spanA = runs['m0275-r1'] + runs['m0276-r1']
spanB = runs['m0276-r2']
want = {f'{ROOT}/reading_body_letter134.txt': spanA + ' ' + spanB + '\n',
        f'{ROOT}/reading_body_letter134_spanA.txt': spanA + '\n',
        f'{ROOT}/reading_body_letter134_spanB.txt': spanB + '\n'}
stale = [p for p, t in want.items() if not (open(p).read() == t if __import__('os').path.exists(p) else False)]
if '--check' in sys.argv:
    print('stale: ' + ', '.join(stale) if stale else 'letter 134 reading files up to date'); sys.exit(1 if stale else 0)
for p, t in want.items():
    open(p, 'w').write(t)
print(f"wrote letter 134: {spanA + ' ' + spanB!r} (Span A {sum(c.isalpha() for c in spanA)} letters, Span B {sum(c.isalpha() for c in spanB)})")
