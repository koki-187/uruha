# My Agent Works / My Agent Series / 宅建BOOST 追加生成素材・使用箇所マップ

作成日: 2026-06-18  
対象: 会社HP `/`、My Agent Series LP `/series`、宅建BOOST LP/法人導入ページ

## 1. 基本方針

- 会社HP `/` は「白基調プレミアム企業HP + ダークシネマティックHero」。
- My Agent Series LP `/series` は「ダークネイビー × ゴールド × シアン」の販売LP。
- 宅建BOOST LPは、既存LPとは別に「主要機能」「法人・団体導入」用ビジュアルを追加。
- 画像は無作為に配置せず、Hero / Feature / Corporate / UI parts / Icons / OGP に分類して使用する。

## 2. 宅建BOOST 追加画像の確定使用箇所

| 画像 | 保存先 | 使用ページ | セクション | 目的 |
|---|---|---|---|---|
| `app-features-src.png` | `takken-boost-lp/assets/biz/app-features-src.png` | 宅建BOOST LP | 主要機能 / FEATURES | 分野別学習、AI弱点分析、弱点復習、模擬試験、学習履歴、PWAを1枚で訴求 |
| `corporate-overview-src.png` | `takken-boost-lp/assets/biz/corporate-overview-src.png` | 宅建BOOST法人・団体導入LP | 法人ID / CORPORATE | 法人ID、組織・グループ管理、学習進捗可視化、KPIレポートを訴求 |

## 3. My Agent Series LP `/series` 追加UI素材

| 素材タイプ | 推奨保存先 | 使用箇所 |
|---|---|---|
| Before / After UI | `/public/images/series/before-after-ui.png` | Before / After セクション |
| Price UI | `/public/images/series/price-ui.png` | Price セクション |
| FAQ UI | `/public/images/series/faq-ui.png` | FAQ セクション |
| MAT Tax AI icon | `/public/images/products/mat-tax-ai.png` | Product Card / Workflow Step |
| Series hero bg | `/public/images/series/series-hero-bg.png` | `/series` Hero |

## 4. 会社HP `/` 使用素材

| 素材 | 推奨保存先 | 使用箇所 |
|---|---|---|
| My Agent Works logo | `/public/images/logo/maw-logo.png` | Header / Footer |
| MAW symbol | `/public/images/logo/maw-symbol.png` | favicon / Hero accent |
| HP hero city | `/public/images/home/hp-top-hero.png` | Hero |
| Product icons | `/public/images/products/*.png` | Product Lineup |

## 5. 実装ルール

- PNG原本は高画質保存用。実装ではWebP版を優先。
- 画像が未配置の場合はbroken imageを出さず、CSS/SVG placeholderで代替。
- 文字が画像内に含まれる場合、本文にも同等情報をHTMLテキストとして記載。
- 3D/アニメーションは軽量実装を優先し、LCPを悪化させない。
- `prefers-reduced-motion` に対応する。

## 6. 法務・表現注意

- AIが投資・税務・法務判断を代替する表現は禁止。
- 宅建BOOSTで合格保証表現は禁止。
- 法人ID・管理画面は提供状況に応じて「提供準備中」「順次展開」等を使用。
