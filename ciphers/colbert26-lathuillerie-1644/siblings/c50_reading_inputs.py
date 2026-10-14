"""COL26-C50 (account 1, LANE DEFAULT-A1-1840-14, 14 Oct 2026): build ciphertext_c50.tsv and exceptions_c50.tsv for the canvas 50
reading (decode.json job 4, tools/decode_key.py), from A2-COL15's reconciled transcription siblings/c5051_reconciled.tsv (canvas 50
rows only, '50a..'/'50b..'). Deterministic; --check exits 1 if either committed file differs from a regeneration (rule 7).

Grade licence (what A2-COL15's test supports, nothing more): A2-COL15 (pre-registered, siblings/c5051_test.py at 2a6826b4) tested the
21 key_f23 C codes OF THAT COMMIT on canvas 50 by the ordered greedy walk against each row's own gloss: 65/97 vs f23-window max 59, PASS.
A token keeps key_f23's grade C on canvas 50 only if (a) its code is one of those 21 codes and (b) the walk, run exactly as
c5051_test.py runs it with that commit's C set, scores it consistent with its own row's gloss. Every other token whose key_f23 grade is C
is lowered to M by an exception row with the reason: 'walk-miss' (code tested, value not found in its row's gloss at its place),
'no-gloss' (row without a gloss: nothing on the leaf checks it), or 'not-in-A2-COL15' (codes 16 se, 23 n, 30 s, made C on f.23 after
3 Oct 2026 by later steps; A2-COL15 did not test them on canvas 50). key_f23 M codes stay M; codes outside key_f23 are U. Unsettled
groups (A2-COL15 left 6 unsettled: 50a10 first, 50a14 first (crop cut), 50b03 last two, 50b04 last, 50b16 last) are written as sign '?'
with conf '?' and are not read.
Usage: python3 siblings/c50_reading_inputs.py [--check]"""
import csv, re, os, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
A2COL15_C = set('10 12 18 22 24 25 28 33 36 40 43 48 49 51 53 65 69 78 89 97 98'.split())  # key_f23.tsv C codes at 2a6826b4
def norm(s): return re.sub(r'[^a-z]', '', re.sub(r'\[[^\]]*\]', '', s.lower())).replace('v', 'u').replace('j', 'i')
key = {r['code']: (r['value'], r['grade']) for r in csv.DictReader(open(f'{T}/key_f23.tsv'), delimiter='\t')}
rows = [r for r in csv.DictReader(open(f'{H}/c5051_reconciled.tsv'), delimiter='\t') if r['line'].startswith('50')]
ct = ['line\tpos\tsign\tconf']; ex = ['line\tpos\tvalue\tgrade\treason']
for r in rows:
    L, toks, g = r['line'], r['tokens'].split(), norm(r['gloss'])
    hitpos = set(); p = 0
    if g:
        for i, t in enumerate(toks, 1):  # c5051_test.py's walk: digits only, A2-COL15's C set, find at/after previous match end
            if not t.isdigit() or t not in A2COL15_C: continue
            j = g.find(norm(key[t][0]), p)
            if j >= 0: hitpos.add(i); p = j + len(norm(key[t][0]))
    for i, t in enumerate(toks, 1):
        if not t.isdigit(): ct.append(f'{L}\t{i}\t?\t?'); continue
        ct.append(f'{L}\t{i}\t{t}\t')
        if t in key and key[t][1] == 'C' and i not in hitpos:
            why = ('not-in-A2-COL15: C on f.23 after 3 Oct 2026, not tested on canvas 50' if t not in A2COL15_C else
                   'no-gloss: row has no gloss, nothing on the leaf checks this token' if not g else
                   'walk-miss: A2-COL15 ordered walk did not find the value in this row\'s gloss at this place')
            ex.append(f'{L}\t{i}\t{key[t][0]}\tM\tCOL26-C50 14 Oct 2026: {why}')
# VER-COL50 (verifier, 14 Oct 2026, PREREG-VER-COL50.md): per-token word-grain check lowered these C tokens to M
VF = f'{H}/verify_c50_lower.tsv'
if os.path.exists(VF):
    tokmap = {r['line']: r['tokens'].split() for r in rows}
    for r in csv.DictReader(open(VF), delimiter='\t'):
        code = tokmap[r['line']][int(r['pos']) - 1]
        ex.append(f"{r['line']}\t{r['pos']}\t{key[code][0]}\tM\tVER-COL50 14 Oct 2026: {r['reason']}: value not at its slot in its "
                  "paired gloss word under either blind word pairing (DA1-COL, DA1-COL2), PREREG-VER-COL50.md")
out = {f'{T}/ciphertext_c50.tsv': '\n'.join(ct) + '\n', f'{T}/exceptions_c50.tsv': '\n'.join(ex) + '\n'}
if '--check' in sys.argv:
    bad = [p for p, s in out.items() if not os.path.exists(p) or open(p).read() != s]
    print('stale: ' + ', '.join(bad) if bad else 'c50 inputs up to date'); sys.exit(1 if bad else 0)
for p, s in out.items(): open(p, 'w').write(s)
print(f'{len(ct)-1} cipher positions, {len(ex)-1} C->M exceptions; hits kept C: {sum(1 for r in rows)} rows')
