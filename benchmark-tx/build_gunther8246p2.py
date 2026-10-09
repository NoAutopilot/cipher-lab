#!/usr/bin/env python3
"""Build the Gunther van Schwarzburg WVO 8246 MS p.2 item for BENCHMARK-TX.tsv (split=eval; TX-POOL-LEAF, 9 Oct 2026).

Brief .claude/briefs/runs/2026-10-09-account4-tx-pool-leaf.md (TX-RED F21 route a): a second confirm-grade EVAL leaf for LANE
TX-ENGINEER-2's pool, built outside the lane under PREREG-txeng2-0 section 0b (truth only from a period/published key and a
known text, aligned by tools/interlinear_align.py, as build_birago87.py / build_spinelli_confirm.py). The lane pools it under
its own Amendment; this script does not.

Leaf: Willem van Oranje to Gunther XLI van Schwarzburg, [Brussels] 2 May 1561, WVO briefnr 8246 (Staatsarchiv Rudolstadt,
Kanzlei Sondershausen 693), MS p.2: 25 cipher lines, no clear text and no gloss on the page. Image
ciphers/gunther-van-schwarzburg-1561/images/08246_p2.jpg (Huygens WVO PDF, non-Gallica). A German homophonic symbol cipher
in a hand, office, language and key family outside every other BENCHMARK-TX item.

Truth = the sign(s) the printed plaintext forces under the key, per position of the committed transcription
(ciphers/gunther-van-schwarzburg-1561/ciphertext.tsv, G1/F1 single careful reading, 24 Sept 2026; reference sequence = home
advantage on segmentation, as spinelli/no.87):
  - plaintext: Japikse, Correspondentie van Willem den Eerste I (1934) no.316 pp.343-344, spaced type (the edition's marking for
    the Prince's cipher insertions; H. Koot's decipherment, no.236 p.232 n.5), transcribed verbatim in
    benchmark-tx/txpool/gunther8246-p2/japikse_p343-344_spaced.txt AFTER the baseline passZ (7e5fbd474) was committed; a modern
    printed decipherment -> grade C with that note, never H;
  - normalisation for alignment (declared): lower case; umlauts folded (a o u); w -> u (the u/w class is one sign set in this
    cipher: pairs_5109.tsv rows with unit w on 44/48/60); 'König' -> 'q' (code 4000 = König, a word code; no q in the text);
    the editor's '(!)' and supplied '(o)' dropped; punctuation stripped by the aligner;
  - alignment: tools/interlinear_align.py align --code-prefix @ --keep-fs --prior <key C rows + 4000=q>, the WHOLE letter
    (pp.1-3, 953 committed signs) against the whole spaced passage, so p.2 is anchored on both sides;
  - key: ciphers/gunther-van-schwarzburg-1561/key.tsv (79 signs, grade C, rebuilt from sibling WVO 5109 against Japikse no.236
    pp.232-233, Koot's printed decipherment; zero conflicts among C pairs). A plain letter L forces the SET of keyed signs whose
    value is L (homophones), so err_true is value-level, as on no.87 and spinelli.

Status per p.2 position: scored when the aligned chunk is exactly one letter and that letter has keyed signs; excluded
(counted, never scored) when the chunk is empty (excluded:unaligned), longer than one letter (excluded:multi-letter), the
committed sign is outside the key (excluded:off-key: the 5109 key's U signs, BLOT) or the letter has no keyed sign
(excluded:letter-unkeyed). Flag column (set here, before any reader is scored): `align-conflict` where the committed sign is
keyed but its key value differs from the aligned letter (a wrong committed sign, a slip by the encipherer, or an alignment
shift: tx_bench --exclude-flagged drops these). Report as measured AND flagged-excluded, never the second alone.

Alignment control (printed, not a gate): share of keyed committed signs whose key value equals the aligned letter, real text vs
20 letter-shuffled texts (same letters, permuted; seeds 1-20).

    python3 benchmark-tx/build_gunther8246p2.py           # (re)build, print counts + control + sha256
    python3 benchmark-tx/build_gunther8246p2.py --check   # rebuild in memory; exit 1 if the committed truth or sha256 is stale
"""
import csv, hashlib, os, random, re, subprocess, sys, tempfile, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = os.path.join(ROOT, 'ciphers/gunther-van-schwarzburg-1561')
W = os.path.join(ROOT, 'benchmark-tx/txpool/gunther8246-p2')
TRUTH = os.path.join(ROOT, 'benchmark-tx/gunther8246-p2.truth.tsv')
SHA = TRUTH + '.sha256'
ALIGN_OUT = os.path.join(W, 'align_letter.tsv')
TOOL = os.path.join(ROOT, 'tools/interlinear_align.py')
HEADER = ('# Gunther van Schwarzburg WVO 8246 MS p.2 (Willem van Oranje, 2 May 1561), split=eval: Japikse 1934 no.316 printed '
          'decipherment (Koot) under the 5109-rebuilt key (C rows); built by benchmark-tx/build_gunther8246p2.py (TX-POOL-LEAF). '
          'Flag align-conflict = committed sign keyed to another letter.\nline\tpos\tref_sign\ttruth\tplain\tstatus\tflag\n')


def rd(p):
    with open(p, newline='', encoding='utf-8') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def plain_text():
    with open(os.path.join(W, 'japikse_p343-344_spaced.txt'), encoding='utf-8') as f:
        t = ' '.join(l.strip() for l in f if not l.startswith('#'))
    t = t.replace('(!)', '').replace('(o)', '')
    t = re.sub(r'k[öo]nig', 'q', t, flags=re.I)
    t = ''.join(c for c in unicodedata.normalize('NFD', t) if unicodedata.category(c) != 'Mn').lower()
    return t.replace('w', 'u')


def key():
    k = {}
    for r in rd(os.path.join(F, 'key.tsv')):
        if r['grade'] == 'C':
            k[r['sign']] = 'q' if r['value'] == 'König' else r['value'].lower().replace('v', 'u').replace('w', 'u')
    return k


def run_align(ct, text, kv, out, tmp):
    pairs = os.path.join(tmp, 'pairs.tsv')
    prior = os.path.join(tmp, 'prior.tsv')
    with open(pairs, 'w', encoding='utf-8') as f:
        f.write('plain_line\tplain_raw\tcipher_line\tcipher_raw\n8246\t%s\t8246\t%s\n'
                % (text, ' '.join('@' + r['sign'] for r in ct)))
    with open(prior, 'w', encoding='utf-8') as f:
        f.write('code\tmeaning\n' + ''.join('%s\t%s\n' % (s, v) for s, v in kv.items() if len(v) == 1))
    subprocess.run([sys.executable, TOOL, 'align', pairs, out, os.path.join(tmp, 'key_out.tsv'), '--code-prefix', '@',
                    '--keep-fs', '--prior', prior], check=True, capture_output=True)
    al = rd(out)
    assert len(al) == len(ct), (len(al), len(ct))
    return al


def agree_share(ct, al, kv):
    n = k = 0
    for c, a in zip(ct, al):
        if c['sign'] in kv:
            n += 1
            k += (a['plain_chunk'] == kv[c['sign']])
    return k / n


def build(write_align):
    ct = rd(os.path.join(F, 'ciphertext.tsv'))
    kv = key()
    by_val = {}
    for s, v in kv.items():
        by_val.setdefault(v, set()).add(s)
    text = plain_text()
    with tempfile.TemporaryDirectory() as tmp:
        out = ALIGN_OUT if write_align else os.path.join(tmp, 'align.tsv')
        al = run_align(ct, text, kv, out, tmp)
        real = agree_share(ct, al, kv)
        ctrl = []
        letters = [c for c in text if c.isalpha()]
        for seed in range(1, 21):
            rnd = random.Random(seed)
            sh = letters[:]
            rnd.shuffle(sh)
            it = iter(sh)
            stext = ''.join(next(it) if c.isalpha() else c for c in text)
            ctrl.append(agree_share(ct, run_align(ct, stext, kv, os.path.join(tmp, 's.tsv'), tmp), kv))
    rows, counts = [], {}
    for c, a in zip(ct, al):
        if not c['line'].startswith('p2'):
            continue
        line = 'p2_L' + c['line'][3:]
        ch, s = a['plain_chunk'], c['sign']
        flag, truth = '', ''
        if ch == '':
            st = 'excluded:unaligned'
        elif len(ch) > 1:
            st = 'excluded:multi-letter'
        elif s not in kv:
            st = 'excluded:off-key'
        elif ch not in by_val:
            st = 'excluded:letter-unkeyed'
        else:
            st, truth = 'scored', '|'.join(sorted(by_val[ch]))
            if kv[s] != ch:
                flag = 'align-conflict'
        counts[st] = counts.get(st, 0) + 1
        if flag:
            counts['flag:' + flag] = counts.get('flag:' + flag, 0) + 1
        rows.append('%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (line, c['pos'], s, truth, ch, st, flag))
    body = HEADER + ''.join(rows)
    return body, counts, real, ctrl


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
