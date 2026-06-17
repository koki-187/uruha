# Codex Prompt: Correct My Agent Works HP Top to White Premium + 3D Interactive Design

You are implementing the My Agent Works corporate homepage.

The current build direction drifted away from the intended reference. Re-align the HP design to the attached reference images and this corrected direction.

---

## 0. Scope

Repository:

```txt
https://github.com/koki-187/My-Agent-Works-KICKOFF
```

Target page:

```txt
/
```

Branch:

```txt
feature/my-agent-works-hp-top
```

Build or revise only the corporate homepage `/`.

Do not build:

```txt
- 宅建BOOST LP
- My Agent Series LP
- /contact form body
- /about, /business, /products, /trust page bodies
```

Those are links only.

---

## 1. First inspect existing structure

Before editing, inspect the project:

```bash
pwd
ls
find . -maxdepth 3 -type f | sed 's#^./##' | sort | head -200
```

Check:

```txt
package.json
src/app
pages
public
components
styles
tailwind.config.*
next.config.*
```

Use the existing tech stack. Do not arbitrarily convert the project to another stack.

---

## 2. Source of truth for design

Use the attached reference images and the corrected direction as the source of truth.

The correct direction is:

```txt
premium white-base corporate SaaS / PropTech design
navy + gold + cyan
transparent PNG-like parts
thin line icons
clean cards
large whitespace
dark cinematic city hero only at the top
body sections mostly white/soft gray
navy footer
subtle 3D/animation as progressive enhancement
```

The page should look closer to the provided corporate mockup:

```txt
dark city hero
white body sections
blue line icons
product card grid
trust/governance section
contact cards
navy footer
```

It must not become a full dark cyberpunk page.

---

## 3. Correct design ratio

```txt
White premium corporate UI: 60%
Dark cinematic hero: 20%
Navy glass/product cards: 15%
Cyan/gold accents: 5%
```

---

## 4. Interactive 3D / animation requirements

Add advanced interaction without sacrificing trust or performance.

### Required lightweight interactions

Implement these even if no 3D library is available:

```txt
- Header glass transition on scroll
- Hero CTA hover depth
- Product card hover tilt, max 4deg
- Icon micro-glow on hover
- Section reveal animation on scroll
- Trust card subtle scan-line or border glow on hover
- Contact card hover elevation
```

Use CSS transitions or existing animation tooling.

### Optional 3D / WebGL enhancement

If the repo supports React/Next and adding dependencies is acceptable, you may add a progressive 3D component.

Recommended component:

```txt
Hero3DAccent
```

Behavior:

```txt
- floating MAW monogram or abstract building/prism
- slow rotation, very subtle
- cyan/gold edge highlights
- placed on the hero visual side only
- not behind important text
- lazy loaded / dynamically imported
- disabled or simplified under prefers-reduced-motion
```

If using Next.js:

```txt
- dynamically import the 3D component with SSR disabled
- provide static CSS/SVG fallback
- do not block LCP
```

If dependencies are not available, do not block implementation. Use CSS/SVG pseudo-3D instead.

### Optional video asset handling

Do not require actual video for first build.

If a loop background is useful, reserve this path only:

```txt
/public/videos/maw-data-flow-loop.webm
```

Use a static poster/fallback until the video is provided.

Do not add a heavy autoplay video by default.

---

## 5. Visual inheritance

Preserve:

```txt
My Agent Works logo language
MAW monogram feel
My Agent Series product icon feel
MAA / MAL / MAM / MAS / MAT / MAR icon style
white background + navy typography
gold accent lines and highlights
cyan technology accent
section title style similar to reference:
  - small uppercase English label
  - large Japanese/English heading
  - thin gold/blue underline
```

---

## 6. Page structure

Implement this exact homepage structure:

```txt
1. Header
2. Hero
3. Business Domain
4. Product Lineup
5. Why My Agent Works
6. Trust / Governance
7. Contact
8. Footer
```

---

## 7. Header

Use:

```txt
Logo: My Agent Works
```

Nav:

```txt
事業領域 → /business
プロダクト → /products
私たちの強み → /about
信頼・ガバナンス → /trust
会社情報 → /company
```

CTA:

```txt
お問い合わせ → /contact
```

Style:

```txt
- On hero: dark transparent/glass header
- On scroll: white/glass or navy/white variant that remains readable
- Clean gold/navy logo area
- Not too tall
- Mobile responsive
```

---

## 8. Hero

Dark cinematic city skyline hero, but refined and readable.

H1:

```txt
不動産実務を、
AIで再設計する。
```

Lead:

```txt
My Agent Worksは、不動産エージェントの検索・分析・資料作成・学習支援を効率化するAI業務支援プロダクトを開発・運用する会社です。
```

CTA:

```txt
My Agent Seriesを見る → /series
宅建BOOSTを見る → /takken-boost
導入について相談する → /contact
```

Design:

```txt
- Left copy, right city/AI visual or 3D accent
- Dark navy hero only
- Spotlight is allowed
- Thin HUD lines are allowed
- Subtle 3D MAW / building accent allowed on right side
- Must remain corporate, not cyberpunk
- Text must be clearly readable
```

---

## 9. Business Domain

White section.

Heading:

```txt
BUSINESS DOMAIN
事業領域
```

Lead:

```txt
不動産業務のバリューチェーン全体を、AIとテクノロジーで支援。エージェントの生産性向上と、業界全体の進化に貢献します。
```

Cards:

```txt
1. 検索・分析
AIによる不動産・エージェント検索や市場分析を高速化。データに基づく意思決定を支援します。

2. 資料作成・提案
物件資料や提案書の作成を自動化・効率化し、エージェントの提案力を強化します。

3. 学習・ナレッジ
学習支援とナレッジ共有で、個人と組織のスキル向上を継続的にサポートします。

4. 業務最適化
AIエージェントが煩雑な業務を最適化し、人的リソースをより創造的な業務へシフトさせます。
```

Interaction:

```txt
- icon micro-motion on hover
- card lift max 8px
- no aggressive glow
```

---

## 10. Product Lineup

White section with cards.

Heading:

```txt
PRODUCT LINEUP
プロダクトラインナップ
```

Lead:

```txt
My Agent Seriesは、現場の課題に寄り添い、成果に直結するAIプロダクト群です。
```

Product cards:

```txt
MAA / My Agent Analytics
MAL / My Agent Lead
MAM / My Agent Marketing
MAS / My Agent Sales
MAT / My Agent Training
MAR / My Agent Research
```

Important:

```txt
If current business docs use different naming, preserve the displayed mockup direction visually but do not claim all products are fully launched. Use neutral wording such as “提供準備中” or “順次展開”.
```

CTA:

```txt
すべてのプロダクトを見る → /products
```

Interaction:

```txt
- product cards may use subtle 3D tilt
- product chips may glow cyan/gold on hover
- do not make cards dark unless used as small accent
```

---

## 11. Why My Agent Works

White section.

Heading:

```txt
WHY MY AGENT WORKS
私たちの強み
```

Lead:

```txt
不動産業界の深い理解とAI技術を掛け合わせ、現場で使えるプロダクトを提供します。
```

Cards:

```txt
1. 不動産業界に特化
現場を知るメンバーが開発。実務に即したプロダクトを提供します。

2. AI × 業務知見
最新のAI技術と業界知見を融合し、実務に耐えられる解決策を実現します。

3. セキュア & コンプライアンス
高いセキュリティ基準と法令遵守の体制で、安心して利用いただけます。

4. 継続的なアップデート
現場の声を反映し、プロダクトを継続的に進化させます。
```

---

## 12. Trust / Governance

White or very soft gray section.

Heading:

```txt
TRUST / GOVERNANCE
信頼・ガバナンス
```

Lead:

```txt
健全なガバナンスと透明性の高い運営で、社会からの信頼に応えます。
```

Cards:

```txt
1. 情報セキュリティ
認証・権限管理・監査ログなど、必要なセキュリティ体制の整備を進めています。

2. プライバシー保護
個人情報保護法を遵守し、適切な取り扱いと管理を徹底します。

3. コンプライアンス
法令遵守・公正な取引を徹底し、健全な事業運営を行います。

4. 透明性のある開示
サービス内容や責任範囲を明確にし、透明性の高い運営を目指します。
```

Important:

```txt
Do not falsely claim certification if not verified.
```

---

## 13. Contact

White section with two cards and optional office image placeholder.

Heading:

```txt
CONTACT
お問い合わせ
```

Lead:

```txt
プロダクトの導入相談や資料請求、取材・パートナーシップのご相談など、お気軽にお問い合わせください。
```

Cards:

```txt
1. お問い合わせ・導入相談 → /contact
2. 資料請求 → /contact
```

Do not build form body yet.

---

## 14. Footer

Dark navy footer.

Include:

```txt
My Agent Works
事業領域
プロダクト
私たちの強み
信頼・ガバナンス
会社情報
採用情報
プライバシーポリシー
```

---

## 15. SEO

Title:

```txt
My Agent Works｜不動産実務をAIで再設計する
```

Description:

```txt
My Agent Worksは、不動産エージェントの検索・分析・資料作成・学習支援を効率化するAI業務支援プロダクトを開発・運用する会社です。
```

Add:

```txt
- OGP
- Organization JSON-LD
- WebSite JSON-LD
```

---

## 16. Image, 3D, and asset handling

If assets are unavailable, implement with CSS/SVG placeholders and use these intended paths:

```txt
/public/images/home/hp-top-hero.webp
/public/images/home/hp-business-domain.webp
/public/images/home/hp-products.webp
/public/images/home/hp-trust-governance.webp
/public/images/home/hp-contact-cta.webp
/public/images/logo/maw-logo.svg
/public/images/logo/maw-symbol.svg
/public/images/ogp/my-agent-works-ogp.png
/public/images/3d/maw-monogram-3d.png
/public/images/3d/product-orbit.png
/public/videos/maw-data-flow-loop.webm
/public/favicon.ico
```

Do not block implementation because images, 3D assets, or video are missing.

If video is missing, do not use a broken video element. Use a static fallback.

---

## 17. Prohibited

```txt
- Do not use a full dark page design.
- Do not replace the white premium corporate design with a cyberpunk layout.
- Do not use purple/pink/red as the main palette.
- Do not overuse 3D, particles, or WebGL.
- Do not hurt readability or LCP with animation.
- Do not build 宅建BOOST LP.
- Do not build My Agent Series LP.
- Do not build /contact form body.
- Do not claim AI replaces investment, legal, tax, or registration decisions.
- Do not claim guaranteed pass for 宅建BOOST.
- Do not falsely claim certification or compliance status.
```

---

## 18. Build checks

Run the available checks:

```bash
npm run lint
npm run build
```

If the project does not have those scripts, report available scripts from `package.json`.

---

## 19. Commit

After implementation:

```bash
git status
git add .
git commit -m "feat: align homepage with white premium interactive My Agent Works design"
git push origin feature/my-agent-works-hp-top
```

---

## 20. Completion report

Report:

```txt
1. Branch
2. Commit SHA
3. Changed files
4. Implemented sections
5. Image paths used
6. 3D/animation interactions added
7. What was corrected from the previous dark/cinematic plan
8. Items still needing real assets
9. Local preview instructions
10. Remaining risks or questions
```
