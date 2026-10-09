#!/usr/bin/env python3
"""TXE2-COST2: per-call token usage from subagent transcripts (JSONL), summed over distinct API messages (deduplicated by
message id: one API turn can be logged once per content block, with partial streamed output counts, so output_tokens
is the largest logged value per message: a LOWER bound; input counts are exact per message). Prints counts only, never content.
    python3 usage.py LABEL=TRANSCRIPT.jsonl [...]"""
import json, sys
K = ('input_tokens', 'cache_creation_input_tokens', 'cache_read_input_tokens', 'output_tokens')
for arg in sys.argv[1:]:
    lab, p = arg.split('=', 1); seen = {}
    for line in open(p):
        try:
            e = json.loads(line)
        except ValueError:
            continue
        m = e.get('message') if isinstance(e, dict) else None
        if isinstance(m, dict) and m.get('role') == 'assistant' and m.get('usage'):
            k = m.get('id') or len(seen); u = dict(m['usage']); o = seen.get(k)
            if o:  # streamed blocks log partial output counts: keep the largest (still a LOWER bound on output)
                u['output_tokens'] = max(u.get('output_tokens') or 0, o.get('output_tokens') or 0)
            seen[k] = u
    tot = {k: sum(u.get(k, 0) or 0 for u in seen.values()) for k in K}
    print(lab, 'api_calls', len(seen), tot, 'input_all', tot[K[0]] + tot[K[1]] + tot[K[2]])
