#!/usr/bin/env python3
"""Build the Birago 1572 f.152r (no.77) known-answer item for BENCHMARK-TX.tsv (TXP-152, LANE TX-ENGINEER-2, 9 Oct 2026).

Recipe copied from benchmark-tx/build_birago87.py. Truth = the sign(s) the decipherment slip pasted on f.151v forces under the
key, per position of the committed reference sequence harvest/f152r/passC.tsv (97 signs). The slip is a LATER hand than the
letter (NEVBIR-152): grade C with that note, as a modern reading, never H.

Alignment: tools/interlinear_align.py align, NEVBIR-87ALIGN's options (--floor 5000 --digits 4 --keep-fs --word-prior, seed =
harvest/align87/prior.tsv, the printed table with T42 = g) plus --wildcard '.' so each of the slip's dots (a sign its decipherer
left unread) stays an explicit unread position. Cipher codes as harvest/align87/build_pairs.py: letter signs Tnn -> nn, the 8
word signs -> 6000+nn, every off-sheet tile its own code 1000+k. Plain side: slip_for_align.tsv L01-L04 (the struck S1x is not
used) joined into one span (the slip's line breaks are not the letter's), j -> i, apostrophes dropped.
Control (GAPS4, harvest/align_sheet.py's statistic): share of decoded letters in difflib matching blocks >= 3 against the folded
slip, real key vs 200 value-shuffled keys (seed 1); printed and written to the truth header.

Key used for "forces": harvest/key_1572_sheet.tsv with the clerk C rows exactly as build_birago87.py: T42 = m; T95 {s, l};
T52 {i, o}; X_CE = s. A plain letter forces the SET of its homophones, so err_true is value-level.

Flag column: verifier verdicts in benchmark-tx/birago1572-f152r.flags.tsv (TXV-152; FLAG/CORRECT/KEEP as build_birago87.py)
override, at their positions, the automatic 'align-conflict' on a scored position whose slip letter disagrees with the committed sign's majority chunk in
this span (interlinear_align status conflict); tx_bench --exclude-flagged reports the figure without them beside the measured one.
Excluded (counted, never scored): slip dot (wildcard) and null/unaligned; multi-letter chunk that is not a word sign's own
value; align status doubtful/repaired/single-segment (align-uncertain); committed sign off-sheet (X_*, ?) except X_CE; T88.

Also writes normalised outputs (line, pos, sign) to benchmark-tx/outputs/birago1572-f152r/: passA, passB (TXP-152 blind Opus
passes), passZ_pipeline (TXP-152 reconcile + Sonnet adjudication), committed (= passC, the reference sequence; home advantage).
  python3 benchmark-tx/build_birago152.py [--check]
--check: rebuild in a temp dir and exit 1 if the committed truth or outputs differ.
"""
import csv, difflib, hashlib, os, random, re, shutil, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = os.path.join(ROOT, 'ciphers/nevers-birago-fr3251-1572/harvest')
F = os.path.join(H, 'f152r')
TX = os.path.join(ROOT, 'benchmark-tx/txeng2/f152r')
ITEM = 'birago1572-f152r'
WORD = {"T11", "T15", "T26", "T29", "T46", "T78", "T84", "T89"}
OPT = ['--floor', '5000', '--digits', '4', '--keep-fs', '--word-prior', '--wildcard', '.']


def rd(p):
    with open(p, newline='') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def fold(s):
    s = s.lower().replace('v', 'u').replace('j', 'i').replace('&', 'et')
    return re.sub(r'[^a-z]', '', s)


def matched(dec, clear):
    sm = difflib.SequenceMatcher(None, dec, clear, autojunk=False)
    return sum(b.size for b in sm.get_matching_blocks() if b.size >= 3) / max(1, len(dec))


def build(out_root):
    key = {r['sign']: r['value'] for r in rd(os.path.join(H, 'key_1572_sheet.tsv'))}
    key['T42'] = 'm'
    vals = {s: {v} for s, v in key.items()}
    vals['T95'] = {'s', 'l'}
    vals['T52'] = {'i', 'o'}
    vals['X_CE'] = {'s'}
    by_val = {}
    for s, vs in vals.items():
        for v in vs:
            by_val.setdefault(v, set()).add(s)

    committed = [('f152r_' + r['passage'], int(r['pos']), r['sign_id'].strip()) for r in rd(os.path.join(F, 'passC.tsv'))]
    assert len(committed) == 97, len(committed)
    slip = ' '.join(r['text'] for r in rd(os.path.join(F, 'slip_for_align.tsv')) if r['line'] in ('L01', 'L02', 'L03', 'L04'))
    slip = slip.replace("'", '').replace('j', 'i')
    toks, k = [], 0
    for _, _, s in committed:
        if s in WORD:
            toks.append(str(6000 + int(s[1:])))
        elif re.fullmatch(r'T\d+', s):
            toks.append(str(int(s[1:])))
        else:
            k += 1
            toks.append(str(1000 + k))
    tmp = tempfile.mkdtemp()
    pairs = os.path.join(tmp, 'pairs.tsv')
    with open(pairs, 'w') as f:
        f.write('plain_line\tplain_raw\tcipher_line\tcipher_raw\nslip\t%s\tf152r\t%s\n' % (slip, ' '.join(toks)))
    al, kk = os.path.join(tmp, 'align.tsv'), os.path.join(tmp, 'key.tsv')
    subprocess.run([sys.executable, os.path.join(ROOT, 'tools/interlinear_align.py'), 'align', pairs, al, kk,
                    '--prior', os.path.join(H, 'align87/prior.tsv')] + OPT, check=True, capture_output=True)
    align = rd(al)
    shutil.rmtree(tmp)
    assert len(align) == len(committed), (len(align), len(committed))
    agrees = sum(1 for a in align if a['status'] == 'agrees')

    # control: GAPS4 statistic (align_sheet.py), decode of the committed sequence vs the folded slip
    clear = fold(slip.replace('.', ''))
    m = {s: v for s, v in key.items()}
    seq = [s for _, _, s in committed]

    def dec(mp):
        return fold(''.join(mp.get(s, '') for s in seq if mp.get(s) not in (None, 'null')))
    real = matched(dec(m), clear)
    ids = list(m)
    vv = [m[i] for i in ids]
    rng = random.Random(1)
    sh = []
    for _ in range(200):
        rng.shuffle(vv)
        sh.append(matched(dec(dict(zip(ids, vv))), clear))
    rank = 1 + sum(1 for x in sh if x >= real)
    ctrl = ('align agrees %d/%d = %.3f; GAPS4 control: real key matched %.3f vs 200 value-shuffled keys mean %.3f max %.3f, '
            'rank %d of 201' % (agrees, len(align), agrees / len(align), real, sum(sh) / len(sh), max(sh), rank))

    # TXV-152 (9 Oct 2026): verifier verdicts per position, as build_birago87.py; FLAG -> flag column, CORRECT -> truth changed
    flags = {}
    fp = os.path.join(ROOT, 'benchmark-tx', ITEM + '.flags.tsv')
    if os.path.exists(fp):
        for r in rd(fp):
            flags[(r['line'], int(r['pos']))] = r
    rows, nsc, nex = [], 0, {}
    for (line, pos, sign), a in zip(committed, align):
        chunk = a['plain_chunk'].strip()
        st, truth = 'scored', ''
        if '.' in chunk:
            st = 'excluded:slip-dot'
        elif not chunk or a['status'].startswith('null'):
            st = 'excluded:unaligned'
        elif a['status'] in ('doubtful', 'repaired', 'single-segment'):
            st = 'excluded:align-uncertain'
        elif sign == 'T88':
            st = 'excluded:key-split-T88'
        elif sign not in vals:
            st = 'excluded:off-sheet'
        elif len(chunk) == 1:
            truth = '|'.join(sorted(by_val.get(chunk, set())))
            if not truth:
                st = 'excluded:no-key-sign-for-' + chunk
        else:
            ws = sorted(s for s, v in key.items() if v == chunk)
            if ws:
                truth = '|'.join(ws)
            else:
                st = 'excluded:multi-letter-chunk'
        if st == 'scored':
            nsc += 1
        else:
            nex[st] = nex.get(st, 0) + 1
        flag = 'align-conflict' if st == 'scored' and a['status'].startswith('conflict') else ''
        fr = flags.get((line, pos))
        if fr and st == 'scored':
            if fr['verdict'] == 'CORRECT':
                if fr['correct_plain']:
                    chunk = fr['correct_plain']
                ts = set(by_val.get(chunk, set())) | set(filter(None, fr['add_signs'].split('|')))
                truth = '|'.join(sorted(ts))
                flag = 'corrected:' + fr['class']
            elif fr['verdict'] == 'FLAG':
                flag = fr['class']
            elif fr['verdict'] == 'KEEP':
                flag = ''
        rows.append((line, pos, sign, truth, chunk, st, flag, a['status']))
    os.makedirs(os.path.join(out_root, 'benchmark-tx'), exist_ok=True)
    tp = os.path.join(out_root, 'benchmark-tx', ITEM + '.truth.tsv')
    with open(tp, 'w') as f:
        f.write('# Birago 1572 f.152r (no.77, BnF fr.3251) known answer: decipherment slip pasted on f.151v (later hand, grade C) '
                'aligned to harvest/f152r/passC.tsv under the printed 1572 key + clerk C rows; built by '
                'benchmark-tx/build_birago152.py; flag column: align-conflict, overridden by birago1572-f152r.flags.tsv (TXV-152)\n# %s\nline\tpos\tref_sign\ttruth\tplain\tstatus\tflag\talign_status\n' % ctrl)
        for r in rows:
            f.write('\t'.join(map(str, r)) + '\n')
    with open(tp + '.sha256', 'w') as f:
        f.write(hashlib.sha256(open(tp, 'rb').read()).hexdigest() + '  ' + ITEM + '.truth.tsv\n')

    od = os.path.join(out_root, 'benchmark-tx/outputs', ITEM)
    os.makedirs(od, exist_ok=True)

    def norm(path, name):
        out = []
        for r in rd(path):
            ln = r.get('line') or 'f152r_' + r['passage']
            out.append((ln, r['pos'], (r.get('sign') or r.get('sign_id')).strip()))
        with open(os.path.join(od, name + '.tsv'), 'w') as f:
            f.write('line\tpos\tsign\n')
            for o in out:
                f.write('\t'.join(o) + '\n')
    norm(os.path.join(TX, 'passA.tsv'), 'passA')
    norm(os.path.join(TX, 'passB.tsv'), 'passB')
    norm(os.path.join(TX, 'passZ_pipeline.tsv'), 'passZ_pipeline')
    norm(os.path.join(F, 'passC.tsv'), 'committed')
    return '%s: %d positions, %d scored, excluded %s; %s' % (ITEM, len(rows), nsc, nex, ctrl)


def main():
    if '--check' in sys.argv:
        tmp = tempfile.mkdtemp()
        build(tmp)
        bad = []
        for rel in ['benchmark-tx/%s.truth.tsv' % ITEM, 'benchmark-tx/%s.truth.tsv.sha256' % ITEM] + \
                ['benchmark-tx/outputs/%s/%s.tsv' % (ITEM, n) for n in ('passA', 'passB', 'passZ_pipeline', 'committed')]:
            a, b = os.path.join(ROOT, rel), os.path.join(tmp, rel)
            if not os.path.exists(a) or open(a, 'rb').read() != open(b, 'rb').read():
                bad.append(rel)
        shutil.rmtree(tmp)
        print('stale: ' + ', '.join(bad) if bad else 'up to date')
        sys.exit(1 if bad else 0)
    print(build(ROOT))


if __name__ == '__main__':
    main()
