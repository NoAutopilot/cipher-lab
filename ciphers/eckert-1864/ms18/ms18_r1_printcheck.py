#!/usr/bin/env python3
"""MS18-R1 (8 Oct 2026): letters-only phrase grep of the decoded phrases of E200-E209 (and the step-0 skips) in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'E200 9696/0': ['Nellie Pentz', 'Eastern State and North Point', 'Eastern State North Point', 'Annapolis to transport colored troops to Hilton Head', 'coal and water for voyage out and back'],
 'E201 9819/2': ["Wilson's cavalry division moved out", "Grover's division", 'will move today by Snicker', "Snicker's Gap"],
 'E202 9875/2': ['appointed special inspector of cavalry Military Division of the Mississippi', 'Cavalry Bureau requests that', 'the whole matter of remounts', 'special inspector of cavalry'],
 'E203 9769/0': ['your command is rested and supplied', 'destroy the railroad at Charlottesville', 'destroy the railroad at Charlottesville and if possible also the canal', 'communicate with him directly by telegraph'],
 'E204 9823/2': ["Longstreet's corps and Fitz Hugh Lee's cavalry have passed", 'have passed this place to join Early', 'captured one of your trains', 'seventy or eighty wagons with five hundred mules'],
 'E205 9730/1': ['Militia raised in the Western States will be placed under your command', 'I propose to send some to Louisville Nashville', 'ordered to the field as fast as replaced by militia', 'To what other places shall I send them'],
 'E206 9751/0': ['Parkersburg to the Monocacy with their stations', 'all troops on or in the vicinity of the line of railroad from Parkersburg', 'line of railroad from Parkersburg to the Monocacy'],
 'E207 9923/3': ['send ocean steamers for three thousand troops', 'ocean steamers to report at Fort Monroe by Monday', 'with coal and water for fifteen days', 'larger transportation to be at Fort Monroe by Monday'],
 'E208 9703/0': ['impossible to supply the necessary transportation', 'send the mules of five hundred of your teams to Louisville', 'Your report of transportation shows over', 'shows over sixteen hundred teams'],
 'E209 9923/2': ['If there is an ocean steamer at Baltimore', 'water and coal at Fort Monroe', 'send her there and advise me by telegraph', 'give the names and capacity for further orders'],
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
