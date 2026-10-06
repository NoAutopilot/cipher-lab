"""Judge input from reading_tokens.tsv: first value of each a|b, U tokens dropped, one line per folio line."""
import csv, sys
out, cur = [], None
for r in csv.DictReader(open(sys.argv[1]), delimiter='\t'):
    k = (r['folio'], r['line'])
    if k != cur: out.append([]); cur = k
    if r['grade'] == 'U' or r['value'] in ('', '?'): continue
    out[-1].append(r['value'].split('|')[0])
print('\n'.join(''.join(x) for x in out))
