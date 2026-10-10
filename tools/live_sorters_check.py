#!/usr/bin/env python3
"""Live sign-sorter pages still on an old template (owner rule R06, tools/data/sorter_owner_requirements.tsv, 9 Oct 2026: "Why we
make same mistakes over and over?" -- a page already sent to the owner gets every later fix).

    python3 tools/live_sorters_check.py [--registry tools/data/live_sorters.tsv] [--template tools/sign_sorter/template.html]
                                        [--account ACCT] [--artifacts LIST.txt] [--warn] [--quiet]
    python3 tools/live_sorters_check.py --record URL_OR_NAME PAGE.html      (after a republish: the marker is read from the page)

Reads the registry (tools/data/live_sorters.tsv: one row per sorter page published to the owner -- account, name, artifact_url,
template_marker, local_source_hint, last_republished, status, notes; '#' lines are comments) and the current template marker (the
<meta name="sign-sorter-template" content=...> of tools/sign_sorter/template.html). Prints one line per live row whose marker differs:

    stale: re-render and republish  <account>  <name>  <artifact_url>  (<page marker> -> <current marker>)

then a summary line. Exit 1 if any row is stale or malformed (or, with --artifacts, any sorter page is missing from the registry), 0 if
none; --warn prints the same and exits 0. --account limits the list to one account's rows (an account can republish only its own
pages; ASKS 145).

status (round-2 check, 10 Oct 2026: 14 sorter pages on account 3 were in no row, so the check passed silently for them): `live` (or
blank) = the owner may still open it, it gets every later fix; `retired YYYY-MM-DD: reason` = left alone on purpose (the owner said
done and the answers were exported, it was withdrawn, or a rebuild replaced it) -- listed in the summary, never stale. Anything else is
a bad row. A page whose marker was never read back carries `unread` and is stale until it is re-rendered.

--artifacts LIST.txt: the text of an Artifact `list` (action list, scope mine) saved to a file -- every line holding a claude.ai artifact
URL, its title before the URL. A line whose title looks like a sorter page (`--sorter-title`, default: sorter, "verify the cuts",
or the word "signs") and whose URL is in no row is printed `unregistered: add a row (live or retired)` and fails the check. The parent
saves the list and runs this at every check-in (.claude/briefs/parent.md duty 6), so a page published without a row is found.

--record URL_OR_NAME PAGE.html: after republishing PAGE.html to that artifact, writes the marker read from PAGE.html itself (never
typed) and the UTC time into the row's template_marker and last_republished, and sets status live. Exit 2 if PAGE.html carries no
marker or no row matches.

The fix for a stale row, by the account that owns the page: read the artifact back (Artifact action read), re-render it with
tools/sorter_rerender.py OLD.html --out NEW.html (DATA, tiles and sids carried over byte for byte, so the owner's saved answers
still apply after a republish to the same URL, R08), run tools/sorter_preflight.py NEW.html (all six checks, the gesture test
included), republish to the same URL, then `--record URL PAGE.html` (the row's template_marker and last_republished). A parent
runs this at every check-in (.claude/briefs/parent.md, duty 6).

Must catch (offline test tools/tests/test_live_sorters_check.py): a row on an older marker; a row with no marker ('none' or blank:
a page built before markers); a row whose marker is newer than the template's (built from an unmerged template); a malformed row
(no artifact URL, or not a claude.ai artifact link) or with a status that is neither live nor `retired DATE: reason` -- reported as
'bad row', never passed over; an `unread` marker; with --artifacts, a sorter-titled artifact with no row. Must NOT block: a row on the
current marker; a retired row on any marker; comment and blank lines; --warn (exit 0); rows of another account under --account; a
registry written before the status column (blank status = live); with --artifacts, an artifact whose title is not a sorter's (a deck,
a dashboard) or a sorter-titled one that has a row.
"""
import argparse, csv, datetime, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REGISTRY = os.path.join(HERE, 'data', 'live_sorters.tsv')
TEMPLATE = os.path.join(HERE, 'sign_sorter', 'template.html')
MARKER_RE = re.compile(r'<meta name="sign-sorter-template" content="([^"]+)"')
URL_RE = re.compile(r'^https://claude\.ai/(?:code/)?artifact/[A-Za-z0-9-]+/?$')
ANY_URL = re.compile(r'https://claude\.ai/(?:code/)?artifact/([A-Za-z0-9-]+)')
RETIRED_RE = re.compile(r'^retired \d{4}-\d{2}-\d{2}: \S')
SORTER_TITLE = r'sorter|verify the cuts|\bsigns\b'   # 'signs': "Birago 1572: settle 24 look-alike signs", "WVO 11106 p.2 signs (group reads)"
COLS = ['account', 'name', 'artifact_url', 'template_marker', 'local_source_hint', 'last_republished', 'status', 'notes']
REQUIRED = [c for c in COLS if c != 'status']   # a registry written before the status column still reads (blank status = live)


def current_marker(template=TEMPLATE):
    m = MARKER_RE.search(open(template, encoding='utf-8').read())
    return m.group(1) if m else None


def read_registry(path=REGISTRY):
    """-> list of row dicts (comment and blank lines skipped). The first non-comment line is the header."""
    lines = [l for l in open(path, encoding='utf-8').read().splitlines() if l.strip() and not l.lstrip().startswith('#')]
    if not lines:
        return []
    return list(csv.DictReader(lines, delimiter='\t'))


def art_id(url):
    m = ANY_URL.search(url or '')
    return m.group(1) if m else None


def check(rows, current, account=None):
    """-> (stale, bad, fresh, retired): lists of (row, why)."""
    stale, bad, fresh, retired = [], [], [], []
    for r in rows:
        if account and (r.get('account') or '') != account:
            continue
        url, mk, stt = (r.get('artifact_url') or '').strip(), (r.get('template_marker') or '').strip(), (r.get('status') or '').strip()
        if not URL_RE.match(url):
            bad.append((r, f'no claude.ai artifact URL ({url or "blank"})')); continue
        if stt.lower().startswith('retired'):
            if RETIRED_RE.match(stt):
                retired.append((r, stt))
            else:
                bad.append((r, f'status "{stt}": write "retired YYYY-MM-DD: reason"'))
            continue
        if stt not in ('', 'live'):
            bad.append((r, f'status "{stt}": live, or "retired YYYY-MM-DD: reason"')); continue
        if mk.lower() in ('', 'none', '-'):
            stale.append((r, 'no marker -> ' + str(current))); continue
        if mk.lower() == 'unread':
            stale.append((r, 'marker not read back -> ' + str(current))); continue
        if mk != current:
            stale.append((r, f'{mk} -> {current}' + (' (newer than the template: built from an unmerged template?)' if mk > (current or '') else '')))
            continue
        fresh.append((r, mk))
    return stale, bad, fresh, retired


def unregistered(listing, rows, title_re=SORTER_TITLE):
    """listing: the text of an Artifact list. -> [(title, url)] for sorter-titled artifacts whose id is in no row."""
    known = {art_id(r.get('artifact_url')) for r in rows}
    pat, out, seen = re.compile(title_re, re.I), [], set()
    for line in listing.splitlines():
        m = ANY_URL.search(line)
        if not m or m.group(1) in seen:
            continue
        title = re.sub(r'^[\s*-]*(\((?:mine|shared)[^)]*\)\s*)?', '', line[:m.start()]).strip(' -—\u2014\t')
        if pat.search(title) and m.group(1) not in known:
            out.append((title, m.group(0))); seen.add(m.group(1))
    return out


def record(path, key, page):
    """Write PAGE's own marker and the UTC time into the row whose artifact_url (or id, or name) is KEY. -> (code, message)."""
    mk = MARKER_RE.search(open(page, encoding='utf-8', errors='replace').read())
    if not mk:
        return 2, f'{page}: no sign-sorter-template marker -- not a current sorter page, nothing recorded'
    text = open(path, encoding='utf-8').read().splitlines(keepends=True)
    hdr_i = next(i for i, l in enumerate(text) if l.strip() and not l.lstrip().startswith('#'))
    hdr = text[hdr_i].rstrip('\n').split('\t')
    if 'status' not in hdr:
        return 2, f'{path}: header has no status column'
    ix = {c: hdr.index(c) for c in hdr}
    now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    hits = 0
    for i in range(hdr_i + 1, len(text)):
        l = text[i]
        if not l.strip() or l.lstrip().startswith('#'):
            continue
        cells = l.rstrip('\n').split('\t'); cells += [''] * (len(hdr) - len(cells))
        if key not in (cells[ix['artifact_url']], art_id(cells[ix['artifact_url']]), cells[ix['name']]):
            continue
        cells[ix['template_marker']], cells[ix['last_republished']], cells[ix['status']] = mk.group(1), now, 'live'
        text[i] = '\t'.join(cells) + '\n'; hits += 1
    if hits != 1:
        return 2, f'{key}: {hits} rows match (want exactly 1) -- nothing recorded'
    open(path, 'w', encoding='utf-8').write(''.join(text))
    return 0, f'recorded {key}: template_marker {mk.group(1)} (read from {page}), last_republished {now}, status live'


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0], formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=__doc__.split('\n', 2)[2])
    ap.add_argument('--registry', default=REGISTRY, help='the live-page registry (default tools/data/live_sorters.tsv)')
    ap.add_argument('--template', default=TEMPLATE, help='the sorter template whose marker is current (default tools/sign_sorter/template.html)')
    ap.add_argument('--account', help="only this account's rows (e.g. acct3, owner)")
    ap.add_argument('--artifacts', metavar='LIST.txt', help='an Artifact list saved to a file: sorter-titled artifacts with no row fail the check')
    ap.add_argument('--sorter-title', default=SORTER_TITLE, help='regex (case-insensitive) a sorter page title matches (default: %(default)s)')
    ap.add_argument('--record', nargs=2, metavar=('URL_OR_NAME', 'PAGE.html'), help="after a republish: write PAGE.html's own marker and the time into the row")
    ap.add_argument('--warn', action='store_true', help='print the list but exit 0')
    ap.add_argument('--quiet', action='store_true', help='print only the summary line')
    a = ap.parse_args(argv)
    if a.record:
        code, msg = record(a.registry, *a.record)
        print(msg, file=sys.stderr if code else sys.stdout); return code
    cur = current_marker(a.template)
    if not cur:
        print(f'{a.template}: no sign-sorter-template marker', file=sys.stderr); return 2
    rows = read_registry(a.registry)
    missing = [c for c in REQUIRED if rows and c not in rows[0]]
    if missing:
        print(f'{a.registry}: header lacks {", ".join(missing)}', file=sys.stderr); return 2
    stale, bad, fresh, retired = check(rows, cur, a.account)
    unreg = unregistered(open(a.artifacts, encoding='utf-8').read(), rows, a.sorter_title) if a.artifacts else []
    if not a.quiet:
        for r, why in stale:
            print(f"stale: re-render and republish  {r['account']}  {r['name']}  {r['artifact_url']}  ({why})")
        for r, why in bad:
            print(f"bad row: {r.get('account')}  {r.get('name')}  ({why})")
        for title, url in unreg:
            print(f"unregistered: add a row (live or retired)  {url}  {title}")
    scope = f' for {a.account}' if a.account else ''
    print(f'live sorters{scope}: {len(stale)} stale, {len(bad)} bad, {len(fresh)} on the current template {cur}, {len(retired)} retired'
          + (f', {len(unreg)} unregistered' if a.artifacts else ' (Artifact list not compared: --artifacts)')
          + ('' if stale or bad or unreg else ' -- nothing to republish'))
    return 0 if a.warn or not (stale or bad or unreg) else 1


if __name__ == '__main__':
    sys.exit(main())
