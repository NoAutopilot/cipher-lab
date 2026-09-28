#!/usr/bin/env python3
"""H4 (28 Sept 2026): is a published clear poem the plaintext (or host text) of any Debosnys cryptogram?

Test statistic S1, for a cipher token sequence c[0..n) aligned at offset o against a plaintext unit sequence u:
    S1 = (number of pairs i<j with c[i]==c[j] and u[o+i]==u[o+j]) / (number of pairs i<j with c[i]==c[j]).
Under any substitution in which one sign always stands for one unit (a MASC or a homophonic cipher, unit = letter,
syllable or word), S1 is 1.0 at the right offset minus transcription noise; under an unrelated text it sits at the
plaintext's own repeat rate. Secondary statistic S2 = the same with the roles swapped (same unit => same sign), which
a MASC satisfies and a homophonic cipher does not. The score reported is the max of S1 over every offset at which the
shorter sequence fits inside the longer (cipher inside poem, and poem inside cipher); the null is the same max over
1000 shuffles of the plaintext unit order, plus a shuffled-line null (poem lines permuted, order within a line kept).
Gate (CAMPAIGN.md H4): a pairing clears when its max S1 is above the 97.5th percentile of BOTH nulls AND its S2 at
the same offset is above the 97.5th percentile of the unit-shuffle null for S2.

Inputs: ciphertext_draft.tsv (160-id, pass A) and ciphertext_draft_base.tsv (base fold), clear_poems.tsv (c3 poem),
optional --extra-text FILE (one line per verse line, e.g. the Anacreon Greek ode once on disk).
Output: h4_result.json and a table on stdout. Seeds fixed (1). CPU only, no claim.
"""
import csv, json, os, re, sys, random, unicodedata, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from count_syllables import vowel_groups
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
def fold(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(ch for ch in s if unicodedata.category(ch) != 'Mn')
    return s.replace('œ', 'oe').replace('æ', 'ae')
def words(line): return [w for w in re.findall(r"[a-z]+", fold(line))]
def letters(line): return list(''.join(words(line)))
def syllables(line):
    out = []
    for w in words(line):
        # crude: split before each vowel group, consonants attach to the following nucleus; trailing consonants to the last
        parts = re.findall(r"[^aeiouy]*[aeiouy]+", w); tail = w[len(''.join(parts)):]
        if not parts: out.append(w); continue
        parts[-1] += tail; out.extend(parts)
    return out
def load_cipher(path):
    seqs = collections.defaultdict(list)
    for r in csv.DictReader(open(os.path.join(root, path)), delimiter='\t'):
        if r['sign'] in ('_', 'MULTI'): continue
        g = r['line'].split('_')[0]; g = {'c2a': 'c2', 'c2b': 'c2', 'c4a': 'c4', 'c4b': 'c4'}.get(g, g)
        seqs[g].append(r['sign']); seqs[g.rstrip('ab') if g in ('c2', 'c4') else g]
    return seqs
def poem_lines():
    return [r['text_as_written'] for r in csv.DictReader(open(os.path.join(root, 'clear_poems.tsv')), delimiter='\t') if r['page'] == 'c3']
import numpy as np
def encode(seq):
    ids = {}; return np.array([ids.setdefault(x, len(ids)) for x in seq], dtype=np.int32)
def pairs_of(c):
    pos = collections.defaultdict(list)
    for i, s in enumerate(c): pos[s].append(i)
    I = []; J = []
    for idx in pos.values():
        for a in range(len(idx)):
            for b in range(a + 1, len(idx)): I.append(idx[a]); J.append(idx[b])
    return np.array(I, dtype=np.int32), np.array(J, dtype=np.int32)
def s1_all(cI, cJ, n_c, U):
    """S1 at every offset; returns array over offsets (cipher-in-poem if n_c <= len(U), else poem-in-cipher)."""
    m = len(U)
    if n_c <= m:
        offs = np.arange(m - n_c + 1); out = np.empty(len(offs))
        if len(cI) == 0: return out * 0, 'cipher-in-poem'
        for k in range(0, len(offs), 64):
            o = offs[k:k + 64][:, None]; out[k:k + 64] = (U[o + cI] == U[o + cJ]).mean(axis=1)
        return out, 'cipher-in-poem'
    offs = np.arange(n_c - m + 1); out = np.zeros(len(offs))
    for o in offs:
        mk = (cI >= o) & (cJ < o + m)
        if mk.any(): out[o] = (U[cI[mk] - o] == U[cJ[mk] - o]).mean()
    return out, 'poem-in-cipher'
def s1(c, u, o):
    """scalar S1 for sequences (lists) at offset o, cipher inside u"""
    I, J = pairs_of(c); U = encode(u)
    return float((U[o + I] == U[o + J]).mean()) if len(I) else 0.0
def best(c, u):
    I, J = pairs_of(c); U = encode(u); arr, nest = s1_all(I, J, len(c), U); o = int(arr.argmax()); return float(arr[o]), o, nest
def best_enc(cI, cJ, n_c, U):
    arr, nest = s1_all(cI, cJ, n_c, U); o = int(arr.argmax()); return float(arr[o]), o, nest
def main():
    extra = None
    if '--extra-text' in sys.argv: extra = [l.rstrip('\n') for l in open(sys.argv[sys.argv.index('--extra-text') + 1], encoding='utf-8') if l.strip()]
    rng = random.Random(1); trials = 1000 if '--quick' not in sys.argv else 100
    texts = {'c3-poem': poem_lines()}
    if extra: texts['extra'] = extra
    results = []
    for level, path in (('id160', 'ciphertext_draft.tsv'), ('base', 'ciphertext_draft_base.tsv')):
        C = load_cipher(path)
        for tname, lines in texts.items():
            for unit, fn in (('letter', letters), ('syllable', syllables), ('word', words)):
                per_line = [fn(l) for l in lines]; U = [x for l in per_line for x in l]
                for g in ('c1', 'c2', 'c3', 'c4'):
                    c = C[g]; cI, cJ = pairs_of(c); Ue = encode(U); obs, off, nest = best_enc(cI, cJ, len(c), Ue)
                    def S2at(Uarr, o, n2):
                        if n2 == 'cipher-in-poem': return s1(list(Uarr[o:o + len(c)]), c, 0)
                        return s1(list(Uarr), c[o:o + len(Uarr)], 0)
                    S2 = S2at(Ue, off, nest)
                    null = []; null2 = []; nullL = []
                    line_enc = []; k0 = 0
                    for l in per_line: line_enc.append(Ue[k0:k0 + len(l)]); k0 += len(l)
                    for t in range(trials):
                        Us = Ue.copy(); rng.shuffle(Us); v, o2, n2 = best_enc(cI, cJ, len(c), Us); null.append(v)
                        null2.append(S2at(Us, o2, n2))
                        pl = line_enc[:]; rng.shuffle(pl); UL = np.concatenate(pl); nullL.append(best_enc(cI, cJ, len(c), UL)[0])
                    null.sort(); null2.sort(); nullL.sort(); q = lambda a: a[int(0.975 * len(a)) - 1]
                    pct = sum(v < obs for v in null) / len(null) * 100
                    row = dict(level=level, text=tname, unit=unit, cryptogram=g, n_cipher=len(c), n_units=len(U), S1=round(obs, 4), offset=off, nesting=nest,
                               null_p975=round(q(null), 4), null_max=round(null[-1], 4), percentile=round(pct, 1), lineshuffle_p975=round(q(nullL), 4),
                               S2=round(S2, 4), S2_null_p975=round(q(null2), 4), trials=trials,
                               clears=bool(obs > q(null) and obs > q(nullL) and S2 > q(null2)))
                    results.append(row)
                    print('\t'.join(str(row[k]) for k in ('level', 'text', 'unit', 'cryptogram', 'n_cipher', 'n_units', 'S1', 'offset', 'nesting', 'null_p975', 'lineshuffle_p975', 'percentile', 'S2', 'S2_null_p975', 'clears')), flush=True)
    json.dump(results, open(os.path.join(root, 'h4_result.json'), 'w'), indent=1)
    print('cleared:', sum(r['clears'] for r in results), 'of', len(results))
def planted(trials=300):
    """Positive control (rule 3): the poem's own units enciphered with a synthetic homophonic key at each cryptogram's
    N-fitting length and K (K homophones spread over the units by frequency, profile like the target's: one dominant
    sign), then type noise p redrawn per token; does max S1 clear the shuffle null? Reports per unit type, K and noise."""
    rng = random.Random(2); lines = poem_lines(); out = []
    C = load_cipher('ciphertext_draft.tsv')
    for unit, fn in (('letter', letters), ('syllable', syllables), ('word', words)):
        per_line = [fn(l) for l in lines]; U = [x for l in per_line for x in l]
        for g in ('c1', 'c3', 'c4'):
            K = len(set(C[g])); n = min(len(C[g]), len(U))
            # homophone allotment: each distinct unit gets at least one sign; the rest go to the most frequent units
            cnt = collections.Counter(U); units = [u for u, _ in cnt.most_common()]
            if K < len(units): K_eff = len(units)
            else: K_eff = K
            alloc = {u: 1 for u in units}; extra = K_eff - len(units)
            for i in range(extra): alloc[units[i % max(1, len(units) // 3)]] += 1
            sign_of = {}; sid = 0
            for u in units: sign_of[u] = list(range(sid, sid + alloc[u])); sid += alloc[u]
            for noise in (0.0, 0.05, 0.15):
                plain = U[:n]; c = [rng.choice(sign_of[u]) for u in plain]
                c = [rng.randrange(sid) if rng.random() < noise else s for s in c]
                cI, cJ = pairs_of(c); Ue = encode(U); obs, off, nest = best_enc(cI, cJ, len(c), Ue)
                null = []
                for t_ in range(trials):
                    Us = Ue.copy(); rng.shuffle(Us); null.append(best_enc(cI, cJ, len(c), Us)[0])
                null.sort(); q = null[int(0.975 * len(null)) - 1]
                row = dict(unit=unit, like=g, n=n, K=sid, noise=noise, S1=round(obs, 4), offset=off, null_p975=round(q, 4), clears=bool(obs > q))
                out.append(row); print('PLANTED\t' + '\t'.join(f'{k}={v}' for k, v in row.items()), flush=True)
    json.dump(out, open(os.path.join(root, 'h4_planted.json'), 'w'), indent=1)
if __name__ == '__main__':
    if '--planted' in sys.argv: planted()
    else: main()
