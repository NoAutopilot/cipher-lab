const { chromium } = require('playwright');
(async () => { const b = await chromium.launch({ executablePath: process.env.PW_EXE }); const page = await b.newPage({viewport:{width:1200,height:900}});
  const errs = []; page.on('pageerror', e => errs.push(e.message)); await page.addInitScript(() => { window.claude = { use: async () => null }; });
  await page.goto('file://' + process.argv[2]); await page.waitForTimeout(400);
  console.log('focus tiles:', await page.locator('#focusTiles .t').count());
  await page.locator('#focusTiles .t').first().click(); console.log('ctx:', await page.textContent('#ctxT'));
  await page.click('#ctxClose'); await page.screenshot({ path: process.argv[3] }); console.log('errors:', errs); await b.close(); })();
