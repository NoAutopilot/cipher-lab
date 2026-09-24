#!/usr/bin/env node
// DECODE (de-crypt.org) login through a real browser, for the case where the plain form POST is never evaluated by
// the server (page re-rendered with IS_LOGGEDIN:false and no "Incorrect user name or password" message, 20-24 Sept
// 2026). The site's login button is disabled until its JavaScript initialises, so a browser submission is the
// form's own submission. Credentials come from DECODE_USER / DECODE_PASS and are never printed or written.
//
//   NODE_PATH=$(npm root -g) node tools/decode_browser_login.js RECORD_ID OUT_DIR [--shot OUT.png]
//     [--fetch URL[,URL...]] [--fetch-page URL[,URL...]] [--delay MS] [--max-files N]
//     [--guess-fullsize] [--probe URL[,URL...]] [--click "PAGE_URL|LINK_TEXT"[,...]]
//
// --fetch downloads each URL (relative URLs are resolved against BASE) in the same logged-in browser context via
// context.request, so session cookies apply, and saves it under OUT_DIR with a filename derived from the URL's
// last path segment or `file` query parameter. --fetch-page does the same but always saves as .html and is meant
// for site pages (DocumentsList, ImagesList, RecordsList) rather than attachment files; after saving one (and
// after saving the primary RecordsView/RECORD_ID page), its HTML is scanned for `/decrypt-custom/filesrv/?file=...`
// attachment links and any not already queued are fetched too (a page linking to full-size images or documents
// needs no separate --fetch call for them). Repeat either flag or pass a comma-separated list. Requests after
// login are spaced --delay ms apart (default 1500, the good-citizen rule) and capped in total at --max-files
// (default 10, explicit --fetch URLs first, then auto-discovered links).
//
// --guess-fullsize (added 24 Sept 2026, LANE N2 dcB): DECODE's thumbnail filenames are `TH_IMG_R<record>_I<img>
// _P<n>.<ext>`; the page's zoom-modal <img alt="..."> attribute names the same file without the `TH_` prefix
// (`IMG_R<record>_I<img>_P<n>.<ext>`), which is not itself a link so the plain filesrv-link scan above never
// finds it. With this flag, every discovered `TH_`-prefixed filesrv link also queues a request for its
// un-prefixed name (still capped by --max-files), so a full-size fetch attempt needs no manual filename
// bookkeeping between runs. It returns whatever the server actually sends (a real image, or DECODE's
// `forbidden.png` placeholder, sha1 035489a0605851154ab88372216354b63596ca22, when access is refused) -- compare
// the saved file's sha1 yourself, this flag does not do that comparison.
//
// --probe (added 24 Sept 2026, LANE N2 dcB): for each URL, makes a context.request.get with maxRedirects:0 (does
// not follow the redirect, so the response is the redirect itself) and, if the response is a 3xx with a
// `location` header, repeats against the resolved location, up to 5 hops, recording each hop's {url, status,
// location} to the JSON output's `probed` array. Use this before ever pointing page.goto at a page suspected of
// redirect-looping (page.goto chases redirects itself, silently burning the request budget on a dead end -- see
// sources/decode/NOTES.md, "No larger image than the 200px thumbnail", record 1162's ImagesList page).
//
// --click (added 24 Sept 2026, LANE N2 dcB): for a page that --probe shows is missing some prerequisite a plain
// GET can't supply (a referrer, a prior AJAX call, a session flag set only by the UI), navigate to PAGE_URL,
// find the first visible link whose text contains LINK_TEXT (case-insensitive), click it, and save wherever it
// lands. Reaches a page the way a person would instead of guessing its request shape; use it only after --probe
// shows the direct route is blocked, not as a first move. Pass "PAGE_URL|LINK_TEXT", comma-separate for several.
//
// Prints one JSON line: {loggedIn, url, title, incorrectMessage, saved, fetched:[{url,path,status,bytes}],
// probed:[{url,hops:[{url,status,location}]}], clicked:[{page,linkText,landedUrl,path}]}. On success it saves
// RecordsView/RECORD_ID as
// OUT_DIR/record_RECORD_ID.html, then runs any --fetch/--fetch-page/--probe requests. Session cookies live only
// in the in-memory browser context, never written to disk. Exit 0 on login, 4 on a rejected login, 1 on an
// error. One login per run; do not loop it (CLAUDE.md single-attempt rule).
const fs = require('fs');
const path = require('path');

const BASE = 'https://de-crypt.org/decrypt-web';

function safeFilename(url) {
  const u = new URL(url, BASE + '/');
  const fileParam = u.searchParams.get('file');
  if (fileParam) return fileParam.replace(/[^A-Za-z0-9._-]/g, '_');
  const last = u.pathname.split('/').filter(Boolean).pop() || 'download';
  // A query string is often the only thing distinguishing one page from another with the same path
  // (DocumentsList?...&fk_id=1411 vs &fk_id=2678 both end in /DocumentsList): fold it into the name so
  // repeat --fetch-page calls in one run don't overwrite each other's saved file (found 24 Sept 2026,
  // six DocumentsList fetches in one login all landing on the same DocumentsList.html).
  const suffix = u.search ? '_' + u.search.slice(1) : '';
  return (last + suffix).replace(/[^A-Za-z0-9._-]/g, '_');
}

// The zoom-modal alt text and the underlying file both keep the plain, un-prefixed name; only the <img src>
// used for the thumbnail itself carries the `TH_` prefix. Returns null when the name isn't TH_-prefixed.
function guessFullsizeName(thumbFileParam) {
  return thumbFileParam.startsWith('TH_') ? thumbFileParam.slice(3) : null;
}

// Shared by the primary RecordsView fetch and every --fetch-page fetch: finds filesrv links, queues any new
// ones (respecting maxFiles), and, with guessFullsize, also queues each TH_-prefixed link's full-size guess.
function scanFilesrvLinks(html, queue, seen, maxFiles, guessFullsize) {
  const linkRe = /\/decrypt-custom\/filesrv\/\?file=([^"'&\s]+)/g;
  for (const m of html.matchAll(linkRe)) {
    const linked = new URL(m[0], 'https://de-crypt.org/').toString();
    if (!seen.has(linked) && seen.size < maxFiles) { seen.add(linked); queue.push(linked); }
    if (guessFullsize) {
      const fullName = guessFullsizeName(decodeURIComponent(m[1]));
      if (fullName) {
        const fullUrl = `https://de-crypt.org/decrypt-custom/filesrv/?file=${encodeURIComponent(fullName)}`;
        if (!seen.has(fullUrl) && seen.size < maxFiles) { seen.add(fullUrl); queue.push(fullUrl); }
      }
    }
  }
}

module.exports = { safeFilename, guessFullsizeName, scanFilesrvLinks };

if (require.main === module) {
const { chromium } = require('playwright');

const args = process.argv.slice(2);
if (args.length < 2) {
  console.error('usage: decode_browser_login.js RECORD_ID OUT_DIR [--shot OUT.png] [--fetch URL[,URL...]] [--fetch-page URL[,URL...]] [--delay MS] [--max-files N] [--guess-fullsize] [--probe URL[,URL...]]');
  process.exit(2);
}
const [recordId, outDir] = args;
const shotIdx = args.indexOf('--shot');
const shot = shotIdx > -1 ? args[shotIdx + 1] : null;
const delayIdx = args.indexOf('--delay');
const delayMs = delayIdx > -1 ? parseInt(args[delayIdx + 1], 10) : 1500;
const maxFilesIdx = args.indexOf('--max-files');
const maxFiles = maxFilesIdx > -1 ? parseInt(args[maxFilesIdx + 1], 10) : 10;
const guessFullsize = args.includes('--guess-fullsize');

function collectUrls(flag) {
  const urls = [];
  for (let i = 0; i < args.length; i++) {
    if (args[i] === flag) urls.push(...args[i + 1].split(','));
  }
  return urls;
}
const fetchUrls = collectUrls('--fetch');
const fetchPageUrls = collectUrls('--fetch-page');
const probeUrls = collectUrls('--probe');
const clickSpecs = collectUrls('--click').map((spec) => {
  const i = spec.indexOf('|');
  return i === -1 ? { pageUrl: spec, linkText: '' } : { pageUrl: spec.slice(0, i), linkText: spec.slice(i + 1) };
});

const user = process.env.DECODE_USER, pass = process.env.DECODE_PASS;
if (!user || !pass) { console.error('DECODE_USER/DECODE_PASS: unset'); process.exit(2); }

const exe = process.env.CHROMIUM_PATH || (fs.existsSync('/opt/pw-browsers/chromium') ? '/opt/pw-browsers/chromium' : undefined);

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

(async () => {
  const browser = await chromium.launch({ executablePath: exe, headless: true, args: ['--no-sandbox', '--disable-gpu'] });
  const ctx = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36',
    viewport: { width: 1280, height: 1200 }, locale: 'en-GB',
  });
  const page = await ctx.newPage();
  const out = { loggedIn: false, url: null, title: null, incorrectMessage: false, saved: null, fetched: [], probed: [], clicked: [] };
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
      const primaryHtml = await page.content();
      const f = path.join(outDir, `record_${recordId}.html`);
      fs.writeFileSync(f, primaryHtml);
      out.saved = f;

      const seen = new Set();
      const queue = fetchUrls.map((u) => new URL(u, BASE + '/').toString());
      queue.forEach((u) => seen.add(u));
      scanFilesrvLinks(primaryHtml, queue, seen, maxFiles, guessFullsize);

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
          scanFilesrvLinks(pageHtml, queue, seen, maxFiles, guessFullsize);
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

      for (const rawUrl of probeUrls) {
        let hopUrl = new URL(rawUrl, BASE + '/').toString();
        const hops = [];
        for (let hop = 0; hop < 5; hop++) {
          await sleep(delayMs);
          try {
            const resp = await ctx.request.get(hopUrl, { maxRedirects: 0, timeout: 60000 });
            const status = resp.status();
            const location = (resp.headers()['location']) || null;
            hops.push({ url: hopUrl, status, location });
            if (location && status >= 300 && status < 400) {
              hopUrl = new URL(location, hopUrl).toString();
            } else break;
          } catch (e) {
            hops.push({ url: hopUrl, status: null, location: null, error: e.message.split('\n')[0] });
            break;
          }
        }
        out.probed.push({ url: rawUrl, hops });
      }

      for (const { pageUrl, linkText } of clickSpecs) {
        await sleep(delayMs);
        const url = new URL(pageUrl, BASE + '/').toString();
        try {
          await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
          const link = page.locator('a', { hasText: linkText }).first();
          await link.waitFor({ state: 'visible', timeout: 10000 });
          await Promise.all([
            page.waitForLoadState('networkidle', { timeout: 60000 }).catch(() => {}),
            link.click(),
          ]);
          await page.waitForTimeout(1000);
          const landedUrl = page.url();
          const name = 'click_' + safeFilename(landedUrl).replace(/\.[^.]*$/, '') + '.html';
          const p = path.join(outDir, name);
          fs.writeFileSync(p, await page.content());
          out.clicked.push({ page: url, linkText, landedUrl, path: p });
        } catch (e) {
          out.clicked.push({ page: url, linkText, landedUrl: null, path: null, error: e.message.split('\n')[0] });
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
}
