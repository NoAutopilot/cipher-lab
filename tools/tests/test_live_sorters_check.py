#!/usr/bin/env python3
"""Offline test for tools/live_sorters_check.py (owner rule R06: pages already sent get every later fix; 10 Oct 2026).
Must catch: an older marker, no marker ('none' / blank), a marker newer than the template's, a malformed row; round 2 (10 Oct 2026):
an 'unread' marker, a status that is neither live nor 'retired DATE: reason', a sorter-titled artifact in an Artifact list with no
row (--artifacts), a --record whose page has no marker or matches no row. Must NOT block: a row on the current marker, comment and
blank lines, --warn, another account's rows under --account, a retired row on an old marker, a registry without the status column,
a non-sorter artifact (a deck) or a registered one in the list. Also: --record writes the page's own marker; the committed registry
parses with the documented columns, every row carries a claude.ai artifact URL and a valid status, and every sorter-titled artifact
of account 3's list of 10 Oct 2026 has a row. Run: python3 tools/tests/test_live_sorters_check.py"""
import io, os, subprocess, sys, tempfile, contextlib
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import live_sorters_check as lc

fails = 0
def check(name, ok):
    global fails
    print('PASS' if ok else 'FAIL', name); fails += not ok

def run(*args):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code = lc.main(list(args))
    return code, buf.getvalue()

with tempfile.TemporaryDirectory() as d:
    d = Path(d)
    tpl = d / 'template.html'; tpl.write_text('<!doctype html>\n<meta name="sign-sorter-template" content="2026-10-09.5">\n')
    hdr = '\t'.join(lc.COLS)
    def reg(rows, name='reg.tsv'):
        p = d / name; p.write_text('# a comment line\n\n' + hdr + '\n' + ''.join('\t'.join(r) + '\n' for r in rows)); return str(p)
    U = 'https://claude.ai/artifact/'
    cur = reg([['acct3', 'fresh', U + 'AAA', '2026-10-09.5', 'scratch', '', '']])
    code, out = run('--registry', cur, '--template', str(tpl))
    check('all rows on the current marker: exit 0, "nothing to republish"', code == 0 and '0 stale, 0 bad, 1 on the current template 2026-10-09.5' in out)
    mixed = reg([['acct3', 'arm', U + 'R9G', '2026-10-08.4', 'scratch', '', ''], ['acct3', 'old', U + 'X1', 'none', 'scratch', '', ''],
                 ['acct3', 'blank', U + 'X2', '', 'scratch', '', ''], ['owner', 'new', U + 'X3', '2026-10-10.1', '', '', ''],
                 ['acct3', 'fresh', U + 'AAA', '2026-10-09.5', '', '', '']], 'mixed.tsv')
    code, out = run('--registry', mixed, '--template', str(tpl))
    check('older marker listed as stale', code == 1 and 'stale: re-render and republish  acct3  arm  ' + U + 'R9G  (2026-10-08.4 -> 2026-10-09.5)' in out)
    check("'none' and blank markers listed as stale (pages built before markers)", 'acct3  old ' in out and 'acct3  blank ' in out and out.count('no marker -> 2026-10-09.5') == 2)
    check('a marker newer than the template is listed too, and says so', 'owner  new' in out and 'newer than the template' in out)
    check('summary counts', '4 stale, 0 bad, 1 on the current template' in out)
    code, out = run('--registry', mixed, '--template', str(tpl), '--warn')
    check('--warn: same list, exit 0', code == 0 and out.count('stale: re-render') == 4)
    code, out = run('--registry', mixed, '--template', str(tpl), '--account', 'owner')
    check("--account owner: only the owner's row", code == 1 and out.count('stale: re-render') == 1 and 'owner  new' in out and 'for owner' in out)
    code, out = run('--registry', reg([['acct3', 'fresh', U + 'AAA', '2026-10-09.5', '', '', ''], ['owner', 'new', U + 'X3', '2026-10-08.4', '', '', '']], 'acc.tsv'),
                    '--template', str(tpl), '--account', 'acct3')
    check("NOT blocked: another account's stale row under --account", code == 0)
    code, out = run('--registry', reg([['acct3', 'nourl', '', '2026-10-09.5', '', '', ''], ['acct3', 'chat', 'https://claude.ai/chat/abc', '2026-10-09.5', '', '', '']], 'bad.tsv'),
                    '--template', str(tpl))
    check('a row with no artifact URL, or a chat link, is a bad row and fails', code == 1 and out.count('bad row:') == 2)
    code, out = run('--registry', cur, '--template', str(tpl), '--quiet')
    check('--quiet: the summary line only', code == 0 and out.count('\n') == 1)
    noh = d / 'nohdr.tsv'; noh.write_text('account\tname\nacct3\tx\n')
    check('a registry without the documented columns: exit 2', lc.main(['--registry', str(noh), '--template', str(tpl)]) == 2)

    # round 2: status, unread, the Artifact list, --record
    st = reg([['acct3', 'done', U + 'R1', '2026-10-06.1', '', '', 'retired 2026-10-04: owner said done', ''],
              ['acct3', 'unr', U + 'R2', 'unread', '', '', 'live', ''],
              ['acct3', 'oddst', U + 'R3', '2026-10-09.5', '', '', 'parked', ''],
              ['acct3', 'nodate', U + 'R4', '2026-10-09.5', '', '', 'retired: done', ''],
              ['acct3', 'fresh', U + 'AAA', '2026-10-09.5', '', '', 'live', '']], 'status.tsv')
    code, out = run('--registry', st, '--template', str(tpl))
    check('NOT blocked: a retired row on an old marker is counted retired, not stale', 'acct3  done ' not in out and '1 retired' in out)
    check("an 'unread' marker is stale (never read back)", 'acct3  unr ' in out and 'marker not read back' in out)
    check('a status other than live / "retired DATE: reason" is a bad row', code == 1 and 'bad row: acct3  oddst' in out and 'bad row: acct3  nodate' in out)
    old7 = d / 'old7.tsv'; old7.write_text('\t'.join(c for c in lc.COLS if c != 'status') + '\n' + '\t'.join(['acct3', 'x', U + 'AAA', '2026-10-09.5', '', '', '']) + '\n')
    code, out = run('--registry', str(old7), '--template', str(tpl))
    check('NOT blocked: a registry written before the status column reads (blank status = live)', code == 0 and '1 on the current template' in out)
    lst = d / 'list.txt'; lst.write_text('54 published artifacts:\n- (mine) Gecko Mix Players — ' + U + 'DECK1 — updated 2026-10-08\n'
        '- (mine) Fresh Sign Sorter — ' + U + 'AAA — updated 2026-10-09\n- (mine) Orange 1564 Sign Sorter — ' + U + 'ORANGE — updated 2026-10-06\n'
        '- (mine) Oracle boxes (vivonne): verify the cuts — ' + U + 'VIV — updated 2026-10-10\n'
        '- (mine) WVO 11106 p.2 signs (group reads) — ' + U + 'BERGH — updated 2026-10-10\n- (mine) What the cipher said — ' + U + 'READ1 — updated 2026-10-10\n')
    code, out = run('--registry', cur, '--template', str(tpl), '--artifacts', str(lst))
    check('--artifacts: a sorter-titled artifact with no row is unregistered and fails', code == 1 and 'unregistered: add a row (live or retired)  ' + U + 'ORANGE  Orange 1564 Sign Sorter' in out
          and U + 'VIV' in out and U + 'BERGH' in out and '3 unregistered' in out)
    check('NOT blocked by --artifacts: a deck, a reading page, and a registered sorter page', 'DECK1' not in out and 'READ1' not in out and 'unregistered: add a row (live or retired)  ' + U + 'AAA' not in out)
    code, out = run('--registry', cur, '--template', str(tpl))
    check('without --artifacts the summary says the list was not compared', 'Artifact list not compared' in out)
    rec = reg([['acct3', 'arm', U + 'R9G', 'unread', 'scratch', '', 'live', 'n'], ['acct3', 'other', U + 'X9', '2026-10-06.1', '', '', 'live', '']], 'rec.tsv')
    pg = d / 'page.html'; pg.write_text('<meta name="sign-sorter-template" content="2026-10-09.5"><p>page</p>')
    code, out = run('--record', U + 'R9G', str(pg), '--registry', rec)
    rr = {r['name']: r for r in lc.read_registry(rec)}
    check("--record writes the page's own marker and the time into that row only", code == 0 and rr['arm']['template_marker'] == '2026-10-09.5' and
          rr['arm']['last_republished'].endswith('UTC') and rr['arm']['status'] == 'live' and rr['other']['template_marker'] == '2026-10-06.1')
    nopg = d / 'nomark.html'; nopg.write_text('<p>no marker</p>')
    check('--record refuses a page with no marker (exit 2)', lc.main(['--record', U + 'X9', str(nopg), '--registry', rec]) == 2)
    check('--record refuses a key that matches no row (exit 2)', lc.main(['--record', U + 'NOPE', str(pg), '--registry', rec]) == 2)

# the committed registry and the real template

rows = lc.read_registry()
check('committed registry parses with the documented columns', bool(rows) and all(c in rows[0] for c in lc.COLS))
check('every committed row has a claude.ai artifact URL and a marker cell', all(lc.URL_RE.match(r['artifact_url']) and r['template_marker'] for r in rows))
check('every committed row has a valid status (live, or "retired DATE: reason")', all((r.get('status') or '') == 'live' or lc.RETIRED_RE.match(r.get('status') or '') for r in rows))
ACCT3_SORTERS_2026_10_10 = ('8AEJf4uQPX3ayZs1YteWN3 Cq5vxXXMJ552jZW1K3kbgY VeQnBtERcqsNPBCAJaH4za R9GrLoF1ajudygVjo4d17N H7RbsWg3PxsLGu3wSq4iqT Wn9GbXBcNCxcbMZbU2uqCZ '
  'QWE4NSg4FsFgZqxxsGkDtn U2VPJbNVAm5S5u4ThNTbU1 FDkHh2hqX826r9fdxwXFAF YC3XqFjy3UbbbmGdF6Kkp9 RAh9VG9BPSQphovNuaPEBA Joua9gdmovgTwZdfsCYzUq 4Wk5gRYgvgHePTX1PhneD1 '
  '4bD1wyNphqeK92U6umxkhe QmKUbTmCWUrRHaYqdeZqPH N4PavgZFLNG9eTc9wwrvXk 8F5HZFaYGFFF5Fnr3u9Wb7 MY5dgGHcM7JdaZhpBuiLpa CJoBEX8sy858LwSG868prC RxURcDEas5VU11B95kVoJo '
  'VdudJ5ppAreb4Srd1HnWtR PhfGzg5sxwChK1XMG49UYC RLiTdKMG6BRhoja1yEQY5Y DHiLGFWiqrHxQYzLrFNh6s 3b1kUhxALuBLWhpAqPHPPo HY4WNLmJSrbfNQhVU7bJcB 4LnyBPVKLYLGUfQgp3GcsN '
  'PJeZjH4CR3DNKbKT1ksMRf QPqar47jhKDuns9JpB28Gw S3r5tyz2x72bMo7Av6Aw9r ApBoTekfK9sTAdUjuQdzuz QzrYKYmTB5xu4VZDaC7oba 3HcBvFdR7EJ17VFy8uE7sM '
  'SAbD9if2Lxgp45srQoJn5A').split()
check("every sorter page on account 3's Artifact list of 10 Oct 2026 (34) has a row (the round-2 check found 18 missing)",
      len(ACCT3_SORTERS_2026_10_10) == 34 and not set(ACCT3_SORTERS_2026_10_10) - {lc.art_id(r['artifact_url']) for r in rows})
check('the real template has a marker', bool(lc.current_marker()))
h = subprocess.run([sys.executable, str(ROOT / 'tools' / 'live_sorters_check.py'), '--help'], capture_output=True, text=True)
check('--help works and names the registry', h.returncode == 0 and 'live_sorters.tsv' in h.stdout)
print('ALL PASS' if not fails else f'{fails} FAILED'); sys.exit(1 if fails else 0)
