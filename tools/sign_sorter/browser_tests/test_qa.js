// QA test for the sign sorter (3 Oct 2026; two-step flow the same evening): drives the page like the owner does, on a
// phone (390x760, touch) and a desktop (1280x900), against mock_db.js (a persistent, slow, out-of-order, sometimes-refusing
// store). Every check prints PASS/FAIL; exit 1 on any FAIL. Works on synthetic fixtures (make_fixtures.py) and on real
// pages: few or no "Check these first" tiles, piles that differ only by case ("O"/"o"), odd pile names, one family.
// Run: NODE_PATH=$(npm root -g) node test_qa.js PAGE.html [DUMP_DIR]   (DUMP_DIR: the store as sign_sorter_apply.py --db reads it)
const { chromium } = require('playwright'); const mock = require('./mock_db');
const PAGE = 'file://' + process.argv[2], DUMP = process.argv[3];
let fails = 0; const ok = (name, cond, extra) => { console.log((cond ? 'PASS ' : 'FAIL ') + name + (extra !== undefined ? '  [' + extra + ']' : '')); if (!cond) fails++; };
const PHONE = { viewport: { width: 390, height: 760 }, isMobile: true, hasTouch: true }, DESK = { viewport: { width: 1280, height: 900 } };
const settle = page => page.waitForFunction(() => /All changes saved|Connected/.test(document.getElementById('save').textContent), null, { timeout: 8000 }).catch(() => {});
const S = page => page.evaluate(() => { const srt = o => o && typeof o === 'object' && !Array.isArray(o) ? Object.fromEntries(Object.keys(o).sort().map(k => [k, srt(o[k])])) : o;
  return JSON.stringify(srt({ moves, state, newPiles, checked })); });
const pileSel = (page, id) => page.evaluate(id => '#pile_' + domKey(id), id);

async function open(b, vp, opts) {
  const ctx = await b.newContext(vp); const store = await mock.install(ctx, opts); const page = await ctx.newPage();
  const errs = []; page.on('pageerror', e => errs.push(e.message)); page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await page.addInitScript(() => { window.__cm = []; document.addEventListener('contextmenu', e => setTimeout(() => window.__cm.push(e.defaultPrevented)), true); });
  await page.goto(PAGE); await page.waitForTimeout((opts && opts.connectMs || 600) + 400); return { ctx, store, page, errs };
}
const focusSids = page => page.evaluate(() => [...document.querySelectorAll('#focusTiles > div')].map(d => d.dataset.sid));
const bracketVisible = (page, cid = 'ctxC') => page.evaluate(cid => { const c = document.getElementById(cid), cv = c.parentElement, sid = cid === 'ctxC' ? ctxSid : s2Cur, it = itemBySid[sid], [x, , w] = it.b;
  const im = pageImgs[it.p], x0 = Math.max(0, x - 180), x1 = Math.min(im.naturalWidth, x + w + 180), css = c.getBoundingClientRect().width;
  const mid = ((x - x0) + w / 2) * css / (x1 - x0); return mid >= cv.scrollLeft && mid <= cv.scrollLeft + cv.clientWidth; }, cid);
// a pile with enough tiles to work on, not settled, from the original piles
const workPile = page => page.evaluate(() => basePiles.map(p => p.id).filter(id => !statusOf(id)).sort((a, b) => membersOf(b).length - membersOf(a).length)[0]);

(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_EXE || '/opt/pw-browsers/chromium' });
  for (const [tag, vp] of [['phone', PHONE], ['desk', DESK]]) {
    const { ctx, store, page, errs } = await open(b, vp);
    const F = await focusSids(page);
    // 1. layout
    const lay = await page.evaluate(() => ({ sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth,
      bh: document.querySelector('.bar').getBoundingClientRect().height, fh: document.getElementById('focus').getBoundingClientRect().height,
      hint: document.getElementById('hint1').textContent, mode: !!document.getElementById('modeSel'), quirks: document.compatMode }));
    ok(tag + ': standards mode (a <!doctype html>)', lay.quirks === 'CSS1Compat', lay.quirks);
    ok(tag + ': no sideways page scroll', lay.sw <= lay.cw, lay.sw + ' vs ' + lay.cw);
    ok(tag + ': the toolbar is a slim strip (steps, Undo, save line)', lay.bh < 130, Math.round(lay.bh));
    ok(tag + ': one-line hint says tap takes out and hold shows larger', /Tap/.test(lay.hint) && /Hold/.test(lay.hint), lay.hint);
    ok(tag + ': the old "Click selects / shows context" switch is gone', !lay.mode);
    const spill = await page.evaluate(async () => { document.querySelectorAll('img[loading=lazy]').forEach(i => i.loading = 'eager'); await new Promise(r => setTimeout(r, 600));
      return [...document.querySelectorAll('.t')].filter(t => { const a = t.getBoundingClientRect(), i = t.querySelector('img').getBoundingClientRect();
        return i.bottom - a.bottom > 1 || a.top - i.top > 1 || i.right - a.right > 1 || a.left - i.left > 1; }).length; });
    ok(tag + ': no tile image spills out of its frame over the buttons', spill === 0, spill + ' tiles');
    const clash = await page.evaluate(() => { const seen = {}; let n = 0; document.querySelectorAll('[id]').forEach(e => { const k = e.id.toLowerCase(); if (seen[k]) n++; seen[k] = 1; }); return n; });
    ok(tag + ': no two elements share an id, even ignoring case ("O" and "o")', clash === 0, clash);
    if (F.length) {
      if (tag === 'phone') ok('phone: "Check these first" box is not a 2,000 px column of captions', lay.fh < 1000 + 30 * Math.max(0, F.length - 24), Math.round(lay.fh));
      const caps = await page.evaluate(() => [...document.querySelectorAll('#focusTiles .fcap')].map(e => e.textContent));
      ok(tag + ': focus captions are the question, not a cut-off note', caps.every(c => c && !/\]$/.test(c)), caps.filter(c => /\]$/.test(c)).join(' | '));
      const fq = await page.evaluate(() => document.querySelectorAll('#list .t.fq').length);
      ok(tag + ': "Check these first" tiles are marked in their piles', fq > 0, fq);
    }
    // 2. the larger view from a focus tile: opens on itself, question, stepping, zoom, brackets
    if (F.length >= 2) {
      const j0 = Math.min(3, F.length - 2);
      await page.locator('#focusTiles .t').nth(j0).click(); await page.waitForTimeout(200);
      ok(tag + ': focus tile opens the larger view on that tile', (await page.textContent('#ctxT')).includes(F[j0]), await page.textContent('#ctxT'));
      ok(tag + ': position reads ' + (j0 + 1) + ' of ' + F.length, (await page.textContent('#ctxPos')).startsWith((j0 + 1) + ' of ' + F.length));
      ok(tag + ': the question is shown in the dialog', await page.isVisible('#ctxQ'));
      await page.click('#ctxNext'); ok(tag + ': Next goes to the next focus tile', (await page.textContent('#ctxT')).includes(F[j0 + 1]));
      await page.click('#ctxPrev'); ok(tag + ': Previous goes back', (await page.textContent('#ctxT')).includes(F[j0]));
      ok(tag + ': bracketed sign in view at zoom 3', await bracketVisible(page));
      const scale = () => page.evaluate(() => { const c = document.getElementById('ctxC'); return c.getBoundingClientRect().width / +c.dataset.span; });
      const w3 = await scale();
      await page.fill('#ctxZ', '6'); await page.dispatchEvent('#ctxZ', 'input'); await page.waitForTimeout(100);
      const w6 = await scale();
      ok(tag + ': zoom in makes the sign larger on screen', w6 > w3 * 1.5, w3.toFixed(2) + ' -> ' + w6.toFixed(2));
      await page.fill('#ctxZ', '1'); await page.dispatchEvent('#ctxZ', 'input'); await page.waitForTimeout(100);
      const w1 = await scale(); const whole = await page.evaluate(() => document.getElementById('ctxC').dataset.whole === '1');
      ok(tag + ': zoom out shows more of the line (sign smaller on screen, or the whole line already shown)', w1 < w3 * 0.8 || (whole && w1 <= w3), w3.toFixed(2) + ' -> ' + w1.toFixed(2) + (whole ? ' (whole line)' : ''));
      ok(tag + ': bracketed sign in view at zoom 1', await bracketVisible(page));
      await page.fill('#ctxZ', '6'); await page.dispatchEvent('#ctxZ', 'input'); await page.waitForTimeout(100);
      ok(tag + ': bracketed sign still in view at zoom 6', await bracketVisible(page));
      await page.fill('#ctxZ', '3'); await page.dispatchEvent('#ctxZ', 'input');
      // stale draw: tile A's page image arrives late, after the person stepped on to a tile on another page
      const late = await page.evaluate(F => { const pa = itemBySid[F[0]].p; const j = F.findIndex(s => itemBySid[s].p !== pa); if (j < 0) return null;
        Object.keys(pageImgs).forEach(k => delete pageImgs[k]);
        const im = new Image(); pageImgs[pa] = im; setTimeout(() => { im.src = 'data:image/jpeg;base64,' + DATA.pages[pa]; }, 400); return j; }, F);
      if (late !== null) {
        await page.click('#ctxClose'); await page.locator('#focusTiles .t').nth(0).click();
        for (let i = 0; i < late; i++) await page.click('#ctxNext');
        await page.waitForTimeout(800);
        const right = await page.evaluate(() => document.getElementById('ctxC').dataset.sid === ctxSid);
        ok(tag + ': a late page image does not paint another tile over the one shown', right);
      }
      await page.click('#ctxClose');
      await page.locator('#focusTiles .t').nth(0).click(); await page.mouse.click(vp.viewport.width - 3, vp.viewport.height - 3);
      ok(tag + ': tapping the backdrop closes the dialog', await page.locator('#ctx').isHidden());
    }
    // 3. STEP 1: tap takes a sign out, hold opens the larger view (and takes nothing out), tray puts back
    const pid = await workPile(page); const sel = await pileSel(page, pid); const el = page.locator(sel);
    await el.scrollIntoViewIfNeeded(); await el.evaluate(e => window.scrollTo(0, e.getBoundingClientRect().top + scrollY - 150));
    const order0 = await page.evaluate(() => [...document.querySelectorAll('.pile .pid')].map(e => e.textContent).join());
    const y0 = await el.evaluate(e => e.getBoundingClientRect().top), n0 = await el.locator('.tiles .t').count();
    const s1 = await el.locator('.tiles .t').nth(1).getAttribute('data-sid');
    await el.locator('.tiles .t').nth(1).click(); await page.waitForTimeout(150);
    ok(tag + ': a tap takes the sign out of its pile', await page.evaluate(s => moves[s], s1) === 'OUT' && (await el.locator('.tiles .t').count()) === n0 - 1);
    ok(tag + ': ...into the "Taken out" tray, with a count on step 2', await page.isVisible('#tray') && (await page.textContent('#trayN')) === '1' && (await page.textContent('#outN')) === '1');
    ok(tag + ': families and piles keep their order after a take-out', order0 === await page.evaluate(() => [...document.querySelectorAll('.pile .pid')].map(e => e.textContent).join()));
    ok(tag + ': the pile stays where it was on screen', Math.abs(await el.evaluate(e => e.getBoundingClientRect().top) - y0) < 3);
    await page.locator('#trayTiles .t').first().click(); await page.waitForTimeout(100);
    ok(tag + ': tapping it in the tray puts it back', await page.evaluate(s => moves[s], s1) === undefined && !(await page.isVisible('#tray')));
    await page.locator(sel + ' .tiles .t').nth(1).click(); await page.click('#undo');
    ok(tag + ': toolbar Undo puts a taken-out sign back', await page.evaluate(s => moves[s], s1) === undefined);
    const h = el.locator('.tiles .t').nth(2); const hs = await h.getAttribute('data-sid');
    await page.evaluate(() => { window.__cm = []; });
    await mock.hold(page, h);
    ok(tag + ': holding a sign opens the larger view on it', await page.isVisible('#ctx') && (await page.textContent('#ctxT')).includes(hs), await page.textContent('#ctxT'));
    ok(tag + ': ...and does not take it out', await page.evaluate(s => moves[s], hs) === undefined);
    ok(tag + ': ...and no browser menu pops up', (await page.evaluate(() => window.__cm)).every(Boolean), JSON.stringify(await page.evaluate(() => window.__cm)));
    ok(tag + ': ...stepping through that pile', /in this pile/.test(await page.textContent('#ctxPos')));
    await page.click('#ctxClose');
    await el.locator('.ph .big').click(); ok(tag + ': "View larger" on a pile opens it too', await page.isVisible('#ctx')); await page.click('#ctxClose');
    // 4. decisions in the larger view, walking a list of 7+ tiles (the focus list if long enough, else the biggest pile)
    const fromFocus = F.length >= 7;
    if (fromFocus) await page.locator('#focusTiles .t').nth(0).click(); else await el.locator('.ph .big').click();
    const L = await page.evaluate(() => ctxList.slice());
    ok(tag + ': a list of 7+ tiles to walk (' + (fromFocus ? 'focus' : 'pile ' + pid) + ')', L.length >= 7, L.length);
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
    await page.click('#ctxKeep'); ok(tag + ': keep records the tile and moves on', (await page.textContent('#ctxT')).includes(L[5]));
    await page.click('#ctxUndo'); ok(tag + ': dialog Undo shows the undone tile again', (await page.textContent('#ctxT')).includes(L[4]));
    await page.click('#ctxOut'); ok(tag + ': "Doesn’t belong: take out" from the larger view', await page.evaluate(s => moves[s], L[4]) === 'OUT');
    await page.click('#ctxClose');
    if (fromFocus) { const c5 = await page.evaluate(() => [...document.querySelectorAll('#focusTiles > div')].slice(0, 5).map(d => d.querySelector('.fdone').textContent));
      ok(tag + ': answered focus tiles say what happened', c5.every(Boolean), JSON.stringify(c5)); }
    if (F.length) {   // last tile of the focus list: Keep and a move both stay on it and say it was the last
      const last = F[F.length - 1];
      await page.locator('#focusTiles .t').nth(F.length - 1).click();
      if (await page.isVisible('#ctxKeep')) { await page.click('#ctxKeep');
        ok(tag + ': Keep on the last focus tile stays on it and says it was the last', (await page.textContent('#ctxT')).includes(last) && /last tile/.test(await page.textContent('#ctxMsg'))); }
      await page.selectOption('#ctxDest', { index: 1 });
      ok(tag + ': moving the last tile keeps it shown, says so', (await page.textContent('#ctxT')).includes(last) && /last tile/.test(await page.textContent('#ctxMsg')));
      await page.click('#ctxClose');
    }
    // 5. pile verdicts, note, jumps
    await page.locator(sel + ' .acts button', { hasText: 'This pile is done' }).click();
    ok(tag + ': "This pile is done" counts in the progress', /^1 of .* piles done/.test(await page.textContent('#prog')), await page.textContent('#prog'));
    await page.locator(sel + ' .acts summary').click();
    const note = page.locator(sel + ' .acts input[type=text]'); await note.click(); await note.type('half a no');
    await store.external(page, 'moves', 'zz_other', { sid: await page.evaluate(() => Object.keys(itemBySid).find(x => !moves[x])), from: 'x', to: dest }); await page.waitForTimeout(200);
    ok(tag + ': a note being typed survives an update from another device', (await page.evaluate(() => document.activeElement.value)) === 'half a no');
    await page.keyboard.type('te'); await page.keyboard.press('Tab');
    const pr = await page.evaluate(() => { const p = basePiles.find(q => !statusOf(q.id) && membersOf(q.id).length && q.near && q.near.length && byBase[q.near[0]] && !statusOf(q.near[0]) && membersOf(q.near[0]).length); return p ? [p.id, p.near[0]] : null; });
    if (pr) {
      const k1 = await pileSel(page, pr[1]), k0 = await pileSel(page, pr[0]);
      await page.locator(k1 + ' .acts button', { hasText: 'This pile is done' }).click();
      await page.locator('.opts summary').click(); await page.selectOption('#show', 'todo');
      await page.locator(k0 + ' .near button', { hasText: new RegExp('^' + pr[1].replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '$') }).click(); await page.waitForTimeout(100);
      const r = await page.evaluate(id => { const e = document.querySelector(id); if (!e) return null; const t = e.getBoundingClientRect().top;
        return { t, bar: Math.max(0, document.querySelector('.bar').getBoundingClientRect().bottom) }; }, k1);
      ok(tag + ': "Possibly similar" jump reaches a pile hidden by the Show filter, not under the toolbar', r && r.t >= r.bar - 1 && r.t < vp.viewport.height / 2, JSON.stringify(r));
      await page.selectOption('#show', 'all'); await page.locator('.opts summary').click();
    }
    // 6. STEP 2: take out three more, then place them by tap, by drag, by "new sign"; undo; done state
    await page.evaluate(() => window.scrollTo(0, 0));
    const pid2 = await workPile(page), sel2 = await pileSel(page, pid2);
    for (let i = 0; i < 3; i++) { await page.locator(sel2 + ' .tiles .t').first().click(); await page.waitForTimeout(60); }
    const waiting = await page.evaluate(() => outList());
    ok(tag + ': tray holds the taken-out signs', waiting.length >= 4, waiting.length);
    await page.click('#trayGo'); await page.waitForTimeout(600);
    ok(tag + ': "Place them" opens step 2 on the first waiting sign', await page.isVisible('#s2Work') && (await page.evaluate(() => s2Cur)) === waiting[0]);
    ok(tag + ': step 2 shows the sign on its line with brackets in view', await bracketVisible(page, 's2C'));
    const cards = await page.evaluate(() => [...document.querySelectorAll('.card')].map(c => c.dataset.pile));
    ok(tag + ': every other pile is a card to place it on', cards.length >= Math.min(3, await page.evaluate(() => basePiles.length)) && !cards.includes('BAD-CUT'), cards.length);
    const fam0 = await page.evaluate(() => { const c = document.querySelector('.card'); return [byBase[c.dataset.pile] && byBase[c.dataset.pile].family, itemBySid[s2Cur].fam]; });
    ok(tag + ': closest piles first (top card from the same family)', fam0[0] === fam0[1] || (await page.evaluate(() => new Set(basePiles.map(p => p.family)).size)) > 3, JSON.stringify(fam0));
    const c0 = await page.locator('.card').nth(1).getAttribute('data-pile'), w0 = waiting[0];
    await page.locator('.card').nth(1).click(); await page.waitForTimeout(100);
    ok(tag + ': tapping a pile card places the sign there', await page.evaluate(s => pileOf(s), w0) === c0 && (await page.evaluate(() => s2Cur)) === waiting[1]);
    await page.click('#undo'); await page.waitForTimeout(100);
    ok(tag + ': Undo in step 2 brings the sign back to place again', (await page.evaluate(s => moves[s], w0)) === 'OUT' && (await page.evaluate(() => s2Cur)) === w0);
    const target = page.locator('.card').nth(2); const c2 = await target.getAttribute('data-pile');
    await mock.drag(page, page.locator('#s2Tile'), target); await page.waitForTimeout(150);
    ok(tag + ': dragging the sign onto a pile card places it there', await page.evaluate(s => pileOf(s), w0) === c2, await page.evaluate(s => moves[s], w0));
    // drag to the bottom edge and hold there: the page scrolls on its own
    await page.evaluate(() => window.scrollTo(0, document.getElementById('s2').getBoundingClientRect().top + scrollY - 80));
    if (await page.evaluate(() => document.documentElement.scrollHeight - innerHeight - scrollY > 120 && !!s2Cur)) {
      const ys = await page.evaluate(() => scrollY);
      const tb = await page.locator('#s2Tile').boundingBox(); const x = tb.x + tb.width / 2;
      await mock.gesture(page, 'down', x, tb.y + 20);
      for (let i = 1; i <= 8; i++) { await mock.gesture(page, 'move', x, tb.y + 20 + i * (vp.viewport.height - 12 - tb.y - 20) / 8); await page.waitForTimeout(16); }
      await page.waitForTimeout(600); const ye = await page.evaluate(() => scrollY);
      await mock.gesture(page, 'move', x, tb.y + 20); await page.waitForTimeout(50); await mock.gesture(page, 'up', x, tb.y + 20); await page.waitForTimeout(100);
      ok(tag + ': holding the dragged sign near the bottom edge scrolls the page', ye > ys + 40, ys + ' -> ' + ye);
    }
    const wt = await page.evaluate(() => s2Cur);
    if (wt) { const n = await page.evaluate(() => JSON.stringify(moves)); await page.evaluate(() => window.scrollTo(0, document.getElementById('s2').getBoundingClientRect().top + scrollY - 80));
      await page.locator('#s2Tile').click(); await page.waitForTimeout(200);
      ok(tag + ': tapping the big sign in step 2 opens its larger view, and the lifted finger presses nothing in it',
        await page.isVisible('#ctx') && (await page.textContent('#ctxT')).includes(wt) && n === await page.evaluate(() => JSON.stringify(moves)));
      await page.click('#ctxClose'); }
    const w1 = await page.evaluate(() => s2Cur);
    if (w1) { const wantN = await page.evaluate(s => nextPileName(homeOf[s]), w1);
      await page.click('#s2New'); ok(tag + ': "None of these: new sign" makes ' + wantN, await page.evaluate(s => moves[s], w1) === wantN); }
    const w2 = await page.evaluate(() => s2Cur);
    if (w2) { await page.click('#s2Mark'); ok(tag + ': "Not a letter" files it with the not-letters (a pile marked not a letter)',
      await page.evaluate(s => moves[s] === 'NOT-LETTER' && state['NOT-LETTER'] && state['NOT-LETTER'].verdict === 'mark', w2)); }
    for (let i = 0; i < 40 && await page.evaluate(() => !!s2Cur); i++) { await page.click('#s2Home'); await page.waitForTimeout(50); }
    ok(tag + ': when the tray is empty step 2 says so', await page.isVisible('#s2Empty') && (await page.textContent('#outN')) === '0');
    await page.click('#s2Back'); ok(tag + ': back to step 1', await page.isVisible('#s1') && !(await page.isVisible('#s2')));
    // one sign left in the tray, never placed: after reload it is still waiting (and apply reads it as taken-out)
    await page.locator(sel2 + ' .tiles .t').first().click();
    // 7. persistence
    await settle(page); await page.waitForTimeout(800);
    const before = await S(page);
    await page.reload(); await page.waitForTimeout(1500);
    const after = await S(page);
    ok(tag + ': every decision is back after a reload', before === after, before.length + ' vs ' + after.length);
    ok(tag + ': the tray is back too', (await page.textContent('#trayN')) === '1');
    ok(tag + ': no page errors', !errs.length, errs.join(' | '));
    if (DUMP && tag === 'desk') store.dump(DUMP);
    await ctx.close();
  }
  // race: take-out + undo of one tile in quick succession, ten times, on a store whose writes can land out of order
  { const { ctx, store, page } = await open(b, DESK, { minMs: 5, maxMs: 60, setMinMs: 300, setMaxMs: 600 });
    const s0 = await page.locator('#list .t').first().getAttribute('data-sid');
    for (let i = 0; i < 10; i++) { await page.locator('#list .t[data-sid="' + s0 + '"]').click(); await page.click('#undo'); }
    await page.waitForTimeout(2500);
    ok('race: take-out+undo x10 leaves no stray move in the store', !Object.values(store.docs.moves || {}).some(m => m.sid === s0), JSON.stringify(store.docs.moves));
    await ctx.close(); }
  // decisions made before storage answers are kept
  { const { ctx, store, page } = await open(b, DESK, { connectMs: 2500 });
    await page.goto(PAGE); await page.waitForTimeout(300);
    await page.locator('#list .t').first().click();
    await page.waitForTimeout(3500);
    ok('early: a take-out made while storage is connecting is saved', Object.keys(store.docs.moves || {}).length === 1);
    await ctx.close(); }
  // a refused save is visible, and can be retried
  { const { ctx, store, page } = await open(b, DESK);
    store.failNext(2);
    await page.locator('#list .t').first().click(); await page.waitForTimeout(1500);
    ok('fail: a refused save says so', /Not saved/.test(await page.textContent('#save')), await page.textContent('#save'));
    await page.locator('#list .t').first().click(); await page.waitForTimeout(1200);
    ok('fail: a later good save does not leave "Saving 1..." stuck', !/Saving/.test(await page.textContent('#save')), await page.textContent('#save'));
    if (await page.isVisible('#retry')) await page.click('#retry');
    await page.waitForTimeout(1200);
    ok('fail: after Try again everything is in the store', Object.keys(store.docs.moves || {}).length === 2 && /All changes saved/.test(await page.textContent('#save')), await page.textContent('#save'));
    store.failNext(2); await page.locator('#list .t').nth(2).click(); await page.waitForTimeout(100);
    await mock.hold(page, page.locator('#list .t').nth(3)); await page.waitForTimeout(1300);
    ok('fail: ...and says so inside the open dialog, where the person is working', await page.isVisible('#ctxErr') && /Not saved/.test(await page.textContent('#ctxErr')));
    await ctx.close(); }
  await b.close();
  console.log(fails ? fails + ' FAILED' : 'ALL PASS'); process.exit(fails ? 1 : 0);
})();
