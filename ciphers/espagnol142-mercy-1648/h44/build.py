"""H44 packets. Control: a Cartas sentence (es17c7, "y al conde de Baynete, su caballerizo mayor") encoded as the target
stretch is shown: letters run together, about 12% shown as "?" (the target's share of nomenclature/M tokens in r16:2-r18),
5% replaced by a wrong letter (the target's bracketed error, H1). Target: r16:2-r18 with key.tsv letters, nomenclature and
M-graded tokens as "?", no other change. Same instructions for both; the reader never sees NOTES."""
import csv, random
INSTR = ("You are helping read a damaged passage of a 17th-century Spanish letter. The passage below between the clear "
         "context is given as a run of letters with no spaces; '?' marks a sign that could stand for one or two letters, and a "
         "few letters may be wrong. Spelling is period Spanish (u/v and i/j interchange, no accents).\n"
         "Question: what does the damaged run most likely say? In particular, name the PERSON it refers to (the proper name, "
         "as exactly as you can) and any OFFICE or title given to that person. Give your best reading with word spaces, then "
         "one line 'PERSON: ...' and one line 'OFFICE: ...', then one line of confidence (high/medium/low) and the letters that "
         "support it. Use your knowledge of the period if it helps.\n\n")
rng = random.Random(44)
ctl = 'yalcondedebaynetesucaballerizomayor'
s = list(ctl)
for i in rng.sample(range(len(s)), round(0.12 * len(s))):
    s[i] = '?'
for i in rng.sample([i for i in range(len(s)) if s[i] != '?'], round(0.05 * len(s))):
    s[i] = rng.choice('aeiosnrlt'.replace(s[i], ''))
open('h44/packet_control.txt', 'w').write(
    INSTR + "CLEAR CONTEXT BEFORE: ... los ministros trataron del ajuste, y habiendo S. A. nombrado a este padre, a D. "
    "Bernardino Foglea, su secretario de camara,\nDAMAGED RUN: " + ''.join(s) +
    "\nCLEAR CONTEXT AFTER: los ministros del duque de Berganza no se conformaron con ...\n")
key = {r['code']: (r['letter'], r['grade']) for r in csv.DictReader(open('key.tsv'), delimiter='\t')}
rows = list(csv.DictReader(open('cipher_codes_522.tsv'), delimiter='\t'))
on = False
t = []
for r in rows:
    if r['line'] == 'r16' and r['position'] == '2':
        on = True
    if r['line'] == 'r18' and r['position'] == '6':
        break
    if on:
        l, g = key.get(r['sign'], ('_', 'M'))
        nomen = r['sign'].isdigit() and int(r['sign']) >= 48
        t.append('?' if (g != 'S' or l == '_' or nomen) else l)
open('h44/packet_target.txt', 'w').write(
    INSTR + "CLEAR CONTEXT BEFORE (a letter of June 1648 from the Brussels court to an envoy): ... y confiar della. "
    "Pasareis a Cleues a ueros con el Elector de Brandenburg\nDAMAGED RUN: " + ''.join(t) +
    "\nCLEAR CONTEXT AFTER: embian cartas de creencia que uan con esta, y les propondreis si se permitira se leuanten en "
    "aquel pais tres mil hombres de infanteria ...\n")
print(''.join(s))
print(''.join(t), len(t), t.count('?'))
