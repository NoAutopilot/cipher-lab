#!/usr/bin/env python3
"""FV-L16a (10 Oct 2026; copied from fv_l15a_apply.py): write the status.json rows, second-opinion prompts and SECOND-OPINIONS-QUEUE.tsv rows for the six N3 entries of
AUDIT.md "## AUDIT (FV-L16a)" (E509 E511 E514 E506 E508 E521). Idempotent: skips a row whose title/label already exists.
Run from the repository root after a rebase."""
import json, os
R = 'https://github.com/NoAutopilot/cipher-lab/tree/main/ciphers/eckert-1864'
SAFE_TAIL = ('; not located in the Official Records ser. I vols. 42 and 46, ORN ser. I vol. 11, Butler\'s correspondence vol. V, The Papers of '
             'Ulysses S. Grant vol. 13 by Google Books snippet search, O\'Brien\'s Telegraphing in Battle or the Huntington\'s full-text search (searched 10 Oct 2026).')
E = [
 dict(id='E509', page=310, ptr=5854, pct=92.3, depth='D3',
      title="Webster, Fort Monroe, to Col. Dodge at Army of the James headquarters, 4 Jan 1865 5 PM: the Ben De Ford is not here; the full list went to Butler; the C. C. Leary sent; the Montauk there; only the Alliance and the Western Metropolis at Monroe (E509)",
      safe="on 4 Jan 1865 at 5 p.m. Fort Monroe (Col. R. C. Webster) answered Col. George S. Dodge at Army of the James headquarters that the Ben De Ford was not there, that the full list of boats had gone to General Butler that morning with a copy held by Ainsworth, that the C. C. Leary had since been sent, that the Montauk was there if wanted (telegraph Bradley at once), that no other vessel was at Monroe but the Alliance and the hospital boat Western Metropolis, and that the boats sent so far fully complied with General Grant's orders",
      gap="N3 one audit (FV-L16a), weak: the request it answers is printed (Dodge to Webster, OR I/46 pt 2 pp.34-35 = holder 5853/0) and O'Brien's diary (Telegraphing in Battle pp.179-180) records the cipher exchange; not N4: Grant Papers vol. 13 by snippets only, NARA RG 92/107 unread",
      comp='12 H + 1 M of 13 code-word groups ("Dodge", final "Webster" plain names; "Orcey" M)',
      sent="On 4 Jan 1865 Webster told Dodge the Ben De Ford was not at Fort Monroe and the full list of boats had gone to Butler that morning.",
      check="code: Knox/Knave = Butler, wreathe = Telegraph, Wicoff = West(ern Metropolis), John = Grant; external (non-statistical): OR I/46 pt 2 pp.34-35 Dodge to Webster, 4 Jan, 'Please send me a full and complete list of the boats ... If possible, send the Ben De Ford for headquarters boat'; O'Brien, Telegraphing in Battle pp.179-180, 4 Jan, 'Colonel Dodge making arrangements with Colonel Webster ... in cipher'; p.211 Ainsworth captain of the port at Fort Monroe",
      so_ctx="Official Records ser. I vol. 46 pt 2 pp.34-35 (Dodge to Webster, 4 Jan 1865, the request this answers: the full list of boats, the Ben De Ford for headquarters boat); J. E. O'Brien, Telegraphing in Battle (1910) pp.179-180 (diary, 4 Jan: Dodge and Webster arranging Terry's expedition in cipher), p.211 (Ainsworth, captain of the port). All are different texts.",
      so_title="Webster to Dodge: the Ben De Ford not at Fort Monroe, the list sent to Butler, 4 Jan 1865",
      head="Ft Monroe Jan 4 / 65 / R. O'Brien Hd Qrs. A. J.", reading="[5 PM] for [Colonel] George Dodge [.] The Ben De Ford is not here [.] Full list was sent to [Butler] this AM [.] Ainsworth has copy with him [.] Since sending the list to [Butler] I have been ordered to send the C. C. Leary and she has gone [.] The Montauk is there and if you need her [telegraph] Bradley at once [.] There is no other vessel here except the Alliance and the hospital boat [West]ern Metropolis [.] The boats sent thus far fully comply with the orders of [Grant] Orcey (M) Webster / Geo. D. Sheldon"),
 dict(id='E511', page=311, ptr=5855, pct=92.3, depth='D3',
      title="Howell, City Point, for Rawlins, to Webster at Fort Monroe, 4 Jan 1865 5.30 PM: two light-draft steamers, not over five feet, like the Eliza Hancox and the Winants, to be held ready at Monroe (E511)",
      safe="on 4 Jan 1865 at 5.30 p.m. Captain W. T. Howell at City Point told Colonel Webster at Fort Monroe that General Rawlins required two light-draft steamers, drawing not over five feet, able to go with the other vessels and stand rough weather, held in readiness at Monroe with a good supply of coal -- boats like the Eliza Hancox and the Winants would answer -- and asked whether they were available",
      gap="N3 one audit (FV-L16a); not N4: Grant Papers vol. 13 by snippets only, NARA RG 92/107 unread",
      comp='12 H + 1 M of 13 code-word groups ("Webster", "William" plain; "ditto" M)',
      sent="On 4 Jan 1865 Rawlins asked for two light-draft steamers drawing not over five feet, like the Eliza Hancox and the Winants, to be held ready at Fort Monroe.",
      check="code: peach = 2, person = 5, shelby = General, animal/appian = Monroe, nutmeg = Available; external (non-statistical): OR I/46 pt 2 p.90 Terry's order, the steam-tug Eliza Hancox with the fleet; ORN I/11 pp.~574-575 the army tug Eliza Hancox at Fort Fisher, 13 Jan",
      so_ctx="Official Records ser. I vol. 46 pt 2 p.90 (Terry's sailing and landing orders: the steam-tug Eliza Hancox to receive the troops); Official Records of the Union and Confederate Navies ser. I vol. 11 pp.~574-575 (ship logs, 13-14 Jan 1865: the army tug Eliza Hancox). Neither is this telegram.",
      so_title="Rawlins asks for two light-draft steamers like the Eliza Hancox and the Winants at Fort Monroe, 4 Jan 1865",
      head="City Point Jan. 4 / 65 / Geo D Sheldon Ft Monroe", reading="[5.30 PM] Webster [.] [2] light draft steamers [,] not over [5] feet [,] suitable for going with the other vessels and standing rough weather will be required and [General] Rawlins wishes them held in readiness at [Monroe] [.] boats similar to the Eliza Hancox and the Winants will answer purpose [.] if they are at [Monroe] or near there he wishes them held in readiness and prepared at once for the service required [.] a good supply coal only will be required on them [.] please inform me if these vessels ditto (M) [available] [signed] W. T. Howell / S. H. Beckwith"),
 dict(id='E514', page=314, ptr=5858, pct=100.0, depth='D3',
      title="Ingalls, City Point, to Col. Webster at Fort Monroe, 5 Jan 1865 1 PM: 350 troops without transportation sent down by river steamer to sail with the rest; the C. C. Leary wanted for special service; the Blackstone may go to the medical department (E514)",
      safe="on 5 Jan 1865 at 1 p.m. General Ingalls told Colonel Webster at Fort Monroe that some 350 troops for whom there was no transportation would be sent down in a river steamer at once, to be put on a sea-going steamer in time to sail with the rest; that the C. C. Leary was required for special service; and that if he could dispense with the Blackstone he might turn her over to the medical department",
      gap="N3 one audit (FV-L16a); not N4: Grant Papers vol. 13 by snippets only, NARA RG 92/107 unread",
      comp='12 H of 12 code-word groups ("Webb steer" = Webster plain-phonetic; "way worner" = Steam(er) H)',
      sent="On 5 Jan 1865 Ingalls sent 350 troops without transportation down to Fort Monroe by river steamer to be put on a sea-going steamer.",
      check="code: pebble prolong and mandate = 350, whinny = Troops, whig = Transportation, windpipe = River, weaseler/wayworn = Steam(er); external (non-statistical): OR I/46 pt 2 p.22 Rawlins, 3 Jan, troops of a vessel too large to go up 'will be sent to Fort Monroe in river transports'; OR I/46 pt 1 p.166 the C. C. Leary reporting 7 Jan for Abbot's siege train",
      so_ctx="Official Records ser. I vol. 46 pt 2 p.22 (Rawlins to Morgan, 3 Jan 1865: troops will be sent to Fort Monroe in river transports), p.90 (the Blackstone in Terry's sailing order, 10 Jan); vol. 46 pt 1 p.166 (Abbot: the C. C. Leary reported 7 Jan and was loaded with the siege train). None is this telegram.",
      so_title="Ingalls to Webster: 350 troops by river steamer, the C. C. Leary for special service, the Blackstone to the medical department, 5 Jan 1865",
      head="City Point Jan. 5 / 65 / Sheldon Ft Monroe", reading="[1 PM] [Colonel] Webster (Webb steer) [.] there are some [300] and [50] [troops] for whom there is no [transportation] they will be sent in [river] [steam]er at once to your place please have them put on sea going [steam]er in time to sail with the rest [.] the C. C. Leary is required for special service [.] if you can dispense with Blackstone you may turn her over to the medical department [signed] Ingalls / S. H. Beckwith"),
 dict(id='E506', page=308, ptr=5852, pct=100.0, depth='D2',
      title="Howell, City Point, for Rawlins, to Webster at Fort Monroe, 4 Jan 1865 1 PM: have the steamers named started? none reported from Jamestown (E506)",
      safe="on 4 Jan 1865 at 1 p.m. Captain W. T. Howell at City Point told Colonel Webster at Fort Monroe that General Rawlins wished to know whether the steamers named in his dispatch had started, as they had not been reported from Jamestown",
      gap="N3 one audit (FV-L16a), short (6 code groups); not N4: Grant Papers vol. 13 by snippets only, NARA RG 92/107 unread; the ledger's own reply is E507",
      comp='6 H of 6 code-word groups ("Webster", "William" plain)',
      sent="On 4 Jan 1865 Rawlins asked whether the steamers named had started, as none had been reported from Jamestown.",
      check="code clause: [General] ran lines (Rawlins) wishes to know if the [steam]ers named in your dispatch have started yet for this point, they haven't yet been [report]ed from James town; external: context only (OR I/46 pt 2 pp.21-22 the fleet's sailing, 3 Jan) and the ledger's reply E507",
      so_ctx="Official Records ser. I vol. 46 pt 2 pp.21-22 (Rawlins and Morgan on the fleet at Fort Monroe, 3 Jan 1865), p.35 (Dodge's request for the list of boats). The ledger's reply is E507. None is this telegram.",
      so_title="Rawlins asks whether the steamers named have started from Fort Monroe, 4 Jan 1865",
      head="City Point Jan 4 / 65 / Geo. D. Sheldon Ft Monroe", reading="[1 PM] [4] Webster [.] [General] Rawlins wishes to know if the [steam]ers named in your dispatch have started yet for this point [.] they haven't yet been [report]ed from Jamestown [signed] W. T. Howell / S. H. Beckwith"),
 dict(id='E508', page=309, ptr=5853, pct=100.0, depth='D2',
      title="Webster, Fort Monroe, to Capt. Howell at City Point, 4 Jan 1865 3 PM: the C. C. Leary just in and leaving for City Point with ten days' coal; send the Montauk if you can spare her (E508)",
      safe="on 4 Jan 1865 at 3 p.m. Colonel Webster at Fort Monroe told Captain W. T. Howell, quartermaster at City Point, that the C. C. Leary was just in and leaving at once for City Point, that she answered the description required and had ten days' coal, and that Monroe needed the Montauk if City Point could spare her",
      gap="N3 one audit (FV-L16a), short (7 code groups); not N4: Grant Papers vol. 13 by snippets only, NARA RG 92/107 unread",
      comp='7 H of 7 code-word groups ("William", "Webster" plain; "Walrus" = Signature added)',
      sent="On 4 Jan 1865 Webster reported the C. C. Leary in at Fort Monroe and leaving for City Point with ten days' coal.",
      check="code clause: The C. C. Leary is just in and leaves immediately for [City Point] she answers the description you required and has [10] days coal; external: the ship's movement only (OR I/46 pt 1 p.166, the Leary at Broadway Landing 7 Jan), not the text",
      so_ctx="Official Records ser. I vol. 46 pt 1 p.166 (Abbot: the C. C. Leary reported 7 Jan 1865 and was loaded with the siege train); vol. 46 pt 2 p.21 (Webster to Howell, another telegram). None is this telegram.",
      so_title="Webster to Howell: the C. C. Leary leaves Fort Monroe for City Point, 4 Jan 1865",
      head="Ft Monroe Jan 4 / 65 / S. H. Beckwith City Point", reading="[3 PM] for [Captain] W. T. Howell a [Quartermaster] [.] The C. C. Leary is just in and leaves immediately for [City Point] [.] She answers the description you required and has [10] days coal [.] If you can spare the Montauk we need her here [signed] Webster &c. / Geo. D. Sheldon"),
 dict(id='E521', page=317, ptr=5861, pct=100.0, depth='D3',
      title="Beckwith, City Point, to Sheldon at Fort Monroe, 6 Jan 1865: find out at once whether General Butler has left Monroe, when and where bound; don't mention who asked (E521)",
      safe="on 6 Jan 1865 S. H. Beckwith at City Point asked G. D. Sheldon at Fort Monroe to find out at once whether General Butler had left Monroe, and if so when and where bound, not to mention who had asked, and to keep him posted",
      gap="N3 one audit (FV-L16a), short (4 code groups); not N4: Grant Papers vol. 13 by snippets only, NARA RG 107 unread",
      comp='4 H of 4 code-word groups',
      sent="On 6 Jan 1865 Beckwith asked Sheldon to find out quietly whether General Butler had left Fort Monroe.",
      check="code: Knox = Butler, stomach = Left, animal = Monroe; external (non-statistical): O'Brien, Telegraphing in Battle pp.180-181, 5 Jan 'General Butler went to Fort Monroe', 6 Jan 'General Butler not yet returned'; OR I/46 pt 2 p.52 Grant to Lincoln, 6 Jan, asking for Butler's removal",
      so_ctx="J. E. O'Brien, Telegraphing in Battle (1910) pp.180-181 (diary: Butler went to Fort Monroe 5 Jan, not returned 6 Jan, relieved 8 Jan); Official Records ser. I vol. 46 pt 2 p.52 (Grant to Lincoln, 6 Jan 1865, cipher, asking prompt action on Butler's removal). Neither is this telegram.",
      so_title="Beckwith asks Fort Monroe, quietly, whether General Butler has left, 6 Jan 1865",
      head="City Point Jan'y 6 1865 / Geo D Sheldon Ft Monroe", reading="please ascertain immediately if [Butler] has [left] [Monroe] & if so when & when bound [.] don't mention that I enquired keep me posted / S. H. Beckwith"),
]
st = json.load(open('status.json'))
have = {r.get('title') for r in st['results'] if isinstance(r, dict)}
n = 0
for e in E:
    doc = f"Huntington mssEC 25 (obj 5952) p.{e['page']}, pointer {e['ptr']}, {e['id']}"
    title = 'Eckert 1864 (Fort Monroe ledger): ' + e['title']
    if title in have: continue
    st['results'].append({
        'link': R, 'key': 'period', 'audit_refs': ["AUDIT.md '## AUDIT (FV-L16a)'"], 'audit_status': 'one audit', 'superseded_by': '',
        'depth_by': 'FV-L16a verifier (account 1)', 'depth_date': '10 Oct 2026', 'decode_status': 'Partially decrypted', 'date': '10 Oct 2026',
        'kind': 'reading', 'claim_scope': 'completed-reading', 'fields_source': "eckert-1864/AUDIT.md '## AUDIT (FV-L16a)' section 4",
        'reading_version': 'FM65 readers 10 Oct 2026 (reading.md), grades as in AUDIT (FV-L16a) s.3 (fixes pending in s.5)',
        'unresolved_spans': 'none' if e['pct'] == 100.0 else 'see AUDIT (FV-L16a) s.3 (M tokens)',
        'depth_unread': {'names_codes': '0', 'other': '0'}, 'depth_pct': e['pct'], 'grade': 'N3', 'plaintext_novelty': 'N3', 'mapping_novelty': 'N3',
        'title': title, 'line': 'Read at grade H with War Department Cipher No. 1: ' + e['safe'] + SAFE_TAIL, 'gap': e['gap'], 'depth': e['depth'],
        'completeness': e['comp'], 'phrases': [doc], 'document_id': doc, 'documents': [doc], 'depth_sentence': e['sent'], 'depth_check': e['check'],
        'depth_note': e['comp']})
    n += 1
json.dump(st, open('status.json', 'w'), indent=2, ensure_ascii=False); open('status.json', 'a').write('\n')
print('status rows added', n)
TPL = open('ciphers/eckert-1864/second-opinions/PROMPT-chatgpt-e517.md').read()
head_end = TPL.index('THE ITEM'); tail_start = TPL.index('HOW TO REPORT')
q = open('SECOND-OPINIONS-QUEUE.tsv').read()
for e in E:
    lab = 'SO-ECKERT-' + e['id']; low = e['id'].lower(); p = f"ciphers/eckert-1864/second-opinions/PROMPT-chatgpt-{low}.md"
    if not os.path.exists(p):
        item = (f"THE ITEM\n- Source: Thomas T. Eckert Papers, Huntington Library, San Marino, mssEC 25 (\"Ciphers Received and Sent\", Fort Monroe) p.{e['page']} "
                f"(digital pointer {e['ptr']}), headed \"{e['head']}\", {e['id']}, https://hdl.huntington.org/digital/collection/p16003coll11/id/{e['ptr']}. "
                f"Read with War Department Cipher No. 1 (Huntington mssEC 41).\n"
                f"- Reading (code words in brackets, as corrected by our verifier, AUDIT (FV-L16a) s.3): \"{e['reading']}\"\n"
                f"- Context we already know: {e['so_ctx']}\n"
                "- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading.md,\n"
                "  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key.md, search log\n"
                "  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section \"AUDIT (FV-L16a)\").\n\n"
                "WHERE WE HAVE LOOKED: Official Records ser. I vols. 42 pt 3 and 46 pts 1-3 and ORN ser. I vol. 11 (full text, by phrase and by name); Butler's "
                "Private and Official Correspondence vol. V; J. E. O'Brien, Telegraphing in Battle (1910); The Papers of Ulysses S. Grant vol. 13 by Google Books "
                "snippet search; Internet Archive full-text search across all collections; the Huntington's CONTENTdm full-text search across the whole Eckert collection.\n\n"
                "WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)\n- The Papers of Ulysses S. Grant vol. 13 notes page by page; "
                "NARA RG 92, 107 and 393; Google Books; HathiTrust; JSTOR; newspapers of the following week.\n\n")
        body = TPL[:head_end] + item + TPL[tail_start:]
        body = body.replace('SO-ECKERT-E517', lab).replace('chatgpt-e517', f'chatgpt-{low}')
        body = body.replace('Fort Monroe to Baltimore: the Quartermaster General countermands any order sending the Baltic to Monroe, 6 Jan 1865', e['so_title'])
        open(p, 'w').write(body)
    if lab + '\t' not in q:
        q += f"{lab}\tciphers/eckert-1864\t{p}\t2026-10-10\tqueued\t\t\n"
open('SECOND-OPINIONS-QUEUE.tsv', 'w').write(q)
print('SO done')
