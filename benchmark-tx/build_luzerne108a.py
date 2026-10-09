#!/usr/bin/env python3
"""Build the Huntington mssDE 108(A) p.1 item for BENCHMARK-TX.tsv (split=eval; TX-POOL-LEAF-2, 9 Oct 2026).

Brief .claude/briefs/runs/2026-10-09-account4-tx-pool-leaf-2.md (Amendment 1 of the TX-POOL-LEAF brief: the other solvers'
solved items as EVAL-POOL candidates), built outside LANE TX-ENGINEER-2 under PREREG-txeng2-0 section 0b (truth only from a
period/published key and a known text, aligned by tools/interlinear_align.py). The lane pools it under its own Amendment;
this script does not. Credit: S. Tomokiyo (Cryptiana blog, 23 Sept 2021, "Decoded but not Identified Code of Luzerne": the
Jan 1781 La Luzerne code and its Beinecke decode) and D. Bourdeau (dbourdeau/cyphersolver destaing/NOTES.md l.13, the same
1199-figure code); the key and the 108(B) transcription are this repository's (ciphers/huntington-luzerne-destouches-1781).

Leaf: La Luzerne to Destouches, Philadelphia 16 Jan 1781, Huntington Library mssDE 108(A) p.1, 11 lines of a numerical code
(figures 4-1199, dot-separated), image ciphers/huntington-luzerne-destouches-1781/images/mssDE108A_p1.jpg (Huntington
CONTENTdm IIIF, non-Gallica). A few interlinear words (de, ri, e) are written under some groups on the leaf.

Truth = the code(s) the period decipherment forces under the key, per position of the committed transcription
(ciphers/huntington-luzerne-destouches-1781/ciphertext.tsv, H-graded reference; home advantage on segmentation, as no.87):
  - known text: mssDE 108(B), the "Duplicata" of the same letter, deciphered in ink under every group by Destouches (Huntington
    catalogue; AUDIT.md N0). Its gloss is transcribed in pairs_108B.tsv (R19, 24 Sept 2026). ONLY PAGE 1 is used: R19 read p.1
    carefully at native resolution (it contradicts the key at 436 nous/vous and 1188 prets/mr), but read pp.2-6 "cross-checked
    line by line against key.tsv's existing values" (NOTES.md R19), so pp.2-6 are not independent of the key and are not used;
  - gloss -> plain line (declared): 108(B)'s leading 835 'cher' dropped (108(A) has no group there; AUDIT.md, R1); a gloss
    that is '?', '_' (struck), '.' (punctuation code) or carries a '?' becomes the wildcard '#' (a sign there, unread: never
    scored, never evidence); every other gloss lower case, accents folded, letters only;
  - key: ciphers/huntington-luzerne-destouches-1781/key.tsv rows of grade C whose source is the contemporary interlinear
    decipherments of the siblings mssDE 68/37/55 (period, Destouches's office). The 31 rows key.tsv took from 108(B) itself,
    the R16 context fills and the pencil rows are NOT used (independence). '|' alternatives each count;
  - alignment: tools/interlinear_align.py align --floor 1 --digits 4 --prior <key> --word-prior --keep-fs --wildcard '#'
    (one pair: 108(A) p.1's 115 committed groups against the p.1 gloss line).

Status per position: scored when the aligned chunk is one whole gloss word that the key carries (truth = every keyed code
with that value); excluded (counted, never scored) when the chunk is empty (excluded:unaligned), the wildcard
(excluded:gloss-unread), or a word the key lacks (excluded:value-unkeyed). Flag column, set here before any reader is scored:
`align-conflict` where the committed group is keyed but to another value (a copying variant between 108(A) and 108(B), a
wrong committed group, or a shift). Report as measured AND flagged-excluded, never the second alone.

Alignment control (printed, not a gate): share of keyed committed groups whose key value equals the aligned chunk, real gloss
vs 20 word-shuffled glosses (seeds 1-20).

    python3 benchmark-tx/build_luzerne108a.py           # (re)build, print counts + control + sha256
    python3 benchmark-tx/build_luzerne108a.py --check   # rebuild in memory; exit 1 if the committed truth or sha256 is stale
"""
import csv, hashlib, os, random, re, subprocess, sys, tempfile, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = os.path.join(ROOT, 'ciphers/huntington-luzerne-destouches-1781')
W = os.path.join(ROOT, 'benchmark-tx/txpool/luzerne108a')
TRUTH = os.path.join(ROOT, 'benchmark-tx/luzerne108a-p1.truth.tsv')
SHA = TRUTH + '.sha256'
ALIGN_OUT = os.path.join(W, 'align_p1.tsv')
TOOL = os.path.join(ROOT, 'tools/interlinear_align.py')
KEY_SRC = 'contemporary interlinear decipherment (mssDE 68/37/55)'
HEADER = ('# Huntington mssDE 108(A) p.1 (La Luzerne to Destouches, 16 Jan 1781), split=eval: mssDE 108(B) p.1 period '
          'decipherment (Destouches) under the 68/37/55 key (C rows); built by benchmark-tx/build_luzerne108a.py '
          '(TX-POOL-LEAF-2). Flag align-conflict = committed group keyed to another value.\n'
          'line\tpos\tref_sign\ttruth\tplain\tstatus\tflag\n')


def rd(p):
    with open(p, newline='', encoding='utf-8') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def norm(s):
    s = ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn').lower()
    return re.sub(r'[^a-z]', '', s)


def gloss_tokens():
    out = []
    for r in rd(os.path.join(F, 'pairs_108B.tsv')):
        if r['page'] != 'p1' or (r['line'] == 'L01' and r['idx'] == '1'):
            continue
        g = r['gloss'].strip()
        out.append('#' if (g in ('?', '_', '.', '') or '?' in g or not norm(g)) else norm(g))
    return out


def key():
    k = {}
    for r in rd(os.path.join(F, 'key.tsv')):
        if r['grade'] == 'C' and r['source'] == KEY_SRC:
            vals = [norm(v) for v in r['value'].split('|') if norm(v)]
            if vals:
                k[r['code']] = vals
    return k


def run_align(ct, toks, kv, out, tmp):
    pairs, prior = os.path.join(tmp, 'pairs.tsv'), os.path.join(tmp, 'prior.tsv')
    with open(pairs, 'w', encoding='utf-8') as f:
        f.write('plain_line\tplain_raw\tcipher_line\tcipher_raw\n108Bp1\t%s\t108Ap1\t%s\n'
                % (' '.join(toks), ' '.join(c['group'] for c in ct)))
    with open(prior, 'w', encoding='utf-8') as f:
        f.write('code\tmeaning\n' + ''.join('%s\t%s\n' % (c, v[0]) for c, v in sorted(kv.items())))
    subprocess.run([sys.executable, TOOL, 'align', pairs, out, os.path.join(tmp, 'key_out.tsv'), '--floor', '1',
                    '--digits', '4', '--prior', prior, '--word-prior', '--keep-fs', '--wildcard', '#'],
                   check=True, capture_output=True)
    al = rd(out)
    assert len(al) == len(ct), (len(al), len(ct))
    return al


def agree_share(ct, al, kv):
    n = k = 0
    for c, a in zip(ct, al):
        if c['group'] in kv:
            n += 1
            k += (a['plain_chunk'] in kv[c['group']])
    return k / n


def build(write_align):
    ct = [r for r in rd(os.path.join(F, 'ciphertext.tsv')) if r['line'].startswith('mssDE108A_p1_')]
    kv = key()
    by_val = {}
    for c, vs in kv.items():
        for v in vs:
            by_val.setdefault(v, set()).add(c)
    toks = gloss_tokens()
    words = set(toks)
    with tempfile.TemporaryDirectory() as tmp:
        al = run_align(ct, toks, kv, ALIGN_OUT if write_align else os.path.join(tmp, 'align.tsv'), tmp)
        real = agree_share(ct, al, kv)
        ctrl = []
        for seed in range(1, 21):
            sh = toks[:]
            random.Random(seed).shuffle(sh)
            ctrl.append(agree_share(ct, run_align(ct, sh, kv, os.path.join(tmp, 's.tsv'), tmp), kv))
    rows, counts = [], {}
    for c, a in zip(ct, al):
        line = c['line'].replace('mssDE108A_', '')
        ch, s = a['plain_chunk'], c['group']
        flag, truth = '', ''
        if ch == '':
            st = 'excluded:unaligned'
        elif '#' in ch:
            st = 'excluded:gloss-unread'
        elif ch not in words:
            st = 'excluded:multi-word'
        elif ch not in by_val:
            st = 'excluded:value-unkeyed'
        else:
            st, truth = 'scored', '|'.join(sorted(by_val[ch], key=int))
            if s in kv and ch not in kv[s]:
                flag = 'align-conflict'
            elif s not in kv:
                flag = 'off-key-ref'
        counts[st] = counts.get(st, 0) + 1
        if flag:
            counts['flag:' + flag] = counts.get('flag:' + flag, 0) + 1
        rows.append('%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (line, c['pos'], s, truth, ch, st, flag))
    return HEADER + ''.join(rows), counts, real, ctrl


def main():
    check = '--check' in sys.argv
    body, counts, real, ctrl = build(write_align=not check)
    sha = hashlib.sha256(body.encode('utf-8')).hexdigest()
    if check:
        ok = os.path.exists(TRUTH) and open(TRUTH, encoding='utf-8').read() == body and \
            os.path.exists(SHA) and open(SHA).read().split()[0] == sha
        print('check', 'OK' if ok else 'STALE', sha)
        sys.exit(0 if ok else 1)
    with open(TRUTH, 'w', encoding='utf-8') as f:
        f.write(body)
    with open(SHA, 'w') as f:
        f.write('%s  %s\n' % (sha, os.path.basename(TRUTH)))
    print('positions', sum(v for k, v in counts.items() if not k.startswith('flag:')), counts)
    print('control: real agree %.3f vs shuffled mean %.3f max %.3f (20 seeds)' % (real, sum(ctrl) / len(ctrl), max(ctrl)))
    print('sha256', sha)


if __name__ == '__main__':
    main()
