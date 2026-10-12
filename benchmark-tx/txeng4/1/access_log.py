"""TXE4-1 (copied from benchmark-tx/txeng3/8/access_log.py, paths and allowlist changed): tool-call file-access log of every reader / adjudicator subagent of THIS
session, from ~/.claude/projects/-home-user-cipher-lab/<session>/subagents/agent-*.jsonl. One row per tool call. A call is ok when every
path it names lies inside the call's own scratch dir (r/RUN_xx or p/RUN_Pnn: task.txt, queue.tsv, the sheet copy, its L01-L12 crops,
its own read.tsv/out.tsv) and no listing/reading shell verb is used; anything else prints OUTSIDE. Usage: python3 access_log.py > access_log.tsv"""
import glob, json, os, re, sys
S = glob.glob(os.path.expanduser('~/.claude/projects/-home-user-cipher-lab/418d81d6-5d23-5452-a42d-0fa425085382/subagents/agent-*.jsonl'))
OWNDIR = re.compile(r'scratchpad/(r)/([DW][12])/?$')
OWN = re.compile(r'scratchpad/(r)/([DW][12])/(task\.txt|read\.tsv|sheet_tomokiyo_v1\.png|sheet_SIGNS_dv1\.md|c105_f102r_L(?:02|04|08|10|16|18|20|24|28|30|32|34|36)_s[12]\.jpg)$')
print('agent\tcall\ttool\ttarget\tok'); bad = 0
for f in sorted(S, key=os.path.getmtime):
    aid = os.path.basename(f)[6:-6]; label = '?'; rows = []
    for ln in open(f):
        try: m = json.loads(ln).get('message') or {}
        except ValueError: continue
        if m.get('role') != 'assistant' or not isinstance(m.get('content'), list): continue
        for c in m['content']:
            if c.get('type') != 'tool_use': continue
            i = c.get('input', {}); tgt = i.get('file_path') or i.get('path') or i.get('command') or i.get('pattern') or json.dumps(i)[:200]
            tgt = ' '.join(str(tgt).split())
            paths = re.findall(r'/tmp/\S+?(?=[\s\'\")]|$)', tgt) + re.findall(r'/home/user/\S+?(?=[\s\'\")]|$)', tgt)
            dirs = {(OWN.search(p) or OWNDIR.search(p)).group(2) for p in paths if OWN.search(p) or OWNDIR.search(p)}
            if label == '?' and dirs: label = sorted(dirs)[0]
            if c['name'] == 'Bash':
                verbs = re.search(r'(^|[;&|]\s*)(cat\s+(?!>)|ls|find|grep|head|tail|less|rg)\s', tgt)
                opens = re.findall(r"open\(\s*['\"]([^'\"]+)['\"]", tgt)
                ok = (not verbs and bool(paths) and all(OWN.search(p) or OWNDIR.search(p) for p in paths) and len(dirs) == 1
                      and all(re.fullmatch(r'(read|out)\.tsv', o) or OWN.search(o) for o in opens))  # a write script in its own dir, no reads
                tgt = 'Bash; paths: ' + ' '.join(sorted(set(paths)))[:300]
            elif c['name'] in ('Read', 'Write'):
                ok = bool(OWN.search(tgt))
            elif c['name'] == 'SubagentHandback':
                ok = True; tgt = '(reply) ' + tgt[:80]
            else:
                ok = False
            rows.append((c['name'], tgt, ok))
    for name, tgt, ok in rows:
        bad += not ok; print(f'{label}\t{aid}\t{name}\t{tgt}\t{"ok" if ok else "OUTSIDE"}')
    # every call of one agent must stay in ONE scratch dir
print(f'# agents {len(S)}; outside-allowlist calls: {bad}', file=sys.stderr)
