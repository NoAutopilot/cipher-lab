// "Fix the cut" (owner, 4 Oct 2026, Longlee f101v_L03_04): in the larger view the bracket box is dragged (desktop: an edge,
// then the whole box) or nudged (phone: the arrow buttons, 2 source px a tap, and a touch drag that must not scroll); "Save
// cut" writes db 'recuts' {sid, page, x, y, w, h, old, at}; the tile gets a "recut" badge and a redrawn thumbnail and stays in
// its pile; Undo removes the recut; a BAD-CUT tile, once recut, goes back to its home pile with one tap.
const { chromium } = require('playwright'); const mock = require('./mock_db');
const box = page => page.evaluate(() => fix ? fix.box.slice() : null);
async function edgePoint(page, which) {   // screen point of an edge midpoint (or the box centre) of the box being edited
  return page.evaluate(w => { const c = document.getElementById('ctxC'), m = c._map, r = c.getBoundingClientRect(), [x, y, bw, bh] = fix.box;
    const sx = w === 'r' ? x + bw : x + bw / 2, sy = w === 'r' ? y + bh / 2 : y + bh / 2;
    return [r.left + ((sx * m.ps - m.x0) * m.s) / m.k, r.top + ((sy * m.ps - m.y0) * m.s + m.ha) / m.k]; }, which);
}
async function dragBy(page, [x, y], dx, dy) {
  await mock.gesture(page, 'down', x, y);
  for (let i = 1; i <= 8; i++) { await mock.gesture(page, 'move', x + dx * i / 8, y + dy * i / 8); await page.waitForTimeout(16); }
  await mock.gesture(page, 'up', x + dx, y + dy); await page.waitForTimeout(100);
}
(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_EXE }); const res = []; const errs = [];
  const ok = (name, cond, extra) => { res.push([name, !!cond]); console.log((cond ? 'ok   ' : 'FAIL ') + name, extra === undefined ? '' : JSON.stringify(extra)); };
  // ---- desktop: drag an edge, drag the box, save, badge, undo
  {
    const ctx = await b.newContext({ viewport: { width: 1200, height: 900 } }); const store = await mock.install(ctx); const page = await ctx.newPage();
    page.on('pageerror', e => errs.push(e.message)); await page.goto('file://' + process.argv[2]); await page.waitForTimeout(1200);
    const t = page.locator('#pile__88_ .tiles .t').nth(1); const sid = await t.getAttribute('data-sid');
    const b0 = await page.evaluate(s => itemBySid[s].b.slice(), sid); const src0 = await t.locator('img').getAttribute('src');
    await mock.hold(page, t); await page.click('#ctxFix'); await page.waitForTimeout(200);
    ok('desktop: edit mode on', !(await page.isHidden('#fixBox')) && (await box(page)).join() === b0.join());
    await dragBy(page, await edgePoint(page, 'r'), 30, 0); const b1 = await box(page);
    ok('desktop: right edge dragged wider', b1[2] > b0[2] + 3 && b1[0] === b0[0], { b0, b1 });
    await dragBy(page, await edgePoint(page, 'c'), -15, 0); const b2 = await box(page);
    ok('desktop: whole box moved, size kept', b2[0] < b1[0] && b2[2] === b1[2] && b2[3] === b1[3], { b1, b2 });
    await page.click('#fixSave'); await page.waitForTimeout(900);
    const doc = (store.docs.recuts || {})[sid];
    ok('desktop: save -> db recuts doc', doc && doc.sid === sid && [doc.x, doc.y, doc.w, doc.h].join() === b2.join() && doc.old.join() === b0.join() && doc.at && doc.page, doc);
    ok('desktop: edit mode off after save', await page.isHidden('#fixBox'));
    await page.click('#ctxClose'); await page.waitForTimeout(300);
    const t2 = page.locator('#pile__88_ .tiles .t[data-sid="' + sid + '"]');
    ok('desktop: tile stays in its pile with a recut badge', (await t2.count()) === 1 && (await t2.locator('.rcb').count()) === 1);
    ok('desktop: thumbnail redrawn at the new box', (await t2.locator('img').getAttribute('src')) !== src0);
    await page.click('#undo'); await page.waitForTimeout(900);
    ok('desktop: undo removes the recut', !(store.docs.recuts || {})[sid] && (await page.locator('#pile__88_ .tiles .t[data-sid="' + sid + '"] .rcb').count()) === 0
      && (await page.locator('#pile__88_ .tiles .t[data-sid="' + sid + '"] img').getAttribute('src')) === src0);
    // cancel restores
    await mock.hold(page, page.locator('#pile__88_ .tiles .t').nth(2)); await page.click('#ctxFix'); await page.click('#fixRp'); await page.click('#fixCancel');
    ok('desktop: cancel leaves no recut', Object.keys(store.docs.recuts || {}).length === 0 && await page.isHidden('#fixBox'));
    await page.click('#ctxClose'); await page.screenshot({ path: (process.argv[3] || '/tmp/test_recut') + '.png' });
    await ctx.close();
  }
  // ---- phone: nudge buttons, a touch drag that does not scroll, save; a BAD-CUT tile put back with one tap
  {
    const ctx = await b.newContext({ viewport: { width: 390, height: 760 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 });
    const store = await mock.install(ctx); const page = await ctx.newPage();
    page.on('pageerror', e => errs.push(e.message)); await page.goto('file://' + process.argv[2]); await page.waitForTimeout(1200);
    const t = page.locator('#pile__88_ .tiles .t').nth(0); const sid = await t.getAttribute('data-sid'); const b0 = await page.evaluate(s => itemBySid[s].b.slice(), sid);
    await mock.hold(page, t); await page.tap('#ctxFix'); await page.waitForTimeout(200);
    for (let i = 0; i < 3; i++) await page.tap('#fixLm');
    for (let i = 0; i < 2; i++) await page.tap('#fixBp');
    await page.tap('#fixTp');
    const b1 = await box(page);
    ok('phone: nudges move edges 2 px a tap', b1[0] === b0[0] - 6 && b1[2] === b0[2] + 6 && b1[1] === b0[1] + 2 && b1[3] === b0[3] - 2 + 4, { b0, b1 });
    await page.evaluate(() => document.getElementById('ctxC').scrollIntoView({ block: 'center' }));
    const sc0 = await page.evaluate(() => [document.querySelector('#ctx .box').scrollTop, window.scrollY]);
    await dragBy(page, await edgePoint(page, 'c'), 0, 25); const b2 = await box(page);
    const sc1 = await page.evaluate(() => [document.querySelector('#ctx .box').scrollTop, window.scrollY]);
    ok('phone: touch drag moves the box, no scroll', b2[1] > b1[1] && b2[2] === b1[2] && sc0.join() === sc1.join(), { b1, b2, sc0, sc1 });
    await page.tap('#fixSave'); await page.waitForTimeout(900);
    const doc = (store.docs.recuts || {})[sid];
    ok('phone: saved', doc && [doc.x, doc.y, doc.w, doc.h].join() === b2.join(), doc);
    // BAD-CUT, then recut, then one tap back home
    await page.tap('#ctxClose'); await page.waitForTimeout(200);
    const u = page.locator('#pile__88_ .tiles .t').nth(3); const sid2 = await u.getAttribute('data-sid');
    await mock.hold(page, u); await page.tap('#ctxBad'); await page.waitForTimeout(300); await page.tap('#ctxClose'); await page.waitForTimeout(200);
    const bad = page.locator('.pile').filter({ has: page.locator('.pid', { hasText: /^BAD-CUT$/ }) }).locator('.t[data-sid="' + sid2 + '"]');
    ok('phone: tile in BAD-CUT', (await bad.count()) === 1);
    await mock.hold(page, bad); await page.tap('#ctxFix'); await page.tap('#fixRm'); await page.tap('#fixSave'); await page.waitForTimeout(600);
    ok('phone: offer to put it back', (await page.locator('#ctxPutBack').count()) === 1 && /Put it back in X/.test(await page.textContent('#ctxPutBack')));
    await page.tap('#ctxPutBack'); await page.waitForTimeout(900);
    ok('phone: back in its home pile, recut kept', !(store.docs.moves || {})[sid2] && !!(store.docs.recuts || {})[sid2]);
    await page.tap('#ctxClose'); await page.waitForTimeout(200);
    ok('phone: home pile shows it with the badge', (await page.locator('#pile__88_ .tiles .t[data-sid="' + sid2 + '"] .rcb').count()) === 1);
    // reload: the saved recuts come back from the store
    await page.reload(); await page.waitForTimeout(2000);
    ok('phone: recuts reload from the db', (await page.locator('.t .rcb').count()) >= 2 && await page.evaluate(s => !!recuts[s] && !!recutImg[s], sid));
    await ctx.close();
  }
  console.log('errors:', errs); const all = res.every(r => r[1]) && !errs.length; console.log(all ? 'ALL PASS' : 'FAILED'); await b.close(); process.exit(all ? 0 : 1);
})();
