# R7-SUR (account 2), 6 Oct 2026: shuffle the 14 single-sign tiles into blind labels. Queries (4 targets + 2 known-answer
# controls) become Q1-Q6, references R1-R8, each set shuffled with seed 20261006. Run from the target folder.
import json, os, random, shutil, sys
sys.path.insert(0, 'passes/signcmp_r7sur')
from cut_tiles import SIGNS
D = 'passes/signcmp_r7sur/'
os.makedirs(D + 'tiles', exist_ok=True)
qs = [s for s in SIGNS if s[4] in ('query', 'control-query')]
rs = [s for s in SIGNS if s[4].startswith('ref')]
rng = random.Random(20261006)
rng.shuffle(qs); rng.shuffle(rs)
key = {}
for pre, group in (('Q', qs), ('R', rs)):
    for i, s in enumerate(group, 1):
        shutil.copy(f'images/crops_r7sur/{s[0]}.jpg', f'{D}tiles/{pre}{i}.jpg')
        key[f'{pre}{i}'] = {'id': s[0], 'linepos': s[1], 'code': s[2], 'current': s[3], 'role': s[4], 'box': s[5]}
json.dump(key, open(D + 'blind_key.json', 'w'), indent=1)
print({k: v['id'] for k, v in key.items()})
