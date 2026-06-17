# My Agent Works 3D / Animation Asset Specification

## Purpose

This file defines the image, 3D, animation, and video assets needed for the corrected My Agent Works HP/LP direction.

The first implementation can proceed with CSS/SVG placeholders. These assets are for quality-up and replacement.

---

# 1. Required visual direction

The assets must match:

```txt
white premium corporate SaaS
navy / gold / cyan
transparent PNG style
thin line icons
subtle 3D depth
not cyberpunk
not game UI
```

---

# 2. Static image assets

| Asset | Format | Use | Path |
|---|---|---|---|
| MAW horizontal logo | SVG / PNG | Header / footer | `/public/images/logo/maw-logo.svg` |
| MAW symbol | SVG / PNG | favicon / hero | `/public/images/logo/maw-symbol.svg` |
| OGP image | PNG | Social preview | `/public/images/ogp/my-agent-works-ogp.png` |
| Hero city image | WebP | Hero visual | `/public/images/home/hp-top-hero.webp` |
| Business domain icon sheet | SVG / PNG | cards | `/public/images/common/business-icons.svg` |
| Product icon sheet | SVG / PNG | product cards | `/public/images/common/product-icons.svg` |

---

# 3. 3D image assets

| Asset | Format | Use | Path |
|---|---|---|---|
| MAW monogram 3D | transparent PNG / GLB | Hero accent | `/public/images/3d/maw-monogram-3d.png` |
| Premium building prism | transparent PNG / GLB | Hero/brand | `/public/images/3d/maw-building-prism.png` |
| Product orbit visual | transparent PNG / SVG | Product lineup | `/public/images/3d/product-orbit.png` |
| Trust shield 3D | transparent PNG | Trust section | `/public/images/3d/trust-shield-3d.png` |

---

# 4. Video / motion assets

Do not require video for first build.

If created later:

| Asset | Format | Use | Path | Rule |
|---|---|---|---|---|
| Data flow loop | WebM | Hero background accent | `/public/videos/maw-data-flow-loop.webm` | optional, muted, lightweight |
| Logo reveal loop | WebM | Hero or loading | `/public/videos/maw-logo-reveal.webm` | optional |
| Product nodes loop | WebM | Product section | `/public/videos/product-nodes-loop.webm` | optional |

## Video rules

- Use WebM first.
- Provide poster image.
- Do not autoplay with sound.
- Keep file small.
- Do not block LCP.
- Respect reduced motion.

---

# 5. Image generation prompts

## 5.1 MAW 3D monogram transparent PNG

```txt
Create a high-resolution transparent-background PNG of a premium 3D MAW monogram emblem for My Agent Works. Style: luxury corporate proptech, deep navy, restrained gold edges, subtle cyan inner glow, clean vector-like geometry, not cyberpunk, not game-like, elegant and minimal. Isolated object, generous transparent padding, suitable for website hero floating element.
```

## 5.2 3D building prism transparent PNG

```txt
Create a high-resolution transparent-background PNG of an abstract premium real estate building prism icon for My Agent Works. Style: white premium corporate SaaS, deep navy outlines, gold highlight edges, cyan technology glow, clean glass material, elegant and minimal. Isolated object, no text, no background, suitable for website hero and brand visuals.
```

## 5.3 Product orbit visual

```txt
Create a high-resolution transparent-background PNG of a refined product orbit visualization for My Agent Series. Six small product nodes orbit a central MAW symbol. Style: premium corporate proptech, white/navy/gold/cyan, thin lines, transparent background, clean and readable. No heavy cyberpunk effects, no clutter, no text.
```

## 5.4 Trust shield 3D transparent PNG

```txt
Create a high-resolution transparent-background PNG of a premium trust and governance shield icon. Style: deep navy glass, gold fine border, cyan inner security line, corporate SaaS, minimal, elegant, no text, isolated object, transparent background.
```

---

# 6. Animation implementation prompts

## Hero3DAccent

```txt
Build a lightweight Hero3DAccent component. It should display a subtle floating MAW monogram/building prism on the right side of the hero. Use CSS 3D transform first. If Three.js is available, lazy-load a canvas with a fallback. Motion must be slow, premium, and disabled under prefers-reduced-motion.
```

## ProductCardMotion

```txt
Add subtle hover tilt to product cards. Max tilt 4deg, translateY max -8px, glow limited to cyan/gold border. Do not make it playful or game-like. Must support keyboard focus styling.
```

## ScrollReveal

```txt
Add scroll reveal for sections using CSS or existing motion library. Opacity 0 to 1, translateY 16px to 0, duration 500-700ms. Respect prefers-reduced-motion.
```

---

# 7. Acceptance criteria

- The page remains mostly white and corporate.
- Hero is premium and dark but not full-page cyberpunk.
- Motion is subtle.
- 3D is progressive enhancement.
- No broken image/video paths.
- Missing assets use placeholders.
- Performance remains acceptable.
