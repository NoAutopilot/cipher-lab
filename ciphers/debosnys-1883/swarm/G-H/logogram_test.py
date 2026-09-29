"""Task 3 control: do the Copiale's known word symbols (the large logograms, [K11] s.5) show the positional signature
H31 found for Debosnys's pictograms (line-initial far above chance)? Measured on the whole public Copiale
transcription, with the same kind of null H31 used (within-line shuffles, 2000 runs).
Also: rate at which a logogram's neighbours are word spaces (gold), against letters' rate."""
import collections, random, json
from copiale_key import LOGO, SPACE
rows = [l.rstrip('\n').split('\t') for l in open('data/copiale_tokens.tsv')][1:]
lines = collections.OrderedDict()
for pg, li, pos, t, g in rows: lines.setdefault((int(pg), int(li)), []).append(t)
L = [v for v in lines.values() if v]
def initial(ls, cls): return sum(1 for l in ls if l[0] in cls)
def final(ls, cls): return sum(1 for l in ls if l[-1] in cls)
obs_i, obs_f = initial(L, LOGO), final(L, LOGO)
rng = random.Random(1); ni = []; nf = []
for _ in range(2000):
    sh = [rng.sample(l, len(l)) for l in L]; ni.append(initial(sh, LOGO)); nf.append(final(sh, LOGO))
ni.sort(); nf.sort()
n_logo = sum(t in LOGO for l in L for t in l)
lines_with = sum(any(t in LOGO for t in l) for l in L)
# neighbour = space?
flat = [t for l in L for t in l]
def nb(cls):
    b = a = n = 0
    for i, t in enumerate(flat):
        if t in cls and 0 < i < len(flat) - 1:
            n += 1; b += flat[i-1] in SPACE; a += flat[i+1] in SPACE
    return round(b / n, 3), round(a / n, 3), n
letters = {t for t in set(flat) if t not in SPACE and t not in LOGO and t != ':'}
res = {'lines': len(L), 'logogram_tokens': n_logo, 'lines_with_logogram': lines_with,
       'line_initial': obs_i, 'line_initial_null_p50_p99_max': [ni[1000], ni[1980], ni[-1]],
       'p_initial': sum(x >= obs_i for x in ni) / 2000,
       'line_final': obs_f, 'line_final_null_p50_p99_max': [nf[1000], nf[1980], nf[-1]],
       'p_final': sum(x >= obs_f for x in nf) / 2000,
       'prev_is_space_next_is_space_logo': nb(LOGO), 'same_for_letter_signs': nb(letters)}
print(json.dumps(res, indent=1)); json.dump(res, open('logogram_copiale.json', 'w'), indent=1)
