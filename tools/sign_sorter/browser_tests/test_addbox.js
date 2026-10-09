// Add a missed sign / split a merged box (MQS-SORTER-BOX, 9 Oct 2026). In "Fix the cut": narrow the box and press "Split" ->
// db recuts doc for the tile (the kept part) + db added doc kind 'split' for the rest of the starting box; move the box and
// press "Add as a missed sign" -> db added doc kind 'missed', the tile's recut unchanged; Undo removes the last added box;
// a reload keeps the added boxes.   node test_addbox.js plain.html [shot]
const { chromium } = require('playwright'); const mock = require('./mock_db');
const box = page => page.evaluate(() => fix ? fix.box.slice() : null);
async function edgePoint(page, which) {
  return page.evaluate(w => { const c = document.getElementById('ctxC'), m = c._map, r = c.getBoundingClientRect(), [x, y, bw, bh] = fix.box;
    const sx = w === 'r' ? x + bw : x + bw / 2, sy = y + bh / 2;
    return [r.left + ((sx * m.ps - m.x0) * m.s) / m.k, r.top + ((sy * m.ps - m.y0) * m.s + m.ha) / m.k]; }, which);
}
async function dragBy(page, [x, y], dx, dy) {
  await mock.gesture(page, 'down', x, y);
  for (let i = 1; i <= 8; i++) { await mock.gesture(page, 'move', x + dx * i / 8, y + dy * i / 8); await page.waitForTimeout(16); }
  await mock.gesture(page, 'up', x + dx, y + dy); await page.waitForTimeout(100);
}
(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_EXE }); const res = []; const errs = [];
  const ok = (name, cond, extra) => { res.push([name, !!cond]); console.log((cond ? 'ok   ' : 'FAIL ') + name, extra === undefined ? '' : JSON.stringify(extra)); };
  const ctx = await b.newContext({ viewport: { width: 1200, height: 900 } }); const store = await mock.install(ctx); const page = await ctx.newPage();
  page.on('pageerror', e => errs.push(e.message)); await page.goto('file://' + process.argv[2]); await page.waitForTimeout(1200);
  const t = page.locator('#pile__88_ .tiles .t').nth(1); const sid = await t.getAttribute('data-sid');
  const b0 = await page.evaluate(s => itemBySid[s].b.slice(), sid);
  await mock.hold(page, t); await page.click('#ctxFix'); await page.waitForTimeout(200);
  // split: drag the right edge left (the kept part is the left), then Split
  const px = await page.evaluate(() => { const m = document.getElementById('ctxC')._map; return m.s * m.ps / m.k; });   // screen px per source px
  await dragBy(page, await edgePoint(page, 'r'), -Math.round(b0[2] * 0.45 * px), 0); const b1 = await box(page);
  ok('split: right edge dragged in', b1[2] < b0[2] - 2 && b1[0] === b0[0], { b0, b1 });
  await page.click('#fixSplit'); await page.waitForTimeout(900);
  const rc = (store.docs.recuts || {})[sid], ad = Object.values(store.docs.added || {});
  ok('split: the kept part saved as the tile\'s recut', rc && [rc.x, rc.y, rc.w, rc.h].join() === b1.join(), rc);
  const sp = ad.find(d => d.kind === 'split');
  ok('split: the rest saved as an added box (from the kept right edge to the first right edge, full height)',
     sp && sp.from === sid && sp.id === sid + '+1' && sp.x === b1[0] + b1[2] && sp.w === b0[0] + b0[2] - sp.x && sp.y === b0[1] && sp.h === b0[3] && sp.page, sp);
  // missed: move the box right past the tile and add it; the tile's recut stays
  await page.click('#ctxFix'); await page.waitForTimeout(200);
  await dragBy(page, await edgePoint(page, 'c'), Math.round(b0[2] * 1.2 * px), 0); const b2 = await box(page);
  await page.click('#fixAdd'); await page.waitForTimeout(900);
  const ms = Object.values(store.docs.added || {}).find(d => d.kind === 'missed'), rc2 = (store.docs.recuts || {})[sid];
  ok('missed: added box saved where the box was moved', ms && ms.id === sid + '+2' && [ms.x, ms.y, ms.w, ms.h].join() === b2.join(), { ms, b2 });
  ok('missed: the tile\'s own cut unchanged', rc2 && [rc2.x, rc2.y, rc2.w, rc2.h].join() === b1.join());
  await page.click('#ctxFix'); await page.waitForTimeout(200);
  ok('the editor lists the signs added from this tile', /2 signs added from this tile/.test(await page.textContent('#fixAddN')), await page.textContent('#fixAddN'));
  await page.click('#fixCancel'); await page.waitForTimeout(100);
  await page.click('#ctxUndo'); await page.waitForTimeout(900);
  const ids = Object.values(store.docs.added || {}).map(d => d.id);
  ok('undo removes the last added box only', ids.length === 1 && ids[0] === sid + '+1', ids);
  await page.reload(); await page.waitForTimeout(1500);
  const n = await page.evaluate(() => Object.keys(added).length);
  ok('reload keeps the added box', n === 1, n);
  if (process.argv[3]) { await store.dump(process.argv[3] + '_db'); await page.screenshot({ path: process.argv[3] + '.png' }); }
  console.log('errors:', errs); await b.close();
  const bad = res.filter(r => !r[1]).length; console.log(bad ? bad + ' FAILED' : 'all ' + res.length + ' passed'); process.exit(bad || errs.length ? 1 : 0);
})();
