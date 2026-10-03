"""GAPS21: map the blind call's rows (result.tsv) onto 2077 tokens by DP alignment on shape keywords, then apply the
pre-registered settle rule (prereg.md). Writes aligned.tsv and settle.tsv; prints class summaries. Offline, deterministic."""
import csv, json, collections
D = 'passes/signcmp_gaps21/'
QL = {'Q1': '2077_L05', 'Q2': '2077_L11', 'Q3': '2077_L15', 'Q4': '2077_L12', 'Q5': '2077_L14', 'Q6': '2077_L18'}
TARGET = {'g', 'b', 't', '[u-dots]', '[f-loop]', '[d-loop]', 's'}
# reference tile -> Nieuw-sheet value (names from passes/signcmp_gaps15/blind_key.json; R_<row><shape>)
bk = json.load(open('passes/signcmp_gaps15/blind_key.json'))['refs']
CODEVAL = {'barrect': 'affuyten', 'buskr': 'buskruit', 'AA': 'stukgeschut', 'Gamma': 'code', 'trefoil': 'code', 'tower': 'code', 'DW': 'd'}
def refval(r):
    if r in (None, '', 'NONE'): return None
    n = bk[r][0][2:]
    return CODEVAL.get(n, n[0].lower())
# transcription sign -> shape keywords the call might use
KW = {'g': ['g '], '[lambda]': ['lambda'], 'λ': ['lambda'], '[delta]': ['delta', 'triangle', 'a (latin'], '[hash]': ['hash'],
      's': ['tail (s', ' s '], 'e': ['e (latin'], '3': ['3-shaped'], 'o': ['o small', 'circle'], 'l': ['l tall'],
      '7': ['7-like'], '[u-dots]': ['diaeresis', 'ij'], 'a': ['a (latin'], '[h-loop]': ['h with'], 'h': ['h with'],
      'x': ['x'], '[x-dots]': ['x'], 't': ['t with', 'crossbar'], '5': ['tail (s', 'v'], '[psi]': ['psi'],
      '[pi]': ['pi'], '[f-loop]': ['long s', 'f with'], '6': ['6'], 'b': ['b with', 'b '], '[d-loop]': ['d (latin', 'looped d', 'd '],
      'c': ['c open'], 'y': ['y (latin'], '[v-tall]': ['crossed loop', 'tall v'], '[ezh-dot]': ['3-shaped', 'z'],
      '[sigma]': ['6', 'sigma'], '[amp]': ['&', 'amp'], '[kappa]': ['kappa', 'k'], '[w-tilde]': ['omega', 'w']}
def sim(sign, shape):
    s = ' ' + shape.lower() + ' '
    return 2 if any(k.lower() in s for k in KW.get(sign, [])) else -1
def align(T, Q):
    n, m = len(T), len(Q); G = -1
    F = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): F[i][0] = i * G
    for j in range(1, m + 1): F[0][j] = j * G
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            F[i][j] = max(F[i-1][j-1] + sim(T[i-1][2], Q[j-1]['shape']), F[i-1][j] + G, F[i][j-1] + G)
    i, j, out = n, m, {}
    while i and j:
        if F[i][j] == F[i-1][j-1] + sim(T[i-1][2], Q[j-1]['shape']):
            out[i-1] = (Q[j-1], sim(T[i-1][2], Q[j-1]['shape']) > 0); i -= 1; j -= 1
        elif F[i][j] == F[i-1][j] + G: i -= 1
        else: j -= 1
    return out
toks = {r['line'] + ':' + r['pos']: r for r in csv.DictReader(open('reading_2077_legend_nieuw_tokens.tsv'), delimiter='\t')}
res = list(csv.DictReader(open(D + 'result.tsv'), delimiter='\t'))
al = open(D + 'aligned.tsv', 'w'); al.write('token\tsign\tvalue\tgrade\tq\tshape\tbest\tbest_val\tconf\tsecond\tsecond_val\tconf2\tneighbour_ok\tsettled\n')
summ = collections.defaultdict(collections.Counter)
for q, L in QL.items():
    T = [l.rstrip('\n').split('\t') for l in open('ciphertext_2077_legend.tsv') if l.startswith(L + '\t')]
    Q = [r for r in res if r['line'] == q]
    A = align(T, Q)
    for i, t in enumerate(T):
        k = L + ':' + t[1]; tk = toks.get(k)
        if not tk or tk['sign'] not in TARGET or tk['grade'] != 'M': continue
        r, ok = A.get(i, (None, False))
        settled = ''
        if r and ok:
            bv, sv = refval(r['best']), refval(r['second'])
            c = float(r['conf'] or 0)
            if c >= 0.6 and bv and bv != sv: settled = bv
        summ[tk['sign']]['n'] += 1
        summ[tk['sign']]['mapped'] += bool(r and ok)
        summ[tk['sign']]['settled:' + (settled or '-')] += 1
        al.write('\t'.join(map(str, [k, tk['sign'], tk['value'], tk['grade'], q, (r or {}).get('shape', ''), (r or {}).get('best', ''),
                 refval((r or {}).get('best')), (r or {}).get('conf', ''), (r or {}).get('second', ''), refval((r or {}).get('second')),
                 (r or {}).get('conf2', ''), ok, settled])) + '\n')
for s, c in sorted(summ.items()): print(s, dict(c))
