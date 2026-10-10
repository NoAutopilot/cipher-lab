#!/usr/bin/env python3
"""CLEAR-SWEEP (10 Oct 2026, for LANE LEDGER-15): Huntington CONTENTdm full-text search (p16003coll11, CISOSEARCHALL, suppressfulltext=1) of 40 Fort Monroe entries,
two queries each (rare plain words of the derived reading). For every hit pointer other than the entry's own, scores the hit's transcription against the reading
(longest shared run of words; share of the reading's >=4-letter words found in a window around the hit). Writes raw JSON to argv[1] and a TSV of candidates.
Usage: clear_sweep_hdl.py SCRATCH START END   (query indices, to keep takes <= 40 requests). >= 3.2 s apart. A miss is a search result (rule 10)."""
import json, os, re, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
HERE = os.path.dirname(os.path.abspath(__file__))
R = {}
for l in open(os.path.join(HERE, '..', 'reading.md'), errors='ignore'):
    m = re.match(r'\*\*(E\d+) \| Page \d+ \| (\d+) \|', l)
    if m and m.group(1) not in R: R[m.group(1)] = (m.group(2), l)
Q = [  # (entry or CTRL, own pointer, query)
 ('CTRL', '5899', 'Dumbarton'), ('CTRL', '5907', 'Lynch torpedoes Wise Inspector'), ('CTRL', '5896', 'Mack party material'),
 ('E509', '5854', 'Montauk Metropolis Alliance'), ('E509', '5854', 'Leary Bradley Ainsworth'),
 ('E511', '5855', 'Hancox Winants'), ('E511', '5855', 'light draft steamers rough weather'),
 ('E514', '5858', 'Blackstone Leary Ingalls'), ('E514', '5858', 'Blackstone medical department'),
 ('E518', '5864', 'Tribune correspondent Smith Ingalls'), ('E518', '5864', 'Elias Smith Tribune'),
 ('E526', '5867', 'Emerick Abbott forage'), ('E526', '5867', 'forage Abbott troops sailed'),
 ('E527', '5869', 'Eastville Carney Norfolk'), ('E527', '5869', 'Carney White resign relieved'),
 ('E542', '5887', 'Saugus turn her back'), ('E542', '5887', 'Saugus Berrien half way'),
 ('E543', '5888', 'contingency headquarters field'), ('E543', '5888', 'absent several days'),
 ('E546', '5890', 'Portsmouth Hampshire detached executive Parker'), ('E546', '5890', 'Willards Faster Portsmouth'),
 ('E548', '5895', 'Annapolis President Point Lookout'), ('E548', '5895', 'Bates Lookout Annapolis'),
 ('E550', '5897', 'Blodget Schofield Annapolis'), ('E550', '5897', 'Schofield despatches Sherman Friday'),
 ('E553', '5902', 'Vogdes Gordon Commission Eastern District'), ('E553', '5902', 'Vogdes investigation command'),
 ('E554', '5902', 'Vogdes investigation quietly'), ('E554', '5902', 'Gordon command present Vogdes'),
 ('E558', '5912', 'Yorktown operators office Ord'), ('E558', '5912', 'Yorktown imperative operators'),
 ('E562', '5917', 'Washburne Johnson rascal'), ('E562', '5917', 'Johnson rascal escape guard'),
 ('E564', '5918', 'pilots monitors James River Bradley'), ('E564', '5918', 'out of pilots Navy monitors'),
 ('E566', '5919', 'Sumner Mounted Rifles Turner'), ('E566', '5919', 'Sumner Turner joined expedition'),
 ('E569', '5924', 'moving office Mrs Ord room'), ('E569', '5924', 'precedent accommodation office room'),
 ('E571', '5929', 'Glisson convoy Roberts Babcock'), ('E571', '5929', 'Glisson gunboat Rawlins convoy'),
 ('E574', '5931', 'River Queen Dealy Eckert boat'), ('E574', '5931', 'Dealy River Queen Sheldon'),
 ('E577', '5933', 'Hartsuff Abbot Gordon district'), ('E577', '5933', 'Hartsuff relieved continue command'),
 ('E506', '5852', 'Jamestown steamers Rawlins reported'), ('E506', '5852', 'steamers Jamestown started Rawlins'),
 ('E508', '5853', 'Leary Montauk Howell Webster'), ('E508', '5853', 'Montauk Leary City Point coal'),
 ('E521', '5861', 'mention enquired keep posted'), ('E521', '5861', 'Butler left Monroe enquired Beckwith'),
 ('E441', '5699', 'Yorktown West Point cable poles'), ('E441', '5699', 'No. 14 wire cable Yorktown'),
 ('E472', '5679', 'Sheridan James foraged Meigs'), ('E472', '5679', 'Sheridan forage Meigs'),
 ('E465', '5768', 'Shaffer New Orleans troops'), ('E465', '5768', 'Shaffer arrived General-in-Chief'),
 ('E447', '5827', 'Saugus Cole Porter six miles'), ('E447', '5827', 'Cole Saugus daylight'),
 ('E442', '5707', 'Homan Collings Williamsburg Jamestown'), ('E442', '5707', 'Bermuda landing cable City Point'),
 ('E474', '5829', 'Ingalls Webster Butler fleet left'), ('E474', '5829', 'Butler fleet left yet'),
 ('E471', '5577', 'Kilpatrick cable repaired ciphers'), ('E471', '5577', 'Kilpatrick cable repaired'),
 ('E470', '5814', 'Mahopac Canonicus Saugus'), ('E470', '5814', 'Mahopac monitors Porter'),
 ('E468', '5810', 'Butler meet tomorrow Monroe Admiral'), ('E468', '5810', 'Admiral Monroe Butler'),
 ('E443', '5785', 'yellow fever Newbern McDougall Horner'), ('E443', '5785', 'yellow fever Newbern'),
 ('E473', '5633', 'Edgar exchanges Clark'), ('E473', '5633', 'Edgar name exchanges orders'),
 ('E445', '5816', 'Baird Hendron instruments'), ('E445', '5816', 'Baird instruments Porter Butler'),
 ('E469', '5720', 'heavy firing battery Grant reached'), ('E469', '5720', 'continuous firing fifteen miles'),
 ('E466', '5638', 'Dunn endorsed believe a word'), ('E466', '5638', 'Dunn Butler endorsed'),
 ('E446', '5583', 'Cherrystone Dunn Baltimore American'), ('E446', '5583', 'Cherrystone operator Dunn'),
 ('E448', '5793', 'Manhattan wharf Secretary of War Dealy'), ('E448', '5793', 'Manhattan Dealy Bates posted'),
 ('E552', '5899', 'Dumbarton'), ('E557', '5907', 'submarine torpedoes immediate James River'), ('E557', '5907', 'Lynch Commander Inspector Ordnance'), ('E549', '5896', 'Mack party material'),
 ('E557', '5907', 'Lynch torpedoes'),
 ('E509', '5854', 'Metropolis Alliance'), ('E511', '5855', 'Winants'), ('E514', '5858', 'Blackstone'), ('E526', '5867', 'Abbott Emerick'),
 ('E527', '5869', 'Carney White'), ('E543', '5888', 'contingency army'), ('E546', '5890', 'Portsmouth Parker'), ('E553', '5902', 'Vogdes Gordon'),
 ('E558', '5912', 'Yorktown office'), ('E564', '5918', 'pilots Bradley'), ('E566', '5919', 'Sumner Mounted'), ('E569', '5924', 'moving office'),
 ('E571', '5929', 'Glisson Roberts'), ('E574', '5931', 'Dealy boat arrival'), ('E577', '5933', 'Hartsuff'), ('E506', '5852', 'Jamestown Rawlins'),
 ('E508', '5853', 'Montauk Webster'), ('E521', '5861', 'Beckwith enquired'), ('E441', '5699', 'Yorktown cable'), ('E472', '5679', 'Sheridan Meigs'),
 ('E447', '5827', 'Saugus Cole'), ('E442', '5707', 'Homan Collings'), ('E474', '5829', 'Ingalls Butler fleet'), ('E471', '5577', 'Kilpatrick ciphers'),
 ('E470', '5814', 'Mahopac Canonicus'), ('E468', '5810', 'Admiral 10.30'), ('E443', '5785', 'yellow Newbern'), ('E473', '5633', 'Edgar Clark'),
 ('E445', '5816', 'City of Hendron'), ('E469', '5720', 'Butler firing battery'), ('E466', '5638', 'Dunn Butler'), ('E446', '5583', 'Dunn Cherrystone'),
 ('E448', '5793', 'Manhattan Dealy'), ('E465', '5768', 'Shaffer'),
 ('E509', '5854', 'Ainsworth'), ('E527', '5869', 'Eastville'), ('E543', '5888', 'contingency'), ('E553', '5902', 'Vogdes'), ('E564', '5918', 'pilots monitors'),
 ('E574', '5931', 'River Queen'), ('E506', '5852', 'steamers Jamestown'), ('E441', '5699', 'West Point cable'), ('E474', '5829', 'fleet Webster'),
 ('E443', '5785', 'fever Newbern'), ('E473', '5633', 'Edgar'), ('E448', '5793', 'Manhattan Secretary'),
]
tok = lambda s: re.findall(r"[a-z]+", s.lower())
def body(line):
    line = line.split(' | ', 3)[3] if line.count(' | ') >= 3 else line
    line = re.sub(r'\[[^\]]*\]', ' | ', line); line = re.sub(r'\([^)]*\)', ' | ', line)
    return [tok(seg) for seg in re.split(r'\|', line)]
def lcs_run(seg_words, text_words):
    best = 0; pos = {}
    for i, w in enumerate(text_words): pos.setdefault(w, []).append(i)
    for seg in seg_words:
        for a in range(len(seg)):
            for j in pos.get(seg[a], []):
                k = 0
                while a + k < len(seg) and j + k < len(text_words) and seg[a + k] == text_words[j + k]: k += 1
                best = max(best, k)
    return best
if __name__ == '__main__':
    out = sys.argv[1]; s, e = int(sys.argv[2]), int(sys.argv[3]); n = 0
    for ent, own, q in Q[s:e]:
        url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/100/1/0/0/1/0/json"
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        except Exception as ex:
            print(f'{ent} {q!r}: ERROR {ex}'); n += 1; time.sleep(3.2); continue
        n += 1; recs = d.get('records', [])
        json.dump(d, open(os.path.join(out, f'q_{ent}_{q.replace(" ", "_")[:40]}.json'), 'w'))
        rw = body(R[ent][1]) if ent in R else []
        sig = {w for seg in rw for w in seg if len(w) >= 4}
        print(f'## {ent} own={own} q={q!r}: total {d.get("pager", {}).get("total")}')
        for r in recs:
            p = str(r.get('pointer')); tr = r.get('transc') or ''
            if not isinstance(tr, str): tr = ''
            tw = tok(tr); first = q.split()[0].lower()
            idx = next((i for i, w in enumerate(tw) if w.startswith(first[:5])), 0)
            win = tw[max(0, idx - 90): idx + 140]
            run = lcs_run(rw, win) if rw else 0
            cov = len(sig & set(win)) / max(1, len(sig))
            tag = 'OWN' if p == own else 'cand'
            print(f'  {tag} {p} ({r.get("title")}) run={run} cov={cov:.2f} :: ' + ' '.join(tr.split())[:0])
            if tag == 'cand' and (run >= 3 or cov >= 0.45):
                i0 = max(0, tr.lower().find(first)); print('      >>', ' '.join(tr[max(0, i0 - 200): i0 + 500].split()))
        time.sleep(3.2)
    print('requests', n)
