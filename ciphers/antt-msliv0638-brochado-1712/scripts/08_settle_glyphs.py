"""PX-BROGLYPH step 3: settle the z/7/2 dispute (glyphs.md) and add a grade column.

Resolution (glyphs.md): every token currently read 'z' -- whether disputed (z<->7 or 7<->z, 58 positions) or
already agreed by both passes (30 positions) -- is one recurring glyph, a period "barred 7", settled to
token '7'; the crop check found agreed-z instances are the identical shape to the disputed ones, so pass
agreement there was two passes sharing one misreading, not evidence it was right (CLAUDE.md rule 2). Every
position disputed 2<->7 (29 positions) is pass B misreading an unrelated, unambiguous loop-shaped '2'; pass
A's '2' stands (already-agreed '2' positions were never disputed and are untouched). Grade H where this job
cropped and viewed the actual leaf image (9 of the ~12 leaves carrying a z/7/2 dispute or an agreed-z
instance: m0280, m0281, m0282, m0289, m0290, m0291, m0292, m0293, m0294); grade M where a position is still
disputed after this pass (the 96 other replace pairs, and the insert/delete/extra-b structural
disagreements, none crop-checked this job) or where a z or z/7/2-disputed token falls on a leaf this job did
not individually re-view (m0283, m0286, m0287, m0288 -- resolved by the same rule, since every leaf checked
showed the identical shape with zero counterexamples, but not itself crop-confirmed).

Rewrites ciphertext_appendix.tsv (token column gets the resolved value, a grade column is added) and
plaintext_appendix.tsv (cipher_line's dot-separated pieces are rewritten to match, using the OLD token
stream to re-segment the line exactly as 01_segment.py does, so the two files stay in the sync 01_segment.py
requires; an entry-level grade column is added, H only if every one of the entry's tokens is H).
"""
import csv

ROOT = '/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712'

CHECKED_LEAVES = {'m0280', 'm0281', 'm0282', 'm0289', 'm0290', 'm0291', 'm0292', 'm0293', 'm0294'}

old_rows = list(csv.DictReader(open(f'{ROOT}/ciphertext_appendix.tsv'), delimiter='\t'))
plain_rows = list(csv.DictReader(open(f'{ROOT}/plaintext_appendix.tsv'), delimiter='\t'))

# disagreements.tsv has \r\n line endings (07_reconcile.py's csv.writer); csv module handles that natively.
disagreements = list(csv.DictReader(open(f'{ROOT}/disagreements.tsv'), delimiter='\t'))
disputed_kind = {}
for d in disagreements:
    key = (d['leaf'], d['entry_label'], d['a_position'])
    disputed_kind[key] = (d['a_token'], d['b_token'], d['kind'])

Z7 = {('z', '7'), ('7', 'z')}


def resolve(leaf, entry, pos, tok):
    key = (leaf, entry, pos)
    if key not in disputed_kind:
        # Both passes already agreed -- but glyphs.md's crop check found every AGREED 'z' it viewed (30
        # instances, on 4 of these 5 leaves) is the identical crossbar shape as the disputed z/7 cases, not
        # a real letter z (see glyphs.md "Genuine `2` is a different..." / the m0280 Carta13 pos29/32 and
        # m0281 Carta15 pos32 controls). Passes agreeing on a misreading is still a misreading (CLAUDE.md
        # rule 2, image over transcription): recode it too, graded by the same per-leaf check as the
        # disputed cases, not left at H on the strength of an agreement this pass has shown to be wrong.
        if tok == 'z':
            return '7', ('H' if leaf in CHECKED_LEAVES else 'M')
        return tok, 'H'
    a, b, kind = disputed_kind[key]
    if kind != 'replace':
        return tok, 'M'  # insert/delete/extra-b: structural, not a single-token call; not settled this pass
    if (a, b) in Z7:
        return '7', ('H' if leaf in CHECKED_LEAVES else 'M')
    if (a, b) == ('2', '7'):
        return '2', ('H' if leaf in CHECKED_LEAVES else 'M')  # pass A's genuine loop-2 stands
    return tok, 'M'  # everything else: still disputed, not settled this pass

new_rows = []
old_token_by_key = {}
for r in old_rows:
    old_token_by_key[(r['leaf'], r['entry_label'], r['position'])] = r['token']
    new_tok, grade = resolve(r['leaf'], r['entry_label'], r['position'], r['token'])
    new_type = 'num' if new_tok.rstrip('±').isdigit() else r['token_type']
    new_rows.append({**r, 'token': new_tok, 'token_type': new_type, 'grade': grade})

with open(f'{ROOT}/ciphertext_appendix.tsv', 'w') as f:
    cols = ['leaf', 'entry_label', 'position', 'token', 'token_type', 'grade']
    f.write('\t'.join(cols) + '\n')
    for r in new_rows:
        f.write('\t'.join(r[c] for c in cols) + '\n')

# Rebuild each entry's cipher_line: same chunk/piece split as 01_segment.py's segment(), but in rewrite
# mode -- a CODE run's pieces are looked up by their ORIGINAL per-entry token position (ptr) and replaced
# by the settled token from new_rows, instead of being parsed out.
entry_new_tokens = {}
for r in new_rows:
    entry_new_tokens.setdefault((r['leaf'], r['entry_label']), []).append(r['token'])
entry_old_tokens = {}
for r in old_rows:
    entry_old_tokens.setdefault((r['leaf'], r['entry_label']), []).append(r['token'])
entry_grades = {}
for r in new_rows:
    entry_grades.setdefault((r['leaf'], r['entry_label']), []).append(r['grade'])


def norm(p):
    return p.lower() if len(p.rstrip('±')) == 1 and p.rstrip('±').isalpha() else p


def code_shaped(piece):
    bare = piece.rstrip('±')
    return bare.isdigit() or (len(bare) == 1 and bare.isalpha())


def rewrite_line(cipher_line, old_tokens, new_tokens):
    out_chunks = []
    ptr = 0
    for chunk in cipher_line.split():
        pieces_raw = [p for p in chunk.split('.') if p != '']
        pieces = [norm(p) for p in pieces_raw]
        n = len(pieces)
        matched = False
        if ptr + n <= len(old_tokens) and pieces == old_tokens[ptr:ptr + n] and n > 0:
            sub_new = new_tokens[ptr:ptr + n]
            out_chunks.append('.'.join(_reglyph(raw, new) for raw, new in zip(pieces_raw, sub_new)) + '.')
            ptr += n
            matched = True
        else:
            for skip in range(1, len(pieces)):
                sub = pieces[skip:]
                m = len(sub)
                if m > 0 and ptr + m <= len(old_tokens) and sub == old_tokens[ptr:ptr + m]:
                    plain_part = '.'.join(pieces_raw[:skip])
                    sub_new = new_tokens[ptr:ptr + m]
                    code_part = '.'.join(_reglyph(raw, new) for raw, new in zip(pieces_raw[skip:], sub_new)) + '.'
                    out_chunks.append(plain_part + '.' + code_part)
                    ptr += m
                    matched = True
                    break
        if not matched and n >= 2 and all(code_shaped(p) for p in pieces):
            sub_new = new_tokens[ptr:ptr + n] if ptr + n <= len(new_tokens) else pieces
            out_chunks.append('.'.join(_reglyph(raw, new) for raw, new in zip(pieces_raw, sub_new)) + '.')
            ptr += n
            matched = True
        if not matched:
            out_chunks.append(chunk)
    return ' '.join(out_chunks)


def _reglyph(raw_piece, new_token):
    """Keep the raw piece's own case/uncertainty marker (e.g. '9±', 'A') except for the settled letter/digit
    itself; new_token may itself already carry the '±' (an untouched position, new_token == old token
    verbatim) so strip before re-appending it once, not twice."""
    unc = '±' if raw_piece.endswith('±') else ''
    base = raw_piece.rstrip('±')
    new_base = new_token.rstrip('±')
    if base.isalpha() and base.isupper() and len(base) == 1:
        return new_base.upper() + unc
    return new_base + unc


plain_out = []
for r in plain_rows:
    key = (r['leaf'], r['entry_label'])
    cl = r['cipher_line']
    if cl.strip():
        old_t, new_t = entry_old_tokens.get(key, []), entry_new_tokens.get(key, [])
        cl = rewrite_line(cl, old_t, new_t)
    grades = entry_grades.get(key, [])
    entry_grade = 'H' if grades and all(g == 'H' for g in grades) else 'M'
    plain_out.append({**r, 'cipher_line': cl, 'grade': entry_grade})

with open(f'{ROOT}/plaintext_appendix.tsv', 'w') as f:
    cols = ['leaf', 'entry_label', 'cipher_line', 'deciffrada_line', 'grade']
    f.write('\t'.join(cols) + '\n')
    for r in plain_out:
        f.write('\t'.join(r[c] for c in cols) + '\n')

changed = sum(1 for r in new_rows if r['token'] != old_token_by_key[(r['leaf'], r['entry_label'], r['position'])])
h = sum(1 for r in new_rows if r['grade'] == 'H')
m = sum(1 for r in new_rows if r['grade'] == 'M')
print(f'{len(new_rows)} tokens: {changed} changed value, grade H={h} M={m}')
