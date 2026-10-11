// Step 2's "Fix the cut" (template 2026-10-09.6; owner, 10 Oct 2026, on a box-check page: "im not seeing fix the cut ... on this
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
    // ---- a page whose questions wait in step 2 (tray.html: the box-check flow)
    let ctx = await b.newContext(opts); await mock.install(ctx); let p = await ctx.newPage(); p.on('pageerror', e => errs.push(name + ': ' + e.message));
    await p.goto('file://' + path.join(DIR, 'tray.html')); await p.waitForFunction(() => typeof ready !== 'undefined' && ready && step === 2 && s2Cur, null, { timeout: 30000 });
    await p.waitForTimeout(500);
    const tap = async sel => { await p.locator(sel).scrollIntoViewIfNeeded(); if (touch) await p.tap(sel); else await p.click(sel); await p.waitForTimeout(350); };
    const S = () => p.evaluate(() => ({ n: outList().length, cur: s2Cur, ctx: !document.getElementById('ctx').hidden, fix: !!fix, msg: document.getElementById('s2Msg').textContent,
      moves: JSON.stringify(moves), checked: JSON.stringify(checked), recuts: Object.keys(recuts).sort().join(','), added: Object.keys(added).sort().join(','),
      pos: document.getElementById('ctxPos').textContent }));
    ok(await p.evaluate(() => { const a = document.getElementById('s2Acts'); return a.firstElementChild && a.firstElementChild.id === 's2Fix'; }) && await p.locator('#s2Fix').isVisible(),
      `${name}: step 2 shows "Fix the cut", the first button under the sign`);
    let a0 = await S(); const sid1 = a0.cur, home1 = await p.evaluate(s => homeOf[s], sid1);
    await tap('#s2Fix'); let a = await S();
    ok(a.ctx && a.fix && await p.locator('#fixSave').isVisible() && await p.locator('#fixSplit').isVisible() && await p.evaluate(() => ctxSid) === sid1 && /waiting in step 2/.test(a.pos),
      `${name}: it opens the card on the sign being placed (${sid1}) with the box editor on, Save cut and Split showing`, a.pos);
    for (let i = 0; i < 3; i++) await tap('#fixRm');
    await tap('#fixSave'); a = await S();
    ok(!a.ctx && a.n === a0.n - 1 && a.cur !== sid1 && /Box checked/.test(a.msg) && JSON.parse(a.checked)[sid1] === home1 && a.recuts.split(',').includes(sid1),
      `${name}: Save cut saves the cut, closes the card, checks the box (kept in ${home1}) and brings up the next (${a0.n} -> ${a.n})`, a.msg);
    // Undo: the keep first (the sign waits again, shown), then the cut
    await tap('#undo'); let u = await S();
    ok(u.n === a0.n && u.cur === sid1 && !JSON.parse(u.checked)[sid1] && u.recuts.split(',').includes(sid1), `${name}: Undo takes the keep back first: ${sid1} waits again, its new cut kept`);
    await tap('#undo'); u = await S();
    ok(u.n === a0.n && !u.recuts.split(',').includes(sid1), `${name}: a second Undo takes the cut back`);
    // Split
    a0 = await S(); const sid2 = a0.cur;
    await tap('#s2Fix'); for (let i = 0; i < 6; i++) await tap('#fixRm');
    await tap('#fixSplit'); a = await S();
    ok(!a.ctx && a.n === a0.n - 1 && /Split/.test(a.msg) && /Box checked/.test(a.msg) && a.added.split(',').includes(sid2 + '+1') && JSON.parse(a.checked)[sid2],
      `${name}: Split saves the cut and the rest as a new box, closes the card, checks the box, next one (${a0.n} -> ${a.n})`, a.msg);
    // Close, Esc, Cancel then Close: nothing changes
    a0 = await S();
    await tap('#s2Fix'); for (let i = 0; i < 2; i++) await tap('#fixRm'); await tap('#ctxX'); a = await S();
    ok(!a.ctx && a.n === a0.n && a.cur === a0.cur && a.moves === a0.moves && a.checked === a0.checked && a.recuts === a0.recuts, `${name}: Close changes nothing`);
    if (!touch) { await tap('#s2Fix'); await p.keyboard.press('Escape'); await p.waitForTimeout(300); a = await S();
      ok(!a.ctx && a.n === a0.n && a.checked === a0.checked && a.recuts === a0.recuts, `${name}: Esc changes nothing`); }
    await tap('#s2Fix'); await tap('#fixRm'); await tap('#fixCancel'); a = await S();
    ok(a.ctx && !a.fix && a.recuts === a0.recuts, `${name}: Cancel stops editing (the card stays open, the cut unchanged)`);
    await tap('#ctxX'); a = await S();
    ok(!a.ctx && a.n === a0.n && a.cur === a0.cur && a.moves === a0.moves && a.checked === a0.checked && a.recuts === a0.recuts, `${name}: Cancel then Close changes nothing`);
    // a later card on the same sign (a hold on the big sign) is not step 2's Fix the cut: its Save does not check the box
    await p.evaluate(() => showCtx(s2Cur, pileOf(s2Cur), false, outList(), 'waiting to be placed')); await p.waitForTimeout(200);
    await tap('#ctxFix'); await tap('#fixRm'); await tap('#fixSave'); a = await S();
    ok(a.ctx && a.n === a0.n && a.checked === a0.checked, `${name}: Save in a card opened by a hold (not by step 2's button) saves the cut only: nothing checked, the card stays`);
    await tap('#ctxX'); await p.evaluate(() => undo()); await p.waitForTimeout(200);
    // "It was right" still checks a box as it is
    a0 = await S(); await tap('#s2Home'); a = await S();
    ok(a.n === a0.n - 1, `${name}: "It was right" still checks a box and moves on (${a0.n} -> ${a.n})`);
    await tap('#undo'); a = await S(); ok(a.n === a0.n && a.cur === a0.cur, `${name}: Undo brings it back`);
    // Save with the box as it was: the box is right as it is -- checked, no cut saved
    a0 = await S(); const sid4 = a0.cur; await tap('#s2Fix'); await tap('#fixSave'); a = await S();
    ok(!a.ctx && a.n === a0.n - 1 && /unchanged/.test(a.msg) && /Box checked/.test(a.msg) && a.recuts === a0.recuts && JSON.parse(a.checked)[sid4],
      `${name}: Save cut with the box unchanged checks the box as it is (no cut saved) and moves on`, a.msg);
    await tap('#undo');
    // no Split button on the page (a page built before 2026-10-09.4 had none): Save cut still checks the box
    await p.evaluate(() => document.getElementById('fixSplit').remove());
    a0 = await S(); await tap('#s2Fix'); await tap('#fixRm'); await tap('#fixSave'); a = await S();
    ok(!a.ctx && a.n === a0.n - 1 && /Box checked/.test(a.msg), `${name}: with no Split button, Save cut still checks the box and moves on`);
    await ctx.close();
    // ---- a sign taken out in step 1 (plain.html: no questions in the tray)
    ctx = await b.newContext(opts); await mock.install(ctx); p = await ctx.newPage(); p.on('pageerror', e => errs.push(name + ' (plain): ' + e.message));
    await p.goto('file://' + path.join(DIR, 'plain.html')); await p.waitForFunction(() => typeof ready !== 'undefined' && ready, null, { timeout: 30000 });
    const sid3 = await p.evaluate(() => { const s = Object.keys(itemBySid).find(x => !trayOrder[x] && !itemBySid[x].r); takeOut(s, null); setStep(2); return s; });
    await p.waitForFunction(() => step === 2 && s2Cur && !document.getElementById('s2Work').hidden, null, { timeout: 30000 }); await p.waitForTimeout(400);
    const S2 = () => p.evaluate(s => ({ cur: s2Cur, ctx: !document.getElementById('ctx').hidden, mv: moves[s] || null, kept: checked[s] || null, recut: !!recuts[s], msg: document.getElementById('s2Msg').textContent }), sid3);
    const tap2 = async sel => { await p.locator(sel).scrollIntoViewIfNeeded(); if (touch) await p.tap(sel); else await p.click(sel); await p.waitForTimeout(350); };
    await tap2('#s2Fix'); await tap2('#fixRm'); await tap2('#fixSave'); a = await S2();
    ok(!a.ctx && a.cur === sid3 && a.mv === 'OUT' && !a.kept && a.recut && /still waiting/.test(a.msg),
      `${name}: a sign taken out in step 1: Save cut saves the cut and it stays waiting for its pile (not put back, not kept)`, JSON.stringify(a));
    await ctx.close();
    // ---- a page whose line crops have lines above and below (region.html in the line-strip view: r_L01-r_L03). Adversarial check, 11 Oct
    // 2026 (Luzerne box page): "Fix the cut" opens the card and starts the editor in one go; the card's plain draw, still waiting for the
    // neighbour line images, ran after the editor's and repainted the plain view (brackets, the lines above and below) and its map under
    // the editor, so a drag on the box saved a collapsed cut. The editor's view (no neighbour lines: map ha 0, hb 0) must stay.
    ctx = await b.newContext(opts); await mock.install(ctx); await ctx.addInitScript(() => { try { localStorage.setItem('sorterPageView', '0'); } catch (e) {} });
    p = await ctx.newPage(); p.on('pageerror', e => errs.push(name + ' (region): ' + e.message));
    await p.goto('file://' + path.join(DIR, 'region.html')); await p.waitForFunction(() => typeof ready !== 'undefined' && ready, null, { timeout: 30000 });
    const sid5 = await p.evaluate(() => { const s = Object.keys(itemBySid).find(x => itemBySid[x].p === 'r_L02' && !itemBySid[x].r); takeOut(s, null); setStep(2); return s; });
    await p.waitForFunction(() => step === 2 && s2Cur && !document.getElementById('s2Work').hidden, null, { timeout: 30000 }); await p.waitForTimeout(400);
    const nb5 = await p.evaluate(s => nbPages(itemBySid[s].p).filter(Boolean).length, sid5);
    const tap5 = async sel => { await p.locator(sel).scrollIntoViewIfNeeded(); if (touch) await p.tap(sel); else await p.click(sel); };
    await tap5('#s2Fix'); await p.waitForTimeout(1500);
    const v5 = await p.evaluate(() => { const c = document.getElementById('ctxC'), m = c._map || {}; return { fix: !!fix, view: c.dataset.view, ha: m.ha, hb: m.hb }; });
    ok(nb5 === 2 && v5.fix && v5.view === 'strip' && v5.ha === 0 && v5.hb === 0,
      `${name}: on a line with lines above and below (${sid5}), step 2's Fix the cut keeps the editor's view once the neighbour lines load (no plain card drawn over it)`, JSON.stringify(v5));
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
