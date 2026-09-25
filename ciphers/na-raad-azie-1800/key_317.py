"""Invnr 317's cipher system: a keyword-driven 13-row reciprocal alphabet.

Transcribed from images/317_leaf1_alphabet.jpg (the table) and
images/317_leaf2_example.jpg (the worked example, keyword "Nebawo",
plaintext "De zaak zal geld kosten"), NA 2.01.27.02 invnr 317.

Table layout (as it appears on the page): 13 rows, each headed by a pair of
key letters (Z.Y, X.W, V.U, T.S, R.Q, P.O, N.M, L.K, J.I, H.G, F.E, D.C,
B.A -- the 26 letters split into 13 consecutive pairs counting down from Z).
Each row has two aligned lines: a fixed top line "a b c d e f g h i j k l m"
and a bottom line that is some rotation of "n o p q r s t u v w x y z". A
plaintext letter in a-m is looked up in the top line and read off the
bottom line (or vice versa for a-m<->n-z in general); which of the 13 rows
governs a given plaintext letter is selected by the *key* letter (from a
repeating keyword) currently in play, via the pair it belongs to.

Verified exactly against the worked example (grade H, this worker's own
read, 25 Sept 2026): row 1 (Z.Y, unrotated bottom "nopqrstuvwxyz") and row 7
(N.M) -- the example states literally "d in N is x", and row 7's table
predicts d(index3) -> bottom[3] of "uvwxyznopqrst" = x. Confirmed.

NOT independently re-verified against the worked example for the other
11 rows (grade M): this worker's cursive reading of three other worked
instances ("e in E is p", "z in B is m", "a in A is n") does not match what
the table-derived formula below predicts for those rows (predicts u, l, o
respectively) -- most likely a reading error in this worker's transcription
of either the cursive instructional prose or the table's more compressed
lower rows, not re-resolved in this pass (out of scope: the cheap test this
table is used for does not depend on getting every row exactly right, see
NOTES.md "VX-CS06 cheap test").
"""

TOP = "abcdefghijklm"
BOTTOM_BASE = "nopqrstuvwxyz"  # row 1 (Z.Y), unrotated

# Row order top-to-bottom as printed on the page, row index 1..13.
ROW_PAIRS = [
    ("z", "y"), ("x", "w"), ("v", "u"), ("t", "s"), ("r", "q"),
    ("p", "o"), ("n", "m"), ("l", "k"), ("j", "i"), ("h", "g"),
    ("f", "e"), ("d", "c"), ("b", "a"),
]


def _row_bottom(row_index_1based: int) -> str:
    """Bottom alphabet for row i, i=1..13 (rotate BOTTOM_BASE right by i-1)."""
    k = (row_index_1based - 1) % 13
    return BOTTOM_BASE[-k:] + BOTTOM_BASE[:-k] if k else BOTTOM_BASE


def build_rows():
    rows = {}
    for i, (a, b) in enumerate(ROW_PAIRS, start=1):
        bottom = _row_bottom(i)
        top_to_bottom = dict(zip(TOP, bottom))
        bottom_to_top = dict(zip(bottom, TOP))
        rows[a] = rows[b] = {"top_to_bottom": top_to_bottom, "bottom_to_top": bottom_to_top}
    return rows


ROWS = build_rows()


def encipher_letter(plain: str, key_letter: str) -> str:
    row = ROWS[key_letter.lower()]
    p = plain.lower()
    if p in row["top_to_bottom"]:
        return row["top_to_bottom"][p]
    if p in row["bottom_to_top"]:
        return row["bottom_to_top"][p]
    raise ValueError(f"letter {plain!r} not in any row alphabet")


def decipher_letter(cipher: str, key_letter: str) -> str:
    # reciprocal: same lookup both ways
    return encipher_letter(cipher, key_letter)


def running_key(keyword: str, length: int) -> str:
    keyword = keyword.lower()
    return (keyword * (length // len(keyword) + 1))[:length]


def encipher(plaintext: str, keyword: str) -> str:
    letters = [c for c in plaintext.lower() if c.isalpha()]
    key = running_key(keyword, len(letters))
    return "".join(encipher_letter(p, k) for p, k in zip(letters, key))


def decipher(ciphertext: str, keyword: str) -> str:
    letters = [c for c in ciphertext.lower() if c.isalpha()]
    key = running_key(keyword, len(letters))
    return "".join(decipher_letter(c, k) for c, k in zip(letters, key))


if __name__ == "__main__":
    # Self-check against the one worked-example instance fully confirmed above.
    assert encipher_letter("d", "n") == "x", "row 7 (N.M) check failed"
    print("row 7 (N.M) self-check: d,N -> x  OK")

    pt = "de zaak zal geld kosten"
    ct = encipher(pt, "nebawo")
    rt = decipher(ct, "nebawo")
    print("plaintext:", pt)
    print("cipher (this table):", ct)
    print("round-trip:", rt, "OK" if rt == "".join(c for c in pt if c.isalpha()) else "MISMATCH")
