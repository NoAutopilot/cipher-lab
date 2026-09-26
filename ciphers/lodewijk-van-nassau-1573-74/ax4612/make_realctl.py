"""AX-4612 extension: a real-letter positive control for block_homophonic. Sibling letters that read under key.tsv
(5811, 13 Apr 1574, W1 two-pass draft, 825 of 1542 reading tokens M; 4610, 3 June 1573, R13 draft settled) cut to
4612's own N=775 numerals 1-120, split into runs at clear words the same way as specs/lodewijk-4612.json, written as
long-format TSVs (line, sign) for tools/family_run.py --cipher. The truth for scoring is key.tsv's letter for each
numeral (the table these letters read under), so recovery = share of numerals the blind solver maps to key.tsv's
letter. Transcription errors are left in: that is the point of a real-letter control."""
import csv
D = 'ciphers/lodewijk-van-nassau-1573-74/'
key = {int(r['code']): r['value'] for r in csv.DictReader(open(D + 'key.tsv'), delimiter='\t') if r['code'].isdigit() and int(r['code']) <= 120}
for nr in ('5811', '4610'):
    rows = list(csv.DictReader(open(D + f'ciphertext_{nr}.tsv'), delimiter='\t'))
    out, run, n = [], 0, 0
    for r in rows:
        s = r['sign']
        if s.startswith('='):
            run += 1; continue
        if s.isdigit() and 1 <= int(s) <= 120:
            out.append((f'r{run:03d}', s)); n += 1
            if n == 775: break
    with open(D + f'ax4612/realctl_{nr}.tsv', 'w') as f:
        f.write('line\tsign\ttruth\n')
        for ln, s in out: f.write(f'{ln}\t{s}\t{key[int(s)]}\n')
    print(nr, len(out), len({l for l, _ in out}), 'runs')
