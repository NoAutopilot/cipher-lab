#!/usr/bin/env python3
"""gloss_align.py -- re-align the leaf's own interlinear gloss to its cipher groups, line by line, with
tools/interlinear_align.py (GAPS2-na-schonenberg-1678-1716, 2 Oct 2026; the Verdict step of NOTES.md
"## Remaining gaps").

Input: ciphertext.tsv (passB's position-by-position (group, gloss letter) rows, reconciled by VX-RD01). For each
glossed line (L01-L14 and L18) the plain line is that line's gloss letters in order and the cipher line is its groups,
each marked as a code ("@89", "@)6", "@[triangle]"). The aligner then re-decides which letter sits over which group
(a group may take no letter, a letter may be skipped), iterating until each code's letter agrees with what the same
code reads elsewhere -- which is what passB's own summary says it could not do by eye on L04, L08, L10, L11, L13, L14
(its cipher-group count and gloss-letter count differ by 1-2 on those lines).

Three runs (same pairs, same tool):
  R0  unseeded
  R1  --prior seeded with key.tsv's grade-C codes only (the pixel-verified and >=75% codes)
  R2  --prior seeded with the C codes plus the five crib-fixed codes 24, 34, 51, 11, 65 (the Verdict line's run)
The tool's own caveat applies: counts for a seeded code are not independent evidence for that code's value. R1 is
therefore the run that decides the crib codes' conflicts (they are not seeded there), and R0 is the run that shows
what the gloss says with no key at all.

Control (CLAUDE.md rule 3): the same R2 (and R0) alignment on the gloss with each line's letters shuffled within the
line (--shuffles N, --seed S). Statistic: the fraction of code tokens whose aligned letter equals the code's own
leaf-wide top letter with at least two occurrences (the tool's status "agrees"), and the number of codes reaching the
folder's C bar (>=2 occurrences, >=75% agreement). Shuffling the letters changes both, so the control can fail.

Writes, beside this script: pairs.tsv, prior_C.tsv, prior_Ccrib.tsv, align_R0.tsv/key_R0.tsv, align_R1.tsv/key_R1.tsv,
align_R2.tsv/key_R2.tsv, moves_R2.tsv (tokens whose aligned letter differs from passB's positional letter),
control.tsv (one row per shuffle) and summary.txt. Nothing fetched.

Usage: python3 ciphers/na-schonenberg-1678-1716/align/gloss_align.py [--shuffles 500] [--seed 1]
"""
import argparse, csv, os, random, statistics, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(TARGET))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import interlinear_align as ia  # noqa: E402

GLOSSED = ['L%02d' % i for i in range(1, 15)] + ['L18']
CRIB_CODES = ['24', '34', '51', '11', '65']
PFX = '@'


def load_ct():
    ct = defaultdict(list)
    with open(os.path.join(TARGET, 'ciphertext.tsv'), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            ct[r['line']].append(r)
    return ct


def load_key():
    with open(os.path.join(TARGET, 'key.tsv'), encoding='utf-8') as f:
        return {r['code']: r for r in csv.DictReader(f, delimiter='\t')}


def letters_of(rows):
    """gloss letters of a line in order; 'en' (L01 pos5, an e with a nasal stroke) is two letters."""
    out = []
    for r in rows:
        g = r['gloss'].strip().lower()
        for ch in g:
            if ch.isalpha():
                out.append(ch)
    return out


def make_pairs(ct, shuffle_rng=None):
    pairs = []
    for ln in GLOSSED:
        rows = ct[ln]
        letters = letters_of(rows)
        if shuffle_rng is not None:
            shuffle_rng.shuffle(letters)
        pairs.append({'plain_line': ln, 'plain_raw': ' '.join(letters), 'cipher_line': ln,
                      'cipher_raw': ' '.join(PFX + r['group'] for r in rows)})
    return pairs


def write_pairs(pairs, path):
    with open(path, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['plain_line', 'plain_raw', 'cipher_line', 'cipher_raw'])
        for p in pairs:
            w.writerow([p['plain_line'], p['plain_raw'], p['cipher_line'], p['cipher_raw']])


def write_prior(key, codes, path):
    with open(path, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['code', 'value'])
        for c in codes:
            w.writerow([c, key[c]['value']])


def stats(rows, counts):
    code_rows = [r for r in rows if r[3] == 'code']
    agrees = sum(1 for r in code_rows if r[7] == 'agrees')
    cbar = 0
    for v, cnt in counts.items():
        n = sum(cnt.values())
        top, topn = ia.top_of(cnt)
        if n >= 2 and topn / n >= 0.75:
            cbar += 1
    return agrees / len(code_rows), cbar, len(code_rows)


def run(pairs, prior_path):
    prior = ia.load_prior(prior_path, 100, code_mode=True) if prior_path else None
    prepared, results, counts, shown = ia.run_align(pairs, prior=prior, code_prefix=PFX)
    rows = ia.token_rows(prepared, results, counts, shown)
    return rows, counts, shown


def write_align(rows, counts, shown, out_align, out_key):
    with open(out_align, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['cipher_line', 'idx', 'raw', 'kind', 'value', 'repair', 'plain_chunk', 'status'])
        w.writerows(rows)
    with open(out_key, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['value', 'meaning', 'n', 'agree', 'others'])
        for v in sorted(counts):
            cnt = counts[v]
            top, topn = ia.top_of(cnt)
            rest = sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))[1:]
            others = ','.join('%s:%d' % (ia.display(shown, v, m), c) for m, c in rest)
            w.writerow([v, ia.display(shown, v, top), sum(cnt.values()), topn, others])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--shuffles', type=int, default=500)
    ap.add_argument('--seed', type=int, default=1)
    a = ap.parse_args()
    ct, key = load_ct(), load_key()
    pairs = make_pairs(ct)
    write_pairs(pairs, os.path.join(HERE, 'pairs.tsv'))
    c_codes = [c for c, r in key.items() if r['grade'] == 'C' and len(r['value']) == 1 and r['value'].isalpha()]
    write_prior(key, c_codes, os.path.join(HERE, 'prior_C.tsv'))
    write_prior(key, c_codes + CRIB_CODES, os.path.join(HERE, 'prior_Ccrib.tsv'))
    out = []
    res = {}
    for tag, prior in (('R0', None), ('R1', 'prior_C.tsv'), ('R2', 'prior_Ccrib.tsv')):
        pp = os.path.join(HERE, prior) if prior else None
        rows, counts, shown = run(pairs, pp)
        write_align(rows, counts, shown, os.path.join(HERE, 'align_%s.tsv' % tag), os.path.join(HERE, 'key_%s.tsv' % tag))
        fr, cbar, ntok = stats(rows, counts)
        st = Counter(r[7].split(':')[0] for r in rows)
        res[tag] = (fr, cbar, ntok, rows, counts)
        out.append('%s prior=%s: code tokens %d, agrees %.3f, codes at C bar (n>=2, >=75%%) %d, statuses %s' %
                   (tag, prior or 'none', ntok, fr, cbar, dict(st)))
    # moves: R2's aligned letter vs passB's positional letter
    moves = []
    for ln in GLOSSED:
        rows_ct = ct[ln]
        al = [r for r in res['R2'][3] if r[0] == ln]
        for r_ct, r_al in zip(rows_ct, al):
            pos_letter = r_ct['gloss'].strip().lower()
            if r_al[6] != pos_letter:
                moves.append([ln, r_ct['pos'], r_ct['group'], pos_letter, r_al[6], r_al[7]])
    with open(os.path.join(HERE, 'moves_R2.tsv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['line', 'pos', 'group', 'passB_letter', 'aligned_letter', 'status'])
        w.writerows(moves)
    out.append('R2 tokens whose aligned letter differs from passB positional letter: %d of %d' % (len(moves), res['R2'][2]))
    # crib codes under R1 (not seeded there) and R0
    for tag in ('R0', 'R1', 'R2'):
        for c in CRIB_CODES:
            occ = [(r[0], r[1], r[6] or '-') for r in res[tag][3] if r[3] == 'code' and r[4] == c]
            out.append('%s code %s (crib %s): %s' % (tag, c, key[c]['value'], ' '.join('%s:%s=%s' % o for o in occ)))
    # control
    rng = random.Random(a.seed)
    ctrl = []
    for tag, prior in (('R2', 'prior_Ccrib.tsv'), ('R0', None)):
        pp = os.path.join(HERE, prior) if prior else None
        for i in range(a.shuffles):
            sp = make_pairs(ct, shuffle_rng=rng)
            rows, counts, shown = run(sp, pp)
            fr, cbar, _ = stats(rows, counts)
            ctrl.append([tag, i, '%.4f' % fr, cbar])
        frs = [float(r[2]) for r in ctrl if r[0] == tag]
        cbs = [r[3] for r in ctrl if r[0] == tag]
        tf, tc = res[tag][0], res[tag][1]
        frs_s = sorted(frs)
        out.append('CONTROL %s within-line shuffled gloss, n=%d seed=%d: agrees mean %.3f p95 %.3f max %.3f, %d at or above target %.3f; '
                   'C-bar codes mean %.1f p95 %d max %d, %d at or above target %d' %
                   (tag, a.shuffles, a.seed, statistics.mean(frs), frs_s[int(0.95 * len(frs_s)) - 1], max(frs),
                    sum(1 for x in frs if x >= tf), tf, statistics.mean(cbs), sorted(cbs)[int(0.95 * len(cbs)) - 1],
                    max(cbs), sum(1 for x in cbs if x >= tc), tc))
    with open(os.path.join(HERE, 'control.tsv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['run', 'shuffle', 'agrees_fraction', 'c_bar_codes'])
        w.writerows(ctrl)
    with open(os.path.join(HERE, 'summary.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    print('\n'.join(out))


if __name__ == '__main__':
    main()
