// Step 2: drag a pile card by its name onto another card merges the whole pile (state.merge_into), the merged card leaves
// the list, and "Undo merge" restores it (owner, 4 Oct 2026). Desktop mouse and phone touch (template 2026-10-09.5: hold the name
// 500 ms until it is outlined, then drag; a still finger lifts nothing -- owner rule R05).
// Run: PW_EXE=/opt/pw-browsers/chromium NODE_PATH=$(npm root -g) node test_s2_pilemerge.js PAGE.html SHOT.png
const { chromium } = require('playwright'); const mock = require('./mock_db');
(async () => {
  const browser = await chromium.launch({ executablePath: process.env.PW_EXE || undefined }); const res = {}; const errs = [];
  for (const [tag, o] of [['desk', { viewport: { width: 1280, height: 800 } }], ['phone', { viewport: { width: 390, height: 760 }, isMobile: true, hasTouch: true }]]) {
    const ctx = await browser.newContext(o); const store = await mock.install(ctx); const page = await ctx.newPage(); page.on('pageerror', e => errs.push(e.message));
    await page.goto('file://' + process.argv[2]); await page.waitForTimeout(1000);
    await page.evaluate(() => { const L = document.querySelectorAll('#list .t'); for (let i = 0; i < Math.min(2, L.length); i++) L[i].click(); });
    await page.click('#trayGo'); await page.waitForTimeout(800);
    const info = await page.evaluate(() => { const cs = [...document.querySelectorAll('.card')]; const a = cs[0], b = cs[1];
      a.scrollIntoView({ block: 'center' }); const sb = document.getElementById('s2Stick').getBoundingClientRect().bottom, ar = a.getBoundingClientRect(); if (ar.top < sb + 10) window.scrollBy(0, ar.top - sb - 10);
      return { from: a.dataset.pile, to: b.dataset.pile }; });
    await page.waitForTimeout(200);
    const hb = await page.locator('.card[data-pile="' + info.from + '"] .cid').boundingBox(), tb = await page.locator('.card[data-pile="' + info.to + '"]').boundingBox(); console.log('cards', await page.locator('.card').count());
    const x0 = hb.x + 10, y0 = hb.y + hb.height / 2, x1 = tb.x + tb.width / 2, y1 = tb.y + tb.height / 2;
    await mock.gesture(page, 'down', x0, y0); await page.waitForTimeout(tag === 'phone' ? 650 : 30);
    if (tag === 'phone') res.phoneStill = await page.evaluate(() => !document.querySelector('.ghost') && !!document.querySelector('.card .cid.armed'));   // armed, nothing lifted yet
    for (let i = 1; i <= 12; i++){ await mock.gesture(page, 'move', x0 + (x1 - x0) * i / 12, y0 + (y1 - y0) * i / 12); await page.waitForTimeout(16); }
    await mock.gesture(page, 'up', x1, y1); await page.waitForTimeout(500);
    const merged = await page.evaluate(f => [state[f] && state[f].merge_into, !!document.querySelector('.card[data-pile="' + f + '"]')], info.from);
    const stored = ((store.docs.piles || {})[info.from] || {}).merge_into;
    await page.locator('#s2Msg button', { hasText: 'Undo merge' }).click(); await page.waitForTimeout(300);
    const undone = await page.evaluate(f => [state[f] && state[f].merge_into, !!document.querySelector('.card[data-pile="' + f + '"]')], info.from);
    res[tag] = merged[0] === info.to && !merged[1] && stored === info.to && !undone[0] && undone[1] && (tag !== 'phone' || res.phoneStill);
    console.log(tag, info, merged, stored, undone);
    if (tag === 'desk') await page.screenshot({ path: process.argv[3] });
    await ctx.close();
  }
  console.log(res, 'errors:', errs); const ok = res.desk && res.phone && !errs.length;
  console.log(ok ? 'ALL PASS' : 'FAILED'); await browser.close(); process.exit(ok ? 0 : 1);
})().catch(e => { console.error(e); process.exit(1); });
