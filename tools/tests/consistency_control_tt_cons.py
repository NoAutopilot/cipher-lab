#!/usr/bin/env python3
"""TT-CONS controls for tools/decode_key.py --consistency (pass lines pre-registered in tools/tests/PREREG-TT-CONS.md).

Known answer (Tomokiyo, breaking.htm): the page's own cipher and key (tools/tests/fixtures/tomokiyo-breaking/), where the
page reports 9(W) consistent in 'wards' and 'with' and 24(O) in 'cooperate' and 'you'. Repo period/known-plaintext keys:
rah-canada-1869 (C, Spanish, lexicon es) and nla-heinrich-braunschweig-1519 (H, German, lexicon de).
Nulls, each able to fail differently from the true key because the lexicon test depends on the values themselves:
  wrong value  one mid-frequency letter code is given each other letter in turn; its lexicon stem count is compared with
               the true value's (the true value must rank first);
  random key   the letter values are permuted over the letter codes (20 seeds); share of codes in >=2 unrelated words.
Run: python3 tools/tests/consistency_control_tt_cons.py  (offline; prints one block per case)"""
import collections, json, os, random, statistics, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import decode_key as dk

CASES = [('tools/tests/fixtures/tomokiyo-breaking', 'en', 0, ['9', '24']),
         ('ciphers/rah-canada-1869', 'es', 0, []),
         ('ciphers/nla-heinrich-braunschweig-1519', 'de', 0, []),
         ('ciphers/nla-heinrich-braunschweig-1519', 'de', 1, [])]


def jobs_of(t):
    cfg = json.load(open(os.path.join(ROOT, t, 'decode.json')))
    return [dict(cfg.get('defaults', {}), **j) for j in cfg.get('jobs', [cfg])]


def letter_codes(key, job):
    return [c for c, r in key.items() if r['value'] and len(r['value']) == 1 and r['value'].isalpha()]


def share_multi(rows):
    return sum(d['category'] == 'multi' for d in rows) / len(rows) if rows else 0.0


def main():
    for t, lang, ji, named in CASES:
        target = os.path.join(ROOT, t)
        job = jobs_of(t)[ji]
        lex = dk.load_lexicon(lang)
        rows, meta = dk.consistency(target, job, lex)
        by = {d['code']: d for d in rows}
        print(f"== {t} job {meta['ciphertext']} lexicon {lang}: {meta['how']}; {meta['words']} words")
        print(f"   true key: codes {len(rows)}, multi {share_multi(rows):.3f} "
              f"({sum(d['category']=='multi' for d in rows)}/{len(rows)})")
        for c in named:
            d = by.get(c)
            print(f"   named code {c}: {d['category'] if d else 'absent'}, stems {d['n_stems'] if d else 0}: "
                  f"{' '.join(d['sample']) if d else ''}")
        key0 = dk.load_keys(target, job.get('key', 'key.tsv'))
        lc = letter_codes(key0, job)
        recs, _ = dk.graded_recs(target, job)
        freq = collections.Counter(r['sign'] for r in recs if r['kind'] == 'sign' and r['sign'] in lc)
        ranked = [c for c, _ in freq.most_common()]
        if not ranked:
            print('   no letter codes'); continue
        mid = ranked[len(ranked) // 2] if t.endswith('breaking') is False else '14'
        true_v = key0[mid]['value']
        alphabet = sorted({key0[c]['value'].lower() for c in lc})
        res = {}
        for v in alphabet:
            def edit(k, v=v):
                k = dict(k); k[mid] = dict(k[mid], value=v); return k
            r2, _ = dk.consistency(target, job, lex, key_edit=edit)
            d = next((x for x in r2 if x['code'] == mid), None)
            res[v] = d['n_stems'] if d else 0
        wrong = [s for v, s in res.items() if v != true_v.lower()]
        rank = 1 + sum(s >= res[true_v.lower()] for s in wrong)
        print(f"   wrong value: code {mid} (true {true_v}, x{freq[mid]}): true stems {res[true_v.lower()]}, "
              f"wrong median {statistics.median(wrong):.1f} max {max(wrong)} over {len(wrong)} letters; "
              f"true rank {rank} (1 = strictly highest)")
        shares = []
        for seed in range(20):
            rnd = random.Random(seed)
            vals = [key0[c]['value'] for c in lc]
            rnd.shuffle(vals)
            perm = dict(zip(lc, vals))
            def edit(k, perm=perm):
                k = dict(k)
                for c, v in perm.items():
                    k[c] = dict(k[c], value=v)
                return k
            r3, _ = dk.consistency(target, job, lex, key_edit=edit)
            shares.append(share_multi(r3))
        print(f"   random key (20 seeds): multi share mean {statistics.mean(shares):.3f}, max {max(shares):.3f}")
        rows_nolex, _ = dk.consistency(target, job, None)
        print(f"   without lexicon (true key): multi {share_multi(rows_nolex):.3f}")


if __name__ == '__main__':
    main()
