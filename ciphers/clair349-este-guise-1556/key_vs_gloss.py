#!/usr/bin/env python3
"""Key-vs-gloss consistency check for clair349-este-guise-1556 (ZX-TR349C, step 4).

For every aligned token where passE.tsv and passF.tsv independently wrote the SAME non-blank
interlinear gloss letter/word, compare that gloss against key_alpha.tsv/key_nomen.tsv's value(s)
for the token's own code (the majority/consensus sign at that column, same selection rule
tools/reconcile_passes.py uses for ciphertext_draft.tsv). This is a check on both the key and the
gloss transcription, not a decode: it never resolves a key homograph and never writes a reading.

Usage: python3 key_vs_gloss.py [--out key_vs_gloss.tsv]
Writes a per-code TSV (code, key_values, n_agreed_gloss_tokens, n_match, n_mismatch, match_share,
example_mismatches) and prints the codes where gloss and key disagree more than once.
"""
import argparse, collections, csv, os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
import reconcile_passes as rp

HERE = os.path.dirname(os.path.abspath(__file__))


def load_key():
    """code -> set of (value, source) the key associates with that code."""
    code_values = collections.defaultdict(set)
    with open(os.path.join(HERE, 'key_alpha.tsv'), encoding='utf-8') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            if row['kind'] == 'void':
                continue
            code_values[row['code']].add((row['letter'], 'key_alpha:' + row['letter']))
    with open(os.path.join(HERE, 'key_nomen.tsv'), encoding='utf-8') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            if not row['code']:
                continue
            code_values[row['code']].add((row['word_or_phrase'], 'key_nomen:' + row['word_or_phrase']))
    return code_values


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--out', default=os.path.join(HERE, 'key_vs_gloss.tsv'))
    ap.add_argument('--pass-a', default=os.path.join(HERE, 'passE.tsv'))
    ap.add_argument('--pass-b', default=os.path.join(HERE, 'passF.tsv'))
    args = ap.parse_args()

    la = argparse.Namespace(split_chars=False, keep_dots=False, keep_plain=False, line_sub=None,
                             halves=False, flag=set(rp.FLAG_CONF))
    Pa, _ = rp.load_pass(args.pass_a, la)
    Pb, _ = rp.load_pass(args.pass_b, la)
    lines = list(Pa) + [l for l in Pb if l not in Pa]
    lines = list(dict.fromkeys(lines))

    code_values = load_key()

    agreed = []  # (line, position, sign, gloss)
    for ln in lines:
        seqs = [Pa.get(ln, []), Pb.get(ln, [])]
        cols = rp.columns(seqs, 'nw')
        pos = 0
        for c in cols:
            signs = [x[0] if x else None for x in c]
            if not any(s is not None for s in signs):
                continue
            pos += 1
            glosses = [x[2] if x else None for x in c]
            non_gap = [g for g in glosses if g is not None]
            if len(non_gap) != len(c) or not all(non_gap) or len(set(non_gap)) != 1:
                continue  # not every pass wrote the same non-blank gloss here
            present = [s for s in signs if s is not None]
            best = collections.Counter(present).most_common()
            sign = best[0][0] if len(best) == 1 or best[0][1] > best[1][1] else present[0]
            agreed.append((ln, pos, sign, non_gap[0]))

    per_code = collections.defaultdict(lambda: dict(n=0, match=0, mismatch=0, examples=[]))
    for ln, pos, sign, gloss in agreed:
        values = code_values.get(sign, set())
        gl = gloss.strip().lower()
        is_match = any(gl == v.lower() for v, _ in values)
        d = per_code[sign]
        d['n'] += 1
        if is_match:
            d['match'] += 1
        else:
            d['mismatch'] += 1
            if len(d['examples']) < 5:
                d['examples'].append(f'{ln}:{pos} gloss={gloss!r} vs key={sorted(v for v, _ in values) or "(code not in key)"}')

    rows = []
    for code in sorted(per_code, key=lambda c: (-per_code[c]['n'], c)):
        d = per_code[code]
        values = sorted({v for v, _ in code_values.get(code, set())})
        share = d['match'] / d['n'] if d['n'] else 0
        rows.append([code, ','.join(values) or '(not in key)', str(d['n']), str(d['match']), str(d['mismatch']),
                     f'{share:.2f}', '; '.join(d['examples'])])

    with open(args.out, 'w', encoding='utf-8') as f:
        f.write('\t'.join(['code', 'key_values', 'n_agreed_gloss_tokens', 'n_match', 'n_mismatch', 'match_share',
                            'example_mismatches']) + '\n')
        for r in rows:
            f.write('\t'.join(r) + '\n')

    tot_n = sum(d['n'] for d in per_code.values())
    tot_match = sum(d['match'] for d in per_code.values())
    print(f'agreed-gloss tokens: {len(agreed)}; codes seen: {len(per_code)}; '
          f'overall key-vs-gloss match {tot_match}/{tot_n} = {tot_match / tot_n:.1%}' if tot_n else
          f'agreed-gloss tokens: {len(agreed)}; no codes to check')
    repeat_mismatch = [c for c, d in per_code.items() if d['mismatch'] > 1]
    if repeat_mismatch:
        print('codes where gloss and key disagree more than once:', ', '.join(sorted(repeat_mismatch)))
    else:
        print('no code disagrees with the key more than once')
    print('wrote', args.out)


if __name__ == '__main__':
    main()
