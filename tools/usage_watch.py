#!/usr/bin/env python3
"""usage_watch.py: every account's latest rate-limit status from what its own sessions wrote (owner, 15 Oct 2026 01:5x UTC,
"you need to track usage for all of them").

No account can read another's rate limits, and USAGE.tsv (the real percent bars) is only filled when a session loads the
cipher-lab-usage mod. So this reads the two registers every account already writes and shows the freshest word per account:

  ROOM.md     any line whose text carries a status word (allowed_warning, allowed, rejected) with an account number
              (role text "account N", "account-N", or "owner account" = 1); the newest such line per account wins
  USAGE.tsv   the percent bars when a session posted them (tools/account_usage.py)

  python3 tools/usage_watch.py [--stale 90] [--json]     table; exit 2 if any account's latest word is allowed_warning or
                                                          rejected (BUDGETS.md scaling rule: no new workers anywhere), exit 1
                                                          if any account with a live claim in the last 6 h has no word newer
                                                          than --stale minutes, else 0
  python3 tools/usage_watch.py --budgets                  also append/replace the "Usage watch" table at the end of BUDGETS.md

Catches: an account running lanes whose last status word is over --stale minutes old (its orchestrator is not reporting), and
a warning posted on one account while another keeps spawning. Must NOT flag as STOP: an idle account (no live claim) whose warning is older than one five-hour window (300 min),
or a line that merely quotes the rule text ("allowed_warning anywhere: no new workers") -- a status word counts only when the
same line names a window ("five_hour", "five-hour", "seven-day", "resets", "window") or a get_session read. Offline test:
tools/tests/test_usage_watch.py.
"""
import argparse, datetime as dt, json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import account_usage as au  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
WORD = re.compile(r'\b(allowed_warning|allowed with warning|rejected|allowed)\b', re.I)
# a reading is the self-report phrase ('usage: five_hour allowed by get_session'), or a status word within 40 characters of a
# window word (five_hour, seven_day, window, rate limit, 'reads'); anything else is prose and is skipped
STATUS_PHRASE = re.compile(r'(?:usage:\s*\S+\s+|(?:five[_ -]hour|seven[_ -]day|window|rate[_ -]?limit|reads?)\b[^.;|]{0,40}?)'
                           r'(allowed_warning|allowed with warning|rejected|allowed)\b'
                           r'|\b(allowed_warning|allowed with warning|rejected|allowed)\b[^.;|]{0,40}?(?:five[_ -]hour|seven[_ -]day|window|rate[_ -]?limit|by get_session)', re.I)
WINDOW = re.compile(r'five[_ -]hour|seven[_ -]day|resets?(At)?\b|window|rate_limit|get_session', re.I)
RESET = re.compile(r'resets?(?:At|\s+at)?\s*:?\s*([0-9]{1,2}:[0-9]{2}\s*UTC(?:\s+[0-9]{1,2}\s+[A-Z][a-z]{2})?|1[0-9]{9})', re.I)


def norm(w):
    w = w.lower()
    return 'allowed_warning' if 'warning' in w else w


def scan_room(text, now, stale_min):
    """{account: {word, when, age_min, reset, line}} newest status word per account, plus live claims per account."""
    latest = {}
    for ln in text.splitlines():
        m = au.ROOM_RE.match(ln)
        if not m:
            continue
        when_s, role, body = m.groups()
        acct = au.account_of(role) or au.account_of(body[:120])
        if not acct:
            continue
        hit = STATUS_PHRASE.search(body)
        if not hit:
            continue  # a status word in result prose ("false rejected 18/20", "allowed_warning anywhere") is not a reading
        when = dt.datetime.strptime(when_s, '%Y-%m-%d %H:%M')
        r = RESET.search(body)
        latest[acct] = dict(word=norm(hit.group(1) or hit.group(2)), when=when_s, age_min=int((now - when).total_seconds() // 60),
                            reset=r.group(1) if r else '', line=body[:160])
    return latest


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--stale', type=int, default=90)
    ap.add_argument('--json', action='store_true')
    ap.add_argument('--budgets', action='store_true')
    ap.add_argument('--room', default=str(ROOT / 'ROOM.md'))
    ap.add_argument('--usage', default=str(ROOT / 'USAGE.tsv'))
    ap.add_argument('--now', default=None, help='UTC "YYYY-MM-DD HH:MM" for tests')
    a = ap.parse_args(argv)
    now = (dt.datetime.strptime(a.now, '%Y-%m-%d %H:%M') if a.now else dt.datetime.now(dt.timezone.utc).replace(tzinfo=None))
    room = Path(a.room).read_text(errors='ignore') if Path(a.room).exists() else ''
    words = scan_room(room, now, a.stale)
    live = au.live(room, now.replace(tzinfo=dt.timezone.utc))
    bars = {}
    up = Path(a.usage)
    if up.exists():
        for ln in up.read_text().splitlines()[1:]:
            f = ln.split('\t')
            if len(f) >= 5 and f[1]:
                bars[f[1]] = dict(utc=f[0], five=f[2], seven=f[4])
    rows, worst = [], 0
    for acct in sorted(set(list(words) + list(live) + ['1', '2', '4'])):
        w = words.get(acct); n_live = len(live.get(acct, []))
        flag = ''
        if w and w['word'] in ('allowed_warning', 'rejected') and (w['age_min'] <= 300 or n_live):
            flag = 'STOP: no new workers anywhere'; worst = max(worst, 2)
        elif w and w['word'] in ('allowed_warning', 'rejected'):
            flag = f"old warning ({w['age_min']} min), idle: not current"
        elif n_live and (not w or w['age_min'] > a.stale):
            flag = f'STALE: {n_live} live, no status word under {a.stale} min'; worst = max(worst, 1)
        b = bars.get(acct, {})
        rows.append(dict(account=acct, word=w['word'] if w else '--', age_min=w['age_min'] if w else None,
                         reset=w['reset'] if w else '', live=n_live, five=b.get('five', ''), seven=b.get('seven', ''),
                         bars_utc=b.get('utc', ''), flag=flag, line=w['line'] if w else ''))
    if a.json:
        print(json.dumps(rows, indent=1))
    else:
        print(f'Usage watch {now:%Y-%m-%d %H:%M} UTC (status words from ROOM.md; bars from USAGE.tsv when posted)')
        for r in rows:
            age = f"{r['age_min']} min ago" if r['age_min'] is not None else 'no word'
            bars_s = f"5h {r['five']}% 7d {r['seven']}% ({r['bars_utc']})" if r['five'] else 'bars not posted'
            print(f"  account {r['account']}  {r['word']:16s} {age:14s} reset {r['reset'] or '--':22s} live {r['live']:2d}  {bars_s}  {r['flag']}")
    if a.budgets:
        bp = ROOT / 'BUDGETS.md'; s = bp.read_text()
        head = '\n## Usage watch (tools/usage_watch.py, rewritten by the parent at every check-in)\n'
        i = s.find(head)
        if i >= 0:
            s = s[:i]
        tbl = [head.rstrip('\n'), f'Read {now:%Y-%m-%d %H:%M} UTC. Status words are each account\'s own ROOM.md self-report; bars need the cipher-lab-usage mod.', '',
               '| account | status word | age (min) | resets | live claims | 5h bar | 7d bar | flag |', '|---|---|---|---|---|---|---|---|']
        for r in rows:
            tbl.append(f"| {r['account']} | {r['word']} | {r['age_min'] if r['age_min'] is not None else '--'} | {r['reset'] or '--'} | {r['live']} | {r['five'] or '--'} | {r['seven'] or '--'} | {r['flag'] or 'ok'} |")
        bp.write_text(s.rstrip('\n') + '\n' + '\n'.join(tbl) + '\n')
    return worst


if __name__ == '__main__':
    sys.exit(main())
