#!/usr/bin/env python3
"""controls_sup.py -- rule-3 controls for the f.66 v2 draft (SUP-NEVREVOL, 20 Oct 2026; PREREG-SUP-NEVREVOL.md).

Statistic S: mean log10 4-gram per letter (tools/judge_plaintext.py fr model), first value of an a|b entry, the
decoded signs in page order -- the same statistic as ciphers/fr3986-nevers-revol-1593/controls_v2.py.
Key: tools/keys/key60.tsv merged with ../fr3986-nevers-revol-1593/key_atlas_extra.tsv through decode_key's loader.

  --positive   positive control (run first): fr16 corpus passages of N=188 letters enciphered into key no.60
               single-letter homophones, fr16 corpus split 80/20 (model / passages, held out); sign errors injected at 0/20/40/60% (wrong sign drawn from the key's
               sign list), 10 seeds each; real-key S ranked against 200 value-shuffled keys. -> controls_pos.txt
  (default)    target: ciphertext_v2.tsv; real S vs 200 value-shuffled keys (rank, z), vs 100 shuffled-target
               orders (p95), fr16 judge on the real decode. -> controls_sup.txt
  --diag       diagnostic (not a gate, never scored on the target): the same positive control at 0/20/40% with a
               length-class shuffle (values permuted only among signs whose value has the same length) and the
               100-order shuffled-sign null. -> controls_diag.txt
  --mixed      positive control for PREREG-NEVREVOL-2 (NEVREVOL-PREREG, 3 Nov 2026): held-out passages enciphered with
               letter, syllable and word signs at the 24 Sept draft's class shares (63.6/33.9/2.5%), N=188 signs,
               0/10/20% injected error, 10 seeds; gate per passage = rank <= 10/201 vs 200 length-class value
               shuffles AND vs 200 shuffled-order nulls; PASS iff >= 8/10 at 0% and >= 6/10 at 10%. -> controls_mixed.txt
  --check      exit 1 if the committed output differs. Deterministic.
"""
import collections, json, os, random, statistics, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import decode_key as dk
import judge_plaintext as jp

KEYS = ['../../tools/keys/key60.tsv', '../fr3986-nevers-revol-1593/key_atlas_extra.tsv']
SPEC = {'language': 'fr', 'min_word_cover': 0.5, 'control_samples': 200}

def val(key, s):
    return key[s]['value'].split('|')[0] if s in key else ''

def decode(key, signs):
    return ' '.join(val(key, s) for s in signs)

def shuffled_keys(key, n=200):
    codes = sorted(key); vals = [key[c]['value'] for c in codes]
    for seed in range(1, n + 1):
        v = vals[:]; random.Random(seed).shuffle(v)
        yield {c: {'value': x} for c, x in zip(codes, v)}

def rank_vs_shuffled(model, key, signs):
    real = model.score(decode(key, signs))
    sh = [model.score(decode(k2, signs)) for k2 in shuffled_keys(key)]
    rank = 1 + sum(1 for x in sh if x >= real)
    mu, sd = statistics.mean(sh), statistics.pstdev(sh)
    return real, rank, mu, sd, max(sh)

def positive(key, model, corpus_text):
    letters = [c for c in jp.fold(corpus_text) if c.isalpha()]
    by_letter = {}
    for s, r in key.items():
        v = r['value']
        if len(v) == 1 and v.isalpha():
            by_letter.setdefault(v, []).append(s)
    signs_all = sorted(key)
    N = 188
    out = [f'positive control: N={N} letters per passage, fr corpus, key no.60 single-letter homophones '
           f'({sum(len(x) for x in by_letter.values())} signs for {len(by_letter)} letters), 200 value-shuffled keys']
    for err in (0.0, 0.2, 0.4, 0.6):
        ranks = []
        for seed in range(1, 11):
            rng = random.Random(1000 + seed)
            start = rng.randrange(0, len(letters) - 5 * N)
            plain = [c for c in letters[start:start + 3 * N] if c in by_letter][:N]
            signs = [rng.choice(by_letter[c]) for c in plain]
            signs = [rng.choice(signs_all) if rng.random() < err else s for s in signs]
            real, rank, mu, sd, mx = rank_vs_shuffled(model, key, signs)
            ranks.append(rank)
        ok = sum(1 for r in ranks if r <= 10)
        out.append(f'error {int(err*100)}%: ranks {" ".join(map(str, ranks))}; rank<=10/201 in {ok}/10 '
                   f'-> {"PASS" if ok >= 8 else "FAIL"}')
    return out

def lenclass_keys(key, n=200):
    codes = sorted(key); groups = {}
    for c in codes:
        groups.setdefault(len(key[c]['value'].split('|')[0]), []).append(c)
    for seed in range(1, n + 1):
        rng = random.Random(seed); k2 = {}
        for L in sorted(groups):
            cs = groups[L]; v = [key[c]['value'] for c in cs]; rng.shuffle(v)
            k2.update({c: {'value': x} for c, x in zip(cs, v)})
        yield k2

def diag(key, model, corpus_text):
    letters = [c for c in jp.fold(corpus_text) if c.isalpha()]
    by_letter = {}
    for s, r in key.items():
        v = r['value']
        if len(v) == 1 and v.isalpha():
            by_letter.setdefault(v, []).append(s)
    signs_all = sorted(key); N = 188
    out = [f'diagnostic: N={N}, held-out passages, length-class shuffled keys (200) and shuffled-sign orders (100)']
    for err in (0.0, 0.2, 0.4):
        ranks = []; above = 0
        for seed in range(1, 11):
            rng = random.Random(1000 + seed)
            start = rng.randrange(0, len(letters) - 5 * N)
            plain = [c for c in letters[start:start + 3 * N] if c in by_letter][:N]
            signs = [rng.choice(by_letter[c]) for c in plain]
            signs = [rng.choice(signs_all) if rng.random() < err else s for s in signs]
            real = model.score(decode(key, signs))
            sh = [model.score(decode(k2, signs)) for k2 in lenclass_keys(key)]
            ranks.append(1 + sum(1 for x in sh if x >= real))
            ts = []
            for s2 in range(1, 101):
                x = signs[:]; random.Random(s2).shuffle(x); ts.append(model.score(decode(key, x)))
            above += real > jp.pct(ts, 95)
        out.append(f'error {int(err*100)}%: length-class ranks {" ".join(map(str, ranks))}; rank<=10/201 in '
                   f'{sum(1 for r in ranks if r <= 10)}/10; real > shuffled-order p95 in {above}/10')
    return out

def mixed_encipher(key, words, rng, p_word, p_syl, N):
    by = {}
    for s, r in key.items():
        v = jp.fold(r['value'].split('|')[0])
        if v: by.setdefault(v, []).append(s)
    signs, cls = [], []
    for w in words:
        if len(signs) >= N: break
        if len(w) >= 4 and w in by and rng.random() < p_word:
            signs.append(rng.choice(by[w])); cls.append('word'); continue
        i = 0
        while i < len(w):
            done = False
            for L in (3, 2):
                ch = w[i:i + L]
                if len(ch) == L and ch in by and rng.random() < p_syl:
                    signs.append(rng.choice(by[ch])); cls.append('syl'); i += L; done = True; break
            if not done:
                if w[i] in by:
                    signs.append(rng.choice(by[w[i]])); cls.append('letter')
                i += 1
    return signs[:N], cls[:N]

def mixed(key, model, corpus_text, p_word=1.0, p_syl=0.83):
    words = [w for w in (jp.fold(x) for x in corpus_text.split()) if w]
    signs_all = sorted(key); N = 188
    out = [f'mixed positive control (PREREG-NEVREVOL-2): N={N} signs per passage, held-out fr16 passages, letter+syllable+word '
           f'signs (p_word {p_word}, p_syl {p_syl}; target shares 63.6/33.9/2.5), nulls: 200 length-class value shuffles, '
           f'200 shuffled orders; passage passes iff rank <= 10/201 against both']
    verdicts = {}
    for err in (0.0, 0.1, 0.2, 0.3, 0.4, 0.5):
        ra, rb, ok = [], [], 0; shares = collections.Counter()
        for seed in range(1, 11):
            rng = random.Random(1000 + seed)
            start = rng.randrange(0, len(words) - 400)
            signs, cls = mixed_encipher(key, words[start:start + 400], rng, p_word, p_syl, N)
            shares.update(cls)
            signs = [rng.choice(signs_all) if rng.random() < err else s for s in signs]
            real = model.score(decode(key, signs))
            sa = [model.score(decode(k2, signs)) for k2 in lenclass_keys(key)]
            sb = []
            for s2 in range(1, 201):
                x = signs[:]; random.Random(s2).shuffle(x); sb.append(model.score(decode(key, x)))
            a = 1 + sum(1 for x in sa if x >= real); b = 1 + sum(1 for x in sb if x >= real)
            ra.append(a); rb.append(b); ok += (a <= 10 and b <= 10)
        tot = sum(shares.values())
        need = 8 if err == 0 else 6 if err == 0.1 else None
        verdicts[err] = ok >= need if need else None
        sh = ' '.join(f'{k} {100*shares[k]/tot:.1f}%' for k in ('letter', 'syl', 'word'))
        out.append(f'error {int(err*100)}%: shares {sh}; length-class ranks {" ".join(map(str, ra))}; '
                   f'shuffled-order ranks {" ".join(map(str, rb))}; both <= 10/201 in {ok}/10'
                   + (f' (need {need}) -> {"PASS" if verdicts[err] else "FAIL"}' if need else ' (reported, not gated)'))
    out.append(f'control gate (>= 8/10 at 0% AND >= 6/10 at 10%): {"PASS -- passes may run" if verdicts[0.0] and verdicts[0.1] else "FAIL -- control below gate, passes not run"}')
    return out

def target(key, model):
    rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(HERE, 'ciphertext_v2.tsv'))
            if l.strip() and not l.startswith('#')][1:]
    signs = [r[2] for r in rows]
    real, rank, mu, sd, mx = rank_vs_shuffled(model, key, signs)
    real_txt = decode(key, signs)
    ts = []
    for seed in range(1, 101):
        s2 = signs[:]; random.Random(seed).shuffle(s2)
        ts.append(model.score(decode(key, s2)))
    p95 = jp.pct(ts, 95)
    jr = jp.judge(SPEC, real_txt)
    unk = sorted({s for s in signs if s not in key})
    beats = rank <= 10 and real > p95
    return [f'signs {len(signs)}; unkeyed tags {len(unk)}: {" ".join(unk)}',
            f'decoded letters {len(jp.fold(real_txt))}',
            f'real S {real:.4f}',
            f'value-shuffled keys (200): mean {mu:.4f} sd {sd:.4f} max {mx:.4f}; real rank {rank}/201; z {(real-mu)/sd if sd else 0:.2f}',
            f'shuffled-target orders (100): median {statistics.median(ts):.4f} p95 {p95:.4f} max {max(ts):.4f}',
            f'judge on real decode: {"PASS" if jr["pass"] else "FAIL"} {json.dumps(jr["checks"], sort_keys=True)}',
            f'gate (rank <= 10/201 AND real > shuffled-target p95): {"BEATS CONTROL" if beats else "DOES NOT BEAT CONTROL"}']

def main():
    key = dk.load_keys(HERE, KEYS)
    corp = jp.LANG_CORPORA[SPEC['language']]
    texts = [jp.read_corpus(p) for p in corp]
    model = jp.NgramModel(texts)
    if '--positive' in sys.argv:
        # held out: the model is trained on the first 80% of the corpus, passages come from the last 20%
        cut = int(len(texts[0]) * 0.8)
        lines, name = positive(key, jp.NgramModel([texts[0][:cut]]), texts[0][cut:]), 'controls_pos.txt'
    elif '--mixed' in sys.argv:
        cut = int(len(texts[0]) * 0.8)
        lines, name = mixed(key, jp.NgramModel([texts[0][:cut]]), texts[0][cut:]), 'controls_mixed.txt'
    elif '--diag' in sys.argv:
        cut = int(len(texts[0]) * 0.8)
        lines, name = diag(key, jp.NgramModel([texts[0][:cut]]), texts[0][cut:]), 'controls_diag.txt'
    else:
        lines, name = target(key, model), 'controls_sup.txt'
    txt = '\n'.join(lines) + '\n'
    p = os.path.join(HERE, name)
    if '--check' in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt
        print(f'{name} up to date' if ok else f'{name} STALE'); sys.exit(0 if ok else 1)
    open(p, 'w').write(txt); print(txt, end='')

if __name__ == '__main__':
    main()
