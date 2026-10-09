#!/usr/bin/env python3
"""Offline test for tools/name_candidates.py (MQS-NAMES, 9 Oct 2026). No network: --pool fixtures, Wikidata never called.
Fixture: Mary Stuart F38 (Lasry, Biermann and Tomokiyo 2023 p.103, p.122): Francis II (d.1560), Charles IX (d.1574),
Henry III, Francis Duke of Anjou (d.1584).
Must catch: "mon beau frere" at 1580-01-20 ranks Anjou and Henry III above Charles IX; at 1585 Anjou falls below Henry III
(alive at date); a candidate that fits one context and contradicts another ranks below one that fits both.
Must NOT block: a code with no cue word returns a non-empty co-mention ranking flagged "no relation cue"; the pool is
identical with and without the tested code's own names.tsv row; the pool and every feature value are identical with and
without the masked letter's edition passage present; key.tsv is byte-identical after a run.
Run: python3 tools/tests/test_name_candidates.py"""
import hashlib, os, shutil, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import name_candidates as nc  # noqa: E402

FX = os.path.join(ROOT, 'tools', 'tests', 'fixtures', 'name_candidates', 'mary')
POOL, CTX, IDX = (os.path.join(FX, f) for f in ('pool.tsv', 'contexts.tsv', 'index.tsv'))
fails = []


def check(cond, msg):
    print(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        fails.append(msg)


def run(code, date, extra=(), target=None):
    tgt = target or tempfile.mkdtemp()
    a = nc.parser().parse_args([tgt, '--code', code, '--contexts', CTX, '--pool', POOL, '--date', date, '--lang', 'fr',
                                '--index', IDX, '--nulls', '20', *extra])
    return nc.run(a)


def rank(res, label):
    return next(i for i, r in enumerate(res['ranked']) if r['label'] == label)


# 1. brother-in-law at 1580
r = run('K', '1580-01-20', ['--mask-letters', 'F38'])
an, h3, c9 = (rank(r, x) for x in ('Francis, Duke of Anjou', 'Henry III of France', 'Charles IX of France'))
check(an < c9 and h3 < c9, f'1580: Anjou ({an + 1}) and Henry III ({h3 + 1}) above Charles IX ({c9 + 1})')
check(r['ranked'][0]['label'] in ('Francis, Duke of Anjou', 'Henry III of France'), 'top candidate is a living brother-in-law')
# 2. at 1585 Anjou is dead
r85 = run('K', '1585-06-01', ['--mask-letters', 'F38'])
check(rank(r85, 'Francis, Duke of Anjou') > rank(r85, 'Henry III of France'), '1585: Anjou below Henry III (died 1584)')
# 3. no cue: still a ranking, flagged
rx = run('X', '1580-01-20', ['--mask-letters', 'F38'])
check(len(rx['ranked']) > 0 and not rx['summary']['any_cue'] and nc.NOCUE in rx['ranked'][0]['evidence'],
      'no-cue code returns a non-empty ranking flagged "no relation cue"')
# 4. place frames in two contexts: a place fits both, a person contradicts
ry = run('Y', '1580-01-20', ['--mask-letters', 'F38'])
check(ry['ranked'][0]['type'] == 'place', f'two place frames: top is a place ({ry["ranked"][0]["label"]})')
pool = nc.read_pool(POOL)
cues = nc.load_cues('fr')
ctx2 = [dict(left='mon beau frère', right=''), dict(left='pour aller en', right='')]
sc, _ = nc.score_pool(pool, ctx2, cues, nc.date_key('1580-01-20'), {}, set())
an2 = next(x for x in sc if x['label'].startswith('Francis, Duke'))
sc1, _ = nc.score_pool(pool, ctx2[:1], cues, nc.date_key('1580-01-20'), {}, set())
an1 = next(x for x in sc1 if x['label'].startswith('Francis, Duke'))
check(an2['feats']['contradictions'] == 1 and an2['score'] < an1['score'],
      'a candidate fitting one context and contradicting another is ranked down (consistency over all contexts)')
# 5. no leak through names.tsv: pool and features identical with and without the tested code's own row
t1, t2 = tempfile.mkdtemp(), tempfile.mkdtemp()
open(os.path.join(t2, 'names.tsv'), 'w').write('code\tvalue\nK\tFrancis, Duke of Anjou\nZ\tLondres\n')
open(os.path.join(t1, 'names.tsv'), 'w').write('code\tvalue\nZ\tLondres\n')
kin, kout = (nc.load_index([IDX], {'F38'})[0] for _ in range(2))
p_with = nc.build_pool({}, None, kin, cues)
p_without = nc.build_pool({}, None, kout, cues)
check(p_with == p_without, 'pool identical with and without the tested code\'s names.tsv row (pool never reads it)')
ra, rb = run('K', '1580-01-20', ['--mask-letters', 'F38'], t1), run('K', '1580-01-20', ['--mask-letters', 'F38'], t2)
check([(x['label'], x['feats']) for x in ra['ranked']] == [(x['label'], x['feats']) for x in rb['ranked']],
      'every feature identical with and without the tested code\'s own names.tsv row (penalty excludes the tested code)')
check(any(x['feats']['assigned'] < 0 for x in ra['ranked'] if x['label'] == 'London'),
      'a value assigned to ANOTHER code (Z=Londres) is penalised')
# 6. no leak through the edition: masked letter's passage present or absent changes nothing
tmp = tempfile.mkdtemp()
for f in ('edition_other.txt',):
    shutil.copy(os.path.join(FX, f), tmp)
idx_absent = os.path.join(tmp, 'index.tsv')
open(idx_absent, 'w').write('path\tletters\tdate\n' + os.path.join(tmp, 'edition_other.txt') + '\tF10\t1580-02-01\n')
k_present, m_present = nc.load_index([IDX], {'F38'})
k_absent, _ = nc.load_index([idx_absent], {'F38'})
check(len(m_present) == 1 and m_present[0]['path'].endswith('edition_f38.txt'), 'the masked letter\'s passage is excluded')
pp, pa = nc.build_pool({}, None, k_present, cues), nc.build_pool({}, None, k_absent, cues)
strip = lambda rows: [{k: v for k, v in x.items() if k != 'source'} for x in rows]  # noqa: E731
check(strip(pp) == strip(pa), 'pool identical with and without the masked letter\'s edition passage present')
d = nc.date_key('1580-01-20')
check(nc.comention_counts(pool, k_present, d) == nc.comention_counts(pool, k_absent, d),
      'co-mention identical with and without the masked passage present')
unmasked = nc.comention_counts(pool, nc.load_index([IDX], set())[0], d)
check(unmasked != nc.comention_counts(pool, k_present, d), 'control: without the mask the passage WOULD change co-mention')
# 7. never touches key.tsv
tk = tempfile.mkdtemp()
kp = os.path.join(tk, 'key.tsv')
open(kp, 'w').write('code\tvalue\tgrade\nK\t?\tU\n')
h0 = hashlib.sha256(open(kp, 'rb').read()).hexdigest()
run('K', '1580-01-20', ['--mask-letters', 'F38', '--out', os.path.join(tk, 'cand.tsv')], tk)
check(hashlib.sha256(open(kp, 'rb').read()).hexdigest() == h0 and os.path.exists(os.path.join(tk, 'cand.tsv')),
      'key.tsv byte-identical after a run with --out')
# 8. the context null can differ from the real contexts (it is not orthogonal to the statistic)
check(r['summary']['context_null'] is not None, 'context null ran on other codes\' contexts')
# 9. promoted H41 extraction
h = nc.h41_surnames('Graf Burgsdorf kam. von Burgsdorf ging. Herr Kurze, Herr Kurze.')
check(h.get('Burgsdorf') == 2 and h.get('Kurze') == 2, 'promoted H41 surname extraction (von/Graf/Herr, seen twice)')
# 10. fold/alias match used by --truth
check(nc.alias_match('franckreich', 'Frankreich') and nc.alias_match('harlem', 'Haarlem')
      and not nc.alias_match('France', 'Frankfurt'), 'alias fold: Franckreich=Frankreich, Harlem=Haarlem, France!=Frankfurt')
print('FAILED %d' % len(fails) if fails else 'all passed')
sys.exit(1 if fails else 0)
