// Owner rows R12-R16 (tools/data/sorter_owner_requirements.tsv; SORTER-FIX-R12-R16, 15 Oct 2026), on a built page:
//   node test_r12_r16.js PAGE.html [SHOT_PREFIX] [--expect-old]
// R16: step 2's question card has no "Fix the cut" (#s2Fix) and keeps "Bad cut". R12: a cut saved from a sign's card (step 1 pile
// tile, and a waiting question tile opened from the tray) leaves the tile rendered from the saved box, in its pile (or still waiting
// in step 2), and placeable: it is then moved into another pile and the move is saved. Reproduction (--expect-old, on a page built
// before template 2026-10-15.1, e.g. the committed f.191r packet): step 2's Fix the cut -> Save cut answers the question "kept in its
// home pile" without a move, so the sign leaves step 2 and is never placed -- the test passes when it sees that defect.
// R15 / R13 (pages with DATA.queue, tools/sign_sorter.py --piles-from): the waiting box is never drawn as a pile, never a step-2 card or
// a "Move this tile to" target, no keep for it; no question tile inside a pile; a pile with a note shows it.
const { chromium } = require('playwright'); const mock = require('./mock_db');
const PAGE = process.argv[2], SHOT = process.argv[3] && !process.argv[3].startsWith('--') ? process.argv[3] : '/tmp/test_r12_r16';
const OLD = process.argv.includes('--expect-old');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_EXE || '/opt/pw-browsers/chromium' }); const res = []; const errs = [];
  const ok = (name, cond, extra) => { res.push([name, !!cond]); console.log((cond ? 'ok   ' : 'FAIL ') + name, extra === undefined ? '' : JSON.stringify(extra)); };
  const open = async (vp) => { const ctx = await b.newContext(vp); const store = await mock.install(ctx); const page = await ctx.newPage();
    page.on('pageerror', e => errs.push(e.message)); await page.goto('file://' + PAGE); await page.waitForTimeout(1800); return { ctx, store, page }; };
  const nudgeSave = async page => { for (let i = 0; i < 3; i++) await page.click('#fixRp'); await page.click('#fixSave'); await page.waitForTimeout(900); };
  if (OLD) {   // the reproduction: the defect must be there on an old page
    const { ctx, store, page } = await open({ viewport: { width: 1200, height: 900 } });
    const sid = await page.evaluate(() => s2Cur);
    ok('old page: step 2 has Fix the cut', await page.locator('#s2Fix').count() === 1);
    await page.click('#s2Fix'); await page.waitForTimeout(300); await nudgeSave(page);
    if (await page.isVisible('#ctxClose')) await page.click('#ctxClose');
    const st = await page.evaluate(s => ({ where: where(s), move: moves[s] || null, checked: checked[s] || null, home: homeOf[s], waiting: outList().includes(s) }), sid);
    ok('old page: REPRODUCED -- after Save cut the question left step 2 unplaced (kept in its home pile, no move)',
      !st.waiting && !st.move && st.checked === st.home && !!(store.docs.recuts || {})[sid], { sid, ...st });
    await page.screenshot({ path: SHOT + '_old.png' }); await ctx.close();
  } else {
    // ---- R16: no Fix the cut on the question card; Bad cut stays
    for (const vp of [{ viewport: { width: 1200, height: 900 } }, { viewport: { width: 390, height: 760 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 }]) {
      const { ctx, page } = await open(vp); const w = vp.viewport.width;
      ok(`R16 (${w}px): no "Fix the cut" on the question card`, (await page.locator('#s2Fix').count()) === 0 &&
        !(await page.locator('#s2Acts').innerText()).includes('Fix the cut'));
      ok(`R16 (${w}px): "Bad cut" on the question card`, await page.locator('#s2Bad').isVisible());
      await ctx.close();
    }
    // ---- R12 (step 1): a pile tile recut stays rendered, in its pile, and is placeable
    {
      const { ctx, store, page } = await open({ viewport: { width: 1200, height: 900 } });
      await page.evaluate(() => setStep(1)); await page.waitForTimeout(400);
      const t = page.locator('#list .pile .tiles .t:not(.wait)').first(); const sid = await t.getAttribute('data-sid');
      const pid = await page.evaluate(s => pileOf(s), sid); const src0 = await t.locator('img').getAttribute('src');
      await mock.hold(page, t); await page.click('#ctxFix'); await page.waitForTimeout(200); await nudgeSave(page); await page.click('#ctxClose'); await page.waitForTimeout(400);
      const t2 = page.locator('#list .pile .tiles .t[data-sid="' + sid + '"]');
      ok('R12 step 1: recut saved', !!(store.docs.recuts || {})[sid]);
      ok('R12 step 1: tile still rendered once, in its pile, visible', (await t2.count()) === 1 && await t2.isVisible() &&
        (await t2.evaluate(e => e.closest('.pile').dataset.pile)) === pid, { sid, pid });
      ok('R12 step 1: re-rendered from the saved box', (await t2.locator('img').getAttribute('src')) !== src0);
      await t2.click(); await page.waitForTimeout(500);   // a tap: into the tray
      const other = await page.evaluate(s => allPiles().map(p => p.id).find(p => p !== pileOf(s) && !SPECIAL.has(p) && !QUEUE.has(p) && membersOf(p).length), sid);
      await page.evaluate(() => setStep(2)); await page.waitForTimeout(300);
      await page.evaluate(s => { s2Cur = s; renderS2(); }, sid); await page.waitForTimeout(400);
      await page.locator('#cards .card[data-pile="' + other + '"]').click(); await page.waitForTimeout(900);
      ok('R12 step 1: then placed in another pile (move saved)', (store.docs.moves || {})[Object.keys(store.docs.moves || {}).find(k => (store.docs.moves[k] || {}).sid === sid) || ''] !== undefined
        || await page.evaluate((a) => moves[a[0]] === a[1], [sid, other]), { sid, other, move: await page.evaluate(s => moves[s], sid) });
      await ctx.close();
    }
    // ---- R12 (a waiting question): recut from its card in the tray, it stays waiting and is then placed
    for (const vp of [{ viewport: { width: 1200, height: 900 } }, { viewport: { width: 390, height: 760 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 }]) {
      const { ctx, store, page } = await open(vp); const w = vp.viewport.width;
      const sid = await page.evaluate(() => outList()[0]);
      const tt = page.locator('#trayTiles .t[data-sid="' + sid + '"]');
      if (!(await tt.count())) { ok(`R12 question (${w}px): a question waits in the tray`, false, { sid }); await ctx.close(); continue; }
      await page.evaluate(() => setStep(1)); await page.waitForTimeout(300);
      await tt.scrollIntoViewIfNeeded(); await mock.hold(page, tt); await page.waitForTimeout(200);
      await page.click('#ctxFix'); await page.waitForTimeout(200); await nudgeSave(page);
      await page.click('#ctxClose'); await page.waitForTimeout(400);
      const st = await page.evaluate(s => ({ where: where(s), move: moves[s] || null, checked: checked[s] || null, waiting: outList().includes(s), rc: !!recutImg[s] }), sid);
      ok(`R12 question (${w}px): recut saved, still waiting, not answered`, !!(store.docs.recuts || {})[sid] && st.waiting && !st.move && !st.checked, { sid, ...st });
      ok(`R12 question (${w}px): shown in the tray from the saved box`, (await page.locator('#trayTiles .t[data-sid="' + sid + '"]').count()) === 1 &&
        (await page.locator('#trayTiles .t[data-sid="' + sid + '"] img').getAttribute('src')) === await page.evaluate(s => recutImg[s], sid));
      await page.evaluate(() => setStep(2)); await page.waitForTimeout(300); await page.evaluate(s => { s2Cur = s; renderS2(); }, sid); await page.waitForTimeout(500);
      const card = page.locator('#cards .card').first(); const to = await card.getAttribute('data-pile');
      if (w < 500) await card.tap(); else await card.click(); await page.waitForTimeout(900);
      ok(`R12 question (${w}px): placeable after the recut (moved to ${to})`, await page.evaluate(a => moves[a[0]] === a[1] || checked[a[0]] === a[1], [sid, to]) &&
        !(await page.evaluate(s => outList().includes(s), sid)));
      await page.screenshot({ path: `${SHOT}_q${w}.png` }); await ctx.close();
    }
    // ---- R15 / R13: queue pages
    {
      const { ctx, page } = await open({ viewport: { width: 1200, height: 900 } });
      const q = await page.evaluate(() => [...QUEUE]);
      if (q.length) {
        await page.evaluate(() => setStep(1)); await page.waitForTimeout(400);
        ok('R15: the waiting box is not drawn as a pile', await page.evaluate(qq => qq.every(id => !document.getElementById('pile_' + domKey(id))), q));
        const qs = await page.evaluate(() => Object.keys(trayOrder));
        ok('R15: no waiting tile inside any pile', await page.evaluate(ss => ss.every(s => !document.querySelector('#list .pile .t[data-sid="' + s + '"]')), qs), { n: qs.length });
        const notes = await page.evaluate(() => DATA.piles.filter(p => p.note && !QUEUE.has(p.id)).map(p => [p.id, !!document.querySelector('#pile_' + domKey(p.id) + ' .pnote')]));
        ok('R15: every same-letter note is shown on its pile', notes.every(x => x[1]), { n: notes.length });
        await page.evaluate(() => setStep(2)); await page.waitForTimeout(400);
        ok('R15: the waiting box is not a step-2 card', await page.evaluate(qq => qq.every(id => !document.querySelector('#cards .card[data-pile="' + id + '"]')), q));
        ok('R15: no "keep it in the waiting box" answer', await page.locator('#s2Home').isHidden());
        await mock.hold(page, page.locator('#s2Tile')); await page.waitForTimeout(300);
        ok('R15: the card offers no keep and no move into the waiting box', await page.locator('#ctxKeep').isHidden() &&
          await page.evaluate(qq => ![...document.querySelectorAll('#ctxDest option')].some(o => qq.includes(o.value)), q));
      } else ok('R15: no queue on this page (built without --piles-from): queue checks n/a', true);
      await ctx.close();
    }
  }
  ok('no page errors', errs.length === 0, errs.slice(0, 3));
  console.log('errors:', errs); await b.close();
  const f = res.filter(r => !r[1]).length; console.log(f ? `${f} FAILED` : 'ALL PASS'); process.exit(f ? 1 : 0);
})();
