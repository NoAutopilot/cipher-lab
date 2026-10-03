#!/usr/bin/env python3
"""Apply a substitution key to a reconciled transcription and regenerate the graded reading (CLAUDE.md rules 4 and 7).

  python3 tools/decode_key.py TARGET_DIR                 write the reading(s) described by TARGET_DIR/decode.json
  python3 tools/decode_key.py TARGET_DIR --check         exit 1 if any committed reading differs from a regeneration
  python3 tools/decode_key.py TARGET_DIR --config F      use config file F instead of TARGET_DIR/decode.json
  python3 tools/decode_key.py TARGET_DIR --ciphertext ciphertext.tsv --key key.tsv [--exceptions exceptions.tsv]
                              [--style spaced|concat|words] [--reading reading.txt] [--tokens reading_tokens.tsv]
  python3 tools/decode_key.py TARGET_DIR --split-check [--split-tsv out.tsv]
                                                       report out-of-key / out-of-range tokens and how each splits
                                                       into two or three key values (a report: writes no reading)

With no decode.json and no options it reads ciphertext.tsv (or ciphertext.txt), key.tsv and exceptions.tsv if present,
and writes reading.txt and reading_tokens.tsv in the 'spaced' style. Nothing is fetched; nothing outside TARGET_DIR
(or the paths named) is written.

Lesson answered (LEDGER.md, 23-24 Sept 2026): six targets each carried their own decode.py, each re-deriving the same
token loop, the same grade downgrade and the same --check; three of them differ only in file layout and print style.
This script is that loop once. A target keeps a small decode.json describing its layout instead of a script.

Inputs (formats found in the repo, detected per file):
  ciphertext  'pipe'  '<folio> <line> | tok tok ...' (fr2980-gramont ciphertext.txt); 0-based index over all tokens;
                      a trailing '?' marks an uncertain sign; '.' is a dot (kept in the index, not a token).
              'tsv'   header 'line  pos|position|index  sign|token|group  conf|confidence' (fr2980-gramont f.30,
                      fr20140-danzay-1557). 'w:word' or '[PLAIN:word]' is a clear word, not a cipher token.
              'rows'  'line <TAB> tokens <TAB> glosses' (dupuy468-anhalt): 1-based positions over the line's tokens,
                      [PLAIN:word] clear words, glosses 'word@i-j'.
  key         TSV with a header row (or a '# name<TAB>name' comment header): the sign column is the first of code, sign,
              token; then value; optional grade, source, note. The key's own grade column is used when present,
              otherwise default_grade (H: read from a key source). decode.json's 'key' may be a list of filenames
              (or --key a,b on the CLI) to merge two key tables (e.g. a separate alphabet key and a nomenclator
              key); a code present in both with the same value merges silently, a code with two different values
              becomes 'value1|value2' (auto-graded M, per the ambiguous-value rule below) rather than one file's
              row silently overwriting the other's.
  exceptions  TSV, one row per position that overrides the key: line (and folio), pos|position|index, value (or the
              column named by exceptions_value_column), optional grade (else exception_grade), reason. By default an
              exception on a low-confidence sign is still downgraded to M like any other token; with
              'exception_grade_overrides_conf': true in decode.json the exception's own grade stands (use it only when the
              exception rows record the image evidence that settled the sign, e.g. a blind check with matched decoys;
              3 Oct 2026, BIR-OPEN).

Grades (rule 4): the key row's grade, or H; M when the sign's confidence is in uncertain_conf (or it carries '?'),
when the value is ambiguous ('a|b'), or when the key row's source is in m_sources or its note contains an m_words
entry; U (or unkeyed_grade) when the sign is not keyed. Optional 'votes' (per-position plaintext evidence such as an
interlinear gloss): voted_grade (H) where the vote matches the key value, unvoted_grade (S) elsewhere, word_glossed_grade (M) for a
word sign whose own gloss disagrees; disagree_grade, when set, for a sign that has a vote which does not match (unvoted_grade
then covers only signs with no vote at all). s_words (3 Oct 2026, READ2-PAG): a key row whose note contains an s_words
entry grades S (cryptanalytic with a control: the value was chosen by a test) where its vote agrees or it has none, and
disagree_grade (or M) where its vote disagrees; checked before m_words.

decode.json: {"jobs": [{...}, ...]} or one job object. Job keys (all optional):
  ciphertext, key, exceptions, reading, tokens   file names relative to TARGET_DIR
  format        pipe | tsv | rows (default: detected)
  split_line    '_' to split a tsv line id 'f30r_L01' into folio 'f30r' and line 'L01'
  line_column   'tsv' format only: header name of the line-id column, default 'line' (antt-linhares-chave uses
                'line' too, but with a separate folio_column since its ciphertext has both a page and a line
                column rather than one combined id)
  folio_column  'tsv' format only: header name of a separate folio/page column, combined with line_column into
                the folio+line label instead of split_line's single-column split (antt-linhares-chave:
                'page_of_letter')
  style         spaced | concat | words (see render_*)
  header        list of header lines for the reading; placeholders {total} {HCSMIU} {grades_sorted} {name} {H} {M} ...
  token_columns list of [header, field]; fields: folio line pos raw sign conf value grade gloss
  include_clear put clear-word rows in the token file (grade 'clear')
  null_values ["NULL", "null"]; empty_is_null (false: '' is unknown); unknown_values ["", "?"];
  unknown_if_q  (a value containing '?' is unknown); unkeyed_value ('?'); unkeyed_grade ('U'); default_grade ('H')
  uncertain_conf (["M","m","L","l","low","?"]); word_values (list: values shown <w> in the spaced style)
  clear_prefix  a tsv sign starting with this prefix is a clear word (e.g. '=' for '=nous', LANE R passes)
  conf_column   'tsv' format only: header name of the sign-confidence column when it is not conf/confidence
                (clairambault1225-paget-1714: 'grade', H/M per transcription pass agreement)
  kind_column, sign_kinds  'tsv' format only: a ciphertext that interleaves clear words and cipher tokens in one
                column with a kind column; a row whose kind is not in sign_kinds is a clear word
                (clairambault1225-paget-1714: kind_column 'kind', sign_kinds ['cipher', 'cipher/insertion-clear'])
  nonsign       list of tsv signs that are not cipher tokens (punctuation, a word-break marker): kept in the index,
                not graded; with it, concat prints them and prints word_sep (e.g. '/') as a space
  defaults (object merged under every job), m_sources, m_words, s_words, votes {file, value_column, word_prefix, strip_prefixes}, voted_grade, unvoted_grade, word_glossed_grade, disagree_grade

--split-check (1 Oct 2026, the espagnol142-mercy-1648 lesson): against a key of values 2-34, four tokens (65, 52,
48, 72) were each two digits written together (D. Bourdeau, dbourdeau/cyphersolver issue 16; snapshot
sources/cyphersolver/2026-10-01/). They had been keyed as M rows by an anneal, so 'not in the key' alone would not
have caught them. The check therefore flags a sign token when (a) it is not a key code ('unkeyed'), or (b) it is
numeric and lies outside the numeric range of the key's confident rows -- codes whose grade is not M, I or U (a
blank grade counts as confident, as default_grade does) -- ('out-of-range'; computed only when at least half the
key's codes, and at least five, are plain digit strings; falls back to all numeric codes when none is confident).
For each flagged digit token it lists every way the digit string cuts into two or three consecutive key codes
(exact strings, so '05' is not '5'; parts drawn from the confident range when there is one) with their values.
Output: a compact table per job and a count line; --split-tsv FILE also writes target, job, key_range, token, n, status,
positions (line:pos), exceptions (occurrences overridden by exceptions.tsv), splits, decoded. Exit 0 whatever it
finds (a report, not a gate); exit 2 only if the target cannot be loaded. It writes no reading and ignores --check.
A split is a candidate for an image check, never a correction by itself: 26 = i at Mercy r18 and r24 was also two
digits (2 6, o s), in range and keyed, which only sense and the image could show.

Test: python3 tools/tests/test_decode_key.py (reproduces fr2980-gramont, fr20140-danzay-1557 and dupuy468-anhalt
readings from tools/tests/decode_configs/*.json, byte for byte, without writing).
"""
import argparse, collections, json, os, re, sys

GRADES = 'HCSMIU'
DEFAULT_UNCERTAIN = ['M', 'm', 'L', 'l', 'low', '?']


def is_comment(line):
    """A comment line is '#' alone, '# ...' (hash + space) or '##...'. It catches the repo's comment and
    '# name<TAB>name' header lines. It must NOT catch a row whose first cell is a cipher sign written with '#':
    '#<TAB>a' (fr3621-dinteville-1592), "#'<TAB>l'Empereur" and '#~<TAB>...' (tools/keys/key60.tsv) are data.
    Before 3 Oct 2026 (TOOL-DK-HASH) every line starting with '#' was skipped, so those signs decoded as U."""
    s = line.rstrip('\r\n')
    return s.startswith('#') and (len(s) == 1 or s[1] in ' #')


def data_lines(path):
    """Non-comment lines split on tabs; the last '# a<TAB>b' comment before data counts as a header."""
    header, out = None, []
    for l in open(path, encoding='utf-8'):
        s = l.rstrip('\n')
        if not s.strip():
            continue
        if is_comment(s):
            c = s.lstrip('#').strip()
            if '\t' in c and not out:
                header = c.split('\t')
            continue
        out.append(s.split('\t'))
    return header, out


def with_header(path, first_names):
    """(header, rows): the first row is the header when its first cell is one of first_names."""
    header, rows = data_lines(path)
    if rows and rows[0][0] in first_names:
        header, rows = rows[0], rows[1:]
    return header, rows


def col(header, *names):
    for n in names:
        if header and n in header:
            return header.index(n)
    return None


# ---------------------------------------------------------------- ciphertext loaders

def clear_word(t):
    if t.startswith('w:'):
        return t[2:]
    if t.startswith('[PLAIN:') and t.endswith(']'):
        return t[7:-1]
    return None


def detect_format(path):
    for l in open(path, encoding='utf-8'):
        if not l.strip() or is_comment(l):
            continue
        if '|' in l.split('\t')[0] and re.match(r'^\S+( \S+)? \|', l):
            return 'pipe'
        h = l.rstrip('\n').split('\t')
        if h[0] == 'line' and len(h) >= 3 and h[1] in ('pos', 'position', 'index', 'idx'):
            return 'tsv'
        return 'rows'
    return 'tsv'


def load_pipe(path, job):
    recs = []
    for l in open(path, encoding='utf-8'):
        if not l.strip() or is_comment(l):
            continue
        head, body = l.split('|', 1)
        hp = head.split()
        fo, ln = (hp[0], hp[1]) if len(hp) > 1 else ('', hp[0])
        label = f'{fo} {ln}' if fo else ln
        recs.append(dict(folio=fo, line=ln, label=label, pos=None, kind='line'))
        for i, t in enumerate(body.split()):
            unsure = t.endswith('?') and t != '[?]'
            recs.append(dict(folio=fo, line=ln, label=label, pos=i, raw=t, sign=t.rstrip('?'),
                             conf='?' if unsure else '', kind='dot' if t == '.' else
                             'clear' if clear_word(t) is not None else 'sign', gloss=''))
    return recs


def load_tsv(path, job):
    lc = job.get('line_column', 'line')
    foc = job.get('folio_column')
    header, rows = with_header(path, (foc, lc) if foc else (lc,))
    if header is None and rows and lc in rows[0]:  # line column not first (a 'letter' column before it)
        header, rows = rows[0], rows[1:]
    ci = col(header, lc); pi = col(header, 'pos', 'position', 'index', 'idx')
    si = col(header, 'sign', 'token', 'group', 'code')
    ki = col(header, *([job['conf_column']] if job.get('conf_column') else ['conf', 'confidence']))
    kc = col(header, job['kind_column']) if job.get('kind_column') else None
    sign_kinds = set(job.get('sign_kinds', []))
    split = job.get('split_line')
    foi = col(header, foc) if foc else None
    recs, seen = [], set()
    for r in rows:
        ln = r[ci]
        if foi is not None:
            fo, l2 = r[foi], ln
        else:
            fo, l2 = (ln.split(split, 1) if split and split in ln else ('', ln))
        label = f'{fo} {l2}' if fo else l2
        seen_key = (fo, ln)
        if seen_key not in seen:
            seen.add(seen_key); recs.append(dict(folio=fo, line=l2, label=label, pos=None, kind='line'))
        t = r[si]; conf = r[ki] if ki is not None and ki < len(r) else ''
        cp = job.get('clear_prefix')
        if cp and t.startswith(cp) and len(t) > len(cp):
            t = 'w:' + t[len(cp):]
        if kc is not None and r[kc] not in sign_kinds:
            t = 'w:' + t
        recs.append(dict(folio=fo, line=l2, label=label, pos=int(r[pi]), raw=t, sign=t, conf=conf, gloss='',
                         kind='dot' if t == '.' or t in job.get('nonsign', []) else
                         'clear' if clear_word(t) is not None else 'sign'))
    return recs


def load_rows(path, job):
    recs = []
    for l in open(path, encoding='utf-8'):
        if is_comment(l) or not l.strip():
            continue
        p = l.rstrip('\n').split('\t') + ['', '']
        ln, toks, graw = p[0], p[1].split(), p[2]
        gl = {}
        for g in graw.split():
            w, _, span = g.rpartition('@')
            a, _, b = span.partition('-')
            for i in range(int(a), int(b or a) + 1):
                gl[i] = w
        recs.append(dict(folio='', line=ln, label=ln, pos=None, kind='line', gloss_raw=graw))
        for i, t in enumerate(toks, 1):
            recs.append(dict(folio='', line=ln, label=ln, pos=i, raw=t, sign=t, conf='', gloss=gl.get(i, ''),
                             kind='clear' if clear_word(t) is not None else 'dot' if t == '.' else 'sign'))
    return recs


LOADERS = {'pipe': load_pipe, 'tsv': load_tsv, 'rows': load_rows}


# ---------------------------------------------------------------- key, exceptions, votes

KEY_COLUMN_NAMES = ('code', 'sign', 'token', 'value', 'letter', 'word_or_phrase', 'word', 'kind', 'grade',
                    'source', 'note', 'crop', 'section')


def merge_key_row(key, code, row):
    """Add row to key under code, without letting a repeated code silently overwrite a different value --
    whether the repeat is two rows of the same key file (clair349-este-guise-1556's key_alpha.tsv has both
    C=9 and DOUBLES:ss=9) or two different key files merged by load_keys. Combines disagreeing values as
    'a|b' (grade_tokens already downgrades any '|' value to M) so a real ambiguity in the cipher design is
    preserved rather than hidden by load order."""
    prev = key.get(code)
    if prev is None:
        key[code] = row
    elif prev['value'] == row['value']:
        return
    else:
        key[code] = dict(value=f"{prev['value']}|{row['value']}", grade='M',
                         source=f"{prev['source']}+{row['source']}".strip('+'),
                         note=f"code {code!r} repeats with a different value: "
                              f"{prev['value']!r} ({prev['note'] or prev['source']}) vs "
                              f"{row['value']!r} ({row['note'] or row['source']})",
                         text=f"{prev['text']} || {row['text']}")


def load_key(path):
    """A key TSV's header may put the code column first (code/sign/token ... value) or the value column first
    (letter/word_or_phrase ... code ...  -- clair349-este-guise-1556's key_alpha.tsv/key_nomen.tsv, each column
    a plain-language name rather than 'code'/'value'); detect the header by any recognised name anywhere in row
    1, not only at position 0, then locate the code and value columns by name wherever they sit. A row whose
    code cell is empty or '?' (unresolved -- not a real mapping) is skipped rather than poisoning the dict. A
    code that repeats within the file goes through merge_key_row rather than the last row silently winning."""
    header, rows = data_lines(path)
    if header is None and rows and any(c in KEY_COLUMN_NAMES for c in rows[0]):
        header, rows = rows[0], rows[1:]
    if header is None:
        header = ['code', 'value', 'source']
    si = col(header, 'code', 'sign', 'token') or 0
    vi = col(header, 'value', 'letter', 'word_or_phrase', 'word')
    gi = col(header, 'grade'); ri = col(header, 'source'); ni = col(header, 'note')
    key = {}
    for r in rows:
        r = r + [''] * (len(header) - len(r))
        code = r[si]
        if not code or code == '?':
            continue
        row = dict(value=r[vi] if vi is not None else '', grade=r[gi] if gi is not None else None,
                   source=r[ri] if ri is not None else '', note=r[ni] if ni is not None else '',
                   text=' '.join(r))
        merge_key_row(key, code, row)
    return key


def load_exceptions(path, job):
    if not path or not os.path.exists(path):
        return {}
    header, rows = with_header(path, ('line', 'folio'))
    fi = col(header, 'folio'); li = col(header, 'line'); pi = col(header, 'pos', 'position', 'index')
    vi = col(header, job.get('exceptions_value_column', 'value'), 'value'); gi = col(header, 'grade')
    ex = {}
    for r in rows:
        k = (r[fi] if fi is not None else '', r[li], int(r[pi]))
        ex[k] = (r[vi], r[gi] if gi is not None and gi < len(r) and r[gi] else job.get('exception_grade', 'M'))
    return ex


def load_keys(target, spec):
    """Load job['key'] where spec is one filename or a list of filenames to merge (e.g. a separate alphabet
    key and a nomenclator key, clair349-este-guise-1556). Files are merged in order; a code already set by an
    earlier file whose value disagrees with a later file's is not silently overwritten -- the two values are
    combined as 'a|b' (grade_tokens already downgrades any '|' value to M) and the note records the collision,
    so a real ambiguity in the underlying cipher design is preserved rather than hidden by load order."""
    paths = spec if isinstance(spec, list) else [spec]
    merged = {}
    for p in paths:
        for code, row in load_key(os.path.join(target, p)).items():
            merge_key_row(merged, code, row)
    return merged


def load_votes(target, job):
    v = job.get('votes')
    if not v:
        return None
    header, rows = with_header(os.path.join(target, v['file']), ('line',))
    li, pi, vi = col(header, 'line'), col(header, 'pos', 'position'), col(header, v.get('value_column', 'value'))
    return {(r[li], int(r[pi])): r[vi] for r in rows}


def same_word(gloss, value, job):
    """A word-sign gloss agrees with a key value when their first word_prefix letters agree (strip_prefixes dropped)."""
    v = job.get('votes', {})
    a, b = gloss.lstrip('=').lower(), value.lstrip('=').lower()
    for p in v.get('strip_prefixes', []):
        if a.startswith(p) and not b.startswith(p):
            a = a[len(p):]
    n = v.get('word_prefix', 3)
    return a[:n] == b[:n]


# ---------------------------------------------------------------- grading

def grade_tokens(recs, key, exc, votes, job):
    null_values = set(job.get('null_values', ['NULL', 'null']))
    unknown_values = set(job.get('unknown_values', ['', '?']))
    if job.get('empty_is_null'):
        unknown_values.discard(''); null_values.add('')
    uncertain = set(job.get('uncertain_conf', DEFAULT_UNCERTAIN))
    m_sources, m_words = set(job.get('m_sources', [])), job.get('m_words', [])
    s_words = job.get('s_words', [])
    ug, uv, dg = job.get('unkeyed_grade', 'U'), job.get('unkeyed_value', '?'), job.get('default_grade', 'H')
    for r in recs:
        if r['kind'] == 'clear':
            r['value'], r['grade'] = clear_word(r['raw']), 'clear'
            continue
        if r['kind'] != 'sign':
            continue
        k, row = (r['folio'], r['line'], r['pos']), key.get(r['sign'])
        v = row['value'] if row else None
        exc_kept = False
        if k in exc:
            v, g = exc[k]
            exc_kept = bool(job.get('exception_grade_overrides_conf')) and k in exc
        elif v is None or v in unknown_values or (job.get('unknown_if_q') and '?' in v):
            v, g = uv, ug
        elif s_words and any(w in row['note'] for w in s_words):
            vote = votes.get((r['line'], r['pos'])) if votes is not None else None
            g = 'S' if vote is None or vote == v else job.get('disagree_grade', 'M')
        elif row['source'] in m_sources or any(w in row['note'] for w in m_words):
            g = 'M'
        elif votes is not None:
            vote = votes.get((r['line'], r['pos']))
            if vote is not None and (vote == v or (v.startswith('=') and vote.startswith('=')
                                                   and same_word(vote, v, job))):
                g = job.get('voted_grade', 'H')
            elif v.startswith('=') and r['gloss']:
                g = job.get('word_glossed_grade', 'M')
            elif vote is not None and 'disagree_grade' in job:
                g = job['disagree_grade']
            else:
                g = job.get('unvoted_grade', 'S')
        else:
            g = row['grade'] or dg
        if g and g in 'HCS' and (r['conf'] in uncertain or '|' in v) and not (exc_kept and '|' not in v):
            g = 'M'
        r['value'], r['grade'], r['null'] = v, g, v in null_values
    return recs


# ---------------------------------------------------------------- rendering

def lines_of(recs):
    out = collections.OrderedDict()
    for r in recs:
        if r['kind'] == 'line':
            out[r['label']] = dict(label=r['label'], toks=[], gloss_raw=r.get('gloss_raw', ''))
        else:
            out[r['label']]['toks'].append(r)
    return out.values()


def render_concat(recs, job):
    """fr2980-gramont style: 'folio line | ' + values run together; nulls dropped, '·' unkeyed, [xx] word signs."""
    uv = job.get('unkeyed_value', '?')
    res = []
    for L in lines_of(recs):
        s = ''
        for r in L['toks']:
            if r['kind'] == 'sign':
                v = r['value']
                s += '' if r['null'] else '·' if v == uv else f'[{v}]' if len(v) > 1 else v
            elif r['kind'] == 'clear':
                s += f"{{{r['value']}}}"
            elif r['kind'] == 'dot' and 'nonsign' in job:
                s += ' ' if r['sign'] == job.get('word_sep') else r['sign']
        res.append(f"{L['label']} | {s}")
    return res


def render_spaced(recs, job):
    """fr20140-danzay-1557 style: 'line<TAB>' + space-separated values; clear words in CAPS, [code] unkeyed,
    first alternative of 'a|b', <w> for word_values."""
    words, uv = set(job.get('word_values', [])), job.get('unkeyed_value', '?')
    res = []
    for L in lines_of(recs):
        outs = []
        for r in L['toks']:
            if r['kind'] == 'clear':
                outs.append(r['value'].upper())
            elif r['kind'] == 'sign':
                v = r['value']
                if r['grade'] == job.get('unkeyed_grade', 'U') and v == uv:
                    outs.append(f"[{r['sign']}]")
                elif r['null']:
                    outs.append('')
                elif '|' in v:
                    outs.append(v.split('|')[0])
                elif v in words or v.startswith('='):
                    outs.append(f"<{v.lstrip('=')}>")
                else:
                    outs.append(v)
        res.append(f"{L['label']}\t" + ' '.join(o for o in outs if o))
    return res


def render_words(recs, job):
    """dupuy468-anhalt style: 'line  ' + clear words as written, cipher runs UPPER CASE, <WORD> for '=word' word
    signs; a 'lineg' row repeats the gloss when there is one."""
    res = []
    for L in lines_of(recs):
        words, cur = [], []
        for r in L['toks']:
            if r['kind'] == 'clear':
                if cur:
                    words.append(''.join(cur).upper()); cur = []
                words.append(r['value'])
            elif r['kind'] == 'sign':
                v = r['value']
                if v.startswith('='):
                    if cur:
                        words.append(''.join(cur).upper()); cur = []
                    words.append('<' + v[1:].upper() + '>')
                else:
                    cur.append(v)
        if cur:
            words.append(''.join(cur).upper())
        res.append(f"{L['label']}  " + ' '.join(w for w in words if w))
        if L['gloss_raw']:
            res.append(f"{L['label']}g " + L['gloss_raw'])
    return res


STYLES = {'concat': render_concat, 'spaced': render_spaced, 'words': render_words}
DEFAULT_HEADER = ['# Generated by tools/decode_key.py from {name} + key; do not edit.',
                  '# tokens {total}: {HCSMIU} (U = sign not covered by the key)']
DEFAULT_COLUMNS = [['line', 'line'], ['pos', 'pos'], ['sign', 'raw'], ['conf', 'conf'], ['value', 'value'],
                   ['grade', 'grade']]


def run_job(target, job):
    ct = job.get('ciphertext') or next((f for f in ('ciphertext.tsv', 'ciphertext.txt')
                                        if os.path.exists(os.path.join(target, f))), 'ciphertext.tsv')
    path = os.path.join(target, ct)
    fmt = job.get('format') or detect_format(path)
    recs = LOADERS[fmt](path, job)
    key = load_keys(target, job.get('key', 'key.tsv'))
    exc = load_exceptions(os.path.join(target, job.get('exceptions', 'exceptions.tsv')), job)
    grade_tokens(recs, key, exc, load_votes(target, job), job)
    cnt = collections.Counter(r['grade'] for r in recs if r['kind'] == 'sign')
    fields = {g: cnt[g] for g in GRADES}
    fields.update(total=sum(cnt.values()), name=ct, HCSMIU=', '.join(f'{g} {cnt[g]}' for g in GRADES),
                  grades_sorted=', '.join(f'{k} {v}' for k, v in sorted(cnt.items())))
    head = [h.format(**fields) for h in job.get('header', DEFAULT_HEADER)]
    reading = '\n'.join(head + STYLES[job.get('style', 'spaced')](recs, job)) + '\n'
    cols = job.get('token_columns', DEFAULT_COLUMNS)
    tok = ['\t'.join(c[0] for c in cols)]
    for r in recs:
        if r['kind'] == 'sign' or (r['kind'] == 'clear' and job.get('include_clear')):
            tok.append('\t'.join(str(r.get(c[1], '')) for c in cols))
    outputs = {job.get('reading', 'reading.txt'): reading, job.get('tokens', 'reading_tokens.tsv'): '\n'.join(tok) + '\n'}
    return outputs, cnt, ct


# ---------------------------------------------------------------- split check (out-of-key / glued digits)

LOW_GRADES = set('MIU')


def key_range(key):
    """(lo, hi, parts, basis): numeric range of the key's confident codes, the set of codes a split may use, and a
    note on how the range was found. (None, None, all codes, why) when the key is not mostly numeric."""
    codes = list(key)
    num = [c for c in codes if c.isdigit()]
    if len(num) < 5 or len(num) * 2 < len(codes):
        return None, None, set(codes), f'no range ({len(num)} of {len(codes)} codes numeric)'
    conf = [c for c in num if not (key[c]['grade'] or '').strip() or (key[c]['grade'] or '').strip()[0] not in LOW_GRADES]
    basis = conf or num
    lo, hi = min(int(c) for c in basis), max(int(c) for c in basis)
    parts = {c for c in codes if not c.isdigit() or lo <= int(c) <= hi}
    why = f'{len(conf)} confident numeric codes' if conf else f'all {len(num)} numeric codes (none confident)'
    return lo, hi, parts, why


def digit_splits(tok, parts, maxparts=3):
    """Every cut of the digit string tok into 2..maxparts consecutive pieces that are each in parts."""
    out = []
    n = len(tok)
    for i in range(1, n):
        a, b = tok[:i], tok[i:]
        if a in parts and b in parts:
            out.append([a, b])
        if maxparts >= 3 and a in parts:
            for j in range(1, len(b)):
                if b[:j] in parts and b[j:] in parts:
                    out.append([a, b[:j], b[j:]])
    return out


def split_check(target, job):
    """Rows (dicts) for every distinct sign token that is unkeyed or outside the key's confident numeric range."""
    ct = job.get('ciphertext') or next((f for f in ('ciphertext.tsv', 'ciphertext.txt')
                                        if os.path.exists(os.path.join(target, f))), 'ciphertext.tsv')
    path = os.path.join(target, ct)
    fmt = job.get('format') or detect_format(path)
    recs = LOADERS[fmt](path, job)
    key = load_keys(target, job.get('key', 'key.tsv'))
    exc = load_exceptions(os.path.join(target, job.get('exceptions', 'exceptions.tsv')), job)
    lo, hi, parts, why = key_range(key)
    flagged = collections.OrderedDict()
    for r in recs:
        if r['kind'] != 'sign':
            continue
        t = r['sign']
        if t not in key:
            status = 'unkeyed'
        elif lo is not None and t.isdigit() and not lo <= int(t) <= hi:
            status = 'out-of-range'
        else:
            continue
        if t.isdigit() and lo is not None and t not in key and not lo <= int(t) <= hi:
            status = 'unkeyed,out-of-range'
        f = flagged.setdefault(t, dict(token=t, status=status, n=0, positions=[], exceptions=0))
        f['n'] += 1
        f['positions'].append(f"{r['label']}:{r['pos']}")
        f['exceptions'] += (r['folio'], r['line'], r['pos']) in exc
    for f in flagged.values():
        sp = digit_splits(f['token'], parts - {f['token']}) if f['token'].isdigit() else []
        f['splits'] = ['|'.join(s) for s in sp]
        f['decoded'] = [' '.join(key[p]['value'] or '?' for p in s) for s in sp]
    meta = dict(ciphertext=ct, range=(lo, hi), basis=why, signs=sum(r['kind'] == 'sign' for r in recs))
    return list(flagged.values()), meta


SPLIT_TSV_COLUMNS = ['target', 'job', 'key_range', 'token', 'n', 'status', 'positions', 'exceptions', 'splits', 'decoded']


def split_report(target, jobs, tsv=None):
    rows_out, total = [], 0
    for job in jobs:
        rows, meta = split_check(target, job)
        lo, hi = meta['range']
        rng = f'{lo}-{hi}' if lo is not None else '-'
        occ = sum(f['n'] for f in rows)
        withsplit = sum(1 for f in rows if f['splits'])
        print(f"split-check {meta['ciphertext']}: {meta['signs']} signs; key range {rng} ({meta['basis']}); "
              f"{len(rows)} flagged tokens ({occ} occurrences), {withsplit} with a candidate split")
        for f in rows:
            pos = ','.join(f['positions'][:6]) + (f",+{len(f['positions']) - 6}" if len(f['positions']) > 6 else '')
            sp = '; '.join(f'{s}={d}' for s, d in zip(f['splits'], f['decoded'])) or '-'
            print(f"  {f['token']:>12}  x{f['n']:<3} {f['status']:<20} {sp}  [{pos}]")
            rows_out.append([os.path.basename(os.path.normpath(target)), meta['ciphertext'], rng, f['token'], str(f['n']),
                             f['status'], ','.join(f['positions']), str(f['exceptions']),
                             '; '.join(f['splits']) or '-', '; '.join(f['decoded']) or '-'])
        total += len(rows)
    print(f'split-check total: {total} flagged tokens')
    if tsv:
        with open(tsv, 'w', encoding='utf-8') as fh:
            fh.write('\t'.join(SPLIT_TSV_COLUMNS) + '\n')
            for r in rows_out:
                fh.write('\t'.join(c.replace('\t', ' ') for c in r) + '\n')
    return rows_out


def load_config(target, a):
    if a.config or (os.path.exists(os.path.join(target, 'decode.json')) and not a.ciphertext):
        cfg = json.load(open(a.config or os.path.join(target, 'decode.json'), encoding='utf-8'))
        return [dict(cfg.get('defaults', {}), **j) for j in cfg.get('jobs', [cfg])]
    key = a.key.split(',') if a.key and ',' in a.key else a.key
    job = {k: v for k, v in (('ciphertext', a.ciphertext), ('key', key), ('exceptions', a.exceptions),
                             ('style', a.style), ('reading', a.reading), ('tokens', a.tokens)) if v}
    return [job]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('target', help='target folder (ciphers/<name>)')
    ap.add_argument('--check', action='store_true', help='exit 1 if a committed output is stale; write nothing')
    ap.add_argument('--config', help='decode.json path (default TARGET/decode.json)')
    ap.add_argument('--ciphertext'); ap.add_argument('--key'); ap.add_argument('--exceptions')
    ap.add_argument('--style', choices=sorted(STYLES)); ap.add_argument('--reading'); ap.add_argument('--tokens')
    ap.add_argument('--split-check', action='store_true',
                    help='report tokens not in the key or outside its confident numeric range, with every split '
                         'into 2-3 key values (writes no reading; exit 0 unless the target cannot be loaded)')
    ap.add_argument('--split-tsv', help='with --split-check: also write the rows to this TSV file')
    a = ap.parse_args(argv)
    if a.split_check:
        try:
            jobs = load_config(a.target, a)
            split_report(a.target, jobs, a.split_tsv)
        except Exception as e:  # a report: only a target that cannot be loaded is an error
            print(f'split-check: cannot load {a.target}: {type(e).__name__}: {e}', file=sys.stderr)
            return 2
        return 0
    stale = []
    for job in load_config(a.target, a):
        outputs, cnt, ct = run_job(a.target, job)
        print(f"{ct}: tokens {sum(cnt.values())}: " + ', '.join(f'{g} {n}' for g, n in sorted(cnt.items())))
        for f, s in outputs.items():
            p = os.path.join(a.target, f)
            if a.check:
                if not os.path.exists(p) or open(p, encoding='utf-8').read() != s:
                    stale.append(f)
            else:
                open(p, 'w', encoding='utf-8').write(s)
    if a.check:
        print('STALE: ' + ', '.join(stale) if stale else 'reading up to date')
        return 1 if stale else 0
    return 0


if __name__ == '__main__':
    sys.exit(main())
