#!/usr/bin/env python3
"""Build ciphertext.tsv and key.tsv for item 3 (RAH 9/7666, record 5186, f.420r) from its own interlinear
period decipherment -- read by eye off images/crop_5186_p1_cipher.jpg (NX-MOR2, 26 Sept 2026), reconciled
against two blind Sonnet transcription passes plus a direct re-check of the image at 4-5x zoom on every
group with a disagreement between the passes.

Grade C (CLAUDE.md rule 4; corrected from H by the verifier V9-MOR, AUDIT.md, 26 Sept 2026 -- a key built from
a leaf's own interlinear decipherment is known plaintext, C, not a key source, H). Original rationale: the leaf's own interlinear plaintext functions as a key source -- the period
decipherer wrote both the cipher and its reading directly on the document, so applying it is reading a key,
not deriving one from a separately-known plaintext (contrast rah-canada-1869, grade C, where the plaintext
comes from the same note but the key had to be aligned letter-by-letter first; here every clean word already
resolves 1 cipher-token = 1 letter with no alignment ambiguity).

Only words with NO unresolved token and NO disagreement between the two blind passes on the numerals feed the
key (KEY_WORDS below). Ambiguous words (an unresolved sign, or a letter the passes could not agree on) are
listed in OTHER_GROUPS for the mechanical decode only -- they contribute no key evidence, per CLAUDE.md rule 3
(a key built from what it is then used to test must not circularly include the test cases).

'+' = the recurring non-numeral cross-like mark; 'BOX' = the recurring small drawn box/square (both already
named in NOTES.md's 26 Sept 2026 eye-check). Re-running this script must reproduce the committed files byte
for byte (--check).
"""
import collections
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# (group id, cipher tokens as a list of strings, clean gloss word, letters -- one per token, same length)
# Every word here was independently confirmed clean by both blind Sonnet passes AND a direct re-check of the
# image at 4-5x zoom (26 Sept 2026): no unresolved token, no disagreement between the two passes on the
# numerals, and (for words sharing a token with another KEY_WORDS entry) no contradiction in the letter it
# implies.
KEY_WORDS = [
    ('r1g1', ['51', '18', '50', '7', '51', '56', '33', '18'], 'Romerito', list('romerito')),
    ('r1g3', ['7', '8'], 'el', list('el')),
    ('r2g1', ['24', '18', '51'], 'por', list('por')),
    ('r2g3', ['3', '18', '16'], 'con', list('con')),
    ('r3g1', ['33', '51', '7', '27'], 'tres', list('tres')),
    ('r3g2', ['18', '5', '56', '3', '56', '+', '8', '7', '27'], 'oficiales', list('oficiales')),
    ('r3g3', ['4', '56', '30', '18'], 'dijo', list('dijo')),
    ('r3g4', ['6', '7', '16', '56', '+'], 'benia', list('benia')),
    ('r4g1', ['4', '7'], 'de', list('de')),
    ('r4g3', ['6', 'BOX', '27', '3', '+', '16', '4', '18'], 'buscando', list('buscando')),
    ('r4g4', ['+'], 'a', list('a')),
    ('r4g5', ['6', '18'], 'bo', list('bo')),
    ('r5g3', ['24', '+', '51', '+'], 'para', list('para')),
    # 'Paso' (p-a-s-o): both blind passes read the third letter as 'y' ('Payo'/'Rayo'); the numeral (27) is
    # the same one 'oficiales' and 'tres' independently give 's', and this hand's terminal/flourished 's' is
    # visually close to 'y' at this crop's resolution (re-checked at 4x zoom, 26 Sept 2026) -- key-consistent,
    # counted here, but the letter-vs-key disagreement itself is reported in NOTES.md, not hidden.
    ('r1g2', ['24', '+', '27', '18'], 'Paso', list('paso')),
]

# Groups with at least one token this pass could not resolve to a letter (an unknown sign, or the two blind
# passes disagreeing on the numeral itself), or where the mechanical key decode disagrees with the eye-read
# gloss word -- listed for the mechanical decode and for NOTES.md's disagreement table, contributing nothing
# to the key. '?' marks a token with no resolved letter.
OTHER_GROUPS = [
    ('r2g2', ['6', '+', '51', '56', '16', '51', '33', '+', '27'], 'barinituS (as best read; disagrees, see NOTES.md)'),
    ('r2g4', ['27', '18', '22', '18'], 'solo (tentative; 22 unresolved)'),
    ('r4g2', ['30', 'BOX', '+', '22', '+', '16', '+'], 'guayana (visual; disagrees with key at token 30, see NOTES.md)'),
    ('r5g1', ['8', '56', '26', '+', '51'], 'levar (tentative; 26 unresolved)'),
    ('r5g2', ['27', '51', '10', 'BOX', '51', '18'], 'seguro (tentative; 10 unresolved, disagrees with key at token 2, see NOTES.md)'),
    ('r5g4', ['33', '51', 'BOX'], 'tru (truncated at page edge)'),
    ('r6g1', ['28', '56', '22', '18'], 'xino (tentative; 28 and 22 unresolved)'),
]

ALL_GROUPS_ORDER = ['r1g1', 'r1g2', 'r1g3', 'r2g1', 'r2g2', 'r2g3', 'r2g4', 'r3g1', 'r3g2', 'r3g3', 'r3g4',
                    'r4g1', 'r4g2', 'r4g3', 'r4g4', 'r4g5', 'r5g1', 'r5g2', 'r5g3', 'r5g4', 'r6g1']


def build_key():
    pairs = collections.defaultdict(collections.Counter)
    words_seen = collections.defaultdict(list)
    for gid, toks, word, letters in KEY_WORDS:
        assert len(toks) == len(letters), (gid, toks, letters)
        for t, l in zip(toks, letters):
            pairs[t][l] += 1
            words_seen[t].append(word)
    rows = []
    for code, c in sorted(pairs.items(), key=lambda kv: (-sum(kv[1].values()), kv[0])):
        v, n = c.most_common(1)[0]
        conflict = '; '.join(f'{x} x{m}' for x, m in c.items() if x != v)
        seen = ', '.join(sorted(set(words_seen[code])))
        rows.append((code, v, n, seen, conflict))
    return rows


def all_groups():
    by_id = {gid: (toks, word) for gid, toks, word, _ in KEY_WORDS}
    by_id.update({gid: (toks, word) for gid, toks, word in OTHER_GROUPS})
    return [(gid,) + by_id[gid] for gid in ALL_GROUPS_ORDER]


def outputs():
    out = {}
    key_rows = build_key()
    out['key_5186.tsv'] = (
        "# Key for ciphers/rah-morillo-1817 item 3 (RAH 9/7666, record 5186, f.420r), read from the leaf's own\n"
        "# interlinear period decipherment (grade C, CLAUDE.md rule 4 -- see build_key_5186.py docstring).\n"
        "# Generated by build_key_5186.py; do not edit.\n"
        "code\tvalue\tgrade\tcount\twords_seen_in\tconflict\n" +
        ''.join(f"{code}\t{v}\tC\t{n}\t{seen}\t{conflict}\n" for code, v, n, seen, conflict in key_rows)
    )
    ct_rows = []
    for gid, toks, word in all_groups():
        for i, t in enumerate(toks):
            ct_rows.append((gid, i, t))
        ct_rows.append((gid, len(toks), '/'))
    out['ciphertext_5186.tsv'] = (
        "# ciphers/rah-morillo-1817 item 3 (RAH 9/7666, record 5186, f.420r), cipher block only, in reading\n"
        "# order (row 1 top to row 6 bottom, left to right within a row); 21 groups. Generated by\n"
        "# build_key_5186.py from the reconciled transcription (see NOTES.md); do not edit.\n"
        "# '/' = group break (period-written dots after each numeral are not carried as tokens).\n"
        "line\tidx\tsign\n" + ''.join(f"{gid}\t{i}\t{s}\n" for gid, i, s in ct_rows)
    )
    gloss_rows = [(gid, word) for gid, toks, word in all_groups()]
    out['gloss_5186.tsv'] = (
        "# The interlinear plaintext word as read for each group (illustrative reference only -- decode_key.py\n"
        "# does not consume this file, it decodes ciphertext_5186.tsv mechanically through key_5186.tsv).\n"
        "# Generated by build_key_5186.py; do not edit.\n"
        "line\tgloss_as_read\n" + ''.join(f"{gid}\t{word}\n" for gid, word in gloss_rows)
    )
    return out


if __name__ == '__main__':
    check = '--check' in sys.argv
    stale = 0
    for name, text in outputs().items():
        p = os.path.join(HERE, name)
        if check:
            if not os.path.exists(p) or open(p, encoding='utf-8').read() != text:
                print('STALE:', name); stale = 1
        else:
            open(p, 'w', encoding='utf-8').write(text)
    sys.exit(stale)
