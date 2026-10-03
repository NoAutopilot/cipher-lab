// The larger view of a pile: stepping (button and arrow key), one-tap new sign (named by the page, X-b), move to it, set aside.
const { chromium } = require('playwright'); const mock = require('./mock_db');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_EXE });
  const ctx = await b.newContext({ viewport: { width: 1200, height: 900 } }); await mock.install(ctx); const page = await ctx.newPage();
  const errs = []; page.on('pageerror', e => errs.push(e.message));
  await page.goto('file://' + process.argv[2]); await page.waitForTimeout(1000);
  const x = page.locator('#pile__88_');
  await x.locator('.ph .big').click();
  console.log(await page.textContent('#ctxT'), '|', await page.textContent('#ctxPos'));
  await page.click('#ctxNext'); await page.keyboard.press('ArrowRight');
  const p3 = await page.textContent('#ctxPos'); console.log('after 2 steps:', await page.textContent('#ctxT'), '|', p3);
  await page.click('#ctxNewB');   // one tap, the page names the pile (X-b); nothing to type (owner, 3 Oct 2026)
  console.log('msg:', await page.textContent('#ctxMsg'), '|', await page.textContent('#ctxT'));
  await page.selectOption('#ctxDest', 'X-b'); console.log('msg2:', await page.textContent('#ctxMsg'));
  await page.click('#ctxAside'); console.log('msg3:', await page.textContent('#ctxMsg'));
  await page.click('#ctxClose');
  console.log('X header:', await x.locator('.cnt').textContent());
  const nb = await page.locator('.pile').filter({ has: page.locator('.pid', { hasText: /^X-b$/ }) }).locator('.t').count();
  console.log('new pile X-b tiles:', nb); const okay = nb === 2 && /^3 of/.test(p3) && !errs.length;
  console.log('errors:', errs); console.log(okay ? 'ALL PASS' : 'FAILED'); await b.close(); process.exit(okay ? 0 : 1);
})();
