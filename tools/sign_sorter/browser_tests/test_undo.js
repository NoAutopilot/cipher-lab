const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_EXE });
  const page = await b.newPage({ viewport: { width: 1200, height: 900 } }); const errs = []; page.on('pageerror', e => errs.push(e.message));
  await page.addInitScript(() => { window.claude = { use: async () => null }; });
  await page.goto('file://' + process.argv[2]); await page.waitForTimeout(400);
  const x = page.locator('.pile').filter({ has: page.locator('.pid', { hasText: /^X$/ }) }).first();
  const before = await x.locator('.cnt').textContent();
  for (let i = 0; i < 3; i++) await x.locator('.tiles .t').nth(i).click();
  await x.locator('.movebar button', { hasText: 'Set aside' }).click();
  const mid = await x.locator('.cnt').textContent();
  await page.click('#undo');
  console.log(before, '|', mid, '|', await x.locator('.cnt').textContent(), '| undo disabled now:', await page.isDisabled('#undo'));
  await page.click('#modeCtx'); await x.locator('.tiles .t').nth(0).click(); const t1 = await page.textContent('#ctxT');
  await page.click('#ctxBad'); await page.click('#ctxUndo');
  console.log('ctx undo:', t1, '->', await page.textContent('#ctxT'), '|', await page.textContent('#ctxMsg'));
  await page.click('#ctxClose'); await page.screenshot({ path: process.argv[3] });
  console.log('errors:', errs); await b.close();
})();
