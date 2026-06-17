# 08a HP / LP Design Inheritance Rules

## 目的

My Agent WorksのHPおよびLP制作において、既存の `My_Agent_Series_Sales.html` および本チャットで検証したデザイン計画を崩さず、Codex / ChatGPTでの実装時に必ず継承すべき設計ルールを固定する。

## 最重要ルール

```txt
HP/LPの実装では、既存の検証計画を崩さない。
会社HPは信頼性を優先し、My Agent Series LPはCinematic PropTechを最大化し、宅建BOOST LPは教育DXとしてCyan中心に調整する。
```

---

# 1. 継承元デザイン

## Source A：My_Agent_Series_Sales.html

既存営業資料HTMLの設計を最優先の継承元とする。

### 継承する要素

- Cinematic dark navy
- Spotlight
- City skyline
- Navy + Gold
- Cyan accent
- Film grain
- Left-side copy / right-side visual
- Product icon grid
- Premium business document mood
- A4資料のような整った余白と情報設計

### 継承するCSS思想

```css
--cin-black: #031122;
--cin-dark: #07192d;
--cin-navy: #15293F;
--cin-mid: #2E445F;
--cin-gray: #4B627E;
--cin-white: #F1F5FA;
--cin-cyan: #7EC7FF;

--navy: #0d1f4d;
--navy-mid: #162d6b;
--gold: #c8982a;
--gold-lt: #deb84a;
--gold-pale: #f5e9c8;
--off-white: #f9f8f5;
--text: #2d2d2d;
--text-mute: #6b6b6b;
--border: #e0d8c8;
```

---

# 2. 絶対に崩してはいけないページ別方針

| Page | Main Role | Design Ratio | Must Keep |
|---|---|---|---|
| 会社HP | 信頼獲得 | Trust 60 / Cinematic 30 / Navy 10 | 堅実性・法人感・金融機関に見せられる品位 |
| My Agent Series LP | 商品訴求 | Cinematic 70 / Navy 25 / Trust 5 | 既存Sales HTMLの世界観を最大限継承 |
| 宅建BOOST LP | 教育DX | Navy 60 / Cinematic 25 / Trust 15 | Cyan中心・学習UI・合格までの道筋 |
| 金融機関/税理士資料 | 信用説明 | Trust 90 / Cinematic 10 | 派手さより説明責任 |

---

# 3. 会社HPへの継承ルール

会社HPでは、Sales HTMLの表紙表現をそのまま全面展開しない。HeroとFinal CTAだけにCinematic要素を使い、本文はTrust Monotoneを中心にする。

## Hero

### 継承する表現

- Dark navy gradient
- City skyline
- Subtle spotlight
- Film grain
- Glass / HUD line
- Left-side copy
- Right-side visual

### 変更する点

- 営業資料より文字量を減らす
- 会社説明として信頼感を上げる
- 見出しは `不動産実務を、AIで再設計する。`
- サブコピーは法人HP用にする

## Body Sections

### 背景

- White / Soft Gray中心
- Dark Navyの連続使用は禁止
- 1セクション1メッセージ

### Typography

- Inter / Noto Sans JP
- Serifは原則使わない
- 明朝体・装飾フォントは禁止

---

# 4. My Agent Series LPへの継承ルール

My Agent Series LPは、Sales HTMLの世界観を最も強く継承する。

## Must Keep

- Dark navy cinematic background
- Gold accent
- Cyan glow
- Product chips
- 6 product grid
- AI workflow hub
- Before / After
- KPI strip
- Premium SaaS / PropTech impression

## Hero Copy

```txt
不動産エージェントの業務時間を、AIで1/3以上削減する。
```

## Product Modules

```txt
MAA Analytics
MAL Locator
MAM Much
MAS Simulate
MAT Tax AI
MAR Doc. AI
```

## 注意

- すべてを提供中と見せない。
- デモ可能、β提供可能、構想段階を分ける。
- AIが最終判断を代替する表現は禁止。

---

# 5. 宅建BOOST LPへの継承ルール

宅建BOOSTはSales HTMLのCinematic感をそのまま持ち込まず、教育DXに調整する。

## Must Keep

- Dark navy
- Cyan accent
- Learning dashboard
- Smartphone / tablet mock
- AI weak-point analysis
- PWA / multi-OS feeling
- 学習進捗・模試・自己採点の可視化

## Hero Copy

```txt
宅建合格まで、何をやるかもう迷わない。
```

## 注意

- Goldは基本使わない。
- 学習アプリとして安心感を優先する。
- 「確実に合格」などの断定は禁止。
- 登録実務講習案内は参考情報として表現する。

---

# 6. 画像・パーツ生成ルール

ページに差し込む画像やアイコンが不足した場合は、都度生成して補完する。

## 必要になりやすい素材

| Category | Assets |
|---|---|
| Logo | horizontal logo / monogram / favicon / social icon |
| HP Icons | AI Product / Education DX / Consulting / Trust / Contact |
| Series Icons | MAA / MAL / MAM / MAS / MAT / MAR |
| UI Parts | CTA button / KPI card / FAQ row / product chip / breadcrumb |
| Background | skyline / grid / node cluster / divider / glow / blueprint texture |
| OGP | corporate OGP / Series OGP / 宅建BOOST OGP |

## Asset Rule

- 最終実装では、画像内文字に頼りすぎない。
- 日本語テキストはHTML/CSS側で載せる。
- 画像はWebP化する。
- 背景透過PNGは切り出し前提で余白を広く取る。
- 装飾画像には空altを使う。
- 意味のある画像には `05-image-usage-alt-text.md` のaltを使う。

---

# 7. Codex / ChatGPT 実装時の禁止事項

- 既存検証計画を勝手に変更しない。
- 全ページを黒背景にしない。
- Sales HTMLの配色から大きく外れない。
- 紫・ピンク・赤をメインカラーにしない。
- サイバーパンクやゲームUIへ寄せすぎない。
- 情報商材風の強い煽りは禁止。
- 不動産仲介業者と誤認される表現は禁止。
- AIが投資・税務・法務・資格登録判断を代替する表現は禁止。
- 宅建BOOSTで合格保証表現は禁止。

---

# 8. Codexへの実装指示要約

```txt
既存の My_Agent_Series_Sales.html のCinematic dark navy / city skyline / cyan glow / navy + gold設計を継承すること。
ただし、会社HPでは信頼性を優先し、HeroとCTAに限定してCinematic表現を使うこと。
My Agent Series LPではこの世界観を最大化すること。
宅建BOOST LPではCyan中心の教育DX表現へ調整すること。
既に作成したタスクボード・ワイヤーフレーム・画像利用表・Trust文・法務チェックリストを崩さないこと。
```

---

# 9. 次の実装ステップ

次は、`08-hp-top-wireframe.md` を前提に、会社HPトップページの実装用コピーを確定する。

```txt
docs/kickoff/implementation/09-hp-top-copy.md
```
