# 10a HP Top Prebuild Gap Check

## 目的

Codexで会社HPトップページを実装する前に、不足している素材・実装条件・構築内容を確認し、実装時の抜け漏れを防ぐ。

## 判定

会社HPトップページの実装は開始可能。  
ただし、Codexに貼り付ける前に、以下の補足を必ず指示すること。

---

# 1. 現在の準備状況

## 完了済み

| 項目 | 状態 |
|---|---|
| トップページワイヤーフレーム | 完了 |
| デザイン継承ルール | 完了 |
| トップページ掲載コピー | 完了 |
| Codex実装プロンプト | 作成済み |
| 画像利用一覧・alt文 | 完了 |
| Trust / Governance文 | 完了 |
| 法務系ページチェック | 初稿完了 |
| 問い合わせフォーム仕様 | 初稿完了 |
| HP用画像素材 | Drive保存済み |
| 共通アイコン・UIパーツ | Drive保存済み |
| OGP用画像 | 生成済み。Drive保存確認が必要 |

---

# 2. 実装前に補足すべき不足項目

## 2-1. 技術スタック確認

Codexに、既存リポジトリの構成を最初に確認させる必要がある。

```txt
最初に package.json、src/app、pages、public、components、styles、tailwind.config.* の有無を確認し、既存技術スタックに合わせて実装してください。Next.js App Router / Pages Router / 静的HTMLのいずれかを勝手に決めず、既存構成を優先してください。
```

## 2-2. 画像配置ルール

Driveに画像は保存済みだが、CodexがDriveから自動取得できない場合がある。実装時の配置先を明確にする。

```txt
Google Driveの画像を直接取得できない場合は、画像配置用ディレクトリを作成し、仮ファイル名と参照パスだけ先に実装してください。実画像は後で /public/images/ に配置する前提にしてください。
```

推奨配置：

```txt
/public/images/home/
/public/images/common/
/public/images/ogp/
```

## 2-3. OGP画像の配置

OGP画像は必要。生成済み素材を使用する。

```txt
/images/ogp/my-agent-works-ogp.png
```

Drive未保存の場合は、後で保存・配置する。

## 2-4. ロゴ・favicon

ロゴガイドシートは生成済みだが、個別SVG/PNGとして切り出す必要がある。

実装時は以下を仮配置でよい。

```txt
/public/images/logo/maw-logo.svg
/public/images/logo/maw-symbol.svg
/public/favicon.ico
```

ただし、未作成の場合はテキストロゴ `My Agent Works` で代替し、後で差し替える。

## 2-5. 問い合わせフォームの実送信

今回のトップページでは `/contact` への導線のみでよい。  
フォーム本体・送信API・自動返信はPhase 1後続で実装する。

```txt
トップページではフォーム本体を作らず、/contact へのリンクにしてください。
```

## 2-6. 下層ページリンク

`/about`、`/business`、`/products`、`/trust`、`/contact` は未実装でもリンクとして設置する。  
404を避けたい場合は、暫定プレースホルダまたは disabled にせず、後続Phaseで作成する。

## 2-7. 宅建BOOST LP

宅建BOOST LPは別構築済み。  
今回作成しない。

```txt
/takken-boost への導線のみ。LP本体は作らない。
```

## 2-8. My Agent Series LP

My Agent Series LPは後続構築。  
今回作成しない。

```txt
/series への導線のみ。LP本体は作らない。
```

---

# 3. 追加で必要な素材

## 優先度 High

| 素材 | 用途 | 状態 |
|---|---|---|
| 横型ロゴ | Header / Footer | 生成済みシートから切り出し必要 |
| favicon | Browser icon | 生成済みシートから切り出し必要 |
| OGP画像 | SNS共有 | 生成済み。Drive保存確認が必要 |
| Hero画像WebP | LCP改善 | PNG保存済み。WebP化必要 |
| Footer用小ロゴ | Footer | 生成済みシートから切り出し必要 |

## 優先度 Medium

| 素材 | 用途 | 状態 |
|---|---|---|
| Business icon 4個 | 事業領域カード | 生成済みシートから切り出し可能 |
| Trust icon 3個 | Trustカード | 生成済みシートから切り出し可能 |
| Product chips | Productsセクション | 生成済みシートから切り出し可能 |
| Divider / grid背景 | セクション装飾 | 生成済みシートから切り出し可能 |

---

# 4. Codexプロンプトへ追加すべき補足文

以下を、Codexへ貼り付けるプロンプトの冒頭または末尾に追加する。

```txt
実装前に必ず既存リポジトリ構成を確認してください。package.json、src/app、pages、public、components、styles、tailwind.config.* の有無を確認し、既存技術スタックに合わせて実装してください。

Google Driveに画像素材は保存済みですが、CodexがDriveから直接取得できない場合は、/public/images/home、/public/images/common、/public/images/ogp に配置する想定の参照パスだけ作成してください。画像本体は後で配置します。

今回の作業では、会社HPトップページ `/` のみを構築してください。宅建BOOST LPとMy Agent Series LPは作成せず、それぞれ `/takken-boost` と `/series` への導線だけ設置してください。

/contact のフォーム本体は後続Phaseで作成します。今回のトップページでは `/contact` へのリンクのみ実装してください。

ロゴ、favicon、OGP画像は生成済み素材から後で切り出すため、未配置の場合はテキストロゴと仮パスで実装してください。
```

---

# 5. 実装開始可否

```txt
実装開始：可能
ただし、技術スタック確認、画像仮パス、LP本体を作らない範囲指定をCodexへ明記すること。
```

## 次アクション

1. Codexプロンプトへ本チェック結果の補足文を追加する。
2. Codexで会社HPトップ `/` を実装する。
3. 実装結果をレビューする。
4. 必要素材が追加で不足した場合は都度生成する。
