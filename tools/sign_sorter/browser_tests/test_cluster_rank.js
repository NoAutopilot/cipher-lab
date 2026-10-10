// TX-SORTER (3 Oct 2026): "Most useful first" box, cluster offer after a one-tile move, cluster doc saved, undo removes it.
// Run: PW_EXE=/opt/pw-browsers/chromium... NODE_PATH=$(npm root -g) node test_cluster_rank.js PAGE.html SHOT.png
const { chromium } = require('playwright'); const mock = require('./mock_db');   // mock.hold: a ranked tile's card opens on a hold (owner rule R05)
(async () => { const b = await chromium.launch({ executablePath: process.env.PW_EXE }); const page = await b.newPage({viewport:{width:1200,height:900}});
  const errs = []; page.on('pageerror', e => errs.push(e.message));
  await page.addInitScript(() => {   // in-memory db stand-in that records every write
    window.__w = []; const mk = name => ({ doc: id => ({ set: async d => { window.__w.push([name, 'set', id, d]); }, delete: async () => { window.__w.push([name, 'del', id]); } }),
      // an empty first snapshot, as the real store sends: the page takes no move until its saved answers are in (template 2026-10-09.5)
      onSnapshot: fn => { setTimeout(() => fn({ docs: [], size: 0, empty: true, metadata: { fromCache: false, hasPendingWrites: false }, docChanges: () => [] }), 0); return () => {}; } });
    window.claude = { use: async () => ({ collection: mk }) }; });
  await page.goto('file://' + process.argv[2]); await page.waitForTimeout(500);
  const nr = await page.locator('#rankTiles .t').count(); console.log('rank tiles:', nr);
  // pick a ranked tile whose cluster has siblings, open it, move it to another pile
  const sid = await page.evaluate(() => (DATA.rank.find(r => clusterOf[r.sid] && clusterMembers[clusterOf[r.sid]].length > 1) || {}).sid);
  const i = await page.evaluate(s => DATA.rank.findIndex(r => r.sid === s), sid);
  await mock.hold(page, page.locator('#rankTiles .t').nth(i));
  const dest = await page.evaluate(s => [...document.getElementById('ctxDest').options].map(o => o.value).filter(v => v && v !== homeOf[s])[0], sid);
  await page.selectOption('#ctxDest', dest);
  const offer = await page.isVisible('#offer'); console.log('offer shown:', offer, await page.textContent('#offerT'));
  await page.click('#offerYes'); await page.waitForTimeout(200);
  const r = await page.evaluate(([s, d]) => { const c = clusterOf[s]; return { c, all: clusterMembers[c].every(x => (moves[x] || homeOf[x]) === d),
    doc: window.__w.filter(w => w[0] === 'clusters' && w[1] === 'set').map(w => w[3]) }; }, [sid, dest]);
  console.log('cluster all moved:', r.all, 'cluster docs:', JSON.stringify(r.doc.map(d => [d.cluster, d.to, d.n])));
  await page.screenshot({ path: process.argv[3] });
  await page.click('#ctxUndo'); await page.waitForTimeout(200);
  const after = await page.evaluate(c => ({ dec: !!clusterDec[c], del: window.__w.some(w => w[0] === 'clusters' && w[1] === 'del') }), r.c);
  console.log('undo removes decision:', !after.dec && after.del);
  const ok = nr > 0 && offer && r.all && r.doc.length === 1 && !after.dec && after.del && !errs.length;
  console.log('errors:', errs); console.log(ok ? 'ALL PASS' : 'FAILED'); await b.close(); process.exit(ok ? 0 : 1); })();
