#!/usr/bin/env python3
"""Build the EXHIBIT-1 private mock-up: three museum-style displays of audited readings.

Usage: python3 research/mockups/exhibit/build_exhibit.py
Writes research/mockups/exhibit/{index,gramont-1530,manteuffel-1712,nassau-1573}.html (images by relative path)
and research/mockups/exhibit-2026-10-09.html (all three inline, images embedded). Reading tokens and grades are read
from the targets' committed token files and keys at build time; nothing under ciphers/ is written.
Wording follows each target's AUDIT.md safe sentence and status.json depth sentence (CLAUDE.md rule 10, rule 4a).
"""
import base64, csv, html, os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "https://github.com/NoAutopilot/cipher-lab/blob/main/"
TREE = "https://github.com/NoAutopilot/cipher-lab/tree/main/"
E = html.escape


def tsv(path):
    with open(os.path.join(ROOT, path), newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


# ---------------------------------------------------------------- reading tokens (read, never written)
def gramont_lines(lines):
    out = {}
    for r in tsv("ciphers/fr2980-gramont/reading_tokens.tsv"):
        if r["folio"] == "f29r" and r["line"] in lines:
            v = r["value"]
            out.setdefault(r["line"], []).append(("" if v == "NULL" else v.lower(), r["grade"], r["sign"]))
    return out


def manteuffel_lines(lines):
    key = {r["code"]: (r["value"], r["grade"]) for r in tsv("ciphers/sachsstaatsarchiv-manteuffel-1712/key.tsv")}
    out = {}
    for line in open(os.path.join(ROOT, "ciphers/sachsstaatsarchiv-manteuffel-1712/f410/reconciled.txt")):
        if line.startswith("#") or not line.strip():
            continue
        lab, *toks = line.split()
        if lab not in lines:
            continue
        row = []
        for t in toks:
            if t == "|":
                continue
            c = t.split(":")[0]
            v, g = key.get(c, ("", "U"))
            if ":low" in t and g == "C":
                g = "M"  # passes split on the digits: shown as uncertain here
            row.append((v, g, c))
        out[lab] = row
    return out


def nassau_lines(lines):
    toks = {(r["line"], r["idx"]): (r["value"], r["grade"]) for r in tsv("ciphers/lodewijk-van-nassau-1573-74/reading_5797_full_tokens.tsv")}
    out = {}
    for r in tsv("ciphers/lodewijk-van-nassau-1573-74/ciphertext_5797.tsv"):
        if r["line"] not in lines:
            continue
        s = r["sign"]
        if s.startswith("="):
            out.setdefault(r["line"], []).append((s[1:], "clear", ""))
        else:
            v, g = toks.get((r["line"], r["position"]), ("?", "U"))
            names = {"pfaltzgraf": "Pfaltzgraf", "landgraf": "Landgraf", "herzogvonsachsen": "Herzog von Sachsen"}
            out.setdefault(r["line"], []).append(("" if v == "NULL" else names.get(v, v), g, s))
    return out


# ---------------------------------------------------------------- content
# Colours: firm grades (H, C, S) one blue, uncertain (M, I) one orange, U grey; tools/cvd_check.py PASS for both themes.
# The grade letter under every sign and the underline style (solid, double, thick, dotted, dashed) carry the grade without hue.
GRADES = [("H", "read from a key source"), ("C", "from known plaintext or a period key table"),
          ("S", "cryptanalytic, with a control"), ("M", "uncertain"), ("I", "inferred"), ("U", "sign not covered by the key")]
NCLASS = {"N4": "No prior decipherment located after the principal editions, catalogues and project pages were searched; "
                "internal or unpublished work not excluded.",
          "N3": "No prior plaintext or decipherment located after a logged search."}
DCLASS = {"D2": "Partially deciphered: at least one clause reads, and a verifier wrote one true, specific sentence about it."}

G = gramont_lines({"L01", "L02", "L03", "L04", "L05"})
M = manteuffel_lines({"L13", "L14", "M4", "L16"})
N = nassau_lines({"p7_spot2", "p5_spot3"})

DISPLAYS = [
  dict(
    slug="gramont-1530", short="Rome, 1530", kicker="Rome · 20 May 1530",
    title="A bishop's secret article, in the weeks Rome held Henry VIII's divorce",
    headline="Writing from Rome, the French envoy Gabriel de Gramont tells the King's secretary he has handed the bearer "
             "an article “set apart”, addressed to the secretary though meant for the King, and calls it "
             "“le total fondement”: the whole foundation.",
    page=("img/gramont_f29r_page.jpg", "Gramont to Villandry, Rome, 20 May [1530]: seven lines in clear, then fourteen in cipher. "
          "BnF, Français 2980 f.29r."),
    lines=[
      ("img/gramont_L01.jpg", G["L01"], "J'ay baillé à ce porteur ung article que j'ay mis",
       "I have given this bearer an article which I have put"),
      ("img/gramont_L02.jpg", G["L02"], "à part, et ay faict l'adresse de dessus à vous, combien qu'[il] soit",
       "apart, and have addressed it, on the outside, to you, although it is"),
      ("img/gramont_L03.jpg", G["L03"], "au Roy ; et si ledict porteur … [not clear to us] … vous",
       "for the King; and if the said bearer … [this stretch is not clear to us] … you"),
      ("img/gramont_L04.jpg", G["L04"], "… bailler, je vous prie le luy demander, car c'est le total",
       "… hand over, I beg you to ask him for it, for it is the whole"),
      ("img/gramont_L05.jpg", G["L05"], "fondement ; et j'ay ce faict d'aultant que nous …",
       "foundation; and I have done this inasmuch as we …"),
    ],
    lang="French",
    faces=[("Gabriel de Gramont", "Bishop of Tarbes, French envoy", "May 1530: writing in cipher from Rome"),
           ("Jean Breton de Villandry", "Francis I's secretary of finances", "receives the f.29r letter"),
           ("Francis I", "King of France", "the f.30 letter is to him"),
           ("Anne de Montmorency", "Grand maître, Francis's chief minister", "Gramont's March letter is to him"),
           ("Clement VII", "Pope, judge of the case", "holds the divorce suit at Rome"),
           ("Henry VIII", "King of England", "wants his marriage annulled"),
           ("Anne Boleyn", "the woman Henry means to marry", "waits on the verdict"),
           ("“Rochefort”", "English envoy, as the letter names him", "pressed the Pope in March")],
    moment=[("July 1529", "Clement VII calls Henry VIII's divorce case to Rome."),
            ("24 Feb 1530", "At Bologna the Pope crowns Charles V emperor; the English and French envoys follow the court."),
            ("28 Mar 1530", "Gramont, at Bologna, tells Montmorency the Pope has suspended the matter for a month and a half "
                            "(a letter already printed in 1688; we used it to check the key)."),
            ("20 May 1530", "From Rome, Gramont writes in cipher to Villandry (f.29r) and to the King (f.30)."),
            ("8 Jun 1530", "Gramont is created cardinal.")],
    places=[("Rome", 12.5, 41.9, "20 May letters"), ("Bologna", 11.34, 44.49, "March 1530"),
            ("Paris", 2.35, 48.86, "the French court"), ("London", -0.13, 51.5, "Henry VIII")],
    secret=("An article travels separately with the bearer: addressed to Villandry, meant for the King, and to be asked for "
            "in person. Gramont calls it the whole foundation of his business. What the article said is not in this letter.",
            ["img/gramont_L04.jpg", "img/gramont_L05.jpg"], "“le total / fondement”, lines 4–5 of the cipher"),
    trial=[("img/gramont_sign_lam.jpg", "", "A", "H", "Tomokiyo; Lasry"),
           ("img/gramont_sign_aq.jpg", "", "Y", "H", "Tomokiyo; Lasry"),
           ("img/gramont_sign_q.jpg", "", "E (or B)", "M", "a variant shape; uncertain")],
    proof=dict(n="N4", d="D2", pct="93.8", audits=["24 Sept 2026 (first audit)", "24 Sept 2026 (second, adversarial)"],
               counts=[("H", 532), ("S", 1), ("M", 30), ("U", 5)], total=568,
               key="Published key: the Gramont 1530 key of Satoshi Tomokiyo (Cryptiana) and George Lasry (2023). "
                   "Tomokiyo identified these letters as readable with it; David Bourdeau catalogued them (no. 328).",
               links=[("Audit and search log", REPO + "ciphers/fr2980-gramont/AUDIT.md"),
                      ("Reading (regenerate: decode.py --check)", REPO + "ciphers/fr2980-gramont/reading.txt"),
                      ("Folder", TREE + "ciphers/fr2980-gramont")],
               safe="No prior decipherment located of Gramont's cipher letter to Villandry (BnF fr.2980 f.29r); read in part "
                    "with the published Gramont 1530 key."),
    credit=[("Page and line crops", "Bibliothèque nationale de France, Français 2980, f.29r (Gallica, ark:/12148/btv1b9059991d, view 31).",
             "BnF images are not public domain: reuse by BnF permission. Shown here in a private mock-up only; permission to be "
             "sought before any publication.")],
  ),
  dict(
    slug="manteuffel-1712", short="Berlin, 1712", kicker="Berlin · November 1712",
    title="What would London do for the North? A Saxon envoy's cipher postscript",
    headline="In a cipher postscript from Berlin, Saxony's envoy names the Queen of England three times: once "
             "“touchant le prince”, once followed by “ne fera rien pour lui, mais luy …”.",
    page=("img/manteuffel_f410_block.jpg", "Manteuffel to Flemming, Berlin, November 1712: clear French and numbered cipher in "
          "the same lines. SHStA Dresden, Loc. 694/08 f.410."),
    lines=[
      ("img/manteuffel_L13.jpg", M["L13"], "… à … la reine d'Angleterre … touchant le prince",
       "… to … the Queen of England … concerning the prince"),
      ("img/manteuffel_L14.jpg", M["L14"], "… fils … la reine d'Angleterre … ne fe-",
       "… son … the Queen of England … will not"),
      ("img/manteuffel_M4.jpg", M["M4"], "-ra rien pour lui, mais luy …",
       "do anything for him, but [to] him …"),
      ("img/manteuffel_L16.jpg", M["L16"], "… sera … Stettin … contraire",
       "… will be … Stettin … contrary"),
    ],
    lang="French",
    faces=[("Ernst Christoph von Manteuffel", "Saxon envoy at Berlin", "writes the cipher postscripts"),
           ("Jakob Heinrich von Flemming", "Augustus II's chief minister", "reads them in Dresden"),
           ("Augustus II", "Elector of Saxony, King of Poland", "Manteuffel's master"),
           ("Frederick I", "King in Prussia", "his court is Manteuffel's post"),
           ("Queen Anne", "Queen of Great Britain", "named three times on f.410"),
           ("Robert Harley, earl of Oxford", "Lord Treasurer", "“too far off” to meddle"),
           ("Henry St John, Bolingbroke", "Secretary of State", "a “far more violent” line"),
           ("Heusch", "Hanoverian resident at Berlin", "Manteuffel's informant, 13 Oct"),
           ("Stanislas Leszczyński", "the rival King of Poland", "his envoy at Berlin that autumn"),
           ("Charles XII", "King of Sweden", "in Ottoman exile at Bender")],
    moment=[("8 Jul 1709", "Poltava: Charles XII's army is destroyed; Augustus II takes back the Polish crown."),
            ("13 Oct 1712", "Manteuffel reports what Heusch told him: Oxford called the Queen too far off to meddle in the "
                            "North; Bolingbroke's line was far harsher (frame 0391)."),
            ("Nov 1712", "Manteuffel's cipher postscript on f.410 names the Queen of England three times."),
            ("25 Feb 1713", "Frederick I of Prussia dies."),
            ("11 Apr 1713", "The Peace of Utrecht is signed; the war in the North goes on.")],
    places=[("Berlin", 13.4, 52.52, "Manteuffel writes"), ("Dresden", 13.74, 51.05, "Flemming reads"),
            ("London", -0.13, 51.5, "the Queen"), ("Stettin", 14.55, 53.43, "named on f.410"),
            ("Utrecht", 5.12, 52.09, "peace congress")],
    secret=("Our reading of the gist: what Britain would or would not do for a prince in the northern settlement, and Stettin. "
            "The unread groups between the phrases decide the meaning, so this stays an interpretation.",
            ["img/manteuffel_L13.jpg", "img/manteuffel_M4.jpg"], "“touchant le prince” and “… ra rien pour lui, mais luy”"),
    trial=[("", "217", "la reine d'Angleterre", "C", "Krauske 1893 table"),
           ("", "390", "Stettin", "C", "Krauske 1893 table"),
           ("", "72", "ch", "C", "Krauske 1893 table")],
    proof=dict(n="N4", d="D2", pct="66.7", audits=["3 Oct 2026 (first audit)", "3 Oct 2026 (second, adversarial)"],
               counts=[("C", 144), ("M", 49), ("U", 23)], total=216,
               key="Published key: Dr. O. Krauske's 1893 manuscript key table (SHStA Dresden, Loc. 694/10), applied as written. "
                   "The story of 13 October is frame 0391, a separate item (N3, D2, audited 8 Oct 2026).",
               links=[("Audit and search log", REPO + "ciphers/sachsstaatsarchiv-manteuffel-1712/AUDIT.md"),
                      ("f.410 transcription and judge", TREE + "ciphers/sachsstaatsarchiv-manteuffel-1712/f410"),
                      ("Folder", TREE + "ciphers/sachsstaatsarchiv-manteuffel-1712")],
               safe="Applying Dr. Krauske's 1893 manuscript key table to the unglossed cipher passage of Loc. 694/08 f.410 gives "
                    "French in stretches; no prior plaintext or decipherment of this passage was located."),
    credit=[("Page and line crops", "Sächsisches Hauptstaatsarchiv Dresden, 10026 Geheimes Kabinett, Loc. 694/08, digitised image "
             "0511 (archiv.sachsen.de).", "Reuse terms not recorded in the repository; to be checked with the SHStA before any "
             "publication. Private mock-up only.")],
  ),
  dict(
    slug="nassau-1573", short="Dillenburg, 1573", kicker="Dillenburg · 22 October 1573",
    title="The blanks in the Orange archives: who “holds well” with the Nassau brothers",
    headline="Where the 1837 edition of William of Orange's letters left blanks, the cipher names the Elector Palatine "
             "as the one who “helt sich wol und thut in warheit viel”: holds well, and in truth does much.",
    page=("img/nassau_p7_page.jpg", "Jan and Lodewijk van Nassau to William of Orange, Dillenburg, 22 Oct 1573, page 7: German in "
          "clear, names in numbers. Koninklijk Huisarchief, A 3, 895/I (WVO 5797)."),
    lines=[
      ("img/nassau_p7_spot2.jpg", N["p7_spot2"], "[Pfaltzgraf] … helt sich wol, und thut in warheit viel",
       "The Palsgrave (Elector Palatine) … holds well, and in truth does a great deal"),
      ("img/nassau_p5_spot3.jpg", N["p5_spot3"], "Bey [Herzog von Sachsen] … und [Landgraf] … ist …",
       "With the Duke of Saxony … and the Landgrave … is …"),
    ],
    lang="German",
    faces=[("William of Orange", "leader of the Dutch Revolt", "in Holland; the letter is to him"),
           ("Louis (Lodewijk) of Nassau", "Orange's brother, soldier and diplomat", "co-writes from Dillenburg"),
           ("Jan of Nassau", "Orange's brother, count at Dillenburg", "co-writes; keeps the house"),
           ("Frederick III", "Calvinist Elector Palatine", "“holds well” in the blank"),
           ("Wilhelm IV", "Landgrave of Hesse-Kassel", "named in the other blank"),
           ("Groen van Prinsterer", "editor of the Orange archives", "printed it, 1837, with blanks")],
    moment=[("1 Apr 1572", "The Sea Beggars take Brielle; Holland rises for Orange."),
            ("24 May 1572", "Louis of Nassau seizes Mons."),
            ("22 Oct 1573", "From Dillenburg, Jan and Louis report to Orange which German princes will help."),
            ("14 Apr 1574", "Mookerheyde: Louis and his brother Henry are killed."),
            ("1837", "Groen van Prinsterer prints the letter, leaving the cipher passages blank.")],
    places=[("Dillenburg", 8.28, 50.74, "the brothers write"), ("Holland", 4.4, 52.0, "Orange"),
            ("Heidelberg", 8.69, 49.4, "Elector Palatine"), ("Kassel", 9.48, 51.31, "Landgrave"),
            ("Dresden", 13.74, 51.05, "Duke of Saxony")],
    secret=("Our reading of the gist: in the brothers' survey of German support, the Palatine is the friend who acts. That the "
            "Palatine backed the Nassaus is long known (Kluckhohn, 1872); what the cipher adds is which name fills Groen's blank.",
            ["img/nassau_p7_spot2.jpg"], "153 · 146 · 137 · helt sich wol"),
    trial=[("", "153", "Pfaltzgraf", "H", "period gloss on WVO 5550"),
           ("", "161", "Landgraf", "H", "period gloss on WVO 5550"),
           ("", "58 · 85 · 38 · 95 · 82 · 35", "zeuget", "C", "letter table; Groen's print")],
    proof=dict(n="N4", d="D2", pct="11.1", audits=["26 Sept 2026 (first audit)", "26 Sept 2026 (second, adversarial)"],
               counts=[("H", 3), ("C", 14), ("M", 44), ("I", 2), ("U", 10)], total=73,
               key="Period and ours: a letter table we recovered from two sibling letters' contemporary decipherments (WVO 4613, "
                   "4615), with the two name codes from a contemporary interlinear gloss on WVO 5550. The rest of the letter is "
                   "Groen van Prinsterer's print (Archives, 1st series, vol. IV, letter CDXLIV).",
               links=[("Audit and search log", REPO + "ciphers/lodewijk-van-nassau-1573-74/AUDIT.md"),
                      ("Reading (regenerate: decode_key.py --check)", REPO + "ciphers/lodewijk-van-nassau-1573-74/reading_5797_full.txt"),
                      ("Matched control", REPO + "ciphers/lodewijk-van-nassau-1573-74/control_5797.py")],
               safe="Two of the blanks Groen van Prinsterer left in WVO 5797 read in part; no prior decipherment of these blanks "
                    "located (N4); the letter's other text is Groen's."),
    credit=[("Page and line crops", "Koninklijk Huisarchief, The Hague, A 3, 895/I, as served by the Huygens Institute "
             "(Willem van Oranje correspondence, letter 5797).", "Reuse terms not recorded in the repository; to be checked "
             "with the Huygens Institute and the Koninklijk Huisarchief before any publication. Private mock-up only.")],
  ),
]

# ---------------------------------------------------------------- rendering
CSS = """
:root{--bg:#f6f2ea;--panel:#fffdf8;--ink:#1d1b18;--muted:#5f5a52;--rule:#d9d1c3;--accent:#123c69;
--gH:#0072B2;--gC:#0072B2;--gS:#0072B2;--gM:#B35900;--gI:#B35900;--gU:#595959;--bt:#ffffff;--chip:#efe8db;--tint:#e8eef6}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#15130f;--panel:#1f1c17;--ink:#efe9de;--muted:#b4ab9c;
--rule:#3a352d;--accent:#9cc3ef;--gH:#56B4E9;--gC:#56B4E9;--gS:#56B4E9;--gM:#E69F00;--gI:#E69F00;--gU:#9a9184;--bt:#1b1916;--chip:#2a261f;--tint:#1d2a3a}}
:root[data-theme="dark"]{--bg:#15130f;--panel:#1f1c17;--ink:#efe9de;--muted:#b4ab9c;--rule:#3a352d;--accent:#9cc3ef;--gH:#56B4E9;
--gC:#56B4E9;--gS:#56B4E9;--gM:#E69F00;--gI:#E69F00;--gU:#9a9184;--bt:#1b1916;--chip:#2a261f;--tint:#1d2a3a}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 Georgia,"Iowan Old Style",serif}
a{color:var(--accent)}.wrap{max-width:1060px;margin:0 auto;padding:0 16px 48px}
.mock{font:13px/1.4 system-ui,sans-serif;background:var(--chip);color:var(--muted);padding:6px 16px;text-align:center}
nav.top{display:flex;gap:16px;flex-wrap:wrap;font:14px system-ui,sans-serif;padding:12px 0;border-bottom:1px solid var(--rule)}
.kicker{font:600 13px system-ui,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:28px 0 4px}
h1{font-size:clamp(26px,4.4vw,40px);line-height:1.15;margin:0 0 14px}h2{font:600 13px system-ui,sans-serif;letter-spacing:.1em;
text-transform:uppercase;color:var(--muted);margin:36px 0 10px;border-top:1px solid var(--rule);padding-top:14px}
.headline{font-size:clamp(18px,2.4vw,22px);max-width:46em;margin:0 0 18px}
.hero{display:grid;grid-template-columns:minmax(0,300px) minmax(0,1fr);gap:20px;align-items:start}
@media (max-width:760px){.hero{grid-template-columns:minmax(0,1fr)}}
figure{margin:0}figure img{width:100%;height:auto;display:block;border:1px solid var(--rule);background:#fff}
figcaption{font:13px/1.4 system-ui,sans-serif;color:var(--muted);margin-top:6px}
.line{background:var(--panel);border:1px solid var(--rule);border-radius:6px;padding:10px;margin-bottom:12px}
.line img{width:100%;height:auto;display:block;background:#fff;border-radius:3px}
.toks{display:flex;justify-content:space-between;gap:2px;margin-top:6px;overflow-x:auto;padding-bottom:2px}
.tok{display:inline-flex;flex-direction:column;align-items:center;font:600 14px/1.1 ui-monospace,Menlo,monospace;min-width:.9em}
.tok small{font:9px system-ui,sans-serif;color:var(--muted);margin-top:2px}
.tok.H b{color:var(--gH);border-bottom:2px solid var(--gH)}.tok.C b{color:var(--gC);border-bottom:3px double var(--gC)}
.tok.S b{color:var(--gS);border-bottom:4px solid var(--gS)}.tok.M b{color:var(--gM);border-bottom:2px dotted var(--gM)}
.tok.I b{color:var(--gI);border-bottom:2px dashed var(--gI)}.tok.U b{color:var(--gU)}
.tok.clear b{font:italic 15px Georgia,serif;color:var(--ink)}.tok.null b{color:var(--gU);font-weight:400}
.layer{font:12px system-ui,sans-serif;color:var(--muted);margin-top:8px}
.en{border-left:3px solid var(--rule);padding:4px 10px;margin-top:4px}.en .fr{font-style:italic}.en .tr{font-size:17px}
.reveal .toks,.reveal .en,.reveal .layer{display:none}.reveal.open .toks,.reveal.open .en,.reveal.open .layer{display:flex}
.reveal.open .en,.reveal.open .layer{display:block}
button{font:600 14px system-ui,sans-serif;background:var(--accent);color:var(--bg);border:0;border-radius:4px;padding:8px 14px;cursor:pointer}
.legend{display:flex;flex-wrap:wrap;gap:10px 18px;font:12px system-ui,sans-serif;color:var(--muted);margin:8px 0 14px}
.legend .tok{flex-direction:row;gap:6px}
.faces{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:14px}
.face{background:var(--panel);border:1px solid var(--rule);border-radius:6px;padding:10px;font:13px/1.35 system-ui,sans-serif}
.face svg{width:100%;height:auto;display:block;border-radius:4px}.face strong{display:block;font:600 14px Georgia,serif;margin-top:6px}
.face .now{color:var(--muted)}
.moment{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:20px}@media (max-width:760px){.moment{grid-template-columns:minmax(0,1fr)}}
ol.strip{list-style:none;margin:0;padding:0;border-left:3px solid var(--rule)}ol.strip li{padding:6px 0 10px 14px;position:relative}
ol.strip li:before{content:"";position:absolute;left:-8px;top:12px;width:12px;height:12px;border-radius:50%;background:var(--panel);
border:3px solid var(--muted)}ol.strip li.this:before{border-color:var(--accent);background:var(--accent)}
ol.strip time{font:600 13px system-ui,sans-serif;display:block}ol.strip li.this time{color:var(--accent)}
.map{background:var(--panel);border:1px solid var(--rule);border-radius:6px}.map svg{width:100%;height:auto;display:block}
.secret{background:var(--tint);border-radius:6px;padding:14px}.secret .tag{font:600 12px system-ui,sans-serif;color:var(--muted)}
.secret img{width:100%;max-width:820px;display:block;margin-top:8px;background:#fff;border-radius:3px}
.try{display:flex;flex-wrap:wrap;gap:12px}.card{background:var(--panel);border:1px solid var(--rule);border-radius:6px;padding:10px;
width:190px;text-align:center;cursor:pointer;font:13px system-ui,sans-serif}.card img{height:84px;width:auto;max-width:100%;background:#fff}
.card .code{font:600 22px ui-monospace,Menlo,monospace;min-height:84px;display:flex;align-items:center;justify-content:center}
.card .ans{visibility:hidden;font:600 18px Georgia,serif;margin-top:6px}.card.open .ans{visibility:visible}
.card .hint{color:var(--muted)}.card.open .hint{display:none}
.badges{display:flex;flex-wrap:wrap;gap:10px}.badge{background:var(--panel);border:1px solid var(--rule);border-radius:6px;padding:10px 12px;
max-width:330px;font:13px/1.4 system-ui,sans-serif}.badge strong{font:600 20px Georgia,serif;display:block}
.bar{display:flex;height:22px;border-radius:4px;overflow:hidden;border:1px solid var(--rule);margin:6px 0;max-width:620px}
.bar span{display:flex;align-items:center;justify-content:center;font:600 11px system-ui,sans-serif;color:var(--bt);min-width:0}
.bar .H{background:var(--gH)}.bar .C{background:var(--gC)}.bar .S{background:var(--gS)}.bar .M{background:var(--gM);
background-image:repeating-linear-gradient(45deg,transparent 0 4px,rgba(255,255,255,.28) 4px 6px)}.bar .I{background:var(--gI)}
.bar .U{background:var(--gU);background-image:repeating-linear-gradient(-45deg,transparent 0 3px,rgba(255,255,255,.35) 3px 5px)}
.small{font:13px/1.45 system-ui,sans-serif;color:var(--muted)}ul.links{font:14px system-ui,sans-serif;padding-left:18px}
.credit{font:12px/1.45 system-ui,sans-serif;color:var(--muted);border-top:1px solid var(--rule);margin-top:30px;padding-top:10px}
.cards3{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px;margin-top:20px}
.cards3 a{display:block;background:var(--panel);border:1px solid var(--rule);border-radius:8px;padding:12px;text-decoration:none;color:var(--ink)}
.cards3 img{width:100%;height:150px;object-fit:cover;object-position:top;border-radius:4px}
"""

JS = """
document.addEventListener('click',function(e){var b=e.target.closest('[data-reveal]');if(b){var s=document.getElementById(b.dataset.reveal);
var o=s.classList.toggle('open');b.textContent=o?'Hide the reading':'Reveal the reading';b.setAttribute('aria-expanded',o);return}
var c=e.target.closest('.card');if(c){c.classList.toggle('open');c.setAttribute('aria-pressed',c.classList.contains('open'))}});
document.addEventListener('keydown',function(e){if((e.key==='Enter'||e.key===' ')&&e.target.classList&&e.target.classList.contains('card')){
e.preventDefault();e.target.click()}});
"""


def initials(name):
    w = [x for x in re.sub(r"[“”(),.]", "", name).split() if x[0].isupper()]
    return (w[0][0] + (w[-1][0] if len(w) > 1 else "")) if w else "?"


def silhouette(name):
    return (f'<svg viewBox="0 0 120 140" role="img" aria-label="No portrait shown for {E(name)}">'
            f'<rect width="120" height="140" fill="var(--chip)"/><circle cx="60" cy="52" r="24" fill="var(--rule)"/>'
            f'<path d="M18 140c4-34 22-50 42-50s38 16 42 50z" fill="var(--rule)"/>'
            f'<text x="60" y="58" text-anchor="middle" font-family="Georgia,serif" font-size="18" fill="var(--muted)">{E(initials(name))}</text>'
            f'<text x="60" y="132" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="var(--muted)">portrait pending</text></svg>')


def tok_html(v, g, sign):
    if g == "clear":
        return f'<span class="tok clear" title="clear text on the page"><b>{E(v)}</b><small>clear</small></span>'
    if v == "" and g != "U":
        return f'<span class="tok null" title="sign {E(sign)}: null (no letter), grade {g}"><b>·</b><small>{g}</small></span>'
    shown = v if v else "?"
    if "|" in shown:
        shown = shown.split("|")[0] + "/…"
    return f'<span class="tok {g}" title="sign {E(sign)} = {E(v or "not in key")}, grade {g}"><b>{E(shown)}</b><small>{g}</small></span>'


def legend():
    return ('<div class="legend">' + "".join(f'<span class="tok {g}"><b>{g}</b> {E(d)}</span>' for g, d in GRADES)
            + '<span class="tok clear"><b>clear</b> written in clear on the page</span></div>')


def map_svg(places):
    lons = [p[1] for p in places]; lats = [p[2] for p in places]
    x0, x1 = min(lons) - 2.5, max(lons) + 5.5; y0, y1 = min(lats) - 1.6, max(lats) + 1.6
    W, H = 400, 300
    sx = lambda lo: 20 + (lo - x0) / (x1 - x0) * (W - 40)
    sy = lambda la: 20 + (y1 - la) / (y1 - y0) * (H - 40)
    pts = "".join(f'<circle cx="{sx(lo):.0f}" cy="{sy(la):.0f}" r="6" fill="var(--accent)"/>'
                  f'<text x="{sx(lo)+10:.0f}" y="{sy(la)-2:.0f}" font-family="Georgia,serif" font-size="15" fill="var(--ink)">{E(n)}</text>'
                  f'<text x="{sx(lo)+10:.0f}" y="{sy(la)+13:.0f}" font-family="system-ui,sans-serif" font-size="11" fill="var(--muted)">{E(r)}</text>'
                  for n, lo, la, r in places)
    first = places[0]
    lines = "".join(f'<line x1="{sx(first[1]):.0f}" y1="{sy(first[2]):.0f}" x2="{sx(lo):.0f}" y2="{sy(la):.0f}" '
                    f'stroke="var(--rule)" stroke-width="2" stroke-dasharray="5 5"/>' for n, lo, la, r in places[1:])
    return (f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Map of {", ".join(p[0] for p in places)}">'
            f'<rect width="{W}" height="{H}" fill="none"/>{lines}{pts}</svg>'
            '<div class="small" style="padding:0 10px 8px">Positions by latitude and longitude; no coastlines drawn.</div>')


def display_html(d, img):
    p = d["proof"]
    out = [f'<section id="{d["slug"]}"><div class="kicker">{E(d["kicker"])}</div><h1>{E(d["title"])}</h1>',
           f'<p class="headline">{E(d["headline"])}</p>',
           f'<div class="hero"><figure><img src="{img(d["page"][0])}" alt="The cipher page"><figcaption>{E(d["page"][1])}</figcaption></figure><div>',
           f'<div class="small" style="margin-bottom:8px">Each line: the signs as written; then, when revealed, the {d["lang"]} as read '
           f'(the audited layer, every sign graded) and an English rendering (ours).</div>',
           f'<button data-reveal="r-{d["slug"]}" aria-expanded="false">Reveal the reading</button>',
           f'<div id="r-{d["slug"]}" class="reveal" style="margin-top:12px">{legend()}']
    for src, toks, fr, en in d["lines"]:
        out.append(f'<div class="line"><img src="{img(src)}" alt="Cipher line">'
                   f'<div class="layer">{d["lang"]} as read, sign by sign (grade under each)</div>'
                   f'<div class="toks">{"".join(tok_html(*t) for t in toks)}</div>'
                   f'<div class="layer">English (translation, interpretation)</div>'
                   f'<div class="en"><div class="fr">{E(fr)}</div><div class="tr">{E(en)}</div></div></div>')
    out.append("</div></div></div>")
    out.append('<h2>Faces</h2><div class="faces">' + "".join(
        f'<div class="face">{silhouette(n)}<strong>{E(n)}</strong>{E(r)}<div class="now">{E(w)}</div></div>' for n, r, w in d["faces"])
        + '</div><p class="small">Portraits pending: public-domain paintings from Wikimedia Commons were to go here; the Commons API '
          'refused this build (rate limit), so every face is a labelled placeholder, never a non-free image.</p>')
    strip = "".join(f'<li class="{"this" if i == 3 or (d["slug"] != "gramont-1530" and i == 2) else ""}"><time>{E(t)}</time>{E(ev)}</li>'
                    for i, (t, ev) in enumerate(d["moment"]))
    out.append(f'<h2>The moment</h2><div class="moment"><ol class="strip">{strip}</ol><div class="map">{map_svg(d["places"])}</div></div>')
    gist, crops, cap = d["secret"]
    out.append(f'<h2>The secret</h2><div class="secret"><div class="tag">Interpretation, not part of the audited reading</div>'
               f'<p style="margin:6px 0 0;font-size:18px">{E(gist)}</p>'
               + "".join(f'<img src="{img(c)}" alt="Cipher words that carry it">' for c in crops)
               + f'<div class="small" style="margin-top:6px">{E(cap)}</div></div>')
    cards = "".join(
        f'<div class="card" tabindex="0" role="button" aria-pressed="false">'
        + (f'<img src="{img(i)}" alt="A cipher sign">' if i else f'<div class="code">{E(code)}</div>')
        + f'<div class="hint">tap to read it</div><div class="ans">{E(val)}</div><div class="small">grade {g} · {E(src)}</div></div>'
        for i, code, val, g, src in d["trial"])
    out.append(f'<h2>Try it</h2><p class="small">Three signs from the key. Guess, then tap.</p><div class="try">{cards}</div>')
    bar = "".join(f'<span class="{g}" style="flex:{n}" title="{g} {n}">{g if n / p["total"] > .04 else ""}</span>' for g, n in p["counts"])
    counts = " · ".join(f"{g} {n}" for g, n in p["counts"])
    out.append('<h2>How we know</h2><div class="badges">'
               f'<div class="badge"><strong>{p["n"]}</strong>{E(NCLASS[p["n"]])}</div>'
               f'<div class="badge"><strong>{p["d"]} · about {p["pct"]}%</strong>{E(DCLASS[p["d"]])}</div>'
               f'<div class="badge"><strong>Two audits</strong>{E("; ".join(p["audits"]))}, each by a session other than the reader.</div></div>'
               f'<div class="small" style="margin-top:12px">Grades of the {p["total"]} cipher signs read: {counts}</div><div class="bar">{bar}</div>'
               f'<p class="small"><b>Whose key.</b> {E(p["key"])}</p><p class="small"><b>The audit\'s sentence.</b> {E(p["safe"])}</p>'
               '<ul class="links">' + "".join(f'<li><a href="{u}">{E(t)}</a></li>' for t, u in p["links"]) + '</ul>')
    out.append('<div class="credit">' + "".join(f'<b>{E(a)}:</b> {E(b)} {E(c)}<br>' for a, b, c in d["credit"])
               + 'Portrait placeholders and map drawn for this mock-up. English renderings and gists are ours.</div></section>')
    return "".join(out)


def page(title, body, desc):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{E(title)}</title><meta name="description" content="{E(desc)}"><style>{CSS}</style></head><body>'
            '<div class="mock">Private mock-up for review, 9 October 2026. Not published, not linked.</div>'
            f'<div class="wrap">{body}</div><script>{JS}</script></body></html>')


def nav(prefix, current=None):
    links = [("index.html" if prefix else "#top", "Three displays")] + [
        ((d["slug"] + ".html") if prefix else "#" + d["slug"], d["short"]) for d in DISPLAYS]
    return '<nav class="top" id="top">' + "".join(
        f'<a href="{h}"{" aria-current=page" if t == current else ""}>{E(t)}</a>' for h, t in links) + "</nav>"


def intro(img, href):
    cards = "".join(f'<a href="{href(d)}"><img src="{img(d["page"][0])}" alt=""><div class="kicker" style="margin-top:8px">'
                    f'{E(d["kicker"])}</div><strong>{E(d["title"])}</strong></a>' for d in DISPLAYS)
    return ('<div class="kicker">Three cipher letters, read</div><h1>Secrets in the post</h1>'
            '<p class="headline">A bishop in Rome, an envoy in Berlin, two brothers in a German castle. Each wrote what mattered most '
            'in signs. See the page, open the reading, meet the people.</p>' + f'<div class="cards3">{cards}</div>')


def main():
    rel = lambda p: p
    def emb(p):
        with open(os.path.join(HERE, p), "rb") as f:
            return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()
    files = {"index.html": page("Secrets in the Post", nav(True, "Three displays") + intro(rel, lambda d: d["slug"] + ".html"),
                                "Three museum-style displays of cipher letters read by the project (private mock-up).")}
    for d in DISPLAYS:
        files[d["slug"] + ".html"] = page(d["short"] + " cipher display", nav(True, d["short"]) + display_html(d, rel), d["headline"])
    for name, s in files.items():
        with open(os.path.join(HERE, name), "w") as f:
            f.write(s)
    single = page("Secrets in the Post", nav(False) + intro(emb, lambda d: "#" + d["slug"])
                  + "".join(display_html(d, emb) for d in DISPLAYS), "Three cipher displays in one file (private mock-up).")
    out = os.path.join(HERE, "..", "exhibit-2026-10-09.html")
    with open(out, "w") as f:
        f.write(single)
    print("wrote", ", ".join(files), "and", os.path.relpath(out, ROOT), f"({len(single)//1024} KB)")


if __name__ == "__main__":
    main()
