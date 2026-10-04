// Step 2 keeps the sign, its line and the action buttons frozen at the top while the pile cards scroll (owner, 4 Oct 2026),
// on a phone and on a desktop.
// Run: PW_EXE=/opt/pw-browsers/chromium NODE_PATH=$(npm root -g) node test_s2_sticky.js PAGE.html SHOT.png
const { chromium } = require('playwright'); const mock = require('./mock_db');
(async () => {
  const browser = await chromium.launch({ executablePath: process.env.PW_EXE || undefined }); const res = {}; const errs = [];
  for (const [tag, o] of [['phone', { viewport: { width: 390, height: 760 }, isMobile: true, hasTouch: true }], ['desk', { viewport: { width: 1280, height: 800 } }]]) {
    const ctx = await browser.newContext(o); await mock.install(ctx); const page = await ctx.newPage(); page.on('pageerror', e => errs.push(e.message));
    await page.goto('file://' + process.argv[2]); await page.waitForTimeout(1000);
    for (let i = 0; i < 4; i++) await page.evaluate(i => { const t = document.querySelectorAll('#list .t')[i]; t && t.click(); }, i);
    await page.evaluate(() => { const L = document.querySelectorAll('#list .t'); for (let i = 0; i < Math.min(12, L.length); i++) L[i].click(); });
    await page.click('#trayGo'); await page.waitForTimeout(600);
    await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight)); await page.waitForTimeout(300);
    const r = await page.evaluate(() => { const s = document.getElementById('s2Stick').getBoundingClientRect(), b = document.querySelector('.bar').getBoundingClientRect();
      const btn = document.getElementById('s2New').getBoundingClientRect(); const st = document.getElementById('s2Stick'); st.style.position = 'static'; const nat = st.getBoundingClientRect().top + scrollY; st.style.position = '';
      return { top: s.top, bottom: s.bottom, bar: b.bottom, btnTop: btn.top, vh: innerHeight, sy: scrollY, engaged: scrollY > nat - b.bottom }; });
    res[tag] = (r.engaged ? (r.top >= r.bar - 2 && r.top <= r.bar + 30) : true) && r.btnTop > r.top && r.bottom - r.top < r.vh * 0.5;
    console.log(tag, r);
    if (tag === 'phone') await page.screenshot({ path: process.argv[3] });
    await ctx.close();
  }
  console.log(res, 'errors:', errs); const ok = res.phone && res.desk && !errs.length;
  console.log(ok ? 'ALL PASS' : 'FAILED'); await browser.close(); process.exit(ok ? 0 : 1);
})().catch(e => { console.error(e); process.exit(1); });
