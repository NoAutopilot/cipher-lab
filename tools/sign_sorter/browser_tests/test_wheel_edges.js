// Template 2026-10-09.7, the edges of owner rules R09 / R10 / R11 found by the two adversarial checks of 11 Oct 2026 (desktop on Matignon
// f.110, phones on Bergh). Each row failed on the first 09.7 build and passes after its fix:
//   1. desktop, "Line strips" with no line above or below (a single line crop, so the window is the crop's whole height and the picture
//      itself grows with each step): Ctrl + wheel keeps the ink under the pointer on the screen (within 2 css px), by scrolling the card
//   2. desktop: Ctrl + wheel with the mouse button held on the picture (the owner's own words: "ctrl+click + mouse scroll") zooms one
//      step, and the drag of the view carries on after it
//   3. desktop: a mouse press whose release never reached the page (a Mac's Ctrl + click opens the context menu): moving the bare mouse
//      does not move the view, and Ctrl + wheel still zooms
//   4. desktop, Fix the cut: after a click on an arrow (nudge) button, Enter saves the cut (owner, 6 Oct 2026) instead of nudging again
//   5. desktop: Alt + Left (the browser's Back) and Ctrl + Right do not step the card; a bare arrow still does
//   6. desktop: Ctrl + wheel over the enlarged sign zooms the picture, not the browser page (the wheel event cancelled)
//   7. iPhone 13 (touch): iOS sends gesturestart / gesturechange beside the two fingers' pointers for one pinch; the zoom follows the
//      pointers alone (no flicker back, the same end as the pinch without gesture events); a Mac trackpad's gesture events (no finger
//      down) still zoom
//   8. iPhone SE (320 px): Fix the cut's panel fits the card (no sideways scroll inside the card)
//   9. zero page errors.
// Must NOT block: a plain wheel still scrolls and is not cancelled (test_wheel.js 6), a Tab-focused button still answers Enter itself.
// Usage: PW_EXE=/opt/pw-browsers/chromium NODE_PATH=$(npm root -g) node test_wheel_edges.js FIXTURE_DIR      (exit 1 on any FAIL)
const { chromium, devices } = require('playwright'); const mock = require('./mock_db'); const path = require('path');
let fails = 0; const errs = [];
const ok = (cond, msg, extra) => { console.log((cond ? 'ok   ' : 'FAIL ') + msg + (extra !== undefined ? '  [' + (typeof extra === 'string' ? extra : JSON.stringify(extra)) + ']' : '')); if (!cond) fails++; };
const prof = d => { const o = { ...devices[d] }; delete o.defaultBrowserType; return o; };
const C = page => page.evaluate(() => ({ sid: ctxSid, z: +document.getElementById('ctxZ').value, pan: [ctxPan.x, ctxPan.y].map(v => Math.round(v * 10) / 10), fix: !!fix,
  quad: fix ? JSON.stringify(fix.quad) : null, recuts: JSON.stringify(recuts), view: document.getElementById('ctxC').dataset.view }));
const under = (page, x, y) => page.evaluate(([x, y]) => { const c = document.getElementById('ctxC'), m = c._map, r = c.getBoundingClientRect();
  return [m.x0 + (x - r.left) * m.k / m.s, m.y0 + ((y - r.top) * m.k - m.ha) / m.s, m.k / m.s]; }, [x, y]);
const setZoom = async (page, z) => { await page.evaluate(z => { const e = document.getElementById('ctxZ'); e.value = z; e.dispatchEvent(new Event('input')); }, z); await page.waitForTimeout(150); };
const load = async (page, file) => { await page.goto('file://' + file); await page.waitForFunction(() => typeof ready !== 'undefined' && ready, null, { timeout: 30000 }); await page.waitForTimeout(300); };
const open = async (page, sid) => { await page.evaluate(s => showCtx(s, pileOf(s)), sid); await page.waitForTimeout(300);
  await page.evaluate(() => document.getElementById('ctxC').scrollIntoView({ block: 'center' })); await page.waitForTimeout(150); };
const pt = (page, fx, fy) => page.evaluate(([fx, fy]) => { const r = document.getElementById('ctxC').getBoundingClientRect(); return { x: r.left + r.width * fx, y: Math.min(innerHeight - 20, r.top + r.height * fy) }; }, [fx, fy]);
const ctrlWheel = async (page, dy) => { await page.keyboard.down('Control'); await page.mouse.wheel(0, dy); await page.keyboard.up('Control'); await page.waitForTimeout(200); };

async function desktop(b, F) {
  const ctx = await b.newContext({ viewport: { width: 1280, height: 800 } }); await mock.install(ctx); const page = await ctx.newPage(); page.on('pageerror', e => errs.push(e.message));
  await load(page, path.join(F, 'plain.html'));
  const L = await page.evaluate(() => Object.keys(itemBySid)); const sid = L[Math.floor(L.length / 2)];
  // 1. strip view with no neighbour line: the ink under the pointer stays put on the screen
  await open(page, sid); await setZoom(page, 5);
  await page.evaluate(() => document.getElementById('ctxC').scrollIntoView({ block: 'start' })); await page.waitForTimeout(150);
  { const p = await pt(page, 0.25, 0.5), u0 = await under(page, p.x, p.y); await page.mouse.move(p.x, p.y); await ctrlWheel(page, -100);
    const a = await C(page), u1 = await under(page, p.x, p.y), off = Math.hypot(u1[0] - u0[0], u1[1] - u0[1]) / u1[2];
    ok(a.z === 6 && off <= 2, 'strips, no line above or below: Ctrl + wheel keeps the ink under the pointer on the screen (zoom 5 -> 6)', { z: a.z, offCss: +off.toFixed(1), view: a.view });
    await ctrlWheel(page, -100); const u2 = await under(page, p.x, p.y), off2 = Math.hypot(u2[0] - u0[0], u2[1] - u0[1]) / u2[2];
    ok(off2 <= 2.5, '...and again (6 -> 7)', { offCss: +off2.toFixed(1) }); }
  // 2. button held + Ctrl + wheel (from zoom 5, where the line is wider than the window, so the drag has room to move it)
  await open(page, sid); await setZoom(page, 5);
  { const p = await pt(page, 0.3, 0.5); const a = await C(page); await page.mouse.move(p.x, p.y); await page.mouse.down(); await page.mouse.move(p.x - 10, p.y, { steps: 3 });
    await ctrlWheel(page, -100); const b1 = await C(page); await page.mouse.move(p.x + 50, p.y, { steps: 5 }); await page.waitForTimeout(100); const b2 = await C(page); await page.mouse.up(); await page.waitForTimeout(100);
    ok(b1.z === a.z + 1 && b2.pan[0] < b1.pan[0] - 1 && b2.sid === a.sid && b2.recuts === a.recuts, 'mouse button held on the picture + Ctrl + wheel: zooms one step, and the drag carries on moving the view', { z: [a.z, b1.z], panX: [b1.pan[0], b2.pan[0]] }); }
  // 3. a lost release
  await open(page, sid); await setZoom(page, 3);
  { const p = await pt(page, 0.5, 0.5); await page.mouse.move(p.x, p.y);
    await page.evaluate(([x, y]) => document.getElementById('ctxC').dispatchEvent(new PointerEvent('pointerdown', { pointerId: 1, pointerType: 'mouse', isPrimary: true, button: 0, buttons: 1, ctrlKey: true, clientX: x, clientY: y, bubbles: true, cancelable: true })), [p.x, p.y]);
    const a = await C(page); for (let k = 1; k <= 8; k++) { await page.mouse.move(p.x - 20 * k, p.y); await page.waitForTimeout(20); } await page.waitForTimeout(100); const b1 = await C(page);
    await ctrlWheel(page, -100); const b2 = await C(page);
    ok(b1.pan[0] === a.pan[0] && b2.z === a.z + 1, 'a mouse press whose release was lost (a Mac Ctrl + click): the bare mouse does not move the view, Ctrl + wheel still zooms', { pan: [a.pan[0], b1.pan[0]], z: [a.z, b2.z] });
    const cm = await page.evaluate(() => { const e = new MouseEvent('contextmenu', { bubbles: true, cancelable: true }); document.getElementById('ctxC').dispatchEvent(e); return e.defaultPrevented; });
    ok(cm, 'no context menu over the picture (it would swallow the release)'); }
  // 4. Enter after a nudge click saves
  await open(page, sid);
  { await page.locator('#ctxFix').click(); await page.waitForTimeout(200); const q0 = (await C(page)).quad; await page.locator('#fixLm').click(); await page.waitForTimeout(100);
    const q1 = (await C(page)).quad; await page.keyboard.press('Enter'); await page.waitForTimeout(300); const a = await C(page);
    ok(q1 !== q0 && !a.fix && a.recuts !== '{}' && JSON.parse(a.recuts)[sid], 'Fix the cut: a click on an arrow button, then Enter, saves the cut (does not nudge again)', { fixing: a.fix }); }
  // must not block: a Tab-focused nudge button still answers Enter itself
  await open(page, sid);
  { await page.locator('#ctxFix').click(); await page.waitForTimeout(200); await page.evaluate(() => document.getElementById('fixLp').focus()); const q0 = (await C(page)).quad;
    await page.keyboard.press('Enter'); await page.waitForTimeout(150); const a = await C(page);
    ok(a.fix && a.quad !== q0, 'Fix the cut: a nudge button reached by keyboard focus still answers Enter itself (keyboard use kept)');
    await page.evaluate(() => document.getElementById('fixCancel').click()); await page.waitForTimeout(150); }
  // 5. modified arrows
  await page.evaluate(() => closeCtx()); await page.locator('#list .pile button.big').nth(0).click().catch(() => {}); await page.waitForTimeout(250);
  if (await page.evaluate(() => document.getElementById('ctx').hidden)) await open(page, sid);
  { await page.keyboard.press('ArrowRight'); await page.waitForTimeout(100); const a = await C(page);
    await page.keyboard.press('Alt+ArrowLeft'); await page.waitForTimeout(100); const b1 = await C(page);
    await page.keyboard.press('Control+ArrowRight'); await page.waitForTimeout(100); const b2 = await C(page);
    await page.keyboard.press('Meta+ArrowRight'); await page.waitForTimeout(100); const b3 = await C(page);
    await page.keyboard.press('ArrowLeft'); await page.waitForTimeout(100); const b4 = await C(page);
    ok(b1.sid === a.sid && b2.sid === a.sid && b3.sid === a.sid, 'Alt + Left (browser Back), Ctrl + Right and Cmd + Right do not step the card', [a.sid, b1.sid, b2.sid, b3.sid]);
    ok(b4.sid !== a.sid, 'a bare Left arrow still steps the card (must not block)', [a.sid, b4.sid]); }
  // 6. Ctrl + wheel over the enlarged sign
  await open(page, sid); await setZoom(page, 3);
  { await page.evaluate(() => { window.__w = []; window.addEventListener('wheel', e => window.__w.push(e.defaultPrevented), { passive: false }); });
    const bb = await page.locator('#ctxBigW').boundingBox(); await page.mouse.move(bb.x + bb.width / 2, bb.y + bb.height / 2); const a = await C(page); await ctrlWheel(page, -100);
    const b1 = await C(page), w = await page.evaluate(() => window.__w.slice(-1)[0]), sc = await page.evaluate(() => visualViewport.scale);
    ok(w === true && b1.z === a.z + 1 && sc === 1, 'Ctrl + wheel over the enlarged sign zooms the picture one step, the browser page does not zoom', { prevented: w, z: [a.z, b1.z] }); }
  await ctx.close();
}

async function touch(page, type, pts) { const cdp = page.__cdp || (page.__cdp = await page.context().newCDPSession(page)); await cdp.send('Input.dispatchTouchEvent', { type, touchPoints: pts.map((p, i) => ({ x: p[0], y: p[1], id: i + 1 })) }); }
const gesture = (page, type, scale) => page.evaluate(([t, s]) => { const ev = new Event(t, { cancelable: true }); ev.scale = s; document.getElementById('ctxC').dispatchEvent(ev); }, [type, scale]);
async function phones(b, F) {
  // 7. iPhone 13: a pinch with iOS's gesture events beside the pointers
  { const ctx = await b.newContext(prof('iPhone 13')); await mock.install(ctx); const page = await ctx.newPage(); page.on('pageerror', e => errs.push(e.message));
    await load(page, path.join(F, 'lines.html')); await open(page, 't_L03_16');
    const at = await pt(page, 0.5, 0.5), d0 = 40;
    const pinch = async withGesture => { await setZoom(page, 3); await page.evaluate(() => document.getElementById('ctxC').scrollIntoView({ block: 'center' })); await page.waitForTimeout(150);
      const c = await pt(page, 0.5, 0.5), zs = [];
      await touch(page, 'touchStart', [[c.x - d0 / 2, c.y], [c.x + d0 / 2, c.y]]); if (withGesture) await gesture(page, 'gesturestart', 1);
      for (let i = 1; i <= 16; i++) { const d = d0 * Math.pow(2, i / 16); await touch(page, 'touchMove', [[c.x - d / 2, c.y], [c.x + d / 2, c.y]]);
        if (withGesture) await gesture(page, 'gesturechange', d / d0); await page.waitForTimeout(20); zs.push((await C(page)).z); }
      await touch(page, 'touchEnd', []); if (withGesture) await gesture(page, 'gestureend', 2); await page.waitForTimeout(300); return { zs, z: (await C(page)).z }; };
    const p0 = await pinch(false), p1 = await pinch(true), flips = p1.zs.filter((z, i) => i && z < p1.zs[i - 1]).length;
    ok(p1.z === p0.z && flips === 0, 'iPhone 13: a pinch with iOS gesture events beside the pointers zooms as the pinch alone does (no double step, no flicker back)', { pinchOnly: p0.zs, withGesture: p1.zs });
    await page.waitForTimeout(500); await setZoom(page, 3);
    await gesture(page, 'gesturestart', 1); for (const s of [1.2, 1.5]) await gesture(page, 'gesturechange', s); await gesture(page, 'gestureend', 1.5); await page.waitForTimeout(200);
    ok((await C(page)).z === 4, 'a trackpad pinch on a Mac (gesture events, no finger on the screen) still zooms one step (must not block)', (await C(page)).z);
    await ctx.close(); }
  // 8. iPhone SE: Fix the cut fits
  { const ctx = await b.newContext(prof('iPhone SE')); await mock.install(ctx); const page = await ctx.newPage(); page.on('pageerror', e => errs.push(e.message));
    await load(page, path.join(F, 'lines.html')); await open(page, 't_L03_16'); await page.evaluate(() => document.getElementById('ctxFix').click()); await page.waitForTimeout(300);
    const r = await page.evaluate(() => { const bx = document.querySelector('#ctx .box'), br = bx.getBoundingClientRect(), out = [];
      bx.querySelectorAll('#fixBox *').forEach(e => { const q = e.getBoundingClientRect(); if (q.width && e.offsetParent !== null && q.right > br.right + 0.5) out.push(e.id || e.tagName); });
      return { sw: bx.scrollWidth, cw: bx.clientWidth, out: out.slice(0, 8), docW: document.documentElement.scrollWidth, vw: innerWidth }; });
    ok(r.sw <= r.cw + 1 && !r.out.length && r.docW <= r.vw, 'iPhone SE: Fix the cut\'s panel fits the card (no sideways scroll inside it; #fixCd on screen)', r);
    await ctx.close(); }
}

(async () => {
  const F = process.argv[2] && path.resolve(process.argv[2]); if (!F) { console.error('usage: node test_wheel_edges.js FIXTURE_DIR'); process.exit(2); }
  const b = await chromium.launch({ executablePath: process.env.PW_EXE || undefined, args: ['--allow-file-access-from-files'] });
  await desktop(b, F); await phones(b, F);
  ok(errs.length === 0, 'zero page errors', errs.slice(0, 3));
  console.log('errors: ' + (errs.length ? "[ '" + errs.join("', '") + "' ]" : '[]'));
  await b.close(); console.log(fails ? fails + ' FAIL' : 'all ok'); process.exit(fails ? 1 : 0);
})();
