#!/usr/bin/env python3
"""FV-L15a (10 Oct 2026): write the status.json rows, second-opinion prompts and SECOND-OPINIONS-QUEUE.tsv rows for the five N3 entries of
AUDIT.md "## AUDIT (FV-L15a)" (E555 E568 E541 E576 E575; E536 is N1 and gets none). Idempotent: skips a row whose title/label already exists.
Run from the repository root after a rebase."""
import json, os
R = 'https://github.com/NoAutopilot/cipher-lab/tree/main/ciphers/eckert-1864'
SAFE_TAIL = ('; not located in the Official Records ser. I vols. 46-47, ORN ser. I vol. 11, Butler\'s correspondence vol. V, The Papers of Ulysses '
             'S. Grant vols. 13-14 by Google Books snippet search, Chronicling America or the Huntington\'s full-text search (searched 10 Oct 2026).')
E = [
 dict(id='E555', page=360, ptr=5904, pct=96.2, depth='D3',
      title="Rucker, Washington, via City Point to Fort Monroe, 9 Feb 1865: Schofield's corps and about 5,000 of Meagher's division shipped; two divisions of the 23rd Corps, 306 mule teams and 102 ambulances still waiting; 2,500 sail tomorrow (E555)",
      safe="on 9 Feb 1865 General Rucker's dispatch, sent from Washington through City Point to Fort Monroe, reported that Schofield's corps and about 5,000 of Meagher's division had shipped from Washington and Annapolis, that two divisions of the 23rd Corps (about 10,000 men) with their horses, three or four batteries, 306 mule teams and wagons and 102 horse ambulances were still waiting, and that 2,500 of these troops would sail the next morning",
      gap="N3 one audit (FV-L15a), weak: the sibling row 5904/0 is printed (OR I/46 pt 2; Grant Papers vol. 13 note) and this row was not found there by 7 snippet queries; not N4: Grant Papers vols. 13-14 by snippets only, ORN I/12 unreachable, NARA RG 92/107 unread; Washington's copy in another cipher at mssEC 18 pointer 9957",
      comp='51 H + 2 M of 53 code-word groups ("promise" and "pledge for spit" M for sense)',
      sent="On 9 Feb 1865 Rucker reported 2,500 of the 23rd Corps troops waiting at Washington would sail the next morning, with 306 mule teams and 102 horse ambulances still to ship.",
      check="code: Kisses pelton = Schofield's Corps, quitman = Division, spartan/Spafford = Horse, pagans = Batteries, whelp = Tomorrow read passim; external (non-statistical): OR I/47 pt 2 pp.354-355 Rucker's A.Q.M., 8 Feb, to embark about 2,550 men of the 2nd Div., 23rd Corps, from Alexandria at 7 a.m. on the 10th; p.306 Halleck, 5 Feb, over 2,000 of Meagher's division off; holder 8569, 8572 Meagher's division at Annapolis",
      so_ctx="Official Records ser. I vol. 47 pt 2 pp.354-355 (Rucker's A.Q.M., 8 Feb: about 2,550 men to embark from Alexandria on the 10th), p.306 (Halleck, 5 Feb), p.192 (Meagher's division to Annapolis); vol. 46 pt 2 and The Papers of Ulysses S. Grant vol. 13 print the telegram just above it on the same ledger page (Halleck to Grant at Fort Monroe, 9 Feb, Rucker and the ice). All are different telegrams.",
      so_title="Rucker to Fort Monroe: Schofield's and Meagher's troops shipped, the 23rd Corps still waiting, 9 Feb 1865",
      head="City Point Feb. 9 - 1865 / Geo. D. Sheldon", reading="[Washington] [9th] [12.30] Glass ring alls (Ingalls?) forwarded [Grant]'s [information] [.] Dispatch received [6] for [men] [,] [1] [battery] and [440] [horses] [1000] [Schofield]'s [corps] with about [5000] of Meagher's [division] shipped from here and Annapolis [.] still waiting while [2] [division]s of [23] [corps] [,] about [10000] [men] [,] the [horse]s of regimental and staff officers [3] or [4] [batteries] [,] [306] mule teams and wagons and [102] [horse] ambulances and ditto [.] [2500] of these [troops] will sail from here [tomorrow] morning and remainder [as soon as] ships arrive and are prepared and loaded [signed] D H Rucker [Brigadier General] etc S. H. Beckwith"),
 dict(id='E568', page=379, ptr=5923, pct=100.0, depth='D2',
      title="R. O'Brien, Wilmington, to Maj. Eckert via Fort Monroe, 26 Feb (forwarded 5 Mar) 1865: Schofield orders a line to Fort Fisher and double lines to Goldsboro; construction parties, relays, operators and tools wanted (E568)",
      safe="on 26 Feb 1865 R. O'Brien at Wilmington told Major Eckert, through Fort Monroe on 5 Mar, that General Schofield had directed a telegraph line from Wilmington to Fort Fisher and double lines from Wilmington and from Morehead City to Goldsboro, and asked for two construction parties, 100 miles of material, 20 relays, 20 operators and the men and tools listed, to be sent to New Bern",
      gap="N3 one audit (FV-L15a); not N4: Grant Papers vols. 13-14 by snippets only, ORN I/12 unreachable, NARA RG 107 (Military Telegraph) unread",
      comp='35 H of 35 code-word groups ("relays", "hatchets" plain)',
      sent="On 26 Feb 1865 O'Brien asked Eckert for 20 relays, 20 operators and two construction parties for Schofield's lines from Wilmington and Morehead City to Goldsboro.",
      check="code clause: King directs ... a double line from here to Camargo [Goldsboro] ... from More head City to Census [Goldsboro] ... fortune [Newbern], all numerals H; external: place only (OR I/47 pt 2 p.~580 Schofield's headquarters at Wilmington on 25 Feb), not content",
      so_ctx="Official Records ser. I vol. 47 pt 2 p.~580 (Schofield's headquarters at Wilmington, 25 Feb 1865). Nothing on the telegraph construction itself located.",
      so_title="O'Brien at Wilmington asks Eckert for telegraph parties, relays and operators for Schofield's lines to Goldsboro, 26 Feb 1865",
      head="Ft Monroe Mar. 5 - 1865 / Maj. Eckert, Washington", reading="[Wilmington] February [26] to [Major] Thomas T. Eckert Superintendent &c [.] [Schofield] arrived here this morning [.] directs that a line be built at once from here to [Fort] Fisher and that it is [necessary] to have a double line from here to [Goldsboro] he also wishes me to start at same time a double line from Morehead City to [Goldsboro] this will necessitate [2] construction parties [,] [100] [miles] more material [20] relays [20] operators [8] construction [men] [1] good foreman [6] diggers [8] shovels [4] vices and straps [6] axes [4] hatchets [4] pliers and climbers [.] I have explained to the [General] the difficulty of getting operators but assured him you will do all in your power to supply [.] These [men] and supplies should be sent to [Newbern] I will send instructions to that place by which they can be guided [.] Please hurry the operators and instruments along Very respectfully Yours R. O'Brien / Geo D. Sheldon"),
 dict(id='E541', page=343, ptr=5887, pct=96.2, depth='D3',
      title="Washington to Fort Monroe, 24 Jan 1865: Rucker orders the steamer Nevada and every sea-going steamer on to City Point; Wise tells Commander Lynch the Bureau has no such torpedoes (E541)",
      safe="on 24 Jan 1865 Washington told Colonel Webster, quartermaster at Fort Monroe, through Sheldon, that the steamer Nevada would arrive in a day or two with recruits and was to go on to City Point after landing them, with every other sea-going steamer reaching Monroe in the next five or six days (signed Rucker), and told Commander Lynch of the St. Lawrence that the Bureau of Ordnance had no torpedoes of the kind he named, that they would take months to prepare, and asked whether the rebel torpedoes on hand, those on the Stromboli or those sent from the ordnance yard would not answer (signed H. A. Wise)",
      gap="N3 one audit (FV-L15a), weak: message 2's substance is relayed in print by Lynch (ORN I/11 p.634); the same telegram's Washington copy is E85 (mssEC 18 pointer 9943, unread); not N4: Grant Papers by snippets only, ORN I/12 unreachable, NARA RG 45/92 unread",
      comp='25 H + 1 M of 26 code-word groups ("Webster", "saint", "Ordnance" plain; "audit" M)',
      sent="On 24 Jan 1865 Wise told Lynch the Bureau of Ordnance had no torpedoes of the kind he named and asked whether those on the Stromboli would not answer.",
      check="code: weaseler/wayworn = Steam(er), wafers = Recruits, Animal/appian = Monroe, walpole = Rebel read passim; external (non-statistical): ORN I/11 p.634 Lynch, 24 Jan, 'The Bureau of Ordnance can not furnish the torpedoes required ... whether those on board the Stromboli ... will not answer'; p.151 Wise, 6 Dec 1864, torpedoes forwarded from the ordnance yard; holder 8529 the Nevada leaving New York for Fort Monroe with recruits",
      so_ctx="Official Records of the Union and Confederate Navies ser. I vol. 11 p.634 (Lynch to Parker, 24 Jan 1865, relaying the Bureau's answer in his own words) and p.151 (Wise to Lynch, 6 Dec 1864); the Huntington's clear book pointer 8529 (New York, 22 Jan: the Nevada to leave for Fort Monroe with recruits). The same telegram's Washington copy is in mssEC 18 at pointer 9943.",
      so_title="Washington to Fort Monroe: the Nevada and the sea-going steamers to City Point; no torpedoes for Commander Lynch, 24 Jan 1865",
      head="Washington Jan. 24 - 1865 / Geo D. Sheldon Ft Monroe Va.", reading="[1 PM] for [Colonel] Webster [Quartermaster] [Monroe] [Steam]er Nevada will be at [Monroe] in a day or [2] with [recruits] please order her to City [Point] immediately after they have landed also all other sea-going [steam] vessels that may reach [Monroe] during the next [5] or [6] days [signed] Rucker / another for [Commander] Lynch ship Saint Lawrence [Norfolk] [Telegram] received no torpedoes [of the] kind you name are [available] audit (as it? M) will take months to prepare them [.] besides the Bureau does not know for what purpose these are intended [.] will not the [rebel] torpedoes on hand or those on board the Stromboli or those sent [from the] ordnance yard answer [?] [signed] H A Wise Chief Bureau / T. T. Eckert"),
 dict(id='E576', page=389, ptr=5933, pct=96.4, depth='D3',
      title="Gordon, Norfolk, to Ord via Fort Monroe, 15 Mar 1865: the guide Boyle is here; the Blackwater cannot be crossed without pontoons except near the Army of the Potomac; Broad Ford, 22 miles from Suffolk, is the best place (E576)",
      safe="on 15 Mar 1865 General Gordon at Norfolk told General Ord that he had seen the guide Boyle, who would accompany any expedition; that the Blackwater could not be crossed without pontoons except near the Army of the Potomac's lines; that Broad Ford, 22 miles from Suffolk, was the best place, the river there being 125 yards wide; and that several bridges were standing on the Nottoway",
      gap="N3 one audit (FV-L15a), weak: its substance is summarised by Ord to Grant, 16 Mar (OR I/46 pt 3 p.9); not N4: Grant Papers vol. 14 by snippets only, ORN I/12 unreachable, NARA RG 393 unread",
      comp='27 H + 1 M of 28 code-word groups ("Black" plain; "villager" M)',
      sent="On 15 Mar 1865 Gordon reported the guide Boyle at hand and Broad Ford, 22 miles from Suffolk, as the best crossing of the Blackwater.",
      check="code: rusty = Ford, Genoa = Suffolk, windsor = River, patents = Bridges, oyster torch attica = Army of the Potomac; external (non-statistical): OR I/46 pt 3 p.9 Ord to Grant, 16 Mar 8.30 a.m., 'The Blackwater ... cannot be forded except near the Army of the Potomac. Cavalry would have to have a ferry or pontoons'; OR I/46 pt 2 p.993 Gordon, 15 Mar 6.30 p.m., Boyle sent for",
      so_ctx="Official Records ser. I vol. 46 pt 3 p.9 (Ord to Grant, 16 Mar 1865 8.30 a.m., summarising the crossing) and vol. 46 pt 2 p.993 (Gordon to Ord, 15 Mar 6.30 p.m., Boyle 'I have sent for him'); pp.978-979, 992 the same exchange. All are different telegrams.",
      so_title="Gordon to Ord: the guide Boyle, the Blackwater crossings and Broad Ford, 15 Mar 1865",
      head="Ft Monroe Mar 15/65 / J. H. Emerick H'dqrs A. J.", reading="[Norfolk] to [Ord] [.] I have just seen the guide Boyle [.] he will be here ready to accompany any [expedition] [.] There is no place that the Blackwater can be [crossed] unless near the [Army] [of the] [Potomac] without [pontoon]s (villager, M) [.] Broad [Ford] is the best place [.] It is [22] [miles] from [Suffolk] [.] The [river] there is [100] and [25] yards wide [.] The Nottoway has several [bridges] standing [signed] George H. Gordon [Brigadier General] / Geo D. Sheldon"),
 dict(id='E575', page=387, ptr=5931, pct=100.0, depth='D3',
      title="City Point to Gordon, Norfolk, for Ord, 15 Mar 1865 5 PM: gunboat draught to Suffolk, a cavalry landing on the Nansemond, pontoons for 500 cavalry to cross to the Nottoway; come up tonight if Sumner's cavalry reaches Norfolk (E575)",
      safe="on 15 Mar 1865 at 5 p.m. City Point asked General Gordon at Norfolk, for General Ord, how much water his gunboats could draw to Suffolk, whether there was a point on the banks of the Nansemond where cavalry could land, covered by gunboats if necessary, and whether a party of about 500 cavalry would have to carry pontoons to cross to the Nottoway; he could come up that night if Sumner's cavalry came to Norfolk",
      gap="N3 one audit (FV-L15a), weak: answered point by point in Gordon's printed reply (OR I/46 pt 2 p.993); not N4: Grant Papers vol. 14 by snippets only, ORN I/12 unreachable, NARA RG 393 unread",
      comp='24 H of 24 code-word groups ("summers" = Sumner\'s and "nancy" (Nansemond) plain)',
      sent="On 15 Mar 1865 City Point asked Gordon whether 500 cavalry would need pontoons to cross to the Nottoway and whether cavalry could land on the Nansemond.",
      check="code: sharons/shannons = Gunboats, panama/pacific = Cavalry, village = Pontoon, plum = Cross, Meriden = Ord read passim; external (non-statistical): OR I/46 pt 2 p.993 Gordon's 6.30 p.m. reply: 'Army gun-boats can go to Suffolk. Cavalry can land at several points on the Nansemond ... pontoons ... necessary ... will leave word where the landing should be for Sumner's cavalry'",
      so_ctx="Official Records ser. I vol. 46 pt 2 p.993 (Gordon's reply of 6.30 p.m., 15 Mar 1865, answering these questions), pp.978-979 (Ord to Gordon, 14 Mar 9 p.m.), p.992 (Gordon, 15 Mar 12 m., 'I have no pontoons'). All are different telegrams.",
      so_title="City Point asks Gordon about gunboats to Suffolk, landing cavalry on the Nansemond and pontoons, 15 Mar 1865",
      head="City Point, Mar. 15 - 1865 / Geo D. Sheldon, Ft Monroe", reading="[5 PM] [15] for [General] George H. Gordon [Norfolk] how much water can your [gunboat]s teacup (draw?) to [Suffolk] [,] and is there no [point] on the Banks [of the] Nansemond where [cavalry] could land [,] covered if [necessary] by [gunboat]s [,] would a party say [500] [cavalry] have to carry [pontoon]s to [cross] to the Nottoway [?] you can come up tonight if Sumner's [cavalry] comes to [Norfolk] as they are expected to do leave word where they had better land [signed] [Ord] send answer to Mister Emerick / S. H. Beckwith"),
]
st = json.load(open('status.json'))
have = {r.get('title') for r in st['results'] if isinstance(r, dict)}
n = 0
for e in E:
    doc = f"Huntington mssEC 25 (obj 5952) p.{e['page']}, pointer {e['ptr']}, {e['id']}"
    title = 'Eckert 1864 (Fort Monroe ledger): ' + e['title']
    if title in have: continue
    st['results'].append({
        'link': R, 'key': 'period', 'audit_refs': ["AUDIT.md '## AUDIT (FV-L15a)'"], 'audit_status': 'one audit', 'superseded_by': '',
        'depth_by': 'FV-L15a verifier (account 1)', 'depth_date': '10 Oct 2026', 'decode_status': 'Partially decrypted', 'date': '10 Oct 2026',
        'kind': 'reading', 'claim_scope': 'completed-reading', 'fields_source': "eckert-1864/AUDIT.md '## AUDIT (FV-L15a)' section 4",
        'reading_version': 'FM65 readers 10 Oct 2026 (reading.md), grades as in AUDIT (FV-L15a) s.3 (fixes pending in s.5)',
        'unresolved_spans': 'none' if e['pct'] == 100.0 else 'see AUDIT (FV-L15a) s.3 (M tokens)',
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
                f"- Reading (code words in brackets, as corrected by our verifier, AUDIT (FV-L15a) s.3): \"{e['reading']}\"\n"
                f"- Context we already know: {e['so_ctx']}\n"
                "- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading.md,\n"
                "  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key.md, search log\n"
                "  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section \"AUDIT (FV-L15a)\").\n\n"
                "WHERE WE HAVE LOOKED: Official Records ser. I vols. 46 pts 1-3 and 47 pt 2 and ORN ser. I vol. 11 (full text, by phrase and by name); Butler's "
                "Private and Official Correspondence vol. V; The Papers of Ulysses S. Grant vols. 13-14 by Google Books snippet search; Internet Archive full-text "
                "search across all collections; Chronicling America; the Huntington's CONTENTdm full-text search across the whole Eckert collection.\n\n"
                "WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)\n- ORN ser. I vol. 12; The Papers of Ulysses S. Grant vols. 13-14 notes page by page; "
                "NARA RG 92, 107 and 393; Google Books; HathiTrust; JSTOR; newspapers of the following week.\n\n")
        body = TPL[:head_end] + item + TPL[tail_start:]
        body = body.replace('SO-ECKERT-E517', lab).replace('chatgpt-e517', f'chatgpt-{low}')
        body = body.replace('Fort Monroe to Baltimore: the Quartermaster General countermands any order sending the Baltic to Monroe, 6 Jan 1865', e['so_title'])
        open(p, 'w').write(body)
    if lab + '\t' not in q:
        q += f"{lab}\tciphers/eckert-1864\t{p}\t2026-10-10\tqueued\t\t\n"
open('SECOND-OPINIONS-QUEUE.tsv', 'w').write(q)
print('SO done')
