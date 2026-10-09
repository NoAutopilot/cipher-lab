#!/usr/bin/env python3
"""V-BRO24 (9 Oct 2026): re-tally code 24 over every glossed appendix entry, 24 masked from the key.

  python3 scripts/26_vbro24_tally.py            # writes code24_attest.tsv
  python3 scripts/26_vbro24_tally.py --check    # rule 7: exit 1 if code24_attest.tsv is stale

Each appendix entry's mixed stream (align/pairs.tsv cipher_raw: '@code' tokens and clear words) is aligned against its
Deciffrada gloss with scripts/24_bro123_align.py's DP, under two masks: (a) only 24 removed from key.tsv; (b) BRO-123's
attest mask (all thin codes removed). The letter each 24 lands on is recorded; grade C when >= 3 of the 4 nearest
aligned neighbours match (BRO-123's anchored rule), else M. Verifier check of a key value, not a reading.
"""
import csv, importlib.util, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location('b', HERE / 'scripts' / '24_bro123_align.py')
b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
csv.field_size_limit(10**8)
key = b.load_key()
masks = {'only24': {c: v for c, v in key.items() if c != '24'},
         'thin': {c: v for c, v in key.items() if c not in b.THIN}}
rows = []
with open(HERE / 'align' / 'pairs.tsv') as f:
    for r in csv.DictReader(f, delimiter='\t'):
        raw = r['cipher_raw'].split()
        if '@24' not in raw:
            continue
        stream = [('', '', t[1:] if t.startswith('@') else 'w:' + t) for t in raw]
        units = b.expand(stream)
        let = b.fold(r['plain_raw'])
        for mname, mk in masks.items():
            pairs = b.align(units, let, mk)
            for idx, (ui, lj) in enumerate(pairs):
                kind, val, k = units[ui]
                if kind != 'c' or val != '24':
                    continue
                L = let[lj] if lj >= 0 else '-'
                def ctx(rng):
                    s = ''
                    for q in rng:
                        if 0 <= q < len(pairs):
                            u2, l2 = pairs[q]
                            if l2 < 0: s += '_'; continue
                            k2, v2, _ = units[u2]
                            ok = (k2 == 'w' and v2 == let[l2]) or (k2 == 'c' and mk.get(v2) == let[l2])
                            s += let[l2].upper() if ok else let[l2]
                    return s
                lc, rc = ctx(range(idx - 4, idx)), ctx(range(idx + 1, idx + 5))
                anch = sum(c.isupper() for c in lc[-2:] + rc[:2]) >= 3
                cid = ' '.join(t for t in raw[max(0, k - 3):k + 4])
                rows.append([r['cipher_line'], k, mname, L, lc, rc, 'C' if (L != '-' and anch) else 'M', cid])
out = 'entry\tstream_idx\tmask\taligned_letter\tleft_ctx\tright_ctx\tgrade\tcipher_ctx\n' + \
      ''.join('\t'.join(map(str, x)) + '\n' for x in rows)
p = HERE / 'code24_attest.tsv'
if '--check' in sys.argv:
    sys.exit(0 if p.exists() and p.read_text() == out else 1)
p.write_text(out)
print(out)
