const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ executablePath: process.env.PW_EXE || undefined });
  const page = await browser.newPage({ viewport: { width: 1200, height: 900 } });
  // Mock claude.use('db'): async writes with latency; snapshots echo every committed write to listeners.
  await page.addInitScript(() => {
    const store = {}; const listeners = {};
    const emit = (c) => (listeners[c] || []).forEach(fn => fn(snapOf(c, true)));
    const snapOf = (c) => { const docs = Object.entries(store[c] || {}).map(([id, d]) => ({ id, exists: true, data: () => d }));
      return { docs, size: docs.length, empty: !docs.length, docChanges: () => docs.map(doc => ({ type: 'modified', doc })), metadata: {} }; };
    const db = { collection: (c) => ({
      doc: (id) => ({
        set: (d) => new Promise(r => setTimeout(() => { (store[c] ||= {})[id] = JSON.parse(JSON.stringify(d)); emit(c); r(); }, 150)),
        delete: () => new Promise(r => setTimeout(() => { delete (store[c] ||= {})[id]; emit(c); r(); }, 150)) }),
      onSnapshot: (fn) => { (listeners[c] ||= []).push(fn); setTimeout(() => fn(snapOf(c)), 10); return () => {}; } }) };
    window.__store = store;
    window.claude = { use: async (n) => n === 'db' ? db : null };
  });
  await page.goto('file://' + process.argv[2]);
  await page.waitForTimeout(500);
  const xPile = page.locator('.pile').filter({ has: page.locator('.pid', { hasText: /^X$/ }) }).first();
  const tiles = xPile.locator('.tiles .t');
  console.log('X tiles:', await tiles.count());
  for (let i = 0; i < 8; i++) { await xPile.locator('.tiles .t').nth(i).click(); }   // rapid selection
  console.log('selected badges:', await xPile.locator('.t.sel').count(), '| bar:', await xPile.locator('.movebar strong').textContent());
  await xPile.locator('.movebar button', { hasText: 'Set aside' }).click();
  await page.waitForTimeout(800);
  console.log('stored moves:', Object.keys(await page.evaluate(() => window.__store.moves || {})).length);
  console.log('X header:', await xPile.locator('.cnt').textContent());
  // select 3 more and create a new pile
  for (let i = 0; i < 3; i++) await xPile.locator('.tiles .t:not(.out)').nth(i).click();
  await xPile.locator('.movebar input').fill('x 2bars');
  await xPile.locator('.movebar button', { hasText: 'New pile' }).click();
  await page.waitForTimeout(800);
  const st = await page.evaluate(() => ({ moves: window.__store.moves, np: window.__store.newpiles }));
  console.log('new piles:', Object.keys(st.np || {}), '| moves to X-2BARS:', Object.values(st.moves).filter(m => m.to === 'X-2BARS').length,
              '| ASIDE:', Object.values(st.moves).filter(m => m.to === 'ASIDE').length);
  const np = page.locator('.pile').filter({ has: page.locator('.pid', { hasText: /^X-2BARS$/ }) });
  console.log('new pile shows tiles:', await np.locator('.t').count(), '| moved-in badges:', await np.locator('.badge').count());
  // verdict button
  await xPile.locator('.acts button', { hasText: 'All one sign' }).click(); await page.waitForTimeout(600);
  console.log('X verdict stored:', await page.evaluate(() => window.__store.piles.X.verdict), '| status:', await page.locator('#save').textContent());
  await page.screenshot({ path: process.argv[3], clip: { x: 0, y: 0, width: 1200, height: 900 } });
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
