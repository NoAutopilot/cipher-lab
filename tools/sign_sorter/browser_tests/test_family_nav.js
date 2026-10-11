// Owner rule R11 (tools/data/sorter_owner_requirements.tsv; 11 Oct 2026, Matignon f.110 sorter: "When I hit left or right keys while into
// one of the family, it moves to another symbol, but doesn't seem to be continuining in that family. I think it should, then when you hit
// the end of that family unit it stops. So I the human can easily click through and knock out a whole family with new cuts or moves."):
// a card opened from a pile in step 1 (a held tile -- a member, a set-aside tile, a question waiting in step 2 drawn in its pile -- or
// "View larger") walks THE FAMILY: every tile drawn under that family's heading, in the order on screen; it does not wrap, it stops at
// either end and says so in words (and in the buttons' own text, owner rule R07: never by colour alone); the position line reads
// "<n> of <N> in family <F>" and names the pile when the family has several; after a move, set aside, bad cut, trash, keep, new sign or a
// saved cut the card shows the NEXT sign of the same fixed list (a moved sign never shifts the order or drops the person into another
// family); after the last one it says the family is done and stays. Cards opened from the tray or "Check these first" keep their own
// lists and say which. A family of one pile walks exactly that pile's drawn tiles.
// Devices: a desktop (mouse; arrow keys and the Previous / Next buttons) and an iPhone 13 (touch through CDP; sideways swipes on the big
// sign and taps on the buttons). Also (desktop): after a mouse pick in "Move this tile to…", Left / Right walk the card and never pick
// the list's next entry (they used to move the shown sign). Zero page errors.
// Must catch: a pile card that stops at its pile's end inside a family of two piles; a waiting tile's card that walks the tray; a walk
// that wraps or leaves the family; a list that shifts after a move. Must NOT block: a page built without the tray (no waiting tiles:
// those checks print "skip"), a family of one pile (walks the pile).
// Usage: PW_EXE=/opt/pw-browsers/chromium NODE_PATH=$(npm root -g) node test_family_nav.js PAGE.html [SHOT.png]   (exit 1 on any FAIL)
// PAGE: tools/sign_sorter/browser_tests/make_fixtures.py's family.html or family_plain.html (family X: piles X and X-DOT; family Y: pile Y).
const { chromium, devices } = require('playwright'); const mock = require('./mock_db'); const path = require('path');
const PAGE = 'file://' + path.resolve(process.argv[2]), SHOT = process.argv[3];
let fails = 0; const errs = [];
const ok = (cond, msg, extra) => { console.log((cond ? 'ok   ' : 'FAIL ') + msg + (extra !== undefined ? '  [' + (typeof extra === 'string' ? extra : JSON.stringify(extra)) + ']' : '')); if (!cond) fails++; };
const skip = msg => console.log('skip ' + msg);
const C = page => page.evaluate(() => ({ open: !document.getElementById('ctx').hidden, sid: ctxSid, list: ctxList.slice(), pos: document.getElementById('ctxPos').textContent,
  end: (e => e && !e.hidden ? e.textContent : '')(document.getElementById('ctxEnd')), msg: document.getElementById('ctxMsg').textContent,
  prev: [document.getElementById('ctxPrev').disabled, document.getElementById('ctxPrev').textContent], next: [document.getElementById('ctxNext').disabled, document.getElementById('ctxNext').textContent],
  moves: JSON.stringify(moves) }));
// the families as drawn: [{name, piles: [{id, sids: [{sid, kind}]}]}], read from the page (headings, piles, tiles in DOM order)
const drawn = page => page.evaluate(() => [...document.querySelectorAll('#list section.fam')].map(sec => ({ name: sec.querySelector('h2').textContent.replace(/^Family /, ''),
  piles: [...sec.querySelectorAll('.pile')].map(p => ({ id: p.dataset.pile, sids: [...p.querySelectorAll(':scope > .tiles > .t[data-sid]')].map(t => ({ sid: t.dataset.sid,
    kind: t.classList.contains('wait') ? 'wait' : t.classList.contains('out') ? 'aside' : t.classList.contains('in') ? 'in' : 'member' })) })) })));
const flat = f => f.piles.flatMap(p => p.sids.map(x => x.sid));
const pileOfIn = (f, sid) => (f.piles.find(p => p.sids.some(x => x.sid === sid)) || {}).id;
const tileLoc = (page, sid) => page.locator('#list .pile .tiles > .t[data-sid="' + sid + '"]').first();

async function swipe(page, dx) {   // a sideways finger swipe on the big sign (CDP touch on the phone)
  await page.evaluate(() => document.getElementById('ctxBigW').scrollIntoView({ block: 'center' })); await page.waitForTimeout(120);
  const b = await page.locator('#ctxBigW').boundingBox(); const x = b.x + b.width / 2, y = b.y + b.height / 2;
  await mock.gesture(page, 'down', x, y);
  for (let i = 1; i <= 6; i++) { await mock.gesture(page, 'move', x + dx * i / 6, y + i); await page.waitForTimeout(16); }
  await mock.gesture(page, 'up', x + dx, y + 6); await page.waitForTimeout(200);
}

async function device(b, name, opts, touch) {
  const ctx = await b.newContext(opts); const store = await mock.install(ctx); const page = await ctx.newPage();
  page.on('pageerror', e => errs.push(name + ': ' + e.message));
  const ready = async () => { await page.waitForFunction(() => ready === true, null, { timeout: 8000 }); await page.waitForTimeout(300);
    await page.evaluate(() => { if (step !== 1) setStep(1); }); };   // the tray build lands on step 2; the piles are in step 1
  await page.goto(PAGE); await ready(); await page.waitForTimeout(300);
  const tray = await page.evaluate(() => TRAY_ON);
  // seed: in the family of two piles, two tiles of its first pile and one of its second set aside, one tile moved from the first to the second
  let fams = await drawn(page); const two = fams.find(f => f.piles.length >= 2), one = fams.find(f => f.piles.length === 1);
  ok(!!two && !!one, `${name}: the fixture has a family of two piles and a family of one`, fams.map(f => f.name + ':' + f.piles.map(p => p.id).join('+')).join(' '));
  if (!two || !one) { await ctx.close(); return; }
  const seed = await page.evaluate(([A, B]) => { const free = id => Object.keys(itemBySid).filter(s => homeOf[s] === id && !focusQ[s] && !itemBySid[s].r).sort();
    const a = free(A), bb = free(B); return { aside: [a[1], a[3], bb[0]].filter(Boolean), moveIn: a[5], A, B, home: Object.fromEntries([a[1], a[3], bb[0], a[5]].filter(Boolean).map(s => [s, homeOf[s]])) }; },
    [two.piles[0].id, two.piles[1].id]);
  store.docs.moves = store.docs.moves || {};
  seed.aside.forEach(s => { store.docs.moves[s] = { sid: s, from: seed.home[s], to: 'ASIDE', updated: '2026-10-11T03:40:00Z' }; });
  store.docs.moves[seed.moveIn] = { sid: seed.moveIn, from: seed.home[seed.moveIn], to: seed.B, updated: '2026-10-11T03:40:00Z' };
  await page.reload(); await ready(); await page.waitForTimeout(400);
  fams = await drawn(page); const F = fams.find(f => f.name === two.name), Y = fams.find(f => f.name === one.name), L = flat(F), N = L.length;
  const kinds = F.piles.flatMap(p => p.sids.map(x => x.kind));
  ok(kinds.filter(k => k === 'aside').length === 3 && kinds.includes('in'), `${name}: family ${F.name} draws its 3 set-aside tiles and the moved-in one`, kinds.join(','));
  if (tray) ok(kinds.includes('wait'), `${name}: ...and its questions waiting in step 2 (tray build)`, kinds.join(','));
  // the family the page itself would list: every tile now in one of its piles, set aside from one, or waiting in one (independent of the DOM)
  const want = await page.evaluate(ps => { const P = new Set(ps);
    return Object.keys(itemBySid).filter(s => (P.has(where(s)) && !(state[homeOf[s]] && state[homeOf[s]].outliers.includes(s) && !moves[s])) || (moves[s] === 'ASIDE' && P.has(homeOf[s])) || (preTrayed(s) && P.has(homeOf[s]))).sort(); },
    F.piles.map(p => p.id));
  ok(JSON.stringify(want) === JSON.stringify(L.slice().sort()), `${name}: the tiles drawn under "Family ${F.name}" are exactly the family's tiles (${N})`, { want, drawn: L });

  // 1. a hold on a tile of the SECOND pile walks the whole family, from that tile's place in it
  const k0 = L.indexOf(F.piles[1].sids[0].sid);
  await mock.hold(page, tileLoc(page, L[k0])); let c = await C(page);
  ok(c.open && c.sid === L[k0], `${name}: holding ${L[k0]} (pile ${F.piles[1].id}) opens its card`, c.sid);
  ok(JSON.stringify(c.list) === JSON.stringify(L), `${name}: the card's list is family ${F.name} in on-screen order, both piles, members then set aside${tray ? ' then waiting' : ''}`, c.list.join(','));
  ok(c.pos === `${k0 + 1} of ${N} in family ${F.name}, pile ${F.piles[1].id}`, `${name}: position line names the family and the pile`, c.pos);
  // 2. walk to the end: arrow keys (desktop) or swipes (phone); every step stays in the family; then the end stops and says so
  const stepFwd = touch ? () => swipe(page, -140) : () => page.keyboard.press('ArrowRight'), stepBack = touch ? () => swipe(page, 140) : () => page.keyboard.press('ArrowLeft');
  const how = touch ? 'swipe' : 'arrow key';
  let seen = [], okWalk = true;
  for (let i = k0 + 1; i < N; i++) { await stepFwd(); c = await C(page); seen.push(c.sid); if (c.sid !== L[i] || !c.pos.startsWith(`${i + 1} of ${N} in family ${F.name}`)) okWalk = false; }
  ok(okWalk, `${name}: ${how} right walks the family tile by tile to its end`, seen.join(','));
  ok(c.sid === L[N - 1] && c.next[0] && /End of family/.test(c.next[1]) && c.end === `Last of ${N} in family ${F.name}`, `${name}: at the last sign Next is off, reads "End of family", and the card says "Last of ${N} in family ${F.name}"`, [c.next, c.end]);
  await stepFwd(); c = await C(page);
  ok(c.sid === L[N - 1] && [c.msg, c.end].every(t => new RegExp(`Last of ${N} in family ${F.name} — that family is done`).test(t)), `${name}: one more ${how} right stops there (no wrap) and says the family is done, under the buttons too`, [c.sid, c.msg, c.end]);
  for (let i = N - 2; i >= 0; i--) await stepBack();
  c = await C(page);
  ok(c.sid === L[0] && c.prev[0] && /Start of family/.test(c.prev[1]) && c.end === `First sign in family ${F.name}`, `${name}: ${how} left walks back to the first sign; Previous is off, reads "Start of family", the card says "First sign in family ${F.name}"`, [c.sid, c.prev, c.end]);
  await stepBack(); c = await C(page);
  ok(c.sid === L[0] && /First sign in family/.test(c.msg) && /First sign in family/.test(c.end), `${name}: one more ${how} left stops there (no wrap) and says so`, [c.sid, c.msg, c.end]);
  ok(c.pos === `1 of ${N} in family ${F.name}, pile ${F.piles[0].id}`, `${name}: position line names the first pile there`, c.pos);
  // 3. the buttons
  const press = sel => touch ? page.tap(sel) : page.click(sel);
  await press('#ctxNext'); await press('#ctxNext'); c = await C(page); const b2 = c.sid; await press('#ctxPrev'); const c1 = await C(page);
  ok(b2 === L[2] && c1.sid === L[1] && !c1.prev[0] && !c1.next[0] && /Previous tile/.test(c1.prev[1]) && /Next tile/.test(c1.next[1]) && c1.end === '', `${name}: Next / Previous buttons step one sign; inside the family both are on, with their usual words`, [b2, c1.sid, c1.prev, c1.next]);
  // 4. decide sign after sign: the card always shows the NEXT sign of the same, fixed family list
  const other = (Y.piles[0] || {}).id; const L0 = JSON.stringify(L);
  const act = async (what, fn, check) => { const before = (await C(page)).sid, i = L.indexOf(before); await fn(); await page.waitForTimeout(250); const a = await C(page);
    ok(a.sid === L[i + 1] && JSON.stringify(a.list) === L0 && a.pos.startsWith(`${i + 2} of ${N} in family ${F.name}`) && (await check(before)),
      `${name}: ${what} on ${before}, then the card shows the next sign of family ${F.name} (${L[i + 1]}), the list unchanged`, [a.sid, a.pos, a.msg]); };
  const shown = async (sel, what) => { if (await page.isVisible(sel)) return true; skip(`${name}: ${what} is not offered on ${(await C(page)).sid}`); return false; };
  await act('Set aside', () => press('#ctxAside'), s => page.evaluate(s => moves[s] === 'ASIDE', s));
  if (await shown('#ctxKeep', 'Keep')) await act('Keep', () => press('#ctxKeep'), s => page.evaluate(s => !!checked[s], s));
  await act('a move to pile ' + other + ' (another family)', () => page.selectOption('#ctxDest', other), s => page.evaluate(([s, o]) => moves[s] === o, [s, other]));
  if (!touch) {   // the list kept the focus after a mouse pick, and the browser's arrow picked its next entry: a move per key press
    const a0 = await C(page); await page.focus('#ctxDest'); await page.keyboard.press('ArrowRight'); await page.waitForTimeout(200); const a1 = await C(page);
    ok(a1.moves === a0.moves && a1.sid === L[L.indexOf(a0.sid) + 1], `${name}: ArrowRight with "Move this tile to…" focused walks on and moves nothing`, [a0.sid, a1.sid, a1.moves === a0.moves]);
    await page.keyboard.press('ArrowLeft'); const a2 = await C(page); ok(a2.sid === a0.sid && a2.moves === a0.moves, `${name}: ...and ArrowLeft walks back`, a2.sid);
    ok(await page.evaluate(() => document.activeElement && document.activeElement.id !== 'ctxDest'), `${name}: ...the list gives the focus back`);
  }
  await act('Bad cut', () => press('#ctxBad'), s => page.evaluate(s => moves[s] === 'BAD-CUT', s));
  await act('Trash', () => press('#ctxTrash'), s => page.evaluate(s => moves[s] === 'NOT-LETTER', s));
  await act('a saved cut', async () => { await press('#ctxFix'); await page.waitForTimeout(150); await press('#fixRp'); await press('#fixSave'); }, s => page.evaluate(s => !!recuts[s], s));
  await act('New sign', () => press('#ctxNewB'), s => page.evaluate(s => !!newPiles[moves[s]], s));
  if (await shown('#ctxOut', '"Doesn’t belong: take out"')) await act('Doesn’t belong: take out', () => press('#ctxOut'), s => page.evaluate(s => moves[s] === 'OUT', s));
  c = await C(page); const back = L[L.indexOf(c.sid) - 1];
  if (touch) await swipe(page, 140); else await page.keyboard.press('ArrowLeft');
  const cb = await C(page); ok(cb.sid === back && JSON.stringify(cb.list) === L0, `${name}: stepping back shows the sign just decided (the list never shifts)`, cb.sid);
  // the last sign: a decision stays on it and says the family is done
  for (let i = L.indexOf(cb.sid); i < N - 1; i++) { if (touch) await swipe(page, -140); else await page.keyboard.press('ArrowRight'); }
  c = await C(page); ok(c.sid === L[N - 1], `${name}: walked on to the last sign`, c.sid);
  await press('#ctxAside'); await page.waitForTimeout(250); c = await C(page);
  ok(c.sid === L[N - 1] && /that family is done/.test(c.msg) && /that family is done/.test(c.end) && c.next[0], `${name}: Set aside on the last sign stays on it and says the family is done`, [c.sid, c.msg, c.end]);
  ok(c.list.every(s => L.includes(s)), `${name}: the whole walk stayed in family ${F.name}`);
  await press('#ctxClose'); await page.waitForTimeout(150);

  // 5. a family of one pile walks exactly that pile, and names no pile
  const YL = flat((await drawn(page)).find(f => f.name === one.name));   // as drawn now (a sign was moved into it above)
  await mock.hold(page, tileLoc(page, YL[1])); c = await C(page);
  ok(JSON.stringify(c.list) === JSON.stringify(YL) && c.pos === `2 of ${YL.length} in family ${Y.name}`, `${name}: family ${Y.name} (one pile) walks that pile's ${YL.length} drawn tiles`, [c.pos, c.list.join(',')]);
  await press('#ctxClose'); await page.waitForTimeout(150);
  // 6. "View larger" on the family's second pile opens on that pile's first tile, inside the family walk
  fams = await drawn(page); const F2 = fams.find(f => f.name === F.name), L2 = flat(F2), p2 = F2.piles[1];
  await page.locator('#pile_' + await page.evaluate(id => domKey(id), p2.id) + ' .ph .big').click(); await page.waitForTimeout(250); c = await C(page);
  ok(c.sid === p2.sids[0].sid && JSON.stringify(c.list) === JSON.stringify(L2) && c.pos === `${L2.indexOf(p2.sids[0].sid) + 1} of ${L2.length} in family ${F.name}, pile ${p2.id}`,
    `${name}: "View larger" on pile ${p2.id} walks family ${F.name} from that pile`, c.pos);
  await press('#ctxClose'); await page.waitForTimeout(150);
  // 7. a question waiting in step 2, drawn in its pile (the owner's case on Matignon: it walked the whole tray, 13 families)
  const w = F2.piles.flatMap(p => p.sids).find(x => x.kind === 'wait');
  if (!w) skip(`${name}: no question waiting in a pile (page built without the tray)`);
  else { await mock.hold(page, tileLoc(page, w.sid)); c = await C(page);
    ok(c.sid === w.sid && JSON.stringify(c.list) === JSON.stringify(L2) && c.pos.startsWith(`${L2.indexOf(w.sid) + 1} of ${L2.length} in family ${F.name}`) && (await page.evaluate(s => moves[s] === undefined, w.sid)),
      `${name}: holding the waiting question ${w.sid} in pile ${pileOfIn(F2, w.sid)} walks family ${F.name}, not the tray, and moves nothing`, c.pos);
    for (let i = L2.indexOf(w.sid); i < L2.length; i++) await stepFwd();
    c = await C(page); ok(c.sid === L2[L2.length - 1] && c.list.every(s => L2.includes(s)), `${name}: ...and stops at the family's end`, c.sid);
    await press('#ctxClose'); await page.waitForTimeout(150); }
  // 8. the other lists keep their own walk and say which (owner rule R05 unchanged: a hold opens the card, moves nothing)
  const tq = await page.evaluate(() => { const e = [...document.querySelectorAll('#trayTiles .t[data-sid]')].find(x => x.offsetParent); return e ? e.dataset.sid : null; });
  if (!tq) skip(`${name}: nothing in the tray`);
  else { const m0 = (await C(page)).moves; await mock.hold(page, page.locator('#trayTiles .t[data-sid="' + tq + '"]').first()); c = await C(page);
    const L3 = await page.evaluate(() => outList());
    ok(c.open && c.sid === tq && JSON.stringify(c.list) === JSON.stringify(L3) && /in the tray|questions in the tray|taken out, in the tray/.test(c.pos) && c.moves === m0, `${name}: a tray tile's card walks the tray and says so`, c.pos);
    await press('#ctxClose'); await page.waitForTimeout(150); }
  const fq = await page.evaluate(() => { const d = [...document.querySelectorAll('#focusTiles > div')].find(x => x.offsetParent && itemBySid[x.dataset.sid]); return d ? d.dataset.sid : null; });
  if (!fq) skip(`${name}: no "Check these first" box`);
  else { const m0 = (await C(page)).moves; await mock.hold(page, page.locator('#focusTiles > div[data-sid="' + fq + '"] .t')); c = await C(page);
    ok(c.open && c.sid === fq && /questions in "Check these first"/.test(c.pos) && c.moves === m0, `${name}: a "Check these first" card walks that box and says so`, c.pos);
    await press('#ctxClose'); await page.waitForTimeout(150); }
  if (SHOT) await page.screenshot({ path: SHOT.replace(/\.png$/, '') + '-' + name.replace(/\W+/g, '_') + '.png' });
  await ctx.close();
}

(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_EXE || '/opt/pw-browsers/chromium' });
  await device(b, 'desktop', { viewport: { width: 1280, height: 900 } }, false);
  await device(b, 'iPhone 13', { ...devices['iPhone 13'] }, true);
  await b.close();
  console.log('errors:', errs);
  console.log(fails || errs.length ? `FAILED (${fails} checks${errs.length ? ', ' + errs.length + ' page errors' : ''})` : 'ALL PASS');
  process.exit(fails || errs.length ? 1 : 0);
})();
