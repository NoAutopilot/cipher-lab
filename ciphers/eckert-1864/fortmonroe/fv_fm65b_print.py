#!/usr/bin/env python3
"""FV-FM65b (10 Oct 2026): letters-only phrase grep of decoded phrases of E502 E507 E512 E520 E530 E532 over the cached
print-check volumes (sources/ia-fulltext/print-check/*.gz) plus scratch djvu texts given as arguments, then KWIC for rare
names in the scratch texts. A miss is a search result, not a verdict (rule 10). Usage: fv_fm65b_print.py [scratch.txt ...]"""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'E502': ['which you have been and are now coaling and watering', 'turn them over to Colonel Morgan', 'chief commissary to be loaded',
          'inform him as soon as the vessels are ready to receive them', 'wishes to know what number of troops each steamer will carry',
          'what number of troops each steamer', 'are ready for service', 'coaling and watering'],
 'E507': ['all the steamers named had left here before', 'had left here before 9 a m', 'if the steamer Russia is at Monroe',
          'in time for a flag ship', 'in time for a flag-ship', 'send her here in time', 'steamer Russia'],
 'E512': ['Eliza Hancox has already been sent', 'Winants is hardly capable', 'the Seneca at Bermuda', 'have the Winants in order',
          'also the tug D D Porter', 'bring down a tug to-morrow', 'hardly capable of going'],
 'E520': ['were all ordered to Baltimore', 'I have not heard from them since except the Baltic', 'the Baltic at 11 p m',
          'which was at Baltimore this morning', 'Ariel General Sedgwick Victor and Illinois'],
 'E530': ['have sailed in perfect order', 'sailed in perfect order', 'Sedgwick Ariel and Ashland', 'Ariel 973 men', 'Ariel 973'],
 'E532': ['transportation for 4000 men', 'transportation for 4,000 men', 'fifty six-mule teams complete', '50 six-mule teams complete',
          'mule teams complete', 'what time can this transportation report here', 'what time can this transportation'],
}
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    texts[os.path.basename(p)[:-12]] = norm(gzip.open(p, 'rt', errors='ignore').read())
raw = {}
for p in sys.argv[1:]:
    k = os.path.basename(p)[:-4]; raw[k] = open(p, errors='ignore').read(); texts[k] = norm(raw[k])
print('volumes searched:', len(texts))
for e, phs in PH.items():
    for ph in phs:
        hits = [v for v, t in texts.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
for name in ['Winants', 'Hancox', 'Russia', 'Ashland', 'Seneca', 'D. D. Porter', 'Howell', 'Webster', 'G. W. Bradley', 'mule teams',
             'flag-ship', 'Sedgwick', 'perfect order', '973']:
    for k, t in raw.items():
        for m in re.finditer(re.escape(name), t):
            s = ' '.join(t[max(0, m.start()-220):m.end()+220].split())
            if name in ('Russia', 'Sedgwick', 'Webster', 'Howell', 'flag-ship', '973', 'Seneca') and not re.search(r'Monroe|City Point|Baltimore|Rawlins|Ingalls|Morgan|Butler|transport|steamer|Terry|Porter|Dodge|Fisher', s):
                continue
            print('KWIC', name, '|', k, '|', s)
