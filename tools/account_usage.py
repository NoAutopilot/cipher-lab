#!/usr/bin/env python3
"""account_usage.py: the usage bars of every account in one view (owner's ask, 3 Oct 2026).

No account can see another's sessions or rate limits, so this reads what every account already writes to the
shared repository, plus one register built for this purpose:

  ROOM.md     live workers: a role whose latest claim/halfway line is newer than its latest done line, within 6 h
  USAGE.tsv   the real usage bars (percent of the 5-hour and 7-day windows, account-wide, so every session and
              subagent on the account is in them), posted by the cipher-lab-usage mod in any session that loads it
              (.claude/skills/cipher-lab-usage), at most once per account per 15 min; or by hand with --post

  python3 tools/account_usage.py                  text table for today (UTC)
  python3 tools/account_usage.py --json           the same as JSON (the cipher-lab-usage mod reads this)
  python3 tools/account_usage.py --ref origin/main  read the files at a git ref (no working-tree change)
  python3 tools/account_usage.py --post auto --five 62.5 --five-resets ISO --seven 81 --seven-resets ISO \
      [--live 2] [--source mod] [--push]          append one USAGE.tsv row; 'auto' = this login's account from
                                                  ~/.claude.json accountUuid via ACCOUNTS.tsv (unmapped: 'u<8 hex>');
                                                  --push commits just that row to origin/main without touching the
                                                  working tree or index (safe inside any worker), skipped when the
                                                  account already has a row under --min-age minutes old

No dollar figures (owner, 3 Oct 2026: the bars are what matter). A reading is as fresh as its row's age. ACCOUNTS.tsv
maps the first 8 hex of each login's accountUuid to its number; an unmapped login posts as 'u<8 hex>' until a parent
adds its row. Offline test: tools/tests/test_account_usage.py.
"""
import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
USAGE_HEADER = 'utc\taccount\tfive_pct\tfive_resets\tseven_pct\tseven_resets\tlive\tsource\tnote\n'
ACCOUNTS = 'ACCOUNTS.tsv'  # account_uuid_prefix (8 hex) -> account number; no emails
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
    cols = USAGE_HEADER.strip().split('\t')
    lines = text.splitlines()
    if not lines or lines[0].split('\t') != cols:
        return latest
    for line in lines[1:]:
        f = line.split('\t')
        if len(f) >= 6:
            latest[f[1]] = dict(zip(cols, f))
    return latest


def account_label(ref=None):
    """This login's account number from ~/.claude.json accountUuid via ACCOUNTS.tsv, else 'u<8 hex>'."""
    try:
        uuid = json.loads((Path.home() / '.claude.json').read_text())['oauthAccount']['accountUuid'][:8]
    except Exception:
        return 'unknown'
    for line in read(ACCOUNTS, ref).splitlines()[1:]:
        f = line.split('\t')
        if len(f) >= 2 and f[0] == uuid:
            return f[1]
    return 'u' + uuid


def summary(ref=None, now=None):
    now = now or dt.datetime.now(dt.timezone.utc)
    lv = live(read('ROOM.md', ref), now)
    us = usage_rows(read('USAGE.tsv', ref))
    accts = sorted(set(lv) | set(us) | {'1', '2', '3', '4'})
    rows = []
    for a in accts:
        u = us.get(a, {})
        age = None
        if u.get('utc'):
            t = dt.datetime.strptime(u['utc'], '%Y-%m-%d %H:%M').replace(tzinfo=dt.timezone.utc)
            age = int((now - t).total_seconds() // 60)
        num = lambda k: float(u[k]) if u.get(k) not in (None, '') else None
        rows.append({
            'account': a, 'live': len(lv.get(a, [])), 'live_roles': sorted(lv.get(a, [])),
            'five_pct': num('five_pct'), 'five_resets': u.get('five_resets', ''),
            'seven_pct': num('seven_pct'), 'seven_resets': u.get('seven_resets', ''),
            'age_min': age,
        })
    return {'utc': now.strftime('%Y-%m-%d %H:%M'), 'accounts': rows}


def _git(*a, env=None, check=True):
    import os
    e = dict(os.environ, **(env or {}))
    r = subprocess.run(['git', '-C', str(ROOT), *a], capture_output=True, text=True, env=e)
    if check and r.returncode != 0:
        raise RuntimeError(r.stderr.strip()[:300])
    return r.stdout.strip()


def push_row(row, account, min_age):
    """Append `row` to USAGE.tsv on origin/main by plumbing (temp index; working tree and index untouched)."""
    import os
    import tempfile
    for attempt in range(4):
        _git('fetch', '-q', 'origin', 'main')
        cur = read('USAGE.tsv', 'origin/main')
        if not cur.startswith(USAGE_HEADER):
            cur = USAGE_HEADER  # missing or an older column layout
        last = usage_rows(cur).get(account)
        if last and min_age:
            t = dt.datetime.strptime(last['utc'], '%Y-%m-%d %H:%M').replace(tzinfo=dt.timezone.utc)
            if (dt.datetime.now(dt.timezone.utc) - t).total_seconds() < min_age * 60:
                return 'skipped: fresh row exists'
        body = cur + ('' if cur.endswith('\n') else '\n') + '\t'.join(row) + '\n'
        with tempfile.TemporaryDirectory() as d:
            env = {'GIT_INDEX_FILE': os.path.join(d, 'index')}
            _git('read-tree', 'origin/main', env=env)
            blob = subprocess.run(['git', '-C', str(ROOT), 'hash-object', '-w', '--stdin'], input=body,
                                  capture_output=True, text=True).stdout.strip()
            _git('update-index', '--add', '--cacheinfo', f'100644,{blob},USAGE.tsv', env=env)
            tree = _git('write-tree', env=env)
            msg = f'USAGE: account {account} bars {row[2]}% 5h / {row[4]}% 7d'
            commit = _git('commit-tree', tree, '-p', 'origin/main', '-m', msg)
        if subprocess.run(['git', '-C', str(ROOT), 'push', '-q', 'origin', f'{commit}:refs/heads/main'],
                          capture_output=True).returncode == 0:
            return 'pushed ' + commit[:9]
        import time
        time.sleep(2 ** (attempt + 1))
    return 'push failed after 4 attempts'


def post(args):
    account = account_label() if args.post == 'auto' else args.post
    now = dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M')
    pct = lambda v: '' if v is None else f'{float(v):g}'
    row = [now, account, pct(args.five), args.five_resets or '', pct(args.seven), args.seven_resets or '',
           str(args.live if args.live is not None else ''), args.source or 'manual',
           (args.note or '').replace('\t', ' ')]
    if args.push:
        print(push_row(row, account, args.min_age))
        return
    p = ROOT / 'USAGE.tsv'
    if not p.exists() or not p.read_text().startswith('utc\taccount\tfive_pct'):
        p.write_text(USAGE_HEADER)
    with p.open('a') as f:
        f.write('\t'.join(row) + '\n')
    print('\t'.join(row))


def bar(p, width=10):
    if p is None:
        return '?' * width
    n = max(0, min(width, round(p / 100 * width)))
    return '#' * n + '.' * (width - n)


def text(s):
    lines = [f"Usage bars across accounts, {s['utc']} UTC (5-hour and 7-day windows, whole account)"]
    for r in s['accounts']:
        f = '--' if r['five_pct'] is None else f"{r['five_pct']:g}%"
        v = '--' if r['seven_pct'] is None else f"{r['seven_pct']:g}%"
        age = 'no reading yet' if r['age_min'] is None else f"read {r['age_min']} min ago"
        lines.append(f"  account {r['account']}  5h [{bar(r['five_pct'])}] {f:>5}  7d [{bar(r['seven_pct'])}] {v:>5}"
                     f"  {r['live']} live  ({age})")
    return '\n'.join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--json', action='store_true')
    ap.add_argument('--ref')
    ap.add_argument('--post', metavar='ACCOUNT', help="account number, or 'auto'")
    ap.add_argument('--five', type=float)
    ap.add_argument('--five-resets')
    ap.add_argument('--seven', type=float)
    ap.add_argument('--seven-resets')
    ap.add_argument('--live', type=int)
    ap.add_argument('--source')
    ap.add_argument('--note')
    ap.add_argument('--push', action='store_true')
    ap.add_argument('--min-age', type=int, default=15, help='minutes; with --push, skip if a newer row exists')
    ap.add_argument('--whoami', action='store_true', help="print this login's account label")
    a = ap.parse_args()
    if a.whoami:
        print(account_label())
        return
    if a.post is not None:
        post(a)
        return
    s = summary(a.ref)
    print(json.dumps(s) if a.json else text(s))


if __name__ == '__main__':
    sys.exit(main())
