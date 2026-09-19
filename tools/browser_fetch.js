#!/usr/bin/env node
// Fetch pages with the real Chromium that Claude Code containers ship, for sites that refuse curl
// (JavaScript challenges, Cloudflare checks, HathiTrust, PARES, Spink, TNA Discovery pages).
//
//   NODE_PATH=$(npm root -g) node tools/browser_fetch.js URL OUT.html [--shot OUT.png] [--pdf OUT.pdf]
//        [--wait 3000] [--selector "css"] [--click "css"] [--type "css=text"] [--ua "..."]
//
// Saves the rendered HTML after network idle plus the optional wait. --selector waits for that element.
// --type fills a field and presses Enter (for search boxes); --click clicks before saving.
// Exit code 0 on success; the final URL and title are printed to stdout.
const { chromium } = require('playwright');
const fs = require('fs');

const args = process.argv.slice(2);
if (args.length < 2) { console.error('usage: browser_fetch.js URL OUT.html [options]'); process.exit(2); }
const [url, out] = args;
const opt = (k, d) => { const i = args.indexOf(k); return i > -1 ? args[i + 1] : d; };
const has = (k) => args.includes(k);

(async () => {
  const browser = await chromium.launch({
    executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium',
    args: ['--no-sandbox', '--disable-gpu'],
  });
  const ctx = await browser.newContext({
    userAgent: opt('--ua', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'),
    viewport: { width: 1280, height: 1800 },
    locale: 'en-GB',
  });
  const page = await ctx.newPage();
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await page.waitForLoadState('networkidle', { timeout: 60000 }).catch(() => {});
    const typeArg = opt('--type', null);
    if (typeArg) {
      const eq = typeArg.indexOf('=');
      await page.fill(typeArg.slice(0, eq), typeArg.slice(eq + 1));
      await page.keyboard.press('Enter');
      await page.waitForLoadState('networkidle', { timeout: 60000 }).catch(() => {});
    }
    const clickSel = opt('--click', null);
    if (clickSel) { await page.click(clickSel); await page.waitForLoadState('networkidle', { timeout: 60000 }).catch(() => {}); }
    const sel = opt('--selector', null);
    if (sel) await page.waitForSelector(sel, { timeout: 60000 });
    const wait = parseInt(opt('--wait', '1500'), 10);
    if (wait > 0) await page.waitForTimeout(wait);
    fs.writeFileSync(out, await page.content());
    if (has('--shot')) await page.screenshot({ path: opt('--shot'), fullPage: true });
    if (has('--pdf')) await page.pdf({ path: opt('--pdf'), format: 'A4' });
    console.log(JSON.stringify({ url: page.url(), title: await page.title(), bytes: fs.statSync(out).size }));
  } catch (e) {
    console.error('browser_fetch failed:', e.message);
    process.exitCode = 1;
  } finally {
    await browser.close();
  }
})();
