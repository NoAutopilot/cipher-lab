#!/usr/bin/env python3
"""Align ciphertext.tsv (clear Dutch words + coded runs) against plaintext_print.txt (the known plaintext,
same letter, different copy) and key every code the known plaintext can fix (job step 1-2 of
.claude/briefs/runs/2026-09-25-lane-ox-vbs2.md).

Method: a global (Needleman-Wunsch) word alignment. Clear cipher words are hard anchors when they match a
plaintext word; coded words score against a plaintext word by letter-count match plus consistency with the
codes already keyed (bootstrapped from key.tsv). Known nomenclator phrases are pre-collapsed into single
plaintext tokens so their codes align 1:1. Between anchors the DP allows insertions/omissions (the two copies
are in different hands and do not agree word for word -- CLAUDE.md rule 2, this is not a byte-identical
duplicate).

Output: prints every accepted coded-word / plaintext-word pair, one vote per code position, to stdout as TSV
(code, letter, cipher_word, plain_word, line). vote.py (or this script's --build mode) turns that into key.tsv.

Usage:
  python3 align.py                 print the alignment (debug: cipher word | plain word, one per aligned pair)
  python3 align.py --votes         print one row per code position: code, letter, plain_word, cipher_line
  python3 align.py --build         write key.tsv (voted) and conflicts.tsv from the votes
"""
import argparse, collections, re, sys, os

TARGET = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- ciphertext

def load_cipher_words():
    rows = []
    for l in open(os.path.join(TARGET, 'ciphertext.tsv'), encoding='utf-8'):
        l = l.rstrip('\n')
        if not l.strip():
            continue
        p = l.split('\t')
        if p[0] == 'line':
            continue
        rows.append(p)  # line, pos, sign, confidence, alt, why

    words, cur = [], None
    for r in rows:
        line, pos, sign = r[0], r[1], r[2]
        if re.match(r'^\d+[,:]$', sign):
            if cur is None:
                cur = {'kind': 'coded', 'codes': [], 'first_line': line}
            cur['codes'].append(sign.rstrip(',:'))
            cur['last_line'] = line
            if sign.endswith(':'):
                words.append(cur)
                cur = None
        else:
            if cur:
                words.append(cur)
                cur = None
            kind = 'mark' if sign in ('[MARK]', '[ILLEGIBLE]') else 'clear'
            words.append({'kind': kind, 'text': sign, 'line': line})
    if cur:
        words.append(cur)
    return words


# ---------------------------------------------------------------- plaintext

# The known-established nomenclator (from key.tsv's grade-C 3-digit rows), used to pre-collapse the
# plaintext into single tokens so an already-recovered nomenclator code aligns 1:1 against its phrase.
NOMENCLATOR = {
    'Vereenichde Nederlanden': '143',
    'Haer Hoog Mog.': '144',
    'Engelandt': '213',
    'Sweden': '105',
    'Vranckrijk': '225',
    'Elseneur': '104',
    'Londen': '222',
    'Denemarcken': '172',
    'Coningh van Denemarcken': '173',
}
# Longest phrase first, so multi-word phrases are collapsed before their component words are seen alone.
NOMENCLATOR_PHRASES = sorted(NOMENCLATOR, key=lambda s: -len(s.split()))


def letter_body():
    lines = open(os.path.join(TARGET, 'plaintext_print.txt'), encoding='utf-8').read().splitlines()
    body = []
    in_body = False
    for l in lines:
        if l.strip().startswith('(19/29 September'):
            in_body = True
            continue
        if l.strip().startswith('--- Footnotes'):
            break
        if in_body and l.strip() and not l.strip().startswith('[p.'):
            body.append(l)
    return ' '.join(body)


def load_plaintext_words():
    """Split into words, then greedily collapse known multi-word nomenclator phrases (longest first) into a
    single token -- done on the word list, not the raw text, because str.split() treats several plausible
    joiner characters (U+00A0, and even the ASCII separators U+001C-U+001F) as whitespace and would silently
    re-split a phrase joined on any of them."""
    raw = letter_body().split()
    phrase_lists = [p.split() for p in NOMENCLATOR_PHRASES if ' ' in p]
    words, i = [], 0
    while i < len(raw):
        matched = None
        for pl in phrase_lists:
            n = len(pl)
            if raw[i:i + n] == pl:
                matched = n
                break
            # last word of the phrase may carry trailing punctuation (e.g. "Nederlanden,")
            if n > 1 and raw[i:i + n - 1] == pl[:-1] and raw[i + n - 1].startswith(pl[-1]):
                matched = n
                break
        if matched:
            words.append({'text': ' '.join(raw[i:i + matched])})
            i += matched
        else:
            words.append({'text': raw[i]})
            i += 1
    return words


# ---------------------------------------------------------------- normalisation

def norm_word(s):
    """Lowercase, strip surrounding punctuation/footnote digits, merge u/v and i/j (period orthography,
    LESSONS.md; key.tsv already treats u/v as one code)."""
    s = s.lower()
    s = re.sub(r"^[\[\(]+|[\]\)\.,;:!\"']+$", '', s)
    s = re.sub(r'\d\)$', '', s)  # footnote markers "1)" "2)"
    s = s.replace('v', 'u').replace('j', 'i')
    return s


def letters_only(s):
    return re.sub(r"[^a-z']", '', norm_word(s))


# ---------------------------------------------------------------- scoring / DP

MATCH_CLEAR, MISMATCH_CLEAR = 8, -3
LEN_MATCH, LEN_OFF_BY_ONE, LEN_MISMATCH = 4, 0, -4
KEY_AGREE, KEY_DISAGREE = 3, -5
GAP = -2


def score(cw, pw, key):
    if cw['kind'] == 'clear':
        return MATCH_CLEAR if norm_word(cw['text']) == norm_word(pw['text']) else MISMATCH_CLEAR
    # coded
    codes = cw['codes']
    pl = letters_only(pw['text'])
    if len(codes) == 1 and int(codes[0]) >= 100:
        # nomenclator-range single code: high score only against a collapsed nomenclator token or an
        # already-agreed value; otherwise a small flat score so the DP can still place it near its context
        # without forcing a specific (possibly wrong) word-length match.
        val = key.get(codes[0])
        if val and norm_word(pw['text']) == norm_word(val):
            return 12
        return 0.5
    base = LEN_MATCH if len(codes) == len(pl) else (LEN_OFF_BY_ONE if abs(len(codes) - len(pl)) == 1 else LEN_MISMATCH)
    consistency = 0
    if len(codes) == len(pl):
        for code, letter in zip(codes, pl):
            kv = key.get(code)
            if kv:
                consistency += KEY_AGREE if kv == letter else KEY_DISAGREE
    return base + consistency


def align(cipher, plain, key):
    # drop 'mark' words entirely from the alignable sequence
    cseq = [w for w in cipher if w['kind'] != 'mark']
    n, m = len(cseq), len(plain)
    NEG = float('-inf')
    dp = [[0.0] * (m + 1) for _ in range(n + 1)]
    bt = [[None] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] + GAP
        bt[i][0] = 'up'
    for j in range(1, m + 1):
        dp[0][j] = dp[0][j - 1] + GAP
        bt[0][j] = 'left'
    for i in range(1, n + 1):
        cw = cseq[i - 1]
        for j in range(1, m + 1):
            pw = plain[j - 1]
            diag = dp[i - 1][j - 1] + score(cw, pw, key)
            up = dp[i - 1][j] + GAP
            left = dp[i][j - 1] + GAP
            best = max(diag, up, left)
            dp[i][j] = best
            bt[i][j] = 'diag' if best == diag else ('up' if best == up else 'left')
    # traceback
    i, j = n, m
    pairs = []
    while i > 0 or j > 0:
        d = bt[i][j]
        if d == 'diag':
            pairs.append((cseq[i - 1], plain[j - 1]))
            i, j = i - 1, j - 1
        elif d == 'up':
            pairs.append((cseq[i - 1], None))
            i -= 1
        else:
            pairs.append((None, plain[j - 1]))
            j -= 1
    pairs.reverse()
    return pairs, dp[n][m]


def bootstrap_key():
    """Seed the scorer with key.tsv's current grade-C rows (letters + nomenclator), so the DP's own
    consistency term can favour alignments that agree with what is already solidly established."""
    key = {}
    path = os.path.join(TARGET, 'key.tsv')
    if not os.path.exists(path):
        return key
    header, rows = None, []
    for l in open(path, encoding='utf-8'):
        l = l.rstrip('\n')
        if not l.strip():
            continue
        p = l.split('\t')
        if header is None:
            header = p
            continue
        rows.append(p)
    ci, vi, gi = header.index('code'), header.index('value'), header.index('grade')
    for r in rows:
        code, value, grade = r[ci].rstrip(',:'), r[vi], r[gi]
        if grade != 'C':
            continue
        if re.match(r'^\d+$', code):
            key[code] = norm_word(value) if len(value) > 1 and value[0].isupper() else value
    return key


# ---------------------------------------------------------------- voting

def votes_from_pairs(pairs):
    """One row per accepted code position: (code, letter, cipher_line, plain_word)."""
    out = []
    for cw, pw in pairs:
        if cw is None or pw is None or cw['kind'] != 'coded':
            continue
        codes = cw['codes']
        if len(codes) == 1 and int(codes[0]) >= 100:
            out.append((codes[0], norm_word(pw['text']), cw['first_line'], pw['text'], 'nomenclator'))
            continue
        pl = letters_only(pw['text'])
        if len(codes) != len(pl):
            continue
        for code, letter in zip(codes, pl):
            out.append((code, letter, cw['first_line'], pw['text'], 'letter'))
    return out


def build_key(votes):
    """Vote per code (job step 2): grade C when the top value has >=2 independent-word support and no
    substantial minority (a lone stray word is noise, not a conflict); grade M when the top value has only
    one supporting word, or when a minority value also has >=2 words behind it (a genuine, unresolved
    conflict -- rule 3/CLAUDE.md: never silently pick a winner when the evidence itself disagrees)."""
    by_code = collections.defaultdict(collections.Counter)
    contexts = collections.defaultdict(list)
    for code, letter, line, word, kind in votes:
        by_code[code][letter] += 1
        contexts[code].append((letter, word, line, kind))
    rows, conflicts = [], []
    for code in sorted(by_code, key=lambda c: int(c)):
        counter = by_code[code]
        total = sum(counter.values())
        common = counter.most_common()
        top_letter, top_n = common[0]
        second_n = common[1][1] if len(common) > 1 else 0
        support_words = [w for (l, w, ln, k) in contexts[code] if l == top_letter]
        genuine_conflict = second_n >= 2
        grade = 'M' if (top_n < 2 or genuine_conflict) else 'C'
        if len(counter) > 1:
            conflicts.append((code, counter, contexts[code], genuine_conflict))
        rows.append((code, top_letter, grade, top_n, total, sorted(set(support_words))))
    return rows, conflicts


def fmt_key_rows(rows):
    out = ['code\tvalue\tgrade\tsource\tnote']
    for code, letter, grade, top_n, total, words in rows:
        note = f"align.py vote {top_n}/{total} ({', '.join(words[:6])})"
        for suf in (',', ':'):
            out.append(f"{code}{suf}\t{letter}\t{grade}\tknown-plaintext alignment (align.py) 25 Sept 2026\t{note}")
    return '\n'.join(out) + '\n'


def fmt_conflicts(conflicts):
    out = ['code\tgenuine\tcounts\tcontexts']
    for code, counts, ctx, genuine in conflicts:
        cstr = ', '.join(f'{l}:{n}' for l, n in counts.most_common())
        ctxstr = '; '.join(f"{l}<-{w}@{ln}" for l, w, ln, k in ctx)
        out.append(f'{code}\t{genuine}\t{cstr}\t{ctxstr}')
    return '\n'.join(out) + '\n'


def load_full_key():
    """key.tsv's current value per code (any grade), first alternative of an 'a|b' ambiguous value --
    used only for --diff reporting, not for scoring (bootstrap_key is what the DP scorer uses)."""
    key = {}
    for l in open(os.path.join(TARGET, 'key.tsv'), encoding='utf-8'):
        l = l.rstrip('\n')
        if not l.strip() or l.startswith('code\t'):
            continue
        p = l.split('\t')
        code, value = p[0].rstrip(',:'), p[1]
        if re.match(r'^\d+$', code):
            key[code] = value.split('|')[0]
    return key


def diff_report(pairs, full_key):
    """job step 3's 'words where the decoded cipher copy differs from the print' table: for every fully-keyed
    coded word (no unresolved code), compare its decoded letters against the aligned plaintext word."""
    rows = []
    for cw, pw in pairs:
        if cw is None or pw is None or cw['kind'] != 'coded':
            continue
        codes = cw['codes']
        if len(codes) == 1 and int(codes[0]) >= 100:
            continue  # nomenclator: already reported via votes, not a letter-diff
        decoded = ''.join(full_key.get(c, '?') for c in codes)
        if '?' in decoded:
            continue  # not fully keyed, not a same/differ comparison
        target = letters_only(pw['text'])
        if decoded != target:
            rows.append((cw['first_line'], ','.join(codes), decoded, pw['text']))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--votes', action='store_true')
    ap.add_argument('--build', action='store_true')
    ap.add_argument('--debug', action='store_true', help='print the full alignment, one pair per line')
    ap.add_argument('--diff', action='store_true', help='print job step 3\'s decoded-vs-print difference table')
    a = ap.parse_args()

    cipher = load_cipher_words()
    plain = load_plaintext_words()
    key = bootstrap_key()
    pairs, total_score = align(cipher, plain, key)

    if a.debug:
        for cw, pw in pairs:
            cs = cw['text'] if cw and cw['kind'] == 'clear' else (','.join(cw['codes']) if cw else '-')
            ps = pw['text'] if pw else '-'
            print(f"{cs}\t{ps}")
        print(f"# alignment score: {total_score}", file=sys.stderr)
        return

    if a.diff:
        full_key = load_full_key()
        print('line\tcodes\tdecoded\tprint_word')
        for line, codes, decoded, word in diff_report(pairs, full_key):
            print(f'{line}\t{codes}\t{decoded}\t{word}')
        return

    votes = votes_from_pairs(pairs)
    if a.votes:
        print('code\tletter\tline\tplain_word\tkind')
        for v in votes:
            print('\t'.join(v))
        return

    rows, conflicts = build_key(votes)
    if a.build:
        open(os.path.join(TARGET, 'key_align.tsv'), 'w', encoding='utf-8').write(fmt_key_rows(rows))
        open(os.path.join(TARGET, 'conflicts.tsv'), 'w', encoding='utf-8').write(fmt_conflicts(conflicts))
        print(f"wrote key_align.tsv ({len(rows)} codes) and conflicts.tsv ({len(conflicts)} conflicting codes)", file=sys.stderr)
        return

    for r in rows:
        print(r)


if __name__ == '__main__':
    main()
