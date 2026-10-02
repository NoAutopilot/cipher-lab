"""A2-LVN4: print +/-W decoded tokens around each once/twice-seen name code (>151) in 4610/4611/4616.
Reads reading_{4610,4611,4616}_full_tokens.tsv (key_full v3). NULLs dropped, U shown as <code>, name codes as [value].
Usage: python3 replies/contexts.py [W]  -> replies/contexts.tsv"""
import csv, sys, os
W = int(sys.argv[1]) if len(sys.argv) > 1 else 14
D = os.path.dirname(os.path.abspath(__file__)) + '/..'
CODES = {'4610': '180 182 184 186 191 194 203 205 225', '4611': '174 175 187 199 204 211 214 225 228 232 245 248 254 280 311 331 335', '4616': '313'}
out = []
for L, cs in CODES.items():
    cs = set(cs.split())
    rows = list(csv.DictReader(open(f'{D}/reading_{L}_full_tokens.tsv'), delimiter='\t'))
    rows = [r for r in rows if r['value'] != 'NULL']
    def show(r):
        v = r['value']
        if r['grade'] == 'U' or v == '?': return '<%s>' % r['sign']
        return v if len(v) == 1 else '[%s]' % v
    for i, r in enumerate(rows):
        if r['sign'] in cs:
            left = ' '.join(show(x) for x in rows[max(0, i - W):i])
            right = ' '.join(show(x) for x in rows[i + 1:i + 1 + W])
            out.append((r['sign'], L, r['line'], left, right))
out.sort(key=lambda t: int(t[0]))
with open(f'{D}/replies/contexts.tsv', 'w') as f:
    f.write('code\tletter\tline\tleft\tright\n')
    for t in out: f.write('\t'.join(t) + '\n')
for t in out: print('%s %s %s | %s  ##  %s' % t)
