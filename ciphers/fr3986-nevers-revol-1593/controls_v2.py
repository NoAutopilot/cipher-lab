#!/usr/bin/env python3
"""controls_v2.py -- rule-3 controls for the f.198 verso v2 draft (GAPS3, 2 Oct 2026).

Reads ciphertext_v2.tsv (one row per cipher sign, line = f198v_LNNrK run id) and the v2 key
(tools/keys/key60.tsv merged with key_atlas_extra.tsv through tools/decode_key.py's own loader, so a
collision is a|b exactly as the decode shows it). For a|b values the first alternative is scored.
  1. real: mean log10 4-gram score (tools/judge_plaintext.py's fr model, fr16 corpus) of the decoded
     run letters, runs joined in page order;
  2. 200 value-shuffled keys (the key's values permuted over its signs, seeds 1..200): same score; rank and z;
  3. judge_plaintext.py's judge() on the real decode and on 20 shuffled-target decodes (sign order permuted
     within the whole draft, seeds 1..20, real key): PASS counts.
Writes controls_v2.txt; --check exits 1 if the committed file differs. Deterministic.
"""
import json, os, random, statistics, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import decode_key as dk
import judge_plaintext as jp

def load():
    key = dk.load_keys(HERE, ['../../tools/keys/key60.tsv', 'key_atlas_extra.tsv'])
    rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(HERE, 'ciphertext_v2.tsv')) if l.strip() and not l.startswith('#')]
    rows = rows[1:]
    return key, [r[2] for r in rows]

def val(key, s):
    if s not in key:
        return ''
    v = key[s]['value'].split('|')[0]
    return v

def decode(key, signs):
    return ' '.join(val(key, s) for s in signs)

def main():
    key, signs = load()
    spec = json.load(open(os.path.join(ROOT, 'specs', 'fr3986-nevers-f198.json')))
    corp = jp.LANG_CORPORA[spec['judge']['language']]
    model = jp.NgramModel([jp.read_corpus(p) for p in corp])
    real_txt = decode(key, signs)
    real = model.score(real_txt)
    codes = sorted(key); vals = [key[c]['value'] for c in codes]
    sh = []
    for seed in range(1, 201):
        v = vals[:]; random.Random(seed).shuffle(v)
        k2 = {c: {'value': x} for c, x in zip(codes, v)}
        sh.append(model.score(decode(k2, signs)))
    rank = 1 + sum(1 for x in sh if x >= real)
    mu, sd = statistics.mean(sh), statistics.pstdev(sh)
    jr = jp.judge(spec, real_txt)
    tp = 0; tscores = []
    for seed in range(1, 21):
        s2 = signs[:]; random.Random(seed).shuffle(s2)
        o = jp.judge(spec, decode(key, s2)); tp += o['pass']; tscores.append(o['checks']['language']['score'])
    unk = sorted({s for s in signs if s not in key})
    out = [f'signs {len(signs)}; unkeyed tags {len(unk)}: {" ".join(unk)}',
           f'decoded letters {len(jp.fold(real_txt))}',
           f'real 4-gram score {real:.4f}',
           f'value-shuffled keys (200): mean {mu:.4f} sd {sd:.4f} max {max(sh):.4f}; real rank {rank}/201; z {(real-mu)/sd if sd else 0:.2f}',
           f'judge on real decode: {"PASS" if jr["pass"] else "FAIL"} {json.dumps(jr["checks"], sort_keys=True)}',
           f'shuffled-target decodes (20): judge PASS {tp}/20; language scores min {min(tscores):.3f} median {statistics.median(tscores):.3f} max {max(tscores):.3f}',
           '']
    txt = '\n'.join(out)
    p = os.path.join(HERE, 'controls_v2.txt')
    if '--check' in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt
        print('controls_v2.txt up to date' if ok else 'controls_v2.txt STALE'); sys.exit(0 if ok else 1)
    open(p, 'w').write(txt); print(txt)

if __name__ == '__main__':
    main()
