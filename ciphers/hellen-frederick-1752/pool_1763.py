"""Write the pooled 1763 cluster as one space-tokenised ciphertext file for tools/family_run.py --cipher.

HEL-T2 (2 Oct 2026, account-4): the spec's `ciphertext` block is a dict of per-record pointers, which
family_run.py cannot read directly ("give --cipher PATH"). This script pools the six 1763 records in
Bourdeau's own audit order (1045,1046,1047,1048,1060,1061), one record per line, keeping only the numeric
tokens (1-4 digits after stripping '_'/'^' transcriber marks, the same rule as pool_stats.py and his
audit_transcription.py); unresolved tokens (any '?' or non 1-4-digit) are dropped, so the stream is the
1234-token pool the spec's test 1 and test 2 describe. Exits non-zero if the counts drift from the spec.

Usage: python3 pool_1763.py            (writes pooled_1763.txt beside this script)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RECORDS_1763 = ['1045', '1046', '1047', '1048', '1060', '1061']
EXPECTED_N = 1234


def numeric_tokens(path):
    out = []
    for seg in path.read_text(encoding='utf-8').split():
        digits = seg.strip().replace('_', '').replace('^', '')
        if re.fullmatch(r'\d{1,4}', digits):
            out.append(str(int(digits)))
    return out


def main():
    lines, n = [], 0
    for r in RECORDS_1763:
        toks = numeric_tokens(ROOT / f'ciphertext_R{r}.txt')
        n += len(toks)
        lines.append(' '.join(toks))
    out = ROOT / 'pooled_1763.txt'
    out.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    k = len({t for l in lines for t in l.split()})
    print(json.dumps({'file': str(out.relative_to(ROOT.parent.parent)), 'records': RECORDS_1763,
                      'N': n, 'K': k, 'per_record': [len(l.split()) for l in lines]}))
    if n != EXPECTED_N:
        print(f'N={n} differs from the spec pool N={EXPECTED_N}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
