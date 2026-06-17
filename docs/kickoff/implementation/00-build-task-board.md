# My Agent Works HP / LP Build Task Board

## 目的

本タスクボードは、合同会社 My Agent Works の会社HP、My Agent Series LP、宅建BOOST LPを実装するための作業順序と成果物を管理する。

## 実装前提

- 会社HPは信頼獲得を目的とする。
- My Agent Series LPは商品訴求・デモ相談獲得を目的とする。
- 宅建BOOST LPは学習アプリ訴求・申込・法人/団体導入相談を目的とする。
- 画像本体はGoogle Driveで管理し、GitHubでは仕様書・プロンプト・利用表を管理する。
- 既存コードを壊さないため、実装は新規ブランチで行う。

## 推奨実装ブランチ

```bash
git checkout -b feature/my-agent-works-hp-lp
```

---

# Phase 0：実装前確定

| No | タスク | 成果物 | 優先度 | 状態 |
|---:|---|---|---|---|
| 0-1 | 掲載情報の公開範囲を整理 | `01-publication-info-checklist.md` | High | Started |
| 0-2 | プロダクト販売ステータスを整理 | `02-product-sales-status.md` | High | Started |
| 0-3 | 価格表・導入プランを整理 | `03-pricing-and-plan.md` | High | Started |
| 0-4 | Trust / Governance本文を作成 | `04-trust-governance-copy.md` | High | Started |
| 0-5 | 画像利用一覧・alt文を作成 | `05-image-usage-alt-text.md` | High | Started |
| 0-6 | 法務系ページの初稿を整理 | `06-legal-pages-checklist.md` | High | ToDo |
| 0-7 | 問い合わせフォーム仕様を確定 | `07-contact-form-spec.md` | High | ToDo |

# Phase 1：会社HP構築

| No | タスク | 内容 | 優先度 | 状態 |
|---:|---|---|---|---|
| 1-1 | トップページ作成 | Hero / Business / Products / Trust / CTA | High | ToDo |
| 1-2 | Aboutページ作成 | 会社概要・設立背景 | High | ToDo |
| 1-3 | Missionページ作成 | Mission / Vision / Value | Medium | ToDo |
| 1-4 | Businessページ作成 | 事業領域 | High | ToDo |
| 1-5 | Productsページ作成 | Series / 宅建BOOST / Consulting | High | ToDo |
| 1-6 | Trustページ作成 | AI・情報管理・責任範囲 | High | ToDo |
| 1-7 | Contactページ作成 | 問い合わせ導線 | High | ToDo |

# Phase 2：My Agent Series LP構築

| No | タスク | 内容 | 優先度 | 状態 |
|---:|---|---|---|---|
| 2-1 | Series LP Hero | 価値訴求・CTA | High | ToDo |
| 2-2 | Problem section | 不動産実務の課題整理 | High | ToDo |
| 2-3 | AI Workflow Map | 業務フローとプロダクト接続 | High | ToDo |
| 2-4 | Product Units | MAA/MAL/MAM/MAS/MAT/MAR | High | ToDo |
| 2-5 | Before/After | 業務削減イメージ | Medium | ToDo |
| 2-6 | Pricing | 導入プラン | High | ToDo |
| 2-7 | FAQ | 反論処理・不安解消 | High | ToDo |
| 2-8 | Final CTA | デモ相談 | High | ToDo |

# Phase 3：宅建BOOST LP構築

| No | タスク | 内容 | 優先度 | 状態 |
|---:|---|---|---|---|
| 3-1 | TakkenBOOST Hero | 学習アプリ訴求 | High | ToDo |
| 3-2 | Feature section | 分野別学習/AI弱点分析等 | High | ToDo |
| 3-3 | Corporate section | 法人・団体導入 | Medium | ToDo |
| 3-4 | Pricing / code flow | 通常価格・コード導線 | High | ToDo |
| 3-5 | FAQ | 申込・ログイン・利用期間 | High | ToDo |

# Phase 4：SEO/GEO/LLMO/AIO

| No | タスク | 内容 | 優先度 | 状態 |
|---:|---|---|---|---|
| 4-1 | FAQページ | 検索・AI回答対策 | High | ToDo |
| 4-2 | Glossaryページ | 用語集 | Medium | ToDo |
| 4-3 | Insights記事初稿 | 不動産AI/DX/宅建学習 | Medium | ToDo |
| 4-4 | JSON-LD実装 | Organization/Product/FAQ等 | High | ToDo |
| 4-5 | llms.txt作成 | AIクローラー向け | Medium | ToDo |

# Phase 5：公開前チェック

| No | タスク | 内容 | 優先度 | 状態 |
|---:|---|---|---|---|
| 5-1 | 表示チェック | PC/SP/タブレット | High | ToDo |
| 5-2 | SEOチェック | title/description/canonical | High | ToDo |
| 5-3 | 法務表現チェック | 断定・誇張表現の除去 | High | ToDo |
| 5-4 | CTAチェック | 問い合わせ導線 | High | ToDo |
| 5-5 | 画像最適化 | WebP/alt/サイズ | Medium | ToDo |

## 次に実行すること

1. Phase 0の5資料を確定する。
2. 問い合わせフォーム仕様を決める。
3. 実装ブランチを作成する。
4. 会社HPトップから構築開始する。
