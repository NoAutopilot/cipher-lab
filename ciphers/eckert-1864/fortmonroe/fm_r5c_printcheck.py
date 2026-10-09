#!/usr/bin/env python3
"""FM-R5c (9 Oct 2026): letters-only phrase grep of the FM-R5c entries' decoded phrases AND rare names/numbers in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5751/2': ['every vessel which can be useful', 'send to Fort Monroe every vessel', 'if you have not already done so send', 'vessels which can be useful in ferrying', 'ferrying troops and trains', 'Quartermaster General Eckert vessel ferrying'],
 'F2 5722/0': ['not to build any farther than White House', 'farther than White House until further orders', 'Bickford has a cipher', 'word from Coldwell', 'Bickford', 'up 3 down 4 up 6', 'number of lines indicated as follows'],
 'F3 5783/1': ['made a raid on the cattle herd near Coggins Point', 'cattle herd near Coggins Point', 'captured the entire herd', 'Coggins Point', 'entire herd 2400', 'order by telegraph from Monroe', 'send 1200 head tomorrow', 'Lieutenant Colonel Morgan Harpers Ferry'],
 'F4 5822/0': ['Rice Dupont and Sedgwick', 'Rice Dupont Sedgwick', 'remaining troops to Monroe', 'if the Rice Dupont', 'embarking the troops with all possible dispatch', 'transfer them', 'Beckwith Colonel Webster'],
 'F5 5616/1': ['I have no steamers now that I can send to sea', 'no steamers now that I can send', 'steamers will be here bound', 'cant send them far', 'if they are bound to Port Royal', 'for General Rucker from Biggs'],
 'F6 5624/0': ['my Chief Quartermaster is much in need of assistant quartermasters', 'much in need of assistant quartermasters', 'highly important that four efficient and experienced assistant quartermasters', 'efficient and experienced assistant quartermasters', 'Lieutenant Colonel Bugs', 'good ones recommended by Colonel'],
 'F7 5827/2': ['I have sent a scout towards Hicksford', 'scout towards Hicksford', 'companies of cavalry in same direction', 'to hold crossing of Blackwater', 'South Quay to hold', 'Rations and forage ready at a moments notice', 'ready at moment notice', 'Hicksford Shepley'],
 'F8 5632/0': ['very fast captured blockade runner', 'blockade runner is I am told about to be sold in', 'about to be sold in New York', 'in the old business', 'she ought to be seized', 'so much in want of vessels', 'how do you like that plan'],
 'F9 5794/1': ['propose Logan for Hookers present command', 'propose Logan for Hooker', 'Hooker go to Missouri', 'Expect to reach City Point', 'What is your opinion in respect to this proposition', 'Have just arrived and will go on immediately', 'Logan Hooker command Missouri'],
 'F10 5609/1': ['captured J H Maddox', 'Maddox on the Virginia shore', 'boxes of tobacco worth some', 'confidential agent of the War Department', 'have him in custody', 'Maddox', 'what shall I do with him'],
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
