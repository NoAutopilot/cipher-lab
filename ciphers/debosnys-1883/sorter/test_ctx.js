const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_EXE });
  const page = await b.newPage({ viewport: { width: 1200, height: 900 } });
  const errs = []; page.on('pageerror', e => errs.push(e.message));
  await page.addInitScript(() => { window.claude = { use: async () => null }; });
  await page.goto('file://' + process.argv[2]); await page.waitForTimeout(400);
  await page.click('#ink2'); await page.click('#modeCtx');
  const x = page.locator('.pile').filter({ has: page.locator('.pid', { hasText: /^X$/ }) }).first();
  await x.locator('.tiles .t').nth(5).click(); await page.waitForTimeout(400);
  console.log('ctx open:', await page.isVisible('#ctx'), await page.textContent('#ctxT'));
  await page.screenshot({ path: process.argv[3] });
  await page.click('#ctxSel'); console.log('selected after ctx:', await x.locator('.t.sel').count());
  console.log('errors:', errs);
  await b.close();
})();
