"""Fetch the three credited reference images and verify their recorded hashes."""
from pathlib import Path
import hashlib
import json
import urllib.request

D = Path(__file__).resolve().parent
R = D.parents[2]
sources = json.loads((D / 'sources.json').read_text())
for source in sources:
    name = source['file']
    url = source['url']
    with urllib.request.urlopen(url, timeout=60) as response:
        data = response.read()
    expected = source['sha256']
    if hashlib.sha256(data).hexdigest() != expected:
        raise ValueError(f'{name}: remote image differs from recorded source; not replacing it')
    (D / name).write_bytes(data)
    print(name, len(data))
