"""TXE4-8 (after benchmark-tx/txeng3/8/access_log.py): tool-call file-access log of every reader subagent of THIS session, from
~/.claude/projects/-home-user-cipher-lab/<session>/subagents/agent-*.jsonl. One row per tool call. A call is ok when every path it
names lies inside the call's own scratch dir (r/<PASS><a|b>: task.txt, sign_sheet.png, crops/*.jpg, its own read.tsv) and no
listing/reading shell verb is used; anything else prints OUTSIDE. Usage: python3 access_log.py > access_log.tsv"""
import glob, json, os, re, sys
S = glob.glob(os.path.expanduser('~/.claude/projects/-home-user-cipher-lab/222cfca4-e907-5f3b-a2fd-bf6b71fb86ae/subagents/agent-*.jsonl'))
OWNDIR = re.compile(r'scratchpad/r/([NOR][12][ab]?)/?$')
OWN = re.compile(r'scratchpad/r/([NOR][12][ab]?)/(task\.txt|read\.tsv|sign_sheet\.png|crops/c105_f102r_L\d\d_s[12](?:_boxes)?\.jpg|[\w.\-]+\.py)$')  # a helper script the reader writes in its OWN dir is allowed
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
            dirs = {(OWN.search(p) or OWNDIR.search(p)).group(1) for p in paths if OWN.search(p) or OWNDIR.search(p)}
            if label == '?' and dirs: label = sorted(dirs)[0]
            if c['name'] == 'Bash':
                verbs = re.search(r'(^|[;&|]\s*)(cat\s+(?!>)|ls|find|grep|head|tail|less|rg)\s', tgt)
                opens = re.findall(r"open\(\s*['\"]([^'\"]+)['\"]", tgt)
                ok = (not verbs and bool(paths) and all(OWN.search(p) or OWNDIR.search(p) for p in paths) and len(dirs) == 1
                      and all(re.fullmatch(r'read\.tsv', o) or OWN.search(o) for o in opens))
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
print(f'# agents {len(S)}; outside-allowlist calls: {bad}', file=sys.stderr)
