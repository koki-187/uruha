# 10 HP Top Codex Build Prompt

## 目的

Codexで、合同会社 My Agent Works 公式HPトップページを実装するための詳細プロンプト。  
本プロンプトは `08-hp-top-wireframe.md`、`08a-hp-design-inheritance-rules.md`、`09-hp-top-copy.md` を前提にする。

## 重要な前提

- 宅建BOOSTのLPは別で構築済み。会社HPトップでは、宅建BOOSTは既存LPへの導線として扱う。
- My Agent Series LPも会社HPトップとは別ページとして構築する。
- 今回の実装対象は、会社HPトップページ `/` のみ。
- 既存コードを壊さない。
- 既存の検証計画を崩さない。

---

# Codexへの依頼文

以下の要件に従って、My Agent Works公式HPトップページを実装してください。

## 1. 実装対象

```txt
Page: /
Project: My Agent Works corporate website
Scope: Top page only
```

会社HPトップページのみを実装してください。  
宅建BOOST LPは別構築済みのため、`/takken-boost` への導線のみ配置し、宅建BOOST LP本体はこの作業では作らないでください。

---

# 2. 参照すべきドキュメント

必ず以下を確認し、内容を崩さないでください。

```txt
docs/kickoff/implementation/08-hp-top-wireframe.md
docs/kickoff/implementation/08a-hp-design-inheritance-rules.md
docs/kickoff/implementation/09-hp-top-copy.md
docs/kickoff/implementation/05-image-usage-alt-text.md
docs/kickoff/cinematic-proptech-design-system.md
```

## 特に守ること

- 会社HPは信頼獲得が目的。
- HeroとFinal CTAにCinematic PropTechを使う。
- 本文はTrust Monotone中心。
- Sales HTMLのCinematic dark navy / city skyline / cyan glow / navy + gold設計を継承する。
- My Agent Series LPのような売り込み過多にはしない。

---

# 3. デザイン方針

## Design Ratio

| Mode | Ratio | Usage |
|---|---:|---|
| Trust Monotone | 60% | Business / Why / Company / Trust |
| Cinematic PropTech | 30% | Hero / Products visual / Final CTA |
| Intelligent Navy | 10% | Product cards / Accent / Section contrast |

## Color Tokens

以下のCSS変数を設計に取り込んでください。

```css
:root {
  --maw-cin-black: #031122;
  --maw-cin-dark: #07192D;
  --maw-cin-navy: #15293F;
  --maw-cin-mid: #2E445F;
  --maw-cin-gray: #4B627E;
  --maw-cin-white: #F1F5FA;
  --maw-cin-cyan: #7EC7FF;

  --maw-navy: #0D1F4D;
  --maw-navy-mid: #162D6B;
  --maw-gold: #C8982A;
  --maw-gold-light: #DEB84A;
  --maw-gold-pale: #F5E9C8;

  --maw-white: #FFFFFF;
  --maw-off-white: #F9F8F5;
  --maw-text: #2D2D2D;
  --maw-text-muted: #6B6B6B;
  --maw-border: #E0D8C8;
}
```

## Typography

- English: Inter
- Japanese: Noto Sans JP
- Serif / 明朝体 / 装飾フォントは使わない
- 見出しは余白を大きく、左揃え基調

---

# 4. ページ構成

実装するセクションは以下です。

```txt
Header
Hero
Business Domain
Products
Why My Agent Works
Trust / Governance Preview
Final CTA
Footer
```

---

# 5. Header

## Layout

```txt
[Logo: My Agent Works]     [About] [Business] [Products] [Trust] [Contact] [導入について相談する]
```

## Navigation

| Label | Link |
|---|---|
| About | `/about` |
| Business | `/business` |
| Products | `/products` |
| Trust | `/trust` |
| Contact | `/contact` |

## CTA

```txt
導入について相談する
```

## Behavior

- sticky header推奨
- desktop: horizontal nav
- mobile: hamburger menu
- Hero上ではglass headerでも可

---

# 6. Hero Section

## Section ID

```txt
hero
```

## Eyebrow

```txt
AI WORKFLOW COMPANY FOR REAL ESTATE
```

## H1

```txt
不動産実務を、AIで再設計する。
```

## Lead

```txt
My Agent Worksは、不動産エージェントの検索・分析・資料作成・学習支援を効率化するAI業務支援プロダクトを開発・運用する会社です。
```

## Optional Sub Lead

```txt
AIが作業を担い、人は判断と信頼構築に集中する。現場の実務から生まれたプロダクトで、不動産業務と教育DXの新しい基盤をつくります。
```

## CTA Buttons

| Button | Link | Style |
|---|---|---|
| My Agent Seriesを見る | `/series` | primary |
| 宅建BOOSTを見る | `/takken-boost` | secondary |
| 導入について相談する | `/contact` | outline/text |

## Proof Chips

```txt
AI業務支援
不動産DX
教育DX
PWA / SaaS
法人導入相談
```

## Visual

Use image:

```txt
01_HP_TOP_HERO_会社HPトップ.png
```

Alt:

```txt
不動産実務をAIで再設計するMy Agent Worksのメインビジュアル
```

## Hero Design

- 左側にcopy、右側にvisual
- 背景はdark navy cinematic gradient
- city skyline / subtle grid / film grain / cyan glowを許可
- ただし文字可読性を最優先
- Hero下部にsoft transitionを入れる

---

# 7. Business Domain Section

## Section ID

```txt
business-domain
```

## Heading

```txt
Business Domain
事業領域
```

## Lead

```txt
My Agent Worksは、不動産実務から生まれたAIプロダクトと、資格学習DXを軸に、現場の業務効率化と事業成長を支援します。
```

## Cards

### AI Product Development

```txt
不動産業務の検索、分析、資料作成、管理を支援するAIプロダクトを企画・開発します。
```

### Education DX

```txt
宅建BOOSTを中心に、資格学習と試験後導線をつなぐ教育DXを展開します。
```

### DX Consulting

```txt
不動産会社や個人エージェントの業務フローを整理し、AI導入・運用改善を支援します。
```

### LP / Content Production

```txt
商品LP、営業資料、FAQ、AI検索対応コンテンツを制作し、事業の伝わり方を設計します。
```

## Design

- 背景：white or soft gray
- card: white, thin border, subtle shadow
- icon: common HP icon sheetから使用
- CTA: `事業内容を見る` → `/business`

---

# 8. Products Section

## Section ID

```txt
products
```

## Heading

```txt
Products
プロダクト
```

## Lead

```txt
不動産実務の効率化を支援するMy Agent Seriesと、宅建学習を支援する宅建BOOSTを中心に、実務と学習の両面から価値を提供します。
```

## Product Card 1: My Agent Series

Label:

```txt
AI WORKFLOW PRODUCTS
```

Title:

```txt
My Agent Series
```

Catch:

```txt
不動産エージェントの業務時間を、AIで再設計するプロダクト群
```

Body:

```txt
検索、分析、判断、シミュレーション、税務サポート、書類管理まで。不動産実務の各工程をAIで支援し、業務時間の削減と提案品質の向上を目指します。
```

Chips:

```txt
MAA Analytics / MAL Locator / MAM Much / MAS Simulate / MAT Tax AI / MAR Doc. AI
```

CTA:

```txt
My Agent Seriesを見る → /series
```

## Product Card 2: 宅建BOOST

Important:

```txt
宅建BOOST LPは別構築済み。ここでは既存LPへの導線として扱う。
```

Label:

```txt
EDUCATION DX PRODUCT
```

Title:

```txt
宅建BOOST
```

Catch:

```txt
宅建合格まで、何をやるかもう迷わない。
```

Body:

```txt
過去問演習、分野別学習、AI弱点分析、模擬試験、自己採点まで。宅建BOOSTは、合格までの学習行動を見える化する宅建学習アプリです。
```

CTA:

```txt
宅建BOOSTを見る → /takken-boost
```

## Product Card 3: DX Consulting

Label:

```txt
BUSINESS SUPPORT
```

Title:

```txt
DX Consulting
```

Catch:

```txt
AI導入を、現場で使える業務フローへ。
```

Body:

```txt
既存業務の棚卸し、AI活用ポイントの整理、LP・営業資料・問い合わせ導線の設計まで、事業化に必要な実務を伴走します。
```

CTA:

```txt
相談する → /contact
```

## Visual

Use image:

```txt
05_HP_PRODUCTS.png
```

---

# 9. Why My Agent Works Section

## Heading

```txt
Why My Agent Works
選ばれる理由
```

## Lead

```txt
My Agent Worksのプロダクトは、現場の不動産実務から生まれています。単なるAI導入ではなく、日々の業務フローを見直し、人が判断と信頼構築に集中できる状態を目指します。
```

## Reasons

### 実務起点の設計

```txt
検索、分析、資料作成、顧客提案。実際の不動産エージェント業務で発生する作業を前提に、使える形へ落とし込みます。
```

### AIと人の役割を分ける

```txt
AIは情報整理と作業支援を担い、人は判断、提案、関係構築に集中する。過度な自動化ではなく、実務に耐える補助設計を重視します。
```

### 小さく始めて改善する

```txt
β提供、KPI計測、フィードバック改善を通じて、現場の運用に耐えるプロダクトへ育てます。
```

---

# 10. Trust / Governance Preview

## Heading

```txt
Trust / Governance
信頼とガバナンス
```

## Lead

```txt
AIを業務判断の代替ではなく、実務を支援する補助ツールとして設計しています。情報の取り扱い、出力結果の確認、専門家判断が必要な領域を明確にし、安心して相談できる運用体制を整えます。
```

## Cards

### AI出力の位置付け

```txt
AI出力は検索・整理・分析・資料作成を補助する情報であり、最終判断を代替するものではありません。
```

### 情報管理

```txt
顧客情報、物件資料、学習履歴などの取り扱い範囲を明確にし、必要最小限の利用を前提に運用します。
```

### 専門家確認

```txt
税務、法務、投資判断、資格登録要件は、必要に応じて専門家・公的機関の確認を前提とします。
```

CTA:

```txt
Trust / Governanceを見る → /trust
```

Use image:

```txt
04_HP_TRUST_GOVERNANCE.png
```

---

# 11. Final CTA

## Label

```txt
Contact
```

## Title

```txt
まずは、現在の業務課題をお聞かせください。
```

## Lead

```txt
My Agent Series、宅建BOOST、法人導入、協業相談など、目的に応じて最適な導入・連携方法を整理します。
```

## Note

```txt
初回相談では、現在の業務課題・利用したい機能・導入範囲を確認し、無理のない導入ステップをご提案します。
```

## CTA

```txt
導入について相談する → /contact
My Agent Seriesのデモを相談する → /series#contact
```

Use image:

```txt
06_HP_CONTACT_CTA.png
```

---

# 12. Footer

## Brand

```txt
My Agent Works
```

## Tagline

```txt
不動産実務を、AIで再設計する。
```

## Description

```txt
不動産業界向けAI業務支援プロダクトと教育DXサービスを開発・運用する会社です。
```

## Columns

```txt
Company: About / Mission / Business / Trust / Contact
Products: My Agent Series / 宅建BOOST / DX Consulting
Legal: Privacy Policy / Terms of Service / Disclaimer / 特定商取引法に基づく表記
Contact: info@my-agent.work
Address: 東京都小平市
```

---

# 13. SEO / Metadata

## title

```txt
My Agent Works｜不動産実務をAIで再設計する
```

## description

```txt
My Agent Worksは、不動産エージェントの検索・分析・資料作成・学習支援を効率化するAI業務支援プロダクトを開発・運用する会社です。My Agent Series、宅建BOOST、DX Consultingを通じて、不動産実務と教育DXを支援します。
```

## OGP

```txt
og:title: My Agent Works｜不動産実務をAIで再設計する
og:description: 不動産業界向けAI業務支援プロダクトと教育DXサービスを開発・運用するMy Agent Worksの公式サイトです。
og:image: /images/ogp/my-agent-works-ogp.png
```

## JSON-LD

Add `Organization` and `WebSite` JSON-LD.

---

# 14. Implementation Requirements

## Components

Create or use the following components:

```txt
Header
Hero
SectionTitle
Button
BusinessCard
ProductCard
ReasonCard
TrustCard
CTASection
Footer
```

## Data files

If project structure allows, separate content into:

```txt
siteConfig.ts
navigation.ts
businessDomains.ts
products.ts
trustItems.ts
homeCopy.ts
```

## Image handling

- Store only necessary production images under `/public/images/`.
- Convert heavy PNGs to WebP if possible.
- Use responsive image loading.
- Use correct alt text from `05-image-usage-alt-text.md`.
- Decorative images should have empty alt.

## Accessibility

- H1 must be only one per page.
- Buttons and links must have clear labels.
- Contrast must pass readability.
- Keyboard navigation must work.
- Mobile menu must be accessible.

## Responsive

- Desktop: max-width 1120px〜1200px, 2-column Hero.
- Tablet: stacked Hero.
- Mobile: copy first, visual second, CTA vertical.

---

# 15. 禁止事項

Do not:

```txt
- 宅建BOOST LP本体をこの作業で作る
- 既存検証計画を変更する
- 全ページを黒背景にする
- 紫・ピンク・赤をメインカラーにする
- サイバーパンクやゲームUIへ寄せすぎる
- 情報商材風の強い煽りを使う
- 不動産仲介業者と誤認される表現を使う
- AIが投資判断・税務判断・法務判断を代替する表現を使う
- 宅建BOOSTで合格保証表現を使う
- 画像内テキストに依存した実装にする
```

---

# 16. Acceptance Criteria

実装完了後、以下を満たすこと。

- ファーストビューで何の会社か分かる。
- Heroコピーが明確に読める。
- My Agent Seriesと宅建BOOSTへの導線がある。
- 宅建BOOST LPは別構築済みとしてリンクのみ。
- 会社HPとして信頼性がある。
- Sales HTMLのCinematic dark navy / city skyline / cyan glow / navy + goldの設計を継承している。
- 本文セクションは白・余白・カード中心で読みやすい。
- Trust / Governance導線がある。
- Contact CTAがHeroとFinal CTAにある。
- PC / tablet / mobileで崩れない。
- SEO metadata / OGP / JSON-LDが入っている。
- 断定・誇張・法務税務投資判断の代替表現がない。

---

# 17. 完了後に出力すること

Codexは実装後に以下を報告する。

```txt
1. 変更ファイル一覧
2. 実装したセクション一覧
3. 使用画像一覧
4. 未実装または要確認事項
5. 表示確認手順
6. 改善提案
```

## Next after this task

```txt
Phase 1-4:
会社HPトップページ実装レビュー・修正指示作成

docs/kickoff/implementation/11-hp-top-review-checklist.md
```
