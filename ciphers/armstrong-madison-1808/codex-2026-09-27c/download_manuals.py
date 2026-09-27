"""Download public-domain primary manuals and check the inspected scan hashes.

Usage: python download_manuals.py /tmp/armstrong-shorthand
Then: pdftotext -layout Annet1770.pdf Annet1770.txt
      pdftoppm -f 3 -singlefile -scale-to 2000 -png Annet1770.pdf Annet1770-03
The PDFs are external inputs, not committed generated artifacts.
"""
from pathlib import Path
import hashlib
import json
import sys
import urllib.request

D = Path(__file__).resolve().parent
out = Path(sys.argv[1])
out.mkdir(parents=True, exist_ok=True)
for item in json.loads((D/'manual_sources.json').read_text()):
    dst = out/f'Annet{item["year"]}.pdf'
    if not dst.exists():
        req = urllib.request.Request(item['url'], headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read()
        assert data.startswith(b'%PDF'), 'Response is not a PDF'
        dst.write_bytes(data)
    data = dst.read_bytes()
    assert len(data) == item['bytes']
    assert hashlib.sha256(data).hexdigest() == item['sha256'], 'Different source revision'
    print(dst, 'verified')
