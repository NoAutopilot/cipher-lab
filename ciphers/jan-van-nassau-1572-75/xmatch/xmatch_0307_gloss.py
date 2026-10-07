#!/usr/bin/env python3
"""XMATCH-0307 (7 Oct 2026): score the 03:00 key_crossmatch lead _keys/gonzaga-nevers-asmn-ag423-c396/key.tsv ->
j5s/ciphertext_glossed_5557_5552.tsv (stat 4.22, own order-shuffled p99 4.13) directly against the leaf's own
interlinear gloss. Per glossed token: exact (folded value == folded gloss), prefix (gloss starts with value, or
value with gloss), and letter agreement (share of the gloss's letters matched position by position from the start).
Control: the same three numbers for 1000 keys with values shuffled within value class (key_crossmatch's own
shuffled_key_by_class) -- this control can differ from the target, since the statistic depends on which value each
code carries. Also the nightly's own pair_lead_null (200 draws). Writes xmatch_0307_gloss.json beside itself."""
import csv, json, random, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'tools'))
import key_crossmatch as kx, judge_plaintext as jp

key, meta = kx.load_key_meta(ROOT / 'ciphers/_keys/gonzaga-nevers-asmn-ag423-c396/key.tsv')
rows = list(csv.DictReader(open(ROOT / 'ciphers/jan-van-nassau-1572-75/j5s/ciphertext_glossed_5557_5552.tsv'), delimiter='\t'))
pairs = [(r['token'], jp.fold(r['gloss'].split('(')[0])) for r in rows if r['gloss'].strip()]
def score(k):
    ex = pre = 0; la = 0.0; cov = 0
    for tok, g in pairs:
        row = k.get(tok)
        if not row or not row.get('value'):
            continue
        v = jp.fold(row['value'].split('|')[0]); cov += 1
        if not v: continue
        ex += v == g
        pre += g.startswith(v) or v.startswith(g)
        la += sum(a == b for a, b in zip(v, g)) / max(len(g), 1)
    return dict(exact=ex, prefix=pre, letter=round(la, 3), covered=cov)
real = score(key)
rnd = random.Random(307)
nulls = [score(kx.shuffled_key_by_class(key, rnd)) for _ in range(1000)]
def p(field):
    xs = sorted(n[field] for n in nulls)
    return dict(mean=round(sum(xs) / len(xs), 3), p95=xs[949], p99=xs[989], n_ge_real=sum(x >= real[field] for x in xs))
decoded = [(t, g, (key.get(t) or {}).get('value')) for t, g in pairs]
# nightly's own lead null on the whole ciphertext
by_lang = kx.reading_files_by_lang(); cmap = kx.build_repo_corpora()
lang, _ = kx.language_for(meta['folder'], meta['lang_hint'], by_lang)
c = kx.load_ct_meta(ROOT / 'ciphers/jan-van-nassau-1572-75/j5s/ciphertext_glossed_5557_5552.tsv')
model = kx.get_model(lang, exclude_folder=c['folder'], corpora_map=cmap)
lead = kx.pair_lead_null(key, c['signs'], model)
out = dict(n_glossed=len(pairs), lang=lang, real=real, control={f: p(f) for f in ('exact', 'prefix', 'letter')},
           lead_null=lead, decoded=decoded, full_decode=kx.decode_with(key, c['signs'])[0])
(Path(__file__).parent / 'xmatch_0307_gloss.json').write_text(json.dumps(out, indent=1, ensure_ascii=False))
print(json.dumps({k: v for k, v in out.items() if k != 'full_decode'}, ensure_ascii=False))
print('DECODE:', out['full_decode'][:300])
