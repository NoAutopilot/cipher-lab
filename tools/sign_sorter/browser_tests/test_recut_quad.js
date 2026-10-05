// "Fix the cut" free corners and "Erase stray ink" (SORTER-QUAD, owner 5 Oct 2026: on a wide looped sign the sheared box could
// not cover the sign without clipping in a neighbour's ink). A corner handle drag moves that corner only; the corner arrows do
// the same 2 px a tap; the brush makes one mask stroke per pointerdown..pointerup and "Undo stroke" removes the last; "Save cut"
// writes db 'recuts' {sid, page, quad: [[x, y]] x 4, mask: [{r, pts}], x y w h (the quad's bounds), old, at}; the thumbnail is
// redrawn with the stroke as paper; the quad reloads from the db; an old {x, y, w, h} recut still loads, draws and re-opens.
// Phone: touch corner drag and a touch stroke, no scroll. Whole-page view: a corner drag moves one corner there too.
//   node test_recut_quad.js plain.html [OUT_PREFIX] [region.html]
const { chromium } = require('playwright'); const mock = require('./mock_db');
const quad = page => page.evaluate(() => fix ? fix.quad.map(p => p.slice()) : null);
async function pointAt(page, x, y) {   // screen point of strip pixel (x, y) on the larger view, strip or whole-page view
  return page.evaluate(([x, y]) => { const c = document.getElementById('ctxC'), m = c._map, r = c.getBoundingClientRect();
    const cy = c.dataset.view === 'page' ? (regY(itemBySid[fix.sid].p, x, y) - m.y0) * m.s : (y * m.ps - m.y0) * m.s + m.ha;
    return [r.left + ((x * m.ps - m.x0) * m.s) / m.k, r.top + cy / m.k]; }, [x, y]);
}
async function dragBy(page, [x, y], dx, dy) {
  await mock.gesture(page, 'down', x, y);
  for (let i = 1; i <= 8; i++) { await mock.gesture(page, 'move', x + dx * i / 8, y + dy * i / 8); await page.waitForTimeout(16); }
  await mock.gesture(page, 'up', x + dx, y + dy); await page.waitForTimeout(150);
}
const same = (a, b) => JSON.stringify(a) === JSON.stringify(b);
const moved = (q0, q1) => q0.map((p, i) => same(p, q1[i]) ? -1 : i).filter(i => i >= 0);
(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_EXE }); const res = []; const errs = [];
  const ok = (name, cond, extra) => { res.push([name, !!cond]); console.log((cond ? 'ok   ' : 'FAIL ') + name, extra === undefined ? '' : JSON.stringify(extra)); };
  // ---- desktop
  {
    const ctx = await b.newContext({ viewport: { width: 1200, height: 900 } }); const store = await mock.install(ctx); const page = await ctx.newPage();
    page.on('pageerror', e => errs.push(e.message)); await page.goto('file://' + process.argv[2]); await page.waitForTimeout(1200);
    const t = page.locator('#pile__88_ .tiles .t').nth(1); const sid = await t.getAttribute('data-sid');
    const b0 = await page.evaluate(s => itemBySid[s].b.slice(), sid); const src0 = await t.locator('img').getAttribute('src');
    await mock.hold(page, t); await page.click('#ctxFix'); await page.waitForTimeout(200);
    const q0 = await quad(page);
    ok('desktop: edit starts from the box as four corners', same(q0, [[b0[0], b0[1]], [b0[0] + b0[2], b0[1]], [b0[0] + b0[2], b0[1] + b0[3]], [b0[0], b0[1] + b0[3]]]), q0);
    await dragBy(page, await pointAt(page, ...q0[1]), 25, -15); const q1 = await quad(page);
    ok('desktop: dragging the top-right handle moves that corner only', same(moved(q0, q1), [1]) && q1[1][0] > q0[1][0] && q1[1][1] < q0[1][1], { q0, q1 });
    const bx = await page.evaluate(() => fix.box.slice());
    ok('desktop: box shown is the quad\'s bounds', bx[2] === q1[1][0] - q1[0][0] && bx[1] === q1[1][1], bx);
    ok('desktop: the corner arrows follow the dragged corner', (await page.inputValue('#fixCorner')) === '1');
    await page.selectOption('#fixCorner', '3'); await page.click('#fixCl'); await page.click('#fixCd'); const q2 = await quad(page);
    ok('desktop: corner arrows nudge one corner 2 px a tap', same(moved(q1, q2), [3]) && q2[3][0] === q1[3][0] - 2 && q2[3][1] === q1[3][1] + 2, { q1, q2 });
    await page.click('#fixRp'); const q3 = await quad(page);
    ok('desktop: the right-edge arrow still moves both right corners, shape kept', same(moved(q2, q3), [1, 2]) && q3[1][0] === q2[1][0] + 2 && q3[2][0] === q2[2][0] + 2, { q2, q3 });
    // brush: one stroke per pointerdown..pointerup; the box does not move while painting
    await page.click('#fixBrush'); ok('desktop: brush toggle on', (await page.getAttribute('#fixBrush', 'aria-pressed')) === 'true');
    await page.fill('#fixBrushR', '4'); await page.dispatchEvent('#fixBrushR', 'input');
    const mid = [(q3[0][0] + q3[2][0]) / 2, (q3[0][1] + q3[2][1]) / 2];
    await dragBy(page, await pointAt(page, mid[0] - 4, mid[1]), 40, 6);
    let mk = await page.evaluate(() => fix.mask.map(s => ({ r: s.r, n: s.pts.length })));
    ok('desktop: a brush stroke makes one mask stroke of the slider radius', mk.length === 1 && mk[0].r === 4 && mk[0].n >= 3, mk);
    ok('desktop: painting does not move the box', same(await quad(page), q3));
    await dragBy(page, await pointAt(page, mid[0], mid[1] - 5), 0, 30);
    ok('desktop: a second stroke is a second mask stroke', (await page.evaluate(() => fix.mask.length)) === 2 && !(await page.isDisabled('#fixBrushUndo')));
    const prev = await page.getAttribute('#ctxBig', 'src');
    await page.click('#fixBrushUndo'); await page.waitForTimeout(250);
    ok('desktop: Undo stroke removes the last stroke only', same(await page.evaluate(() => fix.mask.map(s => ({ r: s.r, n: s.pts.length }))), mk));
    ok('desktop: the enlarged tile previews the cut', (await page.getAttribute('#ctxBig', 'src')).startsWith('data:image/png') && (await page.getAttribute('#ctxBig', 'src')) !== prev);
    const want = await quad(page), wmask = await page.evaluate(() => JSON.parse(JSON.stringify(fix.mask)));
    await page.click('#fixSave'); await page.waitForTimeout(900);
    const doc = (store.docs.recuts || {})[sid];
    const shaped = doc && Array.isArray(doc.quad) && doc.quad.length === 4 && doc.quad.every(p => Array.isArray(p) && p.length === 2 && p.every(Number.isFinite))
      && Array.isArray(doc.mask) && doc.mask.length === 1 && Number.isFinite(doc.mask[0].r) && doc.mask[0].pts.every(p => p.length === 2 && p.every(Number.isFinite));
    ok('desktop: saved db row has the quad / mask shape', shaped && same(doc.quad, want) && same(doc.mask, wmask) && doc.page && doc.at && same(doc.old, b0), doc);
    const xs = want.map(p => p[0]), ys = want.map(p => p[1]);
    ok('desktop: saved x y w h are the quad\'s bounds', doc && same([doc.x, doc.y, doc.w, doc.h], [Math.min(...xs), Math.min(...ys), Math.max(...xs) - Math.min(...xs), Math.max(...ys) - Math.min(...ys)]));
    await page.click('#ctxClose'); await page.waitForTimeout(300);
    const t2 = page.locator('#pile__88_ .tiles .t[data-sid="' + sid + '"]');
    ok('desktop: tile keeps its pile, badge, redrawn thumbnail', (await t2.locator('.rcb').count()) === 1 && (await t2.locator('img').getAttribute('src')) !== src0);
    const differ = await page.evaluate(async s => { const r = recuts[s]; const a = await renderRecut(s, r), b2 = await renderRecut(s, { ...r, mask: [] }); return a && b2 && a !== b2; }, sid);
    ok('desktop: the mask changes the redrawn thumbnail (stroke painted as paper)', differ);
    const white = await page.evaluate(async s => {   // the stroke's centre point, warped into the thumbnail, is paper
      const r = recuts[s], u = await renderRecut(s, r), im = new Image(); im.src = u; await im.decode();
      const cv = document.createElement('canvas'); cv.width = im.width; cv.height = im.height; const g = cv.getContext('2d'); g.drawImage(im, 0, 0);
      const [W, H] = quadSize(r.quad), [top, bot, side] = tileMargins(W, H), OW = W + 2 * side, OH = H + top + bot;
      const inv = homography(r.quad, [[side, top], [side + W, top], [side + W, top + H], [side, top + H]]), p = r.mask[0].pts[1], [u2, v2] = hApply(inv, p[0], p[1]);
      return g.getImageData(Math.floor(u2 / OW * im.width), Math.floor(v2 / OH * im.height), 1, 1).data[0]; }, sid);
    ok('desktop: the thumbnail is white under the stroke', white >= 240, white);
    // an old-form {x, y, w, h} recut from the db still loads, draws and re-opens as a plain box
    const sid2 = await page.locator('#pile__88_ .tiles .t').nth(2).getAttribute('data-sid'); const c0 = await page.evaluate(s => itemBySid[s].b.slice(), sid2);
    await store.external(page, 'recuts', sid2, { sid: sid2, page: 'p1', x: c0[0] - 2, y: c0[1], w: c0[2] + 4, h: c0[3], old: c0, at: '2026-10-04T19:00:00Z' });
    await page.waitForTimeout(600);
    ok('old form: loads as a plain box with badge and thumbnail', await page.evaluate(s => !!recuts[s] && !recuts[s].quad && !!recutImg[s], sid2)
      && (await page.locator('#pile__88_ .tiles .t[data-sid="' + sid2 + '"] .rcb').count()) === 1);
    await mock.hold(page, page.locator('#pile__88_ .tiles .t[data-sid="' + sid2 + '"]')); await page.click('#ctxFix'); await page.waitForTimeout(200);
    ok('old form: Fix the cut opens it as its four box corners', same(await quad(page), [[c0[0] - 2, c0[1]], [c0[0] + c0[2] + 2, c0[1]], [c0[0] + c0[2] + 2, c0[1] + c0[3]], [c0[0] - 2, c0[1] + c0[3]]]));
    await page.click('#fixSave'); await page.waitForTimeout(300);
    ok('old form: saving with no change leaves the old row alone', /unchanged/.test(await page.textContent('#ctxMsg')) && !(store.docs.recuts[sid2].quad));
    await page.click('#ctxClose');
    await page.reload(); await page.waitForTimeout(2000);
    ok('reload: the quad and mask come back from the db', await page.evaluate(([s, q, m]) => !!recuts[s] && JSON.stringify(recuts[s].quad) === JSON.stringify(q)
      && JSON.stringify(recuts[s].mask) === JSON.stringify(m) && !!recutImg[s], [sid, want, wmask]));
    ok('reload: the old-form recut too', await page.evaluate(s => !!recuts[s] && !recuts[s].quad && !!recutImg[s], sid2));
    await mock.hold(page, page.locator('#pile__88_ .tiles .t[data-sid="' + sid + '"]')); await page.click('#ctxFix'); await page.waitForTimeout(200);
    ok('reload: re-opening the quad recut edits its corners and strokes', same(await quad(page), want) && (await page.evaluate(() => fix.mask.length)) === 1);
    await page.click('#fixReset'); await page.click('#fixSave'); await page.waitForTimeout(900);
    ok('"Back to the first cut" then save removes the row', !(store.docs.recuts || {})[sid]);
    await page.screenshot({ path: (process.argv[3] || '/tmp/test_recut_quad') + '.png' });
    await ctx.close();
  }
  // ---- phone: a touch corner drag and a touch stroke, no scroll
  {
    const ctx = await b.newContext({ viewport: { width: 390, height: 760 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 });
    const store = await mock.install(ctx); const page = await ctx.newPage();
    page.on('pageerror', e => errs.push(e.message)); await page.goto('file://' + process.argv[2]); await page.waitForTimeout(1200);
    const t = page.locator('#pile__88_ .tiles .t').nth(0); const sid = await t.getAttribute('data-sid');
    await mock.hold(page, t); await page.tap('#ctxFix'); await page.waitForTimeout(200);
    await page.evaluate(() => document.getElementById('ctxC').scrollIntoView({ block: 'center' }));
    const sc0 = await page.evaluate(() => [document.querySelector('#ctx .box').scrollTop, window.scrollY]);
    const q0 = await quad(page); await dragBy(page, await pointAt(page, ...q0[2]), 12, 10); const q1 = await quad(page);
    const scd = await page.evaluate(() => [document.querySelector('#ctx .box').scrollTop, window.scrollY]);
    ok('phone: touch drag on the bottom-right handle moves that corner only, no scroll', same(moved(q0, q1), [2]) && same(sc0, scd), { q0, q1, sc0, scd });
    await page.tap('#fixBrush'); const mid = [(q1[0][0] + q1[2][0]) / 2, (q1[0][1] + q1[2][1]) / 2];
    await page.evaluate(() => document.getElementById('ctxC').scrollIntoView({ block: 'center' }));   // the toggle sits below the canvas
    const sc2 = await page.evaluate(() => [document.querySelector('#ctx .box').scrollTop, window.scrollY]);
    await dragBy(page, await pointAt(page, mid[0] - 5, mid[1]), 30, 0);
    const sc1 = await page.evaluate(() => [document.querySelector('#ctx .box').scrollTop, window.scrollY]);
    ok('phone: a touch stroke is one mask stroke, the box unmoved, no scroll', (await page.evaluate(() => fix.mask.length)) === 1 && same(await quad(page), q1) && same(sc2, sc1), { sc0, sc2, sc1 });
    await page.tap('#fixSave'); await page.waitForTimeout(900);
    const doc = (store.docs.recuts || {})[sid];
    ok('phone: saved with quad and mask', doc && same(doc.quad, q1) && doc.mask.length === 1, doc);
    await ctx.close();
  }
  // ---- whole-page view (region fixture): a corner drag moves one corner there too
  if (process.argv[4]) {
    const ctx = await b.newContext({ viewport: { width: 1200, height: 900 } }); await mock.install(ctx); const page = await ctx.newPage();
    page.on('pageerror', e => errs.push(e.message)); await page.goto('file://' + process.argv[4]); await page.waitForTimeout(1500);
    await mock.hold(page, page.locator('.tiles .t').first()); await page.waitForTimeout(400); await page.click('#ctxFix'); await page.waitForTimeout(400);
    const view = await page.evaluate(() => document.getElementById('ctxC').dataset.view);
    const q0 = await quad(page); await dragBy(page, await pointAt(page, ...q0[0]), -10, -8); const q1 = await quad(page);
    ok('page view: dragging the top-left handle moves that corner only', view === 'page' && same(moved(q0, q1), [0]) && q1[0][0] < q0[0][0], { view, q0, q1 });
    await ctx.close();
  }
  console.log('errors:', errs); const all = res.every(r => r[1]) && !errs.length; console.log(all ? 'ALL PASS' : 'FAILED'); await b.close(); process.exit(all ? 0 : 1);
})();
