"""AX-4612: recovery of a real-letter positive control decode (families/ file copied to ax4612/realctl_<nr>_decode.txt)
against key.tsv's letter per numeral (ax4612/realctl_<nr>.tsv truth column; u/v and i/j folded as the solver folds)."""
import sys, csv
D = 'ciphers/lodewijk-van-nassau-1573-74/ax4612/'
for nr in sys.argv[1:]:
    truth = ''.join(r['truth'] for r in csv.DictReader(open(D + f'realctl_{nr}.tsv'), delimiter='\t'))
    truth = truth.replace('v', 'u').replace('j', 'i')
    dec = ''.join(l.strip() for l in open(D + f'realctl_{nr}_decode.txt') if not l.startswith('#'))
    ok = sum(a == b for a, b in zip(dec, truth))
    print(f'{nr}: recovery vs key.tsv {ok}/{len(truth)} = {ok/len(truth):.3f}; truth under key.tsv: {truth[:90]}')
    print(f'{" "*len(nr)}  blind decode:                         {dec[:90]}')
