// Undo in both places: the toolbar puts taken-out signs back; the dialog's Undo shows the undone tile again.
const { chromium } = require('playwright'); const mock = require('./mock_db');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_EXE });
  const ctx = await b.newContext({ viewport: { width: 1200, height: 900 } }); await mock.install(ctx); const page = await ctx.newPage();
  const errs = []; page.on('pageerror', e => errs.push(e.message));
  await page.goto('file://' + process.argv[2]); await page.waitForTimeout(1000);
  const x = page.locator('#pile__88_'); const before = await x.locator('.cnt').textContent();
  for (let i = 0; i < 3; i++) await x.locator('.tiles .t').first().click();
  const mid = await x.locator('.cnt').textContent();
  for (let i = 0; i < 3; i++) await page.click('#undo');
  const after = await x.locator('.cnt').textContent();
  console.log(before, '|', mid, '|', after, '| undo disabled now:', await page.isDisabled('#undo'));
  await mock.hold(page, x.locator('.tiles .t').first()); const t1 = await page.textContent('#ctxT');
  await page.click('#ctxBad'); await page.click('#ctxUndo'); const t2 = await page.textContent('#ctxT');
  console.log('ctx undo:', t1, '->', t2, '|', await page.textContent('#ctxMsg'));
  await page.click('#ctxClose'); await page.screenshot({ path: process.argv[3] });
  const okay = before === after && mid !== before && t1 === t2 && !errs.length;
  console.log('errors:', errs); console.log(okay ? 'ALL PASS' : 'FAILED'); await b.close(); process.exit(okay ? 0 : 1);
})();
