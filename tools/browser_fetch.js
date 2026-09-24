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
  // --profile DIR keeps cookies and logins between runs (the owner's local runner, tools/local_runner_brief.md);
  // --headed shows the window so a login or a click can be done by hand. Without --profile nothing changes.
  const exe = process.env.CHROMIUM_PATH || (fs.existsSync('/opt/pw-browsers/chromium') ? '/opt/pw-browsers/chromium' : undefined);
  const ctxOpts = {
    userAgent: opt('--ua', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'),
    viewport: { width: 1280, height: 1800 },
    locale: 'en-GB',
  };
  const profile = opt('--profile', null);
  let browser, ctx;
  if (profile) {
    ctx = await chromium.launchPersistentContext(profile, { executablePath: exe, headless: !has('--headed'), args: ['--disable-gpu'], ...ctxOpts });
    browser = ctx;
  } else {
    browser = await chromium.launch({ executablePath: exe, headless: !has('--headed'), args: ['--no-sandbox', '--disable-gpu'] });
    ctx = await browser.newContext(ctxOpts);
  }
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
    if (/ERR_CERT_AUTHORITY_INVALID/.test(e.message)) {
      // Cloud containers route HTTPS through an agent proxy that re-terminates TLS with its own CA
      // (/root/.ccr/ca-bundle.crt). Node and curl trust it through environment variables; Chromium reads only its NSS
      // store, so it must be added there once per container (needs libnss3-tools; do not use ignoreHTTPSErrors).
      console.error('hint: Chromium does not trust the agent-proxy CA. Add it to its NSS store and rerun:\n' +
        '  apt-get install -y libnss3-tools && certutil -d sql:$HOME/.pki/nssdb -A -t "C,," -n ccr-agent-proxy ' +
        '-i /root/.ccr/agent-proxy-ca.crt');
    }
    process.exitCode = 1;
  } finally {
    await browser.close();
  }
})();
