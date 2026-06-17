# My Agent Works HP / LP 構築仕様書

## 1. 基本方針

My Agent WorksのWeb構築は、会社HPと商品LPを明確に分離する。

- 会社HP：信頼獲得、法人情報、事業領域、代表者背景、協業相談
- My Agent Series LP：商品訴求、導入効果、デモ相談、価格、FAQ
- 宅建BOOST LP：学習アプリ訴求、申込、法人・団体提携相談
- SEO/GEO/LLMO/AIOページ：FAQ、用語集、解説記事、導入事例

## 2. 推奨サイト構成

```txt
/
├─ about/
├─ mission/
├─ business/
├─ products/
├─ company/
├─ trust/
├─ contact/
├─ series/
│  ├─ analytics/
│  ├─ locator/
│  ├─ much/
│  ├─ simulate/
│  ├─ tax-ai/
│  └─ record/
├─ takken-boost/
├─ pricing/
├─ faq/
├─ glossary/
└─ insights/
```

## 3. デザイン配分

| ページ | Trust Monotone | Intelligent Navy | Cinematic PropTech |
|---|---:|---:|---:|
| 会社HP | 60% | 10% | 30% |
| My Agent Series LP | 5% | 25% | 70% |
| 宅建BOOST LP | 15% | 60% | 25% |
| 金融機関向け資料 | 90% | 0% | 10% |

## 4. 会社HP構成

1. Hero：Cinematic PropTech
2. Business Domain：Trust Monotone
3. Product Lineup：Trust + Navy
4. Why My Agent Works：Trust Monotone
5. Trust / Governance：Trust Monotone
6. Contact：Trust + CTA

## 5. My Agent Series LP構成

1. Cinematic Hero
2. 現場課題
3. AI Workflow Map
4. Product Units
5. Before / After
6. KPI Strip
7. Agent Command Center構想
8. Pricing
9. FAQ
10. Final CTA

## 6. 宅建BOOST LP構成

1. Hero
2. 宅建学習の課題
3. 主要機能
4. AI弱点分析
5. 模擬試験・自己採点
6. 法人・団体導入
7. 料金
8. FAQ
9. CTA

## 7. SEO / GEO / LLMO / AIO必須実装

- title / description / canonical
- sitemap.xml
- robots.txt
- OAI-SearchBotを不必要にブロックしない
- JSON-LD：Organization / WebSite / Product / SoftwareApplication / FAQPage / Article / BreadcrumbList
- llms.txt
- FAQページ
- Glossaryページ
- Product Definitionページ
- 導入事例ページ
- 比較ページ

## 8. AI検索向け定義文

```txt
My Agent Worksとは、不動産エージェントの検索・分析・資料作成・学習支援を効率化するAI業務支援プロダクトを開発・運用する会社です。
```

```txt
My Agent Seriesとは、不動産実務の検索、分析、判断、資料作成、税務補助、書類管理を支援するAI業務支援プロダクト群です。
```

```txt
宅建BOOSTとは、宅建試験の過去問演習、分野別学習、AI弱点分析、模擬試験、自己採点を支援する学習アプリです。
```

## 9. 注意事項

- 不動産仲介業者と誤認される表現を避ける
- 税務・投資・法律上の効果を断定しない
- 「完全自動」「必ず儲かる」「確実に合格」などの誇張表現は禁止
- AIは判断を補助する存在として表現する
