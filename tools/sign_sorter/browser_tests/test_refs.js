// --refs (BIR87-SORTER, 4 Oct 2026; made correctable at the owner's ask, 4 Oct 2026 "give me a way to fix, I might make
// mistakes"): tiles the person sorted on an earlier page show a green check as their earlier picks, but they move like any
// tile -- a tap takes one out (a stored move), Undo puts it back, the larger view offers the move controls, and step 2 shows
// the person's earlier picks first on each card.
// Run: PW_EXE=/opt/pw-browsers/chromium NODE_PATH=$(npm root -g) node test_refs.js refs.html SHOT.png
const { chromium } = require('playwright'); const mock = require('./mock_db');
(async () => {
  const browser = await chromium.launch({ executablePath: process.env.PW_EXE || undefined });
  const ctx = await browser.newContext({ viewport: { width: 1200, height: 900 } }); const store = await mock.install(ctx); const page = await ctx.newPage();
  const errs = []; page.on('pageerror', e => errs.push(e.message));
  await page.goto('file://' + process.argv[2]); await page.waitForTimeout(1000);
  const nref = await page.locator('.tiles .t.ref').count();
  // the larger view of an earlier pick offers the move controls
  await page.evaluate(() => showCtx('p1_01', 'X')); await page.waitForTimeout(200);
  const controls = await page.evaluate(() => !$('ctxDest').hidden && !$('ctxBad').hidden && !$('ctxOut').hidden);
  await page.click('#ctxClose');
  // a tap takes an earlier pick out, and the move is stored
  await page.locator('.tiles .t.ref[data-sid="p1_01"]').click(); await page.waitForTimeout(800);
  const outRef = (await page.evaluate(() => moves['p1_01'])) === 'OUT' && ((store.docs.moves || {})['p1_01'] || {}).to === 'OUT';
  const trayHas = await page.locator('#trayTiles [data-sid="p1_01"], #tray [data-sid="p1_01"]').count() > 0;
  // Undo puts it back where it was, still marked as an earlier pick
  await page.click('#undo'); await page.waitForTimeout(800);
  const back = !(await page.evaluate(() => moves['p1_01'])) && (await page.locator('.tiles .t.ref[data-sid="p1_01"]').count()) === 1;
  // a normal tile still taps out; step 2 shows the earlier picks first on the card
  await page.locator('#pile__88_ .tiles .t:not(.ref)').first().click(); await page.waitForTimeout(800);
  await page.click('#trayGo'); await page.waitForTimeout(800);
  const firstX = await page.locator('.card[data-pile="X"] .smp img').first().getAttribute('src');
  const okFirst = [await page.evaluate(() => imgSrc('p1_01')), await page.evaluate(() => imgSrc('p1_07'))].includes(firstX);
  await page.screenshot({ path: process.argv[3] });
  console.log({ nref, controls, outRef, trayHas, back, okFirst });
  const okay = nref === 3 && controls && outRef && trayHas && back && okFirst && !errs.length;
  console.log('errors:', errs); console.log(okay ? 'ALL PASS' : 'FAILED'); await browser.close(); process.exit(okay ? 0 : 1);
})().catch(e => { console.error(e); process.exit(1); });
