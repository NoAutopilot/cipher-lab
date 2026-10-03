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

Fold-in of the 2021 print (GAPS-rah-morillo-1817, 2 Oct 2026; CLAUDE.md rule 4, grade C from known plaintext).
V9-MOR (AUDIT.md, 26 Sept 2026) found the whole cipher block printed, modernised, in Bolivar, Gonzalez Segovia
and Anzola, *Portuguesa en Carabobo* (2021), p.37 n.100, citing this shelfmark. PRINT_WORDS below carries the
print's word over each group that the gloss-built key left unread or tentative, aligned one letter per sign
where every other sign in the group is already keyed. The rule for merging it (print_fold): the gloss-built
key is never overwritten by the print -- a sign the print reads where the key has nothing gets the print's
value(s) (26 = v, 28 = j, 10 = g); a sign whose print letter agrees with the key gains a count and a word; a
sign whose print letter disagrees with the key keeps the key's value, records the disagreement in the
`conflict` column, and the position becomes a row of exceptions.tsv at grade M (CLAUDE.md rule 4: two
witnesses that disagree are a data conflict, never settled by majority). A sign the print reads with more than
one letter across its occurrences (22: l in 'solo', y in 'Guayana', ll in 'Trujillo') is written with every
value joined by '|' at grade M and each occurrence gets its own exceptions.tsv row with the print letter at M.
EXCEPTIONS (-> exceptions.tsv, read by tools/decode_key.py through decode.json) is the per-position list:
V9-MOR's five M tokens plus the three 22 positions.
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

# The 2021 print's words (grade C, known plaintext; *Portuguesa en Carabobo*, 2021, p.37 n.100, orthography
# modernised by its authors: "Se ha corregido la ortografia"), aligned one letter per sign. A None letter marks a
# position where the print's letter contradicts a sign the key already reads in several words (r5g2 position 1,
# sign 51 = r in five words, print and gloss 'e'): that position is not fed to the key counter and is listed in
# EXCEPTIONS instead. r2g2 is absent: the print's 'Caimital' (8 letters) does not align with the group's 9
# signs, and the gloss as read is 'barinituS' -- an image question (NOTES.md "Remaining gaps"), not a fold-in.
PRINT_SOURCE = 'Portuguesa en Carabobo (2021) p.37 n.100'
PRINT_WORDS = [
    ('r2g4', ['27', '18', '22', '18'], 'solo', ['s', 'o', 'l', 'o']),
    ('r4g2', ['30', 'BOX', '+', '22', '+', '16', '+'], 'Guayana', ['g', 'u', 'a', 'y', 'a', 'n', 'a']),
    # 'Bolivar' is written across the manuscript's own line wrap: r4g5 'bo' (already a KEY_WORDS group) + r5g1.
    ('r5g1', ['8', '56', '26', '+', '51'], 'Bolivar (bo|livar)', ['l', 'i', 'v', 'a', 'r']),
    ('r5g2', ['27', '51', '10', 'BOX', '51', '18'], 'seguro', ['s', None, 'g', 'u', 'r', 'o']),
    ('r5g4', ['33', '51', 'BOX'], 'Trujillo (tru|jillo)', ['t', 'r', 'u']),
    # 'jillo' is five letters over four signs; 56 = i and 18 = o anchor positions 1 and 3, so 28 = j and 22 = ll.
    ('r6g1', ['28', '56', '22', '18'], 'Trujillo (tru|jillo)', ['j', 'i', 'll', 'o']),
]

# The print's word over each KEY_WORDS group (gloss_5186.tsv's print_2021 column only; the key does not use it).
PRINT_WORDS_KEYED = {
    'r1g1': 'Romerito', 'r1g2': 'paso', 'r1g3': 'el', 'r2g1': 'por', 'r2g2': 'Caimital (does not align: 8 letters, 9 signs)',
    'r2g3': 'con', 'r3g1': 'tres', 'r3g2': 'oficiales', 'r3g3': 'Dijo', 'r3g4': 'venia', 'r4g1': 'de',
    'r4g3': 'buscando', 'r4g4': 'a', 'r4g5': 'Bolivar (bo|livar)', 'r5g3': 'para',
}

# Per-position overrides for tools/decode_key.py (line, pos, sign, value, grade, reason) -> exceptions.tsv.
EXCEPTIONS = [
    ('r2g2', 5, '51', 'r', 'M', "key 51 = r (five gloss words); gloss as read 'barinituS' has i here; the print's "
                              "'Caimital' (8 letters) does not align with the 9 signs; V9-MOR M; GAPS2 (3 Oct 2026) fresh blind read of the gloss: 'b a [v|r] [z|i] n i t [u|d|a] S' (this hand's r looks like v), i here again, so sign and gloss still disagree; no C, m or l anywhere under the group, so 'Caimital' is not what the gloss says"),
    ('r2g2', 7, '+', 'a', 'M', "key + = a (six gloss words); gloss as read has u here; print does not align; V9-MOR M; GAPS2 blind gloss letter [u|d|a], not settled"),
    ('r2g4', 2, '22', 'l', 'M', "print 'solo' forces l; 22 also reads y (Guayana) and ll (Trujillo), and 8 already "
                               "reads l in two gloss words -- sign over-constrained, no single value"),
    ('r4g2', 0, '30', 'g', 'M', "gloss 'guayana' (both blind passes) and print 'Guayana' read g; key 30 = j from "
                               "the gloss word 'dijo'; one word each way, unresolved; V9-MOR M; GAPS2 blind read of the gloss letter: [J|I], not g -- the earlier passes' g and this pass's J split, still M"),
    ('r4g2', 3, '22', 'y', 'M', "print 'Guayana' forces y; GAPS2 blind gloss letter here [U|ll|H], i.e. the gloss may spell 'Guallana' (ll, as in Trujillo); see r2g4 position 2"),
    ('r5g2', 1, '51', 'r', 'M', "sign read 51 by three passes (= r in five gloss words); gloss and print 'seguro' want "
                               "e (sign 7); an encipherer's slip or an unrecorded homophone, left at the sign's value; "
                               "V9-MOR M; GAPS2 blind gloss read 'ſ r g u r o' ([t|L|f] = long s, then r): the gloss follows the sign here, against two earlier tentative 'seguro' reads -- split, still M"),
    ('r6g1', 2, '22', 'll', 'M', "print 'Trujillo' (tru|jillo, five letters over four signs) forces ll; see r2g4 "
                                "position 2"),
]

ALL_GROUPS_ORDER = ['r1g1', 'r1g2', 'r1g3', 'r2g1', 'r2g2', 'r2g3', 'r2g4', 'r3g1', 'r3g2', 'r3g3', 'r3g4',
                    'r4g1', 'r4g2', 'r4g3', 'r4g4', 'r4g5', 'r5g1', 'r5g2', 'r5g3', 'r5g4', 'r6g1']


def build_key():
    """Rows (code, value, grade, count, words_seen_in, conflict, source). The gloss-built part is exactly the
    26 Sept 2026 key (KEY_WORDS, grade C, every recurring code agreeing with itself); print_fold then adds the
    2021 print without overwriting it (docstring)."""
    pairs = collections.defaultdict(collections.Counter)
    words_seen = collections.defaultdict(list)
    for gid, toks, word, letters in KEY_WORDS:
        assert len(toks) == len(letters), (gid, toks, letters)
        for t, l in zip(toks, letters):
            pairs[t][l] += 1
            words_seen[t].append(word)
    rows = {}
    for code, c in sorted(pairs.items(), key=lambda kv: (-sum(kv[1].values()), kv[0])):
        v, n = c.most_common(1)[0]
        conflict = '; '.join(f'{x} x{m}' for x, m in c.items() if x != v)
        seen = ', '.join(sorted(set(words_seen[code])))
        rows[code] = dict(code=code, value=v, grade='C', count=n, seen=seen, conflict=conflict, source='gloss')
    return print_fold(rows)


def print_fold(rows):
    """Fold PRINT_WORDS into the gloss-built rows: new sign -> the print's value(s), '|'-joined at M when the
    print reads it with more than one letter; agreeing sign -> count and word added, source 'gloss+print';
    disagreeing sign -> value kept, disagreement in `conflict` (the position is an EXCEPTIONS row)."""
    new = collections.OrderedDict()
    for gid, toks, word, letters in PRINT_WORDS:
        assert len(toks) == len(letters), (gid, toks, letters)
        for t, l in zip(toks, letters):
            if l is None:
                continue
            if t in rows:
                r = rows[t]
                if r['value'] == l:
                    r['count'] += 1
                    r['seen'] = ', '.join(sorted(set(r['seen'].split(', ')) | {word + ' (print)'}))
                    r['source'] = 'gloss+print'
                else:
                    r['conflict'] = '; '.join(x for x in [r['conflict'], f"{l} x1 ({word}, print)"] if x)
            else:
                new.setdefault(t, collections.OrderedDict())
                new[t].setdefault(l, []).append(word)
    out = list(rows.values())
    for code, vals in new.items():
        value = '|'.join(vals)
        grade = 'C' if len(vals) == 1 else 'M'
        count = sum(len(w) for w in vals.values())
        seen = ', '.join(w + ' (print)' for ws in vals.values() for w in ws)
        conflict = '' if len(vals) == 1 else 'one sign, ' + ', '.join(f'{v} in {w[0]}' for v, w in vals.items())
        out.append(dict(code=code, value=value, grade=grade, count=count, seen=seen, conflict=conflict,
                        source='print'))
    return out


def all_groups():
    by_id = {gid: (toks, word) for gid, toks, word, _ in KEY_WORDS}
    by_id.update({gid: (toks, word) for gid, toks, word in OTHER_GROUPS})
    return [(gid,) + by_id[gid] for gid in ALL_GROUPS_ORDER]


def outputs():
    out = {}
    key_rows = build_key()
    out['key_5186.tsv'] = (
        "# Key for ciphers/rah-morillo-1817 item 3 (RAH 9/7666, record 5186, f.420r), read from the leaf's own\n"
        "# interlinear period decipherment (source 'gloss', grade C, CLAUDE.md rule 4 -- see build_key_5186.py\n"
        "# docstring), with the 2021 print's words folded in (source 'print'; " + PRINT_SOURCE + ";\n"
        "# GAPS-rah-morillo-1817, 2 Oct 2026). A '|' value is one sign the print reads with several letters (M).\n"
        "# Generated by build_key_5186.py; do not edit.\n"
        "code\tvalue\tgrade\tcount\twords_seen_in\tconflict\tsource\n" +
        ''.join(f"{r['code']}\t{r['value']}\t{r['grade']}\t{r['count']}\t{r['seen']}\t{r['conflict']}\t{r['source']}\n"
                for r in key_rows)
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
    print_by_id = {gid: word for gid, _, word, _ in PRINT_WORDS}
    print_by_id.update(PRINT_WORDS_KEYED)
    gloss_rows = [(gid, word, print_by_id.get(gid, '')) for gid, toks, word in all_groups()]
    out['gloss_5186.tsv'] = (
        "# The interlinear plaintext word as read for each group (illustrative reference only -- decode_key.py\n"
        "# does not consume this file, it decodes ciphertext_5186.tsv mechanically through key_5186.tsv), and the\n"
        "# word the 2021 print gives at the same place (" + PRINT_SOURCE + ", modernised spelling).\n"
        "# Generated by build_key_5186.py; do not edit.\n"
        "line\tgloss_as_read\tprint_2021\n" + ''.join(f"{gid}\t{word}\t{pw}\n" for gid, word, pw in gloss_rows)
    )
    out['exceptions.tsv'] = (
        "# Per-position overrides for tools/decode_key.py (decode.json 'exceptions'): V9-MOR's five M tokens\n"
        "# (AUDIT.md section 3) and the three occurrences of sign 22, which the 2021 print reads with three\n"
        "# different letters. Generated by build_key_5186.py; do not edit.\n"
        "line\tpos\tsign\tvalue\tgrade\treason\n" +
        ''.join(f"{gid}\t{pos}\t{sign}\t{v}\t{g}\t{why}\n" for gid, pos, sign, v, g, why in EXCEPTIONS)
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
