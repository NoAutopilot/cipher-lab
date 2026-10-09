#!/usr/bin/env python3
"""MONLUC-KEY test 2 (7 Oct 2026): Tomokiyo's Monluc Cipher 1 table (key.tsv, unchanged) on the first 5 cipher lines of
c268 (f.138), an unglossed page.

  python3 score_c268.py [--draws 200] [--seed 1] [--check]

Transcription: two blind Sonnet passes (passes/c268_passA.tsv, c268_passB.tsv) on images/c268cipher_L0*_s*.jpg; pass A is
the base (more complete: pass B's L03 stops at 18 signs), positions where an alignment of B to A disagrees get conf M
(written to ciphertext_c268.tsv). W:word tokens (clear-looking words inside the cipher; Tomokiyo: nulls that look like
words) are dropped as nulls. Statistics, each with its matched control on the same tokens shuffled (rule 3):
 (1) judge: tools/judge_plaintext.py on the spec (fr16 corpus) for the decode and for --draws shuffled-token decodes
     (the shuffled-decode control the brief names); the shuffled decodes must FAIL for a PASS to mean anything;
 (2) if c270 clear text (c270_text.txt) is present: score_c172.py's alignment of decode vs that text, target vs shuffle.
Writes reading_c268.txt and results_c268.json; --check exits 1 when stale (rule 7).

Relabel (MONLUC-RELABEL, 9 Oct 2026): the 10 C-curl 'Z' tokens that pass A filed K63/K19 are written K38 (table t), a
transcription correction backed by the MONLUC-BLIND blind sort (blind_k07_sort.tsv group B = pre-registered form A, which
also holds the token both passes call K38, L01:9) and its decode_key.py --try K69=t accept (+49.7 bits; crossword_log.tsv).
The pass-A label is kept in column pass_a; relabelled tokens get conf M (relabel = 'blind-sort'). key.tsv is unchanged.
"""
import argparse, difflib, json, random, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from score_c172 import norm, load_key, align  # noqa: E402
ROOT = HERE.parents[1]
SPEC = ROOT / 'specs' / 'fr4735-monluc-lansac-poland-1573.json'


def read_pass(p):
    out = {}
    for ln in (HERE / 'passes' / p).read_text().splitlines():
        if '\t' in ln:
            lab, r = ln.split('\t', 1)
            out[lab] = r.split()
    return out


def judge(text):
    r = subprocess.run([sys.executable, str(ROOT / 'tools' / 'judge_plaintext.py'), str(SPEC), '--text', text, '--json'],
                       capture_output=True, text=True)
    j = json.loads(r.stdout)
    return j


RELABEL = {('L01', 32): ('K19', 'K38'), ('L02', 16): ('K63', 'K38'), ('L02', 18): ('K63', 'K38'),
           ('L03', 10): ('K63', 'K38'), ('L04', 14): ('K63', 'K38'), ('L04', 20): ('K63', 'K38'),
           ('L04', 24): ('K63', 'K38'), ('L04', 36): ('K63', 'K38'), ('L05', 8): ('K63', 'K38'),
           ('L05', 13): ('K63', 'K38')}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--draws', type=int, default=100)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    key = load_key()
    A, B = read_pass('c268_passA.tsv'), read_pass('c268_passB.tsv')
    rows, toks, lines, agree = [], [], [], 0
    for lab in sorted(A):
        ta, tb = A[lab], B.get(lab, [])
        conf = ['M'] * len(ta)
        for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ta, tb, autojunk=False).get_opcodes():
            if tag == 'equal':
                for i in range(i1, i2):
                    conf[i] = 'H'
        agree += conf.count('H')  # pass A/B agreement, counted before the relabel sets its tokens to M
        pa = ta[:]
        ta = ta[:]
        for (rl, rp), (old, new) in RELABEL.items():
            if rl == lab:
                assert pa[rp - 1] == old, (lab, rp, pa[rp - 1])
                ta[rp - 1] = new
                conf[rp - 1] = 'M'
        for i, t in enumerate(ta, 1):
            rel = 'blind-sort' if (lab, i) in RELABEL else ''
            rows.append(f"{lab}\t{i}\t{t}\t{conf[i-1]}\t{pa[i-1]}\t{rel}\n")
        kt = [t for t in ta if not t.startswith('W:')]
        toks += kt
        lines.append(f"{lab}\t{''.join(key.get(t, '_') for t in ta if not t.startswith('W:'))}")
    dec = norm(''.join(key.get(t, '') for t in toks))
    j = judge(dec)
    rng = random.Random(a.seed)
    sh_pass, sh_scores = 0, []
    for _ in range(a.draws):
        t = toks[:]
        rng.shuffle(t)
        js = judge(norm(''.join(key.get(x, '') for x in t)))
        sh_pass += js.get('verdict') == 'PASS'
        sh_scores.append(js.get('checks', {}).get('language', {}).get('score'))
    res = dict(relabelled=len(RELABEL), tokens=len(toks), signs_pass_a=len(rows), pass_agree_h=agree, decoded_letters=len(dec), decoded=dec,
               judge=j, shuffle_draws=a.draws, shuffle_judge_pass=sh_pass,
               shuffle_language_scores_max=max(s for s in sh_scores if s is not None) if any(sh_scores) else None)
    ct = HERE / 'c270_text.txt'
    if ct.exists():
        g = norm(ct.read_text().split('\n#', 1)[0])
        tgt = align(dec, g)
        ctl = []
        for _ in range(200):
            t = toks[:]
            rng.shuffle(t)
            ctl.append(align(norm(''.join(key.get(x, '') for x in t)), g))
        ctl.sort()
        res.update(c270_letters=len(g), c270_matched=tgt, c270_rate=round(tgt / len(dec), 4),
                   c270_shuffle_mean=round(sum(ctl) / len(ctl) / len(dec), 4), c270_shuffle_p95=round(ctl[189] / len(dec), 4),
                   c270_shuffle_max=round(ctl[-1] / len(dec), 4))
    outs = {HERE / 'ciphertext_c268.tsv': 'line\tpos\tsign\tconf\tpass_a\trelabel\n' + ''.join(rows),
            HERE / 'reading_c268.txt': '# c268 (f.138) first 5 cipher lines, Tomokiyo Monluc Cipher 1 table, pass A base, 10 C-curl tokens relabelled K38 (MONLUC-RELABEL); _ = unkeyed sign;'
                                       ' W: words dropped. Not graded: see NOTES.md.\n' + '\n'.join(lines) + '\n',
            HERE / 'results_c268.json': json.dumps(res, indent=1, default=str) + '\n'}
    if a.check:
        bad = [p.name for p, t in outs.items() if not p.exists() or p.read_text() != t]
        print('STALE ' + ' '.join(bad) if bad else 'OK c268 outputs current')
        sys.exit(1 if bad else 0)
    for p, t in outs.items():
        p.write_text(t)
    print(outs[HERE / 'results_c268.json'])


if __name__ == '__main__':
    main()
