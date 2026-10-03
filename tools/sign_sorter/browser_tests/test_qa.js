// QA pass (3 Oct 2026): drives the sorter like the owner does, on a phone (390x760, touch) and a desktop (1280x900),
// against mock_db.js (a persistent, slow, out-of-order, sometimes-refusing store). Every check prints PASS/FAIL; exit 1 on
// any FAIL. Needs a page built with --focus of at least 6 tiles spread over 2+ pages (the Birago page is the reference).
// Run: NODE_PATH=$(npm root -g) node test_qa.js PAGE.html [DUMP_DIR]   (DUMP_DIR: the store as sign_sorter_apply.py --db reads it)
const { chromium } = require('playwright'); const mock = require('./mock_db');
const PAGE = 'file://' + process.argv[2], DUMP = process.argv[3];
let fails = 0; const ok = (name, cond, extra) => { console.log((cond ? 'PASS ' : 'FAIL ') + name + (extra !== undefined ? '  [' + extra + ']' : '')); if (!cond) fails++; };
const PHONE = { viewport: { width: 390, height: 760 }, isMobile: true, hasTouch: true }, DESK = { viewport: { width: 1280, height: 900 } };
const settle = page => page.waitForFunction(() => /All changes saved|Connected/.test(document.getElementById('save').textContent), null, { timeout: 8000 }).catch(() => {});
const S = page => page.evaluate(() => { const srt = o => o && typeof o === 'object' && !Array.isArray(o) ? Object.fromEntries(Object.keys(o).sort().map(k => [k, srt(o[k])])) : o;
  return JSON.stringify(srt({ moves, state, newPiles, checked: typeof checked === 'undefined' ? {} : checked })); });

async function open(b, vp, opts) {
  const ctx = await b.newContext(vp); const store = await mock.install(ctx, opts); const page = await ctx.newPage();
  const errs = []; page.on('pageerror', e => errs.push(e.message)); page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await page.goto(PAGE); await page.waitForTimeout((opts && opts.connectMs || 600) + 400); return { ctx, store, page, errs };
}
// pile element selector, the way the page itself builds the id (domKey: case-safe, any characters)
const pileSel = (page, id) => page.evaluate(id => '#pile_' + (typeof domKey === 'function' ? domKey(id) : key(id)), id);
const focusSids = page => page.evaluate(() => [...document.querySelectorAll('#focusTiles > div')].map(d => d.dataset.sid || d.querySelector('img').alt));
const bracketVisible = page => page.evaluate(() => { const c = document.getElementById('ctxC'), cv = c.parentElement, it = itemBySid[ctxSid], [x, , w] = it.b;
  const im = pageImgs[it.p], x0 = Math.max(0, x - 180), x1 = Math.min(im.naturalWidth, x + w + 180), css = c.getBoundingClientRect().width;
  const mid = ((x - x0) + w / 2) * css / (x1 - x0); return mid >= cv.scrollLeft && mid <= cv.scrollLeft + cv.clientWidth; });

(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_EXE || '/opt/pw-browsers/chromium' });
  for (const [tag, vp] of [['phone', PHONE], ['desk', DESK]]) {
    const { ctx, store, page, errs } = await open(b, vp);
    const F = await focusSids(page);
    // 1. layout
    const lay = await page.evaluate(() => ({ sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth,
      pos: getComputedStyle(document.querySelector('.bar')).position, fh: document.getElementById('focus').getBoundingClientRect().height }));
    ok(tag + ': no sideways page scroll', lay.sw <= lay.cw, lay.sw + ' vs ' + lay.cw);
    const spill = await page.evaluate(async () => { document.querySelectorAll('img[loading=lazy]').forEach(i => i.loading = 'eager'); await new Promise(r => setTimeout(r, 600));
      return [...document.querySelectorAll('.t')].filter(t => { const a = t.getBoundingClientRect(), i = t.querySelector('img').getBoundingClientRect();
        return i.bottom - a.bottom > 1 || a.top - i.top > 1 || i.right - a.right > 1 || a.left - i.left > 1; }).length; });
    ok(tag + ': no tile image spills out of its frame over the buttons', spill === 0, spill + ' tiles');
    if (tag === 'phone') { ok('phone: toolbar does not stay pinned over a third of the screen', lay.pos !== 'sticky', lay.pos);
      ok('phone: "Check these first" box is not a 2,000 px column of captions', lay.fh < 1000, Math.round(lay.fh)); }
    const caps = await page.evaluate(() => [...document.querySelectorAll('#focusTiles .fcap')].map(e => e.textContent));
    ok(tag + ': focus captions are the question, not a cut-off note', caps.length && caps.every(c => c && !/\]$/.test(c)), caps.filter(c => /\]$/.test(c)).join(' | '));
    const clash = await page.evaluate(() => { const seen = {}; let n = 0; document.querySelectorAll('.pile').forEach(e => { const k = e.id.toLowerCase(); if (seen[k]) n++; seen[k] = 1; }); return n; });
    ok(tag + ': no two piles share an element id, even ignoring case ("O" and "o")', clash === 0, clash);
    // 2. focus tile opens on itself, question shown, stepping, zoom, brackets in view
    const j0 = Math.min(3, F.length - 2);
    await page.locator('#focusTiles .t').nth(j0).click(); await page.waitForTimeout(200);
    ok(tag + ': focus tile opens on that tile', (await page.textContent('#ctxT')).includes(F[j0]), await page.textContent('#ctxT'));
    ok(tag + ': position reads ' + (j0 + 1) + ' of ' + F.length, (await page.textContent('#ctxPos')).startsWith((j0 + 1) + ' of ' + F.length), await page.textContent('#ctxPos'));
    ok(tag + ': the question is shown in the dialog', await page.isVisible('#ctxQ') && (await page.textContent('#ctxQ')).length > 3);
    await page.click('#ctxNext'); ok(tag + ': Next goes to the next focus tile', (await page.textContent('#ctxT')).includes(F[j0 + 1]) && (await page.textContent('#ctxPos')).startsWith((j0 + 2) + ' of'));
    await page.click('#ctxPrev'); ok(tag + ': Previous goes back', (await page.textContent('#ctxT')).includes(F[j0]));
    ok(tag + ': bracketed sign in view at zoom 3', await bracketVisible(page));
    const w3 = await page.evaluate(() => document.getElementById('ctxC').getBoundingClientRect().width);
    await page.fill('#ctxZ', '6'); await page.dispatchEvent('#ctxZ', 'input'); await page.waitForTimeout(100);
    const w6 = await page.evaluate(() => document.getElementById('ctxC').getBoundingClientRect().width);
    ok(tag + ': zoom slider enlarges the line', w6 > w3 * 1.5, Math.round(w3) + ' -> ' + Math.round(w6));
    ok(tag + ': bracketed sign still in view at zoom 6', await bracketVisible(page));
    await page.fill('#ctxZ', '3'); await page.dispatchEvent('#ctxZ', 'input');
    ok(tag + ': Close is on screen', await page.locator('#ctxX').isVisible());
    // stale draw: tile A's page image arrives late, after the person stepped on to a tile on another page
    const late = await page.evaluate(F => { const pa = itemBySid[F[0]].p; const j = F.findIndex(s => itemBySid[s].p !== pa); if (j < 0) return null;
      Object.keys(pageImgs).forEach(k => delete pageImgs[k]);
      const im = new Image(); pageImgs[pa] = im; setTimeout(() => { im.src = 'data:image/jpeg;base64,' + DATA.pages[pa]; }, 400); return j; }, F);
    if (late !== null) {
      await page.click('#ctxClose'); await page.locator('#focusTiles .t').nth(0).click();
      for (let i = 0; i < late; i++) await page.click('#ctxNext');
      await page.waitForTimeout(800);
      const right = await page.evaluate(() => { const it = itemBySid[ctxSid], [x, y, w, h] = it.b, im = pageImgs[it.p], c = document.getElementById('ctxC');
        const x0 = Math.max(0, x - 180), y0 = Math.max(0, y - Math.round(h * 1.8) - 10), x1 = Math.min(im.naturalWidth, x + w + 180), y1 = Math.min(im.naturalHeight, y + h + Math.round(h * 1.4) + 10);
        return Math.abs(c.width / c.height - (x1 - x0) / (y1 - y0)) < 0.02; });
      ok(tag + ': a late page image does not paint another tile over the one shown', right);
    }
    await page.click('#ctxClose');
    // backdrop closes
    await page.locator('#focusTiles .t').nth(0).click(); await page.mouse.click(vp.viewport.width - 3, vp.viewport.height - 3);
    ok(tag + ': tapping the backdrop closes the dialog', await page.locator('#ctx').isHidden());
    // 3. decisions from the dialog, walking a list of 7+ tiles: the focus list if it is long enough, else the biggest pile
    const fromFocus = F.length >= 7;
    let bigPile = null;
    if (fromFocus) await page.locator('#focusTiles .t').nth(0).click();
    else { bigPile = await page.evaluate(() => basePiles.map(p => p.id).sort((a, b) => membersOf(b).length - membersOf(a).length)[0]);
      await page.click('#modeCtx'); await page.locator((await pileSel(page, bigPile)) + ' .tiles .t').first().click(); await page.evaluate(() => setMode('sel')); }
    const L = await page.evaluate(() => ctxList.slice());
    ok(tag + ': a list of 7+ tiles to walk (' + (fromFocus ? 'focus' : 'pile ' + bigPile) + ')', L.length >= 7, L.length);
    const dest = await page.evaluate(() => document.getElementById('ctxDest').options[1].value);
    const cntBefore = await page.evaluate(d => membersOf(d).length, dest);
    await page.selectOption('#ctxDest', dest);
    ok(tag + ': move from the dialog lands in the pile', await page.evaluate(([s, d]) => moves[s] === d && membersOf(d).length, [L[0], dest]) === cntBefore + 1);
    ok(tag + ': dialog moved on to the next tile in the list', (await page.textContent('#ctxT')).includes(L[1]));
    await page.click('#ctxAside'); ok(tag + ': Set aside', await page.evaluate(s => moves[s], L[1]) === 'ASIDE');
    await page.click('#ctxBad'); ok(tag + ': Bad cut', await page.evaluate(s => moves[s], L[2]) === 'BAD-CUT');
    ok(tag + ': no text box to type a pile name', (await page.locator('#ctx input[type=text]').count()) === 0);
    const want3 = await page.evaluate(() => nextPileName(pileOf(ctxSid)));
    await page.click('#ctxNewB'); const np1 = await page.evaluate(s => moves[s], L[3]);
    ok(tag + ': one tap makes a new pile, named by the page', np1 === want3, np1 + ' vs ' + want3);
    ok(tag + ': the new pile is offered first for the next tile', (await page.evaluate(() => document.getElementById('ctxDest').options[1].value)) === np1);
    ok(tag + ': there is a way to say "this tile is in the right pile"', await page.isVisible('#ctxKeep'));
    if (await page.isVisible('#ctxKeep')) { await page.click('#ctxKeep'); ok(tag + ': keep records the tile and moves on', (await page.textContent('#ctxT')).includes(L[5])); }
    await page.click('#ctxUndo'); ok(tag + ': dialog Undo shows the undone tile again', (await page.textContent('#ctxT')).includes(L[4]));
    if (await page.isVisible('#ctxKeep')) await page.click('#ctxKeep');
    await page.click('#ctxClose');
    if (fromFocus) { const caps5 = await page.evaluate(() => [...document.querySelectorAll('#focusTiles > div')].slice(0, 5).map(d => d.querySelector('.t').classList.contains('done')));
      ok(tag + ': answered focus tiles are marked', caps5.every(Boolean), JSON.stringify(caps5)); }
    // last tile of the focus list: Keep, then a move, both stay on it and say it was the last
    const last = F[F.length - 1];
    await page.locator('#focusTiles .t').nth(F.length - 1).click();
    if (await page.isVisible('#ctxKeep')) { await page.click('#ctxKeep');
      ok(tag + ': Keep on the last focus tile stays on it and says it was the last', (await page.textContent('#ctxT')).includes(last) && /last tile/.test(await page.textContent('#ctxMsg'))); }
    const dl = await page.evaluate(() => document.getElementById('ctxDest').options[1].value); await page.selectOption('#ctxDest', dl);
    ok(tag + ': moving the last tile keeps it shown, says so', (await page.textContent('#ctxT')).includes(last) && /last tile/.test(await page.textContent('#ctxMsg')));
    await page.click('#ctxClose');
    // 4. select mode in a pile: page does not reshuffle, the pile stays put
    const pid = await page.evaluate(() => [...document.querySelectorAll('.pile')].map(e => e.querySelector('.pid').textContent).find(id => membersOf(id).length >= 4 && byBase[id] && !statusOf(id)));
    const el = page.locator(await pileSel(page, pid));
    await el.evaluate(e => window.scrollTo(0, e.getBoundingClientRect().top + scrollY - 150));
    const order0 = await page.evaluate(() => [...document.querySelectorAll('.pile .pid')].map(e => e.textContent).join());
    const y0 = await el.evaluate(e => e.getBoundingClientRect().top);
    for (let i = 0; i < 3; i++) await el.locator('.tiles .t:not(.sel)').first().click();
    ok(tag + ': 3 tiles selected', (await el.locator('.t.sel').count()) === 3);
    const far = await page.evaluate(p => { const me = byBase[p].family; return (basePiles.find(q => q.family !== me) || basePiles.find(q => q.id !== p)).id; }, pid);
    await el.locator('.movebar select').selectOption(far); await page.waitForTimeout(100);
    ok(tag + ': families and piles keep their order after a move', order0 === await page.evaluate(() => [...document.querySelectorAll('.pile .pid')].map(e => e.textContent).join()));
    ok(tag + ': the pile you worked on stays where it was on screen', Math.abs(await el.evaluate(e => e.getBoundingClientRect().top) - y0) < 3);
    await page.click('#undo'); ok(tag + ': toolbar Undo puts the 3 tiles back', await page.evaluate(p => membersOf(p).length, pid) >= 4);
    for (let i = 0; i < 2; i++) await el.locator('.tiles .t:not(.sel)').first().click();
    ok(tag + ': pile move bar has no name box to fill', (await el.locator('.movebar input').count()) === 0);
    const prevAuto = await page.evaluate(p => Object.keys(newPiles).filter(n => n.startsWith(p + '-')), pid);
    const want = await page.evaluate(p => nextPileName(p), pid);
    await el.locator('.movebar button', { hasText: 'New pile' }).click(); await page.waitForTimeout(100);
    const auto = await page.evaluate((a) => Object.keys(newPiles).filter(n => n.startsWith(a.p + '-') && !a.b.includes(n)).map(n => [n, membersOf(n).length]), {p: pid, b: prevAuto});
    ok(tag + ': "New pile" in the pile view makes the next auto name (' + want + ') with the 2 tiles', auto.length === 1 && auto[0][0] === want && auto[0][1] === 2, JSON.stringify(auto));
    // verdict + progress
    await el.locator('.acts button', { hasText: 'All one sign' }).click();
    ok(tag + ': All one sign counts in the progress', /^1 of/.test(await page.textContent('#prog')), await page.textContent('#prog'));
    // typing a note survives a snapshot from another device
    const note = el.locator('.acts input[type=text]'); await note.click(); await note.type('half a no');
    await store.external(page, 'moves', 'zz_other', { sid: await page.evaluate(L => Object.keys(itemBySid).find(x => !L.includes(x) && !moves[x]), L), from: 'x', to: dest }); await page.waitForTimeout(200);
    ok(tag + ': a note being typed survives an update from another device', (await page.evaluate(() => document.activeElement.value)) === 'half a no');
    await page.keyboard.type('te'); await page.keyboard.press('Tab');
    // jump to pile from "Possibly similar" while that pile is filtered out of view
    const pr = await page.evaluate(() => { const p = basePiles.find(q => !statusOf(q.id) && membersOf(q.id).length && q.near && q.near.length && byBase[q.near[0]] && !statusOf(q.near[0]) && membersOf(q.near[0]).length); return p ? [p.id, p.near[0]] : null; });
    if (pr) {
      const k1 = await pileSel(page, pr[1]), k0 = await pileSel(page, pr[0]);
      await page.locator(k1 + ' .acts button', { hasText: 'All one sign' }).click();
      await page.selectOption('#show', 'todo');
      await page.locator(k0 + ' .near button', { hasText: new RegExp('^' + pr[1] + '$') }).click(); await page.waitForTimeout(100);
      const r = await page.evaluate(id => { const e = document.querySelector(id); if (!e) return null; const t = e.getBoundingClientRect().top;
        return { t, bar: Math.max(0, document.querySelector('.bar').getBoundingClientRect().bottom) }; }, k1);
      ok(tag + ': "Possibly similar" jump reaches a pile hidden by the Show filter, not under the toolbar', r && r.t >= r.bar - 1 && r.t < vp.viewport.height / 2, JSON.stringify(r));
      await page.selectOption('#show', 'all');
    }
    // 5. persistence
    await settle(page); await page.waitForTimeout(600);
    const before = await S(page);
    await page.reload(); await page.waitForTimeout(1500);
    const after = await S(page);
    ok(tag + ': every decision is back after a reload', before === after, before.length + ' vs ' + after.length);
    ok(tag + ': no page errors', !errs.length, errs.join(' | '));
    if (DUMP && tag === 'desk') store.dump(DUMP);
    await ctx.close();
  }
  // race: move + undo of one tile in quick succession, ten times, on a store whose writes can land out of order
  { const { ctx, store, page } = await open(b, DESK, { minMs: 5, maxMs: 60, setMinMs: 300, setMaxMs: 600 });
    await page.locator('#focusTiles .t').nth(0).click();
    const s0 = await page.evaluate(() => ctxSid);
    for (let i = 0; i < 10; i++) { await page.selectOption('#ctxDest', { index: 1 }); await page.click('#ctxUndo'); }
    await page.waitForTimeout(2500);
    ok('race: move+undo x10 leaves no stray move in the store', !Object.values(store.docs.moves || {}).some(m => m.sid === s0), JSON.stringify(store.docs.moves));
    await ctx.close(); }
  // decisions made before storage answers are kept
  { const { ctx, store, page } = await open(b, DESK, { connectMs: 2500 });
    await page.goto(PAGE); await page.waitForTimeout(300);
    await page.locator('#focusTiles .t').nth(0).click(); await page.selectOption('#ctxDest', { index: 1 });
    await page.waitForTimeout(3500);
    ok('early: a move made while storage is connecting is saved', Object.keys(store.docs.moves || {}).length === 1);
    await ctx.close(); }
  // a refused save is visible, and can be retried
  { const { ctx, store, page } = await open(b, DESK);
    store.failNext(2);
    await page.locator('#focusTiles .t').nth(0).click(); await page.selectOption('#ctxDest', { index: 1 }); await page.waitForTimeout(1500);
    ok('fail: a refused save says so', /Not saved/.test(await page.textContent('#save')), await page.textContent('#save'));
    ok('fail: ...and says so inside the open dialog, where the person is working', await page.isVisible('#ctxErr') && /Not saved/.test(await page.textContent('#ctxErr')));
    await page.selectOption('#ctxDest', { index: 1 }); await page.waitForTimeout(1200);
    ok('fail: a later good save does not leave "Saving 1..." stuck', !/Saving/.test(await page.textContent('#save')), await page.textContent('#save'));
    if (await page.isVisible('#ctxRetry')) await page.click('#ctxRetry'); else if (await page.isVisible('#retry')) await page.click('#retry');
    await page.waitForTimeout(1200);
    ok('fail: after Try again everything is in the store', Object.keys(store.docs.moves || {}).length === 2 && /All changes saved/.test(await page.textContent('#save')), await page.textContent('#save'));
    await ctx.close(); }
  await b.close();
  console.log(fails ? fails + ' FAILED' : 'ALL PASS'); process.exit(fails ? 1 : 0);
})();
