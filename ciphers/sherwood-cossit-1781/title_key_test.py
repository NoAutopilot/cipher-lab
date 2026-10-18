#!/usr/bin/env python3
"""Apply the Haldimand-Clinton 1778 title-page book key to the Cossit/Summer cypher (BL Add MS 21838 pp.345-347).

SHERWOOD-PAGES, 18 Oct 2026. Key: title page of *A List of the General and Field Officers* (1778) as reconciled in
ciphers/pro3055-clinton-1779/passes/title1778_reading.txt (credit Tomokiyo, Cryptiana haldimand.htm; Knepper via
Friedman 1965; Leighton and Matyas 1985). Convention (Haldimand's own explanation, Add MS 21807 f.323): the year line
is dropped, lines numbered 1-29, letters counted left to right across the line, ignoring spaces and punctuation;
pro3055's -1/-2 count-error tolerance is applied as an alternative only (reported, never chosen).

Matched control (rule 3): the same tokens decoded with the key's line order shuffled, 20 seeds. Metric: share of
figure pairs the key can read at all (first figure <= 29 and second figure <= letters in that line) and share of the
decoded letter stream covered by English words of 3+ letters (greedy longest match against a word list built from
tools/data/en). Usage: python3 title_key_test.py [--check]   (--check exits 1 if title_key_test.out is stale).
"""
import random, re, sys, os, gzip
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
KEY = os.path.join(ROOT, 'ciphers/pro3055-clinton-1779/passes/title1778_reading.txt')

def key_lines():
    ls = [l.rstrip('\n') for l in open(KEY) if l.strip() and not l.startswith('#')]
    # drop the imprint-year line(s) (Haldimand: "excepte l'annee, je le retranche")
    ls = [l for l in ls if not re.search(r'MDCC|17\d\d', l)]
    return [re.sub(r'[^a-z]', '', l.lower()) for l in ls][:29]

def tokens():
    out = []
    for l in open(os.path.join(HERE, 'ciphertext.tsv')):
        if l.startswith('#') or l.startswith('line\t'):
            continue
        f = l.rstrip('\n').split('\t')
        if len(f) < 2:
            continue
        for t in f[1].split():
            t = t.split("@")[-1]; m = re.fullmatch(r"(\d+)-(\d+)", t.strip("?"))
            if m:
                out.append((int(m.group(1)), int(m.group(2))))
    return out

def words():
    ws = set()
    for fn in os.listdir(os.path.join(ROOT, 'tools/data/en')):
        if fn.endswith('.txt'):
            ws.update(w for w in re.findall(r'[a-z]+', open(os.path.join(ROOT, 'tools/data/en', fn), errors='ignore').read().lower()) if len(w) >= 3)
    return ws

def decode(pairs, lines):
    s, ok = [], 0
    for a, b in pairs:
        if 1 <= a <= len(lines) and 1 <= b <= len(lines[a - 1]):
            s.append(lines[a - 1][b - 1]); ok += 1
        else:
            s.append('?')
    return ''.join(s), ok

def covered(s, ws):
    i, cov = 0, 0
    while i < len(s):
        for L in range(min(12, len(s) - i), 2, -1):
            if s[i:i + L] in ws:
                cov += L; i += L; break
        else:
            i += 1
    return cov / max(1, len(s))

def main():
    lines, pairs, ws = key_lines(), tokens(), words()
    rows = []
    s, ok = decode(pairs, lines)
    rows.append(('target', len(pairs), ok, round(ok / len(pairs), 3), round(covered(s, ws), 3), s))
    for seed in range(20):
        sh = lines[:]; random.Random(seed).shuffle(sh)
        s2, ok2 = decode(pairs, sh)
        rows.append((f'shuffle{seed}', len(pairs), ok2, round(ok2 / len(pairs), 3), round(covered(s2, ws), 3), s2))
    sh = [r[4] for r in rows[1:]]
    out = ['run\tpairs\tin_range\tin_range_share\tenglish_cover\tdecoded']
    out += ['\t'.join(map(str, r)) for r in rows]
    out.append(f'# pairs with first figure > 29 (outside the title page): {sum(1 for a, b in pairs if a > 29)}/{len(pairs)}; '
               f'shuffle english_cover mean {sum(sh) / len(sh):.3f} max {max(sh):.3f}')
    text = '\n'.join(out) + '\n'
    path = os.path.join(HERE, 'title_key_test.out')
    if '--check' in sys.argv:
        if not os.path.exists(path) or open(path).read() != text:
            print('STALE: title_key_test.out differs from a fresh run'); sys.exit(1)
        print('ok: title_key_test.out is current'); return
    open(path, 'w').write(text); print(text)

if __name__ == '__main__':
    main()
