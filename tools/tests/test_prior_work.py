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
import json
import os
import re
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
r = repo(dict(target("eckert-1864", items=[item("E78", ptr="9714", date="1864-04-21", sender="Meigs", recipient="Biggs",
                                               kind="ledger-entry"),
                                          item("E74x", ptr="9714/1", date="1864-04-22", sender="Meigs", recipient="Butler",
                                               kind="ledger-entry")]), **eck), links)
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
CACHE = tempfile.mkdtemp(prefix="pw-cache-")
atexit.register(shutil.rmtree, CACHE, True)
check("the fixture repository has no remote, so --network's git fetch cannot leave the machine",
      subprocess.run(["git", "-C", r, "remote"], capture_output=True, text=True).stdout.strip() == "")
code, out = run(r, "fx-ed5", "--item", "t1", "--network", "--cache", os.path.join(r, ".cache-inside"))
check("--cache inside --root is refused (exit 1)", code == 1, out)
code, out = run(r, "fx-ed5", "--item", "t1", "--network", "--cache", CACHE)
check("--network with every host failing -> UNCHECKED-NET rows (edition and OpenAlex), never CLEAR",
      "UNCHECKED-NET 4-editions" in out and "UNCHECKED-NET 4-net" in out and "CLEAR         4-" not in out, out)
code, out = run(r, "fx-ed5", "--item", "t1", "--network", "--strict", "--cache", CACHE)
check("--strict makes UNCHECKED-NET blocking (exit 4)", code == 4, out)
pw.pc.Net = real_net
tsv = open(os.path.join(r, "ciphers/fx-ed5/prior-work.tsv")).read()
check("network rows carry a 14-day valid_until and the request count", "2026-10-22" in tsv and "stub:" in tsv, tsv[-600:])
code, out = run(r, "fx-ed5", "--item", "t1")
check("an offline run reuses a still-valid network row instead of reporting it unrun", "cached network row" in out, out)

# ================================================================ review fixes, 8 Oct 2026 (correctness, replay, compliance)
# ---------------------------------------------------------------- shelfmark: binding, ranges, lists, normalisation
check("shelfmark: 'fr.16104 f.98r and fr.16105 f.102r' does NOT name fr.16104 f.102r (each folio bound to its volume)",
      sm.match(u2, "- [x] transcribe fr.16104 f.98r and fr.16105 f.102r (5 Oct 2026)") is None)
check("shelfmark: 'f.18r-v' names f.18v too", sm.match(sm.unit("BnF fr.3040", "18v"), "transcribe BnF fr.3040 f.18r-v") == "exact")
check("shelfmark: a bare year or a dollar figure is not a folio",
      sm.leaves("21 Apr 1864, $300") == set() and sm.match(u, "paid $18 on 18 March 1530, BnF fr.3040") is None)
check("shelfmark: 'WVO 5811, 5810, 4503' names WVO 5810", sm.match(sm.unit(extra_ids={"wvo:5810"}), "WVO 5811, 5810, 4503") == "exact")
check("shelfmark: a shared DECODE id in a line about another volume does not name Colbert 127",
      sm.match(sm.unit("Melanges de Colbert 127", "349", extra_ids={"R2678"}),
               "period interlinear decipherment of Mél. Colbert 159 f.102; DECODE R2678") is None)
check("shelfmark: HStAM, NLA, NA inv., Huntington mss and 'Calig.' shelfmarks parse to volumes",
      all(sm.volume_keys(t) for t in ("HStAM 4 h Nr. 1411", "NLA BU L 1 Nr. 548", "NA 2.01.27.05 invnr 12",
                                      "Huntington mssDE 108(A)", "Calig. C. VII")))

# ---------------------------------------------------------------- classify: negation and modal wording
for text, want in {"no interlinear gloss on the leaf": "neg", "no decipherment attached": "neg",
                   "f.18r has no clear copy attached": "neg", "nothing attached, not glossed": "neg",
                   "That makes a period decipherment of R1953 more likely to have existed": None,
                   "not excluded: a contemporary decipherment in MS Rawl. A. 24": None}.items():
    check(f"classify {text!r} -> {want}", pw.classify(text) == want, pw.classify(text))
check("rule 10: a capitalised name keeps 'New'; a novelty word is masked",
      pw.safe("New Berne ... New Orleans first division") == "New Berne ... New Orleans [*] division",
      pw.safe("New Berne ... New Orleans first division"))

# ---------------------------------------------------------------- 1. own work: markers and verbs
r = repo(target("fx-twovol", "Status: partial\n- [x] transcribe fr.16104 f.98r and fr.16105 f.102r (5 Oct 2026)\n",
                [item("v102", "BnF fr.16104", "102r")]))
code, out = run(r, "fx-twovol", "--item", "v102", "--step-type", "transcribe")
check("[x] bullet naming fr.16104 f.98r and fr.16105 f.102r does not make fr.16104 f.102r DONE", code != 3, out)
for line in ("- [already run 5 Oct: Gallica fetch of BnF fr.3040 f.18r]",
             "- [x] image-check BnF fr.3040 f.18r: no thread of ink; later reading owed",
             "- [x] crop BnF fr.3040 f.18r, spread over two files"):
    r = repo(target("fx-verb", "Status: partial\n" + line + "\n"))
    code, out = run(r, "fx-verb", "--item", "f18", "--step-type", "read")
    check(f"a read step is not DONE from {line[:48]!r}", code != 3, out)
code, out = run(r, "fx-verb", "--item", "f18", "--step-type", "crop")
check("... but the crop marker makes a crop step DONE", code == 3, out)

# crop entries in images/manifest.json (fr16144 shape: canvas from the IIIF source_url)
man = '{"iiif_lines": [{"crop": "c370_L01_s1.jpg", "source_url": "https://gallica.bnf.fr/iiif/ark:/12148/x/f370/1,2,3,4/full/0/native.jpg"}]}'
r = repo(target("fx-cropman", items=[item("c370", "BnF fr.16144")], extra={"ciphers/fx-cropman/images/manifest.json": man}))
code, out = run(r, "fx-cropman", "--item-spec", "item_id=c370;shelfmark=BnF fr.16144;canvas=370", "--step-type", "crop")
check("a crop entry in images/manifest.json (canvas from the source_url) makes a crop step DONE", code == 3 and "crop entry" in out, out)

# a unit with no folio: date-keyed own work is a LEAD (the fr3621 5/13 July lookup shape)
r = repo(target("fx-date", "Status: partial\nThe fr.3623 finding aid lists no Dinteville letters of 5 or 13 July 1592.\n",
                [item("j5", "BnF fr.3623", date="1592-07-05", sender="Dinteville", recipient="Nevers")]))
code, out = run(r, "fx-date", "--item", "j5", "--step-type", "lookup")
check("a lookup for a unit with no folio: a NOTES line naming its volume and date with 'lists no' -> LEAD", code == 4 and
      "date-keyed" in out, out)
check("... and Tomokiyo and the solver caches are UNCHECKED for a unit with no folio, never CLEAR",
      "UNCHECKED     3-tomokiyo" in out and "UNCHECKED     3-solver" in out and "CLEAR         3-tomokiyo" not in out, out)

# ---------------------------------------------------------------- 1. audit steps and attribution
audit3 = "# AUDIT\n\n| item | class |\n|---|---|\n| BnF fr.3040 f.18r no.6 | **N3** |\n"
r = repo(target("fx-aud3", extra={"ciphers/fx-aud3/AUDIT.md": audit3}))
code, out = run(r, "fx-aud3", "--item", "f18", "--step-type", "second-audit")
check("a second-audit on an N3 item is never DONE (Outreach gate 2)", code != 3, out)
code, out = run(r, "fx-aud3", "--item", "f18", "--step-type", "audit")
check("... while a plain audit on it is a re-audit (DONE)", code == 3, out)
th = ("# AUDIT\n\n## P2, P3, P5+P6 -- letters whose decipherment Birch printed\n\n| item | class | where |\n|---|---|---|\n"
      "| P5+P6 W. Stamford, Calais | **N0** | vol. 3 pp.275-276 |\n| E84 | **N1** | not the same telegram as E79 |\n\n"
      "## Postscript on P4, P5+P6\nClass **N0** unchanged for P5+P6; P4 keeps its caveat.\n")
r = repo(target("fx-thur", items=[item("P4"), item("E79"), item("P5")], extra={"ciphers/fx-thur/AUDIT.md": th}))
code, out = run(r, "fx-thur", "--item", "P4")
check("an AUDIT class row labelled P5+P6 (and a prose line under a two-unit heading) is not P4's", "audit classes" not in out, out)
code, out = run(r, "fx-thur", "--item", "E79")
check("an AUDIT row labelled E84 that mentions E79 is not E79's", "audit classes" not in out, out)
code, out = run(r, "fx-thur", "--item", "P5")
check("... and the P5+P6 row is P5's (KNOWN)", "audit classes" in out and code == 2, out)

# ---------------------------------------------------------------- 1. ROOM claims: target level, whole-token tags
room2 = ("# ROOM\n2026-10-08 14:00 | LANE B7 orchestrator | fx-rtag | claim fx-rtag: reference-strip blind eye read\n"
         "2026-10-08 15:00 | LANE C2 orchestrator | fx-rtag | done: unrelated\n")
r = repo(target("fx-rtag", extra={"ROOM.md": room2}))
code, out = run(r, "fx-rtag", "--item", "f18")
check("a target-level claim (slug, no unit) is a live claim; another LANE's done line does not clear it",
      code == 4 and "target-level" in out, out)
tomo_room = dict(tomo, **{"ROOM.md": "# ROOM\n2026-10-08 14:00 | R7 (account 2) | fx-ka | claim: read BnF fr.3040 f.18r\n"})
r = repo(target("fx-ka", extra=tomo_room))
code, out = run(r, "fx-ka", "--item", "f18", "--known-answer", "gate:key-check")
check("KNOWN with a consumer still exits 4 while someone else's live claim covers the item", code == 4 and "live-claim" in out, out)

# ---------------------------------------------------------------- 2. leaf: negation, depth lines, other letters, modal, paragraphs
r = repo(target("fx-bal", items=[item("b229", "BnF Baluze 170", "229r")], extra={"ciphers/fx-bal/AUDIT.md":
     "| item | print | gloss | class |\n|---|---|---|---|\n| Baluze 170 f.229r-v (bare cipher passage) | none located | "
     "none located: no interlinear gloss on the leaf; Tomokiyo quotes nothing from f.229; DECODE R2761 carries only the key | **N3** |\n"}))
code, out = run(r, "fx-bal", "--item", "b229")
check("'no interlinear gloss on the leaf' in the item's own AUDIT row -> CLEAR, never KNOWN", code != 2 and
      "CLEAR         2-leaf" in out and "KNOWN         2-leaf" not in out, out)
r = repo(target("fx-depth", items=[item("w4610")], extra={"ciphers/fx-depth/AUDIT.md":
     "- **WVO 4610 (Lodewijk van Nassau to Orange, 1573-74)**: **D2** (Partially decrypted; outward \"partially deciphered "
     "(about 63%)\"), 62.6% (C 2512 of 4012). Check: key aligned from the period decipherments of WVO 4613 and 4615 (C); "
     "0 regressions.\n"}))
code, out = run(r, "fx-depth", "--item-spec", "item_id=w4610;wvo=4610")
check("our own depth line, and a gloss of WVO 4613/4615 named beside WVO 4610, are not a KNOWN for WVO 4610",
      code != 2 and "KNOWN" not in out.replace("KNOWN-PART", ""), out)
r = repo(target("fx-nevf", "Status: partial\n- L05 run: sibling check (fr.4715 f.27r L09-L12) NON-TEST; f.35r itself "
                "already has four M tokens; the period gloss over fr.4715 f.27r L09 read by 2 blind passes: NON-TEST\n",
                [item("f35", "BnF fr.3416", "35r")]))
code, out = run(r, "fx-nevf", "--item", "f35")
check("'the period gloss over fr.4715 f.27r' in a line naming f.35r is not fr.3416 f.35r's", code != 2, out)
r = repo(target("fx-hel", items=[item("h1", decode="R1953")], extra={"ciphers/fx-hel/AUDIT.md":
     "The letters arrived before September and are not in the register. That makes a period decipherment of R1953 *more*\n"
     "likely to have existed, not less.\n"}))
code, out = run(r, "fx-hel", "--item", "h1")
check("a modal 'period decipherment of R1953 more likely to have existed' (hard-wrapped) is no KNOWN", code != 2, out)
viv = ("### 4. Classification\n**ink 54 (fr.16104 f.173r-v, 7 Sept 1572): N3** (plaintext and mapping). No prior plaintext, summary\n"
       "or decipherment of this letter located; a partial period decipherment exists on the leaf itself (8 legible\n"
       "interlinear fragments, about 60 letters), which our reading agrees with at its positions.\n")
r = repo(target("fx-viv", "Status: partial\n- fr.16104 inks 52, 53, 54 - blocker: not-attempted; no decipherment piece "
                "beside them; next: native crop of f.173r-v's interlinear words\n",
                [item("i54", "BnF fr.16104", "173r")], extra={"ciphers/fx-viv/AUDIT.md": viv}))
code, out = run(r, "fx-viv", "--item", "i54")
check("a hard-wrapped AUDIT paragraph under a label naming f.173r ('a partial period decipherment exists on the leaf "
      "itself') -> KNOWN-PART, exit 0", code == 0 and "KNOWN-PART    2-leaf" in out, out)
r = repo(target("fx-pos", "Status: partial\n- fr.16104 5 Sept 1572 cipher block (ff.157-159v) against its decipherment "
                "ff.162r-163r - blocker: not-attempted\n\n## SIBLINGS paste\n- fr.16104 ff.157-159v letter 5 Sept 1572 "
                "('sans le dechiffrement'; located) -- transcribe with key.tsv\n", [item("l5", "BnF fr.16104", "157r")],
                extra={"ciphers/fx-pos/AUDIT.md": "| BnF fr.16104 f.157r | no interlinear gloss on the leaf | **N3** |\n"}))
code, out = run(r, "fx-pos", "--item", "l5")
check("a decipherment on file outranks a later 'sans le dechiffrement' paste and an AUDIT 'no gloss' (KNOWN, conflict named)",
      code == 2 and "KNOWN         2-leaf" in out and "conflicting" in out, out)

# ---------------------------------------------------------------- 3. Tomokiyo volume-level and date-match; solver registry
tpage = ("<html><body><H4>BnF fr.16104</H4><P>The cipher used by Saint-Gouard in BnF fr.16104 can be read with the "
         "following cipher table.</P><P>Clinton to Haldimand, New York, 6 July 1780, decoded on p.186.</P></body></html>\n")
r = repo(target("fx-tvol", items=[item("i54", "BnF fr.16104", "173r")],
                extra={"sources/cryptiana/web/vol.htm": tpage,
                       "tools/data/prior_portals.tsv": "portal\tkind\tcache_paths\tsource\nunsolved-ciphers\tsolver-repo\t\tgithub\n"
                                                       "cyphersolver\tsolver-repo\tsources/cyphersolver\tgithub\n"}))
code, out = run(r, "fx-tvol", "--item", "i54")
check("a volume-level Tomokiyo line ('can be read with', no folio) -> KEY-SOURCE, not CLEAR",
      "KEY-SOURCE    3-tomokiyo" in out and "CLEAR         3-tomokiyo" not in out, out)
check("a registry solver repository with no cache and no --clone -> UNCHECKED-NET row (not silently CLEAR)",
      "registry:unsolved-ciphers" in open(os.path.join(r, "ciphers/fx-tvol/prior-work.tsv")).read() and
      "UNCHECKED-NET 3-solver" in out, out)
code, out = run(r, "fx-tvol", "--item-spec", "item_id=hc;shelfmark=TNA PRO 30/55/24/76;date=1780-07-06;sender=Clinton;recipient=Haldimand")
check("Tomokiyo 'Clinton to Haldimand, New York, 6 July 1780, decoded' -> LEAD date-match", "date-match" in out and code == 4, out)

# ---------------------------------------------------------------- 5. civil war: the real page shape and same-day entries
eck2 = dict(eck)
eck2["ciphers/eckert-1864/sources/mssEC18/p9714.json"] = ("copy", "huntington_p9714_text.json")
r = repo(dict(target("eckert-1864", items=[item("E78", ptr="9714/2", date="1864-04-21", sender="Meigs", recipient="Biggs",
                                               kind="ledger-entry"),
                                          item("X1", ptr="9714", date="1864-04-21", sender="Meigs", recipient="Biggs",
                                               kind="ledger-entry")]), **eck2), links)
code, out = run(r, "eckert-1864", "--item", "E78")
check("real page shape ('text' key, Beckwith's entry first): ptr 9714/2 -> KNOWN-PART on Sheldon's entry, exit 0",
      code == 0 and "KNOWN-PART" in out and "jennie" in out.lower() and "biscay" not in out.lower(), out)
code, out = run(r, "eckert-1864", "--item", "X1")
check("... ptr 9714 with two entries dated 21 Apr -> LEAD ambiguous entry, never KNOWN/KNOWN-PART",
      "ambiguous entry" in out and "KNOWN-PART" not in out and code == 4, out)
page = {"title": "Page 75 (fixture)", "transc": "Jno Horner  Washn May 21st 1864 10 am\nJennie Wick Belcher\n\n"
        "J. C. Van Duzer Nashville  Wash'n May 21st 1864 10 AM\nPersia Animal Yoke stop\n"}
ct = "### E91 | Page 75 | 8967 | 21 May 1864 10 AM, to H. S. Sanford (operator Jno Horner; LS4-R1a, row 8967/0)\n1 2 3\n"
eck3 = dict(eck, **{"ciphers/eckert-1864/sources/mssEC19/p8967.json": json.dumps(page), "ciphers/eckert-1864/ciphertext.txt": ct})
r = repo(dict(target("eckert-1864", items=[item("Z1", ptr="8967/1", date="1864-05-21", sender="Halleck", recipient="Thomas",
                                               kind="ledger-entry"),
                                          item("Z0", ptr="8967/0", date="1864-05-21", sender="Halleck", recipient="Sanford",
                                               kind="ledger-entry")]), **eck3), links)
code, out = run(r, "eckert-1864", "--item", "Z1")
check("a block read as row 8967/0 does not make the same-day entry 8967/1 DONE", code != 3 and "already read as E91" not in out, out)
code, out = run(r, "eckert-1864", "--item", "Z0")
check("... but makes 8967/0 itself DONE", code == 3 and "already read as E91" in out, out)

# ---------------------------------------------------------------- records survive edits; a false KNOWN can be recorded
r = repo(target("fx-rec", "Status: partial\n- [x] transcribe: BnF fr.3040 f.18r lines 1-10; lines 11-20 remain\n"))
code, out = run(r, "fx-rec", "--item", "f18", "--step-type", "transcribe")
lead = [l.split()[3].strip("[]") for l in out.splitlines() if " LEAD " in l and "1-own" in l][0]
run(r, "fx-rec", "--record", lead, "CLEAR: lines 11-20 still owed; this job does them")
open(os.path.join(r, "ciphers/fx-rec/NOTES.md"), "w").write(
    "Status: partial\n\n## inserted later\nline\n- [x] transcribe: BnF fr.3040 f.18r lines 1-10; lines 11-20 remain\n")
subprocess.run(["git", "-C", r, "-c", "user.email=t@example.org", "-c", "user.name=t", "commit", "-qam", "edit"], check=True)
subprocess.run(["git", "-C", r, "update-ref", "refs/remotes/origin/main", "HEAD"], check=True)
code, out = run(r, "fx-rec", "--item", "f18", "--step-type", "transcribe")
check("an answer given with --record survives lines inserted above the bullet (row id from the text, not the line)",
      "recorded" in out, out)
r = repo(target("fx-gloss3", "Status: open\nf.18r (BnF fr.3040) carries an interlinear period decipherment of this letter.\n"))
code, out = run(r, "fx-gloss3", "--item", "f18")
krow = [l.split()[3].strip("[]") for l in out.splitlines() if "KNOWN         2-leaf" in l][0]
run(r, "fx-gloss3", "--record", krow, "CLEAR: the line is about the next letter; the leaf carries no gloss (seen 8 Oct)")
code, out = run(r, "fx-gloss3", "--item", "f18")
check("--record can answer a false KNOWN (CLEAR), and the next run proceeds", code == 0 and "recorded" in out, out)
before = open(os.path.join(r, "ciphers/fx-gloss3/prior-work.tsv")).read()
run(r, "fx-gloss3", "--record", krow, "KNOWN: changed my mind", "--dry-run")
check("--record --dry-run writes nothing", open(os.path.join(r, "ciphers/fx-gloss3/prior-work.tsv")).read() == before)

# ---------------------------------------------------------------- --brief: per-item exits
r = repo(target("fx-brief", "Status: partial\n- [x] transcribe: BnF fr.3040 f.18r, two blind passes reconciled (5 Oct 2026)\n"
                "f.40r (BnF fr.3040): no interlinear gloss on the leaf (checked 5 Oct 2026).\n",
                [item("f18", "BnF fr.3040", "18r"), item("f40", "BnF fr.3040", "40r"), item("f50", "BnF fr.3040", "50r")]))
b1 = os.path.join(r, "b1.md")
open(b1, "w").write("Transcribe BnF fr.3040 f.18r and BnF fr.3040 f.40r.\n")
code, out1 = run(r, "fx-brief", "--brief", b1, "--step-type", "transcribe")
check("--brief with one DONE item and one that proceeds -> exit 5 (mixed), with a per-item table",
      code == 5 and "per-item exits" in out1 and "f18\texit 3" in out1 and "f40\texit 0" in out1, out1)
open(b1, "w").write("Transcribe BnF fr.3040 f.18r and BnF fr.3040 f.50r.\n")
code, out = run(r, "fx-brief", "--brief", b1, "--step-type", "transcribe")
check("--brief with one DONE item and one owing a look -> exit 4, not 3", code == 4 and "f50\texit 4" in out, out)
check("rule 10: an exit-4 and an exit-0 run print no novelty word",
      all(" first" not in o.lower() and not re.search(r"\bN[0-5]\b", o) for o in (out, out1)), out + out1)

# prior_portals.tsv is append-only: a correction row with the same portal id replaces the earlier one
r = repo(target("fx-portal", extra=dict(tomo, **{"tools/data/prior_portals.tsv":
         "portal\tkind\tcache_paths\nsrc\ttomokiyo\tsources/nowhere\nsrc\ttomokiyo\tsources/cryptiana/web\n"})))
code, out = run(r, "fx-portal", "--item", "f18")
check("prior_portals.tsv: the last row per portal id wins (the correction's cache path is read)",
      "KNOWN         3-tomokiyo" in out and "not on disk" not in out, out)

# ---------------------------------------------------------------- look.tsv is append-only and file_shrink_guard passes
r = repo(target("fx-look", "Status: open\n"))
code, out = run(r, "fx-look", "--item", "f18")
g = ["git", "-C", r, "-c", "user.email=t@example.org", "-c", "user.name=t"]
subprocess.run(g + ["add", "-A"], check=True)
subprocess.run(g + ["commit", "-qm", "look"], check=True)
lrow = [l.split()[3].strip("[]") for l in out.splitlines() if "LOOK          2-leaf" in l][0]
n0 = open(os.path.join(r, "ciphers/fx-look/look.tsv")).read().count("\n")
run(r, "fx-look", "--record", lrow, "CLEAR: f.18r, f.17v, f.19r read at native size, no gloss")
code, out = run(r, "fx-look", "--item", "f18")
lk = open(os.path.join(r, "ciphers/fx-look/look.tsv")).read()
check("after --record answers the LOOK, look.tsv keeps every owed row and appends 'answered' rows",
      lk.count("\n") > n0 and lk.count("\towed\n") == n0 - 2 and "answered CLEAR" in lk, lk[-400:])
fsg = subprocess.run([sys.executable, os.path.join(REPO, "tools", "file_shrink_guard.py"), "ciphers/fx-look/look.tsv",
                      "--root", r], capture_output=True, text=True)
check("tools/file_shrink_guard.py passes on look.tsv after the answer", fsg.returncode == 0, fsg.stdout + fsg.stderr)

# ---------------------------------------------------------------- offline reuse is per route; one Net per run
r = repo(target("fx-g3r", items=[item("t3", date="1864-04-24", sender="H. W. Halleck", recipient="C. C. Augur")]))
rd = os.path.join(r, "reading.txt")
open(rd, "w").write("The cavalry at Warrenton Junction will move at daylight with 350 men toward Bealeton Station.\n")
code, out = run(r, "fx-g3r", "--item", "t3", "--reading", rd, "--json", "--dry-run")
rows = json.loads(out.splitlines()[0])["rows"]
ids = {x["route"]: x["row_id"] for x in rows if x["check"] == "6-g3"}
pwt = os.path.join(r, "ciphers/fx-g3r/prior-work.tsv")
with open(pwt, "w") as f:
    f.write("\t".join(pw.COLUMNS) + "\n")
    for route, v in (("net:ia-global", "LEAD"), ("net:gbooks", "CLEAR")):
        f.write("\t".join({"utc": "2026-10-08 15:00", "item_id": "t3", "scope": "plaintext", "check": "6-g3", "route": route,
                           "evidence": f"{route} fixture", "verdict": v, "requests_by_host": "stub:1",
                           "valid_until": "2026-10-22", "row_id": ids[route]}.get(c, "") for c in pw.COLUMNS) + "\n")
code, out = run(r, "fx-g3r", "--item", "t3", "--reading", rd)
check("an offline G3 run reuses each network route's own row (ia-global LEAD stays LEAD, gbooks CLEAR stays CLEAR)",
      any(" LEAD " in l and "net:ia-global" in l or (" LEAD " in l and "ia-global fixture" in l) for l in out.splitlines())
      and code == 4, out)


r = repo(target("fx-ed8", items=[item("t1", date="1864-04-23", sender="H. W. Halleck", recipient="C. C. Augur")],
                extra={"tools/data/prior_editions.tsv": eds + row2.format("1864-04-21", "Butler", "Fox")
                       .replace("fx-ed*", "fx-ed8").replace("notcached99\tdjvu", "notcached99 notcached98\tdjvu")}))
pwt = os.path.join(r, "ciphers/fx-ed8/prior-work.tsv")
with open(pwt, "w") as f:
    f.write("\t".join(pw.COLUMNS) + "\n")
    f.write("\t".join({"utc": "2026-10-08 15:00", "item_id": "t1", "scope": "plaintext", "check": "4-editions",
                       "route": "net:ia:notcached99", "evidence": "fixture", "verdict": "CLEAR", "requests_by_host": "stub:1",
                       "valid_until": "2026-10-22", "row_id": pw.rid_of("t1", "4-editions", "net:ia:notcached99", "")}.get(c, "")
                      for c in pw.COLUMNS) + "\n")
code, out = run(r, "fx-ed8", "--item", "t1")
check("an offline row standing for two volumes is not answered by a cached row for one of them",
      "UNCHECKED-NET 4-editions" in out and "cached network rows" not in out, out)


class BlockNet:
    """print_check.Net's semantics: a 429 marks the host blocked and later requests to it are skipped, not sent."""
    seen = []

    def __init__(self, offline, max_requests, delay=1.5):
        self.count, self.status, self.offline = {}, {}, offline
        BlockNet.seen.append(self)

    def get(self, url, **kw):
        host = url.split("/")[2]
        if host in self.status:
            return None, self.status[host]
        self.count[host] = self.count.get(host, 0) + 1
        self.status[host] = "blocked: HTTP 429"
        return None, self.status[host]

    def json(self, url, **kw):
        return self.get(url)


real_net, pw.pc.Net = pw.pc.Net, BlockNet
r = repo(target("fx-ed7", items=[item("t1", "BnF fr.3040", "18r", date="1864-04-23", sender="H. W. Halleck", recipient="C. C. Augur"),
                                 item("t2", "BnF fr.3040", "40r", date="1864-04-25", sender="H. W. Halleck", recipient="C. C. Augur")],
                extra={"tools/data/prior_editions.tsv": eds + row2.format("1864-04-21", "Butler", "Fox").replace("fx-ed*", "fx-ed7")}))
b2 = os.path.join(r, "b2.md")
open(b2, "w").write("Read BnF fr.3040 f.18r and BnF fr.3040 f.40r.\n")
code, out = run(r, "fx-ed7", "--brief", b2, "--network", "--cache", CACHE)
pw.pc.Net = real_net
check("one Net for the whole run: a host that answered 429 on item 1 is not asked again on item 2",
      len(BlockNet.seen) == 1 and BlockNet.seen[0].count.get("archive.org") == 1, [n.count for n in BlockNet.seen])

# ---------------------------------------------------------------- paths: restricted material is never read or sent
r = repo(target("debosnys-1883", items=[item("c1", date="1883-05-01", sender="Debosnys", recipient="nobody")],
                extra={"ciphers/debosnys-1883/RESTRICTED.md": "# RESTRICTED\n"}))
os.makedirs(os.path.join(r, "ciphers/debosnys-1883/restricted"), exist_ok=True)
secret = os.path.join(r, "ciphers/debosnys-1883/restricted/reading.txt")
open(secret, "w").write("Zebulon Quartermaine crossed the Ausable River at Keeseville with Philomena.\n")
code, out = run(r, "debosnys-1883", "--item", "c1", "--reading", secret)
check("--reading under a restricted/ folder is refused (exit 1), nothing written",
      code == 1 and not os.path.isfile(os.path.join(r, "ciphers/debosnys-1883/prior-work.tsv")), out)
code, out = run(r, "debosnys-1883", "--item", "c1", "--clone", os.path.join(r, "ciphers/debosnys-1883/restricted"))
check("--clone into a restricted/ folder is refused (exit 1)", code == 1, out)
pub = os.path.join(CACHE, "reading-copy.txt")
open(pub, "w").write(open(secret).read())
code, out = run(r, "debosnys-1883", "--item", "c1", "--reading", pub, "--network", "--cache", CACHE)
check("a folder with RESTRICTED.md: --reading with --network is refused (exit 1)", code == 1, out)
code, out = run(r, "debosnys-1883", "--item", "c1", "--reading", pub)
tsv = open(os.path.join(r, "ciphers/debosnys-1883/prior-work.tsv")).read()
check("... and offline, decoded phrases reach prior-work.tsv only as hashes", "sha1:" in tsv and "Quartermaine" not in tsv
      and "Keeseville" not in tsv, tsv[-500:])

# ---------------------------------------------------------------- inputs that used to crash
r = repo(target("eckert-1864", items=[], extra={"WORK-QUEUE.tsv": BASE["WORK-QUEUE.tsv"] + "J1\towner\tb.md\tS\t3\t30\tdone\textra\tcells\there\n"}))
code, out = run(r, "eckert-1864", "--item-spec", "item_id=pp;ptr=p9714;kind=ledger-entry")
check("ptr=p9714 with no folio and a ragged WORK-QUEUE row: no traceback (exit 0/2/3/4)", code in (0, 2, 3, 4), out)
code, out = run(r, "eckert-1864", "--item-spec", "item_id=bad;date=1530-02-30")
check("an impossible date is a usage error (exit 1), not a traceback", code == 1, out)

# ---------------------------------------------------------------- register: autodetected columns, verb class, real lines
sib = ("target\tsibling\trelation\tcheap_step\n"
       "fx-sib\tBnF fr.3040 f.18r\tsame-volume\tfetch the image of BnF fr.3040 f.18r and eyeball it\n"
       "fx-sib\tBnF fr.3040 f.18r\tsame-volume\ttranscribe BnF fr.3040 f.18r with two blind passes\n")
files = target("fx-sib", "Status: partial\n- [x] transcribe: BnF fr.3040 f.18r, two blind passes reconciled (5 Oct 2026)\n")
files["SIBLINGS-fixture.tsv"] = "# comment line\n" + sib
r = repo(files)
code, out = run(r, "-", "--register", os.path.join(r, "SIBLINGS-fixture.tsv"))
lines = [l.split("\t") for l in out.splitlines() if l[:1].isdigit()]
check("--register autodetects SIBLINGS' sibling,cheap_step columns (no 'empty step cells')", "empty step cells" not in out
      and "sibling,cheap_step" in out, out)
check("... a fetch step is not DONE from a transcribe bullet (LEAD), the transcribe step is DONE, at real file lines",
      [(x[0], x[2]) for x in lines] == [("3", "LEAD"), ("4", "DONE")], out)

# ---------------------------------------------------------------- survivor shapes from the 45-case replay (must NOT block)
surv = [
    ("S05", "item_id=w4610;wvo=4610",
     "All six letters (4610, 4611, 4612, 4616 targets; 4613, 4615 siblings) now fetched in full; both siblings' contemporary\n"
     "decipherments (4613 p2, 4615 p3) are each on a separate sheet in the same file, not interlinear.\n"),
    ("S07", "item_id=w126;wvo=126",
     "- **System B (98, f.66, 1563; the same system reads 126, 1564)**: a different key. **Its decipherment is f.67 (p3), "
     "not ff.68-69.** The contemporary decipherments of the siblings are the key sources for 57 and 126.\n"),
    ("S08", "item_id=n86;shelfmark=BnF fr.3251;folio=174r",
     "- **BnF fr.3251 ff.174r-175v (no.86), Birago to Nevers, 27 Aug 1572**: Check: published 1572 key (Tomokiyo), "
     "calibrated against the period decipherment of no.87 (84% letter agreement).\n"),
    ("S09", "item_id=P4",
     "## Remaining gaps\n- A contemporary decipherment of P4 (Thurloe's office or Eric Sams's 1973 notes) - blocker: waiting-on "
     "ASKS row 139; ASKS row 30's Bodleian reply did not locate P4's leaf\n"),
    ("S11", "item_id=f130;shelfmark=BnF fr.3621;folio=130r;decode=R9451",
     "**Safe sentence:** \"A key that we rebuilt from the contemporary decipherment on Dinteville's letter of 1 July 1592 (BnF\n"
     "fr.3621 f.128) reads the two cipher passages of his letter of 4 July 1592 (f.130) far better than chance.\"\n"),
    ("S13", "item_id=c349;shelfmark=Melanges de Colbert 127;folio=349;decode=R2678",
     "| Gravel to Colbert, 23 Apr 1672 | Mél. Colbert 159 f.102r | **Two-digit groups** with overlines, a contemporary "
     "**interlinear decipherment** over nearly every cipher line: the same design class as R2678 |\n\n"
     "Next (one line each, not done here): (1) cheapest: read f.102r-v's interlinear decipherment into a key with\n"
     "`tools/interlinear_align.py` and test it on R2678.\n"),
    ("S15", "item_id=h1;decode=R1953",
     "- codes 1-800 of the Hellen key (374 R1953 tokens) - blocker: not-attempted; no 1751 Hellen ciphertext survives beside "
     "Fagel 5177's clear copies, so that volume gives context, not code values\nSupporting: 37% of Michell's glossed tokens "
     "are above 1732, R1953 has 1 of 836 there.\n"),
]
for case, spec, notes in surv:
    slug = "fx-" + case.lower()
    r = repo(target(slug, "Status: partial\n" + notes, items=[]))
    code, out = run(r, slug, "--item-spec", spec)
    check(f"survivor shape {case}: no KNOWN from a sibling's, a calibration's, a sought or a planned gloss",
          code != 2 and "KNOWN         2-leaf" not in out, out)

print(f"\n{'all passed' if not fails else f'{fails} FAILED'}")
sys.exit(1 if fails else 0)
