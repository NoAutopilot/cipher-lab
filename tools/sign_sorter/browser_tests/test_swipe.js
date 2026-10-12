// Owner rule R12 (tools/data/sorter_owner_requirements.tsv; 11 Oct 2026, Matignon f.110, on his phone: "I need to lock the page in place,
// it kinda wiggles when you swipe left or right and doesn't actually swipe it left or right. Although allowing me to swipe left or right
// through a pile would be great. I could quickly knock out bad fits etc."; template 2026-10-09.8): a sideways swipe never moves the page,
// the card or the frame; it steps through the signs where it can.
//
// Devices: iPhone 13, iPhone SE (Playwright device profiles) and a 320 px phone; real touch through CDP Input.dispatchTouchEvent
// (touchStart, touchMove every 16 ms, touchEnd), never page.mouse. Fixtures (make_fixtures.py): plain.html (the card and step 1),
// tray.html (step 2 and the "Taken out" tray). Checks, per device:
//   card (opened with a pile's "Go through", walking its family, R11):
//     1. a swipe LEFT on the title, on a button, on the enlarged sign, on the place line or on the question steps +1; RIGHT steps -1
//        (ctxStep, as the arrows and Previous / Next); at either end it stops and the end words show (no wrap)
//     2. while the swipe is under way the enlarged sign (#ctxBig) follows the finger a little (translateX, at most 36 px) and nothing else
//        moves; after the lift it is back (no transform)
//     3. no click fires anywhere from a swipe (not on the button it started on: nothing is moved, kept or taken out)
//     4. a swipe shorter than 50 px, a two-finger swipe, a swipe on the "Move this tile to…" list, and any swipe while a cut is being
//        fixed step nothing
//     5. a vertical swipe scrolls the card's box and steps nothing; a slide on the picture moves the view (canvas._pan.moved, R09) and
//        steps nothing
//   step 2 (tray.html lands on it):
//     6. a swipe LEFT on the pinned sign is Skip (the next question), RIGHT is Previous; also on the line strip, the question, a button
//        (which is not pressed); at either end it stops and says so; the pinned sign follows the finger and springs back
//     7. a swipe on a pile card places nothing and moves nothing
//   step 1:
//     8. a sideways swipe on a pile tile takes nothing out and opens no card; on "Go through" it opens no card
//     9. the "Taken out" tray still scrolls sideways under a finger, and the swipe puts nothing back
//   everywhere: window.scrollX, the root's scrollLeft and visualViewport.offsetLeft stay 0 after every gesture; computed
//   overscroll-behavior-x is none on html and body; the computed touch-action of every swipe region (#ctx .box, .s2top, #s2Acts,
//   step 2's strip) has pan-y and not pan-x; the hints say "swipe left or right" in plain words, no colour (R07); zero page errors.
// Must catch: a sideways swipe that moves the page (scrollX / offsetLeft), a card that steps only on the enlarged sign, a swipe that also
// presses the button it started on, a step-2 swipe on the pile cards that places the sign. Must NOT block: a page with no question in
// the card's walk (the question swipe says skip), a card box too short to scroll on a tall phone (says skip).
// Usage: PW_EXE=/opt/pw-browsers/chromium NODE_PATH=$(npm root -g) node test_swipe.js FIXTURE_DIR [SHOT_DIR]     (exit 1 on any FAIL)
//        node test_swipe.js --probe PAGE   a built (real) page, iPhone 13 and iPhone SE: the card steps both ways on a swipe, step 2 (when
//        anything waits there) steps both ways, nothing moved, the page never moves sideways, zero page errors.
const { chromium, devices } = require('playwright'); const mock = require('./mock_db'); const path = require('path');
let fails = 0; const errs = [], failed = [];
const ok = (cond, msg, extra) => { console.log((cond ? 'ok   ' : 'FAIL ') + msg + (extra !== undefined ? '  [' + (typeof extra === 'string' ? extra : JSON.stringify(extra)) + ']' : '')); if (!cond) { fails++; failed.push(msg); } };
const skip = msg => console.log('skip ' + msg);
const prof = d => { const o = { ...devices[d] }; delete o.defaultBrowserType; return o; };
const DEVICES = [['iPhone 13', prof('iPhone 13')], ['iPhone SE', prof('iPhone SE')],
  ['320 px phone', { viewport: { width: 320, height: 568 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2, userAgent: devices['iPhone SE'].userAgent }]];

const cdpOf = async page => page.__cdp || (page.__cdp = await page.context().newCDPSession(page));
async function touch(page, type, pts) { await (await cdpOf(page)).send('Input.dispatchTouchEvent', { type, touchPoints: pts.map((p, i) => ({ x: p[0], y: p[1], id: i + 1 })) }); }
// the page never moves sideways: checked after every gesture
let side = [];
const sideCheck = async (page, what) => { const s = await page.evaluate(() => ({ x: window.scrollX, root: document.scrollingElement.scrollLeft, vv: window.visualViewport ? window.visualViewport.offsetLeft : 0,
  box: document.querySelector('#ctx .box').scrollLeft, scale: window.visualViewport ? window.visualViewport.scale : 1 }));
  if (s.x || s.root || s.vv || s.box) side.push(what + ': ' + JSON.stringify(s)); };
// one finger from (x, y) by (dx, dy) in `steps` moves 16 ms apart; mid(): called halfway, finger still down
async function swipe(page, x, y, dx, dy, o = {}) {
  const steps = o.steps || 6; let mid = null;
  await page.evaluate(() => { window.__clicks = []; });
  await touch(page, 'touchStart', [[x, y]]);
  for (let i = 1; i <= steps; i++) { await touch(page, 'touchMove', [[x + dx * i / steps, y + dy * i / steps]]); await page.waitForTimeout(16);
    if (o.mid && i === Math.ceil(steps / 2)) mid = await o.mid(); }
  await touch(page, 'touchEnd', []); await page.waitForTimeout(o.after || 260);
  await sideCheck(page, o.what || 'swipe');
  return { mid, clicks: await page.evaluate(() => window.__clicks.slice()) };
}
async function two(page, x, y, dx) {   // two fingers side by side, moved sideways together
  await page.evaluate(() => { window.__clicks = []; });
  await touch(page, 'touchStart', [[x - 25, y], [x + 25, y]]);
  for (let i = 1; i <= 6; i++) { await touch(page, 'touchMove', [[x - 25 + dx * i / 6, y], [x + 25 + dx * i / 6, y]]); await page.waitForTimeout(16); }
  await touch(page, 'touchEnd', []); await page.waitForTimeout(260); await sideCheck(page, 'two fingers');
  return page.evaluate(() => window.__clicks.slice());
}
// a point on the element that the element itself receives (scrolled into view; not under a pinned header or the fixed tray)
async function on(page, sel, fx = 0.5, fy = 0.5) {
  for (let k = 0; k < 4; k++) {
    const p = await page.evaluate(([sel, fx, fy, k]) => { const e = document.querySelector(sel); if (!e || !e.getClientRects().length) return null;
      if (k === 0) e.scrollIntoView({ block: 'center', inline: 'nearest' }); else window.scrollBy(0, -80);
      const r = e.getBoundingClientRect(), xs = [fx, 0.25, 0.75, 0.1, 0.9], ys = [fy, 0.3, 0.7];
      for (const a of xs) for (const b of ys) { const x = r.left + r.width * a, y = r.top + r.height * b, h = document.elementFromPoint(x, y);
        if (h && (h === e || e.contains(h)) && y > 0 && y < innerHeight) return { x, y }; }
      return { none: true }; }, [sel, fx, fy, k]);
    if (!p) return null; if (!p.none) { await page.waitForTimeout(60); return p; }
  }
  return null;
}
const C = page => page.evaluate(() => ({ open: !document.getElementById('ctx').hidden, sid: ctxSid, list: ctxList.slice(), i: ctxList.indexOf(ctxSid),
  end: (e => e && !e.hidden ? e.textContent : '')(document.getElementById('ctxEnd')), msg: document.getElementById('ctxMsg').textContent,
  moves: JSON.stringify(Object.keys(moves).sort().map(k => [k, moves[k]])), checked: JSON.stringify(Object.keys(checked).sort().map(k => [k, checked[k]])),
  tray: outList().length, step, s2: s2Cur, s2msg: document.getElementById('s2Msg').textContent, scroll: document.querySelector('#ctx .box').scrollTop,
  fixing: !!fix, big: getComputedStyle(document.getElementById('ctxBig')).transform, tile: getComputedStyle(document.getElementById('s2Tile')).transform }));
const same = (a, b) => a.moves === b.moves && a.checked === b.checked && a.tray === b.tray;
const tx = m => { const r = /matrix\(([^)]+)\)/.exec(m || ''); return r ? +r[1].split(',')[4] : 0; };
async function load(page, file) { page.__touch = undefined; await page.goto(file);
  await page.waitForFunction(() => typeof ready !== 'undefined' && ready, null, { timeout: 60000 }).catch(() => {}); await page.waitForTimeout(500); }
async function closeCard(page) { await page.evaluate(() => { if (!document.getElementById('ctx').hidden) closeCtx(); }); await page.waitForTimeout(120); }

// ---- the card: open with "Go through" on the first pile (a finger tap), walk it with swipes
async function card(page, dev, full) {
  await page.evaluate(() => { if (step !== 1) setStep(1); }); await page.waitForTimeout(200);
  const go = await on(page, '#list .pile .ph .big');
  ok(!!go && await page.evaluate(() => document.querySelector('#list .pile .ph .big').textContent === 'Go through'), `${dev}: each pile has a "Go through" button`);
  if (!go) return;
  await page.touchscreen.tap(go.x, go.y); await page.waitForTimeout(400);
  let c = await C(page); const L = c.list, N = L.length, s0 = c;
  ok(c.open && c.i === 0 && N >= 4, `${dev}: "Go through" opens the card on the pile's first sign, walking ${N} signs`, c.sid);
  if (!c.open || N < 4) return;
  const hint = await page.evaluate(() => document.getElementById('ctxPanHint').textContent);
  ok(/Swipe left or right/.test(hint) && /not on the page picture/.test(hint) && /Doesn’t belong: take out/.test(hint) && !/\b(red|green|orange|blue)\b/i.test(hint),
    `${dev}: the card's hint says swipe left or right (not on the picture) and how to take a bad fit out, no colour word`, hint);
  // 1-3. swipes from different places on the card; the enlarged sign follows mid-swipe; no click anywhere
  const where = [['the title', '#ctxT', -1], ['a button ("Bad cut")', '#ctxBad', -1], ['the enlarged sign', '#ctxBigW', 1], ['the place line', '#ctxS', 1]];
  let i = 0;
  for (const [name, sel, dir] of where) {
    const p = await on(page, sel); if (!p) { skip(`${dev}: ${name} is not on screen in the card`); continue; }
    const before = await C(page), title0 = await page.evaluate(() => document.getElementById('ctxT').getBoundingClientRect().left);
    const r = await swipe(page, p.x, p.y, dir < 0 ? -140 : 140, 6, { what: 'card, ' + name,
      mid: () => page.evaluate(() => ({ big: getComputedStyle(document.getElementById('ctxBig')).transform, title: document.getElementById('ctxT').getBoundingClientRect().left })) });
    c = await C(page); const want = Math.max(0, Math.min(N - 1, i + (dir < 0 ? 1 : -1)));
    ok(c.sid === L[want] && JSON.stringify(c.list) === JSON.stringify(L) && same(before, c), `${dev}: a swipe ${dir < 0 ? 'left' : 'right'} starting on ${name} goes to sign ${want + 1} of ${N} (nothing moved, kept or taken out)`, [before.sid, c.sid]);
    ok(!r.clicks.length, `${dev}: ...and no click fired (not on ${name})`, r.clicks);
    const m = tx(r.mid && r.mid.big);
    ok(m !== 0 && Math.abs(m) <= 36.5 && Math.sign(m) === (dir < 0 ? -1 : 1) && Math.abs(r.mid.title - title0) < 0.5 && tx(c.big) === 0,
      `${dev}: ...during it the enlarged sign followed the finger a little (${m.toFixed(1)} px), nothing else moved, and it sprang back`, { mid: r.mid && r.mid.big, after: c.big });
    i = want;
  }
  // the question, when a sign of the walk has one
  const qi = await page.evaluate(L => L.findIndex((s, k) => k > 0 && k < L.length - 1 && focusQ[s]), L);
  if (qi < 0) skip(`${dev}: no sign in this walk carries a question`);
  else { await page.evaluate(s => showCtx(s, pileOf(s), true), L[qi]); await page.waitForTimeout(200); const p = await on(page, '#ctxQ');
    if (!p) skip(`${dev}: the question is not on screen`);
    else { const b0 = await C(page), r = await swipe(page, p.x, p.y, -140, 4, { what: 'card, question' }); c = await C(page);
      ok(c.sid === L[qi + 1] && same(b0, c) && !r.clicks.length, `${dev}: a swipe left on the question goes to the next sign`, [b0.sid, c.sid]); } }
  // the ends: no wrap, the end words
  const at = async (k, sel, dx, name, re) => { await page.evaluate(s => showCtx(s, pileOf(s), true), L[k]); await page.waitForTimeout(200);
    const p = await on(page, sel); const r = await swipe(page, p.x, p.y, dx, 5, { what: 'card end' }); const a = await C(page);
    const w = Math.max(0, Math.min(N - 1, k + (dx < 0 ? 1 : -1)));
    ok(a.sid === L[w] && !r.clicks.length, `${dev}: ${name}`, a.sid); return a; };
  await at(N - 2, '#ctxT', -140, `a swipe left on sign ${N - 1} of ${N} goes to the last`);
  c = await at(N - 1, '#ctxT', -140, 'one more swipe left stays on the last sign (no wrap)');
  ok(/^Last of \d+ in family /.test(c.end) && /— that family is done/.test(c.msg), `${dev}: ...and says in words that it is the last of the family`, [c.end, c.msg]);
  c = await at(0, '#ctxS', 140, 'a swipe right on the first sign stays on it (no wrap)');
  ok(/^First sign in family /.test(c.end) && /there is none before it/.test(c.msg), `${dev}: ...and says in words that it is the first`, [c.end, c.msg]);
  // 4. a short swipe, two fingers, the "Move this tile to…" list, and while fixing a cut: no step
  await page.evaluate(s => showCtx(s, pileOf(s), true), L[1]); await page.waitForTimeout(200);
  { const p = await on(page, '#ctxT'); const b0 = await C(page), r = await swipe(page, p.x, p.y, -30, 2, { what: 'short swipe' }); c = await C(page);
    ok(c.sid === b0.sid && !r.clicks.length, `${dev}: a swipe of 30 px steps nothing`, c.sid); }
  { const p = await on(page, '#ctxS'); const b0 = await C(page), cl = await two(page, p.x, p.y, -150); c = await C(page);
    ok(c.sid === b0.sid && same(b0, c) && !cl.length, `${dev}: a two-finger sideways swipe steps nothing`, c.sid); }
  { const p = await on(page, '#ctxDest'); if (!p) skip(`${dev}: the "Move this tile to…" list is not on screen`);
    else { const b0 = await C(page), r = await swipe(page, p.x, p.y, -140, 4, { what: 'move list' }); c = await C(page);
      ok(c.sid === b0.sid && same(b0, c), `${dev}: a swipe on the "Move this tile to…" list steps nothing and moves nothing`, c.sid); } }
  { const f = await on(page, '#ctxFix'); await page.touchscreen.tap(f.x, f.y); await page.waitForTimeout(250);
    const p = await on(page, '#ctxT'); const b0 = await C(page), r = await swipe(page, p.x, p.y, -140, 4, { what: 'while fixing' }); c = await C(page);
    ok(b0.fixing && c.fixing && c.sid === b0.sid && !r.clicks.length, `${dev}: while a cut is being fixed a swipe steps nothing and the editor stays`, [b0.fixing, c.fixing, c.sid]);
    await page.evaluate(() => document.getElementById('fixCancel').click()); await page.waitForTimeout(200); }
  // 5. vertical on the card: it scrolls; the picture pans
  { await page.evaluate(() => { document.querySelector('#ctx .box').scrollTop = 0; }); await page.waitForTimeout(100);
    const room = await page.evaluate(() => { const b = document.querySelector('#ctx .box'); return b.scrollHeight - b.clientHeight; });
    const q = await on(page, '#ctxS');
    if (room < 30 || !q) skip(`${dev}: the card fits the screen, nothing to scroll (${room} px)`);
    else { const b0 = await C(page), up = b0.scroll < room / 2;   // a finger up scrolls the box down, a finger down scrolls it up
      const r = await swipe(page, q.x, q.y, 4, up ? -160 : 160, { steps: 8, what: 'card vertical' }); c = await C(page);
      ok((up ? c.scroll > b0.scroll + 20 : c.scroll < b0.scroll - 20) && c.sid === b0.sid && same(b0, c) && !r.clicks.length,
        `${dev}: a swipe ${up ? 'up' : 'down'} on the card scrolls its box (${b0.scroll} -> ${c.scroll} of ${room}) and steps nothing`, c.sid); } }
  { await page.evaluate(() => { const z = document.getElementById('ctxZ'); z.value = 8; z.dispatchEvent(new Event('input')); }); await page.waitForTimeout(300);
    const pan = await page.evaluate(() => (document.getElementById('ctxC')._pan || {}).pannable);
    const p = await on(page, '#ctxC');
    if (!pan || !p) skip(`${dev}: the picture shows all of its line here, nothing to pan`);
    else { const b0 = await C(page), r = await swipe(page, p.x + 40, p.y, -150, 0, { what: 'picture' }); c = await C(page);
      const moved = await page.evaluate(() => !!(document.getElementById('ctxC')._pan || {}).moved);
      ok(moved && c.sid === b0.sid && same(b0, c), `${dev}: a slide on the picture moves the view (R09) and steps nothing`, { moved, sid: c.sid }); } }
  if (full) await page.screenshot({ path: full });
  ok(same(s0, await C(page)), `${dev}: after all the card swipes nothing was moved, kept or taken out`);
  await closeCard(page);
}

// ---- step 2: the pinned sign and everything above the pile cards
async function step2(page, dev) {
  await page.evaluate(() => { if (step !== 2) setStep(2); }); await page.waitForTimeout(400);
  const L = await page.evaluate(() => outList()); if (L.length < 4) { skip(`${dev}: step 2 has ${L.length} signs waiting (needs 4)`); return; }
  await page.evaluate(s => { s2Cur = s; renderS2(); document.getElementById('s2Msg').textContent = ''; }, L[0]); await page.waitForTimeout(200);
  const s0 = await C(page); let c;
  const go = async (name, sel, dx, want, opt = {}) => { const p = await on(page, sel); if (!p) { skip(`${dev}: ${name} is not on screen in step 2`); return null; }
    const b0 = await C(page), r = await swipe(page, p.x, p.y, dx, 5, { what: 'step 2, ' + name, mid: opt.mid }); c = await C(page);
    ok(c.s2 === L[want] && same(b0, c) && !c.open && !r.clicks.length, `${dev}: step 2, a swipe ${dx < 0 ? 'left' : 'right'} on ${name} ${opt.label || 'goes to sign ' + (want + 1)} (nothing placed, no card, no click)`,
      { from: b0.s2, to: c.s2, clicks: r.clicks }); return r; };
  const r = await go('the pinned sign', '#s2Tile', -140, 1, { label: 'is Skip: the next question', mid: () => page.evaluate(() => getComputedStyle(document.getElementById('s2Tile')).transform) });
  if (r) { const m = tx(r.mid); ok(m < 0 && m >= -36.5 && tx(c.tile) === 0, `${dev}: step 2, the pinned sign followed the finger a little (${m.toFixed(1)} px) and sprang back`, [r.mid, c.tile]); }
  await go('the pinned sign', '#s2Tile', 140, 0, { label: 'is Previous' });
  await go('the pinned sign', '#s2Tile', 140, 0, { label: 'at the first stays (Previous is off)' });
  ok(/first sign waiting/.test(c.s2msg), `${dev}: step 2, ...and says it is the first sign waiting`, c.s2msg);
  await go('the line strip', '#s2C', -140, 1);
  await go('a button ("Bad cut", not pressed)', '#s2Bad', -140, 2);
  const q = await page.evaluate(() => { const e = document.getElementById('s2Q'); return !e.hidden && !!e.textContent; });
  if (q) { const open0 = await page.evaluate(() => document.getElementById('s2Q').className); await go('the question', '#s2Q', 140, 1);
    ok(await page.evaluate(() => document.getElementById('s2Q').className) === open0, `${dev}: step 2, the swipe on the question did not open or fold it (no tap)`); }
  else { await go('the title', '#s2T', 140, 1); }
  await page.evaluate(s => { s2Cur = s; renderS2(); document.getElementById('s2Msg').textContent = ''; }, L[L.length - 1]); await page.waitForTimeout(200);
  await go('the pinned sign', '#s2Tile', -140, L.length - 1, { label: 'at the last stays (Skip is off)' });
  ok(/last sign waiting/.test(c.s2msg), `${dev}: step 2, ...and says it is the last sign waiting`, c.s2msg);
  // 7. a pile card: a swipe places nothing
  { const p = await on(page, '#cards .card', 0.5, 0.3); if (!p) skip(`${dev}: no pile card on screen`);
    else { const b0 = await C(page), rr = await swipe(page, p.x, p.y, -140, 4, { what: 'pile card' }); c = await C(page);
      ok(c.s2 === b0.s2 && same(b0, c) && !c.open, `${dev}: step 2, a sideways swipe on a pile card places nothing and moves nothing`, { s2: c.s2, clicks: rr.clicks }); } }
  ok(same(s0, await C(page)), `${dev}: step 2, after all the swipes nothing was placed`);
}

// ---- step 1: pile tiles, "Go through", the tray
async function step1(page, dev) {
  await page.evaluate(() => { if (step !== 1) setStep(1); }); await page.waitForTimeout(300);
  const sid = await page.evaluate(() => { const t = [...document.querySelectorAll('#list .pile .tiles > .t[data-sid]:not(.wait)')].find(e => e.getClientRects().length); return t ? t.dataset.sid : null; });
  { const p = await on(page, '#list .pile .tiles > .t[data-sid="' + sid + '"]'); const b0 = await C(page), r = await swipe(page, p.x, p.y, -120, 4, { what: 'pile tile' }); const c = await C(page);
    ok(same(b0, c) && !c.open, `${dev}: step 1, a sideways swipe on a pile tile (${sid}) takes nothing out and opens no card`, { tray: [b0.tray, c.tray], clicks: r.clicks }); }
  { const p = await on(page, '#list .pile .ph .big'); const b0 = await C(page); await swipe(page, p.x, p.y, -120, 3, { what: 'Go through' }); const c = await C(page);
    ok(same(b0, c) && !c.open, `${dev}: step 1, a sideways swipe on "Go through" opens no card`); await closeCard(page); }
  const hint = await page.evaluate(() => document.getElementById('hint1').innerText);
  ok(/Go through/.test(hint) && /swipe left or right \(not on the page picture\)/.test(hint) && /Doesn’t belong: take out/.test(hint) && !/\b(red|green|orange|blue)\b/i.test(hint),
    `${dev}: step 1's hint says "Go through", swipe left or right, and how to take a bad fit out, in plain words`, hint.slice(0, 120));
}
async function tray(page, dev) {
  await page.evaluate(() => { if (step !== 1) setStep(1); }); await page.waitForTimeout(300);
  // enough tiles in the tray to scroll it sideways at this width
  await page.evaluate(() => { const w = document.getElementById('trayTiles'); const free = Object.keys(itemBySid).filter(s => !moves[s] && !preTrayed(s));
    for (let k = 0; k < free.length && w.scrollWidth <= w.clientWidth + 60; k++) { takeOut(free[k], null); renderTray(); } });
  await page.waitForTimeout(400);
  const t = await page.evaluate(() => { const w = document.getElementById('trayTiles'); w.scrollLeft = 0; const r = w.getBoundingClientRect();
    const x = r.right - 16, y = r.top + r.height / 2, h = document.elementFromPoint(x, y), e = h && h.closest && h.closest('#trayTiles .t');   // a tile at the tray's visible right
    return e ? { x, y, room: w.scrollWidth - w.clientWidth } : { none: true, w: r.width }; });
  if (!t || t.none || t.room < 40) { ok(false, `${dev}: the tray holds enough to scroll sideways, a tile under the finger`, t); return; }
  const b0 = await C(page); await swipe(page, t.x, t.y, -110, 0, { steps: 6, what: 'tray' }); await page.waitForTimeout(300); const c = await C(page);
  const sl = await page.evaluate(() => document.getElementById('trayTiles').scrollLeft);
  ok(sl > 20 && same(b0, c) && !c.open && c.step === 1, `${dev}: the "Taken out" tray still scrolls sideways under a finger (${Math.round(sl)} px) and the swipe puts nothing back`, { tray: [b0.tray, c.tray], step: c.step });
}
async function lock(page, dev) {
  const s = await page.evaluate(() => { const ta = sel => { const e = document.querySelector(sel); return e ? getComputedStyle(e).touchAction : 'missing'; };
    return { html: getComputedStyle(document.documentElement).overscrollBehaviorX, body: getComputedStyle(document.body).overscrollBehaviorX,
      box: ta('#ctx .box'), top: ta('.s2top'), acts: ta('#s2Acts'), cv: ta('#s2Stick > .cv'), ctx: ta('#ctx') }; });
  ok(s.html === 'none' && s.body === 'none', `${dev}: overscroll-behavior-x is none on html and body`, { html: s.html, body: s.body });
  const good = v => /pan-y/.test(v) && !/pan-x|auto|manipulation/.test(v);
  ok(['box', 'top', 'acts', 'cv', 'ctx'].every(k => good(s[k])), `${dev}: every swipe region's touch-action is pan-y (with pinch-zoom), never pan-x`, s);
}

async function run(b, dev, opts, F, SHOTS) {
  const ctx = await b.newContext(opts); await mock.install(ctx);
  await ctx.addInitScript(() => { window.__clicks = []; window.addEventListener('click', e => { const t = e.target; window.__clicks.push((t.id || (t.className && String(t.className)) || t.tagName) + ''); }, true); });
  const page = await ctx.newPage(); page.on('pageerror', e => errs.push(dev + ': ' + e.message)); side = [];
  await load(page, 'file://' + path.join(F, 'plain.html'));
  await lock(page, dev);
  await card(page, dev, SHOTS ? path.join(SHOTS, 'swipe_' + dev.replace(/\W+/g, '') + '_card.png') : null);
  await step1(page, dev);
  await load(page, 'file://' + path.join(F, 'tray.html'));
  await step2(page, dev);
  await tray(page, dev);
  ok(!side.length, `${dev}: the page never moved sideways (window.scrollX, the root's scrollLeft, visualViewport.offsetLeft and the card's scrollLeft stayed 0)`, side.slice(0, 3));
  await ctx.close();
}
async function probe(b, PAGE) {   // a real page: the card and step 2 step both ways, nothing moves, the page never moves sideways
  for (const [dev, opts] of DEVICES.slice(0, 2)) {
    const ctx = await b.newContext(opts); await mock.install(ctx);
    await ctx.addInitScript(() => { window.__clicks = []; window.addEventListener('click', e => window.__clicks.push(String(e.target.id || e.target.tagName)), true); });
    const page = await ctx.newPage(); page.on('pageerror', e => errs.push(dev + ': ' + e.message)); side = [];
    page.on('console', m => { if (m.type() === 'error') errs.push(dev + ' console: ' + m.text()); });
    await load(page, 'file://' + path.resolve(PAGE)); await lock(page, dev);
    // the card: the first pile whose walk has 3 signs or more, with "Go through"
    await page.evaluate(() => { if (step !== 1) setStep(1); }); await page.waitForTimeout(300);
    const k = await page.evaluate(() => [...document.querySelectorAll('#list .pile')].findIndex(p => p.querySelectorAll(':scope > .tiles > .t[data-sid]').length >= 3));
    if (k < 0) skip(`${dev}: no pile of 3 signs`);
    else { await page.evaluate(k => { const e = document.querySelectorAll('#list .pile')[k]; e.scrollIntoView({ block: 'center' }); e.classList.add('__probe'); }, k);
      const g = await on(page, '#list .pile.__probe .ph .big'); await page.touchscreen.tap(g.x, g.y); await page.waitForTimeout(500);
      // the walk is the pile's whole family (R11): "Go through" opens it at this pile's first sign, k0 (0 for the family's first pile)
      let c = await C(page); const L = c.list, k0 = c.i; ok(c.open && k0 >= 0 && k0 < L.length - 1 && L.length >= 3, `${dev}: "Go through" opens the card at sign ${k0 + 1}, walking ${L.length} signs`, c.sid);
      if (c.open && k0 >= 0 && k0 < L.length - 1) { const s0 = c;
        let p = await on(page, '#ctxT'); let r = await swipe(page, p.x, p.y, -140, 5, { what: 'card left' }); c = await C(page);
        ok(c.sid === L[k0 + 1] && !r.clicks.length, `${dev}: a swipe left on the card goes to the next sign`, [s0.sid, c.sid]);
        p = await on(page, '#ctxActs button:not([hidden])'); r = await swipe(page, p.x, p.y, 140, 5, { what: 'card right' }); c = await C(page);
        ok(c.sid === L[k0] && !r.clicks.length && same(s0, c), `${dev}: a swipe right starting on a button goes back, presses nothing`, [c.sid, r.clicks]);
        await page.evaluate(s => showCtx(s, pileOf(s), true), L[0]); await page.waitForTimeout(250);
        p = await on(page, '#ctxT'); r = await swipe(page, p.x, p.y, 140, 5, { what: 'card first' }); c = await C(page);
        ok(c.sid === L[0] && /^First sign in /.test(c.end) && same(s0, c), `${dev}: at the first sign it stops and says so`, c.end); }
      await closeCard(page); }
    // step 2, when signs wait there
    const n = await page.evaluate(() => { if (step !== 2) setStep(2); return outList().length; }); await page.waitForTimeout(500);
    if (n < 2) skip(`${dev}: ${n} sign(s) waiting in step 2`);
    else { const L = await page.evaluate(() => outList()); await page.evaluate(s => { s2Cur = s; renderS2(); }, L[0]); await page.waitForTimeout(300);
      const s0 = await C(page); let p = await on(page, '#s2Tile'); let r = await swipe(page, p.x, p.y, -140, 5, { what: 's2 left' }); let c = await C(page);
      ok(c.s2 === L[1] && same(s0, c) && !c.open && !r.clicks.length, `${dev}: step 2, a swipe left on the pinned sign is Skip`, [s0.s2, c.s2]);
      p = await on(page, '#s2Tile'); r = await swipe(page, p.x, p.y, 140, 5, { what: 's2 right' }); c = await C(page);
      ok(c.s2 === L[0] && same(s0, c) && !c.open && !r.clicks.length, `${dev}: step 2, a swipe right is Previous`, [c.s2]);
      p = await on(page, '#cards .card', 0.5, 0.3);
      if (p) { r = await swipe(page, p.x, p.y, -140, 4, { what: 's2 card' }); c = await C(page); ok(c.s2 === L[0] && same(s0, c), `${dev}: step 2, a swipe on a pile card places nothing`); } }
    ok(!side.length, `${dev}: the page never moved sideways`, side.slice(0, 3));
    await ctx.close();
  }
}

(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_EXE || '/opt/pw-browsers/chromium', args: ['--allow-file-access-from-files'] });
  if (process.argv[2] === '--probe') { try { await probe(b, process.argv[3]); } catch (e) { ok(false, 'the probe finished without an exception', e.message.split('\n')[0]); } }
  else { const F = path.resolve(process.argv[2]), SHOTS = process.argv[3];
    for (const [dev, opts] of DEVICES) { try { await run(b, dev, opts, F, SHOTS); } catch (e) { ok(false, dev + ': the run finished without an exception', e.message.split('\n')[0]); } } }
  ok(!errs.length, 'no page errors', errs.join(' | '));
  if (failed.length) { console.log('failed checks (repeated here so a log tail shows them):'); failed.forEach(m => console.log('  - ' + m)); }
  console.log('errors:', errs); console.log(fails ? fails + ' FAILED' : 'ALL PASS');
  await b.close(); process.exit(fails ? 1 : 0);
})();
