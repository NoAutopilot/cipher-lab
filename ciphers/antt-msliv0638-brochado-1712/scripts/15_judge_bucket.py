"""ZX-BRO2 (25 Sept 2026), job brief: is letter 134's judge score (-1.443, YX-PTJUDGE) typical of a
same-procedure decode of this material at its length, or in the bottom tail? One held-out control per
length (ZX-BRO's Carta 96/Carta 70) is not enough -- this generalises scripts/14_loo_judge_control.py's
exact method (LOO-rebuild the key excluding one entry's own pairs, decode that entry's own coded tokens
from the rebuilt key, majority vote + C/M threshold total>=2 and n/total>=0.65, unresolved token -> '_')
to EVERY one of the appendix's 38 entries, not just Carta 96.

For entries whose LOO decode is longer than 70 letters (after folding out '_' placeholders the same way
tools/judge_plaintext.py's own fold() drops any non a-z character), the decode is cut into non-overlapping
65-letter windows (chunked on the FOLDED letter stream, i.e. windows of 65 real letters each, not 65 raw
tokens -- the '_' placeholders carry no letter identity for the judge's n-gram model either way, since its
fold() strips them from both a whole-entry candidate and a window the same way). A final remainder shorter
than 65 letters is kept as its own (shorter) window and reported, not silently dropped, so the bucket is a
complete census of this LOO procedure's output, not a cherry-picked subset -- but only windows landing in
the spec's own 40-70 letter range count toward the "40-70-letter bucket" statistics CLAUDE.md rule 3 and
this job's brief ask for (a length-min-40 window from the very end of a long entry is not comparable to a
40-70 window built the normal way, so it is scored and printed, flagged out-of-window, and excluded from
the percentile/median math).

Scoring: this job's brief names the exact CLI form (`python3 tools/judge_plaintext.py <spec> --file <f>`);
with ~38 entries x up to a handful of windows x 2 corpora (pt17, pt18) that is only ~110-130 invocations
(spot-checked below at ~1.7s each, well inside this job's time box), so every score in judge_bucket.tsv IS
that exact CLI invocation's own score, not a re-implementation -- this script shells out to it (see run_judge()
below) rather than importing the model to save code, at the cost of a slightly longer run. Percentiles and
correlation (this job's own step 2, not exposed by the CLI) are computed after the fact from Python's own
statistics module over run_judge()'s reported scores, not by re-deriving the language model.

Never touches key.tsv, _pairs.json, or the committed key.tsv-derived reading_body_letter134.txt -- this is
a read-only census of the SAME LOO procedure ZX-BRO's scripts/14 already established, run over every entry
instead of one. Candidate texts are written to a scratch directory outside the repo (not committed) since
they are not claimed readings (rule 7 applies to readings, not to a bucket-control census); judge_bucket.tsv
(entry, letters, LOO accuracy vs the gloss, score pt17, score pt18) is the only new file this job commits.
"""
import csv, json, subprocess, sys, statistics
from collections import defaultdict, Counter
from importlib import import_module

sys.path.insert(0, '/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712/scripts')
_norm = import_module('13_normalize')

ROOT = '/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712'
REPO = '/home/user/cipher-lab'
SCRATCH = '/tmp/claude-0/-home-user-cipher-lab/96cc9489-00b3-5977-8e8b-036cf961cc8b/scratchpad/judge_bucket'
SPEC_PT17 = f'{REPO}/specs/antt-msliv0638-brochado-1712.json'
SPEC_PT18 = f'{ROOT}/spec_pt18_scratch.json'

ACCENT_MAP = {'ã': 'a', 'á': 'a', 'à': 'a', 'â': 'a', 'é': 'e', 'ê': 'e', 'í': 'i', 'ó': 'o', 'ô': 'o', 'õ': 'o', 'ú': 'u', 'ç': 'c'}


def base(c):
    return _norm.fold_letter(ACCENT_MAP.get(c.lower(), c.lower()))


def fold_letters(s):
    return ''.join(ch for ch in s if ch.isalpha())


import os
os.makedirs(SCRATCH, exist_ok=True)

pairs = json.load(open(f'{ROOT}/scripts/_pairs.json'))
pairs = [(tok, base(let), tuple(key), span) for tok, let, key, span in pairs]

by_entry_pairs = defaultdict(list)
for tok, let, key, span in pairs:
    by_entry_pairs[key].append((tok, let))

entries = sorted(by_entry_pairs.keys())

crows = list(csv.DictReader(open(f'{ROOT}/ciphertext_appendix.tsv'), delimiter='\t'))
by_entry_tokens = defaultdict(list)
for r in crows:
    by_entry_tokens[(r['leaf'], r['entry_label'])].append(r)
for k in by_entry_tokens:
    by_entry_tokens[k].sort(key=lambda r: int(r['position']))

# also cover entries that appear in ciphertext_appendix.tsv but contributed 0 pairs (conflicts.tsv
# "no resolved tokens" rows) -- LOO still makes sense for these (their tokens can still be decoded from
# every OTHER entry's pairs), they just have 0 held-out pairs to check accuracy against.
all_entry_keys = sorted(set(by_entry_tokens.keys()) | set(by_entry_pairs.keys()))
print(f"{len(all_entry_keys)} distinct entries in ciphertext_appendix.tsv / _pairs.json union "
      f"({len(entries)} contribute >=1 aligned pair)")


def build_loo_key(held_entry):
    tally = defaultdict(Counter)
    for tok, let, key, span in pairs:
        if key == held_entry:
            continue
        tally[tok][let] += 1
    loo_key = {}
    for tok, c in tally.items():
        letter, n = c.most_common(1)[0]
        total = sum(c.values())
        grade = 'C' if (total >= 2 and n / total >= 0.65) else 'M'
        loo_key[tok] = (letter, grade)
    return loo_key, tally


def loo_accuracy_vs_gloss(entry, tally):
    """Same computation as scripts/11_loo_control.py's loo() inner loop, restricted to this one entry:
    predict each of the entry's own aligned pairs from the LOO tally (built from every OTHER entry),
    compare against the true letter the appendix's own Deciffrada gloss gives."""
    held = by_entry_pairs.get(entry, [])
    compared = correct = unkeyed = 0
    for tok, let in held:
        if tok in tally:
            pred = tally[tok].most_common(1)[0][0]
            compared += 1
            correct += (pred == let)
        else:
            unkeyed += 1
    pct = (100.0 * correct / compared) if compared else float('nan')
    return len(held), compared, correct, pct, unkeyed


def decode_entry(entry, loo_key):
    rows = by_entry_tokens.get(entry, [])
    decoded = []
    for r in rows:
        tok = r['token']
        if tok in loo_key:
            letter, g = loo_key[tok]
            decoded.append(letter)
        else:
            decoded.append('_')
    return ''.join(decoded)


def run_judge(spec_path, text_path):
    r = subprocess.run(['python3', f'{REPO}/tools/judge_plaintext.py', spec_path, '--file', text_path, '--json'],
                        capture_output=True, text=True, cwd=REPO)
    out = json.loads(r.stdout)
    lang = out['checks'].get('language')
    return lang['score'] if lang else None, lang


candidates = []  # (entry_label, kind, letters, loo_n, loo_compared, loo_correct, loo_pct, loo_unkeyed, text)
for e in all_entry_keys:
    loo_key, tally = build_loo_key(e)
    raw = decode_entry(e, loo_key)
    letters = fold_letters(raw)
    n_held, compared, correct, pct, unkeyed = loo_accuracy_vs_gloss(e, tally)
    label = f"{e[0]}/{e[1]}"
    if len(letters) <= 70:
        candidates.append((label, 'whole', letters, n_held, compared, correct, pct, unkeyed, letters))
    else:
        nwin = (len(letters) + 64) // 65
        for i in range(nwin):
            chunk = letters[i * 65:(i + 1) * 65]
            kind = f'win{i+1}of{nwin}'
            candidates.append((label, kind, chunk, n_held, compared, correct, pct, unkeyed, chunk))

print(f"{len(candidates)} candidates (whole entries + 65-letter windows of entries >70 letters)")

rows_out = []
for i, (label, kind, letters, n_held, compared, correct, pct, unkeyed, text) in enumerate(candidates):
    fname = f"{SCRATCH}/{label.replace('/', '_').replace(' ', '_')}_{kind}.txt"
    with open(fname, 'w') as f:
        f.write(text + '\n')
    score17, lang17 = run_judge(SPEC_PT17, fname)
    score18, lang18 = run_judge(SPEC_PT18, fname)
    in_bucket = 40 <= len(letters) <= 70
    rows_out.append(dict(entry=label, kind=kind, letters=len(letters), loo_held=n_held, loo_compared=compared,
                          loo_correct=correct, loo_pct=round(pct, 1) if pct == pct else '', loo_unkeyed=unkeyed,
                          score_pt17=score17, null_p99_pt17=lang17['null_p99'] if lang17 else '',
                          real_p05_pt17=lang17['real_p05'] if lang17 else '',
                          score_pt18=score18, null_p99_pt18=lang18['null_p99'] if lang18 else '',
                          real_p05_pt18=lang18['real_p05'] if lang18 else '',
                          in_40_70_bucket=in_bucket))
    if (i + 1) % 10 == 0:
        print(f"  scored {i+1}/{len(candidates)}", file=sys.stderr)

with open(f'{ROOT}/judge_bucket.tsv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows_out[0].keys()), delimiter='\t')
    w.writeheader()
    for r in rows_out:
        w.writerow(r)
print(f"wrote {ROOT}/judge_bucket.tsv ({len(rows_out)} rows)")

# ---- step 2: distribution stats over the 40-70-letter bucket ----
bucket17 = [r['score_pt17'] for r in rows_out if r['in_40_70_bucket']]
bucket18 = [r['score_pt18'] for r in rows_out if r['in_40_70_bucket']]
acc_for_corr = [r['loo_pct'] for r in rows_out if r['in_40_70_bucket'] and r['loo_pct'] != '']
score_for_corr17 = [r['score_pt17'] for r in rows_out if r['in_40_70_bucket'] and r['loo_pct'] != '']


def pctile(xs, q):
    xs = sorted(xs)
    if not xs:
        return float('nan')
    idx = min(len(xs) - 1, int(q * (len(xs) - 1)))
    return xs[idx]


def empirical_percentile_of(x, xs):
    xs = sorted(xs)
    if not xs:
        return float('nan')
    below = sum(1 for v in xs if v <= x)
    return 100.0 * below / len(xs)


print()
print(f"=== 40-70-letter bucket (n={len(bucket17)}) ===")
print(f"pt17: median={statistics.median(bucket17):.3f} p05={pctile(bucket17,0.05):.3f} p25={pctile(bucket17,0.25):.3f}")
print(f"pt18: median={statistics.median(bucket18):.3f} p05={pctile(bucket18,0.05):.3f} p25={pctile(bucket18,0.25):.3f}")

if len(acc_for_corr) >= 2 and len(set(acc_for_corr)) > 1 and len(set(score_for_corr17)) > 1:
    r = statistics.correlation(acc_for_corr, score_for_corr17)
    print(f"correlation(LOO accuracy vs gloss, judge score pt17) over bucket members with a defined LOO pct: r={r:.3f} (n={len(acc_for_corr)})")
else:
    print("correlation not computable (insufficient variance or n<2)")

# letter 134's own score, already on file (YX-PTJUDGE): -1.443 pt17. Score it fresh here (pt17 + pt18) for
# an apples-to-apples percentile against this bucket, and against its own shuffled-null distribution.
l134_path = f'{ROOT}/reading_body_letter134.txt'
l134_score17, l134_lang17 = run_judge(SPEC_PT17, l134_path)
l134_score18, l134_lang18 = run_judge(SPEC_PT18, l134_path)
print()
print(f"letter 134: score_pt17={l134_score17} (bucket pt17 percentile: {empirical_percentile_of(l134_score17, bucket17):.1f})")
print(f"letter 134: score_pt18={l134_score18} (bucket pt18 percentile: {empirical_percentile_of(l134_score18, bucket18):.1f})")
