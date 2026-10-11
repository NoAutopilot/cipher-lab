// Owner rule R10 (tools/data/sorter_owner_requirements.tsv; 11 Oct 2026, desktop: "Allow me to ctrl+click + mouse scroll to zoom in and out
// so I can see more around the symbol in questions"): in a sign's card, Ctrl + mouse wheel over the picture zooms the picture around the
// pointer, one step of the Zoom slider per notch (same range 1-8, the slider moves with it), and the browser's own page zoom does not
// happen; a trackpad pinch (a run of small wheel events with ctrlKey, as Chromium sends it) zooms the same way; a plain wheel is not
// cancelled and still scrolls the card; all of it also while a cut is being fixed (the box is not changed).
// Checks, desktop mouse (Chromium, 1100 x 620 so the card scrolls), on lines.html (line strips with lines above and below), region.html
// ("Whole page") and plain.html (single line crops):
//   1. Ctrl + wheel up one notch: Zoom slider +1, the wheel event cancelled (defaultPrevented: no page zoom), visualViewport.scale 1,
//      devicePixelRatio unchanged, the same sign, nothing moved; the window is smaller (zoomed in), unless the whole sheet is in it already
//      (a short single line crop at zoom 3-4: the slider alone draws the same window there too, check 4)
//   2. the point under the pointer stays under it (within 2 css px), a pointer off-centre (a quarter of the picture's width), on every
//      axis where the window is not held at the sheet's edge (both held: said, not failed); again from zoom 5 to 6
//   3. Ctrl + wheel down: Zoom slider -1; at 8 and at 1 a further notch keeps the slider in range (and is still cancelled)
//   4. the slider in step: after the wheel, the window equals the window the slider alone draws at that zoom, centred (vw the same)
//   5. a trackpad pinch: eight wheel events of deltaY -12 with ctrlKey raise the slider by 1 or 2 (never 0, never more than 2)
//   6. a plain wheel over the picture: not cancelled, slider unchanged, and the card scrolls (when it can)
//   7. Fix the cut: Ctrl + wheel changes the zoom, the editor stays on, the box (strip pixels) is unchanged, the point under the pointer
//      stays under it; zero page errors.
// Usage: PW_EXE=/opt/pw-browsers/chromium NODE_PATH=$(npm root -g) node test_wheel.js FIXTURE_DIR      (exit 1 on any FAIL)
const { chromium } = require('playwright'); const mock = require('./mock_db'); const path = require('path');
let fails = 0; const errs = [];
const ok = (cond, msg, extra) => { console.log((cond ? 'ok   ' : 'FAIL ') + msg + (extra !== undefined ? '  [' + (typeof extra === 'string' ? extra : JSON.stringify(extra)) + ']' : '')); if (!cond) fails++; };
const P = page => page.evaluate(() => { const c = document.getElementById('ctxC'), v = c._pan || {}, bx = document.querySelector('#ctx .box');
  return { sid: ctxSid, open: !document.getElementById('ctx').hidden, z: +document.getElementById('ctxZ').value, vx: v.vx, vy: v.vy, vw: v.vw, vh: v.vh,
    wx0: v.wx0, wx1: v.wx1, wy0: v.wy0, wy1: v.wy1, scale: window.visualViewport ? visualViewport.scale : 1, dpr: devicePixelRatio,
    scroll: bx.scrollTop, canScroll: bx.scrollHeight > bx.clientHeight + 4, fix: !!fix, box: fix ? JSON.stringify(fix.box) : null,
    moves: JSON.stringify(moves), recuts: JSON.stringify(recuts) }; });
// the linear picture coordinate under a screen point (the card's own map: page pixels in the strips, region pixels on the page)
const under = (page, x, y) => page.evaluate(([x, y]) => { const c = document.getElementById('ctxC'), m = c._map, r = c.getBoundingClientRect();
  return [m.x0 + (x - r.left) * m.k / m.s, m.y0 + ((y - r.top) * m.k - m.ha) / m.s, m.k / m.s]; }, [x, y]);
// per axis: a window held at the sheet's edge on that axis cannot keep the point there (said, not failed); the other axis is still checked
const edgeX = p => p.vx <= p.wx0 + 0.5 || p.vx + p.vw >= p.wx1 - 0.5, edgeY = p => p.vy <= p.wy0 + 0.5 || p.vy + p.vh >= p.wy1 - 0.5;
const edge = p => edgeX(p) && edgeY(p);
const offOf = (p, u0, u1) => Math.hypot(edgeX(p) ? 0 : u1[0] - u0[0], edgeY(p) ? 0 : u1[1] - u0[1]) / u1[2];   // css px, free axes only
async function at(page, fx, fy) {
  await page.evaluate(() => { const c = document.getElementById('ctxC'); const r = c.getBoundingClientRect(); if (r.top < 0 || r.bottom > innerHeight) c.scrollIntoView({ block: 'center' }); });
  await page.waitForTimeout(100);
  return page.evaluate(([fx, fy]) => { const r = document.getElementById('ctxC').getBoundingClientRect(); return { x: r.left + r.width * fx, y: r.top + r.height * fy }; }, [fx, fy]);
}
async function wheel(page, x, y, dy, ctrl) {
  await page.mouse.move(x, y); if (ctrl) await page.keyboard.down('Control');
  await page.mouse.wheel(0, dy); if (ctrl) await page.keyboard.up('Control'); await page.waitForTimeout(150);
}
const lastWheel = page => page.evaluate(() => window.__w.slice(-1)[0] || {});
const setZoom = async (page, z) => { await page.evaluate(z => { const e = document.getElementById('ctxZ'); e.value = z; e.dispatchEvent(new Event('input')); }, z); await page.waitForTimeout(150); };

async function view(page, file, sid, where) {
  await page.goto('file://' + file); await page.waitForFunction(() => typeof ready !== 'undefined' && ready, null, { timeout: 30000 }).catch(() => {});
  await page.evaluate(() => { window.__w = []; window.addEventListener('wheel', e => window.__w.push({ ctrl: e.ctrlKey, prevented: e.defaultPrevented }), { passive: false }); });
  await page.evaluate(s => showCtx(s, pileOf(s)), sid);
  await page.waitForFunction(s => { const c = document.getElementById('ctxC'); return ctxSid === s && c.dataset.sid === s && c._pan; }, sid, { timeout: 5000 }).catch(() => {});
  await page.waitForTimeout(250);
  await setZoom(page, 3);
  // 1-2. one notch up, the pointer a quarter of the way across
  { const a = await P(page), pt = await at(page, 0.27, 0.5), u0 = await under(page, pt.x, pt.y);
    await wheel(page, pt.x, pt.y, -100, true); const b = await P(page), w = await lastWheel(page), u1 = await under(page, pt.x, pt.y);
    ok(b.z === a.z + 1 && w.ctrl && w.prevented && b.scale === 1 && b.dpr === a.dpr && b.sid === a.sid && b.moves === a.moves && (b.vw * b.vh < a.vw * a.vh - 1 || (b.vw >= b.wx1 - b.wx0 - 0.5 && b.vh >= Math.min(a.vh, b.wy1 - b.wy0) - 0.5)),
      `${where}: Ctrl + wheel up zooms the picture in one step (slider ${a.z} -> ${b.z}), the browser page does not zoom, the same sign, nothing moved`,
      { prevented: w.prevented, scale: b.scale, window: [[a.vw, a.vh], [b.vw, b.vh]].map(q => q.map(v => +(+v).toFixed(1))) });
    const off = offOf(b, u0, u1);
    if (edge(b)) console.log(`note ${where}: the window is held at the sheet's edge after the zoom; the point under the pointer moved ${off.toFixed(1)} css px`);
    else ok(off <= 2, `${where}: the point under the pointer stays under it while zooming in`, { offCss: +off.toFixed(2) });
    // 3. back down, and the ends of the range
    const pt2 = await at(page, 0.7, 0.4), v0 = await under(page, pt2.x, pt2.y);
    await wheel(page, pt2.x, pt2.y, 100, true); const c = await P(page), v1 = await under(page, pt2.x, pt2.y), off2 = offOf(c, v0, v1);
    ok(c.z === b.z - 1 && (await lastWheel(page)).prevented, `${where}: Ctrl + wheel down zooms out one step (slider ${b.z} -> ${c.z})`);
    if (!edge(c)) ok(off2 <= 2, `${where}: the point under the pointer stays under it while zooming out`, { offCss: +off2.toFixed(2) });
    await setZoom(page, 8); const p8 = await at(page, 0.5, 0.5); await wheel(page, p8.x, p8.y, -100, true); const d8 = await P(page), w8 = await lastWheel(page);
    await setZoom(page, 1); const p1 = await at(page, 0.5, 0.5); await wheel(page, p1.x, p1.y, 100, true); const d1 = await P(page), w1 = await lastWheel(page);
    ok(d8.z === 8 && d1.z === 1 && w8.prevented && w1.prevented && d1.scale === 1, `${where}: at the ends of the range (8, 1) a further notch keeps the slider in range and still does not zoom the page`, { at8: d8.z, at1: d1.z }); }
  // 2b. closer in (zoom 5 -> 6), where a short sheet no longer fits the window: the point under the pointer stays under it
  { await setZoom(page, 5); const pt = await at(page, 0.3, 0.45), u0 = await under(page, pt.x, pt.y); await wheel(page, pt.x, pt.y, -100, true);
    const b = await P(page), u1 = await under(page, pt.x, pt.y), off = offOf(b, u0, u1);
    if (edge(b)) console.log(`note ${where}: zoom 5 -> 6 is held at the sheet's edge; the point moved ${off.toFixed(1)} css px`);
    else ok(b.z === 6 && off <= 2, `${where}: zoom 5 -> 6, the point under the pointer stays under it`, { offCss: +off.toFixed(2) }); }
  // 4. in step with the slider
  { await setZoom(page, 3); const pt = await at(page, 0.5, 0.5); await wheel(page, pt.x, pt.y, -100, true); const a = await P(page);
    await setZoom(page, a.z); const b = await P(page);
    ok(a.z === 4 && Math.abs(a.vw - b.vw) < 0.5 && Math.abs(a.vh - b.vh) < 0.5, `${where}: the wheel's zoom is the slider's zoom (the same window size as the slider at ${a.z})`, { wheel: [a.vw, a.vh].map(v => +(+v).toFixed(1)), slider: [b.vw, b.vh].map(v => +(+v).toFixed(1)) }); }
  // 5. a trackpad pinch: small wheel deltas with ctrlKey
  { await setZoom(page, 3); const pt = await at(page, 0.5, 0.5); await page.mouse.move(pt.x, pt.y); await page.keyboard.down('Control');
    for (let i = 0; i < 8; i++) { await page.mouse.wheel(0, -12); await page.waitForTimeout(20); }
    await page.keyboard.up('Control'); await page.waitForTimeout(150); const a = await P(page), ws = await page.evaluate(() => window.__w.slice(-8));
    ok(a.z >= 4 && a.z <= 5 && ws.every(w => w.ctrl && w.prevented) && a.scale === 1, `${where}: a trackpad pinch (eight small Ctrl wheel events) zooms in by one or two steps, the page does not zoom`, { z: a.z }); }
  // 6. a plain wheel scrolls
  { await setZoom(page, 3); await page.evaluate(() => { document.querySelector('#ctx .box').scrollTop = 0; }); const pt = await at(page, 0.5, 0.3);
    await page.evaluate(() => { document.querySelector('#ctx .box').scrollTop = 0; }); await page.waitForTimeout(100);
    const a = await P(page); await wheel(page, pt.x, pt.y, 200, false); await page.waitForTimeout(250); const b = await P(page), w = await lastWheel(page);
    ok(!w.ctrl && !w.prevented && b.z === a.z && (!a.canScroll || b.scroll > a.scroll), `${where}: a plain wheel over the picture is left to the browser (the card scrolls${a.canScroll ? '' : ': nothing to scroll here'}), no zoom`,
      { scroll: [a.scroll, b.scroll], z: b.z }); }
  // 7. while fixing a cut
  { await page.evaluate(() => { document.querySelector('#ctx .box').scrollTop = 0; }); await setZoom(page, 3);
    await page.evaluate(() => document.getElementById('ctxFix').click()); await page.waitForTimeout(250);
    const a = await P(page), pt = await at(page, 0.2, 0.3), u0 = await under(page, pt.x, pt.y);
    await wheel(page, pt.x, pt.y, 100, true); const b = await P(page), u1 = await under(page, pt.x, pt.y), w = await lastWheel(page);
    const off = offOf(b, u0, u1);
    ok(a.fix && b.fix && b.z === a.z - 1 && b.box === a.box && w.prevented && b.recuts === a.recuts, `${where}, Fix the cut: Ctrl + wheel zooms out (slider ${a.z} -> ${b.z}), the editor stays on and the box is unchanged`);
    if (!edge(b)) ok(off <= 2, `${where}, Fix the cut: the point under the pointer stays under it`, { offCss: +off.toFixed(2) });
    else console.log(`note ${where}, Fix the cut: the window is held at the sheet's edge; the point moved ${off.toFixed(1)} css px`);
    await page.evaluate(() => document.getElementById('fixCancel').click()); await page.waitForTimeout(150); }
}

(async () => {
  const F = process.argv[2] && path.resolve(process.argv[2]); if (!F) { console.error('usage: node test_wheel.js FIXTURE_DIR'); process.exit(2); }
  const b = await chromium.launch({ executablePath: process.env.PW_EXE || undefined });
  const ctx = await b.newContext({ viewport: { width: 1100, height: 620 } }); await mock.install(ctx); const page = await ctx.newPage();
  page.on('pageerror', e => errs.push(e.message));
  await view(page, path.join(F, 'lines.html'), 't_L03_16', 'line strips (lines.html)');
  await view(page, path.join(F, 'region.html'), await (async () => { await page.goto('file://' + path.join(F, 'region.html')); await page.waitForFunction(() => typeof ready !== 'undefined' && ready, null, { timeout: 30000 }).catch(() => {});
    return page.evaluate(() => { const s = Object.keys(itemBySid).filter(k => /^r_L02/.test(k)); return s[Math.floor(s.length / 2)]; }); })(), 'whole page (region.html)');
  await view(page, path.join(F, 'plain.html'), await (async () => { await page.goto('file://' + path.join(F, 'plain.html')); await page.waitForFunction(() => typeof ready !== 'undefined' && ready, null, { timeout: 30000 }).catch(() => {});
    return page.evaluate(() => { const s = Object.keys(itemBySid); return s[Math.floor(s.length / 2)]; }); })(), 'single crops (plain.html)');
  ok(errs.length === 0, 'zero page errors', errs.slice(0, 3));
  console.log('errors: ' + (errs.length ? "[ '" + errs.join("', '") + "' ]" : '[]'));
  await b.close(); console.log(fails ? fails + ' FAIL' : 'all ok'); process.exit(fails ? 1 : 0);
})();
