# Build reconciled.tsv from reconcile_passes.py's ciphertext_draft.tsv + the two mapped passes' alignment:
# agree -> draft sign, grade H if both readers H, else M; disagree -> family rule if listed, else the sign one reader named
# (A preferred unless A is '?'/'-'/empty), grade M; a gap (one reader saw a sign the other skipped) -> keep the sign, M.
import csv, sys
draft, rules_f, out = sys.argv[1:4]
rules = {}
for r in open(rules_f):
    if r.startswith('#') or not r.strip(): continue
    a, b, v = r.rstrip('\n').split('\t'); rules[(a, b)] = v
rows = list(csv.DictReader(open(draft), delimiter='\t'))
w = open(out, 'w'); w.write('leaf\tline\tpos\tlabel\tgrade\tA\tB\thow\n')
n = 0; pos = {}
for r in rows:
    line = r['line']; why = r['why']; s = r['sign']; alt = r['alt']
    if why == 'agree': a = b = s; lab, g, how = s, 'H', 'agree'
    elif why == 'agree-flagged': a = b = s; lab, g, how = s, 'M', 'agree-low-conf'
    else:
        # draft carries A's sign (or B's when A empty) in 'sign', the other reader in alt 'A:x'/'B:x'
        if alt.startswith('B:'): a, b = s, alt[2:]
        elif alt.startswith('A:'): a, b = alt[2:], s
        else: a, b = s, ''
        a = '' if a == '-' else a; b = '' if b == '-' else b
        if (a, b) in rules: lab, how = rules[(a, b)], 'family-rule'
        elif not a or not b: lab, how = (a or b), 'one-reader'
        else: lab, how = (a if a not in ('?',) else b), 'take-A'
        g = 'M'
    if not lab: lab = '?'
    leaf, ln = line.split('_', 1)
    pos[line] = pos.get(line, 0) + 1
    w.write(f"{leaf}\t{ln}\t{pos[line]}\t{lab}\t{g}\t{a}\t{b}\t{how}\n"); n += 1
print('wrote', n)
