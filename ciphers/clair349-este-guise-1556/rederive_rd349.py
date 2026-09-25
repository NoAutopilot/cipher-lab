#!/usr/bin/env python3
"""ZX-RD349, 25 Sept 2026: independent, fresh-instance re-derivation of the clair349-este-guise-1556 reading
(CLAUDE.md rule 7). Written without reading build_decode.py's or tools/decode_key.py's output, from the raw
key files and the ciphertext alone, to check the committed reading for a silent bug in the shared pipeline.

Reads key_alpha.tsv and key_nomen.tsv directly (not key_decode.tsv) and applies them to ciphertext.tsv token
by token. A position named in exceptions.tsv takes that row's value exactly (the row states what the value at
that position is; this script does not re-derive the exceptions -- only re-derives the key application, which is
the part rule 7's byte-for-byte pipeline check does not exercise a second time). A code with two different values
in the two key tables (D and L both drawn as digit 5; Q and 'n'aye' both drawn as S32; etc.) and no exceptions
row at that position is left ambiguous as 'a|b', per the rule-7 brief.

Usage: python3 rederive_rd349.py TARGET_DIR, writes rederive_rd349.tsv (line, position, sign, value) in TARGET_DIR.
"""
import csv, os, re, sys


def read_tsv(path):
    with open(path, encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def alpha_value(letter):
    """key_alpha.tsv 'letter' column -> a decoded value, independently of build_decode.py's flat_key()."""
    if letter.startswith('DOUBLES:'):
        pair = letter.split(':', 1)[1]
        pair = re.sub(r'\(.*\)', '', pair)   # strip '(long)'/'(round)' annotations
        pair = pair.rstrip('?')              # strip an unresolved '?' (e.g. 'sc?')
        return pair
    if letter.startswith('NULLES'):
        return 'NULL'
    if letter == 'V':
        return 'u'          # the gloss writes u for V's codes throughout; the key never yields plain 'v'
    return letter.lower()   # A-Z, I -> i, & stays &


def add_code(key, code, value):
    """Merge one (code -> value) mapping into key, combining a real collision as 'a|b' rather than
    letting either row silently overwrite the other (key_alpha's C=9 and DOUBLES:ss(round)=9, for one)."""
    if code in key:
        if value not in key[code].split('|'):
            key[code] = key[code] + '|' + value
    else:
        key[code] = value


def build_key(target):
    key = {}
    for r in read_tsv(os.path.join(target, 'key_alpha.tsv')):
        if r['kind'] == 'void':
            continue
        add_code(key, r['code'], alpha_value(r['letter']))
    for r in read_tsv(os.path.join(target, 'key_nomen.tsv')):
        if r['code'] in ('', '?'):
            continue
        add_code(key, r['code'], r['word_or_phrase'])
    return key


def build_exceptions(target):
    exc = {}
    for r in read_tsv(os.path.join(target, 'exceptions.tsv')):
        exc[(r['line'], r['position'])] = r['value']
    return exc


def main(target):
    key = build_key(target)
    exc = build_exceptions(target)
    ct = read_tsv(os.path.join(target, 'ciphertext.tsv'))
    out = ['line\tposition\tsign\tvalue']
    n_tokens = n_keyed = n_exc = n_ambig = n_unkeyed = 0
    for r in ct:
        sign = r['sign']
        if sign == '|':
            continue
        n_tokens += 1
        ln, pos = r['line'], r['position']
        if (ln, pos) in exc:
            value = exc[(ln, pos)]
            n_exc += 1
        elif sign in key:
            value = key[sign]
            n_keyed += 1
            if '|' in value:
                n_ambig += 1
        else:
            value = '?'
            n_unkeyed += 1
        out.append('\t'.join([ln, pos, sign, value]))
    with open(os.path.join(target, 'rederive_rd349.tsv'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    print('tokens %d: from exceptions.tsv %d, from key directly %d (of which ambiguous a|b %d), unkeyed no rule %d'
          % (n_tokens, n_exc, n_keyed, n_ambig, n_unkeyed))


if __name__ == '__main__':
    main(sys.argv[1])
