"""Compute recovery, source hashes, and the limited Pinckney direct-key check."""
from pathlib import Path
import collections
import csv
import hashlib
import json

D = Path(__file__).resolve().parent
R = D.parents[2]
controls = {f"control{x['seed']}": x for x in json.loads((D / 'glyph_controls.json').read_text())}
results = []
for file in sorted([*D.glob('*_result.tsv'), *D.glob('*_strong.tsv')]):
    name = file.stem.removesuffix('_result').removesuffix('_strong')
    score, key, reading = file.read_text().splitlines()[0].split('\t')
    out = {'file': file.name, 'score': float(score), 'symbols': len(key),
           'decoded_letters': len(reading.replace('|', '')),
           'restarts': 1000 if file.stem.endswith('_strong') else 150,
           'iterations': 60000 if file.stem.endswith('_strong') else 30000}
    if name in controls:
        plain = controls[name]['plain']
        decoded = reading.replace('|', '')
        assert len(plain) == len(decoded)
        out['correct_tokens'] = sum(a == b for a, b in zip(plain, decoded))
        out['token_accuracy'] = out['correct_tokens'] / len(plain)
    results.append(out)

rows = list(csv.DictReader((D / 'glyphs.tsv').open(), delimiter='\t'))
freq = collections.Counter(s for row in rows for s in row['symbols'].split() if s != '|')
data = {'status': 'UNSOLVED', 'transcription_confidence': 'M_provisional',
        'passages': len(rows), 'fragments': sum(1 + row['symbols'].count('|') for row in rows),
        'N': sum(freq.values()), 'K': len(freq), 'symbol_counts': dict(sorted(freq.items())),
        'runs': results}
(D / 'results.json').write_text(json.dumps(data, indent=2) + '\n')

target = D.parent / 'codex-2026-09-27/ciphertext_editorial_clean.txt'
tokens = [int(t) for line in target.read_text().splitlines() if not line.startswith('#')
          for t in line.split() if t.isdigit()]
pinckney = {1651: 'the', 133: 'of', 1343: 'and', 244: 'to', 1578: 'that', 69: 'in'}
anchors = {'source': 'https://github.com/dbourdeau/cyphersolver/blob/main/targets/erving1807/NOTES.md',
           'source_blob_sha': '0e5d7d0c7b54207e3d8d5085e26a078840d78481',
           'scope': 'six published anchor mappings only; not a reconstructed full Pinckney codebook',
           'target_N': len(tokens),
           'anchors': [{'code': c, 'word': w, 'target_occurrences': tokens.count(c)}
                       for c, w in pinckney.items()]}
(D / 'pinckney_anchors.json').write_text(json.dumps(anchors, indent=2) + '\n')

inputs = [D / 'glyphs.tsv', D / 'glyphs.txt', target, R / 'tools/subst_hillclimb.py',
          *sorted((D.parent / 'images').glob('M34-014-003[0-3].jpg')),
          *sorted((R / 'tools/data/en18').glob('*.gz')),
          *sorted((R / 'tools/data/fr18').glob('*.gz')),
          *sorted(D.glob('madison_armstrong_graphic*.png'))]
manifest = {str(p.relative_to(R)): hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
(D / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps({'N': data['N'], 'K': data['K'],
                  'controls': [r for r in results if 'token_accuracy' in r]}, indent=2))
