import csv, json, re
from collections import defaultdict, Counter

"""AX-BRO3 (26 Sept 2026): the NEAR.md-named next step for letter 134 -- more observations of its six
thin codes (x, z, d, f, 16, 9; YX-BRO79 Step 4 / ZX-BRO2 Step 3) -- lives inside the appendix's own
already-transcribed, already-image-reconciled entries, not on unswept body leaves (body_leaves.tsv's
stride-8 sweep of the whole 306-image letterbook already found cipher runs only on the three leaves
already in the appendix plus letter 134 itself; see NOTES.md "AX-BRO3" section, Step 1).

This reuses 02_anchor.py's exact anchor-finding and 03_align_pairs.py's exact nearest-anchor
span-bounding per CODE run (never a flat whole-entry diff -- 34 of 38 entries have PLAIN words mixed
in, so a whole-entry positional decode would be wrong for them), then adds ONE relaxation
03_align_pairs.py does not have: 03_align_pairs.py requires a bounded span's letter-count to equal its
token-count EXACTLY (34 of 38 entries fail this, mostly by a few letters -- the appendix editor's own
abbreviation habit, not a transcription error, per the PX-BRODEC rule-3 lesson already in CLAUDE.md).
Here, where a span's whole length does not match, we still check whether a PREFIX (scanning forward
from the span's start) or a SUFFIX (scanning backward from the span's end) of the codes with an
already-known key.tsv value matches the corresponding gloss letters one-for-one; a target thin code
sitting inside that clean prefix/suffix gets a context-implied letter this way. A code in the drifted
middle of a mismatched span is reported `cannot tell`, never guessed.

Output: ciphers/antt-msliv0638-brochado-1712/thin_codes_attest.tsv, one row per occurrence of the six
codes found in _anchors.json's segment-level token lists, marked new (not already among the 379 pairs
_pairs.json used to build key.tsv) or already-counted, with its verdict (fits / differs / cannot tell).
"""

ROOT = '/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712'
ACCENT_MAP = {'ã': 'a', 'á': 'a', 'à': 'a', 'â': 'a', 'é': 'e', 'ê': 'e', 'í': 'i',
              'ó': 'o', 'ô': 'o', 'õ': 'o', 'ú': 'u', 'ç': 'c'}


def basefold(c):
    return ACCENT_MAP.get(c.lower(), c.lower())


LETTERS_RE = re.compile(r"[A-Za-zÀ-ÿ]")
TARGET = {'x', 'z', 'd', 'f', '16', '9'}

key_rows = list(csv.DictReader(open(f'{ROOT}/key.tsv'), delimiter='\t'))
key_by_code = {r['code'].rstrip('±'): r for r in key_rows}


def code_val(code):
    row = key_by_code.get(code.rstrip('±'))
    return row['value'] if row else None


# which (code, entry) occurrences are already among the pairs used to build key.tsv
pairs = json.load(open(f'{ROOT}/scripts/_pairs.json'))
resolved_n = Counter()
for tok, let, key, ctx in pairs:
    if tok in TARGET:
        resolved_n[(tok, tuple(key))] += 1

anchors = json.load(open(f'{ROOT}/scripts/_anchors.json'))

rows_out = []
seen_count = Counter()
for key, merged, decif, anchor_pos, ok in anchors:
    entry = tuple(key)
    anchor_pos = {int(k): v for k, v in anchor_pos.items()}
    n = len(merged)
    for i, (t, v) in enumerate(merged):
        if t != 'CODE':
            continue
        tokens = v
        if not any(tok in TARGET for tok in tokens):
            continue
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
        letters = [basefold(c) for c in span if LETTERS_RE.match(c)]
        n_t, n_g = len(tokens), len(letters)

        fwd_ok = 0
        for k_ in range(min(n_t, n_g)):
            vv = code_val(tokens[k_])
            if vv is None:
                fwd_ok = k_ + 1
                continue
            if basefold(vv) == letters[k_]:
                fwd_ok = k_ + 1
            else:
                break

        rev_ok = 0
        for k_ in range(min(n_t, n_g)):
            ti, gi = n_t - 1 - k_, n_g - 1 - k_
            vv = code_val(tokens[ti])
            if vv is None:
                rev_ok = k_ + 1
                continue
            if basefold(vv) == letters[gi]:
                rev_ok = k_ + 1
            else:
                break

        for local_idx, tok in enumerate(tokens):
            if tok not in TARGET:
                continue
            seen_count[(tok, entry)] += 1
            is_new = seen_count[(tok, entry)] > resolved_n[(tok, entry)]
            cur = code_val(tok)
            verdict, implied = 'cannot tell', None
            if local_idx < fwd_ok and local_idx < n_g:
                implied = letters[local_idx]
                verdict = 'fits' if (cur and basefold(cur) == implied) else 'differs'
            elif (n_t - 1 - local_idx) < rev_ok:
                gi = n_g - (n_t - local_idx)
                if 0 <= gi < n_g:
                    implied = letters[gi]
                    verdict = 'fits' if (cur and basefold(cur) == implied) else 'differs'
            ctx = tokens[max(0, local_idx - 2):local_idx] + ['[' + tok + ']'] + tokens[local_idx + 1:local_idx + 3]
            rows_out.append({
                'code': tok, 'leaf': entry[0], 'entry_label': entry[1],
                'new_occurrence': 'yes' if is_new else 'no (already in key.tsv build)',
                'context_codes': '.'.join(ctx),
                'decoded_context': span[:70].replace('\t', ' '),
                'verdict': verdict, 'implied_letter': implied or '', 'key_current_value': cur or '',
            })

with open(f'{ROOT}/thin_codes_attest.tsv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['code', 'leaf', 'entry_label', 'new_occurrence', 'context_codes',
                                       'decoded_context', 'verdict', 'implied_letter', 'key_current_value'],
                        delimiter='\t')
    w.writeheader()
    for r in rows_out:
        w.writerow(r)

new_rows = [r for r in rows_out if r['new_occurrence'] == 'yes']
print(f"total thin-code occurrences examined: {len(rows_out)}, new (not already in key.tsv build): {len(new_rows)}")
print("new verdicts:", Counter(r['verdict'] for r in new_rows))
print("new differs (would contradict key.tsv, needs >=2 agreeing before any change, CLAUDE.md rule 3 step 3):")
for r in new_rows:
    if r['verdict'] == 'differs':
        print(' ', r)
print("new fits (confirms key.tsv's current value):")
for r in new_rows:
    if r['verdict'] == 'fits':
        print(' ', r['code'], r['leaf'], r['entry_label'], r['key_current_value'], r['decoded_context'][:50])
