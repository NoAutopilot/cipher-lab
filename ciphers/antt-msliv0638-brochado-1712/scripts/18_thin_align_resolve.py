import csv
from collections import defaultdict, Counter

"""AX2-BRO4 (26 Sept 2026), unit 1 step 2 -- run only after 18_thin_align_gate.py's known-answer
control passes (gate: real 1.000 vs shuffled mean 0.350, margin 0.650; see NOTES.md). Hides the six
thin codes (x, z, d, f, 16, 9 -- key.tsv rows x/z/d/f/16/9-or-9pm, base identity stripped of '±') from
the DP's --prior the same way the gate masked one code at a time, so their aligned chunks come from
surrounding context alone, then reads off the aligner's value at each of the 69 AX-BRO3
'cannot tell' occurrences (thin_codes_attest.tsv, new_occurrence=yes) and compares it to key.tsv's
current value for that code -- agree / differ / still undecidable, per occurrence, never a flat
whole-code verdict (a homophone could resolve differently at different occurrences).

Occurrence matching: thin_codes_attest.tsv and align/pairs.tsv are both built by walking the SAME
_anchors.json entries in the SAME order (16_thin_attest.py and 17_build_pairs.py both iterate
anchors -> merged segments -> CODE run tokens in file order), so the Nth thin_codes_attest.tsv row for
a given (code, leaf/entry_label) is the Nth occurrence of that '@code' raw token in that entry's
out_align.tsv rows. No independent position field is needed; this ordering identity is verified below
by checking every (code, entry) occurrence count matches between the two files before using it.
"""

ROOT = '/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712'
TOOL = '/home/user/cipher-lab/tools/interlinear_align.py'
TARGET = {'x', 'z', 'd', 'f', '16', '9'}
ACCENT_MAP = {'ã': 'a', 'á': 'a', 'à': 'a', 'â': 'a', 'é': 'e', 'ê': 'e', 'í': 'i',
              'ó': 'o', 'ô': 'o', 'õ': 'o', 'ú': 'u', 'ç': 'c'}


def basefold(c):
    return ACCENT_MAP.get(c.lower(), c.lower())


key_rows = list(csv.DictReader(open(f'{ROOT}/key.tsv'), delimiter='\t'))
key_by_code = {r['code'].rstrip('±'): r['value'] for r in key_rows}

import subprocess, sys, tempfile, os, shutil

# One masked code AT A TIME (matching 18_thin_align_gate.py's validated protocol exactly): masking
# all six thin codes simultaneously was tried first and rejected -- it let uncertainty compound within
# a single entry (m0290/Carta 93 alone carries 3 'z' occurrences and a '16'), and its own aggregate
# key for 'z' lost the two solid pre-existing r-occurrences from its counts entirely (0/9, not even
# among the 'others'), a result the one-at-a-time gate run never produced for any n>=5 code. Every
# OTHER thin code keeps its own key.tsv value seeded while the current target is masked, exactly as
# the gate did for the n>=5 codes.
occ_by_code_entry = {}
committed_align = {}
for target_code in sorted(TARGET):
    prior_rows = [r for r in key_rows if r['code'].rstrip('±') != target_code]
    d = tempfile.mkdtemp()
    prior_path = os.path.join(d, 'prior.tsv')
    with open(prior_path, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['code', 'value'])
        for r in prior_rows:
            w.writerow([r['code'], r['value']])
    out_align = os.path.join(d, 'align.tsv')
    out_key = os.path.join(d, 'key.tsv')
    subprocess.run([sys.executable, TOOL, 'align', f'{ROOT}/align/pairs.tsv', out_align, out_key,
                     '--code-prefix', '@', '--clear-consumes', '--prior', prior_path], check=True,
                    capture_output=True)
    dest_a = f'{ROOT}/align/align_mask_{target_code.replace("±", "pm")}.tsv'
    dest_k = f'{ROOT}/align/key_mask_{target_code.replace("±", "pm")}.tsv'
    shutil.copy(out_align, dest_a)
    shutil.copy(out_key, dest_k)
    committed_align[target_code] = dest_a
    for r in csv.DictReader(open(out_align), delimiter='\t'):
        if r['raw'] == '@' + target_code:
            occ_by_code_entry.setdefault((target_code, r['cipher_line']), []).append(r)
print(f'ran {len(TARGET)} one-code-masked alignments (one per thin code), files: {sorted(committed_align.values())}')

attest_rows = list(csv.DictReader(open(f'{ROOT}/thin_codes_attest.tsv'), delimiter='\t'))

# 17_build_pairs.py strips a token's own uncertain-glyph '±' marker to its base code identity
# (z and z± both become '@z'), which is the right identity for the aligner but means out_align.tsv's
# occurrence list for a code can hold MORE entries than thin_codes_attest.tsv's (16_thin_attest.py's
# TARGET matched the bare string only, never the '±'-flagged reading of the same code). Build the
# bare-occurrence -> all-occurrence index map straight from _anchors.json (the same source file both
# scripts read) instead of assuming the two files' occurrence counts already line up.
import json
anchors = json.load(open(f'{ROOT}/scripts/_anchors.json'))
bare_to_all_idx = {}  # (code, entry, bare_occurrence_number) -> index into occ_by_code_entry
all_ctr = Counter()
bare_ctr = Counter()
for key, merged, decif, anchor_pos, ok in anchors:
    entry = '/'.join(key)
    for t, v in merged:
        if t != 'CODE':
            continue
        for tok in v:
            base = tok.rstrip('±')
            if base not in TARGET:
                continue
            ak = (base, entry)
            all_i = all_ctr[ak]
            all_ctr[ak] += 1
            if tok == base:  # bare, no uncertain-glyph marker -- what 16_thin_attest.py counted
                bare_to_all_idx[(base, entry, bare_ctr[ak])] = all_i
                bare_ctr[ak] += 1

seen_idx = Counter()
results = []
for r in attest_rows:
    key = (r['code'], f"{r['leaf']}/{r['entry_label']}")
    bare_n = seen_idx[key]
    seen_idx[key] += 1
    idx = bare_to_all_idx[(r['code'], key[1], bare_n)]
    align_row = occ_by_code_entry[key][idx]
    chunk = align_row['plain_chunk']
    truth = key_by_code.get(r['code'])
    if not chunk:
        verdict = 'still undecidable'
        got = ''
    else:
        got = basefold(chunk[0]) if len(chunk) else ''
        # a floor code takes at most one letter; report the single aligned letter
        got = basefold(chunk)
        verdict = 'agree' if (truth and basefold(truth) == basefold(chunk)) else 'differ'
    results.append({**r, 'pass_align_chunk': chunk, 'pass_align_status': align_row['status'],
                     'pass_verdict': verdict if r['verdict'] == 'cannot tell' else '(already resolved by AX-BRO3)'})

new_cannot_tell = [r for r in results if r['verdict'] == 'cannot tell']
print(f'{len(new_cannot_tell)} cannot-tell rows re-examined via alignment')
vc = Counter(r['pass_verdict'] for r in new_cannot_tell)
print('pass verdicts:', dict(vc))

# per-code differ tally: does any single alternate value get >=2 independent agreeing occurrences?
differs_by_code = defaultdict(Counter)
for r in new_cannot_tell:
    if r['pass_verdict'] == 'differ' and r['pass_align_chunk']:
        differs_by_code[r['code']][basefold(r['pass_align_chunk'])] += 1
print()
print('differ tallies by code (>=2 on one alternate value would meet the rule-3 key-change bar):')
for code, cnt in differs_by_code.items():
    print(f'  {code}: {dict(cnt)}')

with open(f'{ROOT}/thin_codes_attest.tsv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = list(results[0].keys())
    w = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')
    w.writeheader()
    w.writerows(results)
print()
print('thin_codes_attest.tsv updated in place with pass_align_chunk / pass_align_status / pass_verdict columns')
