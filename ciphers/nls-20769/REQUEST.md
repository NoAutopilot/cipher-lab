# Copy request: National Library of Scotland, MS 20769

**Do this in two steps, not one.** The catalogue page (manuscripts.nls.uk) is blocked from this environment
(HTTP 403 / certificate error on two independent attempts, not an org egress policy — see `NOTES.md`), so the
leaf count and the cipher-vs-notation question are both unverified. Get step 1 answered before paying for step 2.

## Step 1: verify, free

Ask NLS (via the copy-enquiry form at auth.nls.uk/copy-enquiry-form/ or manuscripts@nls.uk) or have the person
load manuscripts.nls.uk directly, for:
- The full catalogue description of MS 20769 (or MS.20769) — confirm shelfmark form, exact extent (leaf/folio
  count — the "57 leaves" figure used to score this target needs to be confirmed, not assumed), physical
  description, and provenance/acquisition note.
- Whether the library's own cataloguer characterizes this as a cipher (systematic substitution) or as a
  shorthand/private notation/commonplace book — this changes whether it is a cryptanalytic target at all.

## Step 2: order scans, only once step 1 confirms a genuine cipher worth the leaf count

1. **MS 20769**, all leaves. Ask for A4 (or A3 if the manuscript is oversized) scans of every leaf, both sides.
2. Get a firm quote first: at the published rate (£1.80 inc. VAT per A4 scan, checked 20 Sept 2026), a
   57-leaf, double-sided item would run roughly £100-200+ before any re-use/permission fee — confirm the
   actual leaf count and price before committing.
3. Ask whether a lower-cost route exists for a large item (e.g. a bulk/reader-visit self-scan, or a partial
   scan of a representative sample first).

## Log

| Date | Action | Result |
|---|---|---|
| 20 Sept 2026 | Attempted to load manuscripts.nls.uk directly (curl with browser UA, then `tools/browser_fetch.js` headless Chromium) | Both failed: HTTP 403 (curl), `net::ERR_CERT_AUTHORITY_INVALID` (browser). Confirmed not an org egress block via `/__agentproxy/status` (no relay failures, non-selective proxy). Catalogue description reconstructed from repeated web-search snippets only (see NOTES.md); leaf count and cipher-vs-notation status unverified. |
| | Step 1 verification sent | |
| | Step 2 request sent | |
| | Quote/images received | |
