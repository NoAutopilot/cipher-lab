const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_EXE });
  const page = await b.newPage(); const errs = []; page.on('pageerror', e => errs.push(e.message));
  await page.addInitScript(() => { window.claude = { use: async () => null }; });
  await page.goto('file://' + process.argv[2]); await page.waitForTimeout(400);
  await page.click('#modeCtx');
  await page.locator('.pile').filter({ has: page.locator('.pid', { hasText: /^X$/ }) }).first().locator('.tiles .t').nth(3).click();
  await page.click('#ctxBad'); console.log(await page.textContent('#ctxMsg')); await page.click('#ctxClose');
  const bad = page.locator('.pile').filter({ has: page.locator('.pid', { hasText: /^BAD-CUT$/ }) });
  console.log('BAD-CUT tiles:', await bad.locator('.t').count(), 'errors:', errs); await b.close();
})();
