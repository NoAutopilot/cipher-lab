"""TXE2-SHEETVIV (copy of ../viv102base/assemble.py, output path and name changed only: pass<P>_sv in outputs/vivonne1573-f102r-dev2/): join a pass's 5 chunk reads (reads/pass<P>_c1..c5.tsv, raw, kept) into
benchmark-tx/outputs/vivonne1573-f102r-dev2/pass<P>_sv.tsv (line pos sign alt conf), cleaned as PREREG-N5VIVK step 3:
drop DUP rows, [PLAIN:..] and [...] rows; strip a trailing '?' (conf capped at M); keep {..} tokens; renumber pos.
Usage: python3 assemble.py A"""
import csv, sys, re
P = sys.argv[1]
OUT = f'/home/user/cipher-lab/benchmark-tx/outputs/vivonne1573-f102r-dev2/pass{P}_sv.tsv'
rows, dup, dropped = [], [], 0
for k in range(1, 6):
    for r in csv.DictReader(open(f'reads/pass{P}_c{k}.tsv'), delimiter='\t'):
        ln = r['line'].strip(); s = (r['sign'] or '').strip(); c = (r.get('conf') or 'M').strip().upper()[:1] or 'M'
        if not re.fullmatch(r'f102r_L\d\d', ln):
            sys.exit(f'bad line id {ln!r} in chunk {k}')
        if s == 'DUP':
            dup.append(ln); continue
        if not s or s.startswith('[PLAIN') or s.startswith('[...'):
            dropped += 1; continue
        if s.endswith('?') and len(s) > 1:
            s = s[:-1]; c = 'L' if c == 'L' else 'M'
        rows.append([ln, s, (r.get('alt') or '').strip(), c])
pos = {}
with open(OUT, 'w') as f:
    f.write('line\tpos\tsign\talt\tconf\n')
    for ln, s, a, c in rows:
        pos[ln] = pos.get(ln, 0) + 1
        f.write(f'{ln}\t{pos[ln]}\t{s}\t{a}\t{c}\n')
print(f'pass{P}: {len(rows)} signs on {len(pos)} lines; DUP lines {dup}; dropped [...]/[PLAIN] rows {dropped}')
print('lines without signs:', [f'f102r_L{i:02d}' for i in range(1, 38) if f'f102r_L{i:02d}' not in pos])
