#!/usr/bin/env python3
"""Group E picture tests (DEB-SWARM-E, 29 Sept 2026). Settled drafts via scripts/settled_lines.py, punctuation-class
boxes dropped exactly as H31 (BLOB HOOK-L DASH-H _ MULTI). Null: 10,000 within-line shuffles (each line's multiset
fixed), which can move every statistic below (rule 3: the control can differ from the target).
E1  vessel signs (BUCKET, PICT-JUG, BOX-M: drawn cups/jug, eye-checked on the page) at line end. Run with and without
    the one page-edge artefact kept as a sign (c2a_L02 pos 28 DASH-V, a 5 px bar at the image's right edge, x 1047).
    E1b: only the two vessels H33 could not have selected (PICT-JUG, BOX-M: 1 token each, below H33's >=3 floor).
E2  H31 sensitivity: the pictogram class with the PAGEMAP corrections -- drawings the drafts do not carry as a pictogram
    (c2a_L04 wavy-serpent drawing at line start, c2a_L10 flying bird, c2a_L15 church drawing whose caption dots are
    coded BLOB BAR-SOLID x3 BAR-THIN, c2a_L17 anchor coded MULTI, c2b_L01 trowel coded PICT-LEAF (already a pictogram),
    c2b_L02 hammer (no box), c2b_L02 CHAIN = three linked rings, c2b_L07 dove before the sun) -- and vessels moved out.
E3  the word-initial reading (runner's open idea): if a pictogram writes a word-initial syllable and X divides words,
    interior pictograms are preceded by X more than chance and followed by X no more than chance. Both sides reported.
Writes pict_tests.json. Reads nothing under swarm/controls/."""
import os, sys, json, random, collections
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.normpath(os.path.join(here, '..', '..'))
sys.path.insert(0, os.path.join(root, 'scripts')); from settled_lines import settled_lines
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
VESSEL = {'BUCKET', 'PICT-JUG', 'BOX-M'}
def is_pict(s): return s.startswith('PICT-') or s in ('SUN', 'STAR', 'HEART', 'RAM', 'DRAWN', 'CHAIN')
raw = settled_lines(root, 'c')
def lines_base(fix_edge):
    out = collections.OrderedDict()
    for k, v in raw.items():
        v = list(v)
        if fix_edge and k == 'c2a_L02' and len(v) >= 28 and v[27] == 'DASH-V': v = v[:27] + v[28:]
        out[k] = [s for s in v if s not in PUNCT]
    return out
def corrected():
    """PAGEMAP corrections as described in the docstring; DRAWN marks a drawing the drafts do not carry as a pictogram."""
    by = collections.OrderedDict((k, list(v)) for k, v in raw.items())
    by['c2a_L02'] = by['c2a_L02'][:27] + by['c2a_L02'][28:]          # edge artefact
    by['c2a_L04'] = ['DRAWN'] + by['c2a_L04'][4:]                     # boxes 1-4 '_' = the wavy drawing
    v = by['c2a_L10']; by['c2a_L10'] = v[:4] + ['DRAWN'] + v[4:]       # bird between box 4 (x112) and box 5 (x198)
    v = by['c2a_L15']; by['c2a_L15'] = v[:3] + ['DRAWN'] + v[10:]      # boxes 4-10 = caption dots/marks of the church
    v = by['c2a_L17']; assert v[5] == 'MULTI'; by['c2a_L17'] = v[:5] + ['PICT-ANCHOR'] + v[6:]
    v = by['c2b_L02']; assert v[4] == 'CHAIN'; by['c2b_L02'] = v[:4] + ['DRAWN'] + v[4:]   # hammer before the links
    by['c2b_L07'] = ['DRAWN'] + by['c2b_L07']                          # dove left of the sun
    return collections.OrderedDict((k, [s for s in v if s not in PUNCT]) for k, v in by.items())
def shuffle_test(lines, stat, trials=10000, seed=7):
    obs = stat(lines); rng = random.Random(seed); null = []
    for _ in range(trials):
        sh = []
        for l in lines: c = l[:]; rng.shuffle(c); sh.append(c)
        null.append(stat(sh))
    null.sort()
    return dict(obs=obs, lo=null[int(.025 * trials)], hi=null[int(.975 * trials) - 1], mean=round(sum(null) / trials, 3),
                p_ge=sum(x >= obs for x in null) / trials)
def final_in(cls): return lambda ls: sum(1 for l in ls if l and l[-1] in cls)
def initial_pict(excl=()): return lambda ls: sum(1 for l in ls if l and is_pict(l[0]) and l[0] not in excl)
def final_pict(excl=()): return lambda ls: sum(1 for l in ls if l and is_pict(l[-1]) and l[-1] not in excl)
def x_before(ls): return sum(1 for l in ls for i in range(1, len(l)) if is_pict(l[i]) and l[i - 1] == 'X')
def x_after(ls): return sum(1 for l in ls for i in range(len(l) - 1) if is_pict(l[i]) and l[i + 1] == 'X')
out = {}
for fix in (False, True):
    L = list(lines_base(fix).values()); tag = 'edge_fixed' if fix else 'as_drafted'
    out[f'E1_vessel_final_{tag}'] = dict(tokens=sum(s in VESSEL for l in L for s in l), **shuffle_test(L, final_in(VESSEL)))
    out[f'E1b_jug_boxm_final_{tag}'] = dict(tokens=sum(s in {'PICT-JUG', 'BOX-M'} for l in L for s in l),
                                            **shuffle_test(L, final_in({'PICT-JUG', 'BOX-M'})))
L0 = list(lines_base(True).values()); LC = list(corrected().values())
out['E2_H31_reproduced_edge_fixed'] = shuffle_test(L0, initial_pict())
out['E2_initial_corrected_class_no_vessels'] = dict(pict_tokens=sum(is_pict(s) and s not in VESSEL for l in LC for s in l),
                                                    **shuffle_test(LC, initial_pict(VESSEL)))
out['E2_final_corrected_class_no_vessels'] = shuffle_test(LC, final_pict(VESSEL))
out['E2_final_corrected_class_with_vessels'] = shuffle_test(LC, lambda ls: sum(1 for l in ls if l and (is_pict(l[-1]) or l[-1] in VESSEL)))
out['E3_X_before_pict_corrected'] = shuffle_test(LC, x_before)
out['E3_X_after_pict_corrected'] = shuffle_test(LC, x_after)
out['E3_X_before_pict_drafts'] = shuffle_test(L0, x_before)
out['E3_X_after_pict_drafts'] = shuffle_test(L0, x_after)
json.dump(out, open(os.path.join(here, 'pict_tests.json'), 'w'), indent=1)
for k, d in out.items(): print(k, d)
# --- added: p_le for E3, and class controls for E1 (random id sets of the same token count, rule 3 H31b-style) ---
for k in ('E3_X_before_pict_corrected', 'E3_X_before_pict_drafts'):
    lines = LC if 'corrected' in k else L0; obs = out[k]['obs']; rng = random.Random(11); le = 0
    for _ in range(10000):
        sh = [rng.sample(l, len(l)) for l in lines]; le += x_before(sh) <= obs
    out[k]['p_le'] = le / 10000
cnt = collections.Counter(s for l in L0 for s in l)
fin = collections.Counter(l[-1] for l in L0 if l)
pool = [s for s in cnt if s not in VESSEL and not is_pict(s) and s != 'X']
rng = random.Random(5); hits = 0; tries = 0; best = []
while tries < 2000:
    rng.shuffle(pool); pick = []; n = 0
    for s in pool:
        if n + cnt[s] <= 5: pick.append(s); n += cnt[s]
        if n == 5: break
    if n != 5: continue
    tries += 1; f = sum(fin[s] for s in pick); best.append(f); hits += f >= 5
out['E1_class_control'] = dict(sets=tries, all5_final=hits, p97_5=sorted(best)[int(.975 * tries) - 1], max=max(best))
single = [s for s in pool if cnt[s] == 1]; sf = sum(fin[s] for s in single)
out['E1b_class_control_singletons'] = dict(singleton_ids=len(single), singleton_final=sf,
    p_two_random_singletons_both_final=round(sf / len(single) * (sf - 1) / (len(single) - 1), 5))
json.dump(out, open(os.path.join(here, 'pict_tests.json'), 'w'), indent=1)
for k in ('E3_X_before_pict_corrected', 'E3_X_before_pict_drafts', 'E1_class_control', 'E1b_class_control_singletons'): print(k, out[k])
# --- E4 (logogram-in-phrase reading): if a repeated pictogram names a word inside recurring phrases, its immediate
# neighbours repeat across its occurrences more than chance. Statistic: over pictogram ids with >= 2 tokens, the number
# of (id, left neighbour) and (id, right neighbour) pairs seen twice or more. Same within-line shuffle null.
def neigh_repeats(ls):
    c = collections.Counter()
    for l in ls:
        for i, s in enumerate(l):
            if is_pict(s) and s not in VESSEL:
                if i > 0: c[(s, 'L', l[i - 1])] += 1
                if i + 1 < len(l): c[(s, 'R', l[i + 1])] += 1
    return sum(1 for v in c.values() if v >= 2)
out['E4_pict_neighbour_repeats_corrected'] = shuffle_test(LC, neigh_repeats)
out['E4_pict_neighbour_repeats_drafts'] = shuffle_test(L0, neigh_repeats)
json.dump(out, open(os.path.join(here, 'pict_tests.json'), 'w'), indent=1)
for k in ('E4_pict_neighbour_repeats_corrected', 'E4_pict_neighbour_repeats_drafts'): print(k, out[k])
# E4 power: half of each repeated pictogram's occurrences get the same right-hand neighbour as its first occurrence
# (a phrase recurring at half strength); scored against the same null band.
cntp = collections.Counter(s for l in LC for s in l if is_pict(s) and s not in VESSEL); firstR = {}; planted = []; seen = collections.Counter()
for l in LC:
    l = l[:]
    for i, s in enumerate(l[:-1]):
        if cntp.get(s, 0) >= 2:
            seen[s] += 1
            if s not in firstR: firstR[s] = l[i + 1]
            elif seen[s] % 2 == 0: l[i + 1] = firstR[s]
    planted.append(l)
out['E4_power_half_strength_phrase'] = dict(obs=neigh_repeats(planted), band_hi=out['E4_pict_neighbour_repeats_corrected']['hi'])
json.dump(out, open(os.path.join(here, 'pict_tests.json'), 'w'), indent=1); print('E4 power', out['E4_power_half_strength_phrase'])
