// Holding a sign opens the larger view (ink darkness applies to it); "View larger" on a pile does too.
const { chromium } = require('playwright'); const mock = require('./mock_db');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_EXE });
  const ctx = await b.newContext({ viewport: { width: 1200, height: 900 } }); await mock.install(ctx); const page = await ctx.newPage();
  const errs = []; page.on('pageerror', e => errs.push(e.message));
  await page.goto('file://' + process.argv[2]); await page.waitForTimeout(1000);
  await page.locator('.opts summary').click(); await page.click('#ink2');
  const x = page.locator('#pile__88_'); const sid = await x.locator('.tiles .t').nth(5).getAttribute('data-sid');
  await mock.hold(page, x.locator('.tiles .t').nth(5));
  const t = await page.textContent('#ctxT'); console.log('ctx open:', await page.isVisible('#ctx'), t);
  await page.screenshot({ path: process.argv[3] });
  await page.click('#ctxClose'); await x.locator('.ph .big').click(); const t2 = await page.textContent('#ctxPos');
  console.log('view larger:', t2);
  const okay = t.includes(sid) && /^1 of/.test(t2) && !errs.length;
  console.log('errors:', errs); console.log(okay ? 'ALL PASS' : 'FAILED'); await b.close(); process.exit(okay ? 0 : 1);
})();
