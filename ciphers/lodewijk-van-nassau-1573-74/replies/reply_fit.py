"""A2-LVN4 (2 Oct 2026): test names Orange writes back in his printed replies (Groen IV CDXXVII -> 4610,
CDXXXIII -> 4611, CDLXXXIV -> 4616) against the contexts of the once/twice-seen name codes (>151) in those letters.

Rule (pre-registered here before the first run; no threshold tuned after):
  reply window  = the 8 words either side of the name's anchor in the reply (anchor itself excluded), content words of
                  >= 5 letters not in STOP, folded (accents off, v->u, j->i, y->i), stemmed to their first 5 letters;
  cipher context = up to 30 decoded letters either side of the code occurrence (key_full v3 readings; NULL dropped,
                  U shown as '#', multi-letter name codes spelled out), folded the same way, no word division;
  fit(name, code) = max over the code's occurrences of the number of distinct window stems found as substrings;
  a code gets a PROPOSAL when its best name has fit >= 2 and no other name ties it.
Controls (rule 3; each can differ from the target on the proposal count):
  (a) known answer: every occurrence of a key_full name code already graded C/H in the three letters (153, 161, 192,
      200, 202, 221, 223, ...) is hidden and scored the same way against its own letter's reply; a hit is a proposal
      whose name matches the true value (match table KNOWN below). Gate: hit rate >= 0.50 AND wrong proposals <= hits.
  (b) mismatched reply: each letter scored against the two replies that do NOT answer it; the real pairing must give
      more proposals than the mismatched mean, else the method does not discriminate at this length.
Outputs replies/fit.tsv (all code x name fits for the true pairing) and the summary on stdout.
Usage: python3 replies/reply_fit.py"""
import csv, os, re, unicodedata, statistics
D = os.path.dirname(os.path.abspath(__file__))
T = D + '/..'
STOP = set('quelle quelque toutesfois encoires aultre aultres comme lesquelles lesquels laquelle lequel dicte dictes dict '
           'avoir estre faire monsieur frere vostre nostre seront serons pourroient vouldroient voudrois quant regard mesme '
           'aussi aussy depuis apres avant entre contre selon pource parce toutes celle celles ceulx cellui cela ceste cest '
           'point plusieurs encore bonne grande grand'.split())
def fold(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return s.replace('v', 'u').replace('j', 'i').replace('y', 'i')
def words(s): return re.findall(r"[a-z0-9]+", fold(s))
REPLY = {'CDXXVII': 'groen_IV_CDXXVII.txt', 'CDXXXIII': 'groen_IV_CDXXXIII.txt', 'CDLXXXIV': 'groen_IV_CDLXXXIV.txt'}
LETTER_OF = {'CDXXVII': '4610', 'CDXXXIII': '4611', 'CDLXXXIV': '4616'}
def reply_body(fn):
    t = open(f'{T}/groen/{fn}').read()
    t = t[t.index('Lettre CD'):]
    t = t[:t.find('Vorige [')]
    t = re.sub(r'Ga naar (voetnoot|margenoot)\S*\s*\[#\d+\]', ' ', t)
    t = re.sub(r'\[pagina \d+\]|\[p\. \d+\]', ' ', t)
    return words(t)
NAMES = list(csv.DictReader(open(D + '/names_back.tsv'), delimiter='\t'))
def windows(reply):
    w = reply_body(REPLY[reply]); out = {}
    for n in NAMES:
        if n['reply'] != reply: continue
        a = words(n['anchor (as printed in Groen)'])[-1]
        stems = set()
        for i, x in enumerate(w):
            if x == a:
                for y in w[max(0, i - 8):i] + w[i + 1:i + 9]:
                    if len(y) >= 5 and y not in STOP and y != a: stems.add(y[:5])
                break
        out[n['name']] = stems
    return out
CODES = {'4610': '180 182 184 186 191 194 203 205 225', '4611': '174 175 187 199 204 211 214 225 228 232 245 248 254 280 311 331 335', '4616': '313'}
KNOWN = {'hollande': 'hollande', 'harlem': 'harlem', 'herzogvonalba': 'albe', 'landgraf': 'landgrave', 'franckreich': 'france roidefrance',
         'roidespagne': '-', 'pfaltzgraf': '-', 'prinzzuoranien': '-', 'herzogvonsachsen': '-'}
def letter_rows(L):
    rows = [r for r in csv.DictReader(open(f'{T}/reading_{L}_full_tokens.tsv'), delimiter='\t') if r['value'] != 'NULL']
    return rows
def ctx(rows, i):
    def s(r): return '#' if (r['grade'] == 'U' or r['value'] == '?') else fold(r['value'])
    left = ''.join(s(r) for r in rows[:i])[-30:]; right = ''.join(s(r) for r in rows[i + 1:])[:30]
    return left + '|' + right
def score(stems, c): return sum(1 for st in stems if st in c)
def run(L, reply, targets):
    win = windows(reply); rows = letter_rows(L); occ = {}
    for i, r in enumerate(rows):
        if r['sign'] in targets: occ.setdefault(r['sign'], []).append(ctx(rows, i))
    res = {}
    for code, cs in occ.items():
        fits = {n: max(score(st, c) for c in cs) for n, st in win.items()}
        best = max(fits.values()); top = [n for n, f in fits.items() if f == best]
        res[code] = (fits, top[0] if (best >= 2 and len(top) == 1) else None, best)
    return res
def known_codes(L):
    k = {r['code']: r['value'] for r in csv.DictReader(open(T + '/key_full.tsv'), delimiter='\t') if r['value'] in KNOWN and r['grade'] in 'CH'}
    present = {r['sign'] for r in letter_rows(L)}
    return {c: v for c, v in k.items() if c in present}
if __name__ == '__main__':
    out = open(D + '/fit.tsv', 'w'); out.write('letter\treply\tcode\tname\tfit\n')
    print('== (a) known-answer control: hidden C/H name codes, own reply')
    hits = wrong = n = 0
    for reply, L in LETTER_OF.items():
        kc = known_codes(L)
        res = run(L, reply, set(kc))
        for c, (fits, prop, best) in sorted(res.items()):
            truth = KNOWN[kc[c]].split(); n += 1
            ok = prop is not None and prop in truth
            hits += ok; wrong += (prop is not None and not ok)
            print(f'  {L} {c} true={kc[c]:16s} proposal={prop} best={best} truth-in-reply={any(t in dict(fits) for t in truth)}')
    print(f'  known-answer: {hits} hit, {wrong} wrong proposals, {n} hidden codes; gate hit rate >= 0.50 and wrong <= hits:',
          'PASS' if n and hits / n >= 0.5 and wrong <= hits else 'FAIL')
    print('== target: open name codes, true reply')
    real = 0
    for reply, L in LETTER_OF.items():
        res = run(L, reply, set(CODES[L].split()))
        for c, (fits, prop, best) in sorted(res.items(), key=lambda t: int(t[0])):
            for nm, f in sorted(fits.items(), key=lambda t: -t[1]):
                if f: out.write(f'{L}\t{reply}\t{c}\t{nm}\t{f}\n')
            real += prop is not None
            if best >= 1: print(f'  {L} {c} proposal={prop} best={best} top={sorted(fits.items(), key=lambda t: -t[1])[:3]}')
    print('== (b) mismatched-reply control')
    mm = []
    for L in CODES:
        for reply in REPLY:
            if LETTER_OF[reply] == L: continue
            res = run(L, reply, set(CODES[L].split()))
            mm.append((L, reply, sum(p is not None for _, p, _ in res.values())))
    for row in mm: print('  ', *row)
    per = {}
    for L, reply, k in mm: per.setdefault(reply, 0)
    tot_mm = sum(k for *_, k in mm) / 2  # two wrong replies per letter -> mean over the two
    print(f'  proposals: true pairing {real}; mismatched mean {tot_mm:.1f}; discriminates:', 'yes' if real > tot_mm else 'NO')
