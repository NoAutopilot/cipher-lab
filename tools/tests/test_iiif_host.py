#!/usr/bin/env python3
"""Offline test for the --iiif-host option of tools/iiif_lines.py and tools/gallica_folio.py (IIIF-HOST, 13 Oct 2026).
No network: urlopen is replaced by a stub that records the URL and returns a fixture.
1. URL building, both hosts: gallica keeps its IIIF v2 form (.../full/full/0/native.jpg, unchanged default);
   openapi gives https://openapi.bnf.fr/iiif/image/v3/ark:/12148/ARK/fN/REGION/max/0/default.jpg.
2. iiif_base() strips a v3 request URL (size 'max') back to its service base; fetch_region() asks the stub for the
   v3 URL and caches under a name distinct from the Gallica one.
3. info_size() reads width/height from the live openapi info.json of btv1b90015040 f239 (fixture, 7810x5778), and
   from a v2-shaped dict.
4. gallica_folio: the openapi Presentation v3 manifest (fixture: first four canvases of btv1b90015040) parses to
   canvases with labels and sizes; --iiif-host openapi prints openapi image URLs; with no cache it fetches the v3
   manifest path once and caches it; with OPENAPI_MANIFESTS emptied it exits 2 without fetching.
Run: python3 tools/tests/test_iiif_host.py (or pytest)"""
import contextlib, io, json, os, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import iiif_lines as il
import gallica_folio as gf

FIX = os.path.join(ROOT, 'tools', 'tests', 'fixtures')
INFO = os.path.join(FIX, 'openapi_info_v3_btv1b90015040_f239.json')
MAN3 = os.path.join(FIX, 'openapi_manifest_v3_btv1b90015040_head.json')
ARK = 'btv1b90015040'


class Stub:
    def __init__(self, body):
        self.body, self.urls = body, []

    def __call__(self, req, timeout=None):
        self.urls.append(req.full_url)
        body = self.body
        class R:
            def read(self_):
                return body
        return R()


@contextlib.contextmanager
def patched(mod, stub):
    old = mod.urllib.request.urlopen
    mod.urllib.request.urlopen = stub
    try:
        yield
    finally:
        mod.urllib.request.urlopen = old


def test_url_building():
    g = il.image_base(ARK, 239)
    o = il.image_base(ARK, 239, 'openapi')
    assert g == f'https://gallica.bnf.fr/iiif/ark:/12148/{ARK}/f239'
    assert o == f'https://openapi.bnf.fr/iiif/image/v3/ark:/12148/{ARK}/f239'
    assert il.region_url(g, '10,20,30,40') == g + '/10,20,30,40/full/0/native.jpg'
    assert il.region_url(g) == g + '/full/full/0/native.jpg'
    assert il.region_url(o, '10,20,30,40') == o + '/10,20,30,40/max/0/default.jpg'
    assert il.region_url(o) == o + '/full/max/0/default.jpg'
    assert il.region_url('https://example.org/iiif/x') == 'https://example.org/iiif/x/full/full/0/default.jpg'
    assert il.iiif_base(o + '/10,20,30,40/max/0/default.jpg') == o
    assert il.iiif_base(o + '/info.json') == o
    assert gf.native_url(ARK, 239) == g + '/full/full/0/native.jpg'
    assert gf.native_url(ARK, 239, 'openapi') == o + '/full/max/0/default.jpg'


def test_fetch_region_openapi():
    stub = Stub(b'\xff\xd8\xff' + b'\0' * 64)
    with tempfile.TemporaryDirectory() as d, patched(il, stub):
        il.time.sleep, sl = (lambda s: None), il.time.sleep
        try:
            p_o, url_o, how = il.fetch_region(il.image_base(ARK, 239, 'openapi'), '1,2,3,4', d)
            p_g, url_g, _ = il.fetch_region(il.image_base(ARK, 239), '1,2,3,4', d)
        finally:
            il.time.sleep = sl
    assert how == 'fetched'
    assert stub.urls == [f'https://openapi.bnf.fr/iiif/image/v3/ark:/12148/{ARK}/f239/1,2,3,4/max/0/default.jpg',
                         f'https://gallica.bnf.fr/iiif/ark:/12148/{ARK}/f239/1,2,3,4/full/0/native.jpg']
    assert p_o != p_g


def test_info_size():
    info = json.load(open(INFO))
    assert info['type'] == 'ImageService3'
    assert il.info_size(info) == (7810, 5778)
    assert il.info_size({'@id': 'x', 'width': 10, 'height': 20}) == (10, 20)


def run_folio(*args):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        r = gf.main(list(args))
    return r, buf.getvalue()


def test_folio_v3_manifest():
    cs = gf.canvases(json.load(open(MAN3)))
    assert [(n, lab, w) for n, lab, w, *_ in cs] == [(1, 'NP', 8403), (2, 'NP', 8242), (3, 'NP', 8092), (4, 'NP', 8125)]
    assert all(isinstance(h, int) and h > 0 for *_, h, _ in cs)
    r, out = run_folio(ARK, '--manifest', MAN3, '--iiif-host', 'openapi', '--anchor', '1=1', '--anchor', '3=2',
                       '--folio', '2', '--json')
    assert '4 canvases (file)' in out
    assert r and all(h['native'].startswith(f'https://openapi.bnf.fr/iiif/image/v3/ark:/12148/{ARK}/f')
                     and h['native'].endswith('/full/max/0/default.jpg') for h in r)


def test_folio_openapi_fetch_and_cache():
    body = open(MAN3, 'rb').read()
    stub = Stub(body)
    with tempfile.TemporaryDirectory() as d, patched(gf, stub):
        sl, gf.time.sleep = gf.time.sleep, (lambda s: None)
        try:
            man, how = gf.fetch_manifest(ARK, d, None, 'openapi')
            man2, how2 = gf.fetch_manifest(ARK, d, None, 'openapi')
        finally:
            gf.time.sleep = sl
    assert stub.urls == [f'https://openapi.bnf.fr/iiif/presentation/v3/ark:/12148/{ARK}/manifest.json']
    assert how == 'fetched from openapi.bnf.fr' and how2 == 'cached'
    assert len(gf.canvases(man)) == 4


def test_folio_openapi_no_manifest_route():
    stub = Stub(b'{}')
    saved = list(gf.OPENAPI_MANIFESTS)
    gf.OPENAPI_MANIFESTS[:] = []
    try:
        with tempfile.TemporaryDirectory() as d, patched(gf, stub), contextlib.redirect_stderr(io.StringIO()):
            try:
                gf.fetch_manifest(ARK, d, None, 'openapi')
                code = 0
            except SystemExit as e:
                code = e.code
    finally:
        gf.OPENAPI_MANIFESTS[:] = saved
    assert code == 2 and stub.urls == []


if __name__ == '__main__':
    fails = 0
    for name, fn in sorted(globals().items()):
        if name.startswith('test_') and callable(fn):
            try:
                fn(); print('PASS', name)
            except AssertionError as e:
                fails += 1; print('FAIL', name, e)
    print('iiif_host:', 'all tests pass' if not fails else f'{fails} failures')
    sys.exit(1 if fails else 0)
