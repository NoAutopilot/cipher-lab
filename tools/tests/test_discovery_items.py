"""Offline test for tools/discovery_items.py --notes mode (no network)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import discovery_items as di  # noqa: E402


def fake_fetch(url):
    if "/children/" in url:
        return {"hasMoreAfterLast": False, "assets": [{"id": "C1"}, {"id": "C2"}]}
    if url.endswith("/C1"):
        return {"citableReference": "P/1", "coveringDates": "1749", "id": "C1", "note": "Partly in cipher.",
                "scopeContent": {"description": "<p>Folio 1: A to B. News. </p>"}}
    return {"citableReference": "P/2", "coveringDates": "1749", "id": "C2", "note": None,
            "scopeContent": {"description": "<p>Folio 2: B to A. Thanks. </p>"}}


def test_note_field_flags_cipher_outside_description():
    rows = list(di.note_rows("P", fetch=fake_fetch, pause=0))
    assert rows[0][3] == "Partly in cipher." and rows[0][4] == "cipher"
    assert rows[0][5] == "Folio 1: A to B. News."


def test_item_without_cipher_is_not_flagged():
    rows = list(di.note_rows("P", fetch=fake_fetch, pause=0))
    assert rows[1][3] == "" and rows[1][4] == ""


if __name__ == "__main__":
    test_note_field_flags_cipher_outside_description()
    test_item_without_cipher_is_not_flagged()
    print("ok")
