// Step 1 of the two-step sorter on the synthetic fixture (make_fixtures.py): tapping signs takes them out into the tray,
// the store gets one 'OUT' move each, step 2 places them (tap a card, one-tap new sign), "This pile is done" is saved.
// Run: PW_EXE=/opt/pw-browsers/chromium NODE_PATH=$(npm root -g) node test_sorter.js PAGE.html SHOT.png
const { chromium } = require('playwright'); const mock = require('./mock_db');
(async () => {
  const browser = await chromium.launch({ executablePath: process.env.PW_EXE || undefined });
  const ctx = await browser.newContext({ viewport: { width: 1200, height: 900 } }); const store = await mock.install(ctx); const page = await ctx.newPage();
  const errs = []; page.on('pageerror', e => errs.push(e.message));
  await page.goto('file://' + process.argv[2]); await page.waitForTimeout(1000);
  const x = page.locator('#pile__88_');
  console.log('X tiles:', await x.locator('.tiles .t').count());
  for (let i = 0; i < 5; i++) await x.locator('.tiles .t').first().click();   // rapid taps
  await page.waitForTimeout(800);
  const outs = Object.values(store.docs.moves || {}).filter(m => m.to === 'OUT').length;
  console.log('stored OUT moves:', outs, '| tray:', await page.textContent('#trayN'), '| X header:', await x.locator('.cnt').textContent());
  await page.click('#trayGo'); await page.waitForTimeout(500);
  const first = await page.evaluate(() => s2Cur); const card = await page.locator('.card').first().getAttribute('data-pile');
  await page.locator('.card .cid').first().click(); await page.click('#s2New'); await page.waitForTimeout(800);
  const st = await page.evaluate(() => ({ moves, np: Object.keys(newPiles) }));
  console.log('placed', first, 'in', st.moves[first] || '(home)', '| card was', card, '| new piles:', st.np);
  await page.click('#tab1'); await x.locator('.acts button', { hasText: 'This pile is done' }).click(); await page.waitForTimeout(600);
  const v = (store.docs.piles || {})['X'] || {};
  console.log('X verdict stored:', v.verdict, '| status:', await page.locator('#save').textContent());
  await page.screenshot({ path: process.argv[3] });
  const okay = outs === 5 && (st.moves[first] || 'X') === card && st.np.includes('X-b') && v.verdict === 'same' && !errs.length;
  console.log('errors:', errs); console.log(okay ? 'ALL PASS' : 'FAILED'); await browser.close(); process.exit(okay ? 0 : 1);
})().catch(e => { console.error(e); process.exit(1); });
