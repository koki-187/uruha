# 11 HP Top Review Checklist

## 目的

Codexで実装された合同会社 My Agent Works 公式HPトップページをレビューし、デザイン・構成・導線・SEO・法務表現・レスポンシブの観点から修正指示を作成するためのチェックリスト。

## レビュー対象

```txt
Page: /
Scope: 会社HPトップページのみ
```

## 重要前提

- 宅建BOOST LPは別構築済み。トップページでは `/takken-boost` への導線のみでよい。
- My Agent Series LPは後続構築。トップページでは `/series` への導線のみでよい。
- `/contact` フォーム本体は後続構築。トップページではリンクのみでよい。
- 会社HPトップは信頼獲得が目的。
- 既存のCinematic PropTech計画を崩さない。

---

# 1. 実装範囲チェック

| Check | Criteria | Result |
|---|---|---|
| トップページのみ実装されている | `/` のみが実装対象 | 未確認 |
| 宅建BOOST LP本体を作っていない | `/takken-boost` はリンクのみ | 未確認 |
| My Agent Series LP本体を作っていない | `/series` はリンクのみ | 未確認 |
| `/contact` フォーム本体を作っていない | リンクのみ | 未確認 |
| 既存READMEや既存コードを破壊していない | 不要な上書きがない | 未確認 |

---

# 2. デザイン継承チェック

| Check | Criteria | Result |
|---|---|---|
| Cinematic dark navyを継承 | Hero / CTAで適切に使用 | 未確認 |
| city skyline / glow / grid感がある | 過度ではなく上品 | 未確認 |
| Navy + Gold + Cyanの設計を継承 | 色が大きく外れていない | 未確認 |
| Trust Monotoneが中心 | Business / Why / Trustが白・余白・カード中心 | 未確認 |
| 全ページ黒背景になっていない | 暗色はHero/CTA中心 | 未確認 |
| サイバーパンク化していない | ゲームUI・過剰ネオンがない | 未確認 |
| 文字可読性が高い | 背景と文字が競合しない | 未確認 |

---

# 3. Heroチェック

| Check | Criteria | Result |
|---|---|---|
| H1が正しい | `不動産実務を、AIで再設計する。` | 未確認 |
| Leadが正しい | 指定コピーが入っている | 未確認 |
| CTAが3つある | `/series`, `/takken-boost`, `/contact` | 未確認 |
| Proof chipsがある | AI業務支援等 | 未確認 |
| Hero画像が適切 | 右側または背景で使用 | 未確認 |
| Heroが3秒で伝わる | 何の会社か分かる | 未確認 |
| SPで読める | モバイルでH1が崩れない | 未確認 |

---

# 4. Section構成チェック

| Section | Required | Result |
|---|---|---|
| Header | 必須 | 未確認 |
| Hero | 必須 | 未確認 |
| Business Domain | 必須 | 未確認 |
| Products | 必須 | 未確認 |
| Why My Agent Works | 必須 | 未確認 |
| Trust / Governance Preview | 必須 | 未確認 |
| Final CTA | 必須 | 未確認 |
| Footer | 必須 | 未確認 |

---

# 5. Products導線チェック

| Product | Criteria | Result |
|---|---|---|
| My Agent Series | `/series` への導線のみ | 未確認 |
| 宅建BOOST | `/takken-boost` への導線のみ | 未確認 |
| DX Consulting | `/contact` への導線 | 未確認 |
| Product説明 | 売り込み過多でない | 未確認 |
| 構想段階機能の断定なし | 全機能提供中に見せていない | 未確認 |

---

# 6. Trust / Governanceチェック

| Check | Criteria | Result |
|---|---|---|
| AI出力の補助性を明記 | 最終判断を代替しない | 未確認 |
| 情報管理の説明がある | 必要最小限の利用 | 未確認 |
| 専門家確認の説明がある | 税務・法務・投資判断 | 未確認 |
| Trustページ導線がある | `/trust` へのリンク | 未確認 |
| 不安を煽っていない | 安心材料として表現 | 未確認 |

---

# 7. 禁止表現チェック

以下が入っていたら修正。

```txt
必ず売上が上がる
完全自動で判断する
AIが投資判断を行う
AIが税務判断を行う
AIが法律判断を行う
確実に合格できる
不動産仲介を行う会社
```

| Check | Result |
|---|---|
| 投資判断の断定なし | 未確認 |
| 税務判断の断定なし | 未確認 |
| 法務判断の断定なし | 未確認 |
| 合格保証なし | 未確認 |
| 不動産仲介業者と誤認されない | 未確認 |

---

# 8. SEO / Metadataチェック

| Check | Criteria | Result |
|---|---|---|
| title | `My Agent Works｜不動産実務をAIで再設計する` | 未確認 |
| description | 指定文言が入っている | 未確認 |
| OGP title | 指定文言 | 未確認 |
| OGP image | `/images/ogp/my-agent-works-ogp.png` | 未確認 |
| canonical | 必要に応じて設定 | 未確認 |
| JSON-LD Organization | 追加済み | 未確認 |
| JSON-LD WebSite | 追加済み | 未確認 |

---

# 9. アクセシビリティチェック

| Check | Criteria | Result |
|---|---|---|
| H1は1つ | 1ページ1H1 | 未確認 |
| nav操作可能 | keyboard対応 | 未確認 |
| CTA label明確 | 何をするボタンか分かる | 未確認 |
| alt設定 | 意味ある画像にalt | 未確認 |
| 装飾画像 | empty alt | 未確認 |
| コントラスト | 読める明度差 | 未確認 |
| mobile menu | 操作可能 | 未確認 |

---

# 10. レスポンシブチェック

| View | Criteria | Result |
|---|---|---|
| Desktop | max-width 1120〜1200px程度 | 未確認 |
| Tablet | Heroがstackedでも崩れない | 未確認 |
| Mobile | copy first / visual second | 未確認 |
| CTA | mobileで縦並び | 未確認 |
| Cards | 1カラム化 | 未確認 |
| Header | hamburgerまたは適切な表示 | 未確認 |
| 画像 | はみ出しなし | 未確認 |

---

# 11. Performance / Imageチェック

| Check | Criteria | Result |
|---|---|---|
| Hero画像 | 重すぎない | 未確認 |
| WebP化 | 可能なら実施 | 未確認 |
| LCP | Hero画像の読み込み制御 | 未確認 |
| Lazy load | 下部画像に適用 | 未確認 |
| 不要画像 | 置いていない | 未確認 |

---

# 12. 修正指示テンプレート

Codexへの修正指示は以下形式で出す。

```txt
# Codex修正指示｜My Agent Works HP Top

## 修正対象
- Page: /
- Branch:
- Commit:

## 修正内容
1. 
2. 
3. 

## 優先度 High
- 

## 優先度 Medium
- 

## 優先度 Low
- 

## 禁止事項
- 宅建BOOST LP本体は作らない
- My Agent Series LP本体は作らない
- 既存計画を変更しない

## 完了後に報告すること
1. 変更ファイル
2. 修正内容
3. 表示確認方法
4. 残課題
```

---

# 13. レビュー時にユーザーから受け取るもの

Codex実装後、以下を受け取る。

```txt
1. GitHub branch名
2. commit SHA
3. 変更ファイル一覧
4. ローカルまたはプレビューURL
5. スクリーンショット PC / SP
6. Codexの完了レポート
```

## Next

Codex実装結果を確認後、必要に応じて以下を作成する。

```txt
docs/kickoff/implementation/12-hp-top-fix-prompt.md
```
