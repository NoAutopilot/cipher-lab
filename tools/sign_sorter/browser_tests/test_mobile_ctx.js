const { chromium } = require('playwright');
// Phone-width check (3 Oct 2026, owner report): the context dialog's Close stays on screen, the canvas fits the width,
// and Next from a 'Check these first' tile steps through that list, not the tile's whole pile. Usage: node test_mobile_ctx.js PAGE.html OUT.png
(async () => { const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await b.newPage({viewport:{width:390,height:760}, isMobile:true, hasTouch:true});
  const errs = []; page.on('pageerror', e => errs.push(e.message)); await page.addInitScript(() => { window.claude = { use: async () => null }; });
  await page.goto('file://' + process.argv[2]); await page.waitForTimeout(800);
  await page.locator('#focusTiles .t').first().click(); await page.waitForTimeout(300);
  console.log(await page.textContent('#ctxT'), '|', await page.textContent('#ctxPos'));
  const bb = await page.locator('#ctxX').boundingBox(); console.log('close box', JSON.stringify(bb));
  await page.screenshot({ path: process.argv[3] });
  await page.click('#ctxNext'); console.log(await page.textContent('#ctxT'), '|', await page.textContent('#ctxPos'));
  await page.evaluate(() => document.querySelector('#ctx .box').scrollTop = 2000); await page.waitForTimeout(100);
  console.log('close still visible', JSON.stringify(await page.locator('#ctxX').boundingBox()));
  await page.click('#ctxX'); console.log('hidden after close', await page.locator('#ctx').isHidden());
  console.log('errors:', errs); await b.close(); })();
