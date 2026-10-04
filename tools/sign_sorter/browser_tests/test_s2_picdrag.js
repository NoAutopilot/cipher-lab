// Step 2: drag a small picture from one pile card onto another moves that tile, and the sign being placed stays put
// (owner, 4 Oct 2026). Mouse on a desktop; touch on a phone (press 1/4 s, then drag).
// Run: PW_EXE=/opt/pw-browsers/chromium NODE_PATH=$(npm root -g) node test_s2_picdrag.js PAGE.html SHOT.png
const { chromium } = require('playwright'); const mock = require('./mock_db');
(async () => {
  const browser = await chromium.launch({ executablePath: process.env.PW_EXE || undefined }); const res = {}; const errs = [];
  for (const [tag, o] of [['desk', { viewport: { width: 1280, height: 800 } }], ['phone', { viewport: { width: 390, height: 760 }, isMobile: true, hasTouch: true }]]) {
    const ctx = await browser.newContext(o); await mock.install(ctx); const page = await ctx.newPage(); page.on('pageerror', e => errs.push(e.message));
    await page.goto('file://' + process.argv[2]); await page.waitForTimeout(1000);
    await page.evaluate(() => { const L = document.querySelectorAll('#list .t'); for (let i = 0; i < Math.min(3, L.length); i++) L[i].click(); });
    await page.click('#trayGo'); await page.waitForTimeout(800);
    const cur = await page.evaluate(() => s2Cur);
    const info = await page.evaluate(() => { const cs = [...document.querySelectorAll('.card')].filter(c => c.querySelector('.smp img'));
      const a = cs[0], b = cs[1]; a.scrollIntoView({ block: 'center' }); const sb = document.getElementById('s2Stick').getBoundingClientRect().bottom, ar = a.getBoundingClientRect(); if (ar.top < sb + 10) window.scrollBy(0, ar.top - sb - 10); return { from: a.dataset.pile, to: b.dataset.pile }; });
    await page.waitForTimeout(200);
    const pic = page.locator('.card[data-pile="' + info.from + '"] .smp img').first();
    const sid = await page.evaluate(f => [...document.querySelectorAll('.card')].find(c => c.dataset.pile === f).querySelector('.smp img').src, info.from);
    const pb = await pic.boundingBox(); const tb = await page.locator('.card[data-pile="' + info.to + '"] .cid').boundingBox();
    const x0 = pb.x + pb.width / 2, y0 = pb.y + pb.height / 2, x1 = tb.x + tb.width / 2, y1 = tb.y + tb.height / 2;
    const before = await page.evaluate(f => membersOf(f).length, info.from);
    await mock.gesture(page, 'down', x0, y0); await page.waitForTimeout(tag === 'phone' ? 350 : 30);
    for (let i = 1; i <= 12; i++){ await mock.gesture(page, 'move', x0 + (x1 - x0) * i / 12, y0 + (y1 - y0) * i / 12); await page.waitForTimeout(16); }
    await mock.gesture(page, 'up', x1, y1); await page.waitForTimeout(400);
    const after = await page.evaluate(([f, t]) => [membersOf(f).length, membersOf(t).length, s2Cur, $('ctx').hidden], [info.from, info.to]);
    res[tag] = after[0] === before - 1 && after[2] === cur && after[3] === true;
    console.log(tag, info, before, after);
    if (tag === 'desk') await page.screenshot({ path: process.argv[3] });
    await ctx.close();
  }
  console.log(res, 'errors:', errs); const ok = res.desk && res.phone && !errs.length;
  console.log(ok ? 'ALL PASS' : 'FAILED'); await browser.close(); process.exit(ok ? 0 : 1);
})().catch(e => { console.error(e); process.exit(1); });
