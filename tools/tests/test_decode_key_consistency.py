#!/usr/bin/env python3
"""Offline test for tools/decode_key.py --consistency (TT-CONS, 8 Oct 2026; Tomokiyo practice 16, breaking.htm).
Synthetic fixtures in a scratch folder, plus the breaking.htm fixture (tools/tests/fixtures/tomokiyo-breaking/).
Must flag: a code read in one word only ('M-only (one word)'); a code whose words share a 4-letter stem (one-stem).
Must NOT flag: a code in two unrelated words (multi). No word_sep and no --segment: reported, skipped.
Run: python3 tools/tests/test_decode_key_consistency.py"""
import io, contextlib, os, shutil, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import decode_key as dk

fails = 0
def check(ok, msg):
    global fails
    fails += not ok
    print('PASS' if ok else 'FAIL', msg)

# plaintext "the cat / with wards / cooperate cooperation / zap"; one code per letter except:
#   code 9 = w in 'with' and 'wards' (unrelated: multi); code 50 = c in 'cooperate'/'cooperation' only (one stem:
#   but 'cat' too -> multi). Code 60 = z only in 'zap' (one word). Code 70 = n only in 'cooperation' (one word).
words = ['the', 'cat', 'with', 'wards', 'cooperate', 'cooperation', 'zap']
codes = {}
nxt = [10]
def code_for(ch, w):
    if ch == 'w': return '9'
    if ch == 'z': return '60'
    if ch == 'n': return '70'
    if ch == 'p' and w.startswith('coop'): return '80'   # p in the two cooperat- words only: one stem
    if ch not in codes:
        codes[ch] = str(nxt[0]); nxt[0] += 1
    return codes[ch]
tmp = tempfile.mkdtemp()
try:
    rows, pos = ['line\tpos\tsign\tconf'], 0
    for w in words:
        for ch in w:
            rows.append(f'L1\t{pos}\t{code_for(ch, w)}\t'); pos += 1
        rows.append(f'L1\t{pos}\t/\t'); pos += 1
    open(os.path.join(tmp, 'ciphertext.tsv'), 'w').write('\n'.join(rows) + '\n')
    key = {'9': 'w', '60': 'z', '70': 'n', '80': 'p', **{v: k for k, v in codes.items()}}
    open(os.path.join(tmp, 'key.tsv'), 'w').write('code\tvalue\n' + ''.join(f'{c}\t{v}\n' for c, v in key.items()))
    job = {'ciphertext': 'ciphertext.tsv', 'key': 'key.tsv', 'word_sep': '/', 'nonsign': ['/']}
    rows, meta = dk.consistency(tmp, job)
    by = {d['code']: d for d in rows}
    check(meta['words'] == 7, f"7 words from the '/' separators (got {meta['words']})")
    check(by['9']['category'] == 'multi', "code 9 (w in 'with' and 'wards') is multi -- not flagged")
    check(by['60']['category'] == 'one-word', "code 60 (z in 'zap' only) is one-word (M-only)")
    check(by['70']['category'] == 'one-word', "code 70 (n in 'cooperation' only) is one-word")
    check(by['80']['category'] == 'one-stem', "code 80 (p in 'cooperate' and 'cooperation') is one-stem: related words")
    check(by[codes['c']]['category'] == 'multi', "c in 'cat' and 'cooperat-' is multi")
    # a 2-3 letter word sign standing alone as a word ('the') is a word code, not tested
    wd = os.path.join(tmp, 'w'); os.mkdir(wd)
    seq = ['T', '/', '1', '2', '3', '/', 'T', '/', '4', '5', '6']
    open(os.path.join(wd, 'ciphertext.tsv'), 'w').write('line\tpos\tsign\tconf\n' + ''.join(
        f'L1\t{i}\t{t}\t\n' for i, t in enumerate(seq)))
    open(os.path.join(wd, 'key.tsv'), 'w').write('code\tvalue\nT\tthe\n1\tc\n2\ta\n3\tt\n4\td\n5\to\n6\tg\n')
    rw, mw = dk.consistency(wd, {'ciphertext': 'ciphertext.tsv', 'key': 'key.tsv', 'word_sep': '/', 'nonsign': ['/']})
    check(all(d['code'] != 'T' for d in rw) and mw['word_codes'] == 1, "a sign for 'the' standing alone is a word code, not M-only")
    # lexicon: a word not in the lexicon does not count
    lexf = os.path.join(tmp, 'lex.txt'); open(lexf, 'w').write('the cat with wards cooperate cooperation\n')
    rows2, _ = dk.consistency(tmp, job, dk.load_lexicon(lexf))
    by2 = {d['code']: d for d in rows2}
    check(by2['60']['category'] == 'no-lexicon-word', "with a lexicon lacking 'zap', code 60 is no-lexicon-word")
    check(by2['9']['category'] == 'multi', 'with the lexicon, code 9 stays multi')
    # wrong value: 9 -> k makes 'kith'?? not in lexicon, 'kards' not either: 9 loses its words
    rows3, _ = dk.consistency(tmp, job, dk.load_lexicon(lexf), key_edit=lambda k: {**k, '9': dict(k['9'], value='k')})
    check({d['code']: d for d in rows3}['9']['category'] == 'no-lexicon-word', 'a wrong value for code 9 loses its lexicon words')
    # no word_sep: skipped with a reason
    rows4, meta4 = dk.consistency(tmp, {'ciphertext': 'ciphertext.tsv', 'key': 'key.tsv', 'nonsign': ['/']})
    check(rows4 is None and 'no word segmentation' in meta4['how'], 'no word_sep: "no word segmentation", skipped')
    # --segment: a spaced plain text supplies the word ends instead
    rows5, meta5 = dk.consistency(tmp, {'ciphertext': 'ciphertext.tsv', 'key': 'key.tsv'},
                                  segment_text=' '.join(words))
    by5 = {d['code']: d for d in rows5}
    check(meta5['words'] == 7 and by5['9']['category'] == 'multi' and by5['60']['category'] == 'one-word',
          f"--segment text gives the same words ({meta5['how']})")
    # CLI: exit 0 and the summary line
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = dk.main([tmp, '--ciphertext', 'ciphertext.tsv', '--key', 'key.tsv', '--consistency'])
    out = buf.getvalue()
    check(rc == 0 and 'skipped' in out, 'CLI without word_sep reports and exits 0')
    open(os.path.join(tmp, 'decode.json'), 'w').write('{"ciphertext": "ciphertext.tsv", "key": "key.tsv", '
                                                      '"word_sep": "/", "nonsign": ["/"]}')
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = dk.main([tmp, '--consistency', '--consistency-tsv', os.path.join(tmp, 'c.tsv')])
    out = buf.getvalue()
    check(rc == 0 and 'values: ' in out and 'M-only (one word)' in out and os.path.exists(os.path.join(tmp, 'c.tsv')),
          'CLI with word_sep: summary line, M-only rows, TSV written')
    check(not any(f.startswith('reading') for f in os.listdir(tmp)), '--consistency writes no reading')
finally:
    shutil.rmtree(tmp)
# Tomokiyo's own case: 9(W) and 24(O) consistent (breaking.htm)
fx = os.path.join(ROOT, 'tools', 'tests', 'fixtures', 'tomokiyo-breaking')
rows, meta = dk.consistency(fx, {'ciphertext': 'ciphertext.tsv', 'key': 'key.tsv', 'word_sep': '-', 'nonsign': ['-']})
by = {d['code']: d for d in rows}
check(by['9']['category'] == 'multi' and by['24']['category'] == 'multi' and 'with' in by['9']['words']
      and 'you' in by['24']['words'], "breaking.htm: 9 (with, wards...) and 24 (you, cooperate...) multi")
print(f'decode_key --consistency: {fails} failures')
sys.exit(1 if fails else 0)
