# 08 HP Top Wireframe

## 目的

合同会社 My Agent Works 公式HPトップページのワイヤーフレームを定義する。  
本ページは、金融機関・税理士・司法書士・協業先・法人顧客が最初に確認する入口として、信頼性、事業内容、プロダクト概要、問い合わせ導線を短時間で理解できる構成にする。

## ページゴール

1. My Agent Worksが何の会社かを一瞬で伝える。
2. AIサービスの先進性と法人としての信頼性を両立する。
3. My Agent Series、宅建BOOST、DX Consultingへの導線を明確にする。
4. 協業・導入・デモ相談へ誘導する。
5. 不動産仲介業者ではなく、不動産業界向けAI業務支援・教育DXプロダクトの開発運営会社として認識させる。

## デザイン配分

| Mode | Ratio | Usage |
|---|---:|---|
| Trust Monotone | 60% | Business / Why / Company / Trust |
| Cinematic PropTech | 30% | Hero / Products visual / Final CTA |
| Intelligent Navy | 10% | Product cards / Accent / Section contrast |

## 推奨ページURL

```txt
/
```

## 使用予定画像

| Image | Section | Usage |
|---|---|---|
| `01_HP_TOP_HERO_会社HPトップ.png` | Hero | 右側ビジュアルまたは背景 |
| `02_HP_BUSINESS_DOMAIN.png` | Business Domain | 事業領域セクション画像 |
| `05_HP_PRODUCTS.png` | Products | プロダクト一覧セクション画像 |
| `04_HP_TRUST_GOVERNANCE.png` | Trust | Trust / Governanceセクション画像 |
| `06_HP_CONTACT_CTA.png` | Final CTA | 問い合わせ導線画像 |

---

# 1. Header / Global Navigation

## 目的

法人サイトとしての安心感を出しながら、主要ページへ迷わず移動できる導線を設ける。

## レイアウト

```txt
[Logo: My Agent Works]                       [About] [Business] [Products] [Trust] [Contact]
                                                                               [相談する]
```

## 要素

| Element | 内容 |
|---|---|
| Logo | My Agent Works wordmark / MAW symbol |
| Nav | About / Business / Products / Trust / Contact |
| CTA | 導入について相談する |
| Mobile | Hamburger menu |

## デザイン

- 背景：白または半透明白
- Hero上では軽いglass headerも可
- sticky header推奨
- 高さ：72px前後
- CTAは小さめのprimary button

---

# 2. Hero Section

## 目的

My Agent Worksの存在意義を、最初の3秒で伝える。

## Section ID

```txt
#hero
```

## Layout

Desktop:

```txt
------------------------------------------------------------
| Left Copy Area                         | Right Visual      |
| eyebrow                                | cinematic image   |
| H1                                     | AI / real estate  |
| lead                                   | dashboard / city  |
| CTA buttons                            |                   |
| proof chips                            |                   |
------------------------------------------------------------
```

Mobile:

```txt
Copy
CTA
Visual
Proof chips
```

## Copy

### Eyebrow

```txt
AI WORKFLOW COMPANY FOR REAL ESTATE
```

### H1

```txt
不動産実務を、AIで再設計する。
```

### Lead

```txt
My Agent Worksは、不動産エージェントの検索・分析・資料作成・学習支援を効率化するAI業務支援プロダクトを開発・運用する会社です。
```

### CTA

| Button | Link | Style |
|---|---|---|
| My Agent Seriesを見る | `/series` | primary |
| 宅建BOOSTを見る | `/takken-boost` | secondary |
| 導入について相談する | `/contact` | text or outline |

## Proof Chips

```txt
AI業務支援
不動産DX
教育DX
PWA / SaaS
法人導入相談
```

## Visual

- Image: `01_HP_TOP_HERO_会社HPトップ.png`
- 左側にコピーを載せるため、画像は右寄せまたはbackground-position center right
- overlay gradient: left dark navy -> transparent

## Design Notes

- 背景：Deep Navy / Cinematic PropTech
- 文字：White / Soft White
- Accent：Cyan + restrained Gold
- 過度なネオンは禁止
- Hero下部に薄いgrid line / glowを許可

---

# 3. Business Domain Section

## 目的

会社が扱う事業領域を明確にし、単一ツールではなく事業ポートフォリオを持つ会社として見せる。

## Section ID

```txt
#business-domain
```

## Section Title

```txt
Business Domain
事業領域
```

## Lead

```txt
My Agent Worksは、不動産実務から生まれたAIプロダクトと、資格学習DXを軸に、現場の業務効率化と事業成長を支援します。
```

## Layout

```txt
[Section title]
[Lead]

[4 cards grid]
01 AI Product Development
02 Education DX
03 DX Consulting
04 LP / Content Production

[Right or bottom visual: 02_HP_BUSINESS_DOMAIN.png]
```

## Cards

| No | Title | Body | Link |
|---:|---|---|---|
| 01 | AI Product Development | 不動産業務の検索、分析、資料作成、管理を支援するAIプロダクトを企画・開発します。 | `/products` |
| 02 | Education DX | 宅建BOOSTを中心に、資格学習と試験後導線をつなぐ教育DXを展開します。 | `/takken-boost` |
| 03 | DX Consulting | 不動産会社や個人エージェントの業務フローを整理し、AI導入を支援します。 | `/business` |
| 04 | LP / Content Production | 商品LP、営業資料、FAQ、AI検索対応コンテンツを制作します。 | `/insights` |

## Design Notes

- 背景：White or Soft Gray
- カード：白背景、細いborder、控えめshadow
- アイコン：Common Icon Sheetから切り出し
- 金融機関に見せても違和感のない堅実さを優先

---

# 4. Product Lineup Section

## 目的

My Agent Worksの主力プロダクトを整理して見せ、LPへの導線を作る。

## Section ID

```txt
#products
```

## Section Title

```txt
Products
プロダクト
```

## Lead

```txt
不動産実務の効率化を支援するMy Agent Seriesと、宅建学習を支援する宅建BOOSTを中心に、実務と学習の両面から価値を提供します。
```

## Layout

```txt
[Large product card: My Agent Series]
[Large product card: 宅建BOOST]
[Small product card: DX Consulting]
```

## Main Product 1: My Agent Series

### Title

```txt
My Agent Series
不動産エージェントの業務時間を、AIで再設計するプロダクト群
```

### Body

```txt
検索、分析、判断、シミュレーション、税務サポート、書類管理まで。不動産実務の各工程をAIで支援し、業務時間の削減と提案品質の向上を目指します。
```

### Chips

```txt
MAA / MAL / MAM / MAS / MAT / MAR
```

### CTA

```txt
My Agent Seriesを見る → /series
```

## Main Product 2: 宅建BOOST

### Title

```txt
宅建BOOST
宅建合格まで、何をやるかもう迷わない。
```

### Body

```txt
過去問演習、分野別学習、AI弱点分析、模擬試験、自己採点まで。宅建BOOSTは、合格までの学習行動を見える化する宅建学習アプリです。
```

### Notes

事業計画書では、宅建BOOSTは宅建学習、AI弱点分析、自己採点、登録実務講習案内を一体化するPWA型学習アプリとして整理されている。

### CTA

```txt
宅建BOOSTを見る → /takken-boost
```

## Visual

- `05_HP_PRODUCTS.png`

## Design Notes

- 背景：Deep Navy or Ink Navy block
- Product cards：glassmorphism + readable contrast
- 会社HPのため、派手すぎず上品にする

---

# 5. Why My Agent Works Section

## 目的

なぜこの会社が作るのかを説明し、実務起点・現場理解・運用改善力を訴求する。

## Section ID

```txt
#why
```

## Section Title

```txt
Why My Agent Works
選ばれる理由
```

## Lead

```txt
My Agent Worksのプロダクトは、現場の不動産実務から生まれています。単なるAI導入ではなく、日々の業務フローを見直し、人が判断と信頼構築に集中できる状態を目指します。
```

## 3 Reasons

| No | Title | Body |
|---:|---|---|
| 01 | 実務起点の設計 | 不動産エージェントの検索、分析、資料作成、顧客提案の流れを前提に設計します。 |
| 02 | AIと人の役割を分ける | AIは情報整理と作業支援を担い、人は判断、提案、関係構築に集中します。 |
| 03 | 小さく始めて改善する | β提供、KPI計測、フィードバック改善を通じて、運用に耐える形へ育てます。 |

## Design Notes

- 背景：White
- 構成：3カラムまたは縦timeline
- アイコン：line icon
- 信頼感重視

---

# 6. Trust / Governance Preview

## 目的

AIサービスとしての責任範囲、個人情報、外部AI/API、専門家判断の必要性を明示し、信頼を担保する。

## Section ID

```txt
#trust-preview
```

## Section Title

```txt
Trust / Governance
信頼とガバナンス
```

## Lead

```txt
AIを業務判断の代替ではなく、実務を支援する補助ツールとして設計しています。情報の取り扱い、出力結果の確認、専門家判断が必要な領域を明確にし、安心して相談できる運用体制を整えます。
```

## Cards

| Title | Body |
|---|---|
| AI出力の位置付け | AI出力は検索・整理・分析・資料作成を補助する情報であり、最終判断を代替するものではありません。 |
| 情報管理 | 顧客情報、物件資料、学習履歴などの取り扱い範囲を明確にし、必要最小限の利用を前提に運用します。 |
| 専門家確認 | 税務、法務、投資判断、資格登録要件は、必要に応じて専門家・公的機関の確認を前提とします。 |

## CTA

```txt
Trust / Governanceを見る → /trust
```

## Visual

- `04_HP_TRUST_GOVERNANCE.png`

## Design Notes

- 背景：Soft Gray
- Security visualは控えめに使用
- 不安を煽らず、安心感として表現する

---

# 7. CTA Section

## 目的

閲覧者を問い合わせへ誘導する。

## Section ID

```txt
#final-cta
```

## Layout

```txt
[Left]
Title
Lead
CTA buttons

[Right]
Contact visual
```

## Title

```txt
まずは、現在の業務課題をお聞かせください。
```

## Lead

```txt
My Agent Series、宅建BOOST、法人導入、協業相談など、目的に応じて最適な導入・連携方法を整理します。
```

## CTA Buttons

| Button | Link | Style |
|---|---|---|
| 導入について相談する | `/contact` | primary |
| My Agent Seriesのデモを相談する | `/series#contact` | secondary |

## Visual

- `06_HP_CONTACT_CTA.png`

## Design Notes

- 背景：Cinematic Navy
- CTAは明確に
- フォームへ迷わず誘導

---

# 8. Footer

## 目的

会社情報・主要ページ・法務ページへの導線を提供する。

## Layout

```txt
My Agent Works
不動産実務を、AIで再設計する。

Company: About / Mission / Business / Trust / Contact
Products: My Agent Series / 宅建BOOST
Legal: Privacy Policy / Terms / Disclaimer / 特商法表記
Social or Contact: info@my-agent.work
```

## Notes

- 登記前は設立予定表記にする。
- 所在地は公開範囲が確定するまで「東京都小平市」程度でも可。
- 電話番号は初期非掲載推奨。

---

# 9. SEO Metadata

## title

```txt
My Agent Works｜不動産実務をAIで再設計する
```

## description

```txt
My Agent Worksは、不動産エージェントの検索・分析・資料作成・学習支援を効率化するAI業務支援プロダクトを開発・運用する会社です。My Agent Series、宅建BOOST、DX Consultingを通じて、不動産実務と教育DXを支援します。
```

## og:title

```txt
My Agent Works｜不動産実務をAIで再設計する
```

## og:description

```txt
不動産業界向けAI業務支援プロダクトと教育DXサービスを開発・運用するMy Agent Worksの公式サイトです。
```

## og:image

```txt
/images/ogp/my-agent-works-ogp.png
```

---

# 10. JSON-LD 初期方針

## Organization

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "My Agent Works",
  "legalName": "合同会社 My Agent Works",
  "url": "https://my-agent.work",
  "description": "不動産業界向けAI業務支援プロダクトと教育DXサービスを開発・運用する会社です。"
}
```

## WebSite

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "My Agent Works",
  "url": "https://my-agent.work"
}
```

---

# 11. Responsive Notes

## Desktop

- max-width: 1120px〜1200px
- Heroは2カラム
- Productは2大カード + 1小カード
- Businessは4カードgrid

## Tablet

- Heroはcopy上、visual下
- Product cardsは1カラムまたは2カラム

## Mobile

- Headerはhamburger
- CTAは縦並び
- Hero画像は下配置
- 1セクション1メッセージを維持
- 画像の文字が小さい場合は背景利用に切り替える

---

# 12. Implementation Notes for Claude Code

## Build order

1. Header
2. Hero
3. Business Domain
4. Products
5. Why
6. Trust Preview
7. Final CTA
8. Footer
9. SEO metadata
10. JSON-LD

## Required components

```txt
Header
SectionTitle
Hero
Button
Card
ProductCard
TrustCard
CTASection
Footer
```

## Required data files

```txt
siteConfig.ts
navigation.ts
products.ts
businessDomains.ts
trustItems.ts
```

## Image handling

- 画像本体はGoogle Driveに保存済み。
- 実装時は `/public/images/` に必要画像のみ配置。
- Hero画像はWebP変換推奨。
- altは `05-image-usage-alt-text.md` を参照する。

---

# 13. Acceptance Criteria

- ファーストビューで「何の会社か」が分かる。
- My Agent Seriesと宅建BOOSTへの導線が明確。
- AIサービスとしての免責・Trust導線がある。
- 問い合わせCTAがHeroとFinal CTAの2か所以上にある。
- モバイルでHeroコピーが読める。
- 画像が重すぎない。
- title / description / OGP / JSON-LDが実装されている。
- 不動産仲介業者と誤認される表現がない。
- 税務・投資・法務・合格保証の断定表現がない。

## Next

次の成果物：

```txt
docs/kickoff/implementation/09-hp-top-copy.md
```

内容：会社HPトップページに実装する実際の見出し、本文、CTA、カード文言を確定する。
