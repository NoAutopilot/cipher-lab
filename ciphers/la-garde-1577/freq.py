import csv, re
from collections import Counter

def base_digit(g):
    # strip notation suffixes/prefixes to get the bare numeral, if any
    g = g.strip()
    if g.startswith("[mark"):
        return None
    m = re.match(r"^(\d+)", g)
    return m.group(1) if m else None

files = {
    "6179": "/home/user/cipher-lab/ciphers/la-garde-1577/ciphertext_6179.tsv",
    "6467": "/home/user/cipher-lab/ciphers/la-garde-1577/ciphertext_6467.tsv",
}

overall = Counter()
per_file_counts = {}
marks = Counter()
maxval = 0
n_groups = 0
n_marks = 0
n_overline = 0
n_flourish = 0

for name, path in files.items():
    c = Counter()
    with open(path) as f:
        r = csv.DictReader(f, delimiter="\t")
        for row in r:
            g = row["group"]
            n_groups += 1
            if g.startswith("[mark"):
                n_marks += 1
                marks[g] += 1
                continue
            if "^" in g:
                n_overline += 1
            if "~" in g:
                n_flourish += 1
            d = base_digit(g)
            if d is not None:
                v = int(d)
                maxval = max(maxval, v)
                c[d] += 1
                overall[d] += 1
    per_file_counts[name] = c

print("Total token rows (incl. free-standing marks):", n_groups)
print("Distinct base-digit values:", len(overall))
print("Value range: 1 -", maxval)
print("Free-standing [mark] tokens:", n_marks, dict(marks))
print("Tokens with overline (^):", n_overline)
print("Tokens with the loop/cross flourish (~):", n_flourish)
print()
print("Top 15 most frequent digit values overall:")
for val, cnt in overall.most_common(15):
    print(f"  {val}: {cnt}")
print()
for name, c in per_file_counts.items():
    print(name, "distinct values:", len(c), "total groups:", sum(c.values()))
