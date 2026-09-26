import csv, random, subprocess, sys, tempfile, os

"""AX2-BRO4 (26 Sept 2026), CLAUDE.md rule 3 known-answer control, run BEFORE the 69 cannot-tell
thin-code occurrences are read from the aligner. Every code.tsv value here is a single letter (key.tsv
has no syllable/word-valued code at all -- checked directly, reported below), so 'per class' collapses
to one class for this target; there is no syllable or word class to report separately.

For each key.tsv code with >=5 observations: mask it out of the --prior file (its value hidden from
the aligner entirely), run tools/interlinear_align.py align --code-prefix @ --clear-consumes on the
real align/pairs.tsv, and check whether the aligner's own converged value for that code (from context
alone, seeded by every OTHER code's known value) equals key.tsv's. Repeat on a shuffled-gloss control
(plain_raw reassigned to a different entry's cipher_raw, 3 seeds) to see whether the same recovery rate
would happen even when the plain text is provably wrong for the cipher line it's paired with.
"""

ROOT = '/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712'
TOOL = '/home/user/cipher-lab/tools/interlinear_align.py'

key_rows = list(csv.DictReader(open(f'{ROOT}/key.tsv'), delimiter='\t'))
mask_codes = [r for r in key_rows if int(r['n_occurrences']) >= 5]
print(f'{len(key_rows)} key.tsv codes total, {len(mask_codes)} with >=5 observations (the known-answer set)')
non_single = [r for r in key_rows if len(r['value']) != 1]
print(f'codes with a non-single-letter value: {len(non_single)} -- {non_single}')
print('=> every code.tsv value is one letter; no syllable/word class exists in this cipher to report separately.')


def write_prior(rows, path):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['code', 'value'])
        for r in rows:
            w.writerow([r['code'], r['value']])


def run_align(pairs_path, prior_rows):
    d = tempfile.mkdtemp()
    prior_path = os.path.join(d, 'prior.tsv')
    write_prior(prior_rows, prior_path)
    a, k = os.path.join(d, 'a.tsv'), os.path.join(d, 'k.tsv')
    subprocess.run([sys.executable, TOOL, 'align', pairs_path, a, k,
                     '--code-prefix', '@', '--clear-consumes', '--prior', prior_path],
                    check=True, capture_output=True)
    with open(k) as f:
        return {r['value']: r for r in csv.DictReader(f, delimiter='\t')}


def masked_recovery(pairs_path):
    """For each n>=5 code, mask it from the prior, align, check recovered value vs truth."""
    rows = []
    for masked in mask_codes:
        code, truth = masked['code'], masked['value']
        prior_rows = [r for r in mask_codes if r['code'] != code] + \
                     [r for r in key_rows if int(r['n_occurrences']) < 5]
        out_key = run_align(pairs_path, prior_rows)
        got = out_key.get(code.rstrip('±'))
        recovered = got['meaning'] if got else None
        rows.append({'code': code, 'truth': truth, 'recovered': recovered or '(unaligned)',
                      'match': recovered == truth, 'n': got['n'] if got else 0,
                      'agree': got['agree'] if got else 0})
    return rows


def shuffled_pairs(seed):
    rows = list(csv.DictReader(open(f'{ROOT}/align/pairs.tsv'), delimiter='\t'))
    rnd = random.Random(seed)
    glosses = [r['plain_raw'] for r in rows]
    perm = glosses[:]
    while True:
        rnd.shuffle(perm)
        if all(a != b for a, b in zip(glosses, perm)):
            break
    for r, g in zip(rows, perm):
        r['plain_raw'] = g
        r['plain_line'] = r['plain_line'] + '#shuf'
    d = tempfile.mkdtemp()
    p = os.path.join(d, 'pairs_shuf.tsv')
    with open(p, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['plain_line', 'plain_raw', 'cipher_line', 'cipher_raw'])
        for r in rows:
            w.writerow([r['plain_line'], r['plain_raw'], r['cipher_line'], r['cipher_raw']])
    return p


print()
print('=== real gloss: known-answer masked-code recovery ===')
real_rows = masked_recovery(f'{ROOT}/align/pairs.tsv')
for r in real_rows:
    print(f"  {r['code']:4s} truth={r['truth']} recovered={r['recovered']:10s} "
          f"{'MATCH' if r['match'] else 'MISS '} n={r['n']} agree={r['agree']}")
real_rate = sum(r['match'] for r in real_rows) / len(real_rows)
print(f'real recovery rate: {sum(r["match"] for r in real_rows)}/{len(real_rows)} = {real_rate:.3f}')

print()
print('=== shuffled-gloss control (3 seeds) ===')
shuf_rates = []
for seed in (1, 2, 3):
    sp = shuffled_pairs(seed)
    rows = masked_recovery(sp)
    rate = sum(r['match'] for r in rows) / len(rows)
    shuf_rates.append(rate)
    print(f'seed {seed}: {sum(r["match"] for r in rows)}/{len(rows)} = {rate:.3f}')
shuf_mean = sum(shuf_rates) / len(shuf_rates)
print(f'shuffled mean: {shuf_mean:.3f} (range {min(shuf_rates):.3f}-{max(shuf_rates):.3f})')

print()
margin = real_rate - shuf_mean
gate_met = real_rate >= 0.80 and margin >= 0.30
print(f'GATE: real {real_rate:.3f} vs shuffled mean {shuf_mean:.3f}, margin {margin:.3f} '
      f'(need >=0.80 real AND >=0.30 margin) -> {"MET" if gate_met else "NOT MET"}')

with open(f'{ROOT}/align/gate_result.tsv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f, delimiter='\t', lineterminator='\n')
    w.writerow(['code', 'truth', 'recovered', 'match', 'n', 'agree'])
    for r in real_rows:
        w.writerow([r['code'], r['truth'], r['recovered'], r['match'], r['n'], r['agree']])
    w.writerow([])
    w.writerow(['summary', 'real_rate', real_rate, 'shuffled_mean', shuf_mean, 'margin', margin, 'gate', gate_met])

print()
print('exit code:', 0 if gate_met else 3)
sys.exit(0 if gate_met else 3)
