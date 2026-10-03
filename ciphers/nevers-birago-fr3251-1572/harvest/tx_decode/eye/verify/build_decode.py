#!/usr/bin/env python3
"""A1-BIR-VERIFY step (c): turn vscore.json's kept S candidates into decode_key.py inputs. Run from this folder.
f.144r: the committed job's ciphertext (../../../ciphertext_f144r.tsv; same 90 positions as the lattice) + an exceptions
file. f.117r / f.168 have no decode job: the skeleton is the lam-4 lattice's two-reader top-1 sign per position, conf H where
the top-1 prior >= 0.85 and M below (an approximation of pass agreement, stated in NOTES). Every kept candidate becomes an
exceptions row: value = the printed 1572 key's value for the key-implied sign, grade S, reason 'A1-BIR-VERIFY kept'."""
import csv, json
key = {r['sign']: r['value'] for r in csv.DictReader(open('../../../key_1572_sheet.tsv'), delimiter='\t')}
vs = json.load(open('vscore.json')); jobs = []
for L in ['f117', 'f168', 'f144r']:
    dec = list(csv.DictReader(open(f'../../{L}_lam4.decode.tsv'), delimiter='\t'))
    if L == 'f144r':
        ct = 'harvest/ciphertext_f144r.tsv'; pref = 'f144r_'
    else:
        ct = f'harvest/tx_decode/eye/verify/ciphertext_{L}_top1.tsv'; pref = f'{L}_'
        with open(f'ciphertext_{L}_top1.tsv', 'w') as f:
            f.write('line\tpos\tsign\tconf\n')
            for r in dec:
                f.write(f"{pref}{r['line']}\t{r['pos']}\t{r['top1']}\t{'H' if float(r['prior']) >= 0.85 else 'M'}\n")
    kept = vs.get(L, {}).get('kept', [])
    with open(f'exceptions_{L}.tsv', 'w') as f:
        f.write('folio\tline\tpos\tvalue\tgrade\treason\n')
        for k in kept:
            lp, sw = k.split(' '); line, pos = lp.split(':'); new = sw.split('->')[1]
            f.write(f"{pref[:-1]}\t{line}\t{pos}\t{key.get(new, '?')}\tS\tA1-BIR-VERIFY kept: image read {sw} (blind, G1+G2 PASS)\n")
    jobs.append(dict(ciphertext=ct, key=['harvest/key_1572_sheet.tsv'], format='tsv', split_line='_', style='concat',
                     exceptions=f'harvest/tx_decode/eye/verify/exceptions_{L}.tsv',
                     reading=f'harvest/tx_decode/eye/verify/reading_{L}_verify.txt',
                     tokens=f'harvest/tx_decode/eye/verify/reading_{L}_verify_tokens.tsv',
                     null_values=['NULL'], unknown_values=['', '?'], uncertain_conf=['M', 'L']))
    print(L, 'kept', len(kept))
json.dump(dict(jobs=jobs), open('decode_verify.json', 'w'), indent=1)
