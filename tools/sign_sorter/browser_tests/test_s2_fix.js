// Withdrawn by template 2026-10-15.1 (owner rows R12, R16, 15 Oct 2026; this file now checks the withdrawal and the card's own Fix the
// cut on a waiting sign -- see the first block below; tools/sign_sorter/browser_tests/test_r12_r16.js checks R12-R16 on any page).
// Was: Step 2's "Fix the cut" (template 2026-10-09.6; owner, 10 Oct 2026, on a box-check page: "im not seeing fix the cut ... on this
// page"; four pages were hand-patched the same day by the scratch s2fix_patch.py, whose test this ports). The button is the first in
// #s2Acts and opens the card for the sign being placed with the box editor on (Save cut and Split showing). For a question waiting in
// step 2: "Save cut" or "Split" there saves the cut, checks the box (kept in its pile, a keep) and brings up the next one; Close, Esc and
// Cancel-then-Close change nothing; "It was right" still checks a box as it is; Undo takes the keep back first (the sign waits again),
// then the cut. For a sign taken out in step 1 (no question): Save cut saves the cut and the sign stays waiting for its pile (a fixed
// cut does not say where it belongs). It also works when the page has no Split button. iPhone 13 (taps) and a desktop mouse.
// Also the box-check key (tools/sign_sorter.py --key box): shown under the lede only on a page built with it, its fold kept per browser.
// Also (adversarial check, 11 Oct 2026): on a line with neighbour line crops (region.html, line-strip view) the editor's view survives the
// card's own plain draw that was waiting for those images; the key names "Lines above and below" only on a page that has them.
// Must NOT: move or keep anything on Close / Cancel; put a taken-out sign back in a pile because its cut was fixed; show a key on a page
// built without --key.
// Usage: PW_EXE=/opt/pw-browsers/chromium NODE_PATH=$(npm root -g) node test_s2_fix.js FIXTURE_DIR   (tray.html, plain.html, tray_key.html, region.html there:
// make_fixtures.py)
const { chromium, devices } = require('playwright'); const mock = require('./mock_db'); const path = require('path');
const DIR = path.resolve(process.argv[2]);
let fails = 0; const errs = [];
const ok = (c, m, x) => { console.log((c ? 'ok   ' : 'FAIL ') + m + (x !== undefined ? '  [' + x + ']' : '')); if (!c) fails++; };

(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_EXE || '/opt/pw-browsers/chromium' });
  const prof = d => { const o = { ...devices[d] }; delete o.defaultBrowserType; return o; };
  for (const [name, opts] of [['iPhone 13', prof('iPhone 13')], ['desktop', { viewport: { width: 1400, height: 900 } }]]) {
    const touch = name !== 'desktop';
    // ---- a page whose questions wait in step 2 (tray.html). Template 2026-10-15.1 (owner rows R12, R16, 15 Oct 2026): the question card
    // has no "Fix the cut" any more; "Bad cut" is its only box answer. The sign's own card (a hold on the big sign) still fixes a cut, and
    // a saved cut answers nothing: the question keeps waiting, with its new cut, until the person places it.
    let ctx = await b.newContext(opts); await mock.install(ctx); let p = await ctx.newPage(); p.on('pageerror', e => errs.push(name + ': ' + e.message));
    await p.goto('file://' + path.join(DIR, 'tray.html')); await p.waitForFunction(() => typeof ready !== 'undefined' && ready && step === 2 && s2Cur, null, { timeout: 30000 });
    await p.waitForTimeout(500);
    const tap = async sel => { await p.locator(sel).scrollIntoViewIfNeeded(); if (touch) await p.tap(sel); else await p.click(sel); await p.waitForTimeout(350); };
    const S = () => p.evaluate(() => ({ n: outList().length, cur: s2Cur, ctx: !document.getElementById('ctx').hidden, fix: !!fix,
      moves: JSON.stringify(moves), checked: JSON.stringify(checked), recuts: Object.keys(recuts).sort().join(',') }));
    ok((await p.locator('#s2Fix').count()) === 0 && !(await p.locator('#s2Acts').innerText()).includes('Fix the cut') && await p.locator('#s2Bad').isVisible(),
      `${name}: R16 -- the question card has no "Fix the cut"; "Bad cut" is there`);
    let a0 = await S(); const sid1 = a0.cur;
    await mock.hold(p, p.locator('#s2Tile')); await p.waitForTimeout(300);
    ok(await p.locator('#ctxFix').isVisible(), `${name}: a hold on the big sign opens its card, with Fix the cut`);
    await tap('#ctxFix'); for (let i = 0; i < 2; i++) await tap('#fixRm'); await tap('#fixSave'); let a = await S();
    ok(a.recuts.includes(sid1) && a.n === a0.n && a.moves === a0.moves && a.checked === a0.checked,
      `${name}: R12 -- Save cut in the card saves the cut and answers nothing: the question still waits`, JSON.stringify(a));
    await tap('#ctxClose'); a = await S();
    ok(!a.ctx && a.cur === sid1 && a.n === a0.n, `${name}: after Close the same question is still up in step 2`, JSON.stringify(a));
    await tap('#cards .card >> nth=1'); a = await S();
    ok(a.n === a0.n - 1 && (a.moves !== a0.moves || a.checked !== a0.checked), `${name}: R12 -- and it is placeable: a tap on a card answers it`, JSON.stringify(a));
    a0 = await S(); await mock.hold(p, p.locator('#s2Tile')); await p.waitForTimeout(300); await tap('#ctxFix'); await tap('#fixRm'); await tap('#fixCancel'); await tap('#ctxClose'); a = await S();
    ok(a.recuts === a0.recuts && a.moves === a0.moves && a.checked === a0.checked && a.n === a0.n, `${name}: Cancel then Close changes nothing`);
    await ctx.close();
    // ---- a sign taken out in step 1 (plain.html: no questions in the tray): a cut saved from its card leaves it waiting for its pile
    ctx = await b.newContext(opts); await mock.install(ctx); p = await ctx.newPage(); p.on('pageerror', e => errs.push(name + ' (plain): ' + e.message));
    await p.goto('file://' + path.join(DIR, 'plain.html')); await p.waitForFunction(() => typeof ready !== 'undefined' && ready, null, { timeout: 30000 });
    const sid3 = await p.evaluate(() => { const s = Object.keys(itemBySid).find(x => !trayOrder[x] && !itemBySid[x].r); takeOut(s, null); setStep(2); return s; });
    await p.waitForFunction(() => step === 2 && s2Cur && !document.getElementById('s2Work').hidden, null, { timeout: 30000 }); await p.waitForTimeout(400);
    const S2 = () => p.evaluate(s => ({ cur: s2Cur, ctx: !document.getElementById('ctx').hidden, mv: moves[s] || null, kept: checked[s] || null, recut: !!recuts[s] }), sid3);
    const tap2 = async sel => { await p.locator(sel).scrollIntoViewIfNeeded(); if (touch) await p.tap(sel); else await p.click(sel); await p.waitForTimeout(350); };
    await mock.hold(p, p.locator('#s2Tile')); await p.waitForTimeout(300); await tap2('#ctxFix'); await tap2('#fixRm'); await tap2('#fixSave'); await tap2('#ctxClose'); a = await S2();
    ok(!a.ctx && a.cur === sid3 && a.mv === 'OUT' && !a.kept && a.recut,
      `${name}: a sign taken out in step 1: Save cut in its card saves the cut and it stays waiting for its pile (not put back, not kept)`, JSON.stringify(a));
    await ctx.close();
    // ---- a page whose line crops have lines above and below (region.html in the line-strip view: r_L01-r_L03). Adversarial check, 11 Oct
    // 2026 (Luzerne box page): the card's plain draw, still waiting for the neighbour line images, ran after the editor's and repainted the
    // plain view under the editor, so a drag on the box saved a collapsed cut. The editor's view (no neighbour lines: map ha 0, hb 0) must
    // stay once the lines load. Since template 2026-10-15.1 the editor starts from the card's own Fix the cut, right after the hold.
    ctx = await b.newContext(opts); await mock.install(ctx); await ctx.addInitScript(() => { try { localStorage.setItem('sorterPageView', '0'); } catch (e) {} });
    p = await ctx.newPage(); p.on('pageerror', e => errs.push(name + ' (region): ' + e.message));
    await p.goto('file://' + path.join(DIR, 'region.html')); await p.waitForFunction(() => typeof ready !== 'undefined' && ready, null, { timeout: 30000 });
    const sid5 = await p.evaluate(() => { const s = Object.keys(itemBySid).find(x => itemBySid[x].p === 'r_L02' && !itemBySid[x].r); takeOut(s, null); setStep(2); return s; });
    await p.waitForFunction(() => step === 2 && s2Cur && !document.getElementById('s2Work').hidden, null, { timeout: 30000 }); await p.waitForTimeout(400);
    const nb5 = await p.evaluate(s => nbPages(itemBySid[s].p).filter(Boolean).length, sid5);
    await mock.hold(p, p.locator('#s2Tile')); if (touch) await p.tap('#ctxFix'); else await p.click('#ctxFix'); await p.waitForTimeout(1500);
    const v5 = await p.evaluate(() => { const c = document.getElementById('ctxC'), m = c._map || {}; return { fix: !!fix, view: c.dataset.view, ha: m.ha, hb: m.hb }; });
    ok(nb5 === 2 && v5.fix && v5.view === 'strip' && v5.ha === 0 && v5.hb === 0,
      `${name}: on a line with lines above and below (${sid5}), the card's Fix the cut keeps the editor's view once the neighbour lines load (no plain card drawn over it)`, JSON.stringify(v5));
    await ctx.close();
  }
  // the box-check key (OPTS.key = 'box', tools/sign_sorter.py --key box): shown under the lede on tray_key.html only, open the first
  // time, folded again after a reload once the person folds it (per browser, localStorage behind try/catch)
  { const ctx = await b.newContext(prof('iPhone 13')); await mock.install(ctx); const p = await ctx.newPage(); p.on('pageerror', e => errs.push('key: ' + e.message));
    await p.goto('file://' + path.join(DIR, 'tray.html')); await p.waitForTimeout(800);
    ok(!(await p.evaluate(() => !!document.getElementById('boxKey'))), 'iPhone 13: a page built without --key shows no key (the block is removed)');
    await p.goto('file://' + path.join(DIR, 'tray_key.html')); await p.waitForTimeout(800);
    const k = await p.evaluate(() => { const d = document.getElementById('boxKey'), l = document.querySelector('.lede'); return d ? { vis: !!d.offsetParent, open: d.open, rows: d.querySelectorAll('tr').length,
      after: l && l.nextElementSibling === d, h: Math.round(d.getBoundingClientRect().height), w: Math.round(d.scrollWidth), vw: innerWidth } : null; });
    ok(k && k.vis && k.open && k.rows === 8 && k.after && k.w <= k.vw, 'iPhone 13: --key box shows "What to do: a key" right under the lede, open, eight drawn cases, no sideways scroll', JSON.stringify(k));
    // its "Tick Lines above and below" names a box only cards with neighbour line crops have (adversarial check, 11 Oct 2026: Birago and
    // Vivonne never show it); this page's crops (p1, p2) have none, so the key does not name it; "Not sure" says what to do in step 2
    const k2 = await p.evaluate(() => { const d = document.getElementById('boxKey'); return { nb: /Lines above and below/.test(d.textContent), hasNb: Object.keys(DATA.pages).some(g => nbPages(g).some(Boolean)),
      skip: /In step 2: Skip/.test(d.textContent) }; });
    ok(!k2.hasNb && !k2.nb && k2.skip, 'iPhone 13: on a page with no neighbour line crops the key does not tell the person to tick "Lines above and below"; its "Not sure" row says Skip for step 2', JSON.stringify(k2));
    await p.locator('#boxKey > summary').tap(); await p.waitForTimeout(200); await p.reload(); await p.waitForTimeout(800);
    ok(await p.evaluate(() => { const d = document.getElementById('boxKey'); return !!d && !d.open && !!d.offsetParent; }), 'iPhone 13: folded, it stays folded after a reload');
    await ctx.close(); }
  ok(!errs.length, 'no page errors', errs.join(' | '));
  console.log('errors:', errs); console.log(fails ? fails + ' FAILED' : 'ALL PASS');
  await b.close(); process.exit(fails ? 1 : 0);
})();
