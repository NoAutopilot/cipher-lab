// --refs (BIR87-SORTER, 4 Oct 2026): tiles the person sorted on an earlier page are locked reference examples. A tap on one
// opens the larger view with no move controls and stores no move; a normal tile still taps out; step 2 shows the person's
// examples first on each card and they cannot be dragged to another pile.
// Run: PW_EXE=/opt/pw-browsers/chromium NODE_PATH=$(npm root -g) node test_refs.js refs.html SHOT.png
const { chromium } = require('playwright'); const mock = require('./mock_db');
(async () => {
  const browser = await chromium.launch({ executablePath: process.env.PW_EXE || undefined });
  const ctx = await browser.newContext({ viewport: { width: 1200, height: 900 } }); const store = await mock.install(ctx); const page = await ctx.newPage();
  const errs = []; page.on('pageerror', e => errs.push(e.message));
  await page.goto('file://' + process.argv[2]); await page.waitForTimeout(1000);
  const nref = await page.locator('.tiles .t.ref').count();
  const ref = page.locator('.tiles .t.ref[data-sid="p1_01"]');
  await ref.click(); await page.waitForTimeout(300);
  const ctxOpen = !(await page.evaluate(() => $('ctx').hidden));
  const hidden = await page.evaluate(() => ['ctxOut', 'ctxKeep', 'ctxDest', 'ctxAside', 'ctxBad', 'ctxNewB'].every(k => $(k).hidden));
  await page.click('#ctxClose');
  await page.evaluate(() => setDest('p1_01', 'Y'));          // even a direct call must not move a reference tile
  await page.locator('#pile__88_ .tiles .t:not(.ref)').first().click(); await page.waitForTimeout(800);
  const mv = store.docs.moves || {};
  const refMoved = await page.evaluate(() => ['p1_01', 'p1_07', 'p2_03'].some(s => moves[s])) || ['p1_01', 'p1_07', 'p2_03'].some(s => mv[s]);
  const outs = Object.values(mv).filter(m => m.to === 'OUT').length;
  await page.click('#trayGo'); await page.waitForTimeout(800);
  const firstX = await page.locator('.card[data-pile="X"] .smp img').first().getAttribute('src');
  const refSrc = await page.evaluate(() => imgSrc('p1_01'));
  const refSrc2 = await page.evaluate(() => imgSrc('p1_07'));
  const okFirst = firstX === refSrc || firstX === refSrc2;
  // stale-UI ctx check: a normal tile opened after a reference tile gets its move controls back
  await page.click('#tab1'); await page.waitForTimeout(300);
  await page.evaluate(() => showCtx('p1_01', 'X')); await page.evaluate(() => showCtx('p1_03', 'X'));
  const back = await page.evaluate(() => !$('ctxDest').hidden && !$('ctxBad').hidden);
  await page.screenshot({ path: process.argv[3] });
  console.log({ nref, ctxOpen, hidden, refMoved, outs, okFirst, back });
  const okay = nref === 3 && ctxOpen && hidden && !refMoved && outs === 1 && okFirst && back && !errs.length;
  console.log('errors:', errs); console.log(okay ? 'ALL PASS' : 'FAILED'); await browser.close(); process.exit(okay ? 0 : 1);
})().catch(e => { console.error(e); process.exit(1); });
