# My Agent Works KICKOFF

このディレクトリは、合同会社 My Agent Works のHP・LP・営業資料・プロダクト展開に関する構築準備資料を管理するためのKICKOFFドキュメントです。

## 目的

- 法人HPの信頼設計
- My Agent Series LPの販売導線設計
- 宅建BOOST LP・共同事業導線の整理
- デザインシステムの統一
- SEO / GEO / LLMO / AIO 対応方針の整理
- Claude Codeへ渡す実装指示の管理

## 基本方針

My Agent WorksのWeb構築は、会社HPと商品LPを明確に分離します。

| 種別 | 目的 | 主な読者 | デザイン方針 |
|---|---|---|---|
| 会社HP | 信頼獲得 | 金融機関・税理士・司法書士・協業先・法人顧客 | Trust Monotone中心 + Cinematic Hero |
| My Agent Series LP | 商品訴求・デモ相談 | 不動産会社・個人エージェント・DX担当者 | Cinematic PropTech中心 |
| 宅建BOOST LP | 申込・法人/団体提携 | 宅建受験生・職能研・法人/学校 | Intelligent Navy + Cyan |
| FAQ / Glossary / Insights | SEO/GEO/LLMO/AIO | 検索ユーザー・AI検索・比較検討層 | 人間にもAIにも読みやすい構造 |

## 主要コピー

```txt
不動産実務を、AIで再設計する。
```

```txt
AIが作業を担い、人は判断と信頼構築に集中する。
```

```txt
あなたの毎日に、戦略的な余白を。
```

## 関連ドキュメント

- `docs/kickoff/hp-lp-spec.md`
- `docs/kickoff/cinematic-proptech-design-system.md`
- `docs/kickoff/image-save-manifest.md`
- `prompts/image-generation-prompts.md`
- `prompts/claude-code-hp-lp-build.md`

## 注意

- 既存コードを壊さないため、本KICKOFF資料は `docs/` と `prompts/` に分離して管理します。
- 実装時は必ずバックアップまたはブランチ運用を行います。
- 法務・税務・投資判断の効果を断定する表現は禁止します。
