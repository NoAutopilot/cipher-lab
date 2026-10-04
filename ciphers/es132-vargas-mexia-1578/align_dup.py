#!/usr/bin/env python3
"""align_dup.py -- token-by-token DP alignment of the duplicate cipher copy (f.93r-f.95r) of Philip II's 19 Sept 1578
letter against the f.89 letter (f.89r-f.91r) (A3V3-ES9396, 4 Oct 2026). Reads only committed ciphertext_*.tsv and key.tsv;
changes no reading and no key.

Alignment: global over the duplicate, free end gaps on the f.89 side (semi-global; the duplicate may be transcribed only in
part), Needleman-Wunsch with scores exact 4, same decoded text 2 (test0.dec_tok with key.tsv), same base number 1, other -2,
gap -3. Tokens are compared without '?' and without '{CLEAR...}' tokens (dropped, as test2 does).

Tokens are compared as (number, vowel sign, sorted above-marks); brace words lower-cased, letters only.
Classes per aligned pair (f.89 token x, duplicate token y):
  same      x == y (after stripping '?')
  notation  a declared reading-convention equivalence (NOTATION, LETTER below) -- not an error, counted apart
  variant   x != y but both decode to the same plaintext under key.tsv (homophone/notation choice by the clerk, or a mark
            the key ignores) -- counted as copy variant, not reader error
  differ-*  different decoded text (or one side undecodable): -mark (same number and vowel sign, above-marks differ),
            -vowel (same number), -base (different number/word) -- candidate reader error on either side, or a clerk's variant
  gap       a token present on one side only (indel)
Disagreement = differ / (same + variant + differ) on aligned pairs whose both tokens are unflagged, reported with N; it sums
both readings' errors (f.89 reconciled reading + duplicate reconciled reading) and any clerk variant, so err_true per reading
is about half of it if the two are equally reliable (reported as err_true_per_reading_*).
Window check (letters, not tokens): see the comment in main(); char_disagree_rate = char edits in text-differing windows /
(letters in anchors + letters in those windows); still sums both readings and any clerk spelling variant.
Writes dup_align.tsv (every aligned row) and dup_settlements.tsv (each f.89 '?' token aligned to an unflagged duplicate
token: confirm / propose), prints the summary JSON. --check: exit 1 if the committed outputs are stale.
"""
import sys, json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from test0 import load_key, load_lines, dec_tok

REF = ['f89r', 'f89v', 'f90r', 'f90v', 'f91r']
DUP = ['f93r', 'f93v', 'f94r', 'f94v', 'f95r']
CLEAR89 = 13  # ciphertext_f89r.tsv L01: '26 y a l 15 dρ l dρ c y sρ dρ m /' is the clear opening, not cipher
# Declared reading-convention equivalences (f.89 reading, duplicate reading), not errors: the duplicate's blind passes read the
# '1'+crossed-4 glyph as 14/14+/14. where the f.89 reconcilers read 12+/12. (34x '12+', 0x '14' in the f.89 letter), and the
# o-shaped glyph as 0 where f.89 reads 18 (= o). Marks are compared separately (a pair here with different marks is still notation).
NOTATION = {(('qum', ''), ('rum', '')), (('qom', ''), ('rom', '')),  # cursive capital read Q (f.89) / R (dup)
            (('12', '+'), ('14', '')), (('12', '+'), ('14', '+')), (('12', '.'), ('14', '.')), (('18', ''), ('0', ''))}
LETTER = {'a', 'y', 'e', 'o'}  # a brace single letter equals a key value decoding to it
UNPRINTED = {'f89r', 'f89v', 'f90r', 'f91r'}  # the 113 '?' tokens of NOTES.md are on these pages (f.90v is Teulet's)


def stream(pages):
    out = []
    for p in pages:
        f = HERE / ('ciphertext_%s.tsv' % p)
        if not f.exists(): continue
        L = load_lines(f)
        for ln, toks in L.items():
            for i, t in enumerate(toks):
                if t.startswith('{CLEAR') or t == '/': continue
                if p == 'f89r' and ln == 'L01' and i < CLEAR89: continue  # f.89r L01 tokens 1-13 transliterate the clear opening
                out.append((p, ln, i + 1, t))
    return out


def parts(t):
    """(base, vowel, marks) of a normalised token; brace words lower-cased, letters only."""
    t = t.rstrip('?')
    if t.startswith('{'):
        w = re.sub(r'[^a-z]', '', t.lower()); return (w, '', '')
    m = re.match(r'^(\d+_?|[A-Za-z]+)([+.σρ⊣]?)(.*)$', t)
    if not m: return (t, '', '')
    return (m.group(1), m.group(2), ''.join(sorted(re.findall(r'@\w', m.group(3)))))


def base(t):
    m = re.match(r'^(\{[^}]*\}|\d+|[A-Za-z]+)', t)
    return m.group(1) if m else t


def main():
    key = load_key()
    dec = lambda t: dec_tok(t, key)[0]
    R, D = stream(REF), stream(DUP)
    r = ['%s%s%s' % parts(t[3]) for t in R]; d = ['%s%s%s' % parts(t[3]) for t in D]
    pr = [parts(t[3]) for t in R]; pd = [parts(t[3]) for t in D]
    rd = [dec(t[3].rstrip('?')) for t in R]; dd = [dec(t[3].rstrip('?')) for t in D]

    def sim(i, j):
        if r[i] == d[j]: return 4
        if rd[i] is not None and rd[i] == dd[j]: return 2
        if pr[i][0] == pd[j][0]: return 1
        return -2
    G = -3
    n, m = len(r), len(d)
    # semi-global: free leading/trailing gaps in the reference (rows i), costed gaps in the duplicate (cols j)
    S = [[0.0] * (m + 1) for _ in range(n + 1)]
    P = [[0] * (m + 1) for _ in range(n + 1)]
    for j in range(1, m + 1): S[0][j] = S[0][j - 1] + G; P[0][j] = 2
    for i in range(1, n + 1): S[i][0] = 0; P[i][0] = 1
    for i in range(1, n + 1):
        Si, Sp = S[i], S[i - 1]
        for j in range(1, m + 1):
            a = Sp[j - 1] + sim(i - 1, j - 1); b = Sp[j] + G; c = Si[j - 1] + G
            if a >= b and a >= c: Si[j] = a; P[i][j] = 0
            elif b >= c: Si[j] = b; P[i][j] = 1
            else: Si[j] = c; P[i][j] = 2
    i = max(range(n + 1), key=lambda k: S[k][m]); i_end = i; j = m
    pairs = []
    while j > 0:
        if i == 0: pairs.append((None, j - 1)); j -= 1; continue
        p = P[i][j]
        if p == 0: pairs.append((i - 1, j - 1)); i -= 1; j -= 1
        elif p == 1: pairs.append((i - 1, None)); i -= 1
        else: pairs.append((None, j - 1)); j -= 1
    pairs.reverse(); i_start = i
    rows, cnt, cnt_clean = [], {}, {}
    sett = []
    for a, b in pairs:
        x = R[a] if a is not None else None; y = D[b] if b is not None else None
        if x is None or y is None: cls = 'gap'
        elif r[a] == d[b]: cls = 'same'
        elif rd[a] is not None and rd[a] == dd[b]: cls = 'variant'
        elif (pr[a][:2], pd[b][:2]) in NOTATION or (pr[a][0] in LETTER and pr[a][0] == dd[b]) or (pd[b][0] in LETTER and pd[b][0] == rd[a]):
            cls = 'notation'
        elif pr[a][:2] == pd[b][:2]: cls = 'differ-mark'   # same number and vowel sign, above-marks differ
        elif pr[a][0] == pd[b][0]: cls = 'differ-vowel'     # same number, vowel sign differs
        else: cls = 'differ-base'                           # different number/word
        cnt[cls] = cnt.get(cls, 0) + 1
        clean = x is not None and y is not None and not x[3].endswith('?') and not y[3].endswith('?')
        if clean: cnt_clean[cls] = cnt_clean.get(cls, 0) + 1
        rows.append('\t'.join([
            '%s:%s:%d' % x[:3] if x else '-', x[3] if x else '-', (rd[a] or '') if x else '',
            '%s:%s:%d' % y[:3] if y else '-', y[3] if y else '-', (dd[b] or '') if y else '', cls]))
        if x and y and x[3].endswith('?') and not y[3].endswith('?'):
            act = 'confirm' if cls == 'same' else ('confirm-text' if cls in ('variant', 'notation') else 'propose-' + cls[7:])
            sett.append('\t'.join(['%s:%s:%d' % x[:3], x[3], y[3], '%s:%s:%d' % y[:3], act, 'unprinted' if x[0] in UNPRINTED else 'teulet-f90v']))
    # Window check: between anchors (same/variant/notation pairs), compare the decoded text of the two sides. Equal text =
    # the clerk re-segmented or re-enciphered the same letters (copy variant); else char-level edit distance (difflib opcodes)
    # over the letters, windows containing a '?' or an undecodable token on either side skipped.
    import difflib
    win, wins = ([], []), []
    for (a, b), row in zip(pairs, rows):
        cls = row.rsplit('\t', 1)[1]
        if cls in ('same', 'variant', 'notation'):
            if win[0] or win[1]: wins.append(win)
            win = ([], [])
        else:
            if a is not None: win[0].append(a)
            if b is not None: win[1].append(b)
    if win[0] or win[1]: wins.append(win)
    W = dict(windows=0, skipped=0, text_equal=0, text_differ=0, chars=0, char_edits=0)
    for wa, wb in wins:
        W['windows'] += 1
        ta = [rd[k] for k in wa]; tb = [dd[k] for k in wb]
        if any(t is None for t in ta + tb) or any(R[k][3].endswith('?') for k in wa) or any(D[k][3].endswith('?') for k in wb):
            W['skipped'] += 1; continue
        sa, sb = ''.join(ta), ''.join(tb)
        if sa == sb: W['text_equal'] += 1; continue
        W['text_differ'] += 1
        ops = difflib.SequenceMatcher(None, sa, sb, autojunk=False).get_opcodes()
        W['char_edits'] += sum(max(i2 - i1, j2 - j1) for o, i1, i2, j1, j2 in ops if o != 'equal')
        W['chars'] += max(len(sa), len(sb))
    anchor_chars = sum(len(rd[a] or '') for (a, b), row in zip(pairs, rows) if a is not None and b is not None and row.rsplit('\t', 1)[1] in ('same', 'variant', 'notation'))
    W['anchor_chars'] = anchor_chars
    W['char_disagree_rate'] = round(W['char_edits'] / (anchor_chars + W['chars']), 4) if anchor_chars else None
    C = lambda k: cnt_clean.get(k, 0)
    dif = C('differ-mark') + C('differ-vowel') + C('differ-base')
    al = C('same') + C('variant') + C('notation') + dif
    qref = [t for t in R[i_start:i_end] if t[3].endswith('?')]
    summary = dict(
        ref_tokens=len(R), dup_tokens=len(D), ref_span=('%s:%s:%d' % R[i_start][:3], '%s:%s:%d' % R[i_end - 1][:3]) if R and D else None,
        classes_all=cnt, classes_both_unflagged=cnt_clean, aligned_both_unflagged=al,
        disagree_full=round(dif / al, 4) if al else None,
        disagree_core_base_vowel=round((C('differ-vowel') + C('differ-base')) / al, 4) if al else None,
        disagree_base=round(C('differ-base') / al, 4) if al else None,
        err_true_per_reading_full=round(dif / al / 2, 4) if al else None,
        err_true_per_reading_core=round((C('differ-vowel') + C('differ-base')) / al / 2, 4) if al else None,
        variant_rate=round(cnt_clean.get('variant', 0) / al, 4) if al else None,
        window_check=W,
        ref_q_in_span=len(qref), ref_q_in_span_unprinted=sum(t[0] in UNPRINTED for t in qref),
        settlements=dict(total=len(sett), unprinted=sum(s.endswith('unprinted') for s in sett),
                         confirm=sum('\tconfirm\t' in s for s in sett), confirm_text=sum('\tconfirm-text\t' in s for s in sett),
                         propose_mark=sum('\tpropose-mark\t' in s for s in sett), propose_vowel=sum('\tpropose-vowel\t' in s for s in sett),
                         propose_base=sum('\tpropose-base\t' in s for s in sett)))
    outs = {
        'dup_align.tsv': '# align_dup.py (A3V3-ES9396): f89_pos f89_tok f89_text dup_pos dup_tok dup_text class\n' + '\n'.join(rows) + '\n',
        'dup_settlements.tsv': '# align_dup.py (A3V3-ES9396): f.89 \'?\' tokens aligned to an unflagged duplicate token. For a later rule-7 job; NOT applied.\n'
                               '# f89_pos\tf89_tok\tdup_tok\tdup_pos\taction\tpage_kind\n' + '\n'.join(sett) + '\n',
        'dup_align_summary.json': json.dumps(summary, indent=1, ensure_ascii=False) + '\n'}
    if '--check' in sys.argv:
        stale = [k for k, v in outs.items() if not (HERE / k).exists() or (HERE / k).read_text(encoding='utf-8') != v]
        print('STALE ' + ' '.join(stale) if stale else 'SAME'); sys.exit(1 if stale else 0)
    for k, v in outs.items(): (HERE / k).write_text(v, encoding='utf-8')
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == '__main__':
    main()
