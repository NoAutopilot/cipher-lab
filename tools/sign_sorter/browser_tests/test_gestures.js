// Owner rule R05 (tools/data/sorter_owner_requirements.tsv, said six times, last on 9 Oct 2026: "One tap it takes the symbol out
// and puts it in my tbd pile. If I hold on the symbol open [the] symbol page."): ONE gesture rule on every page and in every box --
// a TAP takes the sign out into the "Taken out" tray, a HOLD opens the sign's card (#ctx: large, on its line, Fix the cut, the
// answer buttons) and MOVES NOTHING. Template 2026-10-08.2 to 2026-10-09.4 turned a touch hold into a drag (a fingertip's drift
// pulled the sign out of its pile), and its "Check these first" / "Most useful first" boxes opened the card on a TAP. Template
// 2026-10-09.5 fixed both; this test is the gate (tools/sorter_preflight.py check 6, `--gestures PAGE`).
//
// Devices: iPhone 13 and iPhone SE (Playwright device profiles; touch through CDP Input.dispatchTouchEvent, the path a phone takes)
// and a desktop mouse. Gestures: a still hold, a drifting hold and a tap. A finger drifts 2.8 -> 10 -> 14.1 px by 450 ms, before the hold
// fires at 500 ms (adversarial check, 10 Oct 2026: the old drift reached only 3.6 px by then), and on the phones also 16 and 17 px
// (past the browser's own ~15 px pan start, inside the page's 18 px); a mouse wanders 5 px, under where a mouse drag starts. Targets (each one present on
// the page; an absent kind prints "skip"):
//   pile tile            an ordinary tile in a pile                  tap -> taken out (tray +1)
//   ref tile (✓)         an earlier pick (--refs)                    tap -> taken out
//   '?' tile             a questioned tile in its pile (no-tray)     tap -> taken out
//   waiting '2' tile     a question waiting in step 2 (tray build)   tap -> nothing moves (it is in the tray already)
//   "Check these first"  a tile in that box                          tap -> taken out, or nothing moves if it is in the tray already
//   "Most useful first"  a tile in that box                          (the same)
//   tray tile            a taken-out sign in the tray                tap -> put back in its pile
//   tray question        a question waiting in the tray              tap -> step 2 opens on it (no card)
//   step-2 picture       a small picture on a step-2 pile card       tap -> the sign is placed in that pile
//   step-2 big sign      the sign being placed                       tap -> nothing moves
//   step-2 card body     its put line and its count (not a picture)  tap -> the sign is placed; hold -> the pile opens, nothing placed
//   step-2 card name     the merge handle                            tap (60 and 300 ms) -> placed; still hold -> no ghost lifts,
//                                                                    nothing placed or merged, the pile opens when the finger lifts
//   cluster offer        a look-alike and the sign just placed       tap -> into the tray (a look-alike leaves "Yes, move N more")
//   trash x (mouse)      the hover x on a pile tile                  click -> trashed; a 700 ms hold -> its card, nothing trashed
// Every hold: #ctx opens and the moves, keeps (checked) and tray count are unchanged. Every tap: never opens #ctx, and does what
// the row says. A re-render while the finger is down (a saved answer arriving): a tap makes exactly one move and no card opens later,
// a hold opens the card and moves nothing. Also: no visible #modeLook and no page text "Shows it large" (the old tap switch); a mouse
// drag of a pile tile onto another pile still moves it; zero page errors. Round 2 (10 Oct 2026), phones only: a quick swipe that
// starts on a tray tile (up, over the piles) or on the step-2 big sign (down, over the cards) is a scroll and moves nothing (it used
// to drop the sign on whatever it lifted over); a hold on a tile lying where the card's "Move this tile to…" list or Zoom slider will
// appear opens the card, and lifting the finger presses nothing in it (the lift's compatibility mousedown opened the picker, moved
// the slider). Also on the phones, owner rule R02 (section 10): every tile whose line has a neighbouring line crop on the page gets
// that line drawn above / below it in the card. Must NOT block: a page without one of the kinds (it is skipped, said so), a page whose saved answers are still
// loading (the test waits for them), a page where no tile lies under the control's spot (skipped, said so).
// Usage: PW_EXE=/opt/pw-browsers/chromium NODE_PATH=$(npm root -g) node test_gestures.js PAGE.html [SHOT_DIR]   (exit 1 on any FAIL)
const { chromium, devices } = require('playwright'); const mock = require('./mock_db'); const path = require('path');
const PAGE = 'file://' + path.resolve(process.argv[2]), SHOTS = process.argv[3];
let fails = 0; const errs = [], failed = [];
const ok = (cond, msg, extra) => { console.log((cond ? 'ok   ' : 'FAIL ') + msg + (extra !== undefined ? '  [' + extra + ']' : '')); if (!cond) { fails++; failed.push(msg); } };
const skip = msg => console.log('skip ' + msg);
// px right, px down, ms before the move. Finger: |d| 3.6 -> 10 -> 14.1 px at 150 / 300 / 450 ms, the hold fires at 500 ms; then 16 and
// 17 px straight down. Mouse: 1.4 -> 3.6 -> 5 px by 350 ms (a mouse drag starts past 6 px on the step-2 sign, 8 px on a step-2 picture
// or pile name, 10 px on a tile: a mouse that moves further is dragging, by design).
const DRIFTS = { touch: [['drifting', [[2, 2, 150], [6, 8, 150], [10, 10, 150]]], ['16 px drifting', [[0, 4, 150], [0, 10, 150], [0, 16, 150]]],
  ['17 px drifting', [[0, 4, 150], [0, 10, 150], [0, 17, 150]]]], mouse: [['drifting', [[1, 1, 100], [3, 2, 150], [4, 3, 100]]]] };

const S = page => page.evaluate(() => ({ ctx: !document.getElementById('ctx').hidden, step, s2Cur, ready,
  moves: JSON.stringify(Object.keys(moves).sort().map(k => [k, moves[k]])), checked: JSON.stringify(Object.keys(checked).sort().map(k => [k, checked[k]])),
  tray: outList().length, note: document.getElementById('save').textContent, s2Msg: document.getElementById('s2Msg').textContent,
  ctxT: document.getElementById('ctxT').textContent, ctxPos: document.getElementById('ctxPos').textContent }));
const same = (a, b) => a.moves === b.moves && a.checked === b.checked && a.tray === b.tray;
const closeCard = page => page.evaluate(() => { if (!document.getElementById('ctx').hidden) closeCtx(); });
const undoLast = page => page.evaluate(() => undo());

// scroll an element into view, clear of the sticky bar, the step-2 header and the fixed tray, and give its centre on screen
// (a covering sticky header can reach below the middle of the screen -- Armstrong's step-2 sign and strip on a desktop, 78-489 px of
// 900 -- so the element is walked down the screen first, then up, never back and forth around the middle)
async function centre(page, loc, fx = 0.5, fy = 0.5) {   // fx, fy: the point inside the element (0.5, 0.5 = its centre)
  await loc.evaluate((e, [fx, fy]) => { e.scrollIntoView({ block: 'center', inline: 'center' });
    const hit = () => { const r = e.getBoundingClientRect(), h = document.elementFromPoint(r.left + r.width * fx, r.top + r.height * fy); return !!h && (e === h || e.contains(h)); };
    const y = () => { const r = e.getBoundingClientRect(); return r.top + r.height * fy; };
    for (const dir of [-1, 1]) { e.scrollIntoView({ block: 'center', inline: 'center' });
      for (let i = 0; i < 24 && y() > 8 && y() < innerHeight - 8; i++) { if (hit()) return; const y0 = scrollY; window.scrollBy(0, dir * 30); if (scrollY === y0) break; }
      if (hit()) return; } }, [fx, fy]);
  await page.waitForTimeout(250);
  const b = await loc.boundingBox(); return { x: b.x + b.width * fx, y: b.y + b.height * fy };
}
async function press(page, kind, x, y) { await mock.gesture(page, kind, x, y); }
// let earlier saves land first: the page's message line is also its save line, and a save confirmed a moment after a tap would
// overwrite the message the tap is checked by ("already in the tray")
const settled = page => page.waitForFunction(() => typeof open_ === 'undefined' || (open_ === 0 && !Object.keys(writers).length), null, { timeout: 8000 }).catch(() => {});
// hold: still (path null), or along a drift path [[dx, dy, ms before the move], ...] while held, until 900 ms; then let go there
async function hold(page, loc, path, at) {
  await settled(page); const { x, y } = at || await centre(page, loc);
  await press(page, 'down', x, y); let t = 0, dx = 0, dy = 0;
  for (const [ddx, ddy, w] of path || []) { await page.waitForTimeout(w); t += w; dx = ddx; dy = ddy; await press(page, 'move', x + dx, y + dy); }
  await page.waitForTimeout(Math.max(150, 900 - t)); await press(page, 'up', x + dx, y + dy); await page.waitForTimeout(450);
}
async function tap(page, loc, touch, ms, at) { await settled(page); const { x, y } = at || await centre(page, loc);
  if (ms) { await press(page, 'down', x, y); await page.waitForTimeout(ms); await press(page, 'up', x, y); }   // a slow tap
  else if (touch) await page.touchscreen.tap(x, y); else await page.mouse.click(x, y);
  await page.waitForTimeout(450); }

// a quick swipe (8 moves in about 100 ms) that starts on a target: a scroll, never a move and never a card (round-2 check, 10 Oct 2026)
async function swipeNothing(page, dev, name, loc, dx, dy, at) {
  await settled(page); const { x, y } = at || await centre(page, loc); const b0 = await S(page);
  await press(page, 'down', x, y); for (let i = 1; i <= 8; i++) { await press(page, 'move', x + dx * i / 8, y + dy * i / 8); await page.waitForTimeout(12); }
  await press(page, 'up', x + dx, y + dy); await page.waitForTimeout(450); const a = await S(page);
  ok(same(a, b0) && !a.ctx, `${dev}: a quick swipe ${dy < 0 ? 'up' : 'down'} ${Math.abs(dy)} px that starts on ${name} moves nothing and opens no card`,
    `card ${a.ctx}, tray ${b0.tray}->${a.tray}, moves ${a.moves === b0.moves ? 'same' : 'CHANGED'}, keeps ${a.checked === b0.checked ? 'same' : 'CHANGED'}`);
  await closeCard(page); if (!same(await S(page), b0)) { await undoLast(page); await page.waitForTimeout(150); }
}
// a tray tile's centre, with the page scrolled so that a pile lies under the point 250 px above it (where a swipe up lifts)
async function trayAt(page, sel, dy) {
  return page.evaluate(([sel, dy]) => { const t = document.querySelector(sel); if (!t) return null; const r = t.getBoundingClientRect(), x = r.left + r.width / 2, y = r.top + r.height / 2;
    const p = [...document.querySelectorAll('#list .pile[data-pile]')].find(p => p.getBoundingClientRect().height > 60);
    if (p) { const q = p.getBoundingClientRect(); window.scrollBy(0, q.top + Math.min(q.height / 2, 40) - (y + dy)); }
    return { x, y }; }, [sel, dy]);
}
// the three gestures on one target. tapCheck(before, after) -> [ok, what]; restore() undoes what the tap did
async function three(page, dev, touch, name, loc, tapCheck, restore, holdCheck, opt = {}) {
  for (const [kind, drift] of [['still', null]].concat(DRIFTS[touch ? 'touch' : 'mouse'])) {
    const at = opt.fx ? await centre(page, loc, opt.fx, opt.fy) : null;
    const b = await S(page); await hold(page, loc, drift, at); const a = await S(page);
    const extra = holdCheck ? holdCheck(a) : true;
    ok(a.ctx && same(a, b) && extra, `${dev}: ${kind} hold on ${name} opens its card and moves nothing`,
      `card ${a.ctx}, tray ${b.tray}->${a.tray}, moves ${b.moves === a.moves ? 'same' : 'CHANGED'}, keeps ${b.checked === a.checked ? 'same' : 'CHANGED'}${a.ctx ? ', ' + a.ctxT + ' | ' + a.ctxPos : ''}`);
    if (a.ctx && SHOTS && !drift && !shot[dev + name]) { shot[dev + name] = 1; await page.screenshot({ path: path.join(SHOTS, `gest_${dev.replace(/\W+/g, '')}_${name.replace(/\W+/g, '_')}_card.png`) }); }
    await closeCard(page); await page.waitForTimeout(150);
    if (!same(await S(page), b)) { await undoLast(page); await page.waitForTimeout(150); }   // a hold that moved something: put it back for the next check
  }
  for (const ms of opt.slowTap ? [0, 300] : [0]) {
    const at = opt.fx ? await centre(page, loc, opt.fx, opt.fy) : null;
    const b = await S(page); await tap(page, loc, touch, ms, at); const a = await S(page);
    const [good, what] = tapCheck(b, a);
    ok(good && !a.ctx, `${dev}: ${ms ? ms + ' ms ' : ''}tap on ${name} ${what} and opens no card`, `card ${a.ctx}, tray ${b.tray}->${a.tray}, step ${b.step}->${a.step}`);
    await closeCard(page); if (restore) { await restore(b, a); await page.waitForTimeout(250); }
  }
}
const shot = {};

async function run(b, dev, opts) {
  const touch = dev !== 'desktop';
  const ctx = await b.newContext(opts); await mock.install(ctx); const page = await ctx.newPage();
  page.on('pageerror', e => errs.push(dev + ': ' + e.message));
  await page.goto(PAGE); await page.waitForFunction(() => typeof ready !== 'undefined' && ready, null, { timeout: 30000 }).catch(() => {});
  await page.waitForTimeout(600);
  const st0 = await S(page); ok(st0.ready, `${dev}: the saved answers are in (ready)`);
  if (st0.step !== 1) { await tap(page, page.locator('#tab1'), touch); }
  ok((await S(page)).step === 1, `${dev}: on step 1`);
  // the old tap switch is gone (looked for on step 1, where it was)
  const sw = await page.evaluate(() => { const m = document.getElementById('modeLook'); return { look: !!(m && m.offsetParent), text: /Shows it large/.test(document.body.innerText) }; });
  ok(!sw.look && !sw.text, `${dev}: no switch that changes what a tap does (no #modeLook, no "Shows it large")`, JSON.stringify(sw));
  const hint = await page.evaluate(() => document.getElementById('hint1').innerText);
  ok(/\bTap\b/.test(hint) && /tray/.test(hint) && /\bHold\b/.test(hint) && /card/.test(hint) && !/lift your finger|hold first|lift to drag/i.test(hint),
    `${dev}: step-1 hint says tap = to the tray, hold = its card (and nothing about hold-to-drag)`, hint.slice(0, 160));

  const outTap = sid => (b0, a) => [a.moves.includes(JSON.stringify([sid, 'OUT']).slice(1, -1)) && a.tray === b0.tray + 1, 'takes it out to the tray'];
  const putBackUndo = async () => { await undoLast(page); };
  const pickSid = sel => page.evaluate(sel => { const e = [...document.querySelectorAll(sel)].find(x => x.offsetParent); return e ? (e.dataset.sid || (e.parentElement && e.parentElement.dataset.sid)) : null; }, sel);

  // 1. tiles in piles: ordinary, ref (✓), '?', waiting '2'
  for (const [name, sel] of [['a pile tile', '#list .pile .tiles .t:not(.ref):not(.wait):not(.fq):not(.out):not(.in)'], ['a ref (✓) tile', '#list .pile .tiles .t.ref'],
                             ['a "?" tile', '#list .pile .tiles .t.fq'], ['a waiting "2" tile', '#list .pile .tiles .t.wait']]) {
    const sid = await pickSid(sel); if (!sid) { skip(`${dev}: ${name} -- none on this page`); continue; }
    const loc = page.locator('#list .pile .tiles .t[data-sid="' + sid + '"]').first();
    if (name.includes('waiting')) await three(page, dev, touch, name + ' (' + sid + ')', loc,
      (b0, a) => [same(a, b0) && /already in the tray/.test(a.note), 'leaves it in the tray (nothing moves, says so)'], null);
    else await three(page, dev, touch, name + ' (' + sid + ')', loc, outTap(sid), putBackUndo);
  }
  // 2. the two boxes
  for (const [name, box, list] of [['a "Check these first" tile', '#focusTiles', 'in "Check these first"'], ['a "Most useful first" tile', '#rankTiles', 'in "Most useful first"']]) {
    const sid = await page.evaluate(box => { const d = [...document.querySelectorAll(box + ' > div')].find(x => x.offsetParent && itemBySid[x.dataset.sid]); return d ? d.dataset.sid : null; }, box);
    if (!sid) { skip(`${dev}: ${name} -- none on this page`); continue; }
    const loc = page.locator(box + ' > div[data-sid="' + sid + '"] .t');
    const inTray = await page.evaluate(s => preTrayed(s) || moves[s] === 'OUT', sid);
    await three(page, dev, touch, name + ' (' + sid + ')', loc,
      inTray ? (b0, a) => [same(a, b0) && /already in the tray/.test(a.note), 'leaves it in the tray (nothing moves, says so)'] : outTap(sid),
      inTray ? null : putBackUndo, a => a.ctxPos.includes(list));
    if (!inTray) {   // a second tap on it, now in the tray: nothing moves
      const b0 = await S(page); await page.evaluate(s => takeOut(s, null), sid); const b1 = await S(page);
      await tap(page, loc, touch); const a = await S(page);
      ok(same(a, b1) && !a.ctx && /already in the tray/.test(a.note), `${dev}: tap on ${name} already taken out leaves it in the tray (nothing moves, no card)`,
        `card ${a.ctx}, tray ${b1.tray}->${a.tray}, moves ${b1.moves === a.moves ? 'same' : 'CHANGED'}, note "${a.note}"`);
      await undoLast(page); ok(same(await S(page), b0), `${dev}: (restored)`);
    }
  }
  // 3. the tray: a taken-out sign, and a question waiting
  { const sid = await pickSid('#list .pile .tiles .t:not(.ref):not(.wait):not(.fq):not(.out):not(.in)');
    if (!sid) skip(`${dev}: no pile tile to take out for the tray`);
    else {
      await page.evaluate(s => takeOut(s, null), sid); await page.waitForTimeout(200);
      const loc = page.locator('#trayTiles .t[data-sid="' + sid + '"]');
      await three(page, dev, touch, 'a tray tile, taken out (' + sid + ')', loc,
        (b0, a) => [!a.moves.includes(JSON.stringify([sid, 'OUT']).slice(1, -1)) && a.tray === b0.tray - 1, 'puts it back in its pile'], null);
      if (await page.evaluate(s => moves[s] !== 'OUT', sid)) { await page.evaluate(s => takeOut(s, null), sid); await page.waitForTimeout(200); }
      if (touch) { const sel = '#trayTiles .t[data-sid="' + sid + '"]', at = await trayAt(page, sel, -250); await page.waitForTimeout(200);
        await swipeNothing(page, dev, 'a tray tile, taken out (' + sid + '), over a pile', loc, 0, -250, at); }
      if (await page.evaluate(s => moves[s] === 'OUT', sid)) await page.evaluate(s => putBack(s), sid);
    } }
  { const sid = await page.evaluate(() => outList().find(s => preTrayed(s)) || null);
    if (!sid) skip(`${dev}: no question waiting in the tray (no-tray build or all answered)`);
    else { await three(page, dev, touch, 'a tray question (' + sid + ')', page.locator('#trayTiles .t[data-sid="' + sid + '"]'),
      (b0, a) => [same(a, b0) && a.step === 2 && a.s2Cur === sid, 'opens step 2 on it (nothing saved)'], async () => { await page.evaluate(() => setStep(1)); });
      if (touch) { await page.evaluate(() => setStep(1)); await page.waitForTimeout(200);
        const sel = '#trayTiles .t[data-sid="' + sid + '"]', at = await trayAt(page, sel, -250); await page.waitForTimeout(200);
        await swipeNothing(page, dev, 'a tray question (' + sid + '), over a pile', page.locator(sel), 0, -250, at); } } }
  // 4. step 2: a small picture on a pile card, and the big sign
  { if (!(await page.evaluate(() => outList().length))) { const sid = await pickSid('#list .pile .tiles .t:not(.ref):not(.wait):not(.fq):not(.out):not(.in)'); if (sid) await page.evaluate(s => takeOut(s, null), sid); }
    if (!(await page.evaluate(() => outList().length))) skip(`${dev}: nothing to place in step 2`);
    else {
      await page.evaluate(() => setStep(2)); await page.waitForFunction(() => document.querySelector('#cards .card .smp img'), null, { timeout: 30000 }).catch(() => {});
      await page.waitForTimeout(300);
      const s2 = await page.evaluate(() => s2Cur);
      const pile = await page.evaluate(() => { const c = [...document.querySelectorAll('#cards .card')].find(c => c.querySelector('.smp img') && c.dataset.pile !== homeOf[s2Cur]); return c ? c.dataset.pile : null; });
      if (!pile) skip(`${dev}: no other pile card with pictures in step 2`);
      else await three(page, dev, touch, 'a step-2 card picture (pile ' + pile + ')', page.locator('#cards .card[data-pile="' + pile + '"] .smp img').first(),
        (b0, a) => [!a.ctx && a.tray === b0.tray - 1 && a.moves.includes(JSON.stringify([s2, pile]).slice(1, -1)), 'places the sign (' + s2 + ') in that pile'], putBackUndo,
        a => a.s2Cur === s2);
      if (SHOTS) await page.screenshot({ path: path.join(SHOTS, `gest_${dev.replace(/\W+/g, '')}_step2.png`) });
      // the rest of a card (adversarial check, 10 Oct 2026: a long press on the put line, the count or the padding placed the sign when
      // the finger lifted): a tap places, a hold opens the pile and places nothing
      const card = pile && page.locator('#cards .card[data-pile="' + pile + '"]');
      const placed = (b0, a) => [!a.ctx && a.tray === b0.tray - 1 && a.moves.includes(JSON.stringify([s2, pile]).slice(1, -1)), 'places the sign (' + s2 + ') in that pile'];
      if (pile) for (const [part, loc, opt] of [['put line', card.locator('.put'), {}], ['count', card.locator('.cnt'), {}], ['padding', card, { fx: 0.97, fy: 0.5 }]])
        await three(page, dev, touch, 'a step-2 card ' + part + ' (pile ' + pile + ')', loc, placed, putBackUndo, a => a.s2Cur === s2, opt);
      // its name, the merge handle: a tap (quick or 300 ms) places; a still hold lifts no ghost, merges nothing, and opens the pile
      if (pile) {
        const name = card.locator('.cid');
        await three(page, dev, touch, 'a step-2 card name (pile ' + pile + ')', name, placed, putBackUndo, a => a.s2Cur === s2, { slowTap: true });
        await settled(page); const at = await centre(page, name); const b0 = await S(page), st0 = await page.evaluate(() => JSON.stringify(state));
        await press(page, 'down', at.x, at.y); await page.waitForTimeout(750);
        const mid = await page.evaluate(() => ({ ghost: document.querySelectorAll('.ghost').length, ctx: !document.getElementById('ctx').hidden }));
        await press(page, 'up', at.x, at.y); await page.waitForTimeout(450); const a = await S(page), st1 = await page.evaluate(() => JSON.stringify(state));
        ok(!mid.ghost && same(a, b0) && st0 === st1 && a.ctx, `${dev}: a still hold on a step-2 card name lifts no ghost, places and merges nothing, and the pile opens`,
          `ghost while held ${mid.ghost}, card after ${a.ctx}, moves ${a.moves === b0.moves ? 'same' : 'CHANGED'}, piles ${st0 === st1 ? 'same' : 'CHANGED'}`);
        await closeCard(page); }
      await three(page, dev, touch, 'the step-2 big sign (' + s2 + ')', page.locator('#s2Tile'),
        (b0, a) => [same(a, b0) && a.s2Cur === s2 && /waiting here to be placed/.test(a.s2Msg), 'leaves it waiting (nothing moves, says so)'], null);
      if (touch) for (const dy of [200, 400]) {   // the cards scrolled up under the pinned sign, as when the owner scrolls back to them
        await page.evaluate(() => { const c = document.querySelectorAll('#cards .card'); const k = c[Math.min(3, c.length - 1)]; if (k) k.scrollIntoView({ block: 'center' }); }); await page.waitForTimeout(250);
        const r = await page.evaluate(() => { const e = document.getElementById('s2Tile').getBoundingClientRect(); return { x: e.left + e.width / 2, y: e.top + e.height / 2 }; });
        await swipeNothing(page, dev, 'the step-2 big sign (' + s2 + '), over the cards', page.locator('#s2Tile'), 0, Math.min(dy, (opts.viewport || {}).height - r.y - 10 || dy), r); }
      await page.evaluate(() => setStep(1));
    } }
  // 6. a re-render while the finger is down (a saved answer arriving re-draws the piles): a tap makes exactly one move and no card
  // opens afterwards; a hold still opens the card and moves nothing (adversarial check, 10 Oct 2026: the old element's hold timer was
  // never cleared, so the tap acted AND the card opened half a second later)
  { const sid = await pickSid('#list .pile .tiles .t:not(.ref):not(.wait):not(.fq):not(.out):not(.in)');
    if (!sid) skip(`${dev}: no pile tile for the re-render rows`);
    else {
      const loc = () => page.locator('#list .pile .tiles .t[data-sid="' + sid + '"]').first();
      await settled(page); let at = await centre(page, loc()); let b0 = await S(page);
      await press(page, 'down', at.x, at.y); await page.waitForTimeout(40); await page.evaluate(() => render()); await page.waitForTimeout(80);
      await press(page, 'up', at.x, at.y); await page.waitForTimeout(900); let a = await S(page);
      // a finger's tap reaches the re-drawn tile (one move); a mouse click whose press target was replaced is dropped by the browser
      // (no click at all): at most one move, and never the card
      ok(!a.ctx && (a.tray === b0.tray + 1 && a.moves.includes(JSON.stringify([sid, 'OUT']).slice(1, -1)) || !touch && same(a, b0)),
        `${dev}: a tap during a re-render ${touch ? 'takes the sign out once' : 'makes at most one move'} and opens no card later`, `card ${a.ctx}, tray ${b0.tray}->${a.tray}`);
      await closeCard(page); if (a.tray !== b0.tray) await undoLast(page); await page.waitForTimeout(250);
      await settled(page); at = await centre(page, loc()); b0 = await S(page);
      await press(page, 'down', at.x, at.y); await page.waitForTimeout(200); await page.evaluate(() => render()); await page.waitForTimeout(700);
      await press(page, 'up', at.x, at.y); await page.waitForTimeout(450); a = await S(page);
      ok(a.ctx && same(a, b0), `${dev}: a hold during a re-render opens the card and moves nothing`, `card ${a.ctx}, moves ${a.moves === b0.moves ? 'same' : 'CHANGED'}`);
      await closeCard(page); if (!same(await S(page), b0)) await undoLast(page);
    } }
  // 7. the cluster offer ("... has N look-alikes ... Move them too?"): its pictures follow the rule (adversarial check, 10 Oct 2026:
  // they answered neither): a hold opens that sign's card, nothing moves; a tap takes it out to the tray, out of "Yes, move N more"
  { const set = await page.evaluate(() => { const sid = Object.keys(clusterOf).find(s => (clusterMembers[clusterOf[s]] || []).length > 2 && !preTrayed(s) && !moves[s] && !itemBySid[s].r); if (!sid) return null;
      const to = allPiles().map(p => p.id).find(id => id !== homeOf[sid] && !SPECIAL.has(id)); remember([sid]); setDest(sid, to); renderSome([homeOf[sid], to]); offerCluster([sid], to);
      return document.getElementById('offer').hidden ? null : { sid, to, rest: offerState.rest.slice() }; });
    if (!set) skip(`${dev}: no cluster offer on this page`);
    else {
      const lk = set.rest[0], loc = page.locator('#offerTiles .t[data-sid="' + lk + '"]');
      for (const [kind, drift] of [['still', null]].concat(DRIFTS[touch ? 'touch' : 'mouse'].slice(0, 1))) {
        const b0 = await S(page); await hold(page, loc, drift); const a = await S(page);
        ok(a.ctx && same(a, b0) && a.ctxT.includes(lk), `${dev}: ${kind} hold on a look-alike in the cluster offer opens its card and moves nothing`, `card ${a.ctx}, ${a.ctxT}`);
        await closeCard(page); }
      const b0 = await S(page); await tap(page, loc, touch); const a = await S(page);
      const o = await page.evaluate(() => ({ shown: !document.getElementById('offer').hidden, rest: offerState ? offerState.rest : null, yes: document.getElementById('offerYes').textContent }));
      ok(!a.ctx && a.moves.includes(JSON.stringify([lk, 'OUT']).slice(1, -1)) && (o.rest ? !o.rest.includes(lk) && o.rest.length === set.rest.length - 1 : set.rest.length === 1),
        `${dev}: a tap on a look-alike in the cluster offer takes it out to the tray and out of "Yes, move N more"`, JSON.stringify(o));
      await closeCard(page); await undoLast(page); await page.evaluate(() => { hideOffer(); undo(); }); await page.waitForTimeout(250);
    } }
  // 8. mouse: a hold on the hover x (trash) opens the card and trashes nothing; a click trashes
  if (!touch) {
    const sid = await pickSid('#list .pile .tiles .t:not(.ref):not(.wait):not(.fq):not(.out):not(.in)');
    if (!sid) skip('desktop: no pile tile for the trash x');
    else {
      const t = page.locator('#list .pile .tiles .t[data-sid="' + sid + '"]').first(); const c = await centre(page, t); await page.mouse.move(c.x, c.y); await page.waitForTimeout(150);
      const xb = await t.locator('.trash').boundingBox(); const b0 = await S(page);
      await page.mouse.move(xb.x + xb.width / 2, xb.y + xb.height / 2); await page.mouse.down(); await page.waitForTimeout(700); await page.mouse.up(); await page.waitForTimeout(400);
      let a = await S(page);
      ok(a.ctx && same(a, b0), 'desktop: a 700 ms hold on the trash x opens the card and trashes nothing', `card ${a.ctx}, moves ${a.moves === b0.moves ? 'same' : 'CHANGED'}`);
      await closeCard(page); if (!same(await S(page), b0)) await undoLast(page);
      await page.mouse.move(c.x, c.y); await page.waitForTimeout(150); await page.mouse.click(xb.x + xb.width / 2, xb.y + xb.height / 2); await page.waitForTimeout(400); a = await S(page);
      ok(!a.ctx && a.moves.includes(JSON.stringify([sid, 'NOT-LETTER']).slice(1, -1)), 'desktop: a click on the trash x trashes the sign', a.moves);
      if (a.moves !== b0.moves) await undoLast(page);
    } }
  // 5. mouse: a drag straight onto another pile still moves the tile
  if (!touch) {
    const r = await page.evaluate(() => { const t = [...document.querySelectorAll('#list .pile .tiles .t:not(.ref):not(.wait):not(.out)')].find(x => x.offsetParent);
      const p = t && [...document.querySelectorAll('#list .pile[data-pile]')].find(p => p.dataset.pile !== t.closest('.pile').dataset.pile && !/^(NOT-LETTER|BAD-CUT)$/.test(p.dataset.pile));
      return t && p ? { sid: t.dataset.sid, to: p.dataset.pile } : null; });
    if (!r) skip('desktop: no two piles for a mouse drag');
    else {
      const from = await centre(page, page.locator('#list .pile .tiles .t[data-sid="' + r.sid + '"]').first());
      await page.mouse.move(from.x, from.y); await page.mouse.down();
      for (let i = 1; i <= 6; i++) { await page.mouse.move(from.x + 3 * i, from.y + 3 * i); await page.waitForTimeout(16); }
      await page.evaluate(to => document.querySelector('#list .pile[data-pile="' + CSS.escape(to) + '"]').scrollIntoView({ block: 'center' }), r.to); await page.waitForTimeout(200);
      const pb = await page.locator('#list .pile[data-pile="' + r.to + '"] .ph').boundingBox();
      for (let i = 1; i <= 8; i++) { await page.mouse.move(pb.x + 30, pb.y + pb.height / 2 + i); await page.waitForTimeout(16); }
      await page.mouse.up(); await page.waitForTimeout(400);
      const got = await page.evaluate(s => moves[s], r.sid);
      ok(got === r.to, `desktop: a mouse drag of a pile tile onto another pile still moves it (${r.sid} -> ${r.to})`, got);
      if (got) await undoLast(page);
    } }
  // 9. the lifted finger presses nothing in the card that opened under it (round-2 check, 10 Oct 2026: after a hold opened the card,
  // the lift's compatibility mousedown opened the "Move this tile to…" picker, so the next tap moved the sign, and jumped the Zoom slider)
  if (touch) for (const ctl of ['ctxDest', 'ctxZ']) {
    if ((await S(page)).step !== 1) await page.evaluate(() => setStep(1));
    const any = await pickSid('#list .pile .tiles .t:not(.wait)');
    if (!any) { skip(`${dev}: no pile tile to open a card for #${ctl}`); break; }
    await page.evaluate(s => showCtx(s, pileOf(s)), any); await page.waitForTimeout(300);
    const sp = await page.evaluate(id => { const e = document.getElementById(id), r = e.getBoundingClientRect(); return r.width && r.top > 0 && r.bottom < innerHeight ? { x: Math.round(r.left + Math.min(30, r.width / 2)), y: Math.round(r.top + r.height / 2) } : null; }, ctl);
    await closeCard(page); await page.waitForTimeout(150);
    if (!sp) { skip(`${dev}: #${ctl} is not on screen when a card opens`); continue; }
    const sid = await page.evaluate(p => { for (let i = 0; i < 400; i++) { const e = document.elementFromPoint(p.x, p.y), t = e && e.closest && e.closest('#list .pile .tiles .t');
      if (t && !t.classList.contains('wait') && !t.classList.contains('ref')) return t.dataset.sid; const y0 = scrollY; window.scrollBy(0, 7); if (scrollY === y0) break; } return null; }, sp);
    if (!sid) { skip(`${dev}: no pile tile lies under #${ctl}'s spot`); continue; }
    await page.waitForTimeout(200);
    const z0 = await page.evaluate(() => document.getElementById('ctxZ').value), b0 = await S(page);
    await page.evaluate(() => { window.__lift = []; if (!window.__liftOn) { window.__liftOn = 1; ['mousedown', 'focusin', 'click', 'input', 'change'].forEach(t =>
      document.getElementById('ctx').addEventListener(t, e => window.__lift.push(t + ':' + (e.target.id || e.target.tagName)), true)); } });
    await hold(page, null, null, sp);
    const r = await page.evaluate(([x, y]) => { const d = document.getElementById('ctxDest'), u = document.elementFromPoint(x, y); let open = false; try { open = d.matches(':open'); } catch (e) {}
      return { ctx: !document.getElementById('ctx').hidden, sid: ctxSid, under: u ? (u.id || u.tagName) : '', focus: document.activeElement ? document.activeElement.id || document.activeElement.tagName : '',
        open, z: document.getElementById('ctxZ').value, ev: window.__lift.slice() }; }, [sp.x, sp.y]);
    const a = await S(page);
    ok(r.ctx && r.sid === sid && same(a, b0) && !r.open && r.z === z0 && !/^(ctx|fix|view)/.test(r.focus) && !r.ev.length,
      `${dev}: a hold on a tile lying under the card's #${ctl} opens its card, and lifting the finger presses nothing in it`, `lift over ${r.under}; ` + JSON.stringify(r));
    await closeCard(page); if (!same(await S(page), b0)) await undoLast(page);
  }
  // 10. owner rule R02 on the phone card ("I can't see above or below the symbol"): for every tile (up to 300, spread over the page)
  // whose line has a neighbouring line crop on the page, the card draws it and shows at least half a crop's height on that side; on
  // the other side, if it has no neighbour, every pixel of the tile's own crop (round-2 check, 10 Oct 2026: Armstrong's crops are
  // p1L05, with no underscore, and the card drew no neighbour line for any of its 997 tiles). On a --region page its "Line strips" view.
  if (touch) {
    const r = await page.evaluate(async () => {
      const sids = Object.keys(itemBySid), k = Math.max(1, Math.ceil(sids.length / 300)), pick = sids.filter((_, i) => i % k === 0), ps = DATA.pageScale || 1;
      const wait = sid => new Promise(res => { const t0 = performance.now(); const f = () => { const c = document.getElementById('ctxC'); if ((c.dataset.sid === sid && c._map) || performance.now() - t0 > 1500) res(); else requestAnimationFrame(f); }; f(); });
      const band = q => Math.round(q.naturalHeight * 0.78) - Math.round(q.naturalHeight * 0.22);
      const out = { n: 0, nb: 0, short: [], cut: [], skipped: 0 }, pv = pageView; pageView = false;   // a --region page: its "Line strips" view
      for (const sid of pick) { if (usePage(sid)) { out.skipped++; continue; }
        showCtx(sid, pileOf(sid)); await wait(sid); const c = document.getElementById('ctxC'), m = c._map;
        if (!m || c.dataset.sid !== sid) { out.skipped++; continue; }
        const it = itemBySid[sid], [pa, pb] = nbPages(it.p), H = pageImg(it.p).naturalHeight, [, by, , bh] = boxOf(sid).map(v => v * ps);
        const hb = pb ? Math.round(band(pageImg(pb)) * m.s) : 0, y1 = m.y0 + (c.height - m.ha - hb) / m.s;
        const above = (by - m.y0) + m.ha / m.s, below = (y1 - by - bh) + hb / m.s; out.n++;
        if (!pa && !pb) continue; out.nb++;
        if ((pa && above < 0.5 * H) || (pb && below < 0.5 * H)) out.short.push(sid + ' ' + Math.round(above) + '/' + Math.round(below) + ' of ' + H);
        if ((!pa && m.y0 > 1) || (!pb && H - y1 > 1)) out.cut.push(sid + ' ' + Math.round(m.y0) + '/' + Math.round(H - y1));
      }
      closeCtx(); pageView = pv; return out; });
    if (!r.nb) skip(`${dev}: R02 -- no tile's line has a neighbouring line crop on this page (${r.n} tiles measured, ${r.skipped} in the whole-page view)`);
    else ok(!r.short.length && !r.cut.length, `${dev}: R02 the card shows the lines above and below: ${r.nb} of ${r.n} tiles measured have a neighbouring line on the page; each card draws it (at least half a line), and all of the tile's own crop on a side with none`,
      `short ${r.short.length}: ${r.short.slice(0, 4).join(', ')}; cut ${r.cut.length}: ${r.cut.slice(0, 4).join(', ')}`);
  }
  await ctx.close();
}

(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_EXE || '/opt/pw-browsers/chromium' });
  const prof = d => { const o = { ...devices[d] }; delete o.defaultBrowserType; return o; };
  for (const [dev, opts] of [['iPhone 13', prof('iPhone 13')], ['iPhone SE', prof('iPhone SE')], ['desktop', { viewport: { width: 1280, height: 900 } }]]) {
    try { await run(b, dev, opts); } catch (e) { ok(false, dev + ': the run finished without an exception', e.message.split('\n')[0]); }
  }
  ok(!errs.length, 'no page errors', errs.join(' | '));
  if (failed.length) { console.log('failed checks (repeated here so a log tail shows them):'); failed.forEach(m => console.log('  - ' + m)); }
  console.log('errors:', errs); console.log(fails ? fails + ' FAILED' : 'ALL PASS');
  await b.close(); process.exit(fails ? 1 : 0);
})();
