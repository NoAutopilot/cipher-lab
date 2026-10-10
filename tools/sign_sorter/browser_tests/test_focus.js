// "Check these first" box (desktop): its tiles open the card on a HOLD (owner rule R05, template 2026-10-09.5; a tap takes the sign
// out to the tray like a tap in a pile). Run: PW_EXE=... NODE_PATH=$(npm root -g) node test_focus.js PAGE.html SHOT.png
const { chromium } = require('playwright'); const mock = require('./mock_db');
(async () => { const b = await chromium.launch({ executablePath: process.env.PW_EXE }); const page = await b.newPage({viewport:{width:1200,height:900}});
  const errs = []; page.on('pageerror', e => errs.push(e.message)); await page.addInitScript(() => { window.claude = { use: async () => null }; });
  await page.goto('file://' + process.argv[2]); await page.waitForTimeout(400);
  console.log('focus tiles:', await page.locator('#focusTiles .t').count());
  await mock.hold(page, page.locator('#focusTiles .t').first()); console.log('ctx:', await page.textContent('#ctxT'), '| moves:', await page.evaluate(() => JSON.stringify(moves)));
  await page.click('#ctxClose'); await page.screenshot({ path: process.argv[3] }); console.log('errors:', errs); await b.close(); })();
