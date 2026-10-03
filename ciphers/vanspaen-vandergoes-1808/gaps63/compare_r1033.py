#!/usr/bin/env python3
"""GAPS63 (3 Oct 2026): compare DECODE R1033 (NA 1.02.13 inv. 226, Six van Oterleek, St Petersburg 1808-10,
decrypted, code "op basis van het cijfer van Van Hogendorp") with R1941 = NA 2.01.08 inv. 281 No 4 + No 6
(gaps36/reconciled.tsv, image reading).

R1033's DECODE documents need a login and are not redistributed here: pass the directory holding
DOC_1033_2026-Jan-09-15-33-07_38295.txt (annotated decode, word[group+mark]) and ..._54844.txt (cipher transcription).
Writes gaps63/compare.tsv (statistics only).

Statistic and control (rule 3): the share of No 4/No 6 groups that are attested code values in R1033 (base number,
mark ignored), and the share whose R1033 value reads as a plausible running text. Control that can differ: the same
statistic on random group sets drawn uniformly from No 4's own range and size (1000 draws, seed 63) -- coverage
depends on which numbers occur, which the random set changes; also No 4's groups <=999 only.
"""
import re, sys, random, collections, os
d = sys.argv[1]
here = os.path.dirname(os.path.abspath(__file__))
ann = open(os.path.join(d, 'DOC_1033_2026-Jan-09-15-33-07_38295.txt'), encoding='utf-8').read()
ct = open(os.path.join(d, 'DOC_1033_2026-Jan-09-15-20-12_54844.txt'), encoding='utf-8').read()
pairs = re.findall(r'([^\[\]\s][^\[\]]*?)?\[(NULL:)?(\d+)([+"~^:=\']?)-?\]', ann)
vals = collections.defaultdict(collections.Counter)    # (num, mark) -> words
base = collections.defaultdict(collections.Counter)    # num -> words
for w, null, n, m in pairs:
    w = 'NULL' if null else (w or '').strip()
    n = int(n); vals[(n, m)][w] += 1; base[n][w] += 1
ctg = [(int(n), m) for n, m in re.findall(r'(\d+)([+"~^:=\']?)', re.sub(r'message_\d+\.txt', '', ct))]
marks = collections.Counter(m or '(none)' for n, m in ctg)
nums = [n for n, m in ctg]
# No 4 / No 6 groups
rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(here, '..', 'gaps36', 'reconciled.tsv'), encoding='utf-8')
        if l.strip() and not l.startswith('#')]
tg = []
for r in rows:
    for g in r[1].split():
        g = re.sub(r'\[.*?\]', '', g).rstrip('-:?')
        if g.isdigit(): tg.append(int(g))
lo, hi = min(tg), max(tg)
cov = lambda gs: sum(1 for g in gs if g in base) / len(gs)
real = cov(tg)
rng = random.Random(63)
draws = [cov([rng.randint(lo, hi) for _ in tg]) for _ in range(1000)]
ge = sum(1 for x in draws if x >= real)
tl = [g for g in tg if g <= 999]
real_l = cov(tl)
draws_l = [cov([rng.randint(lo, 999) for _ in tl]) for _ in range(1000)]
ge_l = sum(1 for x in draws_l if x >= real_l)
# R1033 unmarked-only values (the only ones an unmarked group could take)
unm = {n: c for (n, m), c in vals.items() if m == ''}
dec = [(g, unm[g].most_common(1)[0][0] if g in unm else ('|'.join(w for w, _ in base[g].most_common(2)) + '*' if g in base else '?'))
       for g in tg]
out = os.path.join(here, 'compare.tsv')
with open(out, 'w', encoding='utf-8') as f:
    w = lambda k, v: f.write(f'{k}\t{v}\n')
    w('r1033_cipher_groups', len(ctg)); w('r1033_range', f'{min(nums)}-{max(nums)}')
    w('r1033_groups_over_999', sum(1 for n in nums if n > 999))
    w('r1033_mark_counts', ' '.join(f'{k}:{v}' for k, v in marks.most_common()))
    w('r1033_share_unmarked', round(marks['(none)'] / len(ctg), 3))
    w('r1033_pairs_annotated', len(pairs)); w('r1033_distinct_value_mark', len(vals)); w('r1033_distinct_numbers', len(base))
    w('r1941_groups', len(tg)); w('r1941_range', f'{lo}-{hi}'); w('r1941_groups_over_999', sum(1 for g in tg if g > 999))
    w('r1941_distinct', len(set(tg)))
    w('coverage_target', round(real, 3)); w('coverage_control_mean', round(sum(draws) / len(draws), 3))
    w('coverage_control_p95', round(sorted(draws)[949], 3)); w('coverage_control_ge_target', f'{ge}/1000')
    w('coverage_target_le999', round(real_l, 3)); w('coverage_control_le999_mean', round(sum(draws_l) / len(draws_l), 3))
    w('coverage_control_le999_p95', round(sorted(draws_l)[949], 3)); w('coverage_control_le999_ge_target', f'{ge_l}/1000')
    w('decode_first_60_under_r1033', ' '.join(f'{g}={v}' for g, v in dec[:60]))
print(open(out, encoding='utf-8').read())
