#!/usr/bin/env python3
"""XMATCH-0307 (7 Oct 2026): decoy test for the 03:00 key_crossmatch lead
rah-juan-manuel-1521/key_tomokiyo_alpha.tsv -> trew-posthius-1614-18/ciphertext.tsv (stat 5.68, gate 3.29).
Uses key_crossmatch.py's own loaders, model and pair_stats (seed 0, 20 class-shuffled keys) so the statistic is
the nightly's. Decoys: (a) 20 random alphabets on the same code set (values drawn from the key's own value list
with replacement, a different design from a value shuffle); (b) the target's own best simple-substitution key
found by hill-climbing the 4-gram score over the same code set. Writes xmatch_0307_decoy.json beside itself.
Usage: python3 ciphers/trew-posthius-1614-18/xmatch/xmatch_0307_decoy.py"""
import json, random, sys
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'tools'))
import key_crossmatch as kx

key, meta = kx.load_key_meta(ROOT / 'ciphers/rah-juan-manuel-1521/key_tomokiyo_alpha.tsv')
by_lang = kx.reading_files_by_lang(); cmap = kx.build_repo_corpora()
lang, src = kx.language_for(meta['folder'], meta['lang_hint'], by_lang)
c = kx.load_ct_meta(ROOT / 'ciphers/trew-posthius-1614-18/ciphertext.tsv')
signs = c['signs']
model = kx.get_model(lang, exclude_folder=c['folder'], corpora_map=cmap)
def st(k, sg=signs):
    o = kx.pair_stats(k, sg, model, n_shuffle=20, seed=0)['own']; return o
real = st(key)
text, cov = kx.decode_with(key, signs)
used = sorted(set(s for s in signs if s in key))
mapping = {s: key[s]['value'] for s in used}
# (a) random alphabets
vals = [r['value'] for r in key.values()]
rnd = random.Random(307)
rand = []
for i in range(20):
    k = {cd: {'value': rnd.choice(vals)} for cd in key}
    rand.append(st(k)['stat'])
# (b) best simple-sub key: hill-climb 4-gram score over the codes present, letters a-z
letters = [l for l in 'abcdefghiklmnopqrstuxyz']
codes = sorted(set(s for s in signs if s in key))
def ng(k):
    t, _ = kx.decode_with(k, signs); return model.score(t)
best_overall = None
for restart in range(6):
    r = random.Random(1000 + restart)
    cur = {cd: {'value': r.choice(letters)} for cd in key}
    cs = ng(cur)
    for it in range(3000):
        cd = r.choice(codes); old = cur[cd]['value']; cur[cd] = {'value': r.choice(letters)}
        s = ng(cur)
        if s >= cs: cs = s
        else: cur[cd] = {'value': old}
    if best_overall is None or cs > best_overall[0]:
        best_overall = (cs, {k2: dict(v) for k2, v in cur.items()})
bk = best_overall[1]
best = st(bk)
# order-shuffled real key (the order part of the lead null), 20 draws
orders = []
for i in range(20):
    sg = list(signs); random.Random(500 + i).shuffle(sg); orders.append(st(key, sg)['z_ng'])
# Which signs carry the decode: own-folder clear lines vs cipher lines
lines = [l.split('\t') for l in (ROOT / 'ciphers/trew-posthius-1614-18/ciphertext.tsv').read_text().splitlines()[1:] if l.strip()]
groups = Counter(l[0].rsplit('_', 1)[0] if l[0][-1].isdigit() else l[0] for l in lines)
out = dict(lang=lang, lang_src=src, n_tokens=len(signs), coverage=round(kx.coverage_of(key, signs), 3),
           real=dict(stat=real['stat'], z_ng=real['z_ng'], z_vf=real['z_vf'], score=real['score']),
           random_alphabets=dict(stats=[round(x, 2) for x in rand], max=round(max(rand), 2),
                                 mean=round(sum(rand) / len(rand), 2), n_ge_real=sum(x >= real['stat'] for x in rand)),
           best_simple_sub=dict(stat=best['stat'], z_ng=best['z_ng'], score=best['score'],
                                decode=kx.decode_with(bk, signs)[0].replace(' ', '')[:300]),
           order_shuffled_zng=dict(max=round(max(orders), 2), mean=round(sum(orders) / len(orders), 2)),
           code_to_value_used=mapping, decode=text.replace(' ', ''), line_groups=dict(groups))
(Path(__file__).parent / 'xmatch_0307_decoy.json').write_text(json.dumps(out, indent=1, ensure_ascii=False))
print(json.dumps({k: v for k, v in out.items() if k not in ('decode',)}, ensure_ascii=False, indent=1)[:3000])
print('DECODE:', out['decode'][:400])
