#!/usr/bin/env node
// DECODE (de-crypt.org) login through a real browser, for the case where the plain form POST is never evaluated by
// the server (page re-rendered with IS_LOGGEDIN:false and no "Incorrect user name or password" message, 20-24 Sept
// 2026). The site's login button is disabled until its JavaScript initialises, so a browser submission is the
// form's own submission. Credentials come from DECODE_USER / DECODE_PASS and are never printed or written.
//
//   NODE_PATH=$(npm root -g) node tools/decode_browser_login.js RECORD_ID OUT_DIR [--shot OUT.png]
//     [--fetch URL[,URL...]] [--fetch-page URL[,URL...]] [--delay MS] [--max-files N]
//
// --fetch downloads each URL (relative URLs are resolved against BASE) in the same logged-in browser context via
// context.request, so session cookies apply, and saves it under OUT_DIR with a filename derived from the URL's
// last path segment or `file` query parameter. --fetch-page does the same but always saves as .html and is meant
// for site pages (DocumentsList, ImagesList, RecordsList) rather than attachment files; after saving one, its HTML
// is scanned for `/decrypt-custom/filesrv/?file=...` attachment links and any not already queued are fetched too
// (a page linking to full-size images or documents needs no separate --fetch call for them). Repeat either flag
// or pass a comma-separated list. Requests after login are spaced --delay ms apart (default 1500, the good-citizen
// rule) and capped in total at --max-files (default 10, explicit --fetch URLs first, then auto-discovered links).
//
// Prints one JSON line: {loggedIn, url, title, incorrectMessage, saved, fetched:[{url,path,status,bytes}]}. On
// success it saves RecordsView/RECORD_ID as OUT_DIR/record_RECORD_ID.html, then runs any --fetch/--fetch-page
// requests. Session cookies live only in the in-memory browser context, never written to disk. Exit 0 on login,
// 4 on a rejected login, 1 on an error. One login per run; do not loop it (CLAUDE.md single-attempt rule).
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
if (args.length < 2) {
  console.error('usage: decode_browser_login.js RECORD_ID OUT_DIR [--shot OUT.png] [--fetch URL[,URL...]] [--fetch-page URL[,URL...]] [--delay MS] [--max-files N]');
  process.exit(2);
}
const [recordId, outDir] = args;
const shotIdx = args.indexOf('--shot');
const shot = shotIdx > -1 ? args[shotIdx + 1] : null;
const delayIdx = args.indexOf('--delay');
const delayMs = delayIdx > -1 ? parseInt(args[delayIdx + 1], 10) : 1500;
const maxFilesIdx = args.indexOf('--max-files');
const maxFiles = maxFilesIdx > -1 ? parseInt(args[maxFilesIdx + 1], 10) : 10;

function collectUrls(flag) {
  const urls = [];
  for (let i = 0; i < args.length; i++) {
    if (args[i] === flag) urls.push(...args[i + 1].split(','));
  }
  return urls;
}
const fetchUrls = collectUrls('--fetch');
const fetchPageUrls = collectUrls('--fetch-page');

const user = process.env.DECODE_USER, pass = process.env.DECODE_PASS;
if (!user || !pass) { console.error('DECODE_USER/DECODE_PASS: unset'); process.exit(2); }

const BASE = 'https://de-crypt.org/decrypt-web';
const exe = process.env.CHROMIUM_PATH || (fs.existsSync('/opt/pw-browsers/chromium') ? '/opt/pw-browsers/chromium' : undefined);

function safeFilename(url) {
  const u = new URL(url, BASE + '/');
  const fileParam = u.searchParams.get('file');
  if (fileParam) return fileParam.replace(/[^A-Za-z0-9._-]/g, '_');
  const last = u.pathname.split('/').filter(Boolean).pop() || 'download';
  return last.replace(/[^A-Za-z0-9._-]/g, '_');
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

(async () => {
  const browser = await chromium.launch({ executablePath: exe, headless: true, args: ['--no-sandbox', '--disable-gpu'] });
  const ctx = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36',
    viewport: { width: 1280, height: 1200 }, locale: 'en-GB',
  });
  const page = await ctx.newPage();
  const out = { loggedIn: false, url: null, title: null, incorrectMessage: false, saved: null, fetched: [] };
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

      const seen = new Set();
      const queue = fetchUrls.map((u) => new URL(u, BASE + '/').toString());
      queue.forEach((u) => seen.add(u));

      for (const rawUrl of fetchPageUrls) {
        await sleep(delayMs);
        const url = new URL(rawUrl, BASE + '/').toString();
        try {
          await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
          const pageHtml = await page.content();
          const name = safeFilename(url).replace(/\.[^.]*$/, '') + '.html';
          const p = path.join(outDir, name);
          fs.writeFileSync(p, pageHtml);
          out.fetched.push({ url, path: p, status: 200, bytes: fs.statSync(p).size });
          const linkRe = /\/decrypt-custom\/filesrv\/\?file=[^"'&\s]+/g;
          for (const m of pageHtml.matchAll(linkRe)) {
            const linked = new URL(m[0], 'https://de-crypt.org/').toString();
            if (!seen.has(linked) && seen.size < maxFiles) { seen.add(linked); queue.push(linked); }
          }
        } catch (e) {
          out.fetched.push({ url, path: null, status: null, bytes: 0, error: e.message.split('\n')[0] });
        }
      }

      for (const url of queue.slice(0, maxFiles)) {
        await sleep(delayMs);
        try {
          const resp = await ctx.request.get(url, { timeout: 60000 });
          const body = await resp.body();
          const p = path.join(outDir, safeFilename(url));
          fs.writeFileSync(p, body);
          out.fetched.push({ url, path: p, status: resp.status(), bytes: body.length });
        } catch (e) {
          out.fetched.push({ url, path: null, status: null, bytes: 0, error: e.message.split('\n')[0] });
        }
      }
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
