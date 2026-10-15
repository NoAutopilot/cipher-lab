#!/usr/bin/env python3
"""parent_report.py: the parent's standard check-in report, one shape every hour (owner, 15 Oct 2026 02:5x UTC: "we should have a
standardized report structure").

Reads only what the repository already holds: ROOM.md (lane claims, worker done lines, usage self-reports), WORK-QUEUE.tsv (rows the
parent queued for other accounts), ASKS.md (desk rows), the keystone target's stats, and tools/usage_watch.py.

  python3 tools/parent_report.py [--since "YYYY-MM-DD HH:MM"] [--keystone ciphers/<t>] [--rows VIV-67C,...] [--md]

Sections, always in this order and never more: 1 USAGE (one line per account: status word, age, reset, live), 2 LANES (one line per
account: lane id, open since, workers done in the window, live), 3 KEYSTONE (the target's gate numbers and the parent-queued rows'
status), 4 FINISHED since --since (one line per done row the parent queued, or per lane result named "for" the parent), 5 WAITING ON
THE OWNER (ASKS desk rows), 6 FLAGS (usage_watch exits, stale claims, ROOM flag lines addressed to the parent). Catches: a check-in that
reports feelings instead of counts; a section silently dropped. Must NOT: read another account's sessions (none can), or invent a number
that is not in a file. Offline test: tools/tests/test_parent_report.py.
"""
import argparse, datetime as dt, json, re, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import account_usage as au  # noqa: E402

LANE_RE = re.compile(r'LANE (DEFAULT-(?:A(\d)-\d{4}-\d{2}|account-(\d)-\d{8}-\d{4})|[A-Z0-9-]+)', re.I)


def parse_room(text):
    rows = []
    for ln in text.splitlines():
        m = au.ROOM_RE.match(ln)
        if m:
            rows.append((dt.datetime.strptime(m.group(1), '%Y-%m-%d %H:%M'), m.group(2), m.group(3)))
    return rows


def lanes(rows, now):
    """{account: {lane, since, done, live_roles}} from DEFAULT/LANE claim lines in the last 24 h and done lines in the window."""
    out = {}
    for when, role, body in rows:
        if (now - when).total_seconds() > 24 * 3600:
            continue
        acct = au.account_of(role) or au.account_of(body[:160])
        m = LANE_RE.search(role)
        if m and acct and body.lower().startswith('claim'):
            out[acct] = dict(lane=m.group(1), since=when.strftime('%H:%M'), done=0)
        if m and acct and body.lower().startswith('done') and acct in out and out[acct]['lane'].lower() == m.group(1).lower():
            out[acct]['closed'] = when.strftime('%H:%M')
    return out


def done_in_window(rows, since):
    n, named = {}, []
    for when, role, body in rows:
        if when < since or not re.match(r'(flag \+ )?done\b', body, re.I):
            continue
        acct = au.account_of(role) or au.account_of(body[:200]) or '?'
        n[acct] = n.get(acct, 0) + 1
        if 'for LANE VIV-KEYSTONE' in body or 'parent' in role.lower():
            named.append((when.strftime('%H:%M'), role.split('(')[0].strip(), body[:220]))
    return n, named


def queue_rows(ids):
    out = []
    p = ROOT / 'WORK-QUEUE.tsv'
    if not p.exists() or not ids:
        return out
    for ln in p.read_text().splitlines()[1:]:
        f = ln.split('\t')
        if f and f[0] in ids:
            out.append((f[0], f[1], f[6][:60]))
    return out


def desk_rows():
    out = []
    p = ROOT / 'ASKS.md'
    if not p.exists():
        return out
    for ln in p.read_text().splitlines():
        if ln.startswith('| ') and re.search(r'\|\s*desk\s*\|\s*$', ln):
            f = [x.strip() for x in ln.strip('|').split('|')]
            out.append((f[0], f[3][:140] if len(f) > 3 else ''))
    return out


def keystone(folder):
    out = {}
    sp = ROOT / folder / 'tx' / 'viv63_f191' / 'stats.json'
    if sp.exists():
        try:
            r = json.loads(sp.read_text())
            out['f191r_longest_all_H_run'] = r['after']['longest_H_run']['letters']
            out['gate'] = 42
        except Exception:
            pass
    head = (ROOT / folder / 'NOTES.md').read_text(errors='ignore').splitlines()[:1] if (ROOT / folder / 'NOTES.md').exists() else []
    out['status'] = head[0].strip() if head else '?'
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--since', default=None)
    ap.add_argument('--keystone', default='ciphers/fr16104-vivonne-spain-1572')
    ap.add_argument('--rows', default='')
    ap.add_argument('--room', default=str(ROOT / 'ROOM.md'))
    ap.add_argument('--now', default=None)
    a = ap.parse_args(argv)
    now = dt.datetime.strptime(a.now, '%Y-%m-%d %H:%M') if a.now else dt.datetime.now(dt.timezone.utc).replace(tzinfo=None)
    since = dt.datetime.strptime(a.since, '%Y-%m-%d %H:%M') if a.since else now - dt.timedelta(hours=1)
    rows = parse_room(Path(a.room).read_text(errors='ignore'))
    pac = now - dt.timedelta(hours=7)
    print(f'PARENT REPORT {now:%Y-%m-%d %H:%M} UTC ({pac:%H:%M} Pacific); window since {since:%H:%M} UTC')
    print('1 USAGE')
    uw = subprocess.run([sys.executable, str(ROOT / 'tools/usage_watch.py'), '--room', a.room] + (['--now', a.now] if a.now else []),
                        capture_output=True, text=True)
    for ln in uw.stdout.splitlines()[1:]:
        print('  ' + ln.strip())
    print('2 LANES')
    L = lanes(rows, now); n_done, named = done_in_window(rows, since)
    live = au.live(Path(a.room).read_text(errors='ignore'), now.replace(tzinfo=dt.timezone.utc))
    for acct in sorted(set(list(L) + list(n_done) + list(live)) - {'?'}):
        l = L.get(acct, {})
        state = f"{l.get('lane', 'no lane')} open since {l.get('since', '--')}" + (f", closed {l['closed']}" if 'closed' in l else '')
        print(f"  account {acct}: {state}; workers done in window {n_done.get(acct, 0)}; live roles {len(live.get(acct, []))}")
    print('3 KEYSTONE')
    k = keystone(a.keystone)
    print(f"  {a.keystone}: {k.get('status', '?')}; f.191r longest all-H run {k.get('f191r_longest_all_H_run', '?')} (gate {k.get('gate', 42)})")
    for jid, acct, st in queue_rows(set(x for x in a.rows.split(',') if x)):
        print(f'  {jid} ({acct}): {st}')
    print(f'4 FINISHED since {since:%H:%M} UTC (rows for the parent)')
    for when, role, body in named or []:
        print(f'  {when} {role}: {body}')
    if not named:
        print('  none')
    print('5 WAITING ON THE OWNER (ASKS desk rows)')
    for rid, txt in desk_rows() or [('--', 'none')]:
        print(f'  ASKS {rid}: {txt}')
    print('6 FLAGS')
    flags = [f"usage_watch exit {uw.returncode}"] if uw.returncode else []
    for when, role, body in rows:
        if when >= since and re.match(r'flag\b', body, re.I) and 'parent' in body.lower():
            flags.append(f"{when:%H:%M} {role[:40]}: {body[:160]}")
    for f in flags or ['none']:
        print('  ' + f)
    return 0


if __name__ == '__main__':
    sys.exit(main())
