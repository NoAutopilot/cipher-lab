#!/usr/bin/env python3
"""VIV-HUMAN scorer (PREREG-VIVHUMAN.md "Scoring rule" and "Interpretation rule"). Run by the parent after the owner answers:

  python3 tools/sign_sorter_apply.py --labels ciphers/fr16104-vivonne-spain-1572/tx/sorter_human/labels.tsv --db DIR \
      --out DIR/settled.tsv --page ciphers/fr16104-vivonne-spain-1572/tx/sorter_human/sorter_viv_human.html
  python3 ciphers/fr16104-vivonne-spain-1572/tx/vivhuman/score.py DIR/settled.tsv [--json OUT.json]
  python3 ciphers/fr16104-vivonne-spain-1572/tx/vivhuman/score.py --selftest   # synthetic exports, no owner answer needed

Per question tile (tx/vivhuman/questions.tsv): final label in the truth set -> correct; a label that is no pile of the page as built
(a page-made new pile) -> 'new sign', wrong unless the truth set is empty; still in 'unsorted' -> unanswered; status not-letter /
aside / bad-cut / taken-out -> wrong, counted apart. Any row with mode 'keyed' voids the run (exit 2).
"""
import csv, json, os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
FOLD = os.path.abspath(os.path.join(HERE, '..', '..'))
Q = os.path.join(HERE, 'questions.tsv')
LABELS = os.path.join(FOLD, 'tx', 'sorter_human', 'labels.tsv')
QPILE = 'unsorted'
MIN_ANSWERED = 19   # Addendum A: of 23 (was 20 of 25)
BAD = ('not-letter', 'aside', 'bad-cut', 'taken-out')


def rd(p):
    return list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))


def questions():
    """The scored questions: Addendum A's excluded tiles (box not on the position's one sign) are not on the page."""
    return [q for q in rd(Q) if not q.get('excluded')]


def classify(q, row, piles):
    T = set(filter(None, q['truth'].split('|')))
    if row is None:
        return 'unanswered'
    st, lab = row.get('status', ''), row.get('new_sign', '')
    if st in BAD:
        return st
    if lab == QPILE:
        return 'unanswered'
    if lab not in piles:
        return 'correct' if not T else 'new-sign'
    return 'correct' if lab in T else 'wrong'


def score(settled_rows, questions, piles):
    if any(r.get('mode', 'blind') == 'keyed' for r in settled_rows):
        raise SystemExit(2)
    by = {r['sid']: r for r in settled_rows}
    per, out = [], {}
    for q in questions:
        c = classify(q, by.get(q['sid']), piles)
        per.append(dict(qid=q['qid'], set=q['set'], sid=q['sid'], truth=q['truth'], answer=(by.get(q['sid']) or {}).get('new_sign', ''), outcome=c))
    for s in ('W', 'R'):
        rs = [p for p in per if p['set'] == s]
        cnt = collections.Counter(p['outcome'] for p in rs)
        out[s] = dict(n=len(rs), correct=cnt['correct'], share=round(cnt['correct'] / len(rs), 4) if rs else None, outcomes=dict(cnt))
    answered = sum(p['outcome'] in ('correct', 'wrong', 'new-sign') for p in per)
    if answered < MIN_ANSWERED:
        verdict = 'incomplete'
    elif out['W']['share'] >= 0.60 and out['R']['share'] >= 0.90:
        verdict = 'a person is an instrument for disputed positions of this hand'
    elif out['W']['share'] < 0.40:
        verdict = 'not an instrument'
    else:
        verdict = 'undecided'
    return dict(answered=answered, W=out['W'], R=out['R'], verdict=verdict, per_tile=per)


def piles_as_built():
    return {r['sign'] for r in rd(LABELS)}


def selftest():
    qs = questions()
    piles = {QPILE} | {t for q in qs for t in q['truth'].split('|') if t} | {'z', 'r', 'S', 'l'}
    def mk(fn):
        return [dict(sid=q['sid'], old_sign=QPILE, new_sign=fn(q), status='moved', mode='blind') for q in qs]
    allright = score(mk(lambda q: q['ref_sign']), qs, piles)
    assert allright['W']['share'] == 1.0 and allright['R']['share'] == 1.0, allright
    assert allright['verdict'].startswith('a person is'), allright['verdict']
    readerB = score(mk(lambda q: q['passB']), qs, piles)           # a person who reads like passB
    assert readerB['R']['share'] == 1.0 and readerB['W']['share'] < 0.60, readerB
    newsign = score(mk(lambda q: 'unsorted-b'), qs, piles)
    assert newsign['W']['outcomes'] == {'new-sign': 12} and newsign['verdict'] == 'not an instrument', newsign
    none = score([], qs, piles)
    assert none['verdict'] == 'incomplete' and none['answered'] == 0
    try:
        score([dict(sid=qs[0]['sid'], new_sign='s', status='moved', mode='keyed')], qs, piles); raise AssertionError('keyed not refused')
    except SystemExit as e:
        assert e.code == 2
    print('selftest ok: all-right', allright['W']['share'], allright['R']['share'], '| passB-like W', readerB['W']['share'],
          readerB['verdict'], '| new-sign', newsign['verdict'], '| empty', none['verdict'], '| keyed refused')


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        selftest(); sys.exit(0)
    res = score(rd(sys.argv[1]), questions(), piles_as_built())
    if '--json' in sys.argv:
        json.dump(res, open(sys.argv[sys.argv.index('--json') + 1], 'w'), indent=1)
    for s in ('W', 'R'):
        print(s, res[s])
    print('answered', res['answered'], '| verdict:', res['verdict'])
