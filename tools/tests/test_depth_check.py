"""Offline tests for tools/depth_check.py (run: python3 -m pytest tools/tests/test_depth_check.py)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import depth_check as dc  # noqa: E402


def counted(**kw):
    r = {"title": "t", "date": "4 Oct 2026", "audit_status": "two audits", "plaintext_novelty": "N4",
         "claim_scope": "recovered-passages"}
    r.update(kw)
    return r


def run(results, strict=False):
    return dc.check(results, strict)


def test_d2_with_sentence_counts():
    f, _, tally, _, solves = run([counted(depth="D2", depth_pct=55, depth_sentence="The writer asks for troops.")])
    assert not f and solves == 1 and tally["D2"] == 1


def test_d1_class_without_reading_not_counted_not_failed():
    f, notes, _, _, solves = run([counted(depth="D1", depth_pct=75)])
    assert not f and solves == 0 and any("not counted" in n for n in notes)


def test_new_counted_result_without_depth_fails():
    f, *_ = run([counted()])
    assert f and "no depth" in f[0]


def test_legacy_counted_without_depth_passes_unless_strict():
    r = counted(date="3 Oct 2026")
    f, notes, _, ungraded, _ = run([r])
    assert not f and ungraded == 1
    f2, *_ = run([r], strict=True)
    assert f2


def test_not_counted_kinds_never_fail_without_depth():
    rs = [counted(plaintext_novelty="N1"), counted(audit_status="one audit"),
          counted(claim_scope="key-to-known-text"), {"kind": "dataset", "date": "5 Oct 2026"},
          counted(superseded_by="x")]
    f, *_ = run(rs)
    assert not f


def test_d2_without_sentence_fails():
    f, *_ = run([counted(depth="D2")])
    assert f and "depth_sentence" in f[0]


def test_d4_needs_pct_and_non_statistical_check():
    f, *_ = run([counted(depth="D4", depth_pct=95, depth_sentence="s", depth_check="auth-distance")])
    assert any("external" in x for x in f)
    f2, *_ = run([counted(depth="D4", depth_pct=95, depth_sentence="s", depth_check="period-gloss",
                          decode_status="Decrypted")])
    assert not f2


def test_decode_status_mismatch_fails():
    f, *_ = run([counted(depth="D2", depth_sentence="s", decode_status="Decrypted")])
    assert f and "decode_status" in f[0]


def test_bad_depth_value_fails():
    f, *_ = run([{"depth": "D9"}])
    assert f


def test_nclass_from_grade_field():
    r = counted(plaintext_novelty="", grade="N4 (no prior decipherment located)", depth="D3", depth_pct=85,
                depth_sentence="s", depth_check="period-key")
    f, _, tally, _, solves = run([r])
    assert not f and solves == 1


if __name__ == "__main__":
    n = 0
    for k, v in sorted(globals().items()):
        if k.startswith("test_"):
            v()
            n += 1
    print(f"{n} passed")
