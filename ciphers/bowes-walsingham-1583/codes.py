#!/usr/bin/env python3
"""Numerical name-codes of Bowes's letters of 7 Apr 1583 (Surtees CLXXXVII) and 31 Jul 1583 (CCXXXIX-CCXL).
Reads codes_scan.tsv (made by codes_scan.py from the Surtees 1842 OCR) and audit_csp6_tokens.tsv (HTRC token
counts of CSP Scotland vi, running text unreadable), writes codes.tsv: one row per occurrence in the two letters,
with the collated identification and grade. Identifications are judgements recorded in IDS below (LANE R4 E,
24 Sept 2026); --check exits 1 if codes.tsv is stale."""
import csv, re, sys, collections
LETTERS = {'CLXXXVIL': ('CLXXXVII', '7 Apr 1583', 22906, 23047, (369, 371)),
           'CCXL.': ('CCXL', '31 Jul 1583', 29445, 29640, (564, 567))}
IDS = {  # code: (identification, grade, one-line reasoning / what would settle it)
 '189': ('John Graham, 3rd Earl of Montrose', 'C', "Tomokiyo 24 Sept 2026: MS f.196 has 189 where the Surtees print has 'Montrosse' (CLXXXVII); CSP vi p.371 token bag has Montrose and no 189. CCXL use (suit to 189 for Drumquhassell's relief) consistent with a council lord"),
 '870': ('Esme Stewart, Duke of Lennox', 'M', "in France with Cobham and Smallet Apr 1583; Glencairn commended Smallet to him; to 'return this summer into 70' with French forces (CLXXXIX); in Scotland 1582 entertaining Venables (CXVIII); last use Apr 1583, before Lennox's death 26 May 1583. Settle: Bowes/Cary cipher key (the 'cypher left me by Sir George Cary', CLXXXVII) or a decipher with the name"),
 '91':  ('James VI, King of Scots', 'M', "C-candidate (GAPS59 3 Oct 2026, grade held at M because this brief allows C only from Boyd): Bowes's own clear statement in CXXI (8 Nov 1582, Surtees p.237): his man 'in figure for the King of Scots had wrongfully placed and set the figures of 31 for 91', so the 31s of CXVIII (2 Nov 1582) stand for 91; '223 shall be on his knees before 91 and council' (CCXXXVI, Gowrie's submission); 'offers to 91 and the lords' (CLXXXIX); 'advance 91 greatness' (CLXIII). CSP vi p.371 keeps 91 (x3, as Surtees). Settle: key"),
 '32':  ('Queen Elizabeth', 'C', "GAPS59 3 Oct 2026: Boyd CSP vi p.371 prints 'Finds the Queen of England [\"32\"] as well resolved to entertain the matter' where the Letter-Book copy of the same letter (CLXXXVII) prints 'her Majesty's resolution to entertain the matter': the original carries 32 at the position of 'her Majesty' (Boyd's printed reading, the F9 precedent). Earlier M basis: 'win 870 to 32 devotion', 'the minister of 32' (CLXXXVII); 'delivery of 0100 to 32' (CCXL); '32 hath shaken him off' (CCXXXVI). 32 the person, 000 the country (one-to-one, codes_collation.tsv)"),
 '54':  ('France (the French)', 'M', "'credit from 870 and others in 54' (a place, CLXXXVII); 'favour ... of 54, and chiefly of the duke of Guyse' (CCXL). CSP pp.371 and 567 keep 54. Settle: key"),
 '000': ('England', 'C', "GAPS59 3 Oct 2026: Boyd CSP vi p.568 prints 'shall be 50,000* sent to \"000\" in case he will agree thereto' where the Letter-Book copy of the same letter (CCXL) prints '5000 men sent shortly into England in case he will agree thereunto': the original carries 000 at the position of 'England' (Boyd's printed reading, the F9 precedent). Consistent uses: 'the man to come into 000' (CLXXXVII); 'friends in 000', 'seek a wife in 000' (CXVIII); 'an ambassador into 000 to intreat her Majesty' (CCLXVIII). Open: Boyd's '50,000*' against the Letter-Book's '5000 men' (asterisk = 'In cipher'; footnote unread)"),
 '149': ('Henri III, King of France', 'M', "'an ambassador ... from 149 into this realm' (CCXXXII); '23 had dealt with Mauvisier to persuade 140 [149] to send hither an ambassador' (CCXXXVI); '149 might chiefly advance 91 greatness' (CLXIII); heads both lists '149, 19, 29/23, and 85'. Alternative: Catherine de Medici. Not in CSP p.371 token bag. Settle: key or CSP p.371 running text"),
 '19':  ('Henri, Duke of Guise', 'M', "'149 and 19 will not give full credit ... until advertised by Manningville' (Maineville, Guise's agent, CLXXXIX); second in both lists after 149; '19 is come into Piccardy with the French army' (CXXIII, 1582). Alternative: Anjou. Weak. Settle: key"),
 '29':  ('probably = 23, Mary Queen of Scots (misprint or OCR for 23)', 'M', "occurs once only; the same list a week later reads '149, 19, 23, and 85' (CLXXXIX); 23 = Mary: '23 had dealt with Mauvisier', 'to have intelligence with 23 will satisfy G. Douglas' (CCXLIII), 'at the request of 23 an ambassador ... from 149'. Settle: print page image of p.405 and the MS f.196"),
 '85':  ('unread (candidates: King of Spain, the Pope, the Queen Mother, Archbishop Beaton)', '-', "only in the two lists '149, 19, 29/23, and 85' (CLXXXVII, CLXXXIX): a fourth foreign patron of Lennox and Mary; CSP p.567 has a token 85 in the 31 Jul entry, context unreadable. Settle: key or CSP p.567 text"),
 '223': ('William Ruthven, 1st Earl of Gowrie', 'M', "'223 shall be on his knees before 91 and council, to acknowledge his fault done at Ruthen' (CCXXXVI); in CCXL 223 cannot consent to condemn 'that act done by him and others' (the Ruthven raid); '91 doth stand so fast to 223' (CCLXVII, the treasurer); CSP p.566 keeps 223. Caveat: CCXL also prints 'Gowrye' in clear in the same passage. Settle: key or MS f.299"),
 '0100': ('unread (candidates: the King, Dumbarton Castle)', '-', "once only: Drumquhassell to be examined on 'what had passed betwixt 32 and him for the delivery of 0100 to 32' (CCXL). Not in CSP pp.564-567 token bags. Settle: key or CSP p.566-567 text"),
}
def pages(lines, lo, hi, first):
    p = {}; cur = first
    for i in range(lo, hi + 1):
        m = re.search(r'BOWES\s+CORRESPONDENCE\.?\s+\S*?(\d{3})\s*$|^\s*\S*?(\d{3})\s+BOWES', lines[i - 1])
        if m: cur += 1
        p[i] = cur
    return p
def main():
    T = open('corpus/correspondenceof00bowerich_djvu.txt', encoding='utf-8').read().split('\n')
    scan = list(csv.DictReader(open('codes_scan.tsv'), delimiter='\t'))
    csp = collections.defaultdict(dict)
    for r in csv.reader((l for l in open('audit_csp6_tokens.tsv') if not l.startswith('#')), delimiter='\t'):
        if r[0] == 'seq': continue
        csp[r[1]][r[2]] = int(r[3])
    first = {'CLXXXVIL': 404, 'CCXL.': 530}
    rows = []
    for key, (name, date, lo, hi, cp) in LETTERS.items():
        pg = pages(T, lo, hi, first[key])
        for r in scan:
            ln = int(r['line'])
            if not (lo <= ln <= hi) or r['code'] not in IDS: continue
            if key == 'CCXL.' and ln < 29449: continue
            other = collections.Counter(s['letter'] for s in scan if s['code'] == r['code'] and not (lo <= int(s['line']) <= hi) and int(s['line']) > 12000)
            cspc = ';'.join(f"p{p}:{csp[str(p)].get(r['code'], 0)}" for p in range(cp[0], cp[1] + 1))
            ident, grade, why = IDS[r['code']]
            rows.append([r['code'], f'{name} ({date})', str(pg[ln]), r['printed'], r['context'],
                         'token count only (running text unreadable): ' + cspc,
                         ' '.join(f'{k}x{v}' for k, v in sorted(other.items())) or '-', ident, grade, why])
    # 189 at CLXXXVII: the print gives the name, the MS the number (Tomokiyo's check), so the scan cannot see it.
    i = next(k for k, l in enumerate(T) if 'Mont-' in l and 22960 < k < 22980)
    ctx = re.sub(r'\s+', ' ', ' '.join(T[i - 2:i + 3]))
    rows.insert(0, ['189', 'CLXXXVII (7 Apr 1583)', '405', "Montrosse (print); 189 (MS f.196, Tomokiyo)", ctx,
                    'token count only: Montrose on p371, no 189 token on pp369-371', 'CCXL.x2', *IDS['189']])
    out = 'code\tletter\tsurtees_page\tprinted_as\tcontext_surtees\tcontext_csp\tother_occurrences_surtees\tidentification\tgrade\treasoning\n' + \
          ''.join('\t'.join(r) + '\n' for r in rows)
    if '--check' in sys.argv:
        ok = open('codes.tsv').read() == out
        print('OK: codes.tsv current' if ok else 'STALE: codes.tsv'); sys.exit(0 if ok else 1)
    open('codes.tsv', 'w').write(out)
    g = collections.Counter(IDS[r[0]][1] for r in rows); codes = {r[0] for r in rows}
    print(len(rows), 'occurrences,', len(codes), 'codes; occurrences by grade', dict(g),
          '; codes by grade', dict(collections.Counter(IDS[c][1] for c in codes)))
main()
