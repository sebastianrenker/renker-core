# RENKER platform site

A single self-contained `index.html` — no build step, no external requests, no data collected.
Content is aligned to `../docs/marketing/` and every claim is checked against
`../docs/marketing/reality-check.md`.

**Preview locally:** `python -m http.server -d site` → http://localhost:8000
**Publish:** GitHub Pages (Settings → Pages → branch, `/site` folder) or any static host.

When a status or number changes, update `reality-check.md` first, then this page.
