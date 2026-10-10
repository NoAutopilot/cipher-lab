#!/usr/bin/env python3
"""FV-L16b (10 Oct 2026; copied from fv_l15a_apply.py): write the status.json rows, second-opinion prompts and SECOND-OPINIONS-QUEUE.tsv rows for the six
N3 entries of AUDIT.md "## AUDIT (FV-L16b)" (E518 E526 E527 E546 E553 E554), and the WORK-QUEUE.tsv AUD2-LEDGER16-<n> row. Idempotent: skips a row whose
title/label/job already exists. Run from the repository root after a rebase."""
import json, os
R = 'https://github.com/NoAutopilot/cipher-lab/tree/main/ciphers/eckert-1864'
SAFE_TAIL = ('; not located in the Official Records ser. I vols. 46-47, ORN ser. I vol. 11, Butler\'s correspondence vols. IV-V, The Papers of Ulysses '
             'S. Grant vol. 13 by Google Books snippet search, Internet Archive full-text search or the Huntington\'s full-text search (searched 10 Oct 2026).')
E = [
 dict(id='E518', page=320, ptr=5864, pct=100.0, depth='D3',
      title="Col. R. C. Webster, chief quartermaster, Fort Monroe, to Ingalls at City Point, 7 Jan 1865: will General Grant let Elias Smith, New York Tribune correspondent, pass on the next boat joining the expedition? (E518)",
      safe="on 7 Jan 1865 Col. R. C. Webster, chief quartermaster at Fort Monroe, asked Brig. Gen. Ingalls at City Point whether General Grant would let Elias Smith, correspondent of the New York Tribune, pass on the next boat joining the expedition; the Huntington holds only Smith's own request to Dana of the same morning (pointer 8510)",
      gap="N3 one audit (FV-L16b); not N4: Grant Papers vol. 13 by snippets only, NARA RG 92/107 unread, the Tribune of January 1865 unread",
      comp='10 H of 10 code-word groups ("Webster" plain, the signer)',
      sent="On 7 Jan 1865 Fort Monroe's chief quartermaster asked Ingalls whether Grant would let the Tribune's Elias Smith go on the next boat joining the Fort Fisher expedition.",
      check="code: france = New York, rape = Expedition, Judah = Grant, palate = Brigadier General, Eugenia = 9.30 AM read passim; external (non-statistical): holder 8510 (mssEC 25 p.32), Smith to Dana 9.20 AM 7 Jan asking War Department permission to go on the expedition; OR I/46 pt 2, Webster chief quartermaster at Fort Monroe (Grant to Berrien, 3 Jan); image 5864 re-read",
      so_ctx="The Huntington's clear book, mssEC 25 p.32 (pointer 8510): Elias Smith to C. A. Dana, Fort Monroe 7 Jan 1865 9.20 AM, asking the War Department's permission to go on the expedition (a different message); Official Records ser. I vol. 46 pt 2 names Col. R. C. Webster as chief quartermaster at Fort Monroe.",
      so_title="Webster at Fort Monroe asks Ingalls whether Grant will pass the Tribune's Elias Smith to the expedition, 7 Jan 1865",
      head="Ft Monroe Jan 7/65 / S. H. Beckwith City Point", reading="[9.30 AM] for [Brigadier General] Ingalls Chief [Quartermaster] [.] Mr Elias Smith Correspondent [New York] Tribune desires permission to go on next boat joining the [Expedition] [.] Please inform me if [General Grant] will permit me [him] to pass him and oblige [signed] [Colonel] Webster [Quartermaster]. Geo. D. Sheldon"),
 dict(id='E526', page=323, ptr=5867, pct=100.0, depth='D2',
      title="Fort Monroe quartermaster (Capt. William L. James) to Emerick at City Point, add to Ingalls's message, 9 Jan 1865: no other forage vessels here; no troops arrived or sailed; General Abbott not seen (E526)",
      safe="on 9 Jan 1865 the Fort Monroe quartermaster's office (Capt. William L. James, by direction of the chief quartermaster) added to Ingalls's message that there were no other forage vessels at Fort Monroe, that no troops had arrived or sailed, and that General Abbott had not been seen",
      gap="N3 one audit (FV-L16b), short (34 tokens); not N4: Grant Papers vol. 13 by snippets only, NARA RG 92 unread",
      comp='9 H + 1 S of 10 code-word groups ("William" plain)',
      sent="On 9 Jan 1865 Fort Monroe reported no other forage vessels there and no troops arrived or sailed, adding that General Abbott had not been seen.",
      check="code: shade = Forage, whiskey = Troops (S), Shelter = General, pilgrim = Captain, Vinton = Quartermaster read passim; context only: OR I/46 pt 2 p.105 Ingalls 12 Jan, half rations of forage at City Point; image 5867 re-read",
      so_ctx="Official Records ser. I vol. 46 pt 2 p.105 (Ingalls, 12 Jan 1865: half rations of forage at City Point); context only.",
      so_title="Fort Monroe to City Point: no forage vessels, no troops arrived or sailed, General Abbott not seen, 9 Jan 1865",
      head="Ft Monroe Jan. 9 - 1865 / J. H. Emerick City Point", reading="Add to Ingalls message after no other vessels of [Forage] here [.] No [Troops] arrived nor sailed [.] Have not seen [General] Abbott [.] By direction Chief [Quartermaster] [signed] William L. James [Captain] A. [Quartermaster]. Geo. D. Sheldon"),
 dict(id='E527', page=325, ptr=5869, pct=100.0, depth='D3',
      title="Fort Monroe to the War Department for approval, 12 Jan 1865: Lt. Col. Frank J. White, Eastville, 11 Jan, to Maj. George J. Carney, Superintendent of Negro Affairs, Norfolk: Butler is relieved, I think I will resign, what are you going to do? (E527)",
      safe="on 12 Jan 1865 Fort Monroe forwarded to the War Department, for approval, a telegram of 11 Jan from Lt. Col. Frank J. White at Eastville to Maj. George J. Carney, Superintendent of Negro Affairs at Norfolk: Butler is relieved, White thinks he will resign, and asks what Carney is going to do",
      gap="N3 one audit (FV-L16b); not N4: Grant Papers vol. 13 by snippets only, NARA RG 107 unread, Butler's own papers (LC) unread",
      comp='10 H of 10 code-word groups ("Negro" and "White" plain)',
      sent="On 11 Jan 1865, four days after Butler's removal, White at Eastville told Carney at Norfolk he thought he would resign; Fort Monroe held the telegram for the War Department's approval.",
      check="code: Knox = Butler, Tappan = Major, farmer = Norfolk, flag = 11, quadroon = Department read passim; external (non-statistical): OR I/46 pt 2 p.60 General Orders No. 1, Butler relieved 7 Jan 1865; p.711 and Butler Corr. V p.444, Frank J. White commanding at Eastville; image 5869 re-read",
      so_ctx="Official Records ser. I vol. 46 pt 2 p.60 (General Orders No. 1, 7 Jan 1865, Butler relieved), p.130 (Dodge, 11 Jan: 'sorry to learn General Butler is relieved'), p.711 (Frank J. White commanding at Eastville); Butler's Private and Official Correspondence vol. V p.444 (White at Eastville, Dec 1864).",
      so_title="White at Eastville to Carney at Norfolk, forwarded for approval: Butler is relieved, I think I will resign, 11-12 Jan 1865",
      head="Ft Monroe Jan. 12 - 1865 / Maj. Eckert, Wash'n.", reading="The [Follow]ing is forwarded to war [Department] for approval [.] Eastville January [11] to [Major] George J Carney Supt. Negro affairs [Norfolk] [.] [Butler] is relieved I think I will resign ditto What are you going to do [signed] Frank J White Lieut. [Colonel] and A A G. Geo. D. Sheldon"),
 dict(id='E546', page=346, ptr=5890, pct=100.0, depth='D3',
      title="Commodore Joseph Lanman, U.S.S. Minnesota, via Fort Monroe to Senator L. S. Foster at Willard's Hotel, 29 Jan 1865: ship ordered to Portsmouth, N.H.; I do not wish to go; have me detached here by telegraph; Lieut. Commander Parker can take the ship (E546)",
      safe="on 29 Jan 1865 Commodore Joseph Lanman of the U.S.S. Minnesota telegraphed Senator L. S. Foster at Willard's Hotel that his ship was ordered to Portsmouth, New Hampshire, that he did not wish to go, and asked to be detached there by telegraph, his executive officer Lieut. Commander Parker being able to take the ship; ORN ser. I vol. 11 p.725 prints only the Minnesota's departure for Portsmouth on 2 Feb",
      gap="N3 one audit (FV-L16b); not N4: ORN I/12 by be-api only, NARA RG 45 and RG 107 unread, Foster's papers unread",
      comp='8 H of 8 body code-word groups ("Hotel" plain; header "Washington" a known slip)',
      sent="On 29 Jan 1865 Lanman asked Senator Foster to have him detached by telegraph rather than take the Minnesota to Portsmouth, New Hampshire.",
      check="code: Asia = New Hampshire, wreathe = Telegraph, polka = Command, growl = Washington, Animal = Monroe read passim; external (non-statistical): ORN I/11 pp.724-725 Lanman 1-2 Feb 1865 'shall proceed forthwith to Portsmouth, N. H.'; Army and Navy Journal 1864, James Parker executive officer of the Minnesota; image 5890 re-read",
      so_ctx="Official Records of the Union and Confederate Navies ser. I vol. 11 pp.724-725 (Lanman to Porter, 1-2 Feb 1865: transfers the senior officer's duties, 'shall proceed forthwith to Portsmouth, N. H.'); Official Records ser. I vol. 46 pt 2 p.227 (Lanman at Hampton Roads, 24 Jan); Army and Navy Journal (1864): James Parker, executive officer of the Minnesota.",
      so_title="Commodore Lanman asks Senator Foster to have him detached rather than take the Minnesota to Portsmouth, 29 Jan 1865",
      head="Ft Monroe Jan 29 - 1865 / Maj. Eckert, Washington", reading="[Monroe] [9 AM] to Senator L. F. S. Faster [Foster] Willards Hotel [Washington] [.] Ship ordered to Portsmouth [New Hampshire] I do not wish to go Have me detached here by [Telegraph] my executive officer Lieut [Command]er Parker can take ship [signed] Joseph Land Man [Lanman]. Geo. D. Sheldon"),
 dict(id='E553', page=358, ptr=5902, pct=100.0, depth='D3',
      title="Brig. Gen. George H. Gordon via Fort Monroe to Ord, 8 Feb 1865 11 PM: suggests the command of the Eastern District go temporarily to General Vogdes, as all his time goes to the investigation (E553)",
      safe="on 8 Feb 1865 Brig. Gen. George H. Gordon suggested to General Ord that the command of the Eastern District be given temporarily to General Vogdes, since all his own time and attention went to the investigation; the Official Records print the outcome (General Orders No. 21 of 9 Feb, OR ser. I vol. 46 pt 2 p.504) and Ord's objection to Vogdes (p.348), not this telegram",
      gap="N3 one audit (FV-L16b); not N4: Grant Papers vol. 13 by snippets only, the Gordon commission's papers and NARA RG 393 unread",
      comp='9 H of 9 code-word groups',
      sent="On 8 Feb 1865 Gordon asked Ord to give the Eastern District to Vogdes for the time being so that he could keep at the investigation.",
      check="code: Mentor = Ord, polka = Command, Shelby = General, Palate = Brigadier General, Sarah = 11 PM read passim; external (non-statistical): OR I/46 pt 2 p.348 Ord to Grant 7 Feb (Vogdes to relieve Gordon on the commission; Vogdes unfit), p.504 General Orders No. 21, 9 Feb (Gordon temporarily to the District of Eastern Virginia); image 5902 re-read",
      so_ctx="Official Records ser. I vol. 46 pt 2 p.348 (Ord and Grant, 7 Feb 1865: Vogdes to relieve Gordon on the commission, Gordon to relieve Shepley; Ord's objection to Vogdes) and p.504 (General Orders No. 21, 9 Feb: Gordon temporarily assigned to the District of Eastern Virginia). These give the decision, not this telegram.",
      so_title="Gordon asks Ord to give the Eastern District to Vogdes while he finishes the investigation, 8 Feb 1865",
      head="Ft Monroe Feb 8 - 1865 / J. H. Emerick H'd Qrs A. J.", reading="[11 PM] for [Ord] [.] I would respectfully suggest that the purposes [of the] Commission be more advanced by placing the [Command] [of the] Eastern District temporarily in hands of [General] Vogdes as all my time and attention is devoted to the investigation [signed] George H Gordon [Brigadier General]. Geo. D. Sheldon"),
 dict(id='E554', page=358, ptr=5902, pct=77.8, depth='D2',
      title="Ord, Hd Qrs Army of the James, to Gordon via Fort Monroe, 8 Feb 1865 at 12: you will have to take the command for the present; the investigation can go on quietly at the same time (E554)",
      safe="on 8 Feb 1865 General Ord answered Gordon that he would have to take the command for the present, the investigation going on quietly at the same time, with a further word on General V[ogdes] not read; the Official Records print the outcome (General Orders No. 21 of 9 Feb, OR ser. I vol. 46 pt 2 p.504), not this telegram",
      gap="N3 one audit (FV-L16b), short (24 tokens), 'obtain' x2 unread; not N4: Grant Papers vol. 13 by snippets only, NARA RG 393 unread",
      comp='7 H + 2 M of 9 code-word groups ("obtain" x2 M, unread)',
      sent="Ord told Gordon he must take the district command himself for now and carry on the investigation quietly at the same time.",
      check="code: Mentor = Ord, polka = Command, palsy = Brigadier General, Topsy = 12 read passim; external (non-statistical): OR I/46 pt 2 p.504 General Orders No. 21, 9 Feb 1865, Gordon temporarily assigned to the District of Eastern Virginia; image 5902 re-read",
      so_ctx="Official Records ser. I vol. 46 pt 2 p.504 (General Orders No. 21, 9 Feb 1865: Gordon temporarily to the District of Eastern Virginia) and p.348 (Ord and Grant, 7 Feb, on Vogdes). Decision only, not this telegram.",
      so_title="Ord to Gordon: take the command for the present, the investigation can go on quietly, 8 Feb 1865",
      head="Hd Qrs A. J. Feb 8/65 / Geo D. Sheldon Ft Monroe", reading="[12] for [Brigadier General] Gordon [.] you will have to take the [Command] for the present the investigation can progress quietly at the same time [General] V will not obtain(?) [signed] [Ord]. It is obtain(?) very plain. Emerick"),
]
st = json.load(open('status.json'))
have = {r.get('title') for r in st['results'] if isinstance(r, dict)}
n = 0
for e in E:
    doc = f"Huntington mssEC 25 (obj 5952) p.{e['page']}, pointer {e['ptr']}, {e['id']}"
    title = 'Eckert 1864 (Fort Monroe ledger): ' + e['title']
    if title in have: continue
    st['results'].append({
        'link': R, 'key': 'period', 'audit_refs': ["AUDIT.md '## AUDIT (FV-L16b)'"], 'audit_status': 'one audit', 'superseded_by': '',
        'depth_by': 'FV-L16b verifier (account 1)', 'depth_date': '10 Oct 2026', 'decode_status': 'Partially decrypted', 'date': '10 Oct 2026',
        'kind': 'reading', 'claim_scope': 'completed-reading', 'fields_source': "eckert-1864/AUDIT.md '## AUDIT (FV-L16b)' section 4",
        'reading_version': 'FM65-B..E readers 10 Oct 2026 (reading.md), grades as in AUDIT (FV-L16b) s.3 (fixes pending in s.5)',
        'unresolved_spans': 'none' if e['pct'] == 100.0 else 'see AUDIT (FV-L16b) s.3 (M tokens)',
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
                f"- Reading (code words in brackets, as corrected by our verifier, AUDIT (FV-L16b) s.3): \"{e['reading']}\"\n"
                f"- Context we already know: {e['so_ctx']}\n"
                "- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading.md,\n"
                "  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key.md, search log\n"
                "  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section \"AUDIT (FV-L16b)\").\n\n"
                "WHERE WE HAVE LOOKED: Official Records ser. I vols. 46 pts 1-3 and 47 pt 2 and ORN ser. I vol. 11 (full text, by phrase and by name); Butler's "
                "Private and Official Correspondence vols. IV-V; G. H. Gordon, A War Diary (1882); J. E. O'Brien, Telegraphing in Battle (1910); The Papers of Ulysses S. Grant vols. 13-14 by Google Books snippet search; Internet Archive full-text "
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

wq = open('WORK-QUEUE.tsv').read()
if 'AUD2-LEDGER16-2\t' not in wq:
    note = ('"second audit eckert-1864 E518 E527 E546 E553 (N3 D3) and E526 E554 (N3 D2) (first audit AUDIT.md ""## AUDIT (FV-L16b)""), key period, Fort Monroe ledger '
            'mssEC 25 (obj 5952) pp.320-358 ptrs 5864/1 5867/2 5869/1 5890/2 5902/1-2, War Dept Cipher No. 1, 7 Jan-8 Feb 1865: Webster asks Ingalls about the '
            'Tribune correspondent Elias Smith (context holder 8510); no forage vessels or troops at Fort Monroe; White at Eastville to Carney, Butler relieved '
            '(OR I/46 pt 2 p.60); Lanman (Minnesota) to Senator Foster, ordered to Portsmouth NH (ORN I/11 p.725); Gordon and Ord on the Eastern District and '
            'Vogdes (OR I/46 pt 2 pp.348, 504). Opus 5.5, cap 2.5 per entry (15), box 30 per entry + 30 (210). A FIX job owes AUDIT (FV-L16b) s.5."')
    wq = wq.rstrip('\n') + '\n' + '\t'.join(['AUD2-LEDGER16-2', 'account-1', '.claude/briefs/runs/2026-10-10-acct1-lane-ledger16-jobs.md', 'Opus 5.5', '15', '210',
                                                'queued', '2026-10-10 15:2x', note]) + '\n'
    open('WORK-QUEUE.tsv', 'w').write(wq); print('WORK-QUEUE row added')
