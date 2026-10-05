# N9-COS2, 5 Oct 2026: PREREG-N9-COS2 step 2. Turns a blind reader's slip output (CIPHER / CLEAR sections) into span pairs for
# the unchanged align/run_align.py: clear words standing in clear in both slips are anchors (monotone LCS on normalised words,
# exact match, or edit distance 1 for words of >= 4 letters); the cipher signs between two consecutive anchors and the clear-slip
# letters between the same anchors make one pair (crop label = <slip>_s<n>). No forced split inside a span.
# Usage: python3 .../n9cos2_slip_pairs.py OUT.tsv SLIP:READER.txt [SLIP:READER.txt ...]
import sys, re, csv
def norm(w): return re.sub(r'[^a-z]', '', w.lower())
def ed1(a, b):
    if a == b: return True
    if min(len(a), len(b)) < 4 or abs(len(a) - len(b)) > 1: return False
    if len(a) == len(b): return sum(x != y for x, y in zip(a, b)) == 1
    if len(a) > len(b): a, b = b, a
    return any(b[:i] + b[i + 1:] == a for i in range(len(b)))
def parse(path):
    sec, cipher, clear = None, [], []
    for line in open(path):
        line = line.rstrip('\n')
        if line.strip() in ('CIPHER', 'CLEAR'): sec = line.strip(); continue
        if '\t' not in line or sec is None: continue
        crop, txt = line.split('\t', 1)
        (cipher if sec == 'CIPHER' else clear).append((crop.strip(), txt))
    key = lambda t: t[0]
    return sorted(cipher, key=key), sorted(clear, key=key)   # page order whatever the reading order
def items(cipher):
    out = []
    for _, txt in cipher:
        for m in re.finditer(r'<([^>]*)>|([^<|]+)', txt):
            if m.group(1) is not None:
                w = norm(m.group(1))
                if w: out.append(('w', w))
            else:
                for t in m.group(2).split():
                    t = t.rstrip('*')
                    if t and t not in (':', '.', '-', ',', ';'): out.append(('s', t))
    return out
def main(out, specs):
    rows = []
    for spec in specs:
        slip, path = spec.split(':', 1)
        cipher, clear = parse(path)
        it = items(cipher)
        cw = [w for _, txt in clear for w in (norm(x) for x in txt.split()) if w]
        wi = [i for i, (k, _) in enumerate(it) if k == 'w']
        n, m = len(wi), len(cw)
        L = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                L[i][j] = L[i + 1][j + 1] + 1 if ed1(it[wi[i]][1], cw[j]) else max(L[i + 1][j], L[i][j + 1])
        anchors, i, j = [], 0, 0
        while i < n and j < m:
            if ed1(it[wi[i]][1], cw[j]) and L[i][j] == L[i + 1][j + 1] + 1: anchors.append((wi[i], j)); i += 1; j += 1
            elif L[i + 1][j] >= L[i][j + 1]: i += 1
            else: j += 1
        bounds = [(-1, -1)] + anchors + [(len(it), m)]
        for s, ((a0, c0), (a1, c1)) in enumerate(zip(bounds, bounds[1:])):
            signs = [t for k, t in it[a0 + 1:a1] if k == 's']
            gloss = ''.join(cw[c0 + 1:c1])
            if signs and gloss: rows.append((f'{slip}_s{s:02d}', gloss, ' '.join(signs)))
        print(f'{slip} {path}: {len(it)} items, {len(wi)} clear words in cipher slip, {m} clear-slip words, {len(anchors)} anchors, '
              f'{sum(1 for r in rows if r[0].startswith(slip))} span pairs', file=sys.stderr)
    w = csv.writer(open(out, 'w'), delimiter='\t', lineterminator='\n')
    w.writerow(['crop', 'gloss_above', 'signs', 'clear_context']); [w.writerow(list(r) + ['']) for r in rows]
if __name__ == '__main__': main(sys.argv[1], sys.argv[2:])
