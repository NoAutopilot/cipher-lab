"""BRO-DF (9 Oct 2026): fold a fresh scripts/04_build_key.py tally into the hand-maintained key.tsv.

04_build_key.py rewrites key.tsv from scratch and would drop the hand rows and notes added since
(NEXT-BRO bare 9 and grade changes, D4-BROC ff, V-BRO24 code 24). This merge takes 04's output (argv[1])
and, per code: refreshes n_occurrences / entries / all_observed_letters; keeps the committed value and
grade wherever they differ from what 04 proposes (a hand override, or a vote 04 decides by tie order),
and says so in the note; adds codes 04 newly sees at their 04 value and grade. Codes 04 no longer
sees keep their committed row. Usage: python3 scripts/30_brodf_key_merge.py BUILD.tsv
"""
import csv, sys
ROOT = '/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712'
build = {r['code']: r for r in csv.DictReader(open(sys.argv[1], encoding='utf-8'), delimiter='\t')}
with open(f'{ROOT}/key.tsv', encoding='utf-8', newline='') as f:
    rd = csv.DictReader(f, delimiter='\t'); fields = rd.fieldnames; rows = list(rd)
TAG = 'BRO-DF 9 Oct 2026'
# rows whose committed tally comes from a later pass, not from 04: tally left as is, note only
KEEP = {'24': "row left as V-BRO24 set it (its n=31 tally is V-BRO24's own, not 04's; 04 alone now sees h:1 e:1)",
        '9': ("the m0290 Passage 2a idx82 witness ('indisposicoes', i) was re-read as the looped g-shaped sign 'g' "
              "(two blind Sonnet looks: same sign as a transcribed g; images/crops_brodf/s_A.jpg vs s_D.jpg), so this row "
              "keeps one witness only, m0292 Carta 101 idx29, a 9 with a stroke across its stem that both blind looks "
              "could not tell from g and both called different from the 9+- sign (s_B.jpg vs s_C.jpg); value i no longer "
              "has a firm witness, kept at M pending"),
        'ff': ("second witness: m0291 Carta 96 'Thesoureiro' (f.f -> ff, one sign) and m0290 Passage 2a idx81 "
               "'indisposicoes' (g -> ff, my read + both blind looks: a long f-like stroke), both s by context; neither enters "
               "04's tally because 03 needs an exact letter count and both entries miss it by one; grade left M")}
seen = set()
for r in rows:
    c = r['code']; seen.add(c); b = build.get(c)
    if c in KEEP:
        if TAG not in (r.get('note') or ''):
            r['note'] = ((r.get('note') or '') + f' | {TAG}: ' + KEEP[c]).strip(' |')
        continue
    if not b:
        continue
    moved = (b['n_occurrences'], b['all_observed_letters']) != (r['n_occurrences'], r['all_observed_letters'])
    if moved:
        old = f"n={r['n_occurrences']} {r['all_observed_letters']}"
        for k in ('n_occurrences', 'entries', 'all_observed_letters'):
            r[k] = b[k]
        msg = f"{TAG}: 04 tally moved ({old} -> n={b['n_occurrences']} {b['all_observed_letters']})"
        if (b['value'], b['grade']) != (r['value'], r['grade']):
            msg += f"; 04 would give {b['value']} {b['grade']}, committed {r['value']} {r['grade']} kept"
        if TAG not in (r.get('note') or ''):
            r['note'] = ((r.get('note') or '') + ' | ' + msg).strip(' |')
        print(c, msg)
for c, b in build.items():
    if c not in seen:
        b = dict(b); b['note'] = f'{TAG}: new row from 04 (appendix transcription fix, scripts/29_brodf_datafix.py)'
        rows.append({k: b.get(k, '') for k in fields}); print(c, 'added', b['value'], b['grade'])
with open(f'{ROOT}/key.tsv', 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(rows)
