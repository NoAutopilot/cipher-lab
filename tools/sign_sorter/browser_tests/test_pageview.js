// "Whole page" larger view (SORTER-PAGEVIEW; owner, 4 Oct 2026, Longlee f101v_L32_49: "can we just show the full graphic?").
// On a page built with --region the larger view opens on the original region, continuous (the ruled stroke between lines 2
// and 3 shows, which no strip holds), the tile's ink inside its drawn box and the line above visible; "Line strips" switches
// back and is remembered; "Fix the cut" works on the page image and saves strip pixels; a phone has no horizontal page
// scroll; a region image that fails to load falls back to the strips.   node test_pageview.js region.html [shot]
const { chromium } = require('playwright'); const mock = require('./mock_db');
const box = page => page.evaluate(() => fix ? fix.box.slice() : null);
const pick = page => page.evaluate(() => byBase['X'].items.filter(it => it.p === 'r_L02')[3].sid);
const tileOf = (page, sid) => page.locator('.t[data-sid="' + sid + '"]').first();
// screen point of a strip-pixel point (x, y) of the tile shown, through the page view's own map
const scr = (page, x, y) => page.evaluate(([x, y]) => { const c = document.getElementById('ctxC'), m = c._map, r = c.getBoundingClientRect(), p = itemBySid[ctxSid].p;
  return [r.left + (x - m.x0) * m.s / m.k, r.top + (regY(p, x, y) - m.y0) * m.s / m.k]; }, [x, y]);
// darkest canvas pixel in a region-pixel rectangle (X0..X1, Y0..Y1) of the page view
const darkest = (page, X0, Y0, X1, Y1) => page.evaluate(([X0, Y0, X1, Y1]) => { const c = document.getElementById('ctxC'), m = c._map, g = c.getContext('2d');
  const a = Math.max(0, Math.round((X0 - m.x0) * m.s)), b = Math.max(0, Math.round((Y0 - m.y0) * m.s));
  const w = Math.max(1, Math.round((X1 - X0) * m.s)), h = Math.max(1, Math.round((Y1 - Y0) * m.s)); const d = g.getImageData(a, b, w, h).data; let mn = 255;
  for (let i = 0; i < d.length; i += 4) mn = Math.min(mn, d[i]); return mn; }, [X0, Y0, X1, Y1]);
async function dragBy(page, [x, y], dx, dy) {
  await mock.gesture(page, 'down', x, y);
  for (let i = 1; i <= 8; i++) { await mock.gesture(page, 'move', x + dx * i / 8, y + dy * i / 8); await page.waitForTimeout(16); }
  await mock.gesture(page, 'up', x + dx, y + dy); await page.waitForTimeout(100);
}
(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_EXE, args: ['--allow-file-access-from-files'] }); const res = []; const errs = [];   // file:// region image readable, as the published same-origin file is
  const ok = (name, cond, extra) => { res.push([name, !!cond]); console.log((cond ? 'ok   ' : 'FAIL ') + name, extra === undefined ? '' : JSON.stringify(extra)); };
  {   // ---- desktop
    const ctx = await b.newContext({ viewport: { width: 1200, height: 900 } }); const store = await mock.install(ctx); const page = await ctx.newPage();
    page.on('pageerror', e => errs.push(e.message)); await page.goto('file://' + process.argv[2]); await page.waitForTimeout(1200);
    const sid = await pick(page); const it = await page.evaluate(s => ({ b: itemBySid[s].b.slice(), p: itemBySid[s].p }), sid);
    await mock.hold(page, tileOf(page, sid)); await page.waitForTimeout(500);
    const v = await page.evaluate(() => ({ view: document.getElementById('ctxC').dataset.view, seg: !document.getElementById('viewSeg').hidden,
      nb: document.getElementById('ctxNbL').hidden, pressed: document.getElementById('viewPage').getAttribute('aria-pressed') }));
    ok('desk: opens in "Whole page" by default', v.view === 'page' && v.seg && v.nb && v.pressed === 'true', v);
    const [x, y, w, h] = it.b; const top = await page.evaluate(([p, x, y]) => regY(p, x, y), [it.p, x + w / 2, y]);
    const pitch = await page.evaluate(() => REG.pitch);
    ok('desk: the tile\'s ink is inside its drawn box', await darkest(page, x + 1, top + 1, x + w - 1, top + h - 1) < 110);
    ok('desk: the line above is shown (ink one line up)', await darkest(page, x - 10, top - pitch - 10, x + w + 10, top - pitch + h + 10) < 110);
    const span = await page.evaluate(() => { const c = document.getElementById('ctxC'), m = c._map; return [m.y0, m.y0 + c.height / m.s]; });
    ok('desk: three lines above and below at zoom 3 (here the whole 3-line region)', span[1] - span[0] >= 3 * pitch, span);
    // continuity: the ruled stroke at y = 300 + 0.06 x lies between lines 2 and 3 and is in no strip's middle band
    const ry = 300 + 0.06 * (x + w / 2);
    ok('desk: continuous page (the stroke between lines is drawn, no separators)', await darkest(page, x, ry - 2, x + w, ry + 2) < 180);
    // toggle to strips and back, remembered
    await page.click('#viewStrip'); await page.waitForTimeout(300);
    ok('desk: "Line strips" switches back to the strips', await page.evaluate(() => document.getElementById('ctxC').dataset.view !== 'page' && !document.getElementById('ctxNbL').hidden));
    await page.click('#ctxClose'); await page.reload(); await page.waitForTimeout(1200); await mock.hold(page, tileOf(page, sid)); await page.waitForTimeout(400);
    ok('desk: the choice is remembered', await page.evaluate(() => document.getElementById('ctxC').dataset.view !== 'page'));
    await page.click('#viewPage'); await page.waitForTimeout(400);
    ok('desk: "Whole page" again', await page.evaluate(() => document.getElementById('ctxC').dataset.view === 'page'));
    // zoom: 1 shows more (or the whole region), 8 a close-up
    const sc = () => page.evaluate(() => { const c = document.getElementById('ctxC'); return c.getBoundingClientRect().width / +c.dataset.span; });
    const s3 = await sc(); await page.fill('#ctxZ', '8'); await page.dispatchEvent('#ctxZ', 'input'); await page.waitForTimeout(100); const s8 = await sc();
    ok('desk: zoom in enlarges the page', s8 > s3 * 1.5, [s3, s8]); await page.fill('#ctxZ', '3'); await page.dispatchEvent('#ctxZ', 'input');
    // Fix the cut on the page image
    await page.click('#ctxFix'); await page.waitForTimeout(200);
    ok('desk: edit mode on in page view', !(await page.isHidden('#fixBox')) && (await box(page)).join() === it.b.join());
    await dragBy(page, await scr(page, x + w, y + h / 2), 30, 0); const b1 = await box(page);
    ok('desk: right edge dragged wider, top kept', b1[2] > w + 3 && b1[0] === x && b1[1] === y && b1[3] === h, { b0: it.b, b1 });
    await dragBy(page, await scr(page, b1[0] + b1[2] / 2, y + h), 0, 12); const b2 = await box(page);
    ok('desk: bottom edge dragged down (strip pixels)', b2[3] > h && b2[1] === y && b2[2] === b1[2], { b1, b2 });
    const k = await page.evaluate(() => { const m = document.getElementById('ctxC')._map; return m.k / m.s; });
    await dragBy(page, await scr(page, b2[0] + b2[2] / 2, b2[1] + b2[3] / 2), 0, -10); const b3 = await box(page);
    ok('desk: whole box moved up by the dragged amount', Math.abs((b2[1] - b3[1]) - 10 * k) <= 2 && b3[3] === b2[3], { b2, b3, expect: 10 * k });
    await page.click('#fixSave'); await page.waitForTimeout(900); const doc = (store.docs.recuts || {})[sid];
    ok('desk: saved to db recuts in strip pixels', doc && [doc.x, doc.y, doc.w, doc.h].join() === b3.join() && doc.old.join() === it.b.join() && doc.page === it.p, doc);
    ok('desk: page view kept after saving', await page.evaluate(() => document.getElementById('ctxC').dataset.view === 'page'));
    await page.screenshot({ path: (process.argv[3] || '/tmp/test_pageview') + '.png' });
    await ctx.close();
  }
  {   // ---- phone: no horizontal page scroll, canvas fits the dialog
    const ctx = await b.newContext({ viewport: { width: 390, height: 760 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 });
    await mock.install(ctx); const page = await ctx.newPage(); page.on('pageerror', e => errs.push(e.message));
    await page.goto('file://' + process.argv[2]); await page.waitForTimeout(1200);
    const sid = await pick(page); await mock.hold(page, tileOf(page, sid)); await page.waitForTimeout(500);
    const m = await page.evaluate(() => { const bx = document.querySelector('#ctx .box'), c = document.getElementById('ctxC');
      return { view: c.dataset.view, docW: document.documentElement.scrollWidth, vw: window.innerWidth, boxS: bx.scrollWidth, boxC: bx.clientWidth,
               cw: c.getBoundingClientRect().width, cvw: c.parentElement.clientWidth }; });
    ok('phone: page view, no horizontal page scroll, canvas fits', m.view === 'page' && m.docW <= m.vw && m.boxS <= m.boxC + 1 && m.cw <= m.cvw + 1, m);
    await page.tap('#ctxFix'); await page.tap('#fixRp'); await page.tap('#fixBp');
    const b0 = await page.evaluate(s => itemBySid[s].b.slice(), sid), b1 = await box(page);
    ok('phone: nudges still move the edges 2 px a tap', b1[2] === b0[2] + 2 && b1[3] === b0[3] + 2, { b0, b1 });
    await page.screenshot({ path: (process.argv[3] || '/tmp/test_pageview') + '_phone.png' });
    await ctx.close();
  }
  {   // ---- the region image fails to load: strips, no toggle
    const ctx = await b.newContext({ viewport: { width: 1000, height: 800 } }); await mock.install(ctx); const page = await ctx.newPage();
    page.on('pageerror', e => errs.push(e.message)); await page.goto('file://' + process.argv[2]); await page.waitForTimeout(1000);
    await page.evaluate(() => { REG.src = 'no_such_region.jpg'; delete REG.b64; });
    const sid = await pick(page); await mock.hold(page, tileOf(page, sid)); await page.waitForTimeout(800);
    ok('fallback: no region image -> line strips, toggle hidden', await page.evaluate(() => document.getElementById('ctxC').dataset.view !== 'page'
      && document.getElementById('viewSeg').hidden && document.getElementById('ctxC').width > 0));
    await ctx.close();
  }
  console.log('errors:', errs); const all = res.every(r => r[1]) && !errs.length; console.log(all ? 'ALL PASS' : 'FAILED'); await b.close(); process.exit(all ? 0 : 1);
})();
