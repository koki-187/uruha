# My Agent Works HP/LP Design Reset + 3D Interactive Direction

## Purpose

This document corrects the HP/LP build direction and locks the visual source of truth.

The correct direction is the attached reference design:

- premium white-base corporate SaaS / PropTech layout
- deep navy typography and footer
- gold premium accent
- cyan technology accent
- transparent PNG-like UI parts
- refined line icons
- product card grid
- large whitespace
- dark cinematic city hero only where appropriate
- optional interactive 3D / animation as progressive enhancement

The current build must not drift into a full dark cyberpunk / full cinematic page.

---

# 1. Correct design identity

## Main identity

| Element | Rule |
|---|---|
| Base | White / transparent / soft gray |
| Typography | Deep navy, high contrast, clean corporate |
| Accent | Gold for premium real estate identity, cyan for AI/technology |
| Icons | Thin line, navy/cyan/gold, minimal |
| Cards | White cards, subtle border, restrained shadow |
| Hero | Dark city/cinematic permitted only in Hero |
| Footer | Deep navy corporate footer |

## Page ratio

| Area | Ratio | Usage |
|---|---:|---|
| White premium corporate UI | 60% | Body, cards, business domain, strengths, trust |
| Dark cinematic hero | 20% | Hero only |
| Navy glass/product cards | 15% | Products, CTA, trust highlights |
| Cyan/gold accents | 5% | Icons, lines, buttons, micro-interactions |

---

# 2. What changed from previous plan

Previous prompts over-emphasized Cinematic dark navy.  
This is corrected.

## New rule

```txt
The HP is not a full dark cinematic site.
The HP is a premium white corporate SaaS site with a dark cinematic hero.
```

---

# 3. Correct homepage structure

1. Header
2. Dark cinematic hero
3. White Business Domain section
4. White Product Lineup card grid
5. White Why My Agent Works section
6. White / soft gray Trust & Governance section
7. White Contact cards section
8. Navy Footer

---

# 4. Interactive 3D / animation policy

Interactive 3D and animation are allowed, but must not damage trust, readability, or performance.

## Recommended usage

| Area | 3D / animation concept | Implementation |
|---|---|---|
| Hero | Subtle floating MAW monogram, city glow, AI data nodes | CSS/SVG first, Three.js optional |
| Product Lineup | Hover tilt product cards, glowing product chips | CSS transform / Framer Motion optional |
| Business Domain | Icon micro-motion on hover | CSS animation |
| Trust | Security cards with subtle line scan | CSS pseudo-elements |
| Contact | CTA card hover depth | CSS transform |

## Not allowed

- full-screen 3D game scene
- aggressive particle field
- heavy video background by default
- unreadable motion behind text
- auto-playing large MP4 that hurts LCP
- animations that cannot be reduced with `prefers-reduced-motion`

---

# 5. Technical implementation policy

## Default

Use CSS / SVG / lightweight transforms first.

## If the repository supports React/Next

Optional progressive enhancement:

- `framer-motion` for scroll reveal / card hover
- `three`, `@react-three/fiber`, `@react-three/drei` only if needed and acceptable
- dynamic import for 3D components
- disable SSR for 3D canvas in Next.js
- fallback static hero if WebGL is unavailable

## Performance guardrails

- Do not block LCP with 3D.
- Hero text must render before 3D scene.
- Lazy-load non-critical 3D.
- Use `prefers-reduced-motion`.
- Avoid massive texture assets.
- Keep any video under strict size limits and provide poster image.

---

# 6. Required / optional asset list

## Required for first build

| Asset | Path |
|---|---|
| Hero image or placeholder | `/public/images/home/hp-top-hero.webp` |
| Logo | `/public/images/logo/maw-logo.svg` |
| Symbol | `/public/images/logo/maw-symbol.svg` |
| OGP image | `/public/images/ogp/my-agent-works-ogp.png` |

## Optional advanced assets

| Asset | Purpose | Path |
|---|---|---|
| 3D MAW monogram transparent PNG | Hero floating mark | `/public/images/3d/maw-monogram-3d.png` |
| Product orbit transparent PNG | Product lineup visual | `/public/images/3d/product-orbit.png` |
| Abstract data-flow WebM | Optional hero loop | `/public/videos/maw-data-flow-loop.webm` |
| Animated Lottie JSON | Small icon motion | `/public/lottie/maw-nodes.json` |

If these assets do not exist, build with CSS/SVG placeholders and clearly named paths.

---

# 7. Visual source of truth

The attached images are the source of truth:

1. Transparent PNG UI parts sheet
2. Full corporate homepage mockup
3. My Agent Works / MAW / My Agent Series logo sheet
4. Product icon sheet: MAA / MAL / MAM / MAS / MAT / MAR

The implementation should match that direction, not the full dark cyber style.

---

# 8. Absolute prohibitions

- Do not make the whole page dark.
- Do not replace the white premium body with a cyberpunk dashboard page.
- Do not make every section glassmorphism.
- Do not overuse purple, pink, red.
- Do not build 宅建BOOST LP in this task.
- Do not build My Agent Series LP in this task.
- Do not build /contact form body in this task.
- Do not falsely claim certifications.
- Do not claim AI replaces investment, legal, tax, or registration decisions.
- Do not claim guaranteed pass for 宅建BOOST.

---

# 9. Final design target

The top page should feel like:

```txt
Apple-level whitespace × PropTech corporate trust × subtle AI motion × My Agent Works premium navy/gold/cyan brand.
```
