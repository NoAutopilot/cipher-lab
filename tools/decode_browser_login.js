#!/usr/bin/env node
// DECODE (de-crypt.org) login through a real browser, for the case where the plain form POST is never evaluated by
// the server (page re-rendered with IS_LOGGEDIN:false and no "Incorrect user name or password" message, 20-24 Sept
// 2026). The site's login button is disabled until its JavaScript initialises, so a browser submission is the
// form's own submission. Credentials come from DECODE_USER / DECODE_PASS and are never printed or written.
//
//   NODE_PATH=$(npm root -g) node tools/decode_browser_login.js RECORD_ID OUT_DIR [--shot OUT.png]
//
// Prints one JSON line: {loggedIn, url, title, incorrectMessage, saved}. On success it saves RecordsView/RECORD_ID
// as OUT_DIR/record_RECORD_ID.html. Session cookies live only in the in-memory browser context. Exit 0 on login,
// 4 on a rejected login, 1 on an error. One attempt per run; do not loop it (CLAUDE.md single-attempt rule).
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
if (args.length < 2) { console.error('usage: decode_browser_login.js RECORD_ID OUT_DIR [--shot OUT.png]'); process.exit(2); }
const [recordId, outDir] = args;
const shotIdx = args.indexOf('--shot');
const shot = shotIdx > -1 ? args[shotIdx + 1] : null;
const user = process.env.DECODE_USER, pass = process.env.DECODE_PASS;
if (!user || !pass) { console.error('DECODE_USER/DECODE_PASS: unset'); process.exit(2); }

const BASE = 'https://de-crypt.org/decrypt-web';
const exe = process.env.CHROMIUM_PATH || (fs.existsSync('/opt/pw-browsers/chromium') ? '/opt/pw-browsers/chromium' : undefined);

(async () => {
  const browser = await chromium.launch({ executablePath: exe, headless: true, args: ['--no-sandbox', '--disable-gpu'] });
  const ctx = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36',
    viewport: { width: 1280, height: 1200 }, locale: 'en-GB',
  });
  const page = await ctx.newPage();
  const out = { loggedIn: false, url: null, title: null, incorrectMessage: false, saved: null };
  try {
    await page.goto(`${BASE}/login`, { waitUntil: 'networkidle', timeout: 60000 });
    await page.fill('input[name="username"]', user);
    await page.fill('input[name="password"]', pass);
    const btn = page.locator('button[type="submit"], input[type="submit"], #btn-submit, button[name="btn-submit"]').first();
    await btn.waitFor({ state: 'visible', timeout: 15000 });
    await page.waitForFunction(() => {
      const b = document.querySelector('button[type="submit"], input[type="submit"], #btn-submit, button[name="btn-submit"]');
      return b && !b.disabled;
    }, null, { timeout: 15000 }).catch(() => {});
    await Promise.all([
      page.waitForLoadState('networkidle', { timeout: 60000 }).catch(() => {}),
      btn.click(),
    ]);
    await page.waitForTimeout(1500);
    const html = await page.content();
    out.url = page.url(); out.title = await page.title();
    out.loggedIn = /"IS_LOGGEDIN":true/.test(html);
    out.incorrectMessage = /incorrect user name or password/i.test(html);
    if (shot) await page.screenshot({ path: shot, fullPage: true });
    if (out.loggedIn) {
      fs.mkdirSync(outDir, { recursive: true });
      await page.goto(`${BASE}/RecordsView/${recordId}`, { waitUntil: 'networkidle', timeout: 60000 });
      const f = path.join(outDir, `record_${recordId}.html`);
      fs.writeFileSync(f, await page.content());
      out.saved = f;
    }
    console.log(JSON.stringify(out));
    process.exitCode = out.loggedIn ? 0 : 4;
  } catch (e) {
    console.error('decode_browser_login failed:', e.message.split('\n')[0]);
    process.exitCode = 1;
  } finally {
    await browser.close();
  }
})();
