# 05 Image Usage and Alt Text

## 目的

Google Driveに保存済みのHP/LP用画像を、どのページ・どのセクションで使うかを明確化し、実装時のalt属性を準備する。

## Drive保存先

```txt
08_HP_LP_デザイン_構築準備/
└─ 02_サンプル画像/
   └─ HP_LP_生成画像_2026-06-17/
```

---

# 1. 会社HP用画像

| File | Page / Section | Purpose | Alt Text |
|---|---|---|---|
| `01_HP_TOP_HERO_会社HPトップ.png` | `/` Hero | 会社HPの第一印象 | 不動産実務をAIで再設計するMy Agent Worksのメインビジュアル |
| `02_HP_BUSINESS_DOMAIN.png` | `/` Business Domain | 事業領域 | My Agent Worksの事業領域を示すAI業務支援ネットワーク |
| `03_HP_ABOUT_MISSION.png` | `/mission` or About | MVV・企業理念 | 未来の不動産実務を見据えるMy Agent Worksのビジョンイメージ |
| `04_HP_TRUST_GOVERNANCE.png` | `/trust` | 信頼・ガバナンス | AIサービスの信頼性とデータ管理を表すセキュリティビジュアル |
| `05_HP_PRODUCTS.png` | `/products` | プロダクト一覧 | My Agent Seriesの各プロダクトをつなぐAIネットワークビジュアル |
| `06_HP_CONTACT_CTA.png` | `/contact` CTA | 問い合わせ導線 | My Agent Worksへの相談や問い合わせを表すコミュニケーションビジュアル |
| `07_HP_SAMPLE_FULLPAGE.png` | Design reference only | 実装参照 | My Agent Works会社HPのサンプルデザイン |

---

# 2. My Agent Series LP用画像

| File | Page / Section | Purpose | Alt Text |
|---|---|---|---|
| `01_LP_SERIES_HERO.png` | `/series` Hero | LPトップ | My Agent Seriesの6プロダクトを統合するAI業務OSビジュアル |
| `02_LP_WORKFLOW_MAP.png` | `/series` Workflow | 業務フロー | 不動産業務の検索分析資料作成をつなぐAIワークフロー図 |
| `03_LP_BEFORE_AFTER_alt.png` | `/series` Before/After | 導入前後比較 | 手作業中心の業務からAI活用業務へ変化する比較イメージ |
| `04_LP_COMMAND_CENTER.png` | `/series` Command Center | 統合管理画面 | 不動産エージェント向けAI統合管理画面のイメージ |
| `05_LP_PRICING.png` | `/series` Pricing | 料金プラン | My Agent Seriesの料金プランを示す未来的なUIビジュアル |
| `07_LP_FINAL_CTA.png` | `/series` Final CTA | デモ相談 | My Agent Seriesのデモ相談へ誘導する未来的なCTAビジュアル |
| `08_LP_SERIES_SAMPLE_FULLPAGE.png` | Design reference only | 実装参照 | My Agent Series LPのサンプルデザイン |

---

# 3. 宅建BOOST LP用画像

| File | Page / Section | Purpose | Alt Text |
|---|---|---|---|
| `01_LP_TAKKEN_HERO.png` | `/takken-boost` Hero | LPトップ | 宅建BOOSTの学習アプリとAI学習支援を表すメインビジュアル |
| `02_LP_TAKKEN_FEATURES.png` | `/takken-boost` Feature | 主要機能 | 宅建BOOSTの学習ダッシュボードと主要機能のビジュアル |
| `03_LP_TAKKEN_CORPORATE.png` | `/takken-boost/business` | 法人・団体導入 | 宅建BOOSTの法人IDと学習進捗管理を表す管理画面ビジュアル |

---

# 4. 共通パーツ

| File | Usage | Alt Text |
|---|---|---|
| `01_COMMON_ICON_SHEET.png` | アイコン切り出し | My Agent Worksの共通機能アイコンセット |
| `02_COMMON_PRODUCT_CHIP_SHEET.png` | プロダクトチップ切り出し | My Agent Seriesのプロダクトチップ素材 |
| `03_COMMON_UI_PARTS_SHEET.png` | UIパーツ切り出し | HPとLPで使用する共通UIパーツ素材 |
| `04_COMMON_BACKGROUND_PARTS_SHEET.png` | 背景・装飾素材 | HPとLPで使用する背景パーツ素材 |

## 実装ルール

- 文字が入っている画像は、実装時にHTMLテキストへ置き換えることを検討する。
- 背景画像はWebP化し、`srcset` を用意する。
- Hero画像はLCPに影響するため、圧縮・遅延読み込み・優先読み込みを適切に制御する。
- 装飾画像には空altを使い、意味のある画像には上記altを設定する。
