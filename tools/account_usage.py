#!/usr/bin/env python3
"""account_usage.py: one view of usage across the accounts (owner's ask, 3 Oct 2026).

No account can see another's sessions or rate limits, so this reads what every account already writes to the
shared repository, plus one register built for this purpose:

  LEDGER.md   worker cost by account (column 4, e.g. "account-4", "account 2 (LANE-A2PUSH)"), per UTC date
  ROOM.md     live workers: a role whose latest claim/halfway line is newer than its latest done line, within 6 h
  USAGE.tsv   each parent's / lane's own rate-limit reading from get_session at check-in (this tool's --post)

  python3 tools/account_usage.py                  text table for today (UTC)
  python3 tools/account_usage.py --json           the same as JSON (the cipher-lab-usage mod reads this)
  python3 tools/account_usage.py --ref origin/main  read the files at a git ref (no working-tree change)
  python3 tools/account_usage.py --post 3 --status allowed_warning --type seven_day --resets 1791014400 \
      --session-cost 321.34 [--live 2] [--note "..."]
                                                  append one USAGE.tsv row (parents/lanes, at every check-in)

Ledger cost lags: a worker is ledgered when archived, so today's figure undercounts running work. The rate-limit
column is only as fresh as each account's last --post. Offline test: tools/tests/test_account_usage.py.
"""
import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
USAGE_HEADER = 'utc\taccount\trl_status\trl_type\tresets_utc\tsession_cost\tlive\tnote\n'
ACCT_RE = re.compile(r'account[ -]?(\d)', re.I)
ROOM_RE = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}) \| (.+?) \| (.*)$')


def read(name, ref):
    if ref:
        r = subprocess.run(['git', '-C', str(ROOT), 'show', f'{ref}:{name}'], capture_output=True, text=True)
        return r.stdout if r.returncode == 0 else ''
    p = ROOT / name
    return p.read_text(errors='ignore') if p.exists() else ''


def account_of(text):
    m = ACCT_RE.search(text)
    return m.group(1) if m else None


def ledger(text, days):
    """{account: {date: [cost, rows]}} for the given 'D Mon YYYY' date strings."""
    out = {}
    for line in text.splitlines():
        cells = [c.strip() for c in line.split('|')]
        if len(cells) < 8 or cells[1] not in days:
            continue
        acct = account_of(cells[4]) or account_of(cells[2])
        try:
            cost = float(cells[6])
        except ValueError:
            continue
        if not acct:
            continue
        d = out.setdefault(acct, {}).setdefault(cells[1], [0.0, 0])
        d[0] += cost
        d[1] += 1
    return out


def live(text, now, hours=6):
    """{account: [roles]} whose latest claim/halfway is newer than their latest done, within `hours`."""
    last = {}
    for line in text.splitlines():
        m = ROOM_RE.match(line)
        if not m:
            continue
        t = dt.datetime.strptime(m.group(1), '%Y-%m-%d %H:%M').replace(tzinfo=dt.timezone.utc)
        role, sig = m.group(2), m.group(3).lower()
        key = role.split(':')[0].strip()
        if sig.startswith('done') or ' done' in sig[:12]:
            last[key] = ('done', t)
        elif sig.startswith('claim') or sig.startswith('halfway'):
            if last.get(key, ('', None))[0] != 'open':
                last[key] = ('open', t)
    out = {}
    for role, (state, t) in last.items():
        if state == 'open' and (now - t).total_seconds() < hours * 3600:
            a = account_of(role)
            if a:
                out.setdefault(a, []).append(role)
    return out


def usage_rows(text):
    latest = {}
    for line in text.splitlines()[1:]:
        f = line.split('\t')
        if len(f) >= 7:
            latest[f[1]] = dict(zip(USAGE_HEADER.strip().split('\t'), f))
    return latest


def summary(ref=None, now=None):
    now = now or dt.datetime.now(dt.timezone.utc)
    fmt = lambda d: f'{d.day} {d.strftime("%b")} {d.year}'.replace('Sep ', 'Sept ')
    today, yday = fmt(now), fmt(now - dt.timedelta(days=1))
    led = ledger(read('LEDGER.md', ref), {today, yday})
    lv = live(read('ROOM.md', ref), now)
    us = usage_rows(read('USAGE.tsv', ref))
    accts = sorted(set(led) | set(lv) | set(us) | {'1', '2', '3', '4'})
    rows = []
    for a in accts:
        l = led.get(a, {})
        u = us.get(a, {})
        rows.append({
            'account': a,
            'cost_today': round(l.get(today, [0, 0])[0], 2), 'rows_today': l.get(today, [0, 0])[1],
            'cost_yesterday': round(l.get(yday, [0, 0])[0], 2),
            'live': len(lv.get(a, [])), 'live_roles': sorted(lv.get(a, [])),
            'rl_status': u.get('rl_status', '?'), 'rl_type': u.get('rl_type', ''),
            'resets_utc': u.get('resets_utc', ''), 'rl_seen_utc': u.get('utc', ''),
        })
    return {'utc': now.strftime('%Y-%m-%d %H:%M'), 'today': today, 'accounts': rows}


def post(args):
    p = ROOT / 'USAGE.tsv'
    if not p.exists():
        p.write_text(USAGE_HEADER)
    resets = ''
    if args.resets:
        resets = dt.datetime.fromtimestamp(int(args.resets), dt.timezone.utc).strftime('%Y-%m-%d %H:%M')
    now = dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M')
    row = [now, str(args.post), args.status or '', args.type or '', resets, args.session_cost or '',
           str(args.live if args.live is not None else ''), (args.note or '').replace('\t', ' ')]
    with p.open('a') as f:
        f.write('\t'.join(row) + '\n')
    print('\t'.join(row))


def text(s):
    lines = [f"Usage across accounts, {s['utc']} UTC (ledger = archived workers only)",
             'acct  live  ledger today  (rows)  yesterday  rate limit (as of)']
    for r in s['accounts']:
        rl = f"{r['rl_status']} {r['rl_type']}".strip()
        if r['resets_utc']:
            rl += f", resets {r['resets_utc']}"
        if r['rl_seen_utc']:
            rl += f" (seen {r['rl_seen_utc'][11:]})"
        lines.append(f"  {r['account']}   {r['live']:>3}   ${r['cost_today']:>8.2f}  ({r['rows_today']:>3})  "
                     f"${r['cost_yesterday']:>8.2f}  {rl}")
    return '\n'.join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--json', action='store_true')
    ap.add_argument('--ref')
    ap.add_argument('--post', type=int, metavar='ACCOUNT')
    ap.add_argument('--status')
    ap.add_argument('--type')
    ap.add_argument('--resets', help='epoch seconds (get_session rate_limit_info.resetsAt)')
    ap.add_argument('--session-cost')
    ap.add_argument('--live', type=int)
    ap.add_argument('--note')
    a = ap.parse_args()
    if a.post is not None:
        post(a)
        return
    s = summary(a.ref)
    print(json.dumps(s) if a.json else text(s))


if __name__ == '__main__':
    sys.exit(main())
