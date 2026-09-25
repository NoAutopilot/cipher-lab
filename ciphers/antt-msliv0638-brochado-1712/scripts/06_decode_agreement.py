import csv, json
from collections import defaultdict

"""PX-BROKEY2 step 3: the control CLAUDE.md rule 7 asks for -- "the key must re-read its own source".
key.tsv was built FROM the appendix's own Deciffrada glosses (scripts 01-04), so this does not test
whether the key is right in some independent sense; it tests whether decode_key.py, run mechanically
from ciphertext_appendix.tsv + key.tsv (decode.json), reproduces the same letters scripts/03_align_pairs.py
already paired each code to. A gap here means the *pipeline* (decode_key.py's own grading/rendering, not
the alignment) introduced a discrepancy -- e.g. a code appearing in _pairs.json with one majority letter
but a different key.tsv row (should not happen, both come from the same 04_build_key.py run, but this is
the check that would catch it if the two ever drifted), or a code graded C from a *different* accent-folded
letter than the one a specific occurrence's own span shows (a homophone -- expected and reported, not a
bug). Per-position source: scripts/_pairs.json (leaf, entry_label, and token in original per-entry, per-
position order, produced by 03_align_pairs.py in the same order it reads ciphertext_appendix.tsv's rows).

PX-BRODEC3 (25 Sept 2026) fix: PX-BRODEC2 found that comparing expected vs. decoded via
difflib.SequenceMatcher, even when the two sequences are the SAME LENGTH (no real insertion/deletion --
every one of an entry's tokens resolved to a pair), lets the LCS-style alignment slide real mismatches
onto a same-letter coincidence a few positions away and drop others as an unindexed 'delete' opcode this
script's own tally never counted -- understating both compared and mismatches (Carta 80: true 10/17=58.8%
positional agreement reported as 15/13->86.7% via conflicts.tsv's old row). Fixed: when
len(expected)==len(decoded_known), compare position by position directly (no difflib at all -- there is
no alignment ambiguity to resolve when nothing was inserted or deleted). difflib.SequenceMatcher is used
ONLY when the two sequences differ in length (a real gap -- an unresolved/dropped token), and that entry's
detail column says so explicitly so a reader can tell which entries got the exact count and which got an
aligned estimate.
"""

ROOT = '/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712'
import sys
sys.path.insert(0, f'{ROOT}/scripts')
from importlib import import_module
_norm = import_module('13_normalize')
ACCENTS = str.maketrans('ãáàâéêíóôõúç', 'aaaaeeiooouc')
def fold(c):
    # ZX-BRO (25 Sept 2026): accent fold (unchanged) composed with the u/v, i/j, y/i spelling-convention
    # fold (scripts/13_normalize.py), applied identically to both the expected letter and the decoded
    # value so it reaches BOTH sides of every diff this script reports.
    return _norm.fold_letter(c.lower().translate(ACCENTS))

# expected letter per (leaf, entry_label, occurrence-index-within-entry-of-this-token), built by walking
# ciphertext_appendix.tsv in position order and consuming _pairs.json's per-entry letter list in the same
# order 03_align_pairs.py produced it (one CODE span at a time, tokens and letters zipped 1:1).
pairs = json.load(open(f'{ROOT}/scripts/_pairs.json', encoding='utf-8'))
expected_seq = defaultdict(list)  # (leaf, entry) -> [letter, letter, ...] in the order pairs.json emitted them
for tok, let, key, span in pairs:
    expected_seq[tuple(key)].append(fold(let))

tok_rows = list(csv.DictReader(open(f'{ROOT}/ciphertext_appendix.tsv'), delimiter='\t'))
decoded_rows = list(csv.DictReader(open(f'{ROOT}/reading_appendix_tokens.tsv'), delimiter='\t'))
# reading_appendix_tokens.tsv has one row per ciphertext_appendix.tsv row, same order, columns line/pos/sign/conf/value/grade
assert len(tok_rows) == len(decoded_rows), (len(tok_rows), len(decoded_rows))

# 03_align_pairs.py appends pairs while iterating CODE spans of merged segments in the same order the
# entry's tokens occur (it never re-orders tokens within a span), so expected_seq[(leaf,entry)] consumed
# in order lines up with that entry's own resolved (non-mismatched) tokens, position by position, in the
# SAME relative order as tok_rows/decoded_rows restricted to that entry -- but tok_rows/decoded_rows also
# include tokens from *mismatched* (unresolved) spans that never made it into pairs.json. We can only
# compare where we independently know which of an entry's tokens were resolved: recompute that from
# _anchors.json + the same span logic would duplicate 03_align_pairs.py, so instead this control compares
# per ENTRY, aligning expected_seq's letters against the decoded value sequence via difflib -- exact under
# insertions/deletions from the unresolved gaps, and reports the aligned-position match rate.
import difflib

by_entry_tokens = defaultdict(list)
for tr, dr in zip(tok_rows, decoded_rows):
    key = (tr['leaf'], tr['entry_label'])
    by_entry_tokens[key].append(fold(dr['value']) if dr['value'] not in ('?', '') else None)

rows = []
total_compared = total_agree = 0
for key, decoded_vals in by_entry_tokens.items():
    expected = expected_seq.get(key, [])
    if not expected:
        rows.append((key[0], key[1], 0, 0, '', 'no resolved tokens (entry had no usable anchors)'))
        continue
    decoded_known = [v for v in decoded_vals if v is not None]
    mismatches = []
    if len(expected) == len(decoded_known):
        # No insertion/deletion possible -- compare position by position, no difflib. This is the
        # exact-count case difflib's LCS alignment used to misreport (PX-BRODEC2).
        compared = len(expected)
        agree = 0
        for e, d in zip(expected, decoded_known):
            if e == d:
                agree += 1
            else:
                mismatches.append(f"{e}!={d}")
        note = '; '.join(mismatches)
    else:
        # Lengths genuinely differ (an unresolved/dropped token) -- difflib is the right tool here,
        # and the entry says so rather than presenting an aligned estimate as an exact count.
        sm = difflib.SequenceMatcher(a=expected, b=decoded_known, autojunk=False)
        compared = agree = 0
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == 'equal':
                compared += i2 - i1; agree += i2 - i1
            elif tag == 'replace':
                n = min(i2 - i1, j2 - j1)
                compared += n
                for k in range(n):
                    mismatches.append(f"{expected[i1+k]}!={decoded_known[j1+k]}")
        note = (f"[difflib-aligned, length gap: expected {len(expected)} resolved letters, "
                f"{len(decoded_known)} keyed decode values] " + '; '.join(mismatches))
    total_compared += compared; total_agree += agree
    pct = 100.0 * agree / compared if compared else 0.0
    if agree != compared or compared < len(expected):
        rows.append((key[0], key[1], compared, agree, f"{pct:.0f}%", note or
                     f"length gap: expected {len(expected)} resolved letters, {len(decoded_known)} keyed decode values"))

rows.sort(key=lambda r: (r[0], r[1]))
with open(f'{ROOT}/conflicts.tsv', 'w') as f:
    w = csv.writer(f, delimiter='\t')
    w.writerow(['leaf', 'entry_label', 'compared', 'agree', 'pct', 'detail'])
    for r in rows:
        w.writerow(r)

print(f"entries with a resolved control: {sum(1 for k in by_entry_tokens if expected_seq.get(k))}/{len(by_entry_tokens)}")
print(f"positions compared: {total_compared}, agree: {total_agree} ({100.0*total_agree/total_compared:.1f}%)" if total_compared else "no positions compared")
print(f"entries written to conflicts.tsv (not 100% or not fully resolved): {len(rows)}")
