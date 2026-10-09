#!/usr/bin/env python3
"""Compile research/TX-REGISTER.tsv, the one register of every transcription experiment, and gate new PREREGs on it.

research/TX-PROGRAM.md "Memory" (TX-REGISTER, account 4, 9 Oct 2026): one row per experiment of both transcription
campaigns, compiled best-effort from

  * research/TX-IDEAS-2026-10-09.md and research/TX-IDEAS-2-2026-10-09.md -- the ideas table (one row per idea, its
    status) and the "Results log" table (one row per PREREG'd test, with its numbers);
  * TRANSCRIPTION.md's build-plan "Today" rows for TX-VIEWS, TX-AGREEAUDIT, TX-ALTS, TX-SHEET, TX-FABLE;
  * benchmark-tx/PREREG-*.md and benchmark-tx/txeng/*/RESULTS.md, benchmark-tx/txeng2/*/RESULTS.md -- a file already
    cited by a row above is covered by that row; any other file gets a row of its own, verdict from its own
    "Verdict:" line when one is found.

Columns: id, campaign, family, mechanism_attacked, unit_or_pool, dev_result, eval_result, eval_looks, verdict, reason,
source_file, date. Verdicts: dev-FAIL, dev-PASS, moved-eval, did-not-move, non-test, retired, measured, running, queued;
a row whose status the parser cannot map is written with verdict `unparsed` and its source line in `reason`, never
dropped. The tool reads only; it never edits a PREREG, RESULTS or truth file and never scores anything.

  python3 tools/tx_register.py                 # write research/TX-REGISTER.tsv, print counts per verdict
  python3 tools/tx_register.py --stdout        # print the TSV instead
  python3 tools/tx_register.py --check benchmark-tx/PREREG-new.md

--check PREREG exits non-zero unless the PREREG has a "Nearest prior" or "differs from" section (a markdown heading, or
a line starting with that label) naming at least one register id in a sentence of at least five words, and unless every
named id whose register verdict is `retired` is named in a sentence carrying "different instrument" or "new material"
(the Memory rule: a family retired under CLAUDE.md rule 3's third-attempt clause is not re-run without one).

Must catch (tests/test_tx_register.py::test_check_catches_retired_rerun): a PREREG whose Nearest prior names a retired
id (M1b) and says only that it re-runs the layout at a new threshold -- exit 1; and a PREREG with no Nearest prior
section at all -- exit 1.
Must NOT block (::test_check_allows_retired_with_instrument, ::test_check_allows_non_retired): a PREREG citing the
retired id with "a different instrument (a pixel classifier, no exemplar shown)" -- exit 0; and one citing a dev-FAIL
id with a one-sentence difference -- exit 0.
"""
import argparse
import csv
import glob
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = 'research/TX-REGISTER.tsv'
IDEAS = [('research/TX-IDEAS-2026-10-09.md', 'txeng'), ('research/TX-IDEAS-2-2026-10-09.md', 'txeng2')]
TODAY_IDS = ['TX-VIEWS', 'TX-AGREEAUDIT', 'TX-ALTS', 'TX-SHEET', 'TX-FABLE']
COLS = ['id', 'campaign', 'family', 'mechanism_attacked', 'unit_or_pool', 'dev_result', 'eval_result', 'eval_looks',
        'verdict', 'reason', 'source_file', 'date']
VERDICTS = ['dev-FAIL', 'dev-PASS', 'moved-eval', 'did-not-move', 'non-test', 'retired', 'measured', 'running',
            'queued', 'unparsed']
MONTHS = {'Sept': 9, 'Sep': 9, 'Oct': 10}


def clean(s, n=300):
    s = re.sub(r'\*\*|`', '', s or '').replace('\t', ' ').replace('\n', ' ').strip()
    return s if len(s) <= n else s[:n - 3] + '...'


def map_verdict(text):
    """Map a free-text status or verdict cell to the register vocabulary; None when it cannot be read."""
    t = (text or '').lower()
    if not t.strip():
        return None
    if 'retired' in t:
        return 'retired'
    if 'non-test' in t or 'non test' in t:
        return 'non-test'
    if 'did-not-move' in t or 'did not move' in t:
        return 'did-not-move'
    if 'moved-eval' in t or re.search(r'\bmoved\b', t):
        return 'moved-eval'
    if 'running' in t:
        return 'running'
    if re.search(r'\bqueued\b', t):
        return 'queued'
    if re.search(r'confirm figure|proposal only|no gate|doubt flag', t):
        return 'measured'
    if re.search(r'dev-pass|\bpass\b', t) and not re.search(r'fail', t):
        return 'dev-PASS'
    if re.search(r'fail|not adopted|worse', t):
        return 'dev-FAIL'
    if re.search(r'measured|error map|on file|no gate|proposal only|signal|confirm figure|\bbuilt\b|truth rule', t):
        return 'measured'
    return None


def md_rows(lines, start):
    """Yield (lineno, cells) for a markdown table starting at or after line index `start` (header + rule skipped)."""
    i = start
    while i < len(lines) and not lines[i].startswith('|'):
        i += 1
    i += 2
    while i < len(lines) and lines[i].startswith('|'):
        cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
        yield i + 1, cells
        i += 1


def parse_date(cell, default='2026-10-09'):
    m = re.search(r'(\d{1,2}) (Sept|Sep|Oct)(?: (\d{4}))? (\d{2}:\d[0-9x])', cell or '')
    if not m:
        return default
    return '%s-%02d-%02d %s' % (m.group(3) or '2026', MONTHS[m.group(2)], int(m.group(1)), m.group(4))


def file_date(text, default=''):
    m = re.search(r'(\d{1,2}) (Sept|Sep|Oct) (\d{4})', text)
    return '%s-%02d-%02d' % (m.group(3), MONTHS[m.group(2)], int(m.group(1))) if m else default


def unit_of(text):
    m = re.search(r'\b(dev_tune|eval_heldout|geo unit|dev pool|eval pool|dint-f\w+|spinelli\w*|no\.87|f\.?\d+[rv]?)',
                  text or '')
    return m.group(1) if m else ''


def parse_ideas(path, campaign, root=ROOT):
    rows = []
    full = os.path.join(root, path)
    if not os.path.exists(full):
        return rows
    lines = open(full, encoding='utf-8').read().split('\n')
    try:
        t1 = next(i for i, l in enumerate(lines) if l.startswith('| rank |'))
    except StopIteration:
        t1 = None
    try:
        t2 = next(i for i, l in enumerate(lines) if l.startswith('## Results log'))
    except StopIteration:
        t2 = None
    ideas = {}
    if t1 is not None:
        for ln, c in md_rows(lines, t1):
            if len(c) < 6:
                rows.append(unparsed(campaign, path, ln, lines[ln - 1]))
                continue
            ideas[c[1]] = dict(id=c[1], family=clean(c[2], 160), mechanism_attacked=clean(c[3], 120),
                               unit_or_pool=clean(unit_of(c[4]) or c[4], 80), status=c[5], ln=ln)
    logged = set()
    if t2 is not None:
        for ln, c in md_rows(lines, t2):
            if len(c) < 6:
                rows.append(unparsed(campaign, path, ln, lines[ln - 1]))
                continue
            rid = c[1]
            base = rid.split()[0].split('-')[0].split('+')[0]
            idea = ideas.get(rid) or ideas.get(base) or {}
            logged.add(rid)
            logged.add(base)
            v = map_verdict(c[5])
            looks = re.search(r'looks(?: so far)? (\d+)', c[4])
            rows.append(dict(id=rid, campaign=campaign, family=idea.get('family', ''),
                             mechanism_attacked=idea.get('mechanism_attacked', ''),
                             unit_or_pool=clean(unit_of(c[3]) or idea.get('unit_or_pool', ''), 80),
                             dev_result=clean(c[3], 240), eval_result=clean(c[4], 160),
                             eval_looks=looks.group(1) if looks else ('0' if 'not taken' in c[4].lower() else ''),
                             verdict=v or 'unparsed',
                             reason=clean(c[5], 200) if v else clean('UNPARSED %s:%d %s' % (path, ln, lines[ln - 1]), 300),
                             source_file='%s:%d; %s' % (path, ln, clean(c[2], 120)),
                             date=parse_date(c[0])))
    for rid, idea in ideas.items():
        if rid in logged:
            continue
        v = map_verdict(idea['status'])
        rows.append(dict(id=rid, campaign=campaign, family=idea['family'], mechanism_attacked=idea['mechanism_attacked'],
                         unit_or_pool=idea['unit_or_pool'], dev_result='', eval_result='', eval_looks='',
                         verdict=v or 'unparsed',
                         reason=clean(idea['status'], 200) if v else
                         clean('UNPARSED %s:%d %s' % (path, idea['ln'], lines[idea['ln'] - 1]), 300),
                         source_file='%s:%d' % (path, idea['ln']), date='2026-10-09'))
    return rows


def unparsed(campaign, path, ln, line):
    return dict(id='?%s:%d' % (os.path.basename(path), ln), campaign=campaign, family='', mechanism_attacked='',
                unit_or_pool='', dev_result='', eval_result='', eval_looks='', verdict='unparsed',
                reason=clean('UNPARSED ' + line, 300), source_file='%s:%d' % (path, ln), date='')


def parse_today(root=ROOT):
    rows = []
    path = 'TRANSCRIPTION.md'
    full = os.path.join(root, path)
    if not os.path.exists(full):
        return rows
    lines = open(full, encoding='utf-8').read().split('\n')
    for ln, l in enumerate(lines, 1):
        m = re.match(r'\| (TX-[A-Z]+) \|', l)
        if not m or m.group(1) not in TODAY_IDS:
            continue
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        status = c[2] if len(c) > 2 else ''
        tail = re.split(r'\*\*Today[^*]*\*\*|\*\*Ran[^*]*\*\*|Today \(', status)
        verdict_text = ' '.join(re.findall(r'\*\*([^*]+)\*\*', status)) or status
        v = map_verdict(verdict_text)
        src = re.findall(r'benchmark-tx/[\w./-]+', status)
        rows.append(dict(id=m.group(1), campaign='tx-build', family=clean(c[1], 160), mechanism_attacked='',
                         unit_or_pool='no.87', dev_result=clean(tail[-1] if len(tail) > 1 else status, 240),
                         eval_result='', eval_looks='', verdict=v or 'unparsed',
                         reason=clean(verdict_text, 200) if v else clean('UNPARSED %s:%d %s' % (path, ln, l), 300),
                         source_file='%s:%d%s' % (path, ln, ('; ' + src[0]) if src else ''),
                         date=file_date(status, '2026-10-04')))
    return rows


def parse_files(cited, root=ROOT):
    rows = []
    pats = ['benchmark-tx/PREREG-*.md', 'benchmark-tx/txeng/*/RESULTS.md', 'benchmark-tx/txeng2/*/RESULTS.md']
    for pat in pats:
        for full in sorted(glob.glob(os.path.join(root, pat))):
            rel = os.path.relpath(full, root)
            stem = rel[len('benchmark-tx/'):]
            if rel in cited or stem in cited or os.path.basename(rel) in cited and 'PREREG' in rel:
                continue
            text = open(full, encoding='utf-8').read()
            lines = text.split('\n')
            title = next((l.lstrip('# ').strip() for l in lines if l.startswith('#')), rel)
            vl = ''
            for k, l in enumerate(lines):
                if re.match(r'\s*\**verdict\**\s*:', l, re.I) or re.match(r'#+\s*verdict', l, re.I):
                    vl = l if len(l.split(':', 1)[-1].strip()) > 3 and ':' in l else ' '.join(lines[k:k + 2])
                    break
            v = map_verdict(vl) if vl else None
            if v is None and re.match(r'TXP-', title):
                v, vl = 'measured', 'benchmark item / truth build (TXP-), no gate: ' + title
            elif v is None and 'DRAFT' in title:
                v, vl = 'queued', 'PREREG draft, not frozen: ' + title
            camp = 'txeng2' if 'txeng2' in rel else ('txeng' if 'txeng' in rel else 'tx-build')
            rid = re.sub(r'^(benchmark-tx/)', '', rel).replace('/RESULTS.md', '').replace('.md', '')
            rows.append(dict(id=rid, campaign=camp, family=clean(title, 160), mechanism_attacked='',
                             unit_or_pool=unit_of(text[:2000]), dev_result='', eval_result='', eval_looks='',
                             verdict=v or 'unparsed',
                             reason=clean(vl, 200) if v else clean('UNPARSED no Verdict line read; title: ' + title, 300),
                             source_file=rel, date=file_date(text)))
    return rows


def compile_register(root=ROOT):
    rows = []
    for path, camp in IDEAS:
        rows += parse_ideas(path, camp, root)
    today = parse_today(root)
    rows += today
    blob = ' '.join(r['source_file'] + ' ' + r['reason'] + ' ' + r['dev_result'] + ' ' + r['eval_result'] for r in rows)
    cited = set(re.findall(r'benchmark-tx/[\w./-]+?\.md', blob))
    cited |= set(re.findall(r'\b(PREREG-[\w-]+\.md)', blob))
    cited |= {c[len('benchmark-tx/'):] for c in cited if c.startswith('benchmark-tx/')}
    # "PREREG-txeng2-1 X2" style citations name the file without its .md
    cited |= {m + '.md' for m in re.findall(r'\b(PREREG-[\w-]*\w)\b', blob)}
    # a TRANSCRIPTION.md Today row covers its own PREREG (TX-SHEET -> PREREG-txsheet.md)
    cited |= {'PREREG-%s.md' % r['id'][k:].replace('-', '').lower() for r in today for k in (0, 3)}
    rows += parse_files(cited, root)
    seen = {}
    for r in rows:
        n = seen.get(r['id'], 0)
        seen[r['id']] = n + 1
        if n:
            r['id'] = '%s#%d' % (r['id'], n + 1)
    return rows


def write_tsv(rows, fh):
    w = csv.writer(fh, delimiter='\t', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
    w.writerow(COLS)
    for r in rows:
        w.writerow([r.get(c, '') for c in COLS])


def read_register(path):
    with open(path, encoding='utf-8') as fh:
        return list(csv.DictReader(fh, delimiter='\t'))


def counts(rows):
    out = {}
    for r in rows:
        out[r['verdict']] = out.get(r['verdict'], 0) + 1
    return out


LABEL = re.compile(r'nearest prior|differs? from', re.I)


def prior_sections(text):
    """The text of every 'Nearest prior' / 'differs from' section: a heading's body up to the next heading, or a
    labelled line's paragraph up to the next blank line or heading."""
    lines = text.split('\n')
    out = []
    for i, l in enumerate(lines):
        if l.startswith('#') and LABEL.search(l):
            j = i + 1
            while j < len(lines) and not lines[j].startswith('#'):
                j += 1
            out.append('\n'.join(lines[i + 1:j]))
        elif not l.startswith('#') and LABEL.search(l):
            k = LABEL.search(l).start()
            if k == 0 or re.match(r'[\s*_\-|]*$', l[:k]) or re.search(r'[.;:]\s*\**$', l[:k]):
                j = i + 1
                while j < len(lines) and lines[j].strip() and not lines[j].startswith('#'):
                    j += 1
                out.append(' '.join([l[k:]] + lines[i + 1:j]))
    return out


def sentences(text):
    return [s.strip() for s in re.split(r'(?<=[.;!?])\s+(?=[A-Z(*"])|\n\s*\n|\n\s*[-*]\s', text) if s.strip()]


def check(prereg, register_rows):
    """Return a list of problems (empty = pass) for the PREREG text against the register."""
    text = open(prereg, encoding='utf-8').read() if os.path.exists(prereg) else prereg
    secs = prior_sections(text)
    if not secs:
        return ['no "Nearest prior" / "differs from" section']
    by_id = {}
    for r in register_rows:
        for key in {r['id'].split('#')[0], r['id'].split('#')[0].split()[0]}:
            by_id.setdefault(key, set()).add(r['verdict'])
    named = {}
    for sec in secs:
        for s in sentences(sec):
            for key in by_id:
                if len(key) < 2 or key.startswith('?'):
                    continue
                if re.search(r'(?<![\w-])%s(?![\w-])' % re.escape(key), s):
                    named.setdefault(key, []).append(s)
    if not named:
        return ['the Nearest prior section names no register id']
    problems = []
    if not any(len(s.split()) >= 5 for ss in named.values() for s in ss):
        problems.append('no sentence of difference (>= 5 words) beside the named ids')
    for key, ss in sorted(named.items()):
        if 'retired' in by_id[key] and not any(re.search(r'different instrument|new material', s, re.I) for s in ss):
            problems.append('%s is retired and no sentence naming it says "different instrument" or "new material"' % key)
    return problems


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--root', default=ROOT)
    ap.add_argument('--out', default=OUT, help='register path relative to --root (default %(default)s)')
    ap.add_argument('--stdout', action='store_true', help='print the TSV instead of writing it')
    ap.add_argument('--check', metavar='PREREG', help='gate a PREREG against the register (reads --out)')
    a = ap.parse_args(argv)
    if a.check:
        reg = os.path.join(a.root, a.out)
        if not os.path.exists(reg):
            print('no register at %s: run tools/tx_register.py first' % reg)
            return 2
        probs = check(a.check, read_register(reg))
        if probs:
            print('FAIL %s:\n  ' % a.check + '\n  '.join(probs))
            return 1
        print('OK %s: names register rows and states a difference' % a.check)
        return 0
    rows = compile_register(a.root)
    if a.stdout:
        write_tsv(rows, sys.stdout)
    else:
        with open(os.path.join(a.root, a.out), 'w', encoding='utf-8') as fh:
            write_tsv(rows, fh)
        print('wrote %s: %d rows' % (a.out, len(rows)))
    c = counts(rows)
    print('verdicts: ' + ', '.join('%s %d' % (v, c[v]) for v in VERDICTS if v in c))
    return 0


if __name__ == '__main__':
    sys.exit(main())
