#!/usr/bin/env python3
"""Matched control (CLAUDE.md rule 3) for the interlinear alignment used on the
Montagu letter of 20 April - 29 May 1656 (montagu_1656-05-29_pairs.tsv).

Builds a synthetic Montagu-style nomenclator with the structure the real letter
shows once aligned: single letters on 1-99 with the same number of homophones per
letter (e 8, t/o/r/u 5, ...), 169 alphabetical word codes on 100-622, codes
making up about 39% of cipher groups. Enciphers clear 1650s English from the same
printed volume (Thurloe vol. 5, djvu lines 6076-6400, the Hague intelligence
letters that follow Montagu's), cut into 89 lines of about 18.5 cipher groups,
then prints a synthetic interlinear with the print's OCR faults at the rates seen
in the real pairs: long s read as f, l as 1, adjacent letters and words run
together or split, about 4% of cipher groups OCR-mangled, a few merged groups and
nulls. Runs tools/interlinear_align.py on it and scores every token against the
truth. Deterministic (seed 1656).

    python3 control_interlinear.py            # prints the score table
    python3 control_interlinear.py --check    # exits non-zero if control_result.tsv is stale
"""
import random
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import interlinear_align as ia  # noqa: E402

CLEAR_SOURCE = HERE / 'control_clear_vol5.txt'   # committed copy of the clear text
HOMOPHONES = {'e': 8, 't': 5, 'o': 5, 'r': 5, 'u': 5, 's': 5, 'l': 4, 'a': 4, 'i': 4,
              'd': 4, 'y': 4, 'n': 4, 'p': 3, 'b': 3, 'c': 3, 'm': 3, 'g': 3, 'h': 2,
              'w': 2, 'f': 1, 'q': 1, 'k': 1, 'x': 1, 'j': 1}
NCODES, LINES, PER_LINE = 169, 89, 18.5
DOUBTFUL_RATE, MERGE_RATE, NULL_RATE = 0.04, 0.006, 0.005
BAD = {'1': 'lI', '0': 'o°', '5': 'S$', '2': 'Z', '9': 'g', '7': 'y', '4': '^'}


def build(rng):
    words = re.findall(r'[a-z]+', CLEAR_SOURCE.read_text(encoding='utf-8').lower().replace('ſ', 's'))
    freq = Counter(words)
    vocab = sorted(w for w, _ in freq.most_common(NCODES))
    codes = sorted(rng.sample(range(100, 623), NCODES))
    code_of = dict(zip(vocab, codes))
    pool = [n for n in range(1, 100)]
    rng.shuffle(pool)
    letter_vals, k = {}, 0
    for ch, h in sorted(HOMOPHONES.items()):
        letter_vals[ch] = pool[k:k + h]
        k += h
    truth_key = {v: w for w, v in code_of.items()}
    for ch, vs in letter_vals.items():
        for v in vs:
            truth_key[v] = ch
    return words, code_of, letter_vals, truth_key


def encipher(words, code_of, letter_vals, rng):
    """-> list of (value, plain chunk, word index)"""
    out = []
    for wi, w in enumerate(words):
        if w in code_of and rng.random() < 0.8:
            out.append((code_of[w], w, wi))
        else:
            for ch in w:
                if ch in letter_vals:
                    out.append((rng.choice(letter_vals[ch]), ch, wi))
    return out


def ocr_plain(s, rng):
    s = ''.join('f' if c == 's' and rng.random() < 0.6 else c for c in s)
    s = ''.join('1' if c == 'l' and rng.random() < 0.05 else c for c in s)
    return ''.join(rng.choice('abcdefghilmnorstu') if rng.random() < 0.02 else c for c in s)


def ocr_num(v, rng):
    s = str(v)
    if rng.random() < DOUBTFUL_RATE:
        i = rng.randrange(len(s))
        if s[i] in BAD:
            s = s[:i] + rng.choice(BAD[s[i]]) + s[i + 1:]
        else:
            s = s + '*'
    return s


def make_pairs(stream, rng):
    pairs, truth = [], []
    total = int(LINES * PER_LINE)
    stream = stream[:total]
    size = len(stream) // LINES
    for li in range(LINES):
        seg = stream[li * size:(li + 1) * size] if li < LINES - 1 else stream[li * size:]
        # plain line: letters of a word spelled out are spaced unless OCR runs them together;
        # a code word is one segment; neighbouring segments sometimes run together
        segs, prev_wi = [], None
        for v, ch, wi in seg:
            if v >= 100 or wi != prev_wi or rng.random() < 0.35:
                segs.append(ch)
            else:
                segs[-1] += ch
            prev_wi = wi
        merged = []
        for sgm in segs:
            if merged and rng.random() < 0.06:
                merged[-1] += sgm
            else:
                merged.append(sgm)
        plain = '  '.join(ocr_plain(x, rng) for x in merged)
        toks, tt = [], []
        for v, ch, wi in seg:
            if rng.random() < NULL_RATE:
                toks.append(str(rng.randrange(1, 100)))
                tt.append(None)
            if toks and rng.random() < MERGE_RATE:
                toks[-1] += str(v)
                tt[-1] = None
                continue
            toks.append(ocr_num(v, rng))
            tt.append((v, ch))
        pairs.append({'plain_line': str(2 * li), 'plain_raw': plain,
                      'cipher_line': str(2 * li + 1), 'cipher_raw': '  '.join(toks)})
        truth.append(tt)
    return pairs, truth


def score():
    rng = random.Random(1656)
    words, code_of, letter_vals, truth_key = build(rng)
    stream = encipher(words, code_of, letter_vals, rng)
    pairs, truth = make_pairs(stream, rng)
    prepared, results, counts, shown = ia.run_align(pairs)
    rows = ia.token_rows(prepared, results, counts, shown)
    flat = [t for tt in truth for t in tt]
    assert len(flat) == len(rows)
    by = Counter()
    ok = Counter()
    for r, t in zip(rows, flat):
        st = r[7].split(':')[0]
        by[st] += 1
        if t is None:
            ok[st] += int(st in ('doubtful', 'null-or-unaligned', 'conflict', 'clear'))
            continue
        got = r[5] and int(r[5]) == t[0] or r[4] and int(r[4]) == t[0]
        ok[st] += int(bool(got) and ia.fold(r[6]) == ia.fold(t[1]))
    # key accuracy: value -> majority meaning vs truth
    kv = [(v, ia.top_of(c)[0]) for v, c in counts.items()]
    key_ok = sum(1 for v, m in kv if v in truth_key and ia.fold(truth_key[v]) == m)
    lines = ['status\ttokens\tcorrect\tpct']
    for st in sorted(by):
        lines.append('%s\t%d\t%d\t%.1f' % (st, by[st], ok[st], 100.0 * ok[st] / by[st]))
    cgrade = sum(by[s] for s in ('agrees', 'single-segment'))
    cok = sum(ok[s] for s in ('agrees', 'single-segment'))
    lines.append('C-graded(agrees+single-segment)\t%d\t%d\t%.1f' % (cgrade, cok, 100.0 * cok / cgrade))
    lines.append('key values recovered\t%d\t%d\t%.1f' % (len(kv), key_ok, 100.0 * key_ok / len(kv)))
    lines.append('total tokens\t%d\t\t' % len(rows))
    return '\n'.join(lines) + '\n'


def main():
    out = score()
    res = HERE / 'control_result.tsv'
    if '--check' in sys.argv:
        if not res.exists() or res.read_text(encoding='utf-8') != out:
            print('STALE: control_result.tsv', file=sys.stderr)
            sys.exit(1)
    else:
        res.write_text(out, encoding='utf-8')
    sys.stdout.write(out)


if __name__ == '__main__':
    main()
