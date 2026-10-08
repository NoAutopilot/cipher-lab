#!/usr/bin/env python3
"""f.13 (BnF italien 1584, Pusterla, Guastalla 21 Jan 1447): three-pass vote + key-constrained lattice decode with a
shuffled-key control -- SFZ-P2, 7 Oct 2026 (.claude/briefs/runs/2026-10-07-acct2-st-rebuild-workers.md, Wave 3).

Inputs: ciphertext_f13_passA.tsv (SFZ-P, Opus), ciphertext_f13_passB.tsv (Sonnet, two-line crops), ciphertext_f13_passC.tsv
(SFZ-P2's blind Sonnet pass on level single-line crops); key ../sforza-italien1584-1447/pusterla/key.tsv.

Pre-registered before any decode was run (SFZ-P2, 22:5x UTC 7 Oct 2026), not tuned on f.13:
  * normalisation: in every pass the token pair `g ÷` is the one sign `g÷` (the rule decode.py already applies to pass A);
  * alignment and weights are tools/reconcile_passes.py's own (star alignment on pass A, Needleman-Wunsch; lattice mass
    per column = its --keep-alts rule: reader weight H 1.0 / M 0.6 (a `?`-flagged sign), an alternative 0.3 x weight);
  * skeleton = the --vote rule: a column enters the lattice only when more passes have a sign there than a gap
    (the same rule that emits a vote.tsv row); the vote's top-1 is the plurality sign, ties to the earliest pass;
  * decode = tools/key_decode_lattice.py viterbi with its defaults: lam 1.0, beam 64, unk_cost default, corpus it16dip
    (16th-c. Italian diplomatic letters; a 1447 letter: era mismatch, no 15th-c. Italian corpus on disk);
  * control = the same lattice decode under 200 value-shuffled keys (key_decode_lattice.shuffled, seed 13); statistic =
    it16dip mean log10 4-gram per letter of the decoded text; PASS needs real > shuffle p95, AND the judge
    (tools/judge_plaintext.py, inline spec {"judge": {"corpora": it16dip}}) PASS against real_p05. Both, or FAIL.
The shuffle loop can change the statistic: a shuffled key changes every decoded letter and the path the lattice picks.

    python3 ciphers/sforza-pusterla-1447-f13/lattice_decode.py [--check] [--corpus=it15]
Writes lattice/{vote.tsv,lattice.tsv,decode.tsv,plain.txt,stats.json}; --check exits 1 if those on disk are stale.
"""
import collections, json, os, random, statistics, sys, types
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..', '..')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import reconcile_passes as rp  # noqa: E402
import key_decode_lattice as kdl  # noqa: E402
import judge_plaintext as jp  # noqa: E402
POOL = os.path.join(ROOT, 'ciphers', 'sforza-italien1584-1447', 'pusterla')
OUT = os.path.join(HERE, 'lattice')
PASSES = ['ciphertext_f13_passA.tsv', 'ciphertext_f13_passB.tsv', 'ciphertext_f13_passC.tsv']
LAM, BEAM, NSHUF, SEED = 1.0, 64, 200, 13
# --corpus it15 (SFZ-NEXT, 8 Oct 2026): the same pipeline with the era-nearer tools/data/it15 model for both the decode LM
# and the judge, written to lattice_it15/; the default it16dip run and its lattice/ outputs are unchanged.
CORPUS = next((a.split('=', 1)[1] for a in sys.argv if a.startswith('--corpus=')), 'it16dip')
if CORPUS != 'it16dip':
    OUT = os.path.join(HERE, f'lattice_{CORPUS}')


def merge_che(seq):
    out, i = [], 0
    while i < len(seq):
        if i + 1 < len(seq) and seq[i][0] == 'g' and seq[i + 1][0] == '÷':
            out.append(('g÷',) + seq[i][1:]); i += 2
        else:
            out.append(seq[i]); i += 1
    return out


def build():
    a = types.SimpleNamespace(keep_plain=False, keep_dots=False, sign_map=None, split_chars=False, keep_alts=True,
                              line_sub=None, halves=False)
    P = [rp.load_pass(os.path.join(HERE, f), a)[0] for f in PASSES]
    lines = list(dict.fromkeys(list(P[0]) + [l for p in P[1:] for l in p]))
    vote, lat, gapmaj = [], [], 0
    for ln in lines:
        if ln == 'f13_SIG':
            continue  # the signature is checked separately (decode.py); the body is the test
        cols = rp.columns([merge_che(p.get(ln, [])) for p in P], 'nw')
        pos = 0
        for c in cols:
            signs = [x[0] if x else '-' for x in c]
            pres = [s for s in signs if s != '-']
            if len(pres) <= len(signs) - len(pres):
                gapmaj += 1
                continue
            cnt = collections.Counter(pres); top = max(cnt.values())
            vs = next(s for s in signs if s != '-' and cnt[s] == top)
            pos += 1
            vote.append((ln, pos, vs, top, len(signs)))
            mass = collections.defaultdict(float)
            for x in c:
                if x is None:
                    continue
                w = rp.LAT_CONF_W[x[1]]; mass[x[0]] += w
                for alt in (x[3] if len(x) > 3 else ()):
                    mass[alt] += rp.LAT_ALT_F * w
            tot = sum(mass.values())
            lat.append(((ln, pos), {k: v / tot for k, v in mass.items()}))
    return vote, lat, gapmaj


def run():
    vote, lat, gapmaj = build()
    key = kdl.read_key(os.path.join(POOL, 'key.tsv'))
    model = jp.NgramModel([jp.read_corpus(p) for p in jp.LANG_CORPORA[CORPUS]])
    lm = kdl.LM(model, None)
    seq, _ = kdl.viterbi(lat, key, lm, LAM, BEAM)
    t1 = [v[2] for v in vote]
    real = model.score(kdl.text_of(seq, key)); real_t1 = model.score(kdl.text_of(t1, key))
    rnd = random.Random(SEED); sh, sh_t1 = [], []
    for _ in range(NSHUF):
        k2 = kdl.shuffled(key, rnd)
        sh.append(model.score(kdl.text_of(kdl.viterbi(lat, k2, lm, LAM, BEAM)[0], k2)))
        sh_t1.append(model.score(kdl.text_of(t1, k2)))
    plain = kdl.text_of(seq, key)
    spec = {'judge': {'corpora': [os.path.relpath(p, ROOT) for p in jp.LANG_CORPORA[CORPUS]]}}
    stats = {
        'passes': PASSES, 'positions': len(lat), 'gap_majority_columns_dropped': gapmaj,
        'vote_share_hist': dict(collections.Counter(f'{v[3]}/{v[4]}' for v in vote)),
        'positions_with_alternatives': sum(1 for _, c in lat if len(c) > 1),
        'lam': LAM, 'beam': BEAM, 'n_shuffles': NSHUF, 'seed': SEED,
        'moved_off_vote_top1': sum(1 for a_, b_ in zip(t1, seq) if a_ != b_),
        'unk_positions_chosen': sum(1 for s in seq if s not in key),
        'lattice': {'real': round(real, 4), 'shuf_mean': round(statistics.mean(sh), 4),
                    'shuf_p95': round(float(np.quantile(sh, .95)), 4), 'shuf_max': round(max(sh), 4),
                    'rank': 1 + sum(1 for o in sh if o >= real)},
        'vote_top1': {'real': round(real_t1, 4), 'shuf_mean': round(statistics.mean(sh_t1), 4),
                      'shuf_p95': round(float(np.quantile(sh_t1, .95)), 4),
                      'rank': 1 + sum(1 for o in sh_t1 if o >= real_t1)},
        'letters': len(plain),
        'letter_distribution': dict(collections.Counter(plain).most_common()),
    }
    stats['shuffle_gate'] = 'PASS' if real > stats['lattice']['shuf_p95'] else 'FAIL'
    files = {
        'vote.tsv': 'line\tpos\tsign\tvotes\tn_passes\n' + ''.join(f'{a}\t{b}\t{c}\t{d}\t{e}\n' for a, b, c, d, e in vote),
        'lattice.tsv': 'line\tpos\tcand\tscore\n' + ''.join(f'{k[0]}\t{k[1]}\t{c}\t{s:.4f}\n' for k, cs in lat
                                                            for c, s in sorted(cs.items(), key=lambda kv: -kv[1])),
        'decode.tsv': 'line\tpos\tvote_top1\tchosen\tvalue\tprior\tmoved\n' + ''.join(
            f'{k[0]}\t{k[1]}\t{a_}\t{b_}\t{key.get(b_, "_")}\t{c.get(b_, 0):.3f}\t{int(a_ != b_)}\n'
            for (k, c), a_, b_ in zip(lat, t1, seq)),
        'plain.txt': plain + '\n',
    }
    return stats, files, spec


def main(check=False):
    stats, files, spec = run()
    files['stats.json'] = json.dumps(stats, indent=1, ensure_ascii=False) + '\n'
    files['spec.json'] = json.dumps(spec, indent=1) + '\n'
    if check:
        stale = [n for n, t in files.items()
                 if not os.path.exists(os.path.join(OUT, n)) or open(os.path.join(OUT, n), encoding='utf-8').read() != t]
        print('stale: ' + ', '.join(stale) if stale else f'{os.path.basename(OUT)}/ up to date')
        return 1 if stale else 0
    os.makedirs(OUT, exist_ok=True)
    for n, t in files.items():
        open(os.path.join(OUT, n), 'w', encoding='utf-8').write(t)
    print(json.dumps(stats, indent=1, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main('--check' in sys.argv))
