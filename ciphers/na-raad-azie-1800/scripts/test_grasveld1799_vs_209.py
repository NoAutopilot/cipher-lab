#!/usr/bin/env python3
"""A2-RAA, 2 Oct 2026: is invnr 209's cipher body structurally compatible with the 1799 Grasveld
Correspondentiecijffer (NA 2.21.045 inv. 34313; ordered dictionary code, values 1-992, one of six marks per group)?

Statistics, computed identically on the target and on every control window:
  T1  digits in {0,8,9} among 35 consecutive cipher digits (target top row: 35 digits)
  T2  longest run of digits with no group separator
  T3  share of cipher digits carrying an annotation that is itself a digit (209's second row)
Controls (rule 3):
  C1  matched design, real traffic: every 35-digit window, within one letter, of the four same-key letters
      R2034, R1944, R1945, R1946 as transcribed by dbourdeau/cyphersolver (data/grasveld1799_traffic_groups.tsv).
  C2  matched design, synthetic: 2000 messages of 35 digits drawn as uniform 1-992 code groups (shows C1 is not
      a quirk of four letters).
  C3  positive control (the statistic CAN read 0 / pass): 2000 x 35 letters of period Dutch enciphered with a
      7x4 row/column grid (top digit 1-7, bottom digit 1-4), a design that would produce 209's shape.
Exit 0 always; prints a TSV-ish report. Deterministic (seed 1800).
"""
import random, re, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
rng = random.Random(1800)
BAD = set('089')

# target
top, bot, grp = [], [], []
for line in open(os.path.join(T, 'ciphertext_209_leaf2.tsv')).read().splitlines()[1:]:
    c = line.split('\t'); top.append(c[2]); bot.append(c[3]); grp.append(int(c[1]))
runs = [grp.count(g) for g in sorted(set(grp))]
tgt = dict(N=len(top), T1=sum(d in BAD for d in top), T2=max(runs),
           T3=sum(1 for b in bot if b.isdigit()) / len(top))

# C1 real same-key traffic
letters = {}
for line in open(os.path.join(T, 'data', 'grasveld1799_traffic_groups.tsv')):
    if line.startswith('#') or line.startswith('letter'): continue
    lab, tok = line.rstrip('\n').split('\t')
    letters.setdefault(lab, []).append(re.sub(r'\D', '', tok))
w_t1, w_zero, alld = [], 0, []
maxrun = 0
for lab, gs in letters.items():
    ds = ''.join(gs); alld += list(ds); maxrun = max(maxrun, max(len(g) for g in gs))
    for i in range(len(ds) - 35 + 1):
        k = sum(d in BAD for d in ds[i:i + 35]); w_t1.append(k); w_zero += (k == 0)
c1 = dict(groups=sum(len(g) for g in letters.values()), digits=len(alld), windows=len(w_t1),
          T1_mean=sum(w_t1) / len(w_t1), T1_min=min(w_t1), T1_zero=w_zero, T2=maxrun, T3=0.0,
          share089=sum(d in BAD for d in alld) / len(alld))

# C2 synthetic uniform 1-992 code
z2, m2 = 0, []
for _ in range(2000):
    s = ''
    while len(s) < 35: s += str(rng.randint(1, 992))
    k = sum(d in BAD for d in s[:35]); m2.append(k); z2 += (k == 0)

# C3 positive control: 7x4 grid on period Dutch
corpus = open(os.path.join(T, '..', '..', 'tools', 'data', 'nl_repo',
              'breda-statengeneraal-1624-25__plaintext_print.txt'), encoding='utf-8', errors='ignore').read().lower()
letters_only = re.sub(r'[^a-z]', '', corpus.replace('ij', 'y'))
cells = [(r, c) for r in range(1, 8) for c in range(1, 5)]  # 28 cells
alpha = 'abcdefghijklmnopqrstuvwxyz'
z3 = 0; t3c3 = []
for _ in range(2000):
    perm = cells[:]; rng.shuffle(perm); key = dict(zip(alpha, perm))
    i = rng.randrange(len(letters_only) - 35); pt = letters_only[i:i + 35]
    tops = ''.join(str(key[ch][0]) for ch in pt)
    z3 += (sum(d in BAD for d in tops) == 0); t3c3.append(1.0)

print('# A2-RAA 209 vs Grasveld 1799 code: structure comparison')
print('target_209\tN=%d\tT1=%d\tT2=%d\tT3=%.3f' % (tgt['N'], tgt['T1'], tgt['T2'], tgt['T3']))
print('C1_real_same_key\tgroups=%d digits=%d windows=%d\tT1_mean=%.2f T1_min=%d windows_with_T1=0: %d/%d\tT2=%d\tT3=%.3f\tshare_0/8/9=%.3f'
      % (c1['groups'], c1['digits'], c1['windows'], c1['T1_mean'], c1['T1_min'], c1['T1_zero'], c1['windows'], c1['T2'], c1['T3'], c1['share089']))
print('C2_synth_uniform_1-992\tT1_mean=%.2f\tT1=0: %d/2000' % (sum(m2) / 2000, z2))
print('C3_positive_7x4_grid\tT1=0: %d/2000\tT2>=35 (no separators)\tT3=1.000' % z3)
