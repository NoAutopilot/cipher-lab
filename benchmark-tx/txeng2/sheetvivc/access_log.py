"""TXE2-SHEETVIVC (F63): tool-call file-access log of every reader / adjudicator subagent, from the session's own subagent
transcripts (~/.claude/projects/.../subagents/agent-<id>.jsonl). One row per tool call: call label, agent id, tool, the
file path or command. Then checks: every path is the call's own task file, the text-list sheet, a c105_f102r crop or its own
output file; anything else is printed as OUTSIDE. Usage: python3 access_log.py LABEL=AGENTID ... > access_log_X.tsv"""
import json, sys, glob, os, re
D = glob.glob(os.path.expanduser('~/.claude/projects/-home-user-cipher-lab/*/subagents'))
ALLOW = re.compile(r'(sheetvivc/(reads|packets)/(task_|pass|P)\w*\.(txt|tsv)|viv102base/sheet_SIGNS_dv1\.md|images/c105_f102r_L\d\d_s[12]\.jpg)$')
print('label\tagent\ttool\ttarget\tok')
bad = 0
for arg in sys.argv[1:]:
    lab, aid = arg.split('=')
    f = [p for d in D for p in glob.glob(f'{d}/agent-{aid}.jsonl')][0]
    for ln in open(f):
        m = json.loads(ln).get('message') or {}
        if m.get('role') != 'assistant' or not isinstance(m.get('content'), list): continue
        for c in m['content']:
            if c.get('type') != 'tool_use': continue
            i = c.get('input', {}); tgt = i.get('file_path') or i.get('path') or i.get('command') or i.get('pattern') or json.dumps(i)[:200]
            tgt = ' '.join(str(tgt).split())
            if c['name'] == 'SubagentHandback':
                ok = True; tgt = '(reply) ' + tgt[:120]
            elif c['name'] == 'Bash':
                # a write script: every path it names must be the allowed dir or an allowed file; no listing/reading verbs
                paths = re.findall(r'/home/user/\S+?(?=[\s\'\")]|$)', tgt) + re.findall(r"open\(\s*['\"]([^'\"]+)['\"]\s*,\s*['\"]w", tgt)
                verbs = re.search(r'(^|[;&|]\s*)(cat|ls|find|grep|head|tail|less|rg)\s', tgt)
                ok = not verbs and all(ALLOW.search(p) or re.search(r'sheetvivc/(reads|packets)/?$', p) or re.fullmatch(r'(pass[AB]_c[1-5]|P\d\d_out)\.tsv', p) for p in paths)
                tgt = 'Bash write script; paths named: ' + ' '.join(sorted(set(paths)))
            else:
                ok = c['name'] in ('Read', 'Write') and bool(ALLOW.search(tgt))
            bad += not ok
            print(f'{lab}\t{aid}\t{c["name"]}\t{tgt}\t{"ok" if ok else "OUTSIDE"}')
print(f'# outside-allowlist calls: {bad}', file=sys.stderr)
