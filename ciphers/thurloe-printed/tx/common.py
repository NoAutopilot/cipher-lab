import csv

def load_key(path, value_col='value', meaning_col='meaning', grade_col='grade'):
    """Load a value -> {meaning, grade} key table, tolerant of the small column-order
    differences between key_butler.tsv / key_blake_extended.tsv (value, meaning, grade, ...)
    and key_fauconberg.tsv / pool_1654/key_stamford.tsv (value, meaning, votes, grade, ...)."""
    out = {}
    with open(path, newline='') as f:
        lines = [ln for ln in f if not ln.startswith('#')]
    r = csv.DictReader(lines, delimiter='\t')
    for row in r:
        v = (row.get(value_col) or '').strip()
        if not v:
            continue
        out[v] = {'meaning': (row.get(meaning_col) or '').strip(),
                  'grade': (row.get(grade_col) or '').strip()}
    return out
