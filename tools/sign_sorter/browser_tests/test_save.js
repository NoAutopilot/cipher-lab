// Save state machine of the sign sorter (template 2026-10-20.1, SORTER-SAVEFIX, 20 Oct 2026: the owner's Vivonne sort was mostly
// lost -- refused writes were dropped after one retry and shown only in a small grey line; a page that fell back to "this browser
// only" never handed its choices to storage). Drives plain.html against mock_db.js, desktop; PASS/FAIL per check, exit 1 on any FAIL.
// Covers: connecting (banner says wait, taps move nothing) -> held -> pumped (write, read-back, "All changes saved"); a refused write
// stays visible as "NOT saved" with a retry button and lands by itself; a write the read-back cannot find is not counted as saved;
// at most two writes in flight; this-browser-only mode is labelled, journaled, and offered back by "Recover my sort from this
// browser" on the next connected load (also from an older page's 'sorter:all' copy and from a journal of refused writes), written
// only on confirm, never over a stored document unless ticked.
// Run: NODE_PATH=$(npm root -g) node test_save.js PAGE.html
const { chromium } = require('playwright'); const mock = require('./mock_db');
const PAGE = 'file://' + process.argv[2];
let fails = 0; const ok = (name, cond, extra) => { console.log((cond ? 'PASS ' : 'FAIL ') + name + (extra !== undefined ? '  [' + extra + ']' : '')); if (!cond) fails++; };
const DESK = { viewport: { width: 1280, height: 900 } };
const ban = page => page.evaluate(() => { const b = document.getElementById('saveBan'); return { cls: b.className, t: b.textContent }; });
const tiles = page => page.locator('#list .t:not(.ref)');
const waitSaved = page => page.waitForFunction(() => /All changes saved/.test(document.getElementById('saveBan').textContent), null, { timeout: 15000 }).then(() => true, () => false);
async function open(ctx, opts, wait = true) { const page = await ctx.newPage(); const errs = []; page.on('pageerror', e => errs.push(e.message));
  await page.goto(PAGE); if (wait) await page.waitForTimeout((opts.connectMs || 600) + 600); return { page, errs }; }

(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_EXE || undefined });
  // 1. connecting -> held -> pumped -> saved after read-back
  { const ctx = await b.newContext(DESK); const store = await mock.install(ctx, { connectMs: 2000 }); const { page, errs } = await open(ctx, {}, false);
    await page.waitForTimeout(300); const b0 = await ban(page);
    ok('connecting: the banner says wait before you start', /wait/i.test(b0.t) && / wait/.test(b0.cls), b0.t);
    await tiles(page).first().click(); await page.waitForTimeout(100);
    ok('connecting: a tap moves nothing and writes nothing', !Object.keys(store.docs.moves || {}).length && await page.evaluate(() => !Object.keys(moves).length));
    await page.waitForTimeout(2600);
    const s0 = await tiles(page).first().getAttribute('data-sid'); await tiles(page).first().click();
    const b1 = await ban(page);
    ok('pumped: right after a tap the banner says NOT saved yet', /1 change NOT saved/.test(b1.t), b1.t);
    ok('pumped: "All changes saved" after the read-back', await waitSaved(page), (await ban(page)).t);
    ok('pumped: the move is in storage', (store.docs.moves || {})[s0] && store.docs.moves[s0].to === 'OUT', JSON.stringify(store.docs.moves));
    ok('no page errors', !errs.length, errs.join(' | ')); await ctx.close(); }
  // 2. refused -> visible -> lands by itself
  { const ctx = await b.newContext(DESK); const store = await mock.install(ctx, {}); const { page } = await open(ctx, {});
    store.failNext(2); await tiles(page).first().click(); await page.waitForTimeout(1600);
    const b1 = await ban(page);
    ok('refused: the banner says NOT saved, high contrast, with a retry button', /NOT saved/.test(b1.t) && / bad/.test(b1.cls) && await page.isVisible('#banRetry'), b1.cls + ' ' + b1.t);
    const j = await page.evaluate(() => JSON.parse(localStorage.getItem('sorter:journal')));
    ok('refused: the change is journaled in this browser with its path pending', j && j.pending.length === 1 && Object.keys(j.moves).length === 1, JSON.stringify(j && j.pending));
    ok('refused: it lands by itself (no click) and the banner says so', await waitSaved(page) && Object.keys(store.docs.moves || {}).length === 1, (await ban(page)).t);
    await ctx.close(); }
  // 3. a write the read-back cannot find is not "saved"
  { const ctx = await b.newContext(DESK); const store = await mock.install(ctx, {}); const { page } = await open(ctx, {});
    store.lie(1); await tiles(page).first().click(); await page.waitForTimeout(250);
    const b1 = await ban(page); ok('read-back: an unconfirmed write is not shown as saved', !/All changes saved/.test(b1.t), b1.t);
    ok('read-back: confirmed on the next read, then saved', await waitSaved(page)); await ctx.close(); }
  // 4. a burst of taps: never more than two writes in flight, all land
  { const ctx = await b.newContext(DESK); const store = await mock.install(ctx, { minMs: 200, maxMs: 400 }); const { page } = await open(ctx, {});
    await page.evaluate(() => { window.__max = 0; setInterval(() => { window.__max = Math.max(window.__max, wactive); }, 5); });
    const n = Math.min(8, await tiles(page).count()); const sids = [];
    for (let i = 0; i < n; i++){ const t = page.locator('#list .t:not(.ref):not(.out)').first(); sids.push(await t.getAttribute('data-sid')); await t.click(); await page.waitForTimeout(40); }
    ok('burst: all ' + n + ' land and the banner says saved', await waitSaved(page) && Object.keys(store.docs.moves || {}).length === n, Object.keys(store.docs.moves || {}).length);
    const mx = await page.evaluate(() => window.__max); ok('burst: at most two writes in flight', mx <= 2 && mx >= 1, mx); await ctx.close(); }
  // 5. this-browser-only mode: labelled; journaled; recovered on the next connected load, on confirm only
  { const ctx = await b.newContext(DESK); const store = await mock.install(ctx, { nullDb: true }); let { page } = await open(ctx, {});
    const b1 = await ban(page); ok('local: the banner says storage is not connected, in this browser only', /not connected/.test(b1.t) && / bad/.test(b1.cls), b1.t);
    const s0 = await tiles(page).first().getAttribute('data-sid'); await tiles(page).first().click(); await page.waitForTimeout(200);
    const s1 = await page.locator('#list .t:not(.ref):not(.out)').first().getAttribute('data-sid'); await page.locator('#list .t:not(.ref):not(.out)').first().click(); await page.waitForTimeout(200);
    await page.close();
    // the store comes back (same browser profile, same origin): a second context would lose localStorage, so re-install on this one
    store.nullDb = false; const store2 = store; ({ page } = await open(ctx, {}));
    ok('recover: the box is offered', await page.isVisible('#recGo'), await page.textContent('#recover'));
    ok('recover: nothing is written before the confirm', !Object.keys(store2.docs.moves || {}).length);
    await page.click('#recGo'); await page.waitForTimeout(100);
    const shown = await page.locator('#recList .t').count();
    ok('recover: it shows the recovered piles with their signs', shown === 2 && /Taken out/.test(await page.textContent('#recList')), shown);
    await page.click('#recYes');
    ok('recover: on confirm both moves reach storage and are read back', await waitSaved(page) && store2.docs.moves && store2.docs.moves[s0] && store2.docs.moves[s1], JSON.stringify(store2.docs.moves));
    ok('recover: the page shows them where they were left', await page.evaluate(([a, c]) => moves[a] === 'OUT' && moves[c] === 'OUT', [s0, s1]));
    await page.reload(); await page.waitForTimeout(1400);
    ok('recover: not offered again once recovered', !(await page.isVisible('#recGo')));
    await ctx.close(); }
  // 6. an older page's 'sorter:all' copy; a stored document that differs is shown apart and kept unless ticked
  { const ctx = await b.newContext(DESK); const store = await mock.install(ctx, {});
    const pg = await ctx.newPage(); await pg.goto(PAGE); await pg.waitForTimeout(1300);
    const [a, c] = await pg.evaluate(() => Object.keys(itemBySid).slice(0, 2)); const home = await pg.evaluate(c => homeOf[c], c);
    store.docs.moves = { [c]: { sid: c, from: home, to: 'ASIDE', updated: '2026-10-20T00:00:00Z' } };
    await pg.evaluate(([a, c]) => localStorage.setItem('sorter:all', JSON.stringify({ moves: { [a]: 'OUT', [c]: 'OUT' }, outAt: { [a]: 1 } })), [a, c]);
    await pg.reload(); await pg.waitForTimeout(1400);
    ok('legacy: an older page\'s copy is offered', await pg.isVisible('#recGo'));
    await pg.click('#recGo'); ok('legacy: the differing stored choice is offered apart, unticked', await pg.isVisible('#recOver') && !(await pg.isChecked('#recOver')));
    await pg.click('#recYes'); await waitSaved(pg);
    ok('legacy: the new choice is written, the stored one kept', store.docs.moves[a] && store.docs.moves[a].to === 'OUT' && store.docs.moves[c].to === 'ASIDE', JSON.stringify(store.docs.moves));
    ok('legacy: the older copy is kept under a recovered name, not deleted', await pg.evaluate(() => !localStorage.getItem('sorter:all') && Object.keys(localStorage).some(k => k.startsWith('sorter:all:recovered:'))));
    await ctx.close(); }
  // 7. refused writes, page closed before they landed: offered back on the next load
  { const ctx = await b.newContext(DESK); const store = await mock.install(ctx, {});
    let { page } = await open(ctx, {}); store.failNext(1000); const s0 = await tiles(page).first().getAttribute('data-sid'); await tiles(page).first().click(); await page.waitForTimeout(1500);
    await page.evaluate(() => { window.onbeforeunload = null; }); store.failNext(0);
    await page.close(); ({ page } = await open(ctx, {}));
    ok('pending: a refused write from the last visit is offered back', await page.isVisible('#recGo'));
    await page.click('#recGo'); await page.click('#recYes');
    ok('pending: written on confirm', await waitSaved(page) && store.docs.moves && store.docs.moves[s0] && store.docs.moves[s0].to === 'OUT', JSON.stringify(store.docs.moves));
    await ctx.close(); }
  // 8. "Save my sort": rewrites the arrangement, reads it back whole, says "Saved: N tiles in M piles at HH:MM"; a refusal says NOT saved
  { const ctx = await b.newContext(DESK); const store = await mock.install(ctx, {}); const { page } = await open(ctx, {});
    ok('save button: before the arrangement is saved, no result line', !(await page.isVisible('#saveAllMsg')));
    await tiles(page).first().click(); await waitSaved(page);
    await page.click('#saveAll'); await page.waitForFunction(() => !document.getElementById('saveAll').disabled, null, { timeout: 15000 });
    const m1 = await page.textContent('#saveAllMsg');
    const N = await page.evaluate(() => Object.keys(itemBySid).length);
    ok('save button: "Saved: N tiles in M piles at HH:MM"', new RegExp('Saved: ' + N + ' tiles in \\d+ piles at \\d\\d:\\d\\d').test(m1), m1);
    store.docs.moves = {};   // storage loses the move behind the page's back: Save must notice and rewrite it
    await page.click('#saveAll'); await page.waitForFunction(() => !document.getElementById('saveAll').disabled, null, { timeout: 15000 });
    ok('save button: rewrites a move storage lost, then says Saved', /Saved:/.test(await page.textContent('#saveAllMsg')) && Object.keys(store.docs.moves).length === 1, await page.textContent('#saveAllMsg'));
    store.failNext(1000); await page.click('#saveAll'); await page.waitForTimeout(2500);
    const m3 = await page.evaluate(() => ({ t: document.getElementById('saveAllMsg').textContent, c: document.getElementById('saveAllMsg').className }));
    ok('save button: a refusal is shown as NOT saved, in the high-contrast style', /NOT saved/.test(m3.t) && / bad/.test(m3.c), m3.c + ' ' + m3.t);
    store.failNext(0); await ctx.close(); }
  await b.close(); console.log(fails ? fails + ' FAILED' : 'ALL PASS'); process.exit(fails ? 1 : 0);
})();
