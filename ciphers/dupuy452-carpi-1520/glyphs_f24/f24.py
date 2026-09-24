#!/usr/bin/env python3
"""Point the Raince-to-Madame pipeline (../glyphs/segment.py, classify.py, prototypes.npz; read
only, never edited) at f.24 (Raince to Robertet, Dupuy 452 ff.24r-24v, IIIF f29 and f30).

Everything specific to f.24 lives here: the page columns, the gutter strip (f24v runs past its
crops' right edge at x=4150; strip f30 x4050-4400 y1250-3150 fetched 24 Sept 2026) and the cipher
span (cipher_span_f24.json, set by eye on the reconstructed columns)."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
GLYPHS = os.path.join(os.path.dirname(HERE), "glyphs")
sys.path.insert(0, GLYPHS)
import segment as sg  # noqa: E402

sg.PAGES = {
    "f24r": dict(xlim=(4550, 7850), gutter=[]),
    "f24v": dict(xlim=(150, 4300), gutter=[("f30_x4050_y1250_w350_h1900.jpg", 4050, 1250)]),
}
sg.CIPHER_SPAN_FILE = os.path.join(HERE, "cipher_span_f24.json")
import classify as cl  # noqa: E402  (imports the patched segment module)
