#!/usr/bin/env python3
"""BNE-PRES (15 Oct 2026): phrase map of period_decipherment_reconciled.tsv against Paz y Melia 1914 (IA elcronistaalonso0000unse)
by be-api fts. Presence + snippet only (page_num is not a page locator). <=15 requests, 2 s apart. Writes bne_pres_fts.tsv.
Usage: bne_pres_fts.py            (runs the PHRASES list; a no-hit with a variant queues the variant, until 15 requests)."""
import json, sys, time, urllib.parse, urllib.request
IDENT = 'elcronistaalonso0000unse'
UA = 'cipher-lab research script (contact via repository)'
# (label, line, part of letter, phrase as reconciled, normalised variant or '')
PHRASES = [
 ('P01','D01-02','beginning','dicho charles fazia de reduzir','dicho carlos hazia de reducir'),
 ('P02','D03','beginning','treze del dicho mes de setiembre',''),
 ('P03','D04','beginning','saberlo verdaderament soy maravillado','saberlo verdaderamente soy maravillado'),
 ('P04','D05','beginning','fecho al dicho charles',''),
 ('P05','D06','middle (control)','reposo al regno de navarra',''),
 ('P06','D06','middle','por no venir en effecto la reducion','por no venir en effecto la reduccion'),
 ('P07','D07-08','middle','ninguno de los agramonteses',''),
 ('P08','D12','middle','el dicho charles parezca',''),
 ('P09','D13','end','solamente charles darteida',''),
 ('P10','D14','end','non solo no lo destorbaria',''),
 ('P11','D14-15','end','mis fuerças lo procuraria','mis fuerzas lo procuraria'),
 ('P12','D04','beginning','por aquesta carta me scrive',''),
]
def q(ph):
    url = f'https://be-api.us.archive.org/fts/v1/search?q={urllib.parse.quote(chr(34)+ph+chr(34))}&identifier={IDENT}'
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    try:
        with urllib.request.urlopen(req, timeout=60) as r: d = json.load(r)
    except Exception as e:
        return None, str(e)[:80]
    hits = d.get('hits', {}).get('hits', [])
    sn = ' | '.join(str(h.get('highlight', {}).get('text', [''])[0]) for h in hits[:1]).replace('\t',' ').replace('\n',' ')
    return len(hits), sn
rows, n = [], 0
for lab, line, part, ph, var in PHRASES:
    for kind, p in (('as reconciled', ph), ('normalised', var)):
        if not p or n >= 15: continue
        if kind == 'normalised' and rows and rows[-1][5] not in ('0',): continue
        if n: time.sleep(2)
        h, sn = q(p); n += 1
        rows.append([lab, line, part, kind, p, '?' if h is None else str(h), sn[:300]])
        print(rows[-1], flush=True)
        if h is None: sys.exit('stopped: ' + sn)
with open('bne_pres_fts.tsv', 'w') as f:
    f.write('label\tlines\tpart\tform\tphrase\thits\tsnippet\n')
    for r in rows: f.write('\t'.join(r) + '\n')
print('requests', n)
