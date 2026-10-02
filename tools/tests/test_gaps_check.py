#!/usr/bin/env python3
"""Offline pytest test for tools/gaps_check.py (CLAUDE.md rule 5 "Finish or name the blocker", 1 Oct 2026).

Builds NOTES.md fixtures under tmp_path; no network, no dependence on the real ciphers/ folder. Covers what the
tool must catch (missing sections, bad blockers, waiting-on naming nothing, not-attempted without next, missing or
duplicated steps, short n/a reasons, a dishonest "parked", a miscounted "keep going") and what it must NOT block
(non-partial targets with no sections, a parked partial whose gaps are all outside, [retired] steps under rule 3,
an honest "keep going", superseded earlier sections, prose lines inside a section).

Run: /root/.local/bin/pytest tools/tests/test_gaps_check.py -q   (or: python3 tools/tests/test_gaps_check.py)
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import gaps_check as gc  # noqa: E402

GAPS_PARKED = """## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)
Read so far: 496 of 522 code tokens (95.0%), NOTES.md step 4
- letter of 3 May, lower half of f.12 - blocker: illegible; water stain, no other image (images/f12.jpg)
- R1041 - blocker: no-key-material; different code, no key on DECODE or in print (NOTES step 6)
- f.14v - blocker: waiting-on ASKS row 30; copy order placed with the holding archive
"""

ESC_ALL_DONE = """## Escalation (1 Oct 2026)
- [x] siblings: ff. 20r and 21r opened; clear instructions of the same office give two names
- [x] clear-pages: f. 21r used as crib; gives the name sign
- [x] known-keys: KEY-OFFICES.tsv and design_prior.py: no key of this office and decade
- [x] print: Lonchay IV no. 183 and the CSP calendar grep: nothing on f. 22
- [retired] key-rebuild: homophonic_anneal.py failed its own gate three times (rule 3); needs a different instrument
- [x] image-check: four out-of-key tokens 65, 52, 48, 72 re-read as glued digit pairs
- [n/a] retry: nothing left to rerun after the image check
Verdict: parked: every gap has an outside blocker
"""

GAPS_KEEP = """## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)
Read so far: unmeasured; no token-level reading file exists yet for the second letter
- codes 42, 57, 88 - blocker: open-codes; each occurs once, no context narrows them
- letter 2 lines 1-9 - blocker: not-attempted; never run with the extended key; next: rerun decode_key.py with key v3, ~$1
"""

ESC_KEEP = """## Escalation (1 Oct 2026)
- [x] siblings: R1036-R1042 opened; R1039 is the clear copy of the first segment
- [x] clear-pages: none on the records
- [x] known-keys: R1024, R1038 tried; R1038 fits
- [x] print: Colenbrander, CSP grep, GL.htm: nothing
- [ ] key-rebuild: seeded anneal from the 80 groups that already read
- [x] image-check: doubtful tokens re-read on the page image, two corrected
- [ ] retry: rerun letter 2 with the extended key
Verdict: keep going: 2 internal gaps; cheapest next: rerun letter 2 with key v3, ~$1
"""


def make(tmp_path, target, status_line, body=""):
    d = tmp_path / "ciphers" / target
    d.mkdir(parents=True)
    (d / "NOTES.md").write_text("# Title of %s\n\n%s\n\nSome notes.\n\n%s" % (target, status_line, body), encoding="utf-8")
    return str(tmp_path / "ciphers")


def run(cdir, *args):
    out = io.StringIO()
    code = gc.main(list(args) + ["--ciphers-dir", cdir], out=out)
    return code, out.getvalue()


def check(status, body):
    return gc.check_text("# T\n\n%s\n\n%s" % (status, body), gc.first_status_word("# T\n\n%s\n" % status))


# ---- must NOT block -----------------------------------------------------------------------------------------

def test_open_target_without_sections_is_skipped(tmp_path):
    cdir = make(tmp_path, "t-open", "Status: open")
    code, out = run(cdir, "t-open")
    assert code == 0 and out.startswith("SKIP t-open")


def test_solved_target_without_sections_is_skipped(tmp_path):
    cdir = make(tmp_path, "t-solved", "solved")
    code, out = run(cdir, "t-solved")
    assert code == 0 and "SKIP" in out


def test_parked_partial_all_outside_passes_including_retired_step():
    kind, msg = check("Status: partial", GAPS_PARKED + "\n" + ESC_ALL_DONE)
    assert kind == "OK-parked", msg


def test_honest_keep_going_passes():
    kind, msg = check("partial", GAPS_KEEP + "\n" + ESC_KEEP)
    assert kind == "OK-keep", msg
    assert "2 internal gap(s), 2 step(s) untried" in msg


def test_last_sections_win_over_superseded_ones():
    old = "## Remaining gaps\n- junk without blocker\n\n## Escalation\n- [?] nonsense: x\n\n## Later work\nprose\n\n"
    kind, msg = check("partial", old + GAPS_PARKED + "\n" + ESC_ALL_DONE)
    assert kind == "OK-parked", msg


def test_prose_lines_inside_sections_are_ignored():
    gaps = GAPS_PARKED.replace("Read so far:", "A note before the list, not a bullet.\nRead so far:")
    esc = ESC_ALL_DONE.replace("Verdict:", "  continuation prose for the retry step.\nVerdict:")
    kind, msg = check("partial", gaps + "\n" + esc)
    assert kind == "OK-parked", msg


def test_waiting_on_a_named_reply_passes():
    gaps = GAPS_PARKED.replace("waiting-on ASKS row 30", "waiting-on the Simancas archive reply to the copy order")
    kind, msg = check("partial", gaps + "\n" + ESC_ALL_DONE)
    assert kind == "OK-parked", msg


# ---- must catch ---------------------------------------------------------------------------------------------

def test_partial_without_sections_fails(tmp_path):
    cdir = make(tmp_path, "t-part", "status: partial")
    code, out = run(cdir, "t-part")
    assert code == 1 and "FAIL t-part" in out and "no '## Remaining gaps'" in out


def test_unknown_blocker_fails():
    gaps = GAPS_PARKED.replace("blocker: illegible", "blocker: hard")
    kind, msg = check("partial", gaps + "\n" + ESC_ALL_DONE)
    assert kind == "FAIL" and "not in vocabulary" in msg


def test_gap_without_reason_fails():
    gaps = GAPS_PARKED.replace("blocker: illegible; water stain, no other image (images/f12.jpg)", "blocker: illegible")
    kind, msg = check("partial", gaps + "\n" + ESC_ALL_DONE)
    assert kind == "FAIL" and "no reason" in msg


def test_waiting_on_naming_nothing_fails():
    gaps = GAPS_PARKED.replace("waiting-on ASKS row 30", "waiting-on")
    kind, msg = check("partial", gaps + "\n" + ESC_ALL_DONE)
    assert kind == "FAIL" and "waiting-on names no" in msg


def test_not_attempted_without_next_fails():
    gaps = GAPS_KEEP.replace("; next: rerun decode_key.py with key v3, ~$1", "")
    kind, msg = check("partial", gaps + "\n" + ESC_KEEP)
    assert kind == "FAIL" and "without '; next:" in msg


def test_missing_step_fails():
    esc = "\n".join(l for l in ESC_ALL_DONE.splitlines() if "image-check" not in l) + "\n"
    kind, msg = check("partial", GAPS_PARKED + "\n" + esc)
    assert kind == "FAIL" and "'image-check' missing" in msg


def test_duplicate_and_bad_mark_fail():
    esc = ESC_ALL_DONE.replace("- [x] print:", "- [x] siblings: again, twice over\n- [y] print:")
    kind, msg = check("partial", GAPS_PARKED + "\n" + esc)
    assert kind == "FAIL" and "listed twice" in msg and "mark [y]" in msg


def test_short_na_reason_fails():
    esc = ESC_ALL_DONE.replace("[n/a] retry: nothing left to rerun after the image check", "[n/a] retry: none")
    kind, msg = check("partial", GAPS_PARKED + "\n" + esc)
    assert kind == "FAIL" and "at least three words" in msg


def test_parked_with_internal_gap_fails():
    kind, msg = check("partial", GAPS_KEEP + "\n" + ESC_ALL_DONE)
    assert kind == "FAIL" and "internal" in msg


def test_parked_with_untried_step_fails():
    esc = ESC_ALL_DONE.replace("- [x] print:", "- [ ] print:")
    kind, msg = check("partial", GAPS_PARKED + "\n" + esc)
    assert kind == "FAIL" and "not yet tried: print" in msg


def test_keep_going_count_mismatch_fails():
    esc = ESC_KEEP.replace("keep going: 2 internal gaps", "keep going: 5 internal gaps")
    kind, msg = check("partial", GAPS_KEEP + "\n" + esc)
    assert kind == "FAIL" and "says 5 internal gaps" in msg


def test_missing_verdict_fails():
    esc = "\n".join(l for l in ESC_ALL_DONE.splitlines() if not l.startswith("Verdict")) + "\n"
    kind, msg = check("partial", GAPS_PARKED + "\n" + esc)
    assert kind == "FAIL" and "no 'Verdict:'" in msg


def test_bourdeau_sample_without_image_check_fails():
    """His section-0a sample has six steps; ours adds image-check (the Mercy glued-digit lesson)."""
    esc = "\n".join(l for l in ESC_ALL_DONE.splitlines() if "image-check" not in l) + "\n"
    kind, msg = check("partial", GAPS_PARKED + "\n" + esc)
    assert kind == "FAIL"


def test_waiting_on_an_unnamed_reply_fails():
    """A reply from nobody in particular is not a checkable outside blocker (review, 2 Oct 2026)."""
    gaps = GAPS_PARKED.replace("waiting-on ASKS row 30", "waiting-on a reply")
    kind, msg = check("partial", gaps + "\n" + ESC_ALL_DONE)
    assert kind == "FAIL" and "waiting-on names no" in msg


def test_read_so_far_without_a_number_fails():
    gaps = GAPS_PARKED.replace("496 of 522 code tokens (95.0%), NOTES.md step 4", "most of it")
    kind, msg = check("partial", gaps + "\n" + ESC_ALL_DONE)
    assert kind == "FAIL" and "Read so far" in msg


def test_indented_sub_bullets_are_continuation_not_gaps():
    gaps = GAPS_PARKED.replace("- R1041", "  - the stain covers lines 3-9 of the lower half\n- R1041")
    esc = ESC_ALL_DONE.replace("- [x] clear-pages:", "\t- detail under the siblings step\n- [x] clear-pages:")
    kind, msg = check("partial", gaps + "\n" + esc)
    assert kind == "OK-parked", msg


def test_fenced_code_is_ignored():
    """A quoted copy of the format, or a '# comment' line in a fence, neither replaces nor ends a section."""
    quoted = "\n```\n## Remaining gaps\n- junk without blocker\n```\n"
    esc = ESC_ALL_DONE.replace("Verdict:", "```\n# a shell comment\npython3 tools/gaps_check.py t\n```\nVerdict:")
    kind, msg = check("partial", GAPS_PARKED + "\n" + esc + quoted)
    assert kind == "OK-parked", msg


# ---- --all and exit codes -----------------------------------------------------------------------------------

def test_all_scans_only_partials(tmp_path):
    make(tmp_path, "a-open", "open")
    make(tmp_path, "b-parked", "Status: partial", GAPS_PARKED + "\n" + ESC_ALL_DONE)
    cdir = make(tmp_path, "c-keep", "partial", GAPS_KEEP + "\n" + ESC_KEEP)
    code, out = run(cdir, "--all")
    assert code == 0
    assert "a-open" not in out
    assert "OK parked b-parked" in out and "OK keep-going c-keep" in out
    assert "2 checked: 1 parked, 1 keep-going, 0 FAIL" in out


def test_all_exits_nonzero_on_any_fail(tmp_path):
    make(tmp_path, "b-parked", "partial", GAPS_PARKED + "\n" + ESC_ALL_DONE)
    cdir = make(tmp_path, "d-bare", "partial")
    code, out = run(cdir, "--all")
    assert code == 1 and "FAIL d-bare" in out


def test_unknown_target_is_usage_error(tmp_path):
    cdir = make(tmp_path, "a-open", "open")
    code, out = run(cdir, "nope")
    assert code == 2 and "ERROR nope" in out


def test_help_works():
    try:
        gc.main(["--help"])
    except SystemExit as e:
        assert e.code == 0


if __name__ == "__main__":
    # Plain-python fallback (no pytest needed): run every test_* with a fresh temporary tmp_path.
    import inspect
    import pathlib
    import tempfile
    failures = 0
    for name, fn in sorted(globals().items()):
        if not (name.startswith("test_") and callable(fn)):
            continue
        with tempfile.TemporaryDirectory() as d:
            try:
                fn(pathlib.Path(d)) if inspect.signature(fn).parameters else fn()
                print("ok   " + name)
            except Exception as e:  # noqa: BLE001
                failures += 1
                print("FAIL %s: %r" % (name, e))
    print("passed: %d failure(s)" % failures)
    sys.exit(1 if failures else 0)
