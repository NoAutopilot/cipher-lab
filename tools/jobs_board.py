#!/usr/bin/env python3
"""jobs_board.py: every job across the accounts, grouped by project, with its state (owner, 3 Oct 2026).

No account can see another's sessions, so the board is built from the two shared registers every account writes:
  ROOM.md         claim / halfway / done lines (all accounts, all roles), with the account in the role
  WORK-QUEUE.tsv  jobs queued for another account and not yet claimed
Projects come from PROJECTS.tsv (regex over job id, role and claim text; first match wins; add a row for a new
project). States: queued (WORK-QUEUE, unclaimed), running (claim or halfway, no done, under 6 h), done (within
--hours), stale (claim over 6 h old with no done -- CLAUDE.md's stale-claim rule).

  python3 tools/jobs_board.py [--hours 12] [--ref origin/main]     text board
  python3 tools/jobs_board.py --json                                the same as JSON (the cipher-lab-usage mod's /jobs)
Offline test: tools/tests/test_jobs_board.py.
"""
import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from account_usage import read, account_of, ROOM_RE  # noqa: E402

ORCH = re.compile(r'orchestrator|parent|dispatcher|LANE-|CLOSER', re.I)


def projects(text):
    out = []
    for line in text.splitlines()[1:]:
        f = line.split('\t')
        if len(f) >= 2 and f[1].strip():
            out.append((f[0], re.compile(f[1], re.I)))
    return out


SLUG = re.compile(r'\b([a-z][a-z0-9]*(?:-[a-z0-9]+){1,6})\b')


def project_of(head, text, projs, slugs):
    """PROJECTS.tsv on the job id and role first, then on its text; else the target folder it names; else Other."""
    for hay in (head, text):
        for name, rx in projs:
            if rx.search(hay):
                return name
    for m in SLUG.finditer(f'{head} {text}'):
        if m.group(1) in slugs:
            return m.group(1)
    return 'Other'


def acct(role):
    a = account_of(role)
    if a:
        return a
    if re.search(r'owner', role, re.I):
        return '1'
    return '?'


def jobs(room, queue, projs, now, hours, slugs=frozenset()):
    by = {}
    for line in room.splitlines():
        m = ROOM_RE.match(line)
        if not m:
            continue
        t = dt.datetime.strptime(m.group(1), '%Y-%m-%d %H:%M').replace(tzinfo=dt.timezone.utc)
        if (now - t).total_seconds() > max(hours, 6) * 3600 + 3600:
            continue
        role, sig = m.group(2), m.group(3)
        if ORCH.search(role.split('(')[0]):
            continue
        jid = role.split('(')[0].split(':')[0].strip()
        low = sig.lower()
        kind = 'done' if low.startswith('done') else 'claim' if low.startswith('claim') else \
            'halfway' if low.startswith('halfway') else 'flag' if low.startswith('flag') else None
        if not kind:
            continue
        j = by.setdefault(jid, {'id': jid, 'account': acct(role), 'text': '', 'start': None, 'end': None,
                                'state': None, 'summary': ''})
        if kind == 'claim':
            if j['state'] == 'done':  # a new claim after a done: a fresh run of the same role
                j.update(state=None, end=None)
            j['start'] = j['start'] or t
            j['text'] = j['text'] or sig[6:].strip()
            j['state'] = 'running'
        elif kind == 'halfway':
            j['state'] = j['state'] or 'running'
            j['start'] = j['start'] or t
        elif kind == 'done':
            j['state'], j['end'] = 'done', t
            j['summary'] = re.sub(r'^done[,:]?\s*(for [^:]+:)?\s*', '', sig, flags=re.I)[:220]
        else:
            j.setdefault('flags', 0)
            j['flags'] = j.get('flags', 0) + 1
        j['head'] = f'{jid} {role}'
        j['proj_text'] = f"{j['text']} {j['summary']}"
    out = []
    for j in by.values():
        if j['state'] is None:
            continue
        if j['state'] == 'running' and j['start'] and (now - j['start']).total_seconds() > 6 * 3600:
            j['state'] = 'stale'
        if j['state'] == 'done' and j['end'] and (now - j['end']).total_seconds() > hours * 3600:
            continue
        out.append(j)
    claimed = {j['id'] for j in out}
    wq = {}
    for line in queue.splitlines()[1:]:
        f = line.split('\t')
        if len(f) < 9:
            continue
        wq[f[0]] = f
        if f[6].strip() == 'queued' and f[0] not in claimed:
            out.append({'id': f[0], 'account': 'next free', 'text': f[8], 'state': 'queued', 'start': None,
                        'end': None, 'summary': '', 'head': f'{f[0]} {f[2]}', 'proj_text': f[8]})
    for j in out:
        if j['account'] == '?' and j['id'] in wq:
            j['account'] = '2'  # WORK-QUEUE 'other' rows are run by account 2's dispatcher/lane
        j['project'] = project_of(j.pop('head', j['id']), j.pop('proj_text', ''), projs, slugs)
        for k in ('start', 'end'):
            j[k] = j[k].strftime('%H:%M') if j[k] else ''
    return out


ORDER = {'running': 0, 'queued': 1, 'stale': 2, 'done': 3}


def board(ref=None, hours=12, now=None):
    now = now or dt.datetime.now(dt.timezone.utc)
    slugs = frozenset(p.name for p in (Path(__file__).resolve().parent.parent / 'ciphers').iterdir() if p.is_dir())
    js = jobs(read('ROOM.md', ref), read('WORK-QUEUE.tsv', ref), projects(read('PROJECTS.tsv', ref)), now, hours,
              slugs)
    groups = {}
    for j in js:
        groups.setdefault(j['project'], []).append(j)
    out = []
    for name, items in groups.items():
        items.sort(key=lambda j: (ORDER[j['state']], j['end'] or j['start'] or ''), reverse=False)
        counts = {s: sum(1 for j in items if j['state'] == s) for s in ORDER}
        out.append({'project': name, 'counts': counts, 'jobs': items})
    out.sort(key=lambda g: (-g['counts']['running'], -g['counts']['queued'], g['project']))
    return {'utc': now.strftime('%Y-%m-%d %H:%M'), 'hours': hours, 'projects': out}


MARK = {'running': '>', 'queued': '.', 'stale': '!', 'done': 'x'}


def text(b):
    lines = [f"Jobs across accounts, {b['utc']} UTC (done = last {b['hours']} h)"]
    for g in b['projects']:
        c = g['counts']
        lines.append(f"\n{g['project']}  ({c['running']} running, {c['queued']} queued, {c['done']} done"
                     + (f", {c['stale']} stale" if c['stale'] else '') + ')')
        for j in g['jobs']:
            when = j['end'] or j['start']
            what = j['summary'] if j['state'] == 'done' else j['text']
            who = j['account'] if j['account'] == 'next free' else 'acct ' + j['account']
            lines.append(f"  {MARK[j['state']]} {j['id'][:30]:<30} {who:<9} {when:>5}  {what[:80]}")
    lines.append('\n> running  . queued  x done  ! stale (claim over 6 h, no done)')
    return '\n'.join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--json', action='store_true')
    ap.add_argument('--ref')
    ap.add_argument('--hours', type=int, default=12)
    a = ap.parse_args()
    b = board(a.ref, a.hours)
    print(json.dumps(b) if a.json else text(b))


if __name__ == '__main__':
    sys.exit(main())
