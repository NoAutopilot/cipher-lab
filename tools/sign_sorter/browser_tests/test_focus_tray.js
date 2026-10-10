// Template 2026-10-09.1, questions start in the tray (owner, 9 Oct 2026, Harley 287: "If they were already taken out I could
// put them in piles"). Drives the fixtures from make_fixtures.py against mock_db.js (a persistent, slow store) on a phone
// (390x760, touch) and a desktop:
//   tray.html       default build: the "Check these first" tiles open in the "Taken out" tray, the page lands on step 2, tile 1,
//                   its own pile the first card ("it was right" = one tap = a keep, no move); nothing is written until the person acts;
//   saved state     a tile with a saved move or keep is never put back in the tray (db and browser-only storage);
//   all answered    the page goes back to step 1 once the store says every question is answered (person has not touched it);
//   tray_rank.html  "Most useful first" tiles wait in the tray too, after the focus tiles;
//   plain.html      built with --no-focus-to-tray: the old layout (step 1, tiles in their piles with a "?", empty tray).
// Review fixes (same template, 9 Oct 2026; iPhone and data-safety checks):
//   loading         until the saved answers are in, step 2 shows "Loading your earlier answers…" and no sign or card (a tap there
//                   saved a keep beside an old move); a keep in the home pile clears any move in the same step; no keep at all
//                   is taken before the saved answers are in ("Right pile: keep it" in a card opened meanwhile deleted the saved
//                   move it could not see: round-2 check, 10 Oct 2026);
//   only explicit   a keep is written only by "it was right" / "Right pile: keep it" / the "?" approve: a tray tap on a question opens
//   keeps           step 2 on it, putting a tile back or a cluster move writes no keep (the question waits again), a tray tap puts a
//                   taken-out tile back where it was taken from;
//   in view         waiting tiles stay in their own pile in step 1, dimmed (a pile verdict is given with them on screen);
//   card taps       a tap anywhere on a card (its pictures included; a mouse click too, template 2026-10-09.5) places the sign;
//                   "View pile" opens the pile and places nothing;
//   one rule (R05)  template 2026-10-09.5: a tap on a "Check these first" tile does what a tap in a pile does (into the tray: it is
//                   there already, nothing moves) and a HOLD opens its card; the box's hint says so (tools/sign_sorter/
//                   browser_tests/test_gestures.js checks every box on iPhone 13, iPhone SE and a mouse);
//   wording         the cluster offer names the sign it is about; all answered -> "All N questions answered."; the rank box is
//                   hidden when it only repeats "Check these first", else it gets the same waiting line and captions.
// Must NOT: write a move or keep at load; re-tray a tile with a saved decision; change step after the person touched the page;
// accept an answer before the saved answers are in; write a keep from a put-back, a cluster move or a tray tap.
// Run: NODE_PATH=$(npm root -g) node test_focus_tray.js OUT_DIR   (OUT_DIR from make_fixtures.py; exit 1 on any FAIL)
const { chromium } = require('playwright'); const mock = require('./mock_db');
const DIR = process.argv[2];
let fails = 0; const ok = (name, cond, extra) => { console.log((cond ? 'PASS ' : 'FAIL ') + name + (extra !== undefined ? '  [' + extra + ']' : '')); if (!cond) fails++; };
const PHONE = { viewport: { width: 390, height: 760 }, isMobile: true, hasTouch: true }, DESK = { viewport: { width: 1280, height: 900 } };
const LINE = n => 'These ' + n + ' signs are waiting in step 2 · Place — open it to answer them one by one.';
const saved = page => page.waitForFunction(() => /All changes saved/.test(document.getElementById('save').textContent), null, { timeout: 8000 }).catch(() => {});

async function open(b, vp, file, opts = {}, pre) {
  const ctx = await b.newContext(vp); const store = await mock.install(ctx, opts); if (pre) pre(store);
  const page = await ctx.newPage(); const errs = []; page.on('pageerror', e => errs.push(e.message));
  if (opts.local) await page.addInitScript(v => { try { localStorage.setItem('sorter:all', v); } catch (e) {} }, opts.local);
  await page.goto('file://' + DIR + '/' + file); await page.waitForTimeout((opts.connectMs || 600) + 700); return { ctx, store, page, errs };
}
const S = page => page.evaluate(() => ({ step, tab2: document.getElementById('tab2').getAttribute('aria-selected'), s2Cur, L: outList(),
  pos: document.getElementById('s2Pos').textContent, title: document.getElementById('s2T').textContent, moves: { ...moves }, checked: { ...checked },
  card0: (() => { const c = document.querySelector('#cards .card'); return c ? { pile: c.dataset.pile, cls: c.className, text: c.textContent } : null; })(),
  home: s2Cur && homeOf[s2Cur], note: document.getElementById('focusNote').textContent, tap: document.getElementById('focusTap').textContent,
  tapHidden: document.getElementById('focusTap').hidden, focusSids: [...document.querySelectorAll('#focusTiles > div')].map(d => d.dataset.sid),
  inPiles: [...document.querySelectorAll('#list .pile .t:not(.wait)')].map(t => t.dataset.sid), waitIn: [...document.querySelectorAll('#list .pile .t.wait')].map(t => t.closest('.pile').dataset.pile + ':' + t.dataset.sid),
  opts: OPTS }));
const tap = async (page, loc, touch) => { if (touch) await loc.tap(); else await loc.click(); await page.waitForTimeout(350); };

(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_EXE || '/opt/pw-browsers/chromium' });
  for (const [tag, vp] of [['phone', PHONE], ['desk', DESK]]) {
    const touch = tag === 'phone';
    // 1. default page: lands on step 2 with the questions in the tray, nothing written
    let { ctx, store, page, errs } = await open(b, vp, 'tray.html');
    let s = await S(page); const F = s.focusSids, N = F.length;
    ok(tag + ': page option baked in (focusToTray on)', s.opts && s.opts.focusToTray === true);
    ok(tag + ': lands on step 2', s.step === 2 && s.tab2 === 'true', s.step);
    ok(tag + ': the tray holds the focus tiles, in the focus order', JSON.stringify(s.L) === JSON.stringify(F) && N >= 7, s.L.join(','));
    ok(tag + ': tile 1 of N, the first focus tile', s.s2Cur === F[0] && s.pos.startsWith('1 of ' + N + ' waiting'), s.pos);
    ok(tag + ': it says which pile it is in now', s.title.includes('now in pile ' + s.home), s.title);
    ok(tag + ': its own pile is the first card, marked as its pile now', s.card0 && s.card0.pile === s.home && /\bcur\b/.test(s.card0.cls) && /its pile now/.test(s.card0.text), JSON.stringify(s.card0));
    ok(tag + ': nothing written to the store at load (no fake moves)', store.writes === 0 && !Object.keys(s.moves).length && !Object.keys(s.checked).length, store.writes);
    ok(tag + ': step 1 focus box: one line pointing at step 2', s.note === LINE(N), s.note);
    ok(tag + ': step 1 focus box: the one rule said plainly (tap = to the tray, hold = its card)', !s.tapHidden && /^Tap a sign: it goes to the “Taken out” tray/.test(s.tap) &&
       /Hold a sign: its card opens/.test(s.tap) && !/see it large on its line; nothing moves/.test(s.tap), s.tap);
    ok(tag + ': the focus tiles are not in their piles while they wait', F.every(x => !s.inPiles.includes(x)));
    ok(tag + ': ...but each is shown dimmed in its own pile (a verdict is given with it in view)', F.every(x => s.waitIn.some(w => w.endsWith(':' + x))) &&
       await page.evaluate(W => W.every(w => { const [p, x] = w.split(':'); return homeOf[x] === p; }), s.waitIn), s.waitIn.join(','));
    ok(tag + ': the tray lists the questions in their own order (1, 2, ...)', JSON.stringify(await page.evaluate(() => [...document.querySelectorAll('#trayTiles .t')].map(t => t.dataset.sid))) === JSON.stringify(F));
    ok(tag + ': step 1 hint: questions wait in step 2 (no "?" sentence)', await page.evaluate(() => document.getElementById('hintQ').textContent) === 'Questions wait in step 2 · Place.');
    // 2. one tap on its own pile: a keep (db 'checked'), no move, next tile
    const [a, c2, c3] = [F[0], F[1], F[2]], homeA = s.home;
    await tap(page, page.locator('#cards .card').first().locator('.put'), touch); s = await S(page);
    ok(tag + ': one tap on its own pile keeps it (no move) and shows tile 2', s.checked[a] === homeA && !(a in s.moves) && s.s2Cur === c2, s.s2Cur + ' ' + JSON.stringify(s.checked));
    ok(tag + ': ...and it is back in its pile on step 1', s.inPiles.includes(a));
    // 3. a tap on another pile: a move, next tile; Undo brings it back to the tray as the shown tile
    const other = page.locator('#cards .card:not(.cur)').first(), to = await other.getAttribute('data-pile');
    await tap(page, other.locator('.put'), touch); s = await S(page);
    ok(tag + ': a tap on another pile moves it there and shows tile 3', s.moves[c2] === to && s.s2Cur === c3, s.s2Cur + ' ' + JSON.stringify(s.moves));
    await tap(page, page.locator('#undo'), touch); s = await S(page);
    ok(tag + ': Undo puts it back in the tray and shows it again', !(c2 in s.moves) && s.L.includes(c2) && s.s2Cur === c2, s.s2Cur);
    await saved(page); await page.waitForTimeout(500);
    ok(tag + ': the store has the keep and no move for either tile', store.docs.checked && store.docs.checked[a] && store.docs.checked[a].pile === homeA &&
       !(store.docs.moves && (store.docs.moves[a] || store.docs.moves[c2])), JSON.stringify(store.docs));
    // 4. step 1: the tray tile tap = "it was right"; the focus tile tap opens the large view with "keep" offered
    await tap(page, page.locator('#tab1'), touch); s = await S(page);
    ok(tag + ': step 1 line counts what still waits', s.note === LINE(N - 1), s.note);
    const tb = page.locator('#trayTiles [data-sid="' + c3 + '"]'); await tb.scrollIntoViewIfNeeded();
    const w4 = store.writes; await tap(page, tb, touch); s = await S(page);
    ok(tag + ': a tap on a question in the tray opens step 2 on it, and saves nothing', s.step === 2 && s.s2Cur === c3 && !s.checked[c3] && !(c3 in s.moves) && store.writes === w4,
       s.step + ' ' + s.s2Cur + ' ' + JSON.stringify(s.checked));
    await tap(page, page.locator('#s2Home'), touch); s = await S(page);
    ok(tag + ': ...where "It was right" keeps it', s.checked[c3] && !(c3 in s.moves) && !s.L.includes(c3), JSON.stringify(s.checked));
    await tap(page, page.locator('#tab1'), touch);
    const fi = F.indexOf(F[3]); await page.locator('#focusTiles .t').nth(fi).scrollIntoViewIfNeeded();
    const s4 = await S(page); await tap(page, page.locator('#focusTiles .t').nth(fi), touch); const s4b = await S(page);
    ok(tag + ': a tap on a waiting focus tile leaves it in the tray: nothing moves, no large view (owner rule R05)',
       await page.evaluate(() => document.getElementById('ctx').hidden) && JSON.stringify([s4.moves, s4.checked, s4.L]) === JSON.stringify([s4b.moves, s4b.checked, s4b.L]) &&
       /already in the tray/.test(await page.textContent('#save')), await page.textContent('#save'));
    await mock.hold(page, page.locator('#focusTiles .t').nth(fi));
    const cx = await page.evaluate(() => ({ hidden: document.getElementById('ctx').hidden, t: document.getElementById('ctxT').textContent,
      keep: document.getElementById('ctxKeep').hidden ? '' : document.getElementById('ctxKeep').textContent, out: document.getElementById('ctxOut').hidden }));
    ok(tag + ': a hold on a focus tile opens the large view (nothing moves)', !cx.hidden && cx.t.includes(F[3]) && cx.t.includes('waiting in step 2') &&
       JSON.stringify((await S(page)).moves) === JSON.stringify(s4.moves), cx.t);
    ok(tag + ': ...with "Right pile: keep it" and no "take out" (it is out already)', /Right pile: keep it in/.test(cx.keep) && cx.out, JSON.stringify(cx));
    await tap(page, page.locator('#ctxKeep'), touch); s = await S(page);
    ok(tag + ': "keep" in the large view answers it', s.checked[F[3]] && !s.L.includes(F[3]));
    await page.evaluate(() => document.getElementById('ctxClose').click()); await saved(page); await page.waitForTimeout(400);
    // 5. reload: answered tiles stay answered, the rest wait again, still nothing written by the reload itself
    const w0 = store.writes; await page.reload(); await page.waitForTimeout(1300); s = await S(page);
    ok(tag + ': after a reload answered tiles stay out of the tray, the rest wait', [a, c3, F[3]].every(x => !s.L.includes(x)) && s.L.includes(c2) && s.L.length === N - 3, s.L.join(','));
    ok(tag + ': after a reload it lands on step 2 again', s.step === 2);
    ok(tag + ': a reload writes nothing', store.writes === w0, store.writes - w0);
    ok(tag + ': no page errors', !errs.length, errs.join(' | '));
    await ctx.close();

    // 6. saved decisions from before (db): a move and a keep are never put back in the tray
    ({ ctx, store, page, errs } = await open(b, vp, 'tray.html', {}, st => {
      st.docs.moves = { p1_05: { sid: 'p1_05', from: 'X', to: 'Z', updated: '2026-10-08T10:00:00Z' } };
      st.docs.checked = { p1_02: { sid: 'p1_02', pile: 'Y', updated: '2026-10-08T10:00:00Z' } }; }));
    s = await S(page);
    ok(tag + ': saved move and keep are not re-trayed', !s.L.includes('p1_05') && !s.L.includes('p1_02') && s.L.length === N - 2, s.L.join(','));
    ok(tag + ': ...the moved tile is in its saved pile, the kept one in its own', s.inPiles.includes('p1_05') && s.inPiles.includes('p1_02') && s.moves.p1_05 === 'Z');
    ok(tag + ': ...and the load wrote nothing', store.writes === 0, store.writes);
    await ctx.close();
    // 6b. a question tile moved away, then put back in its own pile by hand: answered (a keep), never back in the tray; Undo undoes both
    ({ ctx, store, page, errs } = await open(b, vp, 'tray.html'));
    { const x = F[0], hx = await page.evaluate(s => homeOf[s], x);
      const away = page.locator('#cards .card:not(.cur)').first(), to2 = await away.getAttribute('data-pile');
      await tap(page, away.locator('.put'), touch);
      await page.evaluate(s => showCtx(s, pileOf(s)), x); await page.selectOption('#ctxDest', hx); await page.waitForTimeout(300); s = await S(page);
      ok(tag + ': moved away then put back home by hand: no keep, its question waits again', !s.checked[x] && !(x in s.moves) && s.L.includes(x), JSON.stringify(s.checked));
      await page.evaluate(() => document.getElementById('ctxUndo').click()); await page.waitForTimeout(300); s = await S(page);
      ok(tag + ': ...one Undo brings the move back', s.moves[x] === to2 && !(x in s.checked), JSON.stringify(s.moves) + ' ' + JSON.stringify(s.checked));
      await page.evaluate(() => document.getElementById('ctxClose').click()); await saved(page); await page.waitForTimeout(300);
      ok(tag + ': ...and the store holds no keep for it', !(store.docs.checked && store.docs.checked[x]), JSON.stringify(store.docs.checked || {}));
      ok(tag + ': ...no page errors', !errs.length, errs.join(' | ')); }
    await ctx.close();
    // 7. every question already answered in the store: back on step 1 once the store answers
    ({ ctx, store, page, errs } = await open(b, vp, 'tray.html', {}, st => {
      st.docs.checked = Object.fromEntries(F.map(x => [x, { sid: x, pile: '?', updated: '2026-10-08T10:00:00Z' }])); }));
    s = await S(page);
    ok(tag + ': all answered in the store: the page shows step 1, tray empty', s.step === 1 && !s.L.length, s.step + ' ' + s.L.length);
    ok(tag + ': ...and the focus line says they are answered', /^All \d+ of these signs are answered/.test(s.note), s.note);
    await ctx.close();
    // 8. browser-only storage (no db): a saved keep is not re-trayed either
    ({ ctx, store, page, errs } = await open(b, vp, 'tray.html', { nullDb: true, local: JSON.stringify({ checked: { p2_02: 'Z' }, moves: {} }) }));
    s = await S(page);
    ok(tag + ': browser-only storage: a saved keep is not re-trayed', !s.L.includes('p2_02') && s.L.length === N - 1, s.L.join(','));
    await ctx.close();
    // 9. the person touches the page before the store answers: the step is theirs
    ({ ctx, store, page, errs } = await (async () => { const ctx = await b.newContext(vp); const store = await mock.install(ctx, { connectMs: 1500 });
      store.docs.checked = Object.fromEntries(F.map(x => [x, { sid: x, pile: '?', updated: '2026-10-08T10:00:00Z' }]));
      const page = await ctx.newPage(); const errs = []; page.on('pageerror', e => errs.push(e.message));
      await page.goto('file://' + DIR + '/tray.html'); await page.waitForTimeout(300); return { ctx, store, page, errs }; })());
    const ld = await page.evaluate(() => ({ load: !document.getElementById('s2Load').hidden, work: !document.getElementById('s2Work').hidden, cards: document.querySelectorAll('#cards .card').length }));
    ok(tag + ': while the saved answers load, step 2 says so and shows no sign and no card', ld.load && !ld.work && !ld.cards, JSON.stringify(ld));
    await tap(page, page.locator('#s2Load'), touch); await page.waitForTimeout(1900); s = await S(page);
    ok(tag + ': after the person touched the page it does not switch step on its own', s.step === 2, s.step);
    ok(tag + ': ...and step 2 says every question is answered', await page.evaluate(() => !document.getElementById('s2Empty').hidden && document.getElementById('s2EmptyH').textContent) === 'All ' + N + ' questions answered.');
    await ctx.close();

    // 10. rank box: "Most useful first" tiles wait too, after the focus tiles
    ({ ctx, store, page, errs } = await open(b, vp, 'tray_rank.html'));
    const r = await page.evaluate(() => ({ L: outList(), F: (DATA.focus || []).map(f => f.sid), R: (DATA.rank || []).map(f => f.sid) }));
    const want = [...new Set(r.F.concat(r.R))];
    ok(tag + ': rank tiles wait in the tray after the focus tiles', JSON.stringify(r.L) === JSON.stringify(want) && r.R.some(x => !r.F.includes(x)), r.L.join(','));
    await tap(page, page.locator('#tab1'), touch);
    const rk = await page.evaluate(() => ({ shown: !document.getElementById('rank').hidden, note: document.getElementById('rankNote').textContent,
      go: !!document.querySelector('#rankNote .go'), cap: [...document.querySelectorAll('#rankTiles .fdone')].map(e => e.textContent) }));
    ok(tag + ': a rank box with tiles of its own stays, with its own waiting line and "→ waiting" captions', rk.shown && /^These \d+ signs are waiting in step 2 · Place/.test(rk.note) && rk.go &&
       rk.cap.length && rk.cap.every(c => c === '→ waiting in step 2'), JSON.stringify(rk));
    ok(tag + ': rank page: no page errors', !errs.length, errs.join(' | '));
    await ctx.close();
    ({ ctx, store, page, errs } = await open(b, vp, 'tray_rank_in.html'));
    ok(tag + ': a rank box that only repeats "Check these first" is not shown', await page.evaluate(() => document.getElementById('rank').hidden && (DATA.rank || []).length > 0));
    await ctx.close();

    // 12. loading: a saved move arrives late; nothing can be answered before it -- not even "Right pile: keep it" in a card opened by a
    // hold (round-2 check, 10 Oct 2026: a keep given meanwhile deleted the saved move it could not see yet); the saved move survives
    ({ ctx, store, page, errs } = await (async () => { const ctx = await b.newContext(vp); const store = await mock.install(ctx, { connectMs: 3000 });
      store.docs.moves = { [F[0]]: { sid: F[0], from: 'Y', to: 'Z', updated: '2026-10-08T10:00:00Z' }, [F[3]]: { sid: F[3], from: '?', to: 'Z', updated: '2026-10-08T10:00:00Z' } };
      const page = await ctx.newPage(); const errs = []; page.on('pageerror', e => errs.push(e.message));
      await page.goto('file://' + DIR + '/tray.html'); await page.waitForTimeout(500); return { ctx, store, page, errs }; })());
    s = await S(page);
    const l0 = await page.evaluate(() => ({ load: !document.getElementById('s2Load').hidden, work: !document.getElementById('s2Work').hidden, cards: document.querySelectorAll('#cards .card').length,
      tray: [...document.querySelectorAll('#trayTiles .t')].length, note: document.getElementById('focusNote').textContent }));
    ok(tag + ': loading: lands on step 2 saying "Loading your earlier answers", no sign, no card, nothing in the tray', s.step === 2 && l0.load && !l0.work && !l0.cards && !l0.tray && !s.L.length, JSON.stringify(l0));
    ok(tag + ': loading: the step-1 line says the answers are loading', l0.note === 'Loading your earlier answers…', l0.note);
    const kx = F[3], kh = await page.evaluate(x => homeOf[x], kx);
    await page.evaluate(() => { setStep(1); }); await page.evaluate(x => showCtx(x, pileOf(x)), kx); const w12 = store.writes; await tap(page, page.locator('#ctxKeep'), touch);
    const kmsg = await page.textContent('#ctxMsg'), kchk = await page.evaluate(x => checked[x] || null, kx);
    ok(tag + ': loading: "Right pile: keep it" in a card opened meanwhile saves nothing and says so', !kchk && store.writes === w12 && /Loading your earlier answers/.test(kmsg), kmsg);
    await page.evaluate(() => document.getElementById('ctxClose').click());
    await page.waitForTimeout(3200); await saved(page); await page.waitForTimeout(400); s = await S(page);
    ok(tag + ': loading: once in, the moved tiles do not wait (their saved moves win), the rest do', !s.L.includes(F[0]) && s.moves[F[0]] === 'Z' && !s.L.includes(kx) && s.moves[kx] === 'Z' && s.L.length === N - 2, s.L.join(','));
    ok(tag + ': the saved moves survive the loading window: the store holds both moves and no keep', (store.docs.moves || {})[kx] && store.docs.moves[kx].to === 'Z' && !(store.docs.checked || {})[kx] &&
       !(store.docs.checked || {})[F[0]], JSON.stringify(store.docs));
    ok(tag + ': loading: no page errors', !errs.length, errs.join(' | '));
    await ctx.close();

    // 12b. a tap before the saved answers are in writes nothing (adversarial check, 10 Oct 2026: on a no-tray page a "Check these
    // first" tap 0.7 s after load replaced a saved 'X' with 'OUT', and Undo then deleted it; a pile-tile tap did the same on both
    // layouts). Slow store (3.5 s), saved moves p2_02 -> X and p1_03 -> Y; tap both before ready; the store and the page keep them.
    for (const file of ['plain.html', 'tray.html']) {
      ({ ctx, store, page, errs } = await (async () => { const ctx = await b.newContext(vp); const store = await mock.install(ctx, { connectMs: 3500 });
        store.docs.moves = { p2_02: { sid: 'p2_02', from: '?', to: 'X', updated: '2026-10-08T10:00:00Z' }, p1_03: { sid: 'p1_03', from: '?', to: 'Y', updated: '2026-10-08T10:00:00Z' } };
        const page = await ctx.newPage(); const errs = []; page.on('pageerror', e => errs.push(e.message));
        await page.goto('file://' + DIR + '/' + file); await page.waitForTimeout(400); return { ctx, store, page, errs }; })());
      await page.evaluate(() => { if (step !== 1) setStep(1); });
      const early = await page.evaluate(() => ready); const w0 = store.writes;
      await tap(page, page.locator('#focusTiles > div[data-sid="p2_02"] .t'), touch);
      await tap(page, page.locator('#list .pile .t[data-sid="p1_03"]').first(), touch);
      const mid = await page.evaluate(() => ({ moves: { ...moves }, note: document.getElementById('save').textContent }));
      await page.waitForFunction(() => ready, null, { timeout: 10000 }).catch(() => {}); await page.waitForTimeout(800);
      const after = await page.evaluate(() => ({ moves: { ...moves } }));
      ok(tag + ': ' + file + ': taps before the saved answers are in move nothing and say so', !early && !mid.moves.p2_02 && !mid.moves.p1_03 && /Loading your earlier answers/.test(mid.note),
        'ready at tap ' + early + ', ' + JSON.stringify(mid));
      ok(tag + ': ' + file + ': ...the store and the page keep the earlier answers (p2_02 X, p1_03 Y), nothing written', store.docs.moves.p2_02.to === 'X' && store.docs.moves.p1_03.to === 'Y' &&
        after.moves.p2_02 === 'X' && after.moves.p1_03 === 'Y' && store.writes === w0, JSON.stringify(store.docs.moves) + ' writes ' + (store.writes - w0));
      ok(tag + ': ' + file + ': early taps: no page errors', !errs.length, errs.join(' | '));
      await ctx.close();
    }
    // 12c. a question in a pile the person already gave a verdict is decided: it does not wait in the tray again (owner rule R08: a
    // page re-rendered onto this layout after he had marked piles done brought their questions back); taking the verdict back does
    ({ ctx, store, page, errs } = await open(b, vp, 'tray.html', {}, st => {
      st.docs.piles = { X: { pile: 'X', verdict: 'same', merge_into: null, outliers: [], note: '', updated: '2026-10-08T10:00:00Z' } }; }));
    { const r = await page.evaluate(() => ({ L: outList(), inX: Object.keys(trayOrder).filter(s => homeOf[s] === 'X'), other: Object.keys(trayOrder).filter(s => homeOf[s] !== 'X') }));
      ok(tag + ': a question in a pile marked done does not wait; the others do', r.inX.length && r.inX.every(x => !r.L.includes(x)) && r.other.every(x => r.L.includes(x)), JSON.stringify(r));
      await page.evaluate(() => { state.X.verdict = null; render(); });
      const L2 = await page.evaluate(() => outList());
      ok(tag + ': ...and it waits again once the verdict is taken back', r.inX.every(x => L2.includes(x)), L2.join(','));
      ok(tag + ': verdict page: no page errors', !errs.length, errs.join(' | ')); }
    await ctx.close();
    // 12d. a merge is not such a verdict (round-2 check, 10 Oct 2026): "same sign as pile X" does not say whether an odd one out
    // belongs with the rest, so a saved merge leaves its questions waiting, and a merge made in step 2 (the name drag) never takes the
    // sign being answered, or any other, out of step 2
    ({ ctx, store, page, errs } = await open(b, vp, 'tray.html', {}, st => {
      st.docs.piles = { 'X-DOT': { pile: 'X-DOT', verdict: null, merge_into: 'X', outliers: [], note: '', updated: '2026-10-08T10:00:00Z' } }; }));
    { const r = await page.evaluate(() => ({ L: outList(), inXD: Object.keys(trayOrder).filter(s => homeOf[s] === 'X-DOT') }));
      ok(tag + ': a question in a pile saved as merged into another still waits', r.inXD.length && r.inXD.every(x => r.L.includes(x)), JSON.stringify(r));
      const m = await page.evaluate(() => { setStep(2); const q = Object.keys(trayOrder).find(s => preTrayed(s) && homeOf[s] !== 'X-DOT'); s2Cur = q; renderS2();
        const h = homeOf[q], to = basePiles.map(p => p.id).find(id => id !== h && !SPECIAL.has(id) && !(state[id] && state[id].merge_into)), before = outList().slice();
        mergePile(h, to); return { q, h, to, before, after: outList().slice(), cur: s2Cur, merged: state[h].merge_into }; });
      ok(tag + ': a merge in step 2 keeps every question waiting and the sign being answered on screen', m.merged === m.to && JSON.stringify(m.before) === JSON.stringify(m.after) && m.cur === m.q, JSON.stringify(m));
      ok(tag + ': merge page: no page errors', !errs.length, errs.join(' | ')); }
    await ctx.close();

    // 13. a question moved in step 2, taken out of that pile in step 1, tapped in the tray: back in the pile it came from, no keep
    ({ ctx, store, page, errs } = await open(b, vp, 'tray.html'));
    { const q = F[0], away = page.locator('#cards .card:not(.cur)').first(), to3 = await away.getAttribute('data-pile');
      await tap(page, away.locator('.put'), touch); await tap(page, page.locator('#tab1'), touch);
      const t = page.locator('#list .pile[data-pile="' + to3 + '"] .t[data-sid="' + q + '"]'); await t.scrollIntoViewIfNeeded(); await tap(page, t, touch);
      s = await S(page); ok(tag + ': taken out of the pile the person put it in', s.moves[q] === 'OUT', JSON.stringify(s.moves));
      const tt = page.locator('#trayTiles .t[data-sid="' + q + '"]'); await tt.scrollIntoViewIfNeeded(); await tap(page, tt, touch); await saved(page); await page.waitForTimeout(300);
      s = await S(page); ok(tag + ': a tray tap puts it back where it was taken from, and writes no keep', s.moves[q] === to3 && !s.checked[q] && !(store.docs.checked || {})[q] &&
        (store.docs.moves || {})[q] && store.docs.moves[q].to === to3, JSON.stringify(store.docs)); }
    await ctx.close();

    // 14. step 2 cards: a tap anywhere on a card places the sign (the middle is a picture); "View pile" opens the pile, places nothing
    ({ ctx, store, page, errs } = await open(b, vp, 'tray.html'));
    { s = await S(page); const q = s.s2Cur, hq = s.home;
      const vp0 = await page.locator('#cards .card').nth(1).getAttribute('data-pile');
      await page.locator('#cards .card').nth(1).locator('.vw').scrollIntoViewIfNeeded(); await tap(page, page.locator('#cards .card').nth(1).locator('.vw'), touch);
      const cv = await page.evaluate(() => ({ open: !document.getElementById('ctx').hidden, t: document.getElementById('ctxT').textContent }));
      s = await S(page); ok(tag + ': "View pile" opens that pile and places nothing', cv.open && cv.t.includes(vp0) && s.s2Cur === q && !Object.keys(s.moves).length && !Object.keys(s.checked).length, JSON.stringify(cv));
      await page.evaluate(() => document.getElementById('ctxClose').click()); await page.waitForTimeout(200);
      const cur = page.locator('#cards .card.cur'); await cur.scrollIntoViewIfNeeded();
      const hit = await cur.evaluate(c => { const r = c.querySelector('.smp img').getBoundingClientRect(); const x = r.left + r.width / 2, y = r.top + r.height / 2; const e = document.elementFromPoint(x, y); return { x, y, img: e && e.tagName === 'IMG' }; });
      if (touch) await page.touchscreen.tap(hit.x, hit.y); else await page.mouse.click(hit.x, hit.y); await page.waitForTimeout(400);
      s = await S(page); const dlg = await page.evaluate(() => !document.getElementById('ctx').hidden);
      ok(tag + ': a ' + (touch ? 'tap' : 'mouse click') + ' on a picture in the middle of its own pile card keeps the sign there (no dialog)', hit.img && s.checked[q] === hq && !dlg && s.s2Cur !== q, JSON.stringify({ hit, dlg, c: s.checked })); }
    await ctx.close();

    // 15. a cluster move that brings a question tile home writes no keep; the offer names the sign it is about
    ({ ctx, store, page, errs } = await open(b, vp, 'cluster_tray.html'));
    { const q = 'p1_02';
      await page.evaluate(q => { s2Cur = q; renderS2(); }, q); await page.waitForTimeout(200);
      await page.evaluate(() => place('X')); await page.waitForTimeout(300);
      const sib = await page.evaluate(q => (clusterMembers[clusterOf[q]] || []).find(x => x !== q && homeOf[x] === homeOf[q] && !trayOrder[x]), q);
      if (sib){
        await page.evaluate(x => { showCtx(x, pileOf(x)); ctxMove('X'); }, sib); await page.waitForTimeout(200);
        await page.evaluate(x => { hideOffer(); showCtx(x, 'X'); ctxMove(homeOf[x]); }, sib); await page.waitForTimeout(200);
        const o = await page.evaluate(() => ({ shown: !document.getElementById('offer').hidden, t: document.getElementById('offerT').textContent, no: document.getElementById('offerNo').textContent,
          rest: offerState && offerState.rest }));
        ok(tag + ': the cluster offer names the sign it is about ("The sign you just put in ..."), "No, only that one"', o.shown && /^The sign you just put in /.test(o.t) && o.no === 'No, only that one', JSON.stringify(o));
        if (o.shown && o.rest.includes(q)){ await page.evaluate(() => document.getElementById('offerYes').click()); await saved(page); await page.waitForTimeout(300); s = await S(page);
          ok(tag + ': a cluster move bringing a question home writes no keep: it waits again', !s.checked[q] && !(store.docs.checked || {})[q] && s.L.includes(q), JSON.stringify(store.docs.checked || {})); }
        else ok(tag + ': (cluster fixture: the question tile was not in the offer)', true);
      } else ok(tag + ': (cluster fixture: no sibling in the question\'s shape group)', true);
      ok(tag + ': cluster page: no page errors', !errs.length, errs.join(' | ')); }
    await ctx.close();
    // 11. --no-focus-to-tray: the old layout
    ({ ctx, store, page, errs } = await open(b, vp, 'plain.html'));
    s = await S(page);
    ok(tag + ': --no-focus-to-tray: option off, step 1, tray empty', s.opts && s.opts.focusToTray === false && s.step === 1 && !s.L.length, s.step + ' ' + s.L.length);
    ok(tag + ': --no-focus-to-tray: focus tiles in their piles with a "?"', F.every(x => s.inPiles.includes(x)) &&
       await page.evaluate(F => F.every(x => { const t = document.querySelector('#list .pile .t.fq[data-sid="' + x + '"]'); return t && t.querySelector('.badge').textContent === '?'; }), F));
    ok(tag + ': --no-focus-to-tray: the focus instructions say the one rule (tap = to the tray, hold = its card) and point at the "?" tiles',
       /^Tap a sign: it goes to the “Taken out” tray \(tap it there to put it back\)/.test(s.note) && /Hold a sign: its card opens/.test(s.note) && /double frame and a "\?"/.test(s.note) && s.tapHidden, s.note);
    ok(tag + ': --no-focus-to-tray: no page errors', !errs.length, errs.join(' | '));
    await ctx.close();
  }
  await b.close();
  console.log(fails ? fails + ' FAILED' : 'ALL PASS'); process.exit(fails ? 1 : 0);
})();
