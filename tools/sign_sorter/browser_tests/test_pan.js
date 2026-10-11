// Owner rule R09 (tools/data/sorter_owner_requirements.tsv; Bergh, 11 Oct 2026: "I wish when I clicked into a symbols page I could slide
// my finger on the manuscript surrounding my target symbol to see its surroundings"; Vivonne box check, 10 Oct: "I marked a bunch a bad
// cut if when I clicked into it I couldn't move the manuscript to properly see around it"): in a sign's card, one finger (or a mouse drag)
// on the manuscript picture moves the view like a map, two fingers pinch the zoom, "Back to the sign" re-centres, the sideways swipe to the
// next sign stays on the enlarged sign, and Fix the cut still edits the box (a drag off the box moves the view).
//
// Devices: iPhone 13 and iPhone SE (Playwright device profiles; touch through CDP Input.dispatchTouchEvent, the path a phone takes, two
// touch points for a pinch) and a desktop mouse. Fixtures (make_fixtures.py): lines.html (line crops t_L01..t_L05, no region: the
// "Line strips" view with lines above and below, and lines n-2 / n+2 beyond them), region.html (the "Whole page" view) and plain.html
// (single line crops, no neighbour: Fix the cut). Checks, per device:
//   1. a drag of 80 px left / right and 60 px up / down on the picture moves the window by the drag (within 8%, at least 2 image px;
//      read from canvas._pan, the window in the drawn image's pixels) in both views, the bracketed box moves with the page, the sign
//      (ctxSid) and the answers stay the same; a drag far past an edge stops at the sheet's edge (the whole line, the whole region, the
//      further lines n-2 / n+2), never past it; ten moves inside one frame draw once (requestAnimationFrame)
//   2. a sideways swipe on the picture does not change the sign; on the enlarged sign (#ctxBigW) it does (touch only)
//   3. "Back to the sign" restores the window the card opened with; so do the Zoom slider and Next
//   4. a two-finger pinch out raises the Zoom slider, a pinch in lowers it (touch only)
//   5. Fix the cut: a drag on the box's right edge moves that edge, a drag off the box moves the view and leaves the box (strip pixels)
//      as it was, the edge dragged again from where it now is, and Save writes the recut doc in the same shape as before (sid, page, x y
//      w h = the quad's bounds, quad, mask, old, at) -- in the line strips and in the "Whole page" view
//   6. "Erase stray ink": one finger paints a stroke (and does not move the view); two fingers move the view and paint nothing (touch only)
//   7. iPhone SE: a slide on the picture moves the view and does not scroll the card; every answer button is reached by sliding the card
//      with a finger outside the picture
//   8. a tap or a hold on the picture moves nothing, takes nothing out and keeps the card on the same sign (owner rule R05 is for tiles);
//      the card opens on a HOLD on the tile (R05), the hint says it in plain words and names no colour (R07); zero page errors.
// Usage: PW_EXE=/opt/pw-browsers/chromium NODE_PATH=$(npm root -g) node test_pan.js FIXTURE_DIR [SHOT_DIR]      (exit 1 on any FAIL)
//        node test_pan.js --probe PAGE   the tools/sorter_preflight.py 'pan' check on any built page: iPhone 13, a tile whose card can
//        move, a drag 80 px left and 60 px down on the picture: the view moved by the drag, the sign unchanged, no page error (a page whose
//        every line is shown to its top and bottom -- nothing above or below to move to -- is checked sideways only, and says so).
const { chromium, devices } = require('playwright'); const mock = require('./mock_db'); const path = require('path');
let fails = 0; const errs = [], failed = [];
const ok = (cond, msg, extra) => { console.log((cond ? 'ok   ' : 'FAIL ') + msg + (extra !== undefined ? '  [' + (typeof extra === 'string' ? extra : JSON.stringify(extra)) + ']' : '')); if (!cond) { fails++; failed.push(msg); } };
const skip = msg => console.log('skip ' + msg);
const prof = d => { const o = { ...devices[d] }; delete o.defaultBrowserType; return o; };
const near = (a, b, tol) => Math.abs(a - b) <= Math.max(2, tol * Math.abs(b));

// the card's window, the sheet it moves over, and the state that must not change
const P = page => page.evaluate(() => { const c = document.getElementById('ctxC'), m = c._map, v = c._pan || {}, bx = document.querySelector('#ctx .box');
  return { sid: ctxSid, open: !document.getElementById('ctx').hidden, vx: v.vx, vy: v.vy, vw: v.vw, vh: v.vh, wx0: v.wx0, wx1: v.wx1, wy0: v.wy0, wy1: v.wy1,
    x0: v.x0, y0: v.y0, pannable: !!v.pannable, moved: !!v.moved, sc: m ? m.s / m.k : 0, z: +document.getElementById('ctxZ').value, view: c.dataset.view,
    scroll: bx.scrollTop, centreOff: document.getElementById('ctxCentre').disabled, ta: c.style.touchAction }; });
const S = page => page.evaluate(() => ({ moves: JSON.stringify(Object.keys(moves).sort().map(k => [k, moves[k]])),
  checked: JSON.stringify(Object.keys(checked).sort().map(k => [k, checked[k]])), tray: outList().length, recuts: JSON.stringify(recuts), added: JSON.stringify(added) }));
const same = (a, b) => a.moves === b.moves && a.checked === b.checked && a.tray === b.tray && a.recuts === b.recuts && a.added === b.added;
// screen point of the tile's box centre (or of the box being fixed), through the card's own map (strip or page view)
const boxAt = (page, fx = 0.5, fy = 0.5) => page.evaluate(([fx, fy]) => { const c = document.getElementById('ctxC'), m = c._map, r = c.getBoundingClientRect(), it = itemBySid[ctxSid];
  const [x, y, w, h] = fix ? fix.box : boxOf(ctxSid), X = x + w * fx, Y = y + h * fy;
  if (m.toSrc) return { x: r.left + (X - m.x0) * m.s / m.k, y: r.top + (regY(it.p, X, Y) - m.y0) * m.s / m.k };
  return { x: r.left + (X * m.ps - m.x0) * m.s / m.k, y: r.top + (m.ha + (Y * m.ps - m.y0) * m.s) / m.k }; }, [fx, fy]);
// a point on the picture (fx, fy of its rectangle), the picture scrolled into the card's view first
async function picAt(page, fx = 0.5, fy = 0.5) {
  await page.evaluate(() => { const c = document.getElementById('ctxC'), bx = document.querySelector('#ctx .box'), r = c.getBoundingClientRect(), b = bx.getBoundingClientRect();
    if (r.top < b.top + 60 || r.bottom > Math.min(b.bottom, innerHeight)) c.scrollIntoView({ block: 'center' }); });
  await page.waitForTimeout(120);
  return page.evaluate(([fx, fy]) => { const r = document.getElementById('ctxC').getBoundingClientRect(); return { x: r.left + r.width * fx, y: r.top + r.height * fy }; }, [fx, fy]);
}
async function drag(page, x, y, dx, dy, steps = 10) {
  await mock.gesture(page, 'down', x, y);
  for (let i = 1; i <= steps; i++) { await mock.gesture(page, 'move', x + dx * i / steps, y + dy * i / steps); await page.waitForTimeout(16); }
  await mock.gesture(page, 'up', x + dx, y + dy); await page.waitForTimeout(150);
}
const cdpOf = async page => page.__cdp || (page.__cdp = await page.context().newCDPSession(page));
async function two(page, type, pts) { const cdp = await cdpOf(page); await cdp.send('Input.dispatchTouchEvent', { type, touchPoints: pts.map((p, i) => ({ x: p[0], y: p[1], id: i + 1 })) }); }
async function twoDrag(page, a, b, da, db, steps = 10) {   // two fingers from a and b, each moved by its own (dx, dy)
  await two(page, 'touchStart', [a, b]);
  for (let i = 1; i <= steps; i++) { await two(page, 'touchMove', [[a[0] + da[0] * i / steps, a[1] + da[1] * i / steps], [b[0] + db[0] * i / steps, b[1] + db[1] * i / steps]]); await page.waitForTimeout(16); }
  await two(page, 'touchEnd', []); await page.waitForTimeout(200);
}
async function waitCard(page, sid) {
  await page.waitForFunction(s => { const c = document.getElementById('ctxC'); return !document.getElementById('ctx').hidden && ctxSid === s && c.dataset.sid === s && c._pan; }, sid, { timeout: 5000 }).catch(() => {});
  await page.waitForTimeout(250);
}
async function openByHold(page, sid) {   // owner rule R05: a hold on the tile opens its card
  await page.evaluate(() => { if (typeof closeCtx === 'function' && !document.getElementById('ctx').hidden) closeCtx(); if (step !== 1) setStep(1); });
  const loc = page.locator('#list .pile .tiles .t[data-sid="' + sid + '"]').first();
  if (!(await loc.count())) { await page.evaluate(s => showCtx(s, pileOf(s)), sid); } else await mock.hold(page, loc, 700);
  await waitCard(page, sid);
}
const recentre = async page => { await page.evaluate(() => document.getElementById('ctxCentre').click()); await page.waitForTimeout(80); };   // no-op when already centred
const setZoom = async (page, z) => { await page.evaluate(z => { const e = document.getElementById('ctxZ'); e.value = z; e.dispatchEvent(new Event('input')); }, z); await page.waitForTimeout(200); };
const room = p => ({ l: p.vx - p.wx0, r: p.wx1 - (p.vx + p.vw), u: p.vy - p.wy0, d: p.wy1 - (p.vy + p.vh) });
// the lowest zoom (from the one the card opened at) whose window has room for the drags in every direction asked
async function roomy(page, dxCss, dyCss) {
  const z0 = (await P(page)).z;
  for (let z = z0; z <= 8; z++) { if (z !== z0) await setZoom(page, z); const p = await P(page), r = room(p), nx = 1.2 * dxCss / p.sc, ny = 1.2 * dyCss / p.sc;
    if ((!dxCss || (r.l >= nx && r.r >= nx)) && (!dyCss || (r.u >= ny && r.d >= ny))) return p; }
  return null;
}

// 1. four directions, the box moving with the page, the sign and the answers unchanged
async function four(page, dev, where) {
  const p0 = await roomy(page, 80, 60);
  if (!p0) { ok(false, `${dev}, ${where}: the window has room to move 80 px sideways and 60 px up and down at some zoom`); return; }
  for (const [dx, dy, name] of [[-80, 0, 'left'], [80, 0, 'right'], [0, -60, 'up'], [0, 60, 'down']]) {
    await page.evaluate(() => document.getElementById('ctxCentre').click()); await page.waitForTimeout(80);
    const a = await P(page), s0 = await S(page), at = await picAt(page, 0.5, 0.5), b0 = await boxAt(page);
    await drag(page, at.x, at.y, dx, dy); const b = await P(page), s1 = await S(page), b1 = await boxAt(page);
    const ex = -dx / a.sc, ey = -dy / a.sc, gx = b.vx - a.vx, gy = b.vy - a.vy;
    ok(near(gx, ex, 0.08) && near(gy, ey, 0.08) && b.sid === a.sid && b.open && same(s0, s1) && b.moved && !b.centreOff,
      `${dev}, ${where}: a drag ${Math.abs(dx || dy)} px ${name} on the picture moves the view with the finger (same sign, nothing moved, "Back to the sign" on)`,
      { zoom: a.z, moved: [+gx.toFixed(1), +gy.toFixed(1)], expected: [+ex.toFixed(1), +ey.toFixed(1)], sign: b.sid });
    ok(Math.abs(b1.x - b0.x - dx) <= 3 && Math.abs(b1.y - b0.y - dy) <= 3, `${dev}, ${where}: the sign's brackets move with the page (${name})`,
      { by: [+(b1.x - b0.x).toFixed(1), +(b1.y - b0.y).toFixed(1)] });
  }
}
// a drag far past each edge stops at the edge of the sheet
async function edges(page, dev, where) {
  await page.evaluate(() => document.getElementById('ctxCentre').click()); await page.waitForTimeout(80);
  const at = await picAt(page, 0.5, 0.5), out = {};
  for (const [dx, dy, k] of [[2000, 0, 'l'], [-2000, 0, 'r'], [0, 1500, 'u'], [0, -1500, 'd']]) {
    await page.evaluate(() => document.getElementById('ctxCentre').click()); await page.waitForTimeout(60);
    for (let i = 0; i < 3; i++) { await drag(page, at.x, at.y, dx / 4, dy / 4, 6); await page.waitForTimeout(150); }   // three slides (further lines load on the way)
    out[k] = room(await P(page)); }
  ok(out.l.l <= 0.5 && out.r.r <= 0.5 && out.u.u <= 0.5 && out.d.d <= 0.5 && Object.values(out).every(r => r.l >= -0.5 && r.r >= -0.5 && r.u >= -0.5 && r.d >= -0.5),
    `${dev}, ${where}: a drag far past each edge stops at the sheet's edge (left, right, top, bottom), never beyond it`,
    Object.fromEntries(Object.entries(out).map(([k, r]) => [k, r[k].toFixed(1)])));
}

async function run(b, dev, opts, F, SHOTS) {
  const touch = dev !== 'desktop';
  const ctx = await b.newContext(opts); const store = await mock.install(ctx); const page = await ctx.newPage();
  page.on('pageerror', e => errs.push(dev + ': ' + e.message));
  const load = async f => { page.__touch = undefined; await page.goto('file://' + path.join(F, f)); await page.waitForFunction(() => typeof ready !== 'undefined' && ready, null, { timeout: 30000 }).catch(() => {}); await page.waitForTimeout(300); };

  // ---- A. the line strips with lines above and below (lines.html)
  await load('lines.html');
  { const sid = 't_L03_16'; const s0 = await S(page); await openByHold(page, sid); const p = await P(page), s1 = await S(page);
    ok(p.open && p.sid === sid && same(s0, s1), `${dev}: a hold on the tile opens its card (owner rule R05) and moves nothing`, { sid: p.sid });
    const hint = await page.evaluate(() => document.getElementById('ctxPanHint').textContent);
    ok(/look around/.test(hint) && (!touch || /swipe the big sign/.test(hint)) && !/\b(red|green|orange|blue)\b/i.test(hint), `${dev}: the card says in plain words how to look around (no colour)`, hint);
    ok(p.view === 'strip' && p.pannable && p.ta === 'none' && p.centreOff && p.wy0 < -1 && p.wy1 > p.vh + 1, `${dev}, line strips: the picture can move (touch-action none, "Back to the sign" off until it does, line n-2 above and n+2 below on the sheet)`,
      { ta: p.ta, sheet: [p.wy0, p.wy1].map(v => +v.toFixed(1)), window: +p.vh.toFixed(1) });
    await four(page, dev, 'line strips');
    await edges(page, dev, 'line strips');
    // 3. Back to the sign
    { const at = await picAt(page); await drag(page, at.x, at.y, -70, 40); const a = await P(page);
      await page.click('#ctxCentre'); await page.waitForTimeout(200); const c = await P(page);
      ok(a.moved && !c.moved && Math.abs(c.vx - c.x0) < 0.5 && Math.abs(c.vy - c.y0) < 0.5 && c.centreOff && c.sid === sid, `${dev}: "Back to the sign" puts the window back where the card opened it`,
        { before: [a.vx, a.vy].map(v => +v.toFixed(1)), after: [c.vx, c.vy].map(v => +v.toFixed(1)), opened: [c.x0, c.y0].map(v => +v.toFixed(1)) }); }
    // requestAnimationFrame: ten moves inside one frame draw once
    { const n = await page.evaluate(() => new Promise(res => { const c = document.getElementById('ctxC'), r = c.getBoundingClientRect(), x = r.left + r.width / 2, y = r.top + r.height / 2;
        let k = 0; const orig = window.drawCtx; window.drawCtx = function () { k++; return orig.apply(this, arguments); };
        const ev = (t, X, Y) => c.dispatchEvent(new PointerEvent(t, { pointerId: 77, pointerType: 'mouse', button: 0, buttons: t === 'pointerup' ? 0 : 1, clientX: X, clientY: Y, bubbles: true, cancelable: true }));
        requestAnimationFrame(() => { ev('pointerdown', x, y); for (let i = 1; i <= 10; i++) ev('pointermove', x - 3 * i, y); const k0 = k;
          requestAnimationFrame(() => requestAnimationFrame(() => { ev('pointerup', x - 30, y); window.drawCtx = orig; res([k0, k]); })); }); }));
      ok(n[0] === 0 && n[1] >= 1 && n[1] <= 2, `${dev}: ten pointer moves inside one frame draw the picture once, on the next frame (requestAnimationFrame)`, { during: n[0], after: n[1] });
      await recentre(page); await page.waitForTimeout(100); }
    // 8. a tap and a hold on the picture: nothing moves, nothing is taken out, the same sign
    for (const kind of ['tap', 'hold']) { const s0 = await S(page), a = await P(page), at = await picAt(page, 0.3, 0.5);
      if (kind === 'tap') { if (touch) await page.touchscreen.tap(at.x, at.y); else await page.mouse.click(at.x, at.y); }
      else { await mock.gesture(page, 'down', at.x, at.y); await page.waitForTimeout(800); await mock.gesture(page, 'up', at.x, at.y); }
      await page.waitForTimeout(400); const s1 = await S(page), c = await P(page);
      ok(same(s0, s1) && c.open && c.sid === a.sid && Math.abs(c.vx - a.vx) < 0.5 && Math.abs(c.vy - a.vy) < 0.5, `${dev}: a ${kind} on the picture changes nothing (no move, nothing taken out, same sign, same view)`,
        { sid: c.sid, tray: [s0.tray, s1.tray] }); }
    // 2. a sideways swipe: on the picture it moves the view, never the sign; on the enlarged sign it goes to the next one (touch)
    { const a = await P(page), at = await picAt(page); await drag(page, at.x + 60, at.y, -150, 0, 6); const c = await P(page);
      ok(c.sid === a.sid && c.open && c.vx > a.vx + 1, `${dev}: a quick sideways swipe on the picture moves the view and keeps the sign`, { sid: c.sid, vx: [a.vx, c.vx].map(v => +v.toFixed(1)) });
      if (touch) { await page.evaluate(() => document.getElementById('ctxBigW').scrollIntoView({ block: 'center' })); await page.waitForTimeout(150);
        const r = await page.locator('#ctxBigW').boundingBox(); const x = r.x + r.width / 2 + 60, y = r.y + r.height / 2;
        await drag(page, x, y, -150, 0, 6); await page.waitForTimeout(300); const d = await P(page);
        ok(d.sid !== a.sid && d.open && !d.moved, `${dev}: a sideways swipe on the enlarged sign goes to the next sign, opened on its sign (re-centred)`, { from: a.sid, to: d.sid });
        await page.evaluate(s => showCtx(s, pileOf(s), true), a.sid); await waitCard(page, a.sid); }
      else skip(`${dev}: the swipe on the enlarged sign is a touch gesture (Previous / Next and the arrow keys on a desk)`); }
    // re-centred by the Zoom slider and by Next
    { await recentre(page); const at = await picAt(page); await drag(page, at.x, at.y, -60, 30); const a = await P(page);
      await setZoom(page, a.z > 1 ? a.z - 1 : a.z + 1); const c = await P(page);
      ok(a.moved && !c.moved && c.sid === a.sid, `${dev}: a change on the Zoom slider re-centres the view on the sign`, { zoom: [a.z, c.z] });
      await drag(page, at.x, at.y, -60, 0); const d0 = await P(page); await page.click('#ctxNext'); await page.waitForTimeout(300); const d = await P(page);
      ok(d0.moved && !d.moved && d.sid !== d0.sid, `${dev}: Next opens the next sign centred`, { from: d0.sid, to: d.sid });
      await page.evaluate(s => showCtx(s, pileOf(s), true), sid); await waitCard(page, sid); }
    // 4. pinch (touch): spread the fingers -> the Zoom slider goes up; pinch them -> down
    if (touch) { await setZoom(page, 4); const a = await P(page), c = await picAt(page);
      await twoDrag(page, [c.x - 20, c.y], [c.x + 20, c.y], [-50, 0], [50, 0]); const u = await P(page);
      await twoDrag(page, [c.x - 70, c.y], [c.x + 70, c.y], [55, 0], [-55, 0]); const d = await P(page);
      ok(u.z > a.z && d.z < u.z && u.sid === a.sid && d.sid === a.sid && u.sc > a.sc && d.sc < u.sc, `${dev}: a two-finger pinch on the picture zooms (out: the slider up, in: down), same sign`, { zoom: [a.z, u.z, d.z] });
      await setZoom(page, (await P(page)).z); }
    else skip(`${dev}: pinch is a touch gesture (the Zoom slider on a desk)`);
    if (SHOTS) { await recentre(page); await page.waitForTimeout(100); await page.screenshot({ path: path.join(SHOTS, `pan_${dev.replace(/\W+/g, '')}_open.png`) });
      const at = await picAt(page); await drag(page, at.x, at.y, -80, 60); await page.screenshot({ path: path.join(SHOTS, `pan_${dev.replace(/\W+/g, '')}_moved.png`) }); }
    // 7. iPhone SE: a slide on the picture does not scroll the card; every answer button is reached by sliding outside the picture
    if (dev === 'iPhone SE') {
      await recentre(page); await page.evaluate(() => { document.querySelector('#ctx .box').scrollTop = 0; }); await page.waitForTimeout(150);
      { const a = await P(page), at = await picAt(page); const a2 = await P(page); await drag(page, at.x, at.y, 0, -100); const c = await P(page);
        ok(c.scroll === a2.scroll && c.vy > a2.vy + 1, 'iPhone SE: a slide up on the picture moves the view and does not scroll the card', { scroll: [a2.scroll, c.scroll], vy: [a2.vy, c.vy].map(v => +v.toFixed(1)) }); }
      await recentre(page); await page.evaluate(() => { document.querySelector('#ctx .box').scrollTop = 0; }); await page.waitForTimeout(150);
      const ids = await page.evaluate(() => [...document.querySelectorAll('#ctxActs button, #ctxActs select')].filter(e => !e.hidden && e.offsetParent).map(e => e.id));
      const reached = [], missed = []; const v0 = await P(page);
      for (const id of ids) { let got = false;
        for (let i = 0; i < 25 && !got; i++) {
          const st = await page.evaluate(id => { const e = document.getElementById(id), r = e.getBoundingClientRect(), bx = document.querySelector('#ctx .box'), b = bx.getBoundingClientRect();
            const bot = Math.min(b.bottom, innerHeight); if (r.top >= b.top && r.bottom <= bot) return { got: true };
            for (let y = bot - 12; y > b.top + 70; y -= 10) for (const x of [b.left + 14, b.left + b.width / 2, b.right - 14]) { const h = document.elementFromPoint(x, y);
              if (h && bx.contains(h) && !h.closest('canvas, button, select, input, label, summary, a, #ctxBigW')) return { x, y, up: r.bottom > bot, top: b.top }; }
            return { none: true }; }, id);
          if (st.got) { got = true; break; } if (st.none) break;
          const dy = st.up ? -Math.min(180, st.y - st.top - 40) : Math.min(180, 400);
          await drag(page, st.x, st.y, 0, dy, 8); await page.waitForTimeout(150); }
        (got ? reached : missed).push(id); }
      const v1 = await P(page);
      ok(!missed.length && reached.length >= 5 && v1.vx === v0.vx && v1.vy === v0.vy && v1.sid === v0.sid, `iPhone SE: every answer button is reached by sliding the card with a finger outside the picture (${reached.length} buttons; the view and the sign unchanged)`,
        { missed, view: v1.vx === v0.vx && v1.vy === v0.vy ? 'same' : 'MOVED' });
      if (SHOTS) await page.screenshot({ path: path.join(SHOTS, 'pan_iPhoneSE_buttons.png') });
    }
  }

  // ---- B. the "Whole page" view (region.html)
  await load('region.html');
  { const sid = await page.evaluate(() => byBase['X'].items.filter(it => it.p === 'r_L02')[3].sid); await openByHold(page, sid); const p = await P(page);
    ok(p.view === 'page' && p.open && p.sid === sid, `${dev}: the region page's card opens in the "Whole page" view`, { view: p.view });
    await four(page, dev, 'whole page');
    await edges(page, dev, 'whole page');
    // 5 (page view). Fix the cut: a drag off the box moves the view, the box keeps its strip pixels; the right edge still drags
    await setZoom(page, touch ? 5 : 3); await page.click('#ctxFix');   // a real press (after a hold the page swallows the lift's click until the next press)
    await page.waitForTimeout(250);
    await page.evaluate(() => document.getElementById('ctxC').scrollIntoView({ block: 'center' })); await page.waitForTimeout(150);
    const b0 = await page.evaluate(() => fix.box.slice()), a = await P(page), r = await page.locator('#ctxC').boundingBox(), e = await boxAt(page, 0.5, 0.5);
    const ox = e.x > r.x + r.width / 2 ? r.x + 14 : r.x + r.width - 14;   // a point well off the box
    await drag(page, ox, e.y, ox < e.x ? 50 : -50, 0); const c = await P(page), b1 = await page.evaluate(() => fix.box.slice());
    ok(b1.join() === b0.join() && Math.abs(c.vx - a.vx) > 1, `${dev}, whole page: fixing a cut, a drag off the box moves the view and leaves the box as it was`, { box: b1, vx: [a.vx, c.vx].map(v => +v.toFixed(1)) });
    const re = await boxAt(page, 1, 0.5); await drag(page, re.x, re.y, 24, 0); const b2 = await page.evaluate(() => fix.box.slice());
    ok(b2[2] > b0[2] + 3 && b2[0] === b0[0] && b2[1] === b0[1], `${dev}, whole page: after moving the view, the box's right edge still drags`, { b0, b2 });
    await page.evaluate(() => document.getElementById('fixCancel').click()); await page.waitForTimeout(150);
  }

  // ---- C. Fix the cut in the line strips (plain.html: one line crop per page, no neighbour)
  await load('plain.html');
  { const sid = 'p1_06'; await openByHold(page, sid); await recentre(page);
    const it = await page.evaluate(s => ({ b: itemBySid[s].b.slice(), p: itemBySid[s].p }), sid);
    await page.click('#ctxFix');   // a real press (after a hold the page swallows the lift's click until the next press)
    await page.waitForTimeout(250);
    const hint = await page.evaluate(() => document.getElementById('ctxPanHint').textContent);
    ok(/fix the cut/.test(hint) && /look around/.test(hint), `${dev}: fixing a cut, the hint says the box edits and the rest of the page moves`, hint);
    const k0 = await page.evaluate(() => { const m = document.getElementById('ctxC')._map; return m.k / m.s / m.ps; });   // image px of the strip per screen px
    const re = await boxAt(page, 1, 0.5); await drag(page, re.x, re.y, 30, 0); const b1 = await page.evaluate(() => fix.box.slice());
    ok(Math.abs((b1[2] - it.b[2]) - 30 * k0) <= 2 && b1[0] === it.b[0] && b1[1] === it.b[1] && b1[3] === it.b[3], `${dev}, line strip: a drag on the box's right edge moves that edge (as before)`, { b0: it.b, b1, expect: +(30 * k0).toFixed(1) });
    const a = await P(page), r = await page.locator('#ctxC').boundingBox(), e = await boxAt(page, 0.5, 0.5);
    const off = e.x > r.x + r.width / 2 ? r.x + 12 : r.x + r.width - 12;
    if (a.pannable) { await drag(page, off, e.y, off < e.x ? 60 : -60, 0); const c = await P(page), b2 = await page.evaluate(() => fix.box.slice());
      ok(b2.join() === b1.join() && Math.abs(c.vx - a.vx) > 1, `${dev}, line strip: fixing a cut, a drag off the box moves the view and leaves the box as it was (strip pixels)`, { box: b2, vx: [a.vx, c.vx].map(v => +v.toFixed(1)) }); }
    else skip(`${dev}, line strip: the fix-the-cut window shows the whole crop here, nothing to move`);
    const re2 = await boxAt(page, 1, 0.5); await drag(page, re2.x, re2.y, 16, 0); const b3 = await page.evaluate(() => fix.box.slice());
    ok(b3[2] > b1[2] + 3, `${dev}, line strip: the right edge drags again from where it now is`, { b1, b3 });
    // 6. Erase stray ink: one finger paints, two fingers move the view
    await page.evaluate(() => document.getElementById('fixBrush').click()); await page.waitForTimeout(100);
    { const n0 = await page.evaluate(() => fix.mask.length), a1 = await P(page), c = await boxAt(page, 0.5, 0.5);
      await drag(page, c.x - 4, c.y - 4, 8, 8, 4); const n1 = await page.evaluate(() => fix.mask.length), a2 = await P(page);
      ok(n1 === n0 + 1 && a2.vx === a1.vx && a2.vy === a1.vy, `${dev}, Erase stray ink: one ${touch ? 'finger' : 'mouse drag'} paints a stroke and does not move the view`, { strokes: [n0, n1] });
      if (touch) { const r2 = await page.locator('#ctxC').boundingBox(), y = r2.y + r2.height / 2, x = e.x > r2.x + r2.width / 2 ? r2.x + r2.width * 0.3 : r2.x + r2.width * 0.7;
        const sx = x > r2.x + r2.width / 2 ? -60 : 60;
        await twoDrag(page, [x - 15, y - 10], [x + 15, y + 10], [sx, 0], [sx, 0]); const n2 = await page.evaluate(() => fix.mask.length), a3 = await P(page);
        if (a2.pannable) ok(n2 === n1 && Math.abs(a3.vx - a2.vx) > 1, `${dev}, Erase stray ink: two fingers move the view and paint nothing`, { strokes: [n1, n2], vx: [a2.vx, a3.vx].map(v => +v.toFixed(1)) });
        else ok(n2 === n1, `${dev}, Erase stray ink: two fingers paint nothing (nothing to move here)`, { strokes: [n1, n2] }); }
      else skip(`${dev}: two-finger slide is a touch gesture`);
      await page.evaluate(() => { document.getElementById('fixBrushUndo').click(); document.getElementById('fixBrush').click(); }); await page.waitForTimeout(100); }
    // Save: the recut doc in the same shape as before
    const q = await page.evaluate(() => fix.quad.map(p => p.slice())); await page.evaluate(() => document.getElementById('fixSave').click()); await page.waitForTimeout(1200);
    const doc = (store.docs.recuts || {})[sid] || null; const xs = q.map(p => p[0]), ys = q.map(p => p[1]);
    const shape = doc && ['sid', 'page', 'x', 'y', 'w', 'h', 'old', 'at', 'quad', 'mask'].every(k => k in doc) && Object.keys(doc).length === 10;
    ok(shape && doc.x === Math.min(...xs) && doc.y === Math.min(...ys) && doc.w === Math.max(...xs) - doc.x && doc.h === Math.max(...ys) - doc.y && doc.old.join() === it.b.join()
      && doc.page === it.p && JSON.stringify(doc.quad) === JSON.stringify(q) && doc.w === b3[2], `${dev}, line strip: Save writes the recut doc in the same shape as before (strip pixels, the box as dragged)`, doc);
  }
  await ctx.close();
}

async function probe(b, PAGE) {   // tools/sorter_preflight.py check 'pan' (owner rule R09) on a built page
  const ctx = await b.newContext(prof('iPhone 13')); await mock.install(ctx); const page = await ctx.newPage(); page.on('pageerror', e => errs.push(e.message));
  await page.goto('file://' + path.resolve(PAGE)); await page.waitForFunction(() => typeof ready !== 'undefined' && ready, null, { timeout: 60000 }).catch(() => {}); await page.waitForTimeout(500);
  const sids = await page.evaluate(() => { const all = Object.keys(itemBySid), withNb = all.filter(s => nbPages(itemBySid[s].p).every(Boolean)); const pool = withNb.length ? withNb : all;
    const k = Math.max(1, Math.floor(pool.length / 25)); return pool.filter((_, i) => i % k === Math.floor(k / 2)).slice(0, 25); });
  // a tile whose window has room for both drags (tiles with a line above and below first; the opening zoom, then 6 and 8); failing
  // that, one with room sideways only -- a page whose every line is shown to its top and bottom has nothing above or below to move to
  let pick = null, side = null;
  for (const z of [null, 6, 8]) { for (const sid of sids) { await page.evaluate(s => showCtx(s, pileOf(s)), sid); await waitCard(page, sid); if (z) await setZoom(page, z);
      const p = await P(page), r = room(p), hx = r.r >= 1.2 * 80 / p.sc, vy = r.u >= 1.2 * 60 / p.sc;
      if (hx && vy) { pick = { sid, both: true }; break; } if (hx && !side) side = { sid, z: p.z }; }
    if (pick) break; }
  if (!pick && side) { await page.evaluate(s => showCtx(s, pileOf(s)), side.sid); await waitCard(page, side.sid); await setZoom(page, side.z); pick = { sid: side.sid, both: false }; }
  if (!pick) { ok(false, 'pan: a card whose picture can move 80 px left (none of ' + sids.length + ' tiles tried, at the opening zoom, 6 and 8)'); await ctx.close(); return; }
  const { sid, both } = pick, s0 = await S(page), at = await picAt(page); const a2 = await P(page);
  await drag(page, at.x, at.y, -80, 60); const c = await P(page), s1 = await S(page);
  const ex = 80 / a2.sc, ey = both ? -60 / a2.sc : 0;
  ok(near(c.vx - a2.vx, ex, 0.1) && (both ? near(c.vy - a2.vy, ey, 0.1) : a2.vy - c.vy >= -0.5 && a2.vy - c.vy <= 60 / a2.sc + 0.5) && c.sid === sid && c.open && same(s0, s1),
    `pan: iPhone 13, a drag 80 px left and 60 px down on the picture of ${sid}'s card (${a2.view} view, zoom ${a2.z}) moves the view with the finger` +
    (both ? '' : ' (sideways only: every line here is shown to its top and bottom, nothing above or below to move to)') + '; the sign and the answers unchanged',
    { moved: [+(c.vx - a2.vx).toFixed(1), +(c.vy - a2.vy).toFixed(1)], expected: [+ex.toFixed(1), +ey.toFixed(1)], sign: c.sid });
  await recentre(page); await page.waitForTimeout(200); const d = await P(page);
  ok(!d.moved && Math.abs(d.vx - d.x0) < 0.5 && Math.abs(d.vy - d.y0) < 0.5, 'pan: "Back to the sign" puts the view back', { at: [d.vx, d.vy], opened: [d.x0, d.y0] });
  await ctx.close();
}

(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_EXE || '/opt/pw-browsers/chromium', args: ['--allow-file-access-from-files'] });
  if (process.argv[2] === '--probe') { try { await probe(b, process.argv[3]); } catch (e) { ok(false, 'pan: the probe finished without an exception', e.message.split('\n')[0]); } }
  else { const F = path.resolve(process.argv[2]), SHOTS = process.argv[3];
    for (const [dev, opts] of [['iPhone 13', prof('iPhone 13')], ['iPhone SE', prof('iPhone SE')], ['desktop', { viewport: { width: 1280, height: 900 } }]]) {
      try { await run(b, dev, opts, F, SHOTS); } catch (e) { ok(false, dev + ': the run finished without an exception', e.message.split('\n')[0]); } } }
  ok(!errs.length, 'no page errors', errs.join(' | '));
  if (failed.length) { console.log('failed checks (repeated here so a log tail shows them):'); failed.forEach(m => console.log('  - ' + m)); }
  console.log('errors:', errs); console.log(fails ? fails + ' FAILED' : 'ALL PASS');
  await b.close(); process.exit(fails ? 1 : 0);
})();
