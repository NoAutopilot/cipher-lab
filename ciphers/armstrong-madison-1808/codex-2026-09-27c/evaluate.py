"""Score retained control solutions by exact decoded piece, without realignment."""
from pathlib import Path
import json
import numpy as np

D = Path(__file__).resolve().parent
ALPHA = 'abcdefghiklmnopqrstuwxyz'
A = len(ALPHA)
lm = np.fromfile(D / 'lm.bin', dtype='float32')

def score(seq, key):
    total = 0.0
    chars = 0
    history = []
    for t in seq:
        if t < 0:
            history = []
            continue
        for ch in key[t]:
            d = ALPHA.index(ch)
            h = history[-3:]
            n = len(h)
            idx = (d if n == 0 else A + h[0]*A+d if n == 1 else
                   A+A*A+(h[0]*A+h[1])*A+d if n == 2 else
                   A+A*A+A*A*A+((h[0]*A+h[1])*A+h[2])*A+d)
            total += float(lm[idx])
            history.append(d)
            chars += 1
    return total, chars

def main():
    results = []
    for c in json.loads((D / 'controls.json').read_text()):
        seed = c['seed']
        seq = list(map(int, (D / f'control{seed}.seq').read_text().split()))
        true_score, true_length = score(seq, c['key'])
        paths = sorted((D / 'results').glob(f'tune{seed}-*.tsv'))
        paths += sorted((D / 'results').glob(f'strong{seed}.tsv'))
        for path in paths:
            raw, key, reading = path.read_text().splitlines()[0].split('\t')
            key = key.split(',')
            got_score, got_length = score(seq, key)
            bonus = float(path.stem.split('-b')[1]) if '-b' in path.stem else 0.0
            assert abs(got_score + bonus*got_length-float(raw)) < 1e-5
            correct = sum(key[t] == c['key'][t] for t in seq if t >= 0)
            row = dict(seed=seed, role=c['role'], file=str(path.relative_to(D)),
                       bonus=bonus, exact_token_pieces=correct, N=c['N'],
                       accuracy=correct/c['N'], predicted_chars=got_length,
                       true_chars=true_length, score=got_score,
                       truth_score=true_score,
                       truth_objective_advantage=true_score+bonus*true_length-float(raw),
                       reading=reading)
            results.append(row)
            print(seed, path.stem, f'{correct}/{c["N"]}', f'{correct/c["N"]:.2%}',
                  'chars', got_length, 'truth advantage', round(row['truth_objective_advantage'], 3))
    (D / 'results.json').write_text(json.dumps(results, indent=2) + '\n')
    target_rows = []
    for name in ['target', 'shuffle0', 'shuffle1', 'shuffle2']:
        path = D/f'results/{name}-strong.tsv'
        if not path.exists():
            continue
        raw, key, reading = path.read_text().splitlines()[0].split('\t')
        key = key.split(',')
        seq = list(map(int, (D/f'{name}.seq').read_text().split()))
        got_score, chars = score(seq, key)
        assert abs(got_score-float(raw)) < 1e-5
        target_rows.append(dict(name=name, log10_score=got_score,
                                decoded_characters=chars, key=key,
                                fragments=reading.strip('|').split('|'),
                                status='unreadable; no accepted mapping'))
    if target_rows:
        (D/'target_results.json').write_text(json.dumps(target_rows, indent=2)+'\n')

if __name__ == '__main__':
    main()
