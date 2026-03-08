# HTML Templates

All HTML files: single self-contained `.html`, inline CSS, no external dependencies.

## Design Direction

Premium dark UI. Layered depth, glassmorphism, micro-animations. Linear/Raycast aesthetic.

**Banned**: Blue-purple gradients, `#7c5cfc`, generic AI color schemes (purple-on-white, blue-to-purple). Pick a distinctive accent palette per session topic instead.

## CSS Variables (Required)

```css
:root {
  /* Backgrounds */
  --bg: #08080c;
  --surface: rgba(255,255,255,0.03);
  --surface-hover: rgba(255,255,255,0.08);
  --border: rgba(255,255,255,0.06);

  /* Text */
  --text: #ededef;
  --text-secondary: rgba(255,255,255,0.55);
  --text-tertiary: rgba(255,255,255,0.3);

  /* Accent — CHOOSE a cohesive palette per topic, NOT blue-purple */
  --accent-1: /* primary accent */;
  --accent-2: /* secondary accent */;
  --accent-gradient: linear-gradient(135deg, var(--accent-1), var(--accent-2));

  /* Status */
  --green: #34d399;
  --amber: #fbbf24;
  --red: #f87171;

  /* Typography */
  --font-mono: 'SF Mono', 'Fira Code', 'JetBrains Mono', monospace;
  --font-sans: -apple-system, 'Inter', system-ui, sans-serif;

  /* Radius */
  --radius: 12px;
}
```

### Accent Palette Examples

Pick based on topic feel. Be creative — avoid the banned blue-purple.

| Topic vibe | accent-1 | accent-2 |
|------------|----------|----------|
| Warm / creative | `#f59e0b` | `#ef4444` |
| Nature / organic | `#10b981` | `#06b6d4` |
| Elegant / editorial | `#e2e8f0` | `#f59e0b` |
| Bold / energetic | `#f43f5e` | `#fb923c` |
| Calm / technical | `#06b6d4` | `#34d399` |

## General Rules

- `<meta charset="UTF-8">` + `<meta name="viewport">`
- Use CSS custom properties — never hardcode colors
- Transitions: `cubic-bezier(0.4, 0, 0.2, 1)`
- Animations subtle: pulse, progress transitions, hover lifts
- Max content width: `720px` centered
- Mobile responsive: `@media (max-width: 480px)`
- Glassmorphism: `backdrop-filter: blur(12px)` on card surfaces
- Subtle mesh gradient background (2-3 radial gradients using accent colors at low opacity)

## Template: Roadmap (`roadmap.html`)

```
┌──────────────────────────────────────────┐
│ Header: gradient title + metadata chips  │
│          + circular SVG progress ring    │
│                                          │
│ Timeline (vertical, left connector line) │
│  ├── Node (mastered)  [✓ green]          │
│  ├── Node (in-progress) [pulsing]        │
│  └── Node (not-started) [dimmed 0.45]    │
│                                          │
│ Footer: overall progress bar             │
└──────────────────────────────────────────┘
```

Key elements:
- **Timeline connector**: vertical 2px line, gradient from accent to border at mastery boundary
- **Node cards**: glass surface, border varies by status (green=mastered, accent=active, dim=upcoming)
- **Progress ring**: SVG `stroke-dasharray`/`stroke-dashoffset` technique
- **`--mastered-pct`**: set on `.timeline` to control gradient line position
- Each node shows: title, status badge (pill), score %, mini progress bar

## Template: Summary (`summary.html`)

```
┌──────────────────────────────────────────┐
│ Header: gradient title + completion badge│
│                                          │
│ Stats Grid (2x2): mastered count,        │
│   questions, mastery rate, duration      │
│                                          │
│ Concept Breakdown: horizontal bar chart  │
│ Key Insights: bullet list                │
│ Next Steps: recommendations              │
└──────────────────────────────────────────┘
```

## Template: Visual Explanation (`visuals/*.html`)

For code walkthroughs:
- Step-by-step panels: code + annotation in glass cards
- `<pre><code>` with manual syntax highlighting via span classes
- Syntax classes: `.kw` (keywords), `.fn` (functions), `.str` (strings), `.num` (numbers), `.cmt` (comments)
- Annotation callouts: left accent border, subtle background

## SVG Gradient Definition

Include once per file for progress rings:
```html
<svg style="position:absolute;width:0;height:0">
  <defs>
    <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="var(--accent-1)"/>
      <stop offset="100%" stop-color="var(--accent-2)"/>
    </linearGradient>
  </defs>
</svg>
```
