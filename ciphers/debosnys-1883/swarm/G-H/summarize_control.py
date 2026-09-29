"""Summarise control/*.json: per size, blind recovery, German rank, space precision/recall, gap vs shuffled null."""
import json, glob, statistics as st
out = {}
for n in (1200, 770, 135):
    B = [json.load(open(f)) for f in sorted(glob.glob(f'control/blind_n{n}_s*.json'))]
    N = [json.load(open(f)) for f in sorted(glob.glob(f'control/null_n{n}_s*.json'))]
    if not B: continue
    out[n] = {'windows': len(B),
              'recovery': [r['recovery'] for r in B],
              'recovery_median': st.median(r['recovery'] for r in B),
              'windows_ge_70': sum(r['recovery'] >= 0.70 for r in B),
              'german_rank': [r['screen_rank_de'] for r in B],
              'space_precision_recall': [(r['a_space_precision'], r['a_space_recall']) for r in B],
              'best_gap': [r['c_screen'][0]['gap'] for r in B],
              'null_best_gap': [r['c_screen'][0]['gap'] for r in N],
              'homophone_pair_precision_vs_chance': [(r.get('b_tight_merge_pair_precision'), r.get('b_chance_pair_precision')) for r in B]}
json.dump(out, open('control/SUMMARY.json', 'w'), indent=1)
for n, v in out.items():
    print(n, 'rec', v['recovery'], '>=70:', v['windows_ge_70'], '/', v['windows'], 'deRank', v['german_rank'],
          'gap', v['best_gap'], 'null', v['null_best_gap'])
# noise and size brackets
br = {}
for pat, label in [('noise0.03_n1200', '1200 @3pct'), ('noise0.08_n1200', '1200 @8pct'), ('noise0.15_n1200', '1200 @15pct'),
                   ('noise0_n658', '658 clean'), ('noise0.05_n658', '658 @5pct'), ('noise0.10_n658', '658 @10pct'),
                   ('n15_n658', '658 @15pct'), ('r12_n658', '658 clean, 2x restarts (the two failures)'),
                   ('r12n15_n658', '658 @15pct, 2x restarts')]:
    rs = [json.load(open(f)) for f in sorted(glob.glob(f'control/{pat}_s*.json'))]
    br[label] = {'recovery': [r['recovery'] for r in rs], 'german_rank': [r['screen_rank_de'] for r in rs]}
    print(label, br[label])
out['brackets'] = br
json.dump(out, open('control/SUMMARY.json', 'w'), indent=1)
