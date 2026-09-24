#!/usr/bin/env python3
"""Align the folio 67 cipher (ciphertext_f67.tsv) to its clear text on folio 68r (dechiffre_f68.txt), grade every group
against key_1659, and write the extended key (24 Sept 2026, LANE G2 worker R).

f.68r is the same letter in clear, from "voudrez bien que je vous die" to "de s'y appliquer" (worker P; AUDIT.md V5b).
The cipher is cut at the clear French f.67 carries ("parceque Sil pouvoit estre", "Desja ie vous ay mandé ce qui s'est
presupposé"); the f.68r text is cut at the same words.  Same hard-EM / Viterbi aligner as align_f86.py, with two changes:
a group may carry up to MAXLEN letters (proper names are coded whole), and key_1659's own f.86/f.88 counts stay in the
model at every iteration as fixed pseudo-counts, so f.67 can confirm or contradict them but a single f.67 occurrence
cannot silently override twenty f.86/f.88 ones.  "Madame" is the symbol '#', as "M.e" in align_f86.norm.

Grades per cipher group (rule 4):
  C  the aligned clear text equals key_1659's value for the code (known plaintext agrees with the key), or equals one of
     the alternate values key_1659 itself attests for the code from f.86/f.88 (its other_values column: the table is
     syllabic, so 7 is ou/u, 15 oi/i, 18 n/on ... on f.86/f.88 too), or the code is absent from key_1659 and every f.67 occurrence aligns to the same non-empty value;
  M  the aligned text is neither key_1659's value nor an attested alternate (a conflict, listed in align_f67_conflicts.tsv), or a code absent
     from key_1659 aligns to different values at different occurrences, or the group aligns to nothing (a null)
     other than an attested one; and every group read at conf M in ciphertext_f67.tsv (the transcription is uncertain),
     even where f.68r agrees, as tools/decode_key.py does.
  (clear French and punctuation are not graded here; decode_key.py passes them through.)

  python3 align_f67.py            write align_f67.tsv, align_f67_conflicts.tsv, key_1659_ext.tsv, exceptions_f67_C.tsv
  python3 align_f67.py --check    exit 1 if any committed output differs from what this script writes
"""
import csv, io, math, os, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
import align_f86 as A

A.MAXLEN = 8
LENPRIOR = {0: math.log(0.05), 1: math.log(0.45), 2: math.log(0.33), 3: math.log(0.12), 4: math.log(0.03),
            5: math.log(0.006), 6: math.log(0.004), 7: math.log(0.003), 8: math.log(0.002)}
PRIOR_W = 1.0          # weight of one f.86/f.88 attestation relative to one f.67 occurrence
# Start values only (first iteration), as align_f86.SEEDS: worker M's context proposals (read_f67.PROPOSE) and the two
# code-words the first unseeded run split across neighbours (154 quelque, _70 avec, 79 du + 80 duc).  Every value is re-estimated.
SEEDS = {'154': 'quelque', '_70': 'avec', '79': 'du', '80': 'duc', '43': 'fo', '72': 'ni', '67': 'mi', '32': 'ci', '68': 'mo', '63': 'lo'}


def norm(s):
    s = s.replace('Madame', 'M.e')
    return A.norm(s)


def f68_text():
    """Clear text of f.68r with struck words dropped and interlined words kept, as one string."""
    out = []
    for line in open('dechiffre_f68.txt', encoding='utf-8'):
        if line.startswith('#'):
            continue
        import re
        line = re.sub(r'\[del: [^\]]*\]', ' ', line)
        line = re.sub(r'\[ins: ([^\]]*)\]', r' \1 ', line)
        line = line.replace('[?]', '')
        out.append(line.strip())
    return ' '.join(out)


def segments():
    rows = list(csv.DictReader(open('ciphertext_f67.tsv', encoding='utf-8'), delimiter='\t'))
    segs, cur = [], []
    for r in rows:
        g = r['group']
        if g.startswith('[PLAIN'):
            if cur:
                segs.append(cur); cur = []
            continue
        if g in A_NONSIGN:
            continue
        cur.append((r['line'], int(r['pos']), g))
    segs.append(cur)
    assert len(segs) == 3, len(segs)
    text = f68_text()
    i1 = text.index('parceque sil pouvoit estre')
    i2 = text.index('que ce qui se dit')
    t1 = text[:i1]
    t2 = text[i1 + len('parceque sil pouvoit estre'):i2]
    t3 = text[i2:text.index('Cest ce que vous')]
    return [('F1', segs[0], norm(t1)), ('F2', segs[1], norm(t2)), ('F3', segs[2], norm(t3))]


A_NONSIGN = {',', ';', '.', ':', '—', 'X'}


def load_key():
    key, prior = {}, defaultdict(Counter)
    rows = list(csv.DictReader(open('key_1659.tsv', encoding='utf-8'), delimiter='\t'))
    for r in rows:
        v = '#' if r['value'] == 'M.' else ('' if r['value'] == '0' else r['value'])
        alts = {('' if kv.rsplit(':', 1)[0] == '0' else kv.rsplit(':', 1)[0]) for kv in filter(None, r['other_values'].split(','))}
        key[r['code']] = (v, r, alts)
        prior[r['code']][v] += int(r['evidence']) * PRIOR_W
        for kv in filter(None, r['other_values'].split(',')):
            k, n = kv.rsplit(':', 1)
            prior[r['code']]['' if k == '0' else k] += int(n) * PRIOR_W
    return key, prior, rows


def make_score(counts, tot, alpha=0.05):
    def score(g, chunk):
        L = len(chunk)
        c = counts[g][chunk]
        return math.log((c + alpha * math.exp(LENPRIOR[L]) / 30) / (tot[g] + alpha)) + LENPRIOR[L]
    return score


def em(segs, prior, iters=40):
    counts, tot = defaultdict(Counter), Counter()
    for g, c in prior.items():
        counts[g].update(c); tot[g] += sum(c.values())
    for g, v in SEEDS.items():
        counts[g][v] += 2; tot[g] += 2
    res = None
    for it in range(iters):
        score = make_score(counts, tot)
        newc, newt, res = defaultdict(Counter), Counter(), []
        for g, c in prior.items():
            newc[g].update(c); newt[g] += sum(c.values())
        for name, toks, text in segs:
            al, s = A.viterbi([t[2] for t in toks], text, score)
            res.append((name, toks, al))
            for t, a in zip(toks, al):
                newc[t[2]][a] += 1; newt[t[2]] += 1
        if newc == counts:
            break
        counts, tot = newc, newt
    return res


def build():
    confs = {(r['line'], int(r['pos'])): r['conf'] for r in csv.DictReader(open('ciphertext_f67.tsv', encoding='utf-8'), delimiter='\t')}
    key, prior, keyrows = load_key()
    segs = segments()
    res = em(segs, prior)
    occ = defaultdict(Counter)
    for name, toks, al in res:
        for t, a in zip(toks, al):
            occ[t[2]][a] += 1
    out_align, conflicts, exc = [], [], []
    counts = Counter()
    for name, toks, al in res:
        for (line, pos, g), a in zip(toks, al):
            folio, ln = line.split('_', 1)
            if g in key:
                kv = key[g][0]
                if a == kv:
                    grade, why = 'C', 'f.68r agrees with key_1659'
                elif a in key[g][2]:
                    grade, why = 'C', f'f.68r "{a or "0"}" = alternate key_1659 attests (modal "{kv or "0"}")'
                else:
                    grade, why = 'M', f'f.68r has "{a or "0"}", key_1659 "{kv or "0"}"'
                    conflicts.append((line, pos, g, kv or '0', a or '0', name))
            else:
                if a and len(occ[g]) == 1:
                    grade, why = 'C', f'code not in key_1659; f.68r gives "{a}" at all {occ[g][a]} occurrences'
                else:
                    grade, why = 'M', f'code not in key_1659; f.68r gives {dict(occ[g])}'
            if grade == 'C' and confs[(line, pos)] != 'H':
                grade, why = 'M', 'conf M group; ' + why
            val = {'#': 'M.'}.get(a, a) or '0'
            counts[grade] += 1
            out_align.append((name, line, pos, g, val, key.get(g, ('-',))[0] or '0', grade))
            exc.append((folio, ln, pos, val, grade, why))
    # extended key: key_1659 rows unchanged, then codes f.67/f.68r adds (not in key_1659, one consistent value)
    ext = [list(r.values()) + ['', ''] for r in keyrows]
    header = list(keyrows[0].keys()) + ['ev_f67', 'f67_evidence']
    for r, row in zip(keyrows, ext):
        c = occ.get(r['code'])
        if c:
            kv = key[r['code']][0]
            row[-2] = f'{c[kv]}/{sum(c.values())}'
            other = {('M.' if k == '#' else (k or '0')): n for k, n in c.items() if k != kv}
            row[-1] = 'f.68r agrees' if not other else f'f.68r other: {other}'
    added = []
    for g in sorted(occ, key=lambda g: (int(g.lstrip('_')) if g.lstrip('_').isdigit() else 999, g)):
        if g in key:
            continue
        c = occ[g]
        v, n = c.most_common(1)[0]
        tot = sum(c.values())
        cons = len(c) == 1 and v
        where = ' '.join(f'{t[0]}/{t[1]}' for s in res for t, a in zip(s[1], s[2]) if t[2] == g)
        note = 'single attestation' if tot == 1 else ('' if cons else 'conflict')
        ext.append([g, ('M.' if v == '#' else v) or '0', 'C' if cons else 'M', str(n), str(tot),
                    ','.join(f'{k or "0"}:{m}' for k, m in c.most_common()[1:]), note, '0/0', '0/0',
                    f'{n}/{tot}', f'added from f.67/f.68r alignment at {where}'])
        added.append((g, v, n, tot))
    return res, out_align, conflicts, exc, header, ext, counts, added


def tsv(header, rows):
    b = io.StringIO()
    b.write('\t'.join(header) + '\n')
    for r in rows:
        b.write('\t'.join(str(x) for x in r) + '\n')
    return b.getvalue()


def main():
    res, out_align, conflicts, exc, header, ext, counts, added = build()
    files = {
        'align_f67.tsv': tsv(['seg', 'line', 'pos', 'group', 'plain_f68', 'key_1659', 'grade'], out_align),
        'align_f67_conflicts.tsv': tsv(['line', 'pos', 'group', 'key_1659', 'f68r', 'seg'], conflicts),
        'key_1659_ext.tsv': tsv(header, ext),
        'exceptions_f67_C.tsv': tsv(['folio', 'line', 'pos', 'value', 'grade', 'reason'], exc),
    }
    if '--check' in sys.argv:
        bad = [f for f, s in files.items() if not os.path.exists(f) or open(f, encoding='utf-8').read() != s]
        print('stale:' if bad else 'ok', ' '.join(bad))
        sys.exit(1 if bad else 0)
    for f, s in files.items():
        open(f, 'w', encoding='utf-8').write(s)
    for name, toks, al in res:
        print(name, len(toks), 'groups:', ' '.join(f'{t[2]}={a or "0"}' for t, a in zip(toks, al)))
    print('grades', dict(counts), 'conflicts', len(conflicts), 'codes added', len(added))
    for a in added:
        print('added', a)


if __name__ == '__main__':
    main()
