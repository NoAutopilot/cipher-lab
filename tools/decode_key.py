#!/usr/bin/env python3
"""Apply a substitution key to a reconciled transcription and regenerate the graded reading (CLAUDE.md rules 4 and 7).

  python3 tools/decode_key.py TARGET_DIR                 write the reading(s) described by TARGET_DIR/decode.json
  python3 tools/decode_key.py TARGET_DIR --check         exit 1 if any committed reading differs from a regeneration
  python3 tools/decode_key.py TARGET_DIR --config F      use config file F instead of TARGET_DIR/decode.json
  python3 tools/decode_key.py TARGET_DIR --ciphertext ciphertext.tsv --key key.tsv [--exceptions exceptions.tsv]
                              [--style spaced|concat|words|case] [--reading reading.txt] [--tokens reading_tokens.tsv]
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

--special-scan [--codes a,b] [--min-n 3] [--nulls 50] [--special-tsv F] (9 Oct 2026, MQS-SPECIAL-SIGNS; Lasry, Biermann and
Tomokiyo 2023 p.111, p.115, Fig. 13 p.126, App. B Fig. B24: repeat-previous, delete-previous and null signs). Per code,
every occurrence read as each letter of the model, NULL, REPEAT (the previous sign again) or DELETE (the previous sign
and this one cancelled), scored by the --try window; stat = best minus runner-up. REPEAT/DELETE are flagged only above
the p95 of the same stat over a shuffled-position null (the code's tokens re-inserted at random slots); NULL at >= 2
bits per occurrence (a relocation cannot vary NULL: an inserted token reads NULL anywhere). Meant to catch a sign after
doubled letters (REPEAT) or after a wrong letter (DELETE); must NOT flag an ordinary letter code (D1 decoy 0/10 flagged,
D2 Danzay H letter codes 1/27 flagged). Controls (tools/tests/PREREG-MQS-SPECIAL-SIGNS.md): REPEAT 8/10, DELETE 10/10
(k=3: 9/10), NULL 6/10 (weak; Tomokiyo's Danzay nulls hidden: 1/9). A report: a flag is a candidate for an image
check and --try, never a key edit. decode.json repeat_values / delete_values apply a settled reading of such signs.

--aliases ALIAS.tsv [--alias-out F] [--alias-tsv F] / --alias-scan LANG / --alias-text FILE (9 Oct 2026, MQS-ALIAS; Lasry,
Biermann and Tomokiyo 2023 pp.189-190, 'la Tour' = Throckmorton; Browne 1840 via sp54-maclean-1745). A shared alias.tsv
(alias meaning grade first_use last_use evidence source; 'feigned_name' read as alias, variants 'A, or B') rendered as
'alias [= meaning, G]' beside each codename, G the identification's own grade; token grades unchanged and the committed
reading never written. --alias-scan flags announcement phrases (tools/data/alias_cues_<lang>.tsv) with the referent and
name spans. Meant to catch a whole-word alias and a cue phrase in order; must NOT match inside a longer word
('morris' in 'morrison', 'la tour' in 'la tourelle'), a short alias (< --alias-min-len letters) inside an undivided
letter run, or a cue with its words reordered (tools/tests/test_decode_key_alias.py). Controls
tools/tests/PREREG-MQS-ALIAS.md: --aliases controlled-only, --alias-scan weak (finds only phrasings its cue file carries).

--lookalike A~B[,C~D...] [--lookalike-min 3.0] [--lookalike-tsv F] (9 Oct 2026, MQS-LOOKALIKE-SLIPS; Lasry, Biermann and
Tomokiyo 2023 pp.123-124 Fig. 11, p.136 n.95, App. B pp.198-200: enciphering errors, a sign written for its look-alike
twin). For each declared pair, every occurrence of A is read as B's value and every occurrence of B as A's, ONE position
at a time (the --try window score, +-W tokens, the other occurrences unchanged); gain = twin minus own, in bits; flagged
when gain >= --lookalike-min. Meant to catch a single slip of a twin sign inside otherwise good prose; must NOT flag
an ordinary occurrence of either code (offline fixture and D-control in tools/tests/test_decode_key_lookalike.py). The
pairs come from the person or a glyph atlas, never from this scan. A report: a flag is a candidate for an image check,
never a key, exception or reading edit. Controls and grade: tools/tests/PREREG-MQS-LOOKALIKE-SLIPS.md.

Base and mark (MQS-BASE-MARK, 9 Oct 2026; research/MARY-STUART-TALK-2026-10-09.tsv M11; Lasry, Biermann and Tomokiyo 2023
p.112 n.48, Figs 3-4 p.113: diacritic variants as separate types). A tsv ciphertext with `base` and `mark` columns and no sign
column (tools/sign_sorter_apply.py --split-marks writes them) reads each sign as 'B' (no mark) or 'B:X'. --merge-mark SPEC
(decode.json 'merge_marks', a string or list) reclassifies marks for the whole text in one edit, on any sign of the form
'B:X' (split on the last ':'; marks joined by '+' are treated one by one): 'X' = mark X carries no meaning (dropped),
'X=Y' = mark X is mark Y, '*' = every mark dropped; comma-separated. Applied before the key lookup; the raw sign column of the
token file keeps what was transcribed. Catches: a mark misread page-wide (tick for dot) fixed by one edit instead of every token
relabelled (control K2, tools/tests/PREREG-MQS-BASE-MARK.md). Must NOT: change any sign when no merge is given, or touch a sign
with no ':'. Guard: a merge that makes two keyed codes with different values read as one ('B' and 'B:X', or 'B:X' and 'B:Y')
prints 'merge-mark collapses B:X -> B (value a vs b)' on stderr for each, every run (the merged code then reads the key row
of its new form, as written).

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
  style         spaced | concat | words | case (see render_*; case = grade shown by letter case, MQS-SHEETS 9 Oct 2026)
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
  repeat_values, delete_values  values that mean 'repeat the previous sign' / 'cancel the previous sign' (see
                apply_special; MQS-SPECIAL-SIGNS 9 Oct 2026). Default none: behaviour unchanged.
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

--consistency (8 Oct 2026, TT-CONS; Tomokiyo practice 16, "Breaking a Simple Cipher", sources/cryptiana/web/breaking.htm:
"occurrences of 9(W) in 'wards' and 'with' and those of 24(O) in 'cooperate' and 'you' are consistent"): for every
cipher code used in the reading, the distinct words of the reading it falls in. A word is a run of sign values between
word breaks: the job's word_sep token and any other nonsign token, a clear word, and a word code (a value starting '=',
listed in word_values, containing a space, or 4+ letters long: it is its own word and is not tested; a 2-3 letter
value that only ever stands alone as a whole word, such as a sign for 'the', is counted as a word code too); with
--line-breaks a line end is a break too. A job without word_sep has no word segmentation and is reported as such and
skipped (--segment FILE, a plain text of the reading with spaces between words, supplies one: its letters are aligned
to the reading's letters and its word ends are copied onto the tokens; --auto-segment LEX builds that text with
tools/segmenter.py from an era lexicon, MQS-SEGMENTER 9 Oct 2026, shelf weak, tools/tests/PREREG-MQS-SEGMENTER.md:
boundary F1 0.805 on held-out fr16 prose -- it can mis-divide, so a 'one-word' row under it is a lead, not a finding). Words are compared after folding case and
accents, j->i and v->u. "Unrelated" = different stems: two words sharing their first 4 letters (or equal, under 4
letters) count as ONE stem (cooperate/cooperation, with/without). With --lexicon (a tools/judge_plaintext.py corpus
code such as en, fr16, es18, or a text file) only words found in that corpus's word types count, so a wrong value --
which turns its words into non-words -- loses its words; without --lexicon every word counts and the check can only
show how many contexts a code was READ in, not that they make sense. Categories per code: multi (>=2 unrelated words),
one-stem (several words, one stem), one-word (reported "M-only (one word)"), no-lexicon-word (none of its words in the
lexicon). It is meant to catch a letter value that reads in one word only (a value chosen to make one word come out);
it must NOT flag a code that recurs in two unrelated real words, and it does not regrade anything (rule 4 grades stand;
this is a report). Exit 0 whatever it finds; 2 if the target cannot be loaded. --consistency-tsv FILE writes the rows.

--try CODE=VALUE[,CODE=VALUE...] / --avalanche (9 Oct 2026, MQS-CROSSWORD; the "crossword" or nomenclature phase of
Lasry, Biermann and Tomokiyo 2023, pp.115 n.51 and 118-122: a guessed value is checked at every other occurrence, each
confirmed value opens more words, a guess that fails anywhere is dropped). Promoted from ciphers/fr2980-gramont/
infer_unkeyed.py (24 Sept 2026: the window score and the greedy loop) and test_f30r_top.py (24 Sept and 3 Oct 2026: the
best-minus-current statistic, the shuffled-position null and the no-breakage rule); both are kept, their outputs cited.
  Score of a window: per unbroken segment log2 P + C x length under a character model (C = model bits/char), +-W tokens
  (--window, 8), a value of two or more letters pays 3 bits, a neighbour with no value is filled with the model's
  likeliest letter. Model: --lm fr16 (tools/french16_ngram.py, default), fr18, or a corpus folder. No word segmentation
  is needed, so it also runs where --consistency prints "skipped" (Danzay, Blathwayt).
  --try: hypotheses held in memory only (key.tsv is never written; tested). Each occurrence is printed in context,
  unknown codes as <code>, the hypothesis in [brackets]. Statistic = score(VALUE) - score(current value), or - the
  runner-up among 23 letters + NULL + --words for a code with no value, summed over occurrences; other hypotheses of the
  same call are in place. Null 1: the same statistic for a pseudo-code at n shuffled positions whose current value
  equals this code's (100 draws, --nulls). Null 2: the code's own positions read as random values of VALUE's class (a
  letter: the other letters; a word: the key's values within 1-2 letters of its length). Rule 3: both nulls can move
  the statistic, because it depends on each occurrence's neighbours (null 1 changes the neighbours, null 2 the value);
  a coverage-only or order-only null could not. Verdict: undecided at n = 1 (never rejected), when VALUE is the current
  value (statistic 0, not an error), when a null cannot be built, when the statistic is not above both null p95s, or
  below the acceptance rule; reject when the statistic is <= 0 or (n >= 4) more than a quarter of the occurrences lose
  over 3 bits; accept otherwise. --try-log FILE appends time, target, hypothesis, occurrences, statistic, both p95s,
  verdict and the flag non-blind (real use: ciphers/<t>/crossword_log.tsv; controls: a scratch path).
  --avalanche: infer_unkeyed's greedy loop over the codes with no value and n >= 2 (fix the code whose best value leads
  the runner-up by the largest margin, decode, repeat; --steps K), printing code, value, margin, runner-up, n and the
  acceptance rule (--accept, default margin>=10,n>=5,null=no: fixed on Gramont control draws 0-4). Never writes a key.
  Meant to catch: a wrong guess for a code that recurs (rejected: the right value reads better at its other
  occurrences); a blank whose value the context fixes (proposed first). Must NOT flag: a hypothesis equal to the key
  (zero, undecided), a code seen once (undecided), a true value on a hidden code (not rejected). Offline tests:
  tools/tests/test_decode_key_try.py.
  What failed before (read before trusting a verdict): the same instrument's later Gramont runs accepted almost
  nothing (test_f30r_top.py rounds 1-3, 24 Sept and 3 Oct 2026: HASH and B8 at shuffled-position p 0.61-1.00; E's I
  rejected by the breakage rule; A2-GRA3 accepted one value, ehx = T, and retired the cross shapes at 5, 2 and 1
  occurrences). At low n, and on lines not in the model's language, the shuffled-position null cannot separate: the
  verdict is then "undecided", not a ranking. The 24 Sept control's own limitation (Gramont NOTES.md): "only 25 distinct
  keyed signs could fill the pool, so the draws repeat signs, and the 103 accepted control proposals are not 103
  independent trials."
  Known-answer controls (tools/tests/PREREG-MQS-CROSSWORD.md, per distinct code): K1 Gramont reproduction, 200/200 rows
  identical to control_f30.tsv on the 24 Sept files (155/200, 50/53) and 210/210 identical to infer_unkeyed.py on
  today's files (a port check, no power claim); K3 Danzay letters (fr16, 23 letters + NULL), true letter first for
  19/23 codes (gate 70%, PASS; unigram-only baseline 2/23); K2 Blathwayt words (fr18, true + 9 same-band values),
  58/116 first (gate 70%, FAIL) and false accepts 17/70 at n >= 5 (gate 10%, FAIL; unigram-only baseline 20/116).
  Grading: a value accepted by --try enters a key (by a person or a later job) as M; as S only for a single-letter
  value in a letter cipher of the Danzay/Gramont design (K3 passed); a word or name value stays M (K2 failed); never H
  or C.

Test: python3 tools/tests/test_decode_key.py (reproduces fr2980-gramont, fr20140-danzay-1557 and dupuy468-anhalt
readings from tools/tests/decode_configs/*.json, byte for byte, without writing).
"""
import argparse, collections, json, math, os, random, re, sys, time, unicodedata

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
    bi, mi = (col(header, 'base'), col(header, 'mark')) if si is None else (None, None)
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
        if si is None and bi is not None:  # base/mark columns (MQS-BASE-MARK)
            mk = r[mi] if mi is not None and mi < len(r) else ''
            t = r[bi] + (':' + mk if mk else '')
        else:
            t = r[si]
        conf = r[ki] if ki is not None and ki < len(r) else ''
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

KEY_COLUMN_NAMES = ('code', 'sign', 'token', 'value', 'letter', 'word_or_phrase', 'word', 'plain', 'kind', 'grade',
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
    vi = col(header, 'value', 'letter', 'word_or_phrase', 'word', 'plain')
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

def parse_merge(spec):
    """'tick=dot,flourish' / ['*'] -> {mark: new mark ('' = dropped)}; '*' key drops every mark."""
    if not spec:
        return {}
    parts = spec if isinstance(spec, list) else str(spec).split(',')
    out = {}
    for p in parts:
        p = p.strip()
        if p:
            x, _, y = p.partition('=')
            out[x.strip()] = y.strip()
    return out


def merge_sign(sign, mm):
    """'B:X+Y' under a merge map -> the reclassified sign; a sign with no ':' is returned unchanged."""
    if not mm or ':' not in sign:
        return sign
    base, marks = sign.rsplit(':', 1)
    if '*' in mm:
        return base
    out = []
    for m in marks.split('+'):
        m = mm.get(m, m) if m in mm else m
        if m and m not in out:
            out.append(m)
    return base + (':' + '+'.join(out) if out else '')


def merge_marks(recs, key, job):
    """Apply job['merge_marks'] to every sign record before the key lookup (MQS-BASE-MARK); warn on collapsed key codes."""
    mm = parse_merge(job.get('merge_marks'))
    if not mm:
        return 0
    for c, row in key.items():
        new = merge_sign(c, mm)
        if new != c and new in key and key[new]['value'] != row['value']:
            print(f"merge-mark collapses {c} -> {new} (value {row['value']} vs {key[new]['value']})", file=sys.stderr)
    n = 0
    for r in recs:
        if r.get('kind') == 'sign':
            new = merge_sign(r['sign'], mm)
            if new != r['sign']:
                r['sign'] = new; n += 1
    return n


def grade_tokens(recs, key, exc, votes, job):
    merge_marks(recs, key, job)
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
    apply_special(recs, job)
    return recs


GRADE_ORDER = 'HCSMIU'


def apply_special(recs, job):
    """repeat_values / delete_values (MQS-SPECIAL-SIGNS, 9 Oct 2026; Lasry, Biermann and Tomokiyo 2023 p.111, p.115,
    App. B Fig. B24). A sign whose key value is in repeat_values reads as the previous sign's value (the previous sign
    token of the same job, nulls skipped) and takes the worse of the two grades; one in delete_values cancels the
    previous sign (it becomes a null, 'deleted') and is a null itself. Clear words and dots are not signs and are
    skipped. With neither list set nothing changes. A repeat or delete with no previous sign reads as unkeyed."""
    rep, dele = set(job.get('repeat_values', [])), set(job.get('delete_values', []))
    if not rep and not dele:
        return
    ug, uv = job.get('unkeyed_grade', 'U'), job.get('unkeyed_value', '?')
    prev = []  # stack of earlier sign records that still carry a value
    for r in recs:
        if r['kind'] != 'sign':
            continue
        if r['value'] in rep:
            r['special'] = 'repeat'
            if prev:
                p = prev[-1]
                worse = max(r['grade'], p['grade'], key=lambda g: GRADE_ORDER.find(g) if g in GRADE_ORDER else 9)
                r['value'], r['grade'], r['null'] = p['value'], worse, False
                prev.append(r)
            else:
                r['value'], r['grade'], r['null'] = uv, ug, False
        elif r['value'] in dele:
            r['special'], r['null'] = 'delete', True
            if prev:
                p = prev.pop()
                p['null'], p['special'] = True, 'deleted'
        elif not r.get('null'):
            prev.append(r)


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


def case_token(r, job):
    """One token in the 'case' style (MQS-SHEETS, 9 Oct 2026): H, C, S in CAPITALS; M in lower case; I in lower case
    inside [brackets]; U as <code>; NULL as _ (the CTTS convention); a clear-hand word as {word}. A '=word' word
    value is shown as the word, cased by its grade (no angle brackets: <...> is reserved for U)."""
    if r['kind'] == 'clear':
        return '{' + r['value'] + '}'
    v, g = r['value'], r['grade']
    if r.get('null'):
        return '_'
    if g == job.get('unkeyed_grade', 'U'):
        return '<' + r['sign'] + '>'
    v = v.lstrip('=')
    if g in ('H', 'C', 'S'):
        return v.upper()
    if g == 'I':
        return '[' + v.lower() + ']'
    return v.lower()


def render_case(recs, job):
    """Grade-by-case reading: 'line<TAB>' + space-separated tokens, each cased by its grade (see case_token).
    Declared forms: H/C/S CAPITALS, M lower case, I [lower case in brackets], U <code>, NULL _, clear {word}.
    Unlike render_spaced/render_words, case carries the grade, so a clear-hand word is never upper-cased."""
    res = []
    for L in lines_of(recs):
        outs = [case_token(r, job) for r in L['toks'] if r['kind'] in ('sign', 'clear')]
        res.append(f"{L['label']}\t" + ' '.join(outs))
    return res


STYLES = {'concat': render_concat, 'spaced': render_spaced, 'words': render_words, 'case': render_case}
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


# ---------------------------------------------------------------- consistency (Tomokiyo practice 16)

def fold_word(w):
    """Case, accents, j->i, v->u folded; letters a-z only (digits kept, so a numeral stays visible)."""
    w = unicodedata.normalize('NFKD', w.lower().replace('\u00df', 'ss'))
    w = ''.join(c for c in w if c.isalnum() and not unicodedata.combining(c))
    return w.replace('j', 'i').replace('v', 'u')


def stem_of(w):
    return w[:4] if len(w) >= 4 else w


def load_lexicon(spec):
    """Word types of a judge_plaintext corpus code (en, fr16, ...) or of a text file, folded like the reading's words."""
    if not spec:
        return None
    if os.path.exists(spec):
        texts = [open(spec, encoding='utf-8', errors='replace').read()]
    else:
        import judge_plaintext
        if spec not in judge_plaintext.LANG_CORPORA:
            raise SystemExit(f'--lexicon {spec!r}: neither a file nor a corpus code in judge_plaintext.LANG_CORPORA')
        texts = [judge_plaintext.read_corpus(p) for p in judge_plaintext.LANG_CORPORA[spec]]
    out = set()
    for t in texts:
        out.update(fold_word(w) for w in re.findall(r"[^\W\d_]+", t))
    out.discard('')
    return out


def is_word_code(v, job):
    b = v.lstrip('=')
    return v.startswith('=') or v in set(job.get('word_values', [])) or ' ' in b or len(b) >= 4


def graded_recs(target, job, key_edit=None):
    """The job's records, graded as run_job grades them; key_edit(key) may alter the key first (controls)."""
    ct = job.get('ciphertext') or next((f for f in ('ciphertext.tsv', 'ciphertext.txt')
                                        if os.path.exists(os.path.join(target, f))), 'ciphertext.tsv')
    path = os.path.join(target, ct)
    recs = LOADERS[job.get('format') or detect_format(path)](path, job)
    key = load_keys(target, job.get('key', 'key.tsv'))
    if key_edit:
        key = key_edit(key)
    exc = load_exceptions(os.path.join(target, job.get('exceptions', 'exceptions.tsv')), job)
    grade_tokens(recs, key, exc, load_votes(target, job), job)
    return recs, ct


def segment_words(recs, job, line_breaks=False, segment_text=None):
    """(words, how): words = lists of sign records (letter/syllable values only, nulls dropped), or (None, why)."""
    uv = job.get('unkeyed_value', '?')
    units = [r for r in recs if r['kind'] == 'sign' and not r.get('null')]
    auto = None
    if isinstance(segment_text, tuple) and segment_text[:1] == ('auto',):  # --auto-segment LEX (MQS-SEGMENTER)
        if job.get('word_sep'):
            segment_text = None
        else:
            import segmenter
            letters = ''.join(fold_word(r['value']) for r in units
                              if r['value'] != uv and not is_word_code(r['value'], job))
            segment_text, auto = segmenter.divided(letters, segment_text[2]), segment_text[1]
    if segment_text is not None:
        import difflib
        letters, owner = [], []
        for r in units:
            v = fold_word(r['value']) if r['value'] != uv else '?'
            if is_word_code(r['value'], job):
                continue
            for ch in v:
                letters.append(ch); owner.append(r)
        seg, wid = [], []
        for i, w in enumerate(segment_text.split()):
            for ch in fold_word(w):
                seg.append(ch); wid.append(i)
        sm = difflib.SequenceMatcher(None, letters, seg, autojunk=False)
        word_of = {}
        for op, a1, a2, b1, b2 in sm.get_opcodes():
            if op == 'equal' or (op == 'replace' and a2 - a1 == b2 - b1):
                for k in range(a2 - a1):
                    word_of.setdefault(id(owner[a1 + k]), wid[b1 + k])
        groups = collections.OrderedDict()
        for r in units:
            if id(r) in word_of:
                groups.setdefault(word_of[id(r)], []).append(r)
        warn = '' if sm.ratio() >= 0.8 else '; WARNING: under 0.8, the segment text is not this reading'
        if auto:
            return list(groups.values()), f'--auto-segment {auto} (tools/segmenter.py, shelf weak; {sm.ratio():.3f} letter agreement)'
        return list(groups.values()), f'--segment file ({sm.ratio():.3f} letter agreement{warn})'
    sep = job.get('word_sep')
    if not sep:
        return None, 'no word segmentation (no word_sep in decode.json; --segment FILE supplies one)'
    words, cur = [], []
    def flush():
        if cur:
            words.append(list(cur)); cur.clear()
    for r in recs:
        if r['kind'] == 'line':
            if line_breaks:
                flush()
        elif r['kind'] in ('dot', 'clear'):
            flush()
        elif r['kind'] == 'sign' and not r.get('null'):
            if is_word_code(r['value'], job):
                flush()
            else:
                cur.append(r)
    flush()
    return words, f'word_sep {sep!r} + nonsign tokens, clear words, word codes' + (' + line ends' if line_breaks else '')


CONS_CATS = ('multi', 'one-stem', 'one-word', 'no-lexicon-word')


def consistency(target, job, lexicon=None, line_breaks=False, segment_text=None, key_edit=None):
    """Per-code rows and a meta dict (see the --consistency paragraph of the module docstring)."""
    recs, ct = graded_recs(target, job, key_edit)
    words, how = segment_words(recs, job, line_breaks, segment_text)
    meta = dict(ciphertext=ct, how=how, words=None if words is None else len(words),
                word_codes=len({r['sign'] for r in recs if r['kind'] == 'sign' and not r.get('null')
                                and is_word_code(r['value'], job)}),
                nulls=len({r['sign'] for r in recs if r['kind'] == 'sign' and r.get('null')}))
    if words is None:
        return None, meta
    uv = job.get('unkeyed_value', '?')
    per = collections.OrderedDict()
    for w in words:
        text = ''.join('?' if r['value'] == uv else fold_word(r['value'].split('|')[0]) for r in w)
        for r in w:
            if r['value'] == uv:
                continue
            d = per.setdefault(r['sign'], dict(code=r['sign'], value=r['value'], n=0, grades=collections.Counter(),
                                               words=collections.Counter()))
            d['n'] += 1; d['grades'][r['grade']] += 1; d['words'][text] += 1
    rows = []
    for d in per.values():
        ws = list(d['words'])
        if len(fold_word(d['value'])) >= 2 and ws == [fold_word(d['value'].split('|')[0])]:
            meta['word_codes'] += 1  # a 2-3 letter word sign ('the') that always stands alone as a word: not tested
            continue
        ok = [w for w in ws if '?' not in w and (lexicon is None or w in lexicon)]
        stems = {stem_of(w) for w in ok}
        cat = ('multi' if len(stems) >= 2 else 'one-stem' if len(ok) >= 2 else 'one-word' if len(ok) == 1
               else 'no-lexicon-word' if lexicon is not None else 'one-word')
        d.update(n_words=len(ws), n_ok=len(ok), n_stems=len(stems), category=cat,
                 grade=d['grades'].most_common(1)[0][0],
                 sample=sorted(ok, key=lambda w: -d['words'][w])[:6] or ws[:6])
        rows.append(d)
    return rows, meta


CONS_TSV_COLUMNS = ['target', 'job', 'code', 'value', 'grade', 'grades', 'n', 'words', 'lexicon_words', 'stems',
                    'category', 'sample_words']


def consistency_report(target, jobs, lexicon=None, line_breaks=False, segment_text=None, tsv=None, show='all'):
    out = []
    name = os.path.basename(os.path.normpath(target))
    for job in jobs:
        rows, meta = consistency(target, job, lexicon, line_breaks, segment_text)
        if rows is None:
            print(f"consistency {name} {meta['ciphertext']}: {meta['how']}; skipped")
            continue
        c = collections.Counter(d['category'] for d in rows)
        print(f"consistency {name} {meta['ciphertext']}: {meta['how']}; {meta['words']} words; "
              f"values: {len(rows)}; in >=2 unrelated words: {c['multi']}; one stem only: {c['one-stem']}; "
              f"one-word only: {c['one-word']}" + (f"; no lexicon word: {c['no-lexicon-word']}" if lexicon is not None else '')
              + f"; word codes (not tested): {meta['word_codes']}; null codes: {meta['nulls']}")
        by_g = collections.defaultdict(collections.Counter)
        for d in rows:
            by_g[d['grade']][d['category']] += 1
        for g in sorted(by_g, key=lambda g: GRADES.find(g) if g in GRADES else 99):
            print(f"  grade {g}: " + ', '.join(f'{k} {by_g[g][k]}' for k in CONS_CATS if by_g[g][k]))
        for d in sorted(rows, key=lambda d: (CONS_CATS.index(d['category']), -d['n'])):
            if show != 'all' and d['category'] == 'multi':
                continue
            flag = 'M-only (one word)' if d['category'] == 'one-word' else d['category']
            gr = ','.join(f'{g}{k}' for g, k in sorted(d['grades'].items()))
            print(f"  {d['code']:>8} = {d['value']:<6} x{d['n']:<4} {gr:<10} {flag:<18} "
                  f"words {d['n_words']}, lexicon {d['n_ok']}, stems {d['n_stems']}: {' '.join(d['sample'])}")
            
        for d in rows:
            out.append([name, meta['ciphertext'], d['code'], d['value'], d['grade'],
                        ','.join(f'{g}{k}' for g, k in sorted(d['grades'].items())), str(d['n']), str(d['n_words']),
                        str(d['n_ok']), str(d['n_stems']), d['category'], ' '.join(d['sample'])])
    if tsv:
        with open(tsv, 'w', encoding='utf-8') as fh:
            fh.write('\t'.join(CONS_TSV_COLUMNS) + '\n')
            for r in out:
                fh.write('\t'.join(c.replace('\t', ' ') for c in r) + '\n')
    return out


# ---------------------------------------------------------------- crossword (--try / --avalanche, MQS-CROSSWORD)

def lm_load(spec=None):
    """The character model for --try/--avalanche: 'fr16' (default, tools/french16_ngram.py as is), a folder name under
    tools/data ('fr18'), or a corpus folder path (every *.txt and *.txt.gz in it)."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import french16_ngram
    if not spec or spec == 'fr16':
        return french16_ngram.load()
    d = spec if os.path.isdir(spec) else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', spec)
    if not os.path.isdir(d):
        raise SystemExit(f'--lm: no corpus folder {spec}')
    return french16_ngram.load(corpus_dir=d)


def lm_fold(v):
    """A key value as the model sees it: '=' and spaces dropped, upper case, accents stripped, J->I, U->V, W->VV."""
    s = unicodedata.normalize('NFD', v.lstrip('='))
    s = ''.join(ch for ch in s if unicodedata.category(ch) != 'Mn').upper()
    return re.sub('[^A-Z]', '', s.replace('J', 'I').replace('U', 'V').replace('W', 'VV'))


class Crossword:
    """Token streams of a target (one per decode.json job, lines run on, dots and nonsign tokens left out) scored
    under a character model, as ciphers/fr2980-gramont/infer_unkeyed.py scores them (MQS-CROSSWORD, 9 Oct 2026).
    Each stream entry is [code, value]: value None = no value (unkeyed or hidden), '' = null, else the folded value;
    a clear word is entry [None, its letters]. A display value ('R', 'NULL', 'COM', 'le') is folded when used."""

    def __init__(self, target, jobs, model, window=8, wpen=3.0, wild=True, key_edit=None):
        self.M, self.W, self.wpen, self.wild = model, window, wpen, wild
        self.C = model.bits_per_char
        self.S, self.cur = [], {}
        for job in jobs:
            recs, _ = graded_recs(target, job, key_edit)
            ug = job.get('unkeyed_grade', 'U')
            s = []
            for r in recs:
                if r['kind'] == 'clear':
                    s.append([None, lm_fold(r['value'] or '')])
                elif r['kind'] == 'sign':
                    v = r['value']
                    if r['grade'] == ug or v in ('?', None):
                        fv = None
                    else:
                        fv = '' if r.get('null') else lm_fold(v.split('|')[0])
                        self.cur.setdefault(r['sign'], collections.Counter())[v] += 1
                    s.append([r['sign'], fv])
            self.S.append(s)
        self.count = collections.Counter(t for s in self.S for t, _ in s if t is not None)
        self._seg = {}

    def current(self, code):
        """The code's display value in the key (its commonest one over occurrences), or None if it has none."""
        c = self.cur.get(code)
        return c.most_common(1)[0][0] if c else None

    def hide(self, codes):
        """The codes lose their value at every position and in current() (a new dict: copies stay intact)."""
        codes = set(codes)
        self.cur = {c: v for c, v in self.cur.items() if c not in codes}
        for s in self.S:
            for e in s:
                if e[0] in codes:
                    e[1] = None

    def fold(self, v):
        return '' if v is None or v.upper() == 'NULL' else lm_fold(v)

    def seg_score(self, seg):
        """infer_unkeyed.seg_score: '?' = no value, filled with the model's likeliest letter (uncharged) when wild."""
        x = self._seg.get(seg)
        if x is not None:
            return x
        M, C = self.M, self.C
        if self.wild:
            out, tot = '', 0.0
            for ch in seg:
                h = out[-(M.order - 1):]
                if ch == '?':
                    out += max(M.alpha, key=lambda a: M.p(h, a))
                else:
                    tot += math.log2(M.p(h, ch)) + C; out += ch
        else:
            tot = sum(M.logp(x) + C * len(x) for x in seg.split('?'))
        self._seg[seg] = tot
        return tot

    def occ(self, code):
        return [(k, i) for k, s in enumerate(self.S) for i, (t, _) in enumerate(s) if t == code]

    def window(self, k, i, code, val, assign):
        cur = ''
        for t, v in self.S[k][max(0, i - self.W):i + self.W + 1]:
            if t == code and code is not None:
                v = val
            elif t in assign:
                v = assign[t]
            cur += '?' if v is None else v
        return cur

    def occ_scores(self, code, val, assign=None, occ=None):
        """One score per occurrence: the window's model score with every occurrence of code read as val (a display
        value), minus wpen for a value of two or more letters (a word sign)."""
        assign = {c: self.fold(v) if v is not None else None for c, v in (assign or {}).items()}
        fv = self.fold(val)
        pen = self.wpen if len(fv) > 1 else 0.0
        return [self.seg_score(self.window(k, i, code, fv, assign)) - pen for k, i in (occ or self.occ(code))]

    def score(self, code, val, assign=None, occ=None):
        return sum(self.occ_scores(code, val, assign, occ))

    def ranked(self, code, cands, assign=None, occ=None):
        """[(score, value)] best first; ties broken as infer_unkeyed breaks them (value string, descending)."""
        return sorted(((self.score(code, v, assign, occ), v) for v in cands), reverse=True)


def avalanche(cw, hidden, cands, steps=None, assign=None):
    """infer_unkeyed.run: greedy, fix the code whose best value leads the runner-up by the largest margin, decode,
    repeat. hidden = codes to assign (their positions must carry no value, see Crossword.hide). Returns
    [(code, value, margin, second, n)] in assignment order. Never writes a key."""
    assign = dict(assign or {})
    out, left = [], [s for s in hidden if cw.count[s]]
    while left and (steps is None or len(out) < steps):
        best = None
        for s in left:
            sc = cw.ranked(s, cands, assign)
            m = sc[0][0] - sc[1][0]
            if best is None or m > best[2]:
                best = (s, sc[0][1], m, sc[1][1])
        assign[best[0]] = best[1]; out.append(best + (cw.count[best[0]],)); left.remove(best[0])
    return out


def parse_accept(spec):
    """'margin>=10,n>=5,null=no' -> dict (infer_unkeyed's acceptance rule, fixed on its control draws 0-4)."""
    r = dict(margin=10.0, n=5, null=False)
    for part in (spec or '').split(','):
        part = part.strip()
        if part.startswith('margin>='):
            r['margin'] = float(part[8:])
        elif part.startswith('n>='):
            r['n'] = int(part[3:])
        elif part.startswith('null='):
            r['null'] = part[5:].lower() in ('yes', 'y', 'true', '1')
    return r


def accepted(value, n, margin, rule):
    return (rule['null'] or value.upper() != 'NULL') and n >= rule['n'] and margin >= rule['margin']


def value_class(cw, val, key_values):
    """Same-class alternatives for the value-class null: a letter -> the model's other letters; a longer value -> the
    key's other values of folded length within 1 (within 2 from 6 letters)."""
    fv = cw.fold(val)
    if len(fv) <= 1:
        return [a for a in cw.M.alpha if a != fv]
    band = 1 if len(fv) < 6 else 2
    seen, out = {fv}, []
    for v in sorted(key_values):
        f = cw.fold(v)
        if f and f not in seen and abs(len(f) - len(fv)) <= band:
            seen.add(f); out.append(v)
    return out


def try_value(cw, code, val, cands, assign=None, nulls=100, seed=0, rule=None, key_values=()):
    """--try for one hypothesis code=val, the other hypotheses (assign) in place. Statistic = score(val) minus
    score(current value), or minus the runner-up among cands when the code has no value; summed over occurrences.
    null_pos: the same statistic for a pseudo-code at n shuffled positions whose current value equals this code's
    (for a code with no value: n random valued positions, hidden); null_val: the code's own positions read as random
    values of val's class. Verdict: accept / reject / undecided (see the module docstring)."""
    rule = rule or parse_accept('')
    rnd = random.Random(seed)
    assign = dict(assign or {}); assign.pop(code, None)
    occ = cw.occ(code); n = len(occ)
    cur = cw.current(code)
    res = dict(code=code, value=val, n=n, current=cur if cur is not None else '')

    def stat_at(occ_, cur_, v, code_=code):
        if cur_ is not None:
            ref = cw.occ_scores(code_, cur_, assign, occ_)
            other = None
        else:
            r = [x for x in cw.ranked(code_, cands, assign, occ_) if cw.fold(x[1]) != cw.fold(v)]
            other = r[0][1] if r else None
            ref = cw.occ_scores(code_, other, assign, occ_) if other is not None else [0.0] * len(occ_)
        got = cw.occ_scores(code_, v, assign, occ_)
        return sum(got) - sum(ref), [a - b for a, b in zip(got, ref)], other

    if n == 0:
        return dict(res, stat=0.0, p95_pos=None, p95_val=None, verdict='undecided', why='no occurrences')
    if cur is not None and cw.fold(cur) == cw.fold(val):
        return dict(res, stat=0.0, p95_pos=None, p95_val=None, verdict='undecided', why='equals the current value')
    st, per, other = stat_at(occ, cur, val)
    res.update(stat=st, ref=cur if cur is not None else (other or ''),
               broken=sum(1 for d in per if d < -3.0))
    # null 1: shuffled positions of matching base value
    fcur = None if cur is None else cw.fold(cur)
    pool = [(k, i) for k, s in enumerate(cw.S) for i, (t, v) in enumerate(s)
            if t is not None and t != code and t not in assign and v is not None and (fcur is None or v == fcur)]
    pos = []
    if len(pool) >= n:
        for _ in range(nulls):
            pick = rnd.sample(pool, n)
            saved = [(k, i, list(cw.S[k][i])) for k, i in pick]
            for k, i in pick:
                cw.S[k][i] = ['\x00pseudo', fcur]   # cur None: hidden
            try:
                pos.append(stat_at(pick, cur, val, '\x00pseudo')[0])
            finally:
                for k, i, e in saved:
                    cw.S[k][i] = e
    # null 2: the code's own positions read as random values of val's class
    alts = [v for v in value_class(cw, val, key_values) if cur is None or cw.fold(v) != fcur]
    vals = []
    if alts:
        for _ in range(nulls):
            vals.append(stat_at(occ, cur, rnd.choice(alts))[0])
    q = lambda xs: sorted(xs)[min(len(xs) - 1, int(0.95 * len(xs)))] if xs else None
    res.update(p95_pos=q(pos), p95_val=q(vals), p_pos=(sum(x >= st for x in pos) / len(pos)) if pos else None,
               p_val=(sum(x >= st for x in vals) / len(vals)) if vals else None)
    if n == 1:
        v, why = 'undecided', 'n = 1'
    elif st <= 0:
        v, why = 'reject', 'no better than ' + ('the current value' if cur is not None else 'the runner-up')
    elif res['broken'] * 4 > n and n >= 4:
        v, why = 'reject', f"breaks {res['broken']} of {n} occurrences by more than 3 bits"
    elif not pos or not vals:
        v, why = 'undecided', 'a null could not be built (too few matching positions or no same-class values)'
    elif st <= res['p95_pos'] or st <= res['p95_val']:
        v, why = 'undecided', 'not above both null p95s (low n or text outside the model language)'
    elif not accepted(val, n, st, rule):
        v, why = 'undecided', 'below the acceptance rule'
    else:
        v, why = 'accept', 'above both nulls and the acceptance rule'
    res.update(verdict=v, why=why)
    return res


def crossword_contexts(cw, code, val, assign=None, width=None):
    """One line per occurrence: the decoded window, unknown codes as <code>, the hypothesis in [brackets]."""
    W = cw.W if width is None else width
    assign = assign or {}
    out = []
    for k, i in cw.occ(code):
        parts = []
        for j in range(max(0, i - W), min(len(cw.S[k]), i + W + 1)):
            t, v = cw.S[k][j]
            if j == i:
                parts.append(f'[{val}]')
            elif t in assign:
                parts.append(str(assign[t]).lower())
            else:
                parts.append(f'<{t}>' if v is None else v.lower() if v else '.')
        out.append(f'  {k}:{i}  ' + ' '.join(parts))
    return out


def word_candidates(key, extra=()):
    return sorted({r['value'] for r in key.values() if len(lm_fold(r['value'])) > 1 and '|' not in r['value']}
                  | set(extra))


# ---------------------------------------------------------------- special signs (--special-scan, MQS-SPECIAL-SIGNS)

SPECIAL_OPS = ('NULL', 'REPEAT', 'DELETE')


def streams_from(model, S, window=8):
    """A Crossword over ready-made streams S (lists of [code, folded value or None]); for synthetic controls."""
    cw = Crossword.__new__(Crossword)
    cw.M, cw.W, cw.wpen, cw.wild, cw.C = model, window, 3.0, True, model.bits_per_char
    cw.S, cw.cur, cw._seg = S, {}, {}
    cw.count = collections.Counter(t for s in S for t, _ in s if t is not None)
    return cw


def render_special(seq, code, interp):
    """The window's letters with every token of code read as interp: a folded letter value, NULL (dropped), REPEAT
    (the previous sign's value again) or DELETE (the previous sign is cancelled, and so is this one); '?' = no value."""
    out = []
    for t, v in seq:
        if t == code and code is not None:
            if interp == 'NULL':
                continue
            if interp == 'REPEAT':
                out.append(out[-1] if out else '?')
            elif interp == 'DELETE':
                if out:
                    out.pop()
            else:
                out.append(interp)
        elif v != '':
            out.append('?' if v is None else v)
    return ''.join(out)


def special_scores(cw, S, code, interps):
    """{interp: summed window score over every occurrence of code in streams S}; a value of 2+ letters pays wpen."""
    occ = [(k, i) for k, s in enumerate(S) for i, (t, _) in enumerate(s) if t == code]
    res = {}
    for it in interps:
        pen = cw.wpen if it not in SPECIAL_OPS and len(it) > 1 else 0.0
        res[it] = sum(cw.seg_score(render_special(S[k][max(0, i - cw.W - 1):i + cw.W + 1], code, it)) - pen
                      for k, i in occ)
    return res, len(occ)


def relocate(S, code, rnd):
    """Shuffled-position null: code's tokens taken out and put back at random token slots of the same streams."""
    T = [[e for e in s if e[0] != code] for s in S]
    n = sum(1 for s in S for e in s if e[0] == code)
    slots = [(k, i) for k, s in enumerate(T) for i in range(len(s) + 1)]
    for k, i in sorted(rnd.sample(slots, n), reverse=True):
        T[k].insert(i, [code, None])
    return T


def special_scan_code(cw, code, letters, nulls=50, seed=0, null_bits=2.0):
    """One row: the code's best interpretation among letters + NULL/REPEAT/DELETE, stat = best minus the runner-up,
    and a flag. REPEAT and DELETE are flagged only above the p95 of the same stat over `nulls` relocations; NULL is
    flagged at >= null_bits per occurrence (a relocation cannot vary it: an inserted token reads NULL anywhere)."""
    cur = cw.current(code)
    interps = list(dict.fromkeys(list(letters) + ([lm_fold(cur)] if cur and lm_fold(cur) and cur.upper() != 'NULL'
                                                   else []) + list(SPECIAL_OPS)))
    sc, n = special_scores(cw, cw.S, code, interps)
    order = sorted(sc, key=lambda x: -sc[x])
    best, second = order[0], order[1]
    stat = sc[best] - sc[second]
    row = dict(code=code, n=n, current=cur or '', best=best, second=second, stat=stat, p95=None, flag='')
    if best == 'NULL' and n and stat / n >= null_bits:
        row['flag'] = 'NULL'
    elif best in ('REPEAT', 'DELETE'):
        rnd, draws = random.Random(seed), []
        for _ in range(nulls):
            T = relocate(cw.S, code, rnd)
            s2, _ = special_scores(cw, T, code, interps)
            others = max(v for k2, v in s2.items() if k2 != best)
            draws.append(s2[best] - others)
        draws.sort()
        row['p95'] = draws[min(len(draws) - 1, int(0.95 * len(draws)))]
        if stat > row['p95']:
            row['flag'] = best
    return row


def special_main(a):
    """--special-scan: prints one row per code (n >= --min-n, or --codes); a report, writes no key or reading."""
    jobs = load_config(a.target, a)
    model = lm_load(a.lm)
    cw = Crossword(a.target, jobs, model, window=a.window)
    codes = a.codes.split(',') if a.codes else [c for c, n in cw.count.most_common() if n >= a.min_n]
    rows = [special_scan_code(cw, c, model.alpha, a.nulls, 0) for c in codes]
    head = 'code\tn\tcurrent\tbest\tsecond\tstat\tp95_reloc\tflag'
    lines = [head] + ['\t'.join([r['code'], str(r['n']), r['current'], r['best'], r['second'], f"{r['stat']:.1f}",
                                  '' if r['p95'] is None else f"{r['p95']:.1f}", r['flag']]) for r in rows]
    print(f'# special-scan: {len(rows)} codes; lm {a.lm or "fr16"}; window {a.window}; relocation draws {a.nulls}; '
          f'flags {sum(1 for r in rows if r["flag"])} (candidates for an image check and decode_key --try, never a key edit)')
    print('\n'.join(lines))
    if a.special_tsv:
        open(a.special_tsv, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    return 0


# ---------------------------------------------------------------- look-alike slips (MQS-LOOKALIKE-SLIPS, 9 Oct 2026)

def parse_pairs(spec):
    """'A~B,C~D' -> [('A', 'B'), ('C', 'D')]."""
    out = []
    for part in (spec or '').split(','):
        part = part.strip()
        if not part:
            continue
        if '~' not in part:
            raise SystemExit(f'--lookalike: expected A~B, got {part!r}')
        a, b = (x.strip() for x in part.split('~', 1))
        if not a or not b or a == b:
            raise SystemExit(f'--lookalike: a pair needs two different codes, got {part!r}')
        out.append((a, b))
    return out


def lookalike_gain(cw, k, i, val):
    """Window score with only position (k, i) read as val (a folded value) minus with its own value; None if either
    is missing. A word value pays wpen as in occ_scores."""
    own = cw.S[k][i][1]
    if own is None or val is None:
        return None
    lo = max(0, i - cw.W)
    seg = ['?' if v is None else v for _, v in cw.S[k][lo:i + cw.W + 1]]
    pen = lambda v: cw.wpen if len(v) > 1 else 0.0
    base = cw.seg_score(''.join(seg)) - pen(own)
    seg[i - lo] = val
    return cw.seg_score(''.join(seg)) - pen(val) - base


def lookalike_scan(cw, pairs, minimum=3.0):
    """One row per examined occurrence: code, twin, stream, index, own, twin value, gain, flag, context."""
    rows = []
    for a, b in pairs:
        for code, twin in ((a, b), (b, a)):
            tv = cw.current(twin)
            ftv = None if tv is None else cw.fold(tv)
            for k, i in cw.occ(code):
                g = lookalike_gain(cw, k, i, ftv)
                if g is None:
                    continue
                s = cw.S[k]
                ctx = ''.join(('?' if v is None else v.lower()) for _, v in s[max(0, i - 6):i]) + '[' + \
                    (s[i][1] or '-') + '>' + (ftv or '-') + ']' + \
                    ''.join(('?' if v is None else v.lower()) for _, v in s[i + 1:i + 7])
                rows.append(dict(code=code, twin=twin, stream=k, index=i, own=s[i][1], twin_value=ftv, gain=g,
                                 flag=g >= minimum, context=ctx))
    return rows


def lookalike_main(a):
    """--lookalike: prints the flagged occurrences (all with --show all); writes no key or reading."""
    jobs = load_config(a.target, a)
    cw = Crossword(a.target, jobs, lm_load(a.lm), window=a.window)
    rows = lookalike_scan(cw, parse_pairs(a.lookalike), a.lookalike_min)
    head = 'code\ttwin\tstream\tindex\town\ttwin_value\tgain\tflag\tcontext'
    lines = [head] + ['\t'.join([r['code'], r['twin'], str(r['stream']), str(r['index']), r['own'], r['twin_value'],
                                  f"{r['gain']:.1f}", 'slip?' if r['flag'] else '', r['context']]) for r in rows]
    shown = [lines[0]] + [l for l, r in zip(lines[1:], rows) if a.show == 'all' or r['flag']]
    print(f"# lookalike: {len(rows)} occurrences examined; flagged {sum(r['flag'] for r in rows)} at gain >= "
          f"{a.lookalike_min} bits; lm {a.lm or 'fr16'}; window {a.window} (candidates for an image check, never a key "
          f"or reading edit; shelf: tools/data/tool_shelf.tsv)")
    print('\n'.join(shown))
    if a.lookalike_tsv:
        open(a.lookalike_tsv, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    return 0


# ---------------------------------------------------------------- aliases (MQS-ALIAS, 9 Oct 2026)

ALIAS_GRADE = re.compile(r'(?<![A-Za-z])([HCSMIU])(?![A-Za-z])')
ALIAS_VARIANTS = re.compile(r'\s*,\s*or\s+|\s*;\s*|\s+or\s+|\s*/\s*')
ALIAS_COLUMNS = ['alias', 'meaning', 'grade', 'first_use', 'last_use', 'evidence', 'source']


def fold_chars(text):
    """(folded, srcs): fold_word per character (case, accents, j->i, v->u); every run of non-letters becomes one
    space. srcs[k] is the index in text of folded character k, so a match can be mapped back to the original."""
    out, srcs = [], []
    for i, c in enumerate(text):
        f = fold_word(c)
        if f:
            out.extend(f); srcs.extend([i] * len(f))
        elif out and out[-1] != ' ':
            out.append(' '); srcs.append(i)
    return ''.join(out), srcs


def alias_grade(cell):
    """The identification's own grade: the last standalone H/C/S/M/I/U in the cell ('H-print, alignment I' -> I);
    M when the cell names none."""
    m = ALIAS_GRADE.findall(cell or '')
    return m[-1] if m else 'M'


def load_aliases(path):
    """Rows of an alias table (schema: alias meaning grade first_use last_use evidence source; 'feigned_name' is read
    as 'alias', so ciphers/sp54-maclean-1745/browne_feigned_names.tsv loads unchanged). An alias cell may list
    variants ('Watson, or Walker'); each variant becomes its own folded pattern."""
    header, rows = with_header(path, ('alias', 'feigned_name', 'row'))
    ia, im, ig = col(header, 'alias', 'feigned_name'), col(header, 'meaning', 'value'), col(header, 'grade')
    if ia is None or im is None:
        raise SystemExit(f'aliases: {path}: needs an alias (or feigned_name) and a meaning column')
    extra = {n: col(header, n) for n in ALIAS_COLUMNS[3:]}
    out = []
    for r in rows:
        cell = lambda i: r[i].strip() if i is not None and i < len(r) else ''
        if not cell(ia):
            continue
        row = dict(alias=cell(ia), meaning=cell(im), grade=alias_grade(cell(ig)),
                   **{n: cell(i) for n, i in extra.items()})
        row['variants'] = [v for v in (fold_chars(x)[0].strip() for x in ALIAS_VARIANTS.split(row['alias'])) if v]
        out.append(row)
    return out


def find_aliases(folded, aliases, bounded=True, min_len=5):
    """[(start, end, row, variant)] in a folded string. bounded: whole words only (an alias never matches inside a
    longer word: 'morris' not in 'morrison'). Unbounded (a letter run with no word divisions): spaces are ignored on
    both sides and a variant of fewer than min_len letters is not looked for (too likely by chance in a run).
    Overlaps keep the earliest, then the longest."""
    hits = []
    if bounded:
        for row in aliases:
            for v in row['variants']:
                for m in re.finditer(r'(?<![a-z0-9])' + re.escape(v) + r'(?![a-z0-9])', folded):
                    hits.append((m.start(), m.end(), row, v))
    else:
        idx = [k for k, c in enumerate(folded) if c != ' ']
        run = ''.join(folded[k] for k in idx)
        for row in aliases:
            for v in row['variants']:
                v2 = v.replace(' ', '')
                if len(v2) < min_len:
                    continue
                for m in re.finditer('(?=' + re.escape(v2) + ')', run):
                    hits.append((idx[m.start()], idx[m.start() + len(v2) - 1] + 1, row, v))
    hits.sort(key=lambda h: (h[0], h[0] - h[1]))
    kept, end = [], -1
    for h in hits:
        if h[0] >= end:
            kept.append(h); end = h[1]
    return kept


def alias_tag(row):
    return f" [= {row['meaning']}, {row['grade']}]"


def annotate_aliases(text, aliases, bounded=True, min_len=5):
    """(annotated text, hits): ' [= meaning, G]' inserted after each alias occurrence; the text is otherwise as given."""
    folded, srcs = fold_chars(text)
    hits = find_aliases(folded, aliases, bounded, min_len)
    out, last = [], 0
    for s, e, row, v in hits:
        cut = srcs[e - 1] + 1
        out.append(text[last:cut] + alias_tag(row)); last = cut
    return ''.join(out) + text[last:], [(srcs[s], srcs[e - 1] + 1, row, v) for s, e, row, v in hits]


def alias_lines(recs, job):
    """[(label, text, char_rec)] per line, a plain view for alias work: sign values run together (nulls dropped,
    '·' for unkeyed, the first of 'a|b'), a '=word' value, a clear word and the job's word_sep as word breaks.
    char_rec[k] is the record behind text[k] (None for a break)."""
    uv = job.get('unkeyed_value', '?')
    out = []
    for L in lines_of(recs):
        text, cr = [], []
        def put(s, r):
            text.extend(s); cr.extend([r] * len(s))
        for r in L['toks']:
            if r['kind'] == 'clear':
                put(' ' + r['value'] + ' ', None)
            elif r['kind'] == 'dot':
                if job.get('word_sep') and r['sign'] == job.get('word_sep'):
                    put(' ', None)
            elif r['kind'] == 'sign' and not r.get('null'):
                v = r['value'].split('|')[0]
                if v == uv and r['grade'] == job.get('unkeyed_grade', 'U'):
                    put('·', r)
                elif v.startswith('='):
                    put(' ', None); put(v[1:], r); put(' ', None)
                else:
                    put(v, r)
        out.append((L['label'], ''.join(text), cr))
    return out


def load_alias_cues(lang):
    """Folded cue word sequences from tools/data/alias_cues_<lang>.tsv (or a path)."""
    path = lang if os.path.exists(lang) else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data',
                                                          f'alias_cues_{lang}.tsv')
    header, rows = with_header(path, ('cue',))
    return [c for c in (fold_chars(r[0])[0].strip() for r in rows if r and r[0].strip()) if c]


def scan_announcements(folded, cues, bounded=True, before=4, after=4):
    """[(start, end, cue, referent, name)]: each cue in the folded text, the `before` words ahead of it (the
    referent: 'monsieur de throckmorton qui') and the `after` words following it (the name span: 'la tour'). bounded:
    the cue matches whole words in order; unbounded: letters with spaces ignored, and the spans are 16 / 12 letters.
    Longer cues win over a cue they contain at the same place. A flag is for a person to read, never an alias row."""
    hits = []
    if bounded:
        for c in cues:
            for m in re.finditer(r'(?<![a-z0-9])' + re.escape(c) + r'(?![a-z0-9])', folded):
                ref = ' '.join(folded[:m.start()].split()[-before:])
                name = ' '.join(folded[m.end():].split()[:after])
                hits.append((m.start(), m.end(), c, ref, name))
    else:
        idx = [k for k, ch in enumerate(folded) if ch != ' ']
        run = ''.join(folded[k] for k in idx)
        for c in cues:
            c2 = c.replace(' ', '')
            for m in re.finditer('(?=' + re.escape(c2) + ')', run):
                s, e = m.start(), m.start() + len(c2)
                hits.append((idx[s], idx[e - 1] + 1, c, run[max(0, s - 16):s], run[e:e + 12]))
    hits.sort(key=lambda h: (h[0], h[0] - h[1]))
    kept, end = [], -1
    for h in hits:
        if h[0] >= end:
            kept.append(h); end = h[1]
        elif h[1] <= end:
            continue
    return kept


def alias_main(a):
    """--aliases / --alias-scan on a target's reading (each decode.json job) or, with --alias-text, on a plain text.
    Writes only --alias-out / --alias-tsv (or stdout); never the committed reading or token file."""
    aliases = load_aliases(a.aliases) if a.aliases else []
    cues = load_alias_cues(a.alias_scan) if a.alias_scan else []
    lines = []  # (job name, label, text, char_rec, bounded)
    if a.alias_text:
        for k, l in enumerate(open(a.alias_text, encoding='utf-8').read().rstrip('\n').split('\n'), 1):
            lines.append(('text', str(k), l, None, True))
    else:
        for job in load_config(a.target, a):
            recs, ct = graded_recs(a.target, job)
            for label, text, cr in alias_lines(recs, job):
                lines.append((ct, label, text, cr, bool(job.get('word_sep'))))
    out, rows = [], []
    for name, label, text, cr, bounded in lines:
        if a.alias_unbounded:
            bounded = False
        if aliases:
            ann, hits = annotate_aliases(text, aliases, bounded, a.alias_min_len)
            out.append(ann if a.alias_text else f'{label}\t{ann}')
            for s, e, row, v in hits:
                recs_hit = []
                for k in range(s, e):
                    if cr and cr[k] is not None and (not recs_hit or recs_hit[-1] is not cr[k]):
                        recs_hit.append(cr[k])
                grades = ''.join(r['grade'] for r in recs_hit)  # one letter per token, as decoded
                rows.append(['alias', name, label, text[s:e], row['alias'], row['meaning'], row['grade'],
                             grades, row.get('evidence', '')])
        if cues:
            folded, srcs = fold_chars(text)
            for s, e, c, ref, nm in scan_announcements(folded, cues, bounded):
                rows.append(['announce', name, label, text[srcs[s]:srcs[e - 1] + 1], c, ref, nm, '', ''])
    if aliases:
        body = '\n'.join(out) + '\n'
        if a.alias_out:
            open(a.alias_out, 'w', encoding='utf-8').write(body)
        else:
            sys.stdout.write(body)
    head = ['kind', 'source', 'line', 'matched', 'alias_or_cue', 'meaning_or_referent', 'grade_or_name',
            'token_grades', 'evidence']
    tsv = '\n'.join('\t'.join(r) for r in [head] + rows) + '\n'
    if a.alias_tsv:
        open(a.alias_tsv, 'w', encoding='utf-8').write(tsv)
    elif cues or not aliases:
        sys.stdout.write(tsv)
    n_a = sum(r[0] == 'alias' for r in rows)
    print(f'aliases: {n_a} alias hits, {len(rows) - n_a} announcement flags (rendering only; token grades unchanged)',
          file=sys.stderr)
    return 0


def load_config(target, a):
    if a.config or (os.path.exists(os.path.join(target, 'decode.json')) and not a.ciphertext):
        cfg = json.load(open(a.config or os.path.join(target, 'decode.json'), encoding='utf-8'))
        return with_merge([dict(cfg.get('defaults', {}), **j) for j in cfg.get('jobs', [cfg])], a)
    key = a.key.split(',') if a.key and ',' in a.key else a.key
    job = {k: v for k, v in (('ciphertext', a.ciphertext), ('key', key), ('exceptions', a.exceptions),
                             ('style', a.style), ('reading', a.reading), ('tokens', a.tokens)) if v}
    return with_merge([job], a)


def with_merge(jobs, a):
    """--merge-mark on the command line overrides each job's merge_marks (MQS-BASE-MARK)."""
    if getattr(a, 'merge_mark', None):
        for j in jobs:
            j['merge_marks'] = a.merge_mark
    return jobs


def crossword_main(a):
    """--try / --avalanche (MQS-CROSSWORD). Prints; appends to --try-log only for --try. Never writes key.tsv."""
    jobs = load_config(a.target, a)
    model = lm_load(a.lm)
    cw = Crossword(a.target, jobs, model, window=a.window)
    key = {}
    for job in jobs:
        for c, r in load_keys(a.target, job.get('key', 'key.tsv')).items():
            key.setdefault(c, r)
    words = [w for w in (a.words or '').split(',') if w]
    cands = list(model.alpha) + ['NULL'] + words
    rule = parse_accept(a.accept)
    if a.avalanche:
        hidden = [c for c, n in cw.count.most_common() if cw.current(c) is None and n >= 2 and '?' not in c]
        print(f'# avalanche: {len(hidden)} codes with no value and n >= 2; candidates {len(cands)}; rule {a.accept}; '
              f'lm {a.lm or "fr16"}; never written to the key')
        print('order\tcode\tvalue\tmargin\tsecond\tn\taccepted')
        for k, (c, v, m, sec, n) in enumerate(avalanche(cw, hidden, cands, a.steps)):
            print(f'{k}\t{c}\t{v}\t{m:.1f}\t{sec}\t{n}\t{"yes" if accepted(v, n, m, rule) else "no"}', flush=True)
        return 0
    hyps = []
    for part in a.try_.split(','):
        if '=' not in part:
            raise SystemExit(f'--try: expected CODE=VALUE, got {part!r}')
        c, v = part.split('=', 1); hyps.append((c.strip(), v.strip()))
    kv = sorted({r['value'] for r in key.values() if '|' not in r['value']} | set(words))
    rows = []
    for c, v in hyps:
        others = {c2: v2 for c2, v2 in hyps if c2 != c}
        r = try_value(cw, c, v, cands, others, a.nulls, 0, rule, kv)
        f = lambda x: '' if x is None else f'{x:.1f}'
        print(f"{c}={v}: n {r['n']}, current {r['current'] or '-'}, statistic {f(r.get('stat'))} bits over "
              f"{r.get('ref') or r['current'] or '-'}; null p95 positions {f(r['p95_pos'])}, value class "
              f"{f(r['p95_val'])}; {r['verdict']} ({r['why']}) [non-blind]")
        for l in crossword_contexts(cw, c, v, others):
            print(l)
        rows.append(r)
    if a.try_log:
        new = not os.path.exists(a.try_log)
        with open(a.try_log, 'a', encoding='utf-8') as fh:
            if new:
                fh.write('time\ttarget\thypothesis\toccurrences\tstatistic\tnull_pos_p95\tnull_val_p95\tverdict\tflag\n')
            t = time.strftime('%Y-%m-%d %H:%M', time.gmtime())
            for r in rows:
                f = lambda x: '' if x is None else f'{x:.1f}'
                fh.write(f"{t}\t{a.target}\t{r['code']}={r['value']}\t{r['n']}\t{f(r.get('stat'))}\t{f(r['p95_pos'])}\t"
                         f"{f(r['p95_val'])}\t{r['verdict']}\tnon-blind\n")
    return 0


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
    ap.add_argument('--consistency', action='store_true',
                    help="Tomokiyo practice 16 (breaking.htm): per cipher code, the distinct words of the reading it "
                         "falls in; 'M-only (one word)' for a code in one word only; words sharing a 4-letter prefix "
                         "count as one stem (related). A report: regrades nothing; needs word_sep in decode.json or "
                         "--segment")
    ap.add_argument('--lexicon', help='with --consistency: count only words found in this corpus (a judge_plaintext '
                                      'corpus code, e.g. en, fr16, es18, or a text file)')
    ap.add_argument('--segment', help='with --consistency: a plain text of the reading with spaces between words')
    ap.add_argument('--auto-segment', metavar='LEX', help='with --consistency: a job without word_sep is divided into '
                    'words by tools/segmenter.py from this lexicon (a judge_plaintext corpus code or a text file); '
                    'shelf weak (MQS-SEGMENTER); a job with word_sep keeps its own breaks')
    ap.add_argument('--line-breaks', action='store_true', help='with --consistency: a line end is a word break')
    ap.add_argument('--consistency-tsv', help='with --consistency: also write the per-code rows to this TSV file')
    ap.add_argument('--show', choices=['all', 'flagged'], default='flagged',
                    help='with --consistency: list every code, or only those not in >=2 unrelated words (default)')
    ap.add_argument('--try', dest='try_', metavar='CODE=VALUE[,CODE=VALUE...]',
                    help='crossword: test guessed values at every occurrence against two nulls (in memory; the key is '
                         'never written); prints each occurrence in context and a verdict accept/reject/undecided')
    ap.add_argument('--avalanche', action='store_true',
                    help='crossword: greedy queue of proposed values for the codes with no value (never written)')
    ap.add_argument('--lm', help='with --try/--avalanche: fr16 (default), fr18, or a corpus folder of *.txt(.gz)')
    ap.add_argument('--window', type=int, default=8, help='with --try/--avalanche: tokens each side (default 8)')
    ap.add_argument('--nulls', type=int, default=100, help='with --try: draws per null (default 100)')
    ap.add_argument('--words', help='with --try/--avalanche: extra word-sign candidates, comma-separated (e.g. ET,COM)')
    ap.add_argument('--accept', default='margin>=10,n>=5,null=no', help='acceptance rule (default %(default)s)')
    ap.add_argument('--steps', type=int, help='with --avalanche: stop after K assignments')
    ap.add_argument('--try-log', help='with --try: append one row per hypothesis to this TSV (real use: '
                                      'ciphers/<t>/crossword_log.tsv; controls: a scratch path)')
    ap.add_argument('--special-scan', action='store_true',
                    help='per code, is it a letter, a NULL, a REPEAT-previous or a DELETE-previous sign? REPEAT/DELETE '
                         'gated on a shuffled-position null (--nulls draws, default 50 here); a report, never a key edit')
    ap.add_argument('--codes', help='with --special-scan: only these codes, comma-separated')
    ap.add_argument('--min-n', type=int, default=3, help='with --special-scan: codes with at least N occurrences (3)')
    ap.add_argument('--special-tsv', help='with --special-scan: also write the rows to this TSV file')
    ap.add_argument('--aliases', metavar='ALIAS.tsv', help='render the reading with "alias [= meaning, G]" after each '
                    'codename in this table (alias.tsv schema; feigned_name read as alias); writes --alias-out or stdout, '
                    'never the committed reading; token grades unchanged (MQS-ALIAS)')
    ap.add_argument('--alias-scan', metavar='LANG', help='flag announcement phrases ("qui s\'apellera entre nous X") '
                    'from tools/data/alias_cues_LANG.tsv (fr, en, it, es) or a cue file path (MQS-ALIAS)')
    ap.add_argument('--alias-text', metavar='FILE', help='with --aliases/--alias-scan: work on this plain text instead '
                    'of the target decode (TARGET is then ignored; pass -)')
    ap.add_argument('--alias-out', help='with --aliases: write the annotated reading here')
    ap.add_argument('--alias-tsv', help='with --aliases/--alias-scan: write the hit and flag rows here')
    ap.add_argument('--alias-min-len', type=int, default=5, help='letters an alias needs to be looked for inside an '
                    'unbounded letter run (default 5)')
    ap.add_argument('--alias-unbounded', action='store_true', help='treat every line as one letter run (no word '
                    'divisions) even when the job has word_sep or the text has spaces')
    ap.add_argument('--lookalike', metavar='A~B[,C~D...]', help='look-alike slips: read each occurrence of A as B '
                    '(and of B as A), one position at a time; flag gain >= --lookalike-min bits (MQS-LOOKALIKE-SLIPS; '
                    'a report, never a key edit)')
    ap.add_argument('--lookalike-min', type=float, default=3.0, help='with --lookalike: flag threshold in bits (3.0)')
    ap.add_argument('--merge-mark', metavar='X[=Y][,..]|*', help='reclassify marks text-wide on B:X signs: X dropped, '
                    'X=Y renamed, * all dropped; warns when two keyed codes collapse (MQS-BASE-MARK)')
    ap.add_argument('--lookalike-tsv', help='with --lookalike: write every examined occurrence to this TSV')
    a = ap.parse_args(argv)
    if a.aliases or a.alias_scan:
        return alias_main(a)
    if a.lookalike:
        return lookalike_main(a)
    if a.special_scan:
        if a.nulls == 100:
            a.nulls = 50
        return special_main(a)
    if a.try_ or a.avalanche:
        return crossword_main(a)
    if a.consistency:
        try:
            jobs = load_config(a.target, a)
            seg = open(a.segment, encoding='utf-8').read() if a.segment else None
            if a.auto_segment and seg is None:
                import segmenter
                seg = ('auto', a.auto_segment, segmenter.Lexicon.load(a.auto_segment))
            consistency_report(a.target, jobs, load_lexicon(a.lexicon), a.line_breaks, seg, a.consistency_tsv, a.show)
        except SystemExit:
            raise
        except Exception as e:
            print(f'consistency: cannot load {a.target}: {type(e).__name__}: {e}', file=sys.stderr)
            return 2
        return 0
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
