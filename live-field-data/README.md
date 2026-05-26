# Live Field Data card

Self-contained drop-in card. No framework required.

## Files

- `live-field-data.css` — all styles, scoped under `.lfd`
- `live-field-data.js`  — animates the clock, "MONITORING" count, "RISK INDEX", and sparkline
- `preview.html`        — open this in a browser to see it in isolation

## Install

Copy `live-field-data.css` and `live-field-data.js` into your site, and load them on the page:

```html
<link rel="stylesheet" href="/path/to/live-field-data.css">
<script src="/path/to/live-field-data.js" defer></script>
```

Then paste the markup (from `preview.html`, the block inside `<div class="demo-wrap">`) anywhere in your hero section. Width is whatever the parent gives it — 280–360px looks best.

The JS auto-initializes every `[data-lfd]` it finds on `DOMContentLoaded`. If you mount the card later (SPA / AJAX), call `window.LiveFieldData.refresh()` after insertion.

## Theming

Override CSS variables on `.lfd` (or any ancestor):

```css
.lfd {
  --lfd-accent: #E85A1A;   /* sparkline + brand orange */
  --lfd-ok:     #19B58A;   /* status dot + ok values */
  --lfd-bg:     rgba(8, 18, 36, 0.55);
  --lfd-border: rgba(255, 255, 255, 0.16);
  --lfd-ink:    #E8EEF7;
}
```

## Localize / change content

All copy is plain HTML — edit the strings directly in your template. The JS only touches the elements that have `data-lfd-*` hooks, so static labels ("STATUS", "REGION", "INCIDENT RATE · 12M ↓ 38%") stay exactly as you write them.

To change what the animated fields show, edit `live-field-data.js`:

- `MONITORING` count: line with `(tick % 7) + 3`
- `RISK INDEX` toggle: line with `tick % 4 === 0 ? "LOW" : "STABLE"`
- Sparkline shape: `buildSparkPoints` function

## Fonts

The card expects "JetBrains Mono" (mono) and "Space Grotesk" (sans) — both Google Fonts. If your site already loads other fonts, swap the `font-family` lines in `live-field-data.css`. Any clean monospace works for the body.
