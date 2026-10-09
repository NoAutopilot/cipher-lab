#!/usr/bin/env python3
"""FM-R5b (9 Oct 2026): letters-only phrase grep of the FM-R5b entries' decoded phrases AND rare names/numbers in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5785/0': ['yellow fever prevailing to an alarming extent','Vanderhoef should be relieved','Vanderhoef','relieved immediately','close the offices','fever is not very fatal','Newport Barracks sick'],
 'F2 5706/0': ['cut poles and assist in building line','Gloster to West Point','Bickford will leave','lay cables at Gloster','machinery for paying it out','connect through from Monroe to White House'],
 'F3 5630/0': ['following steamers have reported here','none of double decked','Chesapeake City ordered','Transportation should be hurried','Highland Light'],
 'F4 5819/1': ['send at once two gunboats down to','keep a good lookout for rebel boats','hold the persons in them as prisoners','will tow them off','Parker Onondaga','Dutch Gap'],
 'F5 5804/1': ['Lizzie Baker is the only boat','transfer the men as fast as they arrive','whether I shall take the boats'],
 'F6 5798/2': ['Tallapoosa is now near Montauk','Yantic is now','the Maumee is','steering for Halifax','before the Tallahassee','miles off shore'],
 'F7 5605/2': ['Fifth New Jersey Battery','be spared to this department','I should direct this to General Grant'],
 'F8 5788/2': ['driven Kautz back','opened fire upon Fort Harrison','advancing on our right toward','enemy have attacked and driven Kautz'],
 'F9 5724/0': ['prepared to send two millions rations','head of cattle to the White House','Commissary General Taylor'],
 'F10 5814/2': ['appear before a court martial','shall the witness leave at such a time as this','Lieutenant Commander Dewey','Dewey'],
}
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    texts[os.path.basename(p)[:-12]] = norm(gzip.open(p, 'rt', errors='ignore').read())
for p in sys.argv[1:]:
    texts[os.path.basename(p)[:-4]] = norm(open(p, errors='ignore').read())
print('volumes searched:', len(texts))
for e, phs in PH.items():
    for ph in phs:
        hits = [v for v, t in texts.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
