// Step-1 extras (owner feedback, 4 Oct 2026): tap the '?' badge to approve a questioned tile (stored in `checked`,
// nothing taken out); a HOLD on a tile opens the larger view with the enlarged tile and takes nothing out (owner rule R05,
// template 2026-10-09.5: the old tap switch is gone, and a stored 'sorterTapMode' changes nothing: a tap still takes out); a tile
// dragged up from the tray onto a pile lands in that pile.
// Run: PW_EXE=/opt/pw-browsers/chromium NODE_PATH=$(npm root -g) node test_s1_extras.js PAGE.html SHOT.png
const { chromium } = require('playwright'); const mock = require('./mock_db');
(async () => {
  const browser = await chromium.launch({ executablePath: process.env.PW_EXE || undefined });
  const ctx = await browser.newContext({ viewport: { width: 1200, height: 900 } }); const store = await mock.install(ctx);
  await ctx.addInitScript(() => { try { localStorage.setItem('sorterTapMode', 'look'); } catch (e) {} });   // a setting an older page left behind
  const page = await ctx.newPage();
  const errs = []; page.on('pageerror', e => errs.push(e.message));
  await page.goto('file://' + process.argv[2]); await page.waitForTimeout(1000);
  const res = {};
  // 1. approve a questioned tile
  const q = page.locator('.t.fq .badge').first();
  if (await q.count()){ const sid = await q.evaluate(g => g.parentElement.dataset.sid);
    await q.click(); await page.waitForTimeout(300);
    res.approve = await page.evaluate(s => !!checked[s] && !moves[s], sid);
  } else res.approve = 'no questioned tile in fixture';
  // 2. a hold shows it large (no switch on the page; an old stored 'look' setting is ignored: a tap still takes out)
  res.noSwitch = (await page.locator('#modeLook').count()) === 0;
  const t = page.locator('#list .t').first(); const tsid = await t.getAttribute('data-sid');
  await mock.hold(page, t); await page.waitForTimeout(150);
  res.look = !(await page.locator('#ctx').isHidden()) && (await page.evaluate(s => !moves[s], tsid)) && (await page.getAttribute('#ctxBig', 'src') || '').length > 20;
  await page.click('#ctxX');
  const t1 = page.locator('#list .t').nth(1); const t1s = await t1.getAttribute('data-sid'); await t1.click(); await page.waitForTimeout(300);
  res.tapOut = (await page.locator('#ctx').isHidden()) && (await page.evaluate(s => moves[s] === 'OUT', t1s));
  await page.evaluate(() => undo()); await page.waitForTimeout(200);
  // 3. drag from tray onto a pile
  const t2 = page.locator('#list .t').nth(2); const sid2 = await t2.getAttribute('data-sid'); await t2.click(); await page.waitForTimeout(300);
  const target = await page.evaluate(s => { const ps = [...document.querySelectorAll('.pile[data-pile]')].filter(p => p.dataset.pile !== homeOf[s]); const p = ps[0]; p.scrollIntoView({block: 'center'}); return p.dataset.pile; }, sid2);
  await page.waitForTimeout(200);
  const tb = await page.locator('#trayTiles .t[data-sid="' + sid2 + '"]').boundingBox();
  const pb = await page.locator('.pile[data-pile="' + target + '"]').boundingBox();
  await page.mouse.move(tb.x + tb.width / 2, tb.y + tb.height / 2); await page.mouse.down();
  for (let i = 1; i <= 12; i++) await page.mouse.move(tb.x + tb.width / 2, tb.y + tb.height / 2 + (pb.y + 20 - tb.y - tb.height / 2) * i / 12);
  await page.waitForTimeout(50);
  const pb2 = await page.locator('.pile[data-pile="' + target + '"]').boundingBox();
  await page.mouse.move(pb2.x + 40, pb2.y + 20); await page.mouse.up(); await page.waitForTimeout(400);
  res.drag = await page.evaluate(([s, p]) => moves[s] === p, [sid2, target]);
  await page.screenshot({ path: process.argv[3] });
  console.log(res); console.log('errors:', errs);
  const okay = (res.approve === true || typeof res.approve === 'string') && res.noSwitch && res.look && res.tapOut && res.drag && !errs.length;
  console.log(okay ? 'ALL PASS' : 'FAILED'); await browser.close(); process.exit(okay ? 0 : 1);
})().catch(e => { console.error(e); process.exit(1); });
