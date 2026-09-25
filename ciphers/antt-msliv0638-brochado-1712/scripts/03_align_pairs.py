import json, re
from collections import defaultdict, Counter

"""PX-BROKEY2 fix (25 Sept 2026): a CODE run's span used to be bounded only by its *immediate* PLAIN
neighbours in the segment list; if either neighbour's own anchor was unresolved (02_anchor.py's new
per-word graceful skip), the span silently fell back to 0/len(decif) -- wrong, and previously masked
because 02_anchor.py aborted the whole entry on any unresolved word instead. This version walks outward
to the *nearest resolved* PLAIN anchor on each side (skipping unresolved ones), so a single unplaced
word only costs the span(s) touching it, not the rest of the entry. A span still bounded by 0 or
len(decif) because *no* anchor exists on that side (start/end of the entry) is unchanged from before."""

data = json.load(open('/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712/scripts/_anchors.json'))

code_letter_pairs = []  # (code, letter, key, word_context)
mismatches = []

LETTERS_RE = re.compile(r"[A-Za-zÀ-ÿ]")

for key, merged, decif, anchor_pos, ok in data:
    anchor_pos = {int(k): v for k, v in anchor_pos.items()}
    n = len(merged)
    for i, (t, v) in enumerate(merged):
        if t != 'CODE':
            continue
        tokens = v
        start = 0
        for j in range(i - 1, -1, -1):
            if j in anchor_pos:
                start = anchor_pos[j][1]
                break
        end = len(decif)
        for j in range(i + 1, n):
            if j in anchor_pos:
                end = anchor_pos[j][0]
                break
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

json.dump(code_letter_pairs, open('/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712/scripts/_pairs.json', 'w'), ensure_ascii=False)

print()
print("=== code -> letter tally (sorted by code) ===")
def sortkey(t):
    tt = t.rstrip('±')
    return (0, int(tt)) if tt.isdigit() else (1, tt)
for tok in sorted(tally.keys(), key=sortkey):
    c = tally[tok]
    total = sum(c.values())
    top = c.most_common()
    print(f"{tok:5s} n={total:3d}  {top}")
