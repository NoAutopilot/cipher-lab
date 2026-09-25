"""ZX-BRO (25 Sept 2026), job brief step 4: a matched control for tools/judge_plaintext.py -- decode one
appendix entry (m0291 Carta 96, 42 coded tokens, held OUT of the key exactly as letter 134 necessarily is)
with a leave-one-out key, exactly the way letter 134 was decoded, and judge that text the same way, so we
know whether a genuinely-Portuguese, similar-length decode of this material can pass the judge at all --
before treating letter 134's own FAIL as a verdict on the reading rather than a limit of the judge at this
length. Chosen for length: Carta 96's full deciffrada line is 51 letters (within the spec's 40-70 window);
its 42 coded tokens are decoded and concatenated the same way reading_body_letter134.txt concatenates its
two spans (no clear-text words re-inserted, since letter 134's own reading file does not include the plain
Portuguese context around its coded spans either).

Never touches key.tsv (the committed key everything else in this folder uses) or _pairs.json -- this is a
throwaway LOO key for this one comparison, discarded after the print below.
"""
import json, csv, sys
from collections import defaultdict, Counter
sys.path.insert(0, '/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712/scripts')
from importlib import import_module
_norm = import_module('13_normalize')

ROOT = '/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712'
ACCENT_MAP = {'ã':'a','á':'a','à':'a','â':'a','é':'e','ê':'e','í':'i','ó':'o','ô':'o','õ':'o','ú':'u','ç':'c'}
def base(c):
    return _norm.fold_letter(ACCENT_MAP.get(c.lower(), c.lower()))

HELD_OUT = ('m0291', 'Carta 96')

pairs = json.load(open(f'{ROOT}/scripts/_pairs.json'))
tally = defaultdict(Counter)
for tok, let, key, span in pairs:
    if tuple(key) == HELD_OUT:
        continue  # true LOO: this entry's own pairs never inform the key that decodes it
    tally[tok][base(let)] += 1

loo_key = {}
for tok, c in tally.items():
    letter, n = c.most_common(1)[0]
    total = sum(c.values())
    grade = 'C' if (total >= 2 and n/total >= 0.65) else 'M'
    loo_key[tok] = (letter, grade)

rows = [r for r in csv.DictReader(open(f'{ROOT}/ciphertext_appendix.tsv'), delimiter='\t')
        if (r['leaf'], r['entry_label']) == HELD_OUT]
print(f"Carta 96 ({HELD_OUT}): {len(rows)} coded tokens")

decoded = []
grades = Counter()
for r in rows:
    tok = r['token']
    if tok in loo_key:
        letter, g = loo_key[tok]
        decoded.append(letter)
        grades[g if g == 'M' else 'C'] += 1  # C/M per the LOO key's own confidence; U below
    else:
        decoded.append('_')
        grades['U'] += 1

text = ''.join(decoded)
print(f"LOO decode (key never saw Carta 96's own pairs): {text!r}")
print(f"length: {len(text)}  grades: C={grades['C']} M={grades['M']} U={grades['U']}")

# accuracy vs the entry's own known gloss, for the tokens that WERE aligned pairs in the real key
# (i.e. compare against the ground truth this entry's Deciffrada line actually gives, position by
# position, for the same positions 03_align_pairs.py resolved -- read straight from _pairs.json's
# per-entry ordering, unaffected by holding the entry out of the KEY used to decode it)
true_by_pos = []
idx = 0
for tok, let, key, span in pairs:
    if tuple(key) == HELD_OUT:
        true_by_pos.append(base(let))
if true_by_pos:
    resolved_positions = [i for i, r in enumerate(rows) if r['token'] in loo_key]
    # _pairs.json's order for this entry matches ciphertext_appendix.tsv's row order restricted to
    # resolved (non-mismatch) spans; Carta 96 contributed 0 pairs (conflicts.tsv), so this is empty --
    # printed for transparency, not assumed non-empty.
    print(f"aligned ground-truth letters available for this entry in _pairs.json: {len(true_by_pos)}")
else:
    print("this entry contributed 0 pairs to _pairs.json (already excluded from the real key too, per "
          "conflicts.tsv 'Carta 96' entry -- LOO here changes nothing about which codes are keyed, only "
          "confirms the same codes decode the same way whether or not this entry's own (non-existent) "
          "pairs are in the tally)")

with open(f'{ROOT}/reading_loo_control_carta96.txt', 'w') as f:
    f.write(text + '\n')
print(f"wrote {ROOT}/reading_loo_control_carta96.txt")
