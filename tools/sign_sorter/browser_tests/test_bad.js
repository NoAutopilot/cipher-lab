// "Bad cut" from the larger view parks the tile in the BAD-CUT pile.
const { chromium } = require('playwright'); const mock = require('./mock_db');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_EXE });
  const ctx = await b.newContext(); await mock.install(ctx); const page = await ctx.newPage(); const errs = []; page.on('pageerror', e => errs.push(e.message));
  await page.goto('file://' + process.argv[2]); await page.waitForTimeout(1000);
  await mock.hold(page, page.locator('#pile__88_ .tiles .t').nth(3));
  await page.click('#ctxBad'); console.log(await page.textContent('#ctxMsg')); await page.click('#ctxClose');
  const n = await page.locator('.pile').filter({ has: page.locator('.pid', { hasText: /^BAD-CUT$/ }) }).locator('.t').count();
  console.log('BAD-CUT tiles:', n, 'errors:', errs); const okay = n === 1 && !errs.length; console.log(okay ? 'ALL PASS' : 'FAILED'); await b.close(); process.exit(okay ? 0 : 1);
})();
