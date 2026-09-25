import json, re
from collections import defaultdict, Counter

data = json.load(open('/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712/scripts/_anchors.json'))

code_letter_pairs = []  # (code, letter, key, word_context)
mismatches = []

LETTERS_RE = re.compile(r"[A-Za-zÀ-ÿ]")

for key, merged, decif, anchor_pos, ok in data:
    if not ok:
        continue
    anchor_pos = {int(k):v for k,v in anchor_pos.items()}
    n = len(merged)
    for i,(t,v) in enumerate(merged):
        if t != 'CODE':
            continue
        tokens = v
        # determine span start
        if i-1 in anchor_pos:
            start = anchor_pos[i-1][1]
        elif i == 0:
            start = 0
        else:
            # previous seg not anchor (shouldn't happen since merged alternates C/P after merge)
            start = 0
        if i+1 in anchor_pos:
            end = anchor_pos[i+1][0]
        elif i == n-1:
            end = len(decif)
        else:
            end = len(decif)
        span = decif[start:end]
        letters = [c for c in span if LETTERS_RE.match(c)]
        if len(letters) != len(tokens):
            mismatches.append((key, tokens, span, letters))
            continue
        for tok, let in zip(tokens, letters):
            code_letter_pairs.append((tok, let, key, span))

print("total aligned pairs:", len(code_letter_pairs))
print("mismatched spans:", len(mismatches))
for m in mismatches:
    print(" MISMATCH", m[0], "ntoks=", len(m[1]), "nletters=", len(m[3]), "span=", repr(m[2])[:80])

# tally
tally = defaultdict(Counter)
for tok, let, key, span in code_letter_pairs:
    tally[tok][let] += 1

json.dump(code_letter_pairs, open('/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712/scripts/_pairs.json','w'), ensure_ascii=False)

print()
print("=== code -> letter tally (sorted by code) ===")
def sortkey(t):
    tt = t.rstrip('±')
    return (0,int(tt)) if tt.isdigit() else (1,tt)
for tok in sorted(tally.keys(), key=sortkey):
    c = tally[tok]
    total = sum(c.values())
    top = c.most_common()
    print(f"{tok:5s} n={total:3d}  {top}")
