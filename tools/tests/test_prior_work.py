#!/usr/bin/env python3
"""Offline tests for tools/prior_work.py and tools/shelfmark.py (PRIOR-WORK v1, 8 Oct 2026; CLAUDE.md Usage 8a).

Each case builds a throwaway git repository (fixtures from tools/tests/fixtures/prior_work/ plus inline files), points
refs/remotes/origin/main at it and runs the gate in-process with --root, --now and a socket guard: no test opens a
network connection.
Must catch: a NOTES '[x]' bullet naming the same leaf (exit 3); a ROOM claim 2 h old without done (LEAD live-claim,
exit 4); Tomokiyo 'f.18 (no.6) ... both deciphered' for fr.3040 (KNOWN, exit 2; --known-answer key-check exit 0); an
AUDIT line classing the item as already known (KNOWN); a NOTES period gloss on THIS leaf (KNOWN); --register flagging
the NEXT-STEPS row whose step is done; an edition window with its control hit (LEAD); G3 SUBSTANCE.
Must NOT block: the E78 shape (KNOWN-PART, exit 0, code words as residue); a gloss on a DIFFERENT letter on a
neighbouring leaf (CONTEXT, not KNOWN); DECODE 'Non-decrypted' (no KNOWN, no CLEAR); fr.16104 vs fr.16105 same folio
(not matched); a check that could not run (UNCHECKED, not CLEAR).
Run: python3 tools/tests/test_prior_work.py"""
import atexit
import contextlib
import io
import os
import shutil
import socket
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
FIX = os.path.join(HERE, "fixtures", "prior_work")
sys.path.insert(0, os.path.join(REPO, "tools"))
import prior_work as pw  # noqa: E402
import shelfmark as sm  # noqa: E402

NOW = "2026-10-08T16:00"
fails = 0


def _no_net(*a, **k):
    raise AssertionError("network access attempted in an offline test")


socket.socket.connect = _no_net
socket.create_connection = _no_net


def check(label, ok, detail=""):
    global fails
    fails += not ok
    print(("PASS" if ok else "FAIL"), label, "" if ok else f"-> {detail}"[:600])


def repo(files, links=()):
    root = tempfile.mkdtemp(prefix="pw-test-")
    atexit.register(shutil.rmtree, root, True)
    for rel, content in files.items():
        p = os.path.join(root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        if isinstance(content, tuple):          # ("copy", fixture name)
            shutil.copy(os.path.join(FIX, content[1]), p)
        else:
            open(p, "w", encoding="utf-8").write(content)
    for rel, target in links:
        p = os.path.join(root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        os.symlink(target, p)
    g = ["git", "-C", root, "-c", "user.email=t@example.org", "-c", "user.name=t"]
    subprocess.run(["git", "-C", root, "init", "-q"], check=True)
    subprocess.run(g + ["add", "-A"], check=True)
    subprocess.run(g + ["commit", "-q", "-m", "fixture"], check=True)
    subprocess.run(["git", "-C", root, "update-ref", "refs/remotes/origin/main", "HEAD"], check=True)
    pw._IDX.clear()
    pw._TEXTS.clear()
    return root


def run(root, *args):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = pw.main(list(args) + ["--root", root, "--now", NOW])
    return code, out.getvalue()


ITEMS = ("item_id\tshelfmark\tfolio\tcanvas\tdecode\tptr\twvo\tdate\tcalendar\tsender\trecipient\toffice\tplace\tlanguage\t"
         "kind\tholder_url\tclear_words\tverified\n")


def item(item_id, shelfmark="", folio="", decode="", ptr="", date="", sender="", recipient="", kind="correspondence"):
    return "\t".join([item_id, shelfmark, folio, "", decode, ptr, "", date, "", sender, recipient, "", "", "", kind,
                      "", "", "catalogue-only"]) + "\n"


BASE = {"ROOM.md": "# ROOM\n", "WORK-QUEUE.tsv": "job_id\taccount\tbrief\tmodel\tcap_usd\tbox_min\tstatus\tadded\tnote\n",
        "status.json": '{"results": []}\n', "sources/cyphersolver/2026-10-01/README.md": "solver snapshot (fixture)\n",
        "sources/cryptiana/web/unsolved.htm": "<html><body><P>index (fixture)</P></body></html>\n"}


def target(slug, notes="Status: open\n", items=None, extra=None, base=True):
    files = dict(BASE) if base else {}
    files[f"ciphers/{slug}/NOTES.md"] = notes
    files[f"ciphers/{slug}/items.tsv"] = ITEMS + "".join(items or [item("f18", "BnF fr.3040", "18r")])
    files.update(extra or {})
    return files


# ---------------------------------------------------------------- shelfmark.py
u = sm.unit("BnF fr.3040", "18r")
check("shelfmark: fr.3040 f.18r matches 'f.18 (no.6) ... BnF fr.3040'", sm.match(u, "BnF fr.3040 f.18 (no.6)") == "exact")
u2 = sm.unit("BnF fr.16104", "102r")
check("shelfmark: fr.16104 f.102r does NOT match fr.16105 f.102r", sm.match(u2, "BnF fr.16105 f.102r") is None)
check("shelfmark: crop c105_f102r_L01.jpg does NOT match fr.16104", sm.match(u2, "c105_f102r_L01.jpg") is None)
check("shelfmark: crop c104_f102r_L01.jpg matches fr.16104", sm.match(u2, "c104_f102r_L01.jpg") == "exact")
check("shelfmark: f.18r does not match f.18v", sm.match(u, "BnF fr.3040 f.18v") is None)
check("shelfmark: bare folio in a multi-volume folder is ambiguous", sm.match(u, "f.18r read", multi_volume=True) == "ambiguous")
check("shelfmark: DECODE id matches", sm.match(sm.unit(extra_ids={"R9502"}), "DECODE R9502 (3 pages)") == "exact")

# ---------------------------------------------------------------- sentence classes
cases = {"no separate déchiffrement item listed": "neg", "f.18 (no.6) from Boulogne, both deciphered": "pos",
         "These undeciphered letters can be read with the key": "keysrc", "Non-decrypted": "neg",
         "En partie chiffrée, sans le déchiffrement": "neg", "Gedeeltelijk gedecodeerd": "partial",
         "*Undeciphered. Deciphered by George above": "pos"}
for text, want in cases.items():
    check(f"classify {text!r} -> {want}", pw.classify(text) == want, pw.classify(text))

# ---------------------------------------------------------------- 1. own work: [x] bullet -> DONE, exit 3
r = repo(target("fx-done", "Status: partial\n\n## Escalation\n- [x] transcribe: BnF fr.3040 f.18r, two blind passes "
                "reconciled (5 Oct 2026)\n"))
code, out = run(r, "fx-done", "--item", "f18", "--step-type", "transcribe")
check("[x] bullet naming the same leaf -> DONE, exit 3", code == 3 and "DONE" in out, out)
code, out = run(r, "fx-done", "--item", "f18", "--step-type", "propagate-revision")
check("propagate-revision is never DONE", code != 3, out)

r = repo(target("fx-otherleaf", "Status: partial\n- [x] transcribe: BnF fr.16105 f.102r, two passes (5 Oct 2026)\n",
                [item("v102", "BnF fr.16104", "102r")]))
code, out = run(r, "fx-otherleaf", "--item", "v102", "--step-type", "transcribe")
check("fr.16105 [x] bullet does NOT make fr.16104 f.102r DONE", code != 3 and " DONE " not in out, out)

# ---------------------------------------------------------------- 1. ROOM live claim
room = ("# ROOM\n2026-10-08 14:00 | R7 (account 2, Sonnet worker) | fx-room | claim: transcribe BnF fr.3040 f.18r, cap USD 3\n"
        "2026-10-08 15:00 | Q9 (account 1, Sonnet worker) | fx-room | done: unrelated check\n")
r = repo(target("fx-room", extra={"ROOM.md": room}))
code, out = run(r, "fx-room", "--item", "f18")
check("ROOM claim 2 h old without done -> LEAD live-claim, exit 4", code == 4 and "live-claim" in out, out)
code, out = run(r, "fx-room", "--item", "f18", "--me", "R7")
check("--me R7: your own claim is not someone else's live work", "live-claim" not in out, out)
r = repo(target("fx-room2", extra={"ROOM.md": room.replace("fx-room", "fx-room2") +
                                   "2026-10-08 15:30 | R7 (account 2, Sonnet worker) | fx-room2 | done: transcribed f.18r\n"}))
code, out = run(r, "fx-room2", "--item", "f18")
check("ROOM claim followed by the same tag's done line -> no live-claim", "live-claim" not in out, out)

r = repo(target("fx-room", extra={"ROOM.md": room.replace("| fx-room |", "| fx-room2 |")}))
code, out = run(r, "fx-room", "--item", "f18")
check("a claim on fx-room2 is not a claim on fx-room (slug matched as a whole word)", "live-claim" not in out, out)

# ---------------------------------------------------------------- 3. Tomokiyo KNOWN -> exit 2; --known-answer -> 0
tomo = {"sources/cryptiana/web/fixture.htm": ("copy", "tomokiyo_fixture.htm")}
r = repo(target("fx-tomo", extra=tomo))
code, out = run(r, "fx-tomo", "--item", "f18")
check("Tomokiyo 'f.18 (no.6) ... both deciphered' under BnF fr.3040 -> KNOWN, exit 2",
      code == 2 and "KNOWN" in out and "3-tomokiyo" in out, out)
code, out = run(r, "fx-tomo", "--item", "f18", "--known-answer", "key-check")
check("--known-answer key-check lowers exit 2 to 0 and names the consumer", code == 0 and "key-check" in out, out)
code, out = run(r, "fx-tomo", "--item-spec", "item_id=f16;shelfmark=BnF fr.3040;folio=16r")
check("Tomokiyo 'Undeciphered' is no evidence (not KNOWN, not CLEAR from that line)",
      code != 2 and "KNOWN " not in out.split("verdict")[0].split("3-tomokiyo")[0][-40:], out)

# ---------------------------------------------------------------- fr.16104 vs fr.16105, same folio
r = repo(target("fx-vol", items=[item("v102", "BnF fr.16104", "102r")], extra=tomo))
code, out = run(r, "fx-vol", "--item", "v102")
check("Tomokiyo fr.16105 f.102 'decipherment attached' does NOT make fr.16104 f.102r KNOWN",
      code != 2 and "plaintext KNOWN" not in out and "CLEAR         3-tomokiyo" in out, out)

# ---------------------------------------------------------------- 1. AUDIT classes the item as already known
audit = "# AUDIT\n\n| item | class | note |\n|---|---|---|\n| BnF fr.3040 f.18r no.6 | **N0** | first printed by Le Grand 1688 |\n"
r = repo(target("fx-audit", extra={"ciphers/fx-audit/AUDIT.md": audit}))
code, out = run(r, "fx-audit", "--item", "f18")
check("AUDIT line classing the item as already known -> KNOWN, exit 2", code == 2 and "1-own" in out and "KNOWN" in out, out)
check("rule 10: no N-class token and no novelty word in the output", " N0" not in out and "first" not in out.lower(), out)
code, out = run(r, "fx-audit", "--item", "f18", "--step-type", "audit")
check("an audit step on an already-classed item -> DONE, exit 3", code == 3, out)
code, out = run(r, "fx-audit", "--item", "f18", "--step-type", "upgrade-audit")
check("upgrade-audit is never DONE (and works no text scope)", code == 0, out)

# ---------------------------------------------------------------- 2. gloss on THIS leaf -> KNOWN; another letter -> CONTEXT
r = repo(target("fx-gloss", "Status: open\nf.18r (BnF fr.3040) carries an interlinear period decipherment of this letter "
                "in the clerk's hand.\n"))
code, out = run(r, "fx-gloss", "--item", "f18")
check("NOTES period gloss on THIS leaf -> KNOWN (2-leaf), exit 2", code == 2 and "2-leaf" in out and "KNOWN" in out, out)
r = repo(target("fx-gloss2", "Status: open\nf.19r (BnF fr.3040) carries an interlinear decipherment of a different "
                "letter (no.7, Raince).\n"))
code, out = run(r, "fx-gloss2", "--item", "f18")
check("gloss on a DIFFERENT letter on a neighbouring leaf -> CONTEXT, not KNOWN",
      code != 2 and "CONTEXT" in out and "plaintext KNOWN" not in out and "verdict plaintext: KNOWN" not in out, out)
check("... and the leaf look for f.18r is still owed (LOOK, exit 4), with look.tsv written",
      code == 4 and "LOOK" in out and os.path.isfile(os.path.join(r, "ciphers/fx-gloss2/look.tsv")), out)
look = open(os.path.join(r, "ciphers/fx-gloss2/look.tsv")).read()
check("look.tsv lists cipher page, facing page, two before and four after", all(x in look for x in (
    "cipher-page\t18r", "facing\t17v", "before-2\t17r", "after-1\t18v", "after-4\t20r")), look)

# ---------------------------------------------------------------- 2. --record answers the LOOK
lrow = [l.split()[3].strip("[]") for l in out.splitlines() if " LOOK " in l][0]
code, rec = run(r, "fx-gloss2", "--record", lrow, "CLEAR: f.18r, f.17v, f.19r read at native size, no gloss")
code, out = run(r, "fx-gloss2", "--item", "f18")
check("--record CLEAR on the LOOK row -> exit 0 on the next run", code == 0 and "recorded" in out, out)
code, rec = run(r, "fx-gloss2", "--record", lrow, "maybe: unsure")
check("--record with no verdict word is a usage error (exit 1)", code == 1, rec)

# ---------------------------------------------------------------- 3. DECODE Non-decrypted / Partially decrypted
dec = {"sources/decode/records-fixture.tsv": ("copy", "decode_listing_fixture.tsv")}
r = repo(target("fx-decode", items=[item("r9502", decode="R9502"), item("r1162", decode="R1162")], extra=dec))
code, out = run(r, "fx-decode", "--item", "r9502")
drows = [l for l in out.splitlines() if "3-decode" in l]
check("DECODE 'Non-decrypted' -> CONTEXT only: no KNOWN and no CLEAR from that line",
      drows and all(" CONTEXT " in l for l in drows), out)
look = open(os.path.join(r, "ciphers/fx-decode/look.tsv")).read()
check("... and a unit of 3 record images is listed whole in look.tsv", "all 3 DECODE record images" in look, look)
code, out = run(r, "fx-decode", "--item", "r1162")
check("DECODE 'Partially decrypted' -> KNOWN-PART", "KNOWN-PART" in out and code != 2, out)

# ---------------------------------------------------------------- checks that cannot run -> UNCHECKED, never CLEAR
r = repo(target("fx-nomirror", base=False, extra={"ROOM.md": "# ROOM\n"}))
code, out = run(r, "fx-nomirror", "--item", "f18")
check("no Tomokiyo mirror on disk -> UNCHECKED (not CLEAR), exit 4",
      code == 4 and "UNCHECKED     3-tomokiyo" in out and "CLEAR         3-tomokiyo" not in out, out)
code, out = run(r, "fx-nomirror", "--item", "f18", "--ref", "origin/nosuchbranch")
check("an unresolvable ref -> own work UNCHECKED, never CLEAR", "UNCHECKED     1-own" in out and code == 4, out)

# ---------------------------------------------------------------- 4. editions: control hit / missed / item window
eds = ("edition_id\tfamily\tmatch_slugs\toffice\tcorrespondents\tdate_from\tdate_to\tlanguage\ttitle\tia_ids\taccess_tier\t"
       "segmenter\tcontrol_date\tcontrol_sender\tcontrol_recipient\tcontrol_ia\tcontrol_source\tverified\tsource\n")
row = "fx-or\tfixture\tfx-ed*\tUS War Dept\tHalleck;Butler\t1864\t1864\ten\tFixture OR\tfixtureed01\tdjvu\tor-dateline\t{}\t{}\t{}\tfixtureed01\tfixture\tfixture\tfixture\n"
edfiles = {"sources/ia-fulltext/print-check/fixtureed01_djvu.txt": ("copy", "fixtureed01_djvu.txt")}
r = repo(target("fx-ed1", items=[item("t1", date="1864-04-23", sender="H. W. Halleck", recipient="C. C. Augur"),
                                 item("t2", date="1864-06-02", sender="H. W. Halleck", recipient="E. O. C. Ord")],
                extra=dict(edfiles, **{"tools/data/prior_editions.tsv": eds + row.format("1864-04-21", "Butler", "Fox")})))
code, out = run(r, "fx-ed1", "--item", "t1")
check("edition: date +-1 day and both correspondents in one window, control hit -> LEAD edition-hit",
      code == 4 and "edition-hit" in out and "control hit" in open(os.path.join(r, "ciphers/fx-ed1/prior-work.tsv")).read(), out)
code, out = run(r, "fx-ed1", "--item", "t2")
check("edition: no window but the control hit -> CLEAR for that volume", "CLEAR         4-editions" in out, out)
r = repo(target("fx-ed2", items=[item("t2", date="1864-06-02", sender="H. W. Halleck", recipient="E. O. C. Ord")],
                extra=dict(edfiles, **{"tools/data/prior_editions.tsv": eds + row.format("1864-05-09", "Sherman", "Thomas")})))
code, out = run(r, "fx-ed2", "--item", "t2")
check("edition: control MISSED -> UNCHECKED, never CLEAR", "UNCHECKED     4-editions" in out and "CLEAR         4-editions" not in out, out)
r = repo(target("fx-ed3", items=[item("t2", date="1864-06-02", sender="H. W. Halleck", recipient="E. O. C. Ord")]))
code, out = run(r, "fx-ed3", "--item", "t2")
check("no edition row matches -> core-only UNCHECKED-NET (a warning, not CLEAR)", "UNCHECKED-NET 4-editions" in out and "core-only" in out, out)

r = repo(target("fx-ed6", items=[item("t4", date="1864-04-23")],
                extra=dict(edfiles, **{"tools/data/prior_editions.tsv": eds + row.format("1864-04-21", "Butler", "Fox").replace("fx-ed*", "fx-ed6")})))
code, out = run(r, "fx-ed6", "--item", "t4")
check("an item with no sender or recipient: the identity search cannot run -> UNCHECKED, not CLEAR",
      "UNCHECKED     4-editions" in out and "CLEAR         4-editions" not in out, out)

# ---------------------------------------------------------------- 6. G3: a print within +-3 days sharing entities -> SUBSTANCE
rd = os.path.join(r, "reading.txt")
open(rd, "w").write("The cavalry at Warrenton Junction will move at daylight with 350 men toward Bealeton Station.\n")
r = repo(target("fx-ed4", items=[item("t3", date="1864-04-24", sender="H. W. Halleck", recipient="C. C. Augur")],
                extra=dict(edfiles, **{"tools/data/prior_editions.tsv": eds.replace("fx-ed*", "fx-ed*") + row.format("1864-04-21", "Butler", "Fox")})))
code, out = run(r, "fx-ed4", "--item", "t3", "--reading", rd)
check("G3: decoded phrase printed within +-3 days with 2+ shared entities -> SUBSTANCE", "SUBSTANCE" in out, out)
check("G3 offline: the network phrase family is UNCHECKED-NET and blocks at G3 (exit 4)", code == 4 and "UNCHECKED-NET 6-g3" in out, out)

# ---------------------------------------------------------------- 5. civil-war adapter: E78 shape and a clear entry
eck = {"ciphers/eckert-1864/key.md": ("copy", "eckert_key.md"), "ciphers/eckert-1864/key-no2.md": ("copy", "eckert_key_min.md"),
       "ciphers/eckert-1864/key-no9.md": ("copy", "eckert_key_min.md"),
       "ciphers/eckert-1864/sources/mssEC18/p9714.json": ("copy", "huntington_p9714.json")}
links = [("ciphers/eckert-1864/entries_mssEC19.py", os.path.join(REPO, "ciphers", "eckert-1864", "entries_mssEC19.py"))]
r = repo(dict(target("eckert-1864", items=[item("E78", ptr="9714", date="1864-04-21", kind="ledger-entry"),
                                          item("E74x", ptr="9714/1", date="1864-04-22", kind="ledger-entry")]), **eck), links)
code, out = run(r, "eckert-1864", "--item", "E78")
check("E78 shape (clear words public, code words not) -> KNOWN-PART, exit 0, code words as residue",
      code == 0 and "KNOWN-PART" in out and "plaintext KNOWN " not in out and "jennie" in out.lower(), out)
code, out = run(r, "eckert-1864", "--item", "E74x")
check("a ledger entry clear in the holder's own transcription -> KNOWN (step 0 skip), exit 2", code == 2 and "step 0 skip" in out, out)

# ---------------------------------------------------------------- step mode: --register
ns = ("folder\tstatus\tblocker\tcost_band\tnear_row\tlast_touched\tnext_step\tparallel\tnext_step_full_len\n"
      "fx-reg\tpartial\trunnable\tS\tn\t5 Oct 2026\ttranscribe BnF fr.3040 f.18r with two blind passes\t\t50\n"
      "fx-reg2\tpartial\trunnable\tS\tn\t5 Oct 2026\tfetch canvas 45 once and look for cipher groups\t\t50\n")
files = target("fx-reg", "Status: partial\n- [x] transcribe: BnF fr.3040 f.18r, two blind passes reconciled (5 Oct 2026)\n")
files.update({"ciphers/fx-reg2/NOTES.md": "Status: partial\nNothing done yet.\n", "NEXT-STEPS.tsv": ns})
r = repo(files)
code, out = run(r, "-", "--register", os.path.join(r, "NEXT-STEPS.tsv"), "--columns", "next_step,parallel")
lines = {l.split("\t")[1]: l for l in out.splitlines()[1:] if "\t" in l}
check("--register flags the NEXT-STEPS row whose step is already done (DONE) and leaves the other CLEAR",
      "DONE" in lines.get("fx-reg", "") and "CLEAR" in lines.get("fx-reg2", ""), out)

# ---------------------------------------------------------------- derive and brief
r = repo(target("fx-derive", "Status: open\n\n## BnF fr.3040 f.18r, Gramont to the grand maitre\ntext\n\n## BnF fr.3040 f.29r\n"))
code, out = run(r, "fx-derive", "--derive")
pend = open(os.path.join(r, "ciphers/fx-derive/items.pending.tsv")).read()
check("--derive writes items.pending.tsv only, every row catalogue-only", code == 0 and pend.count("\tcatalogue-only\t") == 2
      and open(os.path.join(r, "ciphers/fx-derive/items.tsv")).read().count("\n") == 2, pend)
brief = os.path.join(r, "brief.md")
open(brief, "w").write("# Brief\nTranscribe BnF fr.3040 f.18r in two blind passes.\n")
code, out = run(r, "fx-derive", "--brief", brief, "--step-type", "transcribe")
check("--brief extracts the item the brief names (fr.3040 f.18r)", "item f18" in out and code in (0, 2, 3, 4), out)
wq = BASE["WORK-QUEUE.tsv"] + "FX-T1\towner\tbrief.md\tSonnet\t3\t30\tdone 2026-10-07 10:00\t2026-10-07 09:00\tfixture\n"
r2 = repo(dict(target("fx-derive"), **{"WORK-QUEUE.tsv": wq, "brief.md": "# Brief\nTranscribe BnF fr.3040 f.18r.\n"}))
code, out = run(r2, "fx-derive", "--brief", os.path.join(r2, "brief.md"))
check("--brief whose own path has a WORK-QUEUE done row (a re-queued brief) -> exit 3", code == 3 and "already ran" in out, out)
code, out = run(r, "fx-derive", "--item", "nosuch")
check("an unknown item is a usage error (exit 1, not 2)", code == 1, out)

# ---------------------------------------------------------------- --network with print_check.Net stubbed (no socket)
class FakeNet:
    """print_check.Net's interface; every host answers 502, so every network family must come back UNCHECKED-NET."""
    def __init__(self, offline, max_requests, delay=1.5):
        self.count, self.status, self.offline = {}, {}, offline

    def get(self, url, **kw):
        self.count["stub"] = self.count.get("stub", 0) + 1
        return None, "HTTP 502"

    def json(self, url, **kw):
        return self.get(url)


real_net, pw.pc.Net = pw.pc.Net, FakeNet
row2 = row.replace("fixtureed01\tdjvu", "notcached99\tdjvu").replace("\tfixtureed01\tfixture", "\tnotcached99\tfixture")
r = repo(target("fx-ed5", items=[item("t1", date="1864-04-23", sender="H. W. Halleck", recipient="C. C. Augur")],
                extra={"tools/data/prior_editions.tsv": eds + row2.format("1864-04-21", "Butler", "Fox")}))
code, out = run(r, "fx-ed5", "--item", "t1", "--network", "--cache", os.path.join(r, ".cache-outside"))
check("--network with every host failing -> UNCHECKED-NET rows (edition and OpenAlex), never CLEAR",
      "UNCHECKED-NET 4-editions" in out and "UNCHECKED-NET 4-net" in out and "CLEAR         4-" not in out, out)
code, out = run(r, "fx-ed5", "--item", "t1", "--network", "--strict", "--cache", os.path.join(r, ".cache-outside"))
check("--strict makes UNCHECKED-NET blocking (exit 4)", code == 4, out)
pw.pc.Net = real_net
tsv = open(os.path.join(r, "ciphers/fx-ed5/prior-work.tsv")).read()
check("network rows carry a 14-day valid_until and the request count", "2026-10-22" in tsv and "stub:" in tsv, tsv[-600:])
code, out = run(r, "fx-ed5", "--item", "t1")
check("an offline run reuses a still-valid network row instead of reporting it unrun", "cached network row" in out, out)

print(f"\n{'all passed' if not fails else f'{fails} FAILED'}")
sys.exit(1 if fails else 0)
