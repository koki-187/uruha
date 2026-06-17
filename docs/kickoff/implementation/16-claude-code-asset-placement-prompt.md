# Claude Code 指示｜生成画像・追加UI素材の配置反映

## 目的
ここまで生成した画像素材を、会社HP、My Agent Series LP、宅建BOOST LP/法人導入ページへ正しい用途で配置する。

## 1. 宅建BOOST LP 画像配置

### app-features-src.png
ユーザー指定の保存先:
`H:\マイドライブ\♦♦♦オリジナル プロダクト♦♦♦\◇宅建BOOST◇\takken-boost-lp\assets\biz\app-features-src.png`

実装先:
`takken-boost-lp/assets/biz/app-features-src.png`

使用箇所:
- 宅建BOOST LP「主要機能 / FEATURES」
- 分野別学習、AI弱点分析、弱点復習、模擬試験、学習履歴、PWAの6機能を訴求する画像として配置

Alt:
`宅建BOOSTの主要機能を示す学習ダッシュボードと分野別学習、AI弱点分析、模擬試験、学習履歴、PWA対応のUI`

### corporate-overview-src.png
ユーザー指定の保存先:
`H:\マイドライブ\♦♦♦オリジナル プロダクト♦♦♦\◇宅建BOOST◇\takken-boost-lp\assets\biz\corporate-overview-src.png`

実装先:
`takken-boost-lp/assets/biz/corporate-overview-src.png`

使用箇所:
- 宅建BOOST 法人・団体導入ページ
- 法人ID、組織・グループ管理、学習進捗可視化、KPIレポートの説明画像として配置

Alt:
`宅建BOOST法人IDの管理画面、組織グループ管理、学習進捗可視化、KPIレポートを示す法人導入向けビジュアル`

## 2. /series LP UI素材

以下の素材を `/public/images/series/` に配置する。

- `before-after-ui.png`
- `price-ui.png`
- `faq-ui.png`
- `series-hero-bg.png`

使用箇所:
- Before / After
- Price
- FAQ
- Final CTA背景

## 3. Product icon

`MAT Tax AI` の正式透明アイコンを以下へ配置する。

`/public/images/products/mat-tax-ai.png`

使用箇所:
- `/series` Hero下アイコン列
- AI Workflow Map
- Product Lineup
- Price/Plan内の機能チップ

## 4. 実装チェック

- PC/SPで画像のはみ出しなし
- broken imageなし
- 画像はWebP化できるものはWebP化
- 画像内テキストに依存しすぎず、HTML本文にも説明を記載
- altを必ず設定
- LCPに影響するHero画像は圧縮・preload検討
- `prefers-reduced-motion` 対応

## 5. 完了後レポート

1. 配置した画像一覧
2. 変更ファイル一覧
3. 使用ページ・使用セクション
4. WebP変換有無
5. broken image確認結果
6. PC/SP確認結果
7. 残課題
