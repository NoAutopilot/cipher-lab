import json, csv
from collections import defaultdict, Counter

pairs = json.load(open('/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712/scripts/_pairs.json'))
ACCENT_MAP = {'ã':'a','á':'a','à':'a','â':'a','é':'e','ê':'e','í':'i','ó':'o','ô':'o','õ':'o','ú':'u','ç':'c'}
def base(c):
    return ACCENT_MAP.get(c.lower(), c.lower())

tally = defaultdict(Counter)
entries_by_tok = defaultdict(set)
for tok, let, key, span in pairs:
    b = base(let)
    tally[tok][b]+=1
    entries_by_tok[tok].add(f"{key[0]}/{key[1]}")

def sortkey(t):
    tt = t.rstrip('±')
    return (0,int(tt)) if tt.isdigit() else (1,tt)

rows = []
for tok in sorted(tally.keys(), key=sortkey):
    c = tally[tok]
    total = sum(c.values())
    letter, n = c.most_common(1)[0]
    frac = n/total
    grade = 'C' if (total>=2 and frac>=0.65) else 'M'
    entries = ';'.join(sorted(entries_by_tok[tok]))
    rows.append([tok, letter, total, grade, entries, json.dumps(dict(c), ensure_ascii=False)])

with open('/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712/key.tsv','w') as f:
    w = csv.writer(f, delimiter='\t')
    w.writerow(['code','value','n_occurrences','grade','entries','all_observed_letters'])
    for r in rows:
        w.writerow(r)
print("wrote", len(rows), "rows to key.tsv")
