// A stand-in for claude.use('db') that behaves like the real store (runtime contract 0.2.66 db.d.ts), for the sign
// sorter browser tests (QA pass, 3 Oct 2026). The old tests mocked `use: async () => null` or a write-only recorder,
// which hid every save/load bug. This one:
//   - keeps the documents on the Node side, so they survive page.reload() (a real persistent store);
//   - resolves use('db') late (opts.connectMs, default 600 ms: the real one never answers in the script's first run);
//   - delivers snapshots with real docChanges(): first snapshot all 'added', then added/modified/removed, a removed
//     change carrying the last body; own writes echo at once (hasPendingWrites) and again when confirmed;
//   - confirms writes after a random latency (opts.minMs..opts.maxMs), so two overlapping writes to one document can
//     land out of order -- the contract says "one write at a time per document", and a page that ignores it loses data;
//   - rejects a write with {code, message} when the test calls store.failNext(n);
//   - store.external(page, c, id, body) plays another device's write into the page's snapshots.
// Usage: const db = require('./mock_db'); const store = await db.install(context, {minMs: 50, maxMs: 400});
//        store.docs -> {collection: {id: body}};  store.dump(dir) writes DIR/<collection>/<id>.json for sign_sorter_apply.py.
const fs = require('fs'), path = require('path');

async function install(target, opts = {}) {
  const o = Object.assign({ connectMs: 600, minMs: 40, maxMs: 300, nullDb: false }, opts);
  const store = { docs: {}, fail: 0, writes: 0, failNext(n = 1) { this.fail = n; },
    // another viewer (or the same person on a second device) writes a document; the page hears it on its next refresh
    async external(page, c, id, body) { this.docs[c] = this.docs[c] || {}; if (body === null) delete this.docs[c][id]; else this.docs[c][id] = body;
      await page.evaluate(cc => window.__mockDb.refresh(cc), c); },
    dump(dir) { fs.rmSync(dir, { recursive: true, force: true });
      for (const [c, ds] of Object.entries(this.docs)) { fs.mkdirSync(path.join(dir, c), { recursive: true });
        for (const [id, d] of Object.entries(ds)) fs.writeFileSync(path.join(dir, c, id + '.json'), JSON.stringify(d)); } } };
  await target.exposeBinding('__dbWrite', (_src, c, id, body) => {   // body null = delete; returns error text or ''
    store.writes++;
    if (store.fail > 0) { store.fail--; return 'unavailable'; }
    store.docs[c] = store.docs[c] || {};
    if (body === null) delete store.docs[c][id]; else store.docs[c][id] = JSON.parse(body);
    return '';
  });
  await target.exposeBinding('__dbRead', (_src, c) => JSON.stringify(store.docs[c] || {}));
  await target.addInitScript(o2 => {
    const listeners = {};            // collection -> [{fn, seen: {id: frozen body}}]
    const pending = {};              // collection -> {id: body|null} own unconfirmed writes (latency compensation)
    const server = {};               // collection -> last server view {id: body}
    const view = c => { const v = Object.assign({}, server[c] || {}); Object.entries(pending[c] || {}).forEach(([id, b]) => { if (b === null) delete v[id]; else v[id] = b; }); return v; };
    const deliver = (c, hasPending) => (listeners[c] || []).forEach(L => {
      const v = view(c), ch = [];
      Object.keys(v).forEach(id => { if (!(id in L.seen)) ch.push({ type: 'added', id, body: v[id] });
        else if (JSON.stringify(L.seen[id]) !== JSON.stringify(v[id])) ch.push({ type: 'modified', id, body: v[id] }); });
      Object.keys(L.seen).forEach(id => { if (!(id in v)) ch.push({ type: 'removed', id, body: L.seen[id] }); });
      L.seen = v;
      if (!ch.length && !L.first) return; L.first = false;
      const snap = d => Object.freeze({ id: d.id, exists: true, data: () => Object.freeze(JSON.parse(JSON.stringify(d.body))), metadata: { fromCache: false, hasPendingWrites: !!hasPending } });
      const docs = Object.entries(v).map(([id, body]) => snap({ id, body }));
      try { L.fn({ docs, size: docs.length, empty: !docs.length, metadata: { fromCache: false, hasPendingWrites: !!hasPending },
        docChanges: () => ch.map(x => ({ type: x.type, doc: snap(x), oldIndex: -1, newIndex: -1 })) }); } catch (e) { setTimeout(() => { throw e; }); }
    });
    const refresh = async c => { server[c] = JSON.parse(await window.__dbRead(c)); deliver(c, false); };
    const write = (c, id, body) => {
      (pending[c] = pending[c] || {})[id] = body; deliver(c, true);
      const lo = body !== null && o2.setMinMs != null ? o2.setMinMs : o2.minMs, hi = body !== null && o2.setMaxMs != null ? o2.setMaxMs : o2.maxMs;
      const ms = lo + Math.random() * (hi - lo);   // setMinMs/setMaxMs: a slow set overtaken by a quick delete (move, then undo)
      return new Promise((res, rej) => setTimeout(async () => {
        const err = await window.__dbWrite(c, id, body === null ? null : JSON.stringify(body));
        if (pending[c] && pending[c][id] === body) delete pending[c][id];
        await refresh(c);
        if (err) rej({ code: err, message: 'the store is unavailable (test)' }); else res();
      }, ms));
    };
    const ID = /^[A-Za-z0-9_\-.~:@+]{1,200}$/;
    const db = { collection: c => ({ path: c,
      doc: id => { if (!ID.test(id) || id === '.' || id === '..') throw new TypeError('bad doc id ' + id);
        return { id, set: d => { if (!d || typeof d !== 'object') return Promise.reject({ code: 'invalid_argument', message: 'body' }); return write(c, id, JSON.parse(JSON.stringify(d))); },
          delete: () => write(c, id, null) }; },
      onSnapshot: (fn, err) => { const L = { fn, err, seen: {}, first: true }; (listeners[c] = listeners[c] || []).push(L);
        setTimeout(() => refresh(c), 20); return () => { listeners[c] = listeners[c].filter(x => x !== L); }; } }) };
    window.__mockDb = { pending, server, refresh };
    window.claude = { use: name => new Promise(r => setTimeout(() => r(name === 'db' && !o2.nullDb ? db : null), o2.connectMs)) };
  }, o);
  return store;
}
// Gestures for the two-step sorter. On a touch context they go through CDP touch events (real pointerType 'touch',
// the path a phone takes); otherwise through the mouse.
async function touchOrMouse(page, kind, x, y) {
  if (page.__touch === undefined) page.__touch = await page.evaluate(() => navigator.maxTouchPoints > 0);
  if (page.__touch) { const cdp = page.__cdp || (page.__cdp = await page.context().newCDPSession(page));
    const type = { down: 'touchStart', move: 'touchMove', up: 'touchEnd' }[kind];
    await cdp.send('Input.dispatchTouchEvent', { type, touchPoints: kind === 'up' ? [] : [{ x, y }] }); return; }
  if (kind === 'down') { await page.mouse.move(x, y); await page.mouse.down(); } else if (kind === 'move') await page.mouse.move(x, y); else await page.mouse.up();
}
async function hold(page, locator, ms = 650) {   // press and hold, then let go
  await locator.evaluate(e => e.scrollIntoView({ block: 'center' })); await page.waitForTimeout(150);   // centred, so not under the fixed tray
  const b = await locator.boundingBox(); const x = b.x + b.width / 2, y = b.y + b.height / 2;
  await touchOrMouse(page, 'down', x, y); await page.waitForTimeout(ms); await touchOrMouse(page, 'up', x, y); await page.waitForTimeout(150);
}
async function drag(page, from, to) {            // drag one element onto another, in small steps
  await to.evaluate(e => e.scrollIntoView({ block: 'center' })); await page.waitForTimeout(150);
  await to.evaluate(e => { for (let i = 0; i < 20; i++) {   // centred may still sit under a frozen header (phone step 2): scroll until the centre is the element's own
    const r = e.getBoundingClientRect(), h = document.elementFromPoint(r.left + r.width / 2, r.top + r.height / 2);
    if (!h || e.contains(h)) return; window.scrollBy(0, -60); } });
  await page.waitForTimeout(100);
  const a = await from.boundingBox(), b = await to.boundingBox();
  const x0 = a.x + a.width / 2, y0 = a.y + a.height / 2, x1 = b.x + b.width / 2, y1 = b.y + b.height / 2;
  await touchOrMouse(page, 'down', x0, y0);
  for (let i = 1; i <= 12; i++) { await touchOrMouse(page, 'move', x0 + (x1 - x0) * i / 12, y0 + (y1 - y0) * i / 12); await page.waitForTimeout(16); }
  await touchOrMouse(page, 'up', x1, y1); await page.waitForTimeout(150);
}
module.exports = { install, hold, drag, gesture: touchOrMouse };
