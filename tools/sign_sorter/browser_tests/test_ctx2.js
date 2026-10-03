const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_EXE });
  const page = await b.newPage({ viewport: { width: 1200, height: 900 } });
  const errs = []; page.on('pageerror', e => errs.push(e.message));
  await page.addInitScript(() => { window.claude = { use: async () => null }; });
  await page.goto('file://' + process.argv[2]); await page.waitForTimeout(400);
  await page.click('#modeCtx');
  const x = page.locator('.pile').filter({ has: page.locator('.pid', { hasText: /^X$/ }) }).first();
  await x.locator('.tiles .t').nth(0).click();
  console.log(await page.textContent('#ctxT'), '|', await page.textContent('#ctxPos'));
  await page.click('#ctxNext'); await page.keyboard.press('ArrowRight');
  console.log('after 2 steps:', await page.textContent('#ctxT'), '|', await page.textContent('#ctxPos'));
  await page.click('#ctxNewB');   // one tap, the page names the pile (X-b); nothing to type (owner, 3 Oct 2026)
  console.log('msg:', await page.textContent('#ctxMsg'), '|', await page.textContent('#ctxT'));
  await page.selectOption('#ctxDest', 'X-b'); console.log('msg2:', await page.textContent('#ctxMsg'));
  await page.click('#ctxAside'); console.log('msg3:', await page.textContent('#ctxMsg'));
  await page.click('#ctxClose');
  console.log('X header:', await x.locator('.cnt').textContent());
  const nb = await page.locator('.pile').filter({ has: page.locator('.pid', { hasText: /^X-b$/ }) }).locator('.t').count();
  console.log('new pile X-b tiles:', nb); if (nb !== 2 || errs.length) { console.log('FAILED'); process.exit(1); }
  console.log('errors:', errs); await b.close();
})();
