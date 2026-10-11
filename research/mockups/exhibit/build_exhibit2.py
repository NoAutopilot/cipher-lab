#!/usr/bin/env python3
"""Build the EXHIBIT-2 private mock-up: three displays chosen in SELECTION.md by what the audited reading itself says.

Usage: python3 research/mockups/exhibit/build_exhibit2.py
Writes research/mockups/exhibit/{index2,washington-1864,breda-torgau-1561,berlin-1712}.html (images by relative path) and
research/mockups/exhibit-2026-10-09b.html (all three; crops embedded, portraits by relative path). Reading tokens and grades
are read from the targets' committed token files at build time; nothing under ciphers/ is written. Headlines and "the
reading says" panels quote each item's status.json depth sentence or AUDIT.md safe sentence; context is labelled context.
Portraits: every face is an <img> at portraits/<file> from portraits/manifest.tsv over a labelled silhouette; dropping the
files into portraits/ fills the faces without a rebuild (the img removes itself when the file is missing).
EXHIBIT-1 (build_exhibit.py, exhibit-2026-10-09.html) is left untouched; its CSS and helpers are reused.
"""
import base64, csv, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_exhibit as B  # noqa: E402  (CSS, JS, tok_html, legend, map_svg, silhouette)

ROOT, HERE, REPO, TREE, E = B.ROOT, B.HERE, B.REPO, B.TREE, B.E
tsv = B.tsv


# ---------------------------------------------------------------- reading tokens (read, never written)
def august_lines(job):
    out = {}
    for r in tsv(f"ciphers/august-van-saksen-1561-64/reading_tokens_{job}.tsv"):
        out.setdefault(r["line"], []).append((r["value"], r["grade"], r["sign"]))
    return out


def mant0391():
    rows = {}
    for r in tsv("ciphers/sachsstaatsarchiv-manteuffel-1712/f0390_08/reading_tokens.tsv"):
        if "_0391_" in r["line"]:
            rows.setdefault(r["line"].split("_")[-1], []).append(r)
    return rows


def eckert_counts():
    """Grade counts for E46's code words, from the committed reading (H 9)."""
    txt = open(os.path.join(ROOT, "ciphers/eckert-1864/reading.md")).read()
    i = txt.index("**E46 |")
    seg = txt[i:txt.index("**E47 |")]
    line = [l for l in seg.splitlines() if l.startswith("Code-word tokens:")][0]
    return [(g.strip().split()[0], int(g.strip().split()[1])) for g in line.split(":", 1)[1].rstrip(".").split(",")]


A57, A53, M91 = august_lines("57"), august_lines("53"), mant0391()
EC = eckert_counts()


def mtok(row):
    """Manteuffel run as (value, grade, sign) tokens; a multi-sign run keeps one token per sign."""
    names = {"la reine d'Angleterre": "la reine d'Angleterre", "Hannover|Electeur de Hanovre": "l'Electeur de Hanovre",
             "le roi de Danemark|Danemark": "le roi de Danemark", "Le roi de Prusse": "le roi de Prusse"}
    out = []
    for r in row:
        v = names.get(r["value"], r["value"])
        if r["value"] == "Manteuffel":  # 160 as transcribed; the reader's own note: 100 = d by sense
            v = "[160]"
        out.append((v, r["grade"], r["sign"]))
    return out


def clear(s):
    return [(w, "clear", "") for w in [s]]


def ek(words):
    """Eckert ledger line: 'word' clear, ('code', 'value') a code word read at H, ('code', None) unread."""
    out = []
    for w in words:
        if isinstance(w, tuple):
            c, v = w
            out.append((v, "H", c) if v else ("", "U", c))
        else:
            out.append((w, "clear", ""))
    return out


# ---------------------------------------------------------------- content
NCLASS = dict(B.NCLASS)
DCLASS = dict(B.DCLASS, D3="Largely deciphered: at least 80% of the cipher tokens read at firm grades, the gaps mostly names "
                           "or codes, with an external check or a matched control.")

DISPLAYS = [
  dict(
    slug="washington-1864", short="Washington, 1864", kicker="Washington · 30 November 1864",
    title="“Send on a man to identify him”: a telegram about the plot to burn New York",
    headline="A War Department telegram in the Union's code tells New York's police chief that a man believed to be the "
             "chief conspirator in the attempt to burn New York is in the Old Capitol Prison, and asks him to send someone "
             "to identify him.",
    says="Kennedy, New York's police superintendent, is told that a man believed to be the chief conspirator of the attempt "
         "to burn New York, as described in Monday's Evening Post, is in the Old Capitol Prison, and asked to send someone to "
         "identify him.",
    page=("img/eckert_p9130_page.jpg", "The War Department telegraph's ledger copy, page 236: the telegram of 30 November 1864 "
          "is the lower entry. Huntington Library, Thomas T. Eckert Papers, mssEC 19 (item 9130)."),
    lines=[
      ("img/eckert_E46_L1.jpg", ek([("Gertrude", "12.30"), ("Lamp", "30"), "for", "Mr", "Kennedy", "Supt", "Police"]),
       "[12.30] [30th] for Mr Kennedy Supt Police", "12.30 p.m., the 30th. For Mr Kennedy, Superintendent of Police,"),
      ("img/eckert_E46_L2.jpg", ek([("frog", "New York"), "A", "man", "believed", "toby", "the", "man"]),
       "[New York] A man believed toby the man", "New York. A man believed to be the man"),
      ("img/eckert_E46_L3.jpg", ek(["described", ("sligo", "In the"), ("france", "New York"), "evening", ("upton", "Post"),
                                    "of", "Monday"]),
       "described [in the] [New York] evening [Post] of Monday", "described in the New York Evening Post of Monday"),
      ("img/eckert_E46_L4.jpg", ek(["as", "bring", "the", "chief", "conspirator", "forth", "burning"]),
       "as bring the chief conspirator forth burning", "as being the chief conspirator for the burning"),
      ("img/eckert_E46_L5.jpg", ek(["of", ("france", "New York"), "is", ("stephen", "In the"), "old", "capital", "prison"]),
       "of [New York] is [in the] old capital prison", "of New York is in the Old Capitol Prison."),
      ("img/eckert_E46_L6.jpg", ek(["send", "on", "a", "man", "to", "identify", "him"]),
       "send on a man to identify him", "Send on a man to identify him."),
      ("img/eckert_E46_L7.jpg", ek([("youth", "[signature]"), ("M", None), ("wise", None), ("well", None), ("wily", None), "Govr", "&c"]),
       "[signature] … Govr &c", "Signed: four code words we have not read, then “Govr &c”."),
    ],
    lang="English", intro_note="The ledger copies the telegram word for word. Ordinary words travel as written; the code "
                               "words (a frog, a town in Ireland, a country) stand for places, times and phrases.",
    companions=[("7 Nov 1864, Dana to Wallace, Baltimore (N3, D3, 100%)",
                 "Dana tells Wallace at Baltimore that a rebel agent calling himself Dr Hamilton passed through Elmira going south "
                 "on Thursday last, six feet two, with light hair, moustache and whiskers and fine teeth, and to catch him."),
                ("26 May 1864, the War Department to Dix, New York (N3, D3, 96.4%)",
                 "On 26 May 1864 the War Department warned General Dix at New York of a rebel plot to seize a steamer on the "
                 "New York-New Orleans line and described three suspects who had come from Havana.")],
    faces=[("Edwin M. Stanton", "Lincoln's Secretary of War", "his office sends the ledger's telegrams", "stanton.jpg"),
           ("Thomas T. Eckert", "chief of the War Department telegraph", "his clerks keep this ledger", "eckert.jpg"),
           ("John A. Kennedy", "New York's superintendent of police", "the telegram is to him", "kennedy.jpg"),
           ("Charles A. Dana", "Assistant Secretary of War", "sends the Dr Hamilton telegram", "dana.jpg"),
           ("Lew Wallace", "commanding at Baltimore", "told to catch Dr Hamilton", "wallace.jpg"),
           ("John A. Dix", "commanding at New York", "warned of the steamer plot", "dix.jpg")],
    moment=[("8 Nov 1864", "Lincoln is re-elected."),
            ("25 Nov 1864", "Confederate agents set fires in about a dozen New York hotels and at Barnum's Museum; most are put out."),
            ("28 Nov 1864", "The New York Evening Post describes the plot's chief conspirator (reprinted in the Washington "
                            "Evening Star, 29 Nov)."),
            ("30 Nov 1864", "12.30 p.m.: the telegram to Superintendent Kennedy, in code."),
            ("25 Mar 1865", "Robert C. Kennedy, one of the arsonists (no relation), is hanged at Fort Lafayette.")],
    this=3,
    places=[("Washington", -77.04, 38.9, "the telegram is sent"), ("New York", -74.0, 40.71, "Kennedy; the fires"),
            ("Elmira", -76.81, 42.09, "Dr Hamilton seen")],
    trial=[("", "frog", "New York", "H", "War Dept Cipher No. 1, p.14"),
           ("", "sligo", "in the", "H", "War Dept Cipher No. 1, p.21"),
           ("", "upton", "Post", "H", "War Dept Cipher No. 1, p.22")],
    proof=dict(n="N3", d="D3", pct="100", audits=["8 Oct 2026 (first audit)", "8 Oct 2026 (second, adversarial)"],
               counts=EC, total=sum(n for _, n in EC), unit="code words",
               key="Period key: the War Department's own Cipher No. 1 book (Huntington, Eckert Papers, mssEC 41), applied word "
                   "for word. The plain words of the telegram are written in clear in the ledger.",
               links=[("Audit and search log", REPO + "ciphers/eckert-1864/AUDIT.md"),
                      ("Reading (regenerate: decode.py --check)", REPO + "ciphers/eckert-1864/reading.md"),
                      ("Folder", TREE + "ciphers/eckert-1864")],
               safe="Read at grade H with the period Cipher No. 1 book; no prior plaintext or decipherment of this telegram "
                    "located after a logged search (the Post's description it cites is in print; the prisoner is not located)."),
    holder=[("The ledger page at the Huntington Library (mssEC 19, page 236, digital item 9130)",
             "https://hdl.huntington.org/digital/collection/p16003coll11/id/9130")],
    credit=[("Ledger page and line crops", "The Huntington Library, San Marino, Thomas T. Eckert Papers, mssEC 19, page 236 "
             "(digital item 9130, hdl.huntington.org).", "Reuse terms not recorded in the repository; to be checked with the "
             "Huntington before any publication. Private mock-up only.")],
  ),
  dict(
    slug="breda-torgau-1561", short="Breda & Torgau, 1561", kicker="Torgau · 18 November 1561",
    title="An Elector's secret, told in signs: the Emperor wants Maximilian elected now",
    headline="In cipher, Elector August of Saxony tells William of Orange that the Emperor has asked him, through a formal "
             "embassy, to elect his son Maximilian King of the Romans in the Emperor's own lifetime, and asks him to keep it "
             "secret.",
    says="August tells Orange in confidence that the Emperor has recently, through a formal embassy, asked him to elect his son "
         "Maximilian King of the Romans in the Emperor's own lifetime, and that the other Electors will be asked the same. "
         "The approach itself is well known to historians; what we have not located in print (N4: no prior decipherment "
         "located) is this letter's own report of it.",
    page=("img/avs57_page.jpg", "August to Orange, Torgau, 18 November 1561: "
          "the cipher enclosure. Koninklijk Huisarchief, A 11/XIV B/41-6, as served by the Huygens Institute (WVO 57)."),
    lines=[
      ("img/avs57_L01.jpg", A57["57_L01"], "auff freundtlich hochuertrawen wollen [wir] [E.L.] nitt",
       "In friendly, high confidence we will not [hide from] Your Grace"),
      ("img/avs57_L02.jpg", A57["57_L02"], "bergen, das der [Keiser] fur wenig tagen durch seine estadtliche",
       "that the Emperor a few days ago, through his stately"),
      ("img/avs57_L03.jpg", A57["57_L03"], "gesanndthenn bei uns suchen lasen, seinen sohn [König] Max-",
       "envoys, had us asked [to elect] his son, King Max-"),
      ("img/avs57_L04.jpg", A57["57_L04"], "imilianum noch bei seinem, des [Keiser]s, leben [zu] eiem romischen",
       "imilian, still in the Emperor's own lifetime, as Roman"),
      ("img/avs57_L05.jpg", A57["57_L05"], "[König]e [zu] erwelen. konnen erachten, solchs werde bei den an-",
       "King. We judge that the same will be asked of the"),
      ("img/avs57_L06.jpg", A57["57_L06"], "dern [Churfurs]ten gleichergestalt auch gesucht werden, welchs",
       "other Electors in the same way; which"),
      ("img/avs57_L07.jpg", A57["57_L07"], "[E.L.] bei sich inn geheim werden [zu] halten wisen",
       "Your Grace will know how to keep secret to yourself."),
    ],
    lang="German", intro_note="Each sign is a letter; a few signs stand for whole words (Emperor, King, Elector, Your Grace).",
    second=dict(
        title="A month earlier, the other way: Orange to August, Breda, 24 October 1561 (WVO 53)",
        says="Orange's cipher postscript reports news that the Prince of Spain is to marry his father's sister and come to "
             "govern these lands, and that the Duke of Vendome wants to recover his kingdom of Navarre by fair means or war. "
             "The rumours themselves are in print; this is Orange passing them on in cipher.",
        caution="A proposed reading from a key we recovered by cryptanalysis (no key sheet survives): every sign is graded S, "
                "a result checked against a matched control, not read from a key source.",
        lines=[("img/avs53_L03.jpg", A53["53_L03"], "dan das dem printzen zu hispanien", "than that the Prince of Spain"),
               ("img/avs53_L04.jpg", A53["53_L04"], "seines hern uatters schuuester", "[is to marry] his lord father's sister"),
               ("img/avs53_L05.jpg", A53["53_L05"], "ehlich uermahlet uuerden und hieruber", "in wedlock, and thereupon"),
               ("img/avs53_L06.jpg", A53["53_L06"], "diesse lande zu uregieren khomen sollen", "come to govern these lands"),
               ("img/avs53_L08.jpg", A53["53_L08"], "uuolle der hertzog uon uandosmen", "[that] the Duke of Vendôme wants"),
               ("img/avs53_L09.jpg", A53["53_L09"], "sein konigreich nauarra mit der", "his kingdom of Navarre, with"),
               ("img/avs53_L10.jpg", A53["53_L10"], "gute oder krig uuiederholen", "fair means or war, to win back")],
        proof="N4 · D3 · about 97.8% · key ours (cryptanalytic) · S 356, M 8 of 364 signs"),
    faces=[("William of Orange", "prince of Orange, stadholder", "writes 53; receives 57", "orange.jpg"),
           ("August of Saxony", "Elector, Orange's new kinsman", "writes 57 from Torgau", "august.jpg"),
           ("Ferdinand I", "Holy Roman Emperor", "his embassy asks for the vote", "ferdinand.jpg"),
           ("Maximilian", "Ferdinand's son, King of Bohemia", "the King of the Romans to be", "maximilian.jpg"),
           ("Don Carlos", "Prince of Spain", "the rumoured bridegroom in 53", "carlos.jpg"),
           ("Antoine de Bourbon", "Duke of Vendôme, of Navarre", "wants Navarre back (53)", "vendome.jpg")],
    moment=[("24-25 Aug 1561", "Orange marries Anna of Saxony, the Elector's niece, at Leipzig: the families are now allied."),
            ("24 Oct 1561", "From Breda, Orange sends August the Spanish and Navarre rumours in cipher (WVO 53)."),
            ("18 Nov 1561", "From Torgau, August sends Orange the Emperor's request in cipher (WVO 57)."),
            ("24 Nov 1562", "At Frankfurt the Electors choose Maximilian King of the Romans; he is crowned on 30 November.")],
    this=2,
    places=[("Torgau", 13.0, 51.56, "August writes 57"), ("Breda", 4.78, 51.59, "Orange writes 53"),
            ("Vienna", 16.37, 48.21, "the Emperor"), ("Frankfurt", 8.68, 50.11, "the election, 1562")],
    trial=[("img/avs_sign_EL.jpg", "", "E.L. (Your Grace)", "C", "Orange's 1562 key, from a period decipherment"),
           ("img/avs_sign_VmV.jpg", "", "König (King)", "C", "Orange's 1562 key"),
           ("img/avs_sign_ZZ.jpg", "", "zu", "C", "Orange's 1562 key")],
    proof=dict(n="N4", d="D3", pct="97.7", audits=["24 Sept 2026 (first audit)", "24 Sept 2026 (second, adversarial); class kept on later checks"],
               counts=[("C", 294), ("M", 7)], total=301, unit="cipher signs",
               key="Period key: the key of Orange's 1562 cipher, rebuilt from the contemporary decipherment on a sibling letter "
                   "(WVO 74). WVO 53's key is ours, recovered by cryptanalysis.",
               links=[("Audit and search log", REPO + "ciphers/august-van-saksen-1561-64/AUDIT.md"),
                      ("Reading of 57 (regenerate: decode_key.py --check)", REPO + "ciphers/august-van-saksen-1561-64/reading_57.txt"),
                      ("Reading of 53 and its matched control", REPO + "ciphers/august-van-saksen-1561-64/reading_53.txt"),
                      ("Folder", TREE + "ciphers/august-van-saksen-1561-64")],
               safe="The cipher enclosure of Elector August's letter to Orange, Torgau 18 Nov 1561, reads with the key of "
                    "Orange's 1562 cipher as secret news that the Emperor had asked August to elect Maximilian King of the "
                    "Romans. No prior decipherment or printed plaintext located; Demandt's regest summarises only the clear "
                    "text; August's minute in Dresden has not been seen."),
    holder=[("WVO 57 as served by the Huygens Institute (PDF)", "https://resources.huygens.knaw.nl/media/wvo/images/00000-00999/00057.pdf"),
            ("WVO 53 as served by the Huygens Institute (PDF)", "https://resources.huygens.knaw.nl/media/wvo/images/00000-00999/00053.pdf")],
    credit=[("Page and line crops", "Koninklijk Huisarchief, The Hague (WVO 57), and Sächsisches Hauptstaatsarchiv Dresden, "
             "Loc. 9941/3 f.266 (WVO 53), as served by the Huygens Institute, Briefwisseling van Willem van Oranje.",
             "Reuse terms not recorded in the repository; to be checked before any publication. Private mock-up only.")],
  ),
  dict(
    slug="berlin-1712", short="Berlin, 1712", kicker="Berlin · 13 October 1712",
    title="Names in cipher: who in London said what about the war in the North",
    headline="Manteuffel's postscript is in clear French; what he put in cipher are the names. Read, they make the report "
             "say that Oxford called the Queen too far off to meddle in the North, while Bolingbroke would detach Denmark "
             "from its allies by the spring.",
    says="In his postscript of 13 October 1712 Manteuffel passes on what the Hanoverian resident Heusch had told him: Oxford "
         "had said the Queen of England was too far off to meddle in pacifying the North and would defer to Hanover on its "
         "execution, Bolingbroke's declaration had been far more violent (Denmark to be detached from its allies by the "
         "spring), and the Elector had tried to turn the Queen from Bolingbroke's view, saying Hanover would gladly help a "
         "general peace but would never press Denmark into a separate one.",
    page=("img/mant0391_page.jpg", "Manteuffel to Flemming, postscript, Berlin, 13 October 1712: clear French with numbers "
          "where the names go. SHStA Dresden, 10026 Geheimes Kabinett, Loc. 694/08 f.313 (image 0391)."),
    lines=[
      ("img/mant0391_a.jpg", mtok(M91["r0"]) + clear("s'est expliqué par ses ministres au sujet des affaires du nord"),
       "[la reine d'Angleterre] s'est expliquée par ses ministres au sujet des affaires du nord",
       "the Queen of England has explained herself through her ministers on the affairs of the North"),
      ("img/mant0391_b.jpg", clear("bien differente.") + mtok(M91["r1"]) + clear("a dit en gros que") + mtok(M91["r2"])
       + clear("etoit trop"),
       "… bien différente. [Oxford] a dit en gros que [la reine] étoit trop",
       "… quite differently. Oxford said, broadly, that the Queen was too"),
      ("img/mant0391_c.jpg", clear("loin de s'en meler pour les appaiser, et de s'en rap-"),
       "loin de s'en mêler pour les apaiser, et de s'en rap-", "far off to meddle in pacifying them, and would"),
      ("img/mant0391_d.jpg", clear("porter, quant a l'execution, aux sentiments de") + mtok(M91["r3"]),
       "porter, quant à l'exécution, aux sentiments de [l'Electeur de Hanovre]",
       "defer, as to carrying it out, to the views of the Elector of Hanover;"),
      ("img/mant0391_e.jpg", clear("mais la declaration de") + mtok(M91["r4"]) + clear("a été bien"),
       "mais la déclaration de [Bullinbroug] a été bien", "but the declaration of Bolingbroke was much"),
      ("img/mant0391_h.jpg", clear("plus facilement, on") + mtok(M91["r5"]) + clear("(bon gré malgré)") + mtok(M91["r6"])
       + clear("de ses"),
       "plus facilement, on [d]etacheroit (bon gré malgré) [le roi de Danemark] de ses",
       "more easily, the King of Denmark would be detached, willing or not, from his"),
    ],
    lang="French", intro_note="Clear words are shown in italics as written; the numbered groups are the cipher. Two of "
                              "them spell a name letter by letter (Oxford, 'Bullinbroug'); one spells a verb.",
    faces=[("Ernst Christoph von Manteuffel", "Saxon envoy at Berlin", "writes the postscript", "manteuffel.jpg"),
           ("Queen Anne", "Queen of Great Britain", "code 217, three times", "anne.jpg"),
           ("Robert Harley, earl of Oxford", "Lord Treasurer", "“too far off to meddle”", "oxford.jpg"),
           ("Henry St John, Bolingbroke", "Secretary of State", "the “far more violent” line", "bolingbroke.jpg"),
           ("Georg Ludwig", "Elector of Hanover, Anne's heir", "code 266", "hanover.jpg"),
           ("Frederick IV", "King of Denmark", "code 227: to be detached", "denmark.jpg"),
           ("Heusch", "Hanoverian resident at Berlin", "Manteuffel's informant", None)],
    moment=[("1700-1721", "The Great Northern War: Denmark, Saxony-Poland and Russia against Sweden."),
            ("16 Sept 1712", "From London, a Dutch letter doubts a squadron will still be sent against the King of Denmark (printed in the Heinsius correspondence)."),
            ("13 Oct 1712", "Manteuffel's postscript from Berlin: who in London said what."),
            ("11 Apr 1713", "The Peace of Utrecht is signed; the war in the North goes on.")],
    this=2,
    places=[("Berlin", 13.4, 52.52, "Manteuffel writes"), ("Dresden", 13.74, 51.05, "Flemming reads"),
            ("London", -0.13, 51.5, "Oxford, Bolingbroke"), ("Hanover", 9.73, 52.37, "the Elector"),
            ("Copenhagen", 12.57, 55.68, "the King of Denmark")],
    trial=[("", "217", "la reine d'Angleterre", "C", "Krauske 1893 table"),
           ("", "33 · 4 · 1 · 16 · 60 · 120", "O x f o r d", "C/M", "letters from the same table"),
           ("", "227", "le roi de Danemark", "M", "Krauske 1893 table")],
    proof=dict(n="N3", d="D2", pct="46.7", audits=["8 Oct 2026 (first audit)", "8 Oct 2026 (second, adversarial)"],
               counts=None, total=None, unit="cipher signs",
               key="Published key: Dr. O. Krauske's 1893 manuscript key table (SHStA Dresden, Loc. 694/10), applied as written. "
                   "The clear French is the letter's own.",
               links=[("Audit and search log", REPO + "ciphers/sachsstaatsarchiv-manteuffel-1712/AUDIT.md"),
                      ("Frame 0391 transcription and reading", TREE + "ciphers/sachsstaatsarchiv-manteuffel-1712/f0390_08"),
                      ("Folder", TREE + "ciphers/sachsstaatsarchiv-manteuffel-1712")],
               safe="Applying Krauske's 1893 table to the cipher names in Manteuffel's postscript of 13 Oct 1712 gives Oxford, "
                    "Bolingbroke and the Queen of England in a report, passed on by the Hanoverian resident Heusch; no prior "
                    "plaintext of these statements located in the Heinsius correspondence or Droysen."),
    holder=[("The volume's record at the Sächsisches Staatsarchiv (Loc. 694/08; the postscript is image 0391)",
             "https://www.archiv.sachsen.de/archiv/bestand.jsp?guid=3a83f921-9a43-485f-874b-34653ed59b68")],
    credit=[("Page and line crops", "Sächsisches Hauptstaatsarchiv Dresden, 10026 Geheimes Kabinett, Loc. 694/08, digitised "
             "image 0391 (archiv.sachsen.de).", "Reuse terms not recorded in the repository; to be checked with the SHStA "
             "before any publication. Private mock-up only.")],
  ),
]

# grade counts for 0391 from the committed tokens
_c = {}
for rows in M91.values():
    for r in rows:
        _c[r["grade"]] = _c.get(r["grade"], 0) + 1
DISPLAYS[2]["proof"]["counts"] = [(g, _c[g]) for g in "HCSMIU" if g in _c]
DISPLAYS[2]["proof"]["total"] = sum(_c.values())

CSS2 = """
.pf{position:relative}.pf img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;border-radius:4px;border:0;background:var(--chip)}
.says{background:var(--panel);border:2px solid var(--accent);border-radius:6px;padding:14px;margin:0 0 18px}
.says .tag,.ctx{font:600 12px system-ui,sans-serif;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.says p{margin:6px 0 0;font-size:18px}.ctxbox{border:1px dashed var(--rule);border-radius:6px;padding:12px}
.comp{background:var(--panel);border:1px solid var(--rule);border-radius:6px;padding:10px 12px;margin:8px 0;font-size:16px}
.comp b{font:600 13px system-ui,sans-serif;display:block;color:var(--muted)}
.caution{font:13px/1.45 system-ui,sans-serif;border-left:3px solid var(--gM);padding:4px 10px;margin:8px 0}
.holderfig{margin:0}.holderlink{font:14px/1.5 system-ui,sans-serif;border:1px dashed var(--rule);border-radius:6px;padding:10px 12px;
 margin:0 0 6px;overflow-wrap:anywhere}
"""


def lines_html(lines, lang):
    """One block per line. A falsy src (the public site, where holder images are linked, not reproduced) drops the crop."""
    out = []
    for src, toks, fr, en in lines:
        out.append('<div class="line">' + (f'<img src="{src}" alt="Cipher line">' if src else "")
                   + f'<div class="layer">{lang} as read, sign by sign (grade under each)</div>'
                   f'<div class="toks">{"".join(B.tok_html(*t) for t in toks)}</div>'
                   f'<div class="layer">English (translation, interpretation)</div>'
                   f'<div class="en"><div class="fr">{E(fr)}</div><div class="tr">{E(en)}</div></div></div>')
    return "".join(out)


def face_html(name, role, now, file, pdir):
    img = (f'<img src="{pdir}{file}" alt="Portrait of {E(name)}" loading="lazy" onerror="this.remove()">' if file else "")
    return (f'<div class="face"><div class="pf">{B.silhouette(name)}{img}</div><strong>{E(name)}</strong>{E(role)}'
            f'<div class="now">{E(now)}</div></div>')


def holder_links(d):
    return " &middot; ".join(f'<a href="{E(u)}">{E(t)}</a>' for t, u in d.get("holder", []))


def display_html(d, img, pdir, public=False):
    """public=True (the public readings site, 10 Oct 2026): holder images are not reproduced -- img() returns "" -- so the page
    image becomes a link to the holder, line crops and image-only trial cards are dropped, and the credit names the holder and
    says the images are linked, not copied (their reuse terms are not recorded in the repository)."""
    p = d["proof"]
    fix = lambda ls: [(img(s), t, a, b) for s, t, a, b in ls]
    hero_src = img(d["page"][0])
    hero = (f'<figure><img src="{hero_src}" alt="The cipher page"><figcaption>{E(d["page"][1])}</figcaption></figure>' if hero_src else
            f'<figure class="holderfig"><p class="holderlink">The page is at the holder (image not reproduced here): '
            f'{holder_links(d)}</p><figcaption>{E(d["page"][1])}</figcaption></figure>')
    layers = (f'three layers per line: the line as written; the {d["lang"]} as read, every sign graded (the audited layer); an '
              'English rendering (ours).' if hero_src else
              f'two layers per line: the {d["lang"]} as read, every sign graded (the audited layer); an English rendering (ours). '
              'The line as written is on the holder\'s page, linked beside.')
    out = [f'<section id="{d["slug"]}"><div class="kicker">{E(d["kicker"])}</div><h1>{E(d["title"])}</h1>',
           f'<p class="headline">{E(d["headline"])}</p>',
           f'<div class="says"><div class="tag">What the reading says (the audit\'s depth sentence)</div><p>{E(d["says"])}</p></div>',
           f'<div class="hero">{hero}<div>',
           f'<div class="small" style="margin-bottom:8px">{E(d["intro_note"])} Reveal to see {layers}</div>',
           f'<button data-reveal="r-{d["slug"]}" aria-expanded="false">Reveal the reading</button>',
           f'<div id="r-{d["slug"]}" class="reveal" style="margin-top:12px">{B.legend()}{lines_html(fix(d["lines"]), d["lang"])}</div></div></div>']
    if d.get("companions"):
        out.append('<h2>Two more from the same ledger</h2>' + "".join(
            f'<div class="comp"><b>{E(t)}</b>{E(s)}</div>' for t, s in d["companions"])
            + '<p class="small">Each read at grade H with the same code book and audited as its own item; their pages are not '
              'shown here. Quoted from each item\'s depth sentence.</p>')
    if d.get("second"):
        s = d["second"]
        out.append(f'<h2>{E(s["title"])}</h2><div class="says"><div class="tag">What the reading says</div><p>{E(s["says"])}</p></div>'
                   f'<div class="caution">{E(s["caution"])}</div>'
                   f'<button data-reveal="r2-{d["slug"]}" aria-expanded="false">Reveal the reading</button>'
                   f'<div id="r2-{d["slug"]}" class="reveal" style="margin-top:12px">{lines_html(fix(s["lines"]), d["lang"])}</div>'
                   f'<p class="small">{E(s["proof"])}</p>')
    out.append('<h2>Faces</h2><div class="faces">' + "".join(face_html(*f, pdir) for f in d["faces"])
               + '</div><p class="small">Context. Public-domain portraits from Wikimedia Commons are being gathered '
                 '(portraits/manifest.tsv names each file and its licence); until a file arrives, the face is a labelled '
                 'placeholder. No non-free image is used.</p>')
    strip = "".join(f'<li class="{"this" if i == d["this"] else ""}"><time>{E(t)}</time>{E(ev)}</li>' for i, (t, ev) in enumerate(d["moment"]))
    out.append(f'<h2>Context: the moment</h2><div class="ctxbox"><div class="ctx">Context from history, not from the cipher</div>'
               f'<div class="moment" style="margin-top:8px"><ol class="strip">{strip}</ol><div class="map">{B.map_svg(d["places"])}</div></div></div>')
    trial = [t for t in d["trial"] if not t[0] or img(t[0])]  # a sign known only by its image needs the image
    cards = "".join(
        f'<div class="card" tabindex="0" role="button" aria-pressed="false">'
        + (f'<img src="{img(i)}" alt="A cipher sign">' if i else f'<div class="code">{E(code)}</div>')
        + f'<div class="hint">tap to read it</div><div class="ans">{E(val)}</div><div class="small">grade {g} · {E(src)}</div></div>'
        for i, code, val, g, src in trial)
    if trial:
        n = {1: "One sign", 2: "Two signs", 3: "Three signs"}.get(len(trial), f"{len(trial)} signs")
        out.append(f'<h2>Try it</h2><p class="small">{n} from the key. Guess, then tap.</p><div class="try">{cards}</div>')
    bar = "".join(f'<span class="{g}" style="flex:{n}" title="{g} {n}">{g if n / p["total"] > .04 else ""}</span>' for g, n in p["counts"])
    counts = " · ".join(f"{g} {n}" for g, n in p["counts"])
    out.append('<h2>How we know</h2><div class="badges">'
               f'<div class="badge"><strong>{p["n"]}</strong>{E(NCLASS[p["n"]])}</div>'
               f'<div class="badge"><strong>{p["d"]} · about {p["pct"]}%</strong>{E(DCLASS[p["d"]])}</div>'
               f'<div class="badge"><strong>Two audits</strong>{E("; ".join(p["audits"]))}, each by a session other than the reader.</div></div>'
               f'<div class="small" style="margin-top:12px">Grades of the {p["total"]} {p["unit"]} read: {counts}</div><div class="bar">{bar}</div>'
               f'<p class="small"><b>Whose key.</b> {E(p["key"])}</p><p class="small"><b>The audit\'s sentence.</b> {E(p["safe"])}</p>'
               '<ul class="links">' + "".join(f'<li><a href="{u}">{E(t)}</a></li>' for t, u in p["links"]) + '</ul>')
    if public:
        credit = "".join(f'<b>Source:</b> {E(b)} The holder\'s images are linked, not reproduced here: {holder_links(d)}.<br>'
                         for a, b, c in d["credit"])
        tail = 'Map drawn by us. English renderings are ours.'
    else:
        credit = "".join(f'<b>{E(a)}:</b> {E(b)} {E(c)}<br>' for a, b, c in d["credit"])
        tail = 'Map drawn for this mock-up. English renderings are ours.'
    out.append('<div class="credit">' + credit + 'Portraits: Wikimedia Commons, public domain, credits in portraits/manifest.tsv '
               'once fetched. ' + tail + '</div></section>')
    return "".join(out)


def page(title, body, desc):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{E(title)}</title><meta name="description" content="{E(desc)}"><style>{B.CSS}{CSS2}</style></head><body>'
            '<div class="mock">Private mock-up for review, 9 October 2026 (second version). Not published, not linked.</div>'
            f'<div class="wrap">{body}</div><script>{B.JS}</script></body></html>')


def nav(prefix, current=None):
    links = [("index2.html" if prefix else "#top", "Three displays")] + [
        ((d["slug"] + ".html") if prefix else "#" + d["slug"], d["short"]) for d in DISPLAYS]
    return '<nav class="top" id="top">' + "".join(
        f'<a href="{h}"{" aria-current=page" if t == current else ""}>{E(t)}</a>' for h, t in links) + "</nav>"


def intro(img, href):
    """The three display cards; a falsy img() (public site) leaves the card without its page image."""
    cards = "".join(f'<a href="{href(d)}">' + (f'<img src="{img(d["page"][0])}" alt="">' if img(d["page"][0]) else "")
                    + f'<div class="kicker" style="margin-top:8px">{E(d["kicker"])}</div><strong>{E(d["title"])}</strong></a>'
                    for d in DISPLAYS)
    return ('<div class="kicker">Three cipher letters, read</div><h1>What the cipher said</h1>'
            '<p class="headline">A telegram about the plot to burn New York; an Elector\'s secret about the next emperor; a '
            'Saxon envoy\'s names for who in London said what. Chosen for what our reading itself says, not for the history '
            'around it.</p>' + f'<div class="cards3">{cards}</div>')


def main():
    rel = lambda p: p
    def emb(p):
        with open(os.path.normpath(os.path.join(HERE, p)), "rb") as f:
            mime = "image/png" if p.endswith(".png") else "image/jpeg"
            return f"data:{mime};base64," + base64.b64encode(f.read()).decode()
    files = {"index2.html": page("What the Cipher Said", nav(True, "Three displays") + intro(rel, lambda d: d["slug"] + ".html"),
                                 "Three cipher displays chosen by what the audited reading says (private mock-up).")}
    for d in DISPLAYS:
        files[d["slug"] + ".html"] = page(d["short"] + " cipher display", nav(True, d["short"]) + display_html(d, rel, "portraits/"),
                                          d["headline"])
    for name, s in files.items():
        with open(os.path.join(HERE, name), "w") as f:
            f.write(s)
    single = page("What the Cipher Said", nav(False) + intro(emb, lambda d: "#" + d["slug"])
                  + "".join(display_html(d, emb, "exhibit/portraits/") for d in DISPLAYS),
                  "Three cipher displays in one file (private mock-up, second version).")
    out = os.path.join(HERE, "..", "exhibit-2026-10-09b.html")
    with open(out, "w") as f:
        f.write(single)
    print("wrote", ", ".join(files), "and", os.path.relpath(os.path.normpath(out), ROOT), f"({len(single)//1024} KB)")


if __name__ == "__main__":
    main()
