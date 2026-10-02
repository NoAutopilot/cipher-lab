#!/usr/bin/env python3
"""judge_body.py -- GAPS4 (2 Oct 2026): judge the body L01-L14 as Spanish with its controls side by side (CLAUDE.md rule 3).
Texts: KEY = reading_tokens.tsv's key-regenerated letters for L01-L14 (U codes dropped); GLOSS = passB.tsv's own gloss letters
(the leaf's contemporary period gloss, a known-genuine text from the same leaf -- the ZX-DEC349 calibration witness); SENSE =
body/reading_body.txt's SENSE lines with the bracketed inferred letters included (grade I letters count here).
Controls: 20 letter-shuffled nulls of KEY (same letters, order destroyed) and 20 shuffled-target decodes (group order shuffled
within each line, decoded with key.tsv, U dropped -- the ARM-C1 check: a PASS there voids the judge as a gate for this family at
this N). Corpora: es18 (GAPS5, 2 Oct 2026: era-matched 1690-1725 letters/gazette/diplomatic prose, tools/data/es18), es17c7 (1634-1648 letters) and
the spec default es (es17, 1605-1626 fiction); --corpora picks the set, one body/spec_body_<key>.json per corpus.
Headline rows also run through the CLI (tools/judge_plaintext.py <spec variant> --text ...) and are printed verbatim (rule 7).
Usage: python3 body/judge_body.py [--shuffles 20] [--seed 1] [--corpora es18,es17c7,es]   (writes body/judge_body_results.tsv)
"""
import argparse, csv, os, random, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, os.path.join(ROOT, 'tools')); import judge_plaintext as J
ap = argparse.ArgumentParser(); ap.add_argument('--shuffles', type=int, default=20); ap.add_argument('--seed', type=int, default=1)
ap.add_argument('--corpora', default='es18,es17c7,es', help='LANG_CORPORA keys with a body/spec_body_<key>.json each (GAPS5 added es18, 2 Oct 2026)'); a = ap.parse_args()
BODY = ['L%02d' % i for i in range(1, 15)]
toks = [r for r in csv.DictReader(open(os.path.join(T, 'reading_tokens.tsv'), encoding='utf-8'), delimiter='\t') if r['line'] in BODY]
key_text = ''.join(r['value'] for r in toks if r['value'] not in ('[?]', 'NULL'))  # GAPS8 2 Oct 2026: NULL (the blot) carries no letter
ct = [r for r in csv.DictReader(open(os.path.join(T, 'ciphertext.tsv'), encoding='utf-8'), delimiter='\t') if r['line'] in BODY]
gloss_text = ''.join(r['gloss'] for r in ct)
sense = []
for ln in open(os.path.join(HERE, 'reading_body.txt'), encoding='utf-8'):
    m = re.match(r'(L\d\d) SENSE (.*?)(\s{2,}\(.*)?$', ln.rstrip('\n'))
    if m: sense.append(re.sub(r'\[\?\]|\[ \]', '', m.group(2)))
sense_text = ''.join(sense)
key = {r['code']: r['value'] for r in csv.DictReader(open(os.path.join(T, 'key.tsv'), encoding='utf-8'), delimiter='\t')}
exc = {}
for r in csv.DictReader(open(os.path.join(T, 'exceptions.tsv'), encoding='utf-8'), delimiter='\t'):
    exc[(r.get('line'), r.get('pos'))] = r.get('value')
def decode_shuffled(rng):
    out = []
    for L in BODY:
        gs = [r['group'] for r in ct if r['line'] == L]; rng.shuffle(gs)
        out.extend(key.get(g, '[?]') for g in gs)
    return ''.join(v for v in out if v not in ('[?]', 'NULL'))
print('KEY   N=%d %s' % (len(J.fold(key_text)), key_text)); print('GLOSS N=%d %s' % (len(J.fold(gloss_text)), gloss_text)); print('SENSE N=%d %s' % (len(J.fold(sense_text)), sense_text))
rows = []
for corp in a.corpora.split(','):
    spec_path = os.path.join(HERE, 'spec_body_%s.json' % corp)
    print('\n=== corpus %s (CLI, verbatim) ===' % corp)
    for name, txt in (('KEY', key_text), ('GLOSS', gloss_text), ('SENSE', sense_text)):
        p = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'judge_plaintext.py'), spec_path, '--text', txt], capture_output=True, text=True)
        print('$ judge_plaintext.py body/spec_body_%s.json --text <%s>  (exit %d)' % (corp, name, p.returncode)); print('\n'.join('  ' + l for l in p.stdout.strip().splitlines()))
        lang = [l for l in p.stdout.splitlines() if 'language' in l][0]
        rows.append((corp, name, len(J.fold(txt)), re.search(r'score=(\S+),', lang).group(1), re.search(r'real_p05=(\S+),', lang).group(1), re.search(r'null_p99=(\S+),', lang).group(1), 'PASS' if p.returncode == 0 else 'FAIL'))
    model = J.NgramModel([J.read_corpus(q) for q in J.LANG_CORPORA[corp]])
    N = len(J.fold(key_text)); real, null, cov = model.controls(N, samples=200); null99, real05 = J.pct(null, 0.99), J.pct(real, 0.05)
    rng = random.Random(a.seed); sh = [model.score(''.join(rng.sample(J.fold(key_text), N))) for _ in range(a.shuffles)]
    rng = random.Random(a.seed); st = []
    for _ in range(a.shuffles):
        t = J.fold(decode_shuffled(rng)); st.append(model.score(t))
    for lab, xs in (('shuffled-null (letters of KEY)', sh), ('shuffled-target (group order within line, key.tsv)', st)):
        npass = sum(1 for s in xs if s > null99 and s > real05)
        print('%s: %s n=%d min=%.3f max=%.3f mean=%.3f PASS %d of %d (null_p99=%.3f real_p05=%.3f at N=%d)' % (corp, lab, len(xs), min(xs), max(xs), sum(xs) / len(xs), npass, len(xs), null99, real05, N))
        rows.append((corp, lab, N, '%.3f..%.3f' % (min(xs), max(xs)), '%.3f' % real05, '%.3f' % null99, '%d PASS of %d' % (npass, len(xs))))
with open(os.path.join(HERE, 'judge_body_results.tsv'), 'w', encoding='utf-8') as f:
    f.write('corpus\ttext\tN\tscore\treal_p05\tnull_p99\tverdict\n')
    for r in rows: f.write('\t'.join(str(x) for x in r) + '\n')
print('\nwrote body/judge_body_results.tsv')
