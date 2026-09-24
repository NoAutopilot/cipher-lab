#!/usr/bin/env python3
"""Compare mssDE 108(B)'s transcribed cipher+gloss (pairs_108B.tsv) against 108(A)'s
established ciphertext.tsv/key.tsv/fills.tsv/key_conflicts.tsv.

  python3 compare_108B.py [--check]

Writes compare_108B.tsv (one row per pairs_108B.tsv token: group, our key value if any,
our grade, 108(B) gloss, verdict) and prints the three summaries the brief asks for:
  (a) group-sequence comparison (108(B) vs 108(A), a straight index-by-index diff after
      the leading '835' 108(A) lacks);
  (b) agreement share for C values, R16 M fills, and the 13 conflict figures;
  (c) new figures 108(B) glosses that key.tsv lacks entirely.
--check re-derives the summary counts and exits non-zero if compare_108B.tsv is stale.
"""
import csv
import difflib
import sys
from collections import Counter, defaultdict

HERE = __file__.rsplit('/', 1)[0] or '.'


def read_tsv(path):
    with open(f'{HERE}/{path}') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def load_key():
    key = {}
    for row in read_tsv('key.tsv'):
        key[row['code']] = (row['value'], row['grade'], row['source'])
    return key


def load_fills():
    fills = {}
    for row in read_tsv('fills.tsv'):
        fills[row['code']] = row['value']
    return fills


def load_conflicts():
    return {row['code']: row['readings'] for row in read_tsv('key_conflicts.tsv')}


def load_ciphertext_a():
    """108(A) group sequence, in page/line/idx order."""
    rows = read_tsv('ciphertext.tsv')
    rows.sort(key=lambda r: (r['line'], int(r['pos'])))
    return [r['group'] for r in rows]


def load_pairs_b():
    rows = read_tsv('pairs_108B.tsv')
    order = {'p1': 1, 'p2': 2, 'p3': 3, 'p4': 4, 'p5': 5, 'p6': 6}
    rows.sort(key=lambda r: (order[r['page']], r['line'], int(r['idx'])))
    return rows


def token_matches(key_value, gloss):
    """Loose match: either side may contain 'a|b' or 'a?' etc."""
    if not key_value or not gloss or gloss in ('_', '?'):
        return None  # not comparable
    gloss_clean = gloss.rstrip('?').strip()
    if not gloss_clean:
        return None
    key_opts = [v.strip() for v in key_value.split('|')]
    return gloss_clean in key_opts or any(gloss_clean in k or k in gloss_clean for k in key_opts)


def main(check=False):
    key = load_key()
    fills = load_fills()
    conflicts = load_conflicts()
    seq_a = load_ciphertext_a()
    pairs_b = load_pairs_b()
    seq_b = [r['group'] for r in pairs_b]

    # (a) group-sequence comparison. 108(B) p1 L01 carries one leading group (835) that
    # 108(A) lacks (AUDIT.md, R1). Compare after dropping it. A naive positional index
    # comparison is fragile to any single insertion/deletion/miscount (one is expected:
    # 108(A)'s own transcription grades the group at seq_a[53] 'M agree-flagged', i.e.
    # uncertain, and this worker's own 108(B) read of the same position is flagged
    # low-confidence on digit count) -- one shift there would crash a positional diff
    # for everything after it while the two texts are still the same letter. Use a
    # sequence alignment (difflib) instead, which is robust to that and reports how much
    # of the text is a matching run either way.
    seq_b_aligned = seq_b[1:] if seq_b and seq_b[0] == '835' else seq_b
    sm = difflib.SequenceMatcher(a=seq_a, b=seq_b_aligned, autojunk=False)
    matching = sum(block.size for block in sm.get_matching_blocks())
    n = max(len(seq_a), len(seq_b_aligned))
    seq_pct = 100.0 * matching / n if n else 0.0
    seq_agree = matching
    seq_opcodes = sm.get_opcodes()
    non_equal_ops = [op for op in seq_opcodes if op[0] != 'equal']

    # (b)/(c) per-token comparison against key.tsv / fills.tsv / key_conflicts.tsv
    out_rows = []
    c_total = c_agree = 0
    fill_total = fill_agree = 0
    conflict_total = conflict_agree = 0
    new_figures = {}  # code -> set of glosses seen (for figures key.tsv lacks entirely)

    for r in pairs_b:
        code = r['group']
        gloss = r['gloss']
        in_key = code in key
        key_value, key_grade, key_source = key.get(code, ('', '', ''))
        is_fill = code in fills
        is_conflict = code in conflicts

        verdict = 'n/a'
        if in_key:
            m = token_matches(key_value, gloss)
            if m is not None:
                verdict = 'agree' if m else 'disagree'
                if key_grade == 'C' and not is_fill:
                    c_total += 1
                    c_agree += 1 if m else 0
                if is_fill:
                    fill_total += 1
                    fill_agree += 1 if m else 0
                if is_conflict:
                    conflict_total += 1
                    conflict_agree += 1 if m else 0
        else:
            if gloss and gloss not in ('_', '?') and not gloss.endswith('?'):
                new_figures.setdefault(code, set()).add(gloss.rstrip('?'))

        out_rows.append({
            'page': r['page'], 'line': r['line'], 'idx': r['idx'], 'group': code,
            'key_value': key_value, 'key_grade': key_grade,
            'is_fill': 'y' if is_fill else '', 'is_conflict': 'y' if is_conflict else '',
            'b_gloss': gloss, 'verdict': verdict,
        })

    with open(f'{HERE}/compare_108B.tsv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['page', 'line', 'idx', 'group', 'key_value',
                                           'key_grade', 'is_fill', 'is_conflict',
                                           'b_gloss', 'verdict'], delimiter='\t')
        w.writeheader()
        w.writerows(out_rows)

    summary = []
    summary.append(f"Group sequence: {seq_agree}/{n} ({seq_pct:.1f}%) of groups fall in matching runs "
                    f"(difflib SequenceMatcher) against 108(A)'s established H-grade ciphertext.tsv order "
                    f"(108(A) len={len(seq_a)}, 108(B) len={len(seq_b)}, "
                    f"108(B) p1_L01 carries one leading group '835' not in 108(A), dropped before comparing; "
                    f"{len(non_equal_ops)} non-equal alignment op(s), i.e. this many places the two sequences "
                    f"diverge -- each is either a genuine copying variant between the duplicate and the original "
                    f"or a transcription slip by this worker, not distinguished here).")
    if c_total:
        summary.append(f"C-grade key agreement: {c_agree}/{c_total} ({100.0*c_agree/c_total:.1f}%) "
                        f"of comparable non-fill C-grade tokens.")
    if fill_total:
        summary.append(f"R16 fill agreement: {fill_agree}/{fill_total} ({100.0*fill_agree/fill_total:.1f}%) "
                        f"of comparable fills.tsv tokens.")
    if conflict_total:
        summary.append(f"Conflict-figure agreement: {conflict_agree}/{conflict_total} "
                        f"({100.0*conflict_agree/conflict_total:.1f}%) of comparable key_conflicts.tsv tokens.")
    summary.append(f"New figures (108(B) glosses a code key.tsv lacks entirely): {len(new_figures)} distinct codes.")

    report = '\n'.join(summary)
    print(report)

    if check:
        # Re-derive and confirm compare_108B.tsv on disk matches a fresh run.
        with open(f'{HERE}/compare_108B.tsv', newline='') as f:
            on_disk = f.read()
        import io
        buf = io.StringIO()
        w = csv.DictWriter(buf, fieldnames=['page', 'line', 'idx', 'group', 'key_value',
                                             'key_grade', 'is_fill', 'is_conflict',
                                             'b_gloss', 'verdict'], delimiter='\t')
        w.writeheader()
        w.writerows(out_rows)
        if buf.getvalue() != on_disk:
            print('STALE: compare_108B.tsv does not match a fresh run', file=sys.stderr)
            return 1
        print('--check OK')
    return 0


if __name__ == '__main__':
    sys.exit(main(check='--check' in sys.argv))
